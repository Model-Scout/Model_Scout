#!/usr/bin/env python3
"""1점(같은 벤치마크 다른 표기)에 '다른 벤치마크'가 섞이지 않았는지 검사한다.

2점은 질의가 말한 표기 그대로, 1점은 같은 벤치마크의 다른 설정·표기다.
여기서 막아야 하는 것은 이름만 비슷한 **다른** 벤치마크다.

  KMMLU ← GreekMMLU·KazakhMMLU·ArabicMMLU·KMMLU-Pro 는 다른 벤치마크
  MMLU  ← MMLU-Pro·MMMLU·CMMLU·KMMLU 는 다른 벤치마크
  GSM8K ← MGSM(다국어)·KoGSM8k(한국어) 는 다른 벤치마크
  HellaSwag ← mHellaSwag·16개 언어 평균은 다국어판

    python test/model_retrieval/tools/check_benchmark_notation.py
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

AI = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

# 질문별로 1점에 들어오면 안 되는 dataset 표기.
FORBIDDEN = {
    "bm08": [r"greek", r"kazakh", r"arabic", r"indo", r"turkish", r"global", r"^cmmlu", r"kmmlu-pro", r"^mmlu\b"],
    "bm18": [r"mmlu[- ]?pro", r"mmmlu", r"cmmlu", r"kmmlu", r"greek", r"kazakh", r"arabic", r"indo", r"turkish", r"global"],
    "bm19": [r"^mmlu$", r"^mmlu \(", r"^mmlu _", r"redux", r"mmmlu"],
    "bm20": [r"mgsm", r"kogsm"],
    "bm21": [r"mgsm", r"kogsm"],
    "bm24": [r"mhellaswag", r"16 languages"],
    "bm29": [r"^mmlu\b", r"greek", r"kazakh"],
    "bm30": [r"koifeval"],
    "bm17": [r"mgpqa"],
}


def main() -> int:
    import corpus
    import scan

    spec = importlib.util.spec_from_file_location(
        "spec_benchmark", AI / "test" / "model_retrieval" / "queries" / "spec_benchmark.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rows = corpus.load_corpus()

    problems = []
    for item in mod.QUERIES:
        patterns = FORBIDDEN.get(item["qid"])
        if not patterns:
            continue
        query = dict(item)
        query.update(query_id=item["qid"], expected_behavior="recommend", query=item["text"])
        for model_id, decision in scan.scan_query(query, rows)["decisions"].items():
            if decision["class"] == "auto_rejected":
                continue
            dataset = str(((decision.get("evidence") or {}).get("result") or {}).get("dataset") or "")
            for pattern in patterns:
                if re.search(pattern, dataset, re.IGNORECASE):
                    problems.append(f"{item['qid']}: {dataset!r} ({model_id}) — 패턴 {pattern!r}")
    if problems:
        print(f"❌ 다른 벤치마크가 섞였다 ({len(problems)}건)")
        for line in problems:
            print(f"  · {line}")
        return 1
    print(f"✅ 오염 0건 — 질문 {len(FORBIDDEN)}개에서 다른 벤치마크가 섞이지 않았다")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
