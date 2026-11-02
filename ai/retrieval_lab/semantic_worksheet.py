#!/usr/bin/env python3
"""semantic_capability 보완 판정 중 1점을 다시 볼 워크시트를 만든다.

supplemental_judgments.jsonl의 1점(Claude 1차 판정) 중 판정 이유에 위반·불확실
표현이 들어 있는 것만 뽑는다. min_grade=1로 채점하면 이것들이 전부 "정답"으로
세어져 지표를 부풀린다(재채점에서 1점 기준 P@10 0.7~1.0인 질의가 2점 기준으로는
top-10에 정답이 하나도 없었다).

이유 표현은 세 갈래로 나눈다. 갈래마다 다시 볼 질문이 다르다.

    size_speed     "무거움·느림"      질의가 경량을 요구했다면 위반이다 → 0 후보
    not_specialized "~특화 아님"       범용 모델로 할 수는 있다 → 1과 0의 경계(팀 기준 필요)
    no_evidence    "불명·부족·않음"    카드가 침묵한다 → 점수 대신 unjudged(보류) 후보

점수는 0 / 1 / 2 / "unjudged" 중 하나를 적는다. 판정 전에 README(readme_path)를
반드시 연다. lexical·structured 검증에서 오류의 주원인이 README 미확인이었다.

실행:
    python -m retrieval_lab.semantic_worksheet
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
LABEL_DIR = ROOT / "test" / "golden" / "labels"
REPORT = ROOT / "retrieval_lab" / "reports" / "semantic_capability.json"
SUPPLEMENT = LABEL_DIR / "supplemental_judgments.jsonl"
OUT_PATH = LABEL_DIR / "worksheet_semantic_capability.jsonl"
POOLS = ("core", "low_popularity")
QUERY_FILES = ("semantic_golden_queries.jsonl", "semantic_judged_queries.jsonl")

CAVEATS = {
    "size_speed": re.compile(r"무거|느림"),
    "not_specialized": re.compile(r"아님"),
    "no_evidence": re.compile(r"불명|부족|않음"),
}
# 질의가 경량·저사양을 요구하는지. "GPU 서버"가 있으면 요구하지 않은 것으로 본다.
LIGHT = re.compile(r"GPU\s*없|CPU|가벼|경량|소형|작게|작은|Jetson|엣지|온디바이스|휴대폰|모바일|태블릿|빠르게|속도")
HEAVY_OK = re.compile(r"큰\s*GPU|GPU\s*서버")
# 경량 질의에서 이 크기 이상이면 위반이 확인된 것으로 본다.
LIGHT_MAX_BILLION = 4.0


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_corpus() -> Dict[str, Dict[str, Any]]:
    corpus: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if path.exists():
            for row in read_jsonl(path):
                corpus[row["model_id"]] = row
    return corpus


def caveat_of(note: str) -> Optional[str]:
    # 크기·속도 위반이 가장 확실하므로 먼저 본다.
    for name, pattern in CAVEATS.items():
        if pattern.search(note):
            return name
    return None


def evidence_for(row: Dict[str, Any]) -> str:
    meta = row.get("filter_metadata") or {}
    parts = [
        f"task={meta.get('primary_task')}",
        f"params={meta.get('parameter_count_billion')}",
        f"gguf={meta.get('artifacts', {}).get('gguf')}",
        f"quant={meta.get('quantization', {}).get('method')}",
        f"variant={','.join(meta.get('variant_types') or []) or None}",
        f"canonical={row.get('canonical_model_id')}",
        f"downloads={meta.get('downloads')}",
    ]
    return " · ".join(parts)


def main() -> None:
    corpus = load_corpus()
    queries = {item["id"]: item for name in QUERY_FILES if (LABEL_DIR / name).exists()
               for item in read_jsonl(LABEL_DIR / name)}
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    # 지표에 실제로 들어가는 후보부터 본다. Baseline과 최적 설정의 top-10.
    top10: Dict[str, set] = {}
    for run in (report["baseline"], report["best"]):
        for entry in run["per_query"]:
            top10.setdefault(entry["query_id"], set()).update(entry["ranked"][:10])

    out_rows: List[Dict[str, Any]] = []
    for judgment in read_jsonl(SUPPLEMENT):
        if judgment.get("score") != 1:
            continue
        caveat = caveat_of(judgment.get("note") or "")
        query = queries.get(judgment["query_id"])
        row = corpus.get(judgment["model_id"])
        if caveat is None or query is None or row is None:
            continue
        light = bool(LIGHT.search(query["text"])) and not HEAVY_OK.search(query["text"])
        params = (row.get("filter_metadata") or {}).get("parameter_count_billion")
        # 경량 질의인데 크기가 확인된 대형 모델만 0을 제안한다. 나머지는 사람이 정한다.
        size_violation = light and params is not None and params >= LIGHT_MAX_BILLION
        out_rows.append({
            "query_id": judgment["query_id"],
            "query_text": query["text"],
            "model_id": judgment["model_id"],
            "in_top10": judgment["model_id"] in top10.get(judgment["query_id"], set()),
            "caveat": caveat,
            "previous_score": 1,
            "previous_note": judgment.get("note"),
            "query_light": light,
            "suggested": 0 if size_violation else None,
            "score": None,
            "reason": "",
            "judge": "",
            "evidence": evidence_for(row),
            "readme_path": (row.get("benchmark_metadata") or {}).get("readme_path"),
        })

    out_rows.sort(key=lambda r: (not r["in_top10"], list(CAVEATS).index(r["caveat"]), r["query_id"], r["model_id"]))
    with OUT_PATH.open("w", encoding="utf-8") as handle:
        for item in out_rows:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"워크시트 저장: {OUT_PATH.relative_to(ROOT)} · {len(out_rows)}건")
    by_caveat = Counter(r["caveat"] for r in out_rows)
    in_top = Counter(r["caveat"] for r in out_rows if r["in_top10"])
    print(f"{'갈래':<16} {'전체':>4} {'top-10':>7}")
    for name in CAVEATS:
        print(f"{name:<16} {by_caveat[name]:>4} {in_top[name]:>7}")
    print(f"규칙이 0점으로 제안: {sum(r['suggested'] == 0 for r in out_rows)}건 "
          f"(경량 질의 + {LIGHT_MAX_BILLION:g}B 이상 확인)")
    print(f"질의 {len({r['query_id'] for r in out_rows})}개")


if __name__ == "__main__":
    main()
