#!/usr/bin/env python3
"""질문 후보를 한 곳에 모은다. 정답은 가져오지 않는다.

정답(모델 ID)은 2026-11-14 재적재로 바뀌었으므로 전부 버리고, 질문 문장과
조건만 재활용한다. 채점은 현재 코퍼스에 전수 스캔으로 다시 한다.

출처
  labels/   희원님이 9~10월에 만든 178개.
            28개는 실제 커뮤니티 글에서 재구성(출처 URL 확인됨),
            150개는 생성 질의 + 판정실 사람 채점.
  pool      11월 초 v3 작업에서 쓴 60개(abstention 10 제외). v3 디렉터리는 폐기했고
            질문 문장과 채점 규칙만 이 pool.jsonl 에 남겨 이어받는다.

    python test/model_retrieval/tools/collect_questions.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
OUT = AI / "test" / "model_retrieval" / "queries" / "pool.jsonl"
LABELS = AI / "test" / "golden" / "labels"

# retrieval_lab / 05_validate_retrieval 가 아는 하드 필터 키만 옮긴다.
FILTER_KEYS = ("tasks", "korean_required", "max_parameters_billion", "min_parameters_billion",
               "min_context_length", "max_context_length", "popularity_tier",
               "commercial_status", "require_artifact", "max_artifact_gib", "exclude_gated")


def from_labels() -> List[Dict[str, Any]]:
    out = []
    for name, origin in (("semantic_golden_queries.jsonl", "community_case"),
                         ("semantic_judged_queries.jsonl", "generated_judged")):
        path = LABELS / name
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            record: Dict[str, Any] = {
                "qid": item["id"],
                "text": item["text"],
                "query_type": item.get("plan_query_type") or item.get("query_type"),
                "origin": origin,
                "source_url": item.get("source_url"),
                "conditions": {k: item[k] for k in FILTER_KEYS
                               if isinstance(item.get(k), bool) or item.get(k) not in (None, [], False)},
                # 참고용. 채점에는 쓰지 않는다(코퍼스가 바뀌어 정답이 달라졌다).
                "old_answers": sorted(set((item.get("labels") or {}).get("expected_any") or [])
                                      | set((item.get("labels") or {}).get("expected_all") or [])),
                "relevance_rule": None,
            }
            out.append(record)
    return out


def carried_over() -> List[Dict[str, Any]]:
    """폐기한 v3 작업에서 가져온 질문을 pool.jsonl 에서 그대로 이어받는다.

    v3 디렉터리를 지웠으므로 원본은 더 없다. 이 레코드가 유일한 기록이고,
    질문 문장·조건·채점 규칙만 들어 있다(정답 모델 ID 는 애초에 버렸다).
    """
    if not OUT.exists():
        return []
    return [item for line in OUT.read_text(encoding="utf-8").splitlines() if line.strip()
            for item in [json.loads(line)] if item.get("origin") == "golden_v3"]


def main() -> int:
    pool = from_labels() + carried_over()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in pool), encoding="utf-8")

    by = defaultdict(lambda: defaultdict(int))
    for r in pool:
        by[r["query_type"]][r["origin"]] += 1
    print(f"{OUT.relative_to(AI)} — 질문 {len(pool)}개\n")
    print(f"{'유형':24s} {'커뮤니티':>7s} {'생성·판정':>8s} {'v3':>4s} {'합':>4s} {'규칙있음':>7s}")
    for t in sorted(by):
        g = by[t]
        has = sum(1 for r in pool if r["query_type"] == t and r["relevance_rule"])
        print(f"{t:24s} {g['community_case']:>7d} {g['generated_judged']:>8d} "
              f"{g['golden_v3']:>4d} {sum(g.values()):>4d} {has:>7d}")
    print(f"\n채점 규칙이 있는 질문: {sum(1 for r in pool if r['relevance_rule'])} / {len(pool)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
