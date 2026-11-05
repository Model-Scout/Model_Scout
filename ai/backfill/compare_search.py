#!/usr/bin/env python3
"""검색 결과를 전후로 비교한다. "데이터가 채워졌다"가 아니라 "찾을 수 있게 됐다"를 본다.

골든셋 v2 의 질의 70개를 기존 코퍼스와 백필 코퍼스에 각각 돌린다. 판정 라벨이
아직 없으므로 정답률은 못 재고, 대신 세 가지를 본다.

    1. eligible  하드 필터를 통과하는 후보가 몇 개 늘었나
    2. top-10    상위 10개에 새로 들어온 모델이 몇 개인가
    3. 신규 노출 백필 덕분에 처음 상위권에 오른 모델은 무엇인가

3번이 핵심이다. 후보가 늘어도 상위에 안 오르면 사용자에겐 의미가 없다.

    python ai/backfill/compare_search.py             # sparse 만 (BGE 불필요)
    python ai/backfill/compare_search.py --dense     # dense 포함 (BGE 인덱스 필요)
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
DATA_DIR = AI_ROOT / "data"
OUT_DIR = HERE / "out"
V2 = AI_ROOT / "test" / "golden" / "v2"
REPORT_PATH = HERE / "reports" / "search_comparison.md"

POOLS = ("core", "low_popularity")
TOP_K = 10


def validator() -> Any:
    sys.path.insert(0, str(AI_ROOT))
    spec = importlib.util.spec_from_file_location(
        "cmp_validator", AI_ROOT / "05_validate_retrieval.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_corpus(directory: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for pool in POOLS:
        path = directory / f"hf_models_stage4_{pool}.jsonl"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    row.pop("embedding", None)
                    rows.append(row)
    return rows


def queries() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for path in sorted((V2 / "judged").glob("*.jsonl")):
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    out.append(json.loads(line))
    return out


def rank(module: Any, rows: List[Dict[str, Any]], query: Dict[str, Any]) -> Tuple[int, List[str]]:
    """하드 필터 + 어휘 점수로 상위를 뽑는다. 운영과 같은 함수를 쓴다."""
    conditions = dict(query["conditions"])
    conditions.setdefault("pools", list(POOLS))
    conditions["text"] = query["query"]
    eligible = [row for row in rows if module.hard_filter(row, conditions)[0]]
    scored = sorted(
        eligible, key=lambda row: module.lexical_score(row, conditions), reverse=True
    )
    deduped = module.dedupe_canonical(scored)
    return len(eligible), [row["model_id"] for row in deduped[:TOP_K]]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dense", action="store_true", help="BGE dense 채널 포함")
    args = parser.parse_args()

    module = validator()
    before = load_corpus(DATA_DIR)
    after = load_corpus(OUT_DIR)
    items = queries()

    lines: List[str] = []
    out = lines.append
    out("# 검색 결과 전후 비교")
    out("")
    out(f"골든셋 v2 질의 {len(items)}개를 기존 코퍼스({len(before)}행)와 "
        f"백필 코퍼스({len(after)}행)에 각각 돌렸다.")
    out("")
    out("하드 필터와 어휘 점수는 `05_validate_retrieval` 의 함수를 그대로 쓴다. "
        "판정 라벨이 아직 없어 정답률은 재지 않고, 후보와 상위 노출의 변화만 본다.")
    out("")

    total_elig_before = total_elig_after = 0
    changed_queries: List[Dict[str, Any]] = []
    newly_surfaced: Dict[str, int] = {}

    for item in items:
        if item["query_type"] == "abstention":
            continue
        n_before, top_before = rank(module, before, item)
        n_after, top_after = rank(module, after, item)
        total_elig_before += n_before
        total_elig_after += n_after
        entered = [model_id for model_id in top_after if model_id not in top_before]
        if entered or n_before != n_after:
            changed_queries.append({
                "query_id": item["query_id"], "type": item["query_type"],
                "query": item["query"], "elig_before": n_before, "elig_after": n_after,
                "entered": entered,
            })
        for model_id in entered:
            newly_surfaced[model_id] = newly_surfaced.get(model_id, 0) + 1

    scored = [item for item in items if item["query_type"] != "abstention"]
    out("## 1. 후보 수")
    out("")
    out(f"- 질의 {len(scored)}개 (abstention 10개 제외)")
    out(f"- eligible 합계 **{total_elig_before:,} → {total_elig_after:,}** "
        f"(+{total_elig_after - total_elig_before:,})")
    out(f"- 바뀐 질의 **{len(changed_queries)}개** / {len(scored)}")
    out("")

    out("## 2. 상위 10위에 새로 진입한 모델")
    out("")
    out(f"- 연인원 **{sum(newly_surfaced.values())}건**, 서로 다른 모델 **{len(newly_surfaced)}개**")
    out("")
    out("백필 전에는 파라미터·컨텍스트가 null이라 하드 필터에서 탈락했던 모델들이다.")
    out("")
    out("| 모델 | 진입한 질의 수 |")
    out("|---|---:|")
    for model_id, count in sorted(newly_surfaced.items(), key=lambda item: -item[1])[:20]:
        out(f"| `{model_id}` | {count} |")
    out("")

    out("## 3. 질의별 변화")
    out("")
    out("| id | 유형 | 질의 | 후보 전→후 | 신규 진입 |")
    out("|---|---|---|---|---|")
    for entry in changed_queries:
        entered = ", ".join(f"`{model_id}`" for model_id in entry["entered"][:3])
        if len(entry["entered"]) > 3:
            entered += f" 외 {len(entry['entered']) - 3}"
        out(f"| `{entry['query_id']}` | {entry['type']} | {entry['query'][:40]}… | "
            f"{entry['elig_before']} → {entry['elig_after']} | {entered or '—'} |")
    out("")

    out("## 4. abstention 영향 ⚠️")
    out("")
    out("abstention 질의 10개는 `require_known_*` 로 후보 0개를 만들었다. 백필로 "
        "값이 채워지면 후보가 0이 아니게 될 수 있다. 그러면 그 질의는 다시 써야 한다.")
    out("")
    out("| id | 질의 | 후보 전 | 후보 후 | 판정 |")
    out("|---|---|---:|---:|---|")
    broken = 0
    for item in items:
        if item["query_type"] != "abstention":
            continue
        n_before, _ = rank(module, before, item)
        n_after, _ = rank(module, after, item)
        verdict = "✅ 유지" if n_after == 0 else "❌ 재작성 필요"
        if n_after != 0:
            broken += 1
        out(f"| `{item['query_id']}` | {item['query'][:34]}… | {n_before} | {n_after} | {verdict} |")
    out("")
    out(f"**{broken}개 질의가 재작성 대상이다.**")
    out("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"\n→ {REPORT_PATH}")


if __name__ == "__main__":
    main()
