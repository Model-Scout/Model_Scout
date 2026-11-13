"""데이터 계약 필터가 Supabase SQL 과 같은 의미인지 확인한다.

로컬 ``05_validate_retrieval.hard_filter`` 와
``supabase_migration_contract_filters.sql`` 의 WHERE 절이 어긋나면, 골든셋과
오프라인 실험이 운영 검색과 **다른 후보 집합**을 평가한다. 숫자는 나오고
해석만 틀리므로 테스트 없이는 드러나지 않는다.

가장 중요한 규칙 하나:

    조건을 걸면 값이 없는 모델은 탈락한다.

PostgreSQL 이 JSON 값을 캐스팅하면 없는 값은 NULL 이 되고 WHERE 가 그 행을
제외한다. 판단 불가를 "가능"으로 보여주면 사용자가 창업에 쓰고 나서 문제를
알게 된다.

    python test/test_contract_filters.py
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location("validate_retrieval_for_contract_test", ROOT / "05_validate_retrieval.py")
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

MIGRATION = (ROOT / "supabase_migration_contract_filters.sql").read_text(encoding="utf-8")


def _row(**metadata):
    return {
        "model_id": "org/model",
        "source_pool": "core",
        "task": {"primary": "text-generation", "matched": ["text-generation"]},
        "filter_metadata": {"korean_verified": True, **metadata},
    }


def _passes(row, **query):
    ok, _ = validator.hard_filter(row, {"tasks": ["text-generation"], **query})
    return ok


def _reasons(row, **query):
    _, reasons = validator.hard_filter(row, {"tasks": ["text-generation"], **query})
    return reasons


# ── 상업 이용 ─────────────────────────────────────────────────────────────

def test_permitted_passes_a_commercial_query():
    assert _passes(_row(commercial_status="permitted"), commercial_status=["permitted"])


def test_prohibited_fails_a_commercial_query():
    assert not _passes(_row(commercial_status="prohibited"), commercial_status=["permitted"])


def test_review_required_fails_a_commercial_query():
    """조건부 라이선스는 정답 후보로 섞지 않는다. 별도 목록으로만 보여준다."""
    assert not _passes(_row(commercial_status="review_required"), commercial_status=["permitted"])


def test_unknown_license_fails_a_commercial_query():
    """판단 불가를 "가능"으로 보여주지 않는다. 의도된 탈락이다."""
    assert not _passes(_row(commercial_status="unknown"), commercial_status=["permitted"])
    assert _reasons(_row(commercial_status="unknown"), commercial_status=["permitted"]) == ["commercial_status"]


def test_missing_commercial_status_fails_a_commercial_query():
    """필드 자체가 없는 구 데이터도 탈락한다. SQL 의 NULL 비교와 같다."""
    assert not _passes(_row(), commercial_status=["permitted"])


def test_several_allowed_statuses_are_a_union():
    row = _row(commercial_status="review_required")
    assert _passes(row, commercial_status=["permitted", "review_required"])


def test_no_commercial_condition_keeps_every_model():
    """조건이 없으면 전부 후보다. 단 결과에 상태를 함께 표시해야 한다."""
    for status in ("permitted", "prohibited", "review_required", "unknown"):
        assert _passes(_row(commercial_status=status))
    assert _passes(_row())


# ── artifact 포맷 ─────────────────────────────────────────────────────────

def test_required_artifact_must_be_present():
    assert _passes(_row(artifact_formats=["gguf"]), require_artifact=["gguf"])
    assert not _passes(_row(artifact_formats=["safetensors"]), require_artifact=["gguf"])


def test_required_artifacts_must_all_be_present():
    """여러 개를 요구하면 전부 갖춘 모델만 남는다. SQL 의 count = cardinality 와 같다."""
    both = _row(artifact_formats=["gguf", "safetensors"])
    only_one = _row(artifact_formats=["gguf"])
    assert _passes(both, require_artifact=["gguf", "safetensors"])
    assert not _passes(only_one, require_artifact=["gguf", "safetensors"])


def test_missing_artifact_formats_fails_an_artifact_query():
    assert not _passes(_row(), require_artifact=["gguf"])


def test_empty_artifact_requirement_is_no_condition():
    assert _passes(_row(artifact_formats=["safetensors"]), require_artifact=[])


# ── 실행 파일 크기 ────────────────────────────────────────────────────────

def test_artifact_size_upper_bound():
    assert _passes(_row(artifact_runnable_gib=4.1), max_artifact_gib=8)
    assert not _passes(_row(artifact_runnable_gib=13.5), max_artifact_gib=8)


def test_artifact_size_boundary_is_inclusive():
    """SQL 이 <= 이므로 경계는 통과한다."""
    assert _passes(_row(artifact_runnable_gib=8.0), max_artifact_gib=8)


def test_missing_artifact_size_fails_a_size_bound():
    """numeric_ok 의 규칙과 같다. 크기를 모르면 크기 질의에서 사라진다."""
    assert not _passes(_row(), max_artifact_gib=8)
    assert not _passes(_row(artifact_runnable_gib=None), max_artifact_gib=8)


def test_missing_artifact_size_passes_without_a_size_bound():
    assert _passes(_row())


# ── gated ────────────────────────────────────────────────────────────────

def test_exclude_gated_keeps_only_open_repos():
    assert _passes(_row(gated=False), exclude_gated=True)
    assert not _passes(_row(gated="auto"), exclude_gated=True)
    assert not _passes(_row(gated="manual"), exclude_gated=True)


def test_unknown_gated_is_not_treated_as_open():
    """gated 를 못 받은 것은 "공개"가 아니라 "모름"이다.

    모름을 공개로 보면 접근 승인이 필요한 모델을 "바로 쓸 수 있다"고 말하게 된다.
    """
    assert not _passes(_row(gated=None), exclude_gated=True)
    assert not _passes(_row(), exclude_gated=True)


def test_gated_models_pass_without_the_condition():
    assert _passes(_row(gated="manual"))


# ── 조건 조합 ────────────────────────────────────────────────────────────

def test_all_four_conditions_together():
    fits = _row(commercial_status="permitted", artifact_formats=["gguf"],
                artifact_runnable_gib=4.1, gated=False)
    assert _passes(fits, commercial_status=["permitted"], require_artifact=["gguf"],
                   max_artifact_gib=8, exclude_gated=True)


def test_each_failing_condition_is_reported_separately():
    """왜 탈락했는지 하나씩 보여야 "왜 안 나오냐"에 답할 수 있다."""
    bad = _row(commercial_status="unknown", artifact_formats=["safetensors"],
               artifact_runnable_gib=20.0, gated="manual")
    reasons = _reasons(bad, commercial_status=["permitted"], require_artifact=["gguf"],
                       max_artifact_gib=8, exclude_gated=True)
    assert set(reasons) == {"commercial_status", "artifact", "artifact_size", "gated"}


# ── 로컬과 SQL 이 같은 키를 쓰는지 ────────────────────────────────────────

def test_migration_declares_every_local_filter_parameter():
    """로컬에만 있고 SQL 에 없는 조건이 생기면 두 쪽이 갈라진다."""
    for parameter in ("commercial_status_filter", "require_artifact",
                      "max_artifact_gib", "exclude_gated"):
        assert re.search(rf"\b{parameter}\b", MIGRATION), f"SQL 에 {parameter} 가 없다"


def test_migration_reads_the_fields_stage4_writes():
    """04_build_embeddings.contract_filter_fields 가 쓰는 키를 SQL 이 읽어야 한다."""
    for key in ("commercial_status", "artifact_formats", "artifact_runnable_gib", "gated"):
        assert f"'{key}'" in MIGRATION, f"SQL 이 filter_metadata->>'{key}' 를 읽지 않는다"


def test_migration_drops_the_old_signature():
    """파라미터가 늘면 PostgreSQL 이 과부하를 만든다. 구 시그니처를 지워야 한다."""
    assert "drop function if exists public.match_model_scout_models" in MIGRATION


def _migration_signature():
    """migration 의 match_model_scout_models(...) 파라미터를 (이름, 타입) 순서대로."""
    body = MIGRATION.split("create or replace function public.match_model_scout_models(", 1)[1]
    body = body.split("\n)\nreturns table", 1)[0]
    pairs = []
    for line in body.splitlines():
        line = line.split("--", 1)[0].strip().rstrip(",")
        if not line:
            continue
        name, sql_type = line.split()[:2]
        pairs.append((name, "vector" if sql_type.startswith("vector") else sql_type))
    return pairs


def _rpc_args_in_09():
    """09 를 import 하지 않고(mcp 의존성 없이) RPC 인자 상수를 읽는다."""
    import ast

    tree = ast.parse((ROOT / "09_model_scout_mcp_readonly.py").read_text(encoding="utf-8"))
    values = {
        node.targets[0].id: ast.literal_eval(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign)
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id in ("RPC_BASE_ARGS", "RPC_CONTRACT_ARGS")
    }
    return list(values["RPC_BASE_ARGS"]), list(values["RPC_CONTRACT_ARGS"])


def test_09_rpc_arguments_match_the_migration_signature_in_order():
    """09 가 보내는 %s::type 순서가 SQL 시그니처와 어긋나면 값이 엉뚱한 파라미터로 들어간다."""
    base, contract = _rpc_args_in_09()
    assert len(base) == 15 and len(contract) == 4
    assert base + contract == _migration_signature()


def test_planner_exposes_the_contract_filter_keys():
    sys.path.insert(0, str(ROOT / "retrieval_lab"))
    import planner

    for key in ("commercial_status", "require_artifact", "max_artifact_gib", "exclude_gated"):
        assert key in planner.HARD_FILTER_KEYS, f"planner 에 {key} 가 없다"


def test_golden_set_verifier_allows_the_contract_filter_keys():
    """verify.py 의 허용 목록이 좁으면 새 조건을 쓴 질의가 "하드 필터가 모르는 조건"이 된다."""
    source = (ROOT / "test" / "golden" / "v2" / "tools" / "verify.py").read_text(encoding="utf-8")
    for key in ("commercial_status", "require_artifact", "max_artifact_gib", "exclude_gated"):
        assert f'"{key}"' in source, f"verify.py 에 {key} 가 없다"


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
