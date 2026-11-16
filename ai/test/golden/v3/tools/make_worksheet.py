#!/usr/bin/env python3
"""사람 검수 워크시트(review/worksheets/<유형>.md)와 질의별 요약(review/SUMMARY.md)을 만든다.

워크시트는 읽기용이다. 판정은 ``tools/judge.py`` 로 ``review/judgments/<유형>.jsonl`` 에
기록한다. 자동 제외된 모델은 펼치지 않고, 이유별 수와 규칙 감사용 소수 표본만 보여 준다.

    python test/golden/v3/tools/make_worksheet.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
import scan  # noqa: E402
from build_drafts import ABSTAIN_ROW  # noqa: E402

REVIEW = corpus.V3 / "review"
WORKSHEETS = REVIEW / "worksheets"
TYPE_TITLES = {
    "structured_constraint": "구조화 조건", "semantic_capability": "의미 능력", "semantic_constraint": "의미 + 조건",
    "lexical_exact": "모델명 지목", "model_comparison": "모델 비교", "benchmark_lookup": "벤치마크 조회",
    "abstention": "정답 없음(기권)",
}
STYLE = {"technical": "기술형", "goal_oriented": "목적형", "mixed": "혼합형"}


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def cell(value: Any, limit: int = 160) -> str:
    if value is None or value == "" or value == []:
        return "—"
    if isinstance(value, bool):
        text = "true" if value else "false"
    elif isinstance(value, (list, tuple)):
        text = ", ".join(str(v) for v in value)
    elif isinstance(value, dict):
        text = ", ".join(f"{k} {v}" for k, v in value.items())
    else:
        text = str(value)
    text = text.replace("|", "\\|").replace("\n", " ").strip()
    return text if len(text) <= limit else text[:limit] + "…"


def provenance_status(row: Mapping[str, Any]) -> Dict[str, int]:
    fields = (((row.get("source_provenance") or {}).get("contract") or {}).get("fields")) or {}
    out: Dict[str, int] = {}
    for entry in fields.values():
        status = (entry or {}).get("status")
        if status:
            out[status] = out.get(status, 0) + 1
    return out


def first_claim(row: Mapping[str, Any]) -> tuple:
    for field, text in scan.semantic_claims(row):
        if field != "summary":
            return field, text
    return None, None


def first_quote(row: Mapping[str, Any]) -> str:
    sem = row.get("semantic_metadata") or {}
    for field in scan.SEMANTIC_CLAIM_FIELDS:
        for item in sem.get(field) or []:
            if isinstance(item, dict) and item.get("supporting_quote"):
                return item["supporting_quote"]
    return ""


def benchmark_cell(row: Mapping[str, Any], cand: Mapping[str, Any]) -> str:
    ev = cand.get("evidence") or {}
    if ev.get("result"):
        r = ev["result"]
        return (f"{r.get('dataset')} / {r.get('metric')} = {r.get('score')} "
                f"(self_reported={r.get('self_reported')}, {r.get('comparability')}, {r.get('evidence_ref')}; "
                f"같은 dataset·metric 결과 {ev.get('matching_results')}건)")
    results = (row.get("benchmark_metadata") or {}).get("results") or []
    return f"점수 {len(results)}건 저장" if results else "없음"


def candidate_block(index: int, cand: Mapping[str, Any], row: Mapping[str, Any], judgment: Mapping[str, Any]) -> str:
    meta = corpus.meta_of(row)
    ev = cand.get("evidence") or {}
    claim_field, claim = first_claim(row)
    url = (row.get("source_provenance") or {}).get("model_url") or f"https://huggingface.co/{row['model_id']}"
    grade = {2: "2점", 1: "1점"}.get(cand.get("proposed_grade"), "보류(사람 판단)")
    decided = judgment.get("decision")
    lines = [
        f"#### {index}. [{row['model_id']}]({url}) — Claude 제안: **{grade}**",
        "",
        f"- 제안 이유: {cell(cand.get('reason'), 300)}",
        f"- 근거 위치: `{ev.get('stage', '—')}` — {cell(ev.get('snippet'), 240)}",
        "",
        "| 항목 | 값 |", "|---|---|",
        f"| canonical model | {cell(cand.get('canonical_model_id'))} (variant={cell(cand.get('is_variant'))}, "
        f"종류={cell(cand.get('variant_types'))}, 관계 근거={cell(cand.get('relation_source'))}, 변환 표지={cell(cand.get('conversion_marker'))}) |",
        f"| pool | {cell(row.get('source_pool'))} |",
        f"| 파라미터(B) / 컨텍스트 | {cell(meta.get('parameter_count_billion'))} / {cell(meta.get('context_length'))} |",
        f"| task | {cell(meta.get('primary_task'))} (matched: {cell(meta.get('matched_tasks'))}) |",
        f"| 한국어 근거 | {cell(meta.get('korean_evidence'))} |",
        f"| license / commercial_status / gated | {cell(meta.get('license'))} / {cell(meta.get('commercial_status'))} / {cell(meta.get('gated'))} |",
        f"| artifact formats / 실행 파일 크기(GiB) | {cell(meta.get('artifact_formats'))} / {cell(meta.get('artifact_runnable_gib'))} |",
        f"| 벤치마크 근거 | {cell(benchmark_cell(row, cand), 300)} |",
        f"| 의미 claim ({claim_field or '—'}) | {cell(claim, 240)} |",
        f"| README 인용 | {cell(first_quote(row), 240)} |",
        f"| provenance status | {cell(provenance_status(row))} |",
        f"| revision | {cell(meta.get('revision'))} |",
        "",
        f"- 판정: {'**' + str(decided) + '** (최종 ' + str(judgment.get('final_grade')) + '점, ' + str(judgment.get('judged_by')) + ')' if decided else '☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류'}",
        f"- 이유: {cell(judgment.get('judgment_reason'), 300) if decided else '______'}",
        "",
    ]
    return "\n".join(lines)


def conditions_table(draft: Mapping[str, Any]) -> str:
    cond = draft.get("conditions") or {}
    if not cond:
        return "하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.\n"
    lines = ["| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |", "|---|---|---|---|"]
    for key, value in cond.items():
        spec = corpus.CONDITION_KEYS[key]
        lines.append(f"| `{key}` | {cell(value)} | {cell(draft['conditions_fidelity'].get(key))} | "
                     f"{'예' if spec.sql_supported else '아니오(판정용)'} |")
    return "\n".join(lines) + "\n"


def summary_table(draft: Mapping[str, Any]) -> str:
    c = draft["classification"]
    return "\n".join([
        "| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |",
        "|---:|---:|---:|---:|---:|---:|---:|---|---:|",
        f"| {draft['corpus_count']:,} | {draft['eligible_count']:,} | {c['proposed_grade_2']} | {c['proposed_grade_1']} | "
        f"{c['auto_rejected']:,} | {c['unresolved_for_human']} | {draft['review_count']} | "
        f"{'✅' if draft['invariant_ok'] else '❌'} | {draft['unknown_excluded']:,} |",
        "",
    ])


def reject_section(draft: Mapping[str, Any]) -> str:
    reasons = draft.get("auto_reject_reasons") or {}
    if not reasons:
        return ""
    lines = ["자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):", "",
             "| 이유 | 수 | 감사 표본 |", "|---|---:|---|"]
    for reason, count in reasons.items():
        sample = draft.get("auto_reject_audit_sample", {}).get(reason) or []
        lines.append(f"| {scan.REJECT_REASONS.get(reason, reason)} (`{reason}`) | {count:,} | {cell(sample, 300)} |")
    return "\n".join(lines) + "\n"


def abstention_block(draft: Mapping[str, Any]) -> str:
    lines = ["| 조건 하나만 뺐을 때 | 후보 수 | 그 조건 하나만 불충족한 near-miss (최대 5) |", "|---|---:|---|"]
    for key, count in draft["relaxed_candidate_counts"].items():
        lines.append(f"| `{key}` | {count} | {cell((draft['near_miss_models'].get(key) or [])[:5], 300)} |")
    lines += ["", f"- 조건 각각을 단독으로 만족하는 모델 수: {cell(draft['individual_condition_counts'])}",
              f"- near-miss 합계 {draft['near_miss_count']}개, temptation_count {draft['temptation_count']}",
              f"- 극단성 검사: {'통과' if not draft['extreme_reasons'] else '❌ ' + '; '.join(draft['extreme_reasons'])}",
              "- 검수: 정말 정답이 없어야 하는지, near-miss 가 '조건 하나 차이'라는 설명이 맞는지 확인한다.", ""]
    return "\n".join(lines)


def worksheet(query_type: str, drafts: List[Mapping[str, Any]], judgments: Mapping[tuple, Mapping[str, Any]],
              rows_by_id: Mapping[str, Mapping[str, Any]]) -> str:
    out = [f"# 골든셋 v3 검수 워크시트 — {query_type} ({TYPE_TITLES[query_type]})", "",
           "> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.",
           ">",
           "> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason \"…\" --by <이름>`",
           ""]
    for draft in drafts:
        rule = draft["relevance_rule"]
        out += [f"## {draft['query_id']} — {draft['query']}", "",
                f"- 사용자 의도: {draft['user_intent']}",
                f"- persona / 표현: {draft['persona']} / {STYLE[draft['expression_style']]} · 난이도 {draft['difficulty']}",
                f"- 기대 행동: {draft['expected_behavior']}", ""]
        out.append(conditions_table(draft))
        if draft["expected_behavior"] == "abstain":
            out += [f"정답 기준: {rule.get('must')}", ""]
            out.append(abstention_block(draft))
            confirm = judgments.get((draft["query_id"], ABSTAIN_ROW), {})
            out += [f"- 기권 확인: {'**' + str(confirm.get('decision')) + '** (' + str(confirm.get('judged_by')) + ')' if confirm.get('decision') else '☐ 정답 없음 확인 ☐ 보류'}"
                    f" — `judge.py {draft['query_id']} {ABSTAIN_ROW} --decision approve --reason … --by …`", ""]
            continue
        out += [f"- **2점 기준**: {rule.get('grade_2')}", f"- **1점 기준**: {rule.get('grade_1')}"]
        if rule.get("benchmark"):
            b = rule["benchmark"]
            out.append(f"- 비교 기준: dataset `{b['dataset_regex']}` · metric `{b['metric_regex']}` {b.get('note', '')}".rstrip())
        if rule.get("families"):
            out.append("- 비교 계열: " + ", ".join(f"{f['name']} (`{f['id_regex']}`)" for f in rule["families"]))
        if rule.get("note"):
            out.append(f"- 메모: {rule['note']}")
        out += ["", summary_table(draft), reject_section(draft)]
        fam = draft.get("family_counts") or {}
        heavy = {k: v for k, v in fam.items() if v >= 3}
        if heavy:
            out += [f"같은 canonical family 후보가 3개 이상: {cell(heavy)}", ""]
        if not draft["candidates"]:
            out += ["검수할 후보가 없다. eligible 전수가 자동 제외됐다(위 이유 참고).", ""]
        for i, cand in enumerate(draft["candidates"], 1):
            judgment = judgments.get((draft["query_id"], cand["model_id"]), {})
            out.append(candidate_block(i, cand, rows_by_id[cand["model_id"]], judgment))
    return "\n".join(out).rstrip() + "\n"


def summary(all_drafts: List[Mapping[str, Any]], judgments: Mapping[tuple, Mapping[str, Any]]) -> str:
    lines = ["# 골든셋 v3 질의별 요약", "",
             "> 상태: **초안 + 전수 스캔 + 검수 준비 완료** (사람 판정 전). 숫자는 `tools/build_drafts.py` 가 기준 코퍼스에서 계산했다.",
             "",
             "| query | 유형 | 표현 | eligible | 2점 | 1점 | 제외 | 사람 판단 | 검수 대상 | 판정 완료 | invariant |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for d in all_drafts:
        c = d["classification"]
        done = sum(1 for cand in d["candidates"] if judgments.get((d["query_id"], cand["model_id"]), {}).get("decision") not in (None, "hold"))
        lines.append(f"| {d['query_id']} | {d['query_type']} | {STYLE[d['expression_style']]} | {d['eligible_count']:,} | "
                     f"{c['proposed_grade_2']} | {c['proposed_grade_1']} | {c['auto_rejected']:,} | {c['unresolved_for_human']} | "
                     f"{d['review_count']} | {done}/{len(d['candidates'])} | {'✅' if d['invariant_ok'] else '❌'} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = corpus.load_corpus()
    scan.bind(rows)
    rows_by_id = corpus.by_id(rows)
    from build_drafts import DRAFTS, JUDGMENTS
    WORKSHEETS.mkdir(parents=True, exist_ok=True)
    all_drafts: List[Mapping[str, Any]] = []
    judgments: Dict[tuple, Mapping[str, Any]] = {}
    for path in sorted(JUDGMENTS.glob("*.jsonl")):
        for item in read_jsonl(path):
            judgments[(item["query_id"], item["model_id"])] = item
    for query_type in TYPE_TITLES:
        drafts = read_jsonl(DRAFTS / f"{query_type}.jsonl")
        if not drafts:
            raise SystemExit(f"{DRAFTS / (query_type + '.jsonl')} 없음. build_drafts.py 를 먼저 실행한다")
        all_drafts.extend(drafts)
        (WORKSHEETS / f"{query_type}.md").write_text(worksheet(query_type, drafts, judgments, rows_by_id), encoding="utf-8")
    (REVIEW / "SUMMARY.md").write_text(summary(all_drafts, judgments), encoding="utf-8")
    print(f"워크시트 {len(TYPE_TITLES)}개, 요약 1개 생성")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
