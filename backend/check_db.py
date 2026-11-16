"""Read-only check of the database required by the public backend.

Run from the repository root:
    python backend/check_db.py --env-file .env
No credentials or database exception messages are printed.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import psycopg
from psycopg.conninfo import make_conninfo


REQUIRED_ENV = (
    "SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME",
    "SUPABASE_DB_USER", "SUPABASE_PASSWORD",
)
REQUIRED_COLUMNS = {
    "groups": {"group_id", "session_id", "title", "created_at", "updated_at"},
    "messages": {"id", "group_id", "role", "content", "type", "result", "sources", "created_at"},
}


def check_database() -> int:
    missing = [key for key in REQUIRED_ENV if not os.getenv(key)]
    if missing:
        print("FAIL configuration: missing " + ", ".join(missing))
        return 1
    try:
        info = make_conninfo(
            host=os.environ["SUPABASE_DB_HOST"],
            port=os.environ["SUPABASE_DB_PORT"],
            dbname=os.environ["SUPABASE_DB_NAME"],
            user=os.environ["SUPABASE_DB_USER"],
            password=os.environ["SUPABASE_PASSWORD"],
            sslmode=os.getenv("SUPABASE_DB_SSLMODE", "require"),
            connect_timeout=10,
        )
        with psycopg.connect(info) as conn:
            conn.read_only = True
            conn.execute("SET LOCAL statement_timeout = '10s'")
            print("PASS database connection (read-only transaction)")
            ready = True
            for table, expected in REQUIRED_COLUMNS.items():
                relation = f"app.{table}"
                exists = conn.execute("SELECT to_regclass(%s)", (relation,)).fetchone()[0]
                if exists is None:
                    print(f"FAIL {relation}: missing; apply backend/app_schema.sql")
                    ready = False
                    continue
                # PostgreSQL catalogs include columns even when this role lacks table access.
                actual = {row[0] for row in conn.execute(
                    "SELECT attname FROM pg_attribute WHERE attrelid = %s::regclass "
                    "AND attnum > 0 AND NOT attisdropped", (relation,),
                )}
                absent = expected - actual
                if absent:
                    print(f"FAIL {relation}: missing columns " + ", ".join(sorted(absent)))
                    ready = False
                for privilege in ("SELECT", "INSERT", "UPDATE"):
                    allowed = conn.execute(
                        "SELECT has_table_privilege(current_user, %s, %s)",
                        (relation, privilege),
                    ).fetchone()[0]
                    print(f"{'PASS' if allowed else 'FAIL'} {relation}: {privilege} privilege")
                    ready = ready and allowed
                # Check schema access and SELECT permission without reading conversation contents.
                conn.execute(psycopg.sql.SQL("SELECT 1 FROM {}.{} LIMIT 0").format(
                    psycopg.sql.Identifier("app"), psycopg.sql.Identifier(table),
                ))
            print("NOTE: no writes performed; RLS, sequence permissions and save/restore still need E2E verification")
            return 0 if ready else 1
    except (psycopg.Error, ValueError) as exc:
        state = getattr(exc, "sqlstate", None)
        print(f"FAIL database: {type(exc).__name__}; SQLSTATE={state or 'unavailable'}")
        print("Check network/DNS, connection settings, SSL and database permissions. Secrets are omitted.")
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", type=Path, help="Explicit dotenv file; process environment takes precedence")
    args = parser.parse_args()
    if args.env_file is not None:
        if not args.env_file.is_file():
            parser.error("env file does not exist")
        from dotenv import load_dotenv
        load_dotenv(args.env_file, override=False)
    return check_database()


if __name__ == "__main__":
    raise SystemExit(main())
