#!/usr/bin/env python3
"""보류(README 원문에만 근거가 있어 도구가 판단을 미룬 것)를 1차 판정한다.

scan 은 근거가 evidence(README 원문)에서만 나오면 사람에게 넘긴다. 그중 상당수는
기계적으로 가릴 수 있다 — 한계 고지("may differ"), 미지원 서술("does not
support"), 약관 링크, 설치 안내, HTML 태그는 능력의 근거가 아니다.

여기서 거르고 남은 것만 사람이 본다. 판정은 spec 을 고치지 않고 별도 파일에
쌓으므로, 언제든 되돌리거나 사람 판정으로 덮어쓸 수 있다.

    python test/model_retrieval/tools/triage_unresolved.py            # 집계만
    python test/model_retrieval/tools/triage_unresolved.py --write    # 판정 저장
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

AI = Path(__file__).resolve().parents[3]
QUERIES = AI / "test" / "model_retrieval" / "queries"
OUT = QUERIES / "triage.json"
sys.path.insert(0, str(Path(__file__).resolve().parent))

SPECS = ["spec_capability.py", "spec_constraint.py"]

# 근거로 볼 수 없는 문장. 맞으면 제외한다.
REJECT: List[Tuple[str, str]] = [
    (r"may (differ|vary|be lower|experience lower|not )", "한계 고지 — 능력을 보장하지 않는 문장"),
    (r"(does|do|is|are|was|were) not (support|include|designed|intended|recommend)",
     "미지원 서술 — 그 능력이 없다는 문장"),
    (r"지원하지 ?않|해당하지 ?않|권장하지 ?않", "미지원 서술"),
    (r"privacy polic|개인정보처리방침|이용 ?약관|license_link|terms of (use|service)",
     "약관·링크 — 기능 설명이 아니다"),
    (r"pip install|requirements\.txt|```bash|git clone|huggingface-cli", "설치 안내"),
    (r"<(details|summary|table|thead|tbody|tr|th|td|picture|img)\b", "HTML 태그"),
    (r"(is|are|was|were) summarized|summary table|results? (are|is) summar", "상투어 — 결과 요약"),
]
# 반대로, 이 꼴이면 근거로 인정한다(1점). 단정적으로 능력을 말한다.
ACCEPT: List[Tuple[str, str]] = [
    (r"(trained|fine-?tuned|optimized|designed|built) (on|for|to)", "학습·설계 목적을 밝힘"),
    (r"(supports?|capable of|can (be used to|perform)|specializ)", "능력을 선언함"),
    (r"학습(했|됐|되었)|특화|용도로|설계(했|됐)", "학습·용도를 밝힘"),
]


def load(name: str) -> List[Dict[str, Any]]:
    spec = importlib.util.spec_from_file_location(name[:-3], QUERIES / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.QUERIES)


def judge(snippet: str) -> Tuple[Optional[int], str]:
    """(점수, 이유). 점수 None 이면 사람이 봐야 한다."""
    for pattern, why in REJECT:
        if re.search(pattern, snippet, re.IGNORECASE):
            return 0, why
    for pattern, why in ACCEPT:
        if re.search(pattern, snippet, re.IGNORECASE):
            return 1, why
    return None, "근거 문장만으로는 판단할 수 없다"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    import corpus
    import scan

    rows = corpus.load_corpus()
    out: Dict[str, Dict[str, Any]] = {}
    tally: Counter = Counter()
    left: List[Tuple[str, str, str]] = []
    for name in SPECS:
        for item in load(name):
            query = dict(item)
            query.update(query_id=item["qid"], expected_behavior="recommend", query=item["text"])
            for model_id, decision in scan.scan_query(query, rows)["decisions"].items():
                if decision["class"] != "unresolved_for_human":
                    continue
                snippet = (decision.get("evidence") or {}).get("snippet", "")
                grade, why = judge(snippet)
                tally[why] += 1
                if grade is None:
                    left.append((item["qid"], model_id, snippet[:100]))
                    continue
                out.setdefault(item["qid"], {})[model_id] = {"grade": grade, "reason": why}

    done = sum(len(v) for v in out.values())
    print(f"보류 {done + len(left)}건\n  기계가 가린 것 {done}  ·  사람이 볼 것 {len(left)}\n")
    for why, n in tally.most_common():
        print(f"  {n:>4d}  {why}")
    if args.write:
        OUT.write_text(json.dumps({"__note__": "보류 1차 판정. 0=제외, 1=부분 점수. "
                                                "사람 판정이 있으면 그것이 이긴다.",
                                   **out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\n→ {OUT.relative_to(AI)}")
    print(f"\n사람이 볼 {len(left)}건의 예:")
    for qid, model_id, snippet in left[:8]:
        print(f"  {qid} {model_id[:42]:42s} …{snippet[:70]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
