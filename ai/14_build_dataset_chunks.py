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

Portal entries have no README sections. In corpus v2 their card also carries the publisher,
coverage, period, language, category and keywords, and extra chunks hold what does not fit: fields
beyond the card (서울), regional originals and over-long descriptions (포털).

Outputs (data/dataset_index/, or data/dataset_index_v2/ with --corpus v2): chunks.jsonl,
embeddings.npy (float16), manifest.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from corpus_manifest import check_manifest, load_manifest, sha256_file, sha256_text, write_manifest

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
PUBLIC_INPUT = DATA_DIR / "public_datasets_stage1.jsonl"
KAGGLE_INPUT = DATA_DIR / "kaggle_datasets_stage1.jsonl"
CORPUS_DIRS = {
    "v1": (DATA_DIR / "hypergraph", DATA_DIR / "dataset_index"),
    "v2": (DATA_DIR / "hypergraph_v2", DATA_DIR / "dataset_index_v2"),
}
# v2 public rows come from 18_enrich (official license, delivery, cycle); 13 v2 refuses anything else.
PUBLIC_INPUTS = {"v1": PUBLIC_INPUT, "v2": DATA_DIR / "public_enriched" / "public_datasets.jsonl"}
EMBEDDING_MODEL = "text-embedding-3-small"
BATCH_SIZE = 64
DB_REUSE_BATCH = 2000

# Chunk budgets in characters; ~400-500 tokens either way (Korean packs fewer chars per token).
CHUNK_CHARS = {"ko": 900, "mixed": 1200, "en": 2000}
MIN_CHUNK_CHARS = 60
# ponytail: sections past the first 15 rarely change which dataset matches, and every vector costs
# Supabase storage (20); raise if long cards lose key sections.
MAX_SECTION_CHUNKS = 15
# Portal READMEs repeat the card, so they get no heading sections, only portal_extra_chunks.
CARD_ONLY_SOURCES = {"seoul_open_data", "data_go_kr"}
CARD_DESCRIPTION_CHARS = 1500
COVERAGE_BASIS = {
    "stated_in_title": "제목에 명시",
    "inferred_from_publisher": "제공기관 소재지로 추정",
    "inferred_from_seoul_portal": "서울 열린데이터광장 수록으로 추정",
}
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
    current: list[tuple[int, str]] = []
    for match in HEADING_RE.finditer(markdown):
        yield [title for _, title in current], markdown[last : match.start()].strip()
        level, title = len(match.group(1)), match.group(2).strip()
        path = [(depth, t) for depth, t in path if depth < level] + [(level, title)]
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
            pieces.extend(sentence[i : i + budget] for i in range(0, len(sentence), budget))
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


def pack(items, separator, budget):
    """Join whole items into chunks <= budget, so a field or title is never cut in half."""
    parts, buffer = [], ""
    for item in items:
        if buffer and len(buffer) + len(separator) + len(item) > budget:
            parts.append(buffer)
            buffer = item
        else:
            buffer = f"{buffer}{separator}{item}" if buffer else item
    return parts + [buffer] if buffer else parts


def portal_card_lines(row, entity):
    """Facts a portal search has to match that the description may never mention."""
    coverage = ", ".join(entity.get("coverage_regions") or [])
    if entity.get("coverage_district"):
        coverage = f"{coverage} {entity['coverage_district']}".strip()
    basis = COVERAGE_BASIS.get(entity.get("coverage_status"))
    period = ", ".join(entity.get("period") or [])
    units = ", ".join(entity.get("spatial_unit") or [])
    # Seoul tags are only the title's words; portal tags are the publisher's keywords and category.
    keywords = ", ".join(row.get("tags") or []) if row.get("source") == "data_go_kr" else ""
    lines = [
        f"제공기관: {entity['publisher']}" if entity.get("publisher") else None,
        f"제공기관 소재지: {entity['publisher_region']}" if entity.get("publisher_region") else None,
        f"데이터 지역 범위: {coverage} ({basis})" if coverage and basis else "데이터 지역 범위: 미확인",
        f"데이터 기간: {period}" if period else None,
        f"언어판: {entity['language_edition']}" if entity.get("language_edition") else None,
        f"공간 단위: {units}" if units else None,
        f"분류: {row['category']}" if row.get("category") else None,
        f"키워드: {keywords}" if keywords else None,
        None if row.get("licenses") else "이용허락: 확인 필요",
        # The portal's wording only: it labels daily and yearly data "실시간" too.
        f"갱신 주기(포털 표기): {row['update_cycle']}" if row.get("update_cycle") else None,
        f"같은 데이터의 다른 제목: {', '.join(entity['same_data_titles'])}" if entity.get("same_data_titles") else None,
    ]
    return list(filter(None, lines))


def portal_extra_chunks(row, cleaned_readme, description, card_text):
    """(heading, text) pairs for portal facts the card cannot hold; texts fit one chunk."""
    budget = CHUNK_CHARS["ko"]
    extras = []
    if row.get("source") == "seoul_open_data" and "## 제공 필드" in cleaned_readme:
        fields = cleaned_readme.split("## 제공 필드", 1)[1].strip()
        lines = [line for line in fields.splitlines() if line.startswith("- ")]
        # Worth a chunk only for what the card lacks: a field past the card's 40 names or an explanation.
        names = [line[2:].split(" (", 1)[0].strip() for line in lines]
        explained = any(") :" in line or "): " in line for line in lines)
        if explained or any(name and name not in card_text for name in names):
            extras += [("제공 필드", part) for part in pack(lines, "\n", budget)]
    variants = row.get("regional_variants") or []
    if variants:
        total = row.get("regional_variant_count") or len(variants)
        tail = f" (수집된 이름 {len(variants)}건, 전체 {total}건)" if total > len(variants) else ""
        names = pack(variants, ", ", budget)
        extras += [("지역별 원본", f"지역별 원본 {total}건{tail}: {part}") for part in names]
    overflow = " ".join(clean_markdown(description).split())[CARD_DESCRIPTION_CHARS:]
    if overflow:
        extras += [("설명 계속", part) for part in split_budget(overflow, budget)]
    return extras


def build_chunks(row, entity, links, concepts):
    dataset_id = row["dataset_id"]
    raw = (AI_DIR / row["readme_path"]).read_text(encoding="utf-8") if row.get("readme_path") else ""
    cleaned = clean_markdown(raw)
    pretty = (row.get("card_data") or {}).get("pretty_name")
    description = (row.get("description") or "").strip() or cleaned
    card_text = "\n".join(
        filter(
            None,
            [
                f"Dataset 데이터셋: {dataset_id}" + (f" ({pretty})" if pretty else ""),
                f"요약: {entity['summary_ko']}" if entity.get("summary_ko") else None,
                *concept_lines(links, concepts),
                *(portal_card_lines(row, entity) if "coverage_status" in entity else []),
                f"Downloads: {row.get('downloads', 0)}",
                f"Description: {' '.join(clean_markdown(description).split())[:CARD_DESCRIPTION_CHARS]}"
                if description
                else None,
            ],
        )
    )
    chunks = [
        {
            "chunk_id": f"{dataset_id}#card",
            "dataset_id": dataset_id,
            "kind": "card",
            "heading_path": [],
            "text": card_text,
        }
    ]
    if "coverage_status" in entity:  # corpus v2 portal entry
        for index, (heading, text) in enumerate(portal_extra_chunks(row, cleaned, description, card_text)):
            chunks.append(
                {
                    "chunk_id": f"{dataset_id}#s{index}",
                    "dataset_id": dataset_id,
                    "kind": "section",
                    "heading_path": [heading],
                    "text": f"{dataset_id} ({pretty}) > {heading}\n{text}",
                }
            )
        return chunks
    if entity["readme_status"] in CARD_ONLY_STATUSES or row.get("source") in CARD_ONLY_SOURCES:
        return chunks
    budget =CHUNK_CHARS.get(row.get("readme_language") or "en", CHUNK_CHARS["en"])
    for heading_path, body in sections(cleaned):
        for part in split_budget(body, budget):
            if len(part) < MIN_CHUNK_CHARS:
                continue
            index = len(chunks) - 1
            if index >= MAX_SECTION_CHUNKS:
                return chunks
            header = " > ".join([dataset_id, *heading_path])
            chunks.append(
                {
                    "chunk_id": f"{dataset_id}#s{index}",
                    "dataset_id": dataset_id,
                    "kind": "section",
                    "heading_path": heading_path,
                    "text": f"{header}\n{part}",
                }
            )
    return chunks


def embed(texts, model):
    import time

    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    vectors: list[list[float]] = []
    for start in range(0, len(texts), BATCH_SIZE):
        # A dropped connection mid-run would otherwise discard every batch embedded so far.
        for attempt in range(6):
            try:
                response = client.embeddings.create(model=model, input=texts[start : start + BATCH_SIZE])
                break
            except Exception as error:
                if attempt == 5:
                    raise
                print(f"[EMBED] retry {attempt + 1} after {type(error).__name__}", flush=True)
                time.sleep(10 * 2**attempt)
        vectors.extend(item.embedding for item in sorted(response.data, key=lambda item: item.index))
        print(f"[EMBED] {min(start + BATCH_SIZE, len(texts))}/{len(texts)}", flush=True)
    return vectors


def db_vectors(hashes, required=False):
    """(vectors already published to Supabase (20), how the read went).

    A fresh clone without embeddings.npy then re-embeds only new text. Best effort by default:
    no database, no connection or no table reuses nothing. With required=True (--require-db-reuse)
    each of those stops the run instead, so a failed read never turns into a full re-embedding.
    Status: read | no_hashes | not_configured | connect_failed | no_table.
    """
    import numpy as np

    from supabase_db import configured, db_connection, parse_vector

    def unavailable(status, detail=""):
        if required:
            raise SystemExit(f"[EMBED] DB reuse required but unavailable: {status} {detail}".strip())
        print(f"[EMBED] Supabase reuse skipped: {status} {detail}".strip(), flush=True)
        return {}, status

    if not hashes:
        return {}, "no_hashes"
    if not configured():
        return unavailable("not_configured")
    try:
        conn = db_connection()
    except Exception as error:
        return unavailable("connect_failed", type(error).__name__)
    found = {}
    wanted = sorted(hashes)
    try:
        with conn.cursor() as cur:
            cur.execute("select to_regclass('public.model_scout_dataset_chunks')")
            if cur.fetchone()[0] is None:
                return unavailable("no_table")
            # Batched: one query for all ~35K vectors as text overruns Supabase's statement timeout.
            for start in range(0, len(wanted), DB_REUSE_BATCH):
                cur.execute(
                    "select distinct on (text_hash) text_hash, embedding::text from public.model_scout_dataset_chunks "
                    "where text_hash = any(%s)",
                    (wanted[start : start + DB_REUSE_BATCH],),
                )
                found.update({h: parse_vector(v).astype(np.float16) for h, v in cur.fetchall()})
    finally:
        conn.close()
    print(f"[EMBED] reused {len(found)} vectors from Supabase", flush=True)
    return found, "read"


def require_current_graph(hypergraph_dir):
    """Stop before documents or embedding when any source, code or graph file changed since 13 ran."""
    problems = check_manifest(hypergraph_dir)
    if problems:
        raise SystemExit(f"{hypergraph_dir.name} is stale, run 13 --corpus v2 again:\n- " + "\n- ".join(problems))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--embed", action="store_true", help="call the embedding API for new/changed chunks")
    # Guards for a paid run; off by default so dataset-refresh.yml's `14 --embed` behaves as before.
    parser.add_argument("--dry-run", action="store_true", help="plan the embedding (reuse, new count) without the API or saving vectors")
    parser.add_argument("--max-new", type=int, help="stop before the API when more texts than this need new vectors")
    parser.add_argument("--require-db-reuse", action="store_true", help="stop when the Supabase vectors cannot be read")
    parser.add_argument("--self-check", action="store_true")
    # dataset-refresh.yml embeds and publishes the default corpus, so v1 stays the default until cutover.
    parser.add_argument("--corpus", choices=sorted(CORPUS_DIRS), default="v1")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    hypergraph_dir, out_dir = CORPUS_DIRS[args.corpus]
    versioned = args.corpus != "v1"
    if versioned:
        require_current_graph(hypergraph_dir)

    entities = {e["entity_id"]: e for e in read_jsonl(hypergraph_dir / "entities.jsonl")}
    concepts = {c["concept_id"]: c for c in read_jsonl(hypergraph_dir / "concepts.jsonl")}
    links_by_entity = defaultdict(list)
    for link in read_jsonl(hypergraph_dir / "links.jsonl"):
        links_by_entity[link["entity_id"]].append(link)
    if not entities:
        raise SystemExit("run 13_build_hypergraph.py first")

    chunks = []
    for row in read_jsonl(DATASET_INPUT) + read_jsonl(KAGGLE_INPUT) + read_jsonl(PUBLIC_INPUTS[args.corpus]):
        entity_id = f"dataset:{row['dataset_id']}"
        if entity_id not in entities:  # a mirror collapsed into its canonical dataset by 13
            continue
        chunks.extend(build_chunks(row, entities[entity_id], links_by_entity[entity_id], concepts))
    for chunk in chunks:
        chunk["text_hash"] = text_hash(chunk["text"])
        chunk["chars"] = len(chunk["text"])

    out_dir.mkdir(parents=True, exist_ok=True)
    temp = out_dir / "chunks.jsonl.tmp"
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks)
    os.replace(temp, out_dir / "chunks.jsonl")
    total_chars = sum(c["chars"] for c in chunks)
    print(
        json.dumps(
            {
                "chunks": len(chunks),
                "cards": sum(c["kind"] == "card" for c in chunks),
                "sections": sum(c["kind"] == "section" for c in chunks),
                "chars": total_chars,
            },
            ensure_ascii=False,
        )
    )
    documents = None
    if versioned:
        documents = write_manifest(
            out_dir,
            stage="documents",
            corpus=args.corpus,
            # Identity of the documents: whether this run also embeds them is recorded with the vectors.
            options={"corpus": args.corpus, "embedding_model": EMBEDDING_MODEL},
            upstream={"corpus_id": load_manifest(hypergraph_dir)["stage_id"]},
            inputs=[
                *(path for path in (DATASET_INPUT, KAGGLE_INPUT, PUBLIC_INPUTS[args.corpus]) if path.exists()),
                *(DATA_DIR / "readmes" / name for name in ("public", "datasets", "kaggle") if (DATA_DIR / "readmes" / name).exists()),
            ],
            code=[Path(__file__), AI_DIR / "corpus_manifest.py"],
            outputs=[out_dir / "chunks.jsonl"],
            counts={
                "chunks": len(chunks),
                "cards": sum(c["kind"] == "card" for c in chunks),
                "sections": sum(c["kind"] == "section" for c in chunks),
                "chars": total_chars,
                "unique_text_hashes": len({c["text_hash"] for c in chunks}),
                "text_hashes_sha256": sha256_text(c["text_hash"] for c in chunks),
            },
        )
        print(f"documents_id {documents['stage_id']}")
    if not (args.embed or args.dry_run):
        return

    import numpy as np
    from dotenv import load_dotenv

    load_dotenv(".env")
    manifest_path, vectors_path = out_dir / "manifest.json", out_dir / "embeddings.npy"
    reuse = {}
    if manifest_path.exists() and vectors_path.exists():
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        if old["model"] == EMBEDDING_MODEL:
            old_vectors = np.load(vectors_path)
            reuse = {h: old_vectors[i] for i, h in enumerate(old["text_hashes"])}
    needed = {c["text_hash"] for c in chunks}
    reused_local = len(needed & set(reuse))
    from_db, db_status = db_vectors(needed - set(reuse), required=args.require_db_reuse)
    reuse.update(from_db)
    todo = sorted({c["text_hash"]: c["text"] for c in chunks if c["text_hash"] not in reuse}.items())
    plan = {
        "dry_run": args.dry_run,
        "documents_id": documents["stage_id"] if documents else None,
        "model": EMBEDDING_MODEL,
        "unique_texts": len(needed),
        "reused_local": reused_local,
        "db_read": db_status,
        "reused_db": len(from_db),
        "new": len(todo),
        "new_chars": sum(len(text) for _, text in todo),
        "max_new": args.max_new,
    }
    print("[EMBED PLAN] " + json.dumps(plan, ensure_ascii=False), flush=True)
    if args.max_new is not None and len(todo) > args.max_new:
        raise SystemExit(f"[EMBED] {len(todo)} new texts exceed --max-new {args.max_new}; nothing was embedded")
    if args.dry_run:
        print("[EMBED] dry run: no embedding API call, no vectors saved", flush=True)
        return
    if todo:
        fresh = embed([text for _, text in todo], EMBEDDING_MODEL)
        reuse.update({h: np.asarray(v, dtype=np.float16) for (h, _), v in zip(todo, fresh, strict=False)})
    matrix = np.stack([reuse[c["text_hash"]] for c in chunks]).astype(np.float16)
    np.save(out_dir / "embeddings.tmp.npy", matrix)
    os.replace(out_dir / "embeddings.tmp.npy", vectors_path)
    manifest = {
        "model": EMBEDDING_MODEL,
        "dimension": int(matrix.shape[1]),
        "dtype": "float16",
        "rows": len(chunks),
        "chunk_ids": [c["chunk_id"] for c in chunks],
        "text_hashes": [c["text_hash"] for c in chunks],
    }
    if documents:
        manifest.update(corpus_id=documents["upstream"]["corpus_id"], documents_id=documents["stage_id"])
    # This run, kept apart from the documents' identity (documents_id does not change by embedding).
    manifest["embedding_run"] = {
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "unique_texts": len(needed),
        "reused_local": reused_local,
        "reused_db": len(from_db),
        "embedded": len(todo),
        "vectors_sha256": sha256_file(vectors_path),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    print(f"[EMBED] {matrix.shape} -> {vectors_path}")


def self_check():
    md = (
        "---\nlicense: mit\n---\nIntro text\n# A\nalpha\n## B\nbeta\n```py\ncode\n```\n"
        "# C\ngamma\n[More Information Needed]\n"
    )
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
