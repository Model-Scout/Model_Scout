"""전체 재적재(``--reingest``)의 안전장치를 확인한다.

이 셋은 전부 "조용히 틀리는" 종류의 사고를 막는다. 실행은 성공하고 숫자만
어긋나므로 테스트가 없으면 적재가 끝난 뒤에야 알게 된다.

① watermark 를 전진시키지 않는다
     재적재는 Stage 1 을 스캔하지 않는다. 자기 시작 시각을 watermark 로 올리면
     직전 스캔 이후부터 재적재 사이에 Hub 에서 바뀐 모델을 다음 --refresh 가
     영구히 건너뛴다. 그 구간은 아무도 본 적이 없다.

② 언어 게이트 제외분을 DB 에서 비활성화한다
     apply_sync 는 incremental 모드에서 removed_ids 만 비활성화한다. 빈 배열을
     넘기면 새로 제외된 모델이 낡은 데이터로 계속 active 로 남는다.

③ Stage 2 가 대량 실패하면 끊는다
     실패한 모델은 출력에서 그냥 사라지므로 뒤 단계에서는 "원래 없던 모델"과
     구별되지 않는다. 적재까지 가면 그 행들이 전부 비활성화돼 복구가 번거롭다.

    python test/test_reingest_safety.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location("sync_for_reingest_test", ROOT / "08_sync_supabase.py")
assert SPEC is not None and SPEC.loader is not None
sync = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sync
SPEC.loader.exec_module(sync)


# ── ① watermark ───────────────────────────────────────────────────────────

def test_reingest_carries_the_previous_watermark():
    """재적재는 직전 watermark 를 그대로 물려받는다."""
    latest = {
        "completed_at": "2026-11-06T00:00:00+00:00",
        "stage_versions": {"source_watermark": "2026-10-31T06:44:44.365898+00:00"},
    }
    assert sync.carried_watermark(latest) == "2026-10-31T06:44:44.365898+00:00"


def test_carried_watermark_falls_back_to_completed_at():
    """source_watermark 가 없던 옛 기록은 완료 시각을 쓴다."""
    assert sync.carried_watermark({"completed_at": "2026-11-06T00:00:00+00:00"}) == "2026-11-06T00:00:00+00:00"


def test_carried_watermark_is_none_without_a_prior_sync():
    assert sync.carried_watermark(None) is None
    assert sync.carried_watermark({}) is None


def test_reingest_does_not_advance_the_watermark():
    """핵심 불변식. 재적재가 저장하는 watermark 는 직전 값과 같아야 한다."""
    previous = "2026-10-31T06:44:44.365898+00:00"
    refresh_info = {
        "mode": "reingest",
        "started_at": "2026-11-20T09:00:00+00:00",   # 재적재 시작 시각
        "source_watermark": previous,
    }
    stored = sync.resolved_source_watermark(refresh_info)
    assert stored == previous, "재적재가 watermark 를 전진시켰다"
    assert stored != refresh_info["started_at"]


def test_refresh_still_advances_the_watermark():
    """--refresh 는 Stage 1 을 실제로 스캔하므로 전진해야 한다."""
    refresh_info = {"scan_started_at": "2026-11-20T09:00:00+00:00"}
    assert sync.resolved_source_watermark(refresh_info) == "2026-11-20T09:00:00+00:00"


def test_reingest_without_a_prior_watermark_stores_nothing():
    """None 을 돌려주면 apply_sync 가 stage_versions 에 키를 넣지 않는다.

    scan_started_at 으로 조용히 흘러내려 재적재 시각이 박히면 안 된다.
    """
    assert sync.resolved_source_watermark({"source_watermark": None, "started_at": "x"}) is None


# ── ② 언어 게이트 제외분 ──────────────────────────────────────────────────

def test_language_excluded_ids_reads_both_pools():
    with tempfile.TemporaryDirectory() as name:
        data = Path(name)
        (data / "hf_models_stage2_core_language_excluded.json").write_text(
            json.dumps({"org/ja-only": "japanese README"}), encoding="utf-8")
        (data / "hf_models_stage2_low_popularity_language_excluded.json").write_text(
            json.dumps({"org/zh-only": "chinese README"}), encoding="utf-8")
        assert sync.language_excluded_ids(data) == {"org/ja-only", "org/zh-only"}


def test_language_excluded_ids_is_empty_without_reports():
    with tempfile.TemporaryDirectory() as name:
        assert sync.language_excluded_ids(Path(name)) == set()


# ── ③ Stage 2 대량 실패 가드 ──────────────────────────────────────────────

def test_volume_guard_accepts_the_current_corpus_shape():
    """실제 수치: Stage 1 3,886 행에서 언어 게이트 14 건을 빼면 3,872 행이다."""
    sync.assert_stage2_volume(expected=3886, produced=3872, excluded=14)


def test_volume_guard_accepts_a_small_transient_shortfall():
    """개별 모델의 일시적 조회 실패는 통과시킨다. 2% 폭이다."""
    sync.assert_stage2_volume(expected=3886, produced=3800, excluded=14)


def test_volume_guard_blocks_a_mass_failure():
    """절반이 사라지면 끊는다."""
    try:
        sync.assert_stage2_volume(expected=3886, produced=1900, excluded=14)
    except RuntimeError as error:
        assert "대량 실패" in str(error)
        assert "1900" in str(error)
    else:
        raise AssertionError("대량 실패를 통과시켰다")


def test_volume_guard_blocks_an_empty_result():
    try:
        sync.assert_stage2_volume(expected=3886, produced=0, excluded=14)
    except RuntimeError:
        pass
    else:
        raise AssertionError("빈 결과를 통과시켰다")


def test_volume_guard_does_not_punish_language_exclusions():
    """언어 게이트가 많이 떨어뜨린 것은 정상 감소다. 분모에서 빠져야 한다."""
    # 500 건이 제외되면 3,386 행이 기대치다. 그 값으로 통과해야 한다.
    sync.assert_stage2_volume(expected=3886, produced=3386, excluded=500)
    # 같은 3,386 행인데 제외가 없었다면 대량 실패다.
    try:
        sync.assert_stage2_volume(expected=3886, produced=3386, excluded=0)
    except RuntimeError:
        pass
    else:
        raise AssertionError("제외 없이 500 행이 사라진 것을 통과시켰다")


def test_volume_floor_matches_the_tolerance():
    assert sync.stage2_volume_floor(1000, 0) == 980.0
    assert sync.stage2_volume_floor(1000, 100) == 882.0
    # 제외가 전체보다 많다고 음수가 되면 안 된다.
    assert sync.stage2_volume_floor(10, 50) == 0.0


def test_volume_guard_skips_when_stage1_is_empty():
    """Stage 1 스냅샷이 없으면 비교 기준이 없다. 가드를 적용하지 않는다."""
    sync.assert_stage2_volume(expected=0, produced=0, excluded=0)


# ── ④ 재적재가 돌려주는 값이 적재 호출부로 흘러가는지 ──────────────────────

def _result(**over):
    kwargs = {
        "previous_watermark": "2026-10-31T06:44:44.365898+00:00",
        "started_at": "2026-11-20T09:00:00+00:00",
        "steps": ["stage2:3872rows"],
        "contract_gate_report": {},
        "language_excluded": {"org/ja-only", "org/zh-only"},
        "stage2_rows": 3872,
    }
    kwargs.update(over)
    return sync.reingest_result(**kwargs)


def test_language_exclusions_reach_removed_ids():
    """제외된 모델이 removed_ids 로 가야 apply_sync 가 비활성화한다.

    apply_sync 는 incremental 모드에서 removed_ids 만 비활성화한다. 여기가 비면
    새로 제외된 모델이 낡은 데이터로 계속 active 로 남는다.
    """
    result = _result()
    assert result["removed_ids"] == ["org/ja-only", "org/zh-only"]


def test_removed_ids_is_empty_only_when_nothing_was_excluded():
    assert _result(language_excluded=set())["removed_ids"] == []


def test_result_carries_the_previous_watermark_not_the_start_time():
    result = _result()
    assert sync.resolved_source_watermark(result) == "2026-10-31T06:44:44.365898+00:00"
    assert sync.resolved_source_watermark(result) != result["started_at"]


def test_result_requests_a_full_stage4_sync():
    """재적재는 전체 행을 올린다. delta 로 가면 바뀐 행만 적재된다."""
    result = _result()
    assert result["stage4_mode"] == "full"
    assert result["requires_sync"] is True


def test_result_reports_the_row_count_it_validated():
    assert _result(stage2_rows=3872)["stage2_rows"] == 3872


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
