#!/usr/bin/env python3
"""백필 Stage 4 용 BGE-M3 인덱스를 만든다. 공유 인덱스는 건드리지 않는다.

검색 품질을 전후로 비교하려면 dense 채널이 양쪽 다 있어야 한다. BGE 는
embedding_text 를 벡터화하는데, 백필로 그 본문이 1,309개 바뀌었으므로 그만큼
다시 인코딩해야 한다. 나머지는 텍스트 해시가 같아 기존 인덱스를 재사용한다.

    python ai/backfill/build_index.py --seed    # 기존 인덱스를 복사 (재사용용)
    python ai/backfill/build_index.py --build
    python ai/backfill/build_index.py --check
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
OUT_DIR = HERE / "out"
INDEX_DIR = HERE / "index"
# 골든셋 v2 인덱스가 3,872행으로 가장 최신이라 재사용 원천으로 쓴다.
SEED_DIR = AI_ROOT / "test" / "golden" / "v2" / "index"
SHARED_DIR = AI_ROOT / "data" / "retrieval_lab"
POOLS = ("core", "low_popularity")


def rows() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for pool in POOLS:
        path = OUT_DIR / f"hf_models_stage4_{pool}.jsonl"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    out.append({
                        "model_id": row["model_id"],
                        "embedding_text": row["embedding_text"],
                    })
    return out


def seed() -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    source = SEED_DIR if (SEED_DIR / "bge_m3_doc_manifest.json").exists() else SHARED_DIR
    for name in ("bge_m3_doc_embeddings.npy", "bge_m3_doc_manifest.json"):
        path = source / name
        if path.exists():
            shutil.copy2(path, INDEX_DIR / name)
    manifest = json.loads((INDEX_DIR / "bge_m3_doc_manifest.json").read_text(encoding="utf-8"))
    print(f"{source} 에서 복사 — 재사용 가능 {manifest['rows']}행")


def build() -> None:
    sys.path.insert(0, str(AI_ROOT))
    from retrieval_lab import dense

    dense.VECTORS_PATH = INDEX_DIR / "bge_m3_doc_embeddings.npy"
    dense.MANIFEST_PATH = INDEX_DIR / "bge_m3_doc_manifest.json"
    dense.CHECKPOINT_DIR = INDEX_DIR / ".bge_m3_build"
    data = rows()
    dense.load_rows = lambda: data
    print(f"백필 Stage 4 {len(data)}행")
    dense.build()


def check() -> None:
    import numpy as np

    manifest = json.loads((INDEX_DIR / "bge_m3_doc_manifest.json").read_text(encoding="utf-8"))
    matrix = np.load(INDEX_DIR / "bge_m3_doc_embeddings.npy")
    data = rows()
    corpus_ids = {row["model_id"] for row in data}
    index_ids = set(manifest["model_ids"])
    print(f"인덱스 {manifest['rows']}행  shape {matrix.shape}")
    print(f"백필 코퍼스 {len(corpus_ids)}행")
    print(f"벡터 없는 모델 {len(corpus_ids - index_ids)} · 코퍼스에 없는 인덱스 {len(index_ids - corpus_ids)}")
    print("✅ 일치" if corpus_ids == index_ids else "❌ 불일치")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", action="store_true")
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.seed:
        seed()
    elif args.build:
        build()
    elif args.check:
        check()
    else:
        parser.print_help()
