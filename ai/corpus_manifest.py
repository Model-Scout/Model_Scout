"""Build records for a corpus version, so embedding and evaluation can prove what they used.

Stages write build_manifest.json next to their outputs. Its stage_id hashes inputs, code, options
and outputs, so the same build gives the same id; creation time and git state only identify it.

    python corpus_manifest.py --check v2    # exit 1 when a recorded file changed
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

AI_DIR = Path(__file__).resolve().parent
REPO_DIR = AI_DIR.parent
MANIFEST_NAME = "build_manifest.json"
CORPUS_STAGE_DIRS = {"v2": (AI_DIR / "data" / "hypergraph_v2", AI_DIR / "data" / "dataset_index_v2")}
# Generated files must not make the code look changed.
GIT_EXCLUDES = (":(exclude)ai/data", ":(exclude)ai/test/public_data/corpus_v2", ":(exclude)**/__pycache__")


def _relative(path, root=AI_DIR):
    path = Path(path).resolve()
    return path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_text(items):
    digest = hashlib.sha256()
    for item in items:
        digest.update(str(item).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def file_record(path, root=AI_DIR):
    path = Path(path)
    record = {"path": _relative(path, root), "sha256": sha256_file(path), "bytes": path.stat().st_size}
    if path.suffix == ".jsonl":
        with open(path, encoding="utf-8") as f:
            record["rows"] = sum(1 for line in f if line.strip())
    return record


def directory_record(path, root=AI_DIR):
    """One hash over every file's relative path and content."""
    path = Path(path)
    files = sorted(p for p in path.rglob("*") if p.is_file())
    entries = [f"{p.relative_to(path).as_posix()} {sha256_file(p)}" for p in files]
    return {"path": _relative(path, root), "sha256": sha256_text(entries), "files": len(files)}


def _record(path, root=AI_DIR):
    return directory_record(path, root) if Path(path).is_dir() else file_record(path, root)


def _git(*args):
    return subprocess.run(["git", *args], cwd=REPO_DIR, capture_output=True, check=True).stdout


def git_state():
    """Commit plus a fingerprint of uncommitted work. None where git is unavailable."""
    try:
        status = _git("status", "--porcelain", "--", ".", *GIT_EXCLUDES).decode("utf-8", "replace")
        untracked = _git("ls-files", "--others", "--exclude-standard", "--", ".", *GIT_EXCLUDES).decode().split("\n")
        return {
            "commit": _git("rev-parse", "HEAD").decode().strip(),
            "branch": _git("rev-parse", "--abbrev-ref", "HEAD").decode().strip(),
            "dirty": bool(status.strip()),
            "tracked_diff_sha256": hashlib.sha256(_git("diff", "HEAD", "--binary", "--", ".", *GIT_EXCLUDES)).hexdigest(),
            "untracked_files": [
                {"path": name, "sha256": sha256_file(REPO_DIR / name)} for name in sorted(filter(None, untracked))
            ],
        }
    except (OSError, subprocess.CalledProcessError):
        return None


def stage_id(manifest):
    """Stable identity of a build: excludes when and from which checkout it ran."""
    parts = {key: manifest[key] for key in ("stage", "corpus", "options", "inputs", "code", "outputs", "upstream")}
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def write_manifest(out_dir, *, stage, corpus, options, inputs, code, outputs, counts, upstream=None, root=AI_DIR):
    out_dir = Path(out_dir)
    manifest = {
        "stage": stage,
        "corpus": corpus,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "options": options,
        "git": git_state(),
        "upstream": upstream,
        "inputs": [_record(path, root) for path in inputs],
        "code": [file_record(path, root) for path in code],
        "outputs": [_record(path, root) for path in outputs],
        "counts": counts,
    }
    manifest["stage_id"] = stage_id(manifest)
    (out_dir / MANIFEST_NAME).write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return manifest


def load_manifest(out_dir):
    path = Path(out_dir) / MANIFEST_NAME
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def check_manifest(out_dir, root=AI_DIR, sections=("inputs", "code", "outputs")):
    """Problems found by re-hashing what the manifest recorded; empty when nothing changed."""
    manifest = load_manifest(out_dir)
    if manifest is None:
        return [f"{Path(out_dir) / MANIFEST_NAME} 없음"]
    problems = []
    for section in sections:
        for recorded in manifest[section]:
            path = Path(root) / recorded["path"]
            if not path.exists():
                problems.append(f"{section}: {recorded['path']} 없음")
            elif _record(path, root)["sha256"] != recorded["sha256"]:
                problems.append(f"{section}: {recorded['path']} 변경됨")
    if stage_id(manifest) != manifest.get("stage_id"):
        problems.append("stage_id가 기록 내용과 다름")
    return problems


def check_corpus(graph_dir, documents_dir=None, root=AI_DIR):
    """Check both stages and that the documents were built from this graph."""
    problems = check_manifest(graph_dir, root)
    if documents_dir is not None:
        problems += check_manifest(documents_dir, root)
        graph, documents = load_manifest(graph_dir), load_manifest(documents_dir)
        if graph and documents and (documents.get("upstream") or {}).get("corpus_id") != graph["stage_id"]:
            problems.append("검색 문서가 지금의 그래프로 만들어지지 않음")
    return problems


def check_vectors(documents_dir):
    """Problems unless embeddings.npy holds this documents build's chunks, in order, from its model.

    Vectors are a separate record (manifest.json): embedding never changes documents_id.
    """
    documents_dir = Path(documents_dir)
    documents = load_manifest(documents_dir)
    vectors_path, record_path = documents_dir / "embeddings.npy", documents_dir / "manifest.json"
    if documents is None:
        return [f"{documents_dir / MANIFEST_NAME} 없음"]
    if not vectors_path.exists() or not record_path.exists():
        return ["벡터 없음 (14 --embed 전)"]
    record = json.loads(record_path.read_text(encoding="utf-8"))
    problems = []
    if record.get("documents_id") != documents["stage_id"]:
        problems.append("벡터가 지금의 검색 문서로 만들어지지 않음 (documents_id 다름)")
    if record.get("model") != documents["options"].get("embedding_model"):
        problems.append(f"임베딩 모델 다름: {record.get('model')} != {documents['options'].get('embedding_model')}")
    with open(documents_dir / "chunks.jsonl", encoding="utf-8") as f:
        chunks = [json.loads(line) for line in f if line.strip()]
    # Search maps vector rows to datasets through chunk_ids, so both lists must match row by row;
    # equal texts under different ids (the same description on two datasets) pass a hash check alone.
    if record.get("chunk_ids") != [c["chunk_id"] for c in chunks]:
        problems.append("벡터 기록의 chunk_ids가 chunks.jsonl의 청크 ID·순서와 다름")
    if record.get("text_hashes") != [c["text_hash"] for c in chunks]:
        problems.append("벡터 순서·내용이 chunks.jsonl과 다름")
    run = record.get("embedding_run") or {}
    if run.get("vectors_sha256") != sha256_file(vectors_path):
        problems.append("embeddings.npy가 기록과 다름")
    import numpy as np

    shape = np.load(vectors_path, mmap_mode="r").shape
    if len(shape) != 2 or shape[0] != len(chunks) or shape[0] != record.get("rows"):
        problems.append(f"벡터 행 수 다름: 파일 {shape}, 기록 {record.get('rows')}, 청크 {len(chunks)}")
    elif shape[1] != record.get("dimension"):
        problems.append(f"벡터 차원 다름: 파일 {shape[1]}, 기록 {record.get('dimension')}")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", choices=sorted(CORPUS_STAGE_DIRS), required=True)
    args = parser.parse_args()
    graph_dir, documents_dir = CORPUS_STAGE_DIRS[args.check]
    problems = check_corpus(graph_dir, documents_dir)
    for problem in problems:
        print(f"[문제] {problem}")
    if problems:
        sys.exit(1)
    print(f"corpus {args.check} ok: corpus_id {load_manifest(graph_dir)['stage_id'][:16]}, "
          f"documents_id {load_manifest(documents_dir)['stage_id'][:16]}")


if __name__ == "__main__":
    main()
