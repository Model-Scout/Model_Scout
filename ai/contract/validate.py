#!/usr/bin/env python3
"""데이터 계약을 지키는지 검사한다. 하나라도 걸리면 적재하지 않는다.

    python contract/validate.py                         # 예시 레코드 (자기 검사)
    python contract/validate.py path/to/records.jsonl
    python contract/validate.py records.jsonl --baseline old.jsonl   # 품질 하락 검사

JSON Schema가 잡는 것(타입, 필수 키, enum, 범위)과 잡지 못하는 것이 있다.
잡지 못하는 쪽이 실제로 사고를 낸다.

  · status가 unknown인데 값이 들어 있다      → 둘 중 하나가 틀렸다
  · status가 verified인데 값이 비어 있다      → 근거는 적었는데 값이 없다
  · conflicts[]에 있는데 status가 conflict가 아니다
  · 기존 verified 값이 새 inferred 값으로 덮였다 → 재적재 사고의 전형

마지막 항목이 백필 작업에서 실제로 났다. Stage 4 문서를 직접 조립했더니
task·candidate·popularity·search_aliases 등 12개 키가 빠져 하드 필터가 전부
탈락시켰다. 적재 전에 잡아야 하는 종류의 사고다.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple

try:
    import jsonschema
except ModuleNotFoundError:  # pragma: no cover
    raise SystemExit("jsonschema가 필요합니다: pip install -r requirements.txt")

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE / "model-record.schema.json"
EXAMPLES_PATH = HERE / "examples.json"

# 값이 하나의 스칼라/리스트인 계약 필드. 상태↔값 정합성을 여기에만 적용한다.
# artifacts.formats.* 와 deployment.vram_estimate 는 스키마가 객체를 강제하므로
# "비어 있음"을 None으로 표현할 수 없다. 그래서 제외하고, 대신 그 둘은
# 하위 값이 전부 null인지로 따로 본다.
SCALAR_FIELDS = {
    "identity.revision",
    "identity.last_modified",
    "identity.gated",
    "capability.primary_task",
    "capability.languages",
    "capability.korean_verified",
    "capability.translation_pairs",
    "capability.embedding_dimensions",
    "technical.architecture",
    "technical.model_type",
    "technical.parameter_count_total",
    "technical.parameter_count_active",
    "technical.context_length",
    "technical.dtype",
    "artifacts.total_bytes",
    "legal.license_raw",
    "legal.license_file",
    "legal.commercial_status",
    "legal.base_model_constraint",
    "quality.results",
}

# unknown/conflict 여도 값이 남아 있는 것이 정상인 필드.
# commercial_status는 "unknown"이라는 enum 값 자체가 상태의 표현이다.
STATUS_IS_THE_VALUE = {"legal.commercial_status"}


def load_schema() -> Dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def contract_fields(schema: Dict[str, Any]) -> List[str]:
    """목록은 스키마에만 적는다. 두 군데 적으면 한쪽이 낡는다."""
    return list(schema["$defs"]["contract_fields"]["const"])


def dig(record: Dict[str, Any], path: str) -> Tuple[bool, Any]:
    """점 경로로 값을 꺼낸다. (찾았는지, 값)"""
    node: Any = record
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return False, None
        node = node[part]
    return True, node


def is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, (list, tuple, dict, str)):
        return len(value) == 0
    return False


def read_records(path: Optional[Path]) -> Iterator[Tuple[str, Dict[str, Any]]]:
    if path is None:
        for index, record in enumerate(json.loads(EXAMPLES_PATH.read_text(encoding="utf-8"))):
            yield f"{EXAMPLES_PATH.name}[{index}]", record
        return
    if path.suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload if isinstance(payload, list) else [payload]
        for index, record in enumerate(rows):
            yield f"{path.name}[{index}]", record
        return
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if line.strip():
                yield f"{path.name}:{number}", json.loads(line)


def check_record(record: Dict[str, Any], fields: List[str]) -> List[str]:
    """스키마가 잡지 못하는 정합성을 본다."""
    problems: List[str] = []
    provenance = record.get("provenance") or {}
    entries: Dict[str, Any] = provenance.get("fields") or {}

    # ① 계약 필드마다 출처 항목이 있어야 한다
    for field in fields:
        if field not in entries:
            problems.append(f"provenance.fields에 `{field}` 없음")

    # ② 출처 항목이 실재하지 않는 경로를 가리키면 안 된다
    for field in entries:
        found, _ = dig(record, field)
        if not found:
            problems.append(f"provenance.fields의 `{field}`가 레코드에 없는 경로")

    # ③ 상태 ↔ 값 정합성
    for field, entry in entries.items():
        if field not in SCALAR_FIELDS or field in STATUS_IS_THE_VALUE:
            continue
        found, value = dig(record, field)
        if not found:
            continue
        status = (entry or {}).get("status")
        empty = is_empty(value)
        if status in {"unknown", "conflict", "not_applicable"} and not empty:
            problems.append(f"`{field}` status={status} 인데 값이 있음: {value!r}")
        if status in {"verified", "documented", "inferred"} and empty:
            problems.append(f"`{field}` status={status} 인데 값이 비어 있음")

    # ④ conflicts[]와 status=conflict가 짝이 맞아야 한다
    declared = {item.get("field") for item in provenance.get("conflicts") or []}
    marked = {name for name, entry in entries.items() if (entry or {}).get("status") == "conflict"}
    for field in declared - marked:
        problems.append(f"conflicts[]에 `{field}`가 있는데 status가 conflict가 아님")
    for field in marked - declared:
        problems.append(f"`{field}` status=conflict인데 conflicts[]에 후보가 없음")

    # ⑤ 라이선스: review_required가 상태와 맞아야 한다
    legal = record.get("legal") or {}
    status = legal.get("commercial_status")
    base = legal.get("base_model_constraint") or {}
    should_review = status in {"review_required", "unknown"} or bool(base.get("more_restrictive"))
    if bool(legal.get("review_required")) != should_review:
        problems.append(
            f"legal.review_required={legal.get('review_required')} 인데 "
            f"commercial_status={status}, base more_restrictive={base.get('more_restrictive')}"
        )
    if not (legal.get("user_message") or "").strip():
        problems.append("legal.user_message가 비어 있음 — '모른다'도 사용자에게 할 말이 있다")

    # ⑥ MoE: active가 total보다 클 수 없다
    technical = record.get("technical") or {}
    total = technical.get("parameter_count_total")
    active = technical.get("parameter_count_active")
    if isinstance(total, int) and isinstance(active, int) and active > total:
        problems.append(f"parameter_count_active({active}) > total({total})")

    # ⑦ 벤치마크 점수는 원문을 찾아갈 수 있어야 한다
    for index, result in enumerate(((record.get("quality") or {}).get("results") or [])):
        if not (result.get("evidence_ref") or "").strip():
            problems.append(f"quality.results[{index}] evidence_ref 비어 있음")

    return problems


def check_regression(
    record: Dict[str, Any], before: Dict[str, Any], fields: List[str]
) -> List[str]:
    """기존 고신뢰 값이 저신뢰 값으로 덮이거나 사라졌는지. 재적재의 핵심 게이트다."""
    rank = {"verified": 4, "documented": 3, "inferred": 2, "not_applicable": 1, "conflict": 0, "unknown": 0}
    problems: List[str] = []
    old_entries = (before.get("provenance") or {}).get("fields") or {}
    new_entries = (record.get("provenance") or {}).get("fields") or {}
    for field in fields:
        old_status = (old_entries.get(field) or {}).get("status")
        new_status = (new_entries.get(field) or {}).get("status")
        if old_status is None or new_status is None:
            continue
        if rank.get(new_status, 0) < rank.get(old_status, 0):
            _, old_value = dig(before, field)
            _, new_value = dig(record, field)
            problems.append(
                f"`{field}` {old_status} → {new_status} 로 하락 ({old_value!r} → {new_value!r})"
            )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="?", type=Path, default=None,
                        help="검사할 .jsonl 또는 .json. 생략하면 contract/examples.json")
    parser.add_argument("--baseline", type=Path, default=None,
                        help="이전 레코드. 품질 하락을 검사한다")
    parser.add_argument("--limit", type=int, default=20, help="보여줄 문제 모델 수")
    args = parser.parse_args()

    schema = load_schema()
    validator = jsonschema.Draft202012Validator(schema)
    fields = contract_fields(schema)

    baseline: Dict[str, Dict[str, Any]] = {}
    if args.baseline:
        baseline = {record["model_id"]: record for _, record in read_records(args.baseline)}

    total = 0
    failed: List[Tuple[str, List[str]]] = []
    for label, record in read_records(args.records):
        total += 1
        problems = [
            f"스키마: {error.json_path} — {error.message}"
            for error in sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path))
        ]
        problems += check_record(record, fields)
        before = baseline.get(record.get("model_id"))
        if before:
            problems += check_regression(record, before, fields)
        if problems:
            failed.append((f"{label} {record.get('model_id')}", problems))

    source = args.records.name if args.records else EXAMPLES_PATH.name
    print(f"{source} — 레코드 {total:,}개, 계약 필드 {len(fields)}개")
    if args.baseline:
        print(f"품질 하락 검사 기준: {args.baseline.name} ({len(baseline):,}개)")
    print()
    if not failed:
        print("계약 위반 없음")
        return 0
    print(f"계약 위반 {len(failed):,}개 모델 / 문제 {sum(len(p) for _, p in failed):,}건\n")
    for label, problems in failed[: args.limit]:
        print(f"  {label}")
        for problem in problems:
            print(f"    · {problem}")
    if len(failed) > args.limit:
        print(f"\n  ... 외 {len(failed) - args.limit:,}개")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
