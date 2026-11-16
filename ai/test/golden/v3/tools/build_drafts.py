#!/usr/bin/env python3
"""queries.py 의 70개 질문을 기준 코퍼스에 전수 스캔해 초안(drafts/)을 만든다.

검색기를 쓰지 않는다. 결과는 '제안'이며 사람 판정 전에는 정답이 아니다
(expected_any·acceptable 은 비워 둔다). 사람 판정 입력 파일(review/judgments/)은
이미 입력한 판정을 지우지 않고 새 후보만 추가한다.

    python test/golden/v3/tools/build_drafts.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus  # noqa: E402
import scan  # noqa: E402
from queries import QUERY_TYPES, all_queries  # noqa: E402

DRAFTS = corpus.V3 / "drafts"
JUDGMENTS = corpus.V3 / "review" / "judgments"
# abstention 질의는 후보가 없으므로 '정답 없음'을 사람이 확인한 기록을 이 행으로 남긴다
ABSTAIN_ROW = "(abstain)"
DEFINITION_KEYS = ("query_id", "query_type", "query", "user_intent", "persona", "expression_style", "difficulty",
                   "conditions", "conditions_fidelity", "expected_behavior", "relevance_rule")


def candidate_record(row: Mapping[str, Any], decision: Mapping[str, Any]) -> Dict[str, Any]:
    info = scan.variant_info(row)
    grade = {"proposed_grade_2": 2, "proposed_grade_1": 1}.get(decision["class"])
    return {
        "model_id": row["model_id"],
        "class": decision["class"],
        "proposed_grade": grade,
        "reason": decision["reason"],
        "family": decision.get("family"),
        "evidence": decision.get("evidence"),
        "source_pool": row.get("source_pool"),
        **info,
    }


def draft_for(query: Mapping[str, Any], rows: List[Mapping[str, Any]], meta: Mapping[str, Any]) -> Dict[str, Any]:
    result = scan.scan_query(query, rows)
    ids = corpus.by_id(rows)
    candidates = [candidate_record(ids[mid], d) for mid, d in sorted(result["decisions"].items())
                  if d["class"] != "auto_rejected"]
    record: Dict[str, Any] = {k: query.get(k) for k in DEFINITION_KEYS}
    record.update({
        "corpus": corpus.corpus_stamp(meta),
        "corpus_count": result["corpus_count"],
        "eligible_count": result["eligible_count"],
        "eligible_ids_sha256": result["eligible_ids_sha256"],
        "classification": result["counts"],
        "review_count": result["review_count"],
        "invariant_ok": result["invariant_ok"],
        "auto_reject_reasons": result["auto_reject_reasons"],
        "auto_reject_audit_sample": scan.reject_audit_sample(result, f"{meta['sync_run_id']}:{query['query_id']}"),
        "unknown_excluded": result["unknown_excluded"],
        "candidates": candidates,
        "family_counts": result["family_counts"],
        "status": "draft",
        "expected_any": [],
        "acceptable": [],
        "judged_by": None,
        "judged_at": None,
    })
    if "abstention" in result:
        abst = result["abstention"]
        record.update({
            "expected_any": [], "acceptable": [],
            "near_miss_models": abst["near_miss_by_condition"],
            "near_miss_relaxation": {k: f"{k} 조건 하나만 빼면 후보 {v}개" for k, v in abst["relaxed_candidate_counts"].items()},
            "relaxed_candidate_counts": abst["relaxed_candidate_counts"],
            "individual_condition_counts": abst["individual_condition_counts"],
            "near_miss_count": abst["near_miss_count"],
            "temptation_count": abst["temptation_count"],
            "extreme_reasons": abst["extreme_reasons"],
        })
    return record


def merge_judgments(path: Path, drafts: List[Mapping[str, Any]]) -> int:
    """사람이 이미 입력한 판정은 그대로 두고 새 후보만 빈 칸으로 추가한다."""
    existing: Dict[tuple, Dict[str, Any]] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                item = json.loads(line)
                existing[(item["query_id"], item["model_id"])] = item
    rows: List[Dict[str, Any]] = []
    for draft in drafts:
        if draft["expected_behavior"] == "abstain":
            key = (draft["query_id"], ABSTAIN_ROW)
            item = existing.pop(key, None) or {
                "query_id": draft["query_id"], "model_id": ABSTAIN_ROW, "decision": None, "final_grade": None,
                "judged_by": None, "judged_at": None, "judgment_reason": None,
            }
            item.update({"proposed_grade": None, "proposed_class": "abstain", "canonical_model_id": None})
            rows.append(item)
            continue
        for cand in draft["candidates"]:
            key = (draft["query_id"], cand["model_id"])
            item = existing.pop(key, None) or {
                "query_id": draft["query_id"], "model_id": cand["model_id"],
                "decision": None, "final_grade": None,
                "judged_by": None, "judged_at": None, "judgment_reason": None,
            }
            item["proposed_grade"] = cand["proposed_grade"]
            item["proposed_class"] = cand["class"]
            item["canonical_model_id"] = cand["canonical_model_id"]
            rows.append(item)
    stale = [item for item in existing.values() if item.get("decision")]
    for item in stale:  # 후보에서 빠졌지만 사람이 판정한 줄은 지우지 않고 표시만 한다
        item["stale"] = True
        rows.append(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    return len(stale)


def main() -> int:
    rows = corpus.load_corpus()
    meta = corpus.load_meta()
    scan.bind(rows)
    DRAFTS.mkdir(parents=True, exist_ok=True)
    by_type: Dict[str, List[Dict[str, Any]]] = {t: [] for t in QUERY_TYPES}
    for query in all_queries():
        draft = draft_for(query, rows, meta)
        by_type[query["query_type"]].append(draft)
        c = draft["classification"]
        flag = "" if draft["review_count"] <= scan.REVIEW_LIMIT else "  ⚠ 검수 25개 초과"
        print(f"{query['query_id']}  eligible={draft['eligible_count']:5d}  2점={c['proposed_grade_2']:3d}  "
              f"1점={c['proposed_grade_1']:3d}  보류={c['unresolved_for_human']:3d}  "
              f"제외={c['auto_rejected']:5d}  검수={draft['review_count']:3d}{flag}")
    stale_total = 0
    for query_type, drafts in by_type.items():
        path = DRAFTS / f"{query_type}.jsonl"
        path.write_text("".join(json.dumps(d, ensure_ascii=False, sort_keys=True, default=str) + "\n" for d in drafts),
                        encoding="utf-8")
        stale_total += merge_judgments(JUDGMENTS / f"{query_type}.jsonl", drafts)
    if stale_total:
        print(f"\n⚠ 후보에서 빠졌지만 이미 판정된 줄 {stale_total}개를 stale 로 표시했다")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
