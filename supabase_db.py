"""Supabase Postgres connection and pgvector text helpers shared by the dataset stages.

Same connection settings as 08_sync_supabase.py (SUPABASE_DB_* in .env).
"""
from __future__ import annotations

import os
from pathlib import Path

ENV_NAMES = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")


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
        host=os.environ["SUPABASE_DB_HOST"], port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"], user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"], sslmode="require", connect_timeout=15)


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
