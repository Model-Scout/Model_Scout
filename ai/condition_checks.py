"""Per-dataset verdicts on the data conditions a user stated (data_conditions.py), from what the dataset's card
and graph record state. Explains a recommendation; never reorders or removes one.

Each condition is 충족 / 불충족 / 미확인, with the fact it rests on (basis) and what was and was not verified
(scope). A missing fact is 미확인, never 불충족; and some facts never settle a condition:
  - an API address on the portal page is not a successful call
  - the portal's "실시간" update label does not promise current values
  - a card listing only an API does not mean there is no file, nor a file-only listing that there is no API
  - 충북 data does not establish that 청주 is in it
A partial alternative (서울 data for a nationwide request) is told apart from the conditions: the scope stays
불충족 and the dataset carries partial_alternative instead.

Reads only the server's own records (graph entity, v2 card); no golden-set or evaluation file.
"""

from __future__ import annotations

import re
from typing import Any

from hypergraph_search import REGION_CANON, REGIONS

MET, UNMET, UNKNOWN = "충족", "불충족", "미확인"
PORTALS = ("data_go_kr", "seoul_open_data")
FILE_FORMATS = {"csv", "xlsx", "xls", "json", "xml", "shp", "text file", "hwp", "pdf", "zip"}
KOGL_TYPE_RE = re.compile(r"제?\s*([0-4])\s*유형")
_SIDO = sorted({*REGIONS, *REGION_CANON, *(f"{r}{s}" for r in REGIONS for s in ("시", "도", "특별시", "광역시", "특별자치시", "특별자치도"))},
               key=len, reverse=True)
# A 시군구 in a title only right after its 시도 ("충청북도 제천시"): a bare word ending in 시 (도시, 표시) is not a place.
TITLE_PLACE_RE = re.compile(rf"(?:{'|'.join(_SIDO)})\s*([가-힣]{{1,4}}(?:시|군|구))(?![가-힣])")


def _codes(value: str | None) -> list[str]:
    """'API (api), XLSX(엑셀) (xlsx)' -> ['api', 'xlsx']: the code in the last parentheses of each item."""
    out = []
    for item in (value or "").split(", "):
        found = re.findall(r"\(([^()]+)\)\s*$", item)
        if found:
            out.append(found[-1].strip().lower())
    return out


def _check(key, label, status, basis, scope):
    return {"key": key, "label": label, "status": status, "basis": basis, "scope": scope}


def _region_checks(c, entity):
    covered, how = set(entity.get("coverage_regions") or []), entity.get("coverage_status")
    district, title = entity.get("coverage_district"), entity.get("title") or ""
    stated = how == "stated_in_title"
    shown = "/".join(sorted(covered)) or "표시 없음"
    checks, alternative = [], None
    if region := c.get("region"):
        label = f"지역: {region}"
        if region in covered and stated:
            checks.append(_check("region", label, MET, f"제목에 {region}", "제목의 지역명"))
        elif "전국" in covered:
            checks.append(_check("region", label, UNKNOWN, f"전국 자료({'제목에 명시' if stated else '추정'})",
                                 f"{region} 부분이 들어 있는지는 원문 확인"))
        elif covered and stated:
            checks.append(_check("region", label, UNMET, f"제목에 {shown}", "제목의 지역명"))
        elif covered:
            checks.append(_check("region", label, UNKNOWN, f"{shown}로 추정({how})", "추정이라 원문 확인"))
        else:
            checks.append(_check("region", label, UNKNOWN, "지역 범위 표시 없음", "원문 확인"))
    if detail := c.get("region_detail"):
        label = f"세부 지역: {detail}"
        named = [p for p in TITLE_PLACE_RE.findall(title)
                 if not p.startswith(detail) and not p.endswith(("광역시", "특별시", "자치시"))]  # 대구|광역시 is one name
        if detail in title:
            checks.append(_check("region_detail", label, MET, f"제목에 {detail}", "제목의 지역명"))
        elif district and district != detail:
            checks.append(_check("region_detail", label, UNMET, f"제목에 {district}", "제목의 자치구명"))
        elif named:
            checks.append(_check("region_detail", label, UNMET, f"제목에 {', '.join(named)}", "제목의 시군구명"))
        elif c.get("region") and covered and stated and c["region"] not in covered and "전국" not in covered:
            checks.append(_check("region_detail", label, UNMET, f"제목에 {shown}", "제목의 지역명"))
        else:
            what = f"{shown} 자료" if covered else "지역 범위 표시 없음"
            checks.append(_check("region_detail", label, UNKNOWN, what, f"{detail} 포함 여부는 원문 확인"))
    if c.get("region_scope") == "전국":
        label = "전국 범위"
        if "전국" in covered and stated:
            checks.append(_check("region_scope", label, MET, "제목에 전국", "제목의 지역명"))
        elif covered and "전국" not in covered and stated:
            checks.append(_check("region_scope", label, UNMET, f"제목에 {shown}", "제목의 지역명"))
            alternative = f"{shown} 한정 자료 (전국 범위 아님)"
        else:
            what = f"{shown}로 추정({how})" if covered else "지역 범위 표시 없음"
            checks.append(_check("region_scope", label, UNKNOWN, what, "전국 포함 여부는 원문 확인"))
    return checks, alternative


def _delivery_checks(c, facts):
    codes = set(_codes(facts.get("formats")))
    files = sorted(codes & FILE_FORMATS)
    api_status = facts.get("api_status")
    listed = ", ".join(sorted(codes)).upper() or "표시 없음"
    checks = []
    if c.get("delivery") == "api":
        label = "API 제공"
        if api_status and api_status.startswith("미확인"):
            checks.append(_check("delivery", label, UNKNOWN, "API 제공 여부 미확인 (상세 페이지에 주소 없음)", "원 제공처 확인"))
        elif "api" in codes:
            auto = api_status and "자동변환" in api_status
            checks.append(_check("delivery", label, MET,
                                 "파일 자동변환 OpenAPI (내용은 올린 파일과 같음)" if auto else f"포털 등록 형식 {listed}",
                                 "API 주소 등록까지 확인, 실제 호출은 확인하지 않음"))
        elif codes:
            # Not listed is not "not provided": the provider may serve an API elsewhere. Only a stated
            # absence could make this 불충족, and no card states one.
            checks.append(_check("delivery", label, UNKNOWN, f"포털 등록 형식 {listed}에 API 표기 없음",
                                 "API 제공 여부는 원 제공처 확인"))
        else:
            checks.append(_check("delivery", label, UNKNOWN, "제공 방식 표시 없음", "원 제공처 확인"))
    elif c.get("delivery") == "file":
        label = "파일 제공"
        if files:
            checks.append(_check("delivery", label, MET, f"포털 등록 형식 {listed}", "포털 등록 형식"))
        elif codes:
            checks.append(_check("delivery", label, UNKNOWN, "카드에는 API만 있음", "파일 제공 여부는 원 제공처 확인"))
        else:
            checks.append(_check("delivery", label, UNKNOWN, "제공 방식 표시 없음", "원 제공처 확인"))
    for fmt in c.get("formats") or []:
        key = fmt.strip().lower()
        if key in codes:
            checks.append(_check("format", f"{fmt.upper()} 형식", MET, f"포털 등록 형식 {listed}", "포털 등록 형식"))
        else:
            checks.append(_check("format", f"{fmt.upper()} 형식", UNKNOWN, f"포털 등록 형식 {listed}에 {fmt.upper()} 없음",
                                 "다른 경로로 제공하는지 원 제공처 확인"))
    return checks


# Our catalogue is frozen (the refresh pipeline is not scheduled); the providers' own data keeps changing apart
# from it. So a verdict rests on the card as collected, and the provider's present state was not re-checked.
SNAPSHOT = "추천 근거는 고정 수집본 기준, 제공처의 현재 상태는 재확인하지 않음"
# Official sentences about the values' reference time or delay (from facts.limits), quoted as a caution.
TIMING_RE = re.compile(r"기준|지연|\d+\s*일\s*전|갱신")


def _freshness_checks(c, facts):
    """Currentness is a matter of which moment the values are of and how often they change, not of the delivery:
    files can be regenerated and an API can serve old statistics. The portal's update label (실시간, 매일, 연간,
    1회성) does not say what it counts (the values, the file postings or the notice), so it is shown as a
    caution and never decides. 불충족 would need an official statement of the values' reference time or interval
    that conflicts with what the user needs; the cards record no such field yet, so every verdict here is 미확인."""
    portal = facts.get("update_cycle_portal")
    notes = [f"포털 갱신 표기 '{portal or '표시 없음'}'"]
    if "자동변환" in (facts.get("api_status") or ""):
        notes.append("업로드된 파일을 API로 제공하는 방식이라 최신성은 원본 파일 갱신에 의존")
    timing = [s for s in facts.get("limits") or [] if TIMING_RE.search(s)]
    if timing:
        notes.append(f"공식 설명: \"{timing[0][:120]}\"")
    scope = ("포털 표기가 값·파일 게시·안내 중 무엇의 갱신 주기인지 확인되지 않음, "
             f"값의 기준 시점과 반영 지연은 제공처 명세 확인, {SNAPSHOT}")
    checks = []
    if c.get("current_value"):
        checks.append(_check("current_value", "현재 값", UNKNOWN, ", ".join(notes), scope))
    if interval := c.get("update_interval"):
        checks.append(_check("update_interval", f"갱신 간격: {interval}", UNKNOWN, ", ".join(notes), scope))
    return checks


def _license_checks(c, commercial_only, facts, entity):
    checks = []
    if commercial_only:
        use = (_codes(facts.get("commercial_use")) or [None])[0]
        label = "상업 이용"
        basis = facts.get("commercial_use") or "이용 조건 표시 없음"
        status = {"commercial": MET, "non commercial": UNMET}.get(use, UNKNOWN)
        checks.append(_check("commercial", label, status, basis, "카드의 라이선스 분류, 이용허락 원문은 제공처 확인"))
    if c.get("kogl_type1_only"):
        # As the golden set decided (2026-11-09): only 공공누리 제1유형 without third-party rights meets it;
        # any other stated wording, '이용허락범위 제한 없음' included, does not.
        text = " ".join(str(x) for x in entity.get("licenses") or [])
        status = (UNKNOWN if not text else
                  MET if set(KOGL_TYPE_RE.findall(text)) == {"1"} and "제3자" not in text else UNMET)
        checks.append(_check("kogl_type1_only", "공공누리 1유형", status,
                             f"이용허락 '{text}'" if text else "이용허락 표기 없음", "포털의 이용허락 표기"))
    return checks


def judge(conditions: dict[str, Any], commercial_only: bool, entity: dict[str, Any], facts: dict[str, Any]) -> dict[str, Any]:
    """{"checks": [...], "partial_alternative": str | None} for one dataset; checks is empty when the user
    stated no data condition. Only portal datasets are judged: the rules read portal card facts."""
    if (entity.get("source") or "") not in PORTALS:
        return {"checks": [], "partial_alternative": None}
    if facts.get("unavailable"):
        return {"checks": [_check("card", "데이터 카드", UNKNOWN, facts["unavailable"], "조건을 확인하지 못함")],
                "partial_alternative": None}
    region, alternative = _region_checks(conditions, entity)
    checks = region + _delivery_checks(conditions, facts) + _freshness_checks(conditions, facts)
    checks += _license_checks(conditions, commercial_only, facts, entity)
    return {"checks": checks, "partial_alternative": alternative}


def unread(reason: str) -> dict[str, Any]:
    """The verdict when the user's conditions could not be read: not 'no conditions', but not checked."""
    return {"checks": [_check("conditions", "요청 조건", UNKNOWN, "요청 조건을 읽지 못했어요",
                              f"조건 충족 여부를 확인하지 않음 ({reason})")], "partial_alternative": None}
