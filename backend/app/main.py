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
from collections.abc import Iterable, Iterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated, Any
from uuid import UUID, uuid4

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi import Path as PathParam
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool
from pydantic import BaseModel, Field
from rate_limit import RateLimiter
from result import ChatDone, GroupDetail, GroupSummary, SourceFile, build_done, stored_text

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

AI_URL = os.getenv("AI_URL", "http://127.0.0.1:8001")
READMES_DIR = Path(os.getenv("READMES_DIR", Path(__file__).resolve().parents[2] / "ai" / "data" / "readmes"))
# A source id maps to a file by its prefix; other ids are Hugging Face datasets or models.
README_DIRS = {"kaggle/": "kaggle", "seoul_open_data/": "public", "data_go_kr/": "public"}
HF_README_DIRS = ("datasets", "core", "low_popularity")
SOURCE_ID_RE = re.compile(r"^[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)*$")
MAX_README_BYTES = 2_000_000
DB_ENV = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")
AI_TIMEOUT = httpx.Timeout(10.0, read=180.0)
AI_ERROR = "추천을 만드는 중 오류가 났습니다. 잠시 후 다시 시도해 주세요."

limiter = RateLimiter(int(os.getenv("RATE_LIMIT_PER_MINUTE", "10")), int(os.getenv("DAILY_REQUEST_LIMIT", "300")))

SessionId = Annotated[UUID, Header(alias="X-Session-Id", description="crypto.randomUUID() kept in localStorage")]


class ChatRequest(BaseModel):
    group_id: UUID | None = Field(default=None, description="null starts a new conversation")
    query: str = Field(min_length=1, max_length=2000, examples=["따릉이 경로 추천 서비스를 만들고 싶어"])


def _conninfo() -> str | None:
    if not all(os.getenv(name) for name in DB_ENV):
        return None
    env = os.environ
    return (
        f"host={env['SUPABASE_DB_HOST']} port={env['SUPABASE_DB_PORT']} dbname={env['SUPABASE_DB_NAME']} "
        f"user={env['SUPABASE_DB_USER']} password={env['SUPABASE_PASSWORD']} "
        f"sslmode={env.get('SUPABASE_DB_SSLMODE', 'require')}"
    )


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
    event, data = "message", ""
    for line in lines:
        if line.startswith("event: "):
            event = line[7:]
        elif line.startswith("data: "):
            data += line[6:]
        elif not line and data:
            yield event, json.loads(data)
            event, data = "message", ""


def _open_group(pool: Any, group_id: UUID | None, session_id: UUID, query: str) -> UUID:
    with pool.connection() as conn:
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
    with pool.connection() as conn:
        conn.execute(
            "insert into app.messages (group_id, role, content, type, result) values (%s, 'assistant', %s, %s, %s)",
            (done.group_id, stored_text(done), done.type, result),
        )
        conn.execute("update app.groups set updated_at = now() where group_id = %s", (done.group_id,))


def stream_chat(pool: Any, group_id: UUID, query: str, ip: str) -> Iterator[str]:
    started = time.time()
    events: dict[str, Any] = {}
    tokens: list[str] = []
    try:
        with httpx.stream(
            "POST",
            f"{AI_URL}/ai/recommend",
            json={"query": query, "thread_id": str(group_id)},
            timeout=AI_TIMEOUT,
        ) as response:
            response.raise_for_status()
            for event, data in parse_sse(response.iter_lines()):
                if event == "error":
                    raise RuntimeError(data.get("message"))
                if event == "status":
                    yield sse(event, data)
                elif event == "token":
                    tokens.append(data["text"])
                    yield sse(event, data)
                elif event != "done":
                    events[event] = data
        done = build_done(events, group_id, "".join(tokens), round(time.time() - started, 2))
    except Exception:  # internal details stay in the log; the stream must end with an event
        logging.exception("chat failed ip=%s group=%s", ip, group_id)
        yield sse("error", {"message": AI_ERROR})
        return
    try:
        _save_answer(pool, done)
    except Exception:  # the user still gets the answer they waited for; only its history entry is lost
        logging.exception("saving the answer failed group=%s", group_id)
    logging.info("chat done ip=%s type=%s elapsed=%.1f", ip, done.type, done.elapsed)
    yield sse("done", done.model_dump(mode="json"))


CHAT_RESPONSES: dict[int | str, dict[str, Any]] = {
    200: {
        "description": (
            "Server-Sent Events. `status` and `token` repeat, then one `done` (the schema below) or one `error`. "
            "Swagger shows the stream only once it ends; use `curl -N` to watch it."
        ),
        "model": ChatDone,
        "content": {
            "text/event-stream": {
                "example": (
                    'event: status\ndata: {"node": "decompose", "elapsed": 2.4}\n\n'
                    'event: token\ndata: {"text": "추천 "}\n\n'
                    'event: done\ndata: {"type": "answer", "group_id": "...", "elapsed": 14.1, '
                    '"answer": "추천 ...", "result": {"summary": "...", "candidates": [], "datasets": {}, '
                    '"assessment": null, "sources": []}, "questions": null, "message": null}\n\n'
                )
            }
        },
    },
    403: {"description": "다른 세션의 대화"},
    404: {"description": "없는 group_id"},
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
    group_id = _open_group(pool, body.group_id, session_id, body.query)
    return StreamingResponse(
        stream_chat(pool, group_id, body.query, ip),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Group-Id": str(group_id)},
    )


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
            "select role, content, type, result, created_at from app.messages where group_id = %s order by id",
            (group_id,),
        ).fetchall()
    return GroupDetail(**group, messages=messages)


def readme_path(source_id: str) -> Path | None:
    """Only ids of the expected shape reach the disk, so no id can walk out of READMES_DIR."""
    if not SOURCE_ID_RE.fullmatch(source_id) or any(part in (".", "..") for part in source_id.split("/")):
        return None
    for prefix, directory in README_DIRS.items():
        if source_id.startswith(prefix):
            stem = source_id if directory == "public" else source_id[len(prefix) :]
            path = READMES_DIR / directory / f"{stem.replace('/', '__')}.md"
            return path if path.is_file() else None
    for directory in HF_README_DIRS:
        path = READMES_DIR / directory / f"{source_id.replace('/', '__')}.md"
        if path.is_file():
            return path
    return None


@app.get("/api/files/{source_id:path}", responses={404: {"description": "원문 없음"}})
def get_file(
    source_id: Annotated[str, PathParam(description="result.sources[].source_id", examples=["openai/gsm8k"])],
) -> SourceFile:
    """README of a model or dataset."""
    path = readme_path(source_id)
    if path is None:
        raise HTTPException(404, "원문을 찾을 수 없습니다.")
    with open(path, encoding="utf-8", errors="replace") as f:
        return SourceFile(source_id=source_id, content=f.read(MAX_README_BYTES))


@app.get("/api/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8000")))
