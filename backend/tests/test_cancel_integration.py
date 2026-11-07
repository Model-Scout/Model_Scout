"""Cancel and retry across both real servers: backend, ai/api.py and LangGraph talk over HTTP.

Only the node bodies are slow stubs. A backend-only test cannot show this: the backend closing its connection
does not stop the node the AI is running.
"""
import importlib.util
import socket
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch
from uuid import uuid4

import httpx
import pytest
import uvicorn

pytest.importorskip("langgraph")
from langgraph.checkpoint.memory import InMemorySaver

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "ai"))
from backend.app import main as api
from backend.app.rate_limit import RateLimiter
from test_v2 import Store

NODE_SECONDS = 0.6


def load_ai():
    spec = importlib.util.spec_from_file_location("ai_api_integration", ROOT / "ai" / "api.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # pydantic resolves RecommendRequest through it
    spec.loader.exec_module(module)
    return module


class Runs:
    """Records which node each run enters, and any moment two runs are inside a node together."""

    def __init__(self):
        self.lock = threading.Lock()
        self.active = {}
        self.entered = []
        self.overlaps = []

    def node(self, name, out, seconds=NODE_SECONDS):
        def run(state):
            who = state["request"]
            with self.lock:
                self.overlaps += [(name, who, other) for other in self.active if other != who]
                self.active[who] = name
                self.entered.append((who, name))
            time.sleep(seconds)
            with self.lock:
                self.active.pop(who, None)
            return out(who)
        return run


def build_graph(ai, runs):
    need = {"task": "retrieval", "purpose_ko": "검색"}
    limits = {"commercial_only": False, "gpu_memory_gb": None, "min_context_length": None}
    plan = {"needs": [need], "constraints": limits, "clarifying_questions": []}
    return ai.rg.build_graph({
        "decompose": runs.node("decompose", lambda who: {"plan": {**plan, "summary_ko": who}}, seconds=.05),
        "clarify": ai.rg.clarify,
        "search_models": runs.node("search_models", lambda who: {"models": [{"need": need, "models": [{"model_id": "org/m"}]}]}),
        "search_datasets": runs.node("search_datasets", lambda who: {"datasets": {}}),
        "assess": runs.node("assess", lambda who: {"assessment": {}}, seconds=.05),
        "explain": runs.node("explain", lambda who: {"answer": f"answer-of-{who}"}, seconds=.05),
    }, checkpointer=InMemorySaver())


def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@contextmanager
def serving(app):
    # shortcut: creating the event loop in a thread can fail with WinError 10014 here, so start is retried;
    # drop the loop if CI on Linux is the only place this runs.
    for _ in range(20):
        port = free_port()
        server = uvicorn.Server(uvicorn.Config(app, port=port, log_level="warning", lifespan="off"))
        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()
        while thread.is_alive() and not server.started:
            time.sleep(.02)
        if server.started:
            break
    assert server.started, "server did not start"
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.should_exit = True
        thread.join(10)


def post_until_accepted(url, body, headers):
    """A person retrying after cancel: 409 while the group is busy, then the full answer."""
    deadline = time.time() + 20
    while time.time() < deadline:
        with httpx.stream("POST", url, json=body, headers=headers, timeout=30) as response:
            if response.status_code == 200:
                return list(api.parse_sse(response.iter_lines()))
            assert response.status_code == 409
        time.sleep(.1)
    raise AssertionError("retry was never accepted")


def test_cancel_during_slow_node_then_retry_same_group():
    ai, runs = load_ai(), Runs()
    graph = build_graph(ai, runs)
    ai.app.state.graph, ai.app.state.pool = graph, None
    headers = {"X-Session-Id": str(uuid4())}
    started, stream = [], ai.stream_recommendation

    def tracked(*args):
        started.append(stream(*args))
        return started[-1]

    with serving(ai.app) as ai_url, serving(api.app) as backend_url, patch.object(ai, "stream_recommendation", tracked), \
            patch.object(api, "AI_URL", ai_url), patch.object(api, "limiter", RateLimiter(1000, 100000)):
        api.app.state.pool = Store()
        try:
            url = f"{backend_url}/api/chat"
            with httpx.stream("POST", url, json={"query": "RUN1"}, headers=headers, timeout=30) as response:
                group_id = response.headers["x-group-id"]
                for line in response.iter_lines():
                    if "모델 검색" in line:  # search_models is running now
                        break
            events = post_until_accepted(url, {"query": "RUN2", "group_id": group_id}, headers)
        finally:
            api.app.state.pool = None
        assert events[-1][0] == "done" and events[-1][1]["type"] == "answer"
        assert runs.overlaps == []
        assert not {"assess", "explain"} & {node for who, node in runs.entered if who == "RUN1"}
        deadline = time.time() + 5  # the client sees done just before the servers finish cleaning up
        while (api.active_groups or ai.running_threads) and time.time() < deadline:
            time.sleep(.02)
        assert not api.active_groups and not ai.running_threads
        assert len(started) == 2 and all(run.gi_frame is None for run in started)  # Closed, not left to the GC.
    state = graph.get_state({"configurable": {"thread_id": group_id}})
    assert state.values["answer"] == "answer-of-RUN2"  # The cancelled run did not write over the retry.


def test_retry_gives_up_when_the_old_run_does_not_stop():
    ai = load_ai()
    ai.running_threads.add("t")
    with patch.object(ai, "CANCEL_WAIT", .01), pytest.raises(ai.HTTPException) as caught:
        ai.claim_thread("t")
    assert caught.value.status_code == 409
    ai.release_thread("t")
    ai.claim_thread("t")
    assert "t" in ai.running_threads
