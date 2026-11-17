"""Keep unsupported calendar dates out of explanation events before they are streamed.

This checks date presence in retrieved evidence, not the truth of every generated claim.
Lines are buffered because a date can be split across arbitrary LLM token chunks.
"""

import logging
import re
from collections.abc import Iterable, Iterator


EXPLANATION_CAVEAT = "이용 조건과 실행 가능 여부는 각 모델·데이터셋의 공식 문서에서 확인해 주세요."
DATE_RE = re.compile(
    r"(?<!\d)(?P<year>(?:19|20)\d{2})(?:"
    r"\s*년(?:\s*(?P<ko_month>0?[1-9]|1[0-2])\s*월(?:\s*(?P<ko_day>0?[1-9]|[12]\d|3[01])\s*일)?)?"
    r"|[-/.](?P<iso_month>0[1-9]|1[0-2])(?:[-/.](?P<iso_day>0[1-9]|[12]\d|3[01]))?(?!\d)"
    r")"
)


def dates(text: str) -> set[tuple[int, int | None, int | None]]:
    found = set()
    for match in DATE_RE.finditer(text):
        month = match["ko_month"] or match["iso_month"]
        day = match["ko_day"] or match["iso_day"]
        found.add((int(match["year"]), int(month) if month else None, int(day) if day else None))
    return found


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def grounded_lines(chunks: Iterable[str], evidence: dict) -> Iterator[str]:
    """Drop a whole generated line if it contains a date absent from retrieval evidence.

    A full source date supports mentioning its month/year, but a source year cannot support
    inventing a month/day. Requests, history and generated plans must not be evidence.
    """
    supported = set().union(*(dates(text) for text in _strings(evidence)))

    def allowed(line):
        ok = all(
            any(y == sy and (m is None or m == sm) and (d is None or d == sd)
                for sy, sm, sd in supported)
            for y, m, d in dates(line)
        )
        if not ok:  # category only: a dropped line may be a whole recommendation, so make it visible
            logging.info("explanation line dropped: unsupported date")
        return ok

    pending = ""
    for chunk in chunks:
        pending += chunk
        while "\n" in pending:
            line, pending = pending.split("\n", 1)
            if allowed(line):
                yield line + "\n"
    if pending and allowed(pending):
        yield pending
