"""First-pass input rules, not a complete prompt-injection defense.

Known credentials block processing; PII is masked; injection patterns are signals only.
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
