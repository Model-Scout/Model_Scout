"""First-pass input rules, not a complete prompt-injection defense.

Known credentials block processing; PII is masked; broad injection patterns are diagnostic signals.
security_reason() separately rejects explicit service abuse before inference.
Exceptions and diagnostics contain categories only; GuardResult.text carries the masked input.
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


# These rules reject explicit requests to expose, alter or bypass service-owned resources.
# INJECTION_RULES above remain broad diagnostic signals, including legitimate security research.
SECURITY_MESSAGES = {
    "internal_instructions": "Model Scout의 내부 시스템 지침은 공개할 수 없어요. 찾고 있는 모델이나 데이터를 알려주세요.",
    "service_credentials": "서비스의 API 키·비밀번호·접속정보는 제공할 수 없어요.",
    "private_data": "다른 사용자의 비공개 입력과 개인정보는 제공할 수 없어요.",
    "unauthorized_action": "접근 권한이나 보안 검사를 우회하거나 서비스 데이터를 임의로 변경하는 요청은 처리할 수 없어요.",
    "verdict_tampering": "추천 결과에는 확인된 근거와 검증 상태를 그대로 표시해요.",
}
# A request for a detector, example or public resource is left to the existing pipeline.
_RESOURCE_PURPOSE = r"탐지|검출|방지|예시|예제|템플릿|샘플|작성법|모델|데이터셋|공개\s*데이터|detector|example|template|dataset"
_REQUEST_GAP = rf"(?:(?!{_RESOURCE_PURPOSE})[^.!?\n]){{0,80}}?"
_DISCLOSE = (
    r"(?:(?:보여|알려|넘겨|보내|적어|말해|읽어)\s*(?:줘(?:요)?|주세요|주라|줄래|줄\s*수|봐|라\b)"
    r"|(?:공개|출력|조회|덤프|추출|전송|내보내기)\s*(?:해|하라|하세요|시켜)"
    r"|(?:뭐|무엇|뭔)\s*(?:야|니|예요|에요|인가요|인지|이야|냐))"
)
_INTERNAL_PROMPT = (
    r"(?:시스템|내부|숨겨진|비공개|초기|너의?|네|니|당신의?|모델\s*스카우트의?|model\s*scout)"
    r"\s*(?:의\s*)?(?:(?:내부|시스템|숨겨진|초기)\s*)?(?:프롬프트|지침|지시\s*사항|지시문)"
)
_SERVICE = r"(?:서비스|서버|운영|내부|시스템|너희|니네|너의|백엔드|모델\s*스카우트|model\s*scout)"
_OTHERS = r"(?:다른\s*(?:사용자|사람|유저|회원|고객)|타인|남의|other\s+users?|another\s+user)"
_PRIVATE_OBJECT = r"(?:프롬프트|대화|채팅|입력|기록|개인정보|이메일|회원정보|메시지|prompts?|chats?|messages?|emails?)"
_SECURITY_RULES = {
    "internal_instructions": re.compile(
        rf"{_INTERNAL_PROMPT}{_REQUEST_GAP}{_DISCLOSE}"
        rf"|\b(?:show|reveal|print|repeat|give|translate|encode|output|dump)\b{_REQUEST_GAP}"
        r"\b(?:system\s*prompt|hidden\s+(?:instructions|prompt)|your\s+(?:instructions|prompt|rules))", re.I),
    "service_credentials": re.compile(
        rf"{_SERVICE}[^.!?\n]{{0,40}}?(?:api\s*(?:키|key)|비밀번호|비번|접속\s*(?:정보|주소)|"
        rf"연결\s*문자열|토큰|환경\s*변수|\.env|credentials?|password|secrets?){_REQUEST_GAP}{_DISCLOSE}"
        rf"|(?:운영\s*)?supabase[^.!?\n]{{0,30}}(?:접속|연결|비밀번호){_REQUEST_GAP}{_DISCLOSE}"
        rf"|(?:서버|운영|내부){_REQUEST_GAP}\.env{_REQUEST_GAP}{_DISCLOSE}"
        r"|\b(?:show|reveal|print|give|dump)\b[^.!?\n]{0,40}?"
        r"\b(?:your|server|service|production)\b[^.!?\n]{0,30}?"
        r"(?:api\s*key|password|credentials?|secrets?|\.env)", re.I),
    "private_data": re.compile(
        rf"{_OTHERS}{_REQUEST_GAP}{_PRIVATE_OBJECT}{_REQUEST_GAP}{_DISCLOSE}"
        rf"|(?:운영|서비스|내부)\s*(?:db|데이터베이스){_REQUEST_GAP}"
        rf"(?:사용자|회원|대화|채팅){_REQUEST_GAP}{_DISCLOSE}"
        rf"|\b(?:show|reveal|print|give|export|dump|send)\b[^.!?\n]{{0,40}}"
        rf"{_OTHERS}{_REQUEST_GAP}{_PRIVATE_OBJECT}", re.I),
    "unauthorized_action": re.compile(
        r"(?:^|[.!?\n]\s*)(?:이전|기존|위의|앞의|모든)\s*(?:시스템\s*)?(?:지시(?:사항)?|명령|규칙)"
        r"[^.!?\n]{0,15}?(?:무시해|무시하고|잊어)"
        r"|(?:^|[.!?\n]\s*)(?:ignore|disregard|forget)\s+(?:all\s+)?(?:previous|prior|system|above)\s+(?:instructions?|rules?)"
        r"|(?:^|[.!?\n]\s*)(?:너는\s*이제|지금부터\s*(?:너는\s*)?)\s*(?:관리자|개발자|시스템)\s*(?:야|다|모드)"
        r"|(?:^|[.!?\n]\s*)you\s+are\s+now\s+(?:an?\s+)?(?:admin|administrator|developer|system)\b"
        r"|(?:보안\s*검사|권한\s*검사|접근\s*권한|인증\s*검사|보호\s*규칙)"
        r"[^.!?\n]{0,20}?(?:건너뛰어|건너뛰고|우회해|우회하고|꺼\s*줘|끄고|비활성화해|무시해)"
        rf"|{_SERVICE}[^.!?\n]{{0,30}}(?:db|데이터베이스|대화|기록)"
        r"[^.!?\n]{0,40}?(?:삭제해|지워\s*줘|지워줘|변조해|덮어써)"
        r"|\b(?:disable|bypass|skip)\s+(?:the\s+)?(?:security|permission|authorization|authentication)\s*(?:checks?|rules?|controls?)", re.I),
    "verdict_tampering": re.compile(
        r"(?:검증|확인|평가|검수|라이선스|상업\s*이용)\s*(?:을\s*|이\s*)?"
        r"(?:안\s*된|안\s*한|안\s*해도|하지\s*않은|되지\s*않은|미확인|불분명한)"
        r"[^.!?\n]{0,50}?(?:검증|확인|허용|가능|완료|통과)"
        r"[^.!?\n]{0,15}?(?:표시해|표시해줘|표기해|바꿔|적어|써\s*줘)"
        r"|(?:가짜로|허위로|거짓으로|임의로)[^.!?\n]{0,30}"
        r"(?:검증|평가|점수|순위|라이선스|벤치마크)[^.!?\n]{0,20}(?:표시해|바꿔|올려|써\s*줘)", re.I),
}

# A quoted attack used as the subject of a detector search is reference text.
# Mask only the quote: any direct instruction elsewhere in the request is still checked.
_RESEARCH_QUOTE = re.compile(
    r"(['\"`])[^\n]{1,300}?\1(?=\s*(?:같은|라는|와\s*같은)?\s*(?:공격|문장|표현|요청)"
    r"[^.!?\n]{0,30}?(?:탐지|검출|분류|방지)[^.!?\n]{0,20}?(?:모델|데이터셋))"
)


def security_reason(text: str) -> str | None:
    """Return a fixed refusal category for explicit service abuse. No model, DB or tool calls."""
    detection = _RESEARCH_QUOTE.sub("[공격 예시]", _normalize(text))
    return next((reason for reason, pattern in _SECURITY_RULES.items() if pattern.search(detection)), None)


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
