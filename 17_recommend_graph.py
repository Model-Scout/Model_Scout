"""17 - fixed LangGraph workflow: project idea -> models per need -> compatible datasets.

    decompose (LLM) -> search_models (Supabase RPC, 09) -> search_datasets (hypergraph) -> explain (LLM)

The path is the same for every project, so the LLM does not choose tools here; it only
splits the idea into needs (taxonomy task keys) and writes the final answer from the
retrieved rows. Same input -> same retrieval, which keeps the golden-set evaluation honest.
Free-form follow-ups ("이 데이터셋 라이선스는?") stay with the tool-calling agent in 10.

    python 17_recommend_graph.py "따릉이 경로 추천 서비스를 만들고 싶어"
    python 17_recommend_graph.py "..." --json      # full state instead of the answer
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, TypedDict

from langgraph.graph import END, START, StateGraph

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


class State(TypedDict, total=False):
    request: str
    plan: dict
    models: list
    datasets: dict
    answer: str


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


def plan_schema():
    nullable = lambda kind: {"type": [kind, "null"]}
    need = {"type": "object", "additionalProperties": False, "required": ["task", "purpose_ko", "model_query"],
            "properties": {"task": {"type": "string", "enum": list(load_taxonomy()["facets"]["task"]["values"])},
                           "purpose_ko": {"type": "string"}, "model_query": {"type": "string"}}}
    constraints = {"type": "object", "additionalProperties": False,
                   "required": ["commercial_only", "max_parameter_count_billion", "min_context_length"],
                   "properties": {"commercial_only": {"type": "boolean"},
                                  "max_parameter_count_billion": nullable("number"),
                                  "min_context_length": nullable("integer")}}
    return {"type": "object", "additionalProperties": False,
            "required": ["summary_ko", "needs", "constraints", "dataset_terms", "dataset_query"],
            "properties": {"summary_ko": {"type": "string"}, "needs": {"type": "array", "items": need},
                           "constraints": constraints, "dataset_terms": {"type": "array", "items": {"type": "string"}},
                           "dataset_query": {"type": "string"}}}


DECOMPOSE_PROMPT = f"""You plan model and data choices for a Korean AI project idea.
needs: 1-{MAX_NEEDS} distinct model roles the project needs, most important first. task is a taxonomy key.
  purpose_ko: one Korean sentence on what that model does in this project.
  model_query: a search query for that model, Korean and English keywords mixed (e.g. "한국어 문서 임베딩 embedding retrieval").
constraints: only what the user explicitly said; otherwise false/null. Do not infer limits from the idea itself.
  commercial_only: true only if they mention 상업/수익/서비스 출시/commercial.
  max_parameter_count_billion: only for a stated GPU/memory limit (24GB GPU ~ 8, 16GB ~ 4), else null.
  min_context_length: only for stated long inputs (긴 문서, 계약서 전체 등), else null.
dataset_terms: 1-4 short words for the project's data domain and input length, Korean or English (e.g. 교통, 위치, 장문, legal).
dataset_query: one Korean sentence describing the data the project needs."""

EXPLAIN_PROMPT = """You are Model Scout. Answer in Korean markdown (headings and bullets, never JSON or code blocks)
using ONLY the JSON given: the plan, models
retrieved per need, datasets per model, project training datasets, and service data. For each need: the top
model with why it fits (task, context length, license), up to two alternatives, and its datasets with the
reasons listed. Then "프로젝트 학습·평가 데이터" (project_training) and "서비스 데이터 (공공데이터)" (service_data:
서울 열린데이터광장 / 공공데이터포털 sources the app would call or load at runtime). Write model and dataset ids exactly as given. If a list is empty, say so
and suggest what to search instead. Copy license and context_length values verbatim; never invent ids,
numbers, or licenses, and never call an 'unknown' license commercial. End with one line of caveats
(license 'unknown', 신뢰도 낮은 연결 marked '?')."""


def decompose(state: State) -> State:
    response = _openai().chat.completions.create(
        model=LLM_MODEL, temperature=0, max_tokens=800,
        messages=[{"role": "system", "content": DECOMPOSE_PROMPT}, {"role": "user", "content": state["request"]}],
        response_format={"type": "json_schema", "json_schema": {"name": "project_plan", "strict": True, "schema": plan_schema()}})
    plan = json.loads(response.choices[0].message.content)
    plan["needs"] = plan["needs"][:MAX_NEEDS]
    return {"plan": plan}


def _compact_model(row):
    meta = row.get("filter_metadata") or {}
    return {"model_id": row["model_id"], "rank_score": row["ranking"]["rank_score"],
            "task": (row.get("task") or {}).get("primary"), "license": meta.get("license") or "unknown",
            "commercial_use": normalize("commercial_use", meta.get("license")),
            "context_length": meta.get("context_length"), "parameters_b": meta.get("parameter_count_billion"),
            "url": row.get("model_url")}


def search_models(state: State) -> State:
    tools, constraints = _load_09(), state["plan"]["constraints"]
    found = []
    for need in state["plan"]["needs"]:
        out = tools.search_models(need["model_query"], match_count=MODELS_PER_NEED * 2,
                                  task_filters=hf_tags(need["task"]) or None, korean_required=True,
                                  max_parameter_count_billion=constraints["max_parameter_count_billion"],
                                  min_context_length=constraints["min_context_length"])
        rows = [_compact_model(r) for r in out["results"]]
        if constraints["commercial_only"]:
            rows = [r for r in rows if r["commercial_use"] == "commercial"]
        found.append({"need": need, "models": rows[:MODELS_PER_NEED]})
    return {"models": found}


def _compact_dataset(row):
    return {k: row[k] for k in ("dataset", "title", "source", "score", "reasons", "downloads", "url", "summary_ko")}


def search_datasets(state: State) -> State:
    entities = load_graph()[0]
    commercial = state["plan"]["constraints"]["commercial_only"]
    per_model = {}
    for group in state["models"]:
        # The top model that the hypergraph knows; Supabase can be ahead of the local graph.
        for model in group["models"]:
            if f"model:{model['model_id']}" in entities:
                rows = datasets_for_model(model["model_id"], commercial_only=commercial, limit=DATASETS_PER_MODEL)
                per_model[model["model_id"]] = [_compact_dataset(r) for r in rows]
                break
    plan = state["plan"]
    terms = plan["dataset_terms"] + [need["task"] for need in plan["needs"]]
    vector = embed_query(plan["dataset_query"])
    pool = rank_datasets(concepts_from_terms(terms), query_vector=vector, commercial_only=commercial, limit=PROJECT_POOL)
    training = [_compact_dataset(r) for r in pool if r["source"] == "huggingface"][:PROJECT_DATASETS]
    # Service data is matched on the project's domain alone; model tasks say nothing about it.
    served = rank_datasets(concepts_from_terms(plan["dataset_terms"]), query_vector=vector, commercial_only=commercial,
                           roles=["service"], limit=PROJECT_DATASETS)
    service = [_compact_dataset(r) for r in served]
    return {"datasets": {"per_model": per_model, "project_training": training, "service_data": service}}


def explain(state: State) -> State:
    payload = {k: state[k] for k in ("request", "plan", "models", "datasets")}
    response = _openai().chat.completions.create(
        model=LLM_MODEL, temperature=0, max_tokens=1800,
        messages=[{"role": "system", "content": EXPLAIN_PROMPT},
                  {"role": "user", "content": json.dumps(payload, ensure_ascii=False)}])
    return {"answer": response.choices[0].message.content}


def build_graph(nodes=None):
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
    return graph.compile()


def run(request: str) -> dict[str, Any]:
    state: dict[str, Any] = {"request": request}
    for update in build_graph().stream({"request": request}, stream_mode="updates"):
        for node, values in update.items():
            print(f"[graph] {node} done", file=sys.stderr, flush=True)
            state.update(values)
    return state


def self_check():
    assert set(hf_tags("embedding")) == {"sentence-similarity", "feature-extraction"}, hf_tags("embedding")
    assert hf_tags("generation") == ["text-generation"] and hf_tags("reranking") == []
    assert hf_tags("retrieval") == hf_tags("embedding")
    assert plan_schema()["properties"]["needs"]["items"]["properties"]["task"]["enum"][0] == "retrieval"
    order = []
    stub = lambda name, out: (lambda state: (order.append(name), out)[1])
    graph = build_graph({"decompose": stub("decompose", {"plan": {}}), "search_models": stub("search_models", {"models": []}),
                         "search_datasets": stub("search_datasets", {"datasets": {}}), "explain": stub("explain", {"answer": "ok"})})
    assert graph.invoke({"request": "x"})["answer"] == "ok"
    assert order == ["decompose", "search_models", "search_datasets", "explain"], order
    print("17_recommend_graph ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("request", nargs="?")
    parser.add_argument("--json", action="store_true", help="print the full state")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check or not args.request:
        return self_check()
    logging.getLogger("httpx").setLevel(logging.WARNING)
    state = run(args.request)
    print(json.dumps(state, ensure_ascii=False, indent=2) if args.json else state["answer"])


if __name__ == "__main__":
    main()
