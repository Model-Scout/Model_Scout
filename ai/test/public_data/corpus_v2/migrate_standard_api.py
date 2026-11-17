"""One-off: carry the cached official look-ups over the parser that confirms a standard dataset's
OpenAPI from its detail page (2026-11-16).

The change adds standard_api() and its pattern; parse_data_go_kr and parse_seoul are unchanged, so
every non-standard answer is what the new parser returns for the same page. Standard datasets need
their detail page, which was never fetched (the catalog JSON says nothing about an API), so:

- standard-data answers are dropped and looked up again (catalog + detail page, both kept);
- answers with a stored page are left to 18_enrich, which re-parses them;
- other answers accepted for the previous parser are carried as "compat" (not re-verified).

    python test/public_data/corpus_v2/migrate_standard_api.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

AI = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("enrich18", AI / "18_enrich_public_datasets.py")
enrich = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enrich)

MIGRATIONS = AI / "data" / "public_catalog" / "official_meta_migrations.json"
FROM_PARSER = "a66eb216459f"
BASIS = [
    "Adds standard_api() (an api.data.go.kr/openapi/tn_pubr_* address on a standard dataset's detail page) and its pattern.",
    "parse_data_go_kr and parse_seoul are unchanged: a non-standard answer is what the new parser returns for the same page.",
    "Standard-data answers are dropped and looked up again: their API evidence is on a page never fetched before.",
    "This is compatibility, not re-verification: no page was re-read for the carried answers.",
]


def main():
    rows = {r["dataset_id"]: r for r in enrich.read_jsonl(enrich.INPUT)}
    cache = {e["dataset_id"]: e for e in enrich.read_jsonl(enrich.CACHE)}
    accepted = lambda e: e.get("parser_version") == FROM_PARSER or (e.get("compat") or {}).get("accepted_for") == FROM_PARSER  # noqa: E731
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    basis_id = f"{FROM_PARSER}-to-{enrich.PARSER_VERSION}-standard-api"
    dropped, carried, stored = 0, 0, 0
    for k, e in list(cache.items()):
        if not accepted(e):
            continue
        if enrich.page_kind(rows.get(k) or {}) == "standard":
            del cache[k]
            dropped += 1
        elif enrich.load_raw(e) is not None:
            stored += 1  # re-parsed from its page by 18_enrich
        else:
            e["compat"] = {"basis_id": basis_id, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
                           "migrated_at": now, "previous": e.get("compat")}
            carried += 1
    enrich.write_cache(cache)
    record = json.loads(MIGRATIONS.read_text(encoding="utf-8")) if MIGRATIONS.exists() else []
    record = [r for r in record if r["basis_id"] != basis_id] + [{
        "basis_id": basis_id, "migrated_at": now, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
        "entries": carried, "dropped_for_lookup": {"standard": dropped}, "left_for_reparse": stored, "basis": BASIS,
    }]
    MIGRATIONS.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"basis_id": basis_id, "carried": carried, "dropped_standard": dropped, "left_for_reparse": stored}))


if __name__ == "__main__":
    main()
