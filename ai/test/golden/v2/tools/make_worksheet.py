#!/usr/bin/env python3
"""판정 워크시트를 만든다. 사람이 확인할 것만 추려서 마크다운으로 낸다.

abstention은 정답이 없으므로 확인 항목이 다르다. 모델 카드를 열어볼 것이 없고,
대신 조건이 질의문과 맞는지(conditions_fidelity)와 eligible == 0이 실제로
재현되는지만 보면 된다.

    python test/golden/v2/tools/make_worksheet.py abstention
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_v2  # noqa: E402

V2 = Path(__file__).resolve().parents[1]


def read_judged(query_type: str) -> List[Dict[str, Any]]:
    path = V2 / "judged" / f"{query_type}.jsonl"
    if not path.exists():
        raise SystemExit(f"{path} 없음")
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def abstention_worksheet(records: List[Dict[str, Any]]) -> str:
    meta = json.loads((V2 / "corpus_snapshot.meta.json").read_text(encoding="utf-8"))
    out: List[str] = []
    out.append("# abstention 판정 워크시트")
    out.append("")
    out.append(f"- 판정 기준 코퍼스 **{meta['rows']}행** "
               f"(Supabase active, {meta['corpus_refreshed_at'][:10]} 기준, GitHub Actions 중단)")
    out.append(f"- sync_run_id `{meta['last_sync_run_id']}`")
    out.append(f"- 질의 {len(records)}개 — "
               f"easy {sum(1 for r in records if r['difficulty'] == 'easy')} / "
               f"hard {sum(1 for r in records if r['difficulty'] == 'hard')}")
    out.append("")
    out.append("## 이 유형에서 확인할 것")
    out.append("")
    out.append("정답이 없는 유형이라 모델 카드를 열어볼 것이 없습니다. 두 가지만 봐주세요.")
    out.append("")
    out.append("1. **조건이 질의문과 맞나** — `conditions`의 각 키가 질의 문장의 어느 말에서")
    out.append("   왔는지 적어뒀습니다. 질의에 없는 조건이 끼어 있으면 그 질의는 못 씁니다.")
    out.append("2. **후보가 정말 0개인가** — 각 질의마다 재현 명령을 적어뒀습니다.")
    out.append("")
    out.append("## require_known_* 가 왜 들어가 있나")
    out.append("")
    out.append("`numeric_ok`는 값이 없으면 조건을 통과시킵니다. 코퍼스의 파라미터 39.4%, ")
    out.append("컨텍스트 37.7%가 미공개이므로, 이 플래그를 끄면 수치 조건만으로는 후보가 ")
    out.append("0이 될 수 없습니다. 그래서 질의문에 \"명시된 / 공개된 / 확인된\"을 넣어 ")
    out.append("**검증 가능성을 질의의 요구사항으로** 만들었습니다. 숨은 필터가 아닙니다.")
    out.append("")
    out.append("## 난이도 — 유혹 후보의 크기")
    out.append("")
    out.append("검색이 틀리는 방식은 \"조건을 만족하지 않는 비슷한 모델을 끌어다 답하는 것\"입니다.")
    out.append("그런 모델이 몇 개인지를 두 경로로 재서 큰 쪽을 썼습니다.")
    out.append("")
    out.append("| 경로 | 뜻 |")
    out.append("|---|---|")
    out.append("| 수치 완화 | 상한·하한을 한 칸 느슨하게 → 경계 바로 밖의 모델 수 |")
    out.append("| 미공개 허용 | `require_known_*` 제거 → 만족할 수도 있으나 확인 불가한 모델 수 |")
    out.append("")
    out.append(f"기준값은 `planner_config.json`의 `top_k`(30)입니다. 유혹 후보가 그보다 적으면 ")
    out.append("검색이 상위 10개를 채울 만큼 끌어올 것이 애초에 부족합니다.")
    out.append("")
    out.append("## 요약표")
    out.append("")
    out.append("| id | task | 조건 | eligible | 수치완화 | 미공개허용 | 유혹 | 난이도 |")
    out.append("|---|---|---|---:|---:|---:|---:|---|")
    for record in records:
        conditions = record["conditions"]
        temptation = record["temptation"]
        parts = []
        if "max_parameters_billion" in conditions:
            parts.append(f"≤{conditions['max_parameters_billion']}B")
        if "min_context_length" in conditions:
            parts.append(f"ctx≥{conditions['min_context_length']}")
        if conditions.get("pools") == ["core"]:
            parts.append("core만")
        out.append(
            f"| `{record['query_id']}` | {conditions['tasks'][0]} | {' · '.join(parts)} | "
            f"**{record['eligible_count']}** | {temptation['relaxed_numeric']} | "
            f"{temptation['allow_unverified']} | {temptation['pool_size']} | {record['difficulty']} |"
        )
    out.append("")
    out.append("---")
    out.append("")

    for record in records:
        conditions = record["conditions"]
        temptation = record["temptation"]
        out.append(f"## `{record['query_id']}` · {conditions['tasks'][0]} · {record['difficulty']}")
        out.append("")
        out.append(f"> {record['query']}")
        out.append("")
        out.append("**조건이 질의문의 어디서 왔나**")
        out.append("")
        out.append("| 조건 | 값 | 질의문 근거 |")
        out.append("|---|---|---|")
        for key, source in record["conditions_fidelity"].items():
            out.append(f"| `{key}` | `{json.dumps(conditions[key], ensure_ascii=False)}` | {source} |")
        out.append("")
        out.append(f"**후보 수** `eligible = {record['eligible_count']}`")
        out.append("")
        out.append("재현:")
        out.append("")
        out.append("```bash")
        out.append("cd ai && ../.venv/bin/python -c \"")
        out.append("import sys; sys.path.insert(0,'test/golden/v2/tools')")
        out.append("import corpus_v2")
        out.append(f"print(corpus_v2.count(**{json.dumps(conditions, ensure_ascii=False)}))\"")
        out.append("```")
        out.append("")
        out.append(f"**유혹 후보** {temptation['pool_size']}개 "
                   f"(수치완화 {temptation['relaxed_numeric']} / 미공개허용 {temptation['allow_unverified']}) "
                   f"→ 기준 {temptation['threshold']} → **{record['difficulty']}**")
        out.append("")
        out.append("판정: ☐ 조건이 질의와 맞음  ☐ eligible 0 재현됨  ☐ 질의문이 자연스러움")
        out.append("")
        out.append("---")
        out.append("")
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query_type", help="유형 이름 (judged/<이름>.jsonl 을 읽는다)")
    args = parser.parse_args()

    records = read_judged(args.query_type)
    if args.query_type != "abstention":
        raise SystemExit(f"{args.query_type}용 워크시트는 아직 없습니다. abstention만 지원합니다.")

    # 파일에 적힌 eligible 수가 지금도 맞는지 다시 확인한다.
    drift = []
    for record in records:
        now = corpus_v2.count(**record["conditions"])
        if now != record["eligible_count"]:
            drift.append((record["query_id"], record["eligible_count"], now))
    if drift:
        print(f"⚠️ eligible 수가 달라진 질의 {len(drift)}개: {drift}")
        raise SystemExit(1)
    print(f"eligible 재확인 완료 — {len(records)}개 질의 전부 일치")

    path = V2 / "worksheets" / f"{args.query_type}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(abstention_worksheet(records) + "\n", encoding="utf-8")
    print(f"→ {path}")


if __name__ == "__main__":
    main()
