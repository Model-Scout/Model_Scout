"""조각들을 계약 레코드 하나로 조립한다.

기존 파이프라인 단계가 이미 만든 사실(한국어 판정, 후보 등급, 의미 요약,
벤치마크)은 그대로 받아 쓴다. 이 모듈이 새로 하는 일은 **HF 응답에서 뽑은
사실을 합치고, 모든 계약 필드에 출처를 붙이고, 빠진 것을 unknown으로 남기는**
것이다.

    record = resolve.build(raw, stage2=row, stage3=semantic, run_id="...")

``contract/validate.py``가 결과를 검사한다. 조립이 잘못되면 거기서 걸린다 —
Stage 4 문서를 손으로 조립해 12개 키를 빼먹은 사고가 그렇게 났다.
"""

from __future__ import annotations

import datetime as dt
import re
from typing import Any, Callable, Dict, List, Optional

from . import artifacts as artifacts_resolver
from . import facts
from . import legal as legal_resolver
from . import technical as technical_resolver

SCHEMA_VERSION = 1

BYTES_PER_PARAM = {
    "float32": 4.0, "float64": 8.0,
    "float16": 2.0, "bfloat16": 2.0, "float8": 1.0,
    "int8": 1.0, "uint8": 1.0, "int4": 0.5,
}
GIB = 1024 ** 3

EMBEDDING_TASKS = {"sentence-similarity", "feature-extraction"}
TRANSLATION_TASKS = {"translation"}

# README가 지원을 명시했는지. 명시면 documented, 파일만 있으면 artifact_present다.
RUNTIME_MARKERS = {
    "llama_cpp": (r"llama\.cpp", r"\bollama\b", r"\bllama-cpp-python\b", r"\bgguf\b"),
    "vllm": (r"\bvllm\b",),
    "mps": (r"\bmps\b", r"apple silicon", r"\bmetal\b", r"\bm[1-4]\s*(pro|max|ultra)?\b"),
    "cpu": (r"\bcpu[- ]only\b", r"onnxruntime", r"\bopenvino\b"),
    "cuda": (r"\bcuda\b", r"device_map\s*=", r"\.to\(\s*[\"']cuda"),
    "onnx": (r"\bonnx\b", r"onnxruntime"),
}


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _documented(readme_text: str, target: str) -> bool:
    if not readme_text:
        return False
    lowered = readme_text.lower()
    return any(re.search(pattern, lowered) for pattern in RUNTIME_MARKERS.get(target, ()))


def _deployment(
    artifacts: Dict[str, Any],
    technical: Dict[str, Any],
    readme_text: str,
    retrieved_at: str,
) -> Dict[str, Any]:
    formats = artifacts.get("formats") or {}
    present = {name: (spec or {}).get("present") for name, spec in formats.items()}
    any_weights = any(present.get(name) for name in ("safetensors", "pytorch_bin", "gguf", "onnx", "mlx", "ct2"))

    conditions = {
        "cpu": "RAM, 모델 크기, 성능은 런타임과 작업에 따라 달라집니다.",
        "cuda": "GPU VRAM, 드라이버, CUDA, 아키텍처, 양자화가 호환되어야 합니다.",
        "mps": "Apple Silicon과 선택한 프레임워크가 해당 아키텍처를 지원해야 합니다.",
        "vllm": "vLLM 버전, 모델 아키텍처, GPU, 양자화 지원이 필요합니다.",
        "llama_cpp": "GGUF 아키텍처 지원과 llama.cpp 빌드가 호환되어야 합니다.",
        "onnx": "ONNX 그래프와 선택한 실행 공급자가 지원되어야 합니다.",
    }
    artifact_for = {"llama_cpp": "gguf", "onnx": "onnx", "mps": "mlx"}

    targets: Dict[str, Any] = {}
    for name in ("cpu", "cuda", "mps", "vllm", "llama_cpp", "onnx"):
        evidence: List[str] = []
        status = "unknown"
        artifact = artifact_for.get(name)
        if artifact and present.get(artifact):
            status = "artifact_present"
            evidence.append(f"artifact:{artifact}")
        if _documented(readme_text, name):
            status = "documented"
            evidence.append("readme:runtime_marker")
        if status == "unknown" and name in ("cpu", "cuda") and any_weights:
            status = "inferred"
            evidence.append("artifact:model_weights")
        targets[name] = {
            "status": status,
            "confidence": {"documented": "medium", "artifact_present": "medium",
                           "tested": "high", "inferred": "low", "unknown": "none"}[status],
            "evidence": evidence,
            "conditions": conditions[name],
        }

    # VRAM 추정 — 측정값(파일 크기)이 있으면 그쪽이 우선이다.
    smallest = artifacts_resolver.smallest_runnable_bytes(artifacts)
    weights = {"fp16_gib": None, "int8_gib": None, "int4_gib": None, "detected_quantization_gib": None}
    artifact = None
    basis = None
    caveat = None
    source: List[str] = []
    if smallest:
        label, size = smallest
        gib = round(size / GIB, 2)
        artifact = {"label": label, "gib": gib}
        # detected_quantization_gib 는 "양자화된 크기"다. 양자화가 아닌
        # safetensors 크기를 여기 넣으면 그 모델이 양자화본으로 읽힌다.
        if artifacts_resolver.quant_label(f"x-{label}.gguf"):
            weights["detected_quantization_gib"] = gib
        basis = "artifact_bytes"
        kind = "양자화" if weights["detected_quantization_gib"] is not None else "가중치"
        caveat = (
            f"{label} {kind} 파일 크기({gib:.2f}GiB)를 측정한 값입니다. "
            "컨텍스트 길이에 따라 KV 캐시가 추가로 필요합니다."
        )
        source = ["hf_api:siblings[].size"]
    total = technical.get("parameter_count_total")
    if isinstance(total, int):
        weights["fp16_gib"] = round(total * 2.0 / GIB, 2)
        weights["int8_gib"] = round(total * 1.0 / GIB, 2)
        weights["int4_gib"] = round(total * 0.5 / GIB, 2)
        if basis is None:
            basis = "parameter_count"
            caveat = (
                "가중치만 기준 추정입니다. 실제 VRAM/RAM은 KV 캐시, 활성화, "
                "프레임워크에 따라 더 필요합니다."
            )
            source = ["hf_api:safetensors.total"]

    if basis == "artifact_bytes":
        entry = facts.fact("verified", source, "파라미터 추정이 아니라 파일 크기 측정값이다", retrieved_at)
    elif basis == "parameter_count":
        entry = facts.fact("inferred", source, "parameter_count × dtype 바이트로 계산", retrieved_at)
    else:
        entry = facts.unknown("파일 크기도 파라미터 수도 모른다")

    return {
        "deployment": {
            "targets": targets,
            "vram_estimate": {"weights_only": weights, "artifact": artifact,
                              "basis": basis, "caveat": caveat},
        },
        "provenance": {"deployment.vram_estimate": entry},
    }


def _capability(
    raw: Dict[str, Any],
    stage2: Optional[Dict[str, Any]],
    technical: Dict[str, Any],
    retrieved_at: str,
) -> Dict[str, Any]:
    """과제·언어. 한국어 판정과 번역 방향은 기존 Stage 2 결과를 신뢰한다 —
    README 분석과 언어 게이트가 이미 거기에 있다. 다시 구현하면 두 벌이 된다."""
    card = raw.get("cardData") or raw.get("card_data") or {}
    stage2 = stage2 or {}
    language = stage2.get("language") or {}
    task = stage2.get("task") or {}

    primary = task.get("primary") or raw.get("pipeline_tag")
    matched = list(task.get("matched") or ([primary] if primary else []))
    languages = list(language.get("declared_languages") or legal_resolver.taxonomy and [])
    if not languages:
        declared = card.get("language")
        languages = [declared] if isinstance(declared, str) else list(declared or [])

    korean = (language.get("korean") or {}).get("verified")
    multilingual = (language.get("multilingual") or {}).get("verified")
    pairs = list((stage2.get("search_metadata") or {}).get("translation_pairs") or [])

    config = dict(raw.get("config") or {})
    dimensions = config.get("hidden_size") if primary in EMBEDDING_TASKS else None

    provenance = {
        "capability.primary_task": (
            facts.fact("verified", ["hf_api:pipeline_tag"], None, retrieved_at) if primary
            else facts.unknown("pipeline_tag가 없다")),
        "capability.languages": (
            facts.fact("documented", ["model_card:cardData.language"], None, retrieved_at)
            if languages else facts.unknown("cardData.language가 없다")),
        "capability.korean_verified": (
            facts.fact("documented", ["model_card:cardData.language"], None, retrieved_at)
            if korean is not None else facts.unknown("한국어 판정 결과가 없다")),
        "capability.translation_pairs": (
            facts.fact("documented", ["model_card:cardData.tags"], None, retrieved_at) if pairs
            else facts.not_applicable(
                "번역 과제가 아니다" if primary not in TRANSLATION_TASKS
                else "번역 모델인데 방향을 알 수 없다")),
        "capability.embedding_dimensions": (
            facts.fact("verified", ["hf_api:config.hidden_size"], None, retrieved_at)
            if dimensions else facts.not_applicable(
                "임베딩 과제가 아니다" if primary not in EMBEDDING_TASKS
                else "config.hidden_size가 없다")),
    }
    modality = ["text"]
    for marker, name in (("image", "image"), ("audio", "audio"), ("video", "video")):
        if marker in str(primary or "") or marker in " ".join(raw.get("tags") or []):
            modality.append(name)

    return {
        "capability": {
            "primary_task": primary,
            "matched_tasks": matched,
            "languages": languages,
            "korean_verified": korean,
            "multilingual_verified": multilingual,
            "translation_pairs": pairs,
            "modality": sorted(set(modality)),
            "embedding_dimensions": dimensions,
            "reranker": bool(re.search(r"rerank", " ".join(raw.get("tags") or []), re.IGNORECASE)) or None,
        },
        "provenance": provenance,
    }


def build(
    raw: Dict[str, Any],
    *,
    config_json: Optional[Dict[str, Any]] = None,
    stage1: Optional[Dict[str, Any]] = None,
    stage2: Optional[Dict[str, Any]] = None,
    stage3: Optional[Dict[str, Any]] = None,
    benchmark: Optional[Dict[str, Any]] = None,
    readme_text: str = "",
    base_status_of: Optional[Callable[[str], Optional[str]]] = None,
    run_id: str = "unset",
    retrieved_at: Optional[str] = None,
    source_pool: str = "core",
) -> Dict[str, Any]:
    """계약 레코드 하나를 만든다. 없는 사실은 키를 빼지 않고 unknown으로 남긴다."""
    retrieved_at = retrieved_at or _now()
    model_id = raw.get("id") or raw.get("modelId") or (stage2 or {}).get("model_id") or ""
    stage1 = stage1 or {}
    stage2 = stage2 or {}

    tech = technical_resolver.resolve(raw, config_json, retrieved_at=retrieved_at)
    arts = artifacts_resolver.resolve(raw, retrieved_at=retrieved_at)
    lic = legal_resolver.resolve(
        raw, model_id=model_id, base_status_of=base_status_of, retrieved_at=retrieved_at
    )
    cap = _capability(raw, stage2, tech["technical"], retrieved_at)
    dep = _deployment(arts["artifacts"], tech["technical"], readme_text, retrieved_at)

    gated = raw.get("gated")
    sha = raw.get("sha")
    last_modified = raw.get("lastModified") or raw.get("last_modified")
    if hasattr(last_modified, "isoformat"):
        last_modified = last_modified.isoformat()

    identity_provenance = {
        "identity.revision": (
            facts.fact("verified", ["hf_api:sha"], None, retrieved_at) if sha
            else facts.unknown("응답에 sha가 없다")),
        "identity.last_modified": (
            facts.fact("verified", ["hf_api:lastModified"], None, retrieved_at) if last_modified
            else facts.unknown("응답에 lastModified가 없다")),
        # gated를 못 받았을 때 false로 추정하지 않는다. "공개"와 "모름"은 다르다 —
        # 모름을 공개로 적으면 접근 승인이 필요한 모델을 바로 쓸 수 있다고 말하게 된다.
        "identity.gated": (
            facts.fact("verified", ["hf_api:gated"], None, retrieved_at) if gated is not None
            else facts.unknown("응답에 gated가 없다. '공개'를 뜻하지 않는다")),
    }

    popularity = stage2.get("popularity") or {}
    current = popularity.get("current") or {}
    candidate = stage2.get("candidate") or stage1.get("candidate") or {}
    family = stage2.get("family") or {}

    results = list((benchmark or {}).get("results") or [])
    quality_provenance = {
        "quality.results": (
            facts.fact("documented", ["readme:benchmark_table"], None, retrieved_at) if results
            else facts.unknown("model-index와 README 표에 숫자 결과가 없다"))
    }

    semantic = stage3 or {}
    record: Dict[str, Any] = {
        "model_id": model_id,
        "identity": {
            "model_id": model_id,
            "author": raw.get("author") or (model_id.split("/")[0] if "/" in model_id else None),
            "repo_url": f"https://huggingface.co/{model_id}" if model_id else None,
            "revision": sha,
            "last_modified": last_modified,
            "gated": gated,
            "private": raw.get("private"),
        },
        "discovery": {
            "candidate_tier": candidate.get("tier"),
            "candidate_type": candidate.get("type"),
            "korean_evidence": list(((stage2.get("language") or {}).get("korean") or {}).get("evidence") or []),
            "downloads": current.get("downloads") if isinstance(current.get("downloads"), int) else raw.get("downloads"),
            "likes": current.get("likes") if isinstance(current.get("likes"), int) else raw.get("likes"),
            "popularity_tier": (popularity.get("stage1") or {}).get("tier"),
            "canonical_model_id": family.get("canonical_model_id") or model_id,
            "is_variant": bool(family.get("is_variant")),
            "variant_types": list(family.get("variant_types") or []),
            "source_pool": source_pool,
        },
        "capability": cap["capability"],
        "technical": tech["technical"],
        "artifacts": arts["artifacts"],
        "deployment": dep["deployment"],
        "legal": lic["legal"],
        "quality": {"results": results, "summary": (benchmark or {}).get("summary") or {}},
        "semantic": {
            "summary": semantic.get("summary"),
            "strengths": list(semantic.get("strengths") or []),
            "limitations": list(semantic.get("limitations") or []),
            "use_cases": list(semantic.get("use_cases") or []),
            "atomic_evidence": list(semantic.get("atomic_evidence") or []),
            "status": semantic.get("status") or ("completed" if semantic else "skipped"),
        },
    }

    fields: Dict[str, Any] = {}
    for part in (identity_provenance, cap["provenance"], tech["provenance"],
                 arts["provenance"], dep["provenance"], lic["provenance"], quality_provenance):
        fields.update(part)

    record["provenance"] = {
        "schema_version": SCHEMA_VERSION,
        "pipeline_run_id": run_id,
        "retrieved_at": retrieved_at,
        "fields": fields,
        "conflicts": list(tech["conflicts"]),
        "review_queue": list(lic["review_queue"]) + [
            {"field": item["field"],
             "reason": "출처가 서로 다른 값을 말한다. 사람이 판정해야 한다.",
             "hint": None}
            for item in tech["conflicts"]
        ],
    }
    return record
