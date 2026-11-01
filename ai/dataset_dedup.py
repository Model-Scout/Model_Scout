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
  public        same title once org prefixes (서울특별시_, 서울교통공사_), districts (강서구), dates,
                years and translated editions are stripped, so a 25-district series is one entry
                listing its members. Canonical: known license, then city-wide over a district,
                then the longer card.
  same owner    one author on both sites with README overlap >= 25% (podongchip's KOSPI features).
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


def _public_groups(rows, groups, reasons):
    by_title = defaultdict(list)
    for row in rows:
        key = title_key((row.get("card_data") or {}).get("pretty_name"))
        if key:
            by_title[key].append(row["dataset_id"])
    for ids in by_title.values():
        for other in ids[1:]:
            groups.union(other, ids[0])
            reasons[other] = "same title (org prefix / year stripped)"


PORTAL_SOURCES = {"seoul_open_data", "data_go_kr"}


def duplicate_map(hf_rows, public_rows):
    """dataset_id -> {"canonical": id, "reason": str} for every non-canonical member."""
    groups, reasons = _Groups(), dict[str, str]()
    _hf_groups(hf_rows, groups, reasons)
    _public_groups(public_rows, groups, reasons)
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
    assert dup["seoul_open_data/OA-1"]["canonical"] == "data_go_kr/2"  # licensed copy wins
    print("dataset_dedup ok")
