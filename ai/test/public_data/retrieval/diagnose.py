"""Where do the answers sit? For the fixed hybrid (w 0.5), each relevant dataset of each recommend question is put
in one stage, so a low score can be traced to candidates, fusion/filter or top ordering. No API call.

    python -X utf8 test/public_data/retrieval/diagnose.py --dir test/public_data/retrieval/runs/<name> \
        --labels <labels> --spec <spec>

Stages (copies collapse to one dataset, as in scoring):
  no_candidate   in neither channel's top 100 (dense, BM25): the query wording or candidate depth
  filtered       a channel found it, the condition filter removed it (confirmed unmet)
  below_10       a channel found it, it survived, but the fused ranking put it below 10: fusion
  rank_6_10      in the top 10 but not the top 5: top ordering
  top_5
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pilot  # noqa: E402
import sweep  # noqa: E402

STAGES = ("no_candidate", "filtered", "below_10", "rank_6_10", "top_5")


def stage_of(d, dense, sparse, removed, final, canon):
    if d in final[:5]:
        return "top_5"
    if d in final[:10]:
        return "rank_6_10"
    if d not in {canon(x) for x in dense} | {canon(x) for x in sparse}:
        return "no_candidate"
    if d in {canon(x) for x in removed}:
        return "filtered"
    return "below_10"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    args = parser.parse_args()
    if args.dir.exists() and any(args.dir.iterdir()):
        raise SystemExit(f"{args.dir} already holds a run: pick a new --dir")
    identity = pilot.hs.use_corpus("v2")
    labels = pilot.read_jsonl(args.labels)
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    pilot.cc.use_saved_vectors(allow_embed=False)
    alias, conditions, searcher = pilot.cc.confirmed_aliases(), pilot.Conditions(), pilot.Searcher()
    canon = lambda d: min(alias.get(d, {d}))  # noqa: E731

    rows = []
    for lb in labels:
        if lb["expected_behavior"] != "recommend":
            continue
        qid = lb["query_id"]
        vector = pilot.hs.embed_query(lb["query"])
        dense, sparse = searcher.dense(vector), searcher.sparse(lb["query"])
        kept, removed, _ = pilot.apply_filter(sweep.fuse(dense, sparse, sweep.BASE), specs[qid], conditions)
        final = list(dict.fromkeys(canon(d) for d in kept[: pilot.SETTINGS["top_k"]]))
        dr = {canon(d): i + 1 for i, d in reversed(list(enumerate(dense)))}
        sr = {canon(d): i + 1 for i, d in reversed(list(enumerate(sparse)))}
        grades = {}
        for d, g in lb["relevant"].items():
            grades[canon(d)] = max(g, grades.get(canon(d), 0))
        for d, g in sorted(grades.items()):
            rows.append({"query_id": qid, "type": specs[qid]["type"], "dataset_id": d, "grade": g,
                         "stage": stage_of(d, dense, sparse, removed, final, canon),
                         "final_rank": final.index(d) + 1 if d in final else None,
                         "dense_rank": dr.get(d), "bm25_rank": sr.get(d)})

    args.dir.mkdir(parents=True, exist_ok=True)
    (args.dir / "answers.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    (args.dir / "run.json").write_text(json.dumps({
        "identity": identity, "labels": pilot.cc.file_record(args.labels), "spec": pilot.cc.file_record(args.spec),
        "retriever": {"path": "hybrid", "dense_weight": sweep.BASE, **{k: pilot.SETTINGS[k] for k in ("rrf_k", "channel_depth", "top_k")}},
        "api_calls": 0, "code": {**pilot.code_record(), "diagnose_lf_sha256": pilot.content_digest(Path(__file__))[0]},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    L = ["# 정답 위치 진단 (hybrid w 0.5)", "", f"라벨 `{args.labels.stem}`, 명세 `{args.spec.stem}`. 외부 API 호출 0. "
         "추천 문항의 관련 데이터마다 어느 단계에 있는지 셌다(사본은 하나로).", "",
         "| 단계 | 뜻 |", "|---|---|",
         "| no_candidate | dense·BM25 어느 채널 상위 100에도 없음 → 질문 표현·후보 깊이 문제 |",
         "| filtered | 채널에는 있었지만 조건 필터가 불충족으로 제거 |",
         "| below_10 | 후보에 있고 필터도 통과했지만 결합 순위가 10위 밖 → 결합 문제 |",
         "| rank_6_10 | 상위 10 안이지만 5위 밖 → 최상위 순서 문제 |", "| top_5 | 상위 5 안 |", ""]
    for title, keep in (("2점 정답", lambda r: r["grade"] == 2), ("1점 대안", lambda r: r["grade"] == 1)):
        sel = [r for r in rows if keep(r)]
        c = Counter(r["stage"] for r in sel)
        L += [f"## {title} ({len(sel)}개, 문항 {len({r['query_id'] for r in sel})}개)", "",
              "| " + " | ".join(STAGES) + " |", "|" + "---:|" * len(STAGES),
              "| " + " | ".join(f"{c[s]} ({c[s] / len(sel):.0%})" for s in STAGES) + " |", ""]
        by_t = defaultdict(Counter)
        for r in sel:
            by_t[r["type"]][r["stage"]] += 1
        L += ["| 유형 | " + " | ".join(STAGES) + " |", "|---|" + "---:|" * len(STAGES)]
        L += [f"| {t} | " + " | ".join(str(by_t[t][s]) for s in STAGES) + " |" for t in sorted(by_t)] + [""]
    two = [r for r in rows if r["grade"] == 2]
    per_q = defaultdict(Counter)
    for r in two:
        per_q[r["query_id"]][r["stage"]] += 1
    L += ["## 2점 정답이 상위 10에 하나도 없는 문항", ""]
    miss = [q for q, c in sorted(per_q.items()) if not (c["top_5"] + c["rank_6_10"])]
    L += [f"- {q}: " + ", ".join(f"{s} {per_q[q][s]}" for s in STAGES if per_q[q][s]) for q in miss] or ["- 없음"]
    L += ["", "## 2점 정답의 채널 순위 (상위 10 밖에 있는 것)", "",
          "| 문항 | 데이터 | 단계 | dense 순위 | BM25 순위 | 최종 순위 |", "|---|---|---|---:|---:|---:|"]
    for r in two:
        if r["stage"] not in ("top_5", "rank_6_10"):
            L.append(f"| {r['query_id']} | {r['dataset_id']} | {r['stage']} | {r['dense_rank'] or '–'} | {r['bm25_rank'] or '–'} | {r['final_rank'] or '–'} |")
    (args.dir / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{args.dir}: {len(rows)} relevant datasets, stages {dict(Counter(r['stage'] for r in rows))}")


if __name__ == "__main__":
    main()
