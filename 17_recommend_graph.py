"""17 - fixed LangGraph workflow: project idea -> models per need -> compatible datasets.

    decompose (LLM) -> search_models (Supabase RPC, 09) -> search_datasets (hypergraph) -> explain (LLM)

The path is the same for every project, so the LLM does not choose tools here; it only
splits the idea into needs (taxonomy task keys) and writes the final answer from the
retrieved rows. Same input -> same retrieval, which keeps the golden-set evaluation honest.
Free-form follow-ups ("이 데이터셋 라이선스는?") stay with the tool-calling agent in 10.

Multi-turn: with --thread, LangGraph's PostgresSaver keeps each conversation in Supabase
(schema `langgraph`, outside `public` and the Data API). A later turn ("상업용만", "GPU 8GB야")
revises the previous plan instead of starting over. The plan is a Pydantic model, so an LLM
answer with an off-taxonomy task or a malformed constraint fails validation, not retrieval.

    python 17_recommend_graph.py "따릉이 경로 추천 서비스를 만들고 싶어" --thread demo
    python 17_recommend_graph.py "상업용으로만 다시 추천해줘" --thread demo
    python 17_recommend_graph.py "..." --json      # full state instead of the answer
    python 17_recommend_graph.py "..." --memory    # in-process checkpointer, no database
"""
from __future__ import annotations

import argparse
import functools
import importlib.util
import json
import logging
import operator
import os
import time
import sys
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from pathlib import Path
from typing import Annotated, Any, Literal, Optional, TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field

from hypergraph_search import concepts_from_terms, datasets_for_model, embed_query, load_graph, rank_datasets
from taxonomy import load_taxonomy, normalize

ROOT = Path(__file__).resolve().parent
LLM_MODEL = os.getenv("RECOMMEND_LLM_MODEL", "gpt-4.1-mini")
# Primary task tags that exist in the model corpus; search_models can only filter on these.
MODEL_HF_TASKS = ("text-generation", "image-text-to-text", "sentence-similarity", "translation",
                  "automatic-speech-recognition", "feature-extraction", "text-classification",
                  "question-answering", "summarization")
# Retrieval models in the HF corpus are embedding models; there is no "retrieval" task tag.
MODEL_TASK_FALLBACK = {"retrieval": "embedding"}
MODELS_PER_NEED = 3
DATASETS_PER_MODEL = 5
PROJECT_DATASETS = 6
# HF data trains/evaluates models (ranked with the needs' tasks); portal data is what the app serves.
PROJECT_POOL = 30
MAX_NEEDS = 4
# Earlier turns given to the planner and the writer; older ones only cost tokens.
HISTORY_TURNS = 4
CHECKPOINT_SCHEMA = "langgraph"

TaskKey = Literal[tuple(load_taxonomy()["facets"]["task"]["values"])]


class Need(BaseModel):
    task: TaskKey
    purpose_ko: str = Field(description="one Korean sentence on what this model does in the project")
    model_query: str = Field(description="search query, Korean and English keywords mixed")


class Constraints(BaseModel):
    commercial_only: bool
    max_parameter_count_billion: Optional[float]
    min_context_length: Optional[int]


class ProjectPlan(BaseModel):
    summary_ko: str
    needs: list[Need]
    constraints: Constraints
    dataset_terms: list[str]
    dataset_query: str


class State(TypedDict, total=False):
    request: str
    plan: dict  # ProjectPlan.model_dump(): checkpoints stay plain JSON
    models: list
    datasets: dict
    answer: str
    turns: Annotated[list, operator.add]  # [{request, answer}], appended once per turn


def ttl_cache(seconds, maxsize=512):
    """Memoize JSON-serializable results for a while: model search hits Supabase, which the CI
    refreshes daily, so a 10-minute window is safe. Values are stored as JSON so callers can
    never mutate a cached result."""
    def decorate(fn):
        store = {}

        @functools.wraps(fn)
        def wrapper(*args):
            hit = store.get(args)
            if hit and time.time() - hit[0] < seconds:
                return json.loads(hit[1])
            value = fn(*args)
            if len(store) >= maxsize:
                store.pop(next(iter(store)))
            store[args] = (time.time(), json.dumps(value, ensure_ascii=False))
            return value
        return wrapper
    return decorate


@functools.lru_cache(maxsize=1)
def _load_09():
    spec = importlib.util.spec_from_file_location("model_scout_mcp", ROOT / "09_model_scout_mcp_readonly.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return module


def _openai():
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(ROOT / ".env")
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def hf_tags(task_key):
    """Taxonomy task -> the corpus' HF task tags; [] when none fit (reranking: found by query)."""
    task_key = MODEL_TASK_FALLBACK.get(task_key, task_key)
    return [tag for tag in MODEL_HF_TASKS if normalize("task", tag) == task_key]


DECOMPOSE_PROMPT = f"""You plan model and data choices for a Korean AI project idea.
needs: 1-{MAX_NEEDS} distinct model roles the project needs, most important first. task is a taxonomy key.
  purpose_ko: one Korean sentence on what that model does in this project.
  model_query: a search query for that model, Korean and English keywords mixed (e.g. "한국어 문서 임베딩 embedding retrieval").
constraints: only what the user explicitly said; otherwise false/null. Do not infer limits from the idea itself.
  commercial_only: true only if they mention 상업/수익/서비스 출시/commercial.
  max_parameter_count_billion: only for a stated GPU/memory limit (24GB GPU ~ 8, 16GB ~ 4, 8GB ~ 2), else null.
  min_context_length: only for stated long inputs (긴 문서, 계약서 전체 등), else null.
dataset_terms: 1-5 short words for the project's data domain, input length and, if the user named one, the region
  (e.g. 교통, 따릉이, 서울, 장문, legal). Keep proper nouns as written; they are matched against dataset titles.
dataset_query: one Korean sentence describing the data the project needs.
When PREVIOUS_PLAN is given, the user is refining it: return the whole updated plan, changing only
what the new message asks for (e.g. "상업용만" sets commercial_only; "GPU 8GB" sets the size limit)."""

EXPLAIN_PROMPT = """You are Model Scout. The client already shows every retrieved model and dataset as
cards, so write a short Korean markdown briefing (no JSON, no code blocks, about 250-400 words) using ONLY the JSON
given: for each need, the top model in one line with why it fits (task, context length, license) and the
alternatives by id only; then the 2-3 most useful datasets per need, "프로젝트 학습·평가 데이터" (project_training,
top 3) and "서비스 데이터 (공공데이터)" (service_data, top 3: 서울 열린데이터광장 / 공공데이터포털 sources the app
calls at runtime), each with a few-word reason. Write ids exactly as given; copy license and context_length
verbatim; never invent ids, numbers, or licenses; never call an 'unknown' license commercial. If a list is empty,
say so and what to search instead. End with one line of caveats (license 'unknown', '?' = weak link)."""


@ttl_cache(seconds=24 * 3600)
def _first_plan(request):
    """A first-turn plan depends only on the request (temperature 0), so it is cached."""
    return _parse_plan(request)


def _parse_plan(user):
    response = _openai().chat.completions.parse(
        model=LLM_MODEL, temperature=0, max_tokens=800, response_format=ProjectPlan,
        messages=[{"role": "system", "content": DECOMPOSE_PROMPT}, {"role": "user", "content": user}])
    plan = response.choices[0].message.parsed
    if plan is None:
        raise ValueError(f"planner refused: {response.choices[0].message.refusal}")
    plan.needs = plan.needs[:MAX_NEEDS]
    return plan.model_dump()


def decompose(state: State) -> State:
    if not state.get("plan"):
        return {"plan": _first_plan(" ".join(state["request"].split()))}
    history = "\n".join(f"- {t['request']}" for t in (state.get("turns") or [])[-HISTORY_TURNS:])
    return {"plan": _parse_plan(f"EARLIER_REQUESTS:\n{history}\n\nPREVIOUS_PLAN:\n"
                                f"{json.dumps(state['plan'], ensure_ascii=False)}\n\nNEW_MESSAGE:\n{state['request']}")}


def _compact_model(row):
    meta = row.get("filter_metadata") or {}
    return {"model_id": row["model_id"], "rank_score": row["ranking"]["rank_score"],
            "task": (row.get("task") or {}).get("primary"), "license": meta.get("license") or "unknown",
            "commercial_use": normalize("commercial_use", meta.get("license")),
            "context_length": meta.get("context_length"), "parameters_b": meta.get("parameter_count_billion"),
            "url": row.get("model_url")}


@ttl_cache(seconds=600)
def _model_rows(query, task_filters, max_params, min_context):
    out = _load_09().search_models(query, match_count=MODELS_PER_NEED * 2, task_filters=list(task_filters) or None,
                                   korean_required=True, max_parameter_count_billion=max_params,
                                   min_context_length=min_context)
    return [_compact_model(r) for r in out["results"]]


def search_models(state: State) -> State:
    constraints = state["plan"]["constraints"]

    def one(need):
        rows = _model_rows(need["model_query"], tuple(hf_tags(need["task"])),
                           constraints["max_parameter_count_billion"], constraints["min_context_length"])
        if constraints["commercial_only"]:
            rows = [r for r in rows if r["commercial_use"] == "commercial"]
        return {"need": need, "models": rows[:MODELS_PER_NEED]}

    # Needs are independent searches (one DB round trip each); run them side by side.
    with ThreadPoolExecutor(max_workers=MAX_NEEDS) as pool:
        return {"models": list(pool.map(one, state["plan"]["needs"]))}


def _compact_dataset(row):
    return {k: row[k] for k in ("dataset", "title", "source", "score", "reasons", "downloads", "url", "summary_ko")}


def search_datasets(state: State) -> State:
    entities = load_graph()[0]
    plan = state["plan"]
    commercial = plan["constraints"]["commercial_only"]
    # The top model per need that the hypergraph knows; Supabase can be ahead of the local graph.
    top_models = [next((m["model_id"] for m in group["models"] if f"model:{m['model_id']}" in entities), None)
                  for group in state["models"]]
    top_models = list(dict.fromkeys(m for m in top_models if m))
    terms = plan["dataset_terms"] + [need["task"] for need in plan["needs"]]

    with ThreadPoolExecutor(max_workers=len(top_models) + 2) as pool:
        vector = pool.submit(embed_query, plan["dataset_query"])
        per_model_jobs = {m: pool.submit(datasets_for_model, m, commercial_only=commercial, limit=DATASETS_PER_MODEL)
                          for m in top_models}
        query_vector = vector.result()
        project_job = pool.submit(rank_datasets, concepts_from_terms(terms), query_vector=query_vector,
                                  commercial_only=commercial, limit=PROJECT_POOL, keywords=plan["dataset_terms"])
        # Service data is matched on the project's domain alone; model tasks say nothing about it.
        service_job = pool.submit(rank_datasets, concepts_from_terms(plan["dataset_terms"]), query_vector=query_vector,
                                  commercial_only=commercial, roles=["service"], limit=PROJECT_DATASETS,
                                  keywords=plan["dataset_terms"])
        per_model = {m: [_compact_dataset(r) for r in job.result()] for m, job in per_model_jobs.items()}
        training = [_compact_dataset(r) for r in project_job.result() if r["source"] in ("huggingface", "kaggle")]
        service = [_compact_dataset(r) for r in service_job.result()]
    return {"datasets": {"per_model": per_model, "project_training": training[:PROJECT_DATASETS], "service_data": service}}


def explain(state: State) -> State:
    payload = {k: state[k] for k in ("request", "plan", "models", "datasets")}
    payload["earlier_requests"] = [t["request"] for t in (state.get("turns") or [])[-HISTORY_TURNS:]]
    from langgraph.config import get_stream_writer

    # Tokens go out as they arrive (stream_mode="custom"), so a web client shows the answer while
    # it is still being written; the full text is also kept in state for the checkpoint.
    write, parts = get_stream_writer(), []
    stream = _openai().chat.completions.create(
        model=LLM_MODEL, temperature=0, max_tokens=900, stream=True,
        messages=[{"role": "system", "content": EXPLAIN_PROMPT},
                  {"role": "user", "content": json.dumps(payload, ensure_ascii=False)}])
    for chunk in stream:
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            parts.append(delta)
            write({"token": delta})
    answer = "".join(parts)
    return {"answer": answer, "turns": [{"request": state["request"], "answer": answer}]}


def build_graph(nodes=None, checkpointer=None):
    nodes = nodes or {"decompose": decompose, "search_models": search_models,
                      "search_datasets": search_datasets, "explain": explain}
    graph = StateGraph(State)
    for name, fn in nodes.items():
        graph.add_node(name, fn)
    graph.add_edge(START, "decompose")
    graph.add_edge("decompose", "search_models")
    graph.add_edge("search_models", "search_datasets")
    graph.add_edge("search_datasets", "explain")
    graph.add_edge("explain", END)
    return graph.compile(checkpointer=checkpointer)


def supabase_conninfo():
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    env = os.environ
    # Session-mode pooler (port 5432) keeps prepared statements working for PostgresSaver.
    return (f"host={env['SUPABASE_DB_HOST']} port={env['SUPABASE_DB_PORT']} dbname={env['SUPABASE_DB_NAME']} "
            f"user={env['SUPABASE_DB_USER']} password={env['SUPABASE_PASSWORD']} sslmode=require "
            f"options='-c search_path={CHECKPOINT_SCHEMA}'")


@contextmanager
def postgres_checkpointer():
    """PostgresSaver on Supabase; its tables live in their own schema, created on first use."""
    import psycopg
    from langgraph.checkpoint.postgres import PostgresSaver

    conninfo = supabase_conninfo()
    with psycopg.connect(conninfo, autocommit=True) as conn:
        conn.execute(f"create schema if not exists {CHECKPOINT_SCHEMA}")
    with PostgresSaver.from_conn_string(conninfo) as saver:
        saver.setup()  # idempotent migrations
        # Conversations are private: no Data API role may read them (the owner role bypasses RLS).
        with saver.conn.cursor() as cur:
            cur.execute(f"revoke all on schema {CHECKPOINT_SCHEMA} from anon, authenticated")
            for table in ("checkpoints", "checkpoint_blobs", "checkpoint_writes", "checkpoint_migrations"):
                cur.execute(f"alter table {CHECKPOINT_SCHEMA}.{table} enable row level security")
        yield saver


def run(request: str, thread_id: Optional[str] = None, checkpointer=None) -> dict[str, Any]:
    graph = build_graph(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": thread_id}} if thread_id else None
    state: dict[str, Any] = {"request": request}
    for update in graph.stream({"request": request}, config, stream_mode="updates"):
        for node, values in update.items():
            print(f"[graph] {node} done", file=sys.stderr, flush=True)
            state.update(values)
    # With a thread, the checkpoint holds the whole conversation (plan, turns) across runs.
    return graph.get_state(config).values if config else state


def self_check():
    assert set(hf_tags("embedding")) == {"sentence-similarity", "feature-extraction"}, hf_tags("embedding")
    assert hf_tags("generation") == ["text-generation"] and hf_tags("reranking") == []
    assert hf_tags("retrieval") == hf_tags("embedding")
    from pydantic import ValidationError
    from langgraph.checkpoint.memory import InMemorySaver

    plan = {"summary_ko": "s", "needs": [{"task": "embedding", "purpose_ko": "p", "model_query": "q"}],
            "constraints": {"commercial_only": False, "max_parameter_count_billion": None, "min_context_length": None},
            "dataset_terms": ["교통"], "dataset_query": "q"}
    assert ProjectPlan.model_validate(plan).needs[0].task == "embedding"
    try:
        ProjectPlan.model_validate({**plan, "needs": [{"task": "dancing", "purpose_ko": "p", "model_query": "q"}]})
        raise AssertionError("off-taxonomy task accepted")
    except ValidationError:
        pass
    order = []
    stub = lambda name, out: (lambda state: (order.append(name), out)[1])
    graph = build_graph({"decompose": stub("decompose", {"plan": {}}), "search_models": stub("search_models", {"models": []}),
                         "search_datasets": stub("search_datasets", {"datasets": {}}), "explain": stub("explain", {"answer": "ok"})})
    assert graph.invoke({"request": "x"})["answer"] == "ok"
    assert order == ["decompose", "search_models", "search_datasets", "explain"], order
    # Multi-turn: turns accumulate per thread, and the second turn's planner sees the first plan.
    seen = []
    def planner(state):
        seen.append(state.get("plan"))
        return {"plan": {"n": len(seen)}}
    def writer(state):
        return {"answer": f"a{len(seen)}", "turns": [{"request": state["request"], "answer": f"a{len(seen)}"}]}
    noop = lambda state: {}
    memory = build_graph({"decompose": planner, "search_models": noop, "search_datasets": noop, "explain": writer},
                         checkpointer=InMemorySaver())
    config = {"configurable": {"thread_id": "t"}}
    memory.invoke({"request": "first"}, config)
    final = memory.invoke({"request": "second"}, config)
    assert seen == [None, {"n": 1}], seen
    assert [t["request"] for t in final["turns"]] == ["first", "second"], final["turns"]
    print("17_recommend_graph ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("request", nargs="?")
    parser.add_argument("--json", action="store_true", help="print the full state")
    parser.add_argument("--thread", help="conversation id; turns persist in Supabase (PostgresSaver)")
    parser.add_argument("--memory", action="store_true", help="keep --thread in process memory instead")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check or not args.request:
        return self_check()
    logging.getLogger("httpx").setLevel(logging.WARNING)
    if args.thread and not args.memory:
        with postgres_checkpointer() as saver:
            state = run(args.request, args.thread, saver)
    else:
        from langgraph.checkpoint.memory import InMemorySaver

        state = run(args.request, args.thread, InMemorySaver() if args.thread else None)
    print(json.dumps(state, ensure_ascii=False, indent=2) if args.json else state["answer"])


if __name__ == "__main__":
    main()
