"""Pre-retrieval query transforms: Rewrite, Decomposition, Multi-Query, HyDE.

Every LLM output is cached under retrieval_lab/cache/pre_retrieval/<strategy>/
(one JSON file per query, so teammates can commit caches without merge
conflicts). A cached run is free and reproducible; the recorded LLM latency is
reused so p95/p99 still include the pre-retrieval cost.

Bump PROMPT_VERSION when a prompt changes; old cache entries are then ignored.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = Path(__file__).resolve().parent / "cache" / "pre_retrieval"
DEFAULT_LLM = "gpt-4o-mini"
PROMPT_VERSION = 1
STRATEGIES = ("rewrite", "decomposition", "multi_query", "hyde")

_CONTEXT = (
    "You prepare search queries for Model Scout, a search engine over Hugging Face model cards "
    "of Korean-capable models. Documents are English model-card summaries with fields such as "
    "task, declared languages, parameter count, context length, quantization, license, use cases "
    "and benchmarks. User queries are usually Korean. Keep every model name, model family, file "
    "format (GGUF, AWQ, ONNX), translation direction, benchmark and metric name exactly as written. "
    "Never invent model names the user did not mention. Reply with JSON only."
)

PROMPTS = {
    "rewrite": (
        "Rewrite the user request into one search query that keeps the original Korean intent and "
        "adds the English technical terms a model card would use (task name, capability, domain). "
        "Drop filler words. Return {\"query\": \"...\"}."
    ),
    "decomposition": (
        "Split the user request into 2-4 independent sub-queries, one per requirement aspect "
        "(task/capability, domain or data, deployment or size, language). Each sub-query must make "
        "sense on its own. A request with a single aspect returns one sub-query. "
        "Return {\"sub_queries\": [\"...\"]}."
    ),
    "multi_query": (
        "Write 3 different search queries for the same user request: one Korean paraphrase, one "
        "English paraphrase, and one keyword-style query with model-card terms. "
        "Return {\"queries\": [\"...\", \"...\", \"...\"]}."
    ),
    "hyde": (
        "Write a short hypothetical English model-card summary (80-150 words) of a model that would "
        "perfectly satisfy the request: task, languages, size, intended use cases, strengths. Do not "
        "name a specific model unless the user did. Return {\"document\": \"...\"}."
    ),
}


class LLMUnavailable(RuntimeError):
    """Raised on a cache miss when no LLM can be called."""


@dataclass
class Transform:
    strategy: str
    outputs: List[str]
    latency_ms: float
    cached: bool
    raw: Dict[str, Any] = field(default_factory=dict)


def llm_model() -> str:
    return os.getenv("PRE_RETRIEVAL_LLM_MODEL", DEFAULT_LLM)


def cache_path(strategy: str, text: str, model: str) -> Path:
    key = hashlib.sha256(f"{strategy}|v{PROMPT_VERSION}|{model}|{text}".encode("utf-8")).hexdigest()[:20]
    return CACHE_DIR / strategy / f"{key}.json"


def parse_outputs(strategy: str, payload: Dict[str, Any]) -> List[str]:
    if strategy == "rewrite":
        values = [payload.get("query")]
    elif strategy == "decomposition":
        values = payload.get("sub_queries") or []
    elif strategy == "multi_query":
        values = payload.get("queries") or []
    elif strategy == "hyde":
        values = [payload.get("document")]
    else:
        raise ValueError(f"unknown strategy: {strategy}")
    outputs = [str(value).strip() for value in values if value and str(value).strip()]
    if not outputs:
        raise ValueError(f"{strategy}: empty LLM output {payload}")
    return outputs


def _call_llm(strategy: str, text: str, model: str) -> Dict[str, Any]:
    try:
        from dotenv import load_dotenv

        load_dotenv(ROOT / ".env")
    except ImportError:
        pass
    if not os.getenv("OPENAI_API_KEY"):
        raise LLMUnavailable(f"{strategy} 캐시 없음, OPENAI_API_KEY도 없음: {text[:40]}")
    from openai import OpenAI

    response = OpenAI().chat.completions.create(
        model=model,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f"{_CONTEXT}\n\n{PROMPTS[strategy]}"},
            {"role": "user", "content": text},
        ],
    )
    return json.loads(response.choices[0].message.content or "{}")


def transform(strategy: str, text: str, model: Optional[str] = None) -> Transform:
    model = model or llm_model()
    path = cache_path(strategy, text, model)
    if path.exists():
        entry = json.loads(path.read_text(encoding="utf-8"))
        return Transform(strategy, entry["outputs"], float(entry["latency_ms"]), True, entry["response"])
    started = time.perf_counter()
    payload = _call_llm(strategy, text, model)
    latency_ms = (time.perf_counter() - started) * 1000.0
    outputs = parse_outputs(strategy, payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "strategy": strategy,
        "prompt_version": PROMPT_VERSION,
        "model": model,
        "input": text,
        "outputs": outputs,
        "response": payload,
        "latency_ms": round(latency_ms, 1),
    }
    path.write_text(json.dumps(entry, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return Transform(strategy, outputs, latency_ms, False, payload)
