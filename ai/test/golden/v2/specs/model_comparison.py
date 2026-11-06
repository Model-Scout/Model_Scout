"""model_comparison 질의 10개.

질의에 모델 이름이 직접 등장하고, 정답은 그 이름에 해당하는 모델들이다.

★ 모델명도 HARD_FILTER_KEYS에 없다
  benchmark_lookup과 같은 구조다. task와 수치로 후보를 잡고 이름은 ①단계
  (model_id + canonical_model_id) 규칙으로 처리한다. README에서 "BGE-M3보다
  좋다"고 언급한 MILCO 같은 다른 모델을 BGE 계열로 오인하지 않는다.

★ 변종 처리가 이 유형의 유일한 쟁점이다
  "KoBART"를 물으면 원본만인가, 파인튜닝·변환본까지인가. 코퍼스에는 kobart 4개,
  kobert 4개, kot5 1개처럼 같은 계열이 여러 개 있다. 기준을 이렇게 고정했다.

    2점 — 질의가 지목한 계열의 모델이고, 그 task 용도가 확인된다
    1점 — 같은 계열이나 다른 task용 파인튜닝이거나, 변환본·양자화본·재업로드

  `expected_all`이 아니라 `expected_any`로 둔다. 코퍼스에 계열마다 여러 개가
  있어 "정확히 이 둘"을 지목할 수 없고, 사람이 2점/1점을 정한 뒤에 확정한다.
  단, 비교 질의는 이름이 나온 **각 계열마다** 최종 정답이 하나 이상 있어야 한다.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

SPECS = [
    {
        "query_id": "mc01",
        "query": "KoBART랑 KoT5 중에 한국어 요약에 뭐가 더 나아?",
        "conditions": {"tasks": ["summarization"], "korean_required": True},
        "fidelity": {"tasks": "요약", "korean_required": "한국어"},
        "rule": Rule(
            must_any=["kobart", "kot5", "ko-t5"],
            grade_2_any=["kobart", "kot5", "ko-t5"],
            weak_any=[],
            must_label="model_id가 KoBART 또는 KoT5 계열이다",
            grade_2_label="그 계열이고 요약 용도가 확인된다",
            grade_1_label="같은 계열이나 다른 task용이거나 변환본·재업로드",
            comparison_groups={"KoBART": ("kobart",), "KoT5": ("kot5", "ko-t5")},
        ),
    },
    {
        "query_id": "mc02",
        "query": "KoBERT와 KoSimCSE 중 한국어 문장 임베딩·검색에는 어떤 계열이 더 맞아? 많이 쓰이는 모델로.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "문장 임베딩·검색 → feature-extraction",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
        },
        "rule": Rule(
            must_any=["kobert", "kosimcse", "ko-simcse"],
            grade_2_any=["kobert", "kosimcse", "ko-simcse"],
            weak_any=[],
            must_label="model_id가 KoBERT 또는 KoSimCSE 계열이다",
            # KoBERT 원본은 한국어 사전학습 BERT라 hidden state를 꺼낼 수는 있어도,
            # 문장 임베딩·검색용으로 직접 학습되었다는 근거가 없다. 반면 KoSimCSE는
            # 그 용도가 명시된 계열이므로 이 비교에서는 그쪽만 자동 2점 후보로 둔다.
            grade_2_label="KoSimCSE 계열로, 임베딩·검색 용도가 직접 확인된다",
            grade_1_label="KoBERT 원본처럼 임베딩·검색 용도가 불명확하거나 변환본·재업로드",
            comparison_groups={"KoBERT": ("kobert",), "KoSimCSE": ("kosimcse", "ko-simcse")},
            comparison_grade_2_groups=("KoSimCSE",),
        ),
    },
    {
        "query_id": "mc03",
        "query": "ko-sroberta와 KoSBERT 중 한국어 문장 유사도에는 어느 쪽이 더 맞아? 많이 쓰이는 모델로.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["ko-sroberta", "ko-sbert"],
            grade_2_any=["ko-sroberta", "ko-sbert"],
            weak_any=[],
            must_label="model_id가 ko-sroberta 또는 KoSBERT 계열이다",
            grade_2_label="한국어 전용(ko- 접두) 계열이다",
            grade_1_label="다국어 계열이거나 변환본",
            comparison_groups={"ko-sroberta": ("ko-sroberta",), "KoSBERT": ("ko-sbert",)},
        ),
    },
    {
        "query_id": "mc04",
        "query": "BGE랑 multilingual-E5 중에 한국어 임베딩에 뭐가 나아? 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "임베딩 → feature-extraction",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
        },
        "rule": Rule(
            must_any=["bge-m3", "multilingual-e5"],
            grade_2_any=["bge-m3", "multilingual-e5"],
            weak_any=[],
            must_label="model_id가 BGE 또는 E5 계열이다",
            grade_2_label="BGE-M3 또는 multilingual-E5 본체다",
            grade_1_label="같은 계열의 파인튜닝·변환본이거나 단일 언어 변형",
            comparison_groups={"BGE-M3": ("bge-m3",), "multilingual-E5": ("multilingual-e5",)},
        ),
    },
    {
        "query_id": "mc05",
        "query": "KURE와 BGE-M3를 한국어 검색에 쓰면 어느 쪽이 좋아? 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "검색용 임베딩 → feature-extraction",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["kure", "bge-m3"],
            grade_2_any=["kure", "bge-m3"],
            weak_any=[],
            must_label="model_id가 KURE 또는 BGE-M3 계열이다",
            grade_2_label="그 계열의 본체다",
            grade_1_label="같은 계열의 파인튜닝·변환본이거나 양자화본",
            comparison_groups={"KURE": ("kure",), "BGE-M3": ("bge-m3",)},
        ),
    },
    {
        "query_id": "mc06",
        "query": "KoGPT랑 Polyglot-Ko 비교해줘. 많이 쓰이는 한국어 생성 모델로.",
        "conditions": {
            "tasks": ["text-generation"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "생성 → text-generation",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["kogpt", "polyglot"],
            grade_2_any=["kogpt", "polyglot-ko"],
            weak_any=[],
            must_label="model_id가 KoGPT 또는 Polyglot 계열이다",
            grade_2_label="한국어 전용 계열(KoGPT, Polyglot-Ko)이다",
            grade_1_label="다국어 Polyglot이거나 파인튜닝·변환본",
            comparison_groups={"KoGPT": ("kogpt",), "Polyglot-Ko": ("polyglot-ko",)},
        ),
    },
    {
        "query_id": "mc07",
        "query": "NLLB와 mBART 중에 한국어 번역에 뭐가 나아? 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "번역",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
        },
        "rule": Rule(
            must_any=["nllb", "mbart"],
            grade_2_any=["nllb-200", "mbart-large"],
            weak_any=[],
            must_label="model_id가 NLLB 또는 mBART 계열이다",
            grade_2_label="그 계열의 본체다",
            grade_1_label="같은 계열의 파인튜닝·증류·변환본",
            comparison_groups={"NLLB": ("nllb",), "mBART": ("mbart",)},
        ),
    },
    {
        "query_id": "mc08",
        "query": "Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 좋아? 1B 이하인 것 중 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 1.0,
        },
        "fidelity": {
            "tasks": "음성 인식",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "1B 이하",
        },
        "rule": Rule(
            must_any=["whisper-small", "whisper_small", "wav2vec"],
            grade_2_any=["whisper-small", "wav2vec2"],
            # Whisper medium/tiny와 HuBERT는 사용자가 지목한 비교 대상이 아니다.
            # 약한 후보로 올리면 모델명을 직접 비교하는 질의의 정답 범위를 부당하게 넓힌다.
            weak_any=[],
            must_label="model_id가 Whisper small 또는 wav2vec 계열이다",
            grade_2_label="그 계열이고 한국어 파인튜닝이 확인된다",
            grade_1_label="다른 크기의 Whisper이거나 변환본·양자화본",
            comparison_groups={
                "Whisper small": ("whisper-small", "whisper_small"),
                "wav2vec": ("wav2vec",),
            },
        ),
    },
    {
        "query_id": "mc09",
        "query": "opus-mt와 M2M100 중에 한국어가 포함된 다국어 번역에는 어떤 모델이 더 맞아?",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
        },
        "fidelity": {
            "tasks": "한국어가 포함된 다국어 번역 → translation",
            "korean_required": "한국어",
        },
        "rule": Rule(
            must_any=["opus-mt", "opus_mt", "m2m100", "m2m-100"],
            grade_2_any=["opus-mt", "m2m100"],
            weak_any=[],
            must_label="model_id가 opus-mt 또는 M2M100 계열이다",
            grade_2_label="그 계열의 본체이고 한국어 방향이 확인된다",
            grade_1_label="같은 계열이나 한국어 방향이 불명확하거나 변환본",
            comparison_groups={"opus-mt": ("opus-mt", "opus_mt"), "M2M100": ("m2m100", "m2m-100")},
        ),
    },
    {
        "query_id": "mc10",
        "query": "KoELECTRA와 mDeBERTa 중에 한국어 질의응답에 뭐가 나아?",
        "conditions": {"tasks": ["question-answering"], "korean_required": True},
        "fidelity": {"tasks": "질의응답", "korean_required": "한국어"},
        "rule": Rule(
            must_any=["koelectra", "mdeberta"],
            grade_2_any=["koelectra"],
            weak_any=[],
            must_label="model_id가 KoELECTRA 또는 mDeBERTa 계열이다",
            grade_2_label="한국어 전용 계열(KoELECTRA)이고 질의응답 용도가 확인된다",
            grade_1_label="다국어 계열(mDeBERTa)이거나 다른 task용 파인튜닝",
            comparison_groups={"KoELECTRA": ("koelectra",), "mDeBERTa": ("mdeberta",)},
            comparison_grade_2_groups=("KoELECTRA",),
        ),
    },
]
