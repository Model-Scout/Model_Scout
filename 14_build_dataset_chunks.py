"""Stage D3: chunk dataset cards and embed them in the same space as the model documents.

Per dataset:
  - one "card" chunk: id, bilingual concept labels from the hypergraph, and description.
    Concept labels are written in Korean and English so a Korean query reaches a dataset
    whose README is English (89% of them), and vice versa.
  - "section" chunks: the cleaned README split along its heading tree, each prefixed with
    "dataset > heading path" so a chunk still names its context when retrieved alone.
Template-only, thin, and missing READMEs get the card chunk only.

Embeddings use the model pipeline's model (text-embedding-3-small) so dataset and model
vectors are comparable. Vectors are reused when a chunk's text hash is unchanged.

Outputs (data/dataset_index/): chunks.jsonl, embeddings.npy (float16), manifest.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path("data")
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
HYPERGRAPH_DIR = DATA_DIR / "hypergraph"
OUT_DIR = DATA_DIR / "dataset_index"
EMBEDDING_MODEL = "text-embedding-3-small"
BATCH_SIZE = 64

# Chunk budgets in characters; ~400-500 tokens either way (Korean packs fewer chars per token).
CHUNK_CHARS = {"ko": 900, "mixed": 1200, "en": 2000}
MIN_CHUNK_CHARS = 60
# ponytail: hard cap so a 250K-char card cannot dominate retrieval; raise if long cards lose key sections.
MAX_SECTION_CHUNKS = 40
CARD_DESCRIPTION_CHARS = 1500
# Cards whose README is empty boilerplate are embedded from metadata alone.
CARD_ONLY_STATUSES = {"template", "thin", "missing"}

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
CLEAN_PATTERNS = [
    (re.compile(r"<!--.*?-->", re.S), " "),
    (re.compile(r"```.*?```", re.S), " "),
    (re.compile(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)"), " "),
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), " "),
    (re.compile(r"<img[^>]*>", re.I), " "),
    (re.compile(r"<[^>]+>"), " "),
    (re.compile(r"^\s*\[More Information Needed\]\s*$", re.M), ""),
    (re.compile(r"[ \t]+"), " "),
    (re.compile(r" ?\n ?"), "\n"),
    (re.compile(r"\n{3,}"), "\n\n"),
]
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.M)
SENTENCE_RE = re.compile(r"(?<=[.!?。])\s+|(?<=다\.)\s*")


def read_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def text_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_markdown(text):
    text = FRONTMATTER_RE.sub("", text, count=1)
    for pattern, replacement in CLEAN_PATTERNS:
        text = pattern.sub(replacement, text)
    return text.strip()


def sections(markdown):
    """Yield (heading_path, body) along the ATX heading tree; text before any heading has path []."""
    path: list[tuple[int, str]] = []
    last = 0
    current: list[str] = []
    for match in HEADING_RE.finditer(markdown):
        yield [title for _, title in current], markdown[last:match.start()].strip()
        level, title = len(match.group(1)), match.group(2).strip()
        path = [(l, t) for l, t in path if l < level] + [(level, title)]
        current, last = path, match.end()
    yield [title for _, title in current], markdown[last:].strip()


def split_budget(body, budget):
    """Pack paragraphs into chunks <= budget; oversized paragraphs fall back to sentences, then hard cuts."""
    pieces = []
    for paragraph in (p.strip() for p in body.split("\n\n")):
        if len(paragraph) <= budget:
            pieces.append(paragraph)
            continue
        for sentence in SENTENCE_RE.split(paragraph):
            pieces.extend(sentence[i:i + budget] for i in range(0, len(sentence), budget))
    chunks, buffer = [], ""
    for piece in filter(None, pieces):
        if buffer and len(buffer) + len(piece) + 2 > budget:
            chunks.append(buffer)
            buffer = piece
        else:
            buffer = f"{buffer}\n\n{piece}" if buffer else piece
    if buffer:
        chunks.append(buffer)
    return chunks


def concept_lines(links, concepts):
    by_facet = defaultdict(list)
    for link in links:
        concept = concepts.get(link["concept_id"])
        if concept and concept["facet"] not in ("dataset_size",):
            english = concept["key"].replace("_", " ")
            by_facet[concept["facet_label"]].append(f"{concept['label']} ({english})")
    return [f"{facet}: {', '.join(sorted(set(values)))}" for facet, values in sorted(by_facet.items())]


def build_chunks(row, entity, links, concepts):
    dataset_id = row["dataset_id"]
    raw = Path(row["readme_path"]).read_text(encoding="utf-8") if row.get("readme_path") else ""
    cleaned = clean_markdown(raw)
    pretty = (row.get("card_data") or {}).get("pretty_name")
    description = (row.get("description") or "").strip() or cleaned
    card_text = "\n".join(filter(None, [
        f"Dataset 데이터셋: {dataset_id}" + (f" ({pretty})" if pretty else ""),
        *concept_lines(links, concepts),
        f"Downloads: {row.get('downloads', 0)}",
        f"Description: {' '.join(clean_markdown(description).split())[:CARD_DESCRIPTION_CHARS]}" if description else None,
    ]))
    chunks = [{"chunk_id": f"{dataset_id}#card", "dataset_id": dataset_id, "kind": "card", "heading_path": [],
               "text": card_text}]
    if entity["readme_status"] in CARD_ONLY_STATUSES:
        return chunks
    budget = CHUNK_CHARS.get(row.get("readme_language") or "en", CHUNK_CHARS["en"])
    for heading_path, body in sections(cleaned):
        for part in split_budget(body, budget):
            if len(part) < MIN_CHUNK_CHARS:
                continue
            index = len(chunks) - 1
            if index >= MAX_SECTION_CHUNKS:
                return chunks
            header = " > ".join([dataset_id, *heading_path])
            chunks.append({"chunk_id": f"{dataset_id}#s{index}", "dataset_id": dataset_id, "kind": "section",
                           "heading_path": heading_path, "text": f"{header}\n{part}"})
    return chunks


def embed(texts, model):
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    vectors = []
    for start in range(0, len(texts), BATCH_SIZE):
        response = client.embeddings.create(model=model, input=texts[start:start + BATCH_SIZE])
        vectors.extend(item.embedding for item in sorted(response.data, key=lambda item: item.index))
        print(f"[EMBED] {min(start + BATCH_SIZE, len(texts))}/{len(texts)}", flush=True)
    return vectors


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--embed", action="store_true", help="call the embedding API for new/changed chunks")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    entities = {e["entity_id"]: e for e in read_jsonl(HYPERGRAPH_DIR / "entities.jsonl")}
    concepts = {c["concept_id"]: c for c in read_jsonl(HYPERGRAPH_DIR / "concepts.jsonl")}
    links_by_entity = defaultdict(list)
    for link in read_jsonl(HYPERGRAPH_DIR / "links.jsonl"):
        links_by_entity[link["entity_id"]].append(link)
    if not entities:
        raise SystemExit("run 13_build_hypergraph.py first")

    chunks = []
    for row in read_jsonl(DATASET_INPUT):
        entity_id = f"dataset:{row['dataset_id']}"
        chunks.extend(build_chunks(row, entities[entity_id], links_by_entity[entity_id], concepts))
    for chunk in chunks:
        chunk["text_hash"] = text_hash(chunk["text"])
        chunk["chars"] = len(chunk["text"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    temp = OUT_DIR / "chunks.jsonl.tmp"
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks)
    os.replace(temp, OUT_DIR / "chunks.jsonl")
    total_chars = sum(c["chars"] for c in chunks)
    print(json.dumps({"chunks": len(chunks), "cards": sum(c["kind"] == "card" for c in chunks),
                      "sections": sum(c["kind"] == "section" for c in chunks),
                      "chars": total_chars}, ensure_ascii=False))
    if not args.embed:
        return

    import numpy as np
    from dotenv import load_dotenv

    load_dotenv(".env")
    manifest_path, vectors_path = OUT_DIR / "manifest.json", OUT_DIR / "embeddings.npy"
    reuse = {}
    if manifest_path.exists() and vectors_path.exists():
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        if old["model"] == EMBEDDING_MODEL:
            old_vectors = np.load(vectors_path)
            reuse = {h: old_vectors[i] for i, h in enumerate(old["text_hashes"])}
    todo = sorted({c["text_hash"]: c["text"] for c in chunks if c["text_hash"] not in reuse}.items())
    print(f"[EMBED] reuse {len(chunks) - sum(c['text_hash'] not in reuse for c in chunks)} chunks, embedding {len(todo)} unique texts", flush=True)
    if todo:
        fresh = embed([text for _, text in todo], EMBEDDING_MODEL)
        reuse.update({h: np.asarray(v, dtype=np.float16) for (h, _), v in zip(todo, fresh)})
    matrix = np.stack([reuse[c["text_hash"]] for c in chunks]).astype(np.float16)
    np.save(OUT_DIR / "embeddings.tmp.npy", matrix)
    os.replace(OUT_DIR / "embeddings.tmp.npy", vectors_path)
    manifest = {"model": EMBEDDING_MODEL, "dimension": int(matrix.shape[1]), "dtype": "float16", "rows": len(chunks),
                "chunk_ids": [c["chunk_id"] for c in chunks], "text_hashes": [c["text_hash"] for c in chunks]}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    print(f"[EMBED] {matrix.shape} -> {vectors_path}")


def self_check():
    md = "---\nlicense: mit\n---\nIntro text\n# A\nalpha\n## B\nbeta\n```py\ncode\n```\n# C\ngamma\n[More Information Needed]\n"
    cleaned = clean_markdown(md)
    assert "license: mit" not in cleaned and "code" not in cleaned and "More Information" not in cleaned
    assert clean_markdown("a\n \n \n \n \nb") == "a\n\nb"
    assert list(sections(cleaned)) == [([], "Intro text"), (["A"], "alpha"), (["A", "B"], "beta"), (["C"], "gamma")]
    parts = split_budget("aaaa\n\nbbbb\n\ncccc", 10)
    assert parts == ["aaaa\n\nbbbb", "cccc"], parts
    assert all(len(p) <= 50 for p in split_budget("x" * 120, 50))
    print("14_build_dataset_chunks ok")


if __name__ == "__main__":
    main()
