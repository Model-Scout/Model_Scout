"""semantic_capability 질의 10개.

자연어로 원하는 능력과 용도를 설명하는 유형이다. 수치 조건이 없거나 적다.

★ 질의를 task명으로 쓰면 안 된다
  "한국어 텍스트 분류 모델 추천해줘"는 후보 105개 중 정답이 80개를 넘어 판정이
  불가능하고, 아무거나 뽑아도 Recall이 높아 측정 의미가 없다. 용도를 **구체적인
  업무 상황**으로 써야 정답이 3~8개로 수렴한다.

★ 판정은 3단으로만 한다 — 주관을 줄이기 위해
    1단 must  : 이 용도가 데이터에 명시돼 있나? 없으면 0점, 끝.
    2단 2점   : 도메인이 질의와 정확히 일치하나?
    3단 1점   : 더 넓거나 좁은 용도로 쓸 수 있나?

  핵심은 "쓸 수 있을 것 같다"를 2점으로 올리지 않는 것이다. 데이터에 그 용도가
  쓰여 있어야 2점이다. 희원님이 PR #17에서 1점을 재판정한 이유와 같다.

★ 이 유형은 어려움 비중을 낮췄다
  판정이 흔들리기 쉬우므로 쉬움을 많이 둔다. 어려운 질의를 많이 만들면 유형 간
  2점/1점 경계가 어긋난다.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from scan import Rule  # noqa: E402

CLS_CORE = {
    "tasks": ["text-classification"],
    "korean_required": True,
    "pools": ["core"],
}
CLS_CORE_FIDELITY = {
    "tasks": "분류 → text-classification",
    "korean_required": "한국어",
    "pools": "많이 쓰이는 → core (다운로드 500 이상)",
}
I2T_SMALL = {
    "tasks": ["image-text-to-text"],
    "korean_required": True,
    "max_parameters_billion": 1.0,
}
I2T_SMALL_FIDELITY = {
    "tasks": "이미지-텍스트",
    "korean_required": "한국어",
    "max_parameters_billion": "1B 이하",
}

SPECS = [
    {
        "query_id": "ca01",
        "query": "뉴스 기사를 짧게 줄여주는 한국어 모델이 필요해.",
        "conditions": {"tasks": ["summarization"], "korean_required": True},
        "fidelity": {"tasks": "줄여주는 → summarization", "korean_required": "한국어"},
        "rule": Rule(
            must_any=["news", "뉴스"],
            grade_2_any=["뉴스 요약", "news summar", "기사 요약"],
            weak_any=["article", "기사", "문서 요약"],
            must_label="뉴스·기사 도메인이 model_id 또는 claim에서 확인된다",
            grade_2_label="뉴스 기사 요약으로 학습·파인튜닝된 것이 명시돼 있다",
            grade_1_label="일반 문서 요약 모델로 뉴스에도 쓸 수 있으나 도메인 명시가 없다",
        ),
    },
    {
        "query_id": "ca02",
        "query": "지문을 주면 그 안에서 답을 찾아주는 한국어 모델을 찾고 있어.",
        "conditions": {"tasks": ["question-answering"], "korean_required": True},
        "fidelity": {
            "tasks": "답을 찾아주는 → question-answering",
            "korean_required": "한국어",
        },
        "rule": Rule(
            must_any=["korquad", "독해", "reading comprehension", "extractive"],
            grade_2_any=["korquad", "한국어 독해", "기계독해"],
            weak_any=["squad", "mrc", "span"],
            must_label="지문에서 답을 추출하는 용도가 확인된다",
            grade_2_label="KorQuAD 등 한국어 독해 데이터로 학습됐다",
            grade_1_label="다국어 QA 모델이거나 SQuAD 기반으로 한국어를 포함한다",
        ),
    },
    {
        "query_id": "ca03",
        "query": "고객 문의가 어떤 요청인지 자동으로 갈라주는 한국어 모델이 필요해. 많이 쓰이는 것으로.",
        "conditions": CLS_CORE,
        "fidelity": CLS_CORE_FIDELITY,
        "rule": Rule(
            must_any=["intent", "의도", "고객", "문의"],
            grade_2_any=["intent classif", "의도 분류", "고객 문의"],
            weak_any=["customer", "topic", "category"],
            must_label="의도·문의 분류 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="고객 문의·의도 분류 전용으로 학습된 것이 명시돼 있다",
            grade_1_label="주제·범주 분류 모델로 문의 분류에도 쓸 수 있으나 명시가 없다",
        ),
    },
    {
        "query_id": "ca04",
        "query": "상품 리뷰가 좋은 말인지 나쁜 말인지 가려내는 한국어 모델을 추천해줘. 많이 쓰이는 것으로.",
        "conditions": CLS_CORE,
        "fidelity": CLS_CORE_FIDELITY,
        "rule": Rule(
            must_any=["sentiment", "감성", "리뷰", "nsmc"],
            grade_2_any=["nsmc", "한국어 감성", "리뷰 감성", "korean sentiment"],
            weak_any=["emotion", "polarity", "positive"],
            must_label="감성 분류 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="NSMC 등 한국어 리뷰 감성 데이터로 학습됐다",
            grade_1_label="다국어 감성 분류이거나 도메인이 리뷰가 아닌 일반 감성 분류",
        ),
    },
    {
        "query_id": "ca05",
        "query": "댓글에서 남을 공격하는 표현을 걸러내는 한국어 모델이 필요해. 많이 쓰이는 것으로.",
        "conditions": CLS_CORE,
        "fidelity": CLS_CORE_FIDELITY,
        "rule": Rule(
            must_any=["hate", "혐오", "욕설", "unsmile"],
            grade_2_any=["unsmile", "한국어 혐오", "korean hate", "beep"],
            weak_any=["toxic", "offensive", "abusive"],
            must_label="혐오·욕설 탐지 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="UnSmile 등 한국어 혐오 표현 데이터로 학습됐다",
            grade_1_label="다국어 유해성 분류이거나 일반 세이프티 분류 모델",
        ),
    },
    {
        "query_id": "ca06",
        "query": "광고나 스팸 글을 걸러내는 한국어 모델 있어? 많이 쓰이는 것으로.",
        "conditions": CLS_CORE,
        "fidelity": CLS_CORE_FIDELITY,
        "rule": Rule(
            must_any=["spam", "스팸", "광고", "advertis"],
            grade_2_any=["spam", "스팸", "광고 분류"],
            weak_any=["filter", "moderation", "junk"],
            must_label="스팸·광고 탐지 용도가 claim 또는 model_id에서 확인된다",
            grade_2_label="스팸·광고 분류 전용으로 학습된 것이 명시돼 있다",
            grade_1_label="일반 필터링·모더레이션 모델로 스팸에도 쓸 수 있으나 명시가 없다",
        ),
    },
    {
        "query_id": "ca07",
        "query": "같은 뜻을 다르게 쓴 문장을 찾아내는 한국어 모델이 필요해. 많이 쓰이는 것으로.",
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
            must_any=["paraphrase", "중복", "duplicate"],
            grade_2_any=["paraphrase", "중복 문장", "paraphrase identification"],
            must_label="패러프레이즈·중복 문장 탐지 용도가 확인된다",
            grade_2_label="패러프레이즈 탐지로 학습된 것이 명시돼 있다",
            grade_1_label="일반 문장 유사도 모델로 중복 탐지에도 쓸 수 있으나 명시가 없다",
        ),
    },
    {
        "query_id": "ca08",
        "query": "긴 회의 녹음을 전사할 한국어 모델을 찾고 있어. 일반 음성 인식이 아니라 회의·장문 전사 용도가 명시된 모델 중에서, 많이 쓰이는 1B 이하 모델로.",
        "conditions": {
            "tasks": ["automatic-speech-recognition"],
            "korean_required": True,
            "pools": ["core"],
            "max_parameters_billion": 1.0,
        },
        "fidelity": {
            "tasks": "받아 적어주는 → automatic-speech-recognition",
            "korean_required": "한국어",
            "pools": "많이 쓰이는 → core",
            "max_parameters_billion": "1B 이하",
        },
        "rule": Rule(
            must_any=["회의", "meeting", "long-form", "longform", "meeting transcription"],
            grade_2_any=["회의", "meeting", "long-form"],
            weak_any=[],
            must_label="회의·장문 음성 전사 용도가 확인된다",
            grade_2_label="회의·장문 전사 용도가 명시돼 있다",
            grade_1_label="일반 한국어 전사 모델로 회의에도 쓸 수 있으나 도메인 명시가 없다",
        ),
    },
    {
        "query_id": "ca09",
        "query": "사진 속 글자를 읽어서 한국어로 알려주는 모델이 필요해. 파라미터 1B 이하인 것으로.",
        "conditions": I2T_SMALL,
        "fidelity": I2T_SMALL_FIDELITY,
        "rule": Rule(
            must_any=["ocr", "문서", "document"],
            grade_2_any=["korean ocr", "한국어 ocr", "document understanding"],
            weak_any=["chart", "table", "caption"],
            must_label="이미지 속 글자 인식 용도가 확인된다",
            grade_2_label="한국어 OCR·문서 이해로 학습된 것이 명시돼 있다",
            grade_1_label="다국어 VLM으로 글자 인식이 가능하나 한국어 특화 명시가 없다",
        ),
    },
    {
        "query_id": "ca10",
        "query": "표나 그래프가 든 이미지를 읽고 설명해주는 한국어 모델 있어? 파라미터 1B 이하인 것으로.",
        "conditions": I2T_SMALL,
        "fidelity": I2T_SMALL_FIDELITY,
        "rule": Rule(
            must_any=["chart", "table", "표", "도표"],
            grade_2_any=["chart", "chartqa", "table understanding", "도표"],
            weak_any=["diagram", "plot", "figure"],
            must_label="표·차트 이해 용도가 확인된다",
            grade_2_label="차트·표 이해로 학습된 것이 명시돼 있다",
            grade_1_label="일반 VLM으로 표를 읽을 수 있으나 차트 특화 명시가 없다",
        ),
    },
]
