"""One-off: carry the cached official look-ups over the 갱신주기 parser fix (2026-11-13).

The Seoul parser read an empty 갱신주기 cell as the text up to a later "분류" (80 rows, all starting
with "분류 "). The fix changes the cycle value only in that case; every other field and every
non-empty cycle parse the same way. So:

- answers whose cycle starts with "분류 " are dropped from the cache and looked up again (a real
  look-up with the fixed parser, page kept in official_raw/);
- every other answer accepted for the previous parser stays as it was and is accepted for the new
  one. It is still "compat", not re-verified: no page was re-read for it.

Evidence: saved Seoul pages are parsed with the old and the new pattern; they must agree except
where the old one starts with "분류 ".

    python test/public_data/corpus_v2/migrate_cycle_parser.py --evidence <dir> [<dir> ...]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
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
OLD_PATTERN = r"갱신주기 (.+?) 분류 "
FROM_PARSER = "0b08179a53cf"
BASIS = [
    "parse_seoul's cycle pattern changed from '갱신주기 (.+?) 분류 ' to '갱신주기 (.{0,60}?) ?분류 ' (empty -> None).",
    "The two differ only when the 갱신주기 cell is empty: the old one then starts its value with '분류 '. "
    "No other field or parser changed.",
    "Answers whose cycle starts with '분류 ' are dropped and looked up again; the rest keep their values.",
    "This is compatibility, not re-verification: no page was re-read for the carried answers.",
]


def broken(entry):
    return entry["dataset_id"].startswith("seoul_open_data/") and (entry.get("cycle") or "").startswith("분류 ")


def evidence(dirs):
    results = Counter()
    for directory in dirs:
        for path in sorted(Path(directory).glob("*data_seoul_go_kr_dataList_OA*datasetView*")):
            page = path.read_text(encoding="utf-8")
            try:
                new = enrich.parse_seoul(page).get("cycle")
            except (ConnectionError, ValueError):  # busy or table-less page: nothing to compare
                results["unreadable"] += 1
                continue
            old = enrich.first(OLD_PATTERN, enrich.plain_text(page))
            results["same" if old == new else "empty_cell" if (old or "").startswith("분류 ") and new is None else "differs"] += 1
    return dict(results)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--evidence", type=Path, nargs="*", default=[])
    args = parser.parse_args()
    found = evidence(args.evidence)
    if found.get("differs"):
        raise SystemExit(f"old and new patterns disagree beyond empty cells: {found}")

    cache = {e["dataset_id"]: e for e in enrich.read_jsonl(enrich.CACHE)}
    accepted = lambda e: e.get("parser_version") == FROM_PARSER or (e.get("compat") or {}).get("accepted_for") == FROM_PARSER  # noqa: E731
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    basis_id = f"{FROM_PARSER}-to-{enrich.PARSER_VERSION}-cycle"
    dropped = sorted(k for k, e in cache.items() if accepted(e) and broken(e))
    carried = 0
    for k, e in list(cache.items()):
        if k in dropped:
            del cache[k]
        elif accepted(e):
            e["compat"] = {"basis_id": basis_id, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
                           "migrated_at": now, "previous": e.get("compat")}
            carried += 1
    enrich.write_cache(cache)
    record = json.loads(MIGRATIONS.read_text(encoding="utf-8")) if MIGRATIONS.exists() else []
    record = [r for r in record if r["basis_id"] != basis_id] + [{
        "basis_id": basis_id, "migrated_at": now, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
        "entries": carried, "dropped_for_lookup": dropped, "basis": BASIS,
        "evidence": {"note": "saved Seoul official pages (2026-11-05..13), old vs new pattern", "summary": found},
    }]
    MIGRATIONS.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"basis_id": basis_id, "carried": carried, "dropped": len(dropped), "evidence": found}, ensure_ascii=False))


if __name__ == "__main__":
    main()
