from huggingface_hub import (
    HfApi,
    ModelCard,
    hf_hub_download,
)
import json
import time
import os
from typing import Any, Dict, List, Optional


# =========================================================
# CONFIG
# =========================================================

INPUT_PATH = "hf_models_korean_stage1.json"

OUTPUT_PATH = "hf_models_stage2_enriched.json"

CHECKPOINT_PATH = "hf_models_stage2_checkpoint.json"


# 처음 테스트
# 전체 실행 시 None
TEST_LIMIT = 100


REQUEST_SLEEP = 0.2

CHECKPOINT_EVERY = 50


# README 원문 전체 저장 여부
# 지금은 False 추천
STORE_FULL_README = False

MAX_README_CHARS = 200_000


api = HfApi()


# =========================================================
# JSON UTIL
# =========================================================

def load_json(path: str) -> List[Dict[str, Any]]:
    with open(
        path,
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


def save_json(
    data: List[Dict[str, Any]],
    path: str,
):
    tmp_path = path + ".tmp"

    with open(
        tmp_path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2,
        )

    os.replace(
        tmp_path,
        path,
    )


# =========================================================
# GENERAL UTIL
# =========================================================

def ensure_list(value):

    if value is None:
        return []

    if isinstance(value, list):
        return value

    if isinstance(value, tuple):
        return list(value)

    return [value]


def safe_get(
    obj,
    key,
    default=None,
):

    if obj is None:
        return default

    if isinstance(obj, dict):
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


def first_non_null(*values):

    for value in values:

        if value is not None:
            return value

    return None


# =========================================================
# DIRECT JSON DOWNLOAD
# =========================================================

def load_repo_json(
    model_id: str,
    filename: str,
):
    """
    config.json 등을 직접 다운로드해서 dict로 반환
    """

    try:

        path = hf_hub_download(
            repo_id=model_id,
            filename=filename,
            repo_type="model",
        )

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:

            return {
                "data": json.load(f),
                "error": None,
            }

    except Exception as e:

        return {
            "data": {},
            "error":
                f"{type(e).__name__}: {e}",
        }


# =========================================================
# MODEL CARD / README
# =========================================================

def load_model_card(
    model_id: str,
):

    try:

        card = ModelCard.load(
            model_id,
            ignore_metadata_errors=True,
        )

        metadata = {}

        try:

            if card.data:
                metadata = (
                    card.data.to_dict()
                )

        except Exception:
            metadata = {}

        text = (
            card.text
            if card.text
            else ""
        )

        if (
            len(text)
            > MAX_README_CHARS
        ):
            text = text[
                :MAX_README_CHARS
            ]

        return {
            "text": text,
            "metadata": metadata,
            "error": None,
        }

    except Exception as e:

        return {
            "text": None,
            "metadata": {},
            "error":
                f"{type(e).__name__}: {e}",
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


def collect_context_candidates(
    config: Dict[str, Any],
):

    values = []

    if not isinstance(
        config,
        dict,
    ):
        return values

    for key in CONTEXT_KEYS:

        value = config.get(
            key
        )

        if (
            isinstance(value, int)
            and value > 0
        ):
            values.append(
                value
            )

    # multimodal / nested config
    nested_keys = [
        "text_config",
        "language_config",
        "decoder",
    ]

    for nested_key in nested_keys:

        nested = config.get(
            nested_key
        )

        if isinstance(
            nested,
            dict,
        ):

            for key in CONTEXT_KEYS:

                value = nested.get(
                    key
                )

                if (
                    isinstance(value, int)
                    and value > 0
                ):
                    values.append(
                        value
                    )

    return values


def extract_context_length(
    config,
):

    candidates = (
        collect_context_candidates(
            config
        )
    )

    if not candidates:
        return None

    return max(
        candidates
    )


def extract_dtype(
    config,
):

    if not isinstance(
        config,
        dict,
    ):
        return None

    candidates = [
        config.get(
            "torch_dtype"
        ),
        config.get(
            "dtype"
        ),
    ]

    nested_keys = [
        "text_config",
        "language_config",
    ]

    for nested_key in nested_keys:

        nested = config.get(
            nested_key
        )

        if isinstance(
            nested,
            dict,
        ):

            candidates.extend([
                nested.get(
                    "torch_dtype"
                ),
                nested.get(
                    "dtype"
                ),
            ])

    for value in candidates:

        if value:
            return str(value)

    return None


def extract_architectures(
    config,
):

    if not isinstance(
        config,
        dict,
    ):
        return []

    architectures = config.get(
        "architectures"
    )

    return ensure_list(
        architectures
    )


def extract_model_type(
    config,
):

    if not isinstance(
        config,
        dict,
    ):
        return None

    return config.get(
        "model_type"
    )


# =========================================================
# PARAMETER COUNT
# =========================================================

def extract_parameter_count(
    info
):

    safetensors = getattr(
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

    if parameters is None:
        return None

    if isinstance(
        parameters,
        dict,
    ):

        total = 0

        for value in (
            parameters.values()
        ):

            if isinstance(
                value,
                int,
            ):
                total += value

        if total > 0:
            return total

    if isinstance(
        parameters,
        int,
    ):
        return parameters

    return None


# =========================================================
# ARTIFACT
# =========================================================

def detect_artifacts(
    info,
):

    siblings = (
        getattr(
            info,
            "siblings",
            None,
        )
        or []
    )

    filenames = []

    for item in siblings:

        filename = safe_get(
            item,
            "rfilename",
            None,
        )

        if filename:
            filenames.append(
                filename.lower()
            )

    return {

        "safetensors": any(
            filename.endswith(
                ".safetensors"
            )
            for filename
            in filenames
        ),

        "gguf": any(
            filename.endswith(
                ".gguf"
            )
            for filename
            in filenames
        ),
    }


# =========================================================
# QUANTIZATION
# =========================================================

def detect_quantization(
    config,
    tags,
    model_id,
):

    method = None
    bits = None
    evidence = []

    # -----------------------------------------------------
    # config
    # -----------------------------------------------------

    if isinstance(
        config,
        dict,
    ):

        qconfig = config.get(
            "quantization_config"
        )

        if isinstance(
            qconfig,
            dict,
        ):

            method = first_non_null(
                qconfig.get(
                    "quant_method"
                ),
                qconfig.get(
                    "method"
                ),
            )

            if (
                qconfig.get(
                    "bits"
                )
                is not None
            ):

                bits = qconfig.get(
                    "bits"
                )

            evidence.append(
                "config.quantization_config"
            )

    # -----------------------------------------------------
    # names / tags
    # -----------------------------------------------------

    joined = " ".join(
        [model_id.lower()]
        +
        [
            str(tag).lower()
            for tag in tags
        ]
    )

    patterns = [
        ("awq", 4),
        ("gptq", None),
        ("gguf", None),
        ("bnb-4bit", 4),
        ("4-bit", 4),
        ("4bit", 4),
        ("8-bit", 8),
        ("8bit", 8),
        ("int4", 4),
        ("int8", 8),
        ("fp4", 4),
        ("nvfp4", 4),
        ("fp8", 8),
        ("mlx-4bit", 4),
        ("mlx-5bit", 5),
        ("mlx-6bit", 6),
        ("mlx-8bit", 8),
    ]

    for (
        name,
        detected_bits,
    ) in patterns:

        if name in joined:

            if method is None:
                method = name

            if (
                bits is None
                and detected_bits
                is not None
            ):
                bits = detected_bits

            evidence.append(
                f"name_or_tag:{name}"
            )

    quantized = bool(
        method
        or bits
        or any(
            "quantized"
            in str(tag).lower()
            for tag in tags
        )
    )

    return {
        "quantization":
            quantized,

        "quantization_method":
            method,

        "quantization_bits":
            bits,

        "quantization_evidence":
            evidence,
    }


# =========================================================
# WEIGHT MEMORY
# =========================================================

def estimate_weight_memory_gb(
    parameter_count:
        Optional[int],

    bits: int,
):

    if not parameter_count:
        return None

    bytes_per_param = (
        bits / 8
    )

    total_bytes = (
        parameter_count
        * bytes_per_param
    )

    gib = (
        total_bytes
        / (1024 ** 3)
    )

    return round(
        gib,
        2,
    )


# =========================================================
# CARD METADATA MERGE
# =========================================================

def merge_model_card_metadata(
    row,
    metadata,
):

    if not isinstance(
        metadata,
        dict,
    ):
        return

    languages = ensure_list(
        metadata.get(
            "language"
        )
    )

    if languages:
        row["languages"] = (
            languages
        )

    license_value = (
        metadata.get(
            "license"
        )
    )

    if license_value:
        row["license"] = (
            license_value
        )

    datasets = ensure_list(
        metadata.get(
            "datasets"
        )
    )

    if datasets:
        row["datasets"] = (
            datasets
        )

    metrics = ensure_list(
        metadata.get(
            "metrics"
        )
    )

    if metrics:
        row["metrics"] = (
            metrics
        )

    base_model = (
        metadata.get(
            "base_model"
        )
    )

    if base_model:
        row["base_model"] = (
            base_model
        )

    library_name = (
        metadata.get(
            "library_name"
        )
    )

    if library_name:
        row[
            "library_name"
        ] = library_name

    pipeline_tag = (
        metadata.get(
            "pipeline_tag"
        )
    )

    if pipeline_tag:
        row[
            "primary_pipeline_tag"
        ] = pipeline_tag


# =========================================================
# KOREAN / MULTILINGUAL VERIFICATION
# =========================================================

def verify_language_support(
    stage1_row,
    card_metadata,
    readme_text,
):

    evidence = []

    languages = ensure_list(
        card_metadata.get(
            "language"
        )
        if isinstance(
            card_metadata,
            dict,
        )
        else []
    )

    normalized_languages = {
        str(lang).lower()
        for lang in languages
    }

    explicit_korean = {
        "ko",
        "kor",
        "korean",
        "ko-kr",
    }

    # -----------------------------------------------------
    # 1. explicit Korean
    # -----------------------------------------------------

    if (
        normalized_languages
        &
        explicit_korean
    ):

        return {
            "korean_verified": True,
            "multilingual_verified": True,
            "language_confidence": "high",
            "language_evidence": [
                "model_card.language:ko"
            ],
        }

    # -----------------------------------------------------
    # 2. explicitly multilingual
    # -----------------------------------------------------

    if (
        "multilingual"
        in normalized_languages
    ):

        evidence.append(
            "model_card.language:multilingual"
        )

        multilingual = True

    else:

        multilingual = False

    # -----------------------------------------------------
    # 3. README
    # -----------------------------------------------------

    text = (
        readme_text
        or ""
    ).lower()

    korean_terms = [
        "korean",
        "한국어",
        "ko-kr",
    ]

    for term in korean_terms:

        if term.lower() in text:

            evidence.append(
                f"readme:{term}"
            )

    if any(
        item.startswith(
            "readme:"
        )
        for item
        in evidence
    ):

        return {
            "korean_verified": True,
            "multilingual_verified":
                multilingual
                or True,
            "language_confidence":
                "medium",
            "language_evidence":
                evidence,
        }

    # -----------------------------------------------------
    # 4. Stage 1 explicit
    # -----------------------------------------------------

    if (
        stage1_row.get(
            "korean_support_level"
        )
        == "explicit"
    ):

        return {
            "korean_verified": True,
            "multilingual_verified":
                multilingual,
            "language_confidence":
                "medium",
            "language_evidence":
                stage1_row.get(
                    "korean_evidence",
                    []
                ),
        }

    # -----------------------------------------------------
    # 5. Stage 1 multilingual candidate
    # -----------------------------------------------------

    if (
        stage1_row.get(
            "korean_support_level"
        )
        in {
            "multilingual",
            "family_heuristic",
        }
    ):

        return {
            "korean_verified": None,
            "multilingual_verified": True,
            "language_confidence":
                "candidate",
            "language_evidence":
                evidence
                + stage1_row.get(
                    "korean_evidence",
                    []
                ),
        }

    return {
        "korean_verified": None,
        "multilingual_verified":
            multilingual,
        "language_confidence":
            "unknown",
        "language_evidence":
            evidence,
    }


# =========================================================
# SINGLE MODEL
# =========================================================

def enrich_model(
    row,
):

    model_id = row[
        "model_id"
    ]

    row[
        "metadata_error"
    ] = None

    try:

        # =================================================
        # 1. Model Info
        # =================================================

        info = api.model_info(
            model_id,
            files_metadata=True,
        )

        # =================================================
        # 2. config.json 직접 다운로드
        # =================================================

        config_result = (
            load_repo_json(
                model_id,
                "config.json",
            )
        )

        config = (
            config_result[
                "data"
            ]
        )

        row[
            "config_error"
        ] = config_result[
            "error"
        ]

        # -------------------------------------------------
        # config metadata
        # -------------------------------------------------

        row[
            "model_type"
        ] = (
            extract_model_type(
                config
            )
        )

        row[
            "architectures"
        ] = (
            extract_architectures(
                config
            )
        )

        row[
            "context_length"
        ] = (
            extract_context_length(
                config
            )
        )

        row[
            "dtype"
        ] = (
            extract_dtype(
                config
            )
        )

        # =================================================
        # 3. Parameter Count
        # =================================================

        parameter_count = (
            extract_parameter_count(
                info
            )
        )

        row[
            "parameter_count"
        ] = parameter_count

        if parameter_count:

            row[
                "parameter_count_billion"
            ] = round(
                parameter_count
                / 1e9,
                3,
            )

        else:

            row[
                "parameter_count_billion"
            ] = None

        # =================================================
        # 4. Artifact
        # =================================================

        artifacts = (
            detect_artifacts(
                info
            )
        )

        row[
            "safetensors"
        ] = (
            artifacts[
                "safetensors"
            ]
        )

        row[
            "gguf"
        ] = (
            artifacts[
                "gguf"
            ]
        )

        # =================================================
        # 5. Quantization
        # =================================================

        quant = (
            detect_quantization(
                config=config,
                tags=row.get(
                    "tags",
                    []
                ),
                model_id=model_id,
            )
        )

        row.update(
            quant
        )

        # =================================================
        # 6. Model Card / README
        # =================================================

        card = (
            load_model_card(
                model_id
            )
        )

        card_metadata = (
            card.get(
                "metadata",
                {},
            )
        )

        readme_text = (
            card.get(
                "text"
            )
        )

        row[
            "readme_available"
        ] = bool(
            readme_text
        )

        if STORE_FULL_README:

            row[
                "readme"
            ] = readme_text

        else:

            row[
                "readme"
            ] = None

        row[
            "model_card_metadata"
        ] = card_metadata

        row[
            "model_card_error"
        ] = card.get(
            "error"
        )

        merge_model_card_metadata(
            row,
            card_metadata,
        )

        # =================================================
        # 7. Language Verification
        # =================================================

        language_result = (
            verify_language_support(
                stage1_row=row,
                card_metadata=
                    card_metadata,
                readme_text=
                    readme_text,
            )
        )

        row.update(
            language_result
        )

        # =================================================
        # 8. Weight Memory
        # =================================================

        row[
            "estimated_weight_memory_fp32_gb"
        ] = (
            estimate_weight_memory_gb(
                parameter_count,
                32,
            )
        )

        row[
            "estimated_weight_memory_fp16_gb"
        ] = (
            estimate_weight_memory_gb(
                parameter_count,
                16,
            )
        )

        row[
            "estimated_weight_memory_int8_gb"
        ] = (
            estimate_weight_memory_gb(
                parameter_count,
                8,
            )
        )

        row[
            "estimated_weight_memory_int4_gb"
        ] = (
            estimate_weight_memory_gb(
                parameter_count,
                4,
            )
        )

        # =================================================
        # 9. Status
        # =================================================

        row[
            "metadata_enriched"
        ] = True

        return row

    except Exception as e:

        row[
            "metadata_enriched"
        ] = False

        row[
            "metadata_error"
        ] = (
            f"{type(e).__name__}: {e}"
        )

        return row


# =========================================================
# MAIN
# =========================================================

def main():

    models = load_json(
        INPUT_PATH
    )

    print(
        f"Loaded Stage 1 models: "
        f"{len(models):,}"
    )

    # -----------------------------------------------------
    # Test
    # -----------------------------------------------------

    if TEST_LIMIT is not None:

        models = models[
            :TEST_LIMIT
        ]

        print(
            f"TEST MODE: "
            f"{len(models):,} models"
        )

    # -----------------------------------------------------
    # Checkpoint
    # -----------------------------------------------------

    if os.path.exists(
        CHECKPOINT_PATH
    ):

        checkpoint_models = (
            load_json(
                CHECKPOINT_PATH
            )
        )

        checkpoint_by_id = {
            m["model_id"]: m
            for m
            in checkpoint_models
        }

        for index, model in enumerate(
            models
        ):

            model_id = (
                model[
                    "model_id"
                ]
            )

            if (
                model_id
                in checkpoint_by_id
            ):

                models[
                    index
                ] = (
                    checkpoint_by_id[
                        model_id
                    ]
                )

    total = len(
        models
    )

    error_count = 0

    # =====================================================
    # Process
    # =====================================================

    for index, model in enumerate(
        models,
        start=1,
    ):

        model_id = model[
            "model_id"
        ]

        if model.get(
            "metadata_enriched"
        ):

            print(
                f"[{index}/{total}] "
                f"SKIP {model_id}"
            )

            continue

        print(
            f"[{index}/{total}] "
            f"ENRICH {model_id}",
            flush=True,
        )

        result = (
            enrich_model(
                model
            )
        )

        models[
            index - 1
        ] = result

        if not result.get(
            "metadata_enriched"
        ):

            error_count += 1

            print(
                f"  ERROR: "
                f"{result.get('metadata_error')}"
            )

        # -------------------------------------------------
        # checkpoint
        # -------------------------------------------------

        if (
            index
            % CHECKPOINT_EVERY
            == 0
        ):

            save_json(
                models,
                CHECKPOINT_PATH,
            )

            print(
                f"  checkpoint saved "
                f"({index}/{total})"
            )

        time.sleep(
            REQUEST_SLEEP
        )

    # =====================================================
    # SAVE
    # =====================================================

    save_json(
        models,
        OUTPUT_PATH,
    )

    save_json(
        models,
        CHECKPOINT_PATH,
    )

    # =====================================================
    # Stats
    # =====================================================

    enriched = sum(
        model.get(
            "metadata_enriched"
        )
        is True
        for model
        in models
    )

    readme_count = sum(
        model.get(
            "readme_available"
        )
        is True
        for model
        in models
    )

    parameter_count = sum(
        model.get(
            "parameter_count"
        )
        is not None
        for model
        in models
    )

    context_count = sum(
        model.get(
            "context_length"
        )
        is not None
        for model
        in models
    )

    dtype_count = sum(
        model.get(
            "dtype"
        )
        is not None
        for model
        in models
    )

    korean_verified = sum(
        model.get(
            "korean_verified"
        )
        is True
        for model
        in models
    )

    multilingual_verified = sum(
        model.get(
            "multilingual_verified"
        )
        is True
        for model
        in models
    )

    korean_unknown = sum(
        model.get(
            "korean_verified"
        )
        is None
        for model
        in models
    )

    print()
    print("=" * 80)
    print(
        "STAGE 2 FINISHED"
    )
    print("=" * 80)

    print(
        f"Models                  : "
        f"{len(models):,}"
    )

    print(
        f"Metadata enriched       : "
        f"{enriched:,}"
    )

    print(
        f"Errors                   : "
        f"{error_count:,}"
    )

    print(
        f"README available         : "
        f"{readme_count:,}"
    )

    print(
        f"Parameter count          : "
        f"{parameter_count:,}"
    )

    print(
        f"Context length           : "
        f"{context_count:,}"
    )

    print(
        f"Dtype                     : "
        f"{dtype_count:,}"
    )

    print(
        f"Korean verified          : "
        f"{korean_verified:,}"
    )

    print(
        f"Multilingual candidate   : "
        f"{multilingual_verified:,}"
    )

    print(
        f"Korean unknown           : "
        f"{korean_unknown:,}"
    )

    print()
    print(
        f"Saved -> "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()