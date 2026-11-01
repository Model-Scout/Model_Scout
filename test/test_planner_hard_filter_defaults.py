"""유형별 hard filter 기본값 self-check.

계획서는 Planner가 Query Type에 따라 Hard Filter를 선택한다고 적었지만
구현은 질의에 적힌 값만 썼다. 이 테스트는 추가한 기본값이

  - 기존 유형의 동작을 바꾸지 않는지
  - 질의 값이 언제나 우선하는지 (False로 끄는 것까지)
  - 짝이 되는 수치 조건이 없을 때 기본값이 빠지는지
  - 실험 경로와 서비스 경로가 같은 필터를 만드는지

를 확인한다. 마지막 항목이 핵심이다. 처음에는 수치 조건 확인이
experiment.evaluate 쪽에만 있어서, 수치 조건 없는 질의 9/24가
측정한 적 없는 설정으로 서비스될 상태였다.
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("planner", ROOT / "retrieval_lab" / "planner.py")
planner = importlib.util.module_from_spec(spec)
sys.modules["planner"] = planner
spec.loader.exec_module(planner)

KNOWN_ONLY = {"require_known_parameters": True, "require_known_context": True}


def test_type_without_defaults_is_unchanged():
    """기본값이 없는 유형은 예전과 똑같이 질의 값만 쓴다."""
    config = {"types": {"model_comparison": {"dense_weight": 0.5, "use_name_lookup": True}}}
    plan = planner.plan_for("model_comparison", {"tasks": ["text-generation"]}, config)
    assert plan.hard_filters == {"tasks": ["text-generation"]}
    assert plan.use_name_lookup is True


def test_defaults_apply_when_query_is_silent():
    config = {"types": {"structured_constraint": {
        "dense_weight": 0.5,
        "hard_filter_defaults": {"require_known_parameters": True},
    }}}
    plan = planner.plan_for("structured_constraint",
                            {"max_parameters_billion": 1.0}, config)
    assert plan.hard_filters["require_known_parameters"] is True
    assert plan.hard_filters["max_parameters_billion"] == 1.0


def test_query_can_turn_the_default_off():
    """질의가 명시한 False가 유형 기본값을 끈다.

    hard_filters()가 False를 버리던 동안에는 기본값 True가 남아서
    사용자가 필터를 끌 방법이 없었다.
    """
    config = {"types": {"structured_constraint": {
        "hard_filter_defaults": {"require_known_parameters": True},
    }}}
    plan = planner.plan_for("structured_constraint",
                            {"max_parameters_billion": 1.0,
                             "require_known_parameters": False}, config)
    assert plan.hard_filters["require_known_parameters"] is False

    plan = planner.plan_for("structured_constraint",
                            {"max_parameters_billion": 1.0,
                             "require_known_parameters": True}, config)
    assert plan.hard_filters["require_known_parameters"] is True


def test_default_drops_without_a_paired_numeric_condition():
    """수치 조건이 없으면 유형 기본값은 빠진다.

    상한도 하한도 없는 질의에서 "값을 안다"는 이유로 후보를 거르면
    멀쩡한 모델만 잃는다. parameter_count가 없는 2점 정답이 실제로 있다
    (sg_g019의 SungBeom/stt_kr_conformer_ctc_medium, .nemo 단일 파일).
    """
    config = {"types": {"structured_constraint": {"hard_filter_defaults": dict(KNOWN_ONLY)}}}

    plan = planner.plan_for("structured_constraint", {"korean_required": True}, config)
    assert "require_known_parameters" not in plan.hard_filters
    assert "require_known_context" not in plan.hard_filters

    # 파라미터 조건만 있으면 파라미터 플래그만 남는다.
    plan = planner.plan_for("structured_constraint",
                            {"max_parameters_billion": 1.0}, config)
    assert plan.hard_filters["require_known_parameters"] is True
    assert "require_known_context" not in plan.hard_filters

    # context 조건만 있으면 context 플래그만 남는다.
    plan = planner.plan_for("structured_constraint",
                            {"min_context_length": 32768}, config)
    assert plan.hard_filters["require_known_context"] is True
    assert "require_known_parameters" not in plan.hard_filters


def test_query_flag_survives_without_a_numeric_condition():
    """질의가 직접 켠 플래그는 수치 조건이 없어도 남는다. 사용자 의도가 우선이다."""
    config = {"types": {"structured_constraint": {}}}
    plan = planner.plan_for("structured_constraint",
                            {"require_known_parameters": True}, config)
    assert plan.hard_filters["require_known_parameters"] is True


def test_experiment_and_service_paths_agree():
    """실험(hard_filter_plan)과 서비스(plan_for)가 같은 필터를 만든다.

    experiment.evaluate가 hard_filter_plan을 그대로 쓰므로, plan의
    hard_filters를 기본값으로 넘기면 plan_for와 결과가 같아야 한다.
    """
    config = {"types": {"structured_constraint": {"hard_filter_defaults": dict(KNOWN_ONLY)}}}
    queries = [
        {"korean_required": True},                                 # 수치 조건 없음
        {"max_parameters_billion": 1.0},                           # 파라미터 조건
        {"min_context_length": 32768},                             # context 조건
        {"max_parameters_billion": 1.0, "require_known_parameters": False},  # 질의가 끔
        {},                                                        # 빈 질의
    ]
    for query in queries:
        service = planner.plan_for("structured_constraint", query, config).hard_filters
        experiment = planner.hard_filter_plan(KNOWN_ONLY, query)
        assert service == experiment, (query, service, experiment)


def test_save_round_trip():
    import json
    import tempfile

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "planner_config.json"
        plan = planner.replace(planner.BASELINE, query_type="structured_constraint")
        planner.save_type_plan("structured_constraint", plan, {"metric": "recall@10"},
                               path=path, hard_filter_defaults=dict(KNOWN_ONLY))
        saved = json.loads(path.read_text(encoding="utf-8"))
        assert saved["types"]["structured_constraint"]["hard_filter_defaults"] == KNOWN_ONLY

        # 저장한 기본값은 수치 조건이 있는 질의에서 살아난다.
        back = planner.plan_for("structured_constraint", {"max_parameters_billion": 1.0}, saved)
        assert back.hard_filters["require_known_parameters"] is True

        # 빈 질의에서는 걸리지 않는다.
        back = planner.plan_for("structured_constraint", {}, saved)
        assert back.hard_filters == {}


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
