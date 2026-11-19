#!/usr/bin/env python3
"""분해가 뽑은 task 를 질문의 하드 필터 조건으로 넣는다.

운영은 decompose 가 준 need['task'] 를 hf_tags() 로 HF 태그에 매핑해
search_models(task_filters=...) 로 넘긴다(17_recommend_graph.py:565,593).
평가도 같은 태그를 써야 운영과 같은 후보 집합을 본다.

질문이 직접 task 를 말한 경우(전문가형)에는 그 값을 우선한다. 초보 질문은
task 를 말하지 않으므로 분해 결과가 유일한 근거다.

    python test/model_retrieval/tools/apply_decomposed_task.py queries/spec_capability.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
CACHE = AI / "test" / "model_retrieval" / "queries" / "decompose_cache.json"

# 17_recommend_graph 의 MODEL_HF_TASKS / MODEL_TASK_FALLBACK 와 같아야 한다.
HF_TASKS = ("text-generation", "image-text-to-text", "sentence-similarity", "translation",
            "automatic-speech-recognition", "feature-extraction", "text-classification",
            "question-answering", "summarization")
FALLBACK = {"retrieval": "embedding", "tool_use": "generation", "information_extraction": "generation",
            "table_qa": "generation", "ocr": "visual_qa", "chart_understanding": "visual_qa"}
# 분류체계 task -> HF 태그. normalize("task", tag) 가 하던 일을 표로 적는다.
TAXONOMY_TO_HF = {
    "generation": ["text-generation"],
    "visual_qa": ["image-text-to-text"],
    "embedding": ["sentence-similarity", "feature-extraction"],
    "translation": ["translation"],
    "speech_recognition": ["automatic-speech-recognition"],
    "classification": ["text-classification"],
    "question_answering": ["question-answering"],
    "summarization": ["summarization"],
}


def hf_tags(task_key: str) -> List[str]:
    return TAXONOMY_TO_HF.get(FALLBACK.get(task_key, task_key), [])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("specs", nargs="+", type=Path)
    ap.add_argument("--all-needs", action="store_true",
                    help="needs 전부의 태그를 합친다(기본: 첫 need 만 — 프롬프트가 most important first 라고 한다)")
    args = ap.parse_args()

    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    for path in args.specs:
        full = path if path.is_absolute() else AI / "test" / "model_retrieval" / path
        spec = importlib.util.spec_from_file_location(full.stem, full)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(f"\n{full.name}")
        print(f"{'id':6s} {'분해 task':34s} {'→ HF 태그':44s} 질문이 직접 말한 것")
        for item in mod.QUERIES:
            entry = cache.get(item["text"])
            if not entry:
                print(f"{item['qid']:6s} ❌ 분해 캐시 없음")
                continue
            needs = entry["needs"] if args.all_needs else entry["needs"][:1]
            keys = [n["task"] for n in needs]
            tags: List[str] = []
            for key in keys:
                for tag in hf_tags(key):
                    if tag not in tags:
                        tags.append(tag)
            said = (item.get("conditions") or {}).get("tasks")
            print(f"{item['qid']:6s} {str(keys):34s} {str(tags):44s} {said or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
