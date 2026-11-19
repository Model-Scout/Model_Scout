"""semantic_capability 질문 40개 — "이런 걸 할 수 있는 모델"을 찾는 경우.

채점은 README·메타데이터 키워드다. 2점은 그 능력을 주 용도로 명시한 모델,
1점은 부가 기능이거나 다국어 범용이거나 변환본이다.

**초보 질문 20개를 섞었다(origin="beginner").** 운영 검색은 사용자 원문을
보지 않고 decompose(LLM)가 만든 model_query 를 받으므로, 초보가 쓴 문장도
검색 입장에서는 같은 자리에 들어온다. 다만 분해가 task 를 제대로 뽑는지가
달라지므로 따로 집계할 수 있게 태그를 남긴다.

초보 질문은 모델 종류·크기·라이선스를 하나도 말하지 않는다. 그래서 하드
필터 조건도 없다 — 질문에 근거가 없는 조건을 넣으면 안 된다
(conditions_fidelity 원칙).
"""

GEN = ["text-generation"]
EMB = ["sentence-similarity", "feature-extraction"]
ASR = ["automatic-speech-recognition"]
VLM = ["image-text-to-text"]
CLS = ["text-classification"]
QA = ["question-answering"]
SUM = ["summarization"]
TR = ["translation"]

SENTIMENT = [r"sentiment", r"감정", r"감성", r"nsmc", r"polarity", r"emotion"]
HATE = [r"hate.?speech", r"toxic(ity)?", r"혐오 ?(표현|발언)", r"욕설", r"비속어",
        r"offensive (language|speech|content)", r"unsmile", r"profanit", r"abusive language"]
HATE_ID = [r"hate", r"toxic", r"bias", r"curse", r"unsmile", r"profan"]
INTENT = [r"\bintent", r"의도 ?(분류|파악)", r"3i4k"]
# "fine-tuning (NER, classification, NLI)" 처럼 미세조정 대상으로 나열된 NER 은 근거가 아니다.
# 그 모델이 개체명을 뽑는다고 말하는 꼴만 받는다.
# "sequence classification, token classification or question answering" 처럼 나열된 것은 근거가 아니다.
NER = [r"named.?entity recognition", r"개체명 ?(인식|추출)", r"\bner\b (model|task|tagger|system)",
       r"(ner|개체명)[^.]{0,30}(학습|파인튜닝|fine-?tuned|trained)",
       r"(trained|fine-?tuned) (on|for) (ner|named.?entity)"]
PII = [r"\bpii\b", r"개인 ?정보", r"personal(ly)? identifiable", r"redact", r"마스킹", r"de-?identif"]
SPELL = [r"spell(ing)?[ -]?(check|correct)", r"grammar (error )?correct", r"맞춤법", r"문법 ?교정",
         r"오탈자", r"typos? (correct|fix)", r"\bgec\b"]
SPELL_ID = [r"spell", r"typo", r"gec", r"맞춤법"]
SUMMARY = [r"summariz(?:e|es|ing|ation|er)\b", r"요약", r"xlsum"]
SUMMARY_ID = [r"summar", r"요약", r"xlsum"]
RERANK = [r"\breranker\b", r"rerank(ing)? model", r"cross-?encoder", r"재순위", r"재정렬 모델"]
RERANK_ID = [r"rerank", r"cross-?encoder"]
OCR = [r"\bocr\b", r"광학 ?문자", r"optical character", r"문서 ?인식", r"text recognition"]
HANDWRITING = [r"handwrit", r"hand-?written", r"손글씨", r"필기"]
DIALECT = [r"dialect", r"사투리", r"방언"]
# whisper 카드의 "near-real-time speech recognition" 은 스트리밍이 아니다(배치로 쪼개 돌리는 것).
# v3 원본과 같이 near- 를 제외한다.
STREAMING = [r"streaming (asr|speech recognition|transcription|inference|mode|decoding)",
             r"스트리밍",
             r"(?<!near-)(?<!near )real-?time (streaming|asr|speech recognition|transcription)",
             r"실시간 ?(음성 ?인식|전사|받아쓰기|자막)"]
STREAMING_ID = [r"streaming", r"realtime", r"real-time"]
LEGAL = [r"\blegal\b", r"\blaw\b", r"법률", r"판례", r"법령", r"계약서", r"lawir"]
MEDICAL = [r"medical", r"의료", r"진료", r"clinical", r"질병", r"건강 ?보험", r"\bbio-?medical\b"]
FINANCE = [r"financ", r"금융", r"증권", r"주식", r"fin-?bert", r"경제 ?뉴스"]
# "including chat bots and coding assistants" 는 Llama 카드의 상투어라 코딩 모델이 아니어도 걸린다.
# HumanEval·MBPP 는 벤치마크 이름이라 점수 나열에 걸린다(벤치마크는 benchmark_lookup 유형이 본다).
# 코딩이 그 모델의 용도라고 말하는 꼴만 받는다.
CODE = [r"\bcode (generation|completion)\b", r"코드 ?(생성|작성)",
        r"code (llm|model|assistant) ", r"코딩 ?(특화|전용|모델)",
        r"(coder|code)-?(instruct|base)\b", r"for (coding|code) (task|use|assist)",
        r"(trained|fine-?tuned|optimized) (on|for) code"]
# "\bmath\b" 만으로는 수학을 언급만 한 범용 LLM 이 수백 개 걸린다.
MATH = [r"\bmath(ematical)? reasoning\b", r"수학 ?(추론|문제|풀이)", r"gsm8k", r"\bmath\b.{0,20}(bench|solv|problem)"]
# 'tool calling' 은 벤치마크 나열·주의사항에도 흔히 나온다. 지원을 선언하는 꼴만 받는다.
TOOLCALL = [r"supports? (function|tool).?call", r"(function|tool).?calling (is )?(support|enabled|capab)",
            r"native (function|tool).?call", r"(function|tool).?call(ing)? (support|capab)",
            r"함수 ?호출 ?(지원|가능)", r"도구 ?호출 ?(지원|가능)", r"\bbfcl\b"]
ROLEPLAY = [r"role-?play", r"롤플레이", r"캐릭터 ?(대화|챗)", r"persona chat"]
# "<table>" 은 README 의 HTML 표에 전부 걸리고 "chart" 는 벤치마크 표 설명에 걸린다.
# 문서·도표를 읽는 능력을 뜻하는 말만 남긴다.
CHART = [r"chart (understanding|qa|reasoning)", r"table (understanding|qa|recognition|parsing)",
         r"도표 ?(이해|인식)", r"\bdocvqa\b", r"차트 ?(이해|분석)", r"표 ?이해",
         r"document (understanding|parsing|vqa)", r"문서 ?(이해|파싱)", r"\bai2d\b", r"k-dtcbench",
         r"\bchartqa\b", r"\btablevqa\b"]
TRANSLATE_KO_EN = [r"korean.{0,20}english", r"english.{0,20}korean", r"한영", r"영한", r"ko-?en", r"en-?ko"]


def q(qid, text, scan, tasks=None, ko=False, origin="label_reused",
      persona="backend_dev", style="mixed", g2=None, g1=None):
    rule = {
        "grade_2": g2 or "그 능력을 주 용도로 명시한 모델",
        "grade_1": g1 or "그 능력이 부가적이거나 다국어 범용이거나 변환본",
        "scan": scan,
    }
    if ko:
        rule["grade_2_requires_korean_specific"] = True
    return {
        "qid": qid, "text": text, "query_type": "semantic_capability", "origin": origin,
        "persona": persona, "expression_style": style,
        "conditions": {"korean_required": True, **({"tasks": tasks} if tasks else {})},
        "conditions_fidelity": {"tasks": "질의가 지목한 모델 종류"} if tasks else {},
        "relevance_rule": rule,
    }


def b(qid, text, scan, tasks=None, ko=False, **kw):
    """초보 질문 — 모델 종류·크기·라이선스를 말하지 않는다."""
    return q(qid, text, scan, tasks=tasks, ko=ko, origin="beginner",
             persona="beginner", style="natural", **kw)


QUERIES = [
    # ══ 전문가형 20 ══════════════════════════════════════════
    q("sc01", "커뮤니티 댓글에서 욕설이나 혐오 표현을 자동으로 걸러내는 한국어 분류 모델이 필요합니다.",
      {"must_any": HATE, "must_id_any": HATE_ID, "grade_2_any": HATE + [r"hate", r"toxic"]}, CLS, ko=True),
    q("sc02", "주식 앱에서 금융 뉴스가 호재인지 악재인지 나누는 한국어 감성 분류 모델을 찾습니다.",
      {"must_any": SENTIMENT, "also_any": FINANCE, "grade_2_any": SENTIMENT}, CLS, ko=True),
    q("sc03", "고객 문의 챗봇 앞단에 붙일 한국어 intent classification 모델이 필요해요.",
      {"must_any": INTENT, "grade_2_any": INTENT}, CLS, ko=True),
    q("sc04", "한국어 텍스트에서 이름·전화번호 같은 PII 를 탐지하는 모델이 필요합니다. 비식별화 용도예요.",
      {"must_any": PII, "grade_2_any": PII}, GEN),
    q("sc05", "한국어 맞춤법·문법 교정(GEC) 용으로 학습된 모델이 있나요?",
      {"must_any": SPELL, "must_id_any": SPELL_ID, "grade_2_any": SPELL + SPELL_ID}, GEN),
    q("sc06", "RAG 파이프라인에서 1차 검색 결과를 다시 순위 매길 한국어 reranker(cross-encoder)를 찾고 있습니다.",
      {"must_any": RERANK, "must_id_any": RERANK_ID, "grade_2_any": RERANK + RERANK_ID}, ko=True,
      persona="ml_engineer", style="technical"),
    # NER 능력을 선언한 모델이 코퍼스에 1개뿐이라(그마저 상업 제한) 질문이 성립하지 않는다.
    # 같은 '문서에서 뽑아내기' 계열이면서 코퍼스에 있는 능력으로 바꿨다.
    q("sc07", "한국어 문서를 다른 언어로 번역하면서 전문 용어를 유지하는 모델이 필요합니다.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN}, TR,
      persona="ml_engineer", style="technical"),
    q("sc08", "주민센터 민원 서류처럼 손으로 쓴 한국어 문서를 읽는 모델이 있을까요?",
      {"must_any": HANDWRITING, "must_id_any": [r"hand-?ocr", r"handwrit", r"손글씨"],
       "grade_2_any": HANDWRITING}, VLM),
    q("sc09", "사투리가 섞인 한국어 음성도 알아듣는 음성 인식 모델이 있을까요?",
      {"must_any": DIALECT, "grade_2_any": DIALECT}, ASR, ko=True),
    q("sc10", "콜센터 통화를 실시간으로 받아 적을 스트리밍 음성 인식 모델을 찾습니다.",
      {"must_any": STREAMING, "must_id_any": STREAMING_ID, "grade_2_any": STREAMING + STREAMING_ID}, ASR),
    q("sc11", "판례·법령 검색 RAG 에 쓸 법률 도메인 한국어 임베딩 모델이 있을까요?",
      {"must_any": LEGAL, "grade_2_any": LEGAL}, EMB, persona="ml_engineer", style="technical"),
    q("sc12", "병원 원무과에서 의료법·건강보험 규정을 물어볼 사내 Q&A 에 쓸 의료 도메인 한국어 모델이 필요합니다.",
      {"must_any": MEDICAL, "grade_2_any": MEDICAL}, GEN),
    q("sc13", "코드 생성도 되는 한국어 LLM 이 필요합니다.",
      {"must_any": CODE, "grade_2_any": CODE}, GEN),
    q("sc14", "수학 문제 풀이 추론이 되는 한국어 LLM 을 찾습니다.",
      {"must_any": MATH, "grade_2_any": MATH}, GEN),
    q("sc15", "function calling 을 지원하는 한국어 LLM 이 있나요? 에이전트에 붙이려고 합니다.",
      {"must_any": TOOLCALL, "grade_2_any": TOOLCALL}, GEN, persona="ml_engineer", style="technical"),
    q("sc16", "롤플레이·캐릭터 대화용 한국어 모델이 필요합니다.",
      {"must_any": ROLEPLAY, "grade_2_any": ROLEPLAY}, GEN),
    q("sc17", "문서 속 표와 차트를 읽는 비전 언어 모델이 필요합니다.",
      {"must_any": CHART, "grade_2_any": CHART}, VLM, persona="ml_engineer", style="technical"),
    q("sc18", "한국어 문서를 요약하도록 학습된 모델을 찾습니다.",
      {"must_any": SUMMARY, "must_id_any": SUMMARY_ID, "grade_2_any": SUMMARY + SUMMARY_ID}, SUM, ko=True),
    q("sc19", "스캔한 문서에서 글자를 뽑아내는 OCR 모델이 필요합니다.",
      {"must_any": OCR, "grade_2_any": OCR}, VLM),
    q("sc20", "한국어와 영어 사이를 번역하는 모델이 필요합니다. 양방향이면 좋겠어요.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN}, ["translation"]),

    # ══ 초보형 20 — 모델 종류·크기·라이선스를 말하지 않는다 ══
    b("sc21", "유튜브 댓글이 악플인지 자동으로 걸러내는 걸 만들어보고 싶어요. 뭐부터 시작해야 하나요?",
      {"must_any": HATE, "must_id_any": HATE_ID, "grade_2_any": HATE + [r"hate", r"toxic"]}, CLS, ko=True),
    b("sc22", "쇼핑몰 후기가 좋은 평인지 나쁜 평인지 자동으로 구분하고 싶은데 가능할까요?",
      {"must_any": SENTIMENT, "grade_2_any": SENTIMENT}, CLS, ko=True),
    b("sc23", "고객이 뭘 물어보는 건지 자동으로 알아내서 담당자에게 넘기고 싶어요.",
      {"must_any": INTENT, "grade_2_any": INTENT}, CLS, ko=True),
    b("sc24", "상담 기록에 남은 전화번호나 이름을 자동으로 지우고 싶은데 어떻게 하나요?",
      {"must_any": PII, "grade_2_any": PII}, GEN),
    b("sc25", "글 쓰는 서비스를 만드는데 오타랑 띄어쓰기를 자동으로 고쳐 주고 싶어요.",
      {"must_any": SPELL, "must_id_any": SPELL_ID, "grade_2_any": SPELL + SPELL_ID}, GEN),
    b("sc26", "회사 매뉴얼을 챗봇으로 만들고 싶은데 질문이랑 제일 비슷한 문서를 찾는 게 먼저겠죠?",
      {"must_any": RERANK, "must_id_any": RERANK_ID, "grade_2_any": RERANK + RERANK_ID}, EMB, ko=True),
    b("sc27", "외국어 문서를 한국어로 바꿔서 보고 싶은데 전문 용어가 많아요.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN}, TR),
    b("sc28", "손으로 쓴 서류를 사진 찍어서 컴퓨터로 옮기고 싶어요. 되는 게 있을까요?",
      {"must_any": HANDWRITING, "must_id_any": [r"hand-?ocr", r"handwrit", r"손글씨"],
       "grade_2_any": HANDWRITING}, VLM),
    b("sc29", "할머니 할아버지들 말투도 알아듣는 받아쓰기를 만들고 싶은데 어려울까요?",
      {"must_any": DIALECT, "grade_2_any": DIALECT}, ASR, ko=True),
    b("sc30", "통화하는 중에 바로바로 글자로 보여 주는 걸 만들고 싶어요.",
      {"must_any": STREAMING, "must_id_any": STREAMING_ID, "grade_2_any": STREAMING + STREAMING_ID}, ASR),
    b("sc31", "계약서 같은 걸 올리면 비슷한 조항을 찾아 주는 서비스를 생각하고 있어요.",
      {"must_any": LEGAL, "grade_2_any": LEGAL}, EMB),
    # question-answering task 는 코퍼스에 29개뿐이고 의료 모델이 없다. 생성 모델로 본다.
    b("sc32", "병원에서 환자들이 자주 묻는 걸 자동으로 답해 주는 걸 만들어보려고 해요.",
      {"must_any": MEDICAL, "grade_2_any": MEDICAL}, GEN),
    b("sc33", "주식 뉴스를 보고 오를지 내릴지 분위기를 읽어 주는 걸 만들고 싶어요.",
      {"must_any": SENTIMENT, "also_any": FINANCE, "grade_2_any": SENTIMENT}, CLS),
    b("sc34", "코딩을 도와주는 걸 만들고 싶은데 한국어로 물어봐도 되는 게 있나요?",
      {"must_any": CODE, "grade_2_any": CODE}, GEN),
    b("sc35", "아이 수학 숙제를 봐 주는 걸 만들어보고 싶어요.",
      {"must_any": MATH, "grade_2_any": MATH}, GEN),
    b("sc36", "게임 캐릭터가 사람처럼 대화하게 만들고 싶어요.",
      {"must_any": ROLEPLAY, "grade_2_any": ROLEPLAY}, GEN),
    b("sc37", "보고서에 있는 표랑 그래프를 읽어서 설명해 주는 걸 만들고 싶어요.",
      {"must_any": CHART, "grade_2_any": CHART}, VLM),
    b("sc38", "긴 회의록을 짧게 정리해 주는 걸 만들고 싶은데 뭘 쓰면 되나요?",
      {"must_any": SUMMARY, "must_id_any": SUMMARY_ID, "grade_2_any": SUMMARY + SUMMARY_ID}, SUM, ko=True),
    b("sc39", "사진 속 글자를 읽어서 엑셀로 옮기는 걸 만들려고 합니다.",
      {"must_any": OCR, "grade_2_any": OCR}, VLM),
    b("sc40", "영어로 된 자료를 한국어로 바꿔 주는 걸 만들고 싶어요.",
      {"must_any": TRANSLATE_KO_EN, "grade_2_any": TRANSLATE_KO_EN}, TR),
]
