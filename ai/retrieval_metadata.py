"""Deterministic query/model metadata helpers shared by retrieval and indexing.

These helpers intentionally do not change Stage 1 candidate classification. They add
search aliases and translation-pair metadata so lexical retrieval can understand
natural language queries without requiring a manually maintained catalogue for every
language.
"""
from __future__ import annotations

import copy
import re
from typing import Any, Iterable, Mapping, Optional

# Common aliases are deliberately small and stable. Unknown language names/codes are
# preserved as-is by the normalizer, so adding a language never requires a new release.
_LANGUAGE_ALIASES = {
    "ko": {"ko", "kor", "korean", "한국어", "한국어로", "한국말"},
    "en": {"en", "eng", "english", "영어", "영어로"},
    "de": {"de", "deu", "ger", "german", "독일어", "독일어로"},
    "ja": {"ja", "jpn", "japanese", "일본어", "일본어로"},
    "zh": {"zh", "zho", "chi", "chinese", "중국어", "중국어로"},
    "fr": {"fr", "fra", "fre", "french", "프랑스어", "프랑스어로"},
    "es": {"es", "spa", "spanish", "스페인어", "스페인어로"},
    "it": {"it", "ita", "italian", "이탈리아어", "이탈리아어로"},
    "pt": {"pt", "por", "portuguese", "포르투갈어", "포르투갈어로"},
    "ru": {"ru", "rus", "russian", "러시아어", "러시아어로"},
    "ar": {"ar", "ara", "arabic", "아랍어", "아랍어로"},
    "hi": {"hi", "hin", "hindi", "힌디어", "힌디어로"},
    "vi": {"vi", "vie", "vietnamese", "베트남어", "베트남어로"},
    "id": {"id", "ind", "indonesian", "인도네시아어", "인도네시아어로"},
    "th": {"th", "tha", "thai", "태국어", "태국어로"},
    "tr": {"tr", "tur", "turkish", "터키어", "터키어로"},
    "nl": {"nl", "nld", "dut", "dutch", "네덜란드어", "네덜란드어로"},
    "pl": {"pl", "pol", "polish", "폴란드어", "폴란드어로"},
    "sv": {"sv", "swe", "swedish", "스웨덴어", "스웨덴어로"},
    "fi": {"fi", "fin", "finnish", "핀란드어", "핀란드어로"},
    "no": {"no", "nor", "norwegian", "노르웨이어", "노르웨이어로"},
    "da": {"da", "dan", "danish", "덴마크어", "덴마크어로"},
    "cs": {"cs", "ces", "cze", "czech", "체코어", "체코어로"},
    "el": {"el", "ell", "gre", "greek", "그리스어", "그리스어로"},
    "he": {"he", "heb", "hebrew", "히브리어", "히브리어로"},
    "fa": {"fa", "fas", "per", "persian", "페르시아어", "페르시아어로"},
    "uk": {"uk", "ukr", "ukrainian", "우크라이나어", "우크라이나어로"},
    "yo": {"yo", "yor", "yoruba", "요루바어", "요루바어로"},
}
_ALIAS_TO_CODE = {
    alias.casefold(): code
    for code, aliases in _LANGUAGE_ALIASES.items()
    for alias in aliases
}
_CODE_RE = re.compile(r"(?<![a-z0-9])([a-z]{2,3})[-_.]([a-z]{2,3})(?![a-z0-9])", re.I)
_TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*|[가-힣]+")


def normalize_language_code(value: Any) -> str:
    """Return a stable two-letter code when the value is known, else a safe token."""
    raw = str(value or "").strip().casefold()
    if not raw:
        return ""
    return _ALIAS_TO_CODE.get(raw, raw)


def _flatten(values: Any) -> list[str]:
    if values is None:
        return []
    if isinstance(values, Mapping):
        out: list[str] = []
        for key, value in values.items():
            out.extend(_flatten(key))
            out.extend(_flatten(value))
        return out
    if isinstance(values, (list, tuple, set)):
        out: list[str] = []
        for value in values:
            out.extend(_flatten(value))
        return out
    return [str(values)]


def normalized_language_codes(values: Any) -> list[str]:
    result: list[str] = []
    for value in _flatten(values):
        code = normalize_language_code(value)
        if code and code not in result:
            result.append(code)
    return result


def extract_translation_pairs(model_id: str, declared_languages: Optional[Iterable[Any]] = None) -> list[str]:
    """Extract explicit ordered language pairs from a model ID.

    We only accept known language aliases or codes present in structured metadata;
    generic substrings such as ``koala`` and ``tokenizer`` never match.
    """
    model_text = str(model_id or "").casefold()
    # A bare ``it-ko`` can mean instruction-tuned Korean rather than Italian→Korean.
    # Require an explicit translation-family marker before treating a pair as a
    # translation capability signal.
    if not re.search(r"(?:translation|translate|translator|opus[-_.]?mt|nllb|m2m(?:100)?|marian|mbart)", model_text):
        return []
    declared_codes = set(normalized_language_codes(declared_languages))
    known_codes = set(_LANGUAGE_ALIASES)
    # ``it`` is frequently the conventional "instruction-tuned" marker in
    # LLM names (for example ``gemma-it-ko``), so accept it as Italian only when
    # structured metadata explicitly declares it.
    if "it" not in declared_codes:
        known_codes.discard("it")
    known_codes.update(declared_codes)
    pairs: list[str] = []
    # Split into bounded slug segments rather than relying on a non-overlapping
    # regex; this preserves pairs in chains such as ``ja-en-ko-zh`` and
    # ``opus-mt-tc-big-en-ko``.
    segments = [segment for segment in re.split(r"[-_.\/]+", model_text) if segment]
    candidates = list(_CODE_RE.findall(model_text))
    candidates.extend(zip(segments, segments[1:]))
    for left, right in candidates:
        left_code = normalize_language_code(left)
        right_code = normalize_language_code(right)
        if left_code not in known_codes or right_code not in known_codes:
            continue
        pair = f"{left_code}-{right_code}"
        if pair not in pairs:
            pairs.append(pair)
    return pairs


def _query_language_codes(text: str) -> set[str]:
    codes: set[str] = set()
    lowered = text.casefold()
    for alias, code in _ALIAS_TO_CODE.items():
        if alias.isascii():
            present = bool(re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", lowered))
        else:
            present = alias in lowered
        if present:
            codes.add(code)
    for token in _TOKEN_RE.findall(lowered):
        code = normalize_language_code(token)
        if code in _LANGUAGE_ALIASES:
            codes.add(code)
    return codes


def normalize_query_terms(text: Any) -> set[str]:
    """Expand a query into raw terms, language aliases, and ordered language pairs."""
    raw = str(text or "").casefold()
    terms = {token for token in _TOKEN_RE.findall(raw) if len(token) > 1}
    codes = _query_language_codes(raw)
    terms.update(codes)
    for code in codes:
        for alias in _LANGUAGE_ALIASES.get(code, ()):
            if alias.isascii() and len(alias) > 1:
                terms.add(alias.casefold())
    # Korean/English phrasing and common translation wording make direction explicit.
    translation_markers = {"translation", "translate", "translator", "번역", "번역하는", "번역기", "통역"}
    if terms & translation_markers or any(marker in raw for marker in ("번역", "translation", "translate")):
        # Ordered pair is inferred only from directional phrasing, not from an unordered
        # list of languages. This is query expansion, not a model classification rule.
        source = next((code for code in ("en", "de", "ja", "zh", "fr", "es") if code in codes), None)
        target = "ko" if "ko" in codes else None
        if source and target:
            terms.add(f"{source}-{target}")
            terms.add(f"{source}_{target}")
        elif source and "ko" not in codes:
            terms.add(f"{source}-ko") if "한국" in raw or "korean" in raw else None
    return terms


def build_search_metadata(model_id: str, metadata: Mapping[str, Any] | None = None, task: Any = None) -> dict[str, Any]:
    metadata = metadata or {}
    declared = metadata.get("languages") or metadata.get("declared_languages") or metadata.get("language")
    codes = normalized_language_codes(declared)
    pairs = extract_translation_pairs(model_id, codes)
    aliases = list(dict.fromkeys(codes + pairs + [pair.replace("-", "_") for pair in pairs]))
    if task:
        aliases.extend(normalized_language_codes(task))
    return {
        "search_metadata_version": 1,
        "language_codes": codes,
        "translation_pairs": pairs,
        "search_aliases": list(dict.fromkeys(aliases)),
    }


def augment_filter_metadata(model_id: str, metadata: Mapping[str, Any] | None = None, task: Any = None) -> dict[str, Any]:
    result = copy.deepcopy(dict(metadata or {}))
    derived = build_search_metadata(model_id, result, task)
    result.update(derived)
    return result
