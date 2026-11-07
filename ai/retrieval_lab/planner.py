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
    # 데이터 계약 필터(ai/contract/). supabase_migration_contract_filters.sql 과
    # 05_validate_retrieval.hard_filter 가 같은 의미를 구현한다.
    "commercial_status",
    "require_artifact",
    "max_artifact_gib",
    "exclude_gated",
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
    # Pin models named in the query (exact model-name match, no LLM) before fused results.
    use_name_lookup: bool = False
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
        if self.use_name_lookup:
            used.append("Name Lookup")
        return " + ".join(used) if used else "Baseline"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


BASELINE = RetrievalPlan(query_type="baseline")
_TUNABLE = ("dense_weight", "use_rewrite", "use_decomposition", "use_multi_query", "use_hyde", "use_name_lookup", "top_k", "rrf_k")
# Elements the A/B experiments switch on and off: the LLM transforms plus name lookup.
ELEMENTS = ("rewrite", "decomposition", "multi_query", "hyde", "name_lookup")


def with_strategies(plan: RetrievalPlan, strategies: tuple[str, ...]) -> RetrievalPlan:
    return replace(plan, **{f"use_{name}": name in strategies for name in ELEMENTS})


def with_dense_weight(plan: RetrievalPlan, dense_weight: float) -> RetrievalPlan:
    dense_weight = round(float(dense_weight), 4)
    return replace(plan, dense_weight=dense_weight, sparse_weight=round(1.0 - dense_weight, 4))


def hard_filters(query: Mapping[str, Any]) -> Dict[str, Any]:
    # bool은 False도 살린다. 유형 기본값을 끌 수 있는 유일한 수단이다.
    return {key: query[key] for key in HARD_FILTER_KEYS
            if isinstance(query.get(key), bool) or query.get(key) not in (None, [], False)}


# ``require_known_*``는 명시적으로 "값이 공개된 모델"을 요청한 경우에만 의미가
# 있다. 수치 상·하한이 있으면 05_validate_retrieval.hard_filter는 Supabase SQL과
# 동일하게 누락 값을 이미 제외한다.
_KNOWN_FLAG_PAIRS = {
    "require_known_parameters": ("max_parameters_billion",),
    "require_known_context": ("min_context_length", "max_context_length"),
}


def hard_filter_plan(defaults: Mapping[str, Any], query: Mapping[str, Any]) -> Dict[str, Any]:
    """유형 기본값 위에 질의 값을 얹는다. 질의가 직접 말한 값이 언제나 이긴다.

    유형 기본값으로 켜진 require_known_*는 짝이 되는 수치 조건이 있을 때만 남긴다.
    수치 조건이 있으면 이 플래그는 중복이지만, 과거 Planner 설정과의 호환성을 위해
    보존한다. 상한도 하한도 없는 질의에서 "값을 안다"는 이유로 후보를 거르면
    멀쩡한 모델만 잃는다. 질의가 직접 지정한 플래그는 수치 조건과 무관하게 그대로
    둔다.

    실험(experiment.evaluate)과 서비스(plan_for)가 같은 함수를 쓴다. 한쪽에만
    이 처리가 있으면 측정한 설정과 서비스하는 설정이 달라진다.
    """
    asked = hard_filters(query)
    filters = {**defaults, **asked}
    for flag, pair in _KNOWN_FLAG_PAIRS.items():
        if flag not in asked and not any(filters.get(key) for key in pair):
            filters.pop(flag, None)
    return filters


def load_config(path: Path = CONFIG_PATH) -> Dict[str, Any]:
    if not path.exists():
        return {"types": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def plan_for(query_type: str, query: Mapping[str, Any], config: Optional[Mapping[str, Any]] = None) -> RetrievalPlan:
    """Build the plan for one query. Unknown types fall back to the baseline."""
    config = config if config is not None else load_config()
    values = dict((config.get("types") or {}).get(query_type) or {})
    # 유형별 hard filter 기본값. 계획서가 Planner의 역할로 Hard Filter 선택을 꼽지만
    # 지금까지는 질의에 적힌 값만 썼다.
    filters = hard_filter_plan(values.get("hard_filter_defaults") or {}, query)
    plan = replace(BASELINE, query_type=query_type, hard_filters=filters)
    plan = replace(plan, **{key: values[key] for key in _TUNABLE if key in values and key != "dense_weight"})
    if "dense_weight" in values:
        plan = with_dense_weight(plan, values["dense_weight"])
    return plan


def save_type_plan(query_type: str, plan: RetrievalPlan, evidence: Mapping[str, Any],
                   path: Path = CONFIG_PATH,
                   hard_filter_defaults: Optional[Mapping[str, Any]] = None) -> None:
    config = load_config(path)
    entry = {key: getattr(plan, key) for key in _TUNABLE}
    entry["sparse_weight"] = plan.sparse_weight
    if hard_filter_defaults:
        entry["hard_filter_defaults"] = dict(hard_filter_defaults)
    entry["evidence"] = dict(evidence)
    config.setdefault("types", {})[query_type] = entry
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
