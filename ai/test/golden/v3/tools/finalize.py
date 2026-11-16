#!/usr/bin/env python3
"""사람 판정이 끝난 뒤 최종 골든셋(final/<유형>.jsonl)을 만든다.

판정이 하나라도 비어 있거나 보류(hold)면 아무것도 쓰지 않고 실패한다. 0점은 저장하지
않는다. 대신 eligible_count 와 분류 결과로 나머지가 정답이 아님을 증명한다.

    python test/golden/v3/tools/finalize.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
from build_drafts import ABSTAIN_ROW, DRAFTS, JUDGMENTS  # noqa: E402
from queries_loader import QUERY_TYPES  # noqa: E402

FINAL = corpus.V3 / "final"


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def pending(judgments: Mapping[tuple, Mapping[str, Any]], draft: Mapping[str, Any]) -> List[str]:
    keys = [ABSTAIN_ROW] if draft["expected_behavior"] == "abstain" else [c["model_id"] for c in draft["candidates"]]
    out = []
    for model_id in keys:
        item = judgments.get((draft["query_id"], model_id)) or {}
        if item.get("decision") in (None, "hold") or not all(item.get(k) for k in ("judged_by", "judged_at", "judgment_reason")):
            out.append(model_id)
    return out


def final_record(draft: Mapping[str, Any], judgments: Mapping[tuple, Mapping[str, Any]]) -> Dict[str, Any]:
    record = {k: v for k, v in draft.items() if k not in ("candidates", "auto_reject_audit_sample", "status")}
    labels = []
    for cand in draft["candidates"]:
        item = judgments[(draft["query_id"], cand["model_id"])]
        if item["final_grade"] in (1, 2):
            labels.append({
                "model_id": cand["model_id"], "grade": item["final_grade"],
                "canonical_model_id": cand["canonical_model_id"], "family": cand.get("family"),
                "proposed_grade": cand.get("proposed_grade"),
                "judged_by": item["judged_by"], "judged_at": item["judged_at"], "judgment_reason": item["judgment_reason"],
            })
    family_labels: Dict[str, int] = {}
    for label in labels:  # canonical family 기준 평가용: 가족 안의 최고 점수
        family_labels[label["canonical_model_id"]] = max(family_labels.get(label["canonical_model_id"], 0), label["grade"])
    record.update({
        "status": "final",
        "expected_any": sorted(l["model_id"] for l in labels if l["grade"] == 2),
        "acceptable": sorted(l["model_id"] for l in labels if l["grade"] == 1),
        "labels": sorted(labels, key=lambda l: (-l["grade"], l["model_id"])),
        "family_labels": dict(sorted(family_labels.items())),
        "excluded_by_human": sorted(c["model_id"] for c in draft["candidates"]
                                    if judgments[(draft["query_id"], c["model_id"])]["final_grade"] == 0),
    })
    if draft["expected_behavior"] == "abstain":
        confirm = judgments[(draft["query_id"], ABSTAIN_ROW)]
        record.update({k: confirm[k] for k in ("judged_by", "judged_at", "judgment_reason")})
    else:
        record["judged_by"] = sorted({l["judged_by"] for l in labels}) or None
        record["judged_at"] = max((l["judged_at"] for l in labels), default=None)
    return record


def main() -> int:
    judgments = {}
    for path in JUDGMENTS.glob("*.jsonl"):
        for item in read_jsonl(path):
            judgments[(item["query_id"], item["model_id"])] = item
    missing: Dict[str, List[str]] = {}
    outputs: Dict[str, List[Dict[str, Any]]] = {}
    for query_type in QUERY_TYPES:
        drafts = read_jsonl(DRAFTS / f"{query_type}.jsonl")
        for draft in drafts:
            left = pending(judgments, draft)
            if left:
                missing[draft["query_id"]] = left
        outputs[query_type] = [] if missing else [final_record(d, judgments) for d in drafts]
    if missing:
        total = sum(len(v) for v in missing.values())
        print(f"❌ 판정이 끝나지 않았다: 질의 {len(missing)}개, 후보 {total}개 (판정·judged_by·judged_at·이유 필요)")
        for qid, ids in list(missing.items())[:10]:
            print(f"  {qid}: {ids[:3]}{' …' if len(ids) > 3 else ''}")
        return 1
    FINAL.mkdir(parents=True, exist_ok=True)
    for query_type, records in outputs.items():
        (FINAL / f"{query_type}.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False, sort_keys=True, default=str) + "\n" for r in records), encoding="utf-8")
    print(f"✅ final/ {sum(len(v) for v in outputs.values())}개 질의 기록")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
