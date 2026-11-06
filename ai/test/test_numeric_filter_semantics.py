"""로컬 하드 필터가 Supabase SQL의 수치 조건 의미와 같은지 확인한다.

Supabase의 ``(json_value)::numeric <= bound``는 값이 없으면 NULL이 되어
WHERE에서 제외된다. 이 테스트가 없으면 로컬 골든셋/실험만 미공개 모델을
통과시키고, 실제 서비스와 서로 다른 후보 집합을 평가하게 된다.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location("validate_retrieval_for_numeric_test", ROOT / "05_validate_retrieval.py")
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def _row(**metadata):
    return {
        "model_id": "org/model",
        "source_pool": "core",
        "task": {"primary": "text-generation", "matched": ["text-generation"]},
        "filter_metadata": {"korean_verified": True, **metadata},
    }


def test_missing_numeric_value_fails_a_numeric_bound():
    """SQL의 NULL 비교와 같게, 값이 없으면 상·하한을 만족하지 못한다."""
    assert validator.numeric_ok(None, maximum=3.0) is False
    assert validator.numeric_ok(None, minimum=32_768) is False


def test_missing_numeric_value_passes_when_no_numeric_or_known_requirement_exists():
    assert validator.numeric_ok(None) is True


def test_explicit_known_requirement_without_bound_still_works():
    assert validator.numeric_ok(None, required=True) is False
    assert validator.numeric_ok(1.0, required=True) is True


def test_hard_filter_excludes_unknown_parameter_for_bounded_query():
    ok, reasons = validator.hard_filter(
        _row(parameter_count_billion=None),
        {"tasks": ["text-generation"], "korean_required": True, "max_parameters_billion": 3.0},
    )
    assert ok is False
    assert reasons == ["parameter_count"]


def test_hard_filter_keeps_known_parameter_inside_bound():
    ok, reasons = validator.hard_filter(
        _row(parameter_count_billion=2.0),
        {"tasks": ["text-generation"], "korean_required": True, "max_parameters_billion": 3.0},
    )
    assert ok is True
    assert reasons == []


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
