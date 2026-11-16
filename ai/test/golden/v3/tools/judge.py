#!/usr/bin/env python3
"""사람 판정 한 건을 review/judgments/<유형>.jsonl 에 기록한다.

    python test/golden/v3/tools/judge.py st01 BM-K/KoSimCSE-roberta --decision approve --reason "카드에 STS 학습 명시" --by 정훈
    python test/golden/v3/tools/judge.py sc06 some/model --decision 1 --reason "다국어 reranker" --by 정훈
    python test/golden/v3/tools/judge.py --status            # 유형별 남은 판정 수

decision
    approve  Claude 제안 점수를 그대로 확정(unresolved 후보에는 쓸 수 없다)
    2 / 1    점수를 직접 정한다
    exclude  정답 아님
    hold     보류(final 검증을 통과하지 못한다)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_drafts import JUDGMENTS  # noqa: E402

DECISIONS = ("approve", "2", "1", "exclude", "hold")


def load(path: Path) -> list:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def final_grade(decision: str, proposed: int | None, proposed_class: str | None = None) -> int | None:
    if proposed_class == "abstain":
        if decision not in ("approve", "hold"):
            raise SystemExit("기권 질의는 approve(정답 없음 확인) 또는 hold 만 쓴다")
        return None
    if decision == "approve":
        if proposed is None:
            raise SystemExit("unresolved 후보는 approve 할 수 없다. 2 / 1 / exclude 중 하나로 정한다")
        return proposed
    if decision in ("2", "1"):
        return int(decision)
    return 0 if decision == "exclude" else None


def status() -> int:
    for path in sorted(JUDGMENTS.glob("*.jsonl")):
        items = load(path)
        left = sum(1 for i in items if i.get("decision") in (None, "hold"))
        print(f"{path.stem:24s} 후보 {len(items):3d}  남은 판정 {left:3d}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query_id", nargs="?")
    parser.add_argument("model_id", nargs="?")
    parser.add_argument("--decision", choices=DECISIONS)
    parser.add_argument("--reason", default="")
    parser.add_argument("--by", default="")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()
    if args.status:
        return status()
    if not (args.query_id and args.model_id and args.decision):
        parser.error("query_id, model_id, --decision 이 필요하다")
    if args.decision != "hold" and not (args.reason.strip() and args.by.strip()):
        parser.error("확정 판정에는 --reason 과 --by 가 필요하다")
    for path in sorted(JUDGMENTS.glob("*.jsonl")):
        items = load(path)
        for item in items:
            if item["query_id"] == args.query_id and item["model_id"] == args.model_id:
                item.update({
                    "decision": args.decision,
                    "final_grade": final_grade(args.decision, item.get("proposed_grade"), item.get("proposed_class")),
                    "judgment_reason": args.reason.strip() or None,
                    "judged_by": args.by.strip() or None,
                    "judged_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                })
                path.write_text("".join(json.dumps(i, ensure_ascii=False, sort_keys=True) + "\n" for i in items),
                                encoding="utf-8")
                print(f"기록: {args.query_id} {args.model_id} → {args.decision} ({item['final_grade']})")
                return 0
    raise SystemExit(f"{args.query_id} 의 후보에 {args.model_id} 가 없다")


if __name__ == "__main__":
    raise SystemExit(main())
