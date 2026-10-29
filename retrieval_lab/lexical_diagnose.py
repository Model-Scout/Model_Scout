#!/usr/bin/env python3
"""이미 저장된 Baseline 결과에 규칙 지표를 입혀 질의를 분류한다.

Recall이 0이어도 원인이 두 가지다. 검색이 조건에 맞는 모델을 가져왔는데 라벨이
없어서 0인 경우와, 애초에 조건에 맞는 것을 못 가져온 경우다. 전자는 판정으로
풀리고 후자는 검색이나 데이터를 고쳐야 한다. 이 스크립트가 그 둘을 가른다.

검색을 다시 돌리지 않는다. 리포트에 저장된 ranked 목록을 그대로 쓴다.

실행:
    python -m retrieval_lab.lexical_diagnose
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from retrieval_lab import lexical_rules as rules

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REPORT = ROOT / "retrieval_lab" / "reports" / "lexical_exact.json"
POOLS = ("core", "low_popularity")

# 라벨이 없어 Recall이 0으로 보이는 것과, 정말 못 찾은 것을 가르는 선.
MATCH_HIGH = 0.3


def load_corpus() -> Dict[str, Dict]:
    corpus: Dict[str, Dict] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    corpus[row["model_id"]] = row
    return corpus


def classify(recall: float, match: float, requirement: Dict) -> str:
    if recall > 0:
        return "정상"
    if match >= MATCH_HIGH:
        return "라벨 공백"
    if requirement["kind"] == "direction":
        return "데이터 한계 의심"
    return "검색 실패"


def main() -> None:
    corpus = load_corpus()
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    per_query: List[Dict] = report["baseline"]["per_query"]
    print(f"코퍼스 {len(corpus):,}개 · Baseline {report['ran_at']} · 질의 {len(per_query)}개\n")

    rows = []
    for entry in per_query:
        query_id = entry["query_id"]
        requirement = rules.requirement_for(query_id)
        if requirement is None:
            print(f"  요구사항 없음: {query_id}")
            continue
        metrics = entry.get("metrics") or {}
        scored = rules.score(entry["ranked"], corpus, requirement)
        rows.append({
            "query_id": query_id,
            "kind": requirement["kind"],
            "recall@10": metrics.get("recall@10", 0.0),
            "judged@10": entry.get("judged@10", 0.0),
            "lex_match@10": scored["lex_match@10"],
            "lex_violation@10": scored["lex_violation@10"],
            "verdict": classify(metrics.get("recall@10", 0.0), scored["lex_match@10"], requirement),
        })

    header = f"{'질의':<10} {'종류':<10} {'Recall@10':>9} {'judged':>7} {'lex_match':>10} {'위반':>6}  판정"
    print(header)
    print("-" * len(header))
    for row in sorted(rows, key=lambda item: (item["kind"], -item["lex_match@10"])):
        print(f"{row['query_id']:<10} {row['kind']:<10} {row['recall@10']:>9.2f} "
              f"{row['judged@10']:>7.2f} {row['lex_match@10']:>10.2f} "
              f"{row['lex_violation@10']:>6.2f}  {row['verdict']}")

    print("\n=== 종류별 평균 ===")
    for kind in ("direction", "format", "family"):
        group = [row for row in rows if row["kind"] == kind]
        if not group:
            continue
        recall = sum(row["recall@10"] for row in group) / len(group)
        match = sum(row["lex_match@10"] for row in group) / len(group)
        violation = sum(row["lex_violation@10"] for row in group) / len(group)
        print(f"{kind:<10} 질의 {len(group):>2}개 · Recall@10 {recall:.3f} · "
              f"lex_match@10 {match:.3f} · 위반 {violation:.3f}")

    print("\n=== 판정별 ===")
    verdicts: Dict[str, List[str]] = {}
    for row in rows:
        verdicts.setdefault(row["verdict"], []).append(row["query_id"])
    for verdict, ids in sorted(verdicts.items(), key=lambda item: -len(item[1])):
        print(f"{verdict:<14} {len(ids):>2}개  {', '.join(ids)}")


if __name__ == "__main__":
    main()
