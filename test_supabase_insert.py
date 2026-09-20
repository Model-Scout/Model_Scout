import json
import os
from urllib.parse import quote_plus

import psycopg
from dotenv import load_dotenv


load_dotenv()


# =========================================================
# ENV
# =========================================================

DB_HOST = os.getenv("SUPABASE_DB_HOST")
DB_PORT = os.getenv("SUPABASE_DB_PORT", "5432")
DB_NAME = os.getenv("SUPABASE_DB_NAME", "postgres")
DB_USER = os.getenv("SUPABASE_DB_USER")
DB_PASSWORD = os.getenv("SUPABASE_PASSWORD")


required_env = {
    "SUPABASE_DB_HOST": DB_HOST,
    "SUPABASE_DB_USER": DB_USER,
    "SUPABASE_PASSWORD": DB_PASSWORD,
}

missing = [
    key
    for key, value in required_env.items()
    if not value
]

if missing:
    raise RuntimeError(
        f"Missing environment variables: {', '.join(missing)}"
    )


# 비밀번호에 @, :, / 같은 특수문자가 있어도 안전하게 처리
encoded_password = quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# =========================================================
# TEST DATA
# =========================================================

TEST_MODEL_ID = "model-scout/test-model"

metadata = {
    "task": "text-generation",
    "candidate": {
        "tier": "A_verified",
        "type": "korean_explicit",
    },
    "language": {
        "korean": True,
        "multilingual": False,
    },
    "model": {
        "parameter_count": 7_000_000_000,
        "context_length": 32768,
        "dtype": "bfloat16",
    },
    "stage": {
        "stage1_version": 4,
        "stage2_version": 3,
    },
}


# =========================================================
# DB TEST
# =========================================================

print("Connecting to Supabase PostgreSQL...")


with psycopg.connect(
    DATABASE_URL,
    sslmode="require",
) as conn:

    with conn.cursor() as cur:

        # -------------------------------------------------
        # 1. Connection check
        # -------------------------------------------------

        cur.execute(
            """
            SELECT
                current_database(),
                current_user,
                NOW();
            """
        )

        db_info = cur.fetchone()

        print("\n=== CONNECTION SUCCESS ===")
        print("database :", db_info[0])
        print("user     :", db_info[1])
        print("time     :", db_info[2])


        # -------------------------------------------------
        # 2. Create temporary test table
        # -------------------------------------------------

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS model_scout_db_test (
                id BIGSERIAL PRIMARY KEY,
                model_id TEXT UNIQUE NOT NULL,
                source_pool TEXT NOT NULL,
                candidate_tier TEXT,
                metadata JSONB NOT NULL,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            );
            """
        )

        print("\n=== TABLE READY ===")


        # -------------------------------------------------
        # 3. Insert / Upsert one row
        # -------------------------------------------------

        cur.execute(
            """
            INSERT INTO model_scout_db_test (
                model_id,
                source_pool,
                candidate_tier,
                metadata
            )
            VALUES (
                %s,
                %s,
                %s,
                %s::jsonb
            )

            ON CONFLICT (model_id)
            DO UPDATE SET
                source_pool = EXCLUDED.source_pool,
                candidate_tier = EXCLUDED.candidate_tier,
                metadata = EXCLUDED.metadata,
                updated_at = NOW()

            RETURNING id, model_id;
            """,
            (
                TEST_MODEL_ID,
                "core",
                "A_verified",
                json.dumps(
                    metadata,
                    ensure_ascii=False,
                ),
            ),
        )

        inserted = cur.fetchone()

        print("\n=== INSERT / UPSERT SUCCESS ===")
        print("id       :", inserted[0])
        print("model_id :", inserted[1])


        # -------------------------------------------------
        # 4. Select inserted row
        # -------------------------------------------------

        cur.execute(
            """
            SELECT
                id,
                model_id,
                source_pool,
                candidate_tier,
                metadata,
                created_at,
                updated_at
            FROM model_scout_db_test
            WHERE model_id = %s;
            """,
            (TEST_MODEL_ID,),
        )

        row = cur.fetchone()

        print("\n=== SELECT SUCCESS ===")
        print("id             :", row[0])
        print("model_id       :", row[1])
        print("source_pool    :", row[2])
        print("candidate_tier :", row[3])
        print("metadata       :", row[4])
        print("created_at     :", row[5])
        print("updated_at     :", row[6])


        # -------------------------------------------------
        # 5. Count
        # -------------------------------------------------

        cur.execute(
            """
            SELECT COUNT(*)
            FROM model_scout_db_test;
            """
        )

        count = cur.fetchone()[0]

        print("\n=== ROW COUNT ===")
        print(count)


print("\nALL DATABASE TESTS PASSED")