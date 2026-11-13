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

⑤ --full-stage1 (Stage 1 전체 재스캔)
     스캔 시작 시각이 watermark 가 되고, Stage 1 전후 diff 가 보고되고, 새 Stage 1
     이 처리 대상을 너무 많이 잃거나 DB 비활성화 후보가 너무 많으면 멈춘다.
     dry-run 은 DB 를 읽기만 하고, apply 만 같은 트랜잭션 안에서 다시 계산해 쓴다.

네트워크·DB 를 부르지 않는다. 하위 프로세스와 DB 커서는 전부 가짜다.

    python test/test_reingest_safety.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List

import yaml

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


# ── ⑤ --full-stage1 ──────────────────────────────────────────────────────

SCAN = {
    "scan_started_at": "2026-11-20T09:00:00+00:00",
    "diff": {"previous_processable": 3, "current_processable": 3, "removed_ids": []},
}


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


def test_reuse_reingest_keeps_the_previous_watermark():
    result = _result()
    assert result["stage1_mode"] == "reuse"
    assert result["stage1_diff"] is None
    assert sync.resolved_source_watermark(result) == "2026-10-31T06:44:44.365898+00:00"


def test_full_scan_reingest_stores_the_scan_start_not_the_end():
    """스캔 시작 시각이 watermark 다. 재적재 시작/완료 시각이 아니다."""
    result = _result(stage1_scan=SCAN, started_at="2026-11-20T08:59:00+00:00")
    assert result["stage1_mode"] == "full-scan"
    assert sync.resolved_source_watermark(result) == SCAN["scan_started_at"]
    assert result["previous_watermark"] == "2026-10-31T06:44:44.365898+00:00"
    assert result["stage1_diff"] is SCAN["diff"]


def test_stage1_diff_separates_added_removed_and_pool_moves():
    previous = {
        "core": ["a/core-stays", "a/core-falls"],
        "low_popularity": ["a/low-rises", "a/gone"],
        "likely": ["b/1", "b/2"],
        "fallback": ["c/1"],
    }
    current = {
        "core": ["a/core-stays", "a/low-rises", "a/new"],
        "low_popularity": ["a/core-falls"],
        "likely": ["b/1"],
        "fallback": ["c/1", "c/2", "a/gone"],  # A 에서 C 로 내려간 것도 처리 대상에서는 제거다
    }
    diff = sync.stage1_diff(previous, current)
    assert diff["added_ids"] == ["a/new"]
    assert diff["removed_ids"] == ["a/gone"]
    assert diff["core_to_low_ids"] == ["a/core-falls"]
    assert diff["low_to_core_ids"] == ["a/low-rises"]
    assert diff["previous_processable"] == 4 and diff["current_processable"] == 4
    assert diff["pool_counts"]["current"] == {"core": 3, "low_popularity": 1}
    # A/B/C 후보 분포와 처리 대상(A=Core∪Low)을 섞지 않는다.
    assert diff["candidate_tiers"]["previous"] == {"A_verified": 4, "B_likely": 2, "C_fallback": 1}
    assert diff["candidate_tiers"]["current"] == {"A_verified": 4, "B_likely": 1, "C_fallback": 3}


def _ids(prefix: str, count: int) -> List[str]:
    return [f"{prefix}/{index}" for index in range(count)]


def test_stage1_removal_guard_blocks_a_mass_drop():
    previous = {"core": _ids("a", 1000), "low_popularity": []}
    current = {"core": _ids("a", 650), "low_popularity": []}
    try:
        sync.assert_stage1_removal(sync.stage1_diff(previous, current))
    except sync.Stage1RemovalGuardError as error:
        assert "350" in str(error)
        assert error.diff["removal_guard"]["max_fraction"] == 0.30
        assert len(error.diff["removed_ids"]) == 350
    else:
        raise AssertionError("처리 대상 35% 감소를 통과시켰다")


def test_stage1_removal_guard_allows_the_reviewed_long_gap_churn():
    """2026-11-13 full-scan 실측: 3,886 → 4,015, 제거 957·추가 1,086."""
    previous = {"core": _ids("old", 3886), "low_popularity": []}
    current = {
        "core": _ids("old", 2929) + _ids("new", 1086),
        "low_popularity": [],
    }
    diff = sync.stage1_diff(previous, current)
    guard = sync.assert_stage1_removal(diff)
    assert diff["current_processable"] == 4015
    assert len(diff["removed_ids"]) == 957
    assert len(diff["added_ids"]) == 1086
    assert guard["max_allowed"] == 1165
    assert guard["blocked"] is False


def test_stage1_removal_guard_allows_normal_churn_and_pool_moves():
    previous = {"core": _ids("a", 600), "low_popularity": _ids("l", 400)}
    # 50 개 제거(5%) + Core 600 개가 전부 Low 로 이동. 이동은 제거가 아니다.
    current = {"core": [], "low_popularity": _ids("a", 600) + _ids("l", 350)}
    guard = sync.assert_stage1_removal(sync.stage1_diff(previous, current))
    assert guard["count"] == 50 and guard["blocked"] is False


def test_stage1_removal_guard_skips_a_tiny_baseline():
    diff = sync.stage1_diff({"core": _ids("a", 10)}, {"core": []})
    assert sync.assert_stage1_removal(diff)["blocked"] is False


def test_stage1_partition_ids_reads_every_partition():
    with tempfile.TemporaryDirectory() as name:
        data = Path(name)
        for partition, filename in sync.STAGE1_PARTITIONS.items():
            (data / filename).write_text(json.dumps({"model_id": f"x/{partition}"}) + "\n", encoding="utf-8")
        ids = sync.stage1_partition_ids(data)
        assert ids == {partition: [f"x/{partition}"] for partition in sync.STAGE1_PARTITIONS}
        assert sync.stage1_partition_ids(Path(name) / "missing")["core"] == []


def test_deactivation_plan_full_scan_uses_the_db_not_local_files():
    """비활성화 후보 = DB active - 새 Stage 4. 로컬 옛 Stage 4 는 보지 않는다."""
    plan = sync.deactivation_plan(
        db_active_ids=["m/keep", "m/db-only", "m/lang"],
        stage4_ids=["m/keep", "m/new"],
        removed_ids=["m/lang", "m/never-active"],
        deactivate_missing=True,
    )
    assert plan["candidate_ids"] == ["m/db-only", "m/lang"]
    assert plan["db_only_ids"] == ["m/db-only", "m/lang"]
    assert plan["candidate_count"] == 2


def test_deactivation_plan_reuse_only_drops_language_exclusions():
    """Stage 1 재사용은 예전 동작 그대로. DB 에만 있는 행은 보고만 한다."""
    plan = sync.deactivation_plan(
        ["m/keep", "m/db-only", "m/lang"], ["m/keep"], ["m/lang"], deactivate_missing=False,
    )
    assert plan["candidate_ids"] == ["m/lang"]
    assert plan["db_only_ids"] == ["m/db-only", "m/lang"]


def test_deactivation_guard_blocks_too_many_candidates():
    active = _ids("m", 1000)
    plan = sync.deactivation_plan(active, active[:650], deactivate_missing=True)
    assert plan["guard"]["blocked"] is True
    try:
        sync.assert_deactivation_plan(plan)
    except RuntimeError as error:
        assert "350" in str(error)
    else:
        raise AssertionError("35% 비활성화를 통과시켰다")
    ok = sync.deactivation_plan(active, active[:750], deactivate_missing=True)
    sync.assert_deactivation_plan(ok)


def test_stage1_guard_failure_report_preserves_the_full_diff():
    diff = sync.stage1_diff(
        {"core": _ids("old", 1000), "low_popularity": []},
        {"core": _ids("old", 650), "low_popularity": []},
    )
    captured = None
    try:
        sync.assert_stage1_removal(diff)
    except sync.Stage1RemovalGuardError as error:
        error.scan_started_at = "2026-11-13T00:00:00+00:00"
        captured = error
    else:
        raise AssertionError("가드 실패 보고서 테스트가 차단되지 않았다")

    with tempfile.TemporaryDirectory() as name:
        path = Path(name) / "reingest-report.json"
        sync.write_reingest_report(sync.stage1_guard_failure_result(captured), path)
        report = json.loads(path.read_text(encoding="utf-8"))
        stored = json.loads((Path(name) / "reingest-report.stage1-diff.json").read_text(encoding="utf-8"))
        summary = json.loads((Path(name) / "reingest-report.summary.json").read_text(encoding="utf-8"))
        assert report["db_write"] is False
        assert report["error"]["failed_before"] == "stage2"
        assert stored["removed_ids"] == captured.diff["removed_ids"]
        assert stored["removal_guard"]["blocked"] is True
        assert summary["stage1_diff"]["removed"] == 350


# ── apply_sync: 가짜 DB 로 실제 SQL 흐름을 본다 ───────────────────────────────

class FakeCursor:
    def __init__(self, db: "FakeDb"):
        self.db = db
        self.rowcount = 0
        self._rows: List[Any] = []

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, sql: str, params: Any = None) -> None:
        text = " ".join(sql.split())
        self.db.statements.append((text, params))
        self._rows = []
        self.rowcount = 0
        if "from pg_extension" in text:
            self._rows = [(1,)]
        elif text.startswith("select model_id from public.model_scout_models where active = true"):
            self._rows = [(model_id,) for model_id in sorted(self.db.active)]
        elif text.startswith("update public.model_scout_models set active = false"):
            if params and isinstance(params[0], list):
                hit = self.db.active & set(params[0])
            else:
                hit = set(self.db.active) - self.db.upserted
            self.db.deactivated |= hit
            self.rowcount = len(hit)

    def fetchone(self):
        return self._rows[0] if self._rows else None

    def fetchall(self):
        return list(self._rows)


class FakeDb:
    def __init__(self, active: List[str]):
        self.active = set(active)
        self.upserted: set = set()
        self.statements: List[Any] = []
        self.deactivated: set = set()
        self.committed = False
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, *rest):
        self.committed = exc_type is None
        return False

    def cursor(self):
        return FakeCursor(self)

    def rollback(self):
        self.committed = False

    def commit(self):
        pass

    def close(self):
        self.closed = True

    def writes(self) -> List[str]:
        return [sql for sql, _ in self.statements if sql.split()[0] in ("insert", "update", "delete")]


def _run_apply_sync(db: FakeDb, **kwargs: Any) -> Dict[str, Any]:
    import psycopg2.extras

    def execute_values(cur, statement, rows, **_):
        cur.db.statements.append((" ".join(statement.split()), list(rows)))
        if "model_scout_models" in statement:
            cur.db.upserted |= {row[0] for row in rows}

    with patched(sync, db_connection=lambda: db), patched(psycopg2.extras, execute_values=execute_values):
        return sync.apply_sync(
            [("m/keep",)], [], "00000000-0000-0000-0000-000000000001", 100, **kwargs
        )


def _sync_run_versions(db: FakeDb) -> Dict[str, Any]:
    for sql, params in db.statements:
        if sql.startswith("insert into public.model_scout_sync_runs"):
            return json.loads(params[1])
    raise AssertionError("sync run 기록이 없다")


def test_apply_full_scan_deactivates_missing_active_models_and_records_reingest():
    db = FakeDb(active=["m/keep", "m/db-only", "m/lang"] + _ids("pad", 100))
    stage4 = ["m/keep"] + _ids("pad", 100)
    result = _run_apply_sync(
        db,
        sync_mode="reingest",
        removed_ids=["m/lang"],
        deactivate_missing=True,
        stage4_ids=stage4,
        source_watermark=SCAN["scan_started_at"],
        extra_versions={"stage1_mode": "full-scan"},
    )
    assert db.deactivated == {"m/db-only", "m/lang"}
    assert result["deactivated"] == 2
    assert result["deactivation"]["candidate_ids"] == ["m/db-only", "m/lang"]
    versions = _sync_run_versions(db)
    assert versions["sync_mode"] == "reingest", "전체 재적재를 initial/incremental 로 기록했다"
    assert versions["stage1_mode"] == "full-scan"
    assert versions["source_watermark"] == SCAN["scan_started_at"]
    # "이번 run 이 안 본 행 전부" 를 끄는 initial 식 UPDATE 를 쓰지 않는다.
    assert not any("last_seen_run is distinct from" in sql for sql in db.writes())


def test_apply_reuse_reingest_keeps_the_old_deactivation_scope():
    db = FakeDb(active=["m/keep", "m/db-only", "m/lang"])
    _run_apply_sync(
        db, sync_mode="reingest", removed_ids=["m/lang"],
        deactivate_missing=False, stage4_ids=["m/keep"],
    )
    assert db.deactivated == {"m/lang"}
    assert _sync_run_versions(db)["sync_mode"] == "reingest"


def test_apply_aborts_before_any_write_when_the_deactivation_guard_trips():
    active = _ids("m", 1000)
    db = FakeDb(active=active)
    try:
        _run_apply_sync(db, sync_mode="reingest", deactivate_missing=True, stage4_ids=active[:500])
    except RuntimeError:
        pass
    else:
        raise AssertionError("비활성화 50% 를 적재했다")
    assert db.deactivated == set()
    assert not db.committed
    assert not any(sql.startswith("insert into public.model_scout_models") for sql in db.writes())


def test_apply_initial_and_incremental_keep_their_modes():
    db = FakeDb(active=["m/keep", "m/old"])
    _run_apply_sync(db, sync_mode="initial")
    assert _sync_run_versions(db)["sync_mode"] == "initial"
    assert db.deactivated == {"m/old"}

    db = FakeDb(active=["m/keep", "m/old", "m/removed"])
    _run_apply_sync(db, sync_mode="incremental", removed_ids=["m/removed"])
    assert _sync_run_versions(db)["sync_mode"] == "incremental"
    assert db.deactivated == {"m/removed"}


def test_apply_rejects_unknown_modes_and_misused_policy():
    for kwargs in ({"sync_mode": "full"}, {"sync_mode": "incremental", "deactivate_missing": True}):
        try:
            _run_apply_sync(FakeDb([]), **kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError(f"잘못된 조합을 받았다: {kwargs}")


def test_next_refresh_reads_the_reingest_watermark():
    """reingest 로 기록한 run 을 다음 --refresh 가 watermark 기준으로 읽어야 한다."""
    db = FakeDb([])
    with patched(sync, db_connection=lambda: db):
        sync.latest_completed_sync()
    query, params = db.statements[0]
    assert "'reingest'" in query
    # --refresh 는 지금 버전의 run 만 기준으로 삼는다.
    assert params[0] is False and json.loads(params[1]) == sync.EXPECTED_VERSIONS


def test_reingest_lookup_ignores_stage_versions():
    """DB 의 마지막 run 은 stage2=6 인데 코드는 7 이다. 버전으로 거르면 재적재 apply 가
    "sync 기록 없음"으로 멈춘다. 재적재는 버전을 올리는 작업이므로 버전을 따지지 않는다."""
    db = FakeDb([])
    with patched(sync, db_connection=lambda: db):
        sync.latest_completed_sync(any_versions=True)
    assert db.statements[0][1][0] is True


# ── main(): dry-run 은 DB 에 쓰지 않는다 ─────────────────────────────────────

MB = 1_000_000


def _run_main(argv: List[str], *, active: List[str], calls: Dict[str, Any], apply_sync: Any = None,
              database_mb: float = 300, pipeline_error: Any = None) -> int:
    import io

    stage4 = [{"model_id": "m/keep", "source_pool": "core"}]

    def fake_pipeline(previous, full_stage1=False):
        calls["pipeline"] = {"previous": previous, "full_stage1": full_stage1}
        if pipeline_error is not None:
            raise pipeline_error
        return _result(
            previous_watermark=previous,
            stage1_scan=SCAN if full_stage1 else None,
            language_excluded={"m/lang"},
        )

    def refuse(*args, **kwargs):
        raise AssertionError("dry-run 이 DB 쓰기 경로를 불렀다")

    # 승인한 dry-run 번들. apply 는 이것만 적재하고 Stage 1~4 를 다시 돌리지 않는다.
    approved = _result(previous_watermark="2026-10-31T00:00:00+00:00", language_excluded={"m/lang"})

    def verify_bundle(bundle_dir, **expected):
        calls["bundle_expected"] = expected
        return {"reingest": approved, "dry_run_run_id": expected["approved_run_id"],
                "git_sha": "abc", "bundle_sha256": "f" * 64, "model_count": 1,
                "model_ids_sha256": sync.model_ids_sha256({"m/keep"})}

    def no_pipeline_on_apply(previous, full_stage1=False):
        if "--apply" in argv:
            raise AssertionError("apply 가 Stage 1~4 를 다시 만들었다")
        return fake_pipeline(previous, full_stage1)

    # 실제 DB 처럼 옛 Stage 2 버전으로 끝난 run 이다.
    latest = {"completed_at": "2026-11-06T00:00:00+00:00",
              "stage_versions": {"stage2": 6, "source_watermark": "2026-10-31T00:00:00+00:00"}}
    lookups: List[bool] = []

    def latest_completed_sync(any_versions=False):
        lookups.append(any_versions)
        # 버전을 따지는 조회는 옛 run 을 찾지 못한다.
        return latest if any_versions else None

    with contextlib.ExitStack() as stack:
        stack.enter_context(patched(
            sync,
            load_dotenv=lambda *a, **k: None,
            latest_completed_sync=latest_completed_sync,
            full_reingest_pipeline=no_pipeline_on_apply,
            verify_reingest_bundle=verify_bundle,
            install_reingest_bundle=lambda bundle_dir, manifest: calls.setdefault("installed", bundle_dir),
            git_identity=lambda: {"repository": "Model-Scout/Model_Scout", "git_sha": "abc",
                                  "git_ref": "main", "run_id": "999"},
            load_corpora=lambda stage4_delta=False: (stage4, {"m/keep": {}}, {"m/keep": {}}),
            validate_corpus=lambda *a, **k: {"rows": len(stage4), "pool_counts": {"core": 1}},
            load_evidence_indices=lambda: {},
            validate_evidence_indices=lambda *a, **k: {},
            write_stage4_manifest=lambda *a, **k: None,
            payloads=lambda *a, **k: [],
            evidence_payloads=lambda *a, **k: [],
            db_active_model_ids=lambda cur=None: set(active),
            db_storage=lambda cur=None: {"database": int(database_mb * MB), "model_scout_models": 80 * MB,
                                         "model_scout_evidence": 10 * MB, "model_scout_dataset_chunks": 190 * MB,
                                         "model_scout_datasets": 20 * MB},
            estimate_write_bytes=lambda *args, **kwargs: 100 * MB,
            apply_sync=apply_sync or refuse,
            ensure_schema=refuse,
            promote_benchmark_state=lambda: None,
            clear_incremental_artifacts=lambda: None,
        ))
        stack.enter_context(patched(sys, argv=["08_sync_supabase.py", *argv]))
        stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
        code = sync.main()
    calls["lookups"] = lookups
    return code


def test_dry_run_full_scan_reports_without_writing():
    calls: Dict[str, Any] = {}
    with tempfile.TemporaryDirectory() as name:
        report = Path(name) / "reingest-report.json"
        code = _run_main(
            ["--reingest", "--full-stage1", "--report", str(report)],
            active=["m/keep", "m/db-only", "m/lang"], calls=calls,
        )
        assert code == 0
        assert calls["pipeline"] == {"previous": "2026-10-31T00:00:00+00:00", "full_stage1": True}
        result = json.loads(report.read_text(encoding="utf-8"))
        assert result["apply"] is False and result["dry_run"]["db_write"] is False
        assert result["sync_mode"] == "reingest"
        assert result["deactivation"]["candidate_ids"] == ["m/db-only", "m/lang"]
        # 예상 watermark 는 기록만 한다.
        assert result["dry_run"]["expected_source_watermark"] == SCAN["scan_started_at"]
        summary = json.loads((Path(name) / "reingest-report.summary.json").read_text(encoding="utf-8"))
        assert summary["stage1_mode"] == "full-scan"
        assert summary["deactivation_candidates"] == 2
        assert summary["stage4_rows"] == 1
        assert "candidate_ids" not in json.dumps(summary)
        assert (Path(name) / "reingest-report.stage1-diff.json").exists()
        assert (Path(name) / "reingest-report.deactivation.json").exists()


def test_main_persists_the_stage1_diff_when_the_guard_stops_the_pipeline():
    diff = sync.stage1_diff(
        {"core": _ids("old", 1000), "low_popularity": []},
        {"core": _ids("old", 650), "low_popularity": []},
    )
    try:
        sync.assert_stage1_removal(diff)
    except sync.Stage1RemovalGuardError as error:
        error.scan_started_at = "2026-11-13T00:00:00+00:00"
        blocked = error
    else:
        raise AssertionError("가드 실패 경로가 차단되지 않았다")

    with tempfile.TemporaryDirectory() as name:
        report = Path(name) / "reingest-report.json"
        try:
            _run_main(
                ["--reingest", "--full-stage1", "--report", str(report)],
                active=["m/keep"],
                calls={},
                pipeline_error=blocked,
            )
        except sync.Stage1RemovalGuardError:
            pass
        else:
            raise AssertionError("가드 실패를 Action 실패로 전파하지 않았다")
        assert report.exists()
        stored = json.loads((Path(name) / "reingest-report.stage1-diff.json").read_text(encoding="utf-8"))
        assert stored["removed_ids"] == blocked.diff["removed_ids"]
        assert stored["removal_guard"]["blocked"] is True


def test_dry_run_marks_a_blocked_deactivation_as_failure():
    calls: Dict[str, Any] = {}
    with tempfile.TemporaryDirectory() as name:
        report = Path(name) / "r.json"
        code = _run_main(
            ["--reingest", "--full-stage1", "--report", str(report)],
            active=["m/keep"] + _ids("gone", 200), calls=calls,
        )
        assert code == 3
        assert json.loads(report.read_text(encoding="utf-8"))["deactivation"]["guard"]["blocked"]


APPLY_BUNDLE = ["--from-bundle", "reingest-bundle", "--approved-run-id", "123"]


def test_plain_reingest_is_still_the_reuse_path():
    """기존 `--reingest` 회귀 없음: Stage 1 을 스캔하지 않고 watermark 를 물려받는다."""
    calls: Dict[str, Any] = {}
    assert _run_main(["--reingest"], active=["m/keep"], calls=calls) == 0
    assert calls["pipeline"] == {"previous": "2026-10-31T00:00:00+00:00", "full_stage1": False}


def test_apply_replays_the_approved_bundle_without_regenerating():
    calls: Dict[str, Any] = {}
    seen: Dict[str, Any] = {}

    def fake_apply(rows, evidence_rows, run_id, batch_size, **kwargs):
        seen.update(kwargs)
        return {"sync_mode": kwargs["sync_mode"]}

    code = _run_main(["--reingest", "--apply", *APPLY_BUNDLE], active=["m/keep"], calls=calls,
                     apply_sync=fake_apply)
    assert code == 0, "옛 버전 run 만 있는 DB 에서 재적재 apply 가 멈췄다"
    assert "pipeline" not in calls, "apply 가 Stage 1~4 를 다시 돌렸다"
    assert calls["installed"] == Path("reingest-bundle")
    assert calls["bundle_expected"]["approved_run_id"] == "123"
    assert calls["bundle_expected"]["git_sha"] == "abc"
    assert True in calls["lookups"]
    assert seen["sync_mode"] == "reingest"
    assert seen["deactivate_missing"] is False
    assert seen["removed_ids"] == ["m/lang"]
    assert seen["source_watermark"] == "2026-10-31T00:00:00+00:00"
    assert seen["extra_versions"] == {
        "stage1_mode": "reuse", "approved_dry_run_id": "123",
        "bundle_sha256": "f" * 64, "model_ids_sha256": sync.model_ids_sha256({"m/keep"}),
    }


def test_reingest_apply_without_an_approved_bundle_is_refused():
    import io

    for argv in (["--reingest", "--apply"], ["--reingest", "--apply", "--from-bundle", "b"],
                 ["--reingest", "--bundle-dir", "b", "--apply", *APPLY_BUNDLE],
                 ["--reingest", "--apply", "--full-stage1", *APPLY_BUNDLE]):
        with patched(sys, argv=["08_sync_supabase.py", *argv]), contextlib.redirect_stderr(io.StringIO()):
            try:
                sync.main()
            except SystemExit as exit_:
                assert exit_.code == 2, argv
            else:
                raise AssertionError(f"{argv} 를 받았다")


# ── DB 용량 ────────────────────────────────────────────────────────────────

def test_write_estimate_counts_halfvec_not_the_vector_text():
    vector = "[" + ",".join(["0.123456789"] * 1536) + "]"
    row = ["m/x", "core", 7, 7, 1, 1] + ['{"a":1}'] * 12 + ["h", "text-embedding-3-small", 1536, vector, "run", None]
    assert row[sync.PAYLOAD_VECTOR_INDEX] is vector
    size = sync.estimate_write_bytes([tuple(row)], [])
    assert size < len(vector), "벡터 텍스트 길이를 저장 크기로 세면 안 된다"
    assert size >= 2 * 1536 + sync.TSV_BYTES_PER_MODEL


def test_write_estimate_uses_measured_table_sizes_when_the_db_has_rows():
    """압축 전 JSON 으로 세면 실제의 몇 배가 나와 멀쩡한 재적재를 막는다.

    실측: 모델 행 평균 24KB(압축 전) × 3,853 + 계약 9KB 로 세면 약 171MB 라 지금 DB(339MB)에서
    480MB 를 넘는다. 전체 재작성의 실제 증가분은 지금 테이블 한 벌 + 새 계약 정보다.
    """
    storage = {"database": 339 * MB, "model_scout_models": 90 * MB, "model_scout_evidence": 10 * MB,
               "model_rows": 1000}
    rows = [("m",)] * 1000
    assert sync.estimate_write_bytes(rows, [], storage, added_bytes=20 * MB) == 120 * MB
    # 행이 늘면 그 비율만큼 키운다. 줄면 줄이지 않는다(보수적).
    assert sync.estimate_write_bytes([("m",)] * 1500, [], storage) == 150 * MB
    assert sync.estimate_write_bytes([("m",)] * 500, [], storage) == 100 * MB
    # 빈 DB 는 실측할 것이 없으므로 상한 방식이다.
    empty = sync.estimate_write_bytes([("m",)], [], {"database": MB, "model_rows": 0})
    assert empty == 2 * 1536 + sync.TSV_BYTES_PER_MODEL + sync.ROW_OVERHEAD_BYTES + 1


def test_capacity_plan_uses_current_size_plus_what_we_write():
    storage = {"database": 300 * MB, "model_scout_models": 80 * MB}
    ok = sync.capacity_plan(storage, 100 * MB, budget_mb=480)
    assert ok["projected_peak_mb"] == 400.0 and ok["blocked"] is False
    assert ok["tables_mb"] == {"model_scout_models": 80.0}
    blocked = sync.capacity_plan(storage, 200 * MB, budget_mb=480)
    assert blocked["blocked"] is True
    try:
        sync.assert_capacity(blocked)
    except RuntimeError as error:
        assert "500.0MB" in str(error) and "VACUUM" in str(error)
    else:
        raise AssertionError("한도를 넘는 적재를 통과시켰다")


def test_capacity_budget_comes_from_the_shared_env():
    """20_sync_dataset_index.py 와 같은 변수다. 유료 플랜이면 이 값만 올린다."""
    import os

    old = os.environ.get("SUPABASE_DB_BUDGET_MB")
    os.environ["SUPABASE_DB_BUDGET_MB"] = "8000"
    try:
        assert sync.capacity_plan({"database": 700 * MB}, MB)["blocked"] is False
    finally:
        if old is None:
            os.environ.pop("SUPABASE_DB_BUDGET_MB")
        else:
            os.environ["SUPABASE_DB_BUDGET_MB"] = old
    assert sync.capacity_plan({"database": 700 * MB}, MB)["budget_mb"] == sync.DEFAULT_DB_BUDGET_MB


def test_dry_run_reports_capacity_and_fails_when_it_would_overflow():
    with tempfile.TemporaryDirectory() as name:
        report = Path(name) / "r.json"
        assert _run_main(["--reingest", "--report", str(report)], active=["m/keep"], calls={}) == 0
        summary = json.loads((Path(name) / "r.summary.json").read_text(encoding="utf-8"))
        assert summary["capacity"]["projected_peak_mb"] == 400.0
        assert summary["capacity"]["tables_mb"]["model_scout_dataset_chunks"] == 190.0
        # 기본 Pro 안전 한도(1,024MB)를 실제로 넘는 1,100MB 예상치.
        code = _run_main(["--reingest", "--report", str(report)], active=["m/keep"], calls={}, database_mb=1000)
        assert code == 3
        assert json.loads(report.read_text(encoding="utf-8"))["capacity"]["blocked"] is True


def test_apply_stops_before_writing_when_it_would_overflow():
    def refuse(*args, **kwargs):
        raise AssertionError("용량 한도를 넘는데 DB 에 썼다")

    with tempfile.TemporaryDirectory() as name:
        report = Path(name) / "r.json"
        try:
            _run_main(["--reingest", "--apply", *APPLY_BUNDLE, "--report", str(report)], active=["m/keep"], calls={},
                      apply_sync=refuse, database_mb=1000)
        except RuntimeError as error:
            assert "한도" in str(error)
        else:
            raise AssertionError("용량 가드가 apply 를 막지 않았다")
        assert json.loads(report.read_text(encoding="utf-8"))["capacity"]["blocked"] is True


def test_full_stage1_requires_reingest():
    import io

    for argv in (["--full-stage1"], ["--refresh", "--apply", "--full-stage1"]):
        with patched(sys, argv=["08_sync_supabase.py", *argv]), \
                contextlib.redirect_stderr(io.StringIO()):
            try:
                sync.main()
            except SystemExit as exit_:
                assert exit_.code == 2
            else:
                raise AssertionError(f"{argv} 를 받았다")


# ── workflow ──────────────────────────────────────────────────────────────

WORKFLOW = ROOT.parent / ".github" / "workflows" / "model-scout-reingest.yml"


def _workflow() -> Dict[str, Any]:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _steps() -> Dict[str, Dict[str, Any]]:
    return {step["name"]: step for step in _workflow()["jobs"]["reingest"]["steps"]}


def test_workflow_stage1_mode_defaults_to_reuse():
    inputs = _workflow()[True]["workflow_dispatch"]["inputs"]  # yaml 은 `on` 을 True 로 읽는다
    assert inputs["stage1_mode"]["default"] == "reuse"
    assert inputs["stage1_mode"]["options"] == ["reuse", "full-scan"]
    assert inputs["mode"]["default"] == "validate"


def test_workflow_keeps_the_apply_guard():
    guard = _steps()["Guard the apply mode"]
    assert "APPLY" in guard["run"] and "main" in guard["run"]


def test_workflow_runs_full_stage1_inside_the_sync_script():
    """Stage 1 수집을 YAML 에서 따로 돌리지 않는다. diff·watermark 가 한 실행에 묶여야 한다."""
    steps = _steps()
    run = steps["Run the reingest"]
    assert "--full-stage1" in run["run"] and "--report" in run["run"]
    assert "full-scan" in run["run"]
    assert "| tee" not in run["run"], "tee 는 실패 종료 코드를 가린다"
    assert run.get("shell") == "bash"  # GitHub 의 명시적 bash 는 pipefail 을 켠다
    assert "validate" in run["if"]
    assert run["env"]["SUPABASE_DB_BUDGET_MB"] == "1024", "데이터셋 쪽과 같은 용량 한도를 쓴다"
    for step in steps.values():
        assert "python 01_collect_models.py" not in str(step.get("run", "")), step["name"]


def test_workflow_persists_stage1_only_after_a_successful_apply():
    names = list(_steps())
    persist = _steps()["Persist snapshots after apply"]
    assert persist["if"].replace(" ", "") == "${{inputs.mode=='apply'}}"
    assert names.index("Persist snapshots after apply") > names.index("Run the reingest")
    for filename in sync.STAGE1_SNAPSHOT_FILES:
        assert f"data/{filename}" in persist["run"], filename
    for kept in ("hf_models_stage2_contract_core.jsonl", "hf_models_stage3_core.jsonl",
                 "hf_models_stage4_manifest.json", "data/readmes/core"):
        assert kept in persist["run"], kept
    assert "hf_models_stage4_core.jsonl" not in persist["run"], "Stage 4 대용량 파일을 커밋하지 않는다"
    # 긴 실행 중 main 이 움직여도 DB 와 저장소 스냅샷이 어긋나지 않게 rebase 후 재시도한다.
    assert "git pull --rebase && git push" in persist["run"]


def test_workflow_uploads_audit_files_even_when_dry_run_is_blocked():
    upload = _steps()["Upload the reingest report"]
    assert "!cancelled()" in upload["if"]
    paths = upload["with"]["path"]
    for expected in ("reingest-report", "reingest-coverage-", "hf_models_stage4_manifest.json"):
        assert expected in paths, expected


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
