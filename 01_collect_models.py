from huggingface_hub import HfApi

import json
import os
import re
import time

from pathlib import Path
from collections import defaultdict
from types import SimpleNamespace


# =========================================================
# CONFIG
# =========================================================

HF_TOKEN = os.getenv("HF_TOKEN")

api = HfApi(
    token=HF_TOKEN
)


TASKS = [
    "text-generation",
    "feature-extraction",
    "sentence-similarity",
    "text-classification",
    "question-answering",
    "summarization",
    "translation",
    "image-text-to-text",
    "automatic-speech-recognition",
]


# =========================================================
# COLLECTION POLICY
# =========================================================

# Hard cap 없음.
# downloads 기준 adaptive stopping.
LIMIT_PER_TASK = None

# Offline 후보 최소선
MIN_DOWNLOADS = 100

# Main corpus 기준
CORE_DOWNLOADS = 500

# downloads < 100이 연속 N개면 해당 task 종료
CUTOFF_CONFIRMATION = 10

PROGRESS_EVERY = 500
CHECKPOINT_EVERY = 5000
TASK_SLEEP_SECONDS = 0.5


# =========================================================
# OUTPUT
# =========================================================

DATA_DIR = Path("data")

CORE_OUTPUT = (
    DATA_DIR
    / "hf_models_stage1_core.jsonl"
)

LOW_POPULARITY_OUTPUT = (
    DATA_DIR
    / "hf_models_stage1_low_popularity.jsonl"
)

LIKELY_OUTPUT = DATA_DIR / "hf_models_stage1_likely.jsonl"

FALLBACK_OUTPUT = (
    DATA_DIR
    / "hf_models_stage1_fallback.jsonl"
)

GROUP_OUTPUT = (
    DATA_DIR
    / "hf_models_stage1_groups.jsonl"
)

STATE_OUTPUT = (
    DATA_DIR
    / "hf_models_stage1_state.json"
)


# =========================================================
# BASIC FILTER
# =========================================================

EXCLUDE_PATTERNS = [
    "internal-testing",
    "tiny-random",
    "dummy",
    "test-model",
    "testing/",
    "test/",
]


KOREAN_EXPLICIT_TAGS = {
    "ko",
    "kor",
    "korean",
    "ko-kr",
    "language:ko",
    "language:kor",
    "language:korean",
    "language:ko-kr",
}


MULTILINGUAL_TAGS = {
    "multilingual",
    "multilinguality",
    "multi-lingual",
    "multi-language",
    "language:multilingual",
}


# Token boundaries prevent accidental matches in token, kokoro, unknown, etc.
KOREAN_NAME_PATTERNS = [
    r"(?:^|[-_/ .])(?:ko|kor|korean)(?=$|[-_/ .])",
    r"(?:^|[-_/ .])(?:kobert|koelectra|kogpt|kosimcse|korbert|klue|korquad|kullm)(?=$|[-_/ .0-9])",
]


# =========================================================
# FAMILY HEURISTIC
# =========================================================

MULTILINGUAL_FAMILIES = [
    "qwen",
    "aya",
    "gemma",
    "llama",
    "mistral",
    "bloom",
    "xlm",
    "mt5",
    "mbert",
    "multilingual-e5",
    "bge-m3",
]


# =========================================================
# ISO 639-1
# =========================================================

ISO_639_1 = {
    "aa", "ab", "ae", "af", "ak", "am", "an", "ar",
    "as", "av", "ay", "az",
    "ba", "be", "bg", "bh", "bi", "bm", "bn", "bo",
    "br", "bs",
    "ca", "ce", "ch", "co", "cr", "cs", "cu", "cv",
    "cy",
    "da", "de", "dv", "dz",
    "ee", "el", "en", "eo", "es", "et", "eu",
    "fa", "ff", "fi", "fj", "fo", "fr", "fy",
    "ga", "gd", "gl", "gn", "gu", "gv",
    "ha", "he", "hi", "ho", "hr", "ht", "hu", "hy",
    "hz",
    "ia", "id", "ie", "ig", "ii", "ik", "io", "is",
    "it", "iu",
    "ja", "jv",
    "ka", "kg", "ki", "kj", "kk", "kl", "km", "kn",
    "ko", "kr", "ks", "ku", "kv", "kw", "ky",
    "la", "lb", "lg", "li", "ln", "lo", "lt", "lu",
    "lv",
    "mg", "mh", "mi", "mk", "ml", "mn", "mr", "ms",
    "mt", "my",
    "na", "nb", "nd", "ne", "ng", "nl", "nn", "no",
    "nr", "nv", "ny",
    "oc", "oj", "om", "or", "os",
    "pa", "pi", "pl", "ps", "pt",
    "qu",
    "rm", "rn", "ro", "ru", "rw",
    "sa", "sc", "sd", "se", "sg", "si", "sk", "sl",
    "sm", "sn", "so", "sq", "sr", "ss", "st", "su",
    "sv", "sw",
    "ta", "te", "tg", "th", "ti", "tk", "tl", "tn",
    "to", "tr", "ts", "tt", "tw", "ty",
    "ug", "uk", "ur", "uz",
    "ve", "vi", "vo",
    "wa", "wo",
    "xh",
    "yi", "yo",
    "za", "zh", "zu",
}


# =========================================================
# VARIANT
# =========================================================

VARIANT_PATTERNS = [
    ("awq", r"(^|[-_.])awq($|[-_.])"),
    ("gptq", r"(^|[-_.])gptq($|[-_.])"),
    ("gguf", r"(^|[-_.])gguf($|[-_.])"),
    ("fp8", r"(^|[-_.])fp8($|[-_.])"),
    ("nvfp4", r"(^|[-_.])nvfp4($|[-_.])"),
    ("fp4", r"(^|[-_.])fp4($|[-_.])"),
    ("int4", r"(^|[-_.])int4($|[-_.])"),
    ("int8", r"(^|[-_.])int8($|[-_.])"),
    ("bnb_4bit", r"bnb[-_.]?4bit"),
    ("4bit", r"(^|[-_.])4[-_.]?bit($|[-_.])"),
    ("8bit", r"(^|[-_.])8[-_.]?bit($|[-_.])"),
    ("mlx", r"(^|[-_.])mlx($|[-_.])"),
    ("mlx_quantized", r"mlx[-_.]?[4568][-_]?bit"),
]


BASE_MODEL_RELATION_PREFIXES = {
    "finetune",
    "adapter",
    "merge",
    "quantized",
}


# =========================================================
# GENERAL UTILS
# =========================================================

def safe_iso(value):
    if value is None:
        return None

    try:
        return value.isoformat()
    except Exception:
        return str(value)


def get_tags(model):
    value = getattr(
        model,
        "tags",
        None,
    )

    return list(value) if value else []


def normalize_tag(value):
    return (
        str(value)
        .strip()
        .lower()
    )


def normalize_tags(tags):
    return {
        normalize_tag(tag)
        for tag in tags
    }


def is_noise_model(model_id):
    value = model_id.lower()

    return any(
        pattern in value
        for pattern in EXCLUDE_PATTERNS
    )


# =========================================================
# LANGUAGE EXTRACTION
# =========================================================

def normalize_language(value):
    value = normalize_tag(value)
    if value.startswith("language:"):
        value = value.split(":", 1)[1].strip()
    if value in {"multilingual", "multilinguality", "multi-lingual", "multi-language"}:
        return "multilingual"
    if value in {"kor", "korean"}:
        return "ko"
    base = value.replace("_", "-").split("-")[0]
    return base if base in ISO_639_1 else None


def normalize_languages(values):
    if isinstance(values, str):
        values = [values]
    return sorted({language for value in (values or [])
                   if (language := normalize_language(value)) is not None})


def normalize_language_code(value):
    language = normalize_language(value)
    return language if language != "multilingual" else None


def extract_language_codes(tags):
    return [language for language in normalize_languages(tags)
            if language != "multilingual"]


def detect_multilingual_marker(tags):
    return "multilingual" in normalize_languages(tags)


def detect_explicit_korean(
    tags,
    languages,
):

    normalized = normalize_tags(
        tags
    )

    if "ko" in languages:
        return True

    return bool(
        normalized
        &
        KOREAN_EXPLICIT_TAGS
    )


# =========================================================
# BASE MODEL
# =========================================================

def extract_base_models(tags):

    values = []

    for raw_tag in tags:

        if not isinstance(
            raw_tag,
            str,
        ):
            continue

        if not raw_tag.lower().startswith(
            "base_model:"
        ):
            continue

        value = (
            raw_tag[
                len("base_model:"):
            ]
            .strip()
        )

        if not value:
            continue

        # ex:
        # base_model:finetune:Qwen/Qwen3-8B
        if ":" in value:

            first, rest = value.split(
                ":",
                1,
            )

            if (
                first.lower()
                in BASE_MODEL_RELATION_PREFIXES
            ):
                value = rest.strip()

        if (
            value
            and value not in values
        ):
            values.append(
                value
            )

    return values


# =========================================================
# FAMILY HEURISTIC
# =========================================================

def family_match(
    model_id,
    family,
):

    pattern = (
        rf"(^|[/_.\-])"
        rf"{re.escape(family.lower())}"
        rf"([/_.\-0-9]|$)"
    )

    return bool(
        re.search(
            pattern,
            model_id.lower(),
        )
    )


def detect_family_matches(
    model_id,
):

    return [
        family
        for family in MULTILINGUAL_FAMILIES
        if family_match(
            model_id,
            family,
        )
    ]


# =========================================================
# KOREAN NAME
# =========================================================

def detect_korean_name(
    model_id,
):

    value = model_id.lower()

    return [
        pattern
        for pattern
        in KOREAN_NAME_PATTERNS
        if re.search(
            pattern,
            value,
        )
    ]


# =========================================================
# CANDIDATE CLASSIFICATION
# =========================================================

def is_korean_model_name(model_id):
    return bool(detect_korean_name(model_id))


def extract_language_evidence(model):
    # Hub full=True exposes language tags; also accept explicit/card metadata.
    values = list(get_tags(model))
    for field in ("language", "languages"):
        value = getattr(model, field, None)
        if value:
            values.extend([value] if isinstance(value, str) else value)
    card = getattr(model, "card_data", None) or getattr(model, "cardData", None)
    if card is not None:
        value = card.get("language") if hasattr(card, "get") else getattr(card, "language", None)
        if value:
            values.extend([value] if isinstance(value, str) else value)
    normalized = normalize_languages(values)
    languages = [value for value in normalized if value != "multilingual"]
    return {"languages": languages, "concrete_language_count": len(languages),
            "multilingual_marker": "multilingual" in normalized}


def classify_candidate(model):
    model_id = getattr(model, "id", "") or ""
    language = extract_language_evidence(model)
    languages = language["languages"]
    marker = language["multilingual_marker"]
    count = language["concrete_language_count"]
    names = detect_korean_name(model_id)
    families = detect_family_matches(model_id)
    if "ko" in languages:
        tier, kind, evidence = "A_verified", "korean_explicit", ["explicit_language:korean"]
    elif is_korean_model_name(model_id):
        tier, kind, evidence = "A_verified", "korean_name", [f"name:{name}" for name in names]
    elif marker and count >= 2:
        tier, kind, evidence = "A_verified", "multilingual_explicit", ["multilingual_tag", "explicit_language_list:" + ",".join(languages)]
    elif count >= 3:
        tier, kind, evidence = "A_verified", "multilingual_language_list", ["explicit_language_list:" + ",".join(languages)]
    elif count == 2:
        tier, kind, evidence = "B_likely", "bilingual_language_list", ["bilingual_language_list:" + ",".join(languages)]
    elif marker:
        tier, kind, evidence = "B_likely", "multilingual_tag_only", ["multilingual_tag_only"]
    elif families and count == 0:
        tier, kind, evidence = "C_fallback", "family_heuristic", [f"family:{family}" for family in families]
    else:
        return None
    return {"tier": tier, "type": kind,
            "confidence": {"A_verified": "high", "B_likely": "medium", "C_fallback": "low"}[tier],
            **language, "evidence": evidence}


# =========================================================
# VARIANT DETECTION
# =========================================================

def detect_variant_types(
    model_id,
    tags,
):

    joined = " ".join(
        [model_id.lower()]
        +
        [
            normalize_tag(tag)
            for tag in tags
        ]
    )

    variants = []

    for name, pattern in VARIANT_PATTERNS:

        if re.search(
            pattern,
            joined,
        ):

            if name not in variants:
                variants.append(
                    name
                )

    return variants


def normalize_model_name(
    model_id,
):

    if "/" in model_id:

        owner, name = model_id.split(
            "/",
            1,
        )

    else:

        owner = None
        name = model_id


    normalized = name


    patterns = [
        r"[-_.]awq\b",
        r"[-_.]gptq\b",
        r"[-_.]gguf\b",
        r"[-_.]fp8\b",
        r"[-_.]nvfp4\b",
        r"[-_.]fp4\b",
        r"[-_.]int4\b",
        r"[-_.]int8\b",
        r"[-_.]bnb[-_.]?4bit\b",
        r"[-_.]mlx(?:[-_.]?[4568]bit)?\b",
        r"[-_.][4568][-_.]?bit\b",
    ]


    for pattern in patterns:

        normalized = re.sub(
            pattern,
            "",
            normalized,
            flags=re.IGNORECASE,
        )


    normalized = (
        re.sub(
            r"[-_.]{2,}",
            "-",
            normalized,
        )
        .strip("-_.")
    )


    if owner:
        return f"{owner}/{normalized}"

    return normalized


def build_family_info(
    model_id,
    tags,
):

    base_models = (
        extract_base_models(
            tags
        )
    )

    variant_types = (
        detect_variant_types(
            model_id,
            tags,
        )
    )


    if base_models:

        canonical = base_models[0]

        source = (
            "base_model_tag"
        )

    elif variant_types:

        canonical = (
            normalize_model_name(
                model_id
            )
        )

        source = (
            "name_heuristic"
        )

    else:

        canonical = model_id
        source = "self"


    return {
        "canonical_model_id":
            canonical,

        "canonical_source":
            source,

        "is_variant":
            (
                canonical != model_id
                or bool(
                    variant_types
                )
            ),

        "variant_types":
            variant_types,

        "declared_base_models":
            base_models,
    }


# =========================================================
# LICENSE
# =========================================================

def first_license(tags):

    for raw_tag in tags:

        tag = str(raw_tag)

        if tag.lower().startswith(
            "license:"
        ):

            return tag.split(
                ":",
                1,
            )[1]

    return None


# =========================================================
# QUALITY
# =========================================================

# Metadata completeness / popularity signal, never model quality or a deletion filter.
def calculate_quality(
    languages,
    license_value,
    pipeline_tag,
    library_name,
    base_models,
    downloads,
    likes,
):

    metadata_score = 0

    signals = []


    # language metadata는 중요도가 높아서 +2
    if languages:

        metadata_score += 2

        signals.append(
            "languages"
        )


    if license_value:

        metadata_score += 1

        signals.append(
            "license"
        )


    if pipeline_tag:

        metadata_score += 1

        signals.append(
            "pipeline_tag"
        )


    if library_name:

        metadata_score += 1

        signals.append(
            "library_name"
        )


    if base_models:

        metadata_score += 1

        signals.append(
            "base_model"
        )


    popularity_score = 0


    if downloads >= CORE_DOWNLOADS:
        popularity_score += 1


    if likes > 0:
        popularity_score += 1


    total_score = (
        metadata_score
        +
        popularity_score
    )


    if total_score >= 6:
        label = "high"

    elif total_score >= 3:
        label = "medium"

    else:
        label = "low"


    return {
        "metadata_score":
            metadata_score,

        "popularity_score":
            popularity_score,

        "total_score":
            total_score,

        "max_score":
            8,

        "label":
            label,

        "metadata_signals":
            signals,
    }


# =========================================================
# POPULARITY
# =========================================================

def popularity_tier(
    downloads,
):

    if downloads >= CORE_DOWNLOADS:
        return "main"

    if downloads >= MIN_DOWNLOADS:
        return "low_popularity"

    return "excluded"


# =========================================================
# ROW
# =========================================================

def build_row(
    model,
    classification,
):

    model_id = model.id

    tags = get_tags(
        model
    )

    languages = (
        classification[
            "languages"
        ]
    )

    downloads = (
        getattr(
            model,
            "downloads",
            None,
        )
        or 0
    )

    likes = (
        getattr(
            model,
            "likes",
            None,
        )
        or 0
    )

    pipeline_tag = (
        getattr(
            model,
            "pipeline_tag",
            None,
        )
    )

    library_name = (
        getattr(
            model,
            "library_name",
            None,
        )
    )

    license_value = (
        first_license(
            tags
        )
    )

    family_info = (
        build_family_info(
            model_id,
            tags,
        )
    )

    base_models = (
        family_info[
            "declared_base_models"
        ]
    )

    quality = (
        calculate_quality(
            languages=
                languages,

            license_value=
                license_value,

            pipeline_tag=
                pipeline_tag,

            library_name=
                library_name,

            base_models=
                base_models,

            downloads=
                downloads,

            likes=
                likes,
        )
    )


    return {
        "model_id":
            model_id,

        "author":
            getattr(
                model,
                "author",
                None,
            ),

        "library_name":
            library_name,

        "primary_task":
            pipeline_tag,

        "matched_tasks":
            [],


        "candidate": {
            "tier":
                classification[
                    "tier"
                ],

            "type":
                classification[
                    "type"
                ],

            "confidence":
                classification[
                    "confidence"
                ],

            "evidence":
                list(
                    classification[
                        "evidence"
                    ]
                ),
        },


        "language": {
            "languages":
                languages,

            "korean_explicit":
                (
                    "ko"
                    in languages
                ),

            "multilingual_marker":
                classification[
                    "multilingual_marker"
                ],

            "language_count":
                len(
                    languages
                ),
        },


        "popularity": {
            "downloads":
                downloads,

            "likes":
                likes,

            "tier":
                popularity_tier(
                    downloads
                ),
        },


        "family":
            family_info,


        "quality":
            quality,


        "hub": {
            "tags":
                tags,

            "license":
                license_value,

            "gated":
                getattr(
                    model,
                    "gated",
                    None,
                ),

            "private":
                getattr(
                    model,
                    "private",
                    None,
                ),

            "sha":
                getattr(
                    model,
                    "sha",
                    None,
                ),

            "created_at":
                safe_iso(
                    getattr(
                        model,
                        "created_at",
                        None,
                    )
                ),

            "last_modified":
                safe_iso(
                    getattr(
                        model,
                        "last_modified",
                        None,
                    )
                ),
        },


        "stage": {
            "collected":
                True,

            "metadata_enriched":
                False,

            "semantic_enriched":
                False,

            "stage1_version":
                4,
        },
    }


# =========================================================
# RANK
# =========================================================

CANDIDATE_RANK = {
    "A_verified": 3,
    "B_likely": 2,
    "C_fallback": 1,
}


# =========================================================
# MERGE
# =========================================================

def merge_candidate(
    all_models,
    model,
    task,
    classification,
):

    model_id = model.id


    if model_id not in all_models:

        all_models[
            model_id
        ] = build_row(
            model,
            classification,
        )


    else:

        current = (
            all_models[
                model_id
            ]
        )

        current_rank = (
            CANDIDATE_RANK.get(
                current[
                    "candidate"
                ][
                    "tier"
                ],
                0,
            )
        )

        new_rank = (
            CANDIDATE_RANK.get(
                classification[
                    "tier"
                ],
                0,
            )
        )


        if new_rank > current_rank:

            old_tasks = list(
                current[
                    "matched_tasks"
                ]
            )

            old_evidence = list(
                current[
                    "candidate"
                ][
                    "evidence"
                ]
            )


            all_models[
                model_id
            ] = build_row(
                model,
                classification,
            )

            current = (
                all_models[
                    model_id
                ]
            )

            current[
                "matched_tasks"
            ] = old_tasks


            for evidence in old_evidence:

                if (
                    evidence
                    not in current[
                        "candidate"
                    ][
                        "evidence"
                    ]
                ):
                    current[
                        "candidate"
                    ][
                        "evidence"
                    ].append(
                        evidence
                    )


    row = (
        all_models[
            model_id
        ]
    )


    if (
        task
        not in row[
            "matched_tasks"
        ]
    ):

        row[
            "matched_tasks"
        ].append(
            task
        )


    for evidence in (
        classification[
            "evidence"
        ]
    ):

        if (
            evidence
            not in row[
                "candidate"
            ][
                "evidence"
            ]
        ):

            row[
                "candidate"
            ][
                "evidence"
            ].append(
                evidence
            )


# =========================================================
# SAVE UTILS
# =========================================================

def save_jsonl_atomic(
    rows,
    path,
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = path.with_suffix(
        path.suffix
        + ".tmp"
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


def save_json_atomic(
    obj,
    path,
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_path = str(
        path
    ) + ".tmp"


    with open(
        temp_path,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            obj,
            f,
            ensure_ascii=False,
            indent=2,
        )


    os.replace(
        temp_path,
        path,
    )


# =========================================================
# PARTITION
# =========================================================

def partition_rows(all_models):
    core, low, likely, fallback = [], [], [], []
    for row in all_models.values():
        downloads = row["popularity"]["downloads"]
        if downloads < MIN_DOWNLOADS:
            continue
        tier = row["candidate"]["tier"]
        if tier == "A_verified":
            (core if downloads >= CORE_DOWNLOADS else low).append(row)
        elif tier == "B_likely":
            likely.append(row)
        elif tier == "C_fallback":
            fallback.append(row)
    for rows in (core, low, likely, fallback):
        rows.sort(key=lambda row: (row["popularity"]["downloads"], row["popularity"].get("likes", 0), row["model_id"]), reverse=True)
    return core, low, likely, fallback


# =========================================================
# CANONICAL GROUPING
# =========================================================

def build_groups(
    all_models,
):

    grouped = defaultdict(
        list
    )


    for row in (
        all_models.values()
    ):

        canonical = (
            row[
                "family"
            ][
                "canonical_model_id"
            ]
        )

        grouped[
            canonical
        ].append(
            row
        )


    output = []


    for canonical, members in (
        grouped.items()
    ):

        members.sort(
            key=lambda x: (
                x[
                    "popularity"
                ][
                    "downloads"
                ]
                or 0
            ),
            reverse=True,
        )


        canonical_row = next(
            (
                row
                for row in members
                if (
                    row[
                        "model_id"
                    ]
                    == canonical
                )
            ),
            None,
        )


        canonical_present = (
            canonical_row
            is not None
        )


        # 실제 canonical repo가 candidate pool 안에 있으면
        # canonical 자체가 representative.
        #
        # 없다면 가장 다운로드가 높은 variant를
        # representative로 사용한다.
        if canonical_present:

            representative_model_id = (
                canonical_row[
                    "model_id"
                ]
            )

        else:

            representative_model_id = (
                members[0][
                    "model_id"
                ]
            )


        output.append({
            "canonical_model_id":
                canonical,

            "canonical_present":
                canonical_present,

            "representative_model_id":
                representative_model_id,

            "member_count":
                len(
                    members
                ),

            "variants": [
                {
                    "model_id":
                        row[
                            "model_id"
                        ],

                    "is_variant":
                        row[
                            "family"
                        ][
                            "is_variant"
                        ],

                    "variant_types":
                        row[
                            "family"
                        ][
                            "variant_types"
                        ],

                    "candidate_tier":
                        row[
                            "candidate"
                        ][
                            "tier"
                        ],

                    "candidate_type":
                        row[
                            "candidate"
                        ][
                            "type"
                        ],

                    "popularity_tier":
                        row[
                            "popularity"
                        ][
                            "tier"
                        ],

                    "downloads":
                        row[
                            "popularity"
                        ][
                            "downloads"
                        ],
                }

                for row in members
            ],
        })


    output.sort(
        key=lambda group: (
            group[
                "variants"
            ][0][
                "downloads"
            ]
            or 0
        ),
        reverse=True,
    )


    return output


# =========================================================
# SAVE ALL
# =========================================================

def save_all(all_models, state):
    core, low, likely, fallback = partition_rows(all_models)
    retained = {row["model_id"]: row for rows in (core, low, likely, fallback) for row in rows}
    groups = build_groups(retained)
    for rows, path in ((core, CORE_OUTPUT), (low, LOW_POPULARITY_OUTPUT),
                       (likely, LIKELY_OUTPUT), (fallback, FALLBACK_OUTPUT),
                       (groups, GROUP_OUTPUT)):
        save_jsonl_atomic(rows, path)
    save_json_atomic(state, STATE_OUTPUT)


# =========================================================
# STATS
# =========================================================

def calculate_stats(
    all_models,
):

    stats = {
        "A_verified": 0,
        "B_likely": 0,
        "C_fallback": 0,

        "main": 0,
        "low_popularity": 0,

        "variants": 0,
    }


    candidate_types = defaultdict(
        int
    )


    for row in (
        all_models.values()
    ):

        tier = (
            row[
                "candidate"
            ][
                "tier"
            ]
        )

        candidate_type = (
            row[
                "candidate"
            ][
                "type"
            ]
        )

        candidate_types[
            candidate_type
        ] += 1


        if tier in stats:

            stats[
                tier
            ] += 1


        pop = (
            row[
                "popularity"
            ][
                "tier"
            ]
        )

        if pop in stats:

            stats[
                pop
            ] += 1


        if (
            row[
                "family"
            ][
                "is_variant"
            ]
        ):

            stats[
                "variants"
            ] += 1


    stats[
        "candidate_types"
    ] = dict(
        candidate_types
    )


    return stats


# =========================================================
# MAIN
# =========================================================

def validate_outputs(require_complete=True):
    """Audit persisted corpora, evidence, popularity, and group coverage."""
    counts, retained = {}, {}
    specifications = (
        (CORE_OUTPUT, "A_verified", CORE_DOWNLOADS, None),
        (LOW_POPULARITY_OUTPUT, "A_verified", MIN_DOWNLOADS, CORE_DOWNLOADS),
        (LIKELY_OUTPUT, "B_likely", MIN_DOWNLOADS, None),
        (FALLBACK_OUTPUT, "C_fallback", MIN_DOWNLOADS, None),
    )
    for path, tier, minimum, maximum in specifications:
        bad = 0
        rows = [json.loads(line) for line in path.read_text().splitlines() if line]
        for row in rows:
            downloads = row["popularity"]["downloads"]
            bad += int(row["candidate"]["tier"] != tier or downloads < minimum
                       or (maximum is not None and downloads >= maximum))
            assert row["model_id"] not in retained, "Duplicate corpus model"
            expected = classify_candidate(SimpleNamespace(
                id=row["model_id"], tags=row["hub"]["tags"],
                languages=row["language"]["languages"]))
            assert expected is not None, "Excluded model in corpus"
            assert all(row["candidate"][key] == expected[key]
                       for key in ("tier", "type", "confidence")), "Invalid language classification"
            assert row["stage"]["stage1_version"] == 4
            assert row["popularity"]["tier"] == popularity_tier(downloads)
            retained[row["model_id"]] = row
        counts[path.name] = len(rows)
        print(f"AUDIT {path.name}: rows={len(rows)} bad={bad}")
        assert bad == 0, f"Invalid partition: {path}"
    groups = [json.loads(line) for line in GROUP_OUTPUT.read_text().splitlines() if line]
    assert groups == build_groups(retained), "Groups differ from retained corpus union"
    counts[GROUP_OUTPUT.name] = len(groups)
    state = json.loads(STATE_OUTPUT.read_text())
    assert state["stage1_version"] == 4
    assert state["config"]["core_candidate_tier"] == "A_verified"
    if require_complete:
        assert set(state["completed_tasks"]) == set(TASKS), "Incomplete task collection"
        assert all(not stats.get("error") for stats in state["task_stats"].values())
    print(f"AUDIT groups={len(groups)} retained={len(retained)}")
    return counts


def main():

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


    all_models = {}


    state = {
        "stage1_version":
            4,

        "config": {
            "min_downloads":
                MIN_DOWNLOADS,

            "core_downloads":
                CORE_DOWNLOADS,

            "limit_per_task":
                LIMIT_PER_TASK,

            "cutoff_confirmation":
                CUTOFF_CONFIRMATION,

            "multilingual_min_languages":
                3,
            "core_candidate_tier": "A_verified",
        },

        "completed_tasks":
            [],

        "task_stats":
            {},
    }


    total_scanned = 0


    for task in TASKS:

        print()
        print("=" * 80)

        print(
            f"Collecting task: "
            f"{task}"
        )

        print("=" * 80)


        scanned = 0
        accepted = 0

        below_cutoff_streak = 0

        cutoff_reached = False
        cutoff_downloads = None
        task_error = None


        try:

            models = (
                api.list_models(
                    pipeline_tag=task,
                    sort="downloads",
                    limit=LIMIT_PER_TASK,
                    full=True,
                )
            )


            for model in models:

                scanned += 1

                total_scanned += 1


                model_id = (
                    getattr(
                        model,
                        "id",
                        None,
                    )
                )


                if not model_id:
                    continue


                downloads_raw = (
                    getattr(
                        model,
                        "downloads",
                        None,
                    )
                )


                if downloads_raw is None:
                    continue


                downloads = int(
                    downloads_raw
                )


                # =================================================
                # ADAPTIVE DOWNLOAD CUTOFF
                # =================================================

                if (
                    downloads
                    < MIN_DOWNLOADS
                ):

                    below_cutoff_streak += 1


                    if (
                        below_cutoff_streak
                        >= CUTOFF_CONFIRMATION
                    ):

                        cutoff_reached = True
                        cutoff_downloads = downloads


                        print()

                        print(
                            f"Download cutoff confirmed | "
                            f"task={task} | "
                            f"scanned={scanned:,} | "
                            f"downloads={downloads:,}"
                        )


                        break


                    continue


                below_cutoff_streak = 0


                # =================================================
                # NOISE
                # =================================================

                if is_noise_model(
                    model_id
                ):

                    continue


                # =================================================
                # CLASSIFY
                # =================================================

                classification = (
                    classify_candidate(
                        model
                    )
                )


                if (
                    classification
                    is not None
                ):

                    accepted += 1


                    merge_candidate(
                        all_models=
                            all_models,

                        model=
                            model,

                        task=
                            task,

                        classification=
                            classification,
                    )


                # =================================================
                # PROGRESS
                # =================================================

                if (
                    scanned
                    % PROGRESS_EVERY
                    == 0
                ):

                    (
                        core,
                        low,
                        likely,
        fallback,
                    ) = partition_rows(
                        all_models
                    )


                    print(
                        f"  progress | "
                        f"scanned={scanned:,} | "
                        f"core={len(core):,} | "
                        f"low={len(low):,} | "
                        f"fallback={len(fallback):,}",
                        flush=True,
                    )


                # =================================================
                # CHECKPOINT
                # =================================================

                if (
                    scanned
                    % CHECKPOINT_EVERY
                    == 0
                ):

                    save_all(
                        all_models,
                        state,
                    )


                    print(
                        "  checkpoint saved",
                        flush=True,
                    )


        except KeyboardInterrupt:

            print()

            print(
                "Interrupted. "
                "Saving checkpoint..."
            )


            save_all(
                all_models,
                state,
            )


            raise


        except Exception as e:
            task_error = f"{type(e).__name__}: {e}"

            print(
                f"[TASK ERROR] "
                f"{task}: "
                f"{type(e).__name__}: "
                f"{e}"
            )


        state[
            "task_stats"
        ][task] = {
            "scanned":
                scanned,

            "accepted":
                accepted,
            "retained": accepted,
            "cutoff_downloads": cutoff_downloads,
            "error": task_error,

            "cutoff_reached":
                cutoff_reached,
        }


        if task_error is None:
            state["completed_tasks"].append(task)


        save_all(
            all_models,
            state,
        )


        (
            core,
            low,
            likely,
        fallback,
        ) = partition_rows(
            all_models
        )


        print()

        print(
            f"Finished {task}"
        )

        print(
            f"  scanned      : "
            f"{scanned:,}"
        )

        print(
            f"  core         : "
            f"{len(core):,}"
        )

        print(
            f"  low          : "
            f"{len(low):,}"
        )

        print(
            f"  fallback     : "
            f"{len(fallback):,}"
        )


        time.sleep(
            TASK_SLEEP_SECONDS
        )


    # =====================================================
    # FINAL
    # =====================================================

    save_all(
        all_models,
        state,
    )


    (
        core,
        low,
        likely,
        fallback,
    ) = partition_rows(
        all_models
    )


    stats = (
        calculate_stats(
            all_models
        )
    )


    groups = (
        build_groups(
            all_models
        )
    )


    canonical_present = sum(
        group[
            "canonical_present"
        ]
        for group in groups
    )


    print()
    print("=" * 80)

    print(
        "STAGE 1 SCAN ENDED (validation follows)"
    )

    print("=" * 80)


    print(
        f"Total scanned       : "
        f"{total_scanned:,}"
    )

    print(
        f"Unique candidates   : "
        f"{len(all_models):,}"
    )


    print()


    print(
        f"A verified          : "
        f"{stats['A_verified']:,}"
    )

    print(
        f"B likely            : "
        f"{stats['B_likely']:,}"
    )

    print(
        f"C fallback          : "
        f"{stats['C_fallback']:,}"
    )


    print()
    print(f"Likely >=100        : {len(likely):,}")
    print("Candidate types:")


    for (
        candidate_type,
        count,
    ) in sorted(
        stats[
            "candidate_types"
        ].items(),
        key=lambda x: x[1],
        reverse=True,
    ):

        print(
            f"  {candidate_type:32s}"
            f"{count:,}"
        )


    print()


    print(
        f"Main/Core >=500     : "
        f"{len(core):,}"
    )

    print(
        f"Low 100~499         : "
        f"{len(low):,}"
    )

    print(
        f"Family fallback     : "
        f"{len(fallback):,}"
    )


    print()


    print(
        f"Variant models      : "
        f"{stats['variants']:,}"
    )

    print(
        f"Canonical groups    : "
        f"{len(groups):,}"
    )

    print(
        f"Canonical present   : "
        f"{canonical_present:,}"
    )

    print(
        f"Canonical missing   : "
        f"{len(groups) - canonical_present:,}"
    )


    print()

    print(
        f"Core     -> "
        f"{CORE_OUTPUT}"
    )

    print(
        f"Low      -> "
        f"{LOW_POPULARITY_OUTPUT}"
    )

    print(
        f"Fallback -> "
        f"{FALLBACK_OUTPUT}"
    )

    print(
        f"Groups   -> "
        f"{GROUP_OUTPUT}"
    )

    print(
        f"State    -> "
        f"{STATE_OUTPUT}"
    )


def run_collection():
    # Checkpoints remain reviewable without replacing the published corpus on failure.
    output_names = ("CORE_OUTPUT", "LOW_POPULARITY_OUTPUT", "LIKELY_OUTPUT",
                    "FALLBACK_OUTPUT", "GROUP_OUTPUT", "STATE_OUTPUT")
    published = {name: globals()[name] for name in output_names}
    checkpoint_dir = DATA_DIR / ".stage1_v4_checkpoint"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    try:
        for name, path in published.items():
            globals()[name] = checkpoint_dir / path.name
        main()
        validate_outputs()
        for name, path in published.items():
            globals()[name].replace(path)
    finally:
        globals().update(published)


if __name__ == "__main__":
    run_collection()