"""Pilot 1: five public-portal retrieval paths on the frozen v2, one label set, one condition policy.

    python -X utf8 test/public_data/retrieval/pilot.py --dir test/public_data/retrieval/runs/<name>
    python -X utf8 test/public_data/retrieval/pilot.py --dir runs/<new> --rescore runs/<saved> --labels <labels> --spec <spec>
        (score a saved run's rankings against other labels; no search)

Paths (all searched over data.go.kr + 서울 열린데이터광장 datasets only; settings in SETTINGS):
  hg_question  hypergraph_search.rank_datasets with the question vector only (golden_prep "question_only")
  hg_terms     the same with the label's dataset_terms + region as concepts/keywords (22._public_top):
               the 2026-11-16 baseline's method, a 검색어 보조 reference, not a main-experiment input
  dense        question vector vs every chunk of a dataset, dataset score = best chunk
  bm25         the dataset's card text, words + Hangul bigrams (tokens()), Okapi BM25
  hybrid       weighted RRF of the dense and bm25 lists, each taken independently (no dense floor)

No path calls an API: question vectors come from compare/query_vectors.jsonl. Conditions are checked
with golden_prep.condition_checks, the rules the labels were judged by. After a path ranks, datasets
with a confirmed unmet explicit condition are removed, the same for every path; unknown and partial
stay and are counted. Region and realtime are never filters on their own: a region is unmet only when
the title names another region, and realtime is always unknown.

Scoring collapses confirmed copies (the graph's duplicate groups) to one dataset, keeps its first rank,
and reads labels v6 as is: held pairs (label "unjudged") and datasets nobody judged are not hits; raw
keeps them in the ranking, condensed drops them. A run folder is never overwritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
AI = HERE.parents[2]
CORPUS_V2 = HERE.parent / "corpus_v2"
sys.path[:0] = [str(AI), str(CORPUS_V2)]

import compare_corpora as cc  # noqa: E402  (also imports hypergraph_search and 22_eval_recommendations)
import golden_prep as gp  # noqa: E402
from corpus_manifest import content_digest  # noqa: E402
from retrieval_lab import fusion, metrics  # noqa: E402

hs = cc.hs
LABELS = CORPUS_V2 / "golden_prep" / "batch5" / "labels_llm_v6.jsonl"
SPEC = HERE / "query_spec_v1.jsonl"
COVERAGE = None  # --coverage: Coverage@10 labels for multi_dataset questions
PIN = CORPUS_V2 / "data_version.json"
PORTALS = ("data_go_kr/", "seoul_open_data/")
PATHS = ("hg_question", "hg_terms", "dense", "bm25", "hybrid")
K = 10
SETTINGS = {
    "sources": list(PORTALS),
    "channel_depth": 100,  # candidates each of dense / bm25 keeps before fusion
    "hg_limit": 300,  # rank_datasets limit before the source cut (it returns HF/Kaggle too)
    "top_k": 30,
    "rrf_k": fusion.RRF_K,
    "dense_weight": 0.5,
    "sparse_weight": 0.5,
    "bm25": {"k1": 1.2, "b": 0.75, "document": "card chunk only", "query_terms": "unique"},
    "dense": {"model": "text-embedding-3-small (frozen vectors)", "document": "all chunks", "dataset_score": "max chunk cosine"},
    "filter": "after ranking: drop confirmed unmet explicit conditions (golden_prep.condition_checks), then cut to top_k",
    "hg_internal": "rank_datasets keeps its own floors and commercial_only (drops conditional licenses too)",
}
WORD_RE = re.compile(r"[0-9a-z가-힣]+")
HANGUL_RE = re.compile(r"[가-힣]{2,}")
CONDITION_KEYS = ("region", "delivery", "commercial", "kogl_type1_only", "realtime")


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).open(encoding="utf-8") if line.strip()]


def tokens(text):
    """Words (runs of Hangul, Latin and digits, casefolded; anything else splits, so
    data_go_kr/15000115 -> data, go, kr, 15000115 and 1유형 stays one word) plus '#'-marked bigrams of
    each Hangul run of two or more letters (공영주차장 -> #공영 #영주 #주차 #차장)."""
    text = str(text or "").casefold()
    grams = ["#" + run[i : i + 2] for run in HANGUL_RE.findall(text) for i in range(len(run) - 1)]
    return WORD_RE.findall(text) + grams


class BM25:
    """Okapi BM25 over whole documents, postings in numpy arrays (no new dependency)."""

    def __init__(self, texts, k1=1.2, b=0.75):
        self.k1, self.vocab = k1, {}
        terms, docs, tfs, lengths = [], [], [], []
        for d, text in enumerate(texts):
            counts = Counter(tokens(text))
            lengths.append(sum(counts.values()))
            for term, n in counts.items():
                terms.append(self.vocab.setdefault(term, len(self.vocab)))
                docs.append(d)
                tfs.append(n)
        order = np.argsort(np.asarray(terms, dtype=np.int64), kind="stable")
        self.terms = np.asarray(terms, dtype=np.int64)[order]
        self.docs = np.asarray(docs, dtype=np.int64)[order]
        self.tf = np.asarray(tfs, dtype=np.float64)[order]
        self.start = np.searchsorted(self.terms, np.arange(len(self.vocab) + 1))
        n_docs, df = len(texts), np.diff(self.start)
        self.idf = np.log1p((n_docs - df + 0.5) / (df + 0.5))
        lengths = np.asarray(lengths, dtype=np.float64)
        self.norm = k1 * (1.0 - b + b * lengths / max(lengths.mean(), 1.0))
        self.n_docs = n_docs

    def scores(self, query):
        out = np.zeros(self.n_docs)
        for term in set(tokens(query)):
            i = self.vocab.get(term)
            if i is None:
                continue
            a, z = self.start[i], self.start[i + 1]
            tf, docs = self.tf[a:z], self.docs[a:z]  # a term lists each document once
            out[docs] += self.idf[i] * tf * (self.k1 + 1.0) / (tf + self.norm[docs])
        return out


def ranked(ids, scores, depth, positive_only=False):
    order = sorted((i for i in range(len(ids)) if not positive_only or scores[i] > 0), key=lambda i: (-scores[i], ids[i]))
    return [ids[i] for i in order[:depth]]


class Searcher:
    def __init__(self):
        self.cards = {c["dataset_id"]: c["text"] for c in read_jsonl(hs.DATASET_INDEX_DIR / "chunks.jsonl")
                      if c["kind"] == "card" and c["dataset_id"].startswith(PORTALS)}
        self.ids = sorted(self.cards)
        started = time.perf_counter()
        self.bm25 = BM25([self.cards[d] for d in self.ids], SETTINGS["bm25"]["k1"], SETTINGS["bm25"]["b"])
        self.bm25_build_s = round(time.perf_counter() - started, 1)
        hs.load_dataset_vectors()  # warm the matrix so the first query's latency is a search, not a load

    def dense(self, vector):
        scores = hs.dense_scores(vector)
        return ranked(self.ids, [scores[d] for d in self.ids], SETTINGS["channel_depth"])

    def sparse(self, text):
        return ranked(self.ids, self.bm25.scores(text), SETTINGS["channel_depth"], positive_only=True)

    @staticmethod
    def hypergraph(label, vector, with_terms, limit=SETTINGS["hg_limit"]):
        commercial = bool(label["conditions"].get("commercial"))
        terms = []
        if with_terms:  # mirror of 22_eval_recommendations._public_top
            terms = list(label["dataset_terms"]) + ([label["conditions"]["region"]] if label["conditions"].get("region") else [])
        rows = hs.rank_datasets(hs.concepts_from_terms(terms), query_vector=vector, commercial_only=commercial,
                                roles=["service"], limit=limit, keywords=terms)
        names = [r["dataset"] for r in rows]
        if limit != SETTINGS["hg_limit"]:
            return names
        return [n for n in names if n.startswith(PORTALS)], [n for n in names if not n.startswith(PORTALS)]

    def run(self, path, label, vector):
        """(ranking before the condition filter, non-public results cut, ms)."""
        started = time.perf_counter()
        cut = []
        if path in ("hg_question", "hg_terms"):
            out, cut = self.hypergraph(label, vector, path == "hg_terms")
        elif path == "dense":
            out = self.dense(vector)
        elif path == "bm25":
            out = self.sparse(label["query"])
        else:
            lists = fusion.channel_lists([self.dense(vector)], [self.sparse(label["query"])],
                                         SETTINGS["dense_weight"], SETTINGS["sparse_weight"])
            out = [d for d, _ in fusion.weighted_rrf(lists, k=SETTINGS["rrf_k"])]
        return out, cut, (time.perf_counter() - started) * 1000.0


class Conditions:
    """golden_prep's card facts and condition checks, cached per dataset."""

    def __init__(self):
        self.rows = {r["dataset_id"]: r for r in read_jsonl(gp.ENRICHED)}
        self.entities = {e["name"]: e for e in hs.load_graph()[0].values() if e["kind"] == "dataset"}

    @lru_cache(maxsize=None)
    def facts(self, dataset_id):
        row = self.rows.get(dataset_id, {})
        readme = AI / row["readme_path"] if row.get("readme_path") else None
        text = readme.read_text(encoding="utf-8") if readme and readme.is_file() else ""
        return gp.facts(self.entities.get(dataset_id, {}), row, text)

    def check(self, spec, dataset_id):
        query = {"query": spec["query"], "conditions": spec["conditions"]}
        checks = gp.condition_checks(query, self.facts(dataset_id))
        return {k: v["status"] for k, v in checks.items() if k in CONDITION_KEYS}


def apply_filter(ranking, spec, conditions):
    """Drop confirmed unmet explicit conditions; return (kept, removed, statuses of the kept)."""
    kept, removed, statuses = [], [], {}
    for d in ranking:
        status = conditions.check(spec, d)
        if gp.UNMET in status.values():
            removed.append(d)
        else:
            kept.append(d)
            statuses[d] = status
    return kept, removed, statuses


def score_query(ranking, label, alias, statuses):
    """Metrics of one filtered ranking; copies collapse to one dataset at its first rank."""
    canon = lambda d: min(alias.get(d, {d}))  # noqa: E731
    seen, deduped = set(), []
    for d in ranking:
        if canon(d) not in seen:
            seen.add(canon(d))
            deduped.append(d)
    grades = {}
    for d, g in label["relevant"].items():
        grades[canon(d)] = max(g, grades.get(canon(d), 0))
    judged = set(grades) | {canon(d) for d in label["must_exclude"] + label["judged_irrelevant"]}
    held = {canon(d) for d in label["unjudged"]}
    excluded = {canon(d) for d in label["must_exclude"]}
    raw = [canon(d) for d in deduped]
    top = raw[:K]
    out = {
        "returned": len(raw),
        "top10": len(top),
        "judged@10": sum(d in judged for d in top) / K,
        "held@10": sum(d in held for d in top),
        "unjudged@10": sum(d not in judged and d not in held for d in top),
        "must_exclude@10": sum(d in excluded for d in top),
        "relevant_in_top10": sum(grades.get(d, 0) >= 1 for d in top),
        "unknown@10": dict(Counter(k for d in deduped[:K] for k, s in statuses[d].items() if s == gp.UNKNOWN)),
        "partial@10": dict(Counter(k for d in deduped[:K] for k, s in statuses[d].items() if s == gp.PARTIAL)),
        "duplicates_collapsed": len(ranking) - len(deduped),
    }
    if label["expected_behavior"] == "abstain":
        return out
    condensed = [d for d in raw if d in judged]
    out["raw"] = metrics.ranking_metrics(raw, grades, 1)
    out["condensed"] = metrics.ranking_metrics(condensed, grades, 1)
    if any(g == 2 for g in grades.values()):
        out["raw2"] = metrics.ranking_metrics(raw, grades, 2)
        out["condensed2"] = metrics.ranking_metrics(condensed, grades, 2)
    return out


def code_record():
    files = [Path(__file__), SPEC, CORPUS_V2 / "golden_prep.py", CORPUS_V2 / "compare_corpora.py",
             AI / "hypergraph_search.py", AI / "retrieval_lab" / "fusion.py", AI / "retrieval_lab" / "metrics.py"]
    git = lambda *a: subprocess.run(["git", *a], cwd=AI, capture_output=True, text=True).stdout.strip()  # noqa: E731
    return {
        "commit": git("rev-parse", "HEAD"),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "uncommitted": git("status", "--porcelain", "--", *(str(f.relative_to(AI)) for f in files)).splitlines(),
        "files_lf_sha256": {str(f.relative_to(AI)).replace("\\", "/"): content_digest(f)[0] for f in files},
    }


def search_inputs(specs):
    """What a saved ranking depends on per question: the text searched and the conditions filtered by
    (Conditions.check reads only these). Types, aspects and grades can change without a new search."""
    return {q: {"query": s["query"], "conditions": s["conditions"]} for q, s in sorted(specs.items())}


def prior_inputs(prior):
    """The search inputs of a saved run; a run before they were recorded is read from the spec file it names,
    and only while that file is still the one it recorded."""
    if "search_inputs" in prior:
        return prior["search_inputs"]
    path = AI / prior["spec"]["path"]
    if not path.is_file() or content_digest(path)[0] != prior["spec"]["sha256"]:
        raise SystemExit(f"{prior['spec']['path']} is no longer the spec the saved run used "
                         f"(sha256 {prior['spec']['sha256'][:16]}): restore it or search again")
    return search_inputs({s["query_id"]: s for s in read_jsonl(path)})


def rescore_guard(prior, specs):
    """Rescoring is for new grades only: a changed question or filter condition needs a new search."""
    old, new = prior_inputs(prior), search_inputs(specs)
    changed = sorted(q for q in new if old.get(q) != new[q])
    if changed:
        raise SystemExit(f"question or filter conditions differ from the saved run for {changed[:5]}"
                         f"{' ...' if len(changed) > 5 else ''} ({len(changed)}): search again instead of --rescore")


def rescore(prior_dir, labels, specs, alias, conditions):
    """Score a saved run's filtered rankings against other labels: no search, no vectors.
    Filter counts (unmet, non-public cut) depend on the conditions, not the labels, and are carried over."""
    rankings = read_jsonl(prior_dir / "rankings.jsonl")
    old = json.loads((prior_dir / "scores.json").read_text(encoding="utf-8"))
    by_q = {lb["query_id"]: lb for lb in labels}
    scores = defaultdict(dict)
    for r in rankings:
        qid, path = r["query_id"], r["path"]
        statuses = {d: conditions.check(specs[qid], d) for d in r["top"]}
        s = score_query(r["top"], by_q[qid], alias, statuses)
        for key in ("unmet_in_unfiltered_top10", "non_public_cut_in_top10"):
            s[key] = old[path][qid][key]
        scores[path][qid] = s
    return rankings, scores


def run(out, prior_dir=None):
    out = Path(out)
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"{out} already holds a run: pick a new --dir")
    identity = hs.use_corpus("v2")
    pin = json.loads(PIN.read_text(encoding="utf-8"))["data_version"]
    if not identity["documents_id"].startswith(pin):
        raise SystemExit(f"checked-out v2 documents_id {identity['documents_id'][:16]} is not the pin {pin}")
    labels = read_jsonl(LABELS)
    specs = {s["query_id"]: s for s in read_jsonl(SPEC)}
    for label in labels:  # the spec annotates the labels, it never changes what they say
        s = specs[label["query_id"]]
        if (s["query"], s["conditions"], s["expected_behavior"]) != (label["query"], label["conditions"], label["expected_behavior"]):
            raise SystemExit(f"{label['query_id']}: spec differs from the labels in query, conditions or behavior")
    alias = cc.confirmed_aliases()
    conditions = Conditions()

    if prior_dir:
        prior = json.loads((prior_dir / "run.json").read_text(encoding="utf-8"))
        if prior["data_version"] != pin or prior["identity"]["documents_id"] != identity["documents_id"]:
            raise SystemExit(f"{prior_dir} ranked another corpus: rescoring needs the same frozen v2")
        if json.loads((prior_dir / "aliases.json").read_text(encoding="utf-8")) != json.loads(json.dumps(cc.alias_groups(), ensure_ascii=False)):
            raise SystemExit(f"{prior_dir}/aliases.json differs from today's copy groups")
        rescore_guard(prior, specs)
        rankings, scores = rescore(prior_dir, labels, specs, alias, conditions)
        latency_ms, same = prior["latency_ms"], prior["baseline_reproduced"]
        searcher_stats = {k: prior[k] for k in ("corpus_public_datasets", "bm25_vocab", "bm25_build_s")}
    else:
        cc.use_saved_vectors(allow_embed=False)
        searcher = Searcher()
        rankings, scores, latency = [], defaultdict(dict), defaultdict(list)
        for label in labels:
            qid, spec = label["query_id"], specs[label["query_id"]]
            vector = hs.embed_query(label["query"])
            for path in PATHS:
                ranking, cut, ms = searcher.run(path, label, vector)
                kept, removed, statuses = apply_filter(ranking, spec, conditions)
                kept = kept[: SETTINGS["top_k"]]
                unmet_in_unfiltered_top10 = sum(d in removed for d in ranking[:K])
                latency[path].append(ms)
                rankings.append({"path": path, "query_id": qid, "top": kept, "removed_unmet": removed[:50],
                                 "non_public_cut": cut, "ms": round(ms, 2)})
                s = score_query(kept, label, alias, statuses)
                s["unmet_in_unfiltered_top10"] = unmet_in_unfiltered_top10
                s["non_public_cut_in_top10"] = sum(1 for d in cut if d in set(ranking[:K]))
                scores[path][qid] = s

        # Reproduction check: hg_terms before the source cut and filter must equal the 2026-11-16 baseline.
        base = {r["query_id"]: r["top"] for r in read_jsonl(CORPUS_V2 / "compare" / "runs" / "2026-11-16_v2-aa1a71d3_labels-v6" / "rankings_v2.jsonl") if r.get("kind") == "public"}
        same = sum(searcher.hypergraph(lb, hs.embed_query(lb["query"]), True, limit=30) == base[lb["query_id"]] for lb in labels)
        same = f"{same}/{len(labels)} (hg_terms before source cut and filter vs 2026-11-16_v2-aa1a71d3_labels-v6)"
        latency_ms = {p: {"p50": metrics.percentile(v, 50), "p95": metrics.percentile(v, 95), "p99": metrics.percentile(v, 99)} for p, v in latency.items()}
        searcher_stats = {"corpus_public_datasets": len(searcher.ids), "bm25_vocab": len(searcher.bm25.vocab), "bm25_build_s": searcher.bm25_build_s}

    out.mkdir(parents=True, exist_ok=True)
    (out / "aliases.json").write_text(json.dumps(cc.alias_groups(), ensure_ascii=False) + "\n", encoding="utf-8")
    with (out / "rankings.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in rankings:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    (out / "scores.json").write_text(json.dumps(scores, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    blind = unjudged_items(rankings, labels, specs, alias, conditions)
    with (out / "unjudged_blind.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for item in blind:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    worksheet = coverage_worksheet(labels, specs, conditions)
    with (out / "coverage_worksheet.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for item in worksheet:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    cov = coverage_at_k(rankings, labels, specs, alias, read_jsonl(COVERAGE)) if COVERAGE else None
    if cov:
        (out / "coverage.json").write_text(json.dumps(cov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    record = {
        "identity": identity, "data_version": pin,
        "labels": cc.file_record(LABELS), "spec": cc.file_record(SPEC),
        "coverage_labels": cc.file_record(COVERAGE) if COVERAGE else None,
        "query_vectors": cc.file_record(cc.VECTORS), "aliases": cc.file_record(out / "aliases.json"),
        "search_inputs": search_inputs(specs),
        "settings": SETTINGS, "paths": PATHS, "new_query_vectors": 0, "api_calls": 0,
        "rescored_from": None if prior_dir is None else {"dir": str(prior_dir).replace("\\", "/"),
                                                          "rankings": cc.file_record(prior_dir / "rankings.jsonl")},
        "baseline_reproduced": same, **searcher_stats, "latency_ms": latency_ms,
        "environment": {"python": platform.python_version(), "platform": platform.platform(), "processor": platform.processor(),
                        "note": "query vectors read from the saved file: latency excludes question embedding"},
        "code": code_record(),
    }
    (out / "run.json").write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "report.md").write_text(report(scores, specs, labels, record, blind, cov), encoding="utf-8")
    print(f"{out}: {len(rankings)} rankings, unjudged for review {len(blind)}, baseline reproduced {same}")


def unjudged_items(rankings, labels, specs, alias, conditions):
    """Union of every path's top 10 that labels v6 never judged (held pairs apart), blind: no path, no rank."""
    by_q = {lb["query_id"]: lb for lb in labels}
    pairs = set()
    for r in rankings:
        lb = by_q[r["query_id"]]
        known = {n for d in list(lb["relevant"]) + lb["must_exclude"] + lb["judged_irrelevant"] + lb["unjudged"] for n in alias.get(d, {d})}
        pairs |= {(r["query_id"], d) for d in r["top"][:K] if d not in known}
    items = []
    for qid, d in sorted(pairs):
        f = conditions.facts(d)
        item_id = hashlib.sha256(f"{qid}|{d}".encode()).hexdigest()[:12]
        items.append({"item_id": item_id, "query_id": qid, "query": specs[qid]["query"], "conditions": specs[qid]["conditions"],
                      "dataset_id": d, "condition_checks": conditions.check(specs[qid], d),
                      "facts": {k: f[k] for k in ("title", "source", "url", "publisher", "coverage_regions", "coverage_status",
                                                  "formats", "licenses", "api_check", "update_cycle_portal", "fields", "description")},
                      "judgment": None, "grade": None, "evidence": None})
    random.Random(20261116).shuffle(items)  # order says nothing about which path found it
    return items


def coverage_worksheet(labels, specs, conditions):
    """multi_dataset questions: each judged-relevant dataset with an empty aspect tag, grades untouched."""
    rows = []
    for lb in labels:
        s = specs[lb["query_id"]]
        if s["type"] != "multi_dataset":
            continue
        for d, grade in sorted(lb["relevant"].items()):
            rows.append({"query_id": lb["query_id"], "query": lb["query"], "aspects": s["aspects"], "dataset_id": d,
                         "title": conditions.facts(d)["title"], "grade": grade,
                         "covers": None, "covers_fully": None, "evidence": None})
    return rows


def coverage_at_k(rankings, labels, specs, alias, covers):
    """multi_dataset questions: share of the question's aspects that the top 10 covers, counting only datasets
    judged relevant (the coverage labels tag those); copies count once. Every relevant pair must be tagged."""
    canon = lambda d: min(alias.get(d, {d}))  # noqa: E731
    tagged = defaultdict(set)
    for c in covers:
        tagged[(c["query_id"], canon(c["dataset_id"]))] |= set(c["covers"])
    missing = [(lb["query_id"], d) for lb in labels if specs[lb["query_id"]]["type"] == "multi_dataset"
               for d in lb["relevant"] if (lb["query_id"], canon(d)) not in tagged]
    if missing:
        raise SystemExit(f"coverage labels miss {len(missing)} relevant pairs, e.g. {missing[:3]}")
    out = defaultdict(dict)
    for r in rankings:
        qid, s = r["query_id"], specs[r["query_id"]]
        if s["type"] != "multi_dataset" or s["expected_behavior"] != "recommend":
            continue
        top = list(dict.fromkeys(canon(d) for d in r["top"]))[:K]
        got = set().union(*(tagged.get((qid, d), set()) for d in top))
        out[r["path"]][qid] = {"covered": sorted(got), "missing": [a for a in s["aspects"] if a not in got],
                               "coverage@10": len(got) / len(s["aspects"])}
    return out


# ---------------------------------------------------------------- report

COLS = (("recall@5", "R@5"), ("recall@10", "R@10"), ("precision@10", "P@10"), ("f1@10", "F1@10"), ("hit@10", "Hit@10"),
        ("mrr@5", "MRR@5"), ("ndcg@5", "nDCG@5"), ("map@5", "MAP@5"))


def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else float("nan")


def table(scores, qids, key):
    lines = ["| 경로 | 문항 | " + " | ".join(c for _, c in COLS) + " |", "|---|---:|" + "---:|" * len(COLS)]
    for path in PATHS:
        rows = [scores[path][q][key] for q in qids if key in scores[path][q]]
        lines.append(f"| {path} | {len(rows)} | " + " | ".join(f"{mean(r[m] for r in rows):.3f}" for m, _ in COLS) + " |")
    return lines


def report(scores, specs, labels, record, blind, cov=None):
    rec = [lb["query_id"] for lb in labels if lb["expected_behavior"] == "recommend"]
    abst = [lb["query_id"] for lb in labels if lb["expected_behavior"] == "abstain"]
    two = [q for q in rec if "raw2" in scores["dense"][q]]
    again = record.get("rescored_from")
    L = ["# 공공데이터 검색 경로 파일럿 1 (잠정)", "",
         f"코퍼스 v2 `{record['data_version']}`, 라벨 `{Path(record['labels']['path']).stem}` `{record['labels']['sha256'][:16]}`, "
         f"명세 `{Path(record['spec']['path']).stem}` `{record['spec']['sha256'][:16]}`. "
         f"외부 API 호출 0. 기준선 재현 {record['baseline_reproduced']}.", ""]
    if again:
        L += [f"검색은 다시 하지 않았다. `{again['dir']}`에 저장된 순위(`rankings.jsonl` `{again['rankings']['sha256'][:16]}`)를 "
              "이 라벨로 다시 채점했다. 지연 시간과 기준선 재현은 그 실행의 값이다.", ""]
    L += [
         "모든 경로가 공공포털 두 곳만 검색하고, 확인된 명시 조건 불충족을 같은 시점(순위 뒤)에 뺐다. "
         "질문 유형과 조건은 사람이 정한 값(명세)을 쓴 것이라 자동 분류를 포함한 서비스 성능이 아니다.", ""]
    for title, key, qids in (("대안 포함(1점 이상) raw", "raw", rec), ("대안 포함(1점 이상) condensed", "condensed", rec),
                             (f"2점 정답 raw (2점 정답이 있는 {len(two)}문항, 없는 {len(rec) - len(two)}문항 제외)", "raw2", two),
                             ("2점 정답 condensed", "condensed2", two)):
        L += [f"## {title}", ""] + table(scores, qids, key) + [""]
    L += ["## 유형별 R@10 (raw, 1점 이상 / 2점)", "", "| 유형 | 문항(2점) | " + " | ".join(PATHS) + " |", "|---|---:|" + "---:|" * len(PATHS)]
    groups = defaultdict(list)
    for q in rec:
        groups[specs[q]["type"]].append(q)
        if "ai_data" in specs[q]["tags"]:
            groups["(태그) ai_data"].append(q)
    for g, qids in sorted(groups.items()):
        q2 = [q for q in qids if q in two]
        cells = [f"{mean(scores[p][q]['raw']['recall@10'] for q in qids):.2f} / "
                 + (f"{mean(scores[p][q]['raw2']['recall@10'] for q in q2):.2f}" if q2 else "–") for p in PATHS]
        L.append(f"| {g} | {len(qids)}({len(q2)}) | " + " | ".join(cells) + " |")
    if cov:
        mq = sorted(cov[PATHS[0]])
        L += ["", f"## Coverage@10 (multi_dataset {len(mq)}문항: 상위 10의 관련 데이터가 질문의 필요 종류를 몇 개 덮는지)", "",
              "| 질문 | 필요 종류 | " + " | ".join(PATHS) + " |", "|---|---|" + "---:|" * len(PATHS)]
        for q in mq:
            L.append(f"| {q} | {' / '.join(specs[q]['aspects'])} | " + " | ".join(
                f"{cov[p][q]['coverage@10']:.2f}" + (f" (빠짐: {', '.join(cov[p][q]['missing'])})" if cov[p][q]["missing"] else "")
                for p in PATHS) + " |")
        L.append("| 평균 | | " + " | ".join(f"{mean(cov[p][q]['coverage@10'] for q in mq):.2f}" for p in PATHS) + " |")
    L += ["", "## 판정·조건 (추천 문항, 상위 10 합계)", "",
          "| 경로 | 반환 | 상위10 칸 | judged@10 | 보류 | 완전 미판정 | 제외 대상 | 걸러진 불충족(필터 전 상위10) | 사본 병합 | 비공공 제외 |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for p in PATHS:
        s = [scores[p][q] for q in rec]
        L.append(f"| {p} | {sum(x['returned'] for x in s)} | {sum(x['top10'] for x in s)} | {mean(x['judged@10'] for x in s):.3f} | "
                 f"{sum(x['held@10'] for x in s)} | {sum(x['unjudged@10'] for x in s)} | {sum(x['must_exclude@10'] for x in s)} | "
                 f"{sum(x['unmet_in_unfiltered_top10'] for x in s)} | {sum(x['duplicates_collapsed'] for x in s)} | {sum(x['non_public_cut_in_top10'] for x in s)} |")
    L += ["", "조건 미확인·부분 (상위 10, 조건별 칸 수):", ""]
    for p in PATHS:
        unk, par = Counter(), Counter()
        for q in rec:
            unk.update(scores[p][q]["unknown@10"])
            par.update(scores[p][q]["partial@10"])
        L.append(f"- {p}: 미확인 {dict(unk) or '-'}, 부분 {dict(par) or '-'}")
    L += ["", "## 질문별 변화 (R@10 raw, 1점 이상; 기준 hg_question = 같은 원문 입력의 기존 검색)", ""]
    for p in ("dense", "bm25", "hybrid", "hg_terms"):
        up = [q for q in rec if scores[p][q]["raw"]["recall@10"] > scores["hg_question"][q]["raw"]["recall@10"] + 1e-9]
        down = [q for q in rec if scores[p][q]["raw"]["recall@10"] < scores["hg_question"][q]["raw"]["recall@10"] - 1e-9]
        L.append(f"- {p}: 개선 {len(up)} {up}, 악화 {len(down)} {down}, 같음 {len(rec) - len(up) - len(down)}")
    L += ["", "| 질문 | 유형 | " + " | ".join(PATHS) + " |", "|---|---|" + "---:|" * len(PATHS)]
    for q in rec:
        L.append(f"| {q} | {specs[q]['type']} | " + " | ".join(
            f"{scores[p][q]['raw']['recall@10']:.2f}" + (f" ({scores[p][q]['raw2']['recall@10']:.2f})" if 'raw2' in scores[p][q] else "") for p in PATHS) + " |")
    L += ["", "## 기권 문항 (지표 제외: 반환 수, 상위 10의 판정 데이터·보류·미판정)", "", "| 질문 | " + " | ".join(PATHS) + " |", "|---|" + "---|" * len(PATHS)]
    for q in abst:
        L.append(f"| {q} | " + " | ".join(f"{scores[p][q]['returned']} · {scores[p][q]['relevant_in_top10'] + scores[p][q]['must_exclude@10']} · "
                                         f"{scores[p][q]['held@10']} · {scores[p][q]['unjudged@10']}" for p in PATHS) + " |")
    L += ["", "## 지연 시간 (ms, 질문 임베딩 제외)", "", "| 경로 | p50 | p95 | p99 |", "|---|---:|---:|---:|"]
    for p in PATHS:
        lat = record["latency_ms"][p]
        L.append(f"| {p} | {lat['p50']:.1f} | {lat['p95']:.1f} | {lat['p99']:.1f} |")
    by_q = Counter(i["query_id"] for i in blind)
    L += ["", f"## 미판정 후보 (판정 자료 `unjudged_blind.jsonl`, 경로·순위 가림): {len(blind)}쌍, 질문 {len(by_q)}개", "",
          ", ".join(f"{q} {n}" for q, n in sorted(by_q.items())), ""]
    return "\n".join(L) + "\n"


def main():
    global LABELS, SPEC, COVERAGE
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dir", type=Path, required=True, help="a new run folder")
    parser.add_argument("--labels", type=Path, default=LABELS, help="label set to score against (default: v6)")
    parser.add_argument("--spec", type=Path, default=SPEC, help="type/condition spec (default: v1)")
    parser.add_argument("--rescore", type=Path, help="a saved run folder: score its rankings again instead of searching")
    parser.add_argument("--coverage", type=Path, help="coverage labels (covers per relevant multi_dataset pair) for Coverage@10")
    args = parser.parse_args()
    LABELS, SPEC = args.labels.resolve(), args.spec.resolve()
    COVERAGE = args.coverage.resolve() if args.coverage else None
    run(args.dir, args.rescore)


if __name__ == "__main__":
    main()
