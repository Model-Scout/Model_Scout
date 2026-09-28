#!/usr/bin/env python3
"""Compatibility wrapper for the consolidated benchmark metadata step.

Use ``06_extract_benchmark_metadata.py --apply`` for new runs. This entrypoint
remains so existing local commands do not break, but the implementation lives
in one place.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "model_scout_benchmark_metadata", ROOT / "06_extract_benchmark_metadata.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Could not load consolidated benchmark metadata step")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=[*MODULE.POOLS, "all"], default="all")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    pools = MODULE.POOLS if args.pool == "all" else (args.pool,)
    summaries = [MODULE.integrate_pool(pool, args.apply) for pool in pools]
    print(MODULE.json.dumps({"summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
