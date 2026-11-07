"""Internal recommendation API: the one endpoint the backend calls. Not published outside Docker.

The full answer takes ~10-25 s (two LLM calls and the model search), so each step is streamed:

    event: status      {"node": "decompose", "elapsed": 2.4}      after every graph node
    event: plan        ProjectPlan                                   needs + constraints
    event: clarify     {"questions": [...]}                          vague request: the run pauses here
    event: models      [{need, models}]                              per need; each model has gpu_fit,
                                                                     benchmarks and a README evidence quote
    event: datasets    {per_model, project_training, service_data}   each with licenses + evidence quotes
    event: assessment  {"license": {verdict, label, reason, ...}}    commercial launch verdict
    event: token       {"text": "..."}                               answer, as it is written
    event: done        {"thread_id": "...", "elapsed": 14.1}
    event: error       {"message": "..."}

thread_id is the backend's group_id. Checkpoints persist in Supabase (PostgresSaver, schema langgraph), so a
follow-up revises the previous plan and the next query on a paused thread answers its clarify questions.
Without database settings it falls back to memory.

    python ai/api.py                      # HOST / PORT env, default 127.0.0.1:8001
"""

from __future__ import annotations

import importlib.util
import json
import logging
import os
import sys
import threading
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, cast

from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from pydantic import model_validator
from typing import Literal
from recommendation_question import stream_question

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
logging.getLogger("httpx").setLevel(logging.WARNING)


def _load_graph_module():
    spec = importlib.util.spec_from_file_location("recommend_graph", ROOT / "17_recommend_graph.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["recommend_graph"] = module  # LangGraph resolves the State annotations through it
    spec.loader.exec_module(module)
    return module


rg = _load_graph_module()


class RecommendRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000, examples=["따릉이 경로 추천 서비스를 만들고 싶어"])
    thread_id: str = Field(pattern=r"^[A-Za-z0-9_.:-]{1,80}$", description="the backend's group_id")
    mode: Literal["recommend", "question"] = "recommend"
    context: dict[str, Any] | None = None

    @model_validator(mode="after")
    def validate_context(self):
        if self.mode == "question" and (self.context is None or len(json.dumps(self.context, ensure_ascii=False)) > 100_000):
            raise ValueError("question requires a saved recommendation context of at most 100000 characters")
        return self


def _checkpointer():
    """PostgresSaver on a small pool when Supabase is configured; in-memory otherwise."""
    from langgraph.checkpoint.memory import InMemorySaver

    from supabase_db import configured

    if not configured():
        return InMemorySaver(), None
    from langgraph.checkpoint.postgres import PostgresSaver
    from psycopg.rows import dict_row
    from psycopg_pool import ConnectionPool

    with rg.postgres_checkpointer():  # creates schema/tables and locks them down, idempotent
        pass
    pool = ConnectionPool(
        rg.supabase_conninfo(),
        min_size=1,
        max_size=int(os.getenv("CHECKPOINT_POOL_SIZE", "5")),
        kwargs={"autocommit": True, "prepare_threshold": 0, "row_factory": dict_row},
        open=True,
    )
    # row_factory=dict_row makes these dict-row connections; the pool's generic type cannot say so.
    return PostgresSaver(cast(Any, pool)), pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Warm every cache once so the first request does not pay for loading the graph files.
    import hypergraph_search

    hypergraph_search.load_graph()
    if (hypergraph_search.DATASET_INDEX_DIR / "embeddings.npy").exists():
        hypergraph_search.load_dataset_vectors()
    else:
        logging.warning("embeddings.npy is missing: dataset search falls back to Supabase, about 10 s per query")
    rg._load_09()
    try:  # first query after a restart or DB rewrite reads cold pages; pay that here, not per user
        rg._load_09().search_models("한국어 임베딩 모델", match_count=1)
    except Exception:
        logging.exception("warm-up search failed; continuing")
    saver, pool = _checkpointer()
    app.state.graph, app.state.pool = rg.build_graph(checkpointer=saver), pool
    if pool is not None:
        with pool.connection() as conn:
            logging.info(
                "pruned %s idle conversations",
                rg.prune_idle_threads(conn, days=int(os.getenv("THREAD_TTL_DAYS", "30"))),
            )
    yield
    if pool is not None:
        pool.close()


app = FastAPI(
    title="Model Scout AI API (internal)",
    lifespan=lifespan,
    openapi_url="/openapi.json" if os.getenv("ENABLE_DOCS", "1") == "1" else None,  # None also removes /docs and /redoc
)


def sse(event, data):
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


NODE_EVENTS = {
    "decompose": ("plan", "plan"),
    "clarify": ("plan", "plan"),  # resuming re-plans here; decompose does not run again
    "search_models": ("models", "models"),
    "search_datasets": ("datasets", "datasets"),
    "assess": ("assessment", "assessment"),
}


def stream_recommendation(graph, payload, thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    started = time.time()
    try:
        for mode, data in graph.stream(
            payload, config, stream_mode=["updates", "custom"], durability="exit"
        ):  # one checkpoint per turn
            if mode == "custom":
                yield sse("token", {"text": data["token"]})
                continue
            for node, values in data.items():
                if node == "__interrupt__":  # clarify paused the run; the next query resumes it
                    yield sse("clarify", {"questions": values[0].value["questions"]})
                    continue
                yield sse("status", {"node": node, "elapsed": round(time.time() - started, 2)})
                if node in NODE_EVENTS and values and NODE_EVENTS[node][1] in values:
                    event, key = NODE_EVENTS[node]
                    yield sse(event, values[key])
        if app.state.pool is not None:
            with app.state.pool.connection() as conn:
                rg.prune_thread(conn, thread_id)
        yield sse("done", {"thread_id": thread_id, "elapsed": round(time.time() - started, 2)})
    except Exception as error:  # surfaced to the backend; the stream must end with an event
        logging.exception("recommendation failed")
        yield sse("error", {"message": f"{type(error).__name__}: {error}"[:500]})


CANCEL_WAIT = 30  # seconds; a cancelled run only stops once its running node ends, so a retry waits for that
running_threads: set[str] = set()
running_changed = threading.Condition()


def claim_thread(thread_id: str) -> None:
    with running_changed:
        if not running_changed.wait_for(lambda: thread_id not in running_threads, CANCEL_WAIT):
            raise HTTPException(409, "thread is still running")
        running_threads.add(thread_id)


def release_thread(thread_id: str) -> None:
    with running_changed:
        running_threads.discard(thread_id)
        running_changed.notify_all()


class RecommendationStream(StreamingResponse):
    """Stops the graph before freeing the thread, also on a disconnect.

    Closing a run writes its checkpoint. Left to the garbage collector, that write could land on top of a newer run.
    """

    def __init__(self, run: Any, thread_id: str, **kwargs: Any):
        super().__init__(run, **kwargs)
        self.run, self.thread_id = run, thread_id

    async def __call__(self, scope: Any, receive: Any, send: Any) -> None:
        try:
            await super().__call__(scope, receive, send)
        finally:
            try:
                await run_in_threadpool(self.run.close)
            finally:
                release_thread(self.thread_id)


@app.post("/ai/recommend", response_class=StreamingResponse)
def recommend(body: RecommendRequest):
    if body.mode == "question":  # reads the saved snapshot only, so it cannot collide with a run
        return StreamingResponse(stream_question(rg._openai, rg.LLM_MODEL, body.query, body.context, body.thread_id),
                                 media_type="text/event-stream", headers={"Cache-Control": "no-cache"})
    graph = app.state.graph
    claim_thread(body.thread_id)
    try:
        paused = rg.pending_questions(graph, {"configurable": {"thread_id": body.thread_id}})
    except Exception:
        release_thread(body.thread_id)
        raise
    payload = rg.Command(resume=body.query) if paused else {"request": body.query}
    return RecommendationStream(
        stream_recommendation(graph, payload, body.thread_id),
        body.thread_id,
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )


@app.get("/ai/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8001")))
