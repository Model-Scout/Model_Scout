"""QA 2026-11-26 regression: the four questions run through the real graph, each expected result checked.

    python test/qa_regression.py            # all four (OpenAI + Supabase read, about 1-3 minutes)
    python test/qa_regression.py TC2        # one case
    python test/qa_regression.py --out run.json

The question text is what the web app sends: the idea plus the "조건:" line its pickers add (Home.tsx).
Each check is one expected result from the QA request, read off the final state; a case passes when all
of its checks pass. Exit 1 when any check fails. Not a pytest test: it calls paid APIs and its answers
come from LLM calls, so run it by hand before a release and compare with the last run.

As of 2026-11-26 most checks still fail: they record what the QA found and is not fixed yet (language
match, the router sending model-only turns, binary vs multi-class labels). Passing on that day: the CPU-only
size filter and the SFT start filter.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
import time
from pathlib import Path

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
os.environ.setdefault("MODEL_SCOUT_CORPUS", "v2")

import project_checks  # noqa: E402

KO = re.compile(r"(?<![a-z])(ko|kor|korean|klue|kobart|kobert|koelectra|hangul)(?![a-z])|[가-힣]", re.I)
# Binary sentiment checkpoints in the v2 corpus: NSMC (positive/negative movie reviews) or a stated
# positive/negative head. Multi-emotion models (hun3359/klue-bert-base-sentiment) are not on it.
BINARY_SENTIMENT = re.compile(r"nsmc|generalized-sentiment", re.I)
HATE_DATA = {"jeanlee/kmhas_korean_hate_speech", "moon1ite/kor_hate", "jason9693/apeach", "nayohan/apeach",
             "nayohan/korean-hate-speech"}


def models(state, kind=None):
    return [m for g in state.get("models") or [] if g.get("kind") == kind for m in g.get("models") or []]


def group(state, task):
    return next((g.get("models") or [] for g in state.get("models") or [] if g.get("kind") is None
                 and (g.get("need") or {}).get("task") == task), [])


def datasets(state):
    d = state.get("datasets") or {}
    return [r["dataset"] for r in (d.get("project_training") or []) + (d.get("service_data") or [])]


def sft_clean(state):
    bad = [m["model_id"] for m in models(state, "sft") if project_checks.NOT_A_BASE.search(m["model_id"])]
    return not bad, bad or "SFT 후보에 출발점이 아닌 모델 없음"


def has_data(state):
    found = datasets(state)
    return bool(found), found or "추천 데이터 0개"


CASES = {
    "TC1": {
        "query": "쇼핑몰 상품 리뷰를 긍정/부정으로 분류하는 감성분석 서비스\n조건: 언어 한국어, 실행 환경 로컬 GPU 8GB, 상업적 이용 가능.",
        "checks": {
            "1순위가 긍정/부정 이진 분류 모델": lambda s: (
                bool(group(s, "classification")) and bool(BINARY_SENTIMENT.search(group(s, "classification")[0]["model_id"])),
                [m["model_id"] for m in group(s, "classification")[:1]]),
            "한국어 감성 데이터셋(NSMC 등) 1개 이상": lambda s: (
                any(re.search(r"nsmc|sentiment|감성|review", d, re.I) for d in datasets(s)), datasets(s)),
            "SFT 후보는 출발점 모델만": sft_clean,
        },
    },
    "TC2": {
        "query": "영어 뉴스 기사를 3줄로 요약해주는 서비스\n조건: 언어 영어, 실행 환경 CPU만.",
        "checks": {
            "CPU만이면 1B 넘는 모델 없음": lambda s: (
                all((m.get("parameters_b") or 0) <= 1.0 for g in s.get("models") or [] for m in g.get("models") or []),
                [(m["model_id"], m.get("parameters_b")) for g in s.get("models") or [] for m in g.get("models") or []]),
            "요약 후보 중 영어를 지원하지 않는다고 표시된 모델 없음": lambda s: (
                all(not m.get("languages") or "en" in m["languages"] for m in group(s, "summarization")),
                [(m["model_id"], m.get("languages")) for m in group(s, "summarization")]),
            # Fails while the corpus has no English summarizer of 1B or less (BART-CNN and the like are not collected).
            "CPU에서 쓸 영어 요약 후보 1개 이상": lambda s: (
                bool(group(s, "summarization")), [m["model_id"] for m in group(s, "summarization")]),
            "요약 데이터셋 1개 이상": has_data,
        },
    },
    "TC3": {
        "query": "콜센터 상담 녹음을 텍스트로 바꾸고 핵심 내용을 요약하는 서비스\n조건: 언어 한국어, 실행 환경 로컬 GPU 16GB, 상업적 이용 가능.",
        "checks": {
            "한국어 ASR이 1순위": lambda s: (
                bool(group(s, "speech_recognition")) and bool(KO.search(group(s, "speech_recognition")[0]["model_id"])),
                [m["model_id"] for m in group(s, "speech_recognition")[:1]]),
            "요약 1순위가 한국어 전용 요약 모델 (다국어 범용이 아님)": lambda s: (
                bool(group(s, "summarization")) and group(s, "summarization")[0].get("languages") == ["ko"],
                [(m["model_id"], m.get("languages")) for m in group(s, "summarization")[:1]]),
            "같은 모델이 두 번 나오지 않음": lambda s: (
                len(ids := [m["model_id"] for g in s.get("models") or [] if g.get("kind") is None for m in g["models"]])
                == len(set(ids)), ids),
            "상담 음성 데이터 1개 이상": has_data,
        },
    },
    "TC4": {
        "query": "커뮤니티 댓글에서 혐오표현을 탐지하는 모델을 학습하고 싶어. 학습 데이터도 추천해줘\n조건: 언어 한국어.",
        "checks": {
            "혐오표현 전용 데이터가 1순위": lambda s: (
                bool(datasets(s)) and datasets(s)[0] in HATE_DATA, datasets(s)[:3]),
            "SFT 후보는 출발점 모델만": sft_clean,
        },
    },
}


def load_graph():
    from dotenv import load_dotenv

    load_dotenv(AI / ".env")
    spec = importlib.util.spec_from_file_location("recommend_graph_qa", AI / "17_recommend_graph.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("cases", nargs="*", help=f"any of {', '.join(CASES)} (default: all)")
    parser.add_argument("--out", type=Path, help="write every check with what it saw (json)")
    args = parser.parse_args()
    if unknown := set(args.cases) - set(CASES):
        parser.error(f"unknown case: {', '.join(sorted(unknown))}")
    graph = load_graph()
    from langgraph.checkpoint.memory import InMemorySaver

    report, failed = {}, 0
    for name in args.cases or CASES:
        started = time.time()
        state = graph.run(CASES[name]["query"], None, InMemorySaver())
        rows = {}
        for label, check in CASES[name]["checks"].items():
            ok, seen = check(state)
            rows[label] = {"ok": bool(ok), "seen": seen}
            failed += not ok
            print(f"{name} {'PASS' if ok else 'FAIL'}  {label}  | {json.dumps(seen, ensure_ascii=False)[:160]}")
        report[name] = {"seconds": round(time.time() - started, 1), "checks": rows}
    total = sum(len(r["checks"]) for r in report.values())
    print(f"\n{total - failed}/{total} checks pass")
    if args.out:
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
