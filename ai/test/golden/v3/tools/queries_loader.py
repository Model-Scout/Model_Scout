"""v3/queries.py 를 도구 디렉터리에서 import 하기 위한 얇은 래퍼."""

from __future__ import annotations

import sys
from pathlib import Path

_V3 = str(Path(__file__).resolve().parents[1])
if _V3 not in sys.path:
    sys.path.insert(0, _V3)

from queries import QUERY_TYPES, STYLE_QUOTA_EXEMPTIONS, all_queries  # noqa: E402,F401
