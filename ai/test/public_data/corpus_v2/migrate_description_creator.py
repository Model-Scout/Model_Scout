"""One-off: carry the cached official look-ups over the parser that also reads the Seoul page
description and the data.go.kr catalog creator (2026-11-13).

The change only adds two answer fields; every existing field is extracted by unchanged code.
Answers without a stored page cannot gain the new fields without a fetch, so:

- Seoul answers are dropped and looked up again: the page description (coordinate system, data
  delay, …) exists only there;
- data.go.kr standard-data answers are dropped and looked up again: their collected organisation
  is the portal operator, the catalog creator is the responsible agency;
- other data.go.kr answers are carried as "compat" (not re-verified); their organisation stays the
  collected value until a real look-up;
- answers with a stored page are left alone: 18_enrich re-parses them from the page.

    python test/public_data/corpus_v2/migrate_description_creator.py
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
FROM_PARSER = "cbfa23732988"
BASIS = [
    "parse_seoul adds 'description' (the page's meta description); parse_data_go_kr adds 'creator' (catalog creator.name).",
    "No existing answer field changed: the code producing them is the same.",
    "Seoul and standard-data answers are dropped and looked up again to obtain the new fields.",
    "Other answers are carried as compatibility, not re-verification; they have no description/creator until a real look-up.",
]


def main():
    rows = {r["dataset_id"]: r for r in enrich.read_jsonl(enrich.INPUT)}
    cache = {e["dataset_id"]: e for e in enrich.read_jsonl(enrich.CACHE)}
    accepted = lambda e: e.get("parser_version") == FROM_PARSER or (e.get("compat") or {}).get("accepted_for") == FROM_PARSER  # noqa: E731
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    basis_id = f"{FROM_PARSER}-to-{enrich.PARSER_VERSION}-description-creator"
    dropped, carried, stored = {"seoul": 0, "standard": 0}, 0, 0
    for k, e in list(cache.items()):
        if not accepted(e):
            continue
        if enrich.load_raw(e) is not None:
            stored += 1  # re-parsed from its page by 18_enrich
            continue
        row = rows.get(k) or {}
        if k.startswith("seoul_open_data/"):
            del cache[k]
            dropped["seoul"] += 1
        elif enrich.page_kind(row) == "standard":
            del cache[k]
            dropped["standard"] += 1
        else:
            e["compat"] = {"basis_id": basis_id, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
                           "migrated_at": now, "previous": e.get("compat")}
            carried += 1
    enrich.write_cache(cache)
    record = json.loads(MIGRATIONS.read_text(encoding="utf-8")) if MIGRATIONS.exists() else []
    record = [r for r in record if r["basis_id"] != basis_id] + [{
        "basis_id": basis_id, "migrated_at": now, "from_parser": FROM_PARSER, "accepted_for": enrich.PARSER_VERSION,
        "entries": carried, "dropped_for_lookup": dropped, "left_for_reparse": stored, "basis": BASIS,
    }]
    MIGRATIONS.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"basis_id": basis_id, "carried": carried, "dropped": dropped, "left_for_reparse": stored}, ensure_ascii=False))


if __name__ == "__main__":
    main()
