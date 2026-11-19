#!/usr/bin/env python3
"""골든셋 240문항을 기계로 검증한다. 사람이 볼 것과 분리하기 위한 도구다.

사람이 볼 것은 '질문이 자연스러운가'와 'README 해석에 기댄 2점이 맞는가'뿐이다.
나머지는 전부 여기서 확인한다.

    python test/model_retrieval/tools/verify_goldenset.py
"""

from __future__ import annotations

import importlib.util
import json
import statistics
import sys
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
QUERIES = AI / "test" / "model_retrieval" / "queries"
sys.path.insert(0, str(Path(__file__).resolve().parent))

SPECS = ["spec_benchmark.py", "spec_structured.py", "spec_lexical.py",
         "spec_comparison.py", "spec_capability.py", "spec_constraint.py"]
PER_TYPE = 40


def load(name: str) -> List[Dict[str, Any]]:
    spec = importlib.util.spec_from_file_location(name[:-3], QUERIES / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.QUERIES)


def main() -> int:
    import corpus
    import scan

    rows = corpus.load_corpus()
    meta = corpus.load_meta()
    cache = json.loads((QUERIES / "decompose_cache.json").read_text(encoding="utf-8"))
    problems: List[str] = []
    seen_ids: Dict[str, str] = {}
    seen_text: Dict[str, str] = {}

    print(f"기준 코퍼스 {meta['active_row_count']}행 · sync_run {meta['sync_run_id'][:8]} "
          f"· model_ids_sha256 {meta['model_ids_sha256'][:12]}")
    print(f"분해 캐시 {len(cache) - 1}건 (LLM={cache.get('__meta__', {}).get('llm')})\n")
    print(f"{'유형':24s} {'문항':>4s} {'초보':>4s} {'2점':>5s} {'1점':>5s} {'보류':>5s} {'2점중앙':>6s}")

    totals = [0, 0, 0, 0, 0]
    for name in SPECS:
        items = load(name)
        kind = items[0]["query_type"]
        if len(items) != PER_TYPE:
            problems.append(f"{kind}: 문항 {len(items)}개 (기대 {PER_TYPE})")
        g2_counts, t2, t1, tu, beginner = [], 0, 0, 0, 0
        for item in items:
            qid = item["qid"]
            if qid in seen_ids:
                problems.append(f"{qid}: query id 중복 ({seen_ids[qid]}, {kind})")
            seen_ids[qid] = kind
            if item["text"] in seen_text:
                problems.append(f"{qid}: 질문 문장이 {seen_text[item['text']]} 와 같다")
            seen_text[item["text"]] = qid
            if item["text"] not in cache:
                problems.append(f"{qid}: 분해 캐시 없음 — decompose_cache.py 를 돌린다")
            # 조건마다 질문 속 근거가 있어야 한다
            for key in item.get("conditions", {}):
                if key == "korean_required":
                    continue
                if not str((item.get("conditions_fidelity") or {}).get(key) or "").strip():
                    problems.append(f"{qid}: 조건 {key} 에 질문 속 근거가 없다")

            query = dict(item)
            query.update(query_id=qid, expected_behavior="recommend", query=item["text"])
            result = scan.scan_query(query, rows)
            counts = result["counts"]
            graded = counts["proposed_grade_2"] + counts["proposed_grade_1"]
            if graded + counts["unresolved_for_human"] == 0:
                problems.append(f"{qid}: 정답이 0개다")
            if kind == "structured_constraint" and counts["proposed_grade_2"] == result["eligible_count"]:
                problems.append(f"{qid}: 2점이 eligible 전부다 — 순위가 점수를 바꾸지 못한다")
            if kind == "model_comparison":
                families = {d.get("family") for d in result["decisions"].values()
                            if d["class"] != "auto_rejected"}
                if len(families) < 2:
                    problems.append(f"{qid}: 비교 대상 한쪽에 정답이 없다 ({families})")
            g2_counts.append(counts["proposed_grade_2"])
            t2 += counts["proposed_grade_2"]
            t1 += counts["proposed_grade_1"]
            tu += counts["unresolved_for_human"]
            beginner += item.get("origin") == "beginner"
        print(f"{kind:24s} {len(items):>4d} {beginner:>4d} {t2:>5d} {t1:>5d} {tu:>5d} "
              f"{statistics.median(g2_counts):>6.0f}")
        for i, v in enumerate((len(items), beginner, t2, t1, tu)):
            totals[i] += v
    print(f"{'합계':24s} {totals[0]:>4d} {totals[1]:>4d} {totals[2]:>5d} {totals[3]:>5d} {totals[4]:>5d}")

    print()
    if problems:
        print(f"❌ 문제 {len(problems)}건")
        for line in problems:
            print(f"  · {line}")
        return 1
    print("✅ 기계 검증 전부 통과")
    print("\n남은 것은 사람 판단이다.")
    print("  · 질문 240개가 실제로 물어볼 만한가")
    print("  · README 해석에 기댄 2점이 맞는가 (tools/review_sheet.py)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
