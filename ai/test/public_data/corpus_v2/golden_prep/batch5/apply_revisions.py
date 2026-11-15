"""Apply revisions.jsonl (condition changes) to labels built by review_batch.py, and record it in the meta.

    python test/public_data/corpus_v2/golden_prep/batch5/apply_revisions.py <labels.jsonl>
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(path):
    path = Path(path)
    labels = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    built = hashlib.sha256(path.read_bytes()).hexdigest()
    revisions = [json.loads(l) for l in (HERE / "revisions.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    by_id = {l["query_id"]: l for l in labels}
    for r in revisions:
        section, key = r["field"].split(".")
        target = by_id[r["query_id"]][section]
        if target[key] != r["before"]:
            sys.exit(f"{r['query_id']} {r['field']} is {target[key]!r}, not {r['before']!r}: already applied or another base")
        target[key] = r["after"]
    path.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in labels), encoding="utf-8")
    meta_path = path.with_suffix(".meta.json")
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    meta["built_by_review_batch_sha256"] = built
    meta["revisions"] = {"path": "revisions.jsonl", "sha256": hashlib.sha256((HERE / "revisions.jsonl").read_bytes()).hexdigest(),
                         "applied": [f"{r['query_id']} {r['field']} {r['before']} -> {r['after']}" for r in revisions]}
    meta["labels_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(revisions)} revisions -> {path} (sha256 {meta['labels_sha256'][:16]})")


if __name__ == "__main__":
    main(sys.argv[1])
