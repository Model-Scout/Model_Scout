"""Public API for the frontend. Keeps sessions, conversation groups and history; the AI service does the rest.

    POST /api/chat                 question -> SSE: status, token, then done or error
    GET  /api/groups               conversations of this session
    GET  /api/groups/{group_id}    a stored conversation, read-only for anyone holding the link
    GET  /api/files/{source_id}    README of a model or dataset
    GET  /api/health

The session id is the only credential (no login), so it travels in the X-Session-Id header, never in a URL.

    python backend/app/main.py     # HOST / PORT / AI_URL env, default 127.0.0.1:8000, docs at /docs
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
import threading
from collections.abc import Iterable, Iterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated, Any, Literal
from uuid import UUID, uuid4

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi import Path as PathParam
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from psycopg.conninfo import make_conninfo
try:
    from .rate_limit import RateLimiter
    from .result import ChatDone, ChatResult, GroupDetail, GroupSummary, SourceFile, Source, build_done, stored_text
except ImportError:
    from rate_limit import RateLimiter
    from result import ChatDone, ChatResult, GroupDetail, GroupSummary, SourceFile, Source, build_done, stored_text

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

AI_URL = os.getenv("AI_URL", "http://127.0.0.1:8001")
READMES_DIR = Path(os.getenv("READMES_DIR", Path(__file__).resolve().parents[2] / "ai" / "data" / "readmes")).resolve()
# A source id maps to a file by its prefix; other ids are Hugging Face datasets or models.
README_DIRS = {"kaggle/": "kaggle", "seoul_open_data/": "public", "data_go_kr/": "public"}
HF_README_DIRS = ("datasets", "core", "low_popularity")
SOURCE_ID_RE = re.compile(r"^[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*$")
MAX_README_BYTES = 2_000_000
DB_ENV = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")
AI_TIMEOUT = httpx.Timeout(10.0, read=180.0)
AI_ERROR = "추천을 만드는 중 오류가 났습니다. 잠시 후 다시 시도해 주세요."
QUESTION_HISTORY = 6  # latest messages sent with a question, enough to resolve "그럼 두 번째는?"
# The AI reports a node when it finishes, so each entry names the step that starts next.
NEXT_STEP = {"decompose": (1, "요구사항 확인"), "clarify": (2, "모델 검색"), "search_models": (3, "데이터셋 검색"),
             "search_datasets": (3, "조건 확인"), "assess": (4, "답변 생성")}

limiter = RateLimiter(int(os.getenv("RATE_LIMIT_PER_MINUTE", "10")), int(os.getenv("DAILY_REQUEST_LIMIT", "300")))

SessionId = Annotated[UUID, Header(alias="X-Session-Id", description="crypto.randomUUID() kept in localStorage")]
active_groups: dict[UUID, object] = {}
active_lock = threading.Lock()


def release_group(group_id: UUID, lease: object) -> None:
    with active_lock:
        if active_groups.get(group_id) is lease:
            active_groups.pop(group_id, None)


def claim_group(group_id: UUID) -> object:
    with active_lock:
        if group_id in active_groups:
            raise HTTPException(409, "이 대화의 이전 요청이 처리 중입니다.")
        lease = object()
        active_groups[group_id] = lease
        return lease


class ChatRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    group_id: UUID | None = Field(default=None, description="null starts a new conversation")
    query: str = Field(min_length=1, max_length=2000, examples=["따릉이 경로 추천 서비스를 만들고 싶어"])
    mode: Literal["recommend", "question"] = "recommend"
    target_id: str | None = Field(default=None, max_length=300)

    @field_validator("query")
    @classmethod
    def nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("질문을 입력해 주세요.")
        return value.strip()

    @model_validator(mode="after")
    def valid_mode(self):
        if self.mode == "question" and self.group_id is None:
            raise ValueError("question에는 group_id가 필요합니다.")
        if self.target_id and self.mode != "question":
            raise ValueError("target_id는 question에서만 사용합니다.")
        return self


def _conninfo() -> str | None:
    if not all(os.getenv(name) for name in DB_ENV):
        return None
    env = os.environ
    return make_conninfo(host=env['SUPABASE_DB_HOST'], port=env['SUPABASE_DB_PORT'],
        dbname=env['SUPABASE_DB_NAME'], user=env['SUPABASE_DB_USER'], password=env['SUPABASE_PASSWORD'],
        sslmode=env.get('SUPABASE_DB_SSLMODE', 'require'), connect_timeout=10)


@asynccontextmanager
async def lifespan(app: FastAPI):
    conninfo = _conninfo()
    app.state.pool = None
    if conninfo:
        app.state.pool = ConnectionPool(
            conninfo,
            min_size=1,
            max_size=int(os.getenv("DB_POOL_SIZE", "4")),
            kwargs={"autocommit": True, "prepare_threshold": 0, "row_factory": dict_row},
            open=True,
        )
    else:
        logging.warning("database settings are missing: conversation routes answer 503")
    yield
    if app.state.pool is not None:
        app.state.pool.close()


app = FastAPI(
    title="Model Scout API",
    lifespan=lifespan,
    openapi_url="/openapi.json" if os.getenv("ENABLE_DOCS", "1") == "1" else None,  # None also removes /docs and /redoc
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_origin_regex=os.getenv("CORS_ORIGIN_REGEX") or None,  # Vercel Preview URLs differ per PR
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    expose_headers=["X-Group-Id", "Retry-After"],
)


def _pool() -> Any:
    if app.state.pool is None:
        raise HTTPException(503, "데이터베이스가 설정되지 않았습니다.")
    return app.state.pool


def client_ip(request: Request) -> str:
    # Caddy overwrites X-Forwarded-For and the API port is not published, so this cannot be spoofed in production.
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.client.host if request.client else "unknown"


def sse(event: str, data: Any) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def parse_sse(lines: Iterable[str]) -> Iterator[tuple[str, Any]]:
    event, data = "message", []
    for line in lines:
        if line.startswith("event:"):
            event = line[6:].lstrip(" ")
        elif line.startswith("data:"):
            data.append(line[5:].lstrip(" "))
        elif not line and data:
            yield event, json.loads("\n".join(data))
            event, data = "message", []
    if data:
        yield event, json.loads("\n".join(data))


def _open_group(pool: Any, group_id: UUID | None, session_id: UUID, query: str) -> UUID:
    with pool.connection() as conn, conn.transaction():
        if group_id is None:
            group_id = uuid4()
            conn.execute(
                "insert into app.groups (group_id, session_id, title) values (%s, %s, %s)",
                (group_id, session_id, " ".join(query.split())[:80]),
            )
        else:
            row = conn.execute("select session_id from app.groups where group_id = %s", (group_id,)).fetchone()
            if row is None:
                raise HTTPException(404, "대화를 찾을 수 없습니다.")
            if row["session_id"] != session_id:
                raise HTTPException(403, "이 대화에 이어서 질문할 수 없습니다.")
        conn.execute(
            "insert into app.messages (group_id, role, content) values (%s, 'user', %s)",
            (group_id, query),
        )
    return group_id


def _save_answer(pool: Any, done: ChatDone) -> None:
    result = Jsonb(done.result.model_dump(mode="json")) if done.result else None
    with pool.connection() as conn, conn.transaction():
        conn.execute(
            "insert into app.messages (group_id, role, content, type, result, sources) values (%s, 'assistant', %s, %s, %s, %s)",
            (done.group_id, stored_text(done), done.type, result, Jsonb([s.model_dump() for s in done.sources])),
        )
        conn.execute("update app.groups set updated_at = now() where group_id = %s", (done.group_id,))


class ChatStream(StreamingResponse):
    """Ends the AI call before freeing the group, also on a client disconnect.

    Starlette leaves an abandoned generator to the garbage collector, so the AI call would outlive the lease.
    """

    def __init__(self, chat_stream: Iterator[str], group_id: UUID, lease: object, **kwargs: Any):
        super().__init__(chat_stream, **kwargs)
        self.chat_stream, self.group_id, self.lease = chat_stream, group_id, lease

    async def __call__(self, scope: Any, receive: Any, send: Any) -> None:
        try:
            await super().__call__(scope, receive, send)
        finally:
            try:
                self.chat_stream.close()  # type: ignore[attr-defined]
            finally:
                release_group(self.group_id, self.lease)


def stream_chat(pool: Any, group_id: UUID, query: str, ip: str, context: dict | None = None) -> Iterator[str]:
    started = time.time()
    events: dict[str, Any] = {}
    tokens: list[str] = []
    completed = False
    payload = {"query": query, "thread_id": str(group_id)}
    if context is not None:
        payload.update(mode="question", context=context)
    first_step, first_label = (4, "답변 생성") if context is not None else (1, "요구사항 분석")
    yield sse("status", {"step": first_step, "total": 4, "label": first_label, "elapsed": 0})
    try:
        with httpx.stream(
            "POST",
            f"{AI_URL}/ai/recommend",
            json=payload,
            timeout=AI_TIMEOUT,
        ) as response:
            response.raise_for_status()
            for event, data in parse_sse(response.iter_lines()):
                if event == "error":
                    raise RuntimeError(data.get("message"))
                if event == "status":
                    if data.get("node") in NEXT_STEP:
                        step, label = NEXT_STEP[data["node"]]
                        yield sse(event, {"step": step, "total": 4, "label": label, "elapsed": data.get("elapsed", 0)})
                elif event == "token":
                    tokens.append(data["text"])
                    yield sse(event, data)
                elif event == "done":
                    completed = True
                else:
                    events[event] = data
        if not completed:
            raise RuntimeError("AI stream ended without done")
        if context is not None and not "".join(tokens).strip():
            raise RuntimeError("AI returned an empty question answer")
        elapsed = round(time.time() - started, 2)
        done = (ChatDone(type="answer", group_id=group_id, elapsed=elapsed, answer="".join(tokens),
                        sources=[Source(**s) for s in context["sources"]]) if context is not None
                else build_done(events, group_id, "".join(tokens), elapsed))
    except Exception:  # internal details stay in the log; the stream must end with an event
        logging.exception("chat failed ip=%s group=%s", ip, group_id)
        yield sse("error", {"code": "AI_UNAVAILABLE", "message": AI_ERROR, "group_id": str(group_id)})
        return
    try:
        _save_answer(pool, done)
    except Exception:  # the user still gets the answer they waited for; only its history entry is lost
        logging.exception("saving the answer failed group=%s", group_id)
        done.history_saved = False
    logging.info("chat done ip=%s type=%s elapsed=%.1f", ip, done.type, done.elapsed)
    yield sse("done", done.model_dump(mode="json"))


CHAT_RESPONSES: dict[int | str, dict[str, Any]] = {
    200: {
        "description": (
            "Server-Sent Events. `status` and `token` repeat, then one `done` (the schema below) or one `error`. "
            "Swagger shows the stream only once it ends; use `curl -N` to watch it."
        ),
        "content": {
            "text/event-stream": {
                "schema": {"type": "string"},
                "example": (
                    'event: status\ndata: {"step": 1, "total": 4, "label": "요구사항 분석", "elapsed": 2.4}\n\n'
                    'event: token\ndata: {"text": "추천 "}\n\n'
                    'event: done\ndata: {"schema_version": 2, "type": "answer", "group_id": "00000000-0000-0000-0000-000000000001", "elapsed": 14.1, '
                    '"answer": "추천 후보가 없습니다.", "sources": [], "result": {"title": "추천 결과", "summary": [], "needs_check": [], '
                    '"candidates": [], "assessment": null}, "history_saved": true}\n\n'
                )
            }
        },
    },
    403: {"description": "다른 세션의 대화"},
    404: {"description": "없는 group_id"},
    409: {"description": "해당 대화 처리 중 또는 질문할 추천 결과 없음"},
    422: {"description": "요청 형식 오류 또는 유효하지 않은 질문 대상"},
    503: {"description": "DB 미설정"},
    429: {"description": "요청 제한 초과, Retry-After 헤더 참고"},
}


@app.post("/api/chat", response_class=StreamingResponse, responses=CHAT_RESPONSES)
def chat(body: ChatRequest, request: Request, session_id: SessionId):
    """Ask a question. A query on a group waiting at `clarify` answers its questions."""
    ip = client_ip(request)
    wait = limiter.retry_after(ip)
    if wait is not None:
        logging.warning("chat rate limited ip=%s retry_after=%s", ip, wait)
        raise HTTPException(429, "요청이 너무 많습니다. 잠시 후 다시 시도해 주세요.", {"Retry-After": str(wait)})
    pool = _pool()
    group_id = body.group_id
    lease = None
    if group_id is not None:
        lease = claim_group(group_id)
    try:
        context = question_context(pool, body, session_id) if body.mode == "question" else None
        group_id = _open_group(pool, group_id, session_id, body.query)
        if body.group_id is None:
            lease = claim_group(group_id)
    except Exception:
        if group_id is not None:
            release_group(group_id, lease)
        raise
    return ChatStream(
        stream_chat(pool, group_id, body.query, ip, context),
        group_id,
        lease,
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Group-Id": str(group_id), "X-Accel-Buffering": "no"},
    )


def question_context(pool: Any, body: ChatRequest, session_id: UUID) -> dict:
    with pool.connection() as conn:
        owner = conn.execute("select session_id from app.groups where group_id = %s", (body.group_id,)).fetchone()
        if owner is None:
            raise HTTPException(404, "대화를 찾을 수 없습니다.")
        if owner["session_id"] != session_id:
            raise HTTPException(403, "이 대화에 이어서 질문할 수 없습니다.")
        row = conn.execute("select result, sources from app.messages where group_id = %s and result is not null order by id desc limit 1",
                           (body.group_id,)).fetchone()
        history = conn.execute("select role, content from app.messages where group_id = %s order by id desc limit %s",
                               (body.group_id, QUESTION_HISTORY)).fetchall()
    if row is None:
        raise HTTPException(409, "먼저 추천을 완료해 주세요.")
    result = ChatResult.model_validate(row["result"])
    candidates = result.candidates
    if body.target_id:
        candidates = [c for c in candidates if c.id == body.target_id]
        if not candidates:
            raise HTTPException(422, "현재 추천 결과에 없는 target_id입니다.")
    ids = {(c.source_id, c.type) for c in candidates}
    saved_sources = row.get("sources") or row["result"].get("sources") or []
    context = {"summary": result.summary, "candidates": [c.model_dump() for c in candidates],
               "sources": [Source(**s).model_dump() for s in saved_sources if (s["source_id"], s["kind"]) in ids],
               "history": [{"role": m["role"], "content": m["content"][:2000]} for m in reversed(history)]}
    if len(json.dumps(context, ensure_ascii=False)) > 100_000:
        raise HTTPException(422, "질문 대상 모델 또는 데이터셋을 선택해 주세요.")
    return context


@app.get("/api/groups")
def list_groups(session_id: SessionId) -> list[GroupSummary]:
    """Conversations of this session, latest first."""
    with _pool().connection() as conn:
        rows = conn.execute(
            "select group_id, title, created_at, updated_at from app.groups "
            "where session_id = %s order by updated_at desc limit 100",
            (session_id,),
        ).fetchall()
    return [GroupSummary(**row) for row in rows]


@app.get("/api/groups/{group_id}", responses={404: {"description": "없는 group_id"}})
def get_group(group_id: UUID) -> GroupDetail:
    """A stored conversation. Readable by anyone holding the link; continuing it needs the same session."""
    with _pool().connection() as conn:
        group = conn.execute(
            "select group_id, title, created_at, updated_at from app.groups where group_id = %s", (group_id,)
        ).fetchone()
        if group is None:
            raise HTTPException(404, "대화를 찾을 수 없습니다.")
        messages = conn.execute(
            "select id, role, content, type, result, sources, created_at from app.messages where group_id = %s order by id",
            (group_id,),
        ).fetchall()
    latest = next((m["result"] for m in reversed(messages) if m["result"] is not None), None)
    for message in messages:
        if not message.get("sources") and message.get("result"):
            message["sources"] = message["result"].get("sources") or []
    return GroupDetail(**group, messages=messages, result=latest)


def readme_path(source_id: str, kind: Literal["model", "dataset"] | None = None) -> Path | None:
    """Only ids of the expected shape reach the disk, so no id can walk out of READMES_DIR."""
    if not SOURCE_ID_RE.fullmatch(source_id) or any(part in (".", "..") for part in source_id.split("/")):
        return None
    for prefix, directory in README_DIRS.items():
        if source_id.startswith(prefix):
            if kind == "model":
                return None
            stem = source_id if directory == "public" else source_id[len(prefix) :]
            path = READMES_DIR / directory / f"{stem.replace('/', '__')}.md"
            path = path.resolve()
            return path if path.is_relative_to(READMES_DIR) and path.is_file() else None
    for directory in HF_README_DIRS:
        if kind == "model" and directory == "datasets" or kind == "dataset" and directory != "datasets":
            continue
        path = READMES_DIR / directory / f"{source_id.replace('/', '__')}.md"
        path = path.resolve()
        if path.is_relative_to(READMES_DIR) and path.is_file():
            return path
    return None


@app.get("/api/files/{source_id:path}", responses={404: {"description": "원문 없음"}})
def get_file(
    source_id: Annotated[str, PathParam(description="result.sources[].source_id", examples=["openai/gsm8k"])],
    kind: Literal["model", "dataset"] | None = None,
) -> SourceFile:
    """README of a model or dataset."""
    path = readme_path(source_id, kind)
    if path is None:
        raise HTTPException(404, "원문을 찾을 수 없습니다.")
    with open(path, encoding="utf-8", errors="replace") as f:
        content = f.read(MAX_README_BYTES + 1)
        return SourceFile(source_id=source_id, content=content[:MAX_README_BYTES], truncated=len(content) > MAX_README_BYTES)


@app.get("/api/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8000")))
