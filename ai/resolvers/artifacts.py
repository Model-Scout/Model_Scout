"""siblings 파일 목록에서 포맷·실제 용량·양자화 레이블을 뽑는다.

기존 ``02_enrich_metadata.extract_artifacts()``는 ``rfilename``만 읽고
``size``를 버렸다. ``load_model_info``가 ``files_metadata=True``로 호출하므로
크기는 이미 응답에 있다. 받아 놓고 안 쓴 것이다.

용량이 왜 중요한가
------------------
"내 GPU에 들어가나"는 파라미터 수에서 추정하는 것보다 실제 파일 크기로
답하는 편이 정확하다. 특히 GGUF는 한 레포에 Q2_K~Q8_0이 여러 벌 들어 있어
"이 모델 몇 GB냐"의 답이 파일마다 다르다.

    GRaPE-2.5-Helios-GGUF
      GRaPE-2.5-Helios.Q2_K_M.gguf    3.4 GB
      GRaPE-2.5-Helios.Q4_K_M.gguf    5.8 GB
      GRaPE-2.5-Helios.Q8_0.gguf      9.8 GB
      mmproj-BF16.gguf                0.7 GB   ← 비전 인코더 사이드카

레포 전체 크기를 합치면 19.7 GB가 되지만 돌리는 데 필요한 건 한 벌이다.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from . import facts

FORMAT_SUFFIX = {
    "safetensors": (".safetensors",),
    "gguf": (".gguf",),
    "onnx": (".onnx", ".onnx_data"),
    "pytorch_bin": (".bin", ".pt", ".pth"),
    "ct2": (".bin",),          # CTranslate2는 model.bin + config. 아래에서 경로로 가린다
    "mlx": (".safetensors",),  # MLX도 safetensors. 아래에서 경로로 가린다
}
FORMATS: Tuple[str, ...] = ("safetensors", "gguf", "onnx", "pytorch_bin", "ct2", "mlx")

# GGUF 양자화 레이블을 열거하지 않는다. llama.cpp와 배포자가 계속 늘린다 —
# Q2_K_L, IQ4_NL, MXFP4_MOE, TQ1_0, unsloth의 UD-Q4_K_XL 까지 있다. 목록으로
# 관리하면 새 표기가 나올 때마다 조용히 UNLABELED가 된다(실측 310개가 그랬다).
#
# 대신 파일명을 `-`·`.`로 쪼개 오른쪽부터 양자화 토큰처럼 생긴 것을 찾는다.
#   LFM2.5-8B-A1B-MXFP4_MOE.gguf  → [LFM2, 5, 8B, A1B, MXFP4_MOE] → MXFP4_MOE
#   GRaPE-2.5-Helios.Q4_K_M.gguf  → [..., Helios, Q4_K_M]         → Q4_K_M
#   Qwen3-8B.gguf                 → [Qwen3, 8B]                   → 없음
# "Qwen3"은 Q 다음이 숫자가 아니라서 걸리지 않는다.
_QUANT_TOKEN = re.compile(
    r"^(?:"
    r"I?Q\d+(?:_[A-Z0-9]+)*"       # Q4_K_M, Q2_K_L, IQ3_XXS, IQ4_NL
    r"|MXFP\d+(?:_[A-Z0-9]+)*"     # MXFP4_MOE
    r"|TQ\d+_\d+"                  # TQ1_0
    r"|(?:B?F\d+|FP\d+)_I?Q\d+(?:_[A-Z0-9]+)*"   # f16_q8_0 (임베딩만 고정밀)
    r"|BF16|F16|F32|FP16|FP32|FP8"  # 비양자화
    r")$",
    re.IGNORECASE,
)

# 가중치가 아닌 파일. 용량에 넣으면 "몇 GB 필요하냐"의 답이 틀린다.
#   mmproj / projector   비전·오디오 인코더 사이드카
#   imatrix              양자화 캘리브레이션 데이터. 모델이 아니다 (실측 140개)
SIDECAR_PATTERNS = ("mmproj", "projector", "vision_encoder", "audio_tower", "imatrix")


def _siblings(raw: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for sibling in raw.get("siblings") or []:
        name = sibling.get("rfilename")
        if not name:
            continue
        size = sibling.get("size")
        out.append({
            "name": name,
            "lower": name.lower(),
            "size": size if isinstance(size, int) and size >= 0 else None,
        })
    return out


def _belongs(entry: Dict[str, Any], fmt: str) -> bool:
    """어떤 포맷의 파일인지. 확장자가 겹치는 포맷은 경로로 가른다."""
    lower = entry["lower"]
    if fmt == "mlx":
        return lower.endswith(".safetensors") and ("mlx" in lower or lower.startswith("mlx"))
    if fmt == "ct2":
        return lower.endswith("model.bin") and ("ct2" in lower or "ctranslate" in lower)
    if fmt == "safetensors":
        return lower.endswith(".safetensors") and not ("mlx" in lower or lower.startswith("mlx"))
    if fmt == "pytorch_bin":
        if lower.endswith("model.bin") and ("ct2" in lower or "ctranslate" in lower):
            return False
        return lower.endswith(FORMAT_SUFFIX["pytorch_bin"])
    return lower.endswith(FORMAT_SUFFIX[fmt])


def quant_label(filename: str) -> Optional[str]:
    """파일명에서 양자화 레이블을 뽑는다. 못 찾으면 None."""
    stem = re.sub(r"\.gguf$", "", filename.rsplit("/", 1)[-1], flags=re.IGNORECASE)
    for token in reversed(re.split(r"[-.]", stem)):
        if _QUANT_TOKEN.match(token):
            return token.upper()
    return None


def is_sidecar(filename: str) -> bool:
    lower = filename.lower()
    return any(pattern in lower for pattern in SIDECAR_PATTERNS)


def resolve(raw: Dict[str, Any], retrieved_at: Optional[str] = None) -> Dict[str, Any]:
    """계약의 ``artifacts`` 그룹과 그에 대한 provenance 항목을 만든다."""
    entries = _siblings(raw)
    sizes_known = any(entry["size"] is not None for entry in entries)
    total_bytes = sum(entry["size"] or 0 for entry in entries) if sizes_known else None

    # usedStorage는 교차 검증에 쓰지 않는다. 현재 스냅샷 크기가 아니라 LFS
    # 히스토리를 포함한 과금 기준 용량으로 보인다. 실측(표본 1,796):
    #   yongzx/gpt2-finetuned-oscar-ko   siblings 404MB vs usedStorage 709GB (0.001배)
    #   RANITBAG/on_the_way              siblings 1.6GB vs usedStorage 630MB (2.509배)
    # 중앙값은 1.000이지만 521건(29%)이 2% 밖으로 벗어난다. 중앙값만 보고
    # 교차 검증에 쓰면 정상 모델에 거짓 경고가 붙는다.
    note = None

    formats: Dict[str, Any] = {}
    for fmt in FORMATS:
        members = [entry for entry in entries if _belongs(entry, fmt)]
        weights = [entry for entry in members if not is_sidecar(entry["name"])]
        fmt_bytes = (
            sum(entry["size"] or 0 for entry in weights)
            if weights and all(entry["size"] is not None for entry in weights)
            else None
        )
        quantization = None
        if fmt == "gguf" and weights:
            buckets: Dict[str, Dict[str, int]] = {}
            for entry in weights:
                label = quant_label(entry["name"]) or "UNLABELED"
                bucket = buckets.setdefault(label, {"total_bytes": 0, "file_count": 0})
                bucket["total_bytes"] += entry["size"] or 0
                bucket["file_count"] += 1
            quantization = [
                {"label": label, "total_bytes": bucket["total_bytes"], "file_count": bucket["file_count"]}
                for label, bucket in sorted(buckets.items(), key=lambda item: item[1]["total_bytes"])
            ]
        formats[fmt] = {
            "present": bool(members),
            "file_count": len(members),
            "total_bytes": fmt_bytes,
            "shard_count": _shard_count(weights),
            "quantization": quantization,
        }

    provenance: Dict[str, Any] = {}
    if entries:
        source = ["hf_api:siblings[].size"] if sizes_known else ["hf_api:siblings[].rfilename"]
        provenance["artifacts.total_bytes"] = (
            facts.fact("verified", source, note, retrieved_at)
            if total_bytes is not None
            else facts.unknown("siblings에 size가 없다")
        )
        for fmt in ("gguf", "safetensors"):
            provenance[f"artifacts.formats.{fmt}"] = facts.fact(
                "verified",
                ["hf_api:siblings[].rfilename"],
                None if formats[fmt]["present"] else f"{fmt} 파일이 없음을 확인했다",
                retrieved_at,
            )
    else:
        provenance["artifacts.total_bytes"] = facts.unknown("siblings가 비어 있다")
        for fmt in ("gguf", "safetensors"):
            provenance[f"artifacts.formats.{fmt}"] = facts.unknown("siblings가 비어 있다")

    return {
        "artifacts": {
            "file_count": len(entries),
            "total_bytes": total_bytes,
            "formats": formats,
        },
        "provenance": provenance,
    }


def _shard_count(weights: Sequence[Dict[str, Any]]) -> Optional[int]:
    """`model-00002-of-00005.safetensors` 꼴에서 샤드 수를 읽는다.

    파일 수를 그대로 쓰면 안 된다. GGUF 레포의 파일 6개는 한 모델의 샤드 6개가
    아니라 양자화본 6벌이다. 패턴이 없고 파일이 하나일 때만 1로 본다.
    """
    for entry in weights:
        match = re.search(r"-of-(\d{3,6})\.", entry["lower"])
        if match:
            return int(match.group(1))
    return 1 if len(weights) == 1 else None


def smallest_runnable_bytes(artifacts: Dict[str, Any]) -> Optional[Tuple[str, int]]:
    """실제로 돌리는 데 필요한 최소 한 벌의 크기. (레이블, 바이트)

    GGUF 레포는 양자화본이 여러 벌이므로 전체 합이 아니라 가장 작은 한 벌이
    "이 GPU에 들어가나"의 하한이다.

    ``UNLABELED`` 묶음은 레이블 있는 묶음이 하나라도 있으면 쓰지 않는다. 같은
    레포에 LoRA 어댑터(`...-r16.gguf`)나 MoE 전문가 레이어(`layer-01-experts.gguf`)
    가 섞여 들어오는데, 이들은 단독으로 돌아가지 않는다. 바이트만 보고 최소를
    고르면 43MB짜리 어댑터가 "이 모델 43MB면 됩니다"가 된다.
    """
    gguf = (artifacts.get("formats") or {}).get("gguf") or {}
    quantization = gguf.get("quantization") or []
    usable = [item for item in quantization if item.get("total_bytes")]
    labeled = [item for item in usable if item["label"] != "UNLABELED"]
    pool = labeled or usable
    if pool:
        best = min(pool, key=lambda item: item["total_bytes"])
        return best["label"], best["total_bytes"]
    for fmt in ("safetensors", "pytorch_bin", "onnx", "mlx", "ct2"):
        spec = (artifacts.get("formats") or {}).get(fmt) or {}
        if spec.get("present") and spec.get("total_bytes"):
            return fmt, spec["total_bytes"]
    return None
