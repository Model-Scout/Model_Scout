#!/usr/bin/env python3
"""판정이 필요한 후보를 모아 워크시트로 만든다.

Baseline이 top-10으로 가져왔지만 아무도 점수를 매기지 않은 모델만 뽑는다.
각 후보에는 규칙이 본 근거(조건 충족 여부, 형식, task, 방향)를 함께 적어
사람이 판단에 쓸 정보를 한 줄에서 볼 수 있게 한다.

규칙이 "조건 위반"이라고 본 후보에는 suggested=0 을 적어 둔다. 나머지는
비워 두고 사람이 채운다. 점수를 자동으로 확정하지 않는 이유는, 조건을
만족한다는 것과 좋은 추천이라는 것이 다르기 때문이다.

실행:
    python -m retrieval_lab.lexical_worksheet
    python -m retrieval_lab.lexical_worksheet --all      # 라벨 공백 질의 외 전부
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

from retrieval_lab import lexical_rules as rules

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT.parent / "backend" / "data"
REPORT = ROOT / "retrieval_lab" / "reports" / "lexical_exact.json"
OUT_PATH = ROOT / "test" / "golden" / "labels" / "worksheet_lexical_exact.jsonl"
POOLS = ("core", "low_popularity")

# lexical_diagnose 가 "라벨 공백"으로 분류한 질의. 판정 효과가 가장 큰 곳이다.
LABEL_GAP_QUERIES = [
    "sg_g002", "sg_g003", "sg_g005", "sg_h049",
    "sg_h054", "sg_h055", "sg_h079", "sg_h081",
]


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


def evidence_for(row: Dict, requirement: Dict) -> str:
    """사람이 한 줄로 판단할 수 있게 규칙이 본 근거를 모은다."""
    meta = row.get("filter_metadata") or {}
    parts = [f"task={meta.get('primary_task')}"]
    kind = requirement["kind"]
    if kind == "direction":
        pairs = sorted(rules.explicit_pairs(row))
        languages = [code for code in (meta.get("languages") or [])]
        parts.append(f"pairs={pairs or '없음'}")
        parts.append(f"languages={len(languages)}개")
    elif kind == "format":
        artifacts = {key for key, on in (meta.get("artifacts") or {}).items() if on is True}
        parts.append(f"artifacts={sorted(artifacts) or '없음'}")
        parts.append(f"variants={meta.get('variant_types') or '없음'}")
    else:
        parts.append(f"canonical={meta.get('canonical_model_id')}")
    parts.append(f"downloads={meta.get('downloads')}")
    parts.append(f"license={meta.get('license')}")
    return " · ".join(str(part) for part in parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true",
                        help="라벨 공백 질의뿐 아니라 미판정이 있는 질의 전부")
    parser.add_argument("--top", type=int, default=10, help="질의당 상위 몇 개까지 볼지")
    args = parser.parse_args()

    corpus = load_corpus()
    report = json.loads(REPORT.read_text(encoding="utf-8"))

    wanted = None if args.all else set(LABEL_GAP_QUERIES)
    out_rows: List[Dict] = []
    per_query_counts: List[tuple] = []

    for entry in report["baseline"]["per_query"]:
        query_id = entry["query_id"]
        if wanted is not None and query_id not in wanted:
            continue
        requirement = rules.requirement_for(query_id)
        if requirement is None:
            continue
        unjudged = set(entry.get("unjudged@10") or [])
        candidates = [model_id for model_id in entry["ranked"][:args.top] if model_id in unjudged]
        for rank, model_id in enumerate(candidates, start=1):
            row = corpus.get(model_id)
            if row is None:
                continue
            satisfies = rules.satisfies(row, requirement)
            violates = rules.violates(row, requirement)
            out_rows.append({
                "query_id": query_id,
                "model_id": model_id,
                "rank": rank,
                # 규칙이 위반으로 본 것만 0을 제안한다. 나머지는 사람이 채운다.
                "suggested": 0 if (violates or not satisfies) else None,
                "score": None,
                "reason": "",
                "judge": "",
                "rule_satisfies": satisfies,
                "rule_violates": violates,
                "evidence": evidence_for(row, requirement),
            })
        per_query_counts.append((query_id, requirement["kind"], len(candidates)))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as handle:
        for row in out_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"워크시트 저장: {OUT_PATH.relative_to(ROOT)}")
    print(f"질의 {len(per_query_counts)}개 · 판정 후보 {len(out_rows)}개\n")
    print(f"{'질의':<10} {'종류':<10} {'후보':>4}")
    print("-" * 28)
    for query_id, kind, count in per_query_counts:
        print(f"{query_id:<10} {kind:<10} {count:>4}")

    auto_zero = sum(1 for row in out_rows if row["suggested"] == 0)
    print(f"\n규칙이 0점으로 제안한 후보: {auto_zero}개 (조건 위반)")
    print(f"사람이 판단할 후보       : {len(out_rows) - auto_zero}개")


if __name__ == "__main__":
    main()
