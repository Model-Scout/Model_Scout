"""Stage D2: sample-length statistics for collected HF datasets.

Uses the Hugging Face dataset viewer statistics API (no data download). For each dataset
one split of the first config is measured: the longest string_text column becomes the
dataset's sample length, so input_length can be mapped without NER. Results are cached by
dataset sha; unsupported datasets are recorded with their reason and retried only when
the repo changes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from dotenv import load_dotenv

INPUT = Path("data/hf_datasets_stage1.jsonl")
OUTPUT = Path("data/hf_datasets_length_stats.jsonl")
VIEWER = "https://datasets-server.huggingface.co"
SPLIT_PREFERENCE = ("validation", "test", "train")
# Rough chars-per-token for current multilingual tokenizers; Korean packs far fewer chars per token.
CHARS_PER_TOKEN = {"ko": 1.5, "default": 4.0}
MAX_RETRIES = 4
# Encoded blobs and markup are string_text to the viewer but not prose a model reads as input.
NON_PROSE_RE = re.compile(r"base64|bytes|html|xml|metadata|test_cases|^(?:image|audio|url|path|id)$|_(?:id|url|path)$", re.I)
KO_CONFIG_RE = re.compile(r"(?:^|[._\-])(?:ko|kor|kor_hang|korean)(?:$|[._\-])", re.I)


def get_json(session, path, params):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = session.get(f"{VIEWER}/{path}", params=params, timeout=30)
        except requests.RequestException:
            # Dropped connections are transient; the "http_" reason makes the next run retry it.
            if attempt == MAX_RETRIES:
                return None, "http_network"
            time.sleep(5 * 2**attempt)
            continue
        if response.status_code == 429 or response.status_code >= 500:
            if attempt == MAX_RETRIES:
                return None, f"http_{response.status_code}"
            time.sleep(int(response.headers.get("Retry-After") or 5 * 2**attempt))
            continue
        if response.status_code != 200:
            # Viewer returns 4xx with an error body for unsupported/gated/too-large datasets.
            return None, (response.json().get("error", "") if response.headers.get("content-type", "").startswith("application/json") else "")[:200] or f"http_{response.status_code}"
        return response.json(), None
    return None, "retries_exhausted"


def histogram_quantile(histogram, q):
    """Approximate quantile from viewer histogram bins (counts per [edge_i, edge_i+1])."""
    counts, edges = histogram.get("hist") or [], histogram.get("bin_edges") or []
    total = sum(counts)
    if not total or len(edges) != len(counts) + 1:
        return None
    target, seen = q * total, 0
    for count, low, high in zip(counts, edges, edges[1:]):
        if seen + count >= target:
            return low + (high - low) * ((target - seen) / count if count else 0)
        seen += count
    return edges[-1]


def chars_per_token(languages):
    return CHARS_PER_TOKEN["ko"] if languages and set(languages) <= {"ko", "en"} and "ko" in languages else CHARS_PER_TOKEN["default"]


def measure(session, row):
    base = {"dataset_id": row["dataset_id"], "sha": row["sha"], "measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    splits, error = get_json(session, "splits", {"dataset": row["dataset_id"]})
    if error or not splits.get("splits"):
        return {**base, "status": "unsupported", "reason": error or "no_splits"}
    by_config: dict[str, list[str]] = {}
    for item in splits["splits"]:
        by_config.setdefault(item["config"], []).append(item["split"])
    # Multilingual datasets split languages into configs (wikipedia: 20231101.ko); measure the Korean one.
    config = next((c for c in by_config if KO_CONFIG_RE.search(c)), next(iter(by_config)))
    names = by_config[config]
    split = next((s for s in SPLIT_PREFERENCE if s in names), names[0])
    stats, error = get_json(session, "statistics", {"dataset": row["dataset_id"], "config": config, "split": split})
    if error:
        return {**base, "status": "unsupported", "reason": error, "config": config, "split": split}
    columns = [s for s in stats.get("statistics", []) if s["column_type"] == "string_text"
               and not NON_PROSE_RE.search(s["column_name"])]
    if not columns:
        return {**base, "status": "no_text_column", "config": config, "split": split,
                "column_types": sorted({s["column_type"] for s in stats.get("statistics", [])})}
    longest = max(columns, key=lambda s: s["column_statistics"].get("median") or 0)
    col = longest["column_statistics"]
    p90 = histogram_quantile(col.get("histogram") or {}, 0.9)
    ratio = chars_per_token(row.get("languages"))
    return {
        **base,
        "status": "ok",
        "config": config,
        "split": split,
        "num_examples": stats.get("num_examples"),
        "partial": stats.get("partial"),
        "text_column": longest["column_name"],
        "chars": {k: col.get(k) for k in ("min", "median", "mean", "max")} | {"p90": round(p90) if p90 is not None else None},
        "chars_per_token": ratio,
        "tokens_p90_estimate": round((p90 if p90 is not None else col.get("max") or 0) / ratio),
        "text_columns": [s["column_name"] for s in columns],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    load_dotenv(".env")
    session = requests.Session()
    if token := os.getenv("HF_TOKEN"):
        session.headers["Authorization"] = f"Bearer {token}"
    rows = [json.loads(line) for line in open(INPUT, encoding="utf-8")][: args.limit]
    cached = {}
    if OUTPUT.exists():
        cached = {r["dataset_id"]: r for r in map(json.loads, open(OUTPUT, encoding="utf-8"))}
    def stale(r):
        old = cached.get(r["dataset_id"])
        return (not old or old["sha"] != r["sha"]
                or old["status"] == "unsupported" and old["reason"].startswith("http_")
                or old["status"] == "ok" and bool(NON_PROSE_RE.search(old["text_column"])))
    todo = [r for r in rows if stale(r)]
    print(f"[LENGTH] {len(rows)} datasets, {len(rows) - len(todo)} cached, measuring {len(todo)}", flush=True)

    results = {r["dataset_id"]: cached[r["dataset_id"]] for r in rows if r["dataset_id"] in cached}
    # Append each result as it lands so a crash keeps finished work; the cache read keeps the last row per id.
    with ThreadPoolExecutor(args.workers) as pool, open(OUTPUT, "a", encoding="utf-8") as log:
        futures = [pool.submit(measure, session, r) for r in todo]
        for done, future in enumerate(as_completed(futures), 1):
            result = future.result()
            results[result["dataset_id"]] = result
            log.write(json.dumps(result, ensure_ascii=False) + "\n")
            log.flush()
            if done % 100 == 0:
                print(f"[LENGTH] {done}/{len(todo)}", flush=True)

    temp = OUTPUT.with_suffix(".jsonl.tmp")
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(results[r["dataset_id"]], ensure_ascii=False) + "\n" for r in rows if r["dataset_id"] in results)
    os.replace(temp, OUTPUT)
    status: dict[str, int] = {}
    for r in results.values():
        status[r["status"]] = status.get(r["status"], 0) + 1
    print(json.dumps(status), f"-> {OUTPUT}")


def self_check():
    hist = {"hist": [10, 80, 10], "bin_edges": [0, 100, 200, 300]}
    assert histogram_quantile(hist, 0.5) == 150
    assert histogram_quantile(hist, 0.9) == 200
    assert histogram_quantile({"hist": [], "bin_edges": []}, 0.9) is None
    assert chars_per_token(["ko"]) == 1.5 and chars_per_token(["ko", "en"]) == 1.5
    assert chars_per_token(["ko", "en", "ja"]) == 4.0 and chars_per_token([]) == 4.0
    assert KO_CONFIG_RE.search("20231101.ko") and KO_CONFIG_RE.search("kor_Hang") and KO_CONFIG_RE.search("en-ko")
    assert NON_PROSE_RE.search("image_base64") and NON_PROSE_RE.search("mhtml") and NON_PROSE_RE.search("doc_id")
    assert not NON_PROSE_RE.search("text") and not NON_PROSE_RE.search("context") and not NON_PROSE_RE.search("question")
    assert not KO_CONFIG_RE.search("kok") and not KO_CONFIG_RE.search("kong")
    print("12_collect_dataset_length_stats ok")


if __name__ == "__main__":
    main()
