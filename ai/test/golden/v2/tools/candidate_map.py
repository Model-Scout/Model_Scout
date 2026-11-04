#!/usr/bin/env python3
"""조건별 후보 수 지도. 질의 설계의 재료다.

중요: ``require_known_parameters`` / ``require_known_context``는 기본 False다.
이 플래그를 켜면 값을 공개하지 않은 모델이 탈락한다. 코퍼스의 39%가 파라미터
수를 공개하지 않으므로, 후보를 줄이는 용도로 켜면 정답이 통째로 사라진다.
질의가 "파라미터 수가 명시된"처럼 공개를 요구할 때만 켠다.

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
    print("B. task × 파라미터 상한  (require_known_parameters=False — 미공개 모델도 통과)")
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
    print("C. task × context 하한  (require_known_context=False)")
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
    print("D. require_known_* 플래그가 숨기는 후보 수  ⚠️ 정답 누락 경로")
    print("=" * 100)
    print(f"{'질의':40s} {'known=F':>9s} {'known=T':>9s} {'숨은 탈락':>10s}")
    for task in TASKS:
        for cap in (0.3, 1.0, 3.0):
            off = corpus_v2.count(tasks=[task], korean_required=True, max_parameters_billion=cap)
            on = corpus_v2.count(
                tasks=[task],
                korean_required=True,
                max_parameters_billion=cap,
                require_known_parameters=True,
            )
            if off - on > 0:
                print(f"{task + f' ≤{cap}B':40s} {off:9d} {on:9d} {off - on:10d}")

    print()
    print("=" * 100)
    print("E. 값 미공개 비율 — 위 D의 원인")
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
