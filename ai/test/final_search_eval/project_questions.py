"""프로젝트형 모델 질문 30개 — "~ 프로젝트를 하려는데 모델만 추천해줘".

운영에서 이런 질문은 recommend=true 라 project 경로(PROJECT_MODEL_SEARCH)로 검색된다. planner 가 역할(need)을
나누고, 역할마다 모델을 찾는다. 그래서 정답도 질문 단위가 아니라 **역할 단위**로 매긴다.

역할 하나 = family(검색 task 계열) + scan 규칙. 정답은 사람이 고른 목록이 아니라 기존 모델 골든셋과 같은
방법(test/model_retrieval/tools/scan.py)으로 코퍼스 4,017개를 전수 스캔해 매긴다.

    2점  그 역할의 능력이 모델명·원본명·의미 claim 에 명시되고, ko=True 면 한국어 전용
    1점  능력은 확인되지만 다국어 범용·변환본이거나, 근거가 메타데이터나 README 원문에만 있음
    0점  나머지

family 는 17_recommend_graph.MODEL_TASK_FALLBACK 을 거친 task 키다(retrieval→embedding, ocr→visual_qa ...).
planner 의 need 는 family 가 맞는 역할에 짝지어진다. 짝이 없는 역할은 모든 방식에서 0점이다(검색 전 단계의 실패).

질문 문장은 검색 결과를 보기 전에 썼다. 패턴은 test/model_retrieval/queries/spec_capability.py 를 그대로 쓴다.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SPEC = Path(__file__).resolve().parents[1] / "model_retrieval" / "queries" / "spec_capability.py"
_spec = importlib.util.spec_from_file_location("spec_capability", _SPEC)
cap = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cap)

# 범용 역할: 능력 자체는 흔하고, 한국어 전용인지가 2점을 가른다.
KO_LLM = [r"\bchat\b", r"instruct", r"assistant", r"대화", r"챗봇", r"conversation"]
KO_EMB = [r"embedding", r"sentence.?(similarity|transformer|embedding)", r"semantic search", r"retriev",
          r"임베딩", r"문장 ?유사", r"유사도", r"dense passage"]
ASR = [r"speech recognition", r"\basr\b", r"음성 ?인식", r"transcri", r"받아쓰기", r"speech-to-text", r"\bstt\b"]
FRAUD = [r"\bfraud", r"\bscam", r"phishing", r"smishing", r"사기", r"스미싱", r"피싱", r"\bspam\b", r"스팸"]


def role(family, scan, ko=False, also_family=()):
    """family: 이 역할을 맡는 need 의 task 계열. also_family: 같은 역할을 다른 계열로 풀어도 인정할 때."""
    return {"family": family, "also_family": list(also_family), "scan": scan, "ko": ko}


def cap_scan(must, must_id=None, strong=None, also=None):
    out = {"must_any": must, "grade_2_any": strong or must}
    if must_id:
        out["must_id_any"] = must_id
    if also:
        out["also_any"] = also
    return out


EMB = role("embedding", cap_scan(KO_EMB), ko=True)
RERANK = role("reranking", cap_scan(cap.RERANK, cap.RERANK_ID, cap.RERANK + cap.RERANK_ID))
LLM = role("generation", cap_scan(KO_LLM), ko=True)
SUMMARY = role("summarization", cap_scan(cap.SUMMARY, cap.SUMMARY_ID, cap.SUMMARY + cap.SUMMARY_ID), ko=True,
               also_family=["generation"])
SPEECH = role("speech_recognition", cap_scan(ASR), ko=True)
KO_EN = role("translation", cap_scan(cap.TRANSLATE_KO_EN), also_family=["generation"])


def q(qid, text, *roles):
    return {"qid": qid, "text": text, "roles": list(roles)}


QUESTIONS = [
    q("pj01", "회사 매뉴얼로 사내 RAG 챗봇을 만드는 프로젝트를 하려고 해. 데이터는 있으니까 모델만 추천해줘.",
      EMB, RERANK, LLM),
    q("pj02", "유튜브 댓글 악플을 자동으로 걸러내는 프로젝트를 하려는데 모델만 추천해줘.",
      role("classification", cap_scan(cap.HATE, cap.HATE_ID, cap.HATE + [r"hate", r"toxic"]), ko=True)),
    q("pj03", "쇼핑몰 리뷰가 긍정인지 부정인지 분석하고 리뷰를 한 줄로 요약해 주는 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("classification", cap_scan(cap.SENTIMENT), ko=True), SUMMARY),
    q("pj04", "콜센터 통화를 실시간으로 받아 적고 통화 내용을 요약하는 프로젝트를 하려고 합니다. 모델만 골라 주세요.",
      role("speech_recognition", cap_scan(ASR, strong=cap.STREAMING)), SUMMARY),
    q("pj05", "판례랑 법령을 검색해 주는 법률 검색 서비스 프로젝트를 하려는데 모델만 추천해줘.",
      role("embedding", cap_scan(cap.LEGAL)), RERANK),
    q("pj06", "병원 원무과에서 쓸 의료 규정 Q&A 챗봇 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("generation", cap_scan(cap.MEDICAL)), EMB),
    q("pj07", "주민센터에 들어오는 손글씨 민원 서류를 디지털로 옮기는 프로젝트를 하려는데 모델만 추천해줘.",
      role("visual_qa", cap_scan(cap.HANDWRITING + cap.OCR, [r"hand-?ocr", r"handwrit", r"손글씨", r"ocr"],
                                 cap.HANDWRITING))),
    q("pj08", "어르신들 사투리 음성을 받아쓰는 앱 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("speech_recognition", cap_scan(ASR, strong=cap.DIALECT), ko=True)),
    q("pj09", "영어 기술 문서를 한국어로 번역해 주는 사이트를 만드는 프로젝트야. 모델만 추천해줘.", KO_EN),
    q("pj10", "금융 뉴스가 호재인지 악재인지 알려 주는 주식 알림 앱 프로젝트를 하려는데 모델만 추천해줘.",
      role("classification", cap_scan(cap.SENTIMENT, also=cap.FINANCE))),
    q("pj11", "고객 문의 내용을 보고 어느 부서로 보낼지 자동 분류하는 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("classification", cap_scan(cap.INTENT), ko=True)),
    q("pj12", "상담 기록에서 이름이나 전화번호 같은 개인정보를 자동으로 가리는 프로젝트를 하려는데 모델만 추천해줘.",
      role("generation", cap_scan(cap.PII), also_family=["classification"])),
    q("pj13", "블로그 글의 맞춤법이랑 띄어쓰기를 고쳐 주는 글쓰기 도우미 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("generation", cap_scan(cap.SPELL, cap.SPELL_ID, cap.SPELL + cap.SPELL_ID))),
    q("pj14", "사내 개발자들이 한국어로 물어보면 코드를 짜 주는 코딩 어시스턴트 프로젝트를 하려는데 모델만 추천해줘.",
      role("generation", cap_scan(cap.CODE))),
    q("pj15", "초등학생 수학 숙제를 풀이해 주는 학습 도우미 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("generation", cap_scan(cap.MATH))),
    q("pj16", "게임 NPC가 캐릭터 말투로 대화하게 만드는 프로젝트를 하려는데 모델만 추천해줘.",
      role("generation", cap_scan(cap.ROLEPLAY))),
    q("pj17", "재무 보고서 PDF의 표랑 차트를 읽어서 설명해 주는 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("visual_qa", cap_scan(cap.CHART))),
    q("pj18", "회의 녹음을 받아 적고 회의록으로 요약해 주는 프로젝트를 하려고 합니다. 모델만 추천해 주세요.",
      SPEECH, SUMMARY),
    q("pj19", "영수증 사진을 찍으면 금액이랑 상호를 읽어서 가계부에 넣어 주는 앱 프로젝트야. 모델만 추천해줘.",
      role("visual_qa", cap_scan(cap.OCR))),
    q("pj20", "사내 시스템 API를 호출해서 업무를 대신 처리하는 AI 에이전트 프로젝트를 하려는데 모델만 추천해줘.",
      role("generation", cap_scan(cap.TOOLCALL))),
    q("pj21", "뉴스 기사를 읽으면 비슷한 기사를 묶어서 추천해 주는 프로젝트를 하려고 해. 모델만 추천해줘.", EMB),
    q("pj22", "논문 초록으로 비슷한 연구를 찾아 주는 시맨틱 검색 프로젝트를 하려는데 모델만 추천해줘.", EMB, RERANK),
    q("pj23", "커뮤니티 게시글의 혐오 표현을 감지하고 순화한 문장을 제안하는 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("classification", cap_scan(cap.HATE, cap.HATE_ID, cap.HATE + [r"hate", r"toxic"]), ko=True), LLM),
    q("pj24", "보험 약관 내용을 물어보면 답해 주는 상담 챗봇 프로젝트를 하려는데 모델만 추천해줘.", EMB, LLM),
    q("pj25", "강의 영상에 한국어 자막을 자동으로 달아 주는 프로젝트를 하려고 해. 모델만 추천해줘.", SPEECH),
    q("pj26", "외국인 관광객이 한국어로 말하면 영어로 통역해 주는 앱 프로젝트를 하려고 합니다. 모델만 추천해 주세요.",
      SPEECH, KO_EN),
    q("pj27", "진료 상담 기록을 짧게 요약해서 의사에게 보여 주는 프로젝트를 하려는데 모델만 추천해줘.", SUMMARY),
    q("pj28", "계약서를 올리면 비슷한 조항을 찾아 주는 리걸테크 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("embedding", cap_scan(cap.LEGAL))),
    q("pj29", "쇼핑몰 상품 문의에 상품 정보를 찾아서 답해 주는 챗봇 프로젝트를 하려는데 모델만 추천해줘.",
      EMB, RERANK, LLM),
    q("pj30", "중고거래 게시글이 사기인지 판별해 주는 프로젝트를 하려고 해. 모델만 추천해줘.",
      role("classification", cap_scan(FRAUD))),
]
