#!/usr/bin/env python3
"""Turn team judgments into golden labels (no API key).

Input
- reports/judging_marks.json: snapshot of the review page's shared score board
  (collection `marks` of the 판정실 artifact). Re-export it after judging changes.
- labels/judging_queries_batch*.jsonl: the judged queries.

Output
- labels/judged_queries.jsonl: same label schema as golden_queries.jsonl, so
  convert_golden.py can turn it into the retrieval run schema.
- reports/golden_label_review.md: golden-tab scores that disagree with the
  current golden labels. Golden labels come from verified cases and are not
  changed automatically.

Score → label
- 2 → expected_any, 1 → acceptable.
- 0 with a fatal reason (license, size/hardware, language/direction) → must_exclude.
  Other 0s (wrong use, wrong identifier, no benchmark number) → judged_irrelevant.
- ? with conditional_license → needs_review; other ? → unjudged.
- No 2 in the pool: 1-scored models are promoted to expected_any and
  `answer_grade` is set to "acceptable_only". No 1 or 2: evaluable_now=false.
- model_comparison: expected_behavior "compare"; every model in expected_all
  (the compared models) must appear in top-k. A compared model scored 0 stays
  out of must_exclude, since the answer has to explain why it does not fit.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
MARKS_PATH = HERE / "reports" / "judging_marks.json"
QUERY_PATHS = sorted((HERE / "labels").glob("judging_queries_batch*.jsonl"))
GOLDEN_PATH = HERE / "labels" / "golden_queries.jsonl"
OUTPUT_PATH = HERE / "labels" / "judged_queries.jsonl"
REVIEW_PATH = HERE / "reports" / "golden_label_review.md"

FATAL_RULES = (
    ("license", re.compile(r"비상업|\bNC\b|-nc|noncommercial|라이선스 명시' 조건 위반", re.I)),
    ("hardware", re.compile(
        r"크기|초과|VRAM|GiB|GB|메모리|파라미터|미달|컨텍스트|토큰|더 작지 않음|더 빠르지 않음|비슷한 크기 아님|"
        r"파라미터 동일|길지 않음|전용 변환본|전용 FP8|Blackwell 전용", re.I)),
    ("language", re.compile(
        r"방향 불일치|언어쌍|단일 언어쌍|[한영]→[한영] 전용|한↔영 전용|en→ko 전용|ko→en 전용|영어 전용|"
        r"영어만 명시|아랍어 출력|한국어 입력 전용|한국어 전용\(다국어 아님\)")),
)
ROLE_FIELDS = {"정답": "expected_any", "허용": "acceptable", "제외": "must_exclude", "경고 필요": "needs_review"}


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fatal_rule(note: str) -> str | None:
    for rule, pattern in FATAL_RULES:
        if pattern.search(note or ""):
            return rule
    return None


def build_label(query: Dict[str, Any], marks: List[Dict[str, Any]], query_note: str | None) -> Dict[str, Any]:
    by_score = defaultdict(list)
    must_exclude, needs_review, irrelevant, unjudged = [], [], [], []
    # A compared model must be retrieved even when it fails the need (the answer says so).
    compared = {m.casefold() for m in query.get("reference_models") or []} if query.get("query_type") == "model_comparison" else set()
    for mark in sorted(marks, key=lambda m: m["key"]):
        model_id, note = mark["key"], mark.get("note") or ""
        if mark["score"] in (1, 2):
            by_score[mark["score"]].append(model_id)
        elif mark["score"] == 0:
            rule = None if model_id.casefold() in compared else fatal_rule(note)
            if rule:
                must_exclude.append({"model_id": model_id, "reason": note, "violated_rule": rule})
            else:
                irrelevant.append({"model_id": model_id, "reason": note})
        elif mark.get("review_reason") == "conditional_license":
            needs_review.append({"model_id": model_id, "reason": note})
        else:
            unjudged.append({"model_id": model_id, "reason": note})

    expected_any, acceptable = by_score[2], by_score[1]
    answer_grade = "judged_2"
    if not expected_any and acceptable:
        expected_any, acceptable, answer_grade = acceptable, [], "acceptable_only"
    evaluable = bool(expected_any)
    behavior = "recommend"
    label: Dict[str, Any] = {}
    if query.get("query_type") == "model_comparison":
        behavior, evaluable = "compare", True
        label["expected_all"] = query.get("reference_models") or []

    notes = [n for n in (query_note,) if n]
    if answer_grade == "acceptable_only":
        notes.append("후보 풀에 2점 모델이 없어 1점 모델을 정답으로 올림")
    if not evaluable:
        notes.append("후보 풀에 1·2점 모델이 없음")
    return {
        "query_id": query["query_id"],
        "source_case_id": None,
        "source_url": None,
        "label_type": "judged",
        "query_type": query.get("query_type"),
        "evaluable_now": evaluable,
        "blocked_by": [] if evaluable else ["no_relevant_in_pool"],
        "query": query["query"],
        "conditions": query["conditions"],
        **({"reference_models": query["reference_models"]} if query.get("reference_models") else {}),
        "expected_behavior": behavior,
        **label,
        "expected_any": expected_any,
        "acceptable": acceptable,
        "must_exclude": must_exclude,
        "needs_review": needs_review,
        "judged_irrelevant": irrelevant,
        "unjudged": unjudged,
        "answer_grade": answer_grade,
        "known_failure_cause": None,
        "notes": " / ".join(notes) or None,
    }


def golden_review(golden: List[Dict[str, Any]], marks: Dict[str, List[Dict[str, Any]]]) -> List[str]:
    expected = {"expected_any": 2, "acceptable": 1, "must_exclude": 0}
    lines = ["# 골든셋 라벨 검토 결과", "", "판정실 골든셋 탭의 점수가 현재 라벨과 다른 후보다. 골든셋 라벨은 원문 확인을 거친 사례라 자동으로 바꾸지 않는다.", "",
             "| 질의 | 모델 | 현재 라벨 | 점수 | 판정 메모 |", "|---|---|---|---:|---|"]
    count = 0
    for item in golden:
        roles = {}
        for field in ("expected_any", "acceptable", "must_exclude", "needs_review"):
            for entry in item.get(field) or []:
                roles[(entry["model_id"] if isinstance(entry, dict) else entry).casefold()] = field
        for mark in marks.get(item["query_id"], []):
            field = roles.get(mark["key"].casefold())
            score = mark["score"]
            if field is None or (field in expected and score == expected[field]) or (field == "needs_review" and score is None):
                continue
            count += 1
            shown = "?" if score is None else score
            lines.append(f"| `{item['query_id']}` | {mark['key']} | {field} | {shown} | {(mark.get('note') or '').replace('|', '/')} |")
    lines.insert(3, f"불일치 {count}건.")
    return lines + [""]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--marks", type=Path, default=MARKS_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    snapshot = json.loads(args.marks.read_text(encoding="utf-8"))
    marks: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    query_notes: Dict[str, str] = {}
    for mark in snapshot["marks"]:
        if mark["key"] == "query_note":
            query_notes[mark["query_id"]] = mark.get("note") or None
        else:
            marks[mark["query_id"]].append(mark)

    queries = [query for path in QUERY_PATHS for query in read_jsonl(path)]
    labels = []
    for query in queries:
        if not marks.get(query["query_id"]):
            raise SystemExit(f"{query['query_id']}: no judgments in {args.marks.name}")
        labels.append(build_label(query, marks[query["query_id"]], query_notes.get(query["query_id"])))
    args.output.write_text("".join(json.dumps(label, ensure_ascii=False) + "\n" for label in labels), encoding="utf-8")
    REVIEW_PATH.write_text("\n".join(golden_review(read_jsonl(GOLDEN_PATH), marks)), encoding="utf-8")

    print(json.dumps({
        "queries": len(labels),
        "evaluable": sum(label["evaluable_now"] for label in labels),
        "behavior": dict(Counter(label["expected_behavior"] for label in labels)),
        "answer_grade": dict(Counter(label["answer_grade"] for label in labels)),
        "expected_any": sum(len(label["expected_any"]) for label in labels),
        "acceptable": sum(len(label["acceptable"]) for label in labels),
        "must_exclude": dict(Counter(item["violated_rule"] for label in labels for item in label["must_exclude"])),
        "needs_review": sum(len(label["needs_review"]) for label in labels),
        "judged_irrelevant": sum(len(label["judged_irrelevant"]) for label in labels),
        "unjudged": sum(len(label["unjudged"]) for label in labels),
        "not_evaluable": [label["query_id"] for label in labels if not label["evaluable_now"]],
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
