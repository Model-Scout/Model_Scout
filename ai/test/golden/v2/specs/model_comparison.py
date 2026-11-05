"""model_comparison 질의 10개.

질의에 모델 이름이 직접 등장하고, 정답은 그 이름에 해당하는 모델들이다.

★ 모델명도 HARD_FILTER_KEYS에 없다
  benchmark_lookup과 같은 구조다. task와 수치로 후보를 잡고 이름은 ①단계
  (model_id) 규칙으로 처리한다. 그래서 ✅ 오답 더미가 대부분을 흡수한다.

★ 변종 처리가 이 유형의 유일한 쟁점이다
  "KoBART"를 물으면 원본만인가, 파인튜닝·변환본까지인가. 코퍼스에는 kobart 4개,
  kobert 4개, kot5 1개처럼 같은 계열이 여러 개 있다. 기준을 이렇게 고정했다.

    2점 — 질의가 지목한 계열의 모델이고, 그 task 용도가 확인된다
    1점 — 같은 계열이나 다른 task용 파인튜닝이거나, 변환본·양자화본·재업로드

  `expected_all`이 아니라 `expected_any`로 둔다. 코퍼스에 계열마다 여러 개가
  있어 "정확히 이 둘"을 지목할 수 없고, 사람이 2점/1점을 정한 뒤에 확정한다.
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
            weak_any=["bart", "t5"],
            must_label="model_id가 KoBART 또는 KoT5 계열이다",
            grade_2_label="그 계열이고 요약 용도가 확인된다",
            grade_1_label="같은 계열이나 다른 task용이거나 변환본·재업로드",
        ),
    },
    {
        "query_id": "mc02",
        "query": "KoELECTRA와 KoBERT를 한국어 텍스트 분류에 쓸 때 어느 쪽이 좋아? 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "텍스트 분류",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
        },
        "rule": Rule(
            must_any=["koelectra", "kobert"],
            grade_2_any=["koelectra", "kobert"],
            weak_any=["distilkobert"],
            must_label="model_id가 KoELECTRA 또는 KoBERT 계열이다",
            grade_2_label="그 계열이고 분류 용도가 확인된다",
            grade_1_label="같은 계열이나 다른 task용이거나 경량화·변환본",
        ),
    },
    {
        "query_id": "mc03",
        "query": "ko-sroberta랑 KoSimCSE 비교해줘. 많이 쓰이는 한국어 문장 유사도 모델로.",
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
            must_any=["sroberta", "simcse"],
            grade_2_any=["ko-sroberta", "kosimcse", "ko-simcse"],
            weak_any=["ko-sbert"],
            must_label="model_id가 sroberta 또는 SimCSE 계열이다",
            grade_2_label="한국어 전용(ko- 접두) 계열이다",
            grade_1_label="다국어 계열이거나 변환본",
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
            weak_any=["bge-large", "e5-large"],
            must_label="model_id가 BGE 또는 E5 계열이다",
            grade_2_label="BGE-M3 또는 multilingual-E5 본체다",
            grade_1_label="같은 계열의 파인튜닝·변환본이거나 단일 언어 변형",
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
            weak_any=["bge"],
            must_label="model_id가 KURE 또는 BGE-M3 계열이다",
            grade_2_label="그 계열의 본체다",
            grade_1_label="같은 계열의 파인튜닝·변환본이거나 양자화본",
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
            weak_any=["gpt-neox", "gpt2"],
            must_label="model_id가 KoGPT 또는 Polyglot 계열이다",
            grade_2_label="한국어 전용 계열(KoGPT, Polyglot-Ko)이다",
            grade_1_label="다국어 Polyglot이거나 파인튜닝·변환본",
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
            weak_any=["m2m", "opus-mt"],
            must_label="model_id가 NLLB 또는 mBART 계열이다",
            grade_2_label="그 계열의 본체다",
            grade_1_label="같은 계열의 파인튜닝·증류·변환본",
        ),
    },
    {
        "query_id": "mc08",
        "query": "Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 좋아? 1B 이하로 공개된 것 중 많이 쓰이는 것으로.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 1.0,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "음성 인식",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "1B 이하",
            "require_known_parameters": "로 공개된",
        },
        "rule": Rule(
            must_any=["whisper-small", "whisper_small", "wav2vec"],
            grade_2_any=["whisper-small", "wav2vec2"],
            weak_any=["whisper", "hubert"],
            must_label="model_id가 Whisper small 또는 wav2vec 계열이다",
            grade_2_label="그 계열이고 한국어 파인튜닝이 확인된다",
            grade_1_label="다른 크기의 Whisper이거나 변환본·양자화본",
        ),
    },
    {
        "query_id": "mc09",
        "query": "opus-mt와 m2m100 중에 한국어 번역에 뭐가 나아? 많이 쓰이는 것으로.",
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
            must_any=["opus-mt", "opus_mt", "m2m100", "m2m-100"],
            grade_2_any=["opus-mt", "m2m100"],
            weak_any=["marian", "m2m"],
            must_label="model_id가 opus-mt 또는 M2M100 계열이다",
            grade_2_label="그 계열의 본체이고 한국어 방향이 확인된다",
            grade_1_label="같은 계열이나 한국어 방향이 불명확하거나 변환본",
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
            weak_any=["electra", "deberta"],
            must_label="model_id가 KoELECTRA 또는 mDeBERTa 계열이다",
            grade_2_label="한국어 전용 계열(KoELECTRA)이고 질의응답 용도가 확인된다",
            grade_1_label="다국어 계열(mDeBERTa)이거나 다른 task용 파인튜닝",
        ),
    },
]
