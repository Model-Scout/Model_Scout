#!/usr/bin/env python3
"""골든셋 v3 자동 검증기.

    python test/golden/v3/tools/verify.py --mode structure-only   # 스냅샷 없이 질문 구조만
    python test/golden/v3/tools/verify.py --mode draft            # 전수 스캔 재계산 + 워크시트 생성
    python test/golden/v3/tools/verify.py --mode final            # 사람 판정 완료까지 요구

draft·final 은 기준 코퍼스 스냅샷이 없거나 메타와 다르면 실패한다. 조용히 통과하지 않는다.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402
import scan  # noqa: E402
from build_drafts import ABSTAIN_ROW, DRAFTS, JUDGMENTS  # noqa: E402
from queries_loader import QUERY_TYPES, STYLE_QUOTA_EXEMPTIONS, all_queries  # noqa: E402

PER_TYPE = 10
PERSONAS = {"startup_dev", "backend_dev", "local_user", "ml_engineer", "researcher", "korean_service_planner", "limited_gpu"}
STYLES = {"technical", "goal_oriented", "mixed"}
DIFFICULTIES = {"easy", "hard"}
FAMILY_OVERUSE = 5  # 한 질의의 정답 후보 중 같은 canonical family 가 이보다 많으면 경고


@dataclass
class Issue:
    level: str  # error / warn
    code: str
    query_id: str
    message: str


def _issue(out: List[Issue], level: str, code: str, query_id: str, message: str) -> None:
    out.append(Issue(level, code, query_id, message))


# --------------------------------------------------------------------------- 숨은 조건

GATED_RE = re.compile(r"승인 없이|약관 동의 없이|gated|바로 받")
FORMAT_ALIASES = {"gguf": ("gguf", "ollama", "llama.cpp", "whisper.cpp"), "onnx": ("onnx",),
                  "safetensors": ("safetensors",), "pytorch_bin": ("pytorch",), "mlx": ("mlx",)}
LICENSE_WORDS = {"apache-2.0": "apache", "mit": "mit", "gemma": "gemma"}


def _number_forms(value: float) -> List[str]:
    forms = {f"{value:g}"}
    if value >= 1024 and value % 1024 == 0:
        forms.add(f"{int(value // 1024)}K")
    if value < 1:
        forms.add(f"{int(round(value * 1000))}M")
    return sorted(forms)


def hidden_condition_problems(query: Mapping[str, Any]) -> List[str]:
    """conditions 의 각 조건이 질문 문장에서 나왔는지 검사한다. 빈 목록이면 통과."""
    text = query.get("query") or ""
    lower = text.lower()
    fidelity = query.get("conditions_fidelity") or {}
    problems = []
    for key, value in (query.get("conditions") or {}).items():
        fid = fidelity.get(key)
        if not fid:
            problems.append(f"{key}: conditions_fidelity 없음")
            continue
        for piece in re.sub(r"\([^)]*\)", "", fid).split("…"):
            piece = piece.split("→")[0].strip()
            if piece and piece not in text:
                problems.append(f"{key}: 근거 표현 '{piece}' 이 질문에 없다")
        if key in scan.NUMERIC_FIELD:
            if not re.search(r"\d", fid):
                problems.append(f"{key}: 수치 조건인데 근거 표현에 숫자가 없다(숨은 수치 조건)")
            elif not any(form.lower() in lower for form in _number_forms(float(value))):
                problems.append(f"{key}: 값 {value} 이 질문에 그대로 나오지 않는다")
        elif key == "commercial_status" and "상업" not in text:
            problems.append("commercial_status: 질문에 상업 이용 언급이 없다")
        elif key == "licenses":
            for name in value:
                if LICENSE_WORDS.get(name, name).lower() not in lower:
                    problems.append(f"licenses: '{name}' 이 질문에 없다")
        elif key == "require_artifact":
            for fmt in value:
                if not any(alias in lower for alias in FORMAT_ALIASES.get(fmt, (fmt,))):
                    problems.append(f"require_artifact: '{fmt}' 이 질문에 없다")
        elif key == "exclude_gated" and not GATED_RE.search(text):
            problems.append("exclude_gated: 승인·약관 없이 받는다는 말이 없다")
        elif key == "korean_required" and "한국어" not in text:
            problems.append("korean_required: 질문에 한국어 언급이 없다")
    for key in fidelity:
        if key not in (query.get("conditions") or {}):
            problems.append(f"{key}: conditions 에 없는 fidelity 항목")
    return problems


# --------------------------------------------------------------------------- structure-only

def check_structure(queries: Sequence[Mapping[str, Any]]) -> List[Issue]:
    out: List[Issue] = []
    by_type = Counter(q["query_type"] for q in queries)
    for query_type in QUERY_TYPES:
        if by_type.get(query_type, 0) != PER_TYPE:
            _issue(out, "error", "type_count", "-", f"{query_type} 질문 {by_type.get(query_type, 0)}개 (기대 {PER_TYPE})")
    if len(queries) != PER_TYPE * len(QUERY_TYPES):
        _issue(out, "error", "total_count", "-", f"전체 {len(queries)}개 (기대 {PER_TYPE * len(QUERY_TYPES)})")
    ids = Counter(q.get("query_id") for q in queries)
    for qid, n in ids.items():
        if n > 1:
            _issue(out, "error", "duplicate_id", str(qid), f"query_id {n}번 중복")
    for q in queries:
        qid = q.get("query_id") or "?"
        if not (q.get("query") or "").strip():
            _issue(out, "error", "empty_query", qid, "질문이 비었다")
        if q.get("persona") not in PERSONAS:
            _issue(out, "error", "persona", qid, f"persona {q.get('persona')!r}")
        if q.get("expression_style") not in STYLES:
            _issue(out, "error", "expression_style", qid, f"expression_style {q.get('expression_style')!r}")
        if q.get("difficulty") not in DIFFICULTIES:
            _issue(out, "error", "difficulty", qid, f"difficulty {q.get('difficulty')!r}")
        if not q.get("user_intent"):
            _issue(out, "error", "user_intent", qid, "user_intent 없음")
        for key in q.get("conditions") or {}:
            if key not in corpus.CONDITION_KEYS:
                _issue(out, "error", "unsupported_condition", qid, f"지원하지 않는 조건 키 {key}")
        for problem in hidden_condition_problems(q):
            _issue(out, "error", "hidden_condition", qid, problem)
        rule = q.get("relevance_rule") or {}
        abstain = q.get("expected_behavior") == "abstain"
        if abstain != (q["query_type"] == "abstention"):
            _issue(out, "error", "expected_behavior", qid, "abstention 유형만 abstain 이어야 한다")
        if abstain:
            if not q.get("conditions"):
                _issue(out, "error", "abstention_conditions", qid, "abstention 에 조건이 없다")
            continue
        if not rule.get("grade_2") or not rule.get("grade_1"):
            _issue(out, "error", "relevance_rule", qid, "2점·1점 기준 문장이 없다")
        if q["query_type"] == "benchmark_lookup":
            bench = rule.get("benchmark") or {}
            if not bench.get("dataset_regex") or not bench.get("metric_regex"):
                _issue(out, "error", "benchmark_rule", qid, "dataset_regex·metric_regex 가 모두 필요하다")
        if q["query_type"] == "model_comparison" and len(rule.get("families") or []) < 2:
            _issue(out, "error", "comparison_families", qid, "비교 계열이 둘 이상 필요하다")
        if q["query_type"] == "lexical_exact" and not rule.get("families"):
            _issue(out, "error", "lexical_family", qid, "지목한 모델 계열 정의가 없다")
    for query_type in QUERY_TYPES:
        styles = Counter(q["expression_style"] for q in queries if q["query_type"] == query_type)
        exempt = STYLE_QUOTA_EXEMPTIONS.get(query_type, {})
        thin = [s for s in sorted(STYLES) if styles.get(s, 0) < 2 and s not in exempt]
        if thin:
            _issue(out, "warn", "style_mix", query_type, f"표현 스타일 2개 미만: {thin} ({dict(styles)})")
    return out


# --------------------------------------------------------------------------- draft

def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_drafts() -> Dict[str, Dict[str, Any]]:
    out = {}
    for query_type in QUERY_TYPES:
        for draft in read_jsonl(DRAFTS / f"{query_type}.jsonl"):
            out[draft["query_id"]] = draft
    return out


def check_draft(queries: Sequence[Mapping[str, Any]], rows: Sequence[Mapping[str, Any]],
                meta: Mapping[str, Any], drafts: Mapping[str, Mapping[str, Any]]) -> List[Issue]:
    out: List[Issue] = []
    scan.bind(rows)
    ids = {r["model_id"] for r in rows}
    stamp = corpus.corpus_stamp(meta)
    for q in queries:
        qid = q["query_id"]
        draft = drafts.get(qid)
        if draft is None:
            _issue(out, "error", "draft_missing", qid, "초안이 없다. build_drafts.py 실행")
            continue
        for key in ("query", "conditions", "relevance_rule", "expected_behavior"):
            if draft.get(key) != q.get(key):
                _issue(out, "error", "draft_stale", qid, f"초안의 {key} 가 queries.py 와 다르다. build_drafts.py 재실행")
        if draft.get("corpus") != stamp:
            _issue(out, "error", "corpus_mismatch", qid, f"초안 코퍼스 {draft.get('corpus')} ≠ 메타 {stamp}")
        fresh = scan.scan_query(q, rows)
        eligible_ids = {mid for cls in fresh["classes"].values() for mid in cls} if q["expected_behavior"] != "abstain" \
            else {r["model_id"] for r in corpus.eligible(rows, q.get("conditions") or {})}
        if draft.get("eligible_count") != fresh["eligible_count"] or draft.get("eligible_ids_sha256") != fresh["eligible_ids_sha256"]:
            _issue(out, "error", "eligible_mismatch", qid,
                   f"기록 eligible {draft.get('eligible_count')} ≠ 재계산 {fresh['eligible_count']}")
        if draft.get("classification") != fresh["counts"]:
            _issue(out, "error", "classification_mismatch", qid, f"기록 {draft.get('classification')} ≠ 재계산 {fresh['counts']}")
        if not fresh["invariant_ok"]:
            _issue(out, "error", "invariant", qid, "eligible 전수가 네 분류에 정확히 한 번씩 들어가지 않았다")
        if sum(fresh["counts"].values()) != fresh["eligible_count"] and q["expected_behavior"] != "abstain":
            _issue(out, "error", "invariant_sum", qid, "분류 합계 ≠ eligible_count")
        cand_ids = {c["model_id"] for c in draft.get("candidates") or []}
        if not cand_ids <= eligible_ids or not cand_ids <= ids:
            _issue(out, "error", "grade_outside_eligible", qid, f"eligible 밖 후보: {sorted(cand_ids - eligible_ids)[:3]}")
        if q["expected_behavior"] == "abstain":
            check_abstention(out, qid, draft, fresh)
            continue
        if draft.get("review_count", 0) > scan.REVIEW_LIMIT:
            _issue(out, "warn", "review_limit", qid, f"사람 검수 후보 {draft['review_count']}개 > {scan.REVIEW_LIMIT}")
        if not cand_ids:
            _issue(out, "error", "no_candidate", qid, "recommend 질의인데 제안 후보가 없다")
        elif fresh["counts"]["proposed_grade_2"] == 0:
            _issue(out, "warn", "no_grade_2", qid, "2점 제안이 없다(1점·사람 판단만)")
        if q["query_type"] == "model_comparison":
            fams = {c.get("family") for c in draft["candidates"] if c["class"] != "auto_rejected"}
            for fam in q["relevance_rule"]["families"]:
                if fam["name"] not in fams:
                    _issue(out, "error", "comparison_family_missing", qid, f"비교 계열 {fam['name']} 후보 없음")
        if q["query_type"] == "benchmark_lookup":
            by_id = corpus.by_id(rows)
            for c in draft["candidates"]:
                found, _ = scan.matching_results(by_id[c["model_id"]], q["relevance_rule"]["benchmark"])
                if not found:
                    _issue(out, "error", "benchmark_mismatch", qid, f"{c['model_id']} 에 같은 dataset·metric 결과가 없다")
        families = Counter(c["canonical_model_id"] for c in draft["candidates"])
        for fam, n in families.items():
            if n > FAMILY_OVERUSE:
                _issue(out, "warn", "family_overuse", qid, f"canonical {fam} 후보 {n}개")
    return out


def check_abstention(out: List[Issue], qid: str, draft: Mapping[str, Any], fresh: Mapping[str, Any]) -> None:
    abst = fresh["abstention"]
    if fresh["eligible_count"] != 0 or draft.get("eligible_count") != 0:
        _issue(out, "error", "abstention_not_empty", qid, f"eligible {fresh['eligible_count']}개 (0이어야 한다)")
    if draft.get("expected_any") or draft.get("acceptable"):
        _issue(out, "error", "abstention_labels", qid, "abstention 에 정답 라벨이 있다")
    if draft.get("relaxed_candidate_counts") != abst["relaxed_candidate_counts"]:
        _issue(out, "error", "relaxation_mismatch", qid, "기록된 단일 조건 완화 결과가 재계산과 다르다")
    if not any(v > 0 for v in abst["relaxed_candidate_counts"].values()):
        _issue(out, "error", "no_relaxation_candidate", qid, "어떤 조건을 완화해도 후보가 없다")
    if abst["near_miss_count"] == 0:
        _issue(out, "error", "no_near_miss", qid, "조건 하나만 불충족한 near-miss 가 없다")
    non_task = sum(len(v) for k, v in abst["near_miss_by_condition"].items() if k != "tasks")
    if non_task < 3:
        _issue(out, "warn", "few_near_miss", qid, f"task 외 조건 하나 차이 near-miss {non_task}개 (<3)")
    for reason in abst["extreme_reasons"]:
        _issue(out, "error", "extreme_abstention", qid, reason)


# --------------------------------------------------------------------------- final

def check_final(queries: Sequence[Mapping[str, Any]], drafts: Mapping[str, Mapping[str, Any]]) -> List[Issue]:
    out: List[Issue] = []
    judgments: Dict[tuple, Mapping[str, Any]] = {}
    for path in JUDGMENTS.glob("*.jsonl"):
        for item in read_jsonl(path):
            judgments[(item["query_id"], item["model_id"])] = item
            if item.get("stale"):
                _issue(out, "error", "stale_judgment", item["query_id"], f"{item['model_id']} 판정이 현재 후보에 없다")
    final = {}
    for query_type in QUERY_TYPES:
        for record in read_jsonl(corpus.V3 / "final" / f"{query_type}.jsonl"):
            final[record["query_id"]] = record
    for q in queries:
        qid = q["query_id"]
        draft = drafts.get(qid) or {}
        keys = [ABSTAIN_ROW] if q["expected_behavior"] == "abstain" else [c["model_id"] for c in draft.get("candidates") or []]
        for model_id in keys:
            item = judgments.get((qid, model_id)) or {}
            if item.get("decision") in (None, "hold"):
                _issue(out, "error", "unjudged", qid, f"{model_id} 미판정·보류")
            elif not all(item.get(k) for k in ("judged_by", "judged_at", "judgment_reason")):
                _issue(out, "error", "judgment_fields", qid, f"{model_id} 에 judged_by·judged_at·judgment_reason 이 없다")
        record = final.get(qid)
        if record is None:
            _issue(out, "error", "final_missing", qid, "final/ 에 없다. finalize.py 실행")
            continue
        labels = record.get("labels") or []
        if not set(l["model_id"] for l in labels) <= {c["model_id"] for c in draft.get("candidates") or []}:
            _issue(out, "error", "final_outside_candidates", qid, "최종 라벨이 eligible 후보 밖에 있다")
        if any(not all(l.get(k) for k in ("judged_by", "judged_at", "judgment_reason")) for l in labels):
            _issue(out, "error", "label_fields", qid, "최종 라벨에 judged_by·judged_at·judgment_reason 이 없다")
        if q["expected_behavior"] == "recommend":
            if not labels:
                _issue(out, "error", "no_confirmed_answer", qid, "확정 정답이 없다")
            elif not record.get("expected_any"):
                _issue(out, "warn", "no_confirmed_grade_2", qid, "확정 2점 정답이 없다")
        if q["query_type"] == "model_comparison":
            fams = {l.get("family") for l in labels}
            for fam in q["relevance_rule"]["families"]:
                if fam["name"] not in fams:
                    _issue(out, "error", "comparison_family_unconfirmed", qid, f"{fam['name']} 계열 확정 정답 없음")
        if draft.get("unresolved_for_human") and any(judgments.get((qid, m), {}).get("decision") is None
                                                       for m in (draft.get("classes") or {}).get("unresolved_for_human", [])):
            _issue(out, "error", "unresolved_left", qid, "unresolved 후보가 남았다")
    return out


def family_report(drafts: Mapping[str, Mapping[str, Any]]) -> List[str]:
    lines = []
    for qid, draft in sorted(drafts.items()):
        fams = Counter(c["canonical_model_id"] for c in draft.get("candidates") or [])
        top = [(f, n) for f, n in fams.most_common(3) if n > 1]
        if top:
            lines.append(f"  {qid}: " + ", ".join(f"{f} ×{n}" for f, n in top))
    return lines


def report(issues: Iterable[Issue]) -> int:
    issues = list(issues)
    errors = [i for i in issues if i.level == "error"]
    warns = [i for i in issues if i.level == "warn"]
    for item in errors + warns:
        print(f"{'❌' if item.level == 'error' else '⚠️ '} [{item.code}] {item.query_id}: {item.message}")
    print(f"\n오류 {len(errors)}개, 경고 {len(warns)}개")
    return 1 if errors else 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--mode", choices=("structure-only", "draft", "final"), default="draft")
    parser.add_argument("--no-worksheets", action="store_true", help="draft 모드에서 워크시트를 다시 쓰지 않는다")
    args = parser.parse_args(argv)
    queries = all_queries()
    issues = check_structure(queries)
    if args.mode == "structure-only":
        print("structure-only: 스냅샷 없이 질문 구조만 검사했다. eligible·정답은 검증하지 않았다.")
        return report(issues)
    try:
        rows = corpus.load_corpus()
        meta = corpus.load_meta()
    except corpus.CorpusError as exc:
        print(f"❌ 기준 코퍼스를 쓸 수 없어 {args.mode} 검증을 할 수 없다: {exc}")
        return 2
    print(f"기준 코퍼스: sync_run_id={meta['sync_run_id']} 행 {len(rows):,} (SHA256 일치)")
    drafts = load_drafts()
    issues += check_draft(queries, rows, meta, drafts)
    print("canonical family 중복(질의별 상위):")
    print("\n".join(family_report(drafts)) or "  없음")
    if args.mode == "final":
        issues += check_final(queries, drafts)
    elif not args.no_worksheets:
        import make_worksheet
        make_worksheet.main()
    return report(issues)


if __name__ == "__main__":
    raise SystemExit(main())
