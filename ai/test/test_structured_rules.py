"""structured_rules 판정 규칙 self-check. 실제 코퍼스 값 모양을 그대로 쓴다."""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    "structured_rules", ROOT / "retrieval_lab" / "structured_rules.py"
)
rules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rules)


def model(model_id="x/y", **meta):
    return {"model_id": model_id, "filter_metadata": meta}


def test_numeric_three_states():
    """조건 값이 없으면 통과도 위반도 아니다. 코퍼스의 39%가 이 상태다."""
    cond = {"max_parameters_billion": 0.05}
    assert rules.verdict(model(parameter_count_billion=0.03), cond) is True
    assert rules.verdict(model(parameter_count_billion=2.0), cond) is False
    assert rules.verdict(model(parameter_count_billion=None), cond) is None
    # 필드 자체가 없는 경우도 판정 불가다.
    assert rules.verdict(model(), cond) is None


def test_context_minimum():
    cond = {"min_context_length": 8192}
    assert rules.verdict(model(context_length=32768), cond) is True
    assert rules.verdict(model(context_length=512), cond) is False
    assert rules.verdict(model(context_length=None), cond) is None


def test_license_policy_follows_golden_readme():
    """apache/mit은 허용, nc는 위반, other/gemma/미기재는 확인 필요."""
    cond = {"license_requirement": "commercial"}
    assert rules.verdict(model(license="apache-2.0"), cond) is True
    assert rules.verdict(model(license="mit"), cond) is True
    assert rules.verdict(model(license="cc-by-nc-4.0"), cond) is False
    assert rules.verdict(model(license="cc-by-nc-sa-2.0"), cond) is False
    assert rules.verdict(model(license="other"), cond) is None
    assert rules.verdict(model(license="gemma"), cond) is None
    assert rules.verdict(model(license=None), cond) is None
    # cc-by-4.0은 nc가 아니므로 허용. 'nc'를 부분 문자열로 찾으면 안 된다.
    assert rules.verdict(model(license="cc-by-4.0"), cond) is True

    # 상업 조건이 없는 질의에서는 라이선스를 보지 않는다.
    assert rules.verdict(model(license="cc-by-nc-4.0"), {}) is True


def test_violation_beats_unknown():
    """위반이 판정 불가보다 우선한다. 하나라도 어기면 그 모델은 오답이다."""
    cond = {"max_parameters_billion": 0.05, "min_context_length": 8192}
    row = model(parameter_count_billion=12.0, context_length=None)
    assert rules.verdict(row, cond) is False
    assert rules.violated_fields(row, cond) == ["parameters"]
    assert rules.unknown_fields(row, cond) == ["context"]


def test_task_matching_uses_both_fields():
    cond = {"tasks": ["feature-extraction", "sentence-similarity"]}
    assert rules.verdict(model(primary_task="sentence-similarity"), cond) is True
    # primary가 달라도 matched에 있으면 통과
    assert rules.verdict(
        model(primary_task="text-generation",
              matched_tasks=["feature-extraction"]), cond) is True
    assert rules.verdict(model(primary_task="translation", matched_tasks=[]), cond) is False
    # task 정보가 전혀 없으면 판정 불가
    assert rules.verdict(model(), cond) is None


def test_conditions_of_reads_query_fields():
    query = {
        "tasks": ["question-answering"],
        "max_parameters_billion": 0.05,
        "min_context_length": None,
        "license_requirement": "any",
        "korean_required": True,
    }
    cond = rules.conditions_of(query)
    assert cond["tasks"] == ["question-answering"]
    assert cond["max_parameters_billion"] == 0.05
    # 값이 없는 조건은 넣지 않는다.
    assert "min_context_length" not in cond
    assert "license_requirement" not in cond
    assert cond["korean_required"] is True


def test_score_splits_three_ways():
    corpus = {
        "ok": model("ok", parameter_count_billion=0.03, korean_verified=True),
        "bad": model("bad", parameter_count_billion=12.0, korean_verified=True),
        "unknown": model("unknown", parameter_count_billion=None, korean_verified=True),
        "ok2": model("ok2", parameter_count_billion=0.01, korean_verified=True),
    }
    cond = {"max_parameters_billion": 0.05, "korean_required": True}
    out = rules.score(["ok", "bad", "unknown", "ok2"], corpus, cond, ks=(4,))
    assert out["cond_ok@4"] == 0.5
    assert out["cond_violation@4"] == 0.25
    assert out["cond_unknown@4"] == 0.25
    # 세 비율의 합은 항상 1이다.
    assert abs(sum(out.values()) - 1.0) < 1e-9


def test_no_conditions_means_pass():
    assert rules.verdict(model(), {}) is True


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
