"""Step 2b: how the two channel lists are merged. Development set: the settings are chosen on the same 58 questions,
so a winner here still needs other questions before it goes near the service. No API call.

    python -X utf8 test/public_data/retrieval/fusion_compare.py --dir test/public_data/retrieval/runs/<name> \
        --labels <labels> --spec <spec>

Fixed: corpus, questions, both channel lists (dense / BM25 top 100, pilot SETTINGS), weights 0.5 / 0.5, the
condition filter, scoring. Only the merge changes (METHODS). rrf60 is pilot 1's hybrid and must reproduce it.

Reported against rrf60 with paired bootstrap intervals: 2-point MRR@5 and graded nDCG@5 first, then 2-point R@10
and P@10 (1+) as guards. Pairs a method lifts into its top 10 are listed by what they are: a relevant dataset only
one channel found (the case this targets), a judged non-answer, or unjudged. Unjudged pairs are never counted as
wrong silently: they go to unjudged_blind.jsonl for the next label round, and the raw scores here treat them as
misses only until then (judged@10 is reported next to every score).
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

PROTECT = 3  # protect: each channel's top PROTECT go first (alternating), then RRF k 60 for the rest


def rrf(k):
    def merge(dense, sparse):
        lists = pilot.fusion.channel_lists([dense], [sparse], 0.5, 0.5)
        return [d for d, _ in pilot.fusion.weighted_rrf(lists, k=k)]
    return merge


def interleave(dense, sparse):
    """dense 1, BM25 1, dense 2, BM25 2, ... skipping what is already in."""
    out = []
    for pair in zip(dense, sparse):
        out += [d for d in pair if d not in out]
    longer = dense if len(dense) > len(sparse) else sparse
    return list(dict.fromkeys(out + list(longer)))


def protect(dense, sparse, m=PROTECT):
    head = interleave(dense[:m], sparse[:m])
    return head + [d for d in rrf(60)(dense, sparse) if d not in head]


METHODS = {"rrf60": rrf(60), "rrf20": rrf(20), "rrf5": rrf(5), "interleave": interleave, f"protect{PROTECT}+rrf60": protect}
BASE = "rrf60"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    args = parser.parse_args()
    out = args.dir
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"{out} already holds a run: pick a new --dir")
    identity = pilot.hs.use_corpus("v2")
    labels = pilot.read_jsonl(args.labels)
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    pilot.cc.use_saved_vectors(allow_embed=False)
    alias, conditions, searcher = pilot.cc.confirmed_aliases(), pilot.Conditions(), pilot.Searcher()
    canon = lambda d: min(alias.get(d, {d}))  # noqa: E731
    saved = {r["query_id"]: r["top"] for r in pilot.read_jsonl(sweep.PILOT1 / "rankings.jsonl") if r["path"] == "hybrid"}

    scores, rankings, channels, reproduced = defaultdict(dict), [], {}, 0
    for lb in labels:
        qid = lb["query_id"]
        vector = pilot.hs.embed_query(lb["query"])
        dense, sparse = searcher.dense(vector), searcher.sparse(lb["query"])
        channels[qid] = ({canon(d) for d in dense}, {canon(d) for d in sparse})
        for name, merge in METHODS.items():
            kept, _, statuses = pilot.apply_filter(merge(dense, sparse), specs[qid], conditions)
            kept = kept[: pilot.SETTINGS["top_k"]]
            reproduced += name == BASE and kept == saved[qid]
            rankings.append({"path": name, "query_id": qid, "top": kept})
            scores[name][qid] = pilot.score_query(kept, lb, alias, statuses)
    if reproduced != len(labels):
        raise SystemExit(f"{BASE} reproduced pilot 1 hybrid for {reproduced}/{len(labels)} questions only")

    by_q = {lb["query_id"]: lb for lb in labels}
    rec = [q for q in by_q if by_q[q]["expected_behavior"] == "recommend"]
    two = [q for q in rec if "raw2" in scores[BASE][q]]
    mean = lambda xs: sum(xs) / len(xs)  # noqa: E731
    measures = (("2점 MRR@5", two, "raw2", "mrr@5"), ("nDCG@5(등급)", rec, "raw", "ndcg@5"),
                ("2점 R@10", two, "raw2", "recall@10"), ("P@10(1점 이상)", rec, "raw", "precision@10"))

    # What each method lifts into its top 10 compared with rrf60.
    top10 = {(r["path"], r["query_id"]): list(dict.fromkeys(canon(d) for d in r["top"]))[:pilot.K] for r in rankings}
    lifted = defaultdict(list)
    for name in METHODS:
        if name == BASE:
            continue
        for q in rec:
            lb = by_q[q]
            grades = {}
            for d, g in lb["relevant"].items():
                grades[canon(d)] = max(g, grades.get(canon(d), 0))
            wrong = {canon(d) for d in lb["must_exclude"] + lb["judged_irrelevant"]}
            held = {canon(d) for d in lb["unjudged"]}
            for d in top10[(name, q)]:
                if d in top10[(BASE, q)]:
                    continue
                dn, sp = (d in channels[q][0]), (d in channels[q][1])
                kind = (f"{grades[d]}점" + ("(한 채널만)" if dn != sp else "")) if d in grades else \
                       "오답(판정됨)" if d in wrong else "보류" if d in held else "미판정"
                lifted[name].append({"query_id": q, "dataset_id": d, "kind": kind, "rank": top10[(name, q)].index(d) + 1,
                                     "channel": "dense" if dn and not sp else "bm25" if sp and not dn else "both"})

    blind = pilot.unjudged_items(rankings, labels, specs, alias, conditions)
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in (("rankings.jsonl", rankings), ("unjudged_blind.jsonl", blind),
                       ("lifted.jsonl", [{"method": m, **x} for m, xs in lifted.items() for x in xs])):
        (out / name).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "run.json").write_text(json.dumps({
        "identity": identity, "labels": pilot.cc.file_record(args.labels), "spec": pilot.cc.file_record(args.spec),
        "methods": list(METHODS), "base": BASE, "protect": PROTECT, "weights": [0.5, 0.5], "settings": pilot.SETTINGS,
        "bootstrap": {"n": sweep.BOOT, "seed": sweep.SEED}, "api_calls": 0, "development_set": True,
        "pilot1_hybrid_reproduced": f"{reproduced}/{len(labels)}",
        "code": {**pilot.code_record(), "fusion_compare_lf_sha256": pilot.content_digest(Path(__file__))[0]},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    ci = lambda t: f"{t[0]:+.3f} [{t[1]:+.3f}, {t[2]:+.3f}]"  # noqa: E731
    L = ["# 채널 결합 방식 비교 (개발용)", "",
         f"라벨 `{args.labels.stem}`, 명세 `{args.spec.stem}`. 외부 API 호출 0. 채널 후보(dense·BM25 상위 100), 가중치 0.5/0.5, "
         f"조건 필터, 채점은 고정하고 결합 방식만 바꿨다. `{BASE}`가 파일럿 1 hybrid를 {reproduced}/{len(labels)} 재현.", "",
         "**개발용 결과다.** 같은 58문항으로 설정을 고르므로, 운영에 반영하기 전에 별도 질문으로 확인해야 한다.", "",
         f"- `rrf20`, `rrf5`: RRF k를 줄인 것(각 채널 상위를 더 강하게 우대). `interleave`: 두 채널 순위를 번갈아 합침. "
         f"`protect{PROTECT}+rrf60`: 각 채널 상위 {PROTECT}개를 먼저 두고 나머지는 RRF k 60.", "",
         "| 방식 | " + " | ".join(m for m, *_ in measures) + " | judged@10 | 미판정@10 합 |", "|---|" + "---:|" * (len(measures) + 2)]
    for name in METHODS:
        L.append(f"| {name} | " + " | ".join(f"{mean([scores[name][q][k][m] for q in qs]):.3f}" for _, qs, k, m in measures)
                 + f" | {mean([scores[name][q]['judged@10'] for q in rec]):.3f} | {sum(scores[name][q]['unjudged@10'] for q in rec)} |")
    L += ["", f"## {BASE} 대비 차이 (평균 [95% 부트스트랩 구간], 문항 재표집 {sweep.BOOT}회)", "",
          "| 방식 | " + " | ".join(m for m, *_ in measures) + " |", "|---|" + "---|" * len(measures)]
    for name in METHODS:
        if name == BASE:
            continue
        L.append(f"| {name} | " + " | ".join(
            ci(sweep.interval([scores[name][q][k][m] - scores[BASE][q][k][m] for q in qs])) for _, qs, k, m in measures) + " |")
    L += ["", f"## {BASE}의 상위 10에 없던 데이터가 새로 들어온 것", "", "| 방식 | " + " | ".join(
        ("2점(한 채널만)", "2점", "1점(한 채널만)", "1점", "오답(판정됨)", "보류", "미판정")) + " |", "|---|" + "---:|" * 7]
    for name, xs in lifted.items():
        c = Counter(x["kind"] for x in xs)
        L.append(f"| {name} | " + " | ".join(str(c[k]) for k in ("2점(한 채널만)", "2점", "1점(한 채널만)", "1점", "오답(판정됨)", "보류", "미판정")) + " |")
    for name, xs in lifted.items():
        good = [x for x in xs if x["kind"].startswith("2점")][:8]
        bad = [x for x in xs if x["kind"] == "오답(판정됨)"][:8]
        L += ["", f"### {name}: 살린 2점 정답 예 / 올라온 오답 예", ""]
        L += [f"- 살림 {x['query_id']} `{x['dataset_id']}` {x['rank']}위 ({x['channel']})" for x in good] or ["- 살린 2점 정답 없음"]
        L += [f"- 오답 {x['query_id']} `{x['dataset_id']}` {x['rank']}위 ({x['channel']})" for x in bad] or ["- 올라온 오답 없음"]
    L += ["", f"## 미판정 후보: {len(blind)}쌍 (`unjudged_blind.jsonl`, 방식·순위 가림). 판정 전까지 위 raw 점수에서 적중이 아니다.", ""]
    (out / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out}: {len(METHODS)} methods, reproduced {reproduced}/{len(labels)}, unjudged {len(blind)}")


if __name__ == "__main__":
    main()
