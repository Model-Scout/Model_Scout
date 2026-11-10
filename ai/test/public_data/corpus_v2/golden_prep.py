"""Prepare public golden-set review on corpus v2: what to judge, its evidence, and proposals kept apart.

Labels (labels/, reports/) are read, never written. Every score here is a proposal; a person decides.

Writes, under corpus_v2/golden_prep/:
  review_items.jsonl        for judging: query, conditions and the dataset's full card facts only,
                            with an empty judgment. No rank, search mode or proposal in it.
  review_context.jsonl      why each item is on the list (new unjudged / existing hold / high
                            review), the existing judgment, and where the search found it
  review_suggestions.jsonl  automatic condition checks (met / partial / unmet / unknown), topic
                            word match and a proposal
  prelim_top10.jsonl        the preliminary search itself (discovery)
  prelim_summary.json       counts by scope and label state, and the exact search settings
  proposed_queries.jsonl    proposed district / language / period / spatial-unit queries, with the
                            same three parts kept apart (facts, suggestions, discovery)

Search modes share the question embedding and the golden filters; they differ in keywords:
  question_only  rank_datasets(concepts=[], query_vector=question, commercial_only, roles=["service"])
  pool_terms     as 22_eval_recommendations._public_top: + concepts/keywords from the label's
                 dataset_terms (= the query's pool_terms) and the region condition
Delivery, realtime and the p026 type-1 condition are not passed to the ranker in either mode.

Query vectors come from the local cache; a query missing there stops the run unless --allow-embed.

    python test/public_data/corpus_v2/golden_prep.py
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUBLIC = HERE.parent
AI = PUBLIC.parents[1]
sys.path.insert(0, str(AI))

import hypergraph_search as hs  # noqa: E402
from taxonomy import normalize  # noqa: E402

OUT = HERE / "golden_prep"
QUERIES = PUBLIC / "labels" / "public_data_queries.jsonl"
GOLDEN = PUBLIC / "labels" / "public_data_golden.jsonl"
DECISIONS = PUBLIC / "reports" / "public_judgment_decisions.jsonl"
WORKSHEET = PUBLIC / "reports" / "public_pool_worksheet.csv"
REVIEW = HERE / "golden_review.jsonl"
RELATIONS = HERE / "id_relations.jsonl"
ENRICHED = AI / "data" / "public_enriched" / "public_datasets.jsonl"
VECTOR_CACHE = AI / "data" / "dataset_index_v2" / "query_vectors.jsonl"
K = 10
MODES = ("question_only", "pool_terms")
PORTALS = ("seoul_open_data/", "data_go_kr/")
WORD_RE = re.compile(r"[가-힣A-Za-z0-9]{2,}")
TYPE1_ONLY_RE = re.compile(r"공공누리\s*제?\s*1\s*유형")
KOGL_TYPE_RE = re.compile(r"제?\s*([0-4])\s*유형")
REALTIME_HINT_RE = re.compile(r"실시간|현재|측정\s*시각|측정일시|갱신\s*시각|기준\s*시각|수신\s*시각|도착\s*예정")
# Words that say nothing about the topic: places and generic catalogue words.
GENERIC = {"위치", "정보", "현황", "데이터", "목록", "좌표", "현재", "서비스", "조회", "전국", "지역", "필요", "제공",
           "주소", "운영", "시간", "종류", "구분", "기준", "자료", "내역", "상세"}
MET, PARTIAL, UNMET, UNKNOWN = "충족", "부분", "불충족", "미확인"
# Not a condition: a fact the reviewer weighs against what the question is for (e.g. the area a
# dataset covers when the question names none). It never moves the proposal by itself.
PURPOSE = "목적 판단"
# 0-point reason per failed check; the last four are proposals for the new query kinds.
FAIL_REASON = {"region": "wrong_region", "commercial": "license", "kogl_type1_only": "license",
               "delivery": "wrong_delivery", "district": "wrong_region", "language": "wrong_language(제안)",
               "period": "wrong_period(제안)", "spatial_unit": "wrong_spatial_unit(제안)"}


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


# ---------------------------------------------------------------- facts (full, uncut)


def seoul_fields(readme_text):
    """Every '## 제공 필드' line as written: name, English name and explanation."""
    if "## 제공 필드" not in readme_text:
        return []
    return [line[2:] for line in readme_text.split("## 제공 필드", 1)[1].splitlines() if line.startswith("- ")]


def facts(entity, row, readme_text=""):
    """Card facts for judging, nothing cut and nothing inferred beyond what v2 recorded."""
    licenses = row.get("licenses") or []
    official = row.get("official") or {}
    return {
        "title": (row.get("card_data") or {}).get("pretty_name") or entity.get("title"),
        "source": row.get("source") or entity.get("source"),
        "url": row.get("url"),
        "publisher": entity.get("publisher"),
        "publisher_region": entity.get("publisher_region"),
        "coverage_regions": entity.get("coverage_regions") or [],
        "coverage_status": entity.get("coverage_status"),
        "coverage_district": entity.get("coverage_district"),
        "period": entity.get("period") or [],
        "language_edition": entity.get("language_edition"),
        "spatial_unit": entity.get("spatial_unit") or [],
        "series_id": entity.get("series_id"),
        "formats": row.get("formats") or [],
        "licenses": licenses,
        "commercial_use": normalize("commercial_use", licenses[0]) if licenses else None,
        "license_text": official.get("license_text"),
        "official_status": official.get("status"),
        "official_verification": official.get("verification"),
        "official_checked_at": official.get("checked_at"),
        "update_cycle_portal": row.get("update_cycle"),
        "last_modified": row.get("last_modified"),
        "category": row.get("category"),
        "keywords": row.get("tags") or [] if row.get("source") == "data_go_kr" else [],
        "fields": seoul_fields(readme_text) if row.get("source") == "seoul_open_data" else [],
        "field_count": row.get("field_count"),
        "regional_variants": row.get("regional_variants") or [],
        "regional_variant_count": row.get("regional_variant_count"),
        "description": row.get("description") or "",
    }


# ---------------------------------------------------------------- automatic checks


def check(status, basis):
    return {"status": status, "basis": basis}


def condition_checks(query, f, extension=None):
    """Each required condition of the query, judged from the card: met / partial / unmet / unknown."""
    cond, checks = query["conditions"], {}
    covered, status = set(f["coverage_regions"]), f["coverage_status"]
    region = cond.get("region")
    if region:
        if region in covered and status == "stated_in_title":
            checks["region"] = check(MET, f"제목에 {region}")
        elif region in covered:
            checks["region"] = check(UNKNOWN, f"{region}로 추정({status}), 원문 확인")
        elif "전국" in covered:
            checks["region"] = check(PARTIAL, "전국 데이터: README 기준 요청 지역을 포함하면 1점")
        elif covered and status == "stated_in_title":
            checks["region"] = check(UNMET, f"제목에 {sorted(covered)}, 요청 {region}")
        elif covered:
            checks["region"] = check(UNKNOWN, f"추정 범위 {sorted(covered)}({status})가 요청 {region}와 다름, 원문 확인")
        else:
            checks["region"] = check(UNKNOWN, "지역 범위 미확인")
    else:
        # No region named is not a nationwide requirement: whether a local dataset serves the
        # question depends on what the question is for, which the reviewer decides.
        scope = ("전국" if "전국" in covered else f"{sorted(covered)} ({status})" if covered else "범위 표시 없음")
        checks["region_scope"] = check(PURPOSE, f"지역 미지정 질문. 데이터 범위: {scope}. 질문 목적에 비춰 판단")
    if cond.get("commercial"):
        use = f["commercial_use"]
        if use == "commercial":
            checks["commercial"] = check(MET, f["license_text"] or str(f["licenses"]))
        elif use == "non_commercial":
            checks["commercial"] = check(UNMET, f["license_text"] or str(f["licenses"]))
        else:
            checks["commercial"] = check(UNKNOWN, f"이용 조건 확인 필요: {f['license_text'] or '라이선스 미확인'}")
    if TYPE1_ONLY_RE.search(query["query"]):  # p026: "공공누리 1유형 데이터만" — read literally
        checks["kogl_type1_only"] = kogl_type1_check(f["license_text"])
    delivery = cond.get("delivery")
    formats = set(f["formats"])
    # An API or file the question requires is a hard condition: the other kind does not meet it.
    if delivery == "api":
        checks["delivery"] = (check(MET, f"제공 방식 {sorted(formats)}") if "api" in formats else
                              check(UNMET, f"API 필수인데 {sorted(formats)}만 제공") if formats else
                              check(UNKNOWN, "제공 방식 미확인"))
    elif delivery == "file":
        files = formats - {"api"}
        checks["delivery"] = (check(MET, f"파일 {sorted(files)}") if files else
                              check(UNMET, "파일 필수인데 API만 제공") if formats else
                              check(UNKNOWN, "제공 방식 미확인"))
    if cond.get("realtime"):
        hints = [x for x in f["fields"] + f["keywords"] if REALTIME_HINT_RE.search(x)]
        checks["realtime"] = check(UNKNOWN, f"포털 표기 '{f['update_cycle_portal'] or '없음'}'는 근거로 쓰지 않음. "
                                            f"현재값 필드 확인 필요 (단서 필드 {hints[:5] or '없음'})")
    for key, wanted in (extension or {}).items():
        checks[key] = extension_check(key, wanted, f)
    return checks


def kogl_type1_check(text):
    """The question accepts 공공누리 제1유형 only (decided 2026-11-09: the condition is kept as
    written), so any other wording, including 'no restriction', does not meet it."""
    if not text:
        return check(UNKNOWN, "이용허락 문구 미확인")
    if "제3자" in text:
        return check(UNMET, f"'{text}': 제3자 권리가 포함돼 출처표시만으로 쓰는 1유형이 아님")
    types = set(KOGL_TYPE_RE.findall(text))
    if types == {"1"}:
        return check(MET, text)
    return check(UNMET, f"'{text}': 공공누리 1유형이 아님" + (f" ({sorted(types)}유형)" if types else ""))


def extension_check(key, wanted, f):
    """district / language / period / spatial unit; no mark on the card is unknown, never a default."""
    if key == "district":
        have = f["coverage_district"]
        return (check(UNKNOWN, "자치구 표시 없음 (서울 전체인지 미확인)") if not have else
                check(MET, have) if have == wanted else check(UNMET, f"{have}"))
    if key == "language":
        have = f["language_edition"]
        return (check(UNKNOWN, "언어판 표시 없음 (한국어판으로 단정하지 않음)") if not have else
                check(MET, have) if have == wanted else check(UNMET, f"{have}판"))
    if key == "period":
        have, want = set(f["period"]), set(wanted.split("-"))
        return (check(UNKNOWN, "기간 표시 없음") if not have else
                check(MET, f"{sorted(have)}") if want <= have else check(UNMET, f"기간 {sorted(have)}"))
    if key == "spatial_unit":
        have = f["spatial_unit"]
        return (check(UNKNOWN, "공간 단위 표시 없음") if not have else
                check(MET, f"{have}") if wanted in have else check(UNMET, f"단위 {have}"))
    raise ValueError(key)


def content_words(text):
    regions = hs.REGIONS + ("서울시", "서울특별시")
    return [w for w in WORD_RE.findall(text) if w not in GENERIC and not any(w.startswith(r) for r in regions)]


def topic_match(query, f):
    haystack = " ".join([f["title"] or "", f["description"], " ".join(f["fields"]), " ".join(f["keywords"]),
                         f["category"] or ""])
    full, partial, unscored = [], [], []
    for aspect in query.get("aspects") or []:
        words = content_words(aspect)
        hit = [w for w in words if w in haystack]
        if not words:
            unscored.append(aspect)
        elif len(hit) == len(words):
            full.append(aspect)
        elif hit:
            partial.append({"aspect": aspect, "found": hit})
    # Without a field list a missing word says the card is short, not that the data lacks it.
    return {"full": full, "partial": partial, "unscored": unscored, "scored": len(query.get("aspects") or []) - len(unscored),
            "field_list": bool(f["fields"])}


def propose(query, checks, topic):
    """A proposal from the checks, in this order:

    unmet condition -> 0; no topic word -> off-topic or hold; anything unknown -> hold (missing
    information is never a 1); evidence of a partial fit -> 1; otherwise 2. Facts left to the
    question's purpose (PURPOSE) are attached for the reviewer and change nothing here.
    """
    unmet = [k for k, c in checks.items() if c["status"] == UNMET]
    unknown = [k for k, c in checks.items() if c["status"] == UNKNOWN]
    partial = [k for k, c in checks.items() if c["status"] == PARTIAL]
    purpose = [k for k, c in checks.items() if c["status"] == PURPOSE]
    basis = []
    if query.get("expected_behavior") == "abstain":
        basis.append("기권 질의: 관련 데이터라면 질의 자체를 다시 봐야 함")
    if purpose:
        basis.append(f"목적 판단 필요: {purpose} (점수를 자동으로 바꾸지 않음)")
    if unmet:
        reasons = sorted({FAIL_REASON[k] for k in unmet})
        return {"proposal": f"0 후보 ({', '.join(reasons)})", "basis": basis + [f"불충족: {unmet}"]}
    if not topic["full"] and not topic["partial"]:
        return {"proposal": "0 off_topic 또는 보류", "basis": basis + ["요구 항목 단어가 카드에 없음 (단어 일치일 뿐)"]}
    missing_aspects = len(topic["full"]) < topic["scored"]
    if missing_aspects and not partial and not topic.get("field_list", True):
        unknown = unknown + ["aspects (필드 목록 없음)"]
    if unknown:
        return {"proposal": f"보류 (확인 필요: {', '.join(unknown)})",
                "basis": basis + ["정보가 부족하면 점수를 제안하지 않음 (1점도 아님)"]}
    if partial or missing_aspects:
        why = [f"조건 {partial}" if partial else None,
               f"요구 항목 {len(topic['full'])}/{topic['scored']}만 확인" if len(topic["full"]) < topic["scored"] else None]
        return {"proposal": "1 후보 (부분 적합)", "basis": basis + [w for w in why if w]}
    return {"proposal": "2 후보", "basis": basis + ["필수 조건 모두 충족, 요구 항목 단어 모두 확인"]}


def suggestion(query, f, extension=None):
    checks = condition_checks(query, f, extension)
    topic = topic_match(query, f)
    return {"checks": checks, "topic": topic, **propose(query, checks, topic)}


# ---------------------------------------------------------------- search (discovery)


def search(label, vector, mode):
    """One preliminary search. Returns (results, settings actually passed to the ranker)."""
    commercial = bool(label["conditions"].get("commercial"))
    settings = {"query_vector": "question embedding", "commercial_only": commercial, "roles": ["service"], "limit": K}
    if mode == "question_only":
        settings.update(concepts=[], keywords=[])
        rows = hs.rank_datasets([], query_vector=vector, commercial_only=commercial, roles=["service"], limit=K)
    else:  # mirror of 22_eval_recommendations._public_top
        terms = list(label["dataset_terms"])
        if region := label["conditions"].get("region"):
            terms.append(region)
        concepts = hs.concepts_from_terms(terms)
        settings.update(concepts=sorted(concepts), keywords=terms)
        rows = hs.rank_datasets(concepts, query_vector=vector, commercial_only=commercial, roles=["service"],
                                limit=K, keywords=terms)
    settings["not_passed"] = [k for k in ("delivery", "realtime") if label["conditions"].get(k) not in (None, False, "any")]
    return rows, settings


def query_vectors(queries, allow_embed):
    model = hs.query_model()
    key = lambda text: hashlib.sha256(f"{model}\n{text}".encode()).hexdigest()  # noqa: E731
    cache = {r["key"]: r["vector"] for r in read_jsonl(VECTOR_CACHE)} if VECTOR_CACHE.exists() else {}
    missing = [q for q in queries if key(q["query"]) not in cache]
    if missing and not allow_embed:
        raise SystemExit("질의 벡터 캐시에 없는 질의가 있어 API 호출이 필요함 (실행하지 않음): "
                         + ", ".join(q["query_id"] for q in missing))
    for q in missing:
        cache[key(q["query"])] = hs._embed_query(q["query"], model)
    if missing:
        write_jsonl(VECTOR_CACHE, [{"key": k, "vector": v} for k, v in cache.items()])
    return {q["query_id"]: cache[key(q["query"])] for q in queries}, len(missing)


def label_state(label, dataset_id, v1_canonical):
    if not dataset_id.startswith(PORTALS):
        return "비공공데이터"
    if dataset_id in label["relevant"]:
        return f"정답 {label['relevant'][dataset_id]}점"
    if dataset_id in label["must_exclude"]:
        return "제외 0점"
    if dataset_id in label["judged_irrelevant"]:
        return "오답 0점"
    if dataset_id in label["unjudged"]:
        return "보류"
    canonical = v1_canonical.get(dataset_id)
    judged = canonical and (canonical in label["relevant"] or canonical in label["must_exclude"] + label["judged_irrelevant"])
    return "미판정 (v1 판정 데이터의 분리 사본)" if judged else "미판정"


# ---------------------------------------------------------------- review list


def build_review(queries, labels, decisions, top, high_rows, worksheet, v1_canonical, fact_of):
    """(items, context, suggestions) for every new unjudged result, existing hold and high-review row."""
    sources, discovery = defaultdict(set), defaultdict(dict)
    for t in top:
        key = (t["query_id"], t["dataset_id"])
        if t["label_state"].startswith("미판정"):
            sources[key].add("new_unjudged")
        if key in sources or t["label_state"] == "보류":
            discovery[key][t["mode"]] = t["rank"]
    for qid, label in labels.items():
        for did in label["unjudged"]:
            sources[(qid, did)].add("existing_hold")
    high_by_key = {(r["query_id"], r["dataset_id"]): r for r in high_rows}
    for key in high_by_key:
        sources[key].add("high_review")
    surfaced = defaultdict(set)
    for t in top:
        surfaced[t["query_id"]].add(t["dataset_id"])

    items, context, suggestions = [], [], []
    for qid, did in sorted(sources):
        query, review_id = queries[qid], f"{qid}|{did}"
        f = fact_of(did)
        items.append({
            "review_id": review_id,
            "query_id": qid,
            "query": query["query"],
            "query_type": query["query_type"],
            "conditions": query["conditions"],
            "aspects": query.get("aspects"),
            "expected_behavior": query["expected_behavior"],
            "dataset_id": did,
            "facts": f,
            "judgment": {"score": None, "reason": None, "note": None},
        })
        decision = decisions.get((qid, did))
        ctx = {
            "review_id": review_id,
            "review_sources": sorted(sources[(qid, did)]),
            "existing_judgment": {k: decision.get(k) for k in ("score", "reason", "note", "judge", "judged_on")} if decision else None,
            "discovery": discovery.get((qid, did)) or None,
            "v1_canonical": v1_canonical.get(did),
        }
        sug = {"review_id": review_id, **suggestion(query, f)}
        if (qid, did) in high_by_key:
            row = high_by_key[(qid, did)]
            copies = row.get("v1_copies_now_separate") or []
            ctx["high_review"] = {
                "reasons": row["review_reasons"],
                "worksheet_regions_shown": worksheet.get((qid, did)),
                "v1_copies_now_separate": copies,
                "v1_copies_in_prelim_top10": [c for c in copies if c in surfaced[qid]],
            }
            sug["high_review_note"] = high_note(row, decision, f)
        context.append(ctx)
        suggestions.append(sug)
    return items, context, suggestions


def high_note(row, decision, f):
    notes = []
    if "card_national_but_publisher_is_local_government" in row["review_reasons"]:
        notes.append(f"1차 판정 때는 전국으로 보였음. v2: 제공기관 {f['publisher']}, 범위 {f['coverage_regions'] or '미확인'}"
                     f"({f['coverage_status']}). 실제 수록 지역은 설명·필드로 확인")
        notes.append("1차 판정의 '전국' 근거는 바뀌었지만 점수를 일괄로 내리지 않음. "
                     "질문 목적에 이 지역 데이터로 충분한지 판단")
    if "v1_copies_now_separate" in row["review_reasons"]:
        notes.append("이 행의 판정은 이 ID에만 적용됨. 분리된 사본은 정답으로 대체하지 않고 따로 판정")
    return notes


# ---------------------------------------------------------------- proposed queries

PROPOSALS = [
    ("d1", "district", "서울 도봉구의 모범음식점 지정 현황 데이터가 필요해. 다른 구 자료는 필요 없어.",
     {"region": "서울"}, {"district": "도봉구"}, ["도봉구 모범음식점 목록"], ["모범음식점"], ["seoul_open_data/OA-10063"]),
    ("d2", "district", "강서구에 등록된 대부업체 현황을 정리해서 지역 금융 안내 서비스를 만들고 싶어.",
     {"region": "서울"}, {"district": "강서구"}, ["강서구 대부업 등록 현황"], ["대부업"], ["seoul_open_data/OA-10019"]),
    ("d3", "district", "광진구 스마트보안등 IoT 측정값으로 야간 조도 대시보드를 만들려고 해.",
     {"region": "서울"}, {"district": "광진구"}, ["광진구 스마트보안등 측정값"], ["스마트보안등", "보안등"], ["seoul_open_data/OA-15961"]),
    ("d4", "district", "양천구 주민에게 동네 문화시설을 추천하는 앱을 만들고 싶어. 양천구 문화시설 목록이 필요해.",
     {"region": "서울"}, {"district": "양천구"}, ["양천구 문화시설 목록"], ["문화시설"], ["seoul_open_data/OA-22032"]),
    ("d5", "district", "강북구 전통시장 위치와 목록을 받고 싶어.",
     {"region": "서울"}, {"district": "강북구"}, ["강북구 전통시장 목록·위치"], ["전통시장"], ["seoul_open_data/OA-11624"]),
    ("l1", "language", "외국인 관광객용 앱에 넣을 서울 전통시장 정보를 영어 데이터로 받고 싶어.",
     {"region": "서울"}, {"language": "en"}, ["영문 서울 전통시장 정보"], ["전통시장"], ["seoul_open_data/OA-13036"]),
    ("l2", "language", "중국인 관광객 안내에 쓸 서울 문화시설 목록을 중국어(간체)로 구하고 싶어.",
     {"region": "서울"}, {"language": "zh"}, ["중국어 서울 문화시설 목록"], ["문화시설"], ["seoul_open_data/OA-13078"]),
    ("l3", "language", "외국인용 서울 혼잡도 안내에 쓸 실시간 인구 데이터를 영문판으로 받고 싶어.",
     {"region": "서울", "realtime": True}, {"language": "en"}, ["영문 실시간 인구 혼잡도"], ["실시간 인구"],
     ["seoul_open_data/OA-22270", "data_go_kr/15146171"]),
    ("l4", "language", "서울 실시간 도시데이터의 영문판이 있으면 외국인 지도 앱에 붙이고 싶어.",
     {"region": "서울", "realtime": True}, {"language": "en"}, ["영문 실시간 도시데이터"], ["실시간 도시데이터"], ["seoul_open_data/OA-22714"]),
    ("y1", "period", "서울 2007년 연평균기온 위치정보 데이터가 필요해.",
     {"region": "서울"}, {"period": "2007"}, ["2007년 연평균기온 공간 분포"], ["연평균기온"], ["seoul_open_data/OA-348"]),
    ("y2", "period", "2015년 기준 노동조합 현황 통계를 찾고 있어.",
     {}, {"period": "2015"}, ["2015년 노동조합 현황"], ["노동조합"], ["data_go_kr/15056900"]),
    ("y3", "period", "동작구 환경 지도점검 내역을 2010년부터 2017년까지 받고 싶어.",
     {"region": "서울"}, {"district": "동작구", "period": "2010-2017"}, ["동작구 환경 지도점검 내역 2010~2017"], ["환경 지도점검"],
     ["seoul_open_data/OA-10586"]),
    ("s1", "spatial_unit", "집계구 단위 서울 생활인구(내국인) 데이터로 골목 상권을 분석하려고 해.",
     {"region": "서울"}, {"spatial_unit": "집계구"}, ["집계구별 내국인 생활인구"], ["생활인구"], ["seoul_open_data/OA-14979"]),
    ("s2", "spatial_unit", "자치구 단위로 집계된 서울 단기체류 외국인 생활인구가 필요해.",
     {"region": "서울"}, {"spatial_unit": "자치구"}, ["자치구별 단기체류 외국인 생활인구"], ["생활인구", "단기체류 외국인"],
     ["seoul_open_data/OA-15441"]),
]


def proposed_query(spec):
    pid, kind, text, conditions, extension, aspects, pool_terms, targets = spec
    return {
        "query_id": f"new_{pid}",
        "status": "제안 (질의 파일에 추가하지 않음, 라벨 아님)",
        "query_type": "constrained",
        "variant_kind": kind,
        "query": text,
        "conditions": {"region": None, "delivery": "any", "realtime": False, "commercial": False, **conditions},
        "conditions_extension": extension,
        "aspects": aspects,
        "pool_terms": pool_terms,
        "expected_behavior": "recommend",
        # The designer's hypothesis of the answer, not evidence: suggestions ignore it.
        "designer_targets": targets,
    }


def build_proposals(series, fact_of, v1_canonical, vectors, labels_for_search):
    by_member = {m: g for g in series for m in g["members"]}
    out = []
    for spec in PROPOSALS:
        q = proposed_query(spec)
        group = by_member.get(q["designer_targets"][0])
        members = sorted(set(group["members"] if group else []) | set(q["designer_targets"]))
        discovery = {}
        for mode in MODES:
            rows, settings = search(labels_for_search(q), vectors[q["query_id"]], mode)
            found = [r["dataset"] for r in rows]
            discovery[mode] = {"settings": settings, "top10": found,
                               "designer_target_ranks": {t: found.index(t) + 1 if t in found else None for t in q["designer_targets"]}}
        out.append({
            **q,
            "series_id": group["series_id"] if group else None,
            "candidates": [{"dataset_id": m, "facts": fact_of(m), "v1_merged_into": v1_canonical.get(m)} for m in members],
            "suggestions": [{"dataset_id": m, **suggestion(q, fact_of(m), q["conditions_extension"])} for m in members],
            "discovery": discovery,
        })
    return out


# ---------------------------------------------------------------- main


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--allow-embed", action="store_true", help="embed queries missing from the vector cache (API call)")
    args = parser.parse_args()
    identity = hs.use_corpus("v2")
    queries = {q["query_id"]: q for q in read_jsonl(QUERIES)}
    labels = {g["query_id"]: g for g in read_jsonl(GOLDEN)}
    decisions = {(d["query_id"], d["dataset_id"]): d for d in read_jsonl(DECISIONS)}
    v1_canonical = {r["dataset_id"]: r["v1_canonical"] for r in read_jsonl(RELATIONS)}
    rows = {r["dataset_id"]: r for r in read_jsonl(ENRICHED)}
    entities = {e["name"]: e for e in hs.load_graph()[0].values() if e["kind"] == "dataset"}
    with open(WORKSHEET, encoding="utf-8-sig", newline="") as f:
        worksheet = {(r["query_id"], r["dataset_id"]): r["regions"] for r in csv.DictReader(f)}

    def fact_of(did):
        row = rows.get(did, {})
        readme = AI / row["readme_path"] if row.get("readme_path") else None
        return facts(entities.get(did, {}), row, readme.read_text(encoding="utf-8") if readme and readme.is_file() else "")

    proposals = [proposed_query(s) for s in PROPOSALS]
    vectors, embedded = query_vectors(list(queries.values()) + proposals, args.allow_embed)

    top, settings_used, summary = [], {}, {m: Counter() for m in MODES}
    non_public = defaultdict(list)
    for qid, label in labels.items():
        for mode in MODES:
            results, settings = search(label, vectors[qid], mode)
            settings_used.setdefault(mode, []).append({"query_id": qid, **settings})
            for rank, r in enumerate(results, 1):
                state = label_state(label, r["dataset"], v1_canonical)
                top.append({"query_id": qid, "mode": mode, "rank": rank, "dataset_id": r["dataset"],
                            "title": r["title"], "score": r["score"], "dense": r["dense"], "label_state": state})
                summary[mode]["results"] += 1
                if state == "비공공데이터":
                    non_public[mode].append(f"{qid}|{r['dataset']}")
                else:
                    summary[mode][state.split(" (")[0]] += 1

    high_rows = [r for r in read_jsonl(REVIEW) if r["review_priority"] == "high"]
    items, context, suggestions = build_review(queries, labels, decisions, top, high_rows, worksheet, v1_canonical, fact_of)
    series = json.loads((AI / "data" / "hypergraph_v2" / "series.json").read_text(encoding="utf-8"))
    proposed = build_proposals(series, fact_of, v1_canonical, vectors, lambda q: {**q, "dataset_terms": q["pool_terms"]})

    OUT.mkdir(exist_ok=True)
    for stale in ("unjudged_candidates.jsonl", "high_review_evidence.jsonl"):  # replaced by the three review files
        (OUT / stale).unlink(missing_ok=True)
    write_jsonl(OUT / "prelim_top10.jsonl", top)
    write_jsonl(OUT / "review_items.jsonl", items)
    write_jsonl(OUT / "review_context.jsonl", context)
    write_jsonl(OUT / "review_suggestions.jsonl", suggestions)
    write_jsonl(OUT / "proposed_queries.jsonl", proposed)
    report = {
        "note": "예비 검색이다. 미판정이 섞여 있어 성능 수치로 해석하지 않는다. 제안은 판정이 아니다.",
        "corpus": identity,
        "query_vectors_embedded_this_run": embedded,
        "search_settings": {
            "question_only": "rank_datasets(concepts=[], query_vector=질문 임베딩, commercial_only=골든 conditions.commercial, "
                             "roles=['service'], limit=10, keywords=[])",
            "pool_terms": "rank_datasets(concepts_from_terms(dataset_terms + [conditions.region]), query_vector=질문 임베딩, "
                          "commercial_only=골든 conditions.commercial, roles=['service'], limit=10, "
                          "keywords=dataset_terms + [conditions.region])  # 22_eval_recommendations._public_top과 같음",
            "not_passed_to_ranker": "delivery, realtime, p026의 공공누리 1유형 한정 조건",
            "queries_with_commercial_filter": sorted(q for q, l in labels.items() if l["conditions"].get("commercial")),
            "queries_with_region_keyword_pool_terms_only": sorted(q for q, l in labels.items() if l["conditions"].get("region")),
            "per_query": settings_used,
        },
        "top10_by_mode": {
            m: {"results": c["results"],
                "public": {k: v for k, v in c.items() if k != "results"},
                "non_public": len(non_public[m]), "non_public_items": non_public[m]}
            for m, c in summary.items()
        },
        "review_list": {
            "items": len(items),
            "by_source": dict(Counter(s for c in context for s in c["review_sources"])),
            "existing_hold_total": sum(len(l["unjudged"]) for l in labels.values()),
            "proposals": dict(Counter(s["proposal"].split(" (")[0] for s in suggestions)),
            "checks_unknown": dict(Counter(k for s in suggestions for k, c in s["checks"].items() if c["status"] == UNKNOWN)),
        },
        "proposed_queries": len(proposed),
    }
    (OUT / "prelim_summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "search_settings"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
