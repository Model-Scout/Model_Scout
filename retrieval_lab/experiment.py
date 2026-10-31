"""Per-query-type A/B experiments for the Retrieval Planner.

For each query type:
  1. Baseline (BGE-M3 + BM25, weighted RRF 0.5/0.5, no pre-retrieval)
  2. Single A/B: Rewrite, Decomposition, Multi-Query, HyDE, Name Lookup (one at a time)
  3. Combinations of the strategies that beat the baseline on --metric
  4. Dense-weight search (Optuna or grid, 0.1-0.9, sparse = 1 - dense) on the best combination,
     and on the baseline too when a pre-retrieval setting won (weight alone may tie it for free)
Reports go to retrieval_lab/reports/<type>.md|json; --write-planner stores the
winner in planner_config.json.

Examples:
    python -m retrieval_lab.experiment --types semantic_capability,model_comparison
    python -m retrieval_lab.experiment --types lexical_exact --stage single
    python -m retrieval_lab.experiment --stage baseline            # no LLM needed
    python -m retrieval_lab.experiment --stage weight              # baseline + dense-weight search, no LLM
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from retrieval_lab import golden, metrics
from retrieval_lab.pipeline import Retriever
from retrieval_lab.planner import (
    BASELINE,
    ELEMENTS,
    PLAN_QUERY_TYPES,
    RetrievalPlan,
    hard_filter_plan,
    save_type_plan,
    with_dense_weight,
    with_strategies,
)
from retrieval_lab.pre_retrieval import STRATEGIES, LLMUnavailable, llm_model

# 조건 값이 없는 모델을 거르는 하드 필터. 코퍼스의 parameter_count 39%,
# context_length 38%가 비어 있어 수치 조건이 붙은 유형에서 결과가 갈린다.
KNOWN_ONLY_FILTERS = {"require_known_parameters": True, "require_known_context": True}

REPORT_DIR = Path(__file__).resolve().parent / "reports"
TABLE_COLUMNS = (
    ("Recall@5", "recall@5"), ("Recall@10", "recall@10"), ("F1@10", "f1@10"), ("MRR@5", "mrr@5"),
    ("nDCG@5", "ndcg@5"), ("MAP@5", "map@5"), ("p95", "p95_ms"),
)
DETAIL_COLUMNS = (
    ("P@5", "precision@5"), ("P@10", "precision@10"), ("F1@5", "f1@5"), ("Hit@10", "hit@10"),
    ("nRecall@10", "nrecall@10"), ("p99", "p99_ms"), ("제외 위반@10", "must_exclude_violation_rate@10"), ("Judged@10", "judged@10"),
)


def evaluate(retriever: Retriever, queries: Sequence[golden.GoldenQuery], plan: RetrievalPlan, min_grade: int) -> Dict[str, Any]:
    per_query: List[Dict[str, Any]] = []
    for query in queries:
        # 서비스(planner.plan_for)와 같은 함수로 필터를 만든다. 측정한 설정과
        # 서비스하는 설정이 갈라지지 않게 하는 유일한 방법이다.
        query_plan = replace(plan, query_type=query.plan_query_type,
                             hard_filters=hard_filter_plan(plan.hard_filters, query.query))
        result = retriever.run(query.text, query_plan)
        top10 = result.ranked[:10]
        per_query.append({
            "query_id": query.query_id,
            "expected_behavior": query.expected_behavior,
            "ranked": result.ranked,
            "eligible": result.eligible_count,
            "metrics": metrics.ranking_metrics(result.ranked, query.grades, min_grade) if query.scored else None,
            "relevant": sorted(model_id for model_id, grade in query.grades.items() if grade >= min_grade),
            "missed@10": sorted(m for m, g in query.grades.items() if g >= min_grade and m not in top10),
            "must_exclude_checked": bool(query.must_exclude),
            "must_exclude_hits": [model_id for model_id in top10 if model_id in query.must_exclude],
            "unjudged@10": [] if query.judged is None else [m for m in top10 if m not in query.judged],
            "judged@10": None if query.judged is None or not top10 else sum(m in query.judged for m in top10) / len(top10),
            "latency_ms": result.latency_ms,
            "dense_queries": result.dense_queries,
            "sparse_queries": result.sparse_queries,
        })
    return {"plan": plan.to_dict(), "label": plan.label(), "summary": metrics.aggregate(per_query), "per_query": per_query}


def score_of(run: Dict[str, Any], metric: str) -> Tuple[float, ...]:
    summary = run["summary"]
    # Ties: fewer pre-retrieval calls, then lower p95.
    return (
        summary.get(metric) or 0.0,
        summary.get("recall@5") or 0.0,
        summary.get("ndcg@5") or 0.0,
        -sum(1 for strategy in STRATEGIES if run["plan"].get(f"use_{strategy}")),
        -(summary.get("p95_ms") or 0.0),
    )


def quality_of(run: Dict[str, Any], metric: str) -> Tuple[float, ...]:
    """score_of without latency: weight choices must not hinge on timing noise."""
    return score_of(run, metric)[:4]


def weight_choice(runs: Sequence[Dict[str, Any]], metric: str) -> Dict[str, Any]:
    # On equal quality, keep the weight closest to the 0.5 baseline.
    return max(runs, key=lambda run: (quality_of(run, metric), -abs(run["plan"]["dense_weight"] - BASELINE.dense_weight)))


def try_evaluate(retriever, queries, plan, min_grade, log, name: str = "") -> Optional[Dict[str, Any]]:
    started = time.perf_counter()
    try:
        run = evaluate(retriever, queries, plan, min_grade)
    except LLMUnavailable as error:
        log(f"  {plan.label()}: 건너뜀 ({error})")
        return None
    summary = run["summary"]
    log(f"  {name or plan.label():<40} Recall@10={fmt(summary['recall@10'])} nDCG@5={fmt(summary['ndcg@5'])} "
        f"p95={fmt(summary['p95_ms'], 'ms')} ({time.perf_counter() - started:.0f}s)")
    return run


def weight_search(retriever, queries, plan, min_grade, metric, method, trials, log) -> List[Dict[str, Any]]:
    runs: Dict[float, Dict[str, Any]] = {}

    def run_at(dense_weight: float) -> Dict[str, Any]:
        dense_weight = round(dense_weight, 2)
        if dense_weight not in runs:
            runs[dense_weight] = evaluate(retriever, queries, with_dense_weight(plan, dense_weight), min_grade)
        return runs[dense_weight]

    if method == "grid":
        for step in range(1, 10):
            run_at(step / 10)
    elif method == "optuna":
        import optuna

        optuna.logging.set_verbosity(optuna.logging.WARNING)
        study = optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler(seed=42))
        # The plan's grid (0.1-0.9, step 0.1) first, then TPE refines at 0.05 steps.
        for step in range(1, 10):
            study.enqueue_trial({"dense_weight": step / 10})
        study.optimize(
            lambda trial: run_at(trial.suggest_float("dense_weight", 0.1, 0.9, step=0.05))["summary"].get(metric) or 0.0,
            n_trials=trials,
        )
    ordered = [runs[key] for key in sorted(runs)]
    best = weight_choice(ordered, metric)
    log(f"  가중치 탐색({method}, {len(ordered)}점): dense={best['plan']['dense_weight']} "
        f"{metric}={fmt(best['summary'].get(metric))}")
    return ordered


def fmt(value: Optional[float], unit: str = "") -> str:
    if value is None:
        return "-"
    return f"{value:.0f}{unit}" if unit == "ms" else f"{value:.3f}"


def table(rows: Sequence[Tuple[str, Dict[str, Any]]], columns=TABLE_COLUMNS) -> List[str]:
    lines = ["| 실험 | " + " | ".join(name for name, _ in columns) + " |", "|---" * (len(columns) + 1) + "|"]
    for label, run in rows:
        summary = run["summary"]
        cells = [fmt(summary.get(key), "ms" if key.endswith("_ms") else "") for _, key in columns]
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    return lines


def render(query_type: str, result: Dict[str, Any]) -> str:
    singles = result["single"]
    rows = [("Baseline", result["baseline"])] + [(run["label"], run) for run in singles]
    best = result.get("best")
    lines = [
        f"# {query_type} 검색 실험",
        "",
        f"- 질의 {result['queries']}개 (채점 {result['scored_queries']}개), 기준 지표 `{result['metric']}`, 관련 등급 ≥ {result['min_grade']}",
        f"- Dense `{result['dense_model']}` · Sparse fielded BM25 · Weighted RRF (k={BASELINE.rrf_k}) · Pre-Retrieval LLM `{result['llm']}`",
        f"- 라벨: {result.get('labels', '기존 라벨')}",
        f"- 실행 {result['ran_at']}",
        "",
        "## 실험표",
        "",
    ]
    if best:
        rows.append((f"Best Combination ({best['label']}, dense {best['plan']['dense_weight']})", best))
    lines += table(rows)
    lines += ["", "### 보조 지표", ""] + table(rows, DETAIL_COLUMNS)
    if result.get("channels"):
        channel_rows = [("Dense only (BGE-M3)", result["channels"][0]), ("Sparse only (BM25)", result["channels"][1]),
                        ("Hybrid (Weighted RRF 0.5/0.5)", result["baseline"])]
        lines += ["", "## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)", ""] + table(channel_rows)
    if result.get("combos"):
        lines += ["", "## 조합 실험", "", f"개선된 단일 요소: {', '.join(result['improved']) or '없음'}", ""]
        lines += table([(run["label"], run) for run in result["combos"]])
    if result.get("weights"):
        lines += ["", "## Dense/Sparse 가중치 탐색", "", f"대상: {result['weight_base']} · 방법: {result['weight_method']}", ""]
        lines += table([(f"dense {run['plan']['dense_weight']} / sparse {run['plan']['sparse_weight']}", run) for run in result["weights"]])
    if result.get("baseline_weights"):
        lines += ["", "## Dense/Sparse 가중치 탐색 (Pre-Retrieval 없음)", "", f"대상: Baseline · 방법: {result['weight_method']}", ""]
        lines += table([(f"dense {run['plan']['dense_weight']} / sparse {run['plan']['sparse_weight']}", run) for run in result["baseline_weights"]])
    reference = best or result["baseline"]
    misses = [item for item in reference["per_query"] if item["metrics"] and item["missed@10"]]
    if misses:
        lines += ["", f"## top-10에서 놓친 관련 모델 ({reference['label']})", "", "| 질의 | Recall@10 | 놓친 모델 |", "|---|---:|---|"]
        for item in misses:
            lines.append(f"| {item['query_id']} | {item['metrics']['recall@10']:.2f} | {', '.join(item['missed@10'])} |")
    pool = result.get("unjudged_pool") or {}
    if pool:
        lines += [
            "",
            "## 추가 판정이 필요한 후보",
            "",
            f"이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 {len(pool)}개에 걸쳐 "
            f"{sum(len(ids) for ids in pool.values())}개다. 목록은 JSON의 `unjudged_pool`에 있다.",
        ]
    lines += [
        "",
        "## 해석 주의",
        "",
        "- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.",
        "- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.",
        "- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.",
        "- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.",
    ]
    return "\n".join(lines) + "\n"


def run_type(retriever, queries, query_type, args, log) -> Dict[str, Any]:
    log(f"\n[{query_type}] 질의 {len(queries)}개")
    from retrieval_lab.dense import MODEL_NAME

    result: Dict[str, Any] = {
        "query_type": query_type,
        "queries": len(queries),
        "scored_queries": sum(query.scored for query in queries),
        "metric": args.metric,
        "min_grade": args.min_grade,
        "dense_model": MODEL_NAME,
        "llm": llm_model(),
        "ran_at": time.strftime("%Y-%m-%d %H:%M"),
        "single": [],
        "combos": [],
        "improved": [],
    }
    baseline = replace(BASELINE, query_type=query_type)
    result["baseline"] = try_evaluate(retriever, queries, baseline, args.min_grade, log)
    if args.stage == "baseline":
        return result
    result["channels"] = [
        try_evaluate(retriever, queries, with_dense_weight(baseline, weight), args.min_grade, log, name)
        for weight, name in ((1.0, "Dense only"), (0.0, "Sparse only"))
    ]
    if args.stage == "weight":
        # Dense-weight search without pre-retrieval: no LLM calls.
        result["weight_base"] = result["baseline"]["label"]
        result["weight_method"] = args.weight_search
        result["weights"] = weight_search(retriever, queries, baseline, args.min_grade, args.metric, args.weight_search, args.trials, log)
        result["best"] = weight_choice([result["baseline"]] + result["weights"], args.metric)
        return result

    base_score = result["baseline"]["summary"].get(args.metric) or 0.0

    # 수치 조건을 아는 모델만 남기는 하드 필터. LLM 변환과 달리 질의를 건드리지 않고
    # 후보를 줄이는 쪽이라 Pre-Retrieval 요소와 같은 자리에서 비교한다.
    known_only = replace(baseline, hard_filters=KNOWN_ONLY_FILTERS)
    known_run = try_evaluate(retriever, queries, known_only, args.min_grade, log, "Known values only")
    if known_run:
        known_run["label"] = "Known values only"
        known_run["hard_filter_defaults"] = dict(KNOWN_ONLY_FILTERS)
        result["single"].append(known_run)
        if (known_run["summary"].get(args.metric) or 0.0) > base_score + args.min_delta:
            result["improved_filters"] = dict(KNOWN_ONLY_FILTERS)

    for strategy in ELEMENTS:
        run = try_evaluate(retriever, queries, with_strategies(baseline, (strategy,)), args.min_grade, log)
        if run:
            result["single"].append(run)
            if (run["summary"].get(args.metric) or 0.0) > base_score + args.min_delta:
                result["improved"].append(strategy)
    if args.stage == "single":
        return result

    for size in range(2, len(result["improved"]) + 1):
        for combo in itertools.combinations(result["improved"], size):
            run = try_evaluate(retriever, queries, with_strategies(baseline, combo), args.min_grade, log)
            if run:
                result["combos"].append(run)
    # Only strategies that beat the baseline on the metric may win (plan rule).
    improved_singles = [run for run in result["single"] if any(run["plan"][f"use_{s}"] for s in result["improved"])]
    # 하드 필터로 이긴 실험은 use_* 플래그가 없어 improved_singles에 잡히지 않는다.
    improved_filters = [run for run in result["single"]
                        if run.get("hard_filter_defaults") and result.get("improved_filters")]
    candidates = [result["baseline"]] + improved_singles + improved_filters + result["combos"]
    best = max(candidates, key=lambda run: score_of(run, args.metric))
    result["best"] = best

    if args.weight_search != "none":
        base_plan = with_strategies(baseline, tuple(s for s in ELEMENTS if best["plan"].get(f"use_{s}")))
        # 하드 필터로 이긴 설정은 use_* 플래그가 없어서 with_strategies로는 안 따라온다.
        # 이걸 빼먹으면 weight_base 라벨만 붙고 실제로는 Baseline 가중치를 재게 된다.
        if best.get("hard_filter_defaults"):
            base_plan = replace(base_plan, hard_filters=dict(best["hard_filter_defaults"]))
        result["weight_base"] = best["label"]
        result["weight_method"] = args.weight_search
        result["weights"] = weight_search(retriever, queries, base_plan, args.min_grade, args.metric, args.weight_search, args.trials, log)
        tuned = weight_choice(result["weights"], args.metric)
        if quality_of(tuned, args.metric) > quality_of(best, args.metric):
            result["best"] = tuned
        if best is not result["baseline"]:
            # Re-tuning the weight alone may match the pre-retrieval winner without any LLM call.
            result["baseline_weights"] = weight_search(retriever, queries, baseline, args.min_grade, args.metric, args.weight_search, args.trials, log)
            tuned = weight_choice(result["baseline_weights"], args.metric)
            if quality_of(tuned, args.metric) > quality_of(result["best"], args.metric):
                result["best"] = tuned
    return result


def unjudged_pool(result: Dict[str, Any]) -> Dict[str, List[str]]:
    """Union of unjudged top-10 models over every run, per query (for the 판정실)."""
    runs = [result.get("baseline")] + [run for key in ("channels", "single", "combos", "weights", "baseline_weights") for run in result.get(key) or []]
    pool: Dict[str, set] = {}
    for run in runs:
        for item in (run or {}).get("per_query", []):
            pool.setdefault(item["query_id"], set()).update(item["unjudged@10"])
    return {query_id: sorted(ids) for query_id, ids in sorted(pool.items()) if ids}


def compact(result: Dict[str, Any]) -> Dict[str, Any]:
    """Keep per-query detail only for baseline and best; summaries for the rest."""
    out = dict(result)
    for key in ("channels", "single", "combos", "weights", "baseline_weights"):
        out[key] = [{"label": run["label"], "plan": run["plan"], "summary": run["summary"]} for run in result.get(key) or []]
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--types", default="", help="쉼표로 구분한 plan_query_type (기본: 라벨이 있는 모든 유형)")
    parser.add_argument("--query-files", nargs="*", type=Path, default=list(golden.DEFAULT_QUERY_FILES))
    parser.add_argument("--stage", choices=("baseline", "single", "weight", "all"), default="all",
                        help="weight: Pre-Retrieval 없이 Baseline에서 dense weight만 탐색 (LLM 불필요)")
    parser.add_argument("--metric", default="recall@10", choices=metrics.METRIC_KEYS)
    parser.add_argument("--min-grade", type=int, default=1, choices=(1, 2), help="1: 정답+허용을 관련으로, 2: 정답만")
    parser.add_argument("--min-delta", type=float, default=0.0, help="단일 요소가 '개선'으로 인정되는 최소 차이")
    parser.add_argument("--weight-search", choices=("optuna", "grid", "none"), default="optuna")
    parser.add_argument("--trials", type=int, default=20, help="Optuna 시행 수 (앞의 9회는 0.1~0.9 grid)")
    parser.add_argument("--no-supplement", action="store_true",
                        help="supplemental_judgments.jsonl(추가 판정)을 빼고 기존 라벨만으로 채점")
    parser.add_argument("--supplement", type=Path, default=None,
                        help="추가 판정 파일을 직접 지정한다. 공유 파일 대신 자기 유형의 "
                             "판정만 담은 파일을 쓸 때 사용한다 (--no-supplement가 우선)")
    parser.add_argument("--write-planner", action="store_true", help="유형별 최적 설정을 planner_config.json에 저장")
    args = parser.parse_args()

    retriever = Retriever()
    # Load BGE-M3 before timing so the first query's latency excludes model loading.
    from retrieval_lab.dense import encode

    encode(["warm-up"])
    corpus_ids = set(retriever.ids)
    wanted = [t for t in args.types.split(",") if t] or list(PLAN_QUERY_TYPES)
    unknown = sorted(set(wanted) - set(PLAN_QUERY_TYPES))
    if unknown:
        parser.error(f"알 수 없는 유형: {unknown}")
    supplement_path = None if args.no_supplement else (args.supplement or golden.SUPPLEMENT_PATH)
    all_queries = golden.load(args.query_files, corpus_ids, wanted, supplement_path)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    summary_rows = []
    for query_type in wanted:
        queries = [query for query in all_queries if query.plan_query_type == query_type]
        if not queries:
            print(f"\n[{query_type}] 라벨된 질의 없음, 건너뜀")
            continue
        result = run_type(retriever, queries, query_type, args, print)
        result["labels"] = "기존 라벨" if supplement_path is None else f"기존 라벨 + 추가 판정({supplement_path.name})"
        result["unjudged_pool"] = unjudged_pool(result)
        (REPORT_DIR / f"{query_type}.json").write_text(json.dumps(compact(result), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (REPORT_DIR / f"{query_type}.md").write_text(render(query_type, result), encoding="utf-8")
        best = result.get("best")
        if best:
            summary_rows.append((query_type, result))
            if args.write_planner:
                plan = RetrievalPlan(**{**best["plan"], "query_type": query_type, "hard_filters": {}})
                save_type_plan(query_type, plan, {
                    "metric": args.metric,
                    "value": best["summary"].get(args.metric),
                    "baseline": result["baseline"]["summary"].get(args.metric),
                    "queries": result["queries"],
                    "ran_at": result["ran_at"],
                }, hard_filter_defaults=best.get("hard_filter_defaults"))
    if summary_rows:
        lines = ["| 유형 | 최적 설정 | dense | " + " | ".join(name for name, _ in TABLE_COLUMNS) + " |", "|---" * (len(TABLE_COLUMNS) + 3) + "|"]
        for query_type, result in summary_rows:
            best = result["best"]
            cells = [fmt(best["summary"].get(key), "ms" if key.endswith("_ms") else "") for _, key in TABLE_COLUMNS]
            lines.append(f"| {query_type} | {best['label']} | {best['plan']['dense_weight']} | " + " | ".join(cells) + " |")
        print("\n" + "\n".join(lines))


if __name__ == "__main__":
    main()
