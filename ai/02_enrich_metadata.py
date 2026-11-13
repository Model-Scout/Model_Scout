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


AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"

# 데이터 계약(ai/contract/)의 resolver. 사실마다 출처·신뢰도를 기록한다.
import sys as _sys

if str(AI_DIR) not in _sys.path:
    _sys.path.insert(0, str(AI_DIR))
from resolvers import resolve as contract_resolve


# =========================================================
# SOURCE POOL
# =========================================================

SOURCE_POOLS = ["core", "low_popularity"]

POOL_CONFIGS = {
    pool: {
        "input": DATA_DIR / f"hf_models_stage1_{pool}.jsonl",
        "output": DATA_DIR / f"hf_models_stage2_{pool}.jsonl",
        # 계약 레코드(출처·신뢰도)는 별도 파일에 둔다. 한 건이 약 9KB라
        # stage2 본문에 넣으면 17MB → 52MB로 3배가 된다. 03/04/05/08은 값만
        # 읽으므로 본문이 커질 이유가 없다. 품질 게이트와 Stage 4의 필터
        # 필드 생성이 이 파일을 읽는다.
        "contract_output": DATA_DIR / f"hf_models_stage2_contract_{pool}.jsonl",
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


# 7: 데이터 계약 필드(contract) 추가. gated·revision·artifact 용량·GGUF 파라미터가
#    새로 들어오므로 기존 Stage 2 파일은 재적재해야 한다.
STAGE2_VERSION = 7
SOURCE_STAGE1_VERSION = 7
A_VERIFIED_TYPES = {"korean_explicit", "korean_translation_pair", "korean_name_strong"}


_RUN_ID = None


def pipeline_run_id():
    """이 프로세스가 만든 레코드를 한 묶음으로 묶는 ID.

    골든셋 판정과 검색 평가가 같은 run의 데이터를 쓰는지 확인하는 기준이다.
    환경변수로 넘기면 08_sync_supabase가 자기 run ID를 물려줄 수 있다.
    """
    global _RUN_ID
    if _RUN_ID is None:
        _RUN_ID = os.getenv("MODEL_SCOUT_RUN_ID") or f"stage2-{utc_now()}"
    return _RUN_ID


# ModelInfo 객체 → resolver가 읽는 평범한 dict.
#
# resolver는 HF REST 응답과 같은 모양을 받는다. 그래야 ai/backfill/raw/ 에 받아
# 둔 실제 응답 1,804건을 그대로 테스트 입력으로 쓸 수 있다. 객체를 직접 읽게
# 만들면 테스트에 HF 호출이 필요해진다.
def model_info_as_dict(info):
    """``load_model_info``가 돌려준 ModelInfo를 REST 응답 모양으로 눕힌다."""
    if info is None:
        return {}
    if isinstance(info, dict):
        return info

    siblings = []
    for sibling in getattr(info, "siblings", None) or []:
        siblings.append({
            "rfilename": getattr(sibling, "rfilename", None),
            "size": getattr(sibling, "size", None),
            "blobId": getattr(sibling, "blob_id", None),
        })

    card_data = getattr(info, "card_data", None)
    if card_data is not None and not isinstance(card_data, dict):
        card_data = getattr(card_data, "to_dict", lambda: None)() or dict(card_data)

    safetensors = getattr(info, "safetensors", None)
    if safetensors is not None and not isinstance(safetensors, dict):
        safetensors = {
            "total": getattr(safetensors, "total", None),
            "parameters": getattr(safetensors, "parameters", None),
        }

    last_modified = getattr(info, "last_modified", None)
    return {
        "id": getattr(info, "id", None) or getattr(info, "modelId", None),
        "modelId": getattr(info, "modelId", None),
        "author": getattr(info, "author", None),
        "sha": getattr(info, "sha", None),
        "lastModified": safe_iso(last_modified),
        # gated는 False / "auto" / "manual" 세 값을 갖는다. 없으면 None이고,
        # None은 "공개"가 아니라 "모름"이다.
        "gated": getattr(info, "gated", None),
        "private": getattr(info, "private", None),
        "disabled": getattr(info, "disabled", None),
        "downloads": getattr(info, "downloads", None),
        "likes": getattr(info, "likes", None),
        "pipeline_tag": getattr(info, "pipeline_tag", None),
        "library_name": getattr(info, "library_name", None),
        "tags": list(getattr(info, "tags", None) or []),
        "cardData": card_data or {},
        "config": getattr(info, "config", None) or {},
        "safetensors": safetensors or {},
        "gguf": getattr(info, "gguf", None) or {},
        "siblings": siblings,
        "usedStorage": getattr(info, "used_storage", None),
        "model-index": getattr(info, "model_index", None),
        "base_models": list(getattr(info, "base_models", None) or []),
    }


def adopt_contract_values(row, record):
    """계약 resolver가 새로 알아낸 값을 기존 키 자리에 되먹인다.

    **기존 값을 덮지 않는다.** 비어 있던 자리만 채운다. 기존 값은 safetensors나
    config.json에서 나온 것이고 resolver의 출처와 등급이 같으므로, 교체해서
    얻을 것이 없고 재적재 diff만 커진다.

    새로 생기는 자리(artifacts 용량, gated 등)는 ``contract``에만 있고 Stage 4가
    거기서 읽는다.
    """
    technical = record.get("technical") or {}
    model = row.setdefault("model", {})

    if not isinstance(model.get("parameter_count"), int):
        total = technical.get("parameter_count_total")
        if isinstance(total, int):
            model["parameter_count"] = total
            model["parameter_count_billion"] = round(total / 1_000_000_000, 3)
            model.setdefault("metadata_status", {})["parameter_count"] = "known"
    if not isinstance(model.get("context_length"), int):
        context = technical.get("context_length")
        if isinstance(context, int):
            model["context_length"] = context
            model.setdefault("metadata_status", {})["context_length"] = "known"
    if not model.get("architectures") and technical.get("architecture"):
        model["architectures"] = list(technical["architecture"])
    if not model.get("type") and technical.get("model_type"):
        model["type"] = technical["model_type"]
    if not model.get("dtype") and technical.get("dtype"):
        model["dtype"] = technical["dtype"]

    # 가중치 메모리 추정. 파라미터 수가 새로 생기면 여기도 따라 채워져야 한다 —
    # 그러지 않으면 "8GB에서 돌아가는 모델" 질의가 여전히 그 모델을 못 찾는다.
    hardware = row.setdefault("hardware", {})
    weights = hardware.setdefault("weights_only", {})
    estimate = ((record.get("deployment") or {}).get("vram_estimate") or {}).get("weights_only") or {}
    for key in ("fp16_gib", "int8_gib", "int4_gib", "detected_quantization_gib"):
        if weights.get(key) is None and estimate.get(key) is not None:
            weights[key] = estimate[key]

    return row


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
                output_path.relative_to(AI_DIR).as_posix()
                if output_path.is_relative_to(AI_DIR)
                else str(output_path),
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


# A fine-tune can inherit its base model's language tags (VNJPTranslate lists kor from
# Qwen2.5 but is trained for Vietnamese/Japanese). When the README never mentions Korean
# and its name or title names another target language, the Korean tag is not evidence.
README_FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
KOREAN_MENTION_RE = re.compile(
    r"korean|한국어|한국|(?<![a-z])ko(?:-kr)?(?![a-z])|(?<![a-z])kor(?![a-z])|[가-힣]{2,}", re.I)
TARGET_LANGUAGE_RE = re.compile(
    r"(?<![a-z])(vietnamese|japanese|chinese|mandarin|cantonese|thai|indonesian|malay|tagalog|filipino|"
    r"hindi|urdu|bengali|tamil|telugu|marathi|punjabi|nepali|sinhala|arabic|persian|farsi|turkish|hebrew|"
    r"kazakh|uzbek|mongolian|russian|ukrainian|polish|czech|german|french|spanish|portuguese|italian|dutch|"
    r"flemish|swedish|norwegian|danish|finnish|greek|romanian|hungarian|hausa|yoruba|igbo|swahili|amharic|"
    r"zulu|afrikaans|pakistani|brazilian|catalan|basque|serbian|croatian|bulgarian|khmer|burmese)(?![a-z])",
    re.I)


def non_korean_targets(model_id, readme_text):
    """Languages a model's name or README title targets, when nothing in it mentions Korean."""
    name = model_id.split("/")[-1]
    body = README_FRONTMATTER_RE.sub("", readme_text or "", count=1)
    if KOREAN_MENTION_RE.search(body) or KOREAN_MENTION_RE.search(name):
        return []
    title = next((line for line in body.splitlines() if line.startswith("# ")), "")
    return sorted({m.casefold() for m in TARGET_LANGUAGE_RE.findall(f"{re.sub(r'[-_]', ' ', name)} {title}")})


def _saved_readme(model_id):
    for pool in SOURCE_POOLS:
        path = DATA_DIR / "readmes" / pool / f"{model_id.replace('/', '__')}.md"
        if path.is_file():
            return path.read_text(encoding="utf-8", errors="ignore")
    return None


def language_exclusions(rows):
    """model_id -> reason for rows whose own or base model's README targets another language.

    Runs on saved READMEs, so resumed rows are re-checked without new Hub calls.
    """
    excluded = {}
    for row in rows:
        model_id = row["model_id"]
        for source in [model_id, *(row.get("base_models") or [])]:
            readme = _saved_readme(source)
            targets = non_korean_targets(source, readme) if readme is not None else []
            if targets:
                via = "" if source == model_id else f" (base {source})"
                excluded[model_id] = f"README targets {', '.join(targets)} and never mentions Korean{via}"
                break
    return excluded


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

    row = {
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

            # Hub revision this row was built from (Stage 1's list_models values).
            # resume_matches reuses the row only while it is still current.
            **source_revision(stage1_row),
        },
    }

    # =====================================================
    # DATA CONTRACT  (ai/contract/)
    # =====================================================
    #
    # 기존 키는 그대로 둔다. 03/04/05/08과 골든셋 도구가 이 모양을 읽고 있다.
    # 계약 레코드는 `contract` 아래에 덧붙이고, 새로 알아낸 값만 기존 자리에
    # 되먹인다.
    #
    # resolver 가 읽는 것은 지금까지 받아 놓고 버리던 응답이다 —
    # gated, sha, lastModified, siblings[].size, gguf.{total,architecture,
    # context_length}, safetensors.parameters. load_model_info() 가 이미
    # files_metadata=True 로 호출하므로 추가 API 호출이 없다.

    raw = model_info_as_dict(info)
    record = contract_resolve.build(
        raw,
        config_json=config,
        stage1=stage1_row,
        stage2=row,
        readme_text=readme_text or "",
        run_id=pipeline_run_id(),
        source_pool=source_pool,
    )
    row["contract"] = record
    adopt_contract_values(row, record)

    return row


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
            if not path or (AI_DIR / path).parent != POOL_CONFIGS[source_pool]["readme_dir"]:
                reasons.append("README path is outside the source pool directory")
        if reasons:
            problems.append(f"{model_id}: {'; '.join(reasons)}")
    if problems:
        raise ValueError(f"[{source_pool}] Stage 2 validation failed:\n" + "\n".join(problems))
    return {"source_pool": source_pool, "rows": len(rows), "bad_count": 0}


def source_revision(stage1_row):
    """The Hub revision a Stage 1 row describes: commit SHA and last-modified time."""
    hub = stage1_row.get("hub") or {}
    return {"source_sha": hub.get("sha"), "source_last_modified": hub.get("last_modified")}


def revision_matches(row, source_row):
    """Whether a saved Stage 2 row was built from the Hub revision Stage 1 now reports.

    SHA when both sides have one, else last_modified. A row with no recorded revision
    (written before this check existed) is never current, so it is collected again.
    """
    stage = row.get("stage", {})
    current = source_revision(source_row)
    if stage.get("source_sha") and current["source_sha"]:
        return stage["source_sha"] == current["source_sha"]
    if stage.get("source_last_modified") and current["source_last_modified"]:
        return stage["source_last_modified"] == current["source_last_modified"]
    return False


def resume_matches(row, source_row, source_pool):
    """Reuse only this pool/version, the unchanged Stage 1 snapshot and the same Hub revision.

    Without the revision check a model that changed on the Hub (new README, new files) keeps
    its old Stage 2 facts whenever downloads and tags happen to be unchanged, even though the
    incremental scan selected it as changed.
    """
    stage = row.get("stage", {})
    return (
        revision_matches(row, source_row)
        and stage.get("stage2_version") == STAGE2_VERSION
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


def process_pool(source_pool, model_ids=None):
    config = POOL_CONFIGS[source_pool]
    if not config["input"].is_file():
        raise FileNotFoundError(f"[{source_pool}] Missing input: {config['input']}")
    all_source_rows = load_jsonl(config["input"])
    source_by_id = {row["model_id"]: row for row in all_source_rows}
    source_rows = all_source_rows if TEST_LIMIT is None else all_source_rows[:TEST_LIMIT]
    if model_ids is not None:
        source_rows = [row for row in source_rows if row.get("model_id") in model_ids]
    config["readme_dir"].mkdir(parents=True, exist_ok=True)

    # Keep compatible prior results outside TEST_LIMIT, too: a small run must not
    # truncate a previously enriched larger corpus. Matching IDs are refreshed.
    # Retain prior rows until the user requests removal of out-of-source models.
    previous_by_id = {row["model_id"]: row for row in load_jsonl(config["output"])}
    # 이어서 돌릴 때 건너뛴 모델의 계약 레코드가 사라지지 않게 미리 읽어 둔다.
    contracts_by_id = {
        record["model_id"]: record for record in load_jsonl(config["contract_output"])
    }
    results_by_id = {
        row["model_id"]: row for row in previous_by_id.values()
        if row.get("model_id") in source_by_id
        and resume_matches(row, source_by_id[row["model_id"]], source_pool)
    }
    success = skipped = errors = 0
    print(f"[{source_pool}] START: source={len(all_source_rows):,} selected={len(source_rows):,}", flush=True)

    # Accumulates across checkpoints and runs so excluded models are neither re-enriched nor
    # dropped from the report. ponytail: an excluded model stays excluded even if its card later
    # adds Korean; delete its entry from the report to re-check it.
    report = DATA_DIR / f"hf_models_stage2_{source_pool}_language_excluded.json"
    excluded = json.loads(report.read_text(encoding="utf-8")) if report.is_file() else {}

    def checkpoint():
        excluded.update(language_exclusions(results_by_id.values()))
        for model_id in excluded:
            results_by_id.pop(model_id, None)
        report.write_text(json.dumps(excluded, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for model_id in excluded:
            contracts_by_id.pop(model_id, None)
        rows = list(results_by_id.values())
        validate_stage2_rows(rows, source_pool)
        # Validate current v7-source results; older retained rows keep provenance.
        # Stage 2 is authoritative for the current Stage 1 pool. Do not
        # carry rows that disappeared from the source pool into output.
        save_jsonl_atomic(list(results_by_id.values()), config["output"])
        save_jsonl_atomic(
            [contracts_by_id[model_id] for model_id in results_by_id if model_id in contracts_by_id],
            config["contract_output"],
        )

    checkpoint()  # apply the language gate to resumed rows before the loop
    try:
        for index, source_row in enumerate(source_rows, start=1):
            model_id = source_row["model_id"]
            prefix = f"[{source_pool}] {index}/{len(source_rows)}"
            if model_id in results_by_id or model_id in excluded:
                skipped += 1
                print(f"{prefix} SKIP {model_id}")
            else:
                print(f"{prefix} ENRICH {model_id}", flush=True)
                try:
                    row = enrich(source_row, source_pool)
                    # 계약 레코드는 본문에서 떼어 별도 파일로 보낸다.
                    contracts_by_id[model_id] = row.pop("contract")
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
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pool",
        choices=(*SOURCE_POOLS, "all"),
        default="all",
        help="Source pool to enrich; all keeps both Core and Low Popularity.",
    )
    parser.add_argument(
        "--model-ids-file",
        type=Path,
        default=None,
        help="Optional JSON list of model IDs to enrich; other rows are retained.",
    )
    args = parser.parse_args()
    model_ids = None
    if args.model_ids_file is not None:
        value = json.loads(args.model_ids_file.read_text(encoding="utf-8"))
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            parser.error("--model-ids-file must contain a JSON list of model IDs")
        model_ids = set(value)

    validate_source_pools()
    selected_pools = SOURCE_POOLS if args.pool == "all" else (args.pool,)
    for source_pool in selected_pools:
        process_pool(source_pool, model_ids=model_ids)


if __name__ == "__main__":
    main()
