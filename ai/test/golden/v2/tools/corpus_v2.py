"""골든셋 v2의 판정 기준 코퍼스 로더.

``retrieval_lab.corpus``는 ``ai/data/hf_models_stage4_*.jsonl``(3,853행)을 읽는다.
그 파일은 Actions가 커밋하지 않아 Supabase(3,872행)보다 19행 뒤처져 있다.
골든셋 판정은 확정 집합인 Supabase 스냅샷을 기준으로 해야 하므로 이 모듈을 쓴다.

하드 필터는 ``05_validate_retrieval.hard_filter``를 그대로 재사용한다. 수치 조건의
누락 값 처리까지 운영 Supabase SQL과 같아야 판정 기준이 실제 검색의 후보 결정
로직과 달라지지 않는다.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

AI_ROOT = Path(__file__).resolve().parents[4]
SNAPSHOT = Path(__file__).resolve().parents[1] / "corpus_snapshot.jsonl"


@lru_cache(maxsize=1)
def validator() -> Any:
    """05_validate_retrieval.py를 import해 하드 필터를 운영과 동일하게 쓴다."""
    if str(AI_ROOT) not in sys.path:
        sys.path.insert(0, str(AI_ROOT))
    spec = importlib.util.spec_from_file_location(
        "golden_v2_validator", AI_ROOT / "05_validate_retrieval.py"
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("05_validate_retrieval.py를 불러올 수 없습니다")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def load_rows() -> List[Dict[str, Any]]:
    if not SNAPSHOT.exists():
        raise FileNotFoundError(
            f"{SNAPSHOT} 없음. `python test/golden/v2/tools/dump_corpus.py`를 먼저 실행하세요."
        )
    rows: List[Dict[str, Any]] = []
    with SNAPSHOT.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def hard_filter(row: Dict[str, Any], query: Dict[str, Any]) -> bool:
    return validator().hard_filter(row, query)[0]


def eligible(query: Dict[str, Any]) -> List[Dict[str, Any]]:
    """질의 조건을 통과한 후보 전체. 정답은 반드시 이 안에 있다."""
    query = dict(query)
    query.setdefault("pools", ["core", "low_popularity"])
    return [row for row in load_rows() if hard_filter(row, query)]


def count(**query: Any) -> int:
    return len(eligible(query))
