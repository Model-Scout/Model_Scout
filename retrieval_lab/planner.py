"""Retrieval Planner: query type -> hard filters, channel weights, pre-retrieval, top_k.

Per-type values live in retrieval_lab/planner_config.json. They start at the
baseline and are replaced with the winners of the golden-set experiments
(`python -m retrieval_lab.experiment ... --write-planner`).
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

CONFIG_PATH = Path(__file__).resolve().parent / "planner_config.json"

PLAN_QUERY_TYPES = (
    "model_comparison",
    "semantic_capability",
    "lexical_exact",
    "structured_constraint",
    "benchmark_lookup",
    "semantic_constraint",
    "abstention",
)

# Query-schema keys that 05_validate_retrieval.hard_filter understands.
HARD_FILTER_KEYS = (
    "pools",
    "tasks",
    "korean_required",
    "max_parameters_billion",
    "min_context_length",
    "max_context_length",
    "require_known_parameters",
    "require_known_context",
    "popularity_tier",
)


@dataclass(frozen=True)
class RetrievalPlan:
    query_type: str
    hard_filters: Dict[str, Any] = field(default_factory=dict)
    dense_weight: float = 0.5
    sparse_weight: float = 0.5
    use_rewrite: bool = False
    use_decomposition: bool = False
    use_multi_query: bool = False
    use_hyde: bool = False
    top_k: int = 30
    rrf_k: int = 60

    def strategies(self) -> tuple[str, ...]:
        flags = (
            ("rewrite", self.use_rewrite),
            ("decomposition", self.use_decomposition),
            ("multi_query", self.use_multi_query),
            ("hyde", self.use_hyde),
        )
        return tuple(name for name, on in flags if on)

    def label(self) -> str:
        names = {"rewrite": "Rewrite", "decomposition": "Decomposition", "multi_query": "Multi-Query", "hyde": "HyDE"}
        used = [names[name] for name in self.strategies()]
        return " + ".join(used) if used else "Baseline"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


BASELINE = RetrievalPlan(query_type="baseline")
_TUNABLE = ("dense_weight", "use_rewrite", "use_decomposition", "use_multi_query", "use_hyde", "top_k", "rrf_k")


def with_strategies(plan: RetrievalPlan, strategies: tuple[str, ...]) -> RetrievalPlan:
    return replace(plan, **{f"use_{name}": name in strategies for name in ("rewrite", "decomposition", "multi_query", "hyde")})


def with_dense_weight(plan: RetrievalPlan, dense_weight: float) -> RetrievalPlan:
    dense_weight = round(float(dense_weight), 4)
    return replace(plan, dense_weight=dense_weight, sparse_weight=round(1.0 - dense_weight, 4))


def hard_filters(query: Mapping[str, Any]) -> Dict[str, Any]:
    return {key: query[key] for key in HARD_FILTER_KEYS if query.get(key) not in (None, [], False)}


def load_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    if not path.exists():
        return {"types": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def plan_for(query_type: str, query: Mapping[str, Any], config: Optional[Mapping[str, Any]] = None) -> RetrievalPlan:
    """Build the plan for one query. Unknown types fall back to the baseline."""
    config = config if config is not None else load_config()
    values = dict((config.get("types") or {}).get(query_type) or {})
    plan = replace(BASELINE, query_type=query_type, hard_filters=hard_filters(query))
    plan = replace(plan, **{key: values[key] for key in _TUNABLE if key in values and key != "dense_weight"})
    if "dense_weight" in values:
        plan = with_dense_weight(plan, values["dense_weight"])
    return plan


def save_type_plan(query_type: str, plan: RetrievalPlan, evidence: Mapping[str, Any], path: Path = CONFIG_PATH) -> None:
    config = load_config(path)
    entry = {key: getattr(plan, key) for key in _TUNABLE}
    entry["sparse_weight"] = plan.sparse_weight
    entry["evidence"] = dict(evidence)
    config.setdefault("types", {})[query_type] = entry
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
