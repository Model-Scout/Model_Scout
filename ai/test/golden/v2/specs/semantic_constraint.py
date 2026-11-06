"""semantic_constraint 질의 10개.

이 유형은 의미적 요구와 수치 조건이 AND로 걸린다.

★ 수치 조건은 하드 필터가, 의미 조건은 규칙이 처리한다
  "CPU에서 돌아가는", "상업용 가능한", "VRAM 8GB 이내" 같은 말은 HARD_FILTER_KEYS에
  없어서 후보를 좁히지 못한다(runtime_compatibility·license는 데이터에 있지만
  hard_filter가 읽지 않는다). 그래서 좁히는 조건은 반드시 필터가 읽는 키로 걸고,
  의미 조건은 2점/1점을 가르는 데 쓴다.

★ weak_any를 좁게 쓴다
  이 유형에서 ⚠️가 가장 쉽게 폭발한다. 처음에 'ce-', 'rank', 'embed', 'classif'
  같은 말을 넣었더니 후보 전체가 ⚠️로 올라왔다('ce-'는 아무 단어에나 걸린다).
  인접 개념 이름만 쓴다.

판정 기준
    2점 — 질의가 말한 용도·도메인이 데이터에서 그대로 확인된다
    1점 — 조건은 충족하나 도메인이 더 좁거나 넓다 / 근거가 claim에 없다 /
          변환본·재업로드다
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

SPECS = [
    {
        "query_id": "sm01",
        # 처음엔 "법률이나 의료 같은 전문 분야"로 썼더니 사람이 볼 것이 35개가 됐다.
        # 도메인 셋을 묶으면 각 도메인의 후보가 다 올라온다. 하나로 좁혔다.
        "query": "의료 분야에 쓸 한국어 LLM이 필요해. 많이 쓰이는 것 중에 파라미터 4B 이하인 모델로.",
        "conditions": {
            "tasks": ["text-generation"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 4.0,
        },
        "fidelity": {
            "tasks": "LLM → text-generation",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
            "max_parameters_billion": "4B 이하",
        },
        "rule": Rule(
            # 'bio'·'health'는 "biology", "healthcare" 외에도 넓게 걸려 ⚠️를 키운다.
            must_any=["medical", "의료", "clinical", "진료", "임상", "의학"],
            grade_2_any=["korean medical", "한국어 의료", "의료 도메인", "clinical",
                         "의학", "진료"],
            weak_any=["domain", "전문", "specialized"],
            must_label="의료 도메인 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="한국어 의료 데이터로 특화 학습된 것이 명시돼 있다",
            grade_1_label="의료를 언급하나 다국어 모델이거나, 의료가 부가 기능인 범용 모델",
        ),
    },
    {
        "query_id": "sm02",
        "query": "실시간으로 받아쓰기를 해야 해. 스트리밍·저지연 처리를 지원하는 한국어 음성 인식 모델 중 파라미터 100M 이하인 것을 찾고 있어.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
        },
        "fidelity": {
            "tasks": "음성 인식",
            "korean_required": "한국어",
            "max_parameters_billion": "온디바이스에서 … 파라미터 100M 이하",
        },
        "rule": Rule(
            must_any=["streaming", "realtime", "real-time", "실시간", "online", "low latency", "저지연"],
            grade_2_any=["streaming", "실시간", "low latency", "저지연"],
            # CTC는 모델 구조이지 스트리밍 지원 자체의 증거는 아니다.
            weak_any=[],
            must_label="스트리밍·실시간 처리 지원이 claim에 명시돼 있다",
            grade_2_label="스트리밍·실시간 용도가 명시돼 있다",
            grade_1_label="실시간 처리 근거는 있으나 지연시간·지원 방식이 불명확하다",
        ),
    },
    {
        "query_id": "sm03",
        "query": "한국어를 영어로 번역하는 경량 모델이 필요해. 파라미터 500M 이하인 것으로.",
        "conditions": {
            "tasks": ["translation"],
            "korean_required": True,
            "max_parameters_billion": 0.5,
        },
        "fidelity": {
            "tasks": "번역",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 500M 이하",
        },
        "rule": Rule(
            must_any=["ko-en", "ko2en", "한영", "korean-english", "ko_en", "kor2eng"],
            grade_2_any=["ko-en", "ko2en", "한영", "korean to english"],
            weak_any=["en-ko", "en2ko", "영한", "m2m", "nllb", "mbart"],
            must_label="한국어→영어 방향이 model_id 또는 claim에서 확인된다",
            grade_2_label="ko→en 방향이 명시돼 있다",
            grade_1_label="다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다",
        ),
    },
    {
        "query_id": "sm04",
        "query": "한국어 기계독해용 모델을 찾고 있어. 파라미터 1B 이하로.",
        "conditions": {
            "tasks": ["question-answering"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
        },
        "fidelity": {
            "tasks": "기계독해 → question-answering",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 1B 이하",
        },
        "rule": Rule(
            must_any=["korquad", "기계독해", "extractive", "독해", "reading comprehension"],
            grade_2_any=["korquad", "기계독해", "한국어 독해"],
            weak_any=["squad", "mrc", "span"],
            must_label="추출형 기계독해 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="KorQuAD 등 한국어 독해 데이터로 학습됐다",
            grade_1_label="다국어 QA 모델이거나 SQuAD 기반이고 한국어를 포함한다",
        ),
    },
    {
        "query_id": "sm05",
        "query": "아주 긴 입력을 받아서 안전성이나 품질을 평가하는 한국어 모델이 필요해. 컨텍스트 131072 토큰 이상인 것으로.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "min_context_length": 131072,
        },
        "fidelity": {
            "tasks": "평가·분류 → text-classification",
            "korean_required": "한국어",
            "min_context_length": "컨텍스트 131072 토큰 이상",
        },
        "rule": Rule(
            must_any=["rerank", "reward", "guard", "safety", "moderation", "안전",
                      "품질", "judge", "verifier"],
            grade_2_any=["reward model", "safety", "guard", "한국어 안전", "moderation"],
            weak_any=["score", "ranking", "preference"],
            must_label="안전성·품질 평가 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="보상 모델·세이프티 분류 등 평가 전용으로 만들어졌다",
            grade_1_label="점수를 내는 모델이나 안전성·품질 평가 용도가 명시되지 않았다",
        ),
    },
    {
        "query_id": "sm06",
        "query": "문서나 표를 읽어야 해서 OCR이 되는 한국어 이미지-텍스트 모델을 찾아줘. 파라미터 1B 이하인 것으로.",
        "conditions": {
            "tasks": ["image-text-to-text"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
        },
        "fidelity": {
            "tasks": "이미지-텍스트",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 1B 이하",
        },
        "rule": Rule(
            must_any=["ocr", "document", "문서", "receipt"],
            grade_2_any=["korean ocr", "한국어 ocr", "document understanding",
                         "문서 이해"],
            weak_any=["chart", "table", "표", "caption", "vqa", "grounding"],
            must_label="문서·표·OCR 처리 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="한국어 문서·OCR 전용으로 학습된 것이 명시돼 있다",
            grade_1_label="다국어 VLM으로 문서 처리가 가능하나 한국어 특화 명시가 없다",
        ),
    },
    {
        "query_id": "sm07",
        "query": "RAG에 쓸 한국어 검색용 임베딩 모델이 필요해. 파라미터 100M 이하인 것으로.",
        "conditions": {
            "tasks": ["feature-extraction"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
        },
        "fidelity": {
            "tasks": "임베딩 → feature-extraction",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 100M 이하",
        },
        "rule": Rule(
            must_any=["retriev", "rag", "passage", "검색", "search", "dpr"],
            grade_2_any=["한국어 검색", "korean retriev", "rag", "passage retrieval"],
            weak_any=["sts", "similar", "유사도"],
            must_label="검색·RAG 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="한국어 검색·RAG 용도로 학습된 것이 명시돼 있다",
            grade_1_label="문장 유사도 모델로 검색에도 쓸 수 있으나 검색 용도 명시가 없다",
        ),
    },
    {
        "query_id": "sm08",
        "query": "두 문장이 얼마나 비슷한지 점수를 내는 한국어 모델이 필요해. 파라미터 100M 이하인 것으로.",
        "conditions": {
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "max_parameters_billion": 0.1,
        },
        "fidelity": {
            "tasks": "문장 유사도",
            "korean_required": "한국어",
            "max_parameters_billion": "파라미터 100M 이하",
        },
        "rule": Rule(
            must_any=["sts", "유사도", "simcse", "paraphrase", "similarity"],
            grade_2_any=["korsts", "klue-sts", "한국어 유사도", "ko-sroberta", "ko-simcse"],
            weak_any=["retriev", "search", "embed"],
            must_label="문장 유사도 점수 산출 용도가 확인된다",
            grade_2_label="한국어 STS 데이터로 학습된 전용 모델",
            grade_1_label="다국어 문장 임베딩 모델이거나 검색 용도가 주된 모델",
        ),
    },
    {
        "query_id": "sm09",
        "query": "상품 리뷰의 감성을 분류하는 한국어 모델을 찾고 있어. 많이 쓰이는 것 중에 300M 이하인 것으로.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 0.3,
        },
        "fidelity": {
            "tasks": "분류 → text-classification",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
            "max_parameters_billion": "300M 이하",
        },
        "rule": Rule(
            must_any=["sentiment", "감성", "nsmc", "리뷰", "review", "emotion", "감정"],
            grade_2_any=["nsmc", "한국어 감성", "korean sentiment", "리뷰"],
            weak_any=["polarity", "binary", "positive"],
            must_label="감성 분류 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="NSMC 등 한국어 리뷰 감성 데이터로 학습됐다",
            grade_1_label="다국어 감성 분류 모델이거나, 도메인이 리뷰가 아닌 일반 감성 분류",
        ),
    },
    {
        "query_id": "sm10",
        "query": "혐오 표현이나 욕설을 걸러내는 한국어 모델이 필요해. 많이 쓰이는 것 중 파라미터 300M 이하인 것으로.",
        "conditions": {
            "tasks": ["text-classification"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 0.3,
        },
        "fidelity": {
            "tasks": "분류 → text-classification",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core (다운로드 500 이상)",
            "max_parameters_billion": "파라미터 300M 이하",
        },
        "rule": Rule(
            must_any=["hate", "혐오", "toxic", "욕설", "abusive", "offensive",
                      "unsmile", "비속어"],
            grade_2_any=["unsmile", "한국어 혐오", "korean hate", "욕설", "beep"],
            weak_any=["moderation", "safety", "guard"],
            must_label="혐오·욕설 탐지 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="UnSmile 등 한국어 혐오 표현 데이터로 학습됐다",
            grade_1_label="다국어 유해성 분류 모델이거나, 일반 세이프티 분류 모델",
        ),
    },
]
