"""Regression check of a service planner change: a decompose_compare run of the changed planner against the
baseline service plans, at the same routes and the same fixed retriever (hybrid RRF k 20, spec filter).

    python -X utf8 test/public_data/retrieval/decompose_regress.py --new <decompose_compare run> \
        --base-plans <run with the baseline plans.jsonl> --base-scores <run whose scores.json has base/spec> \
        --spec <spec> [--labels <labels>] [--out report.md]

Search: dq_terms (the service's input) of the new plans against base/spec of a decompose_v2 run (the baseline
plans' dq_terms with the spec filter), paired per question. Extraction: the new data_conditions scored like
decompose_v2 (region at 시도 level, a named 시군구 also right; detail kept counted apart).
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decompose_v2 as dv  # noqa: E402
import pilot  # noqa: E402
import sweep  # noqa: E402

MEASURES = (("2점 MRR@5", "two", "raw2", "mrr@5"), ("nDCG@5", "rec", "raw", "ndcg@5"),
            ("2점 R@10", "two", "raw2", "recall@10"), ("P@10", "rec", "raw", "precision@10"))


def extracted(plan):
    """The service plan's data_conditions in decompose_v2's vocabulary (current_value stands for realtime)."""
    c = plan["data_conditions"]
    return {"region": dv.canon_region(c["region"]) or c["region_detail"], "region_scope": c["region_scope"],
            "delivery": c["delivery"], "realtime": c["current_value"], "commercial": bool(plan["commercial_only"]),
            "kogl_type1_only": c["kogl_type1_only"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--base-plans", type=Path, required=True)
    parser.add_argument("--base-scores", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    new = {p["query_id"]: p for p in pilot.read_jsonl(args.new / "plans.jsonl")}
    base = {p["query_id"]: p for p in pilot.read_jsonl(args.base_plans / "plans.jsonl")}
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    s_new = json.loads((args.new / "scores.json").read_text(encoding="utf-8"))["dq_terms"]
    s_base = json.loads((args.base_scores / "scores.json").read_text(encoding="utf-8"))["base/spec"]
    rec = [q for q in new if "raw" in s_new[q]]
    sets = {"rec": rec, "two": [q for q in rec if "raw2" in s_base[q]]}
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")  # noqa: E731

    same_q = sum(new[q]["dataset_query"] == base[q]["dataset_query"] for q in new)
    same_t = sum(new[q]["dataset_terms"] == base[q]["dataset_terms"] for q in new)
    L = [f"# 서비스 분해 회귀 확인: `{args.new.as_posix()}`", "",
         f"기준선 분해 `{args.base_plans.as_posix()}`, 기준선 점수 `{args.base_scores.as_posix()}` (base/spec), 명세 `{args.spec.stem}`. "
         "라우팅은 기준선 것을 그대로 썼다. 검색기 고정(hybrid RRF k 20, 명세 조건 필터).", "",
         f"- dataset_query 그대로 {same_q}/{len(new)}, dataset_terms 그대로 {same_t}/{len(new)}",
         f"- 새 상위 10의 미판정 합 {sum(s_new[q]['unjudged@10'] for q in rec)} (기준선 {sum(s_base[q]['unjudged@10'] for q in rec)}). "
         "미판정은 raw에서 적중이 아니므로, 미판정이 남아 있으면 새 분해 점수가 낮게 나온다.", "",
         "| 지표 | 문항 | 기준선 | 새 분해 | 차이 [95% 구간] |", "|---|---:|---:|---:|---|"]
    for name, which, key, m in MEASURES:
        qs = sets[which]
        a, b = [s_base[q][key][m] for q in qs], [s_new[q][key][m] for q in qs]
        d = sweep.interval([y - x for x, y in zip(a, b)])
        L.append(f"| {name} | {len(qs)} | {mean(a):.3f} | {mean(b):.3f} | {d[0]:+.3f} [{d[1]:+.3f}, {d[2]:+.3f}] |")
    cond = {"region", "region_scope", "delivery", "realtime", "commercial", "kogl_type1_only"}
    tot, per, detail, errors = Counter(), Counter(), [], []
    for q in sorted(new):
        want, got = dv.truth(specs[q]), extracted(new[q])
        cmp = dv.compare(want, got, specs[q])
        tot.update(cmp.values())
        per.update((c, s) for c, s in cmp.items())
        bad = [f"{c} {s} (명세 {want[c]!r}, 추출 {got[c]!r})" for c, s in cmp.items() if s in ("missed", "added", "wrong")]
        if bad:
            errors.append(f"- {q}: " + "; ".join(bad))
        if d := specs[q].get("region_detail"):
            detail.append(f"{q} {d} {'O' if dv.detail_kept({**new[q], 'explicit': {'region': new[q]['data_conditions']['region_detail']}}, d) else 'X'}")
    L += ["", f"## 조건 추출 (명세가 답지, {len(new)}문항, 실시간 = current_value)", "",
          "| 조건 | 맞음 | 누락 | 잘못 추가 | 값 틀림 |", "|---|---:|---:|---:|---:|"]
    L += [f"| {c} | {per[(c, 'ok')]} | {per[(c, 'missed')]} | {per[(c, 'added')]} | {per[(c, 'wrong')]} |" for c in sorted(cond)]
    L += [f"| **합계** | {tot['ok']} | {tot['missed']} | {tot['added']} | {tot['wrong']} |", ""]
    if detail:
        L += ["세부 지역 보존: " + ", ".join(detail), ""]
    L += ["오류:", ""] + (errors or ["- 없음"])
    L += ["", "## 분해가 바뀐 문항", "", "| 문항 | 기준선 dataset_terms | 새 dataset_terms | 새 dataset_query |", "|---|---|---|---|"]
    L += [f"| {q} | {', '.join(base[q]['dataset_terms'])} | {', '.join(new[q]['dataset_terms'])} | {new[q]['dataset_query']} |"
          for q in sorted(new) if (new[q]["dataset_query"], new[q]["dataset_terms"]) != (base[q]["dataset_query"], base[q]["dataset_terms"])]
    text = "\n".join(L) + "\n"
    (args.out or args.new / "regress.md").write_text(text, encoding="utf-8")
    print(text[:3000])


if __name__ == "__main__":
    main()
