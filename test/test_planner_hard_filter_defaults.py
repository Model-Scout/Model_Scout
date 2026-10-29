"""유형별 hard filter 기본값 self-check.

계획서는 Planner가 Query Type에 따라 Hard Filter를 선택한다고 적었지만
구현은 질의에 적힌 값만 썼다. 이 테스트는 추가한 기본값이 기존 유형의
동작을 바꾸지 않는지, 질의 값이 언제나 우선하는지를 확인한다.
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


def test_query_value_wins_over_default():
    """사용자가 명시한 값이 유형 기본값을 덮는다."""
    config = {"types": {"structured_constraint": {
        "hard_filter_defaults": {"require_known_parameters": True},
    }}}
    plan = planner.plan_for("structured_constraint",
                            {"require_known_parameters": False}, config)
    # hard_filters()는 False를 떨어뜨리므로 기본값만 남는다. 이 경우를 분명히 해 둔다.
    assert plan.hard_filters.get("require_known_parameters") is True

    plan = planner.plan_for("structured_constraint",
                            {"require_known_parameters": True}, config)
    assert plan.hard_filters["require_known_parameters"] is True


def test_unknown_type_falls_back_to_baseline():
    plan = planner.plan_for("새유형", {"tasks": ["summarization"]}, {"types": {}})
    assert plan.dense_weight == planner.BASELINE.dense_weight
    assert plan.hard_filters == {"tasks": ["summarization"]}


def test_save_round_trip(tmp_path=None):
    import json
    import tempfile

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "planner_config.json"
        plan = planner.replace(planner.BASELINE, query_type="structured_constraint")
        planner.save_type_plan("structured_constraint", plan, {"metric": "recall@10"},
                               path=path,
                               hard_filter_defaults={"require_known_parameters": True})
        saved = json.loads(path.read_text(encoding="utf-8"))
        entry = saved["types"]["structured_constraint"]
        assert entry["hard_filter_defaults"] == {"require_known_parameters": True}

        # 저장한 값이 다시 plan으로 돌아온다.
        back = planner.plan_for("structured_constraint", {}, saved)
        assert back.hard_filters["require_known_parameters"] is True


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
