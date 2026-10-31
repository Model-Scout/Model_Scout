"""Stage D4: grounded attribute extraction (NER) from dataset READMEs.

Metadata (tags, task_categories) is missing for ~500 datasets and wrong for some, and
domain/role are rarely tagged at all. This stage asks an LLM to pick taxonomy concepts
for each dataset, each backed by a quote copied from the README. A quote that is not an
exact (whitespace/case-insensitive) substring of the supplied text drops the concept, so
every NER link in the hypergraph points at real evidence.

The context is the dataset description and README sections only, never the card chunk:
its concept lines were written from metadata, and quoting them back would be circular.
Works on Korean and English READMEs alike; the summary is always Korean so English cards
are reachable from Korean queries.

Output: data/hf_datasets_ner.jsonl, appended per dataset (resumable); a row is reused
while its context hash and PROMPT_VERSION are unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from taxonomy import load_taxonomy

DATA_DIR = Path("data")
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
CHUNKS_INPUT = DATA_DIR / "dataset_index" / "chunks.jsonl"
OUTPUT = DATA_DIR / "hf_datasets_ner.jsonl"
# gpt-4o-mini dropped 2x more quotes on the 30-card sample and missed benchmark roles; 4.1-mini costs ~$3 per full run.
MODEL = os.getenv("NER_LLM_MODEL", "gpt-4.1-mini")
PROMPT_VERSION = "dataset-ner-v2"
NER_FACETS = ("task", "domain", "dataset_role", "input_modality", "output_modality")
# ponytail: first sections only; ~2.5K tokens covers the summary/usage part of nearly every card.
MAX_CONTEXT_CHARS = 8000
MAX_RETRIES = 4
# Below this the card is just an id and a line; the LLM only invents labels, so metadata stands alone.
MIN_CONTEXT_CHARS = 200
FACET_GUIDE = {
    "task": "The 1-3 tasks this data is built for, primary first. Not every annotation column, and not the model that produced the data.",
    "domain": "Subject area of the content itself. academic = scholarly papers or science content, not merely 'a paper describes this dataset'. "
              "general = broad web/wiki/chat with no single subject. Omit when unclear.",
    "dataset_role": "train = training/fine-tuning data; evaluation = benchmark/test set; service = lookup data an application queries at "
                    "runtime (station lists, place or product databases, public-data APIs). Corpora, translations and benchmarks are never service.",
    "input_modality": "Modality of the model input built from this data.",
    "output_modality": "Modality of the target/label/answer.",
}


def read_jsonl(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def squash(text):
    return " ".join(text.casefold().split())


def build_context(row, sections):
    pretty = (row.get("card_data") or {}).get("pretty_name")
    parts = [f"DATASET_ID: {row['dataset_id']}" + (f" ({pretty})" if pretty else "")]
    if description := (row.get("description") or "").strip():
        parts.append(description)
    used = sum(map(len, parts))
    for text in sections:
        if used + len(text) > MAX_CONTEXT_CHARS:
            parts.append(text[: MAX_CONTEXT_CHARS - used])
            break
        parts.append(text)
        used += len(text)
    return "\n\n".join(parts)


def schema():
    facets = load_taxonomy()["facets"]
    item = lambda facet: {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["value", "quote"],
        "properties": {"value": {"type": "string", "enum": list(facets[facet]["values"])}, "quote": {"type": "string"}}}}
    return {"type": "object", "additionalProperties": False, "required": ["summary_ko", *NER_FACETS],
            "properties": {"summary_ko": {"type": "string"}, **{f: item(f) for f in NER_FACETS}}}


def system_prompt():
    facets = load_taxonomy()["facets"]
    lines = ["You label Hugging Face dataset cards with a fixed taxonomy. The card may be Korean or English.",
             "For each facet return only concepts the text states or directly shows, each with a quote: a short span "
             "(5-25 words) copied character-for-character from the text, in its original language. "
             "Never quote the DATASET_ID line alone unless the name itself states the concept. "
             "Return an empty list when the text gives no evidence; guessing is worse than omitting.",
             "summary_ko: one Korean sentence (<= 80 chars) saying what the data is and what it is for; "
             "keep proper nouns and dataset names as written.", ""]
    for facet in NER_FACETS:
        spec = facets[facet]
        lines.append(f"## {facet} ({spec['label']}): {FACET_GUIDE[facet]}")
        for key, value in spec["values"].items():
            aliases = ", ".join(str(a) for a in (value.get("aliases") or [])[:6])
            lines.append(f"- {key}: {value['label']}" + (f" (e.g. {aliases})" if aliases else ""))
    return "\n".join(lines)


def verify(extracted, context):
    """Keep concepts whose quote appears in the context; return (facet -> [{value, quote}], dropped count)."""
    haystack, kept, dropped = squash(context), defaultdict(list), 0
    for facet in NER_FACETS:
        seen = set()
        for item in extracted.get(facet, []):
            quote = item["quote"].strip()
            if len(quote) < 3 or squash(quote) not in haystack:
                dropped += 1
            elif item["value"] not in seen:
                seen.add(item["value"])
                kept[facet].append({"value": item["value"], "quote": quote})
    return dict(kept), dropped


def extract(client, row, context, system, response_schema):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=MODEL, temperature=0, max_tokens=900,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": context}],
                response_format={"type": "json_schema", "json_schema": {"name": "dataset_ner", "strict": True, "schema": response_schema}})
            break
        except Exception as error:  # rate limits and transient API errors; the last one propagates
            if attempt == MAX_RETRIES:
                raise
            time.sleep(min(60, 5 * 2**attempt))
            print(f"[NER] retry {row['dataset_id']}: {type(error).__name__}", flush=True)
    extracted = json.loads(response.choices[0].message.content)
    concepts, dropped = verify(extracted, context)
    return {"dataset_id": row["dataset_id"], "sha": row["sha"], "prompt_version": PROMPT_VERSION, "model": MODEL,
            "context_hash": hashlib.sha256(context.encode("utf-8")).hexdigest(), "context_chars": len(context),
            "summary_ko": extracted["summary_ko"].strip(), "concepts": concepts, "dropped_quotes": dropped,
            "usage": {"prompt": response.usage.prompt_tokens, "completion": response.usage.completion_tokens}}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--limit", type=int)
    parser.add_argument("--ids", nargs="*", help="only these dataset ids (for spot checks)")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()

    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(".env")
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sections = defaultdict(list)
    for chunk in read_jsonl(CHUNKS_INPUT):
        if chunk["kind"] == "section":
            sections[chunk["dataset_id"]].append(chunk["text"])
    rows = read_jsonl(DATASET_INPUT)
    if args.ids:
        rows = [r for r in rows if r["dataset_id"] in set(args.ids)]
    rows = rows[: args.limit]
    cached = {r["dataset_id"]: r for r in read_jsonl(OUTPUT)}
    contexts = {r["dataset_id"]: build_context(r, sections[r["dataset_id"]]) for r in rows}

    def fresh(row):
        old = cached.get(row["dataset_id"])
        context_hash = hashlib.sha256(contexts[row["dataset_id"]].encode("utf-8")).hexdigest()
        return old and (old["prompt_version"], old["model"], old["context_hash"]) == (PROMPT_VERSION, MODEL, context_hash)

    todo = [r for r in rows if not fresh(r) and len(contexts[r["dataset_id"]]) >= MIN_CONTEXT_CHARS]
    thin = sum(len(c) < MIN_CONTEXT_CHARS for c in contexts.values())
    print(f"[NER] {len(rows)} datasets, {thin} too thin to read, {len(rows) - len(todo) - thin} cached, "
          f"extracting {len(todo)} with {MODEL}", flush=True)
    system, response_schema = system_prompt(), schema()
    tokens, failed = [0, 0], 0
    with ThreadPoolExecutor(args.workers) as pool, open(OUTPUT, "a", encoding="utf-8") as log:
        futures = {pool.submit(extract, client, r, contexts[r["dataset_id"]], system, response_schema): r for r in todo}
        for done, future in enumerate(as_completed(futures), 1):
            try:
                result = future.result()
            except Exception as error:
                failed += 1
                print(f"[NER] failed {futures[future]['dataset_id']}: {error}", flush=True)
                continue
            cached[result["dataset_id"]] = result
            tokens[0] += result["usage"]["prompt"]
            tokens[1] += result["usage"]["completion"]
            log.write(json.dumps(result, ensure_ascii=False) + "\n")
            log.flush()
            if done % 50 == 0:
                print(f"[NER] {done}/{len(todo)} tokens in/out {tokens[0]}/{tokens[1]}", flush=True)

    # Compact the append log to one row per dataset, in input order.
    order = [r["dataset_id"] for r in read_jsonl(DATASET_INPUT)]
    temp = OUTPUT.with_suffix(".jsonl.tmp")
    with open(temp, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(cached[d], ensure_ascii=False) + "\n" for d in order if d in cached)
    os.replace(temp, OUTPUT)
    print(json.dumps({"extracted": len(todo) - failed, "failed": failed, "tokens_in": tokens[0], "tokens_out": tokens[1],
                      "rows": len(cached)}), f"-> {OUTPUT}")


def self_check():
    context = "DATASET_ID: x/y\n\nThis   benchmark evaluates Korean\nlegal QA."
    kept, dropped = verify({"task": [{"value": "question_answering", "quote": "evaluates korean legal QA"},
                                     {"value": "summarization", "quote": "summarizes news"}],
                            "dataset_role": [{"value": "evaluation", "quote": "This benchmark"},
                                             {"value": "evaluation", "quote": "benchmark evaluates"}],
                            "domain": [{"value": "legal", "quote": "QA"}]}, context)
    assert kept == {"task": [{"value": "question_answering", "quote": "evaluates korean legal QA"}],
                    "dataset_role": [{"value": "evaluation", "quote": "This benchmark"}]}, kept
    assert dropped == 2, dropped
    built = build_context({"dataset_id": "a/b", "description": "desc", "card_data": {}}, ["s" * 5000, "t" * 5000])
    assert built.startswith("DATASET_ID: a/b\n\ndesc") and len(built) <= MAX_CONTEXT_CHARS + 10
    assert set(schema()["required"]) == {"summary_ko", *NER_FACETS}
    assert "따릉이" in system_prompt() or "transport" in system_prompt()
    print("16_extract_dataset_ner ok")


if __name__ == "__main__":
    main()
