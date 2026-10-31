"""Stage D1b: collect Korean public-data cards (서울 열린데이터광장, 공공데이터포털).

Both portals publish a catalog API, so the whole catalog is cached once and filtered
locally; only the selected datasets cost per-item calls (field schema, license).

  seoul_open_data   SearchOpenAPIService (catalog, ~5.9K OpenAPIs) + SearchOpenAPIIOValueService
                    (output fields) + the dataset page for its 공공누리 type (the catalog has none).
                    All ~5.9K APIs; district and translated editions are grouped later, not dropped.
  data_go_kr        목록조회서비스 15077093 (/dataset ~100K files, /open-data-list ~17K APIs) +
                    per-dataset catalog JSON-LD for the 공공누리 license.

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
from pathlib import Path

import requests

DATA_DIR = Path("data")
OUTPUT = DATA_DIR / "public_datasets_stage1.jsonl"
CATALOG_DIR = DATA_DIR / "public_catalog"
README_DIR = DATA_DIR / "readmes" / "public"
SEOUL_API = "http://openapi.seoul.go.kr:8088"
SEOUL_CITY_HOST = "openapi.seoul.go.kr"
DATA_GO_KR_API = "https://api.odcloud.kr/api/15077093/v1"
PAGE_SIZE = 1000
MAX_RETRIES = 4
# ponytail: per-category popularity cut keeps ~3K well-used datasets out of ~120K; raise it
# (or add keyword seeds) when a domain the demos need comes up empty.
DATA_GO_KR_PER_CATEGORY = 150
DATA_GO_KR_API_PER_CATEGORY = 60
MIN_DESCRIPTION_CHARS = 80
# File types a model pipeline can read; images, hwp-only notices and zip bundles are skipped.
USABLE_EXTENSIONS = {"csv", "json", "xml", "xlsx", "xls", "shp", "geojson", "txt"}
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


def cached(name, fetch, refresh):
    path = CATALOG_DIR / f"{name}.jsonl"
    if refresh or not path.exists():
        write_jsonl(path, fetch())
    return read_jsonl(path)


def cached_items(name, items, item_key, one, refresh, workers):
    """Per-item lookups cached in <name>.jsonl by "key"; only items not cached yet are fetched,
    so widening the selection costs just the new items."""
    path = CATALOG_DIR / f"{name}.jsonl"
    have = {} if refresh else {r["key"]: r["value"] for r in read_jsonl(path) if "key" in r}
    missing = [item for item in items if item_key(item) not in have]
    if missing:
        with ThreadPoolExecutor(workers) as pool:
            have.update(zip(map(item_key, missing), pool.map(one, missing)))
        write_jsonl(path, [{"key": k, "value": v} for k, v in have.items()])
    return have


def kogl_license(text):
    """Portal license text -> a taxonomy alias: 공공누리 type, or the portal's no-restriction grant."""
    match = KOGL_RE.search(text or "")
    if match:
        return f"공공누리 제{match.group(1)}유형"
    return "이용허락범위 제한 없음" if "제한 없음" in (text or "") else None


def card_row(source, item_id, title, description, url, tags, formats, licenses, downloads, extra, readme):
    dataset_id = f"{source}/{item_id}"
    README_DIR.mkdir(parents=True, exist_ok=True)
    readme_path = README_DIR / f"{source}__{item_id}.md"
    readme_path.write_text(readme, encoding="utf-8")
    return {
        "dataset_id": dataset_id, "source": source, "url": url,
        "sha": hashlib.sha256(readme.encode("utf-8")).hexdigest()[:40],
        "seed_reasons": [source], "referenced_by_models": [], "downloads": downloads, "likes": None, "gated": False,
        "languages": ["ko"], "licenses": licenses, "task_categories": [], "task_ids": [], "size_categories": [],
        "modalities": ["tabular"], "formats": formats, "tags": sorted(set(tags)), "description": description,
        "card_data": {"pretty_name": title}, "readme_path": str(readme_path), "readme_language": "ko",
        "readme_chars": len(readme), **extra,
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


def collect_seoul(session, refresh, workers):
    key = os.environ["SEOUL_OPEN_API_KEY"]

    def fetch_catalog():
        total, rows = seoul_page(session, key, "SearchOpenAPIService", 1, PAGE_SIZE)
        for start in range(PAGE_SIZE + 1, total + 1, PAGE_SIZE):
            rows += seoul_page(session, key, "SearchOpenAPIService", start, start + PAGE_SIZE - 1)[1]
        return rows

    catalog = cached("seoul_openapi", fetch_catalog, refresh)
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
    fields = cached_items("seoul_fields_by_id", selected, inf_id, one_fields, refresh, workers)
    licenses = cached_items("seoul_licenses_by_id", selected, inf_id, one_license, refresh, workers)
    rows = []
    for item in selected:
        outputs = [f for f in fields.get(item["INF_ID"], []) if f.get("PTYPE_NM") != "요청인자"]
        title = item["INF_NM"]
        lines = [f"- {f.get('COL_KOR_NM') or ''} ({f.get('COL_ENG_NM') or ''})" + (f": {f['COL_EXP']}" if f.get("COL_EXP") else "")
                 for f in outputs]
        description = f"{title}. {item.get('EXM_NM') or ''}".strip()
        readme = "\n".join([f"# {title}", "", description, "", f"서비스명: {item['API_SERVICE_NM']}", "",
                            "## 제공 필드", "", *lines]) + "\n"
        rows.append(card_row(
            "seoul_open_data", item["INF_ID"], title, description,
            f"https://data.seoul.go.kr/dataList/{item['INF_ID']}/A/1/datasetView.do",
            WORD_RE.findall(title), ["api"], [licenses[item["INF_ID"]]] if licenses.get(item["INF_ID"]) else [], None,
            {"api_service": item["API_SERVICE_NM"], "field_count": len(outputs)}, readme))
    print(f"[seoul] catalog {len(catalog)}, rows {len(rows)}, licensed {sum(bool(r['licenses']) for r in rows)}", flush=True)
    return rows


# ---------------------------------------------------------------- 공공데이터포털

def collect_data_go_kr(session, refresh, workers):
    key = os.environ["DATA_GO_KR_API_KEY"]

    def fetch_list(path):
        def fetch():
            first = get_json(session, f"{DATA_GO_KR_API}/{path}",
                             {"page": 1, "perPage": PAGE_SIZE, "returnType": "JSON", "serviceKey": key})
            rows, pages = first["data"], -(-first["matchCount"] // PAGE_SIZE)
            for page in range(2, pages + 1):
                rows += get_json(session, f"{DATA_GO_KR_API}/{path}",
                                 {"page": page, "perPage": PAGE_SIZE, "returnType": "JSON", "serviceKey": key})["data"]
            return rows
        return fetch

    files = cached("data_go_kr_dataset", fetch_list("dataset"), refresh)
    apis = cached("data_go_kr_openapi", fetch_list("open-data-list"), refresh)

    def usable(row, is_api):
        if row.get("is_deleted") == "Y" or len(row.get("desc") or "") < MIN_DESCRIPTION_CHARS:
            return False
        return is_api or (row.get("ext") or "").lower() in USABLE_EXTENSIONS

    picked = []
    for rows, is_api, limit in ((files, False, DATA_GO_KR_PER_CATEGORY), (apis, True, DATA_GO_KR_API_PER_CATEGORY)):
        by_category = defaultdict(list)
        for row in rows:
            if usable(row, is_api):
                by_category[row.get("new_category_nm") or row.get("category_nm") or "기타"].append(row)
        for members in by_category.values():
            members.sort(key=lambda r: -(r.get("view_cnt") or 0))
            picked += [(r, is_api) for r in members[:limit]]

    def one_license(item):
        row, is_api = item
        kind = "openapi" if is_api else "fileData"
        try:
            meta = get_json(session, f"https://www.data.go.kr/catalog/{row.get('list_id') or row['id']}/{kind}.json")
        except Exception:  # the license lookup is best effort; unknown stays visible downstream
            meta = {}
        return (meta.get("license") or {}).get("name")

    licenses = cached_items("data_go_kr_licenses_by_id", picked, lambda item: item[0]["id"], one_license, refresh, workers)
    out, seen = [], set()
    for row, is_api in picked:
        item_id = re.sub(r"[^0-9A-Za-z_-]", "_", str(row.get("list_id") or row["id"]))
        if item_id in seen:  # one OpenAPI listing can expose several operations
            continue
        seen.add(item_id)
        title, desc = row.get("title") or row.get("list_title"), " ".join((row.get("desc") or "").replace("<br/>", " ").split())
        keywords = [k.strip() for k in (row.get("keywords") or "").split(",") if k.strip()]
        category = row.get("new_category_nm") or row.get("category_nm")
        formats = ["api"] if is_api else [(row.get("ext") or "").lower()]
        license_value = kogl_license(licenses.get(row["id"]))
        readme = "\n".join([f"# {title}", "", desc, "", f"제공기관: {row.get('org_nm')}", f"분류: {category}",
                            f"키워드: {', '.join(keywords)}", f"형식: {', '.join(formats)}",
                            f"수정일: {row.get('updated_at')}", f"이용허락: {licenses.get(row['id']) or 'unknown'}"]) + "\n"
        out.append(card_row(
            "data_go_kr", item_id, title, desc, row.get("page_url") or f"https://www.data.go.kr/data/{item_id}/openapi.do",
            keywords + [x for x in (category, row.get("category_nm")) if x], formats,
            [license_value] if license_value else [], row.get("download_cnt"),
            {"org": row.get("org_nm"), "category": category, "last_modified": row.get("updated_at"),
             "views": row.get("view_cnt"), "list_type": "openapi" if is_api else "file"}, readme))
    print(f"[data.go.kr] files {len(files)}, apis {len(apis)}, selected {len(out)}, "
          f"licensed {sum(bool(r['licenses']) for r in out)}", flush=True)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", choices=("seoul", "data_go_kr", "all"), default="all")
    parser.add_argument("--refresh", action="store_true", help="re-download cached catalogs")
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
        rows += collect_seoul(session, args.refresh, args.workers)
    else:
        rows += [r for r in previous.values() if r["source"] == "seoul_open_data"]
    if args.source in ("data_go_kr", "all"):
        rows += collect_data_go_kr(session, args.refresh, args.workers)
    else:
        rows += [r for r in previous.values() if r["source"] == "data_go_kr"]
    write_jsonl(OUTPUT, rows)
    print(f"{len(rows)} public datasets -> {OUTPUT}")


def self_check():
    assert kogl_license("공공저작물 : 출처표시 (제 1유형)") == "공공누리 제1유형"
    assert kogl_license("공공저작물 : 출처표시 + 상업적 이용금지 + 변경금지 (제4유형)") == "공공누리 제4유형"
    assert kogl_license("공공누리 1유형 : 출처표시 (상업적 이용 및 변경 가능)") == "공공누리 제1유형"
    assert kogl_license(None) is None and kogl_license("이용허락범위 제한 없음") == "이용허락범위 제한 없음"
    assert SEOUL_DISTRICT_RE.search("서울시 강서구 모범음식점") and not SEOUL_DISTRICT_RE.search("서울시 공공자전거 따릉이 대여소 정보")
    assert SEOUL_SKIP_RE.search("서울시 의원 인허가 정보") and SEOUL_SKIP_RE.search("한양도성 스탬프 투어 정보(일문)")
    assert WORD_RE.findall("서울시 공공자전거 따릉이 실시간 대여정보") == ["서울시", "공공자전거", "따릉이", "실시간", "대여정보"]
    print("18_collect_public_datasets ok")


if __name__ == "__main__":
    main()
