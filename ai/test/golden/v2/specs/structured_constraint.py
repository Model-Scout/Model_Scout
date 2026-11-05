"""structured_constraint 질의 10개.

이 유형은 Task + 파라미터 수 + 컨텍스트 길이 같은 구조화 조건이 중심이다. 조건
충족 여부는 하드 필터가 이미 걸러주므로, 판정에 남는 것은 **용도 적합성**뿐이다.
그래서 2점/1점 기준이 유형 전체에 걸쳐 같다.

    2점 — 그 task 전용으로 만들어진 모델 (모델명·claim이 그 용도를 말한다)
    1점 — 조건은 충족하나 범용 모델이고 그 task가 부가 기능이거나,
          도메인이 질의보다 좁거나 넓거나, 변환본·재업로드

조건은 전부 질의문에 근거가 있다. require_known_*는 질의가 "스펙이 공개된",
"파라미터 수가 명시된"처럼 값의 공개를 요구할 때만 켠다. 코퍼스의 파라미터
39.4%, 컨텍스트 37.7%가 미공개이므로 이 플래그를 후보 축소에 쓰면 정답이
통째로 사라진다.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

# task 전용 모델을 가리키는 말과, 범용/다른 용도를 가리키는 말을 분리해 둔다.
SPECS = [
    {
        "query_id": "sc01",
        "query": "3B 이하 한국어 요약 모델을 찾고 있어.",
        "conditions": {
            "tasks": ["summarization"],
            "korean_required": True,
            "max_parameters_billion": 3.0,
        },
        "fidelity": {
            "tasks": "요약",
            "korean_required": "한국어",
            "max_parameters_billion": "3B 이하",
        },
        "rule": Rule(
            must_any=["summar", "요약", "xlsum", "crosssum", "sum"],
            grade_2_any=["kobart", "kot5", "korean summar", "한국어 요약",
                         "요약 모델", "summarization"],
            weak_any=["bart", "t5", "seq2seq", "text2text", "key-point", "key_point"],
            must_label="요약 용도가 model_id / filter_metadata / claim에서 확인된다",
            grade_2_label="한국어 요약 전용으로 학습·파인튜닝된 모델",
            grade_1_label="다국어 요약 모델이거나, 요약이 부가 기능인 범용 생성 모델",
        ),
    },
    {
        "query_id": "sc02",
        "query": "파라미터 1B 이하인 한국어 질의응답 모델이 필요해.",
        "conditions": {
            "tasks": ["question-answering"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
        },
        "fidelity": {
            "tasks": "질의응답",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 1B 이하",
        },
        "rule": Rule(
            must_any=["qa", "question", "질의응답", "질문", "squad", "korquad", "mrc"],
            grade_2_any=["korquad", "한국어 질의응답", "korean qa", "extractive",
                         "기계독해", "독해"],
            weak_any=["bert", "roberta", "electra", "answer", "응답"],
            must_label="질의응답 용도가 model_id / filter_metadata / claim에서 확인된다",
            grade_2_label="KorQuAD 등 한국어 QA 데이터로 학습된 전용 모델",
            grade_1_label="다국어 QA 모델이거나, QA가 부가 기능인 범용 인코더",
        ),
    },
    {
        "query_id": "sc03",
        "query": "긴 문서를 다뤄야 해서 컨텍스트 32768 토큰 이상인 한국어 텍스트 분류 모델을 찾아줘.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "min_context_length": 32768,
        },
        "fidelity": {
            "tasks": "텍스트 분류",
            "korean_required": "한국어",
            "min_context_length": "컨텍스트 32768 토큰 이상",
        },
        "rule": Rule(
            must_any=["classif", "분류", "sentiment", "감성", "label", "category",
                      "intent", "topic", "rerank", "reward"],
            grade_2_any=["한국어 분류", "korean classif", "감성 분석",
                         "sentiment analysis", "text-classification"],
            weak_any=["bert", "roberta", "electra", "embedding", "score"],
            must_label="분류 용도가 model_id / filter_metadata / claim에서 확인된다",
            grade_2_label="한국어 텍스트 분류 전용으로 학습된 모델",
            grade_1_label="다국어 분류 모델이거나, 분류 헤드가 붙은 범용 인코더",
        ),
    },
    {
        "query_id": "sc04",
        "query": "컨텍스트 131072 토큰 이상인 한국어 텍스트 분류 모델이 있을까?",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "min_context_length": 131072,
        },
        "fidelity": {
            "tasks": "텍스트 분류",
            "korean_required": "한국어",
            "min_context_length": "컨텍스트 131072 토큰 이상",
        },
        "rule": Rule(
            must_any=["classif", "분류", "sentiment", "감성", "label", "intent",
                      "topic", "rerank", "reward", "guard", "safety"],
            grade_2_any=["한국어 분류", "korean classif", "감성 분석",
                         "text-classification"],
            weak_any=["bert", "roberta", "electra", "embedding", "score"],
            must_label="분류 용도가 model_id / filter_metadata / claim에서 확인된다",
            grade_2_label="한국어 텍스트 분류 전용으로 학습된 모델",
            grade_1_label="다국어 분류 모델이거나, 분류 헤드가 붙은 범용 인코더",
        ),
    },
    {
        "query_id": "sc05",
        "query": "많이 쓰이는 모델 중에서 컨텍스트 32768 토큰 이상인 한국어 문장 유사도 모델을 추천해줘.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "pools": ["core"],
            "min_context_length": 32768,
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
            "min_context_length": "컨텍스트 32768 토큰 이상",
        },
        "rule": Rule(
            must_any=["sentence", "similar", "유사도", "embed", "임베딩", "sbert",
                      "sroberta", "simcse", "e5", "bge", "retriev", "검색"],
            grade_2_any=["ko-sroberta", "ko-sbert", "한국어 임베딩", "korean sentence",
                         "kure", "ko-simcse", "sentence-similarity"],
            weak_any=["bert", "roberta", "encoder", "vector", "dense"],
            must_label="문장 임베딩·유사도 용도가 확인된다",
            grade_2_label="한국어 문장 임베딩 전용으로 학습된 모델",
            grade_1_label="다국어 임베딩 모델이거나, 임베딩이 부가 용도인 범용 인코더",
        ),
    },
    {
        "query_id": "sc06",
        "query": "파라미터 수가 명시된 것 중에 100M 이하인 한국어 음성 인식 모델을 찾고 있어.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "음성 인식",
            "korean_required": "한국어",
            "max_parameters_billion": "100M 이하",
            "require_known_parameters": "파라미터 수가 명시된 것",
        },
        "rule": Rule(
            must_any=["asr", "speech", "음성", "whisper", "wav2vec", "stt",
                      "transcri", "voice", "audio"],
            grade_2_any=["korean speech", "한국어 음성", "ko-whisper", "zeroth",
                         "ksponspeech", "automatic-speech-recognition"],
            weak_any=["tiny", "base", "small", "encoder", "ctc"],
            must_label="음성 인식 용도가 확인된다",
            grade_2_label="한국어 음성 데이터로 학습·파인튜닝된 전용 모델",
            grade_1_label="다국어 ASR 모델이거나 한국어가 포함된 범용 음성 모델",
        ),
    },
    {
        "query_id": "sc07",
        "query": "파라미터 1B 이하로 공개된 한국어 이미지-텍스트 모델을 추천해줘.",
        "conditions": {
            "tasks": ["image-text-to-text"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "이미지-텍스트",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 1B 이하",
            "require_known_parameters": "로 공개된",
        },
        "rule": Rule(
            must_any=["vl", "vision", "image", "이미지", "ocr", "multimodal",
                      "멀티모달", "caption", "chart", "doc"],
            grade_2_any=["korean vl", "한국어 비전", "kollava", "ko-vl",
                         "image-text-to-text", "한국어 멀티모달"],
            weak_any=["qwen", "llava", "intern", "gemma", "phi"],
            must_label="이미지 입력을 받는 용도가 확인된다",
            grade_2_label="한국어 이미지-텍스트 전용으로 학습된 모델",
            grade_1_label="다국어 VLM으로 한국어를 포함하거나, 변환본·양자화본",
        ),
    },
    {
        "query_id": "sc08",
        "query": "파라미터 수가 공개된 100M 이하 한국어 임베딩 모델이 필요해.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "임베딩 → feature-extraction",
            "korean_required": "한국어",
            "max_parameters_billion": "100M 이하",
            "require_known_parameters": "파라미터 수가 공개된",
        },
        "rule": Rule(
            must_any=["embed", "임베딩", "feature", "vector", "sbert", "sroberta",
                      "simcse", "e5", "bge", "retriev"],
            grade_2_any=["한국어 임베딩", "korean embed", "ko-sroberta", "ko-sbert",
                         "kure", "feature-extraction"],
            weak_any=["bert", "roberta", "electra", "encoder", "pooling"],
            must_label="임베딩·특징 추출 용도가 확인된다",
            grade_2_label="한국어 임베딩 전용으로 학습된 모델",
            grade_1_label="다국어 임베딩 모델이거나, 임베딩이 부가 용도인 범용 인코더",
        ),
    },
    {
        "query_id": "sc09",
        "query": "파라미터 100M 이하로 명시된 한국어 문장 유사도 모델을 찾아줘.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
            "require_known_parameters": True,
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 100M 이하",
            "require_known_parameters": "로 명시된",
        },
        "rule": Rule(
            must_any=["sentence", "similar", "유사도", "sbert", "sroberta", "simcse",
                      "embed", "임베딩", "e5", "bge"],
            grade_2_any=["ko-sroberta", "ko-sbert", "한국어 문장", "korean sentence",
                         "ko-simcse", "sentence-similarity", "klue-sts", "kakaobank"],
            weak_any=["bert", "roberta", "electra", "minilm", "encoder"],
            must_label="문장 유사도 용도가 확인된다",
            grade_2_label="한국어 STS 데이터로 학습된 전용 모델",
            grade_1_label="다국어 문장 임베딩 모델이거나 범용 인코더",
        ),
    },
    {
        "query_id": "sc10",
        "query": "많이 쓰이는 한국어 요약 모델을 추천해줘.",
        "conditions": {
            "tasks": ["summarization"],
            "korean_required": True,
            "pools": ["core"],
        },
        "fidelity": {
            "tasks": "요약",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
        },
        "rule": Rule(
            must_any=["summar", "요약", "xlsum", "crosssum", "sum"],
            grade_2_any=["kobart", "kot5", "한국어 요약", "korean summar",
                         "summarization"],
            weak_any=["bart", "t5", "seq2seq", "text2text"],
            must_label="요약 용도가 확인된다",
            grade_2_label="한국어 요약 전용으로 학습·파인튜닝된 모델",
            grade_1_label="다국어 요약 모델이거나, 요약이 부가 기능인 범용 생성 모델",
        ),
    },
]
