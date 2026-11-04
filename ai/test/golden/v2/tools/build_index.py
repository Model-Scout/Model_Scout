#!/usr/bin/env python3
"""골든셋 v2 전용 BGE-M3 문서 인덱스를 만든다. 공유 인덱스는 건드리지 않는다.

왜 따로 만드나
--------------
``ai/data/retrieval_lab/bge_m3_*``는 3,606행이고 팀원 9개 도구가 같이 읽는다.
그걸 덮어쓰면 다른 사람 실험 숫자가 예고 없이 바뀐다. v2 작업은 확정 코퍼스
3,872행 기준이어야 하므로 v2 안에 별도 인덱스를 둔다. 골든셋이 완성되고 전
유형 재측정을 할 때 팀과 합의해 공유 인덱스를 갱신한다.

embedding_text 재구성
---------------------
BGE가 벡터화하는 원본은 ``embedding_text``인데 Supabase에는 그 컬럼이 없다
(04_build_embeddings.py가 Stage 3 행에서 만들어 벡터만 올린다). 그래서 Actions가
커밋해 둔 Stage 3 스냅샷(3,872행)에서 ``build_embedding_text()``로 다시 만들고,
Supabase의 ``document_hash``와 대조해 한 행도 틀리지 않았음을 확인한다.

재사용
------
``dense.reusable_vectors()``는 텍스트 해시로 기존 벡터를 찾는다. 기존 인덱스를
v2로 복사해 두면 3,606행은 재사용되고 새 행만 인코딩된다(1행당 약 1초).

    python test/golden/v2/tools/build_index.py --seed   # 기존 인덱스 복사
    python test/golden/v2/tools/build_index.py --build  # 재구성 + 빌드
    python test/golden/v2/tools/build_index.py --check  # 검증만
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

V2 = Path(__file__).resolve().parents[1]
AI_ROOT = Path(__file__).resolve().parents[4]
INDEX_DIR = V2 / "index"
SHARED_INDEX = AI_ROOT / "data" / "retrieval_lab"
TEXTS_PATH = INDEX_DIR / "embedding_texts.jsonl"


def load_module(filename: str, name: str) -> Any:
    sys.path.insert(0, str(AI_ROOT))
    spec = importlib.util.spec_from_file_location(name, AI_ROOT / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"{filename}을 불러올 수 없습니다")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def stage3_rows() -> Dict[str, Dict[str, Any]]:
    rows: Dict[str, Dict[str, Any]] = {}
    for pool in ("core", "low_popularity"):
        path = AI_ROOT / "data" / f"hf_models_stage3_{pool}.jsonl"
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    row = json.loads(line)
                    rows[row["model_id"]] = row
    return rows


def reconstruct() -> List[Dict[str, Any]]:
    """확정 코퍼스 3,872행에 embedding_text를 붙인다. document_hash로 검증한다."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import corpus_v2

    builder = load_module("04_build_embeddings.py", "v2_embedding_builder")
    stage3 = stage3_rows()
    print(f"Stage 3 스냅샷 {len(stage3)}행")

    rows: List[Dict[str, Any]] = []
    mismatched: List[str] = []
    for row in corpus_v2.load_rows():
        model_id = row["model_id"]
        source = stage3.get(model_id)
        if source is None:
            mismatched.append(f"{model_id}: Stage 3에 없음")
            continue
        text = builder.build_embedding_text(source)
        if builder.digest(text) != row.get("document_hash"):
            mismatched.append(f"{model_id}: document_hash 불일치")
            continue
        rows.append({"model_id": model_id, "embedding_text": text})

    print(f"재구성 성공 {len(rows)}행 / 검증 실패 {len(mismatched)}행")
    if mismatched:
        for entry in mismatched[:10]:
            print(f"  ⚠️ {entry}")
        raise SystemExit("document_hash 검증 실패. 인덱스를 만들지 않습니다.")

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with TEXTS_PATH.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"→ {TEXTS_PATH}")
    return rows


def seed() -> None:
    """기존 공유 인덱스를 v2로 복사해 3,606행을 재사용할 수 있게 한다."""
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    copied = []
    for name in ("bge_m3_doc_embeddings.npy", "bge_m3_doc_manifest.json"):
        source = SHARED_INDEX / name
        if not source.exists():
            print(f"⚠️ {source} 없음 — 전체를 새로 인코딩해야 합니다")
            continue
        shutil.copy2(source, INDEX_DIR / name)
        copied.append(name)
    manifest_path = INDEX_DIR / "bge_m3_doc_manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        print(f"복사 완료: {copied}")
        print(f"  재사용 가능 행 {manifest['rows']} (model: {manifest['model']}, dim {manifest['dimension']})")


def build() -> None:
    rows = reconstruct()
    from retrieval_lab import dense

    # 공유 인덱스를 덮어쓰지 않도록 쓰기 경로를 v2로 돌린다.
    dense.VECTORS_PATH = INDEX_DIR / "bge_m3_doc_embeddings.npy"
    dense.MANIFEST_PATH = INDEX_DIR / "bge_m3_doc_manifest.json"
    dense.CHECKPOINT_DIR = INDEX_DIR / ".bge_m3_build"
    dense.load_rows = lambda: rows

    print()
    dense.build()


def check() -> None:
    manifest_path = INDEX_DIR / "bge_m3_doc_manifest.json"
    vectors_path = INDEX_DIR / "bge_m3_doc_embeddings.npy"
    if not manifest_path.exists():
        raise SystemExit(f"{manifest_path} 없음")

    import numpy as np

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import corpus_v2

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    matrix = np.load(vectors_path)
    corpus_ids = {row["model_id"] for row in corpus_v2.load_rows()}
    index_ids = set(manifest["model_ids"])

    print(f"인덱스 행 수      {manifest['rows']}  (벡터 shape {matrix.shape})")
    print(f"확정 코퍼스 행 수  {len(corpus_ids)}")
    print(f"모델              {manifest['model']}  dim {manifest['dimension']}  {manifest['dtype']}")
    print(f"벡터 없는 모델     {len(corpus_ids - index_ids)}")
    print(f"코퍼스에 없는 인덱스 {len(index_ids - corpus_ids)}")
    print(f"공유 인덱스 보존   {(SHARED_INDEX / 'bge_m3_doc_manifest.json').exists()}")

    ok = corpus_ids == index_ids and manifest["rows"] == len(corpus_ids)
    print("\n" + ("✅ 확정 코퍼스와 일치" if ok else "❌ 불일치"))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--seed", action="store_true", help="기존 공유 인덱스를 v2로 복사 (재사용용)")
    parser.add_argument("--build", action="store_true", help="embedding_text 재구성 후 인덱스 빌드")
    parser.add_argument("--check", action="store_true", help="만들어진 인덱스를 검증")
    args = parser.parse_args()
    if args.seed:
        seed()
    elif args.build:
        build()
    elif args.check:
        check()
    else:
        parser.print_help()
