"""Deterministic project checks used by the recommendation graph (17) and the API (21).

  gpu_fit         will a model run on the user's GPU at fp16 / int8 / int4?
  license_verdict can the recommended stack (models + training data + service data) ship commercially?
  implementation_guide  what should the user check about output format or fine-tuning?
  compare_models  side-by-side table of 2-3 candidate models

No LLM here: these answers must be exact and repeatable, so the writer only reports them.
"""

from __future__ import annotations

import re
from typing import Any

from taxonomy import normalize

# Runtime memory beyond the weights: activations, KV cache for short prompts, allocator slack.
# ponytail: one factor for every architecture; long-context LLM serving needs a KV-cache term
# (layers x heads x context) once the corpus records those dimensions.
RUNTIME_OVERHEAD = 1.2
CUDA_CONTEXT_GIB = 0.6
GIB_PER_BILLION_PARAMS = {"fp16": 2e9 / 1024**3, "int8": 1e9 / 1024**3, "int4": 0.5e9 / 1024**3}
PRECISION_LABEL = {"fp16": "fp16", "int8": "8bit 양자화", "int4": "4bit 양자화"}
FIT_LABEL = {"runs": "돌아감", "runs_quantized": "양자화하면 돌아감", "too_large": "불가", "unknown": "판단 불가"}
# What a gpu_fit number is. It is never a measured VRAM figure, and it is not the artifact file size
# (filter_metadata.artifact_runnable_gib), which is a download size and is reported separately.
GPU_FIT_BASIS = "weights_estimate"
GPU_FIT_NOTE = "가중치 기반 추정치이며 긴 입력의 KV cache는 포함하지 않아요."

# Model rows carry Stage 2's contract verdict (resolvers/legal.py); datasets only have raw license
# strings. Both end in the same four classes so one stack verdict can combine them.
COMMERCIAL_STATUS_CLASS = {
    "permitted": "commercial",
    "prohibited": "non_commercial",
    "review_required": "conditional",
    "unknown": "unknown",
}


STRUCTURED_OUTPUT = re.compile(
    r"구조화\s*(?:된\s*)?출력|structured\s+outputs?|json\s*(?:스키마|schema)|"
    r"(?:api|함수|도구)\s*(?:호출\s*)?(?:인자|인수|파라미터)|"
    r"json\s*(?:으로|로|을|를)?\s*(?:출력|반환|생성|변환|보내|넘기|전달|만들)|"
    r"(?:출력|반환|생성|추출).{0,12}json",
    re.IGNORECASE,
)
# "파인튜닝된 모델", "추가 학습된", "SFT된" name a model already trained, not a plan to train one.
ALREADY_DONE = r"(?!\s*(?:된|되어|돼|한))"
FINE_TUNING = (
    rf"파인\s*튜닝{ALREADY_DONE}|\bfine[-\s]*tun(?:e|ing)\b|(?<![a-z])sft(?![a-z]){ALREADY_DONE}|추가\s*학습{ALREADY_DONE}"
)
SKIP_FINE_TUNING = re.compile(
    rf"(?:{FINE_TUNING}|튜닝|학습)\s*(?:(?:은|는|을|를|도)\s*)?"
    r"(?:없이|제외|안\s*(?:하|할|해|함)|하지\s*않|필요\s*없|생각\s*없|계획\s*없)|"
    r"(?:without|no)\s+fine[-\s]*tun",
    re.IGNORECASE,
)
# "LFM3-1.7B-Base", "klue/roberta-base": a name ending in base. A mid-name size tag ("bert-base-nsmc") is
# usually a model already fine-tuned for another task.
BASE_CHECKPOINT = re.compile(r"(?<![a-z])base$", re.IGNORECASE)


def fine_tuning_declined(said: list[str]) -> bool:
    """said: the user's messages, oldest first. The newest one that talks about fine-tuning decides,
    so "파인튜닝은 안 해" and later "SFT도 해볼래" searches again."""
    for text in reversed(said):
        if SKIP_FINE_TUNING.search(text):
            return True
        if re.search(FINE_TUNING, text, re.IGNORECASE):
            return False
    return False


# Checkpoints made for another job than a starting point: an ELECTRA generator, sparse or dense retrieval encoders,
# rerankers. The SFT search for a label task looks under feature-extraction, where these sit beside plain encoders.
# ponytail: name patterns only; an architecture field from the cards would catch the unnamed ones.
NOT_A_BASE = re.compile(r"generator|sparse|splade|colbert|embed|retriev|rerank|sbert|simcse|sentence-?transformer"
                        r"|(?<![a-z0-9])(?:e5|bge|gte)(?![a-z0-9])", re.IGNORECASE)


def sft_candidates(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Models to fine-tune from: full-precision weights, base checkpoints first, search order otherwise.
    Rows loaded before the contract reingest have no artifact_formats; unknown is kept, not rejected."""
    ready = [
        r for r in rows
        if not r.get("quant_bits") and (r.get("artifact_formats") is None or "safetensors" in r["artifact_formats"])
        and not NOT_A_BASE.search(r["model_id"])
    ]
    return sorted(ready, key=lambda r: not BASE_CHECKPOINT.search(r["model_id"]))


def implementation_guide(request: str, tasks: set[str]) -> dict[str, str]:
    """Advise on a task without claiming that a candidate supports it or needs training."""
    guide = {}
    if "tool_use" in tasks or STRUCTURED_OUTPUT.search(request):
        guide["structured_output"] = (
            "프로그램에 넘길 필드와 자료형을 JSON 스키마로 정하고, "
            "모델을 실행할 환경에서 그 형식으로 출력할 수 있는지 확인하세요."
        )
    has_repeated_errors = re.search(r"(?:계속|자꾸|반복해서)\s*(?:틀|오류|실패|잘못|혼동)", request)
    has_labelled_examples = re.search(r"정답\s*(?:예시|데이터|라벨)|라벨링", request)
    asks_about_training = re.search(FINE_TUNING, request, re.IGNORECASE)
    if (asks_about_training or (has_repeated_errors and has_labelled_examples)) and not SKIP_FINE_TUNING.search(request):
        guide["fine_tuning"] = (
            "기본 모델을 실제 예시로 먼저 평가하세요. 프롬프트를 보완해도 같은 내용 오류가 반복되고 "
            "원하는 답의 기준이 명확하다면, 정답 예시를 모아 SFT(지도 파인튜닝)를 검토하세요."
        )
    return guide


def runtime_gib(weights_gib: float) -> float:
    return round(weights_gib * RUNTIME_OVERHEAD + CUDA_CONTEXT_GIB, 2)


def max_params_for_gpu(gpu_gib: float) -> float:
    """Largest model (billions of parameters) that still fits at 4-bit."""
    return round((gpu_gib - CUDA_CONTEXT_GIB) / (RUNTIME_OVERHEAD * GIB_PER_BILLION_PARAMS["int4"]), 1)


def gpu_fit(
    params_b: float | None, gpu_gib: float | None, hardware: dict | None = None, quant_bits: int | None = None
) -> dict[str, Any] | None:
    """Verdict for one model. Weight sizes come from Stage 2's weights_only estimate when present.

    An already-quantized checkpoint (GGUF, AWQ ...) only exists at its own precision.
    """
    if gpu_gib is None:
        return None
    weights = (hardware or {}).get("weights_only") or {}
    fit = _gpu_fit(params_b, gpu_gib, weights, quant_bits)
    return {**fit, "basis": GPU_FIT_BASIS}


def _gpu_fit(params_b: float | None, gpu_gib: float, weights: dict, quant_bits: int | None) -> dict[str, Any]:
    if quant_bits:
        size = weights.get("detected_quantization_gib")
        if size is None and params_b:
            size = params_b * GIB_PER_BILLION_PARAMS["fp16"] * quant_bits / 16
        if size is None:
            return {"verdict": "unknown", "label": FIT_LABEL["unknown"], "precision": None, "needed_gib": None}
        need = runtime_gib(size)
        verdict = "runs" if need <= gpu_gib else "too_large"
        return {
            "verdict": verdict,
            "label": f"{FIT_LABEL[verdict]} (원본 {quant_bits}bit)",
            "precision": f"{quant_bits}bit",
            "needed_gib": need,
        }
    if not params_b and not weights.get("fp16_gib"):
        return {"verdict": "unknown", "label": FIT_LABEL["unknown"], "precision": None, "needed_gib": None}
    for precision in ("fp16", "int8", "int4"):
        size = weights.get(f"{precision}_gib")
        if size is None:
            if not params_b:  # weights estimate missing for this precision and no size to derive it
                return {"verdict": "unknown", "label": FIT_LABEL["unknown"], "precision": None, "needed_gib": None}
            size = params_b * GIB_PER_BILLION_PARAMS[precision]
        need = runtime_gib(size)
        if need <= gpu_gib:
            verdict = "runs" if precision == "fp16" else "runs_quantized"
            return {
                "verdict": verdict,
                "label": f"{FIT_LABEL[verdict]} ({PRECISION_LABEL[precision]})",
                "precision": precision,
                "needed_gib": need,
            }
    return {
        "verdict": "too_large",
        "label": f"{FIT_LABEL['too_large']} (4bit도 {need}GiB 필요)",
        "precision": None,
        "needed_gib": need,
    }


def license_class(licenses: Any) -> str:
    """Most restrictive class among a dataset's or model's licenses."""
    values = licenses if isinstance(licenses, list) else [licenses]
    classes = {normalize("commercial_use", value) or "unknown" for value in values if value} or {"unknown"}
    for cls in ("non_commercial", "conditional", "unknown", "commercial"):
        if cls in classes:
            return cls
    return "unknown"


def model_license_class(commercial_status: str | None, license_value: Any = None) -> str:
    """A model's class: its contract commercial_status when present, else the raw license (old rows)."""
    if commercial_status in COMMERCIAL_STATUS_CLASS:
        return COMMERCIAL_STATUS_CLASS[commercial_status]
    return license_class(license_value)


def license_verdict(items: list[dict[str, Any]]) -> dict[str, Any]:
    """items: [{"kind": "model"|"training data"|"service data", "id", "license", "commercial_status"?}].

    Any non-commercial piece blocks a commercial launch: a fine-tuned model inherits its training
    data's terms, and an app cannot serve NC data commercially. Conditional/unknown -> review.
    A model item may carry commercial_status; it wins over re-classifying the raw license.
    Datasets keep the raw-license path.
    """
    if not items:
        # Nothing was recommended, so nothing can be cleared for a commercial launch either.
        return {"verdict": "none", "label": "판정 대상 없음", "reason": "추천된 모델·데이터가 없음",
                "blockers": [], "review": []}
    blockers, review = [], []
    for item in items:
        cls = model_license_class(item.get("commercial_status"), item.get("license"))
        entry = {**item, "class": cls}
        if cls == "non_commercial":
            blockers.append(entry)
        elif cls in ("conditional", "unknown"):
            review.append(entry)
    if blockers:
        names = ", ".join(f"{b['kind']} {b['id']} ({b['license']})" for b in blockers[:4])
        return {
            "verdict": "blocked",
            "label": "상업 출시 불가",
            "reason": f"비상업 라이선스 포함: {names}",
            "blockers": blockers,
            "review": review,
        }
    if review:
        names = ", ".join(f"{r['kind']} {r['id']} ({r['license'] or 'unknown'})" for r in review[:4])
        return {
            "verdict": "review",
            "label": "조건부 (라이선스 원문 확인 필요)",
            "reason": f"확인 필요: {names}",
            "blockers": [],
            "review": review,
        }
    return {
        "verdict": "commercial_ok",
        "label": "상업 출시 가능",
        "reason": "모든 구성 요소가 상업 이용 허용",
        "blockers": [],
        "review": [],
    }


TRAINING_KIND = "학습 데이터"


def stack_verdict(items: list[dict[str, Any]], commercial_only: bool) -> dict[str, Any]:
    """items as for license_verdict. The service runs on the models and service data, so they decide;
    training data binds only if the user trains on it, so a non-commercial set is named to leave out
    instead of blocking the stack. With no service parts (a dataset-only answer) training data decides.
    commercial_only (the user mentioned a company, launch or sales) picks the question the headline answers.
    """
    core = [i for i in items if i["kind"] != TRAINING_KIND]
    training = [i for i in items if i["kind"] == TRAINING_KIND]
    verdict = license_verdict(core or training)
    optional = [{**item, "class": license_class(item["license"])} for item in training] if core else []
    verdict["training_non_commercial"] = [i for i in optional if i["class"] == "non_commercial"]
    verdict["training_review"] = [i for i in optional if i["class"] in ("conditional", "unknown")]
    verdict["use"] = "commercial" if commercial_only else "personal"
    return verdict


def _names(items: list[dict[str, Any]], limit: int = 4) -> str:
    def text(value):
        values = [v for v in (value if isinstance(value, list) else [value]) if v]
        return ", ".join(map(str, values)) or "라이선스 미확인"

    names = ", ".join(f"{i['id']} ({text(i['license'])})" for i in items[:limit])
    return names + (f" 외 {len(items) - limit}개" if len(items) > limit else "")


def license_section(verdict: dict[str, Any]) -> str:
    """The answer's closing license verdict, rendered from stack_verdict so it never depends on the writer."""
    if verdict.get("verdict", "none") == "none":
        return ""
    avoid, check = verdict.get("training_non_commercial", []), verdict.get("training_review", [])
    launch = verdict["label"]
    if verdict["verdict"] == "commercial_ok" and avoid:
        launch += " (아래 비상업 학습 데이터를 빼면)"
    if verdict.get("use") == "commercial":
        lines = [f"**라이선스 판정 (상업 출시 기준): {launch}**"]
    else:
        lines = [
            "**라이선스 판정 (개인·로컬 사용 기준)**",
            "- 개인·로컬 사용: " + ("원문 확인이 필요한 항목이 있어요" if verdict["review"] else "막는 라이선스 없음"),
            f"- 상업 출시할 경우: {launch}",
        ]
    if verdict["blockers"]:
        lines.append(f"- 비상업 라이선스: {_names(verdict['blockers'])}")
    if verdict["review"]:
        lines.append(f"- 라이선스 원문 확인 필요: {_names(verdict['review'])}")
    if avoid:
        lines.append(f"- 상업 출시 시 학습에서 뺄 데이터: {_names(avoid)}")
    if check:
        lines.append(f"- 학습에 쓰기 전 원문 확인: {_names(check)}")
    return "\n".join(lines)


def compact_benchmarks(benchmark_metadata: dict | None, limit: int = 3) -> list[dict[str, Any]]:
    rows = (benchmark_metadata or {}).get("results_preview") or []
    return [{k: row.get(k) for k in ("benchmark", "dataset", "metric", "score")} for row in rows[:limit]]


def compare_models(rows: list[dict[str, Any]], gpu_gib: float | None = None) -> list[dict[str, Any]]:
    """Side-by-side rows from 09.compare_models output (or search rows with filter_metadata)."""
    table = []
    for row in rows:
        meta = row.get("filter_metadata") or {}
        quant = meta.get("quantization") or {}
        table.append(
            {
                "model_id": row["model_id"],
                "task": (row.get("task") or {}).get("primary"),
                "parameters_b": meta.get("parameter_count_billion"),
                "context_length": meta.get("context_length"),
                "license": meta.get("license") or "unknown",
                "commercial_status": meta.get("commercial_status"),
                "license_class": model_license_class(meta.get("commercial_status"), meta.get("license")),
                "downloads": (row.get("popularity") or {}).get("downloads"),
                "quantization": f"{quant.get('bits')}bit {quant.get('method') or ''}".strip()
                if quant.get("enabled")
                else None,
                "gpu_fit": gpu_fit(
                    meta.get("parameter_count_billion"), gpu_gib, meta.get("hardware"), quant.get("bits")
                ),
                "benchmarks": compact_benchmarks(row.get("benchmark_metadata")),
                "url": row.get("model_url"),
            }
        )
    return table


if __name__ == "__main__":
    small = gpu_fit(0.57, 8.0)
    assert small and small["verdict"] == "runs" and small["precision"] == "fp16", small
    seven = gpu_fit(7.6, 8.0)
    assert seven and seven["verdict"] == "runs_quantized" and seven["precision"] == "int4", seven
    huge = gpu_fit(70.0, 8.0)
    assert huge and huge["verdict"] == "too_large", huge
    gguf = gpu_fit(7.6, 8.0, {"weights_only": {"detected_quantization_gib": 4.7}}, quant_bits=4)
    assert gguf and gguf["verdict"] == "runs" and gguf["precision"] == "4bit", gguf
    unknown = gpu_fit(None, 8.0)
    assert unknown and unknown["verdict"] == "unknown" and gpu_fit(7.0, None) is None
    partial = gpu_fit(None, 8.0, {"weights_only": {"fp16_gib": 20.0}})  # no int8/int4 estimate, no size
    assert partial and partial["verdict"] == "unknown", partial
    assert 12 < max_params_for_gpu(8.0) < 14
    ok = license_verdict(
        [
            {"kind": "model", "id": "m", "license": "apache-2.0"},
            {"kind": "training data", "id": "d", "license": ["cc-by-4.0"]},
        ]
    )
    assert ok["verdict"] == "commercial_ok", ok
    nc = license_verdict(
        [
            {"kind": "model", "id": "m", "license": "apache-2.0"},
            {"kind": "training data", "id": "klue", "license": ["cc-by-nc-4.0"]},
        ]
    )
    assert nc["verdict"] == "blocked" and "klue" in nc["reason"], nc
    assert license_verdict([{"kind": "model", "id": "m", "license": None}])["verdict"] == "review"
    assert license_verdict([])["verdict"] == "none"
    assert license_class(["mit", "cc-by-nc-4.0"]) == "non_commercial"
    # A model's contract status wins over its raw license; datasets keep the raw path.
    stack = [{"kind": "model", "id": "m", "license": "other", "commercial_status": "permitted"},
             {"kind": "training data", "id": "d", "license": ["cc-by-4.0"]}]
    assert license_verdict(stack)["verdict"] == "commercial_ok"
    assert license_verdict([{**stack[0], "commercial_status": "prohibited"}])["verdict"] == "blocked"
    assert small["basis"] == GPU_FIT_BASIS
    # An NC training set is named to leave out; it does not block a stack whose service parts are clear.
    core = [{"kind": "모델", "id": "m", "license": "apache-2.0"}]
    nc_train = [{"kind": "학습 데이터", "id": "nc", "license": ["cc-by-nc-sa-4.0"]}]
    personal = stack_verdict(core + nc_train, commercial_only=False)
    assert personal["verdict"] == "commercial_ok" and personal["training_non_commercial"][0]["id"] == "nc"
    text = license_section(personal)
    assert "개인·로컬 사용 기준" in text and "빼면" in text and "학습에서 뺄 데이터: nc (cc-by-nc-sa-4.0)" in text, text
    launch = license_section(stack_verdict(core, commercial_only=True))
    assert launch == "**라이선스 판정 (상업 출시 기준): 상업 출시 가능**", launch
    # With no service parts (a dataset-only answer), the training data is the stack itself.
    assert stack_verdict(nc_train, commercial_only=True)["verdict"] == "blocked"
    assert license_section(stack_verdict([], commercial_only=False)) == ""
    # Fine-tuning: the newest message that mentions it decides; a refusal stops the SFT search.
    for no in ("파인튜닝은 안 할 거야", "SFT 없이 쓸래", "학습은 필요 없어", "추가 학습 계획 없어", "no fine-tuning"):
        assert fine_tuning_declined([no]), no
    assert not fine_tuning_declined(["한국어 문서 분류 서비스", "SFT할 모델도 알려줘"])
    assert not fine_tuning_declined(["파인튜닝 안 해", "역시 SFT 해볼래"])
    assert fine_tuning_declined(["SFT할 거야", "파인튜닝은 안 하기로 했어", "상업용만"])
    assert not fine_tuning_declined(["학습 데이터도 추천해줘"])
    picks = sft_candidates([
        {"model_id": "a/LFM-Instruct", "quant_bits": None, "artifact_formats": ["safetensors"]},
        {"model_id": "a/LFM-GGUF", "quant_bits": 4, "artifact_formats": ["gguf"]},
        {"model_id": "a/onnx-only", "quant_bits": None, "artifact_formats": ["onnx"]},
        {"model_id": "a/LFM-Base", "quant_bits": None, "artifact_formats": None},
        {"model_id": "a/database-bert", "quant_bits": None, "artifact_formats": ["safetensors"]},
        {"model_id": "a/bert-base-nsmc", "quant_bits": None, "artifact_formats": ["safetensors"]},
        {"model_id": "kiwi-farm/kiwi-coco-lm-base-generator", "quant_bits": None, "artifact_formats": None},
        {"model_id": "nlpai-lab/KURE-Sparse-base", "quant_bits": None, "artifact_formats": None},
        {"model_id": "a/ko-sbert-base", "quant_bits": None, "artifact_formats": None},
        {"model_id": "a/multilingual-e5-small-distill-base-0.1", "quant_bits": None, "artifact_formats": None},
        {"model_id": "BAAI/bge-m3", "quant_bits": None, "artifact_formats": None},
    ])
    assert [p["model_id"] for p in picks] == ["a/LFM-Base", "a/LFM-Instruct", "a/database-bert", "a/bert-base-nsmc"]
    print("project_checks ok")
