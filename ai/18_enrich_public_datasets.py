"""Stage D1c (corpus v2 only): fill license, delivery and update cycle from each dataset's official page.

18_collect_public_datasets.py leaves gaps that this stage closes without touching its output, so
corpus v1 and dataset-refresh.yml keep reading the collector's file unchanged:

  license   data.go.kr rows were looked up as fileData even when the page is an OpenAPI or standard
            data page (blank), and failed lookups were cached as "no license" for good (Seoul 595).
  delivery  Seoul was always ["api"] although many pages offer a Sheet/CSV download or files;
            standard data was always ["csv", "api"].
  cycle     the portal's update cycle was not kept. It is shown as the portal's wording only: the
            portal labels daily or yearly data "실시간" too, so it is never treated as realtime.

  data.go.kr        https://www.data.go.kr/catalog/<id>/<openapi|fileData|standard>.json (JSON-LD)
  seoul_open_data   https://data.seoul.go.kr/dataList/<id>/A/1/datasetView.do (HTML)

A look-up is reused only while the collected row (sha), the parser (PARSER_VERSION) and its age
(TTL_DAYS by status) all still match; anything else is looked up again. Only answers are cached:
"ok", and "deleted" when data.go.kr says the dataset no longer exists (Seoul has no such notice;
its datasets leave the catalog list instead). A failed look-up never erases what was confirmed
before: the row keeps those values with their checked_at, records the failure in official.recheck,
and is flagged for review when the row or the parser changed since that confirmation.

  official.status   ok | deleted                          confirmed at official.checked_at
                    failed | parse_error | no_page | unchecked   never confirmed, collected values kept
  official.recheck  None, or why the latest look-up failed while an older confirmation is in use
  official.verification   how the answer in use relates to the current parser:
                    fetched   parsed by it when the page was fetched
                    reparsed  re-parsed by it from the stored page after a parser change (no fetch)
                    compat    an older parser's answer accepted without re-parsing; the basis is in
                              official_meta_migrations.json and the age limit still applies, so a
                              real re-check follows

Each confirmed answer keeps the page it was parsed from (official_raw/, gzip), so a parser change
is applied by re-parsing stored pages instead of fetching every page again.

Outputs: data/public_enriched/public_datasets.jsonl, build_manifest.json
Cache:   data/public_catalog/official_meta.jsonl, official_raw/, official_meta_migrations.json
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import importlib.util
import inspect
import json
import re
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from corpus_manifest import write_manifest

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
INPUT = DATA_DIR / "public_datasets_stage1.jsonl"
OUT_DIR = DATA_DIR / "public_enriched"
OUTPUT = OUT_DIR / "public_datasets.jsonl"
CACHE = DATA_DIR / "public_catalog" / "official_meta.jsonl"
RAW_DIR = DATA_DIR / "public_catalog" / "official_raw"
# Cache fields that describe the look-up; everything else in an entry is the parsed answer.
ENTRY_KEYS = {"dataset_id", "row_sha", "parser_version", "checked_at", "raw_sha256", "verification",
              "reparsed_at", "reparsed_from", "reparse_changed", "compat"}
COLLECTOR = AI_DIR / "18_collect_public_datasets.py"
USER_AGENT = "Mozilla/5.0 (compatible; model-scout-public-data)"
MAX_RETRIES = 3

_spec = importlib.util.spec_from_file_location("collect18", COLLECTOR)
collect18 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(collect18)

PAGE_KIND_RE = re.compile(r"data\.go\.kr/data/(\d+)/(openapi|fileData|standard)\.do")
SEOUL_TAB_RE = re.compile(r"dataSetView\('[^']*'\s*,\s*'([A-Z])'")
SEOUL_FILE_RE = re.compile(r"downloadFile\('\d+'\);\">([^<]+)</span>")
# The portal answers 200 with this page when it is overloaded ("서비스 지연이 발생하고 있습니다").
SEOUL_BUSY_RE = re.compile(r"서비스 지연이 발생|다시 시도하여 주십시오|이용에 불편을 드려")
API_DELIVERY = {"REST", "SOAP", "LINK"}
# Formats the taxonomy maps (data_format); anything else on a page is not a model-readable file.
FILE_FORMATS = {"csv", "xlsx", "xls", "json", "xml", "txt", "shp", "geojson"}
CONFIRMED = {"ok", "deleted"}
# ponytail: fixed re-check ages; tune per portal if pages change faster than this.
TTL_DAYS = {"ok": 30, "deleted": 7}


def plain_text(page):
    page = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", page)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", page)))


def first(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


def official_license(text):
    """Official license wording -> taxonomy alias; None when there is no wording or it is unknown."""
    if not text:
        return None
    if re.search(r"제한\s*없음", text):  # "이용허락범위 제한 없음", Seoul's "이용제한없음 : 자유이용"
        return "이용허락범위 제한 없음"
    kogl = collect18.kogl_license(text)
    if kogl in ("공공누리 제2유형", "공공누리 제4유형"):  # non-commercial wins over anything else stated
        return kogl
    if re.search(r"비영리|상업적 이용\s*금지", text):  # e.g. third-party works under BY-NC terms
        return "비영리 조건(제3자 권리 포함)"
    # Third-party works inside a free or type 1/3 grant need their own permission: check the original.
    if re.search(r"제\s*0\s*유형", text):
        return "공공누리 제0유형"
    if kogl and "제3자 권리" in text:
        return f"{kogl}(제3자 권리 포함)"
    return kogl


def catalog_url(row):
    match = PAGE_KIND_RE.search(row.get("url") or "")
    return f"https://www.data.go.kr/catalog/{match.group(1)}/{match.group(2)}.json" if match else None


def page_kind(row):
    match = PAGE_KIND_RE.search(row.get("url") or "")
    return match.group(2) if match else None


def parse_data_go_kr(text):
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("catalog is not a JSON-LD object")
    if not data.get("name"):
        if "존재하지 않습니다" in (data.get("description") or ""):  # the portal's own deletion notice
            return {"status": "deleted"}
        raise ValueError("catalog without a dataset name")
    props = {p.get("name"): p.get("value") for p in data.get("additionalProperty") or []}
    return {
        "status": "ok",
        "license_text": (data.get("license") or {}).get("name"),
        "encoding": data.get("encodingFormat"),
        "delivery": props.get("제공형태"),
        "cycle": props.get("업데이트 주기"),
        "modified": data.get("dateModified"),
    }


def parse_seoul(page):
    text = plain_text(page)
    if "이용허락범위" not in text:  # the busy marker is only trusted when the dataset table is absent
        if SEOUL_BUSY_RE.search(text):
            raise ConnectionError("seoul portal busy page")
        raise ValueError("seoul page without the dataset table")
    return {
        "status": "ok",
        "license_text": first(r"이용허락범위 (?:--> )?(.{3,60}?) (?:AI유형|메타정보|관련 태그)", text),
        "tabs": sorted(set(SEOUL_TAB_RE.findall(page))),
        "files": sorted({name.strip() for name in SEOUL_FILE_RE.findall(page)}),
        "cycle": first(r"갱신주기 (.+?) 분류 ", text),
        "modified": first(r"데이터 갱신일 ([\d.]+)", text),
    }


# Changes whenever the parsing code changes, so results of an older parser are looked up again.
PARSER_VERSION = hashlib.sha256(
    "".join(inspect.getsource(f) for f in (plain_text, first, parse_data_go_kr, parse_seoul)).encode("utf-8")
    + "".join(r.pattern for r in (SEOUL_TAB_RE, SEOUL_FILE_RE, SEOUL_BUSY_RE)).encode("utf-8")
).hexdigest()[:12]


def parser_accepted(entry):
    """The answer counts as the current parser's: parsed by it, or accepted for it by a migration."""
    return entry.get("parser_version") == PARSER_VERSION or (entry.get("compat") or {}).get("accepted_for") == PARSER_VERSION


def verification(entry):
    if entry.get("parser_version") == PARSER_VERSION:
        return entry.get("verification") or "fetched"
    return "compat" if parser_accepted(entry) else "older_parser"


def raw_path(dataset_id):
    return RAW_DIR / (re.sub(r"[^0-9A-Za-z_-]", "_", dataset_id) + ".gz")


def save_raw(dataset_id, page):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_path(dataset_id).write_bytes(gzip.compress(page.encode("utf-8")))
    return hashlib.sha256(page.encode("utf-8")).hexdigest()


def load_raw(entry):
    """The page this answer was parsed from; None when it was not kept or has been replaced."""
    path = raw_path(entry["dataset_id"])
    if not entry.get("raw_sha256") or not path.exists():
        return None
    page = gzip.decompress(path.read_bytes()).decode("utf-8")
    return page if hashlib.sha256(page.encode("utf-8")).hexdigest() == entry["raw_sha256"] else None


def parse(row, page):
    return parse_seoul(page) if row["source"] == "seoul_open_data" else parse_data_go_kr(page)


def answer(entry):
    return {k: v for k, v in entry.items() if k not in ENTRY_KEYS}


def reparse(entry, row, now):
    """The stored page run through the current parser; None when there is no page or no answer.

    The page is the one fetched at checked_at, so the answer keeps that time and its age limit.
    """
    page = load_raw(entry)
    if page is None:
        return None
    try:
        meta = parse(row, page)
    except Exception:  # noqa: BLE001 - this page needs a real look-up
        return None
    if meta["status"] not in CONFIRMED:
        return None
    old = answer(entry)
    return {
        **{k: entry[k] for k in ("dataset_id", "row_sha", "checked_at", "raw_sha256")},
        "parser_version": PARSER_VERSION,
        **meta,
        "verification": "reparsed",
        "reparsed_from": entry.get("parser_version"),
        "reparsed_at": now.isoformat(timespec="seconds"),
        "reparse_changed": sorted(k for k in set(old) | set(meta) if old.get(k) != meta.get(k)),
    }


def official_formats(row, meta):
    """Delivery the official page shows; the collected value when the page was not read."""
    if row["source"] == "data_go_kr" and page_kind(row) == "openapi":
        return ["api"]  # the URL already says so; the encoding is the response format, not a file
    if meta.get("status") != "ok":
        return row.get("formats") or []
    if row["source"] == "seoul_open_data":
        formats = {"api"}  # every Seoul row comes from the OpenAPI catalog
        if "S" in meta["tabs"]:  # the Sheet tab downloads the whole table as CSV
            formats.add("csv")
        formats |= {name.rsplit(".", 1)[-1].lower() for name in meta["files"] if "." in name} & FILE_FORMATS
        return sorted(formats)
    kind = page_kind(row)
    encoding = set(re.split(r"[+,/\s]+", (meta.get("encoding") or "").lower())) & FILE_FORMATS
    api = {"api"} if meta.get("delivery") in API_DELIVERY else set()
    # A standard dataset that states no format stays unknown instead of the old ["csv", "api"].
    return sorted(encoding | api) or (row.get("formats") or [] if kind == "fileData" else [])


def enrich_row(row, meta, recheck=None, review=()):
    """The collected row with official facts; the collected value stays wherever the page is silent.

    meta is the confirmed look-up in use, or only a failure status; recheck says why the latest
    look-up failed while meta is an older confirmation; review says why that confirmation is in doubt.
    """
    out = dict(row)
    status = meta.get("status", "unchecked")
    out["formats"] = official_formats(row, meta)
    if status == "ok" and meta.get("license_text"):
        mapped = official_license(meta["license_text"])
        out["licenses"] = [mapped] if mapped else []
    if row["source"] == "data_go_kr" and page_kind(row):
        out["list_type"] = "openapi" if page_kind(row) == "openapi" else "file"
    out["update_cycle"] = meta.get("cycle") if status == "ok" else None
    out["official"] = {
        "status": status,
        "checked_at": meta.get("checked_at") if status in CONFIRMED else None,
        "parser_version": meta.get("parser_version") if status in CONFIRMED else None,
        "verification": verification(meta) if status in CONFIRMED else None,
        "recheck": recheck,
        "needs_review": bool(review),
        "review_reasons": list(review),
        "license_text": meta.get("license_text") if status == "ok" else None,
        "modified": meta.get("modified") if status == "ok" else None,
    }
    return out


def fetch(session, url):
    import requests

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = session.get(url, timeout=60, headers={"User-Agent": USER_AGENT})
            if response.status_code == 429 or response.status_code >= 500:
                raise requests.HTTPError(f"http_{response.status_code}")
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            if attempt == MAX_RETRIES:
                raise
            time.sleep(3 * 2**attempt)


def lookup(session, row):
    """Parsed official facts; a failure comes back as a status and is never cached.

    failed       the page could not be fetched (network, HTTP error, the portal's busy page)
    parse_error  a page came back, but not in a shape this parser knows
    no_page      the row has no official page address
    """
    url = row.get("url") if row["source"] == "seoul_open_data" else catalog_url(row)
    if not url:
        return {"status": "no_page"}
    try:
        page = fetch(session, url)
    except Exception:  # noqa: BLE001
        return {"status": "failed"}
    try:
        meta = parse(row, page)
    except ConnectionError:
        return {"status": "failed"}
    except Exception:  # noqa: BLE001
        return {"status": "parse_error"}
    # Keep the page behind every answer, so a later parser change can re-parse it locally.
    return {**meta, "raw_sha256": save_raw(row["dataset_id"], page)}


def is_fresh(entry, row, now):
    """A cached answer still stands for this collected row, parser and day."""
    if not entry or entry.get("row_sha") != row.get("sha") or not parser_accepted(entry):
        return False
    return (now - datetime.fromisoformat(entry["checked_at"])).days < TTL_DAYS.get(entry.get("status"), 0)


def resolve(row, entry, attempt, now, offline):
    """(meta in use, recheck failure, review reasons) for one row after this run's look-ups."""
    attempt_failed = bool(attempt) and attempt["status"] not in CONFIRMED
    if is_fresh(entry, row, now) and not attempt_failed:
        return entry, None, ()
    failure = attempt["status"] if attempt_failed else "unchecked" if offline or not attempt else "failed"
    if not entry:
        return {"status": failure}, None, ()
    review = []
    if entry.get("row_sha") != row.get("sha"):
        review.append("row_changed_since_check")
    if not parser_accepted(entry):
        review.append("parser_changed_since_check")
    return entry, failure, tuple(review)


def write_cache(cache):
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cache.values()), encoding="utf-8")


def read_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="use cached look-ups only")
    parser.add_argument("--refresh", action="store_true", help="look every row up again (confirmed values are kept on failure)")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    rows = read_jsonl(INPUT)
    if not rows:
        raise SystemExit(f"run 18_collect_public_datasets.py first ({INPUT} is empty)")
    # Only answers count; anything else in the file (an older format's "missing") is looked up again.
    cache = {c["dataset_id"]: c for c in read_jsonl(CACHE) if c.get("status") in CONFIRMED}
    now = datetime.now(timezone.utc)
    reparsed = 0
    for row in rows:  # a parser change is applied to stored pages first, without fetching
        entry = cache.get(row["dataset_id"])
        if entry and entry.get("row_sha") == row.get("sha") and not parser_accepted(entry):
            fresh = reparse(entry, row, now)
            if fresh:
                cache[row["dataset_id"]], reparsed = fresh, reparsed + 1
    todo = [r for r in rows if args.refresh or not is_fresh(cache.get(r["dataset_id"]), r, now)]
    print(f"[enrich] rows {len(rows)}, re-parsed {reparsed}, fresh {len(rows) - len(todo)}, to look up {len(todo)}", flush=True)
    if reparsed:
        write_cache(cache)
    attempts = {}
    if todo and not args.offline:
        import requests

        session = requests.Session()
        checked = now.isoformat(timespec="seconds")
        with ThreadPoolExecutor(args.workers) as pool:
            for row, meta in zip(todo, pool.map(lambda r: lookup(session, r), todo), strict=True):
                attempts[row["dataset_id"]] = meta
                if meta["status"] in CONFIRMED:
                    cache[row["dataset_id"]] = {
                        "dataset_id": row["dataset_id"],
                        "row_sha": row.get("sha"),
                        "parser_version": PARSER_VERSION,
                        "checked_at": checked,
                        "verification": "fetched",
                        **meta,
                    }
        write_cache(cache)

    enriched = [
        enrich_row(row, *resolve(row, cache.get(row["dataset_id"]), attempts.get(row["dataset_id"]), now, args.offline))
        for row in rows
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in enriched), encoding="utf-8")
    counts = {
        "rows": len(enriched),
        "status": Counter(f"{r['source']}:{r['official']['status']}" for r in enriched),
        "recheck_failed": Counter(r["official"]["recheck"] for r in enriched if r["official"]["recheck"]),
        "needs_review": sum(r["official"]["needs_review"] for r in enriched),
        "verification": Counter(r["official"]["verification"] for r in enriched if r["official"]["verification"]),
        "reparsed_this_run": reparsed,
        "parser_version": PARSER_VERSION,
        "licensed_before": sum(bool(r.get("licenses")) for r in rows),
        "licensed_after": sum(bool(r.get("licenses")) for r in enriched),
        "formats_changed": sum(a.get("formats") != b.get("formats") for a, b in zip(rows, enriched, strict=True)),
        "with_update_cycle": sum(bool(r.get("update_cycle")) for r in enriched),
    }
    manifest = write_manifest(
        OUT_DIR,
        stage="enrich",
        corpus="v2",
        options={"offline": args.offline},
        inputs=[INPUT],
        code=[Path(__file__), COLLECTOR, AI_DIR / "corpus_manifest.py"],
        outputs=[OUTPUT],
        counts=counts,
    )
    print(json.dumps(counts, ensure_ascii=False))
    print(f"enrich_id {manifest['stage_id']}")


if __name__ == "__main__":
    main()
