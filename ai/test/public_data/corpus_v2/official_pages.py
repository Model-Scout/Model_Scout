"""The detail pages behind the API evidence (official_raw/*.page.gz, ~100 MB, not in git): pack, verify.

    python test/public_data/corpus_v2/official_pages.py pack <bundle.tar>   # bundle + official_pages_manifest.json
    python test/public_data/corpus_v2/official_pages.py verify [<bundle.tar>]

The manifest (in git) holds the bundle's sha256 and each page file's sha256. To restore, check the
bundle against the manifest and unpack it into data/public_catalog/official_raw/:

    tar -xf <bundle.tar> -C data/public_catalog/official_raw
    python test/public_data/corpus_v2/official_pages.py verify

verify checks every cached answer that cites a detail page (page_sha256 in official_meta.jsonl) against
the page on disk, the way 18_enrich reads it, and reports pages that are missing or differ.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path

AI = Path(__file__).resolve().parents[3]
MANIFEST = Path(__file__).resolve().parent / "official_pages_manifest.json"
sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("enrich18", AI / "18_enrich_public_datasets.py")
enrich = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enrich)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pack(bundle):
    bundle = Path(bundle)
    pages = sorted(enrich.RAW_DIR.glob("*.page.gz"))
    with tarfile.open(bundle, "w") as tar:  # pages are gzip already
        for p in pages:
            tar.add(p, arcname=p.name)
    MANIFEST.write_text(json.dumps({
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bundle": {"name": bundle.name, "sha256": sha(bundle), "bytes": bundle.stat().st_size},
        "parser_version": enrich.PARSER_VERSION,
        "pages": {p.name: sha(p) for p in pages},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(pages)} pages -> {bundle} ({bundle.stat().st_size / 1e6:.0f} MB), manifest {MANIFEST.name}")


def verify(bundle=None):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = []
    if bundle:
        if sha(bundle) != manifest["bundle"]["sha256"]:
            problems.append(f"{bundle} is not the bundle the manifest records")
    cited = [e for e in enrich.read_jsonl(enrich.CACHE) if e.get("page_sha256")]
    for e in cited:
        if enrich.load_page(e) is None:
            problems.append(f"{e['dataset_id']}: page missing or not the one its answer cites")
    for name, digest in manifest["pages"].items():
        path = enrich.RAW_DIR / name
        if path.exists() and sha(path) != digest:
            problems.append(f"{name}: differs from the manifest")
    print(f"{len(cited)} cited pages checked, {len(problems)} problems")
    for p in problems[:20]:
        print(" -", p)
    return problems


if __name__ == "__main__":
    command, *rest = sys.argv[1:] or ["verify"]
    if command == "pack":
        pack(rest[0])
    else:
        sys.exit(1 if verify(rest[0] if rest else None) else 0)
