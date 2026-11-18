"""Supabase Postgres connection and pgvector text helpers shared by the dataset stages.

Same connection settings as 08_sync_supabase.py (SUPABASE_DB_* in .env).
"""

from __future__ import annotations

import os
from pathlib import Path

ENV_NAMES = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")
# Local validation (deploy/compose.local.yml): Supabase is read only, every write goes to these hosts.
LOCAL_DB_HOSTS = {"postgres", "localhost", "127.0.0.1"}
READ_ONLY_OPTIONS = "-c default_transaction_read_only=on"


def local_mode():
    return os.getenv("MODEL_SCOUT_LOCAL") == "1"


def require_local_host(host, what):
    """In local mode a write target must be the local Postgres; never fall back to production."""
    if local_mode() and host not in LOCAL_DB_HOSTS:
        raise RuntimeError(f"MODEL_SCOUT_LOCAL=1: {what} must be a local Postgres {sorted(LOCAL_DB_HOSTS)}, not {host!r}")


def configured():
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent / ".env")
    return all(os.getenv(name) for name in ENV_NAMES)


def db_connection():
    import psycopg2

    if not configured():
        missing = [name for name in ENV_NAMES if not os.getenv(name)]
        raise RuntimeError("Missing Supabase environment variables: " + ", ".join(missing))
    return psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"],
        port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"],
        user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"],
        sslmode="require",
        connect_timeout=15,
        # A local run reads production data; the server refuses any write in these sessions.
        **({"options": READ_ONLY_OPTIONS} if local_mode() else {}),
    )


def vector_literal(values):
    return "[" + ",".join(f"{float(v):.6g}" for v in values) + "]"


def parse_vector(text):
    import numpy as np

    return np.asarray(text.strip()[1:-1].split(","), dtype=np.float32)


if __name__ == "__main__":
    import numpy as np

    vec = np.asarray([0.5, -0.25, 1e-3], dtype=np.float16)
    assert np.allclose(parse_vector(vector_literal(vec)), vec.astype(np.float32), atol=1e-6)
    print("supabase_db ok")
