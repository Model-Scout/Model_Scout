"""17 - fixed LangGraph workflow: project idea -> models per need -> compatible datasets.

    decompose (LLM) -> clarify (interrupt, only when the idea is too vague) -> search_models (Supabase
    RPC, 09; GPU fit per model) -> search_datasets (hypergraph; README evidence per card) -> assess
    (license stack verdict, no LLM) -> explain (LLM)

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
    python 17_recommend_graph.py --compare BM-K/KoSimCSE-roberta intfloat/multilingual-e5-small --gpu 8
"""

from __future__ import annotations

import argparse
import functools
import importlib.util
import json
import logging
import operator
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from pathlib import Path
from typing import Annotated, Any, Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt
from pydantic import BaseModel, Field, model_validator

import project_checks
from hypergraph_search import concepts_from_terms, datasets_for_model, embed_query, load_graph, rank_datasets
from taxonomy import load_taxonomy, normalize

ROOT = Path(__file__).resolve().parent
LLM_MODEL = os.getenv("RECOMMEND_LLM_MODEL", "gpt-4.1-mini")
# Primary task tags that exist in the model corpus; search_models can only filter on these.
MODEL_HF_TASKS = (
    "text-generation",
    "image-text-to-text",
    "sentence-similarity",
    "translation",
    "automatic-speech-recognition",
    "feature-extraction",
    "text-classification",
    "question-answering",
    "summarization",
)
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

# Generated from the taxonomy at import time: pydantic validates against it, mypy cannot see it.
TaskKey = Literal[tuple(load_taxonomy()["facets"]["task"]["values"])]  # type: ignore[valid-type]


class Need(BaseModel):
    task: TaskKey  # type: ignore[valid-type]
    purpose_ko: str = Field(description="one Korean sentence on what this model does in the project")
    model_query: str = Field(description="search query, Korean and English keywords mixed")


# Download formats a user can name; a subset of resolvers/artifacts.FORMATS.
ArtifactFormat = Literal["gguf", "safetensors", "onnx", "mlx"]
# Words that must appear in what the user said before the planner may set a contract constraint.
# The LLM is told the same rules; this keeps a misread from silently narrowing the search.
ARTIFACT_MARKERS = {
    "gguf": ("gguf", "ollama", "llama.cpp", "llama-cpp", "llamacpp"),
    "safetensors": ("safetensors",),
    "onnx": ("onnx",),
    "mlx": ("mlx",),
}
GATED_MARKERS = ("승인 없", "승인없", "신청 없", "신청없", "바로 다운", "바로 내려", "gated", "동의 없")
FILE_SIZE_MARKERS = ("파일", "다운로드", "내려받", "디스크", "file", "download", "disk")


def constraint_defaults() -> dict[str, Any]:
    return {
        "commercial_only": False,
        "gpu_memory_gb": None,
        "max_parameter_count_billion": None,
        "min_context_length": None,
        "required_artifacts": [],
        "max_artifact_gib": None,
        "exclude_gated": False,
    }


class Constraints(BaseModel):
    commercial_only: bool
    gpu_memory_gb: float | None
    max_parameter_count_billion: float | None
    min_context_length: int | None
    required_artifacts: list[ArtifactFormat]
    max_artifact_gib: float | None
    exclude_gated: bool

    @model_validator(mode="before")
    @classmethod
    def fill_missing(cls, value: Any) -> Any:
        # Plans checkpointed before a field existed lack it. Every field stays required in the
        # JSON schema the planner LLM sees; only stored plans get the defaults.
        if isinstance(value, dict):
            return {**constraint_defaults(), **value}
        return value


def constraints_of(plan: dict) -> dict[str, Any]:
    """A stored plan's constraints with defaults for fields added after it was saved."""
    return {**constraint_defaults(), **(plan.get("constraints") or {})}


def explicit_constraints(constraints: dict, said: str, previous: dict | None = None) -> dict[str, Any]:
    """Drop new contract constraints the user did not state. Never adds one.

    A value already in the previous plan is kept: the user stated it in an earlier turn.
    """
    previous = previous or {}
    text = said.casefold()
    out = {**constraint_defaults(), **constraints}
    out["required_artifacts"] = [
        fmt
        for fmt in out["required_artifacts"]
        if fmt in (previous.get("required_artifacts") or []) or any(m in text for m in ARTIFACT_MARKERS.get(fmt, ()))
    ]
    if out["exclude_gated"] and not previous.get("exclude_gated") and not any(m in text for m in GATED_MARKERS):
        out["exclude_gated"] = False
    if (
        out["max_artifact_gib"] is not None
        and out["max_artifact_gib"] != previous.get("max_artifact_gib")
        and not any(m in text for m in FILE_SIZE_MARKERS)
    ):
        out["max_artifact_gib"] = None
    return out


class ProjectPlan(BaseModel):
    summary_ko: str
    needs: list[Need]
    constraints: Constraints
    dataset_terms: list[str]
    dataset_query: str
    clarifying_questions: list[str]


class State(TypedDict, total=False):
    request: str
    plan: dict  # ProjectPlan.model_dump(): checkpoints stay plain JSON
    models: list
    datasets: dict
    assessment: dict
    answer: str
    turns: Annotated[list, operator.add]  # [{request, answer}], appended once per turn


def ttl_cache(seconds, maxsize=512):
    """Memoize JSON-serializable results for a while: model search hits Supabase, which the CI
    refreshes daily, so a 10-minute window is safe. Values are stored as JSON so callers can
    never mutate a cached result."""

    def decorate(fn):
        store: dict[tuple, tuple[float, str]] = {}
        lock = threading.Lock()  # the API serves requests on several threads

        @functools.wraps(fn)
        def wrapper(*args):
            with lock:
                hit = store.get(args)
            if hit and time.time() - hit[0] < seconds:
                return json.loads(hit[1])
            value = fn(*args)
            with lock:
                if len(store) >= maxsize:
                    store.pop(next(iter(store)))
                store[args] = (time.time(), json.dumps(value, ensure_ascii=False))
            return value

        return wrapper

    return decorate


@functools.lru_cache(maxsize=1)
def _load_09():
    spec = importlib.util.spec_from_file_location("model_scout_mcp", ROOT / "09_model_scout_mcp_readonly.py")
    assert spec and spec.loader
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
  model_query: a search query for that model, Korean and English keywords mixed
  (e.g. "한국어 문서 임베딩 embedding retrieval").
constraints: only what the user explicitly said; otherwise false/null. Do not infer limits from the idea itself.
  commercial_only: true only if they mention 상업/수익/서비스 출시/commercial.
  gpu_memory_gb: the GPU memory they state (e.g. "8GB GPU", "RTX 4090" -> 24), else null.
  max_parameter_count_billion: only for an explicit size limit ("3B 이하"), else null. Never derive it from the GPU.
  min_context_length: only for stated long inputs (긴 문서, 계약서 전체 등), else null.
  required_artifacts: file formats they name. "GGUF", "Ollama", "llama.cpp" -> ["gguf"]; "ONNX" -> ["onnx"];
  "MLX" -> ["mlx"]; "safetensors" -> ["safetensors"]. "로컬 실행", "온프레미스", "내 PC" alone set nothing: [].
  max_artifact_gib: only an explicit model file/download size limit ("모델 파일 5GB 이하"), in GB, else null.
  GPU memory is gpu_memory_gb, never this; a file size is not GPU memory.
  exclude_gated: true only if they say 승인 없이/신청 없이/바로 다운로드/gated 제외, else false.
dataset_terms: 1-5 short words for the project's data domain, input length and, if the user named one, the region
  (e.g. 교통, 따릉이, 서울, 장문, legal). Keep proper nouns as written; they are matched against dataset titles.
dataset_query: one Korean sentence describing the data the project needs.
clarifying_questions: up to 3 short Korean questions ONLY when the idea is too vague to choose model roles
  (e.g. "챗봇 만들고 싶어" with no domain or purpose); then also ask about GPU memory and commercial use if unstated.
  If the purpose is clear, return [] even when GPU or license are unstated. Always [] when PREVIOUS_PLAN is given
  or the message already contains "(추가 정보)".
When PREVIOUS_PLAN is given, the user is refining it: return the whole updated plan, changing only
what the new message asks for (e.g. "상업용만" sets commercial_only; "GPU 8GB" sets gpu_memory_gb;
"GGUF로" sets required_artifacts)."""

EXPLAIN_PROMPT = """You are Model Scout. The client already shows every retrieved model and dataset as
cards, so write a short Korean markdown briefing (no JSON, no code blocks, about 250-400 words) using ONLY the JSON
given: for each need, the top model in one line with why it fits (task, context length, license) and the
alternatives by id only; then the 2-3 most useful datasets per need, "프로젝트 학습·평가 데이터" (project_training,
top 3) and "서비스 데이터 (공공데이터)" (service_data, top 3: 서울 열린데이터광장 / 공공데이터포털 sources the app
calls at runtime), each with a few-word reason. If a model has gpu_fit, state its label (e.g. "8GB에서 4bit 양자화하면
돌아감"). Close with "라이선스 판정": assessment.license.label and its reason, verbatim in substance. Write ids exactly
as given; copy license and context_length verbatim; never invent ids, numbers, or licenses; never call an 'unknown'
license commercial. commercial_status (permitted/prohibited/review_required/unknown), when present, is the license
verdict to report. gpu_fit is an estimate from weight sizes, not measured VRAM, and excludes long-input KV cache;
artifact_runnable_gib is a download file size, never GPU memory. If a list is empty, say so and what to search
instead. End with one line of caveats."""


@ttl_cache(seconds=24 * 3600)
def _first_plan(request):
    """A first-turn plan depends only on the request (temperature 0), so it is cached."""
    return _parse_plan(request)


def _parse_plan(user, said=None, previous=None):
    """said: only what the user wrote (the planner input may also hold the previous plan's JSON)."""
    plan = _llm_plan(user)
    plan["constraints"] = explicit_constraints(plan["constraints"], user if said is None else said, previous)
    return plan


def _llm_plan(user):
    response = _openai().chat.completions.parse(
        model=LLM_MODEL,
        temperature=0,
        max_tokens=800,
        response_format=ProjectPlan,
        messages=[{"role": "system", "content": DECOMPOSE_PROMPT}, {"role": "user", "content": user}],
    )
    plan = response.choices[0].message.parsed
    if plan is None:
        raise ValueError(f"planner refused: {response.choices[0].message.refusal}")
    plan.needs = plan.needs[:MAX_NEEDS]
    return plan.model_dump()


def decompose(state: State) -> State:
    if not state.get("plan"):
        return {"plan": _first_plan(" ".join(state["request"].split()))}
    earlier = [t["request"] for t in (state.get("turns") or [])[-HISTORY_TURNS:]]
    history = "\n".join(f"- {request}" for request in earlier)
    return {
        "plan": _parse_plan(
            f"EARLIER_REQUESTS:\n{history}\n\nPREVIOUS_PLAN:\n"
            f"{json.dumps(state['plan'], ensure_ascii=False)}\n\nNEW_MESSAGE:\n{state['request']}",
            said="\n".join([*earlier, state["request"]]),
            previous=constraints_of(state["plan"]),
        )
    }


METADATA_LINE_PREFIXES = ("```", "---", "- ", "base_model", "license", "pipeline_tag", "library_name", "tags")
# Front-matter fragments and the usage note every quantized GGUF repack carries say nothing
# about the model itself.
NOT_EVIDENCE_RE = re.compile(r"(?:library_name|pipeline_tag|base_model)\s*:|how to use GGUF|TheBloke", re.I)


def _model_quote(row):
    """README text backing the model: 09's audit quote, else the Stage 3 summary, else the first
    prose paragraph of its evidence; None when the card is metadata only (shown as such)."""
    candidates = [
        (row.get("audit_evidence") or {}).get("supporting_quote"),
        ((row.get("semantic_metadata") or {}).get("summary") or {}).get("text"),
    ]
    for parent in row.get("evidence_preview") or []:
        candidates += [
            child.get("text") for child in parent.get("children", []) if child.get("content_type") == "paragraph"
        ]
    for text in candidates:
        text = " ".join((text or "").split())
        if len(text) >= 40 and not text.startswith(METADATA_LINE_PREFIXES) and not NOT_EVIDENCE_RE.search(text):
            return text[:240]
    return None


def _compact_model(row):
    meta = row.get("filter_metadata") or {}
    quant = meta.get("quantization") or {}
    status = meta.get("commercial_status")
    return {
        "model_id": row["model_id"],
        "rank_score": row["ranking"]["rank_score"],
        "task": (row.get("task") or {}).get("primary"),
        "license": meta.get("license") or "unknown",
        # Stage 2's contract verdict; None on rows loaded before the contract reingest.
        "commercial_status": status,
        # Kept for API consumers. Derived from commercial_status when the row has one, so the
        # raw license is no longer classified twice with possibly different results.
        "commercial_use": project_checks.COMMERCIAL_STATUS_CLASS.get(status)
        or normalize("commercial_use", meta.get("license")),
        "context_length": meta.get("context_length"),
        "parameters_b": meta.get("parameter_count_billion"),
        "hardware": meta.get("hardware"),
        "quant_bits": quant.get("bits") if quant.get("enabled") else None,
        "gated": meta.get("gated"),
        "artifact_formats": meta.get("artifact_formats"),
        "artifact_runnable_gib": meta.get("artifact_runnable_gib"),
        "artifact_runnable_label": meta.get("artifact_runnable_label"),
        "dtype": meta.get("dtype"),
        "unresolved_filter_fields": meta.get("unresolved_filter_fields") or [],
        "benchmarks": project_checks.compact_benchmarks(row.get("benchmark_metadata")),
        "evidence": _model_quote(row),
        "url": row.get("model_url"),
    }


@ttl_cache(seconds=600)
def _model_rows(
    query,
    task_filters,
    max_params,
    min_context,
    commercial_only,
    required_artifacts,
    max_artifact_gib,
    exclude_gated,
    contract_filters,
):
    """Every search condition is an argument, so each one is part of the TTL cache key.

    contract_filters (MODEL_CONTRACT_FILTERS_ENABLED) decides whether the contract conditions go to
    the RPC as hard filters. Off, the call is the original one and the caller keeps its post-filter.
    """
    contract = (
        {
            "commercial_status_filter": ["permitted"] if commercial_only else None,
            "require_artifact": list(required_artifacts) or None,
            "max_artifact_gib": max_artifact_gib,
            "exclude_gated": exclude_gated,
        }
        if contract_filters
        else {}
    )
    out = _load_09().search_models(
        query,
        match_count=MODELS_PER_NEED * 2,
        task_filters=list(task_filters) or None,
        korean_required=True,
        max_parameter_count_billion=max_params,
        min_context_length=min_context,
        **contract,
    )
    return {
        "rows": [_compact_model(r) for r in out["results"]],
        "contract_filters_applied": bool((out.get("contract_filters") or {}).get("applied")),
    }


def search_models(state: State) -> State:
    constraints = constraints_of(state["plan"])
    gpu = constraints.get("gpu_memory_gb")
    # A GPU limit admits anything that fits at 4-bit; each card then says at which precision.
    size_limits = [
        v
        for v in (constraints["max_parameter_count_billion"], project_checks.max_params_for_gpu(gpu) if gpu else None)
        if v
    ]
    max_params = min(size_limits) if size_limits else None

    contract_filters = _load_09().contract_filters_enabled()

    def one(need):
        found = _model_rows(
            need["model_query"],
            tuple(hf_tags(need["task"])),
            max_params,
            constraints["min_context_length"],
            constraints["commercial_only"],
            tuple(constraints["required_artifacts"]),
            constraints["max_artifact_gib"],
            constraints["exclude_gated"],
            contract_filters,
        )
        rows = found["rows"]
        if constraints["commercial_only"] and not found["contract_filters_applied"]:
            # Before the contract migration: filter the top rows here. The RPC filter (flag on)
            # applies before the top-N cut, so a permitted model ranked below it is not lost.
            rows = [r for r in rows if r["commercial_use"] == "commercial"]
        for row in rows:
            row["gpu_fit"] = project_checks.gpu_fit(
                row["parameters_b"], gpu, row.pop("hardware", None), row["quant_bits"]
            )
        rows = [r for r in rows if not r["gpu_fit"] or r["gpu_fit"]["verdict"] != "too_large"]
        return {"need": need, "models": rows[:MODELS_PER_NEED]}

    # Needs are independent searches (one DB round trip each); run them side by side.
    with ThreadPoolExecutor(max_workers=MAX_NEEDS) as pool:
        return {"models": list(pool.map(one, state["plan"]["needs"]))}


def _compact_dataset(row):
    return {
        k: row[k]
        for k in (
            "dataset",
            "title",
            "source",
            "score",
            "reasons",
            "downloads",
            "url",
            "summary_ko",
            "licenses",
            "evidence",
        )
    }


def search_datasets(state: State) -> State:
    entities = load_graph()[0]
    plan = state["plan"]
    commercial = constraints_of(plan)["commercial_only"]
    # The top model per need that the hypergraph knows; Supabase can be ahead of the local graph.
    top_models = [
        next((m["model_id"] for m in group["models"] if f"model:{m['model_id']}" in entities), None)
        for group in state["models"]
    ]
    top_models = list(dict.fromkeys(m for m in top_models if m))
    terms = plan["dataset_terms"] + [need["task"] for need in plan["needs"]]

    with ThreadPoolExecutor(max_workers=len(top_models) + 2) as pool:
        vector = pool.submit(embed_query, plan["dataset_query"])
        per_model_jobs = {
            m: pool.submit(datasets_for_model, m, commercial_only=commercial, limit=DATASETS_PER_MODEL)
            for m in top_models
        }
        query_vector = vector.result()
        project_job = pool.submit(
            rank_datasets,
            concepts_from_terms(terms),
            query_vector=query_vector,
            commercial_only=commercial,
            limit=PROJECT_POOL,
            keywords=plan["dataset_terms"],
        )
        # Service data is matched on the project's domain alone; model tasks say nothing about it.
        service_job = pool.submit(
            rank_datasets,
            concepts_from_terms(plan["dataset_terms"]),
            query_vector=query_vector,
            commercial_only=commercial,
            roles=["service"],
            limit=PROJECT_DATASETS,
            keywords=plan["dataset_terms"],
        )
        per_model = {m: [_compact_dataset(r) for r in job.result()] for m, job in per_model_jobs.items()}
        training = [_compact_dataset(r) for r in project_job.result() if r["source"] in ("huggingface", "kaggle")]
        service = [_compact_dataset(r) for r in service_job.result()]
    return {
        "datasets": {"per_model": per_model, "project_training": training[:PROJECT_DATASETS], "service_data": service}
    }


def clarify(state: State) -> State:
    """Pause a vague first request (interrupt) until the user answers, then re-plan with it."""
    questions = state["plan"].get("clarifying_questions") or []
    if not questions or state.get("turns"):
        return {}
    answer = interrupt({"questions": questions})
    request = f"{state['request']}\n(추가 정보) {answer}"
    return {"request": request, "plan": _parse_plan(request)}


def assess(state: State) -> State:
    """License verdict for the stack a user would actually build: each need's top model, its top
    training sets, the project's top training sets and the service data the app would call."""
    items = []
    for group in state["models"]:
        if group["models"]:
            top = group["models"][0]
            items.append(
                {
                    "kind": "모델",
                    "id": top["model_id"],
                    "license": top["license"],
                    "commercial_status": top.get("commercial_status"),
                }
            )
    datasets = state["datasets"]
    for rows in datasets["per_model"].values():
        items += [{"kind": "학습 데이터", "id": d["dataset"], "license": d["licenses"]} for d in rows[:2]]
    items += [
        {"kind": "학습 데이터", "id": d["dataset"], "license": d["licenses"]} for d in datasets["project_training"][:3]
    ]
    items += [
        {"kind": "서비스 데이터", "id": d["dataset"], "license": d["licenses"]} for d in datasets["service_data"][:3]
    ]
    seen, unique = set(), []
    for item in items:
        if item["id"] not in seen:
            seen.add(item["id"])
            unique.append(item)
    return {
        "assessment": {
            "license": project_checks.license_verdict(unique),
            "gpu_memory_gb": constraints_of(state["plan"]).get("gpu_memory_gb"),
        }
    }


def explain(state: State) -> State:
    payload = {k: state[k] for k in ("request", "plan", "models", "datasets", "assessment")}
    payload["earlier_requests"] = [t["request"] for t in (state.get("turns") or [])[-HISTORY_TURNS:]]
    from langgraph.config import get_stream_writer

    # Tokens go out as they arrive (stream_mode="custom"), so a web client shows the answer while
    # it is still being written; the full text is also kept in state for the checkpoint.
    write, parts = get_stream_writer(), []
    stream = _openai().chat.completions.create(
        model=LLM_MODEL,
        temperature=0,
        max_tokens=900,
        stream=True,
        messages=[
            {"role": "system", "content": EXPLAIN_PROMPT},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            parts.append(delta)
            write({"token": delta})
    answer = "".join(parts)
    return {"answer": answer, "turns": [{"request": state["request"], "answer": answer}]}


def build_graph(nodes=None, checkpointer=None):
    nodes = nodes or {
        "decompose": decompose,
        "clarify": clarify,
        "search_models": search_models,
        "search_datasets": search_datasets,
        "assess": assess,
        "explain": explain,
    }
    graph = StateGraph(State)
    for name, fn in nodes.items():
        graph.add_node(name, fn)
    order = [START, *nodes, END]
    for source, target in zip(order, order[1:], strict=False):
        graph.add_edge(source, target)
    return graph.compile(checkpointer=checkpointer)


def supabase_conninfo():
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    env = os.environ
    # Session-mode pooler (port 5432) keeps prepared statements working for PostgresSaver.
    return (
        f"host={env['SUPABASE_DB_HOST']} port={env['SUPABASE_DB_PORT']} dbname={env['SUPABASE_DB_NAME']} "
        f"user={env['SUPABASE_DB_USER']} password={env['SUPABASE_PASSWORD']} sslmode=require "
        f"options='-c search_path={CHECKPOINT_SCHEMA}'"
    )


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
        saver_conn: Any = saver.conn  # from_conn_string always yields a single connection
        with saver_conn.cursor() as cur:
            cur.execute(f"revoke all on schema {CHECKPOINT_SCHEMA} from anon, authenticated")
            for table in ("checkpoints", "checkpoint_blobs", "checkpoint_writes", "checkpoint_migrations"):
                cur.execute(f"alter table {CHECKPOINT_SCHEMA}.{table} enable row level security")
        yield saver


PRUNE_SQL = (
    # A thread's latest checkpoint already holds every turn (state.turns), so older checkpoints,
    # their pending writes and blobs no longer referenced by it are dead weight on a 500 MB DB.
    "delete from {s}.checkpoint_writes w where w.thread_id = %(t)s and w.checkpoint_id <> %(c)s",
    "delete from {s}.checkpoints where thread_id = %(t)s and checkpoint_id <> %(c)s",
    "delete from {s}.checkpoint_blobs b where b.thread_id = %(t)s and not exists (select 1 from {s}.checkpoints k "
    "where k.thread_id = %(t)s and k.checkpoint_id = %(c)s "
    "and k.checkpoint->'channel_versions'->>b.channel = b.version)",
)


def prune_thread(conn, thread_id):
    """Keep only the newest checkpoint of one conversation (PostgresSaver tables)."""
    row = conn.execute(
        f"select checkpoint_id from {CHECKPOINT_SCHEMA}.checkpoints where thread_id = %s "
        "and checkpoint_ns = '' order by checkpoint_id desc limit 1",
        (thread_id,),
    ).fetchone()
    if row:
        latest = row["checkpoint_id"] if isinstance(row, dict) else row[0]
        for statement in PRUNE_SQL:
            conn.execute(statement.format(s=CHECKPOINT_SCHEMA), {"t": thread_id, "c": latest})


def prune_idle_threads(conn, days=30):
    """Drop conversations untouched for `days` (checkpoint ids are time-ordered uuid6)."""
    stale = [
        r["thread_id"] if isinstance(r, dict) else r[0]
        for r in conn.execute(
            f"select thread_id from {CHECKPOINT_SCHEMA}.checkpoints group by thread_id "
            "having max((checkpoint->>'ts')::timestamptz) < now() - make_interval(days => %s)",
            (days,),
        ).fetchall()
    ]
    for table in ("checkpoint_writes", "checkpoint_blobs", "checkpoints"):
        conn.execute(f"delete from {CHECKPOINT_SCHEMA}.{table} where thread_id = any(%s)", (stale,))
    return len(stale)


def pending_questions(graph, config) -> list[str]:
    """Questions of a clarify interrupt the thread is waiting on, else []."""
    for task in graph.get_state(config).tasks:
        for pending in task.interrupts:
            return list(pending.value.get("questions", []))
    return []


def run(
    request: str | None, thread_id: str | None = None, checkpointer=None, answer: str | None = None
) -> dict[str, Any]:
    """One turn. clarify needs a checkpointer to pause, so a run without --thread gets a private
    in-memory one; pass answer= to resume a thread that is waiting on questions."""
    from langgraph.checkpoint.memory import InMemorySaver

    graph = build_graph(checkpointer=checkpointer or InMemorySaver())
    config = {"configurable": {"thread_id": thread_id or "local"}}
    payload: Any = Command(resume=answer) if answer is not None else {"request": request}
    # durability="exit": persist once per turn, not after every node (5x fewer checkpoint rows).
    for update in graph.stream(payload, config, stream_mode="updates", durability="exit"):
        for node in update:
            print(f"[graph] {node} done", file=sys.stderr, flush=True)
    state = dict(graph.get_state(config).values)
    state["clarifying_questions"] = pending_questions(graph, config)
    return state


def compare(model_ids: list[str], gpu_gb: float | None = None) -> dict[str, Any]:
    """Side-by-side comparison of 2-3 models (09.compare_models + GPU fit + license class)."""
    out = _load_09().compare_models(model_ids)
    return {"models": project_checks.compare_models(out["models"], gpu_gb), "missing": out["missing_model_ids"]}


def self_check():
    assert set(hf_tags("embedding")) == {"sentence-similarity", "feature-extraction"}, hf_tags("embedding")
    assert hf_tags("generation") == ["text-generation"] and hf_tags("reranking") == []
    assert hf_tags("retrieval") == hf_tags("embedding")
    from langgraph.checkpoint.memory import InMemorySaver
    from pydantic import ValidationError

    plan = {
        "summary_ko": "s",
        "needs": [{"task": "embedding", "purpose_ko": "p", "model_query": "q"}],
        "constraints": {
            "commercial_only": False,
            "gpu_memory_gb": 8,
            "max_parameter_count_billion": None,
            "min_context_length": None,
        },
        "dataset_terms": ["교통"],
        "dataset_query": "q",
        "clarifying_questions": [],
    }
    assert ProjectPlan.model_validate(plan).needs[0].task == "embedding"
    try:
        ProjectPlan.model_validate({**plan, "needs": [{"task": "dancing", "purpose_ko": "p", "model_query": "q"}]})
        raise AssertionError("off-taxonomy task accepted")
    except ValidationError:
        pass

    order: list[str] = []

    def stub(name, out):
        def node(state):
            order.append(name)
            return out

        return node

    graph = build_graph(
        {
            "decompose": stub("decompose", {"plan": {}}),
            "clarify": stub("clarify", {}),
            "search_models": stub("search_models", {"models": []}),
            "search_datasets": stub("search_datasets", {"datasets": {}}),
            "assess": stub("assess", {"assessment": {}}),
            "explain": stub("explain", {"answer": "ok"}),
        }
    )
    assert graph.invoke({"request": "x"})["answer"] == "ok"
    assert order == ["decompose", "clarify", "search_models", "search_datasets", "assess", "explain"], order

    # Multi-turn: turns accumulate per thread, and the second turn's planner sees the first plan.
    seen = []

    def planner(state):
        seen.append(state.get("plan"))
        return {"plan": {"n": len(seen)}}

    def writer(state):
        return {"answer": f"a{len(seen)}", "turns": [{"request": state["request"], "answer": f"a{len(seen)}"}]}

    def noop(state):
        return {}

    memory = build_graph(
        {"decompose": planner, "search_models": noop, "search_datasets": noop, "explain": writer},
        checkpointer=InMemorySaver(),
    )
    config = {"configurable": {"thread_id": "t"}}
    memory.invoke({"request": "first"}, config)
    final = memory.invoke({"request": "second"}, config)
    assert seen == [None, {"n": 1}], seen
    assert [t["request"] for t in final["turns"]] == ["first", "second"], final["turns"]

    # Clarify: a vague request pauses with questions; resuming carries the answer into the request.
    def vague_plan(state):
        return {"plan": {"clarifying_questions": ["용도는?"]}}

    def asking(state):
        questions = state["plan"].get("clarifying_questions") or []
        if not questions:
            return {}
        return {"request": f"{state['request']} | {interrupt({'questions': questions})}", "plan": {}}

    paused = build_graph(
        {"decompose": vague_plan, "clarify": asking, "explain": lambda state: {"answer": state["request"]}},
        checkpointer=InMemorySaver(),
    )
    cfg = {"configurable": {"thread_id": "c"}}
    paused.invoke({"request": "챗봇"}, cfg)
    assert pending_questions(paused, cfg) == ["용도는?"]
    resumed = paused.invoke(Command(resume="법률 상담"), cfg)
    assert resumed["answer"] == "챗봇 | 법률 상담" and pending_questions(paused, cfg) == []

    # assess: one non-commercial training set blocks a commercial launch.
    verdict = assess(
        {
            "plan": plan,
            "models": [{"models": [{"model_id": "m", "license": "apache-2.0"}]}],
            "datasets": {
                "per_model": {"m": [{"dataset": "klue/klue", "licenses": ["cc-by-nc-4.0"]}]},
                "project_training": [],
                "service_data": [],
            },
        }
    )
    assert verdict["assessment"]["license"]["verdict"] == "blocked", verdict
    print("17_recommend_graph ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("request", nargs="?")
    parser.add_argument("--json", action="store_true", help="print the full state")
    parser.add_argument("--thread", help="conversation id; turns persist in Supabase (PostgresSaver)")
    parser.add_argument("--memory", action="store_true", help="keep --thread in process memory instead")
    parser.add_argument("--compare", nargs="+", metavar="MODEL_ID", help="compare 2-3 models side by side")
    parser.add_argument("--gpu", type=float, help="GPU memory (GB) for --compare")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    logging.getLogger("httpx").setLevel(logging.WARNING)
    if args.compare:
        print(json.dumps(compare(args.compare, args.gpu), ensure_ascii=False, indent=2))
        return
    if args.self_check or not args.request:
        return self_check()

    def converse(saver):
        state = run(args.request, args.thread, saver)
        while state["clarifying_questions"] and sys.stdin.isatty():
            print("\n".join(f"- {q}" for q in state["clarifying_questions"]))
            state = run(None, args.thread, saver, answer=input("답변> "))
        return state

    if args.thread and not args.memory:
        with postgres_checkpointer() as saver:
            state = converse(saver)
            prune_thread(saver.conn, args.thread)
    else:
        from langgraph.checkpoint.memory import InMemorySaver

        state = converse(InMemorySaver())
    if state["clarifying_questions"] and not args.json:
        print("추가 정보가 필요합니다:\n" + "\n".join(f"- {q}" for q in state["clarifying_questions"]))
        return
    print(json.dumps(state, ensure_ascii=False, indent=2) if args.json else state["answer"])


if __name__ == "__main__":
    main()
