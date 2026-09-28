from huggingface_hub import (
    HfApi,
    ModelCard,
    hf_hub_download,
)

import json
import os
import re
import time

from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


# =========================================================
# CONFIG
# =========================================================

HF_TOKEN = os.getenv("HF_TOKEN")

api = HfApi(
    token=HF_TOKEN
)


DATA_DIR = Path("data")


# =========================================================
# SOURCE POOL
# =========================================================

SOURCE_POOLS = ["core", "low_popularity"]

POOL_CONFIGS = {
    pool: {
        "input": DATA_DIR / f"hf_models_stage1_{pool}.jsonl",
        "output": DATA_DIR / f"hf_models_stage2_{pool}.jsonl",
 # Error rows are reported on stdout; no error JSON artifact is generated.
        "readme_dir": DATA_DIR / "readmes" / pool,
    }
    for pool in SOURCE_POOLS
}


# =========================================================
# RUN POLICY
# =========================================================

# 첫 검증:
TEST_LIMIT = None

# 전체 실행:
# TEST_LIMIT = None


CHECKPOINT_EVERY = 25

REQUEST_SLEEP = 0.10

MAX_RETRIES = 3

RETRY_BASE_SECONDS = 1.0


# README는 Stage 3 입력이므로
# 너무 큰 README만 절단.
MAX_README_CHARS = 300_000


STAGE2_VERSION = 6
SOURCE_STAGE1_VERSION = 7
A_VERIFIED_TYPES = {"korean_explicit", "korean_translation_pair", "korean_name_strong"}


def model_page_url(model_id):
    """Return the canonical Hugging Face model page for provenance output."""
    return f"https://huggingface.co/{quote(str(model_id), safe='/')}"


def model_readme_url(model_id):
    """Return the clickable README source URL for a model card."""
    return f"{model_page_url(model_id)}/blob/main/README.md"


# =========================================================
# IO
# =========================================================

def load_jsonl(path):

    rows = []

    if not path.exists():
        return rows


    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            rows.append(
                json.loads(
                    line
                )
            )

    return rows


def save_jsonl_atomic(
    rows,
    path,
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = (
        path.with_suffix(
            path.suffix
            + ".tmp"
        )
    )


    with open(
        temp_path,
        "w",
        encoding="utf-8",
    ) as f:

        for row in rows:

            f.write(
                json.dumps(
                    row,
                    ensure_ascii=False,
                )
            )

            f.write("\n")


    os.replace(
        temp_path,
        path,
    )


# =========================================================
# GENERAL UTILS
# =========================================================

def ensure_list(value):

    if value is None:
        return []

    if isinstance(
        value,
        list,
    ):
        return value

    if isinstance(
        value,
        tuple,
    ):
        return list(value)

    if isinstance(
        value,
        set,
    ):
        return list(value)

    return [value]


def numeric_metadata_status(value):
    """Return an explicit status for numeric metadata used by recommenders.

    ``None`` means that the source did not provide a trustworthy value.  It
    must remain an unknown value and must never be coerced to zero.  Zero and
    negative values are also treated as unknown because they are not valid
    parameter counts or context lengths.
    """
    if isinstance(value, bool):
        return "unknown"
    if isinstance(value, (int, float)) and value > 0:
        return "known"
    return "unknown"


def safe_get(
    obj,
    key,
    default=None,
):

    if obj is None:
        return default

    if isinstance(
        obj,
        dict,
    ):
        return obj.get(
            key,
            default,
        )

    return getattr(
        obj,
        key,
        default,
    )


def safe_iso(value):

    if value is None:
        return None

    try:
        return value.isoformat()

    except Exception:
        return str(value)


def utc_now():

    return (
        datetime.now(
            timezone.utc
        )
        .isoformat()
    )


def safe_filename(
    model_id,
):

    return (
        re.sub(
            r"[^a-zA-Z0-9._\-]+",
            "__",
            model_id,
        )
        + ".md"
    )


# =========================================================
# RETRY
# =========================================================

def retry_call(
    func,
    *args,
    **kwargs,
):

    last_error = None


    for attempt in range(
        1,
        MAX_RETRIES + 1,
    ):

        try:

            return func(
                *args,
                **kwargs,
            )

        except Exception as e:

            last_error = e


            if attempt >= MAX_RETRIES:
                break


            wait = (
                RETRY_BASE_SECONDS
                * attempt
            )


            time.sleep(
                wait
            )


    raise last_error


# =========================================================
# HUB MODEL INFO
# =========================================================

def load_model_info(
    model_id,
):

    try:

        info = retry_call(
            api.model_info,
            model_id,
            files_metadata=True,
        )


        return {
            "data":
                info,

            "available":
                True,

            "error":
                None,
        }


    except Exception as e:

        return {
            "data":
                None,

            "available":
                False,

            "error":
                (
                    f"{type(e).__name__}: "
                    f"{e}"
                ),
        }


# =========================================================
# JSON FILE FETCH
# =========================================================

def load_json_file(
    model_id,
    filename,
):

    try:

        path = retry_call(
            hf_hub_download,
            repo_id=model_id,
            filename=filename,
            token=HF_TOKEN,
        )


        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:

            data = json.load(
                f
            )


        return {
            "data":
                data,

            "available":
                True,

            "error":
                None,
        }


    except Exception as e:

        return {
            "data":
                {},

            "available":
                False,

            "error":
                (
                    f"{type(e).__name__}: "
                    f"{e}"
                ),
        }


# =========================================================
# README
# =========================================================

def load_and_save_readme(
    model_id,
    readme_dir,
):

    try:

        source_path = retry_call(
            hf_hub_download,
            repo_id=model_id,
            filename="README.md",
            token=HF_TOKEN,
        )


        with open(
            source_path,
            "r",
            encoding="utf-8",
            errors="replace",
        ) as f:

            full_text = f.read()


        original_chars = len(
            full_text
        )


        truncated = (
            original_chars
            > MAX_README_CHARS
        )


        if truncated:

            saved_text = (
                full_text[
                    :MAX_README_CHARS
                ]
            )

        else:

            saved_text = (
                full_text
            )


        readme_dir.mkdir(
            parents=True,
            exist_ok=True,
        )


        output_path = (
            readme_dir
            / safe_filename(
                model_id
            )
        )


        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(
                saved_text
            )


        return {
            "text":
                saved_text,

            "available":
                True,

            "path":
                str(
                    output_path
                ),
            "source_url":
                model_page_url(model_id),
            "readme_url":
                model_readme_url(model_id),

            "original_chars":
                original_chars,

            "saved_chars":
                len(
                    saved_text
                ),

            "truncated":
                truncated,

            "error":
                None,
        }


    except Exception as e:

        return {
            "text":
                None,

            "available":
                False,

            "path":
                None,
            "source_url":
                model_page_url(model_id),
            "readme_url":
                model_readme_url(model_id),

            "original_chars":
                None,

            "saved_chars":
                None,

            "truncated":
                False,

            "error":
                (
                    f"{type(e).__name__}: "
                    f"{e}"
                ),
        }


# =========================================================
# MODEL CARD
# =========================================================

def load_card_metadata(
    model_id,
    info=None,
):

    # =====================================================
    # 1. model_info.cardData 우선
    # =====================================================

    card_data = safe_get(
        info,
        "cardData",
        None,
    )


    if card_data:

        if isinstance(
            card_data,
            dict,
        ):

            return {
                "data":
                    card_data,

                "source":
                    "model_info.cardData",

                "error":
                    None,
            }


        try:

            return {
                "data":
                    card_data.to_dict(),

                "source":
                    "model_info.cardData",

                "error":
                    None,
            }

        except Exception:
            pass


    # =====================================================
    # 2. fallback: ModelCard.load
    # =====================================================

    try:

        try:

            card = retry_call(
                ModelCard.load,
                model_id,
                ignore_metadata_errors=True,
            )

        except TypeError:

            # huggingface_hub 버전 호환
            card = retry_call(
                ModelCard.load,
                model_id,
            )


        if not card.data:

            return {
                "data":
                    {},

                "source":
                    "ModelCard.load",

                "error":
                    None,
            }


        try:

            data = (
                card.data.to_dict()
            )

        except Exception:

            data = {}


        return {
            "data":
                data,

            "source":
                "ModelCard.load",

            "error":
                None,
        }


    except Exception as e:

        return {
            "data":
                {},

            "source":
                None,

            "error":
                (
                    f"{type(e).__name__}: "
                    f"{e}"
                ),
        }


# =========================================================
# CONFIG PARSING
# =========================================================

CONTEXT_KEYS = [
    "max_position_embeddings",
    "n_positions",
    "max_seq_len",
    "max_sequence_length",
    "seq_length",
    "model_max_length",
    "context_length",
    "max_context_length",
]


NESTED_CONFIG_KEYS = [
    "text_config",
    "language_config",
    "decoder",
    "llm_config",
]


def config_sections(
    config,
):

    if not isinstance(
        config,
        dict,
    ):
        return []


    sections = [
        config
    ]


    for key in (
        NESTED_CONFIG_KEYS
    ):

        value = (
            config.get(
                key
            )
        )

        if isinstance(
            value,
            dict,
        ):

            sections.append(
                value
            )


    return sections


def extract_context_candidates(
    config,
    tokenizer_config,
):

    candidates = []


    # =====================================================
    # config.json
    # =====================================================

    for section in (
        config_sections(
            config
        )
    ):

        for key in (
            CONTEXT_KEYS
        ):

            value = (
                section.get(
                    key
                )
            )


            if (
                isinstance(
                    value,
                    int,
                )
                and
                0 < value < 10_000_000
            ):

                candidates.append({
                    "value":
                        value,

                    "source":
                        f"config.{key}",
                })


    # =====================================================
    # tokenizer_config.json
    # =====================================================

    if isinstance(
        tokenizer_config,
        dict,
    ):

        value = (
            tokenizer_config.get(
                "model_max_length"
            )
        )


        if (
            isinstance(
                value,
                int,
            )
            and
            0 < value < 10_000_000
        ):

            candidates.append({
                "value":
                    value,

                "source":
                    (
                        "tokenizer_config."
                        "model_max_length"
                    ),
            })


    return candidates


def choose_context_length(
    candidates,
):

    if not candidates:
        return {
            "value":
                None,

            "evidence":
                [],
        }


    # 여러 config 위치에서 발견되면
    # 가장 큰 유효값 사용.
    best = max(
        candidates,
        key=lambda x:
            x[
                "value"
            ],
    )


    return {
        "value":
            best[
                "value"
            ],

        "evidence":
            candidates,
    }


def extract_dtype(
    config,
):

    for section in (
        config_sections(
            config
        )
    ):

        value = (
            section.get(
                "torch_dtype"
            )
            or
            section.get(
                "dtype"
            )
        )

        if value:
            return str(
                value
            )


    return None


def extract_architectures(
    config,
):

    if not isinstance(
        config,
        dict,
    ):
        return []


    architectures = (
        config.get(
            "architectures"
        )
    )


    return ensure_list(
        architectures
    )


# =========================================================
# PARAMETER COUNT
# =========================================================

def extract_parameter_count(
    info,
):

    if info is None:
        return None


    safetensors = safe_get(
        info,
        "safetensors",
        None,
    )


    if safetensors is None:
        return None


    parameters = safe_get(
        safetensors,
        "parameters",
        None,
    )


    if isinstance(
        parameters,
        int,
    ):

        return parameters


    if isinstance(
        parameters,
        dict,
    ):

        values = [
            value
            for value
            in parameters.values()
            if isinstance(
                value,
                int,
            )
        ]


        total = sum(
            values
        )


        if total > 0:
            return total


    return None


# =========================================================
# ARTIFACTS
# =========================================================

def extract_artifacts(
    info,
):

    filenames = []


    if info is not None:

        for sibling in (
            safe_get(
                info,
                "siblings",
                [],
            )
            or []
        ):

            filename = (
                safe_get(
                    sibling,
                    "rfilename",
                    None,
                )
            )

            if filename:

                filenames.append(
                    filename.lower()
                )


    return {
        "safetensors":
            any(
                x.endswith(
                    ".safetensors"
                )
                for x in filenames
            ),

        "gguf":
            any(
                x.endswith(
                    ".gguf"
                )
                for x in filenames
            ),

        "pytorch_bin":
            any(
                x.endswith(
                    ".bin"
                )
                for x in filenames
            ),

        "onnx":
            any(
                x.endswith(
                    ".onnx"
                )
                for x in filenames
            ),

        "file_count":
            len(
                filenames
            ),
    }


# =========================================================
# QUANTIZATION
# =========================================================

QUANTIZATION_PATTERNS = [
    ("awq", "awq", 4),
    ("gptq", "gptq", None),
    ("bnb-4bit", "bnb", 4),
    ("bnb_4bit", "bnb", 4),
    ("4bit", "unknown", 4),
    ("int4", "int4", 4),
    ("8bit", "unknown", 8),
    ("int8", "int8", 8),
    ("fp4", "fp4", 4),
    ("nvfp4", "nvfp4", 4),
    ("fp8", "fp8", 8),
    ("mlx-4bit", "mlx", 4),
    ("mlx-5bit", "mlx", 5),
    ("mlx-6bit", "mlx", 6),
    ("mlx-8bit", "mlx", 8),
]


def extract_quantization(
    stage1_row,
    config,
):

    model_id = (
        stage1_row[
            "model_id"
        ]
    )


    tags = (
        stage1_row.get(
            "hub",
            {},
        ).get(
            "tags",
            [],
        )
    )


    variant_types = (
        stage1_row.get(
            "family",
            {},
        ).get(
            "variant_types",
            [],
        )
    )


    method = None
    bits = None
    evidence = []


    # =====================================================
    # 1. config.json
    # =====================================================

    if isinstance(
        config,
        dict,
    ):

        qconfig = (
            config.get(
                "quantization_config"
            )
        )

    else:

        qconfig = None


    if isinstance(
        qconfig,
        dict,
    ):

        method = (
            qconfig.get(
                "quant_method"
            )
            or
            qconfig.get(
                "method"
            )
        )


        qbits = (
            qconfig.get(
                "bits"
            )
        )


        if isinstance(
            qbits,
            int,
        ):

            bits = qbits


        evidence.append(
            "config.quantization_config"
        )


    # =====================================================
    # 2. Stage 1 variant detection
    # =====================================================

    for variant in (
        variant_types
    ):

        evidence.append(
            f"stage1.variant:{variant}"
        )


    # =====================================================
    # 3. name / tags
    # =====================================================

    joined = " ".join(
        [
            model_id.lower()
        ]
        +
        [
            str(tag).lower()
            for tag in tags
        ]
        +
        [
            str(v).lower()
            for v in variant_types
        ]
    )


    for (
        keyword,
        inferred_method,
        inferred_bits,
    ) in QUANTIZATION_PATTERNS:

        if keyword in joined:

            if method is None:

                method = (
                    inferred_method
                )


            if (
                bits is None
                and inferred_bits
                is not None
            ):

                bits = (
                    inferred_bits
                )


            evidence.append(
                f"name_or_tag:{keyword}"
            )


    return {
        "enabled":
            bool(
                method
                or bits
                or variant_types
            ),

        "method":
            method,

        "bits":
            bits,

        "evidence":
            list(
                dict.fromkeys(
                    evidence
                )
            ),
    }


# =========================================================
# LANGUAGE
# =========================================================

KOREAN_CODES = {
    "ko",
    "kor",
    "korean",
    "ko-kr",
}


MULTILINGUAL_MARKERS = {
    "multilingual",
    "multilinguality",
    "multi-lingual",
    "multi-language",
}


def normalize_language_values(values):
    output = set()
    for value in ensure_list(values):
        if value is None:
            continue
        value = str(value).strip().lower()
        if value.startswith("language:"):
            value = value.split(":", 1)[1].strip()
        if value in MULTILINGUAL_MARKERS:
            output.add("multilingual")
        elif value:
            value = value.replace("_", "-")
            if value in KOREAN_CODES:
                value = "ko"
            # Regional spellings of the same language do not inflate counts.
            if re.fullmatch(r"[a-z]{2,3}(?:-[a-z0-9]+)+", value):
                value = value.split("-", 1)[0]
            output.add(value)
    return output


def verify_languages(stage1_row, card_metadata, readme_text):
    """Additional factual evidence; never rewrite the Stage 1 candidate."""
    stage1_language = stage1_row.get("language", {})
    candidate_type = stage1_row.get("candidate", {}).get("type")
    stage1_values = normalize_language_values(stage1_language.get("languages", []))
    card_values = normalize_language_values(card_metadata.get("language", []))
    stage1_languages = stage1_values - MULTILINGUAL_MARKERS
    card_languages = card_values - MULTILINGUAL_MARKERS
    languages = stage1_languages | card_languages
    readme_lower = (readme_text or "").lower()

    korean = None
    korean_confidence = "unknown"
    korean_evidence = []
    if languages & KOREAN_CODES:
        korean, korean_confidence = True, "high"
        korean_evidence.append("metadata.language:korean")
    if candidate_type in A_VERIFIED_TYPES:
        korean, korean_confidence = True, "high"
        korean_evidence.append(f"stage1:{candidate_type}")
    if any(phrase in readme_lower for phrase in (
        "supports korean", "korean language", "korean support", "한국어 지원", "supports ko-kr"
    )):
        if korean is None:
            korean, korean_confidence = True, "medium"
        korean_evidence.append("readme:korean_explicit_phrase")

    multilingual = None
    multilingual_confidence = "unknown"
    multilingual_evidence = []
    if candidate_type in {"multilingual_explicit", "multilingual_language_list"}:
        multilingual, multilingual_confidence = True, "high"
        multilingual_evidence.append(f"stage1:{candidate_type}")
    if len(stage1_languages) >= 3:
        multilingual, multilingual_confidence = True, "high"
        multilingual_evidence.append("stage1:3plus_languages")
    if len(card_languages) >= 3:
        multilingual, multilingual_confidence = True, "high"
        multilingual_evidence.append("model_card:3plus_languages")
    if card_values & MULTILINGUAL_MARKERS:
        if len(card_languages) >= 2:
            multilingual, multilingual_confidence = True, "high"
            multilingual_evidence.append("model_card:multilingual_with_language_list")
        else:
            multilingual_evidence.append("model_card:multilingual_marker_only")
    if candidate_type == "multilingual_tag_only":
        # A weak Stage 1 marker remains unverified without additional evidence.
        multilingual_evidence.append("stage1:multilingual_tag_only")

    bilingual = None
    bilingual_evidence = []
    if candidate_type == "bilingual_language_list":
        bilingual = True
        bilingual_evidence.append("stage1:bilingual_language_list")
    if len(card_languages) == 2:
        bilingual = True
        bilingual_evidence.append("model_card:2_languages")
    return {
        "stage1": stage1_language,
        "declared_languages": sorted(languages),
        "language_count": len(languages),
        "korean": {"verified": korean, "confidence": korean_confidence, "evidence": korean_evidence},
        "multilingual": {"verified": multilingual, "confidence": multilingual_confidence, "evidence": multilingual_evidence},
        "bilingual": {"verified": bilingual, "evidence": bilingual_evidence},
    }


# =========================================================
# MEMORY ESTIMATE
# =========================================================

def weight_memory_gib(
    parameters,
    bits,
):

    if not parameters:
        return None


    return round(
        (
            parameters
            * bits
            / 8
        )
        /
        (
            1024 ** 3
        ),
        2,
    )


def build_hardware_estimate(
    parameters,
    quantization,
):

    actual_bits = (
        quantization.get(
            "bits"
        )
    )


    actual_estimate = None


    if isinstance(
        actual_bits,
        int,
    ):

        actual_estimate = (
            weight_memory_gib(
                parameters,
                actual_bits,
            )
        )


    return {
        # 이것들은 runtime VRAM이 아니라
        # weights-only theoretical estimate.
        "weights_only": {
            "fp16_gib":
                weight_memory_gib(
                    parameters,
                    16,
                ),

            "int8_gib":
                weight_memory_gib(
                    parameters,
                    8,
                ),

            "int4_gib":
                weight_memory_gib(
                    parameters,
                    4,
                ),

            "detected_quantization_gib":
                actual_estimate,
        },

        "note":
            (
                "Weights-only estimate. "
                "Runtime VRAM/RAM also depends on "
                "KV cache, activations, framework, "
                "batch size, and context length."
            ),
    }


# =========================================================
# RUNTIME COMPATIBILITY
# =========================================================

RUNTIME_COMPATIBILITY_VERSION = 1


def _runtime_marker_status(readme_text, patterns):
    """Return documented support status for a runtime marker."""
    text = str(readme_text or "")
    lowered = text.casefold()
    for pattern, label in patterns:
        match = re.search(pattern, lowered, flags=re.IGNORECASE)
        if not match:
            continue
        window = lowered[max(0, match.start() - 100): min(len(lowered), match.end() + 100)]
        if re.search(r"(?:not|no|without|unsupported|does not)\s+(?:currently\s+)?support", window):
            return {
                "status": "documented_unsupported",
                "confidence": "high",
                "evidence": [f"readme_marker:{label}"],
            }
        if not re.search(
            r"support|compatible|install|serve|run|use|backend|provider|export|inference",
            window,
        ):
            return {
                "status": "mentioned",
                "confidence": "low",
                "evidence": [f"readme_marker:{label}"],
            }
        return {
            "status": "documented",
            "confidence": "high",
            "evidence": [f"readme_marker:{label}"],
        }
    return None


def extract_runtime_compatibility(artifacts, readme_text):
    """Build conservative, auditable runtime compatibility metadata.

    ``documented`` means the model card mentions the runtime. ``artifact_present``
    means only that a compatible-looking artifact exists. ``inferred`` is a
    weak format-based hint; it is never treated as a successful execution test.
    """
    artifacts = artifacts if isinstance(artifacts, dict) else {}
    runtime_patterns = {
        "cpu": [(r"\bcpu(?:-only)?\b|\bavx(?:2|512)?\b", "cpu")],
        "cuda": [(r"\bcuda\b|\bnvidia\s+cuda\b|\bcu\d{2,3}\b", "cuda")],
        "mps": [(r"\bmps\b|metal performance shaders|\bapple silicon\b|\bmlx\b", "mps")],
        "vllm": [(r"\bvllm\b|vllm\.entrypoints", "vllm")],
        "onnx": [(r"\bonnxruntime\b|\bonnx\b", "onnx")],
        "llama_cpp": [(r"llama[ ._-]*cpp|llama-server|llama-cli|llama_server", "llama_cpp")],
    }
    conditions = {
        "cpu": "RAM, model size, and performance depend on the runtime and workload.",
        "cuda": "GPU VRAM, driver, CUDA, architecture, and quantization must be compatible.",
        "mps": "Apple Silicon and the selected framework must support the architecture.",
        "vllm": "vLLM version, model architecture, GPU, and quantization support are required.",
        "onnx": "The ONNX graph and selected execution provider must be supported.",
        "llama_cpp": "GGUF architecture support and the llama.cpp build must be compatible.",
    }
    result = {"version": RUNTIME_COMPATIBILITY_VERSION}
    for runtime, patterns in runtime_patterns.items():
        documented = _runtime_marker_status(readme_text, patterns)
        if documented:
            result[runtime] = {**documented, "conditions": conditions[runtime]}
            continue

        artifact_key = {"onnx": "onnx", "llama_cpp": "gguf"}.get(runtime)
        if artifact_key and artifacts.get(artifact_key) is True:
            result[runtime] = {
                "status": "artifact_present",
                "confidence": "medium",
                "evidence": [f"artifact:{artifact_key}"],
                "conditions": conditions[runtime],
            }
            continue

        if runtime == "cpu" and any(artifacts.get(key) is True for key in ("safetensors", "pytorch_bin", "onnx", "gguf")):
            result[runtime] = {
                "status": "inferred",
                "confidence": "low",
                "evidence": ["artifact:model_weights"],
                "conditions": conditions[runtime],
            }
            continue

        if runtime == "cuda" and any(artifacts.get(key) is True for key in ("safetensors", "pytorch_bin", "gguf")):
            result[runtime] = {
                "status": "inferred",
                "confidence": "low",
                "evidence": ["artifact:model_weights"],
                "conditions": conditions[runtime],
            }
            continue

        result[runtime] = {
            "status": "unknown",
            "confidence": "low",
            "evidence": [],
            "conditions": conditions[runtime],
        }
    return result


# =========================================================
# BASE MODEL / CARD FIELDS
# =========================================================

def normalize_base_model(
    value,
):

    values = []


    for item in (
        ensure_list(
            value
        )
    ):

        if item is None:
            continue


        item = str(
            item
        ).strip()


        if (
            item
            and item not in values
        ):

            values.append(
                item
            )


    return values


def extract_base_models(
    stage1_row,
    card_metadata,
):

    card_base = (
        normalize_base_model(
            card_metadata.get(
                "base_model"
            )
        )
    )


    stage1_base = (
        normalize_base_model(
            stage1_row.get(
                "family",
                {},
            ).get(
                "declared_base_models",
                [],
            )
        )
    )


    combined = []


    for value in (
        card_base
        +
        stage1_base
    ):

        if value not in combined:

            combined.append(
                value
            )


    return combined


# =========================================================
# ENRICH
# =========================================================

def enrich(
    stage1_row,
    source_pool,
):

    model_id = (
        stage1_row[
            "model_id"
        ]
    )


    # =====================================================
    # Hub
    # =====================================================

    info_result = (
        load_model_info(
            model_id
        )
    )

    info = (
        info_result[
            "data"
        ]
    )


    # =====================================================
    # config.json
    # =====================================================

    config_result = (
        load_json_file(
            model_id,
            "config.json",
        )
    )

    config = (
        config_result[
            "data"
        ]
    )


    # =====================================================
    # tokenizer_config.json
    # =====================================================

    tokenizer_result = (
        load_json_file(
            model_id,
            "tokenizer_config.json",
        )
    )

    tokenizer_config = (
        tokenizer_result[
            "data"
        ]
    )


    # =====================================================
    # README
    # =====================================================

    readme_result = (
        load_and_save_readme(
            model_id,
            POOL_CONFIGS[source_pool]["readme_dir"],
        )
    )

    readme_text = (
        readme_result[
            "text"
        ]
    )


    # =====================================================
    # Model Card metadata
    # =====================================================

    card_result = (
        load_card_metadata(
            model_id,
            info,
        )
    )

    card_metadata = (
        card_result[
            "data"
        ]
    )


    # =====================================================
    # Parameters
    # =====================================================

    parameters = (
        extract_parameter_count(
            info
        )
    )


    # =====================================================
    # Context
    # =====================================================

    context_candidates = (
        extract_context_candidates(
            config,
            tokenizer_config,
        )
    )

    context = (
        choose_context_length(
            context_candidates
        )
    )


    # =====================================================
    # Quantization
    # =====================================================

    quantization = (
        extract_quantization(
            stage1_row,
            config,
        )
    )


    # =====================================================
    # Language
    # =====================================================

    language = (
        verify_languages(
            stage1_row,
            card_metadata,
            readme_text,
        )
    )


    # =====================================================
    # Base model
    # =====================================================

    base_models = (
        extract_base_models(
            stage1_row,
            card_metadata,
        )
    )


    # =====================================================
    # Current Hub popularity
    # =====================================================

    current_downloads = (
        safe_get(
            info,
            "downloads",
            None,
        )
        if info
        else None
    )

    current_likes = (
        safe_get(
            info,
            "likes",
            None,
        )
        if info
        else None
    )


    # =====================================================
    # FINAL SCHEMA
    # =====================================================

    return {
        # -------------------------------------------------
        # Identity
        # -------------------------------------------------

        "model_id":
            model_id,

        "author":
            stage1_row.get(
                "author"
            ),


        # -------------------------------------------------
        # Stage 1 classification preserved
        # -------------------------------------------------

        "task": {
            "primary":
                stage1_row.get(
                    "primary_task"
                ),

            "matched":
                stage1_row.get(
                    "matched_tasks",
                    [],
                ),
        },


        "candidate":
            stage1_row.get(
                "candidate",
                {},
            ),


        "popularity": {
            "stage1": {
                "downloads":
                    stage1_row.get(
                        "popularity",
                        {},
                    ).get(
                        "downloads"
                    ),

                "likes":
                    stage1_row.get(
                        "popularity",
                        {},
                    ).get(
                        "likes"
                    ),

                "tier":
                    stage1_row.get(
                        "popularity",
                        {},
                    ).get(
                        "tier"
                    ),
            },

            "current": {
                "downloads":
                    current_downloads,

                "likes":
                    current_likes,
            },
        },


        "family":
            stage1_row.get(
                "family",
                {},
            ),


        "stage1_quality":
            stage1_row.get(
                "quality",
                {},
            ),


        # -------------------------------------------------
        # Verified/enriched language
        # -------------------------------------------------

        "language":
            language,


        # -------------------------------------------------
        # Model technical metadata
        # -------------------------------------------------

        "model": {
            "type":
                (
                    config.get(
                        "model_type"
                    )
                    if isinstance(
                        config,
                        dict,
                    )
                    else None
                ),

            "architectures":
                extract_architectures(
                    config
                ),

            "parameter_count":
                parameters,

            "parameter_count_billion":
                (
                    round(
                        parameters
                        / 1e9,
                        3,
                    )
                    if parameters
                    else None
                ),

            "context_length":
                context[
                    "value"
                ],

            "context_evidence":
                context[
                    "evidence"
                ],

            # ``unknown`` is intentional. Recommendation and hardware
            # filters must not interpret missing metadata as zero.
            "metadata_status": {
                "parameter_count": numeric_metadata_status(parameters),
                "context_length": numeric_metadata_status(context["value"]),
            },

            "dtype":
                extract_dtype(
                    config
                ),
        },


        # -------------------------------------------------
        # Deployment / artifact
        # -------------------------------------------------

        "quantization":
            quantization,


        "artifacts":
            extract_artifacts(
                info
            ),


        "hardware":
            build_hardware_estimate(
                parameters,
                quantization,
            ),
        "runtime_compatibility": extract_runtime_compatibility(
            extract_artifacts(info),
            readme_text,
        ),


        # -------------------------------------------------
        # Model card
        # -------------------------------------------------

        "license":
            (
                card_metadata.get(
                    "license"
                )
                or
                stage1_row.get(
                    "hub",
                    {},
                ).get(
                    "license"
                )
            ),


        "base_models":
            base_models,


        "datasets":
            ensure_list(
                card_metadata.get(
                    "datasets"
                )
            ),


        "metrics":
            ensure_list(
                card_metadata.get(
                    "metrics"
                )
            ),


        # -------------------------------------------------
        # Source provenance
        # -------------------------------------------------

        "source": {
            "hub": {
                "available":
                    info_result[
                        "available"
                    ],

                "error":
                    info_result[
                        "error"
                    ],
            },


            "config": {
                "available":
                    config_result[
                        "available"
                    ],

                "error":
                    config_result[
                        "error"
                    ],
            },


            "tokenizer_config": {
                "available":
                    tokenizer_result[
                        "available"
                    ],

                "error":
                    tokenizer_result[
                        "error"
                    ],
            },


            "model_card": {
                "source":
                    card_result[
                        "source"
                    ],

                "error":
                    card_result[
                        "error"
                    ],
            },


            "readme": {
                "available":
                    readme_result[
                        "available"
                    ],

                "path":
                    readme_result[
                        "path"
                    ],

                "original_chars":
                    readme_result[
                        "original_chars"
                    ],

                "saved_chars":
                    readme_result[
                        "saved_chars"
                    ],

                "truncated":
                    readme_result[
                        "truncated"
                    ],

                "error":
                    readme_result[
                        "error"
                    ],
            },
        },


        # -------------------------------------------------
        # Stage
        # -------------------------------------------------

        "stage": {
            "source_pool":
                source_pool,

            "source_stage1_version":
                stage1_row.get(
                    "stage",
                    {},
                ).get(
                    "stage1_version"
                ),

            "metadata_enriched":
                True,

            "semantic_enriched":
                False,

            "stage2_version":
                STAGE2_VERSION,

            "enriched_at":
                utc_now(),
        },
    }


# =========================================================
# MAIN
# =========================================================

def validate_stage2_rows(rows, source_pool):
    """Validate saved results using Stage 1 popularity, never current downloads."""
    if source_pool not in POOL_CONFIGS:
        raise ValueError(f"Unsupported source pool: {source_pool}")
    problems = []
    seen = set()
    required = {
        "model_id", "author", "task", "candidate", "popularity", "family", "stage1_quality",
        "language", "model", "quantization", "artifacts", "hardware", "runtime_compatibility", "license", "base_models",
        "datasets", "metrics", "source", "stage",
    }
    for row in rows:
        model_id = row.get("model_id", "<missing model_id>")
        reasons = []
        if required - row.keys():
            reasons.append(f"missing fields: {sorted(required - row.keys())}")
        if model_id in seen:
            reasons.append("duplicate model_id")
        seen.add(model_id)
        if row.get("candidate", {}).get("tier") != "A_verified":
            reasons.append("candidate.tier must be A_verified")
        if row.get("candidate", {}).get("type") not in A_VERIFIED_TYPES:
            reasons.append("candidate.type must be a Stage 1 v7 A_verified type")
        downloads = row.get("popularity", {}).get("stage1", {}).get("downloads")
        if not isinstance(downloads, (int, float)) or isinstance(downloads, bool):
            reasons.append("missing/invalid Stage 1 downloads")
        elif source_pool == "core" and not downloads >= 500:
            reasons.append("Stage 1 downloads must be >= 500")
        elif source_pool == "low_popularity" and not 80 <= downloads < 500:
            reasons.append("Stage 1 downloads must be 80..499")
        stage = row.get("stage", {})
        for key, expected in (("source_pool", source_pool), ("source_stage1_version", SOURCE_STAGE1_VERSION),
                              ("stage2_version", STAGE2_VERSION), ("metadata_enriched", True),
                              ("semantic_enriched", False)):
            if stage.get(key) != expected:
                reasons.append(f"stage.{key} must be {expected!r}")
        if "stage1" not in row.get("language", {}):
            reasons.append("missing language.stage1 snapshot")

        model = row.get("model", {})
        metadata_status = model.get("metadata_status", {})
        for field in ("parameter_count", "context_length"):
            expected_status = numeric_metadata_status(model.get(field))
            if metadata_status and metadata_status.get(field) != expected_status:
                reasons.append(
                    f"model.metadata_status.{field} must be {expected_status!r}"
                )
        readme = row.get("source", {}).get("readme", {})
        if readme.get("available"):
            path = readme.get("path")
            if not path or Path(path).parent != POOL_CONFIGS[source_pool]["readme_dir"]:
                reasons.append("README path is outside the source pool directory")
        if reasons:
            problems.append(f"{model_id}: {'; '.join(reasons)}")
    if problems:
        raise ValueError(f"[{source_pool}] Stage 2 validation failed:\n" + "\n".join(problems))
    return {"source_pool": source_pool, "rows": len(rows), "bad_count": 0}


def resume_matches(row, source_row, source_pool):
    """Reuse only this pool/version and the unchanged Stage 1 snapshot."""
    stage = row.get("stage", {})
    return (
        stage.get("stage2_version") == STAGE2_VERSION
        and stage.get("source_pool") == source_pool
        and stage.get("source_stage1_version") == source_row.get("stage", {}).get("stage1_version")
        and stage.get("metadata_enriched") is True
        and stage.get("semantic_enriched") is False
        and row.get("candidate") == source_row.get("candidate", {})
        and row.get("popularity", {}).get("stage1") == source_row.get("popularity", {})
        and row.get("family") == source_row.get("family", {})
        and row.get("stage1_quality") == source_row.get("quality", {})
        and row.get("language", {}).get("stage1") == source_row.get("language", {})
        and row.get("task") == {"primary": source_row.get("primary_task"),
                                "matched": source_row.get("matched_tasks", [])}
    )


def print_pool_stats(rows, source_pool, success, skipped, errors):
    config = POOL_CONFIGS[source_pool]
    print(f"[{source_pool}] FINISHED: rows={len(rows):,} enriched={success:,} skipped={skipped:,} errors={errors:,}")
    stats = {
        "README available": sum(row["source"]["readme"]["available"] is True for row in rows),
        "Config available": sum(row["source"]["config"]["available"] is True for row in rows),
        "Tokenizer config": sum(row["source"]["tokenizer_config"]["available"] is True for row in rows),
        "Parameter count": sum(row["model"]["parameter_count"] is not None for row in rows),
        "Context length": sum(row["model"]["context_length"] is not None for row in rows),
        "Quantized": sum(row["quantization"]["enabled"] is True for row in rows),
        "Korean verified": sum(row["language"]["korean"]["verified"] is True for row in rows),
        "Multilingual verified": sum(row["language"]["multilingual"]["verified"] is True for row in rows),
    }
    for label, count in stats.items():
        print(f"[{source_pool}] {label}: {count:,}")
    for key in ("output", "readme_dir"):
        print(f"[{source_pool}] {key}: {config[key]}")


def process_pool(source_pool):
    config = POOL_CONFIGS[source_pool]
    if not config["input"].is_file():
        raise FileNotFoundError(f"[{source_pool}] Missing input: {config['input']}")
    all_source_rows = load_jsonl(config["input"])
    source_by_id = {row["model_id"]: row for row in all_source_rows}
    source_rows = all_source_rows if TEST_LIMIT is None else all_source_rows[:TEST_LIMIT]
    config["readme_dir"].mkdir(parents=True, exist_ok=True)

    # Keep compatible prior results outside TEST_LIMIT, too: a small run must not
    # truncate a previously enriched larger corpus. Matching IDs are refreshed.
    # Retain prior rows until the user requests removal of out-of-source models.
    previous_by_id = {row["model_id"]: row for row in load_jsonl(config["output"])}
    results_by_id = {
        row["model_id"]: row for row in previous_by_id.values()
        if row.get("model_id") in source_by_id
        and resume_matches(row, source_by_id[row["model_id"]], source_pool)
    }
    success = skipped = errors = 0
    print(f"[{source_pool}] START: source={len(all_source_rows):,} selected={len(source_rows):,}", flush=True)

    def checkpoint():
        rows = list(results_by_id.values())
        validate_stage2_rows(rows, source_pool)
        # Validate current v7-source results; older retained rows keep provenance.
        # Stage 2 is authoritative for the current Stage 1 pool. Do not
        # carry rows that disappeared from the source pool into output.
        save_jsonl_atomic(list(results_by_id.values()), config["output"])

    try:
        for index, source_row in enumerate(source_rows, start=1):
            model_id = source_row["model_id"]
            prefix = f"[{source_pool}] {index}/{len(source_rows)}"
            if model_id in results_by_id:
                skipped += 1
                print(f"{prefix} SKIP {model_id}")
            else:
                print(f"{prefix} ENRICH {model_id}", flush=True)
                try:
                    row = enrich(source_row, source_pool)
                    validate_stage2_rows([row], source_pool)
                    results_by_id[model_id] = row
                    success += 1
                except Exception as error:
                    errors += 1
                    print(f"{prefix} ERROR {model_id}: {type(error).__name__}: {error}")
                time.sleep(REQUEST_SLEEP)
            if index % CHECKPOINT_EVERY == 0:
                checkpoint()
                print(f"[{source_pool}] checkpoint {index}/{len(source_rows)}", flush=True)
    except KeyboardInterrupt:
        print(f"[{source_pool}] Interrupted. Saving checkpoint...", flush=True)
        checkpoint()
        raise
    checkpoint()
    print_pool_stats(list(results_by_id.values()), source_pool, success, skipped, errors)
    if errors:
        raise RuntimeError(
            f"[{source_pool}] Stage 2 failed for {errors} model(s); "
            "refusing to continue with an incomplete pool"
        )


def validate_source_pools():
    """Reject stale sources before any API call or output modification."""
    state = json.loads((DATA_DIR / "hf_models_stage1_state.json").read_text())
    if state.get("stage1_version") != SOURCE_STAGE1_VERSION:
        raise ValueError("Stage 1 v7 collection and validation must finish first")
    if not state.get("completed_tasks") or any(
        stats.get("error") for stats in state.get("task_stats", {}).values()
    ):
        raise ValueError("Stage 1 collection is incomplete")
    for pool in SOURCE_POOLS:
        for row in load_jsonl(POOL_CONFIGS[pool]["input"]):
            candidate = row.get("candidate", {})
            downloads = row.get("popularity", {}).get("downloads", -1)
            valid_downloads = downloads >= 500 if pool == "core" else 80 <= downloads < 500
            if (row.get("stage", {}).get("stage1_version") != SOURCE_STAGE1_VERSION
                    or candidate.get("tier") != "A_verified"
                    or candidate.get("type") not in A_VERIFIED_TYPES
                    or not valid_downloads):
                raise ValueError(f"[{pool}] Invalid Stage 1 v7 source: {row.get('model_id')}")


def main():
    validate_source_pools()
    for source_pool in SOURCE_POOLS:
        process_pool(source_pool)


if __name__ == "__main__":
    main()
