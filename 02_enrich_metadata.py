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

# 지금은 core만 처리.
#
# 나중에:
# SOURCE_POOL = "low"
#
SOURCE_POOL = "core"


INPUT_PATHS = {
    "core":
        DATA_DIR
        / "hf_models_stage1_core.jsonl",

    "low":
        DATA_DIR
        / "hf_models_stage1_low_popularity.jsonl",
}


OUTPUT_PATHS = {
    "core":
        DATA_DIR
        / "hf_models_stage2_core.jsonl",

    "low":
        DATA_DIR
        / "hf_models_stage2_low.jsonl",
}


ERROR_PATHS = {
    "core":
        DATA_DIR
        / "hf_models_stage2_core_errors.jsonl",

    "low":
        DATA_DIR
        / "hf_models_stage2_low_errors.jsonl",
}


INPUT_PATH = (
    INPUT_PATHS[
        SOURCE_POOL
    ]
)

OUTPUT_PATH = (
    OUTPUT_PATHS[
        SOURCE_POOL
    ]
)

ERROR_PATH = (
    ERROR_PATHS[
        SOURCE_POOL
    ]
)


README_DIR = (
    DATA_DIR
    / "readmes"
)


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


STAGE2_VERSION = 2


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


def append_error(
    row,
):

    ERROR_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        ERROR_PATH,
        "a",
        encoding="utf-8",
    ) as f:

        f.write(
            json.dumps(
                row,
                ensure_ascii=False,
            )
        )

        f.write("\n")


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


        README_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )


        output_path = (
            README_DIR
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


def normalize_language_values(
    values,
):

    output = set()


    for value in (
        ensure_list(
            values
        )
    ):

        if value is None:
            continue


        value = (
            str(value)
            .strip()
            .lower()
        )


        if value:
            output.add(
                value
            )


    return output


def verify_languages(
    stage1_row,
    card_metadata,
    readme_text,
):

    stage1_candidate = (
        stage1_row.get(
            "candidate",
            {},
        )
    )


    stage1_language = (
        stage1_row.get(
            "language",
            {},
        )
    )


    stage1_languages = (
        normalize_language_values(
            stage1_language.get(
                "languages",
                [],
            )
        )
    )


    card_languages = (
        normalize_language_values(
            card_metadata.get(
                "language",
                [],
            )
        )
    )


    languages = (
        stage1_languages
        |
        card_languages
    )


    candidate_type = (
        stage1_candidate.get(
            "type"
        )
    )


    readme_lower = (
        readme_text
        or ""
    ).lower()


    # =====================================================
    # Korean
    # =====================================================

    korean = None

    korean_confidence = (
        "unknown"
    )

    korean_evidence = []


    if (
        languages
        &
        KOREAN_CODES
    ):

        korean = True

        korean_confidence = (
            "high"
        )

        korean_evidence.append(
            "metadata.language:korean"
        )


    elif (
        candidate_type
        ==
        "korean_explicit"
    ):

        korean = True

        korean_confidence = (
            "high"
        )

        korean_evidence.append(
            "stage1:korean_explicit"
        )


    elif any(
        phrase
        in readme_lower

        for phrase
        in [
            "supports korean",
            "korean language",
            "korean support",
            "한국어 지원",
            "supports ko-kr",
        ]
    ):

        korean = True

        korean_confidence = (
            "medium"
        )

        korean_evidence.append(
            "readme:korean_explicit_phrase"
        )


    # =====================================================
    # Multilingual
    # =====================================================

    multilingual = None

    multilingual_confidence = (
        "unknown"
    )

    multilingual_evidence = []


    # Stage 1 explicit multilingual
    if candidate_type in {
        "multilingual_explicit",
        "multilingual_language_list",
    }:

        multilingual = True

        multilingual_confidence = (
            "high"
        )

        multilingual_evidence.append(
            f"stage1:{candidate_type}"
        )


    # Model card language list에서 3개 이상
    elif len(
        card_languages
    ) >= 3:

        multilingual = True

        multilingual_confidence = (
            "high"
        )

        multilingual_evidence.append(
            "model_card:3plus_languages"
        )


    elif (
        card_languages
        &
        MULTILINGUAL_MARKERS
    ):

        multilingual = True

        multilingual_confidence = (
            "high"
        )

        multilingual_evidence.append(
            "model_card:multilingual"
        )


    # =====================================================
    # Bilingual
    # =====================================================

    bilingual = (
        candidate_type
        ==
        "bilingual_language_list"
    )


    return {
        "declared_languages":
            sorted(
                languages
            ),

        "language_count":
            len(
                languages
            ),

        "korean": {
            "verified":
                korean,

            "confidence":
                korean_confidence,

            "evidence":
                korean_evidence,
        },

        "multilingual": {
            "verified":
                multilingual,

            "confidence":
                multilingual_confidence,

            "evidence":
                multilingual_evidence,
        },

        "bilingual": {
            "verified":
                bilingual,

            "evidence":
                (
                    [
                        "stage1:bilingual_language_list"
                    ]
                    if bilingual
                    else []
                ),
        },
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
            model_id
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
                SOURCE_POOL,

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

def main():

    README_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


    source_rows = (
        load_jsonl(
            INPUT_PATH
        )
    )


    original_source_count = (
        len(
            source_rows
        )
    )


    if TEST_LIMIT is not None:

        source_rows = (
            source_rows[
                :TEST_LIMIT
            ]
        )


    print(
        f"Source pool          : "
        f"{SOURCE_POOL}"
    )

    print(
        f"Stage 1 total        : "
        f"{original_source_count:,}"
    )

    print(
        f"Processing this run  : "
        f"{len(source_rows):,}"
    )


    # =====================================================
    # RESUME
    # =====================================================

    existing_rows = (
        load_jsonl(
            OUTPUT_PATH
        )
    )


    existing_by_id = {
        row[
            "model_id"
        ]:
            row

        for row
        in existing_rows

        if (
            row.get(
                "stage",
                {},
            ).get(
                "stage2_version"
            )
            ==
            STAGE2_VERSION
        )
    }


    results = []

    success = 0
    skipped = 0
    errors = 0


    try:

        for (
            index,
            source_row,
        ) in enumerate(
            source_rows,
            start=1,
        ):

            model_id = (
                source_row[
                    "model_id"
                ]
            )


            # =============================================
            # RESUME
            # =============================================

            if (
                model_id
                in existing_by_id
            ):

                print(
                    f"[{index}/{len(source_rows)}] "
                    f"SKIP "
                    f"{model_id}"
                )


                results.append(
                    existing_by_id[
                        model_id
                    ]
                )


                skipped += 1

                continue


            # =============================================
            # ENRICH
            # =============================================

            print(
                f"[{index}/{len(source_rows)}] "
                f"ENRICH "
                f"{model_id}",
                flush=True,
            )


            try:

                row = enrich(
                    source_row
                )


                results.append(
                    row
                )


                success += 1


            except Exception as e:

                errors += 1


                error_row = {
                    "model_id":
                        model_id,

                    "error_type":
                        type(e).__name__,

                    "error":
                        str(e),

                    "source_pool":
                        SOURCE_POOL,

                    "stage2_version":
                        STAGE2_VERSION,

                    "created_at":
                        utc_now(),
                }


                append_error(
                    error_row
                )


                print(
                    f"  ERROR "
                    f"{type(e).__name__}: "
                    f"{e}"
                )


            # =============================================
            # CHECKPOINT
            # =============================================

            if (
                index
                % CHECKPOINT_EVERY
                == 0
            ):

                save_jsonl_atomic(
                    results,
                    OUTPUT_PATH,
                )


                print(
                    f"  checkpoint "
                    f"{index}/"
                    f"{len(source_rows)}"
                )


            time.sleep(
                REQUEST_SLEEP
            )


    except KeyboardInterrupt:

        print()

        print(
            "Interrupted. "
            "Saving current results..."
        )


        save_jsonl_atomic(
            results,
            OUTPUT_PATH,
        )


        raise


    # =====================================================
    # FINAL SAVE
    # =====================================================

    save_jsonl_atomic(
        results,
        OUTPUT_PATH,
    )


    # =====================================================
    # STATS
    # =====================================================

    readmes = sum(
        (
            row.get(
                "source",
                {},
            ).get(
                "readme",
                {},
            ).get(
                "available"
            )
            is True
        )
        for row in results
    )


    parameters = sum(
        (
            row.get(
                "model",
                {},
            ).get(
                "parameter_count"
            )
            is not None
        )
        for row in results
    )


    context_lengths = sum(
        (
            row.get(
                "model",
                {},
            ).get(
                "context_length"
            )
            is not None
        )
        for row in results
    )


    configs = sum(
        (
            row.get(
                "source",
                {},
            ).get(
                "config",
                {},
            ).get(
                "available"
            )
            is True
        )
        for row in results
    )


    tokenizer_configs = sum(
        (
            row.get(
                "source",
                {},
            ).get(
                "tokenizer_config",
                {},
            ).get(
                "available"
            )
            is True
        )
        for row in results
    )


    korean = sum(
        (
            row.get(
                "language",
                {},
            ).get(
                "korean",
                {},
            ).get(
                "verified"
            )
            is True
        )
        for row in results
    )


    multilingual = sum(
        (
            row.get(
                "language",
                {},
            ).get(
                "multilingual",
                {},
            ).get(
                "verified"
            )
            is True
        )
        for row in results
    )


    quantized = sum(
        (
            row.get(
                "quantization",
                {},
            ).get(
                "enabled"
            )
            is True
        )
        for row in results
    )


    print()
    print("=" * 80)

    print(
        "STAGE 2 FINISHED"
    )

    print("=" * 80)


    print(
        f"Source pool           : "
        f"{SOURCE_POOL}"
    )

    print(
        f"Models                : "
        f"{len(results):,}"
    )

    print(
        f"Enriched this run     : "
        f"{success:,}"
    )

    print(
        f"Skipped               : "
        f"{skipped:,}"
    )

    print(
        f"Errors                : "
        f"{errors:,}"
    )


    print()


    print(
        f"README available      : "
        f"{readmes:,}"
    )

    print(
        f"Config available      : "
        f"{configs:,}"
    )

    print(
        f"Tokenizer config      : "
        f"{tokenizer_configs:,}"
    )

    print(
        f"Parameter count       : "
        f"{parameters:,}"
    )

    print(
        f"Context length        : "
        f"{context_lengths:,}"
    )

    print(
        f"Quantized             : "
        f"{quantized:,}"
    )

    print(
        f"Korean verified       : "
        f"{korean:,}"
    )

    print(
        f"Multilingual verified : "
        f"{multilingual:,}"
    )


    print()

    print(
        f"Metadata -> "
        f"{OUTPUT_PATH}"
    )

    print(
        f"Errors   -> "
        f"{ERROR_PATH}"
    )

    print(
        f"README   -> "
        f"{README_DIR}"
    )


if __name__ == "__main__":
    main()