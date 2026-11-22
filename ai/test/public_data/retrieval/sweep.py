"""Step 2: dense/BM25 weight sweep for the hybrid path, on the frozen v2 and one label set. No API call.

    python -X utf8 test/public_data/retrieval/sweep.py --dir test/public_data/retrieval/runs/<name> \
        --labels test/public_data/corpus_v2/golden_prep/batch6/labels_llm_v7.jsonl --spec test/public_data/retrieval/query_spec_v2.jsonl

Each question's dense and BM25 channel lists (depth 100, pilot SETTINGS) are computed once from the saved question
vectors; every dense weight w in WEIGHTS fuses them with weighted RRF (k 60, BM25 weight 1 - w), then the pilot's
condition filter and scoring apply unchanged. w = 0.5 must reproduce pilot 1's hybrid rankings exactly.

Differences against w = 0.5 come with a paired bootstrap interval over questions (seeded): with 43-53 questions a
small mean gain is noise, so a weight is only called better when its interval stays above 0. Per-type best weights
are printed for reading, not for choosing: most types have too few questions.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pilot  # noqa: E402

WEIGHTS = [round(i / 10, 1) for i in range(11)]
BASE = 0.5
PILOT1 = HERE / "runs" / "2026-11-16_pilot1"
BOOT, SEED = 2000, 20261120


def fuse(dense, sparse, w):
    lists = pilot.fusion.channel_lists([dense], [sparse], w, 1 - w)
    return [d for d, _ in pilot.fusion.weighted_rrf(lists, k=pilot.SETTINGS["rrf_k"])]


def interval(diffs, seed=SEED, n=BOOT):
    """Mean of paired differences and its 95% bootstrap interval."""
    if not diffs:  # no question to compare (e.g. a pooling run before labels exist)
        return float("nan"), float("nan"), float("nan")
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(diffs) for _ in diffs) / len(diffs) for _ in range(n))
    return sum(diffs) / len(diffs), means[int(0.025 * n)], means[int(0.975 * n) - 1]


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
    pin = json.loads(pilot.PIN.read_text(encoding="utf-8"))["data_version"]
    if not identity["documents_id"].startswith(pin):
        raise SystemExit(f"checked-out v2 is not the pin {pin}")
    labels = pilot.read_jsonl(args.labels)
    specs = {s["query_id"]: s for s in pilot.read_jsonl(args.spec)}
    pilot.cc.use_saved_vectors(allow_embed=False)
    alias, conditions, searcher = pilot.cc.confirmed_aliases(), pilot.Conditions(), pilot.Searcher()
    saved = {r["query_id"]: r["top"] for r in pilot.read_jsonl(PILOT1 / "rankings.jsonl") if r["path"] == "hybrid"}

    scores, reproduced = defaultdict(dict), 0
    for label in labels:
        qid, spec = label["query_id"], specs[label["query_id"]]
        vector = pilot.hs.embed_query(label["query"])
        dense, sparse = searcher.dense(vector), searcher.sparse(label["query"])
        for w in WEIGHTS:
            kept, _, statuses = pilot.apply_filter(fuse(dense, sparse, w), spec, conditions)
            kept = kept[: pilot.SETTINGS["top_k"]]
            if w == BASE:
                reproduced += kept == saved[qid]
            scores[str(w)][qid] = pilot.score_query(kept, label, alias, statuses)
    if reproduced != len(labels):
        raise SystemExit(f"w={BASE} reproduced pilot 1 hybrid for {reproduced}/{len(labels)} questions only")

    rec = [lb["query_id"] for lb in labels if lb["expected_behavior"] == "recommend"]
    two = [q for q in rec if "raw2" in scores[str(BASE)][q]]
    metric = lambda w, q, key, m: scores[str(w)][q][key][m]  # noqa: E731
    mean = lambda xs: sum(xs) / len(xs)  # noqa: E731
    rows = {}
    for w in WEIGHTS:
        d2 = [metric(w, q, "raw2", "recall@10") - metric(BASE, q, "raw2", "recall@10") for q in two]
        d1 = [metric(w, q, "raw", "recall@10") - metric(BASE, q, "raw", "recall@10") for q in rec]
        rows[w] = {"r10_2": mean([metric(w, q, "raw2", "recall@10") for q in two]),
                   "r10_1": mean([metric(w, q, "raw", "recall@10") for q in rec]),
                   "ndcg5": mean([metric(w, q, "raw", "ndcg@5") for q in rec]),
                   "mrr5_2": mean([metric(w, q, "raw2", "mrr@5") for q in two]),
                   "judged10": mean([scores[str(w)][q]["judged@10"] for q in rec]),
                   "d2": interval(d2), "d1": interval(d1),
                   "wins2": sum(x > 1e-9 for x in d2), "losses2": sum(x < -1e-9 for x in d2)}
    types = defaultdict(list)
    for q in rec:
        types[specs[q]["type"]].append(q)

    out.mkdir(parents=True, exist_ok=True)
    (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    record = {"identity": identity, "data_version": pin, "labels": pilot.cc.file_record(args.labels),
              "spec": pilot.cc.file_record(args.spec), "weights": WEIGHTS, "base": BASE, "bootstrap": {"n": BOOT, "seed": SEED},
              "settings": pilot.SETTINGS, "api_calls": 0, "pilot1_hybrid_reproduced": f"{reproduced}/{len(labels)}",
              "code": {**pilot.code_record(), "sweep_lf_sha256": pilot.content_digest(Path(__file__))[0]}}
    (out / "run.json").write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    f = lambda x: f"{x:.3f}"  # noqa: E731
    ci = lambda t: f"{t[0]:+.3f} [{t[1]:+.3f}, {t[2]:+.3f}]"  # noqa: E731
    L = ["# Hybrid 가중치 비교 (2단계)", "",
         f"코퍼스 v2 `{pin}`, 라벨 `{args.labels.stem}`, 명세 `{args.spec.stem}`. 외부 API 호출 0. "
         f"w = dense 가중치(BM25는 1 − w), RRF k {pilot.SETTINGS['rrf_k']}, 채널 깊이 {pilot.SETTINGS['channel_depth']}. "
         f"w = {BASE}가 파일럿 1 hybrid 순위를 {reproduced}/{len(labels)} 재현.", "",
         f"차이는 w = {BASE} 대비 문항별 차이의 평균과 95% 부트스트랩 구간(문항 재표집 {BOOT}회)이다. "
         "구간이 0을 넘지 않으면 잡음과 구별되지 않는다.", "",
         f"| w | 2점 R@10 ({len(two)}문항) | 대안 포함 R@10 ({len(rec)}) | nDCG@5 | 2점 MRR@5 | judged@10 | 2점 R@10 차이 | 개선/악화 | 대안 포함 R@10 차이 |",
         "|---:|---:|---:|---:|---:|---:|---|---:|---|"]
    for w, r in rows.items():
        L.append(f"| {w} | {f(r['r10_2'])} | {f(r['r10_1'])} | {f(r['ndcg5'])} | {f(r['mrr5_2'])} | {f(r['judged10'])} | "
                 f"{ci(r['d2'])} | {r['wins2']}/{r['losses2']} | {ci(r['d1'])} |")
    L += ["", "## 유형별 대안 포함 R@10 (읽기용: 문항 수가 적어 유형별 가중치를 고르는 근거로 쓰지 않음)", "",
          "| 유형 | 문항 | " + " | ".join(str(w) for w in WEIGHTS) + " | 최고 w |", "|---|---:|" + "---:|" * (len(WEIGHTS) + 1)]
    for t, qs in sorted(types.items()):
        vals = {w: mean([metric(w, q, "raw", "recall@10") for q in qs]) for w in WEIGHTS}
        best = max(vals.values())
        L.append(f"| {t} | {len(qs)} | " + " | ".join(f"{v:.2f}" for v in vals.values()) + " | "
                 + ", ".join(str(w) for w, v in vals.items() if v >= best - 1e-9) + " |")
    (out / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out}: {len(WEIGHTS)} weights, pilot 1 hybrid reproduced {reproduced}/{len(labels)}")


if __name__ == "__main__":
    main()
