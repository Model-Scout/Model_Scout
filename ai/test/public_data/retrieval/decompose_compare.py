"""Step 3: the service's query decomposition as retrieval input, on a fixed retriever. Development set.

    # calls the service router + planner (gpt-4.1-mini) and embeds each dataset_query: 58 x 3 API requests
    python -X utf8 test/public_data/retrieval/decompose_compare.py --dir runs/<new> --labels <labels> --spec <spec> --allow-api
    # reuse a run's saved plans and vectors: no API call
    python -X utf8 test/public_data/retrieval/decompose_compare.py --dir runs/<new> --labels <labels> --spec <spec> --reuse runs/<old>

Retriever fixed for every input: hybrid, dense / BM25 top 100, RRF k 20, weights 0.5 / 0.5 (fusion_compare), the
pilot's condition filter on the spec's human conditions (so only the search input changes, not the filter).

Inputs (dense text / BM25 text):
  question        the question / the question
  dq              dataset_query / dataset_query
  dq_terms        dataset_query / dataset_query + dataset_terms      (how the service passes them: vector + keywords)
  question_golden the question / the question + the label's dataset_terms
                  (reference: hand-written helper terms, not a ceiling)

The planner gets the target the service router picks; a needs_clarification route is run as "both", the
service's fallback after its question. Retention: whether each stated condition of the spec survives into
dataset_query / dataset_terms (or commercial_only), checked by words, reported apart from the scores.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fusion_compare as fc  # noqa: E402
import pilot  # noqa: E402
import sweep  # noqa: E402

K_RRF = 20
INPUTS = ("question", "dq", "dq_terms", "question_golden")
BASE = "question"
DELIVERY_WORDS = {"api": r"api|오픈\s*api|openapi", "file": r"csv|파일|엑셀|xlsx|다운로드|내려받"}


def load_graph_module():
    spec = importlib.util.spec_from_file_location("recommend_graph", pilot.AI / "17_recommend_graph.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["recommend_graph"] = module
    spec.loader.exec_module(module)
    return module


def plan_for(rg, question, routed=None):
    """routed: a saved route to reuse (no router call), so only the planner differs from that run."""
    routed = routed or rg._route(question)
    target = routed["target"] if routed.get("target") in ("model", "dataset", "both") else "both"
    plan = rg._first_plan(" ".join(question.split()), target)
    return {"route": routed, "target_used": target, "model": rg.LLM_MODEL,
            "dataset_query": plan["dataset_query"], "dataset_terms": plan["dataset_terms"],
            "commercial_only": plan["constraints"]["commercial_only"], "clarifying_questions": plan["clarifying_questions"],
            "data_conditions": plan.get("data_conditions")}


def retention(spec, plan):
    """Each stated condition of the spec: kept in the planner output or not."""
    text = (plan["dataset_query"] + " " + " ".join(plan["dataset_terms"])).lower()
    cond, out = spec["conditions"], {}
    if cond.get("region"):  # 경상남도 and 경남 are one region (hypergraph_search.REGION_CANON)
        names = {cond["region"]} | {full for full, short in pilot.hs.REGION_CANON.items() if short == cond["region"]}
        out["region"] = any(n in text for n in names)
    if spec.get("region_scope"):
        out["region_scope"] = spec["region_scope"] in text
    if cond.get("delivery") in DELIVERY_WORDS:
        out["delivery"] = bool(re.search(DELIVERY_WORDS[cond["delivery"]], text))
    if cond.get("realtime"):
        out["realtime"] = "실시간" in text
    if cond.get("commercial"):
        out["commercial"] = bool(plan["commercial_only"]) or "상업" in text
    if spec.get("kogl_type1_only"):
        out["kogl_type1_only"] = bool(re.search(r"1\s*유형", text))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--allow-api", action="store_true", help="call the service planner and embed dataset_query")
    group.add_argument("--reuse", type=Path, help="a run folder whose plans.jsonl and dq_vectors.jsonl are reused")
    parser.add_argument("--routes", type=Path, help="with --allow-api: reuse this run's routes, call only the planner")
    args = parser.parse_args()
    out = args.dir
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"{out} already holds a run: pick a new --dir")
    identity = pilot.hs.use_corpus("v2")
    labels = pilot.read_jsonl(args.labels)
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    cache, added = pilot.cc.use_saved_vectors(allow_embed=bool(args.allow_api))

    if args.reuse:
        plans = {p["query_id"]: p for p in pilot.read_jsonl(args.reuse / "plans.jsonl")}
        for row in pilot.read_jsonl(args.reuse / "dq_vectors.jsonl"):
            cache[row["key"]] = row["vector"]
    else:
        rg = load_graph_module()
        routes = {p["query_id"]: p["route"] for p in pilot.read_jsonl(args.routes / "plans.jsonl")} if args.routes else {}
        plans = {}
        for lb in labels:
            plans[lb["query_id"]] = {"query_id": lb["query_id"], **plan_for(rg, lb["query"], routes.get(lb["query_id"]))}
            print(lb["query_id"], plans[lb["query_id"]]["target_used"], plans[lb["query_id"]]["dataset_query"][:60], flush=True)

    alias, conditions, searcher = pilot.cc.confirmed_aliases(), pilot.Conditions(), pilot.Searcher()
    merge = fc.rrf(K_RRF)
    scores, rankings, dq_vectors = defaultdict(dict), [], []
    for lb in labels:
        qid, p = lb["query_id"], plans[lb["query_id"]]
        qvec = pilot.hs.embed_query(lb["query"])
        dvec = pilot.hs.embed_query(p["dataset_query"])
        dq_vectors.append({"query_id": qid, "key": pilot.cc.vector_key(pilot.hs.query_model(), p["dataset_query"]), "vector": dvec})
        # the question vector too: questions outside the saved golden vectors (a holdout set) need it to be reused
        dq_vectors.append({"query_id": qid, "kind": "question", "key": pilot.cc.vector_key(pilot.hs.query_model(), lb["query"]), "vector": qvec})
        texts = {"question": (qvec, lb["query"]), "dq": (dvec, p["dataset_query"]),
                 "dq_terms": (dvec, p["dataset_query"] + " " + " ".join(p["dataset_terms"])),
                 "question_golden": (qvec, lb["query"] + " " + " ".join(lb["dataset_terms"]))}
        for name, (vec, text) in texts.items():
            kept, _, statuses = pilot.apply_filter(merge(searcher.dense(vec), searcher.sparse(text)), specs[qid], conditions)
            kept = kept[: pilot.SETTINGS["top_k"]]
            rankings.append({"path": name, "query_id": qid, "top": kept})
            scores[name][qid] = pilot.score_query(kept, lb, alias, statuses)

    blind = pilot.unjudged_items(rankings, labels, specs, alias, conditions)
    kept_by = {qid: retention(specs[qid], plans[qid]) for qid in plans}
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("plans.jsonl", [plans[q] for q in sorted(plans)]), ("dq_vectors.jsonl", dq_vectors),
                       ("rankings.jsonl", rankings), ("unjudged_blind.jsonl", blind)):
        (out / name).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    api = {"planner_and_router": 0 if args.reuse else (1 if args.routes else 2) * len(labels), "embeddings": len(added)}
    (out / "run.json").write_text(json.dumps({
        "identity": identity, "labels": pilot.cc.file_record(args.labels), "spec": pilot.cc.file_record(args.spec),
        "retriever": {"merge": f"rrf{K_RRF}", "weights": [0.5, 0.5], **{k: pilot.SETTINGS[k] for k in ("channel_depth", "top_k")}},
        "inputs": INPUTS, "base": BASE, "reused_from": str(args.reuse).replace("\\", "/") if args.reuse else None,
        "routes_from": str(args.routes).replace("\\", "/") if args.routes else None,
        "planner_model": next(iter(plans.values()))["model"], "api_calls": api, "development_set": True,
        "bootstrap": {"n": sweep.BOOT, "seed": sweep.SEED},
        "code": {**pilot.code_record(), "decompose_compare_lf_sha256": pilot.content_digest(Path(__file__))[0]},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    by_q = {lb["query_id"]: lb for lb in labels}
    rec = [q for q in by_q if by_q[q]["expected_behavior"] == "recommend"]
    two = [q for q in rec if "raw2" in scores[BASE][q]]
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")  # noqa: E731
    measures = (("2점 MRR@5", two, "raw2", "mrr@5"), ("nDCG@5(등급)", rec, "raw", "ndcg@5"),
                ("2점 R@10", two, "raw2", "recall@10"), ("P@10(1점 이상)", rec, "raw", "precision@10"))
    ci = lambda t: f"{t[0]:+.3f} [{t[1]:+.3f}, {t[2]:+.3f}]"  # noqa: E731
    L = ["# 질의 분해 입력 비교 (3단계, 개발용)", "",
         f"라벨 `{args.labels.stem}`, 명세 `{args.spec.stem}`. 분해 모델 `{run_model(plans)}`. API 호출: 라우터·분해 {api['planner_and_router']}회, 임베딩 {api['embeddings']}회. "
         f"검색기 고정: hybrid, RRF k {K_RRF}, 0.5/0.5, 조건 필터는 명세(사람이 정한 조건).", "",
         "**개발용 결과다.** 같은 58문항으로 검색기를 골랐으므로 운영 반영 전에 별도 질문으로 확인해야 한다. "
         "`question_golden`은 수작업 보조 검색어를 넣은 참고 결과이며 상한선이 아니다.", "",
         "| 입력 | " + " | ".join(m for m, *_ in measures) + " | judged@10 | 미판정@10 합 |", "|---|" + "---:|" * (len(measures) + 2)]
    for name in INPUTS:
        L.append(f"| {name} | " + " | ".join(f"{mean([scores[name][q][k][m] for q in qs]):.3f}" for _, qs, k, m in measures)
                 + f" | {mean([scores[name][q]['judged@10'] for q in rec]):.3f} | {sum(scores[name][q]['unjudged@10'] for q in rec)} |")
    L += ["", f"## `{BASE}` 대비 차이 (평균 [95% 부트스트랩 구간])", "", "| 입력 | " + " | ".join(m for m, *_ in measures) + " |", "|---|" + "---|" * len(measures)]
    for name in INPUTS[1:]:
        L.append(f"| {name} | " + " | ".join(ci(sweep.interval([scores[name][q][k][m] - scores[BASE][q][k][m] for q in qs])) for _, qs, k, m in measures) + " |")
    L += ["", "## 유형별 2점 MRR@5", "", "| 유형 | 문항 | " + " | ".join(INPUTS) + " |", "|---|---:|" + "---:|" * len(INPUTS)]
    types = defaultdict(list)
    for q in two:
        types[specs[q]["type"]].append(q)
    for t, qs in sorted(types.items()):
        L.append(f"| {t} | {len(qs)} | " + " | ".join(f"{mean([scores[n][q]['raw2']['mrr@5'] for q in qs]):.2f}" for n in INPUTS) + " |")
    kept_total = Counter()
    for qid, kept in kept_by.items():
        for c, ok in kept.items():
            kept_total[(c, ok)] += 1
    conds = sorted({c for c, _ in kept_total})
    L += ["", "## 조건 유지 (명세의 명시 조건이 dataset_query·dataset_terms·commercial_only에 남았는지, 단어 기준)", "",
          "| 조건 | 유지 | 빠짐 |", "|---|---:|---:|"]
    L += [f"| {c} | {kept_total[(c, True)]} | {kept_total[(c, False)]} |" for c in conds]
    L += ["", "빠진 문항:", ""] + [f"- {q} {[c for c, ok in kept.items() if not ok]}: `{plans[q]['dataset_query']}` / {plans[q]['dataset_terms']}"
                                    for q, kept in sorted(kept_by.items()) if not all(kept.values())]
    routes = Counter(p["route"].get("target") for p in plans.values())
    L += ["", f"## 라우터 결과: {dict(routes)} (needs_clarification 등은 서비스처럼 both로 실행)", ""]
    if all("expected_route" in specs[q] for q in plans):  # a spec that states the expected route per question
        agree = Counter((specs[q]["expected_route"], plans[q]["route"].get("target")) for q in plans)
        L += ["| 기대 경로 → 라우터 | 문항 |", "|---|---:|"] + [f"| {e} → {g} | {n} |" for (e, g), n in sorted(agree.items())]
        L += ["", "기대와 다른 문항: " + (", ".join(f"{q}({specs[q]['expected_route']}→{plans[q]['route'].get('target')})"
                                              for q in sorted(plans) if specs[q]["expected_route"] != plans[q]["route"].get("target")) or "없음"), ""]
    L += [
          "## 분해 결과 (문항별)", "", "| 문항 | 라우터 | dataset_query | dataset_terms |", "|---|---|---|---|"]
    L += [f"| {q} | {plans[q]['route'].get('target')} | {plans[q]['dataset_query']} | {', '.join(plans[q]['dataset_terms'])} |" for q in sorted(plans)]
    L += ["", f"## 미판정 후보: {len(blind)}쌍 (`unjudged_blind.jsonl`). 판정 전까지 raw 점수에서 적중이 아니다.", ""]
    (out / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out}: unjudged {len(blind)}, api {api}")


def run_model(plans):
    return ", ".join(sorted({p["model"] for p in plans.values()}))


if __name__ == "__main__":
    main()
