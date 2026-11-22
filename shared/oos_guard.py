"""High-confidence, whole-utterance OOS rules. No model or retrieval calls.

A missing match leaves intent undecided. Callers must preserve replies to pending
questions instead of applying these context-free rules to those replies.
"""
import re

from .input_guard import _normalize

OOS_MESSAGE = "Model Scout는 모델과 데이터를 추천하는 서비스예요. 만들고 싶은 프로젝트나 찾고 있는 모델·데이터를 알려주세요."

# Only the settings currently appended by Home.withConditions are removed from
# the detection copy. A user-written, unrecognized '조건:' line remains intact.
_HOME_SETTING = r"(?:언어 (?:한국어|영어)|실행 환경 (?:로컬 GPU (?:8|16|24)GB|CPU만)|상업적 이용 가능)"
_HOME_CONDITIONS = re.compile(rf"\n조건: {_HOME_SETTING}(?:, {_HOME_SETTING}){{0,2}}\.\s*\Z")
_WISH_ENDING = r"(?:어|어요|다|네|습니다|은데)"
_PATTERNS = {
    "greeting": r"(?:안녕(?:하세요|하십니까)?|하이|반가워(?:요)?|hello|hi|hey|ㅎㅇ)",
    "thanks_farewell": r"(?:고마워(?:요)?|고맙(?:다|습니다)|감사(?:합니다|해요)|수고했(?:어|어요)|잘자(?:요)?|다음에보자)",
    "small_talk": r"(?:뭐해(?:요)?|밥먹었(?:어|어요)|잘잤(?:어|어요)|오늘기분어때(?:요)?)",
    "daily_state": r"(?:배고(?:파|파요|프다)|졸(?:려|려요|리다)|심심(?:해|해요|하다)|피곤(?:해|해요|하다))",
    "rest_home_wish": rf"(?:(?:집(?:에)?가고|퇴근하고|쉬고|푹자고|자고)싶{_WISH_ENDING})",
    "food_travel_wish": rf"(?:(?:치킨|라면|밥|고기|맛있는거)먹고싶{_WISH_ENDING}|"
                        rf"(?:여행|바다(?:에)?)가고싶{_WISH_ENDING})",
    "personal_exam_wish": rf"(?:(?:수능|시험|면접)(?:을|를)?잘보고싶{_WISH_ENDING}|"
                          rf"(?:수능|시험|면접)(?:에)?합격하고싶{_WISH_ENDING})",
    "entertainment": r"(?:농담(?:해줘|해주세요)|끝말잇기(?:하자|해줘)|스무고개(?:하자|해줘)|노래(?:불러줘|불러주세요))",
    "standalone_abuse": r"(?:(?:씨발|시발|ㅅㅂ|병신|ㅂㅅ|지랄|fuck)[.!?~]*|"
                        r"너병신이냐|멍청한새끼|꺼져|fuckyou|stupidbot)+",
}
OOS_RULES = {reason: re.compile(_normalize(pattern)) for reason, pattern in _PATTERNS.items()}


def oos_reason(text: str) -> str | None:
    """Return a known OOS category, or None. Whole-text matching protects mixed requests."""
    words = _HOME_CONDITIONS.sub("", text)
    words = re.sub(r"\s+", "", _normalize(words).casefold())
    words = words.rstrip(_normalize(".!?~…ㅠㅜㅋㅎ"))
    return next((reason for reason, pattern in OOS_RULES.items() if pattern.fullmatch(words)), None)
