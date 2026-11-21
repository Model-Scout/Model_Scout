"""batch6 cards: pilot 1's unjudged pairs (runs/2026-11-16_pilot1/unjudged_blind.jsonl) with full facts and
golden_prep's automatic checks, in the batch5 format review_batch.py validates.

    python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_items.py
    # a later round: other blind pairs, other base labels, another batch folder
    python -X utf8 .../batch6/make_items.py --blind <unjudged_blind.jsonl> --labels <base labels> --out <batch folder>
"""

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parents[2]
sys.path[:0] = [str(PUBLIC / "retrieval"), str(PUBLIC / "corpus_v2")]

import golden_prep as gp  # noqa: E402
import pilot  # noqa: E402

BLIND = PUBLIC / "retrieval" / "runs" / "2026-11-16_pilot1" / "unjudged_blind.jsonl"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--blind", type=Path, default=BLIND)
    parser.add_argument("--labels", type=Path, default=pilot.LABELS, help="labels the questions and conditions come from")
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    pilot.hs.use_corpus("v2")  # the frozen corpus the pilot ranked; v1 has no coverage facts
    queries = {q["query_id"]: q for q in gp.read_jsonl(gp.QUERIES)}
    labels = {lb["query_id"]: lb for lb in gp.read_jsonl(args.labels)}
    conditions = pilot.Conditions()
    items, suggestions = [], []
    for pair in gp.read_jsonl(args.blind):
        qid, did = pair["query_id"], pair["dataset_id"]
        lb = labels[qid]
        q = queries.get(qid) or lb  # a holdout question carries its aspects in the labels file
        query = {"query": lb["query"], "conditions": lb["conditions"], "aspects": q["aspects"],
                 "expected_behavior": lb["expected_behavior"]}
        f = conditions.facts(did)
        rid = f"{qid}|{did}"
        items.append({"review_id": rid, "query_id": qid, "query": lb["query"], "query_type": lb["query_type"],
                      "expected_behavior": lb["expected_behavior"], "dataset_id": did, "conditions": lb["conditions"],
                      "aspects": q["aspects"], "facts": f})
        suggestions.append({"review_id": rid, **gp.suggestion(query, f)})
    args.out.mkdir(parents=True, exist_ok=True)
    gp.write_jsonl(args.out / "items.jsonl", items)
    gp.write_jsonl(args.out / "review_suggestions.jsonl", suggestions)
    print(f"{len(items)} items -> {args.out / 'items.jsonl'}")


if __name__ == "__main__":
    main()
