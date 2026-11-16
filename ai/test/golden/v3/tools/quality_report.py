#!/usr/bin/env python3
"""질문 품질 보고서(reports/quality_report.md·.json)와 질문 검수 문서(review/QUESTION_REVIEW.md)를 만든다.

분포는 기계가 세지만 "실제 사용자가 물을 법한가"는 기계가 판정할 수 없다. 그래서 질문마다
사람이 체크할 칸을 두고, 기계가 찾을 수 있는 신호(반복 문형, 모델명 노출, 길이)만 힌트로 붙인다.

    python test/golden/v3/tools/quality_report.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
from make_worksheet import STYLE, TYPE_TITLES, read_jsonl  # noqa: E402
from build_drafts import DRAFTS  # noqa: E402
from queries_loader import STYLE_QUOTA_EXEMPTIONS  # noqa: E402

REPORTS = corpus.V3 / "reports"
# 모델명을 지목하는 것이 질문의 본질인 유형. 그 밖의 유형에서 모델명이 보이면 정답 유도 신호다.
NAME_TYPES = {"lexical_exact", "model_comparison"}
MODEL_NAME_RE = re.compile(
    r"(?i)\b(kosimcse|sroberta|kanana|exaone|bllossom|polyglot|whisper|nllb|m2m100|madlad|opus-mt|kure|bge|e5|"
    r"midm|varco|solar|qwen|gemma(?! ?라이선스)|llama(?!\.cpp)|sensevoice|tri-\d)")
NUMERIC_KEYS = {"min_parameters_billion", "max_parameters_billion", "min_context_length", "max_context_length"}


def table(headers: List[str], rows: List[List[Any]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def pct(n: int, total: int) -> str:
    return f"{n} ({n / total:.0%})" if total else "0"


def collect(drafts: List[Mapping[str, Any]]) -> Dict[str, Any]:
    total = len(drafts)
    by_type: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for d in drafts:
        by_type[d["query_type"]].append(d)
    keys = Counter(k for d in drafts for k in d["conditions"])
    proposed = [c for d in drafts for c in d["candidates"] if c["proposed_grade"]]
    stage_of = Counter((c.get("evidence") or {}).get("stage") for c in proposed)
    families = Counter(c["canonical_model_id"] for c in proposed)
    data = {
        "total": total,
        "per_type": {t: len(v) for t, v in by_type.items()},
        "style": dict(Counter(d["expression_style"] for d in drafts)),
        "style_by_type": {t: dict(Counter(d["expression_style"] for d in v)) for t, v in by_type.items()},
        "persona": dict(Counter(d["persona"] for d in drafts).most_common()),
        "difficulty": dict(Counter(d["difficulty"] for d in drafts)),
        "difficulty_by_type": {t: dict(Counter(d["difficulty"] for d in v)) for t, v in by_type.items()},
        "condition_keys": dict(keys.most_common()),
        "proposed_pool": dict(Counter(c["source_pool"] for c in proposed)),
        "proposed_pool_by_grade": {g: dict(Counter(c["source_pool"] for c in proposed if c["proposed_grade"] == g)) for g in (2, 1)},
        "proposed_evidence_stage": dict(stage_of.most_common()),
        "top_families": dict(families.most_common(15)),
        "per_query": [{
            "query_id": d["query_id"], "eligible": d["eligible_count"], "review": d["review_count"],
            "grade_2": d["classification"]["proposed_grade_2"], "grade_1": d["classification"]["proposed_grade_1"],
            "unresolved": d["classification"]["unresolved_for_human"], "unknown_excluded": d["unknown_excluded"],
            "max_family": max(Counter(c["canonical_model_id"] for c in d["candidates"]).values(), default=0),
        } for d in drafts],
        "abstention": [{"query_id": d["query_id"], "near_miss": {k: len(v) for k, v in d["near_miss_models"].items()},
                        "relaxed": d["relaxed_candidate_counts"], "temptation": d["temptation_count"],
                        "extreme": d["extreme_reasons"]} for d in by_type.get("abstention", [])],
        "commercial_or_license_queries": sum(1 for d in drafts if {"commercial_status", "licenses"} & set(d["conditions"])),
        "parameter_or_context_queries": sum(1 for d in drafts if NUMERIC_KEYS & set(d["conditions"])),
        "artifact_queries": sum(1 for d in drafts if {"require_artifact", "max_artifact_gib"} & set(d["conditions"])),
        "pure_semantic_queries": sum(1 for d in drafts if d["query_type"] in ("semantic_capability",)
                                     and set(d["conditions"]) <= {"tasks"}),
        "style_exemptions": STYLE_QUOTA_EXEMPTIONS,
    }
    return data


def render_report(data: Mapping[str, Any], meta: Mapping[str, Any]) -> str:
    total = data["total"]
    out = ["# 골든셋 v3 질문 품질 보고서", "",
           f"> 기준 코퍼스 sync_run_id `{meta['sync_run_id']}` · active {meta['active_row_count']:,} · "
           "상태: 초안 + 전수 스캔 + 검수 준비 완료(사람 판정 전). 아래 '정답'은 모두 Claude 제안 기준이다.", "",
           "## 유형·표현·페르소나", "",
           table(["유형", "질문 수", "기술형", "목적형", "혼합형", "easy", "hard"],
                 [[f"{t} ({TYPE_TITLES[t]})", n, data["style_by_type"][t].get("technical", 0),
                   data["style_by_type"][t].get("goal_oriented", 0), data["style_by_type"][t].get("mixed", 0),
                   data["difficulty_by_type"][t].get("easy", 0), data["difficulty_by_type"][t].get("hard", 0)]
                  for t, n in data["per_type"].items()]), "",
           "전체 표현 비율: " + ", ".join(f"{STYLE[k]} {pct(v, total)}" for k, v in data["style"].items()), "",
           "페르소나: " + ", ".join(f"{k} {v}" for k, v in data["persona"].items()), ""]
    for qtype, styles in data["style_exemptions"].items():
        for style, why in styles.items():
            out += [f"- 쿼터 예외 — {qtype} 의 {STYLE[style]}: {why}"]
    out += ["", "## 조건 사용", "",
            table(["조건 키", "질문 수"], [[f"`{k}`", v] for k, v in data["condition_keys"].items()]), "",
            f"- 상업 이용·라이선스 조건 질문: {data['commercial_or_license_queries']}개",
            f"- 파라미터·컨텍스트 수치 조건 질문: {data['parameter_or_context_queries']}개",
            f"- GGUF·ONNX 등 파일 형식·크기 조건 질문: {data['artifact_queries']}개",
            f"- 순수 의미 질문(semantic_capability 중 task 외 조건 없음): {data['pure_semantic_queries']}개", "",
            "## 제안 정답 분포", "",
            f"- pool: {data['proposed_pool']} (2점 {data['proposed_pool_by_grade'][2]}, 1점 {data['proposed_pool_by_grade'][1]})",
            f"- 근거가 확인된 단계: {data['proposed_evidence_stage']}",
            "- 같은 canonical family 상위: " + ", ".join(f"{k} ×{v}" for k, v in data["top_families"].items()), "",
            "## 질문별 수", "",
            table(["query", "eligible", "2점 제안", "1점 제안", "사람 판단", "검수 대상", "unknown 때문에 제외", "최대 family 중복"],
                  [[q["query_id"], f"{q['eligible']:,}", q["grade_2"], q["grade_1"], q["unresolved"], q["review"],
                    f"{q['unknown_excluded']:,}", q["max_family"]] for q in data["per_query"]]), "",
            "## abstention near-miss", "",
            table(["query", "조건 하나만 불충족한 near-miss", "단일 조건 완화 후보", "temptation", "극단성"],
                  [[a["query_id"], a["near_miss"], a["relaxed"], a["temptation"], a["extreme"] or "통과"]
                   for a in data["abstention"]]), ""]
    return "\n".join(out).rstrip() + "\n"


def hints(draft: Mapping[str, Any], endings: Counter) -> List[str]:
    q = draft["query"]
    out = []
    if draft["query_type"] not in NAME_TYPES and MODEL_NAME_RE.search(q):
        out.append(f"모델명 노출: {MODEL_NAME_RE.search(q).group(0)}")
    ending = q.rstrip(" ?.!")[-5:]
    if endings[ending] >= 5:
        out.append(f"같은 어미 반복 '{ending}' ×{endings[ending]}")
    if len(q) > 130:
        out.append(f"긴 문장 {len(q)}자")
    if len(draft["conditions"]) >= 4:
        out.append(f"조건 {len(draft['conditions'])}개 — 필터 나열처럼 읽히는지 확인")
    if draft.get("extreme_reasons"):
        out.append("극단성 검사 실패")
    return out


def render_question_review(drafts: List[Mapping[str, Any]]) -> str:
    endings = Counter(d["query"].rstrip(" ?.!")[-5:] for d in drafts)
    checks = ["실제로 물을 법함", "필터 나열 아님", "목적 이해됨", "숨은 조건 없음", "극단적이지 않음",
              "불필요한 모델명 없음", "표현 스타일 적절", "문형 반복 아님"]
    out = ["# 골든셋 v3 질문 검수표", "",
           "질문 품질은 기계가 완전히 판정할 수 없다. 아래 여덟 항목을 질문마다 확인하고 문제가 있으면 "
           "`queries.py` 에서 질문을 고친 뒤 `build_drafts.py` 를 다시 돌린다. '기계 힌트'는 확인이 필요한 신호일 뿐 판정이 아니다.", "",
           "점검 항목: " + " · ".join(f"{i + 1}) {c}" for i, c in enumerate(checks)), "",
           "자동으로 이미 확인된 것: 숨은 조건(모든 조건에 질문 속 근거 표현 존재), abstention 극단성, 유형별 10개.", ""]
    for qtype in TYPE_TITLES:
        out += [f"## {qtype} ({TYPE_TITLES[qtype]})", "",
                "| id | 질문 | 표현 | persona | 기계 힌트 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 메모 |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for d in drafts:
            if d["query_type"] != qtype:
                continue
            hint = "; ".join(hints(d, endings)) or "—"
            out.append(f"| {d['query_id']} | {d['query'].replace('|', '/')} | {STYLE[d['expression_style']]} | {d['persona']} | "
                       f"{hint} |" + " ☐ |" * 8 + "  |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    meta = corpus.load_meta()
    drafts = [d for t in TYPE_TITLES for d in read_jsonl(DRAFTS / f"{t}.jsonl")]
    if len(drafts) != 70:
        raise SystemExit(f"초안 {len(drafts)}개. build_drafts.py 를 먼저 실행한다")
    data = collect(drafts)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "quality_report.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REPORTS / "quality_report.md").write_text(render_report(data, meta), encoding="utf-8")
    (corpus.V3 / "review" / "QUESTION_REVIEW.md").write_text(render_question_review(drafts), encoding="utf-8")
    print("reports/quality_report.md·.json, review/QUESTION_REVIEW.md 생성")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
