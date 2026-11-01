"""22 - golden-set evaluation of dataset recommendation (hypergraph_search).

Deterministic: no LLM, only the retrieval the graph (17) calls, so a weight or rule change can be
judged by numbers before it ships. Each scenario lists datasets a reviewer would accept in the
top 10; ids missing from the current corpus are reported and skipped, not counted as misses.

    python 22_eval_recommendations.py           # table + means; exit 1 if mean P@10 < --min-p10
    python 22_eval_recommendations.py --public  # also score test/public_data/labels/public_data_golden.jsonl

Public-data scenarios come from the judged golden set (test/public_data/README.md) and are run
the way 17 searches service data: dataset_terms + query vector, roles=["service"]. A judged id
also matches its cross-listed copies (entity `duplicates`). nDCG@10 uses the 0/1/2 grades.
Abstention queries are reported separately: how many judged-relevant or must_exclude datasets
appear in the top 10, since the ranker has no empty-result path yet.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import hypergraph_search as hs

SEOUL = "seoul_open_data/"
SCENARIOS: list[dict[str, Any]] = [
    {"name": "embedding: snowflake-ko", "model": "dragonkue/snowflake-arctic-embed-l-v2.0-ko", "expected": "embedding"},
    {"name": "embedding: KoSimCSE", "model": "BM-K/KoSimCSE-Unsup-RoBERTa", "expected": "embedding"},
    {"name": "embedding: e5-small", "model": "intfloat/multilingual-e5-small", "expected": "embedding"},
    {"name": "reranker: ko-reranker", "model": "Dongjin-kr/ko-reranker", "expected": "reranking"},
    {"name": "generation: Qwen2.5-3B-Korean", "model": "MyeongHo0621/Qwen2.5-3B-Korean", "expected": "generation"},
    {
        "name": "service: 따릉이",
        "terms": ["교통", "따릉이"],
        "roles": ["service"],
        "query": "따릉이 대여소 위치와 실시간 대여 가능 자전거 수",
        "expected": "ddareungi",
    },
    {
        "name": "service: 서울 미세먼지",
        "terms": ["미세먼지", "서울"],
        "roles": ["service"],
        "query": "서울시 실시간 미세먼지 농도와 대기질 측정 데이터",
        "expected": "air",
    },
]
EXPECTED = {
    "embedding": {
        "klue/klue",
        "kakaobrain/kor_nli",
        "taeminlee/Ko-StrategyQA",
        "miracl/miracl",
        "miracl/miracl-corpus",
        "sentence-transformers/miracl",
        "nlpai-lab/miracl-multilingual-triplets",
        "KaLM-Embedding/KaLM-reranker-training-data",
        "cnupo23/korean-medicine-embedding-dataset",
        "BCCard/BCAI-Finance-Kor-Embedding-Triplet",
        "BCCard/BCAI-Finance-Kor-Embedding-Pair",
        "whybe-choi/ko-vdr-hn",
        "whybe-choi/ko-triplet-hn",
        "codefuse-ai/F2LLM-v2",
        "hakari-bench/NanoMIRACL",
        "MoritzLaurer/multilingual-NLI-26lang-2mil7",
        "felfri/MSTS",
        "gyung/ko-law-retriever-artifacts-20260622",
        "datalama/miracl-hard-negatives",
        "yoh/modular-sentence-encoders-sts",
        "Pixel-Linguist/rendered-sts17",
        "BidirLM/BidirLM-Contrastive",
        "sentence-transformers/parallel-sentences-talks",
        "LLM-OS-Models2/ko-legal-embedding-training-v1",
        "watchstep/ko-en-code-mixing-sts",
    },
    "reranking": {
        "KaLM-Embedding/KaLM-reranker-training-data",
        "Horizon-Labs/multilingual-rerank-distill",
        "olaverse/reranker-triples-multi",
        "nlpai-lab/miracl-multilingual-triplets",
        "lightblue/reranker_continuous_filt_max7_train",
        "ggh5454/legal-provence-ko-with-teacher-scores",
        "ggh5454/legal-provence-ko",
        "datalama/miracl-hard-negatives",
        "miracl/miracl",
        "taeminlee/Ko-StrategyQA",
        "whybe-choi/ko-triplet-hn",
        "sentence-transformers/miracl",
        "upskyy/ko-wiki-reranking",
        "LLM-OS-Models/korean-embedding-ko-triplet-hn-pilot-10k",
    },
    "generation": {
        "allganize/IFEval-Ko",
        "nayohan/GPT4-LLM-Cleaned-ko",
        "kyujinpy/OpenOrca-KO",
        "kyujinpy/KOR-OpenOrca-Platypus-v3",
        "nvidia/Nemotron-SFT-Multilingual-v2",
        "brandonbaek/konglish-synthetic-instruct",
        "llami-team/Korean-OpenThoughts-114k-Normalized",
        "KOREAson/YiSang-HighQuality",
        "jojo0217/korean_rlhf_dataset",
        "HAERAE-HUB/KMMLU",
        "HAERAE-HUB/HAE_RAE_BENCH_1.1",
        "nlpai-lab/databricks-dolly-15k-ko",
        "squarelike/OpenOrca-gugugo-ko",
        "nlpai-lab/openassistant-guanaco-ko",
        "beomi/KoAlpaca-v1.1a",
        "Qwen/P-MMEval",
        "MyeongHo0621/korean-quality-cleaned",
    },
    "ddareungi": {
        SEOUL + i
        for i in (
            "OA-15493",
            "OA-13252",
            "OA-15182",
            "OA-20447",
            "OA-21235",
            "OA-15246",
            "OA-15248",
            "OA-15249",
            "OA-15242",
            "OA-15245",
            "OA-21229",
        )
    },
    "air": {
        SEOUL + i
        for i in (
            "OA-2223",
            "OA-2275",
            "OA-2221",
            "OA-2218",
            "OA-2217",
            "OA-2216",
            "OA-21090",
            "OA-1200",
            "OA-2219",
            "OA-2220",
            "OA-15526",
            "OA-1201",
        )
    },
}
K = 10
PUBLIC_GOLDEN = Path(__file__).resolve().parent / "test" / "public_data" / "labels" / "public_data_golden.jsonl"


def run(scenario):
    if "model" in scenario:
        return [r["dataset"] for r in hs.datasets_for_model(scenario["model"], limit=K)]
    rows = hs.rank_datasets(
        hs.concepts_from_terms(scenario["terms"]),
        query_vector=hs.embed_query(scenario["query"]),
        roles=scenario.get("roles"),
        limit=K,
        keywords=scenario["terms"],
    )
    return [r["dataset"] for r in rows]


def evaluate():
    entities = hs.load_graph()[0]
    present = {e["name"] for e in entities.values() if e["kind"] == "dataset"}
    rows: list[tuple[str, float | None, float | None, float | None, str]] = []
    for scenario in SCENARIOS:
        if "model" in scenario and f"model:{scenario['model']}" not in entities:
            rows.append((scenario["name"], None, None, None, "model not in corpus"))
            continue
        expected = EXPECTED[scenario["expected"]] & present
        top = run(scenario)
        hits = [d for d in top if d in expected]
        first = next((i for i, d in enumerate(top, 1) if d in expected), None)
        rows.append(
            (
                scenario["name"],
                len(hits) / K,
                len(hits) / min(K, len(expected)) if expected else None,
                1 / first if first else 0.0,
                f"{len(expected)} expected in corpus",
            )
        )
    return rows


def _aliases(entities):
    """dataset name -> every name that counts as the same dataset (itself + cross-listed copies)."""
    out = {}
    for e in entities.values():
        if e["kind"] == "dataset":
            names = {e["name"], *(e.get("duplicates") or [])}
            for name in names:
                out[name] = names
    return out


def _public_top(label):
    terms = list(label["dataset_terms"])
    if region := label["conditions"].get("region"):
        terms.append(region)
    rows = hs.rank_datasets(
        hs.concepts_from_terms(terms),
        query_vector=hs.embed_query(label["query"]),
        commercial_only=bool(label["conditions"].get("commercial")),
        roles=["service"],
        limit=K,
        keywords=terms,
    )
    return [r["dataset"] for r in rows]


def evaluate_public(path):
    entities = hs.load_graph()[0]
    alias = _aliases(entities)
    labels = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    scored, abstain = [], []
    for label in labels:
        if not label["evaluable"]:
            continue
        grades = {}
        for dataset, grade in label["relevant"].items():
            for name in alias.get(dataset, {dataset}):
                grades[name] = max(grade, grades.get(name, 0))
        excluded = {n for d in label["must_exclude"] for n in alias.get(d, {d})}
        top = _public_top(label)
        if label["expected_behavior"] == "abstain":
            abstain.append((label["query_id"], sum(d in excluded or d in grades for d in top), len(top)))
            continue
        gains = [grades.get(d, 0) for d in top]
        ideal = sorted(label["relevant"].values(), reverse=True)[:K]
        dcg = sum(g / math.log2(i + 2) for i, g in enumerate(gains))
        idcg = sum(g / math.log2(i + 2) for i, g in enumerate(ideal))
        first = next((i for i, g in enumerate(gains, 1) if g), None)
        hits = sum(1 for g in gains if g)
        scored.append(
            (
                f"{label['query_id']} {label['query_type']}",
                hits / K,
                hits / min(K, len(label["relevant"])),
                1 / first if first else 0.0,
                dcg / idcg if idcg else 0.0,
                sum(d in excluded for d in top),
            )
        )
    return scored, abstain


def print_public(path):
    scored, abstain = evaluate_public(path)
    print(f"\npublic data ({path.name})")
    print(f"{'query':<34} {'P@10':>5} {'R@10':>5} {'MRR':>5} {'nDCG':>5}  must_exclude in top")
    for name, p, r, mrr, ndcg, bad in scored:
        print(f"{name:<34} {p:5.2f} {r:5.2f} {mrr:5.2f} {ndcg:5.2f}  {bad}")
    if scored:
        mean = lambda i: sum(row[i] for row in scored) / len(scored)  # noqa: E731
        print(f"{'mean (' + str(len(scored)) + ')':<34} {mean(1):5.2f} {mean(2):5.2f} {mean(3):5.2f} {mean(4):5.2f}")
    for query_id, wrong, returned in abstain:
        print(f"abstain {query_id}: {returned} returned, {wrong} judged relevant/excluded in top {K}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min-p10", type=float, default=0.0, help="fail (exit 1) below this mean P@10")
    parser.add_argument("--public", nargs="?", type=Path, const=PUBLIC_GOLDEN, help="also score a public golden set")
    args = parser.parse_args()
    rows = evaluate()
    print(f"{'scenario':<34} {'P@10':>5} {'R@10':>5} {'MRR':>5}  note")
    for name, p, r, mrr, note in rows:
        fmt = lambda v: "  -  " if v is None else f"{v:5.2f}"  # noqa: E731
        print(f"{name:<34} {fmt(p)} {fmt(r)} {fmt(mrr)}  {note}")
    scored = [row for row in rows if row[1] is not None]
    mean = lambda i: sum(row[i] for row in scored) / len(scored)  # noqa: E731
    print(f"{'mean':<34} {mean(1):5.2f} {mean(2):5.2f} {mean(3):5.2f}")
    if args.public:
        print_public(args.public)
    if mean(1) < args.min_p10:
        sys.exit(1)


if __name__ == "__main__":
    main()
