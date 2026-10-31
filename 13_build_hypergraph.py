"""Stage H1: map model and dataset metadata onto taxonomy concepts (the hypergraph).

Each taxonomy concept is a hyperedge; an entity joins it through a link that records
where the value came from. This stage uses structured metadata only (no LLM), so every
link is reproducible from metadata, except method="ner" links read from Stage D4
(16_extract_dataset_ner.py). An NER link is "medium" when its README quote names the
concept and "low" when the quote merely exists. Once NER has read a card, a metadata task
keeps "high" only if a quote states it, drops to "medium" if NER names it loosely, and to
"low" if NER does not name it at all (tags like sentence-similarity are often wrong).

Outputs (data/hypergraph/):
  entities.jsonl   one row per model/dataset with quality flags
  links.jsonl      entity -> concept, with method, source field, raw value, confidence
  relations.jsonl  entity -> entity edges (model trained_with dataset)
  concepts.jsonl   every concept with its member count
  report.json      coverage per facet and the raw values that did not map
"""
from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

from taxonomy import label, load_taxonomy, mentions, normalize

DATA_DIR = Path("data")
OUT_DIR = DATA_DIR / "hypergraph"
MODEL_INPUTS = (DATA_DIR / "hf_models_stage4_core.jsonl", DATA_DIR / "hf_models_stage4_low_popularity.jsonl")
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
PUBLIC_INPUT = DATA_DIR / "public_datasets_stage1.jsonl"  # 서울 열린데이터광장 + 공공데이터포털 (18)
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
    if not path or not Path(path).exists():
        return "missing"
    body = FRONTMATTER_RE.sub("", Path(path).read_text(encoding="utf-8"), count=1).strip()
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
        self.links[key] = {"entity_id": entity_id, "concept_id": f"{facet}/{concept}", "facet": facet,
                           "method": method, "fields": [field], "raw": raw, "confidence": confidence}

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
        "entity_id": entity_id, "kind": "model", "name": row["model_id"], "source": "huggingface",
        "url": f"https://huggingface.co/{row['model_id']}", "source_pool": row.get("source_pool"),
        "downloads": fm.get("downloads"), "languages": languages, "license": fm.get("license"),
        "context_length": fm.get("context_length"), "parameter_count_billion": fm.get("parameter_count_billion"),
    }


def map_ner(linker, entity_id, ner):
    """Add README-grounded concepts; demote metadata tasks the README does not back up."""
    tasks = {}
    for facet, items in ner["concepts"].items():
        for item in items:
            stated = mentions(facet, item["value"], item["quote"])
            if facet == "task":
                tasks[item["value"]] = tasks.get(item["value"]) or stated
            linker.add(entity_id, facet, item["quote"][:QUOTE_CHARS], "readme", method="ner",
                       confidence="medium" if stated else "low", concept=item["value"])
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
    tag_facets = ("task", "domain") if row.get("source", "huggingface") == "huggingface" else ("domain",)
    for tag in free_tags:
        for facet in tag_facets:
            if normalize(facet, tag):
                linker.add(entity_id, facet, tag, "tags", method="tag_match", confidence="medium")
    if ner:
        map_ner(linker, entity_id, ner)
    source = row.get("source", "huggingface")
    if source != "huggingface":
        # Public portal data is looked up by apps at runtime; titles are Korean compounds
        # (공공자전거, 미세먼지농도) that hold a domain alias without equalling it.
        linker.add(entity_id, "dataset_role", "service", "source", method="source_rule", confidence="medium")
        text = " ".join([(row.get("card_data") or {}).get("pretty_name") or "", *(row.get("tags") or [])])
        for value in load_taxonomy()["facets"]["domain"]["values"]:
            if value != "general" and mentions("domain", value, text):
                linker.add(entity_id, "domain", value, "title/keywords", method="tag_match", confidence="medium", concept=value)
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
            linker.add(entity_id, "dataset_size", upper - 1, "size_categories", concept=normalize("dataset_size", upper - 1))
    if row.get("referenced_by_models"):
        linker.add(entity_id, "dataset_role", "train", "referenced_by_models", confidence="medium")
    if EVAL_NAME_RE.search(row["dataset_id"]) or any(normalize("dataset_role", t) == "evaluation" for t in free_tags):
        linker.add(entity_id, "dataset_role", "evaluation", "dataset_id/tags", method="name_rule", confidence="medium")
    if length and length.get("status") == "ok" and length.get("tokens_p90_estimate"):
        linker.add(entity_id, "input_length", length["tokens_p90_estimate"], "viewer_statistics",
                   method="viewer_stats", confidence="medium")
    status = readme_status(row)
    return {
        "entity_id": entity_id, "kind": "dataset", "name": row["dataset_id"], "source": source,
        "url": row["url"], "downloads": row.get("downloads"), "likes": row.get("likes"), "gated": row.get("gated"),
        "languages": languages, "licenses": row.get("licenses"), "seed_reasons": row.get("seed_reasons"),
        "readme_path": row.get("readme_path"), "readme_language": row.get("readme_language"),
        "readme_status": status, "korean_focus": korean_focus(languages),
        "summary_ko": ner.get("summary_ko") if ner else None,
        "title": (row.get("card_data") or {}).get("pretty_name") if source != "huggingface" else None,
        "sample_length": {k: length.get(k) for k in ("text_column", "chars", "tokens_p90_estimate", "config", "split")}
        if length and length.get("status") == "ok" else None,
    }


def coverage(entities, links):
    facets = load_taxonomy()["facets"]
    linked = defaultdict(set)
    for link in links:
        linked[link["facet"]].add(link["entity_id"])
    report = {}
    for kind in ("model", "dataset"):
        ids = {e["entity_id"] for e in entities if e["kind"] == kind}
        report[kind] = {facet: f"{len(linked[facet] & ids)}/{len(ids)}" for facet, spec in facets.items()
                        if kind in spec["applies_to"]}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    linker = Linker()
    lengths = {r["dataset_id"]: r for r in read_jsonl(LENGTH_INPUT)}
    entities = [map_model(linker, row) for path in MODEL_INPUTS for row in read_jsonl(path)]
    ners = {r["dataset_id"]: r for r in read_jsonl(NER_INPUT)}
    entities += [map_dataset(linker, row, lengths.get(row["dataset_id"]), ners.get(row["dataset_id"]))
                 for path in (DATASET_INPUT, PUBLIC_INPUT) for row in read_jsonl(path)]
    links = sorted(linker.links.values(), key=lambda l: (l["entity_id"], l["concept_id"]))

    known = {e["entity_id"] for e in entities}
    relations = []
    for row in read_jsonl(DATASET_INPUT):
        for model_id in row.get("referenced_by_models") or []:
            if f"model:{model_id}" in known:
                relations.append({"source": f"model:{model_id}", "relation": "trained_with",
                                  "target": f"dataset:{row['dataset_id']}", "method": "metadata",
                                  "fields": ["cardData.datasets"], "confidence": "high"})

    members = Counter(link["concept_id"] for link in links)
    concepts = []
    for facet, spec in load_taxonomy()["facets"].items():
        keys = list(spec["values"]) + sorted({c.split("/", 1)[1] for c in members if c.startswith(facet + "/")} - set(spec["values"]))
        for key in keys:
            concept_id = f"{facet}/{key}"
            concepts.append({"concept_id": concept_id, "facet": facet, "facet_label": spec["label"], "key": key,
                             "label": label(facet, key),
                             "aliases": [a for a in spec["values"].get(key, {}).get("aliases", []) if a],
                             "members": members.get(concept_id, 0)})

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_jsonl(OUT_DIR / "entities.jsonl", entities)
    write_jsonl(OUT_DIR / "links.jsonl", links)
    write_jsonl(OUT_DIR / "relations.jsonl", relations)
    write_jsonl(OUT_DIR / "concepts.jsonl", concepts)
    report = {
        "entities": Counter(e["kind"] for e in entities),
        "links": len(links), "relations": len(relations),
        "links_by_method": Counter(l["method"] for l in links),
        "links_by_confidence": Counter(l["confidence"] for l in links),
        "coverage": coverage(entities, links),
        "dataset_readme_status": Counter(e["readme_status"] for e in entities if e["kind"] == "dataset"),
        "dataset_korean_focus": Counter(e["korean_focus"] for e in entities if e["kind"] == "dataset"),
        "unmapped_top": {k: v.most_common(25) for k, v in sorted(linker.unmapped.items())},
    }
    (OUT_DIR / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "unmapped_top"}, ensure_ascii=False, indent=2))
    print(f"unmapped value groups: {len(linker.unmapped)} (see {OUT_DIR / 'report.json'})")


def self_check():
    assert size_category_upper("10K<n<100K") == 1e5
    assert size_category_upper("n<1K") == 1e3
    assert size_category_upper("1B<n<10B") == 1e10
    assert size_category_upper("n>1T") == float("inf")
    assert korean_focus(["ko"]) == "ko_only" and korean_focus(["en"]) == "not_ko"
    assert korean_focus([f"l{i}" for i in range(11)] + ["ko"]) == "wide_multilingual"

    linker = Linker()
    model = {"model_id": "BAAI/bge-reranker-v2-m3", "task": {"matched": ["text-classification"]},
             "language_codes": ["en", "ko", "zh"],
             "filter_metadata": {"license": "apache-2.0", "context_length": 8192, "parameter_count_billion": 0.57}}
    map_model(linker, model)
    concepts = {link["concept_id"] for link in linker.links.values()}
    assert {"task/classification", "task/reranking", "input_modality/text", "language/ko",
            "language/multilingual", "commercial_use/commercial", "input_length/long", "model_size/tiny"} <= concepts, concepts
    assert normalize("task", "unseen-task") is None
    linker.add("model:x", "task", "unseen-task", "task.matched")
    assert linker.unmapped["model.task.task.matched"]["unseen-task"] == 1
    linker = Linker()
    row = {"dataset_id": "x/y", "url": "", "sha": "", "task_categories": ["sentence-similarity", "text-generation", "translation"],
           "modalities": ["text"]}
    ner = {"summary_ko": "요약", "concepts": {
        "task": [{"value": "generation", "quote": "for text generation models"},
                 {"value": "translation", "quote": "used to train the M3 model"}],
        "input_modality": [{"value": "text", "quote": "columns anchor positive"}],
        "domain": [{"value": "finance", "quote": "Korean financial-domain data"}]}}
    entity = map_dataset(linker, row, None, ner)
    by_concept = {l["concept_id"]: l for l in linker.links.values() if l["entity_id"] == "dataset:x/y"}
    assert by_concept["task/generation"]["confidence"] == "high"  # metadata confirmed by a stated quote
    assert by_concept["task/embedding"]["confidence"] == "low"  # tag only; the README reading never names it
    assert by_concept["task/translation"]["confidence"] == "medium"  # named by NER, but loosely quoted
    assert by_concept["input_modality/text"]["confidence"] == "high"  # metadata raises the earlier low NER link
    assert by_concept["domain/finance"]["method"] == "ner" and by_concept["domain/finance"]["confidence"] == "medium"
    assert entity["summary_ko"] == "요약"
    public = {"dataset_id": "seoul_open_data/OA-1", "source": "seoul_open_data", "url": "", "sha": "", "languages": ["ko"],
              "licenses": [], "formats": ["api"], "tags": ["공공자전거", "검색"], "card_data": {"pretty_name": "서울시 공공자전거 대여소"}}
    assert map_dataset(linker, public, None)["source"] == "seoul_open_data"
    public_links = {l["concept_id"] for l in linker.links.values() if l["entity_id"] == "dataset:seoul_open_data/OA-1"}
    assert {"domain/transport", "dataset_role/service", "data_format/api", "language/ko"} <= public_links, public_links
    assert "task/retrieval" not in public_links, public_links
    print("13_build_hypergraph ok")


if __name__ == "__main__":
    main()
