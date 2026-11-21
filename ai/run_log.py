"""Local JSONL trace of recommendation runs: one line per event, keyed by trace_id.

Always one stdout line; a file only when RECOMMEND_LOG_PATH is set (e.g. ai/logs/recommend.jsonl in .env),
so tests and other machines write nothing. A user who reports "추적 ID: 1a2b3c4d" is found with
    grep 1a2b3c4d ai/logs/recommend.jsonl
"""

import json
import logging
import os
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

_lock = threading.Lock()
_warned = False


def new_trace_id() -> str:
    return uuid.uuid4().hex[:8]


def log_path() -> Path | None:
    value = os.getenv("RECOMMEND_LOG_PATH", "").strip()
    return Path(value) if value and value != "off" else None


def log_event(event: str, **fields) -> None:
    """Never raises: a log that cannot be written must not fail the answer."""
    record = {"ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), "event": event, **fields}
    line = json.dumps(record, ensure_ascii=False, default=str)
    logging.info("run_log %s", line[:1000])
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


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        os.environ["RECOMMEND_LOG_PATH"] = f"{tmp}/x/run.jsonl"
        log_event("explain", trace_id="abc", note="한국어")
        row = json.loads(Path(tmp, "x", "run.jsonl").read_text(encoding="utf-8"))
        assert row["event"] == "explain" and row["note"] == "한국어" and row["trace_id"] == "abc", row
        os.environ["RECOMMEND_LOG_PATH"] = "/dev/null/blocked/run.jsonl"
        log_event("explain")  # unwritable path: warns, never raises
    print("run_log ok")
