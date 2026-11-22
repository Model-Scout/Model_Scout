"""골든셋 v3 판정 기준 코퍼스: 스냅샷 로더, 무결성 검사, 하드 필터.

판정 기준은 최신 completed reingest 의 active 모델 전체다. 스냅샷 원문
(``corpus_snapshot.jsonl``)은 커밋하지 않고, 행 수·모델 ID SHA256·파일 SHA256·
sync_run_id 를 ``corpus_snapshot.meta.json`` 에 커밋한다. 파일이 없거나 checksum 이
다르면 ``load_corpus`` 가 예외를 던진다 — 조용히 통과하지 않는다.

하드 필터는 운영 SQL(``supabase_migration_contract_filters.sql`` 의
``match_model_scout_models``)의 WHERE 절을 그대로 옮겼다. 값이 없으면 수치·상업
이용·gated 조건을 통과하지 못한다. ``05_validate_retrieval.hard_filter`` 와는
tasks 가 비었을 때(SQL 은 통과, 05 는 탈락)와 최소 파라미터(05 에 없음)가 다르므로
재사용하지 않고, 겹치는 범위에서 결과가 같은지를 테스트로 확인한다.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

LAB = Path(__file__).resolve().parents[1]
AI_ROOT = LAB.parents[1]
SNAPSHOT = LAB / "corpus_snapshot.jsonl"
META = LAB / "corpus_snapshot.meta.json"
CORPUS_SCHEMA_VERSION = 1


class CorpusError(RuntimeError):
    """스냅샷이 없거나 메타와 다르다. 전체 검증은 여기서 멈춰야 한다."""


# --------------------------------------------------------------------------- 하드 필터

@dataclass(frozen=True)
class ConditionKey:
    name: str
    kind: str          # list / bool / number
    sql_supported: bool  # 운영 RPC 인자로 같은 조건을 걸 수 있는가
    description: str


# 질의 conditions 에 쓸 수 있는 키는 이것뿐이다. verify 가 이 목록 밖의 키를 거부한다.
CONDITION_KEYS: Dict[str, ConditionKey] = {k.name: k for k in (
    ConditionKey("tasks", "list", True, "task.primary 또는 task.matched 중 하나라도 일치"),
    ConditionKey("korean_required", "bool", True, "filter_metadata.korean_verified = true"),
    ConditionKey("min_parameters_billion", "number", True, "parameter_count_billion ≥ 값 (값 없으면 탈락)"),
    ConditionKey("max_parameters_billion", "number", True, "parameter_count_billion ≤ 값 (값 없으면 탈락)"),
    ConditionKey("min_context_length", "number", True, "context_length ≥ 값 (값 없으면 탈락)"),
    ConditionKey("max_context_length", "number", True, "context_length ≤ 값 (값 없으면 탈락)"),
    ConditionKey("commercial_status", "list", True, "commercial_status 가 목록 중 하나 (unknown 은 permitted 로 보지 않음)"),
    ConditionKey("require_artifact", "list", True, "artifact_formats 에 목록 전부가 있음"),
    ConditionKey("max_artifact_gib", "number", True, "artifact_runnable_gib ≤ 값 (값이 없거나 양수가 아니면 탈락). GPU VRAM 이 아니라 파일 크기"),
    ConditionKey("exclude_gated", "bool", True, "gated = false 만 (auto·manual·모름은 탈락)"),
    ConditionKey("popularity_tier", "string", True, "filter_metadata.popularity_tier 가 값과 같음"),
    ConditionKey("licenses", "list", False, "filter_metadata.license 가 목록 중 하나. 운영 RPC 에는 없는 v3 판정용 조건"),
)}


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(float(value)) else None


def _range_ok(value: Any, minimum: Any, maximum: Any) -> bool:
    if minimum is None and maximum is None:
        return True
    number = _number(value)
    if number is None:  # SQL: NULL 비교는 참이 아니다
        return False
    return (minimum is None or number >= minimum) and (maximum is None or number <= maximum)


def _tasks_of(row: Mapping[str, Any]) -> set:
    task = row.get("task") or {}
    found = set(task.get("matched") or [])
    if task.get("primary"):
        found.add(task["primary"])
    return found


def condition_failures(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> List[str]:
    """통과하지 못한 조건 키 목록. 빈 목록이면 eligible."""
    meta = row.get("filter_metadata") or {}
    failed: List[str] = []
    for key, wanted in conditions.items():
        if key not in CONDITION_KEYS:
            raise KeyError(f"지원하지 않는 조건 키: {key}")
        if key == "tasks":
            if wanted and not (_tasks_of(row) & set(wanted)):
                failed.append(key)
        elif key == "korean_required":
            if wanted and meta.get("korean_verified") is not True:
                failed.append(key)
        elif key == "min_parameters_billion":
            if not _range_ok(meta.get("parameter_count_billion"), wanted, None):
                failed.append(key)
        elif key == "max_parameters_billion":
            if not _range_ok(meta.get("parameter_count_billion"), None, wanted):
                failed.append(key)
        elif key == "min_context_length":
            if not _range_ok(meta.get("context_length"), wanted, None):
                failed.append(key)
        elif key == "max_context_length":
            if not _range_ok(meta.get("context_length"), None, wanted):
                failed.append(key)
        elif key == "commercial_status":
            if wanted and meta.get("commercial_status") not in set(wanted):
                failed.append(key)
        elif key == "require_artifact":
            if wanted and not set(wanted) <= set(meta.get("artifact_formats") or []):
                failed.append(key)
        elif key == "max_artifact_gib":
            # 05_validate_retrieval 와 같은 규칙: 측정값이 양수가 아니면 크기를 모르는 것이다.
            # 과거 결함 데이터의 0 GiB 가 "아주 작은 모델"로 통과하면 안 된다.
            size = _number(meta.get("artifact_runnable_gib"))
            if size is None or size <= 0 or not _range_ok(size, None, wanted):
                failed.append(key)
        elif key == "exclude_gated":
            if wanted and meta.get("gated") is not False:
                failed.append(key)
        elif key == "popularity_tier":
            # 운영 RPC 의 popularity_tier_filter 와 같다: 같은 값만 남는다.
            if wanted and meta.get("popularity_tier") != wanted:
                failed.append(key)
        elif key == "licenses":
            license_value = meta.get("license")
            names = set(license_value) if isinstance(license_value, list) else {license_value}
            if wanted and not (names & set(wanted)):
                failed.append(key)
    return failed


def hard_filter(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> bool:
    return row.get("active", True) is True and not condition_failures(row, conditions)


def eligible(rows: Iterable[Mapping[str, Any]], conditions: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    return [row for row in rows if hard_filter(row, conditions)]


def unknown_exclusions(rows: Iterable[Mapping[str, Any]], conditions: Mapping[str, Any]) -> int:
    """다른 조건은 모두 통과했는데, 걸린 조건의 값이 없어서만 탈락한 모델 수."""
    field_of = {
        "min_parameters_billion": "parameter_count_billion", "max_parameters_billion": "parameter_count_billion",
        "min_context_length": "context_length", "max_context_length": "context_length",
        "max_artifact_gib": "artifact_runnable_gib",
    }
    count = 0
    for row in rows:
        failed = condition_failures(row, conditions)
        if not failed:
            continue
        meta = row.get("filter_metadata") or {}
        if all(
            (key in field_of and _number(meta.get(field_of[key])) is None)
            or (key == "commercial_status" and meta.get("commercial_status") in (None, "unknown"))
            or (key == "exclude_gated" and meta.get("gated") is None)
            for key in failed
        ):
            count += 1
    return count


# --------------------------------------------------------------------------- 스냅샷

def canonical_line(row: Mapping[str, Any]) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True, default=str, separators=(",", ":"))


def model_ids_sha256(model_ids: Iterable[str]) -> str:
    return hashlib.sha256("\n".join(sorted(model_ids)).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_meta(path: Path = META) -> Dict[str, Any]:
    if not path.exists():
        raise CorpusError(f"{path} 없음. 기준 코퍼스가 기록되지 않았다")
    return json.loads(path.read_text(encoding="utf-8"))


_CACHE: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}


def load_corpus(snapshot: Path = SNAPSHOT, meta_path: Path = META, *, verify_checksum: bool = True) -> List[Dict[str, Any]]:
    """메타와 일치하는 스냅샷만 돌려준다. 없거나 다르면 CorpusError."""
    meta = load_meta(meta_path)
    if not snapshot.exists():
        raise CorpusError(
            f"{snapshot} 없음. `python test/model_retrieval/tools/dump_corpus.py` 로 "
            f"sync_run_id={meta.get('sync_run_id')} 스냅샷을 복구한다")
    key = (str(snapshot), meta.get("snapshot_sha256", ""))
    if key in _CACHE:
        return _CACHE[key]
    if verify_checksum and file_sha256(snapshot) != meta.get("snapshot_sha256"):
        raise CorpusError("스냅샷 파일 SHA256 이 메타와 다르다. 다시 덤프하거나 메타를 확인한다")
    rows = [json.loads(line) for line in snapshot.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [r["model_id"] for r in rows]
    problems = []
    if len(rows) != meta.get("active_row_count"):
        problems.append(f"행 수 {len(rows)} ≠ 메타 {meta.get('active_row_count')}")
    if model_ids_sha256(ids) != meta.get("model_ids_sha256"):
        problems.append("model_id 집합 SHA256 불일치")
    if len(set(ids)) != len(ids):
        problems.append("model_id 중복")
    # 기준은 reingest 하나가 아니라 "그 reingest + 이후 적용된 run" 이다(메타의 applied_runs).
    # 옛 메타에는 applied_runs 가 없으므로 sync_run_id 하나로 본다.
    allowed = {run.get("run_id") for run in meta.get("applied_runs") or []} or {meta.get("sync_run_id")}
    runs = {r.get("last_seen_run") for r in rows}
    if not runs <= allowed:
        problems.append(
            f"기준에 없는 run 이 쓴 행이 있다: {sorted(map(str, runs - allowed))[:3]}. "
            "`dump_corpus.py --restore` 로 기준을 맞추거나 기준을 다시 정한다")
    if problems:
        raise CorpusError("; ".join(problems))
    _CACHE[key] = rows
    return rows


def corpus_stamp(meta: Mapping[str, Any]) -> Dict[str, Any]:
    """질의마다 붙이는 기준 코퍼스 표지."""
    return {
        "sync_run_id": meta["sync_run_id"],
        "active_row_count": meta["active_row_count"],
        "model_ids_sha256": meta["model_ids_sha256"],
        "corpus_schema_version": meta["corpus_schema_version"],
    }


# --------------------------------------------------------------------------- 행 접근

def meta_of(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return row.get("filter_metadata") or {}


def canonical_of(row: Mapping[str, Any]) -> str:
    return meta_of(row).get("canonical_model_id") or row["model_id"]


def by_id(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Mapping[str, Any]]:
    return {r["model_id"]: r for r in rows}


Predicate = Callable[[Mapping[str, Any]], bool]
