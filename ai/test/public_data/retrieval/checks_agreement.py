"""Agreement of the service's condition verdicts (ai/condition_checks.py) with the experiment checker that made the
golden labels (golden_prep.condition_checks), on every judged portal pair of a question set. No API call.

    python -X utf8 test/public_data/retrieval/checks_agreement.py --labels <labels> --spec <spec> --out <report.md>

Both get the spec's human conditions, so only the checkers differ: the experiment one reads the collected rows
(public_enriched), the service one only what a server has (graph entity, v2 card). realtime there is
current_value here. A 部分 (partial) verdict has no counterpart in the service, which keeps partial alternatives
apart from conditions; it is listed, not counted as a disagreement.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pilot  # noqa: E402

sys.path.insert(0, str(pilot.AI))
import condition_checks as cc  # noqa: E402
import data_conditions as dc  # noqa: E402

KEYS = {"region": "region", "delivery": "delivery", "commercial": "commercial", "kogl_type1_only": "kogl_type1_only",
        "realtime": "current_value"}


def service_conditions(spec):
    c = spec["conditions"]
    return {**dc.defaults(), "region": c.get("region"), "region_detail": spec.get("region_detail"),
            "region_scope": spec.get("region_scope"),
            "delivery": c.get("delivery") if c.get("delivery") in ("api", "file") else None,
            "current_value": bool(c.get("realtime")),
            "kogl_type1_only": bool(pilot.gp.TYPE1_ONLY_RE.search(spec["query"]))}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--labels", type=Path, action="append", required=True)
    parser.add_argument("--spec", type=Path, action="append", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    pilot.hs.use_corpus("v2")
    entities = {e["name"]: e for e in pilot.hs.load_graph()[0].values() if e["kind"] == "dataset"}
    cards = pilot.hs._local_cards()
    conditions = pilot.Conditions()
    table, examples, pairs, partial = defaultdict(Counter), defaultdict(list), 0, []
    for labels_path, spec_path in zip(args.labels, args.spec, strict=True):
        specs = {s["query_id"]: s for s in pilot.read_jsonl(spec_path)}
        for lb in pilot.read_jsonl(labels_path):
            spec = specs[lb["query_id"]]
            want = service_conditions(spec)
            judged = list(lb["relevant"]) + lb["judged_irrelevant"] + lb["must_exclude"]
            for d in dict.fromkeys(judged):
                ent = entities.get(d) or {}
                if ent.get("source") not in cc.PORTALS:
                    continue
                pairs += 1
                gold = pilot.gp.condition_checks({"query": spec["query"], "conditions": spec["conditions"]}, conditions.facts(d))
                serv = {c["key"]: c for c in cc.judge(want, bool(spec["conditions"].get("commercial")), ent,
                                                      pilot.hs.card_facts(cards.get(d, "")))["checks"]}
                for gk, sk in KEYS.items():
                    if gk not in gold and sk not in serv:
                        continue
                    g = gold.get(gk, {}).get("status", "없음")
                    s = serv.get(sk, {}).get("status", "없음")
                    table[gk][(g, s)] += 1
                    if g == pilot.gp.PARTIAL:
                        partial.append((lb["query_id"], d, gk, s))
                    elif g != s and len(examples[(gk, g, s)]) < 3:
                        examples[(gk, g, s)].append(f"{lb['query_id']} {d} `{ent.get('title')}`: 실험 '{gold[gk]['basis']}' / "
                                                    f"서비스 '{serv.get(sk, {}).get('basis')}'")
    L = ["# 조건 판정 비교: 서비스 판정기 vs 실험용 판정기", "",
         f"라벨 {', '.join(p.stem for p in args.labels)} · 명세 {', '.join(p.stem for p in args.spec)}. "
         f"판정된 공공포털 쌍 {pairs}개. 두 판정기 모두 명세의 사람이 정한 조건을 받았다.", ""]
    for gk, counts in table.items():
        n = sum(counts.values())
        same = sum(v for (g, s), v in counts.items() if g == s)
        part = sum(v for (g, s), v in counts.items() if g == pilot.gp.PARTIAL)
        L += [f"## {gk} ({n}칸, 일치 {same}, 실험 '부분' {part}, 불일치 {n - same - part})", "",
              "| 실험 → 서비스 | 칸 |", "|---|---:|"] + [f"| {g} → {s} | {v} |" for (g, s), v in sorted(counts.items())]
        L += [""] + [f"- {g} → {s}: {e}" for (k, g, s), es in sorted(examples.items()) if k == gk for e in es] + [""]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
