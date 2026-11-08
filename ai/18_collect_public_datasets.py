"""Stage D1b: collect Korean public-data cards (서울 열린데이터광장, 공공데이터포털).

Both portals publish a catalog API, so the whole catalog is cached once and filtered
locally; only the selected datasets cost per-item calls (field schema, license).

  seoul_open_data   SearchOpenAPIService (catalog, ~5.9K OpenAPIs) + SearchOpenAPIIOValueService
                    (output fields) + the dataset page for its 공공누리 type (the catalog has none).
                    All ~5.9K APIs; district and translated editions are grouped later, not dropped.
  data_go_kr        목록조회서비스 15077093 (/dataset ~100K files, /open-data-list ~17K APIs,
                    /standard-data-list) + per-dataset catalog JSON-LD for the 공공누리 license.
                    Selected by quality the portal itself certifies, not by popularity:
                      A  국가중점데이터 OpenAPIs (government-designated high-value data)
                      B  OpenAPIs of ministries / agencies / 광역시도 with production auto-approval
                         (an app can call them today)
                      C  machine-readable files of the same publishers: every 표준데이터 (one
                         national schema merging all regions), then up to FILE_CAP_PER_CATEGORY
                         per category, year editions merged
                    시군구 copies of the same data are not loaded as datasets; they are listed on
                    the national/standard dataset they repeat (regional_variants).

Rows use the HF stage-1 schema (dataset_id, tags, formats, licenses, readme_path, ...) so
13/14/15 treat them like any dataset. The generated README (description + fields) is the
card text that chunking, embedding, and the wiki read.

Outputs: data/public_datasets_stage1.jsonl, data/public_catalog/*.jsonl (raw catalog cache),
data/readmes/public/<source>__<id>.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
OUTPUT = DATA_DIR / "public_datasets_stage1.jsonl"
CATALOG_DIR = DATA_DIR / "public_catalog"
README_DIR = DATA_DIR / "readmes" / "public"
SEOUL_API = "http://openapi.seoul.go.kr:8088"
SEOUL_CITY_HOST = "openapi.seoul.go.kr"
DATA_GO_KR_API = "https://api.odcloud.kr/api/15077093/v1"
PAGE_SIZE = 1000
MAX_RETRIES = 4
# ponytail: views only order files inside one category (the portal has no other usefulness signal
# for files); raise the cap when a demo domain comes up thin and the Supabase budget allows.
FILE_CAP_PER_CATEGORY = 300
MAX_REGIONAL_VARIANTS = 30
MIN_DESCRIPTION_CHARS = 150
# Seoul field lists (--renew-fields): the catalog has no column-change date, so a list is renewed when
# its catalog row changes, and every list at least this often, a bounded number per run.
FIELD_MAX_AGE_DAYS = 30
FIELD_RENEW_PER_RUN = 300
# Catalog keys that move without the API changing; they must not count as a change.
VOLATILE_KEY_RE = re.compile(r"CNT|COUNT|HIT|VIEW|DOWN|RANK", re.I)
# File types a model pipeline can read; images, hwp-only notices and zip bundles are skipped.
USABLE_EXTENSIONS = {"csv", "json", "xml", "json+xml", "xlsx", "xls", "shp", "geojson", "txt"}
PROVINCES = (
    "서울특별시",
    "부산광역시",
    "대구광역시",
    "인천광역시",
    "광주광역시",
    "대전광역시",
    "울산광역시",
    "세종특별자치시",
    "경기도",
    "강원특별자치도",
    "강원도",
    "충청북도",
    "충청남도",
    "전북특별자치도",
    "전라북도",
    "전라남도",
    "경상북도",
    "경상남도",
    "제주특별자치도",
)
REGION_PREFIX_RE = re.compile(
    r"^(?:[가-힣]+(?:특별시|광역시|특별자치시|특별자치도|도)[_\s]*)?(?:[가-힣]+(?:시|군|구)[_\s]+)?"
)
EDITION_RE = re.compile(r"_?\d{8}$|\(\d{4}[^)]*\)|\d{4}\s*년")
KOGL_RE = re.compile(r"(?:제|공공누리)\s*([1-4])\s*유형")
SEOUL_PAGE = "https://data.seoul.go.kr/dataList/{}/A/1/datasetView.do"
WORD_RE = re.compile(r"[가-힣A-Za-z]{2,}")
# Seoul repeats one API per district (서울시 강서구 ...), per licensing category (인허가 정보 ~3K) and
# per translation (영문/일문/중문); the city-wide Korean original is the one card worth keeping.
SEOUL_DISTRICT_RE = re.compile(r"(?:^|\s)[가-힣]{1,3}구(?:\s|_|$)")
SEOUL_SKIP_RE = re.compile(r"인허가|\((?:영문|일문|중문|영어|일본어|중국어)[^)]*\)")


def get_json(session, url, params=None):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = session.get(url, params=params, timeout=60)
            if response.status_code == 429 or response.status_code >= 500:
                raise requests.HTTPError(f"http_{response.status_code}")
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError):
            if attempt == MAX_RETRIES:
                raise
            time.sleep(5 * 2**attempt)


def read_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    os.replace(temp, path)


def catalog_version(row):
    """Hash of a catalog row without counters: changes when the portal edits the API's metadata."""
    stable = {k: v for k, v in row.items() if not VOLATILE_KEY_RE.search(k)}
    return hashlib.sha256(json.dumps(stable, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def cached(name, fetch, refresh):
    path = CATALOG_DIR / f"{name}.jsonl"
    if refresh or not path.exists():
        write_jsonl(path, fetch())
    return read_jsonl(path)


def cached_items(name, items, item_key, one, refresh, workers, version=None, max_age_days=None, max_renew=None):
    """Per-item lookups cached in <name>.jsonl by "key".

    By default only items not cached yet are fetched, so widening the selection costs just the new
    items and a cached value is never looked at again. Renewal of cached values is opt-in:
      version       item -> str; a value is fetched again when the item's version changed since
      max_age_days  values older than this (or of unknown age) are fetched again
      max_renew     at most this many renewals per run, changed items first, then the oldest
    A renewal that fails keeps the cached value; a new item that fails still raises.
    """
    path = CATALOG_DIR / f"{name}.jsonl"
    stored = {} if refresh else {r["key"]: r for r in read_jsonl(path) if "key" in r}
    now = datetime.now(timezone.utc)

    def age(entry):
        fetched = entry.get("fetched_at")
        return (now - datetime.fromisoformat(fetched)).days if fetched else float("inf")

    keyed = [(item_key(item), item) for item in items]
    new = [item for key, item in keyed if key not in stored]
    changed = [
        item for key, item in keyed
        if key in stored and version and stored[key].get("version") not in (None, version(item))
    ]
    changed_keys = {item_key(item) for item in changed}
    stale = sorted(
        (item for key, item in keyed if key in stored and key not in changed_keys
         and max_age_days is not None and age(stored[key]) >= max_age_days),
        key=lambda item: -age(stored[item_key(item)]),
    )
    renew = (changed + stale)[:max_renew] if max_renew is not None else changed + stale
    todo = new + renew
    if todo:

        def attempt(item):
            try:
                return True, one(item)
            except Exception as error:  # noqa: BLE001 - decided per item below
                return False, error

        fetched_at = now.isoformat(timespec="seconds")
        with ThreadPoolExecutor(workers) as pool:
            for item, (ok, value) in zip(todo, pool.map(attempt, todo), strict=True):
                key = item_key(item)
                if ok:
                    stored[key] = {"key": key, "value": value, "fetched_at": fetched_at,
                                   **({"version": version(item)} if version else {})}
                elif key not in stored:
                    raise value
        write_jsonl(path, list(stored.values()))
    if renew:
        print(f"[{name}] renewed {len(renew)} cached items ({len(changed)} changed, {len(stale)} stale)", flush=True)
    return {key: entry["value"] for key, entry in stored.items()}


def kogl_license(text):
    """Portal license text -> a taxonomy alias: 공공누리 type, or the portal's no-restriction grant."""
    match = KOGL_RE.search(text or "")
    if match:
        return f"공공누리 제{match.group(1)}유형"
    return "이용허락범위 제한 없음" if "제한 없음" in (text or "") else None


TIER_LABELS = {
    "A_core_api": "국가중점데이터 OpenAPI",
    "B_ready_api": "운영 자동승인 OpenAPI",
    "C_standard": "표준데이터",
    "C_national_file": "중앙·광역 기관 파일데이터",
}


def publisher_level(org):
    """national (ministries, agencies) / province (광역시도) / local (시군구)."""
    org = (org or "").strip()
    if org in PROVINCES:
        return "province"
    return "local" if org.endswith(("시", "군", "구")) or " " in org and org.split()[0] in PROVINCES else "national"


def series_key(title):
    """Data name without publisher and edition: one key for a dataset across regions and years.

    Portal titles follow "{기관명}_{데이터명}[_{기준일}]", so the publisher is everything before the
    first underscore; titles without one fall back to stripping a region prefix.
    """
    title = title or ""
    title = title.split("_", 1)[1] if "_" in title else REGION_PREFIX_RE.sub("", title)
    title = EDITION_RE.sub("", title)
    return re.sub(r"[\s_()\[\]·,.\-]+", "", title).casefold()


def card_row(source, item_id, title, description, url, tags, formats, licenses, downloads, extra, readme):
    dataset_id = f"{source}/{item_id}"
    README_DIR.mkdir(parents=True, exist_ok=True)
    readme_path = README_DIR / f"{source}__{item_id}.md"
    readme_path.write_text(readme, encoding="utf-8")
    return {
        "dataset_id": dataset_id,
        "source": source,
        "url": url,
        "sha": hashlib.sha256(readme.encode("utf-8")).hexdigest()[:40],
        "seed_reasons": [source],
        "referenced_by_models": [],
        "downloads": downloads,
        "likes": None,
        "gated": False,
        "languages": ["ko"],
        "licenses": licenses,
        "task_categories": [],
        "task_ids": [],
        "size_categories": [],
        "modalities": ["tabular"],
        "formats": formats,
        "tags": sorted(set(tags)),
        "description": description,
        "card_data": {"pretty_name": title},
        "readme_path": readme_path.relative_to(AI_DIR).as_posix(),
        "readme_language": "ko",
        "readme_chars": len(readme),
        **extra,
    }


# ---------------------------------------------------------------- 서울 열린데이터광장


def seoul_page(session, key, service, start, end, *args):
    data = get_json(session, "/".join([SEOUL_API, key, "json", service, str(start), str(end), *args]) + "/")
    body = data.get(service) or {}
    code = (body.get("RESULT") or data.get("RESULT") or {}).get("CODE", "")
    if code == "INFO-200":  # no data
        return 0, []
    if not body:
        raise RuntimeError(f"{service}: {data}")
    return int(body.get("list_total_count") or 0), body.get("row") or []


def collect_seoul(session, refresh, workers, refresh_lists=False, renew_fields=False):
    key = os.environ["SEOUL_OPEN_API_KEY"]

    def fetch_catalog():
        total, rows = seoul_page(session, key, "SearchOpenAPIService", 1, PAGE_SIZE)
        for start in range(PAGE_SIZE + 1, total + 1, PAGE_SIZE):
            rows += seoul_page(session, key, "SearchOpenAPIService", start, start + PAGE_SIZE - 1)[1]
        return rows

    catalog = cached("seoul_openapi", fetch_catalog, refresh or refresh_lists)
    # Every API is kept; district / 인허가 / translated editions are folded into one series by
    # dataset_dedup (13), so they stay findable without crowding the ranking.
    selected = catalog

    def one_fields(row):
        return seoul_page(session, key, "SearchOpenAPIIOValueService", 1, 300, row["INF_ID"])[1]

    def one_license(row):
        try:
            return kogl_license(session.get(SEOUL_PAGE.format(row["INF_ID"]), timeout=60).text)
        except requests.RequestException:  # best effort, like the data.go.kr lookup
            return None

    inf_id = lambda row: row["INF_ID"]  # noqa: E731
    # Opt-in (--renew-fields): a cached field list is fetched again when its catalog row changed or
    # it is older than FIELD_MAX_AGE_DAYS, at most FIELD_RENEW_PER_RUN a run. Otherwise only new APIs.
    renewal = {"version": catalog_version, "max_age_days": FIELD_MAX_AGE_DAYS, "max_renew": FIELD_RENEW_PER_RUN}
    fields = cached_items(
        "seoul_fields_by_id", selected, inf_id, one_fields, refresh, workers, **(renewal if renew_fields else {})
    )
    licenses = cached_items("seoul_licenses_by_id", selected, inf_id, one_license, refresh, workers)
    rows = []
    for item in selected:
        outputs = [f for f in fields.get(item["INF_ID"], []) if f.get("PTYPE_NM") != "요청인자"]
        title = item["INF_NM"]
        lines = [
            f"- {f.get('COL_KOR_NM') or ''} ({f.get('COL_ENG_NM') or ''})"
            + (f": {f['COL_EXP']}" if f.get("COL_EXP") else "")
            for f in outputs
        ]
        # The card is the only vector a portal dataset gets (14), so it carries the field names.
        names = [f.get("COL_KOR_NM") for f in outputs if f.get("COL_KOR_NM")]
        description = f"{title}. {item.get('EXM_NM') or ''}".strip() + (
            f" 제공 필드: {', '.join(names[:40])}" if names else ""
        )
        readme = (
            "\n".join(
                [
                    f"# {title}",
                    "",
                    description,
                    "",
                    f"서비스명: {item['API_SERVICE_NM']}",
                    "",
                    "## 제공 필드",
                    "",
                    *lines,
                ]
            )
            + "\n"
        )
        rows.append(
            card_row(
                "seoul_open_data",
                item["INF_ID"],
                title,
                description,
                f"https://data.seoul.go.kr/dataList/{item['INF_ID']}/A/1/datasetView.do",
                WORD_RE.findall(title),
                ["api"],
                [licenses[item["INF_ID"]]] if licenses.get(item["INF_ID"]) else [],
                None,
                {"api_service": item["API_SERVICE_NM"], "field_count": len(outputs)},
                readme,
            )
        )
    print(
        f"[seoul] catalog {len(catalog)}, rows {len(rows)}, licensed {sum(bool(r['licenses']) for r in rows)}",
        flush=True,
    )
    return rows


# ---------------------------------------------------------------- 공공데이터포털


def collect_data_go_kr(session, refresh, workers, refresh_lists=False):
    key = os.environ["DATA_GO_KR_API_KEY"]

    def fetch_list(path):
        def fetch():
            first = get_json(
                session,
                f"{DATA_GO_KR_API}/{path}",
                {"page": 1, "perPage": PAGE_SIZE, "returnType": "JSON", "serviceKey": key},
            )
            rows, pages = first["data"], -(-first["matchCount"] // PAGE_SIZE)
            for page in range(2, pages + 1):
                rows += get_json(
                    session,
                    f"{DATA_GO_KR_API}/{path}",
                    {"page": page, "perPage": PAGE_SIZE, "returnType": "JSON", "serviceKey": key},
                )["data"]
            return rows

        return fetch

    files = cached("data_go_kr_dataset", fetch_list("dataset"), refresh or refresh_lists)
    apis = cached("data_go_kr_openapi", fetch_list("open-data-list"), refresh or refresh_lists)

    # 표준데이터: ~300 national schemas (전국공중화장실표준데이터 ...), registered by 공공데이터활용지원센터
    # with a blank file type; the ~13K standard-list rows are each region's submission to one of them.
    standard = cached("data_go_kr_standard", fetch_list("standard-data-list"), refresh or refresh_lists)
    standard_ids = {r.get("list_id") for r in standard}
    standard_desc: dict[str, str] = {}
    submissions: defaultdict[str, list[str]] = defaultdict(list)
    for r in standard:
        if len(r.get("desc") or "") > len(standard_desc.get(r.get("list_id"), "")):
            standard_desc[r.get("list_id")] = r.get("desc") or ""
        submissions[r.get("list_id")].append(r.get("title"))
    usable = lambda r: r.get("is_deleted") != "Y" and len(r.get("desc") or "") >= MIN_DESCRIPTION_CHARS

    apis_by_list: dict[str, dict] = {}
    for row in apis:  # one listing per API; several operations share a list_id
        if usable(row):
            apis_by_list.setdefault(row.get("list_id") or row["id"], row)
    picked = [(r, True, "A_core_api") for r in apis_by_list.values() if r.get("is_core_data") == "Y"]
    picked += [
        (r, True, "B_ready_api")
        for r in apis_by_list.values()
        if r.get("is_core_data") != "Y"
        and publisher_level(r.get("org_nm")) != "local"
        and r.get("is_confirmed_for_prod") == "Y"
    ]

    for row in files:
        if row["id"] in standard_ids and row.get("is_deleted") != "Y":
            desc = max(row.get("desc") or "", standard_desc.get(row["id"], ""), key=len)
            picked.append(({**row, "desc": desc, "ext": row.get("ext") or "csv"}, False, "C_standard"))
    files_ok = [r for r in files if usable(r) and (r.get("ext") or "").lower() in USABLE_EXTENSIONS]
    national = [r for r in files_ok if publisher_level(r.get("org_nm")) != "local"]
    by_category, seen_series = defaultdict(list), set()
    for row in sorted((r for r in national if r["id"] not in standard_ids), key=lambda r: -(r.get("view_cnt") or 0)):
        key = series_key(row.get("title"))
        if key not in seen_series:  # year editions of one dataset count once
            seen_series.add(key)
            by_category[row.get("new_category_nm") or row.get("category_nm") or "기타"].append(row)
    for members in by_category.values():
        picked += [(r, False, "C_national_file") for r in members[:FILE_CAP_PER_CATEGORY]]

    # 시군구 files repeat a national/standard dataset region by region; list them on it instead.
    variants = defaultdict(list)
    for row in files_ok:
        if publisher_level(row.get("org_nm")) == "local":
            variants[series_key(row.get("title"))].append(row.get("title"))

    def one_license(item):
        row, is_api = item[:2]
        kind = "openapi" if is_api else "fileData"
        try:
            meta = get_json(session, f"https://www.data.go.kr/catalog/{row.get('list_id') or row['id']}/{kind}.json")
        except Exception:  # the license lookup is best effort; unknown stays visible downstream
            meta = {}
        return (meta.get("license") or {}).get("name")

    licenses = cached_items(
        "data_go_kr_licenses_by_id", picked, lambda item: item[0]["id"], one_license, refresh, workers
    )
    out, seen = [], set()
    for row, is_api, tier in picked:
        item_id = re.sub(r"[^0-9A-Za-z_-]", "_", str(row.get("list_id") or row["id"]))
        if item_id in seen:  # one OpenAPI listing can expose several operations
            continue
        seen.add(item_id)
        title, desc = (
            row.get("title") or row.get("list_title"),
            " ".join((row.get("desc") or "").replace("<br/>", " ").split()),
        )
        keywords = [k.strip() for k in (row.get("keywords") or "").split(",") if k.strip()]
        category = row.get("new_category_nm") or row.get("category_nm")
        formats = ["api"] if is_api else ["csv", "api"] if tier == "C_standard" else [(row.get("ext") or "").lower()]
        license_value = kogl_license(licenses.get(row["id"]))
        regional = submissions.get(row["id"]) if tier == "C_standard" else variants.get(series_key(title), [])
        regional = regional or []
        readme = (
            "\n".join(
                [
                    f"# {title}",
                    "",
                    desc,
                    "",
                    f"제공기관: {row.get('org_nm')}",
                    f"분류: {category}",
                    f"키워드: {', '.join(keywords)}",
                    f"형식: {', '.join(formats)}",
                    f"선정 기준: {TIER_LABELS[tier]}",
                    f"수정일: {row.get('updated_at')}",
                    f"이용허락: {licenses.get(row['id']) or 'unknown'}",
                ]
                + (
                    [f"지역별 원본 {len(regional)}건: {', '.join(regional[:MAX_REGIONAL_VARIANTS])}"]
                    if regional
                    else []
                )
            )
            + "\n"
        )
        out.append(
            card_row(
                "data_go_kr",
                item_id,
                title,
                desc,
                row.get("page_url") or f"https://www.data.go.kr/data/{item_id}/openapi.do",
                keywords + [x for x in (category, row.get("category_nm")) if x],
                formats,
                [license_value] if license_value else [],
                row.get("download_cnt"),
                {
                    "org": row.get("org_nm"),
                    "category": category,
                    "last_modified": row.get("updated_at"),
                    "views": row.get("view_cnt"),
                    "list_type": "openapi" if is_api else "file",
                    "tier": tier,
                    "regional_variants": regional[:MAX_REGIONAL_VARIANTS],
                    "regional_variant_count": len(regional),
                },
                readme,
            )
        )
    tiers: defaultdict[str, int] = defaultdict(int)
    for row in out:
        tiers[row["tier"]] += 1
    print(
        f"[data.go.kr] files {len(files)}, apis {len(apis)}, selected {len(out)} {dict(tiers)}, "
        f"licensed {sum(bool(r['licenses']) for r in out)}",
        flush=True,
    )
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", choices=("seoul", "data_go_kr", "all"), default="all")
    parser.add_argument("--refresh", action="store_true", help="re-download cached catalogs")
    # Lists only: new datasets appear, while per-item lookups are fetched just for ids not cached yet.
    parser.add_argument("--refresh-lists", action="store_true", help="re-download catalog lists, keep per-item caches")
    parser.add_argument("--renew-fields", action="store_true", help="re-fetch Seoul field lists that changed or aged out")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    from dotenv import load_dotenv

    load_dotenv(".env")
    session = requests.Session()
    previous = {r["dataset_id"]: r for r in read_jsonl(OUTPUT)}
    rows = []
    if args.source in ("seoul", "all"):
        rows += collect_seoul(session, args.refresh, args.workers, args.refresh_lists, args.renew_fields)
    else:
        rows += [r for r in previous.values() if r["source"] == "seoul_open_data"]
    if args.source in ("data_go_kr", "all"):
        rows += collect_data_go_kr(session, args.refresh, args.workers, args.refresh_lists)
    else:
        rows += [r for r in previous.values() if r["source"] == "data_go_kr"]
    write_jsonl(OUTPUT, rows)
    print(f"{len(rows)} public datasets -> {OUTPUT}")


def self_check():
    assert kogl_license("공공저작물 : 출처표시 (제 1유형)") == "공공누리 제1유형"
    assert kogl_license("공공저작물 : 출처표시 + 상업적 이용금지 + 변경금지 (제4유형)") == "공공누리 제4유형"
    assert kogl_license("공공누리 1유형 : 출처표시 (상업적 이용 및 변경 가능)") == "공공누리 제1유형"
    assert kogl_license(None) is None and kogl_license("이용허락범위 제한 없음") == "이용허락범위 제한 없음"
    assert SEOUL_DISTRICT_RE.search("서울시 강서구 모범음식점") and not SEOUL_DISTRICT_RE.search(
        "서울시 공공자전거 따릉이 대여소 정보"
    )
    assert SEOUL_SKIP_RE.search("서울시 의원 인허가 정보") and SEOUL_SKIP_RE.search("한양도성 스탬프 투어 정보(일문)")
    assert publisher_level("행정안전부") == "national" and publisher_level("경기도") == "province"
    assert publisher_level("경기도 성남시") == "local" and publisher_level("부산광역시 동구") == "local"
    assert series_key("경상남도 창원시_누비자 터미널_20251231") == series_key("누비자 터미널")
    assert series_key("행정안전부_공중화장실정보_20251127") == series_key("경기도 성남시_공중화장실정보")
    assert series_key("해양수산부 국립해양조사원_기본수준점_20260209") == series_key(
        "해양수산부 국립해양조사원_기본수준점"
    )
    assert WORD_RE.findall("서울시 공공자전거 따릉이 실시간 대여정보") == [
        "서울시",
        "공공자전거",
        "따릉이",
        "실시간",
        "대여정보",
    ]
    print("18_collect_public_datasets ok")


if __name__ == "__main__":
    main()
