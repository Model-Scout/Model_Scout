from huggingface_hub import HfApi
import json
import time
import re
import os


# =========================================================
# CONFIG
# =========================================================

api = HfApi()

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


# ---------------------------------------------------------
# 테스트:
#     1000
#
# 중간 확인:
#     5000
#
# 전체:
#     None
# ---------------------------------------------------------

LIMIT_PER_TASK = 1000


# ---------------------------------------------------------
# 다운로드 수가 너무 적은 모델 제거
#
# 0   = 사실상 전체
# 100 = 지금 추천
# ---------------------------------------------------------

MIN_DOWNLOADS = 100


OUTPUT_PATH = "hf_models_korean_stage1.json"


# 터미널 진행률
PROGRESS_EVERY = 500


# 같은 task를 처리하는 중에도 저장
CHECKPOINT_EVERY = 5000


TASK_SLEEP_SECONDS = 0.5


# =========================================================
# FILTER CONFIG
# =========================================================

EXCLUDE_PATTERNS = [
    "internal-testing",
    "tiny-random",
    "dummy",
    "test-model",
    "testing/",
    "test/",
]


# =========================================================
# Korean Explicit
# =========================================================

KOREAN_EXPLICIT_TAGS = {
    "ko",
    "kor",
    "korean",
    "language:ko",
    "language:kor",
    "language:korean",
}


# =========================================================
# Multilingual
# =========================================================

MULTILINGUAL_TAGS = {
    "multilingual",
    "multilinguality",
    "multi-lingual",
    "multi_language",
    "multi-language",
}


# =========================================================
# Korean-specialized names
# =========================================================

KOREAN_NAME_PATTERNS = [
    r"(^|[/_.\-])ko([/_.\-]|$)",
    r"korean",
    r"kobert",
    r"kogpt",
    r"korbert",
    r"koelectra",
    r"klue",
    r"korquad",
    r"kullm",
    r"polyglot[-_]?ko",
]


# =========================================================
# Known multilingual families
#
# Korean 확정은 아님.
# Stage 2에서 검증하기 위한 recall-oriented candidate.
# =========================================================

KNOWN_MULTILINGUAL_KOREAN_FAMILIES = [
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
# UTILITIES
# =========================================================

def safe_iso(value):

    if value is None:
        return None

    try:
        return value.isoformat()

    except Exception:
        return str(value)


def get_tags(model):

    tags = getattr(
        model,
        "tags",
        None
    )

    if not tags:
        return []

    return list(tags)


def extract_tag_value(
    tags,
    prefix
):

    for tag in tags:

        if not isinstance(
            tag,
            str
        ):
            continue

        if tag.startswith(
            prefix
        ):
            return tag[
                len(prefix):
            ]

    return None


def extract_tag_values(
    tags,
    prefix
):

    values = []

    for tag in tags:

        if not isinstance(
            tag,
            str
        ):
            continue

        if tag.startswith(
            prefix
        ):

            value = tag[
                len(prefix):
            ]

            if (
                value
                and value not in values
            ):
                values.append(
                    value
                )

    return values


# =========================================================
# TEST / NOISE FILTER
# =========================================================

def is_test_model(
    model_id
):

    model_id = (
        model_id.lower()
    )

    return any(
        pattern in model_id
        for pattern
        in EXCLUDE_PATTERNS
    )


# =========================================================
# FAMILY MATCH
# =========================================================

def model_family_match(
    model_id,
    family
):
    """
    단순 substring 대신 boundary를 사용한다.

    Qwen/Qwen3-8B
        -> qwen match

    unrelated-somethingphi
        -> phi 같은 잘못된 match 감소
    """

    model_id = (
        model_id.lower()
    )

    family = (
        family.lower()
    )

    pattern = (
        rf"(^|[/_.\-])"
        rf"{re.escape(family)}"
        rf"([/_.\-0-9]|$)"
    )

    return bool(
        re.search(
            pattern,
            model_id
        )
    )


# =========================================================
# LANGUAGE CANDIDATE DETECTION
# =========================================================

def detect_language_candidate(
    model
):
    """
    Stage 1에서는 '한국어 확정'이 아니라
    '한국어 사용 가능성이 있는 후보'를 찾는다.

    priority:

    explicit
        ko / korean 명시

    name_heuristic
        KoBERT, KLUE 등

    multilingual
        multilingual 태그 명시

    family_heuristic
        Qwen/Gemma/Llama 등

    none
        후보 제외
    """

    model_id = (
        getattr(
            model,
            "id",
            None
        )
        or ""
    ).lower()

    tags_original = (
        get_tags(model)
    )

    tags = [
        str(tag).lower()
        for tag
        in tags_original
    ]

    evidence = []

    # =====================================================
    # 1. Explicit Korean
    # =====================================================

    for tag in tags:

        if (
            tag
            in KOREAN_EXPLICIT_TAGS
        ):

            evidence.append(
                f"explicit_korean:{tag}"
            )

    if evidence:

        return (
            True,
            "explicit",
            evidence
        )


    # =====================================================
    # 2. Korean-specific model name
    # =====================================================

    for pattern in (
        KOREAN_NAME_PATTERNS
    ):

        if re.search(
            pattern,
            model_id
        ):

            evidence.append(
                f"korean_name:{pattern}"
            )

    if evidence:

        return (
            True,
            "name_heuristic",
            evidence
        )


    # =====================================================
    # 3. Explicit Multilingual
    # =====================================================

    for tag in tags:

        if (
            tag
            in MULTILINGUAL_TAGS
        ):

            evidence.append(
                f"multilingual_tag:{tag}"
            )

    if evidence:

        return (
            True,
            "multilingual",
            evidence
        )


    # =====================================================
    # 4. Known multilingual family
    # =====================================================

    for family in (
        KNOWN_MULTILINGUAL_KOREAN_FAMILIES
    ):

        if model_family_match(
            model_id,
            family
        ):

            evidence.append(
                f"multilingual_family:{family}"
            )

    if evidence:

        return (
            True,
            "family_heuristic",
            evidence
        )


    return (
        False,
        "none",
        []
    )


# =========================================================
# BUILD STAGE 1 ROW
# =========================================================

def build_stage1_row(
    model,
    support_level,
    language_evidence
):

    model_id = (
        model.id
    )

    tags = (
        get_tags(model)
    )

    # -----------------------------------------------------
    # lightweight metadata only
    # -----------------------------------------------------

    license_value = (
        extract_tag_value(
            tags,
            "license:"
        )
    )

    base_model = (
        extract_tag_value(
            tags,
            "base_model:"
        )
    )

    language_tags = (
        extract_tag_values(
            tags,
            "language:"
        )
    )

    lower_tags = [
        str(tag).lower()
        for tag in tags
    ]

    # HF에서는 언어가 그냥 "ko", "en"처럼
    # tag로 들어가 있는 경우도 있다.
    if (
        "ko"
        in lower_tags
        and "ko"
        not in language_tags
    ):

        language_tags.append(
            "ko"
        )


    return {

        # =================================================
        # Identity
        # =================================================

        "model_id":
            model_id,

        "author":
            getattr(
                model,
                "author",
                None
            ),

        "library_name":
            getattr(
                model,
                "library_name",
                None
            ),


        # =================================================
        # Task
        # =================================================

        "primary_pipeline_tag":
            getattr(
                model,
                "pipeline_tag",
                None
            ),

        "matched_tasks": [],


        # =================================================
        # Language candidate
        # =================================================

        "language_candidate":
            True,

        "korean_candidate":
            True,

        # Stage 2에서 판정
        "korean_verified":
            None,

        "multilingual_verified":
            None,

        "language_support_level":
            support_level,

        # 이전 코드 호환
        "korean_support_level":
            support_level,

        "language_evidence":
            list(
                language_evidence
            ),

        "korean_evidence":
            list(
                language_evidence
            ),


        # =================================================
        # Popularity
        # =================================================

        "downloads":
            getattr(
                model,
                "downloads",
                None
            ),

        "likes":
            getattr(
                model,
                "likes",
                None
            ),


        # =================================================
        # Lightweight raw HF metadata
        # =================================================

        "tags":
            tags,

        "languages":
            language_tags,

        "license":
            license_value,

        "base_model":
            base_model,

        "gated":
            getattr(
                model,
                "gated",
                None
            ),

        "private":
            getattr(
                model,
                "private",
                None
            ),

        "disabled":
            getattr(
                model,
                "disabled",
                None
            ),

        "sha":
            getattr(
                model,
                "sha",
                None
            ),

        "created_at":
            safe_iso(
                getattr(
                    model,
                    "created_at",
                    None
                )
            ),

        "last_modified":
            safe_iso(
                getattr(
                    model,
                    "last_modified",
                    None
                )
            ),


        # =================================================
        # Pipeline state
        # =================================================

        "stage1_collected":
            True,

        "metadata_enriched":
            False,

        "semantic_enriched":
            False,
    }


# =========================================================
# SAVE
# =========================================================

def save_json_atomic(
    data,
    output_path
):

    temp_path = (
        output_path
        + ".tmp"
    )

    with open(
        temp_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    os.replace(
        temp_path,
        output_path
    )


def save_current_results(
    unique_models
):

    results = list(
        unique_models.values()
    )

    results.sort(
        key=lambda x:
            x.get(
                "downloads"
            )
            or 0,
        reverse=True
    )

    save_json_atomic(
        results,
        OUTPUT_PATH
    )


# =========================================================
# MAIN
# =========================================================

def main():

    unique_models = {}


    stats = {

        "total_seen": 0,

        "excluded_test": 0,

        "excluded_downloads": 0,

        "non_language_candidate": 0,

        "language_candidates": 0,
    }


    # support level priority
    priority = {

        "none": 0,

        "family_heuristic": 1,

        "multilingual": 2,

        "name_heuristic": 3,

        "explicit": 4,
    }


    for task in TASKS:

        print()
        print("=" * 80)

        print(
            f"Collecting task: "
            f"{task}"
        )

        print("=" * 80)


        task_seen = 0

        task_candidates = 0


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

                stats[
                    "total_seen"
                ] += 1

                task_seen += 1


                # =========================================
                # Progress
                # =========================================

                if (
                    task_seen
                    % PROGRESS_EVERY
                    == 0
                ):

                    print(

                        f"  progress | "
                        f"task={task} | "

                        f"scanned="
                        f"{task_seen:,} | "

                        f"candidates="
                        f"{task_candidates:,} | "

                        f"unique="
                        f"{len(unique_models):,}",

                        flush=True,
                    )


                # =========================================
                # Periodic checkpoint
                # =========================================

                if (
                    task_seen
                    % CHECKPOINT_EVERY
                    == 0
                ):

                    save_current_results(
                        unique_models
                    )

                    print(

                        f"  checkpoint | "
                        f"{task_seen:,} scanned | "

                        f"{len(unique_models):,} "
                        f"unique saved",

                        flush=True,
                    )


                model_id = (
                    getattr(
                        model,
                        "id",
                        None
                    )
                )

                if not model_id:
                    continue


                # =========================================
                # Noise model
                # =========================================

                if is_test_model(
                    model_id
                ):

                    stats[
                        "excluded_test"
                    ] += 1

                    continue


                # =========================================
                # Downloads
                # =========================================

                downloads = (
                    getattr(
                        model,
                        "downloads",
                        None
                    )
                    or 0
                )


                if (
                    downloads
                    < MIN_DOWNLOADS
                ):

                    stats[
                        "excluded_downloads"
                    ] += 1

                    continue


                # =========================================
                # Language candidate
                # =========================================

                (
                    is_candidate,
                    support_level,
                    language_evidence,

                ) = (
                    detect_language_candidate(
                        model
                    )
                )


                if not is_candidate:

                    stats[
                        "non_language_candidate"
                    ] += 1

                    continue


                task_candidates += 1


                # =========================================
                # Unique model
                # =========================================

                if (
                    model_id
                    not in unique_models
                ):

                    unique_models[
                        model_id
                    ] = (
                        build_stage1_row(

                            model=model,

                            support_level=
                                support_level,

                            language_evidence=
                                language_evidence,
                        )
                    )

                    stats[
                        "language_candidates"
                    ] += 1


                row = (
                    unique_models[
                        model_id
                    ]
                )


                # =========================================
                # Merge task
                # =========================================

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


                # =========================================
                # Merge evidence
                # =========================================

                for evidence in (
                    language_evidence
                ):

                    if (
                        evidence
                        not in row[
                            "language_evidence"
                        ]
                    ):

                        row[
                            "language_evidence"
                        ].append(
                            evidence
                        )

                    if (
                        evidence
                        not in row[
                            "korean_evidence"
                        ]
                    ):

                        row[
                            "korean_evidence"
                        ].append(
                            evidence
                        )


                # =========================================
                # Keep strongest support level
                # =========================================

                old_level = (
                    row[
                        "language_support_level"
                    ]
                )


                if (
                    priority[
                        support_level
                    ]
                    >
                    priority[
                        old_level
                    ]
                ):

                    row[
                        "language_support_level"
                    ] = (
                        support_level
                    )

                    # Stage 2 이전 코드와 호환
                    row[
                        "korean_support_level"
                    ] = (
                        support_level
                    )


            # =============================================
            # Task finished
            # =============================================

            print()

            print(
                f"Finished {task}"
            )

            print(
                f"  scanned       : "
                f"{task_seen:,}"
            )

            print(
                f"  candidates    : "
                f"{task_candidates:,}"
            )

            print(
                f"  total unique  : "
                f"{len(unique_models):,}"
            )


        except Exception as e:

            print(

                f"[TASK ERROR] "
                f"{task}: "

                f"{type(e).__name__}: "
                f"{e}",

                flush=True,
            )


        # ================================================
        # task checkpoint
        # ================================================

        save_current_results(
            unique_models
        )

        print(
            f"Checkpoint saved -> "
            f"{OUTPUT_PATH}"
        )

        time.sleep(
            TASK_SLEEP_SECONDS
        )


    # =====================================================
    # FINAL SAVE
    # =====================================================

    results = list(
        unique_models.values()
    )

    results.sort(
        key=lambda x:
            x.get(
                "downloads"
            )
            or 0,
        reverse=True
    )

    save_json_atomic(
        results,
        OUTPUT_PATH
    )


    # =====================================================
    # STATISTICS
    # =====================================================

    def count_level(level):

        return sum(

            model[
                "language_support_level"
            ]
            == level

            for model
            in results
        )


    explicit_count = (
        count_level(
            "explicit"
        )
    )

    name_count = (
        count_level(
            "name_heuristic"
        )
    )

    multilingual_count = (
        count_level(
            "multilingual"
        )
    )

    family_count = (
        count_level(
            "family_heuristic"
        )
    )


    print()
    print("=" * 80)

    print(
        "STAGE 1 COLLECTION FINISHED"
    )

    print("=" * 80)


    print(
        f"Total scanned           : "
        f"{stats['total_seen']:,}"
    )

    print(
        f"Test models removed     : "
        f"{stats['excluded_test']:,}"
    )

    print(
        f"Low-download removed    : "
        f"{stats['excluded_downloads']:,}"
    )

    print(
        f"Non-language candidates : "
        f"{stats['non_language_candidate']:,}"
    )

    print(
        f"Unique candidates       : "
        f"{len(results):,}"
    )


    print()
    print(
        "Language candidate evidence"
    )


    print(
        f"  explicit Korean       : "
        f"{explicit_count:,}"
    )

    print(
        f"  Korean name heuristic : "
        f"{name_count:,}"
    )

    print(
        f"  multilingual tag      : "
        f"{multilingual_count:,}"
    )

    print(
        f"  family heuristic      : "
        f"{family_count:,}"
    )


    print()
    print(
        f"Saved -> "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()