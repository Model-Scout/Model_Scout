"""Common evaluator for public-data retrieval experiments: ranked lists in, metrics out.

    python test/public_data/evaluate_public.py --runs baseline.jsonl rewrite.jsonl \
        [--labels <v5>] [--duplicates data/hypergraph_v2/duplicates.json] [--types types.json] \
        [--out report.json] [--unjudged-out unjudged.jsonl]

A run file has one line per query: {"query_id": "p001", "ranked": ["data_go_kr/...", ...], "latency_ms": 812}.
It must hold every evaluable query of the labels (abstention ones too) and nothing unknown.
The evaluator does not search; any retriever that writes this format can be compared.

Rules (fixed; change them only with a new version noted in test/public_data/README.md):
- Formulas are retrieval_lab/metrics.py (Recall/Precision/F1/Hit@5,10, MRR@5, nDCG@5, MAP@5).
  Recall = found distinct answers / all distinct answers, no cap at k.
- Two scores per query: `direct` counts grade 2 only, `any` counts grade >= 1. A query without a
  grade-2 answer has no `direct` score and is counted in `no_direct_answer`. nDCG uses the grades
  in both.
- Cross-listed copies (--duplicates) are one dataset: labels and ranked ids are mapped to the
  canonical id and a ranked list keeps the first occurrence only.
- raw: anything not labelled relevant is a miss. condensed: datasets without a judgment are dropped
  from the ranking first. Held pairs (label `unjudged`, '?') are misses in raw and dropped in
  condensed, and counted in held@10.
- must_exclude@10: excluded datasets in the top 10 (condition violations).
- Abstention queries get no accuracy (the rankers have no empty-result path): only how many
  datasets were returned and how many of the top 10 are judged relevant or excluded.
- --unjudged-out merges every run's top-10 datasets that have no judgment, without run names, so
  they can be judged blind.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

AI = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(AI))

from retrieval_lab.metrics import percentile, ranking_metrics  # noqa: E402

V5 = Path(__file__).resolve().parent / "corpus_v2" / "golden_prep" / "batch3" / "labels_llm_v5.jsonl"
K = 10
SHOWN = ("recall@5", "recall@10", "precision@5", "precision@10", "f1@5", "f1@10",
         "hit@10", "mrr@5", "ndcg@5", "map@5")  # nrecall (recall capped at k) is left out on purpose


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_duplicates(path: Optional[Path]) -> Dict[str, str]:
    """duplicates.json ({copy: {"canonical": id, ...}}) -> {copy: canonical}."""
    if not path:
        return {}
    return {copy: entry["canonical"] for copy, entry in json.loads(path.read_text(encoding="utf-8")).items()}


def canonical_grades(label: Mapping[str, Any], canonical: Mapping[str, str]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for dataset, grade in label["relevant"].items():
        key = canonical.get(dataset, dataset)
        out[key] = max(int(grade), out.get(key, 0))
    return out


def _dedupe(ids: Iterable[str], canonical: Mapping[str, str]) -> List[str]:
    seen, out = set(), []
    for d in ids:
        key = canonical.get(d, d)
        if key not in seen:
            seen.add(key)
            out.append(key)
    return out


def _pick(m: Mapping[str, float]) -> Dict[str, float]:
    return {key: m[key] for key in SHOWN}


def score_query(label: Mapping[str, Any], ranked: Sequence[str], canonical: Mapping[str, str]) -> Dict[str, Any]:
    grades = canonical_grades(label, canonical)
    as_set = lambda ids: {canonical.get(d, d) for d in ids}  # noqa: E731
    excluded = as_set(label["must_exclude"])
    held = as_set(label["unjudged"])
    judged = set(grades) | excluded | as_set(label["judged_irrelevant"])
    ranked = _dedupe(ranked, canonical)
    top = ranked[:K]
    condensed = [d for d in ranked if d in judged]
    out: Dict[str, Any] = {
        "query_id": label["query_id"],
        "judged@10": sum(d in judged for d in top) / len(top) if top else 0.0,
        "held@10": sum(d in held for d in top),
        "must_exclude@10": sum(d in excluded for d in top),
        "unjudged_top10": [d for d in top if d not in judged and d not in held],
        "any": None, "direct": None, "abstain": None,
    }
    if label["expected_behavior"] == "abstain":
        out["abstain"] = {"returned": len(ranked), "judged_relevant_or_excluded": sum(d in grades or d in excluded for d in top)}
        return out
    for name, min_grade in (("any", 1), ("direct", 2)):
        if any(g >= min_grade for g in grades.values()):
            out[name] = {"raw": _pick(ranking_metrics(ranked, grades, min_grade)),
                         "condensed": _pick(ranking_metrics(condensed, grades, min_grade))}
    return out


def _mean(rows: List[Dict[str, float]]) -> Optional[Dict[str, float]]:
    return {key: sum(r[key] for r in rows) / len(rows) for key in SHOWN} if rows else None


def summarize(scored: List[Dict[str, Any]], latencies: Sequence[float] = ()) -> Dict[str, Any]:
    with_any = [s for s in scored if s["any"]]
    with_direct = [s for s in scored if s["direct"]]
    return {
        "queries": len(scored),
        "direct_queries": len(with_direct),
        "no_direct_answer": len(scored) - len(with_direct),
        "any": {view: _mean([s["any"][view] for s in with_any]) for view in ("raw", "condensed")},
        "direct": {view: _mean([s["direct"][view] for s in with_direct]) for view in ("raw", "condensed")},
        "judged@10": sum(s["judged@10"] for s in scored) / len(scored) if scored else None,
        "held@10": sum(s["held@10"] for s in scored),
        "queries_with_must_exclude@10": sum(1 for s in scored if s["must_exclude@10"]),
        "unjudged@10": sum(len(s["unjudged_top10"]) for s in scored),
        "p95_ms": percentile(list(latencies), 95),
        "p99_ms": percentile(list(latencies), 99),
    }


def evaluate(labels: Sequence[Mapping[str, Any]], runs: Mapping[str, Sequence[str]], canonical: Mapping[str, str],
             types: Optional[Mapping[str, str]] = None, latency: Optional[Mapping[str, float]] = None) -> Dict[str, Any]:
    by_id = {l["query_id"]: l for l in labels}
    unknown = sorted(set(runs) - set(by_id))
    if unknown:
        raise ValueError(f"run has queries not in labels: {unknown}")
    missing = sorted(q for q, l in by_id.items() if l["evaluable"] and q not in runs)
    if missing:
        raise ValueError(f"run is missing evaluable queries: {missing}")
    types = types or {}
    latency = latency or {}
    per_query, abstain, groups = [], [], {}
    for qid, label in sorted(by_id.items()):
        if not label["evaluable"]:
            continue
        s = score_query(label, runs[qid], canonical)
        s["type"] = types.get(qid, label["query_type"])
        per_query.append(s)
        if s["abstain"]:
            abstain.append({"query_id": qid, **s["abstain"]})
        else:
            groups.setdefault(s["type"], []).append(s)
    lat = lambda rows: [latency[s["query_id"]] for s in rows if s["query_id"] in latency]  # noqa: E731
    summary = {t: summarize(rows, lat(rows)) for t, rows in sorted(groups.items())}
    everything = [s for rows in groups.values() for s in rows]
    summary["all"] = summarize(everything, lat(everything))
    return {"summary": summary, "abstain": abstain, "per_query": per_query,
            "skipped_not_evaluable": sorted(q for q, l in by_id.items() if not l["evaluable"])}


def load_run(path: Path):
    rows = read_jsonl(path)
    ids = [r["query_id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{path}: a query appears more than once")
    return ({r["query_id"]: list(r["ranked"]) for r in rows},
            {r["query_id"]: float(r["latency_ms"]) for r in rows if r.get("latency_ms") is not None})


def _fmt(v: Optional[float]) -> str:
    return "    -" if v is None else f"{v:5.2f}"


def print_report(name: str, result: Dict[str, Any]) -> None:
    print(f"\n== {name}")
    print("direct = 2점만, any = 1점 포함 | raw = 미판정은 오답, cond = 미판정 제외")
    print(f"{'type':<22} {'n':>3} {'n2':>3} | {'R@5':>5} {'R@10':>5} {'MRR':>5} {'nDCG':>5} | "
          f"{'R@10':>5} {'MRR':>5} | {'R@10':>5} | {'jdg':>5} {'excl':>4} {'p95':>6}")
    print(f"{'':<22} {'':>3} {'':>3} | {'direct raw':^23} | {'any raw':^11} | {'cond':>5} |")
    for t, s in result["summary"].items():
        d, a, dc = s["direct"]["raw"] or {}, s["any"]["raw"] or {}, s["direct"]["condensed"] or {}
        p95 = "-" if s["p95_ms"] is None else f"{s['p95_ms']:.0f}"
        print(f"{t:<22} {s['queries']:>3} {s['direct_queries']:>3} | "
              f"{_fmt(d.get('recall@5'))} {_fmt(d.get('recall@10'))} {_fmt(d.get('mrr@5'))} {_fmt(d.get('ndcg@5'))} | "
              f"{_fmt(a.get('recall@10'))} {_fmt(a.get('mrr@5'))} | {_fmt(dc.get('recall@10'))} | "
              f"{_fmt(s['judged@10'])} {s['queries_with_must_exclude@10']:>4} {p95:>6}")
    for a in result["abstain"]:
        print(f"abstain {a['query_id']}: {a['returned']} returned, {a['judged_relevant_or_excluded']} judged relevant/excluded in top {K}")
    if result["skipped_not_evaluable"]:
        print(f"not evaluable (skipped): {', '.join(result['skipped_not_evaluable'])}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", type=Path, nargs="+", required=True)
    parser.add_argument("--labels", type=Path, default=V5)
    parser.add_argument("--duplicates", type=Path, help="duplicates.json of the corpus the runs searched")
    parser.add_argument("--types", type=Path, help="json {query_id: type} to group by instead of the label query_type")
    parser.add_argument("--out", type=Path, help="write the full report (per query) as json")
    parser.add_argument("--unjudged-out", type=Path, help="jsonl of unjudged top-10 pairs merged over all runs, run names hidden")
    args = parser.parse_args()
    labels = read_jsonl(args.labels)
    canonical = load_duplicates(args.duplicates)
    types = json.loads(args.types.read_text(encoding="utf-8")) if args.types else None
    header = {"labels": str(args.labels), "labels_sha256": sha256(args.labels),
              "duplicates": str(args.duplicates) if args.duplicates else None,
              "duplicates_sha256": sha256(args.duplicates) if args.duplicates else None,
              "types": str(args.types) if args.types else "label query_type"}
    print("eval " + json.dumps(header, ensure_ascii=False))
    if not canonical:
        print("[주의] --duplicates 없음: 교차 등록 사본을 다른 데이터로 셈")
    report, pending = {"header": header, "runs": {}}, set()
    for path in args.runs:
        runs, latency = load_run(path)
        result = evaluate(labels, runs, canonical, types, latency)
        report["runs"][path.name] = {"sha256": sha256(path), **result}
        print_report(f"{path.name} (sha256 {sha256(path)[:12]})", result)
        pending |= {(s["query_id"], d) for s in result["per_query"] for d in s["unjudged_top10"]}
    if args.out:
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\nreport -> {args.out}")
    if args.unjudged_out:
        args.unjudged_out.write_text("".join(json.dumps({"query_id": q, "dataset_id": d}, ensure_ascii=False) + "\n"
                                             for q, d in sorted(pending)), encoding="utf-8")
        print(f"{len(pending)} unjudged pairs -> {args.unjudged_out}")


if __name__ == "__main__":
    main()
