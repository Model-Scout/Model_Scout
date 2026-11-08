"""Collapse re-uploaded and cross-listed datasets to one canonical entry.

Hugging Face is full of mirrors (30 copies of wikipedia, 10 of MathNet), and the two public
portals list the same dataset twice (서울교통공사_지하철혼잡도정보 on both) or split one series
by year. Recommending all of them is noise, so 13_build_hypergraph keeps one canonical row
per group and records the rest as its duplicates.

  HF + Kaggle   same README body (>= 300 chars), or same repo/slug name with README word sets
                overlapping >= 80%. A shared generic name alone ("data", "train") is not enough.
                A Kaggle re-upload of a Hub dataset is renamed (KR3 -> kr3-korean-restaurant-reviews),
                so Kaggle vs HF also matches on README word overlap >= 50% (true pairs 0.53-0.73,
                the next best 0.27).
                Canonical: cited by a model card, then the Hub original over a Kaggle re-upload,
                then most downloads.
  public        policy "verified" (corpus v2): only when the metadata itself shows the same data:
                same title, coverage, language, period and spatial unit, plus identical fields and
                description (서울) or the same publisher and description (포털), and the same known
                license. A matching title alone is not evidence, so districts, years, translated
                editions, cross-portal listings and rows with an unknown license stay separate,
                searchable entries. public_series records how they relate.
                policy "title" (corpus v1, frozen): same title once org prefixes, districts, dates,
                years and translated editions are stripped. Kept only to rebuild v1 until cutover.
  same owner    one author on both sites with README overlap >= 25% (podongchip's KOSPI features).

Only duplicates may stand in for each other when scoring. A series relation never does.
"""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from pathlib import Path

AI_DIR = Path(__file__).resolve().parent  # stored readme_path values are relative to it
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
MIN_BODY_CHARS = 300
NAME_JACCARD = 0.8
CROSS_SITE_JACCARD = 0.5
WORD_RE = re.compile(r"[a-z가-힣0-9]{3,}")
TITLE_NOISE = [
    re.compile(r"_?\d{8}$"),  # 기본수준점_20260209
    re.compile(r"\(\s*\d{4}[^)]*\)"),  # (2009~2013년), (2017년)
    re.compile(r"\d{4}\s*년"),  # 상수도 사용량 2005년
    re.compile(r"^(?:서울특별시|서울시|서울교통공사)[_\s]+"),
    re.compile(r"(?:^|\s)[가-힣]{1,3}구(?=\s|_|$)"),  # 강서구 ... : one series per district
    re.compile(r"\((?:영문|일문|중문|영어|일본어|중국어)[^)]*\)"),  # translated editions
]
DISTRICT_RE = re.compile(r"(?:^|\s)[가-힣]{1,3}구(?:\s|_|$)")
SAME_OWNER_JACCARD = 0.25
TITLE_PUNCT_RE = re.compile(r"[\s_()\[\]·,.\-]+")

REGION_NAMES = {
    "서울": ("서울특별시", "서울시"),
    "부산": ("부산광역시", "부산시"),
    "대구": ("대구광역시", "대구시"),
    "인천": ("인천광역시", "인천시"),
    "광주": ("광주광역시", "광주시"),
    "대전": ("대전광역시", "대전시"),
    "울산": ("울산광역시", "울산시"),
    "세종": ("세종특별자치시", "세종시"),
    "경기": ("경기도",),
    "강원": ("강원특별자치도", "강원도"),
    "충북": ("충청북도",),
    "충남": ("충청남도",),
    "전북": ("전북특별자치도", "전라북도"),
    "전남": ("전라남도",),
    "경북": ("경상북도",),
    "경남": ("경상남도",),
    "제주": ("제주특별자치도", "제주도"),
}
SEOUL_DISTRICTS = frozenset(
    "종로구 중구 용산구 성동구 광진구 동대문구 중랑구 성북구 강북구 도봉구 노원구 은평구 서대문구 "
    "마포구 양천구 강서구 구로구 금천구 영등포구 동작구 관악구 서초구 강남구 송파구 강동구".split()
)
_FULL_REGION = {name: region for region, names in REGION_NAMES.items() for name in names}
_FULL_RE = "|".join(sorted(_FULL_REGION, key=len, reverse=True))
_SHORT_RE = "|".join(REGION_NAMES)
# 줄임말은 경계가 있어야 인정한다. 그래야 "경기동향", "환경기초시설"이 경기도가 되지 않는다.
TITLE_REGION_RE = re.compile(rf"{_FULL_RE}|(?:^|[_\s(])(?:{_SHORT_RE})(?=[\s_)]|지역|도내|시내|$)")
LOCAL_UNIT_RE = re.compile(rf"(?:{_FULL_RE})[\s_+]+([가-힣]{{1,5}}(?:시|군|구))(?=[\s_+]|$)")
TITLE_DISTRICT_RE = re.compile(r"(?:^|[\s_+])([가-힣]{1,3}구)(?=[\s_+]|$)")
NATIONAL_RE = re.compile(r"전국")
PUBLISHER_REGION_RE = re.compile(rf"^(?:{_FULL_RE}|{_SHORT_RE})")
PUBLISHER_GOVERNMENT_RE = re.compile(rf"^(?:{_FULL_RE})(?:\s*[가-힣]{{1,5}}(?:시|군|구))?$")
LANGUAGE_RE = re.compile(r"영문|영어|일문|일본어|중문|중국어(?:[_\s]*(?:간체|번체))?|\bEnglish\b", re.I)
LANGUAGE_NAMES = {"영문": "en", "영어": "en", "english": "en", "일문": "ja", "일본어": "ja", "중문": "zh"}
PERIOD_RE = re.compile(r"(?<!\d)(?:19|20)\d{2}(?!\d)")
REVISION_RE = re.compile(r"_((?:19|20)\d{6})$")  # 포털이 파일에 붙이는 등록일. 데이터 기간이 아니다.
SPATIAL_UNIT_RE = re.compile(r"집계구|자치구|행정동|법정동|시군구|읍면동|권역|격자|\d+\s*m\b", re.I)
FIELD_LINE_RE = re.compile(r"^- (.+)$", re.M)
MIN_SAME_DESCRIPTION_CHARS = 100
# 빌드 안전장치. 공공데이터는 근거가 있을 때만 병합하므로 이 비율을 넘으면 규칙 오류로 본다.
MAX_PUBLIC_MERGE_RATE = 0.05
RELATION_ORDER = (
    "language_variant",
    "spatial_unit_variant",
    "region_variant",
    "subset_candidate",
    "edition_variant",
    "cross_listing_candidate",
)


def readme_body(row):
    path = row.get("readme_path")
    path = AI_DIR / path if path else None
    text = path.read_text(encoding="utf-8", errors="ignore") if path and path.exists() else ""
    return " ".join(FRONTMATTER_RE.sub("", text, count=1).split())


def title_key(title):
    for pattern in TITLE_NOISE:
        title = pattern.sub("", title or "")
    return TITLE_PUNCT_RE.sub("", title).casefold()


def _jaccard(a, b):
    a, b = set(a.casefold().split()), set(b.casefold().split())
    return len(a & b) / len(a | b) if a and b else 0.0


class _Groups:
    def __init__(self):
        self.parent = {}

    def find(self, item):
        self.parent.setdefault(item, item)
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)


def _hf_groups(rows, groups, reasons):
    bodies = {r["dataset_id"]: readme_body(r) for r in rows}
    by_hash, by_name = defaultdict(list), defaultdict(list)
    for row in rows:
        body = bodies[row["dataset_id"]]
        if len(body) >= MIN_BODY_CHARS:
            by_hash[hashlib.sha1(body.encode("utf-8")).hexdigest()].append(row["dataset_id"])
        by_name[row["dataset_id"].rsplit("/", 1)[-1].casefold()].append(row["dataset_id"])  # kaggle/owner/slug -> slug
    for ids in by_hash.values():
        for other in ids[1:]:
            groups.union(other, ids[0])
            reasons[other] = "identical README"
    for ids in by_name.values():
        for i, a in enumerate(ids):
            for b in ids[i + 1 :]:
                if groups.find(a) != groups.find(b) and _jaccard(bodies[a], bodies[b]) >= NAME_JACCARD:
                    groups.union(a, b)
                    reasons.setdefault(b, "same name, near-identical README")
    words = {k: set(WORD_RE.findall(v.casefold())) for k, v in bodies.items()}
    hub = [r["dataset_id"] for r in rows if r.get("source", "huggingface") == "huggingface" and words[r["dataset_id"]]]
    for row in rows:
        kaggle_id = row["dataset_id"]
        if row.get("source") != "kaggle" or len(words[kaggle_id]) < 30:
            continue
        mine = words[kaggle_id]
        score, match = max(((len(mine & words[h]) / len(mine | words[h]), h) for h in hub), default=(0.0, None))
        if score >= CROSS_SITE_JACCARD:
            groups.union(kaggle_id, match)
            reasons[kaggle_id] = f"Kaggle re-upload of {match} (README overlap {score:.2f})"
            continue
        owner = kaggle_id.split("/")[1].casefold()
        for hub_id in hub:
            if hub_id.split("/")[0].casefold() == owner:
                overlap = len(mine & words[hub_id]) / len(mine | words[hub_id])
                if overlap >= SAME_OWNER_JACCARD:
                    groups.union(kaggle_id, hub_id)
                    reasons[kaggle_id] = f"same author's Kaggle copy of {hub_id} (README overlap {overlap:.2f})"
                    break


def _title(row):
    return (row.get("card_data") or {}).get("pretty_name") or ""


def _title_regions(title):
    found = set()
    for match in TITLE_REGION_RE.finditer(title):
        name = match.group(0).strip("_ (")
        found.add(_FULL_REGION.get(name, name))
    return sorted(found)


def _district(title):
    local = LOCAL_UNIT_RE.search(title)
    if local:
        return local.group(1)
    return next((d for d in TITLE_DISTRICT_RE.findall(title) if d in SEOUL_DISTRICTS), None)


def public_identity(row):
    """What the metadata says about one portal row.

    제공기관 소재지와 데이터 지역 범위는 다른 값이다. 경기도가 낸 데이터가 경기도만 다루는지는
    제목이 말하지 않으면 추정이고, 근거가 없으면 "전국"이 아니라 미확인으로 둔다.
    """
    title, org = _title(row), (row.get("org") or "").strip()
    publisher_match = PUBLISHER_REGION_RE.match(org)
    publisher_region = None
    if publisher_match:
        publisher_region = _FULL_REGION.get(publisher_match.group(0), publisher_match.group(0))
    regions, district = _title_regions(title), _district(title)
    if regions:
        status = "stated_in_title"
    elif NATIONAL_RE.search(title):
        regions, status = ["전국"], "stated_in_title"
    elif row.get("source") == "seoul_open_data":
        regions, status = ["서울"], "inferred_from_seoul_portal"
    elif publisher_region and PUBLISHER_GOVERNMENT_RE.match(org):
        regions, status = [publisher_region], "inferred_from_publisher"
    else:
        status = "unknown"
    if district and not regions:  # a district name with no region: 25 Seoul districts only reach here
        regions, status = ["서울"], "stated_in_title"
    language = LANGUAGE_RE.search(title)
    language_edition = None
    if language:
        word = language.group(0).casefold()
        language_edition = LANGUAGE_NAMES.get(word, "zh" if word.startswith("중국어") else word)
    revision = REVISION_RE.search(title)
    return {
        "publisher": org or None,
        "publisher_region": publisher_region,
        "coverage_regions": regions,
        "coverage_district": district,
        "coverage_status": status,
        "language_edition": language_edition,
        "period": sorted(set(PERIOD_RE.findall(REVISION_RE.sub("", title)))),
        "revision": revision.group(1) if revision else None,
        "spatial_unit": sorted(set(SPATIAL_UNIT_RE.findall(title))),
    }


def _scope(identity):
    return (
        tuple(identity["coverage_regions"]),
        identity["coverage_district"],
        identity["language_edition"],
        tuple(identity["period"]),
        identity["revision"],
        tuple(identity["spatial_unit"]),
    )


def seoul_fields(row):
    path = AI_DIR / row["readme_path"] if row.get("readme_path") else None
    if not path or not path.exists():
        return frozenset()
    text = path.read_text(encoding="utf-8", errors="ignore")
    return frozenset(FIELD_LINE_RE.findall(text.split("## 제공 필드", 1)[-1])) if "## 제공 필드" in text else frozenset()


def same_data_evidence(a, b):
    """The metadata evidence that two portal rows are one dataset, or None.

    Row-level content is not collected, so this is the strongest proof available locally: a
    missing or differing fact keeps the rows apart. Cross-portal pairs share no comparable
    metadata and stay separate until checked against the source.
    """
    title_a, title_b = (TITLE_PUNCT_RE.sub("", _title(r)).casefold() for r in (a, b))
    if title_a != title_b or a.get("source") != b.get("source"):
        return None
    if _scope(public_identity(a)) != _scope(public_identity(b)):
        return None
    # 미확인 라이선스는 어느 쪽과도 "같다"고 볼 수 없다. 허용하면 상업 가능-미확인-비상업이
    # 연쇄로 한 그룹이 되어, 대표의 라이선스만 보는 필터가 비상업 데이터를 통과시킨다.
    licenses_a, licenses_b = a.get("licenses") or [], b.get("licenses") or []
    if not licenses_a or licenses_a != licenses_b:
        return None
    description_a, description_b = (" ".join((r.get("description") or "").split()) for r in (a, b))
    if description_a != description_b:
        return None
    if a["source"] == "seoul_open_data":
        fields = seoul_fields(a)
        return "same title, scope, fields and description" if fields and fields == seoul_fields(b) else None
    same_publisher = (a.get("org") or "") == (b.get("org") or "") and a.get("org")
    if same_publisher and len(description_a) >= MIN_SAME_DESCRIPTION_CHARS:
        return "same title, scope, publisher and description"
    return None


def _public_groups(rows, groups, reasons):
    by_title = defaultdict(list)
    for row in rows:
        key = title_key(_title(row))
        if key:
            by_title[key].append(row)
    for members in by_title.values():
        for i, a in enumerate(members):
            for b in members[i + 1 :]:
                evidence = same_data_evidence(a, b)
                if evidence:
                    groups.union(b["dataset_id"], a["dataset_id"])
                    reasons[b["dataset_id"]] = evidence


def _public_groups_by_title(rows, groups, reasons):
    by_title = defaultdict(list)
    for row in rows:
        key = title_key(_title(row))
        if key:
            by_title[key].append(row["dataset_id"])
    for ids in by_title.values():
        for other in ids[1:]:
            groups.union(other, ids[0])
            reasons[other] = "same title (org prefix / year stripped)"


def _relation_types(anchor, other):
    """How one series member differs from the anchor. Never evidence of the same data."""
    a, b = public_identity(anchor), public_identity(other)
    types = set()
    if a["language_edition"] != b["language_edition"]:
        types.add("language_variant")
    if a["spatial_unit"] != b["spatial_unit"]:
        types.add("spatial_unit_variant")
    same_regions = a["coverage_regions"] == b["coverage_regions"]
    if a["coverage_district"] and b["coverage_district"] and a["coverage_district"] != b["coverage_district"]:
        types.add("region_variant")
    elif not same_regions:
        types.add("region_variant")
    elif not a["coverage_district"] and b["coverage_district"]:
        types.add("subset_candidate")  # 전체판의 분할본 후보일 뿐, 포함 관계는 검증하지 않았다.
    if a["period"] != b["period"] or a["revision"] != b["revision"]:
        types.add("edition_variant")
    if anchor.get("source") != other.get("source"):
        types.add("cross_listing_candidate")
    return [t for t in RELATION_ORDER if t in types] or ["same_title_unverified"]


def _anchor_rank(row):
    identity = public_identity(row)
    return (
        bool(identity["coverage_district"]),
        bool(identity["language_edition"]),
        bool(identity["period"]),
        row["dataset_id"],
    )


def public_series(public_rows, duplicates):
    """Rows sharing a stripped title, kept as separate entries, with how each relates to an anchor.

    A series helps grouping and navigation. It says nothing about the rows holding the same data,
    so evaluation must not treat members as interchangeable answers.
    """
    by_title = defaultdict(list)
    for row in public_rows:
        key = title_key(_title(row))
        if key and row["dataset_id"] not in duplicates:
            by_title[key].append(row)
    series = []
    for key, members in sorted(by_title.items()):
        if len(members) < 2:
            continue
        anchor = min(members, key=_anchor_rank)
        series.append(
            {
                "series_id": "series:" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:12],
                "series_key": key,
                "anchor": anchor["dataset_id"],
                "members": sorted(row["dataset_id"] for row in members),
                "relations": [
                    {
                        "dataset_id": row["dataset_id"],
                        "relation_to_anchor": _relation_types(anchor, row),
                        "verified": False,
                        "answer_substitutable": False,
                    }
                    for row in sorted(members, key=lambda r: r["dataset_id"])
                    if row is not anchor
                ],
            }
        )
    return series


def check_public_duplicates(duplicates, public_rows):
    """Stop the build when public merges look wrong. Returns the number of public merges."""
    rows = {row["dataset_id"]: row for row in public_rows}
    merged = {d: info for d, info in duplicates.items() if d in rows}
    for dataset_id, info in merged.items():
        scope_a = _scope(public_identity(rows[dataset_id]))
        scope_b = _scope(public_identity(rows[info["canonical"]]))
        if scope_a != scope_b:
            raise ValueError(f"{dataset_id} merged into {info['canonical']} across different scopes")
    groups = defaultdict(set)
    for dataset_id, info in merged.items():
        groups[info["canonical"]].update((dataset_id, info["canonical"]))
    for canonical, members in groups.items():
        licenses = {tuple(rows[member].get("licenses") or []) for member in members}
        if len(licenses) != 1 or () in licenses:
            raise ValueError(f"license conflict or unknown license in the group of {canonical}: {sorted(members)}")
    if rows and len(merged) / len(rows) > MAX_PUBLIC_MERGE_RATE:
        raise ValueError(f"public merge rate {len(merged)}/{len(rows)} is over {MAX_PUBLIC_MERGE_RATE:.0%}")
    return len(merged)


PORTAL_SOURCES = {"seoul_open_data", "data_go_kr"}


def duplicate_map(hf_rows, public_rows, public_policy="verified"):
    """dataset_id -> {"canonical": id, "reason": str} for every non-canonical member."""
    groups, reasons = _Groups(), dict[str, str]()
    _hf_groups(hf_rows, groups, reasons)
    (_public_groups if public_policy == "verified" else _public_groups_by_title)(public_rows, groups, reasons)
    rows = {r["dataset_id"]: r for r in [*hf_rows, *public_rows]}
    members = defaultdict(list)
    for dataset_id in rows:
        members[groups.find(dataset_id)].append(dataset_id)

    def rank(dataset_id):
        row = rows[dataset_id]
        if row.get("source") in PORTAL_SOURCES:
            title = (row.get("card_data") or {}).get("pretty_name") or ""
            return (bool(row.get("licenses")), not DISTRICT_RE.search(title), row.get("readme_chars") or 0)
        return (
            bool(row.get("referenced_by_models")),
            row.get("source", "huggingface") == "huggingface",
            row.get("downloads") or 0,
        )

    duplicates = {}
    for ids in members.values():
        if len(ids) < 2:
            continue
        canonical = max(ids, key=rank)
        # The union root has no reason of its own when another member wins; it shares the group's.
        group_reason = next((reasons[i] for i in ids if i in reasons), "grouped")
        for dataset_id in ids:
            if dataset_id != canonical:
                duplicates[dataset_id] = {"canonical": canonical, "reason": reasons.get(dataset_id, group_reason)}
    return duplicates


if __name__ == "__main__":
    assert title_key("서울교통공사_지하철혼잡도정보") == title_key("서울교통공사_지하철혼잡도정보 ")
    assert title_key("서울특별시_공공서비스예약 정보") == title_key("서울시 공공서비스예약 정보")
    assert title_key("해양수산부 국립해양조사원_기본수준점_20260209") == title_key(
        "해양수산부 국립해양조사원_기본수준점"
    )
    assert title_key("서울시 한강공원 이용객 현황 (2009~2013년)") == title_key("서울시 한강공원 이용객 현황(2017년)")
    assert title_key("서울시 강우량 정보") != title_key("서울시 강설량 정보")
    assert title_key("서울시 강서구 모범음식점 현황") == title_key("서울시 마포구 모범음식점 현황")
    assert title_key("서울시 한양도성 스탬프 투어 정보(일문)") == title_key("서울시 한양도성 스탬프 투어 정보")
    hf = [
        {"dataset_id": "wikimedia/wikipedia", "downloads": 9},
        {"dataset_id": "copy/wikipedia", "downloads": 1},
        {"dataset_id": "a/data", "downloads": 5},
        {"dataset_id": "b/data", "downloads": 3},
    ]
    bodies = {
        "wikimedia/wikipedia": "w " * 400,
        "copy/wikipedia": "w " * 400,
        "a/data": "apple " * 200,
        "b/data": "pear " * 200,
    }
    readme_body = lambda row: bodies[row["dataset_id"]]  # noqa: E731  (self-check stub)
    globals()["readme_body"] = readme_body
    pub = [
        {
            "dataset_id": "seoul_open_data/OA-1",
            "source": "seoul_open_data",
            "licenses": [],
            "readme_chars": 900,
            "card_data": {"pretty_name": "서울교통공사_지하철혼잡도정보"},
        },
        {
            "dataset_id": "data_go_kr/2",
            "source": "data_go_kr",
            "licenses": ["공공누리 제1유형"],
            "readme_chars": 300,
            "card_data": {"pretty_name": "서울교통공사_지하철혼잡도정보"},
        },
    ]
    dup = duplicate_map(hf, pub)
    assert dup["copy/wikipedia"]["canonical"] == "wikimedia/wikipedia"
    assert "a/data" not in dup and "b/data" not in dup  # same generic name, different content
    assert "seoul_open_data/OA-1" not in dup  # the same title on two portals is not proof
    print("dataset_dedup ok")
