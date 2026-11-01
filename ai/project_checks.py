"""Deterministic project checks used by the recommendation graph (17) and the API (21).

  gpu_fit         will a model run on the user's GPU at fp16 / int8 / int4?
  license_verdict can the recommended stack (models + training data + service data) ship commercially?
  compare_models  side-by-side table of 2-3 candidate models

No LLM here: these answers must be exact and repeatable, so the writer only reports them.
"""

from __future__ import annotations

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


def license_verdict(items: list[dict[str, Any]]) -> dict[str, Any]:
    """items: [{"kind": "model"|"training data"|"service data", "id", "license"}] -> stack verdict.

    Any non-commercial piece blocks a commercial launch: a fine-tuned model inherits its training
    data's terms, and an app cannot serve NC data commercially. Conditional/unknown -> review.
    """
    blockers, review = [], []
    for item in items:
        cls = license_class(item.get("license"))
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
                "license_class": license_class(meta.get("license")),
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
    assert license_class(["mit", "cc-by-nc-4.0"]) == "non_commercial"
    print("project_checks ok")
