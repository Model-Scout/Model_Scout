"""Stage H1: map model and dataset metadata onto taxonomy concepts (the hypergraph).

Each taxonomy concept is a hyperedge; an entity joins it through a link that records
where the value came from. This stage uses structured metadata only (no LLM), so every
link is reproducible from metadata, except method="ner" links read from Stage D4
(16_extract_dataset_ner.py). An NER link is "medium" when its README quote names the
concept and "low" when the quote merely exists. Once NER has read a card, a metadata task
keeps "high" only if a quote states it, drops to "medium" if NER names it loosely, and to
"low" if NER does not name it at all (tags like sentence-similarity are often wrong).

Outputs (data/hypergraph/, or data/hypergraph_v2/ with --corpus v2):
  entities.jsonl   one row per model/dataset with quality flags
  links.jsonl      entity -> concept, with method, source field, raw value, confidence
  relations.jsonl  entity -> entity edges (model trained_with dataset)
  concepts.jsonl   every concept with its member count
  duplicates.json  same data -> canonical id and reason (dataset_dedup.py); may share a label
  series.json      v2 only: separate portal entries related by region, edition or language; never share a label
  report.json    coverage per facet and the raw values that did not map; "models" records which
                 model corpus was used (source, count, sha256 of the sorted model IDs)

Model source (--model-source):
  auto      a real local Stage 4 snapshot if both files hold JSONL, else Supabase (default, local dev)
  local     the local snapshot or fail; an LFS pointer, empty or corrupt file is an error
  supabase  the active rows in Supabase; local files are ignored. dataset-refresh.yml uses this, so the
            published graph has exactly the models the recommendation search can return.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

from corpus_manifest import check_manifest, load_manifest, read_jsonl_snapshot, sha256_text, write_manifest
from dataset_dedup import check_public_duplicates, duplicate_map, public_identity, public_series
from taxonomy import label, load_taxonomy, mentions, normalize

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
CORPUS_DIRS = {"v1": DATA_DIR / "hypergraph", "v2": DATA_DIR / "hypergraph_v2"}
README_DIRS = (DATA_DIR / "readmes" / "public", DATA_DIR / "readmes" / "datasets", DATA_DIR / "readmes" / "kaggle")
MODEL_INPUTS = (DATA_DIR / "hf_models_stage4_core.jsonl", DATA_DIR / "hf_models_stage4_low_popularity.jsonl")
MODEL_SOURCES = ("auto", "local", "supabase")
SUPABASE_MODEL_QUERY = (
    "select model_id, source_pool, task, filter_metadata from public.model_scout_models "
    "where active order by model_id"
)
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
PUBLIC_INPUT = DATA_DIR / "public_datasets_stage1.jsonl"  # 서울 열린데이터광장 + 공공데이터포털 (18)
ENRICH_DIR = DATA_DIR / "public_enriched"  # v2 reads 18_enrich's output: official license, delivery, cycle
PUBLIC_INPUTS = {"v1": PUBLIC_INPUT, "v2": ENRICH_DIR / "public_datasets.jsonl"}
KAGGLE_INPUT = DATA_DIR / "kaggle_datasets_stage1.jsonl"  # 19
PORTAL_SOURCES = {"seoul_open_data", "data_go_kr"}
LENGTH_INPUT = DATA_DIR / "hf_datasets_length_stats.jsonl"
NER_INPUT = DATA_DIR / "hf_datasets_ner.jsonl"
QUOTE_CHARS = 160
CONFIDENCE_RANK = ["low", "medium", "high"]

# ponytail: languages are linked one hub each only up to this count; wider corpora join
# ko/en/multilingual hubs so 100-language crawls do not flood every language page.
MAX_LINKED_LANGUAGES = 10
MULTILINGUAL_MIN = 3

# Task concept -> (input modalities, output modalities). Models carry no modality metadata.
TASK_MODALITIES = {
    "generation": (["text"], ["text"]),
    "summarization": (["text"], ["text"]),
    "translation": (["text"], ["text"]),
    "question_answering": (["text"], ["text"]),
    "classification": (["text"], []),
    "embedding": (["text"], []),
    "retrieval": (["text"], []),
    "reranking": (["text"], []),
    "information_extraction": (["text"], []),
    "speech_recognition": (["audio"], ["text"]),
    "text_to_speech": (["text"], ["audio"]),
    "visual_qa": (["image", "text"], ["text"]),
    "ocr": (["image", "document"], ["text"]),
    "chart_understanding": (["image", "text"], ["text"]),
    "table_qa": (["table", "text"], ["text"]),
    "forecasting": (["time_series"], ["time_series"]),
    "language_modeling": (["text"], ["text"]),
    "audio_classification": (["audio"], []),
    "vision": (["image"], []),
    "image_generation": (["text", "image"], ["image"]),
    "tabular_prediction": (["table"], []),
}

TEMPLATE_MARK = "[More Information Needed]"
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
RERANKER_RE = re.compile(r"rerank", re.I)
EVAL_NAME_RE = re.compile(r"bench|eval|leaderboard", re.I)
SIZE_BOUND_RE = re.compile(r"(\d+(?:\.\d+)?)([KMBT]?)$")
SIZE_UNITS = {"": 1, "K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}


def read_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    temp = path.with_suffix(path.suffix + ".tmp")
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    os.replace(temp, path)


def size_category_upper(value):
    """'10K<n<100K' -> 1e5, 'n<1K' -> 1e3, 'n>1T' -> inf. None when unparseable."""
    if value.startswith("n>"):
        return float("inf")
    match = SIZE_BOUND_RE.search(value)
    return float(match.group(1)) * SIZE_UNITS[match.group(2)] if match else None


def readme_status(row):
    path = row.get("readme_path")
    if not path or not (AI_DIR / path).exists():
        return "missing"
    body = FRONTMATTER_RE.sub("", (AI_DIR / path).read_text(encoding="utf-8"), count=1).strip()
    if body.count(TEMPLATE_MARK) >= 5:
        return "template"
    return "thin" if len(body) < 200 else "ok"


def korean_focus(languages):
    if "ko" not in languages:
        return "not_ko"
    if len(languages) > MAX_LINKED_LANGUAGES:
        return "wide_multilingual"
    return "ko_only" if languages == ["ko"] else "ko_with_others"


class Linker:
    def __init__(self):
        self.links: dict[tuple, dict] = {}
        self.unmapped: dict[str, Counter] = defaultdict(Counter)

    def add(self, entity_id, facet, raw, field, method="metadata", confidence="high", concept=None):
        concept = concept or normalize(facet, raw)
        if concept is None:
            self.unmapped[f"{entity_id.split(':', 1)[0]}.{facet}.{field}"][str(raw)] += 1
            return
        key = (entity_id, facet, concept)
        # First evidence keeps method/raw; later sources add their field and can only raise confidence.
        if key in self.links:
            link = self.links[key]
            link["fields"] = sorted(set(link["fields"]) | {field})
            link["confidence"] = max(link["confidence"], confidence, key=CONFIDENCE_RANK.index)
            return
        self.links[key] = {
            "entity_id": entity_id,
            "concept_id": f"{facet}/{concept}",
            "facet": facet,
            "method": method,
            "fields": [field],
            "raw": raw,
            "confidence": confidence,
        }

    def languages(self, entity_id, languages, field, multilingual_flag=False):
        linked = languages if len(languages) <= MAX_LINKED_LANGUAGES else [c for c in languages if c in ("ko", "en")]
        for code in linked:
            self.add(entity_id, "language", code, field)
        if multilingual_flag or len(languages) >= MULTILINGUAL_MIN:
            self.add(entity_id, "language", f"{len(languages)} languages", field, concept="multilingual")

    def modalities_from_tasks(self, entity_id):
        tasks = [k[2] for k in self.links if k[0] == entity_id and k[1] == "task"]
        for task in tasks:
            inputs, outputs = TASK_MODALITIES.get(task, ([], []))
            for value in inputs:
                self.add(entity_id, "input_modality", value, f"task:{task}", method="task_rule", confidence="medium")
            for value in outputs:
                self.add(entity_id, "output_modality", value, f"task:{task}", method="task_rule", confidence="medium")


def load_supabase_models():
    from supabase_db import db_connection

    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(SUPABASE_MODEL_QUERY)
            return [
                {"model_id": m, "source_pool": pool, "task": task or {}, "filter_metadata": meta or {}}
                for m, pool, task, meta in cur.fetchall()
            ]
    finally:
        conn.close()


def load_model_rows(source="auto"):
    """(rows, info): the model corpus and a record of where it came from.

    Stage 4 snapshots are Git LFS files (vectors live in Supabase), so a checkout without LFS has
    pointer stubs at those paths. Only real JSONL counts as a local snapshot.
    """
    if source not in MODEL_SOURCES:
        raise ValueError(f"unknown model source: {source}")
    local_status = {}
    if source != "supabase":
        snapshots = {path: read_jsonl_snapshot(path) for path in MODEL_INPUTS}
        local_status = {path.name: status for path, (status, _) in snapshots.items()}
        if all(status == "jsonl" for status, _ in snapshots.values()):
            rows = [row for _, rows in snapshots.values() for row in rows]
            return rows, model_source_info("local_stage4", source, rows, local_status,
                                           selection=[path.name for path in MODEL_INPUTS])
        if source == "local":
            raise SystemExit(f"--model-source local needs real Stage 4 JSONL files: {local_status}")
        print(f"local Stage 4 snapshot unusable {local_status}; reading active models from Supabase")
    rows = load_supabase_models()
    return rows, model_source_info("supabase", source, rows, local_status, selection=SUPABASE_MODEL_QUERY)


def model_source_info(used, requested, rows, local_status, selection):
    """Same meaning in v1 report.json and the v2 manifest."""
    return {
        "source": used,
        "requested_source": requested,
        "count": len(rows),
        "model_ids_sha256": sha256_text(sorted(row["model_id"] for row in rows)),
        "selection": selection,
        "local_status": local_status,
    }


def map_model(linker, row):
    entity_id = f"model:{row['model_id']}"
    fm = row.get("filter_metadata") or {}
    task = row.get("task") or {}
    for value in task.get("matched") or [task.get("primary")]:
        if value:
            linker.add(entity_id, "task", value, "task.matched")
    if RERANKER_RE.search(row["model_id"]):
        linker.add(entity_id, "task", "reranking", "model_id", method="name_rule", confidence="medium")
    linker.modalities_from_tasks(entity_id)
    languages = sorted(set(row.get("language_codes") or fm.get("languages") or []))
    linker.languages(entity_id, languages, "language_codes", bool(fm.get("multilingual_verified")))
    linker.add(entity_id, "commercial_use", fm.get("license"), "license")
    if fm.get("context_length"):
        linker.add(entity_id, "input_length", fm["context_length"], "context_length")
    if fm.get("parameter_count_billion"):
        linker.add(entity_id, "model_size", fm["parameter_count_billion"], "parameter_count_billion")
    return {
        "entity_id": entity_id,
        "kind": "model",
        "name": row["model_id"],
        "source": "huggingface",
        "url": f"https://huggingface.co/{row['model_id']}",
        "source_pool": row.get("source_pool"),
        "downloads": fm.get("downloads"),
        "languages": languages,
        "license": fm.get("license"),
        "context_length": fm.get("context_length"),
        "parameter_count_billion": fm.get("parameter_count_billion"),
    }


def map_ner(linker, entity_id, ner):
    """Add README-grounded concepts; demote metadata tasks the README does not back up."""
    tasks: dict[str, bool] = {}
    for facet, items in ner["concepts"].items():
        for item in items:
            stated = mentions(facet, item["value"], item["quote"])
            if facet == "task":
                tasks[item["value"]] = tasks.get(item["value"]) or stated
            linker.add(
                entity_id,
                facet,
                item["quote"][:QUOTE_CHARS],
                "readme",
                method="ner",
                confidence="medium" if stated else "low",
                concept=item["value"],
            )
    for (owner, facet, concept), link in linker.links.items():
        if owner == entity_id and facet == "task" and link["method"] != "ner" and not tasks.get(concept):
            link["confidence"] = "medium" if concept in tasks else "low"


def map_dataset(linker, row, length, ner=None):
    entity_id = f"dataset:{row['dataset_id']}"
    for field in ("task_categories", "task_ids"):
        for value in row.get(field) or []:
            linker.add(entity_id, "task", value, field)
    # Free-form Hub tags (no "prefix:") often name a task or domain exactly: "rag", "legal", "medical".
    free_tags = [t for t in row.get("tags") or [] if ":" not in t]
    # Portal keywords are plain words (검색 = "search" in "지하철역 검색"), not ML task tags.
    tag_facets = ("domain",) if row.get("source") in PORTAL_SOURCES else ("task", "domain")
    for tag in free_tags:
        for facet in tag_facets:
            if normalize(facet, tag):
                linker.add(entity_id, facet, tag, "tags", method="tag_match", confidence="medium")
    if ner:
        map_ner(linker, entity_id, ner)
    source = row.get("source", "huggingface")
    if source in PORTAL_SOURCES:
        # Public portal data is looked up by apps at runtime; titles are Korean compounds
        # (공공자전거, 미세먼지농도) that hold a domain alias without equalling it.
        linker.add(entity_id, "dataset_role", "service", "source", method="source_rule", confidence="medium")
        text = " ".join([(row.get("card_data") or {}).get("pretty_name") or "", *(row.get("tags") or [])])
        for value in load_taxonomy()["facets"]["domain"]["values"]:
            if value != "general" and mentions("domain", value, text):
                linker.add(
                    entity_id, "domain", value, "title/keywords", method="tag_match", confidence="medium", concept=value
                )
    for value in row.get("modalities") or []:
        linker.add(entity_id, "input_modality", value, "modality")
    linker.modalities_from_tasks(entity_id)
    languages = row.get("languages") or []
    linker.languages(entity_id, languages, "languages")
    for value in row.get("licenses") or [None]:
        linker.add(entity_id, "commercial_use", value, "license")
    for value in row.get("formats") or []:
        linker.add(entity_id, "data_format", value, "format")
    for value in row.get("size_categories") or []:
        upper = size_category_upper(value)
        if upper is not None:
            # Category upper bounds are exclusive ("1K<n<10K"), so step just below them.
            linker.add(
                entity_id, "dataset_size", upper - 1, "size_categories", concept=normalize("dataset_size", upper - 1)
            )
    if row.get("referenced_by_models"):
        linker.add(entity_id, "dataset_role", "train", "referenced_by_models", confidence="medium")
    if EVAL_NAME_RE.search(row["dataset_id"]) or any(normalize("dataset_role", t) == "evaluation" for t in free_tags):
        linker.add(entity_id, "dataset_role", "evaluation", "dataset_id/tags", method="name_rule", confidence="medium")
    if length and length.get("status") == "ok" and length.get("tokens_p90_estimate"):
        linker.add(
            entity_id,
            "input_length",
            length["tokens_p90_estimate"],
            "viewer_statistics",
            method="viewer_stats",
            confidence="medium",
        )
    status = readme_status(row)
    return {
        "entity_id": entity_id,
        "kind": "dataset",
        "name": row["dataset_id"],
        "source": source,
        "url": row["url"],
        "downloads": row.get("downloads"),
        "likes": row.get("likes"),
        "gated": row.get("gated"),
        "languages": languages,
        "licenses": row.get("licenses"),
        "seed_reasons": row.get("seed_reasons"),
        "readme_path": row.get("readme_path"),
        "readme_language": row.get("readme_language"),
        "readme_status": status,
        "korean_focus": korean_focus(languages),
        "summary_ko": ner.get("summary_ko") if ner else None,
        "title": (row.get("card_data") or {}).get("pretty_name") if source != "huggingface" else None,
        "quality_flags": row.get("quality_flags") or [],
        "sample_length": {k: length.get(k) for k in ("text_column", "chars", "tokens_p90_estimate", "config", "split")}
        if length and length.get("status") == "ok"
        else None,
    }


def coverage(entities, links):
    facets = load_taxonomy()["facets"]
    linked = defaultdict(set)
    for link in links:
        linked[link["facet"]].add(link["entity_id"])
    report = {}
    for kind in ("model", "dataset"):
        ids = {e["entity_id"] for e in entities if e["kind"] == kind}
        report[kind] = {
            facet: f"{len(linked[facet] & ids)}/{len(ids)}"
            for facet, spec in facets.items()
            if kind in spec["applies_to"]
        }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-check", action="store_true")
    # dataset-refresh.yml embeds and publishes the default corpus, so v1 stays the default until cutover.
    parser.add_argument("--corpus", choices=sorted(CORPUS_DIRS), default="v1")
    # Production (dataset-refresh.yml) passes supabase; auto keeps local development working offline.
    parser.add_argument("--model-source", choices=MODEL_SOURCES, default="auto")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    verified = args.corpus == "v2"
    out_dir = CORPUS_DIRS[args.corpus]
    public_input = PUBLIC_INPUTS[args.corpus]
    if verified:
        # New or changed collected rows must pass enrichment before refining, never around it.
        problems = check_manifest(ENRICH_DIR)
        if problems:
            raise SystemExit("run 18_enrich_public_datasets.py first:\n- " + "\n- ".join(problems))

    linker = Linker()
    lengths = {r["dataset_id"]: r for r in read_jsonl(LENGTH_INPUT)}
    model_rows, model_info = load_model_rows(args.model_source)
    entities = [map_model(linker, row) for row in model_rows]
    ners = {r["dataset_id"]: r for r in read_jsonl(NER_INPUT)}
    hf_rows, public_rows = read_jsonl(DATASET_INPUT) + read_jsonl(KAGGLE_INPUT), read_jsonl(public_input)
    duplicates = duplicate_map(hf_rows, public_rows, "verified" if verified else "title")
    public_merges = check_public_duplicates(duplicates, public_rows) if verified else None
    series = public_series(public_rows, duplicates) if verified else []
    series_of = {member: group["series_id"] for group in series for member in group["members"]}
    canonical_rows =[r for r in hf_rows + public_rows if r["dataset_id"] not in duplicates]
    copies = defaultdict(list)
    for dataset_id, info in duplicates.items():
        copies[info["canonical"]].append(dataset_id)
    by_id = {r["dataset_id"]: r for r in hf_rows + public_rows}
    for row in canonical_rows:
        # A portal file and its OpenAPI twin are one dataset offered two ways.
        for copy in copies.get(row["dataset_id"], []):
            row["formats"] = sorted(set(row.get("formats") or []) | set(by_id[copy].get("formats") or []))
    for row in canonical_rows:
        entity = map_dataset(linker, row, lengths.get(row["dataset_id"]), ners.get(row["dataset_id"]))
        entity["duplicates"] = sorted(copies.get(row["dataset_id"], []))
        if verified and row.get("source") in PORTAL_SOURCES:
            entity.update(public_identity(row))
            entity["series_id"] = series_of.get(row["dataset_id"])
            entity["same_data_titles"] = sorted(
                {(by_id[copy].get("card_data") or {}).get("pretty_name") or "" for copy in entity["duplicates"]}
                - {entity["title"], ""}
            )
        entities.append(entity)
    links = sorted(linker.links.values(), key=lambda link: (link["entity_id"], link["concept_id"]))

    known = {e["entity_id"] for e in entities}
    relations = []
    seen_relations = set()
    for row in hf_rows:
        # A model citing a mirror is linked to the canonical dataset.
        target = duplicates.get(row["dataset_id"], {}).get("canonical", row["dataset_id"])
        for model_id in row.get("referenced_by_models") or []:
            if f"model:{model_id}" in known and (model_id, target) not in seen_relations:
                seen_relations.add((model_id, target))
                relations.append(
                    {
                        "source": f"model:{model_id}",
                        "relation": "trained_with",
                        "target": f"dataset:{target}",
                        "method": "metadata",
                        "fields": ["cardData.datasets"],
                        "confidence": "high",
                    }
                )

    members = Counter(link["concept_id"] for link in links)
    concepts = []
    for facet, spec in load_taxonomy()["facets"].items():
        keys = list(spec["values"]) + sorted(
            {c.split("/", 1)[1] for c in members if c.startswith(facet + "/")} - set(spec["values"])
        )
        for key in keys:
            concept_id = f"{facet}/{key}"
            concepts.append(
                {
                    "concept_id": concept_id,
                    "facet": facet,
                    "facet_label": spec["label"],
                    "key": key,
                    "label": label(facet, key),
                    "aliases": [a for a in spec["values"].get(key, {}).get("aliases", []) if a],
                    "members": members.get(concept_id, 0),
                }
            )

    out_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(out_dir / "entities.jsonl", entities)
    (out_dir / "duplicates.json").write_text(json.dumps(duplicates, ensure_ascii=False, indent=1), encoding="utf-8")
    if verified:
        (out_dir / "series.json").write_text(json.dumps(series, ensure_ascii=False, indent=1), encoding="utf-8")
    write_jsonl(out_dir / "links.jsonl", links)
    write_jsonl(out_dir / "relations.jsonl", relations)
    write_jsonl(out_dir / "concepts.jsonl", concepts)
    report = {
        "entities": Counter(e["kind"] for e in entities),
        "links": len(links),
        "relations": len(relations),
        "dataset_duplicates_removed": Counter(by_id[d].get("source", "huggingface") for d in duplicates),
        "links_by_method": Counter(link["method"] for link in links),
        "links_by_confidence": Counter(link["confidence"] for link in links),
        "coverage": coverage(entities, links),
        "dataset_readme_status": Counter(e["readme_status"] for e in entities if e["kind"] == "dataset"),
        "dataset_korean_focus": Counter(e["korean_focus"] for e in entities if e["kind"] == "dataset"),
        "unmapped_top": {k: v.most_common(25) for k, v in sorted(linker.unmapped.items())},
        "models": model_info,
    }
    if verified:
        report.update(public_merges=public_merges, public_series=len(series))
    (out_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "unmapped_top"}, ensure_ascii=False, indent=2))
    if verified:
        local_models = model_info["source"] == "local_stage4"
        names = ("entities.jsonl", "links.jsonl", "relations.jsonl", "concepts.jsonl", "duplicates.json", "series.json", "report.json")
        manifest = write_manifest(
            out_dir,
            stage="hypergraph",
            corpus=args.corpus,
            options={"corpus": args.corpus, "public_policy": "verified"},
            upstream={"enrich_id": load_manifest(ENRICH_DIR)["stage_id"]},
            inputs=[
                *(path for path in (DATASET_INPUT, KAGGLE_INPUT, public_input, LENGTH_INPUT, NER_INPUT) if path.exists()),
                *(MODEL_INPUTS if local_models else ()),
                *(path for path in README_DIRS if path.exists()),
                AI_DIR / "taxonomy.yaml",
            ],
            code=[Path(__file__), AI_DIR / "dataset_dedup.py", AI_DIR / "taxonomy.py", AI_DIR / "retrieval_metadata.py", AI_DIR / "corpus_manifest.py"],
            outputs=[out_dir / name for name in names],
            counts={
                "entities": Counter(e["kind"] for e in entities),
                "datasets_by_source": Counter(e["source"] for e in entities if e["kind"] == "dataset"),
                "public_merges": public_merges,
                "public_series": len(series),
                "model_source": model_info["source"],
                "models": model_info["count"],
                "model_ids_sha256": model_info["model_ids_sha256"],
            },
        )
        print(f"corpus_id {manifest['stage_id']}")
    print(f"unmapped value groups: {len(linker.unmapped)} (see {out_dir / 'report.json'})")


def self_check():
    assert size_category_upper("10K<n<100K") == 1e5
    assert size_category_upper("n<1K") == 1e3
    assert size_category_upper("1B<n<10B") == 1e10
    assert size_category_upper("n>1T") == float("inf")
    assert korean_focus(["ko"]) == "ko_only" and korean_focus(["en"]) == "not_ko"
    assert korean_focus([f"l{i}" for i in range(11)] + ["ko"]) == "wide_multilingual"

    linker = Linker()
    model = {
        "model_id": "BAAI/bge-reranker-v2-m3",
        "task": {"matched": ["text-classification"]},
        "language_codes": ["en", "ko", "zh"],
        "filter_metadata": {"license": "apache-2.0", "context_length": 8192, "parameter_count_billion": 0.57},
    }
    map_model(linker, model)
    concepts = {link["concept_id"] for link in linker.links.values()}
    assert {
        "task/classification",
        "task/reranking",
        "input_modality/text",
        "language/ko",
        "language/multilingual",
        "commercial_use/commercial",
        "input_length/long",
        "model_size/tiny",
    } <= concepts, concepts
    assert normalize("task", "unseen-task") is None
    linker.add("model:x", "task", "unseen-task", "task.matched")
    assert linker.unmapped["model.task.task.matched"]["unseen-task"] == 1
    linker = Linker()
    row = {
        "dataset_id": "x/y",
        "url": "",
        "sha": "",
        "task_categories": ["sentence-similarity", "text-generation", "translation"],
        "modalities": ["text"],
    }
    ner = {
        "summary_ko": "요약",
        "concepts": {
            "task": [
                {"value": "generation", "quote": "for text generation models"},
                {"value": "translation", "quote": "used to train the M3 model"},
            ],
            "input_modality": [{"value": "text", "quote": "columns anchor positive"}],
            "domain": [{"value": "finance", "quote": "Korean financial-domain data"}],
        },
    }
    entity = map_dataset(linker, row, None, ner)
    by_concept = {link["concept_id"]: link for link in linker.links.values() if link["entity_id"] == "dataset:x/y"}
    assert by_concept["task/generation"]["confidence"] == "high"  # metadata confirmed by a stated quote
    assert by_concept["task/embedding"]["confidence"] == "low"  # tag only; the README reading never names it
    assert by_concept["task/translation"]["confidence"] == "medium"  # named by NER, but loosely quoted
    assert by_concept["input_modality/text"]["confidence"] == "high"  # metadata raises the earlier low NER link
    assert by_concept["domain/finance"]["method"] == "ner" and by_concept["domain/finance"]["confidence"] == "medium"
    assert entity["summary_ko"] == "요약"
    public = {
        "dataset_id": "seoul_open_data/OA-1",
        "source": "seoul_open_data",
        "url": "",
        "sha": "",
        "languages": ["ko"],
        "licenses": [],
        "formats": ["api"],
        "tags": ["공공자전거", "검색"],
        "card_data": {"pretty_name": "서울시 공공자전거 대여소"},
    }
    assert map_dataset(linker, public, None)["source"] == "seoul_open_data"
    public_links = {
        link["concept_id"] for link in linker.links.values() if link["entity_id"] == "dataset:seoul_open_data/OA-1"
    }
    assert {"domain/transport", "dataset_role/service", "data_format/api", "language/ko"} <= public_links, public_links
    assert "task/retrieval" not in public_links, public_links
    print("13_build_hypergraph ok")


if __name__ == "__main__":
    main()
