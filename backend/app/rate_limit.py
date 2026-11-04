"""Per-IP and daily request limits for the endpoints that spend OpenAI credit.

python backend/app/rate_limit.py    # self-check
"""

from __future__ import annotations

import threading
import time
from collections import deque
from collections.abc import Callable

MINUTE = 60
DAY = 86400
MAX_TRACKED_IPS = 10000


class RateLimiter:
    # ponytail: in-process counters; fine for one uvicorn worker, reset on restart. Redis if workers grow.
    def __init__(self, per_minute: int, per_day: int, clock: Callable[[], float] = time.time):
        self.per_minute, self.per_day, self.clock = per_minute, per_day, clock
        self.lock = threading.Lock()
        self.hits: dict[str, deque[float]] = {}
        self.day, self.day_count = -1, 0

    def retry_after(self, ip: str) -> int | None:
        """Record a request and return None, or the seconds to wait when it is over a limit."""
        now = self.clock()
        with self.lock:
            day = int(now // DAY)
            if day != self.day:
                self.day, self.day_count = day, 0
            if self.day_count >= self.per_day:
                return int(DAY - now % DAY) + 1

            hits = self.hits.setdefault(ip, deque())
            while hits and now - hits[0] >= MINUTE:
                hits.popleft()
            if len(hits) >= self.per_minute:
                return int(MINUTE - (now - hits[0])) + 1

            if len(self.hits) > MAX_TRACKED_IPS:
                self.hits = {k: v for k, v in self.hits.items() if v and now - v[-1] < MINUTE}
                self.hits[ip] = hits
            hits.append(now)
            self.day_count += 1
            return None


if __name__ == "__main__":
    t = [1000.0]
    limiter = RateLimiter(per_minute=2, per_day=4, clock=lambda: t[0])
    assert limiter.retry_after("a") is None and limiter.retry_after("a") is None
    assert limiter.retry_after("a") == 61, "third request in a minute waits for the oldest hit"
    assert limiter.retry_after("b") is None, "another IP has its own window"
    t[0] += 60
    assert limiter.retry_after("a") is None, "window slid"
    assert limiter.retry_after("c") is not None, "fifth request of the day hits the daily cap"
    t[0] = DAY * 2.0
    assert limiter.retry_after("c") is None, "new day resets the cap"
    print("rate_limit self-check ok")
