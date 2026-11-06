"""Contract/HTTP/stream/storage tests. SQLite is a local storage double, not PostgreSQL validation."""
import importlib.util
import json
import sqlite3
import sys
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from uuid import UUID, uuid4

import anyio
import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "ai"))
from backend.app import main as api
from backend.app.rate_limit import RateLimiter
from backend.app.result import ChatDone, ChatResult, GroupDetail, build_done, build_sources
from recommendation_question import stream_question


def recommendation_events():
    need = {"task": "retrieval", "purpose_ko": "문서 검색"}
    model = {"model_id": "org/model", "rank_score": .9, "license": "mit", "commercial_use": "commercial",
             "context_length": 512, "gpu_fit": {"verdict": "too_large", "label": "GPU 부족"}, "evidence": "original quote"}
    dataset = {"dataset": "org/data", "title": "데이터", "licenses": ["mit"],
               "evidence": [{"concept": "검색", "source": "README 인용", "text": "dataset quote"}]}
    return {"plan": {"summary_ko": "문서 검색 서비스", "needs": [need],
                     "constraints": {"gpu_memory_gb": 8, "min_context_length": 1024}},
            "models": [{"need": need, "models": [model]}, {"need": need, "models": [model]}],
            "datasets": {"per_model": {"org/model": [dataset]}, "service_data": [dataset]}}


class Store:
    def __init__(self):
        self.db = sqlite3.connect(":memory:", check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
            attach database ':memory:' as app;
            create table app.groups (group_id text primary key, session_id text, title text,
                created_at text default '2026-11-06T00:00:00Z', updated_at text default '2026-11-06T00:00:00Z');
            create table app.messages (id integer primary key, group_id text, role text, content text,
                type text, result text, sources text default '[]', created_at text default '2026-11-06T00:00:00Z');
        """)
        self.db.create_function("now", 0, lambda: "2026-11-06T00:00:01Z")
        self.fail_save = False

    @contextmanager
    def connection(self):
        yield self

    @contextmanager
    def transaction(self):
        with self.db:
            yield

    def execute(self, sql, params):
        if self.fail_save and "'assistant'" in sql:
            raise RuntimeError("storage unavailable")
        def encode(value):
            if isinstance(value, UUID):
                return str(value)
            if hasattr(value, "obj"):
                return json.dumps(value.obj)
            return value
        cursor = self.db.execute(sql.replace("%s", "?"), tuple(encode(v) for v in params))
        def decode(row):
            if row is None:
                return None
            item = dict(row)
            for key in ("result", "sources"):
                if item.get(key):
                    item[key] = json.loads(item[key])
            if "session_id" in item:
                item["session_id"] = UUID(item["session_id"])
            return item
        return SimpleNamespace(fetchone=lambda: decode(cursor.fetchone()),
                               fetchall=lambda: [decode(r) for r in cursor.fetchall()])


@pytest.fixture(scope="module")
def http_client():
    with patch.object(api, "_conninfo", return_value=None), TestClient(api.app) as client:
        yield client


@pytest.fixture
def client(http_client):
    store = Store()
    try:
        api.app.state.pool = store
        api.active_groups.clear()
        api.limiter = RateLimiter(100, 1000)
        yield http_client, store
    finally:
        api.app.state.pool = None
        store.db.close()


class Upstream:
    def __init__(self, events):
        self.events = events
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    def raise_for_status(self):
        pass
    def iter_lines(self):
        for event, data in self.events:
            yield from api.sse(event, data).splitlines()


def ai_events(events=None, done=True):
    events = recommendation_events() if events is None else events
    result = [(k, v) for k, v in events.items()]
    result += [("token", {"text": "답변"})]
    if done:
        result.append(("done", {"elapsed": 1}))
    return result


def final(response):
    assert response.status_code == 200, response.text
    events = list(api.parse_sse(response.text.splitlines()))
    return events[-1]


def test_result_links_dedup_and_unknowns():
    done = build_done(recommendation_events(), uuid4(), "답", 1)
    assert len(done.result.candidates) == 2
    model, dataset = done.result.candidates
    assert model.related == [dataset.id] and dataset.related == [model.id]
    statuses = {c.key: c.status for c in model.checks}
    assert statuses == {"license": "ok", "gpu": "check", "context": "check", "language": "unknown", "execution": "unknown"}
    assert done.sources[0].quote == "original quote"
    assert done.sources[1].quote == "dataset quote"
    assert model.checks[0].quote is None  # Metadata is not fabricated as a README quote.
    assert [c.key for c in dataset.checks] == ["license"] and dataset.checks[0].status == "check"
    assert dataset.evidence[0].label == "검색" and dataset.evidence[0].origin == "readme"
    assert ChatDone.model_validate_json(done.model_dump_json()) == done


def test_clarify_reject_and_no_candidates():
    clarify = build_done({"clarify": {"questions": ["어떤 서비스?"]}}, uuid4(), "", 1)
    assert clarify.type == "clarify" and clarify.answer == "어떤 서비스?" and clarify.result is None
    reject = build_done({"plan": {"needs": []}}, uuid4(), "", 1)
    assert reject.type == "reject" and reject.answer and reject.sources == []
    empty = build_done({"plan": {"needs": [{"task": "retrieval"}]}}, uuid4(), "없어요", 1)
    assert empty.type == "answer" and empty.result.candidates == []


def test_http_recommend_question_and_restore(client):
    client, store = client
    headers = {"X-Session-Id": str(uuid4())}
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events())):
        response = client.post("/api/chat", json={"query": "문서 검색"}, headers=headers)
    event, done = final(response)
    assert event == "done" and done["history_saved"]
    gid = done["group_id"]
    assert response.headers["x-group-id"] == gid
    assert not api.active_groups
    groups = client.get("/api/groups", headers=headers).json()
    assert groups[0]["group_id"] == gid
    assert client.get("/api/groups", headers={"X-Session-Id": str(uuid4())}).json() == []
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events({}, done=True))) as upstream:
        response = client.post("/api/chat", json={"query": "왜 추천했어?", "mode": "question",
            "group_id": gid, "target_id": "model:org/model"}, headers=headers)
    event, question = final(response)
    assert event == "done" and question["result"] is None and question["sources"]
    payload = upstream.call_args.kwargs["json"]
    assert payload["mode"] == "question" and len(payload["context"]["candidates"]) == 1
    assert [m["role"] for m in payload["context"]["history"]] == ["user", "assistant"]
    assert payload["context"]["history"][0]["content"] == "문서 검색"
    restored = client.get(f"/api/groups/{gid}").json()  # Shared-link read is intentional.
    assert restored["result"] == done["result"]
    assert len(restored["messages"]) == 4
    assert restored["messages"][-1]["sources"] == question["sources"]
    assert restored["messages"][-1]["id"] > restored["messages"][0]["id"]
    with patch.object(api.httpx, "stream") as upstream:
        assert client.post("/api/chat", json={"query": "x", "group_id": gid},
                           headers={"X-Session-Id": str(uuid4())}).status_code == 403
        assert client.post("/api/chat", json={"query": "x", "group_id": gid, "mode": "question",
            "target_id": "model:other"}, headers=headers).status_code == 422
        upstream.assert_not_called()


def test_failures_do_not_pretend_success(client):
    client, store = client
    headers = {"X-Session-Id": str(uuid4())}
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events(done=False))):
        response = client.post("/api/chat", json={"query": "x"}, headers=headers)
    assert final(response)[0] == "error"
    assert not api.active_groups
    store.fail_save = True
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events())):
        response = client.post("/api/chat", json={"query": "y"}, headers=headers)
    assert final(response)[1]["history_saved"] is False


def test_validation_limits_and_cors(client):
    client, store = client
    headers = {"X-Session-Id": str(uuid4())}
    for body in [{"query": " "}, {"query": "x", "conditions": {}}, {"query": "x", "mode": "question"},
                 {"query": "x", "target_id": "model:a"}, {"query": "x" * 2001}]:
        assert client.post("/api/chat", json=body, headers=headers).status_code == 422
    assert client.post("/api/chat", json={"query": "x"}).status_code == 422
    api.limiter = RateLimiter(1, 1000)
    api.limiter.retry_after("testclient")
    response = client.post("/api/chat", json={"query": "x"}, headers={**headers, "Origin": "http://localhost:3000"})
    assert response.status_code == 429 and "retry-after" in response.headers
    assert "Retry-After" in response.headers["access-control-expose-headers"]
    api.app.state.pool = None
    assert client.get("/api/groups", headers=headers).status_code == 503


def test_single_group_lease():
    gid = uuid4()
    lease = api.claim_group(gid)
    with pytest.raises(api.HTTPException) as caught:
        api.claim_group(gid)
    assert caught.value.status_code == 409
    api.release_group(gid, lease)
    newer = api.claim_group(gid)
    api.release_group(gid, lease)  # A stale holder must not release a newer request.
    assert gid in api.active_groups
    api.release_group(gid, newer)


def test_source_path_and_truncation(client, tmp_path):
    client, _ = client
    (tmp_path / "core").mkdir()
    (tmp_path / "core" / "org__model.md").write_text("원문입니다", encoding="utf-8")
    (tmp_path / "datasets").mkdir()
    (tmp_path / "datasets" / "org__model.md").write_text("데이터원문", encoding="utf-8")
    with patch.object(api, "READMES_DIR", tmp_path), patch.object(api, "MAX_README_BYTES", 3):
        assert api.readme_path("../outside") is None
        assert api.readme_path("org/../outside") is None
        response = client.get("/api/files/org/model?kind=model")
        assert response.json() == {"source_id": "org/model", "content": "원문입", "truncated": True}
        assert client.get("/api/files/org/model?kind=dataset").json()["content"] == "데이터"
        assert client.get("/api/files/no/such").status_code == 404


def test_sse_framing_and_legacy_snapshot():
    assert list(api.parse_sse(['event:token', 'data:{"text":', 'data:"가"}', ''])) == [("token", {"text": "가"})]
    assert list(api.parse_sse(['event: done', 'data: {"elapsed": 1}'])) == [("done", {"elapsed": 1})]
    legacy = {"summary": "old", "candidates": [{"model_id": "a/b", "task": "retrieval", "purpose": "검색",
        "license": "mit", "rank_score": .8, "checks": [
            {"key": "gpu", "label": "GPU", "status": "review", "reason": "old GPU constraint"}]}], "datasets": {}, "sources": []}
    restored = ChatResult.model_validate(legacy)
    assert restored.candidates[0].id == "model:a/b"
    assert restored.candidates[0].checks[0].status == "check"
    assert restored.candidates[0].checks[0].reason == "old GPU constraint"


def test_question_ai_uses_snapshot_and_handles_errors():
    class Stream:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def __iter__(self):
            yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content="근거 답변"))])
    from unittest.mock import Mock
    factory = Mock()
    factory.return_value.chat.completions.create.return_value = Stream()
    events = list(api.parse_sse("".join(stream_question(factory, "test", "질문", {"sources": []}, "thread")).splitlines()))
    assert events[-1][0] == "done" and events[1][1]["text"] == "근거 답변"
    assert "context" in factory.return_value.chat.completions.create.call_args.kwargs["messages"][1]["content"]
    factory.side_effect = RuntimeError("secret must not leak")
    events = list(api.parse_sse("".join(stream_question(factory, "test", "질문", {}, "thread")).splitlines()))
    assert events[-1][0] == "error" and "secret" not in events[-1][1]["message"]


def test_screen_text_shows_only_real_conditions():
    events = recommendation_events()
    events["plan"]["constraints"] = {"commercial_only": False, "gpu_memory_gb": 8, "min_context_length": None}
    result = build_done(events, uuid4(), "답", 1).result
    assert result.summary == ["문서 검색 서비스", "GPU 메모리(GB): 8"]
    assert result.needs_check == ["model: GPU 메모리"]
    events["plan"]["constraints"]["commercial_only"] = True
    assert "상업 이용 가능한 모델만" in build_done(events, uuid4(), "답", 1).result.summary


def test_same_id_keeps_model_and_dataset_sources():
    need = {"task": "retrieval"}
    events = {"models": [{"need": need, "models": [{"model_id": "org/x"}]}],
              "datasets": {"service_data": [{"dataset": "org/x", "title": "t"}]}}
    assert {s.kind for s in build_sources(events)} == {"model", "dataset"}


def test_status_names_the_running_step(client):
    client, _ = client
    nodes = ["decompose", "clarify", "search_models", "search_datasets", "assess", "explain"]
    upstream = [("status", {"node": n, "elapsed": 1}) for n in nodes] + ai_events()
    with patch.object(api.httpx, "stream", return_value=Upstream(upstream)):
        response = client.post("/api/chat", json={"query": "x"}, headers={"X-Session-Id": str(uuid4())})
    labels = [d["label"] for e, d in api.parse_sse(response.text.splitlines()) if e == "status"]
    assert labels == ["요구사항 분석", "요구사항 확인", "모델 검색", "데이터셋 검색", "조건 확인", "답변 생성"]


@pytest.mark.parametrize("started", [True, False])
def test_disconnect_ends_ai_call_before_freeing_group(started):
    gid, closed = uuid4(), []
    lease = api.claim_group(gid)

    def body():
        try:
            yield "a"
            yield "b"
        finally:
            closed.append(gid in api.active_groups)

    stream = body()
    if started:
        next(stream)

    async def receive():
        return {"type": "http.disconnect"}

    async def send(message):
        pass

    anyio.run(api.ChatStream(stream, gid, lease), {"type": "http", "asgi": {"spec_version": "2.3"}}, receive, send)
    assert gid not in api.active_groups
    assert closed == ([True] if started else [])  # An unstarted generator has no finally, the group is still freed.


def test_resume_after_clarify_returns_the_new_plan():
    """Real graph and clarify node with the real AI stream; only the LLM and the searches are stubbed."""
    pytest.importorskip("langgraph")
    from langgraph.checkpoint.memory import InMemorySaver
    spec = importlib.util.spec_from_file_location("ai_api", ROOT / "ai" / "api.py")
    ai = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ai)
    ai.app.state.pool = None
    need = {"task": "retrieval", "purpose_ko": "검색"}
    limits = {"commercial_only": False, "gpu_memory_gb": None, "min_context_length": None}
    vague = {"summary_ko": "모호", "needs": [need], "constraints": limits, "clarifying_questions": ["어떤 서비스?"]}
    graph = ai.rg.build_graph({
        "decompose": lambda s: {"plan": vague},
        "clarify": ai.rg.clarify,
        "search_models": lambda s: {"models": [{"need": need, "models": [{"model_id": "org/m"}]}]},
        "search_datasets": lambda s: {"datasets": {}},
        "assess": lambda s: {"assessment": {}},
        "explain": lambda s: {"answer": "답"},
    }, checkpointer=InMemorySaver())
    gid = uuid4()

    def turn(payload):
        sent = api.parse_sse("".join(ai.stream_recommendation(graph, payload, str(gid))).splitlines())
        return build_done({e: d for e, d in sent if e not in ("status", "done")}, gid, "답", 1)

    assert turn({"request": "추천해줘"}).type == "clarify"
    plan = {**vague, "summary_ko": "구체화된 계획", "clarifying_questions": []}
    with patch.object(ai.rg, "_parse_plan", return_value=plan):
        done = turn(ai.rg.Command(resume="문서 검색"))
    assert done.type == "answer" and done.result.title == "구체화된 계획"


def test_http_clarify_resume_and_busy(client):
    client, store = client
    headers = {"X-Session-Id": str(uuid4())}
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events({"clarify": {"questions": ["어떤 서비스?"]}}))):
        _, clarify = final(client.post("/api/chat", json={"query": "추천"}, headers=headers))
    gid = clarify["group_id"]
    assert clarify["type"] == "clarify" and clarify["answer"] == "어떤 서비스?"
    assert client.post("/api/chat", json={"query": "질문", "mode": "question", "group_id": gid}, headers=headers).status_code == 409
    lease = api.claim_group(UUID(gid))
    try:
        response = client.post("/api/chat", json={"query": "문서 검색", "group_id": gid}, headers=headers)
        assert response.status_code == 409
    finally:
        api.release_group(UUID(gid), lease)
    with patch.object(api.httpx, "stream", return_value=Upstream(ai_events())) as upstream:
        _, answer = final(client.post("/api/chat", json={"query": "문서 검색", "group_id": gid}, headers=headers))
    assert answer["type"] == "answer" and upstream.call_args.kwargs["json"]["thread_id"] == gid
    assert len(client.get(f"/api/groups/{gid}").json()["messages"]) == 4


def test_frontend_fixtures_match_contract():
    examples = ROOT / "backend" / "examples"
    for name in ["answer", "question", "clarify", "reject", "empty", "save-failed"]:
        ChatDone.model_validate_json((examples / f"{name}.json").read_text(encoding="utf-8"))
    GroupDetail.model_validate_json((examples / "group.json").read_text(encoding="utf-8"))
    stored_schema = json.loads((examples / "chat-done.schema.json").read_text(encoding="utf-8"))
    assert stored_schema == ChatDone.model_json_schema()
    stored_openapi = json.loads((examples / "openapi.json").read_text(encoding="utf-8"))
    assert stored_openapi == api.app.openapi()
