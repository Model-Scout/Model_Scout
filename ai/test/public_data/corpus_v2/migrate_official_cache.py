"""One-off: record the 2026-11-08 official look-ups as compatible with the current parser.

Those look-ups ran before answers carried a parser version or kept their page, so they cannot be
re-parsed. This keeps each answer as it was (parser_version null = unversioned, the same
checked_at) and adds a compat record pointing at one documented basis. It is not a re-check:
official.verification reads "compat", and the 30-day age limit sends every one of them to a real
look-up by 2026-12-08. Answers that were not "ok" are dropped, so they are looked up again.

Evidence: pages saved during the earlier label investigation (fetched 2026-11-05..06, a few days
before the answers) are re-parsed with the current parser and compared with the cached answer.

    python test/public_data/corpus_v2/migrate_official_cache.py --original <cache backup> \
        --evidence <dir> [<dir> ...]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

AI = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("enrich18", AI / "18_enrich_public_datasets.py")
enrich = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enrich)

MIGRATIONS = AI / "data" / "public_catalog" / "official_meta_migrations.json"
BASIS = [
    "The answers were produced by the parser of 2026-11-08 before versioning (not recorded).",
    "The current parser differs from it only for pages without the dataset table or without a dataset "
    "name: those raise (busy / parse_error) instead of returning 'missing'. The branch that returns "
    "'ok' is the same code, so an 'ok' answer is what the current parser returns for the same page.",
    "'missing' answers are not migrated; one of them was the portal's busy page.",
    "This is compatibility, not re-verification: the pages were not kept, so nothing was re-parsed.",
]


def evidence_id(name):
    seoul = re.search(r"dataList_(OA_\d+)_A_1_datasetView", name)
    if seoul:
        return "seoul_open_data", "seoul_open_data/" + seoul.group(1).replace("_", "-")
    portal = re.search(r"catalog_(\d+)_(openapi|fileData|standard)_json", name)
    if portal:
        return "data_go_kr", f"data_go_kr/{portal.group(1)}"
    return None, None


def compare(original, dirs):
    results = []
    for directory in dirs:
        for path in sorted(Path(directory).iterdir()):
            source, dataset_id = evidence_id(path.name)
            entry = original.get(dataset_id)
            if not source or not entry or entry["status"] != "ok":
                continue
            try:
                meta = enrich.parse({"source": source}, path.read_text(encoding="utf-8"))
            except Exception as error:  # noqa: BLE001
                results.append({"dataset_id": dataset_id, "page": path.name, "result": type(error).__name__})
                continue
            differ = sorted(k for k in meta if k != "status" and meta.get(k) != entry.get(k))
            results.append({"dataset_id": dataset_id, "page": path.name, "result": "same" if not differ else "differs",
                            "fields": differ})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--original", type=Path, required=True, help="cache as written by the 2026-11-08 run")
    parser.add_argument("--evidence", type=Path, nargs="*", default=[])
    args = parser.parse_args()

    original = {e["dataset_id"]: e for e in map(json.loads, args.original.read_text(encoding="utf-8").splitlines()) if e}
    if any("parser_version" in e for e in original.values()):
        raise SystemExit("--original must be the unversioned cache written before this migration")
    current = {e["dataset_id"]: e for e in enrich.read_jsonl(enrich.CACHE)}
    # Answers really produced by the current parser since then are kept as they are.
    real = {k: e for k, e in current.items() if e.get("verification") in ("fetched", "reparsed")}

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    basis_id = f"unversioned-20261108-to-{enrich.PARSER_VERSION}"
    evidence = compare(original, args.evidence)
    migrated = {
        k: {**e, "parser_version": None,
            "compat": {"basis_id": basis_id, "from_parser": None, "accepted_for": enrich.PARSER_VERSION, "migrated_at": now}}
        for k, e in original.items()
        if e["status"] == "ok" and k not in real
    }
    excluded = Counter(e["status"] for k, e in original.items() if e["status"] != "ok")
    enrich.write_cache({**migrated, **real})
    record = json.loads(MIGRATIONS.read_text(encoding="utf-8")) if MIGRATIONS.exists() else []
    record = [r for r in record if r["basis_id"] != basis_id] + [{
        "basis_id": basis_id,
        "migrated_at": now,
        "from_parser": None,
        "accepted_for": enrich.PARSER_VERSION,
        "entries": len(migrated),
        "kept_real_answers": len(real),
        "excluded": dict(excluded),
        "recheck_due_by": "checked_at + 30 days (TTL_DAYS['ok'])",
        "basis": BASIS,
        "evidence": {
            "note": "pages fetched 2026-11-05..06, answers checked 2026-11-08; a difference can be a real page change",
            "summary": dict(Counter(r["result"] for r in evidence)),
            "pages": evidence,
        },
    }]
    MIGRATIONS.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"basis_id": basis_id, "migrated": len(migrated), "kept_real": len(real),
                      "excluded": dict(excluded), "evidence": dict(Counter(r["result"] for r in evidence))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
