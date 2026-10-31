"""21 - HTTP API for the recommendation graph (17), streamed with Server-Sent Events.

The full answer takes ~10-25 s (two LLM calls and the model search), so the API streams each
step as it finishes instead of waiting for the end:

    event: status    {"node": "decompose", "elapsed": 2.4}        after every graph node
    event: plan      ProjectPlan                                     needs + constraints
    event: models    [{need, models}]                                per-need model ranking
    event: datasets  {per_model, project_training, service_data}
    event: token     {"text": "..."}                                 answer, as it is written
    event: done      {"thread_id": "...", "elapsed": 14.1}
    event: error     {"message": "..."}

Conversations persist in Supabase (PostgresSaver, schema langgraph) by thread_id, so a follow-up
("상업용만 다시") revises the previous plan. Without database settings it falls back to memory.

    python 21_api_server.py                         # HOST / PORT env, default 127.0.0.1:8000
    curl -N -X POST localhost:8000/api/recommend -H 'content-type: application/json' \\
         -d '{"message": "따릉이 경로 추천 서비스를 만들고 싶어"}'
"""
from __future__ import annotations

import importlib.util
import json
import logging
import os
import sys
import time
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
logging.getLogger("httpx").setLevel(logging.WARNING)


def _load_graph_module():
    spec = importlib.util.spec_from_file_location("recommend_graph", ROOT / "17_recommend_graph.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["recommend_graph"] = module  # LangGraph resolves the State annotations through it
    spec.loader.exec_module(module)
    return module


rg = _load_graph_module()


class RecommendRequest(BaseModel):
    message: str = Field(min_length=2, max_length=2000)
    thread_id: Optional[str] = Field(default=None, pattern=r"^[A-Za-z0-9_.:-]{1,80}$")


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
    pool = ConnectionPool(rg.supabase_conninfo(), min_size=1, max_size=int(os.getenv("CHECKPOINT_POOL_SIZE", "5")),
                          kwargs={"autocommit": True, "prepare_threshold": 0, "row_factory": dict_row}, open=True)
    return PostgresSaver(pool), pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Warm every cache once so the first request does not pay for loading the graph files.
    import hypergraph_search

    hypergraph_search.load_graph()
    rg._load_09()
    try:  # first query after a restart or DB rewrite reads cold pages; pay that here, not per user
        rg._load_09().search_models("한국어 임베딩 모델", match_count=1)
    except Exception:
        logging.exception("warm-up search failed; continuing")
    saver, pool = _checkpointer()
    app.state.graph, app.state.pool = rg.build_graph(checkpointer=saver), pool
    if pool is not None:
        with pool.connection() as conn:
            logging.info("pruned %s idle conversations", rg.prune_idle_threads(conn, days=int(os.getenv("THREAD_TTL_DAYS", "30"))))
    yield
    if pool is not None:
        pool.close()


app = FastAPI(title="Model Scout API", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
                   allow_methods=["GET", "POST"], allow_headers=["*"])


def sse(event, data):
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


NODE_EVENTS = {"decompose": ("plan", "plan"), "search_models": ("models", "models"),
               "search_datasets": ("datasets", "datasets")}


def stream_recommendation(graph, message, thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    started = time.time()
    try:
        for mode, data in graph.stream({"request": message}, config, stream_mode=["updates", "custom"],
                                       durability="exit"):  # one checkpoint per turn
            if mode == "custom":
                yield sse("token", {"text": data["token"]})
                continue
            for node, values in data.items():
                yield sse("status", {"node": node, "elapsed": round(time.time() - started, 2)})
                if node in NODE_EVENTS:
                    event, key = NODE_EVENTS[node]
                    yield sse(event, values[key])
        if app.state.pool is not None:
            with app.state.pool.connection() as conn:
                rg.prune_thread(conn, thread_id)
        yield sse("done", {"thread_id": thread_id, "elapsed": round(time.time() - started, 2)})
    except Exception as error:  # surfaced to the client; the stream must end with an event
        logging.exception("recommendation failed")
        yield sse("error", {"message": f"{type(error).__name__}: {error}"[:500]})


@app.post("/api/recommend")
def recommend(body: RecommendRequest):
    thread_id = body.thread_id or uuid.uuid4().hex
    return StreamingResponse(stream_recommendation(app.state.graph, body.message, thread_id),
                             media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.get("/api/threads/{thread_id}")
def thread(thread_id: str):
    values = app.state.graph.get_state({"configurable": {"thread_id": thread_id}}).values
    if not values:
        raise HTTPException(404, "unknown thread")
    return {"thread_id": thread_id, "turns": values.get("turns", []), "plan": values.get("plan")}


@app.get("/api/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8000")))
