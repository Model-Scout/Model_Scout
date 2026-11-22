"""First-pass input rules, not a complete prompt-injection defense.

Known credentials block processing; PII is masked; injection patterns are signals only.
Exceptions and diagnostics contain categories only; GuardResult.text carries the masked input.
blocked_request() ends a turn whose clear purpose is to expose or falsify what the service holds, before any LLM.
"""

from dataclasses import dataclass, field
import re
import unicodedata
from typing import Any


KEY_MESSAGE = "API 키 또는 토큰으로 보이는 값이 포함되어 요청을 중단했습니다. 값을 제거하고, 실제 키라면 폐기 후 재발급해 주세요."
PASSWORD_MESSAGE = "비밀번호로 보이는 값이 포함되어 요청을 중단했습니다. 값을 제거하고, 실제 비밀번호를 공유했다면 변경해 주세요."


class InputBlocked(ValueError):
    def __init__(self, kind: str):
        self.kind = kind
        super().__init__(PASSWORD_MESSAGE if kind == "password" else KEY_MESSAGE)


@dataclass(frozen=True)
class GuardResult:
    text: str = field(repr=False)
    masked_types: tuple[str, ...] = ()
    injection_signals: tuple[str, ...] = ()


# Conservative known shapes. Short examples such as sk-... are not credentials.
TOKEN_RE = re.compile(
    r"(?<![\w-])(?:sk-(?:(?:proj|svcacct|ant-api\d+)-)?[A-Za-z0-9_-]{20,}"
    r"|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
    r"|hf_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{15,}"
    r"|(?:AKIA|ASIA)[A-Z0-9]{16}"
    r"|eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,})(?![\w-])"
)
BEARER_RE = re.compile(r"\bbearer\s+[A-Za-z0-9._~+/-]{16,}={0,2}", re.I)
ASSIGNMENT_RE = re.compile(
    r"(?<!\w)[\"']?(?P<label>api[_ -]?key|access[_ -]?token|refresh[_ -]?token|"
    r"auth[_ -]?token|secret[_ -]?key|api\s*키|토큰|password|passwd|pwd|비밀번호|비번)[\"']?"
    r"\s*[:=]\s*(?P<value>\"[^\"\r\n]{1,512}\"|'[^'\r\n]{1,512}'|[^\s,;\"'}\]]{1,512})",
    re.I,
)
PLACEHOLDERS = {"...", "…", "xxx", "xxxx", "example", "your_api_key", "your_token", "your_password",
                "api_key_here", "token_here", "password_here", "redacted", "비밀번호", "토큰", "예시"}

PII_RULES = (
    ("RRN", re.compile(r"(?<!\d)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[- \t]?[1-8]\d{6}(?!\d)")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+82[- .]?1[016789]|01[016789])[- .]?\d{3,4}[- .]?\d{4}(?!\d)")),
    ("EMAIL", re.compile(r"(?<![\w.+-])[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]{1,64}@(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}(?![\w-])")),
)
INJECTION_RULES = {
    "ignore_instructions": r"(?:이전|기존|위의|앞의|모든)\s*(?:시스템\s*)?(?:지시(?:사항)?|명령|규칙).{0,30}(?:무시|잊어)|(?:ignore|disregard|forget).{0,35}(?:previous|prior|system|above).{0,25}(?:instructions?|rules?|prompts?)",
    "role_override": r"너는\s*이제.{0,20}(?:관리자|개발자|시스템)|you\s+are\s+now.{0,25}(?:admin|developer|system)|(?:developer|admin)\s+mode",
    "prompt_extraction": r"(?:시스템|숨겨진|내부)\s*(?:시스템\s*)?(?:프롬프트|지시사항).{0,30}(?:공개|출력|보여|알려)|(?:reveal|show|print|output).{0,35}(?:system\s+prompt|hidden\s+instructions)",
    "secret_exfiltration": r"(?:내부|시스템|서버).{0,20}(?:api\s*키|api\s*key|토큰|비밀번호).{0,20}(?:알려|공개|출력|보여)|(?:reveal|show|print).{0,30}(?:api\s*keys?|secrets?|passwords?)",
    "format_override": r"json\s*(?:대신|말고).{0,35}(?:출력|반환)|(?:ignore|override).{0,25}(?:output\s+format|json\s+format)",
}


# Requests the service refuses outright, by purpose. A rule needs an owner word (the service's own prompt, keys or other
# users' chats), the protected object, and a request to hand it over in the same clause. A model or data noun between
# object and verb means the user is searching for a resource about it ("시스템 프롬프트 유출을 탐지하는 모델 알려줘").
SECURITY_NOTICES = {
    "instruction_override": "서비스의 추천 기준을 변경하는 지시는 처리할 수 없어요.",
    "system_prompt": "서비스의 내부 지침은 공개할 수 없어요. 찾고 있는 모델이나 데이터를 알려주세요.",
    "service_secret": "서비스의 접속 키는 공개할 수 없어요.",
    "private_conversation": "다른 사용자의 비공개 대화는 제공할 수 없어요.",
    "verdict_tampering": "추천 결과에는 확인된 근거와 검증 상태를 그대로 표시해요.",
}
_RESOURCE = r"모델|데이터|dataset|model|예시|예제|템플릿|샘플|작성|쓰는\s*법|만드는|형식|포맷|example|template|sample"
_GAP = rf"(?:(?!{_RESOURCE})[^.?!\n]){{0,25}}?"
# "보여줘", "알려 줄래", "출력해", "확인해 줘"; adnominal forms such as "보여주는 모델" are not requests.
_HAND_OVER = (r"(?:(?:보여|알려|읊어|넘겨|보내|적어|말해)\s*(?:줘|주세요|줄래|줄\s*수|주시|주라|달라|봐|라\b)"
              r"|(?:공개|출력|확인|덤프)\s*(?:해|하라|하세요|시켜)|(?:뭐|무엇|뭔)\s*(?:야|니|예요|에요|인가요|인지|이야|냐|데))")
_HAND_OVER_EN = r"\b(?:show|reveal|print|tell|give|display|output|repeat|dump|leak)\b[^.?!\n]{0,40}?"
BLOCK_RULES = {
    "instruction_override": re.compile(
        r"(?:^|[.!?]\s*)(?:(?:이전|기존|위의|앞의|모든)\s*(?:시스템\s*)?(?:지시(?:사항)?|명령|규칙)(?:을|를)?\s*"
        r"(?:무시해(?:줘|주세요|라)?|무시하고|잊어(?:줘|라)?)|(?:ignore|disregard)\s+(?:all\s+)?"
        r"(?:previous|prior|system|above)\s+(?:instructions?|rules?|prompts?))(?=\s|[.!?,]|$)", re.I),

    "system_prompt": re.compile(
        r"(?:시스템|내부|숨겨진|숨긴|비공개|비밀|초기|원래|처음에?\s*(?:받은|설정된)|너의?|네|니|당신의?|"
        r"이\s*서비스의?|모델\s*스카우트의?)\s*(?:의\s*)?(?:시스템\s*)?(?:프롬프트|지침|지시\s*사항|지시문)"
        rf"{_GAP}{_HAND_OVER}|{_HAND_OVER_EN}\b(?:system\s*prompt|hidden\s+instructions|your\s+(?:instructions|prompt|rules))",
        re.I),
    "service_secret": re.compile(
        r"(?:서버|내부|시스템|서비스|운영|백엔드|backend|너희|니네|네가|너가|당신이|이\s*사이트|모델\s*스카우트)"
        r"[^.?!\n]{0,15}?(?:api\s*키|api\s*key|접속\s*키|액세스\s*키|access\s*key|비밀\s*키|secret|토큰|token|비밀번호|비번|"
        rf"password|credential|자격\s*증명|환경\s*변수|\.env){_GAP}{_HAND_OVER}",
        re.I),
    "private_conversation": re.compile(
        r"(?:다른\s*(?:사용자|사람|유저|이용자|회원|고객)|타인|남의|남들|other\s+users?|another\s+user)"
        rf"{_GAP}(?:대화|채팅|질문\s*내역|기록|내역|히스토리|메시지|conversation|chat|history|messages?){_GAP}{_HAND_OVER}",
        re.I),
    "verdict_tampering": re.compile(
        r"(?:검증|확인|평가|검수|라이선스|상업\s*이용)\s*(?:이\s*)?(?:안\s*된|안된|되지\s*않은|안\s*한|미완료|미확인|불분명한?)"
        r"[^.?!\n]{0,25}?(?:검증|확인|통과|허용|가능|완료|합격)\s*(?:완료|됨|된\s*것)?\s*(?:으로|로|처럼|이라고|라고)"
        r"[^.?!\n]{0,10}?(?:표시|표기|바꿔|바꾸|처리|적어|써|기록|달아)"
        r"|(?:가짜로|허위로|거짓으로|임의로|마음대로|무조건)[^.?!\n]{0,20}?(?:검증|평가|점수|순위|라이선스|벤치마크|성능|상업\s*이용)"
        r"[^.?!\n]{0,15}?(?:표시|표기|바꿔|올려|높여|처리|적어|써|만들어|달아)",
        re.I),
}


def blocked_request(text: str) -> str | None:
    """The refusal kind (a SECURITY_NOTICES key) for a request to expose or falsify service data, else None."""
    detection = _normalize(text)
    return next((kind for kind, pattern in BLOCK_RULES.items() if pattern.search(detection)), None)


def _is_placeholder(value: str) -> bool:
    value = value.strip("\"'").strip()
    return (value.casefold() in PLACEHOLDERS
            or bool(re.fullmatch(r"<[^<>]{1,80}>|\[(?:[A-Z_]+)\]?|\$\{[A-Z_][A-Z0-9_]*\}", value))
            or bool(re.fullmatch(r"[xX*•.]+", value)))


def _normalize(text: str) -> str:
    return re.sub(r"[\u200b-\u200d\ufeff]", "", unicodedata.normalize("NFKC", text))


def _assignment_kind(match: re.Match) -> str | None:
    value = match["value"].strip("\"'")
    if _is_placeholder(value):
        return None
    if match["label"].casefold() in {"password", "passwd", "pwd", "비밀번호", "비번"}:
        return "password"
    # Keys look random: words like "토큰: sentencepiece" or "토큰: 1000000000" are not secrets.
    if len(value) >= 16 and re.search(r"[A-Za-z]", value) and re.search(r"\d", value):
        return "api_key"
    return None


def _redact_secrets(text: str) -> str:
    text = BEARER_RE.sub("[SECRET]", TOKEN_RE.sub("[SECRET]", _normalize(text)))
    return ASSIGNMENT_RE.sub(lambda m: m[0][:m.start("value") - m.start()] + "[SECRET]"
                             if _assignment_kind(m) else m[0], text)


def protect_text(text: str) -> GuardResult:
    """Raise a constant safe error on a secret; otherwise return masked text and category-only signals."""
    # Normalize only the detection view; preserve original wording outside redacted PII.
    detection = _normalize(text)
    if TOKEN_RE.search(detection) or BEARER_RE.search(detection):
        raise InputBlocked("api_key")
    for match in ASSIGNMENT_RE.finditer(detection):
        if kind := _assignment_kind(match):
            raise InputBlocked(kind)
    masked = []
    for kind, pattern in PII_RULES:
        text, count = pattern.subn(f"[{kind}]", text)
        if count:
            masked.append(kind)
    signals = tuple(name for name, pattern in INJECTION_RULES.items() if re.search(pattern, detection, re.I))
    return GuardResult(text, tuple(masked), signals)


def protect_context(value: Any) -> Any:
    """Apply the same rules to supplied/saved question context before it reaches an LLM.

    Never raises: saved rows and README sources are not user-editable, so secrets are masked as [SECRET].
    Non-string values and container shapes are preserved. Historical DB rows are not rewritten.
    """
    if isinstance(value, str):
        try:
            return protect_text(value).text
        except InputBlocked:
            return protect_text(_redact_secrets(value)).text
    if isinstance(value, list):
        return [protect_context(item) for item in value]
    if isinstance(value, dict):
        return {protect_context(key): protect_context(item) for key, item in value.items()}
    return value
