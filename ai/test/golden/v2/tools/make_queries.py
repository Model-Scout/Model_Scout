#!/usr/bin/env python3
"""질의 사양(specs/<유형>.py)을 읽어 라벨 초안과 판정 워크시트를 만든다.

abstention 외 모든 유형이 같은 흐름을 쓴다.

    사양 (질의문 + conditions + conditions_fidelity + Rule)
      → eligible 추출 (하드 필터)
      → 6단계 규칙 스캔 (전수)
      → 🚩 / ⚠️ / ✅ 세 더미
      → judged/<유형>.jsonl (judged_by=null — 사람 확정 전)
      → worksheets/<유형>.md (사람이 볼 것만)

    python test/golden/v2/tools/make_queries.py structured_constraint
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

TOOLS = Path(__file__).resolve().parent
V2 = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import corpus_v2  # noqa: E402
import scan  # noqa: E402

PILE_LIMIT = 25  # 🚩 + ⚠️ 가 이보다 많으면 질의를 더 구체적으로 다시 써야 한다.


def load_specs(query_type: str) -> List[Dict[str, Any]]:
    path = V2 / "specs" / f"{query_type}.py"
    if not path.exists():
        raise SystemExit(f"{path} 없음")
    spec = importlib.util.spec_from_file_location(f"specs_{query_type}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.SPECS


def condition_label(conditions: Dict[str, Any]) -> str:
    parts = []
    if "max_parameters_billion" in conditions:
        cap = conditions["max_parameters_billion"]
        parts.append(f"≤{round(cap * 1000)}M" if cap < 1 else f"≤{cap}B")
    if "min_context_length" in conditions:
        parts.append(f"ctx≥{conditions['min_context_length']:,}")
    if conditions.get("pools") == ["core"]:
        parts.append("core만")
    return " · ".join(parts) or "조건 없음"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query_type")
    args = parser.parse_args()
    query_type = args.query_type

    meta = json.loads((V2 / "corpus_snapshot.meta.json").read_text(encoding="utf-8"))
    snapshot = {
        "source": meta["source"],
        "rows": meta["rows"],
        "sync_run_id": meta["last_sync_run_id"],
        "refreshed_at": meta["corpus_refreshed_at"],
    }
    specs = load_specs(query_type)

    print(f"판정 기준 코퍼스 {meta['rows']}행 · {query_type} 질의 {len(specs)}개")
    print()
    print(f"{'id':7s} {'task':26s} {'elig':>5s} {'🚩':>4s} {'⚠️':>4s} {'✅':>4s} "
          f"{'사람':>5s} {'난이도':>7s}  상태")
    print("-" * 86)

    records: List[Dict[str, Any]] = []
    worksheet: List[str] = []
    overflow: List[str] = []
    comparison_coverage_gaps: List[str] = []

    for item in specs:
        conditions = item["conditions"]
        rows = corpus_v2.eligible(conditions)
        flags, unsure, reject = scan.scan(rows, item["rule"])
        human = len(flags) + len(unsure)
        rule = item["rule"]

        # 비교 질의는 "둘 중 어느 쪽"을 묻는다. 한쪽 계열이 후보에 하나도 없으면
        # 검색 성능과 무관하게 제대로 비교할 수 없는, 잘못 설계된 문항이다.
        comparison_membership = {
            hit.model_id: list(hit.comparison_groups)
            for hit in (flags + unsure)
            if hit.comparison_groups
        }
        missing_groups = [
            name
            for name in rule.comparison_groups
            if not any(name in groups for groups in comparison_membership.values())
        ]
        if missing_groups:
            comparison_coverage_gaps.append(
                f"{item['query_id']}: {', '.join(missing_groups)} 후보 없음"
            )

        # 난이도: 사람이 볼 것 중 ③ 이후 단계에서 판정되는 비율이 높으면 어려움
        hard_hits = sum(1 for hit in flags if hit.difficulty == "hard") + len(unsure)
        difficulty = "hard" if hard_hits * 2 >= max(human, 1) else "easy"

        status = "✅" if human <= PILE_LIMIT and not missing_groups else (
            f"❌ 비교 대상 후보 없음: {', '.join(missing_groups)}"
            if missing_groups else f"❌ 사람이 볼 것 {human}개 > {PILE_LIMIT}"
        )
        if human > PILE_LIMIT:
            overflow.append(item["query_id"])
        print(f"{item['query_id']:7s} {conditions['tasks'][0]:26s} {len(rows):5d} "
              f"{len(flags):4d} {len(unsure):4d} {len(reject):4d} {human:5d} "
              f"{difficulty:>7s}  {status}")

        records.append({
            "query_id": item["query_id"],
            "query_type": query_type,
            "query": item["query"],
            "difficulty": difficulty,
            "conditions": conditions,
            "conditions_fidelity": item["fidelity"],
            "expected_behavior": "recommend",
            "relevance_rule": {
                "must": rule.must_label,
                "grade_2": rule.grade_2_label,
                "grade_1": rule.grade_1_label,
                "must_any": list(rule.must_any),
                "grade_2_any": list(rule.grade_2_any),
                "weak_any": list(rule.weak_any),
                "reject_any": list(rule.reject_any),
            },
            # model_comparison만 채운다. 사람 최종 라벨이 양쪽 계열을 모두
            # 포함하는지 verify.py가 이 정보로 확인한다.
            "comparison_groups": {
                name: list(aliases) for name, aliases in rule.comparison_groups.items()
            },
            # 사람이 확정하기 전이라 비워 둔다. judged/ 에 들어가지만 judged_by=null이다.
            "expected_any": [],
            "acceptable": [],
            "must_exclude": [],
            "eligible_count": len(rows),
            "relevant_complete": False,
            "verification": {
                "method": "eligible 전수 6단계 규칙 스캔 (검색기 미사용)",
                "rule_scan_covered": len(rows),
                "flagged_for_human": [hit.model_id for hit in flags],
                "unsure_for_human": [hit.model_id for hit in unsure],
                "proposals": {hit.model_id: hit.proposal for hit in flags},
                "flag_reasons": {hit.model_id: hit.reason for hit in flags},
                "unsure_reasons": {hit.model_id: hit.reason for hit in unsure},
                "comparison_group_membership": comparison_membership,
                "reject_groups": scan.reject_reasons(rows, reject, conditions["tasks"][0]),
            },
            "corpus_snapshot": snapshot,
            "judged_by": None,
            "judged_on": None,
        })

        worksheet.append(f"### `{item['query_id']}` {condition_label(conditions)} "
                         f"· {conditions['tasks'][0]} · {difficulty}")
        worksheet.append("")
        worksheet.append(f"> {item['query']}")
        worksheet.append("")
        worksheet.append("조건 → 질의문 근거")
        worksheet.append("")
        for key, source in item["fidelity"].items():
            worksheet.append(f"- `{key}={json.dumps(conditions[key], ensure_ascii=False)}` ← {source}")
        worksheet.append("")
        worksheet.append("판정 규칙 (판정 전에 고정)")
        worksheet.append("")
        worksheet.append(f"- **must** {rule.must_label}")
        worksheet.append(f"- **2점** {rule.grade_2_label}")
        worksheet.append(f"- **1점** {rule.grade_1_label}")
        if rule.comparison_groups:
            worksheet.append(
                "- **비교 완결성** "
                + " / ".join(rule.comparison_groups)
                + " 계열이 최종 정답에 각각 하나 이상 있어야 한다"
            )
        worksheet.append("")
        worksheet.append(f"후보 {len(rows)}개 전수 스캔 → "
                         f"🚩 {len(flags)} / ⚠️ {len(unsure)} / ✅ {len(reject)}")
        worksheet.append("")

        if flags:
            worksheet.append("#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요")
            worksheet.append("")
            if rule.comparison_groups:
                worksheet.append("| 비교 대상 | 모델 | 제안 | 근거 | 확정 |")
                worksheet.append("|---|---|:--:|---|:--:|")
            else:
                worksheet.append("| 모델 | 제안 | 근거 | 확정 |")
                worksheet.append("|---|:--:|---|:--:|")
            for hit in flags:
                if rule.comparison_groups:
                    worksheet.append(
                        f"| {' / '.join(hit.comparison_groups)} | `{hit.model_id}` | "
                        f"{hit.proposal}점 | {hit.reason} |  |"
                    )
                else:
                    worksheet.append(f"| `{hit.model_id}` | {hit.proposal}점 | {hit.reason} |  |")
            worksheet.append("")
        if unsure:
            worksheet.append("#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다")
            worksheet.append("")
            if rule.comparison_groups:
                worksheet.append("| 비교 대상 | 모델 | 왜 애매한가 | 확정 |")
                worksheet.append("|---|---|---|:--:|")
            else:
                worksheet.append("| 모델 | 왜 애매한가 | 확정 |")
                worksheet.append("|---|---|:--:|")
            for hit in unsure:
                if rule.comparison_groups:
                    worksheet.append(
                        f"| {' / '.join(hit.comparison_groups) or '미분류'} | `{hit.model_id}` | "
                        f"{hit.reason} |  |"
                    )
                else:
                    worksheet.append(f"| `{hit.model_id}` | {hit.reason} |  |")
            worksheet.append("")
        groups = scan.reject_reasons(rows, reject, conditions["tasks"][0])
        if groups:
            worksheet.append("#### ✅ 명백한 오답 — 소분류만 보고 넘기세요")
            worksheet.append("")
            for reason, ids in groups.items():
                worksheet.append(f"- **{reason}** {len(ids)}개 — "
                                 + ", ".join(f"`{model_id}`" for model_id in ids[:6])
                                 + (" …" if len(ids) > 6 else ""))
            worksheet.append("")
        worksheet.append("")

    (V2 / "judged").mkdir(parents=True, exist_ok=True)
    out = V2 / "judged" / f"{query_type}.jsonl"
    with out.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    total_human = sum(len(r["verification"]["flagged_for_human"])
                      + len(r["verification"]["unsure_for_human"]) for r in records)
    header = [
        f"# {query_type} 판정 워크시트",
        "",
        "**숫자 검증은 명령 한 줄이 전부 합니다.**",
        "",
        "```bash",
        f"cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py {query_type}",
        "```",
        "",
        "## 정훈님이 판단할 것",
        "",
        "| | 질문 | 아니라면 |",
        "|---|---|---|",
        "| **①** | 조건이 질의문이 요구한 것을 넘지 않나? | 조건을 뺀다 |",
        "| **②** | 🚩 의 제안 등급(2점/1점)이 맞나? | 고친다 |",
        "| **③** | ⚠️ 중에 정답이 섞여 있나? | 정답으로 올린다 |",
        "",
        "③이 재현율 방어선입니다. 빠진 정답은 걸러낸 쪽에 숨어 있으므로 🚩만 보면",
        "영원히 못 찾습니다. ✅ 더미는 소분류 이유만 읽고 넘기시면 됩니다.",
        "",
        "### 등급 기준 (유형 공통)",
        "",
        "| 등급 | 뜻 |",
        "|---:|---|",
        "| **2** | 질의의 모든 조건을 데이터로 확인 + 용도가 정확히 일치 |",
        "| **1** | 조건은 충족하나 도메인이 넓거나 좁음 / 근거 미확인 / 변환본·재업로드 |",
        "| **0** | 기록하지 않음 — 라벨에 없으면 오답 |",
        "",
        f"코퍼스 {meta['rows']}행 · {meta['corpus_refreshed_at'][:10]} 기준 · "
        f"질의 {len(records)}개 · 사람이 볼 것 **{total_human}개**",
        "",
        "---",
        "",
    ]
    (V2 / "worksheets").mkdir(parents=True, exist_ok=True)
    (V2 / "worksheets" / f"{query_type}.md").write_text(
        "\n".join(header + worksheet) + "\n", encoding="utf-8"
    )

    print()
    print(f"사람이 볼 것 합계 {total_human}개 (질의당 평균 {total_human / len(records):.1f}개)")
    if overflow:
        print(f"⚠️ 질의당 {PILE_LIMIT}개를 넘긴 질의: {overflow} — 용도를 더 구체적으로 다시 쓸 것")
    if comparison_coverage_gaps:
        print("❌ 비교 대상 커버리지 오류:")
        for gap in comparison_coverage_gaps:
            print(f"  · {gap}")
    print(f"→ {out}")
    print(f"→ {V2 / 'worksheets' / (query_type + '.md')}")
    if comparison_coverage_gaps:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
