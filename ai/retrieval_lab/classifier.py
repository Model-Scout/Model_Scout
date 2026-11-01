"""Query type classifier: rules first, LLM for the rest.

1. Rule: two or more model names found by name lookup plus a comparison cue
   ("비교", "vs", "중", "차이", ...) -> model_comparison. No LLM call.
2. Otherwise the LLM picks one type from the descriptions below. Few-shot
   examples are written for this prompt, not taken from the golden set, so the
   golden set stays a fair test.

LLM outputs are cached in one file, retrieval_lab/cache/classifier.json (key -> entry).

    python -m retrieval_lab.classifier --eval        # golden set accuracy, macro F1, confusion matrix
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import numpy as np

from retrieval_lab.pre_retrieval import ROOT, LLMUnavailable, llm_model

CACHE_PATH = Path(__file__).resolve().parent / "cache" / "classifier.json"
REPORT_DIR = Path(__file__).resolve().parent / "reports"
PROMPT_VERSION = 2
TYPES = (
    "model_comparison",
    "semantic_capability",
    "lexical_exact",
    "structured_constraint",
    "benchmark_lookup",
    "semantic_constraint",
)
COMPARE_CUE = re.compile(r"비교|vs\.?|VS|versus|차이|중\s*(뭐|어느|어떤|더)|어느\s*(쪽|게|것)|더\s*(나아|좋|낫)|나을까|나아\?")

PROMPT = """You classify Korean user requests to Model Scout, a search engine over Hugging Face models, into exactly one type.
Apply the rules in order and stop at the first that matches.

1. model_comparison: the user names two or more specific models and compares them.
2. benchmark_lookup: the user asks for benchmark, dataset or metric evidence (BLEU, chrF, COMET, CER, WER,
   KMMLU, MTEB, FLORES, KorQuAD, Common Voice...), even if they also say "compare".
3. lexical_exact: the request hinges on an exact string, whatever other conditions it has:
   - a translation direction or language pair (일본어→한국어, 영어를 한국어로, ko→fr),
   - a model family or base model name used as the anchor (Kanana 계열, KoELECTRA 기반, KoBART 기반, KLUE-RoBERTa 베이스),
   - a file, quantization or runtime format (GGUF, AWQ, GPTQ, MLX, ONNX, OpenVINO, CTranslate2/faster-whisper, transformers.js).
4. semantic_constraint (anchored): one named model is the reference point, e.g. "X를 내 GPU에서 돌릴 수 있어?",
   "X보다 가벼운", "X 대신".
5. Hard conditions = a number (parameter count, VRAM/RAM GB, context tokens) or a license requirement
   (상업 이용/상업 서비스/라이선스 명확). "GPU 없이", "CPU", "로컬", "맥", "온디바이스", "라이선스 상관없어" alone
   are NOT hard conditions.
   - Hard conditions + only a plain task (임베딩, 질의응답, 기계독해, 챗봇, 대화, 음성인식, 요약, 텍스트 분류, VLM)
     -> structured_constraint
   - Hard conditions + a specific domain, use or capability (회의록, RAG, 리랭커, OCR, 감성분석, 코딩, 잡음 음성,
     법률, 게임 로그...) -> semantic_constraint
6. Otherwise (capability or use case in natural language, no hard conditions) -> semantic_capability.

Examples:
- "Llama-3-8B와 Qwen2.5-7B 중 한국어 대화는 뭐가 나아?" -> model_comparison
- "KMMLU 점수가 공개된 한국어 LLM을 비교하고 싶어" -> benchmark_lookup
- "중국어를 한국어로 번역하는 모델을 노트북 GPU 6GB에서 돌리려고 해" -> lexical_exact
- "llama.cpp에서 쓸 GGUF 버전 한국어 LLM" -> lexical_exact
- "Qwen2.5-14B를 RTX 3070에서 돌릴 수 있어?" -> semantic_constraint
- "파라미터 3B 이하 한국어 챗봇, 상업 이용 가능해야 해" -> structured_constraint
- "콜센터 녹취 감정 분류 모델, 상업 서비스라 라이선스가 명확해야 해" -> semantic_constraint
- "GPU 없는 서버에서 돌릴 한국어 혐오 표현 필터" -> semantic_capability
- "아이들 동화책을 읽어줄 자연스러운 한국어 음성 합성 모델" -> semantic_capability

Reply with JSON only: {"type": "<one of the types>"}"""


@dataclass
class Classification:
    query_type: str
    source: str  # "rule" or "llm"
    latency_ms: float
    named_models: List[str]


def cache_key(text: str, model: str) -> str:
    return hashlib.sha256(f"classify|v{PROMPT_VERSION}|{model}|{text}".encode("utf-8")).hexdigest()[:20]


def load_cache(path: Optional[Path] = None) -> Dict[str, Dict[str, Any]]:
    path = path or CACHE_PATH
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save_cache(cache: Dict[str, Dict[str, Any]], path: Optional[Path] = None) -> None:
    path = path or CACHE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = dict(sorted(cache.items(), key=lambda item: item[1]["input"]))
    path.write_text(json.dumps(ordered, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _call_llm(text: str, model: str) -> Dict[str, Any]:
    try:
        from dotenv import load_dotenv

        load_dotenv(ROOT / ".env")
    except ImportError:
        pass
    if not os.getenv("OPENAI_API_KEY"):
        raise LLMUnavailable(f"분류 캐시 없음, OPENAI_API_KEY도 없음: {text[:40]}")
    from openai import OpenAI

    response = OpenAI().chat.completions.create(
        model=model,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": PROMPT}, {"role": "user", "content": text}],
    )
    return json.loads(response.choices[0].message.content or "{}")


def llm_type(text: str, model: Optional[str] = None) -> tuple[str, float]:
    model = model or llm_model()
    cache = load_cache()
    key = cache_key(text, model)
    if key in cache:
        return cache[key]["type"], float(cache[key]["latency_ms"])
    started = time.perf_counter()
    payload = _call_llm(text, model)
    latency_ms = (time.perf_counter() - started) * 1000.0
    query_type = payload.get("type") if payload.get("type") in TYPES else "semantic_capability"
    cache[key] = {"prompt_version": PROMPT_VERSION, "model": model, "input": text, "type": query_type,
                  "response": payload, "latency_ms": round(latency_ms, 1)}
    save_cache(cache)
    return query_type, latency_ms


def classify(text: str, retriever: Any, use_rule: bool = True, use_llm: bool = True) -> Classification:
    """retriever: a pipeline.Retriever (only its name index is used)."""
    started = time.perf_counter()
    named = retriever.name_lookup(text, np.arange(len(retriever.ids)))
    rule_ms = (time.perf_counter() - started) * 1000.0
    if use_rule and len(named) >= 2 and COMPARE_CUE.search(text):
        return Classification("model_comparison", "rule", rule_ms, named)
    if not use_llm:
        return Classification("semantic_capability", "default", rule_ms, named)
    query_type, llm_ms = llm_type(text)
    return Classification(query_type, "llm", rule_ms + llm_ms, named)


def scores(gold: Sequence[str], predicted: Sequence[str]) -> Dict[str, Any]:
    per_class = {}
    for label in TYPES:
        tp = sum(g == p == label for g, p in zip(gold, predicted))
        fp = sum(p == label != g for g, p in zip(gold, predicted))
        fn = sum(g == label != p for g, p in zip(gold, predicted))
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        per_class[label] = {"precision": precision, "recall": recall, "f1": f1, "support": tp + fn}
    labels = [label for label in TYPES if per_class[label]["support"]]
    return {
        "accuracy": sum(g == p for g, p in zip(gold, predicted)) / len(gold),
        "macro_f1": sum(per_class[label]["f1"] for label in labels) / len(labels),
        "per_class": per_class,
        "confusion": {g: dict(Counter(p for gg, p in zip(gold, predicted) if gg == g)) for g in labels},
    }


def render(results: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]], queries: int) -> str:
    short = {t: t.replace("_", " ") for t in TYPES}
    lines = ["# 쿼리 유형 분류 실험", "", f"- 골든셋 질의 {queries}개 (semantic_golden + semantic_judged, plan_query_type 라벨)",
             f"- LLM `{llm_model()}`, 프롬프트 v{PROMPT_VERSION}, few-shot 예시는 골든셋과 별도로 작성", "",
             "## 방식별 결과", "", "| 방식 | Accuracy | Macro F1 | LLM 호출 |", "|---|---:|---:|---:|"]
    for name, result in results.items():
        lines.append(f"| {name} | {result['accuracy']:.3f} | {result['macro_f1']:.3f} | {result['llm_calls']} |")
    best = results["규칙 + LLM"]
    lines += ["", "## 유형별 (규칙 + LLM)", "", "| 유형 | Precision | Recall | F1 | 질의 수 |", "|---|---:|---:|---:|---:|"]
    for label in TYPES:
        row = best["per_class"][label]
        lines.append(f"| {label} | {row['precision']:.3f} | {row['recall']:.3f} | {row['f1']:.3f} | {row['support']} |")
    labels = [label for label in TYPES if best["per_class"][label]["support"]]
    lines += ["", "## Confusion Matrix (행: 정답, 열: 예측)", "",
              "| 정답 \\ 예측 | " + " | ".join(short[label] for label in labels) + " |", "|---" * (len(labels) + 1) + "|"]
    for gold in labels:
        lines.append(f"| {short[gold]} | " + " | ".join(str(best["confusion"][gold].get(p, 0)) for p in labels) + " |")
    lines += ["", f"## 틀린 질의 ({len(errors)}개)", "", "| 질의 | 정답 | 예측 | 문장 |", "|---|---|---|---|"]
    for error in errors:
        lines.append(f"| {error['id']} | {error['gold']} | {error['predicted']} | {error['text'][:70].replace('|', '/')} |")
    return "\n".join(lines) + "\n"


def evaluate() -> None:
    from retrieval_lab import golden
    from retrieval_lab.pipeline import Retriever

    items = [item for path in golden.DEFAULT_QUERY_FILES for item in golden.read_jsonl(path) if item.get("plan_query_type") in TYPES]
    retriever = Retriever()
    gold = [item["plan_query_type"] for item in items]
    runs = {"규칙만 (나머지 semantic_capability)": dict(use_llm=False), "LLM만": dict(use_rule=False), "규칙 + LLM": {}}
    results: Dict[str, Dict[str, Any]] = {}
    predictions: Dict[str, List[Classification]] = {}
    for name, options in runs.items():
        predictions[name] = [classify(item["text"], retriever, **options) for item in items]
        result = scores(gold, [c.query_type for c in predictions[name]])
        result["llm_calls"] = sum(c.source == "llm" for c in predictions[name])
        results[name] = result
        print(f"{name:32} accuracy={result['accuracy']:.3f} macro_f1={result['macro_f1']:.3f} llm_calls={result['llm_calls']}")
    best = predictions["규칙 + LLM"]
    errors = [{"id": item["id"], "gold": g, "predicted": c.query_type, "text": item["text"]}
              for item, g, c in zip(items, gold, best) if g != c.query_type]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "query_classification.md").write_text(render(results, errors, len(items)), encoding="utf-8")
    (REPORT_DIR / "query_classification.json").write_text(json.dumps(
        {"results": results, "errors": errors}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--eval", action="store_true", help="골든셋으로 분류 정확도 측정")
    parser.add_argument("query", nargs="?", help="분류할 질의 하나")
    args = parser.parse_args()
    if args.eval:
        evaluate()
    elif args.query:
        from retrieval_lab.pipeline import Retriever

        result = classify(args.query, Retriever())
        print(json.dumps(result.__dict__, ensure_ascii=False))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
