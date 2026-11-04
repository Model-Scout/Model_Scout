#!/usr/bin/env python3
"""abstention 질의 10개를 작성하고 eligible == 0을 실측으로 검증한다.

선정 기준
---------
① task 분산 — 한 task에 2개까지
② 하드 필터 종류를 섞음 — 파라미터 상한 / context 하한 / core 풀 한정
③ 경계에서 한 칸 들어간 조합 — 0이 아슬아슬하지 않게
④ 사람이 실제로 물어볼 만한 질의문 — 5M 같은 극단값은 쓰지 않는다

난이도 — 유혹 후보(temptation pool)의 크기
------------------------------------------
abstention에서 검색이 틀리는 방식은 "비슷하지만 조건을 만족하지 않는 모델을 끌어다
답하는 것"이다. 그래서 난이도는 그런 모델이 몇 개나 있는지로 정한다. 두 경로를 재서
큰 쪽을 쓴다.

  ① 수치 완화     상한/하한을 한 칸 느슨하게 → 경계 바로 밖의 모델 수
  ② 미공개 허용   require_known_* 를 빼면 → 조건을 만족할 수도 있으나 확인 불가한 모델 수

②를 빠뜨리면 난이도를 크게 잘못 본다. 예를 들어 image-text-to-text ≤0.1B는 수치를
0.3B로 완화해도 0이지만, 미공개를 허용하면 227개가 나온다. 검색이 끌어올 유혹은
거기서 생긴다.

기준값은 ``planner_config.json``의 ``top_k``(30)를 쓴다. 유혹 후보가 top_k보다 적으면
검색이 상위 10개를 채울 만큼 끌어올 것이 애초에 부족하다.

require_known_* 플래그
----------------------
숨은 필터가 아니라 질의의 의미다. numeric_ok는 값이 없으면 통과시키므로, 플래그를
끄면 미공개 모델(파라미터 39.4% / 컨텍스트 37.7%)이 모든 수치 조건을 통과해 후보가
0이 될 수 없다. "컨텍스트 100만 토큰 이상인 모델"을 추천하려면 그 길이가 문서로
확인돼야 하므로, 질의문에 "확인된/명시된"을 넣고 플래그로 그 뜻을 표현한다.

    python test/golden/v2/tools/make_abstention.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_v2  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "judged" / "abstention.jsonl"

# planner_config.json의 top_k. 유혹 후보가 이보다 적으면 검색이 끌어올 것이 부족하다.
TOP_K = 30

# (query_id, 질의문, conditions, conditions_fidelity, 완화 조건)
SPECS: List[Dict[str, Any]] = [
    {
        "query_id": "ab01",
        "query": "온디바이스로 돌릴 수 있게 파라미터 100M 이하인 한국어 이미지 이해 모델을 찾고 있어. 파라미터 수가 명시된 것만.",
        "conditions": {
            "tasks": ["image-text-to-text"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "이미지 이해 → image-text-to-text",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 100M 이하 → 0.1B",
            "require_known_parameters": "파라미터 수가 명시된 것만",
        },
        "relaxed": {"max_parameters_billion": 0.3},
    },
    {
        "query_id": "ab02",
        "query": "파라미터 50M 이하인 초소형 한국어 요약 모델이 필요해. 파라미터 수가 공개된 모델로.",
        "conditions": {
            "tasks": ["summarization"],
            "korean_required": True,
            "max_parameters_billion": 0.05,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "요약",
            "korean_required": "한국어",
            "max_parameters_billion": "50M 이하 → 0.05B",
            "require_known_parameters": "파라미터 수가 공개된",
        },
        "relaxed": {"max_parameters_billion": 0.3},
    },
    {
        "query_id": "ab03",
        "query": "컨텍스트 길이가 262144 토큰 이상인 것으로 확인된 한국어 질의응답 모델 있어?",
        "conditions": {
            "tasks": ["question-answering"],
            "korean_required": True,
            "min_context_length": 262144,
            "require_known_context": True,
        },
        "fidelity": {
            "tasks": "질의응답",
            "korean_required": "한국어",
            "min_context_length": "262144 토큰 이상",
            "require_known_context": "것으로 확인된",
        },
        "relaxed": {"min_context_length": 131072},
    },
    {
        "query_id": "ab04",
        "query": "파라미터 10M 이하로 명시된 한국어 질의응답 모델을 추천해줘.",
        "conditions": {
            "tasks": ["question-answering"],
            "korean_required": True,
            "max_parameters_billion": 0.01,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "질의응답",
            "korean_required": "한국어",
            "max_parameters_billion": "10M 이하 → 0.01B",
            "require_known_parameters": "로 명시된",
        },
        "relaxed": {"max_parameters_billion": 0.05},
    },
    {
        "query_id": "ab05",
        "query": "책 한 권을 통째로 번역하려고 해. 컨텍스트 100만 토큰 이상이 확인된 한국어 번역 모델을 찾아줘.",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
            "min_context_length": 1000000,
            "require_known_context": True,
        },
        "fidelity": {
            "tasks": "번역",
            "korean_required": "한국어",
            "min_context_length": "100만 토큰 이상",
            "require_known_context": "이 확인된",
        },
        "relaxed": {"min_context_length": 262144},
    },
    {
        "query_id": "ab06",
        "query": "많이 쓰이는 한국어 번역 모델 중에서 파라미터 100M 이하로 공개된 게 있을까?",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 0.1,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "번역",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
            "max_parameters_billion": "100M 이하 → 0.1B",
            "require_known_parameters": "로 공개된",
        },
        "relaxed": {"pools": ["core", "low_popularity"]},
    },
    {
        "query_id": "ab07",
        "query": "아주 긴 문서를 분류해야 해. 컨텍스트 524288 토큰 이상으로 확인된 한국어 텍스트 분류 모델 있어?",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "min_context_length": 524288,
            "require_known_context": True,
        },
        "fidelity": {
            "tasks": "텍스트 분류",
            "korean_required": "한국어",
            "min_context_length": "524288 토큰 이상",
            "require_known_context": "으로 확인된",
        },
        "relaxed": {"min_context_length": 131072},
    },
    {
        "query_id": "ab08",
        "query": "파라미터 50M 이하로 명시된 한국어 임베딩 모델을 찾고 있어.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "max_parameters_billion": 0.05,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "임베딩 → feature-extraction",
            "korean_required": "한국어",
            "max_parameters_billion": "50M 이하 → 0.05B",
            "require_known_parameters": "로 명시된",
        },
        "relaxed": {"max_parameters_billion": 0.3},
    },
    {
        "query_id": "ab09",
        "query": "파라미터 10M 이하로 공개된 한국어 문장 유사도 모델이 있나?",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "max_parameters_billion": 0.01,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "max_parameters_billion": "10M 이하 → 0.01B",
            "require_known_parameters": "로 공개된",
        },
        "relaxed": {"max_parameters_billion": 0.05},
    },
    {
        "query_id": "ab10",
        "query": "파라미터 10M 이하로 명시된 한국어 음성 인식 모델을 추천해줘.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "max_parameters_billion": 0.01,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "음성 인식 → automatic-speech-recognition",
            "korean_required": "한국어",
            "max_parameters_billion": "10M 이하 → 0.01B",
            "require_known_parameters": "로 명시된",
        },
        "relaxed": {"max_parameters_billion": 0.05},
    },
]


def main() -> None:
    meta = json.loads(
        (Path(__file__).resolve().parents[1] / "corpus_snapshot.meta.json").read_text(encoding="utf-8")
    )
    snapshot = {
        "source": meta["source"],
        "rows": meta["rows"],
        "sync_run_id": meta["last_sync_run_id"],
        "refreshed_at": meta["corpus_refreshed_at"],
    }

    print(f"판정 기준 코퍼스 {meta['rows']}행 (Actions 중단 시점 확정 집합)")
    print()
    print(f"{'id':6s} {'task':28s} {'elig':>5s} {'수치완화':>8s} {'미공개허용':>10s} {'유혹':>5s} {'난이도':>7s}")
    print("-" * 78)

    records = []
    failures = []
    for spec in SPECS:
        conditions = spec["conditions"]
        eligible = corpus_v2.count(**conditions)

        # ① 수치 완화: 경계 바로 밖에 몇 개가 있나
        numeric = dict(conditions)
        numeric.update(spec["relaxed"])
        relaxed_numeric = corpus_v2.count(**numeric)

        # ② 미공개 허용: 조건을 만족할 수도 있으나 확인 불가한 모델이 몇 개인가
        unverified = {
            key: value
            for key, value in conditions.items()
            if key not in ("require_known_parameters", "require_known_context")
        }
        relaxed_unknown = corpus_v2.count(**unverified)

        temptation = max(relaxed_numeric, relaxed_unknown)
        difficulty = "hard" if temptation >= TOP_K else "easy"
        task = conditions["tasks"][0]

        if eligible != 0:
            failures.append((spec["query_id"], eligible))
        print(f"{spec['query_id']:6s} {task:28s} {eligible:5d} {relaxed_numeric:8d} "
              f"{relaxed_unknown:10d} {temptation:5d} {difficulty:>7s}")

        records.append(
            {
                "query_id": spec["query_id"],
                "query_type": "abstention",
                "query": spec["query"],
                "difficulty": difficulty,
                "conditions": spec["conditions"],
                "conditions_fidelity": spec["fidelity"],
                "expected_behavior": "abstain",
                "relevance_rule": {
                    "must": "조건을 만족하는 모델이 코퍼스에 존재하지 않는다. 추천하지 않는 것이 정답이다.",
                    "grade_2": None,
                    "grade_1": None,
                },
                "expected_any": [],
                "acceptable": [],
                "must_exclude": [],
                "eligible_count": eligible,
                "temptation": {
                    "note": "조건을 만족하지 않으나 검색이 끌어올 수 있는 모델 수. 난이도의 근거.",
                    "relaxed_numeric": relaxed_numeric,
                    "relaxed_numeric_conditions": spec["relaxed"],
                    "allow_unverified": relaxed_unknown,
                    "pool_size": temptation,
                    "threshold": TOP_K,
                },
                "relevant_complete": True,
                "verification": {
                    "method": "hard_filter 전수 적용 — eligible == 0 실측",
                    "rule_scan_covered": eligible,
                    "flagged_for_human": [],
                },
                "corpus_snapshot": snapshot,
                "judged_by": None,
                "judged_on": None,
            }
        )

    print()
    kinds: Dict[str, int] = {}
    tasks: Dict[str, int] = {}
    for spec in SPECS:
        key = "core" if spec["conditions"].get("pools") == ["core"] else (
            "context" if "min_context_length" in spec["conditions"] else "parameters"
        )
        kinds[key] = kinds.get(key, 0) + 1
        tasks[spec["conditions"]["tasks"][0]] = tasks.get(spec["conditions"]["tasks"][0], 0) + 1
    print(f"조건 종류 분포  {kinds}")
    print(f"task 분포      {len(tasks)}개 task, 최대 {max(tasks.values())}개/task")
    print(f"난이도         easy {sum(1 for r in records if r['difficulty'] == 'easy')} / "
          f"hard {sum(1 for r in records if r['difficulty'] == 'hard')}")

    if failures:
        print(f"\n❌ eligible != 0 인 질의 {len(failures)}개: {failures}")
        raise SystemExit(1)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"\n✅ 10개 전부 eligible == 0 확인")
    print(f"→ {OUT}")


if __name__ == "__main__":
    main()
