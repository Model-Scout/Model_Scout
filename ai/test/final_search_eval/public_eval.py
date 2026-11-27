#!/usr/bin/env python3
"""공공데이터 골든셋(코퍼스 v2, 라벨 v9)으로 공공데이터 검색의 최종 성능을 잰다. B 가 운영 그대로의 값이다.

    A   검색 순서: 운영 _rank_lists 의 공공데이터(service) 목록, DATASET_RERANK=off 와 같은 순서(비교군)
    B   운영 리랭커(dataset_rerank.rerank)를 켠 것. 지금 서버의 기본 동작이다

운영 search_project_datasets 를 그대로 부르고 dataset_rerank.rerank 를 가로채 재순위 직전 20개를 받는다.
A 는 그 목록, B 는 그 목록에 실제 rerank 를 부른 결과다(--runs 번 평균). 질문마다 라우팅·planner 도 운영과
같이 한 번씩 돈다. 라벨 v9 의 recommend 질문(53개)만 채점하고, 판정되지 않은 데이터는 0점이다. 사본(v2
그래프의 duplicates)은 같은 데이터로 친다.

    # ai/ 에서. MODEL_SCOUT_CORPUS=v2 MODEL_SCOUT_DATA_VERSION=aa1a71d35a121150 필수
    python -X utf8 test/final_search_eval/public_eval.py run --dir test/final_search_eval/runs/<폴더> --runs 2
    python -X utf8 test/final_search_eval/public_eval.py score --dir test/final_search_eval/runs/<폴더>
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
AI = HERE.parents[1]
LABELS = AI / "test" / "public_data" / "corpus_v2" / "golden_prep" / "batch8" / "labels_llm_v9.jsonl"
ENTITIES = AI / "data" / "hypergraph_v2" / "entities.jsonl"
PINNED = "aa1a71d35a121150"

os.environ.update(RECOMMEND_LLM_PROVIDER="openai", RECOMMEND_LLM_MODEL="gpt-4.1-mini", MODEL_SPARSE_IDF_ENABLED="1")
sys.path[:0] = [str(AI), str(HERE)]

import metrics  # noqa: E402
from model_eval import load_graph  # noqa: E402


def questions() -> list[dict]:
    return [q for q in map(json.loads, LABELS.open(encoding="utf-8")) if q["expected_behavior"] == "recommend"]


def run(out_dir: Path, runs: int) -> int:
    if os.environ.get("MODEL_SCOUT_CORPUS") != "v2" or os.environ.get("MODEL_SCOUT_DATA_VERSION") != PINNED:
        raise SystemExit(f"MODEL_SCOUT_CORPUS=v2 MODEL_SCOUT_DATA_VERSION={PINNED} 로 실행하세요(서버와 같은 코퍼스)")
    rg = load_graph()
    from dotenv import load_dotenv
    load_dotenv(AI / ".env")
    real_rerank = rg.dataset_rerank.rerank
    captured: list[tuple] = []

    def capture(question, rows, client_factory, model, facts):
        captured.append((list(rows), model, facts))
        return list(rows)

    rg.dataset_rerank.rerank = capture
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "public_lists.jsonl"
    done = {json.loads(line)["qid"] for line in path.open(encoding="utf-8")} if path.exists() else set()
    with path.open("a", encoding="utf-8") as sink:
        for label in questions():
            if label["query_id"] in done:
                continue
            text = label["query"]
            started = time.perf_counter()
            captured.clear()
            route = rg._route(text)
            target = route["target"] if route["target"] in ("dataset", "both") else "dataset"
            plan = rg._first_plan(text, target)
            out = rg.search_project_datasets({"request": text, "plan": plan, "route": route})
            shown = [r["dataset"] for r in out["project_datasets"].get("service_data") or []]
            record = {"qid": label["query_id"], "text": text, "route": route.get("target"),
                      "data_kind": route.get("data_kind"), "recommend": plan.get("recommend"),
                      "path": out["dataset_route"]["path"], "A": shown, "B": [], "rerank_s": []}
            if captured:
                rows, model, facts = captured[0]
                record["A"] = [r["dataset"] for r in rows]
                for _ in range(runs):
                    t = time.perf_counter()
                    order = real_rerank(text, rows, rg._openai, model, facts)
                    record["rerank_s"].append(round(time.perf_counter() - t, 2))
                    record["B"].append([r["dataset"] for r in order])
            else:  # 재순위가 일어나지 않은 경로(이름 조회 등): 두 방식이 같다
                record["B"] = [shown] * runs
            record["seconds"] = round(time.perf_counter() - started, 1)
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            sink.flush()
            print(f"{record['qid']} route={record['route']}/{record['data_kind']} path={record['path']} "
                  f"rows={len(record['A'])} reranked={bool(captured)} {record['seconds']}s", flush=True)
    meta = {"labels": str(LABELS.relative_to(AI)), "corpus": PINNED, "rerank_model": rg.dataset_rerank.MEASURED_MODEL,
            "depth": rg.dataset_rerank.RERANK_DEPTH, "shown": rg.PROJECT_DATASETS, "runs": runs}
    (out_dir / "public_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


def aliases() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for entity in map(json.loads, ENTITIES.open(encoding="utf-8")):
        if entity["kind"] == "dataset":
            names = {entity["name"], *(entity.get("duplicates") or [])}
            for name in names:
                out[name] = names
    return out


def canonical(ranked: list[str], alias: dict[str, set[str]]) -> list[str]:
    """사본은 첫 순위에 한 번만 남긴다."""
    seen, out = set(), []
    for item in ranked:
        key = min(alias.get(item, {item}))
        if key not in seen:
            seen.add(key)
            out.append(key)
    return out


def score(out_dir: Path) -> int:
    alias = aliases()
    labels = {q["query_id"]: q for q in questions()}
    records = [json.loads(line) for line in (out_dir / "public_lists.jsonl").open(encoding="utf-8")]
    result: dict = {"paired": {}, "by_question": {}}
    for min_grade in (2, 1):
        a_scores, b_scores = [], []
        for record in records:
            grades: dict[str, int] = {}
            for dataset, grade in labels[record["qid"]]["relevant"].items():
                key = min(alias.get(dataset, {dataset}))
                grades[key] = max(grade, grades.get(key, 0))
            if not any(g >= min_grade for g in grades.values()):
                continue  # 이 기준의 정답이 없는 질문은 뺀다
            a = metrics.score(canonical(record["A"], alias), grades, min_grade)
            runs = [metrics.score(canonical(order, alias), grades, min_grade) for order in record["B"]]
            b = {k: metrics.mean([r[k] for r in runs]) for k in runs[0]}
            a_scores.append(a)
            b_scores.append(b)
            result["by_question"].setdefault(str(min_grade), {})[record["qid"]] = {"A": a, "B": b}
        for k in a_scores[0]:
            result["paired"][f"g{min_grade}:B:{k}"] = metrics.paired([s[k] for s in a_scores], [s[k] for s in b_scores])
    (out_dir / "public_scores.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n",
                                                encoding="utf-8")
    for min_grade in (2, 1):
        n = result["paired"][f"g{min_grade}:B:ndcg@5"]["n"]
        print(f"\n## min_grade {min_grade} (질문 {n}개)     A      B   (Δ, 95% CI)")
        for k in ("ndcg@3", "ndcg@5", "ndcg@10", "mrr@10", "r@5", "r@10", "p@3", "p@5", "hit@3"):
            p = result["paired"][f"g{min_grade}:B:{k}"]
            print(f"{k:8s}  {p['a']:.3f}  {p['b']:.3f}  ({p['delta']:+.3f} [{p['lo']:+.3f},{p['hi']:+.3f}] "
                  f"↑{p['up']}↓{p['down']})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("run", "score"))
    ap.add_argument("--dir", type=Path, required=True)
    ap.add_argument("--runs", type=int, default=2)
    args = ap.parse_args()
    return run(args.dir, args.runs) if args.step == "run" else score(args.dir)


if __name__ == "__main__":
    raise SystemExit(main())
