#!/usr/bin/env python3
"""백필된 Stage 2로 Stage 4를 다시 만든다. 바뀐 모델만 임베딩한다.

Stage 3 는 다시 돌리지 않는다
    Stage 3 의 입력은 README 뿐이다(03_generate_semantic_metadata 가 읽는 것은
    source.readme 하나다). 파라미터 수를 채워도 claim 은 달라지지 않으므로
    기존 출력을 그대로 승계한다. LLM 호출이 없으니 비용도 없다.

    다만 Stage 3 는 stage2 행 전체를 해시해 재실행을 판정한다
    (source_stage2_hash). 정식 파이프라인으로 돌리면 1,724개가 재실행 대상이
    된다. 여기서는 병행 데이터셋을 만드는 것이므로 승계가 맞고, 교체 시점에
    팀이 Stage 3 재실행 여부를 결정하면 된다.

Stage 4 는 다시 돌려야 한다
    build_embedding_text() 가 파라미터 수·컨텍스트 길이·architecture·hardware 를
    본문에 담는다. 값이 바뀌면 문서가 바뀌고 document_hash 도 바뀐다.
    바뀐 문서만 다시 임베딩한다.

    python ai/backfill/rebuild_stage4.py --estimate   # 비용만 계산
    python ai/backfill/rebuild_stage4.py --apply      # 실제 임베딩
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
DATA_DIR = AI_ROOT / "data"
OUT_DIR = HERE / "out"
REPORT_PATH = HERE / "reports" / "stage4_rebuild.json"

POOLS = ("core", "low_popularity")
MODEL = os.getenv("STAGE4_EMBEDDING_MODEL", "text-embedding-3-small")
PRICE_PER_1M = 0.02      # text-embedding-3-small, 2026-11 기준
BATCH = 100


def builder() -> Any:
    sys.path.insert(0, str(AI_ROOT))
    spec = importlib.util.spec_from_file_location(
        "backfill_stage4", AI_ROOT / "04_build_embeddings.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def assemble(pool: str, stage2_dir: Path) -> List[Dict[str, Any]]:
    """04_build_embeddings 가 기대하는 모양으로 stage2 + stage3 를 합친다."""
    stage2 = {row["model_id"]: row for row in read_jsonl(stage2_dir / f"hf_models_stage2_{pool}.jsonl")}
    stage3 = {row["model_id"]: row for row in read_jsonl(DATA_DIR / f"hf_models_stage3_{pool}.jsonl")}
    rows: List[Dict[str, Any]] = []
    for model_id, source in stage2.items():
        semantic_row = stage3.get(model_id)
        if semantic_row is None:
            continue
        # Stage 3 행을 통째로 승계하고 source_stage2 만 백필본으로 바꾼다.
        # build_document 가 stage3 / status / evidence 를 그대로 읽으므로
        # 키 이름을 임의로 바꾸면 안 된다.
        row = dict(semantic_row)
        row["source_stage2"] = source
        row["source_pool"] = pool
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--estimate", action="store_true", help="비용만 계산하고 끝낸다")
    parser.add_argument("--apply", action="store_true", help="실제로 임베딩한다")
    args = parser.parse_args()
    if not (args.estimate or args.apply):
        parser.print_help()
        return

    module = builder()
    changed: List[Dict[str, Any]] = []
    unchanged = 0
    per_pool: Dict[str, Dict[str, int]] = {}

    for pool in POOLS:
        before = {row["model_id"]: row for row in assemble(pool, DATA_DIR)}
        # 로컬 Stage 4 가 Supabase 보다 19행 뒤처져 있어, 문서가 안 바뀌었어도
        # 재사용할 벡터가 없는 모델이 있다. 그런 모델도 임베딩해야 빠지지 않는다.
        has_vector = set()
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if path.exists():
            has_vector = {row["model_id"] for row in read_jsonl(path) if row.get("embedding")}
        after = assemble(pool, OUT_DIR)
        pool_changed = 0
        for row in after:
            text_after = module.build_embedding_text(row)
            source = before.get(row["model_id"])
            text_before = module.build_embedding_text(source) if source else None
            row["embedding_text"] = text_after
            row["document_hash"] = module.digest(text_after)
            if text_before != text_after or row["model_id"] not in has_vector:
                changed.append(row)
                pool_changed += 1
            else:
                unchanged += 1
        per_pool[pool] = {"rows": len(after), "changed": pool_changed}
        print(f"{pool:16s} {len(after):5d}행  문서 바뀜 {pool_changed:5d}")

    total_chars = sum(len(row["embedding_text"]) for row in changed)
    # 한국어·영어가 섞인 문서라 대략 3자당 1토큰으로 잡는다. 보수적으로 본다.
    tokens = total_chars / 3
    cost = tokens / 1_000_000 * PRICE_PER_1M

    print()
    print(f"다시 임베딩할 문서   {len(changed)}")
    print(f"그대로 두는 문서     {unchanged}")
    print(f"총 글자수            {total_chars:,}")
    print(f"추정 토큰            {tokens:,.0f}")
    print(f"추정 비용            ${cost:.3f}  ({MODEL}, 1M토큰당 ${PRICE_PER_1M})")

    if args.estimate:
        print("\n--estimate 모드. 임베딩하지 않았습니다.")
        return

    if not os.getenv("OPENAI_API_KEY"):
        from dotenv import load_dotenv

        load_dotenv(AI_ROOT / ".env")
        load_dotenv(AI_ROOT.parent / ".env")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY 없음")

    from openai import OpenAI

    client = OpenAI()
    print()
    started = time.perf_counter()
    vectors: Dict[str, List[float]] = {}
    for index in range(0, len(changed), BATCH):
        chunk = changed[index:index + BATCH]
        response = client.embeddings.create(
            model=MODEL, input=[row["embedding_text"] for row in chunk]
        )
        for row, item in zip(chunk, response.data):
            vectors[row["model_id"]] = item.embedding
        done = min(index + BATCH, len(changed))
        print(f"  {done}/{len(changed)}  {time.perf_counter() - started:.0f}s", flush=True)

    # 바뀐 문서는 새 벡터로, 나머지는 기존 Stage 4 벡터를 그대로 쓴다.
    written = reused = 0
    for pool in POOLS:
        existing = {row["model_id"]: row for row in read_jsonl(DATA_DIR / f"hf_models_stage4_{pool}.jsonl")}
        rows_out: List[str] = []
        for row in assemble(pool, OUT_DIR):
            text = module.build_embedding_text(row)
            model_id = row["model_id"]
            vector = vectors.get(model_id)
            if vector is None:
                old = existing.get(model_id)
                if old is None:
                    continue
                vector = old.get("embedding")
                reused += 1
            else:
                written += 1
            # 04_build_embeddings.build_document 를 그대로 쓴다. 직접 조립했더니
            # task, candidate, popularity, search_aliases 등 12개 키가 빠져서
            # hard_filter 가 전부 탈락시켰다. 운영과 같은 함수를 써야 한다.
            document = module.build_document(row, MODEL)
            document["embedding"] = vector
            document["embedding_dimensions"] = len(vector) if vector else None
            backfill = (row["source_stage2"] or {}).get("backfill")
            if backfill:
                document["backfill"] = backfill
            rows_out.append(json.dumps(document, ensure_ascii=False))
        target = OUT_DIR / f"hf_models_stage4_{pool}.jsonl"
        target.write_text("\n".join(rows_out) + "\n", encoding="utf-8")
        print(f"{pool:16s} → {target.name}  {len(rows_out)}행")

    print(f"\n새 벡터 {written} · 기존 벡터 재사용 {reused} · {time.perf_counter() - started:.0f}s")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps({
        "embedding_model": MODEL,
        "documents_changed": len(changed),
        "documents_unchanged": unchanged,
        "vectors_new": written,
        "vectors_reused": reused,
        "estimated_tokens": int(tokens),
        "estimated_cost_usd": round(cost, 4),
        "by_pool": per_pool,
        "stage3": "기존 출력 승계. README 가 바뀌지 않아 claim 도 같다.",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
