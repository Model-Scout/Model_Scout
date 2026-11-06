#!/usr/bin/env python3
"""abstention 질의 후보 탐색: 하드 필터 통과 후보가 0개가 되는 조건 조합.

수치값이 없는 모델의 처리
------------------------
``numeric_ok``는 Supabase SQL과 동일하다. 상한 또는 하한이 주어졌는데 값이 없으면
그 모델은 조건을 만족한다고 검증할 수 없으므로 후보에서 제외한다. 따라서 이
탐색기는 자연스러운 수치 질의 그대로 후보 0개 조합을 찾는다.

    python test/golden/v2/tools/find_abstention.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_v2  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "reports" / "abstention_candidates.json"

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
CAPS = (0.005, 0.01, 0.02, 0.05, 0.1)
FLOORS = (262144, 524288, 1000000, 2000000)


def probe(**query):
    return corpus_v2.count(**query)


def main() -> None:
    print(f"판정 기준 코퍼스 {len(corpus_v2.load_rows())}행")
    print()

    found = []

    print("=" * 96)
    print("A. 파라미터 상한 × task   (값 없는 모델은 운영 검색과 같이 제외)")
    print("=" * 96)
    print(f"{'task':32s} " + " ".join(f"{cap:>8}B" for cap in CAPS))
    for task in TASKS:
        cells = []
        for cap in CAPS:
            query = dict(
                tasks=[task],
                korean_required=True,
                max_parameters_billion=cap,
            )
            n = probe(**query)
            cells.append(n)
            if n == 0:
                found.append({"kind": "parameters", "task": task, "cap": cap, "conditions": query})
        print(f"{task:32s} " + " ".join(f"{v:9d}" for v in cells))

    print()
    print("=" * 96)
    print("B. context 하한 × task   (값 없는 모델은 운영 검색과 같이 제외)")
    print("=" * 96)
    print(f"{'task':32s} " + " ".join(f"{f:>10}" for f in FLOORS))
    for task in TASKS:
        cells = []
        for floor in FLOORS:
            query = dict(
                tasks=[task],
                korean_required=True,
                min_context_length=floor,
            )
            n = probe(**query)
            cells.append(n)
            if n == 0:
                found.append({"kind": "context", "task": task, "floor": floor, "conditions": query})
        print(f"{task:32s} " + " ".join(f"{v:10d}" for v in cells))

    print()
    print("=" * 96)
    print("C. core 풀 한정 + 수치 조건   (유명한 모델 중에는 없다는 질의)")
    print("=" * 96)
    for task in TASKS:
        for cap in (0.05, 0.1):
            query = dict(
                tasks=[task],
                korean_required=True,
                pools=["core"],
                max_parameters_billion=cap,
            )
            n = probe(**query)
            if n == 0:
                found.append({"kind": "core_parameters", "task": task, "cap": cap, "conditions": query})
                print(f"  {task:32s} core · ≤{cap}B  →  0")

    print()
    print("=" * 96)
    print(f"후보 조합 {len(found)}개 — eligible == 0 확인됨")
    print("=" * 96)
    by_task: dict[str, int] = {}
    for item in found:
        by_task[item["task"]] = by_task.get(item["task"], 0) + 1
    for task, n in sorted(by_task.items(), key=lambda x: -x[1]):
        print(f"  {task:32s} {n}개")

    OUT.write_text(json.dumps(found, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n→ {OUT}")


if __name__ == "__main__":
    main()
