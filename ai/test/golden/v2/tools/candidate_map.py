#!/usr/bin/env python3
"""조건별 후보 수 지도. 질의 설계의 재료다.

수치 상·하한이 있는 질의는 실제 Supabase SQL과 동일하게 값이 없는 모델을
자동으로 제외한다. 값이 없으면 "≤1B"나 "≥32K"를 만족한다고 검증할 수 없기
때문이다. 이 지도에 나오는 수치는 곧 운영 검색이 보게 될 후보 수다.

    python test/golden/v2/tools/candidate_map.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_v2  # noqa: E402

TASKS = (
    "summarization",
    "question-answering",
    "text-classification",
    "feature-extraction",
    "translation",
    "automatic-speech-recognition",
    "sentence-similarity",
    "image-text-to-text",
    "text-generation",
)
CAPS = (0.3, 0.5, 1.0, 3.0, 8.0)
FLOORS = (2048, 8192, 32768, 131072)


def main() -> None:
    rows = corpus_v2.load_rows()
    print(f"판정 기준 코퍼스 {len(rows)}행 (Supabase active 스냅샷)")
    print()

    print("=" * 100)
    print("A. task별 후보 수 (한국어 필수, 다른 조건 없음)")
    print("=" * 100)
    print(f"{'task':32s} {'전체':>7s} {'core만':>8s} {'low만':>8s}")
    base = {}
    for task in TASKS:
        total = corpus_v2.count(tasks=[task], korean_required=True)
        core = corpus_v2.count(tasks=[task], korean_required=True, pools=["core"])
        base[task] = total
        print(f"{task:32s} {total:7d} {core:8d} {total - core:8d}")

    print()
    print("=" * 100)
    print("B. task × 파라미터 상한  (운영 검색과 동일 — 값 없는 모델은 제외)")
    print("=" * 100)
    print(f"{'task':32s} " + " ".join(f"{cap:>8}B" for cap in CAPS))
    for task in TASKS:
        cells = [
            corpus_v2.count(tasks=[task], korean_required=True, max_parameters_billion=cap)
            for cap in CAPS
        ]
        print(f"{task:32s} " + " ".join(f"{value:9d}" for value in cells))

    print()
    print("=" * 100)
    print("C. task × context 하한  (운영 검색과 동일 — 값 없는 모델은 제외)")
    print("=" * 100)
    print(f"{'task':32s} " + " ".join(f"{floor:>9}" for floor in FLOORS))
    for task in TASKS:
        cells = [
            corpus_v2.count(tasks=[task], korean_required=True, min_context_length=floor)
            for floor in FLOORS
        ]
        print(f"{task:32s} " + " ".join(f"{value:9d}" for value in cells))

    print()
    print("=" * 100)
    print("D. 수치 조건을 제거했을 때의 후보 수  ⚠️ 조건 누락 시 유입 경로")
    print("=" * 100)
    print(f"{'질의':40s} {'수치적용':>9s} {'수치제거':>9s} {'차이':>10s}")
    for task in TASKS:
        for cap in (0.3, 1.0, 3.0):
            bounded = corpus_v2.count(tasks=[task], korean_required=True, max_parameters_billion=cap)
            unbounded = corpus_v2.count(tasks=[task], korean_required=True)
            if unbounded - bounded > 0:
                print(f"{task + f' ≤{cap}B':40s} {bounded:9d} {unbounded:9d} {unbounded - bounded:10d}")

    print()
    print("=" * 100)
    print("E. 값 미공개 비율 — 백필의 남은 과제")
    print("=" * 100)
    for field, label in (("parameter_count_billion", "파라미터 수"), ("context_length", "컨텍스트 길이")):
        unknown = sum(
            1
            for row in rows
            if not isinstance((row.get("filter_metadata") or {}).get(field), (int, float))
        )
        print(f"  {label:14s} 미공개 {unknown:5d} / {len(rows)} = {unknown / len(rows) * 100:5.1f}%")


if __name__ == "__main__":
    main()
