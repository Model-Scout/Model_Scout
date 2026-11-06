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


def condition_label(conditions: Dict[str, Any]) -> str:
    parts = []
    if "max_parameters_billion" in conditions:
        cap = conditions["max_parameters_billion"]
        parts.append(f"≤{round(cap * 1000)}M" if cap < 1 else f"≤{cap}B")
    if "min_context_length" in conditions:
        parts.append(f"ctx≥{conditions['min_context_length']:,}")
    if conditions.get("pools") == ["core"]:
        parts.append("core만")
    return " · ".join(parts)


def abstention_worksheet(records: List[Dict[str, Any]]) -> str:
    meta = json.loads((V2 / "corpus_snapshot.meta.json").read_text(encoding="utf-8"))
    out: List[str] = []

    out.append("# abstention 판정 워크시트")
    out.append("")
    out.append("**읽고 판단하면 됩니다. 명령을 10번 돌릴 필요 없습니다.**")
    out.append("숫자가 맞는지는 아래 한 줄이 전부 확인합니다.")
    out.append("")
    out.append("```bash")
    out.append("cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py abstention")
    out.append("```")
    out.append("")
    out.append("`✅ 기계 검증 전부 통과`가 나오면 다음을 확인한 것입니다.")
    out.append("")
    out.append("- 조건이 하드 필터가 실제로 읽는 키인지 (`HARD_FILTER_KEYS`)")
    out.append("- 조건마다 질의문 근거가 적혀 있는지")
    out.append("- `eligible == 0`이 지금도 재현되는지")
    out.append("- 정답이 잘못 기록돼 있지 않은지")
    out.append("- 판정 기준 코퍼스가 같은 스냅샷인지")
    out.append("")
    out.append("## 정훈님이 판단할 것 — 두 가지")
    out.append("")
    out.append("정답이 없는 유형이라 **모델 카드를 열어볼 것이 없습니다.**")
    out.append("")
    out.append("| | 질문 | 아니라면 |")
    out.append("|---|---|---|")
    out.append("| **①** | 이 질의를 실제로 누가 물어볼까? | 질의문을 바꾼다 |")
    out.append("| **②** | 조건이 질의문이 요구한 것을 넘지 않나? | 조건을 뺀다 |")
    out.append("")
    out.append("②가 핵심입니다. 질의에 없는 조건이 끼어 있으면 후보가 부당하게 깎이고,")
    out.append("정답이 있는 유형에서는 그게 바로 정답 누락이 됩니다. abstention에서는")
    out.append("\"없어야 할 이유\"가 질의문에 다 적혀 있는지를 보는 것입니다.")
    out.append("")
    out.append("### 수치값이 없는 모델의 처리")
    out.append("")
    out.append("실제 Supabase 검색과 같은 규칙을 씁니다. 파라미터·컨텍스트의 상한 또는 하한을")
    out.append("요구하면, 값이 없는 모델은 그 수치를 만족한다고 **검증할 수 없으므로 후보에서")
    out.append("제외**됩니다. 따라서 질문에 \"공개된 / 확인된 모델만\" 같은 말을 인위적으로")
    out.append("넣지 않습니다. 이 처리 자체가 데이터 품질의 한계이므로, 미기재 모델을 더")
    out.append("채우는 일은 별도 백필 작업으로 계속 추적합니다.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 질의 10개")
    out.append("")
    out.append(f"코퍼스 {meta['rows']}행 · {meta['corpus_refreshed_at'][:10]} 기준 · "
               f"easy {sum(1 for r in records if r['difficulty'] == 'easy')} / "
               f"hard {sum(1 for r in records if r['difficulty'] == 'hard')}")
    out.append("")

    for record in records:
        conditions = record["conditions"]
        temptation = record["temptation"]
        out.append(f"### `{record['query_id']}` {condition_label(conditions)} "
                   f"· {conditions['tasks'][0]} · {record['difficulty']}")
        out.append("")
        out.append(f"> {record['query']}")
        out.append("")
        pairs = [
            f"`{key}={json.dumps(conditions[key], ensure_ascii=False)}` ← {source}"
            for key, source in record["conditions_fidelity"].items()
        ]
        out.append("조건 → 질의문 근거")
        out.append("")
        for pair in pairs:
            out.append(f"- {pair}")
        out.append("")
        out.append(f"후보 **0개** · 유혹 후보 {temptation['pool_size']}개"
                   f"(조건완화 {temptation['relaxed_conditions']} / 수치제거 {temptation['without_numeric_constraints']})")
        out.append("")
        out.append("**① 물어볼 만한 질의인가** ☐ 예  ☐ 아니오 → ")
        out.append("")
        out.append("**② 조건이 질의문을 넘지 않나** ☐ 예  ☐ 아니오 → ")
        out.append("")

    out.append("---")
    out.append("")
    out.append("## 제가 불확실한 것")
    out.append("")
    small = [r for r in records if r["conditions"].get("max_parameters_billion") == 0.01]
    if small:
        ids = ", ".join(f"`{r['query_id']}`" for r in small)
        out.append(f"**10M 이하 질의가 {len(small)}개입니다** ({ids}). 10M은 아주 작습니다 —")
        out.append("비교하면 `whisper-tiny`가 39M, `MiniLM-L6`이 22M입니다. 그래서 \"실제로")
        out.append("물어볼 질문인가\"가 의심스럽습니다. 과하다고 보시면 조건을 올리겠습니다.")
        out.append("다만 숫자를 올리면 후보가 0이 아니게 되는 task가 있어서, 그때는 질의를")
        out.append("다른 조합으로 바꿔야 합니다.")
        out.append("")
    out.append("**`ab06`은 `pools: [\"core\"]`를 씁니다.** \"많이 쓰이는\"을 다운로드 500 이상으로")
    out.append("옮긴 것인데, 이 해석이 과한지 봐주세요. core/low 경계는 다운로드 500입니다.")
    out.append("")
    out.append("## 고칠 것이 있으면")
    out.append("")
    out.append("`tools/make_abstention.py`의 `SPECS`를 고치고 다시 생성합니다.")
    out.append("")
    out.append("```bash")
    out.append("cd ai")
    out.append("../.venv/bin/python test/golden/v2/tools/make_abstention.py    # eligible==0 재확인")
    out.append("../.venv/bin/python test/golden/v2/tools/make_worksheet.py abstention")
    out.append("```")
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
