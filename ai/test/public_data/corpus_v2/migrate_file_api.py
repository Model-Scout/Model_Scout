"""One-off: carry the cached official look-ups over the parser that reads a file dataset's
auto-converted OpenAPI from its detail page (2026-11-16).

The change adds file_api() / detail_api() and FILE_API_RE; parse_data_go_kr, parse_seoul and
standard_api are unchanged, so every catalog answer is what the new parser returns for the same page.
Nothing is dropped:

- answers with a stored page are left to 18_enrich, which re-parses them (standard data with its
  detail page gets its API evidence again from that page);
- other answers accepted for the previous parser are carried as "compat" (not re-verified);
- a file dataset's answer is kept as it is and only its detail page is read (18_enrich needs_page),
  so its catalog values are not looked up again.

    python test/public_data/corpus_v2/migrate_file_api.py
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
FROM_PARSER = "93147dea4dd7"
BASIS = [
    "Adds file_api() (an infuser.odcloud.kr/oas/docs?namespace=<the dataset's number> address on a file dataset's "
    "detail page), detail_api() and FILE_API_RE.",
    "parse_data_go_kr, parse_seoul and standard_api are unchanged: a catalog answer is what the new parser returns.",
    "File-dataset answers keep their catalog values; only their detail page is read for the API evidence.",
    "This is compatibility, not re-verification: no catalog page was re-read for the carried answers.",
]


def main():
    cache = {e["dataset_id"]: e for e in enrich.read_jsonl(enrich.CACHE)}
    accepted = lambda e: e.get("parser_version") == FROM_PARSER or (e.get("compat") or {}).get("accepted_for") == FROM_PARSER  # noqa: E731
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    basis_id = f"{FROM_PARSER}-to-{enrich.PARSER_VERSION}-file-api"
    carried, stored = 0, 0
    for e in cache.values():
        if not accepted(e):
            continue
        if enrich.load_raw(e) is not None:
            stored += 1  # re-parsed from its page by 18_enrich
        else:
            e["compat"] = {"basis_id": basis_id, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
                           "migrated_at": now, "previous": e.get("compat")}
            carried += 1
    enrich.write_cache(cache)
    record = json.loads(MIGRATIONS.read_text(encoding="utf-8")) if MIGRATIONS.exists() else []
    record = [r for r in record if r["basis_id"] != basis_id] + [{
        "basis_id": basis_id, "migrated_at": now, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
        "entries": carried, "dropped_for_lookup": {}, "left_for_reparse": stored, "basis": BASIS,
    }]
    MIGRATIONS.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"basis_id": basis_id, "carried": carried, "left_for_reparse": stored}))


if __name__ == "__main__":
    main()
