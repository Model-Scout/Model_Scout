"""Trace of recommendation turns: one JSON line per event (assess, explain), keyed by trace_id.

Always one stdout line ("run_log {...}", so `docker compose logs ai` holds it); a file only when
RECOMMEND_LOG_PATH is set (e.g. logs/recommend.jsonl in ai/.env), so tests and other machines write nothing.

Reading it back (file, or "-" for stdin such as docker logs):
    python ai/run_log.py trace 1a2b3c4d-2 logs/recommend.jsonl
    docker compose logs ai | python ai/run_log.py summary -
"""

import json
import logging
import os
import sys
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

_lock = threading.Lock()
_warned = False
MARKER = "run_log "
# USD per 1M tokens, for a rough cost line only; check the provider's billing page for real numbers.
PRICE_PER_M = {"gpt-4.1-mini": (0.40, 1.60)}


def new_trace_id() -> str:
    return uuid.uuid4().hex[:8]


def log_path() -> Path | None:
    value = os.getenv("RECOMMEND_LOG_PATH", "").strip()
    return Path(value) if value and value != "off" else None


def log_event(event: str, **fields) -> None:
    """Never raises: a log that cannot be written must not fail the answer."""
    record = {"ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), "event": event, **fields}
    line = json.dumps(record, ensure_ascii=False, default=str)
    logging.info("%s%s", MARKER, line)  # whole line: the reader parses it back from docker logs
    path = log_path()
    if path is None:
        return
    try:
        # ponytail: one growing file, no rotation; add logrotate or a size cap if it is kept on the server.
        with _lock:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
    except OSError as error:
        global _warned
        if not _warned:  # e.g. the image runs as nobody: say it once, the stdout line still has the record
            _warned = True
            logging.warning("run_log not written to %s: %s (set RECOMMEND_LOG_PATH)", path, error)


def read_records(lines):
    """JSONL lines or log lines carrying "run_log {...}" (any prefix: docker service name, logging level)."""
    for line in lines:
        text = line[line.index(MARKER) + len(MARKER):] if MARKER in line else line.strip()
        if not text.startswith("{"):
            continue
        try:
            record = json.loads(text)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict) and "event" in record:
            yield record


def trace(records, wanted: str) -> list[dict]:
    """Every event of one turn or conversation: a trace id ("1a2b3c4d-2") or any part of the thread/group id."""
    return [r for r in records if wanted in str(r.get("trace_id", "")) or wanted in str(r.get("thread_id", ""))]


def _pct(values, q):
    values = sorted(v for v in values if isinstance(v, (int, float)))
    return values[min(len(values) - 1, int(q * len(values)))] if values else None


def summary(records) -> dict:
    explains = [r for r in records if r["event"] == "explain"]
    assesses = [r for r in records if r["event"] == "assess"]
    checks = [r for r in records if r["event"] == "injection_check"]
    n = len(explains)

    def rate(test):
        return round(sum(1 for r in explains if test(r)) / n, 3) if n else None

    written = [r for r in explains if r.get("usage")]
    cost = 0.0
    priced = 0
    for r in written:
        price = PRICE_PER_M.get(r.get("model"))
        if price:
            priced += 1
            cost += (r["usage"]["prompt"] * price[0] + r["usage"]["completion"] * price[1]) / 1e6
    return {
        "turns": n,
        "explain_s": {"p50": _pct([r.get("elapsed_s") for r in explains], 0.5),
                      "p95": _pct([r.get("elapsed_s") for r in explains], 0.95)},
        "first_token_s": {"p50": _pct([r.get("first_token_s") for r in explains], 0.5),
                          "p95": _pct([r.get("first_token_s") for r in explains], 0.95)},
        "rates": {
            "cut_by_length": rate(lambda r: r.get("finish_reason") == "length"),
            "fallback": rate(lambda r: "error" in r),
            "replayed": rate(lambda r: r.get("writer") == "cache"),
            "writer_skipped": rate(lambda r: r.get("writer") == "skipped"),
            "lines_dropped": rate(lambda r: r.get("dropped_lines")),
            "search_failed": rate(lambda r: r.get("search_errors")),
        },
        "tokens_avg": {
            "prompt": round(sum(r["usage"]["prompt"] for r in written) / len(written)) if written else None,
            "completion": round(sum(r["usage"]["completion"] for r in written) / len(written)) if written else None,
        },
        "explain_cost_usd_estimate": round(cost, 4) if priced else None,
        "card_lookup_failed_turns": sum(1 for r in assesses if (r.get("facts") or {}).get("lookup_failed")),
        "license_verdicts": _count(r.get("license", {}).get("verdict") for r in assesses),
        "prompts": _count(r.get("prompt") for r in explains),
        "errors": _count(r["error"].split(":")[0] for r in explains if r.get("error")),
        # Shadow classifier: "flagged_rule_passed" are the inputs to review before it may block anything.
        "injection_check": {
            "labels": _count(r.get("label") for r in checks),
            "flagged_rule_passed": sum(1 for r in checks if r.get("label") == "injection" and not r.get("rule")),
            "ms": {"p50": _pct([r.get("ms") for r in checks], 0.5), "p95": _pct([r.get("ms") for r in checks], 0.95)},
        },
    }


def _count(values) -> dict:
    out: dict = {}
    for v in values:
        if v is not None:
            out[v] = out.get(v, 0) + 1
    return out


def main(argv) -> int:
    if len(argv) < 2 or argv[0] not in ("trace", "summary") or (argv[0] == "trace" and len(argv) < 3):
        print(__doc__)
        return 2
    source = argv[-1]
    lines = sys.stdin if source == "-" else open(source, encoding="utf-8")
    records = list(read_records(lines))
    out = trace(records, argv[1]) if argv[0] == "trace" else summary(records)
    if argv[0] == "trace":
        for r in out:
            print(json.dumps(r, ensure_ascii=False))
        if not out:
            print(f"no events for {argv[1]}", file=sys.stderr)
            return 1
    else:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


def _self_check():
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        os.environ["RECOMMEND_LOG_PATH"] = f"{tmp}/x/run.jsonl"
        log_event("explain", trace_id="abc", note="한국어")
        row = json.loads(Path(tmp, "x", "run.jsonl").read_text(encoding="utf-8"))
        assert row["event"] == "explain" and row["note"] == "한국어" and row["trace_id"] == "abc", row
        os.environ["RECOMMEND_LOG_PATH"] = "/dev/null/blocked/run.jsonl"
        log_event("explain")  # unwritable path: warns, never raises
    lines = [
        'ai-1  | INFO:root:run_log {"event": "assess", "trace_id": "1a2b3c4d-1", "thread_id": "1a2b3c4d-9", '
        '"facts": {"found": 3, "lookup_failed": 2}, "license": {"verdict": "review"}}',
        '{"event": "explain", "trace_id": "1a2b3c4d-1", "thread_id": "1a2b3c4d-9", "elapsed_s": 6.4, '
        '"first_token_s": 0.7, "finish_reason": "stop", "model": "gpt-4.1-mini", "prompt": "p1", '
        '"usage": {"prompt": 4706, "completion": 856}}',
        '{"event": "explain", "trace_id": "ffff0000-1", "elapsed_s": 9.0, "writer": "cache", "error": "TimeoutError: x"}',
        "ai-1  | INFO:httpx:unrelated line",
        'ai-1  | INFO:root:run_log {"event": "explain", "cut off by the old 1000-char limit',
    ]
    records = list(read_records(lines))
    assert len(records) == 3, records
    assert [r["event"] for r in trace(records, "1a2b3c4d")] == ["assess", "explain"]
    s = summary(records)
    assert s["turns"] == 2 and s["explain_s"]["p50"] == 9.0 and s["rates"]["replayed"] == 0.5, s
    assert s["tokens_avg"] == {"prompt": 4706, "completion": 856} and s["errors"] == {"TimeoutError": 1}, s
    assert s["card_lookup_failed_turns"] == 1 and s["explain_cost_usd_estimate"] == 0.0033, s
    print("run_log ok")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else _self_check())
