"""데이터 계약 필터가 09 검색 → 17 LangGraph → project_checks 로 이어지는지 확인한다.

    09_model_scout_mcp_readonly.search_models   RPC 15/19 인자, 기능 플래그
    17_recommend_graph                          Constraints, 캐시 키, DB 필터 vs 후처리
    project_checks                              모델 commercial_status 와 데이터 라이선스 판정

MODEL_CONTRACT_FILTERS_ENABLED 가 꺼져 있으면(기본) 운영 DB 에 마이그레이션이 없어도
지금과 같은 15개 인자 호출이어야 한다. DB 와 OpenAI 는 전부 가짜다.

mcp·langgraph 가 필요하다(requirements_mcp.txt).

    python test/test_recommend_contract_stack.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


search09 = _load("model_scout_mcp_for_stack_test", "09_model_scout_mcp_readonly.py")
graph17 = _load("recommend_graph", "17_recommend_graph.py")
stage4 = _load("stage4_for_stack_test", "04_build_embeddings.py")
import project_checks  # noqa: E402

MIGRATION = (ROOT / "supabase_migration_contract_filters.sql").read_text(encoding="utf-8")
# main 의 09 가 보내던 SQL 의 캐스트 순서 그대로다. 플래그 OFF 경로가 이것과 같아야 한다.
ORIGINAL_CASTS = [
    "vector", "integer", "text", "text[]", "boolean", "numeric", "numeric", "integer",
    "integer", "boolean", "boolean", "text", "text", "real", "real",
]


@contextlib.contextmanager
def patched(target: Any, **attrs: Any):
    old = {name: getattr(target, name) for name in attrs}
    for name, value in attrs.items():
        setattr(target, name, value)
    try:
        yield
    finally:
        for name, value in old.items():
            setattr(target, name, value)


@contextlib.contextmanager
def flag(value: str | None):
    old = os.environ.get(search09.CONTRACT_FILTERS_ENV)
    if value is None:
        os.environ.pop(search09.CONTRACT_FILTERS_ENV, None)
    else:
        os.environ[search09.CONTRACT_FILTERS_ENV] = value
    try:
        yield
    finally:
        if old is None:
            os.environ.pop(search09.CONTRACT_FILTERS_ENV, None)
        else:
            os.environ[search09.CONTRACT_FILTERS_ENV] = old


# ── 09: RPC 호출 모양 ─────────────────────────────────────────────────────

def _search(**kwargs: Any):
    captured: Dict[str, Any] = {}

    class Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def execute(self, statement, parameters):
            captured["statement"] = statement
            captured["parameters"] = parameters

        def fetchall(self):
            return []

    class Connection:
        def cursor(self, cursor_factory=None):
            return Cursor()

    @contextlib.contextmanager
    def connection():
        yield Connection()

    with patched(search09, _query_embedding=lambda query: [0.0] * 1536, _read_connection=connection):
        out = search09.search_models("한국어 챗봇 모델", **kwargs)
    casts = re.findall(r"%s::([a-z\[\]]+)", captured["statement"])
    return out, casts, captured["parameters"]


CONTRACT = {
    "commercial_status_filter": ["permitted"],
    "require_artifact": ["GGUF"],
    "max_artifact_gib": 8.0,
    "exclude_gated": True,
}


def test_flag_off_keeps_the_15_argument_call_even_with_conditions():
    with flag(None):
        out, casts, params = _search(**CONTRACT)
    assert casts == ORIGINAL_CASTS and len(params) == 15
    assert params[-2:] == (0.65, 0.35), "검색 가중치를 바꾸지 않는다"
    assert out["contract_filters"] == {"enabled": False, "requested": True, "applied": False}


def test_old_callers_get_the_original_call():
    for value in (None, "true"):
        with flag(value):
            out, casts, params = _search(task_filters=["text-generation"], korean_required=True)
        assert casts == ORIGINAL_CASTS and len(params) == 15
        assert out["contract_filters"]["requested"] is False


def test_flag_on_sends_19_arguments_in_signature_order():
    with flag("true"):
        out, casts, params = _search(**CONTRACT)
    expected = [sql_type for _, sql_type in search09.RPC_BASE_ARGS + search09.RPC_CONTRACT_ARGS]
    assert casts == expected and len(params) == 19
    assert params[15:] == (["permitted"], ["gguf"], 8.0, True)
    assert out["contract_filters"]["applied"] is True
    assert out["filters"]["require_artifact"] == ["gguf"]


def test_flag_values():
    for value, expected in (("1", True), ("TRUE", True), ("on", True), ("false", False), ("", False), (None, False)):
        with flag(value):
            assert search09.contract_filters_enabled() is expected, value


def test_migration_parameter_names_match_09():
    names = [name for name, _ in search09.RPC_BASE_ARGS + search09.RPC_CONTRACT_ARGS]
    positions = [MIGRATION.index(f"    {name} ") for name in names]
    assert positions == sorted(positions), "migration 과 09 의 인자 순서가 다르다"


def test_compact_filter_metadata_passes_the_stage4_contract_fields():
    contract_fields = set(stage4.contract_filter_fields({"identity": {}}))
    wanted = {"commercial_status", "artifact_formats", "artifact_runnable_gib", "gated", "dtype",
              "unresolved_filter_fields"}
    assert wanted <= contract_fields, "Stage 4 에 없는 이름을 상상해서 넣었다"
    meta = {key: f"v-{key}" for key in wanted} | {"license": "mit", "embedding": [0.1]}
    compact = search09._compact_filter_metadata(meta)
    assert wanted <= set(compact) and "embedding" not in compact


# ── 17: Constraints ─────────────────────────────────────────────────────

def test_old_checkpoint_plans_still_validate():
    old = {"commercial_only": True, "gpu_memory_gb": 8, "max_parameter_count_billion": None,
           "min_context_length": None}
    parsed = graph17.Constraints.model_validate(old)
    assert parsed.required_artifacts == [] and parsed.max_artifact_gib is None and parsed.exclude_gated is False
    assert graph17.constraints_of({"constraints": old})["exclude_gated"] is False
    assert graph17.constraints_of({})["required_artifacts"] == []


def test_planner_schema_requires_every_constraint_field():
    """구조화 출력 스키마에는 기본값 없이 전부 필수다. 기본값은 저장된 plan 에만 채운다."""
    schema = graph17.Constraints.model_json_schema()
    assert set(schema["required"]) == set(graph17.constraint_defaults())


def _llm(constraints: Dict[str, Any]):
    return {**graph17.constraint_defaults(), **constraints}


def test_local_execution_alone_does_not_require_gguf():
    kept = graph17.explicit_constraints(_llm({"required_artifacts": ["gguf"]}), "로컬에서 실행할 한국어 챗봇")
    assert kept["required_artifacts"] == []


def test_named_runtimes_require_gguf():
    for said in ("Ollama로 돌릴 모델", "GGUF 파일 있는 모델", "llama.cpp 로 쓸 거야"):
        kept = graph17.explicit_constraints(_llm({"required_artifacts": ["gguf"]}), said)
        assert kept["required_artifacts"] == ["gguf"], said


def test_gpu_memory_is_not_an_artifact_size():
    said = "RTX 4060 8GB GPU 에서 돌릴 모델"
    kept = graph17.explicit_constraints(_llm({"gpu_memory_gb": 8, "max_artifact_gib": 8}), said)
    assert kept["max_artifact_gib"] is None and kept["gpu_memory_gb"] == 8
    stated = graph17.explicit_constraints(_llm({"max_artifact_gib": 5}), "모델 파일 5GB 이하")
    assert stated["max_artifact_gib"] == 5


def test_gated_exclusion_needs_an_explicit_request():
    assert graph17.explicit_constraints(_llm({"exclude_gated": True}), "공개 모델 추천")["exclude_gated"] is False
    assert graph17.explicit_constraints(_llm({"exclude_gated": True}), "승인 없이 바로 쓸 모델")["exclude_gated"]


def test_refinement_keeps_conditions_from_earlier_turns_and_can_remove_them():
    previous = _llm({"required_artifacts": ["gguf"], "exclude_gated": True})
    kept = graph17.explicit_constraints(_llm({"required_artifacts": ["gguf"], "exclude_gated": True}),
                                        "상업용만", previous)
    assert kept["required_artifacts"] == ["gguf"] and kept["exclude_gated"] is True
    dropped = graph17.explicit_constraints(_llm({}), "GGUF 아니어도 돼", previous)
    assert dropped["required_artifacts"] == []


def test_parse_plan_applies_the_explicit_filter_to_llm_output():
    plan = {"summary_ko": "s", "needs": [], "dataset_terms": [], "dataset_query": "q", "clarifying_questions": [],
            "constraints": _llm({"commercial_only": True, "required_artifacts": ["gguf"], "exclude_gated": True})}
    with patched(graph17, _llm_plan=lambda user: dict(plan)):
        parsed = graph17._parse_plan("로컬에서 돌릴 상업용 챗봇")
    assert parsed["constraints"]["commercial_only"] is True  # 기존 동작: LLM 판단 그대로
    assert parsed["constraints"]["required_artifacts"] == [] and parsed["constraints"]["exclude_gated"] is False


def test_decompose_prompt_states_the_parsing_rules():
    prompt = graph17.DECOMPOSE_PROMPT
    for phrase in ("required_artifacts", "Ollama", "로컬 실행", "max_artifact_gib", "never this", "exclude_gated",
                   "승인 없이"):
        assert phrase in prompt, phrase


# ── 17: 검색 경로 ────────────────────────────────────────────────────────

def _row(model_id: str, status: str | None, license_value: str = "other") -> Dict[str, Any]:
    meta = {"license": license_value}
    if status is not None:
        meta["commercial_status"] = status
    return {"model_id": model_id, "ranking": {"rank_score": 0.5}, "task": {"primary": "text-generation"},
            "filter_metadata": meta}


class FakeSearch:
    """09 의 계약대로 움직이는 가짜. 필터가 켜지면 top-N 자르기 **전에** 거른다."""

    def __init__(self, corpus: List[Dict[str, Any]], enabled: bool):
        self.corpus = corpus
        self.enabled = enabled
        self.calls: List[Dict[str, Any]] = []

    def contract_filters_enabled(self):
        return self.enabled

    def search_models(self, query, match_count=5, **kwargs):
        self.calls.append({"query": query, **kwargs})
        statuses = kwargs.get("commercial_status_filter")
        applied = self.enabled and any(
            kwargs.get(k) not in (None, False)
            for k in ("commercial_status_filter", "require_artifact", "max_artifact_gib", "exclude_gated")
        )
        rows = self.corpus
        if applied and statuses:
            rows = [r for r in rows if r["filter_metadata"].get("commercial_status") in statuses]
        return {"results": rows[:match_count], "contract_filters": {"applied": applied}}


def _plan(query: str = "한국어 챗봇", **constraints: Any) -> Dict[str, Any]:
    # _model_rows 의 TTL 캐시는 프로세스 전역이다. 테스트마다 질의를 달리해 서로 섞이지 않게 한다.
    return {"needs": [{"task": "generation", "purpose_ko": "p", "model_query": query}],
            "constraints": _llm(constraints)}


def _run_search(fake: FakeSearch, plan: Dict[str, Any]):
    with patched(graph17, _load_09=lambda: fake):
        return graph17.search_models({"plan": plan})["models"][0]["models"]


def _corpus_with_permitted_at(rank: int) -> List[Dict[str, Any]]:
    rows = [_row(f"org/unknown-{i}", "unknown") for i in range(10)]
    rows.insert(rank - 1, _row("org/permitted", "permitted"))
    return rows


def test_flag_on_filters_commercial_in_the_database_before_the_top_n_cut():
    """permitted 모델이 7위면 Top-6 후처리로는 사라진다. DB 필터는 그 전에 거른다."""
    fake = FakeSearch(_corpus_with_permitted_at(7), enabled=True)
    rows = _run_search(fake, _plan("db-filter", commercial_only=True))
    assert [r["model_id"] for r in rows] == ["org/permitted"]
    assert fake.calls[0]["commercial_status_filter"] == ["permitted"]


def test_flag_off_keeps_the_legacy_post_filter():
    fake = FakeSearch(_corpus_with_permitted_at(7), enabled=False)
    rows = _run_search(fake, _plan("post-filter", commercial_only=True, required_artifacts=["gguf"]))
    assert rows == [], "플래그 OFF 는 예전처럼 Top-N 뒤에 거른다"
    assert "commercial_status_filter" not in fake.calls[0] and "require_artifact" not in fake.calls[0]


def test_cache_key_separates_contract_conditions():
    fake = FakeSearch([_row("org/a", "permitted")], enabled=True)
    _run_search(fake, _plan("cache"))
    _run_search(fake, _plan("cache"))
    assert len(fake.calls) == 1, "같은 조건은 캐시를 탄다"
    _run_search(fake, _plan("cache", commercial_only=True, required_artifacts=["gguf"], exclude_gated=True))
    assert len(fake.calls) == 2, "상업+GGUF+gated 제외 검색이 일반 검색 캐시를 공유했다"
    assert fake.calls[1]["require_artifact"] == ["gguf"] and fake.calls[1]["exclude_gated"] is True
    disabled = FakeSearch([_row("org/a", "permitted")], enabled=False)
    _run_search(disabled, _plan("cache"))
    assert len(disabled.calls) == 1, "플래그 상태도 키에 들어간다"


def test_compact_model_prefers_commercial_status_over_the_raw_license():
    row = graph17._compact_model(_row("org/m", "permitted", "other"))
    assert row["commercial_status"] == "permitted" and row["commercial_use"] == "commercial"
    assert row["license"] == "other"  # 원문은 그대로 같이 보낸다
    prohibited = graph17._compact_model(_row("org/m", "prohibited", "apache-2.0"))
    assert prohibited["commercial_use"] == "non_commercial"


def test_compact_model_falls_back_to_the_raw_license_on_old_rows():
    row = graph17._compact_model(_row("org/m", None, "mit"))
    assert row["commercial_status"] is None and row["commercial_use"] == "commercial"
    assert row["gated"] is None and row["artifact_formats"] is None


# ── 모델·데이터 라이선스 판정 ─────────────────────────────────────────────

def _stack(model_status: str | None, dataset_license: Any, model_license: str = "other"):
    return project_checks.license_verdict([
        {"kind": "모델", "id": "m", "license": model_license, "commercial_status": model_status},
        {"kind": "학습 데이터", "id": "d", "license": dataset_license},
    ])["verdict"]


def test_stack_verdict_follows_the_most_restrictive_piece():
    assert _stack("permitted", ["cc-by-4.0"]) == "commercial_ok"
    assert _stack("permitted", ["other"]) == "review"            # 데이터 조건부 → 전체 review
    assert _stack("permitted", ["cc-by-nc-4.0"]) == "blocked"
    assert _stack("prohibited", ["cc-by-4.0"]) == "blocked"
    assert _stack("unknown", ["cc-by-4.0"]) == "review"
    assert _stack("review_required", ["cc-by-4.0"], "apache-2.0") == "review"  # status 가 원문보다 우선
    assert _stack(None, ["cc-by-4.0"], "apache-2.0") == "commercial_ok"         # 옛 행은 원문으로
    assert _stack(None, ["공공누리 제2유형"], "apache-2.0") == "blocked"           # 공공데이터 경로 유지


def test_assess_passes_the_model_status_through():
    plan = _plan()
    state = {"plan": plan,
             "models": [{"models": [{"model_id": "m", "license": "apache-2.0", "commercial_status": "prohibited"}]}],
             "datasets": {"per_model": {}, "project_training": [], "service_data": []}}
    assert graph17.assess(state)["assessment"]["license"]["verdict"] == "blocked"


# ── GPU ──────────────────────────────────────────────────────────────────

def test_gpu_fit_never_invents_numbers():
    assert project_checks.gpu_fit(7.0, None) is None
    unknown = project_checks.gpu_fit(None, 8.0, {})
    assert unknown["verdict"] == "unknown" and unknown["needed_gib"] is None
    estimate = project_checks.gpu_fit(0.5, 8.0)
    assert estimate["basis"] == project_checks.GPU_FIT_BASIS


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
