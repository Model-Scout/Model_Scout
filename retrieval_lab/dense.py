"""BGE-M3 dense channel: document index on disk, query encoder in memory.

Build the document index once. On a laptop CPU this takes hours (about 5 s per
document at 1,024 tokens); a GPU takes minutes. The build checkpoints every
chunk and resumes when re-run. The result is committed so the team can skip it:

    python -m retrieval_lab.dense --build
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Sequence

import numpy as np

from retrieval_lab.corpus import DATA_DIR, load_rows

MODEL_NAME = os.getenv("DENSE_MODEL", "BAAI/bge-m3")
INDEX_DIR = DATA_DIR / "retrieval_lab"
VECTORS_PATH = INDEX_DIR / "bge_m3_doc_embeddings.npy"
MANIFEST_PATH = INDEX_DIR / "bge_m3_doc_manifest.json"
CHECKPOINT_DIR = INDEX_DIR / ".bge_m3_build"
CHUNK_SIZE = 64
DOC_MAX_TOKENS = 1024
QUERY_MAX_TOKENS = 512


def doc_text(row: Dict[str, Any]) -> str:
    return str(row.get("embedding_text") or row.get("model_id") or "")


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


@lru_cache(maxsize=1)
def encoder() -> Any:
    from sentence_transformers import SentenceTransformer

    import torch

    model = SentenceTransformer(MODEL_NAME, device="cuda" if torch.cuda.is_available() else "cpu")
    model.max_seq_length = QUERY_MAX_TOKENS
    return model


def encode(texts: Sequence[str], max_tokens: int = QUERY_MAX_TOKENS, batch_size: int = 16) -> np.ndarray:
    model = encoder()
    model.max_seq_length = max_tokens
    vectors = model.encode(list(texts), batch_size=batch_size, normalize_embeddings=True, show_progress_bar=len(texts) > 64)
    return np.asarray(vectors, dtype=np.float32)


class DenseIndex:
    """Normalized document vectors aligned with corpus row order by model_id."""

    def __init__(self, rows: Sequence[Dict[str, Any]]) -> None:
        if not VECTORS_PATH.exists() or not MANIFEST_PATH.exists():
            raise FileNotFoundError(f"{VECTORS_PATH} 없음. `python -m retrieval_lab.dense --build`를 먼저 실행하세요.")
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if manifest["model"] != MODEL_NAME:
            raise ValueError(f"index model {manifest['model']} != DENSE_MODEL {MODEL_NAME}")
        matrix = np.load(VECTORS_PATH).astype(np.float32)
        position = {model_id: index for index, model_id in enumerate(manifest["model_ids"])}
        stale = [
            row["model_id"] for row in rows
            if row["model_id"] not in position
            or manifest["text_hashes"][position[row["model_id"]]] != text_hash(doc_text(row))
        ]
        if stale:
            raise ValueError(f"dense index가 corpus와 다릅니다({len(stale)}개, 예: {stale[:3]}). --build로 다시 만드세요.")
        self.matrix = matrix[[position[row["model_id"]] for row in rows]]

    def scores(self, query_vector: np.ndarray) -> np.ndarray:
        return self.matrix @ query_vector


def build() -> None:
    rows = load_rows()
    texts = [doc_text(row) for row in rows]
    hashes = [text_hash(text) for text in texts]
    # Chunk files are keyed by their content hash, so a resumed build never
    # mixes vectors from a different corpus snapshot.
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    chunks: List[np.ndarray] = []
    for start in range(0, len(texts), CHUNK_SIZE):
        key = text_hash(MODEL_NAME + str(DOC_MAX_TOKENS) + "".join(hashes[start:start + CHUNK_SIZE]))
        path = CHECKPOINT_DIR / f"{start:05d}_{key}.npy"
        if not path.exists():
            np.save(path, encode(texts[start:start + CHUNK_SIZE], max_tokens=DOC_MAX_TOKENS, batch_size=8))
            done = min(start + CHUNK_SIZE, len(texts))
            print(f"{done}/{len(texts)} docs, {time.perf_counter() - started:.0f}s", flush=True)
        chunks.append(np.load(path))
    vectors = np.concatenate(chunks)
    np.save(VECTORS_PATH, vectors.astype(np.float16))
    manifest = {
        "model": MODEL_NAME,
        "dimension": int(vectors.shape[1]),
        "doc_max_tokens": DOC_MAX_TOKENS,
        "doc_field": "embedding_text",
        "dtype": "float16",
        "rows": len(rows),
        "build_seconds": round(time.perf_counter() - started, 1),
        "model_ids": [row["model_id"] for row in rows],
        "text_hashes": hashes,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: manifest[key] for key in ("model", "rows", "dimension", "build_seconds")}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--build", action="store_true", help="문서 임베딩을 새로 만든다")
    args = parser.parse_args()
    if args.build:
        build()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
