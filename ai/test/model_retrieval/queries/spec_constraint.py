"""semantic_constraint 질문 40개 — 능력과 제약을 함께 요구하는 경우.

semantic_capability 와 다른 점은 하드 필터 조건이 함께 걸린다는 것이다
(크기·컨텍스트·포맷·라이선스·게이팅). 채점은 조건을 통과한 모델 안에서
README·메타데이터 키워드로 한다.

**초보 질문 15개를 섞었다(origin="beginner").** 초보는 모델 스펙을 말하지
않지만 "노트북에서", "무료로", "회사에서 쓸 건데" 같은 말로 제약을 드러낸다.
그 말에 근거가 있는 조건만 넣는다(conditions_fidelity 원칙).

task 조건은 운영과 같게 decompose 가 뽑은 task 를 쓴다.
"""

import importlib.util
from pathlib import Path

_cap = importlib.util.spec_from_file_location(
    "spec_capability", Path(__file__).resolve().parent / "spec_capability.py")
_m = importlib.util.module_from_spec(_cap)
_cap.loader.exec_module(_m)

GEN, EMB, ASR, VLM, CLS = _m.GEN, _m.EMB, _m.ASR, _m.VLM, _m.CLS
TR, SUM, QA = _m.TR, _m.SUM, _m.QA
SENTIMENT, HATE, HATE_ID, INTENT = _m.SENTIMENT, _m.HATE, _m.HATE_ID, _m.INTENT
PII, SPELL, SPELL_ID, SUMMARY, SUMMARY_ID = _m.PII, _m.SPELL, _m.SPELL_ID, _m.SUMMARY, _m.SUMMARY_ID
RERANK, RERANK_ID, OCR, HANDWRITING = _m.RERANK, _m.RERANK_ID, _m.OCR, _m.HANDWRITING
DIALECT, STREAMING, STREAMING_ID = _m.DIALECT, _m.STREAMING, _m.STREAMING_ID
LEGAL, MEDICAL, FINANCE, CODE, MATH = _m.LEGAL, _m.MEDICAL, _m.FINANCE, _m.CODE, _m.MATH
TOOLCALL, ROLEPLAY, CHART = _m.TOOLCALL, _m.ROLEPLAY, _m.CHART
TRANSLATE_KO_EN, NER = _m.TRANSLATE_KO_EN, _m.NER

PERMITTED = ["permitted"]


def q(qid, text, scan, conditions, fidelity, ko=False, origin="label_reused",
      persona="backend_dev", style="mixed"):
    rule = {
        "grade_2": "조건을 만족하면서 그 능력을 주 용도로 명시한 모델",
        "grade_1": "조건은 만족하지만 능력이 부가적이거나 다국어 범용이거나 변환본",
        "scan": scan,
    }
    if ko:
        rule["grade_2_requires_korean_specific"] = True
    if conditions.get("require_artifact"):
        rule["format_requested"] = True
    return {
        "qid": qid, "text": text, "query_type": "semantic_constraint", "origin": origin,
        "persona": persona, "expression_style": style,
        "conditions": {"korean_required": True, **conditions},
        "conditions_fidelity": fidelity,
        "relevance_rule": rule,
    }


def b(qid, text, scan, conditions, fidelity, ko=False, **kw):
    return q(qid, text, scan, conditions, fidelity, ko=ko, origin="beginner",
             persona="beginner", style="natural", **kw)


QUERIES = [
    # ══ 전문가형 25 ══════════════════════════════════════════
    q("sx01", "상품 리뷰 감정 분석을 유료 서비스에 넣으려고 해요. 상업 이용이 허용되는 라이선스 계열인 한국어 모델이면 좋겠습니다.",
      {"must_any": SENTIMENT, "grade_2_any": SENTIMENT},
      {"tasks": CLS, "commercial_status": PERMITTED},
      {"tasks": "감정 분석", "commercial_status": "상업 이용이 허용되는 라이선스 계열"}, ko=True),
    q("sx02", "Ollama 로 내 PC 에서 한국어와 영어를 번역하고 싶어요. GGUF 파일이 5GB 이하인 모델을 찾아 주세요.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN},
      {"tasks": TR, "require_artifact": ["gguf"], "max_artifact_gib": 5},
      {"tasks": "번역", "require_artifact": "Ollama 로 … GGUF", "max_artifact_gib": "GGUF 파일이 5GB 이하"},
      persona="local_user"),
    q("sx03", "병원 내부용 의료 Q&A 도우미를 만들려는데 GPU 가 넉넉하지 않아요. 파라미터 8B 이하인 의료 특화 한국어 생성 모델이 있을까요?",
      {"must_any": MEDICAL, "grade_2_any": MEDICAL},
      {"tasks": GEN, "max_parameters_billion": 8},
      {"tasks": "Q&A 도우미(생성 모델)", "max_parameters_billion": "파라미터 8B 이하"}),
    q("sx04", "계약서처럼 긴 법률 문서를 통째로 임베딩해서 검색하려고 해요. 최소 8K 토큰을 넣을 수 있는 법률 특화 한국어 임베딩 모델이 필요해요.",
      {"must_any": LEGAL, "grade_2_any": LEGAL},
      {"tasks": EMB, "min_context_length": 8192},
      {"tasks": "임베딩 모델", "min_context_length": "최소 8K 토큰을 넣을 수 있는"}),
    q("sx05", "콜센터 통화를 실시간으로 받아 적는 서비스를 상업적으로 운영하려고 해요. 파라미터 1B 이하로 가볍고 상업 이용 허용 계열인 스트리밍 음성 인식 모델이 필요해요.",
      {"must_any": STREAMING, "must_id_any": STREAMING_ID, "grade_2_any": STREAMING + STREAMING_ID},
      {"tasks": ASR, "commercial_status": PERMITTED, "max_parameters_billion": 1},
      {"tasks": "받아 적는(음성 인식)", "commercial_status": "상업 이용 허용 계열",
       "max_parameters_billion": "파라미터 1B 이하"}),
    q("sx06", "파라미터 4B 이하 비전-언어 모델 중에서 한국어 OCR 용도로 학습된 걸 찾고 있습니다.",
      {"must_any": OCR, "grade_2_any": OCR},
      {"tasks": VLM, "max_parameters_billion": 4},
      {"tasks": "비전-언어 모델", "max_parameters_billion": "파라미터 4B 이하"}, ko=True,
      persona="ml_engineer", style="technical"),
    q("sx07", "게임 커뮤니티 채팅 필터를 상용으로 붙이려고 해요. 관리자 승인 없이 바로 받을 수 있고 상업 이용 허용 계열인 한국어 욕설·혐오 표현 분류 모델을 찾아 주세요.",
      {"must_any": HATE, "must_id_any": HATE_ID, "grade_2_any": HATE + [r"hate", r"toxic"]},
      {"tasks": CLS, "exclude_gated": True, "commercial_status": PERMITTED},
      {"tasks": "분류 모델", "exclude_gated": "관리자 승인 없이 바로 받을 수 있고",
       "commercial_status": "상업 이용 허용 계열"}, ko=True),
    q("sx08", "유료 사내 검색 SaaS 에 reranker 를 붙이려고 합니다. 상업 이용 허용 계열인 한국어 재순위 모델이 있을까요?",
      {"must_any": RERANK, "must_id_any": RERANK_ID, "grade_2_any": RERANK + RERANK_ID},
      {"commercial_status": PERMITTED},
      {"commercial_status": "상업 이용 허용 계열"}, ko=True, persona="ml_engineer", style="technical"),
    q("sx09", "뉴스 기사를 짧게 요약하는 앱을 만들고 있어요. 파라미터 1B 이하로 가벼운 한국어 요약 모델이 있을까요?",
      {"must_any": SUMMARY, "must_id_any": SUMMARY_ID, "grade_2_any": SUMMARY + SUMMARY_ID},
      {"max_parameters_billion": 1},
      {"max_parameters_billion": "파라미터 1B 이하"}, ko=True, persona="local_user"),
    q("sx10", "CS 상담 로그에서 개인정보를 지우는 배치 작업을 만들고 있어요. 상업 이용 허용 계열이고 파일 크기가 2GB 이하인 개인정보 탐지 모델이 있나요?",
      {"must_any": PII, "grade_2_any": PII},
      {"commercial_status": PERMITTED, "max_artifact_gib": 2},
      {"commercial_status": "상업 이용 허용 계열", "max_artifact_gib": "파일 크기가 2GB 이하"}),
    q("sx11", "맞춤법 교정 기능을 상업 서비스에 넣으려고 합니다. 상업 이용 허용 계열이고 0.5B 이하인 한국어 모델을 찾아 주세요.",
      {"must_any": SPELL, "must_id_any": SPELL_ID, "grade_2_any": SPELL + SPELL_ID},
      {"commercial_status": PERMITTED, "max_parameters_billion": 0.5},
      {"commercial_status": "상업 이용 허용 계열", "max_parameters_billion": "0.5B 이하"}),
    # CLS + ONNX 후보 30개는 전부 다국어 모델이다. 한국어 금융 감성은 ONNX 로 없다.
    q("sx12", "금융 뉴스 감성 분류를 상업 서비스에 넣으려고 합니다. 상업 이용 허용 계열인 한국어 모델이 필요해요.",
      {"must_any": SENTIMENT, "also_any": FINANCE, "grade_2_any": SENTIMENT},
      {"tasks": CLS, "commercial_status": PERMITTED},
      {"tasks": "감성 분류", "commercial_status": "상업 이용 허용 계열"}),
    q("sx13", "손글씨 OCR 을 상업 서비스에 쓰려고 합니다. 상업 이용 허용 계열이고 4B 이하인 모델이 있나요?",
      {"must_any": HANDWRITING, "must_id_any": [r"hand-?ocr", r"handwrit", r"손글씨"],
       "grade_2_any": HANDWRITING},
      {"tasks": VLM, "commercial_status": PERMITTED, "max_parameters_billion": 4},
      {"tasks": "OCR(비전 언어 모델)", "commercial_status": "상업 이용 허용 계열",
       "max_parameters_billion": "4B 이하"}),
    q("sx14", "코드 생성이 되는 한국어 LLM 을 llama.cpp 로 돌리려고 합니다. GGUF 로 받을 수 있고 8GB 이하였으면 해요.",
      {"must_any": CODE, "grade_2_any": CODE},
      {"tasks": GEN, "require_artifact": ["gguf"], "max_artifact_gib": 8},
      {"tasks": "한국어 LLM", "require_artifact": "llama.cpp … GGUF", "max_artifact_gib": "8GB 이하"}),
    q("sx15", "function calling 을 지원하는 한국어 LLM 을 상업 서비스에 쓰려고 합니다. 상업 이용 허용 계열로 찾아 주세요.",
      {"must_any": TOOLCALL, "grade_2_any": TOOLCALL},
      {"tasks": GEN, "commercial_status": PERMITTED},
      {"tasks": "한국어 LLM", "commercial_status": "상업 이용 허용 계열"},
      persona="ml_engineer", style="technical"),
    q("sx16", "방언 음성 인식을 모바일에 넣으려고 합니다. 파라미터 1B 이하인 모델이 있을까요?",
      {"must_any": DIALECT, "grade_2_any": DIALECT},
      {"tasks": ASR, "max_parameters_billion": 3},
      {"tasks": "음성 인식", "max_parameters_billion": "파라미터 3B 이하"}, ko=True),
    q("sx17", "표와 차트를 읽는 비전 언어 모델이 필요한데 상업 이용이 가능해야 합니다.",
      {"must_any": CHART, "grade_2_any": CHART},
      {"tasks": VLM, "commercial_status": PERMITTED},
      {"tasks": "비전 언어 모델", "commercial_status": "상업 이용이 가능해야"}),
    # ONNX 로 올라온 분류 모델은 전부 다국어다. 한국어 특화를 2점 조건으로 걸면 0이 된다.
    q("sx18", "의도 분류 모델을 ONNX 로 배포하려고 합니다. ONNX 파일이 있는 모델을 찾아 주세요.",
      {"must_any": INTENT, "grade_2_any": INTENT},
      {"tasks": CLS, "require_artifact": ["onnx"]},
      {"tasks": "의도 분류 모델", "require_artifact": "ONNX 로 배포하려고"}),
    q("sx19", "법률 문서 검색용 임베딩을 상업 서비스에 쓰려고 합니다. 상업 이용 허용 계열이면 좋겠어요.",
      {"must_any": LEGAL, "grade_2_any": LEGAL},
      {"tasks": EMB, "commercial_status": PERMITTED},
      {"tasks": "검색용 임베딩", "commercial_status": "상업 이용 허용 계열"}),
    q("sx20", "롤플레이 대화 모델을 개인 PC 에서 돌리려고 합니다. GGUF 로 받을 수 있고 8GB 이하면 좋겠어요.",
      {"must_any": ROLEPLAY, "grade_2_any": ROLEPLAY},
      {"tasks": GEN, "require_artifact": ["gguf"], "max_artifact_gib": 8},
      {"tasks": "대화 모델", "require_artifact": "GGUF 로 받을 수 있고", "max_artifact_gib": "8GB 이하"},
      persona="local_user"),
    q("sx21", "수학 추론이 되는 한국어 LLM 중 컨텍스트가 32K 이상인 걸 찾습니다.",
      {"must_any": MATH, "grade_2_any": MATH},
      {"tasks": GEN, "min_context_length": 32768},
      {"tasks": "한국어 LLM", "min_context_length": "컨텍스트가 32K 이상"}),
    # NER 능력을 선언한 모델이 코퍼스에 1개뿐이라 질문이 성립하지 않는다. 요약으로 바꿨다.
    q("sx22", "문서 요약 모델을 상업 서비스에 쓰려고 합니다. 상업 이용 허용 계열이고 1B 이하면 좋겠어요.",
      {"must_any": SUMMARY, "must_id_any": SUMMARY_ID, "grade_2_any": SUMMARY + SUMMARY_ID},
      {"commercial_status": PERMITTED, "max_parameters_billion": 1},
      {"commercial_status": "상업 이용 허용 계열", "max_parameters_billion": "1B 이하"}, ko=True),
    q("sx23", "OCR 모델을 llama.cpp 로 돌리려고 합니다. GGUF 로 받을 수 있는 걸 찾아 주세요.",
      {"must_any": OCR, "grade_2_any": OCR},
      {"tasks": VLM, "require_artifact": ["gguf"]},
      {"tasks": "OCR 모델", "require_artifact": "llama.cpp … GGUF 로 받을 수 있는"}),
    q("sx24", "스트리밍 음성 인식을 ONNX Runtime 으로 올리려고 합니다. ONNX 파일이 있는 모델이 필요해요.",
      {"must_any": STREAMING, "must_id_any": STREAMING_ID, "grade_2_any": STREAMING + STREAMING_ID},
      {"tasks": ASR, "require_artifact": ["onnx"]},
      {"tasks": "음성 인식", "require_artifact": "ONNX Runtime 으로"}),
    q("sx25", "한영 번역 모델 중 컨텍스트가 8K 이상이고 상업 이용이 가능한 걸 찾습니다.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN},
      {"tasks": TR, "min_context_length": 8192, "commercial_status": PERMITTED},
      {"tasks": "번역 모델", "min_context_length": "컨텍스트가 8K 이상",
       "commercial_status": "상업 이용이 가능한"}),

    # ══ 초보형 15 — 스펙 대신 상황으로 제약을 말한다 ══════════
    b("sx26", "쇼핑몰 후기 분석을 서비스에 넣으려는데 나중에 돈 받고 팔아도 되는 걸로 알려 주세요.",
      {"must_any": SENTIMENT, "grade_2_any": SENTIMENT},
      {"tasks": CLS, "commercial_status": PERMITTED},
      {"tasks": "후기 분석(분류)", "commercial_status": "돈 받고 팔아도 되는"}, ko=True),
    b("sx27", "제 노트북에서 돌려 보고 싶은데 한국어랑 영어 번역되는 걸로 가벼운 게 있을까요?",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN},
      {"tasks": TR, "max_parameters_billion": 2},
      {"tasks": "번역", "max_parameters_billion": "노트북에서 돌려 보고 싶은데 … 가벼운"}),
    b("sx28", "회사에서 쓸 거라 라이선스 문제 없는 걸로 악플 거르는 걸 찾고 있어요.",
      {"must_any": HATE, "must_id_any": HATE_ID, "grade_2_any": HATE + [r"hate", r"toxic"]},
      {"tasks": CLS, "commercial_status": PERMITTED},
      {"tasks": "악플 거르는(분류)", "commercial_status": "회사에서 쓸 거라 라이선스 문제 없는"}, ko=True),
    b("sx29", "상담 기록에서 개인정보 지우는 걸 회사 서비스에 넣으려는데 무료로 써도 되는 게 있나요?",
      {"must_any": PII, "grade_2_any": PII},
      {"commercial_status": PERMITTED},
      {"commercial_status": "회사 서비스에 넣으려는데 무료로 써도 되는"}),
    b("sx30", "회의록 요약하는 걸 만들고 싶은데 제 컴퓨터에서 돌아갈 만큼 작았으면 해요.",
      {"must_any": SUMMARY, "must_id_any": SUMMARY_ID, "grade_2_any": SUMMARY + SUMMARY_ID},
      {"max_parameters_billion": 2},
      {"max_parameters_billion": "제 컴퓨터에서 돌아갈 만큼 작았으면"}, ko=True),
    b("sx31", "병원 안내 챗봇을 만들려는데 서버가 작아서 큰 모델은 못 올려요.",
      {"must_any": MEDICAL, "grade_2_any": MEDICAL},
      {"tasks": GEN, "max_parameters_billion": 8},
      {"tasks": "챗봇(생성 모델)", "max_parameters_billion": "서버가 작아서 큰 모델은 못 올려요"}),
    b("sx32", "계약서 찾아 주는 걸 만들려는데 문서가 길어서 한 번에 많이 넣을 수 있어야 해요.",
      {"must_any": LEGAL, "grade_2_any": LEGAL},
      {"tasks": EMB, "min_context_length": 8192},
      {"tasks": "문서 찾아 주는(임베딩)", "min_context_length": "문서가 길어서 한 번에 많이 넣을 수 있어야"}),
    b("sx33", "사진 글자 읽는 걸 만들고 싶은데 회사 제품에 넣을 거라 라이선스가 걸리면 안 돼요.",
      {"must_any": OCR, "grade_2_any": OCR},
      {"tasks": VLM, "commercial_status": PERMITTED},
      {"tasks": "사진 글자 읽는(OCR)", "commercial_status": "회사 제품에 넣을 거라 라이선스가 걸리면 안 돼요"}),
    b("sx34", "오타 고쳐 주는 걸 서비스에 넣으려는데 상업적으로 써도 되는 작은 모델이 있을까요?",
      {"must_any": SPELL, "must_id_any": SPELL_ID, "grade_2_any": SPELL + SPELL_ID},
      {"commercial_status": PERMITTED, "max_parameters_billion": 1},
      {"commercial_status": "상업적으로 써도 되는", "max_parameters_billion": "작은 모델"}),
    b("sx35", "통화 실시간 받아쓰기를 만들려는데 동시에 여러 명이 써서 가벼워야 해요.",
      {"must_any": STREAMING, "must_id_any": STREAMING_ID, "grade_2_any": STREAMING + STREAMING_ID},
      {"tasks": ASR, "max_parameters_billion": 1},
      {"tasks": "받아쓰기(음성 인식)", "max_parameters_billion": "동시에 여러 명이 써서 가벼워야"}),
    b("sx36", "코딩 도와주는 걸 제 PC 에 깔아서 쓰고 싶은데 Ollama 로 되는 게 있나요?",
      {"must_any": CODE, "grade_2_any": CODE},
      {"tasks": GEN, "require_artifact": ["gguf"]},
      {"tasks": "코딩 도와주는(생성 모델)", "require_artifact": "Ollama 로 되는"}),
    b("sx37", "게임 캐릭터 대화를 제 컴퓨터에서 돌리고 싶어요. 너무 크면 안 돌아갈 것 같은데요.",
      {"must_any": ROLEPLAY, "grade_2_any": ROLEPLAY},
      {"tasks": GEN, "max_parameters_billion": 8},
      {"tasks": "캐릭터 대화(생성 모델)", "max_parameters_billion": "너무 크면 안 돌아갈 것 같은데요"}),
    b("sx38", "문서 속 표 읽는 걸 회사에서 쓸 건데 라이선스 깨끗한 게 필요해요.",
      {"must_any": CHART, "grade_2_any": CHART},
      {"tasks": VLM, "commercial_status": PERMITTED},
      {"tasks": "표 읽는(비전 언어 모델)", "commercial_status": "회사에서 쓸 건데 라이선스 깨끗한"}),
    b("sx39", "고객 문의 자동 분류를 웹서비스에 넣으려는데 브라우저에서도 돌아가면 좋겠어요.",
      {"must_any": INTENT, "grade_2_any": INTENT},
      {"tasks": CLS, "require_artifact": ["onnx"]},
      {"tasks": "자동 분류", "require_artifact": "브라우저에서도 돌아가면"}),
    b("sx40", "사투리 쓰는 분들 말도 알아듣는 받아쓰기를 만들려는데 작은 기기에 넣을 거예요.",
      {"must_any": DIALECT, "grade_2_any": DIALECT},
      {"tasks": ASR, "max_parameters_billion": 3},
      {"tasks": "받아쓰기(음성 인식)", "max_parameters_billion": "작은 기기에 넣을 거예요"}, ko=True),
]
