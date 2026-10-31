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
import functools
import hashlib
import json
import os
import re
import time
from collections import defaultdict
from typing import Literal
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pydantic import BaseModel, create_model

from taxonomy import load_taxonomy

DATA_DIR = Path("data")
DATASET_INPUT = DATA_DIR / "hf_datasets_stage1.jsonl"
# Kaggle tags are noisy (restaurant reviews tagged finance/health); NER confirms or demotes them.
# Portal data (18) is skipped: its category already names the domain and it has no ML task.
KAGGLE_INPUT = DATA_DIR / "kaggle_datasets_stage1.jsonl"
CHUNKS_INPUT = DATA_DIR / "dataset_index" / "chunks.jsonl"
OUTPUT = DATA_DIR / "hf_datasets_ner.jsonl"
# gpt-4o-mini dropped 2x more quotes on the 30-card sample and missed benchmark roles; 4.1-mini costs ~$3 per full run.
MODEL = os.getenv("NER_LLM_MODEL", "gpt-4.1-mini")
PROMPT_VERSION = "dataset-ner-v2"
NER_FACETS = ("task", "domain", "dataset_role", "input_modality", "output_modality")
# ponytail: first sections only; ~2.5K tokens covers the summary/usage part of nearly every card.
MAX_CONTEXT_CHARS = 8000
MAX_RETRIES = 4
RETRY_CONTEXT_CHARS = 1500
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


@functools.lru_cache(maxsize=1)
def ner_model() -> type[BaseModel]:
    """Pydantic output model built from the taxonomy: each facet is a list of {value, quote},
    and value is a Literal of that facet's concept keys, so an off-taxonomy label fails validation."""
    facets = load_taxonomy()["facets"]
    fields = {"summary_ko": (str, ...)}
    for facet in NER_FACETS:
        value_type = Literal[tuple(facets[facet]["values"])]
        evidence = create_model(f"{facet.title().replace('_', '')}Evidence", value=(value_type, ...), quote=(str, ...))
        fields[facet] = (list[evidence], ...)
    return create_model("DatasetNER", **fields)


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


def validate_loose(data):
    """Free-form JSON -> the Pydantic model, keeping only items that validate on their own."""
    from typing import get_args

    from pydantic import ValidationError

    model, fields = ner_model(), {"summary_ko": str((data or {}).get("summary_ko") or "")}
    for facet in NER_FACETS:
        evidence = get_args(model.model_fields[facet].annotation)[0]
        fields[facet] = []
        for item in (data or {}).get(facet) or []:
            try:
                fields[facet].append(evidence.model_validate(item))
            except ValidationError:
                continue
    return model(**fields)


def json_mode_fallback(client, system, context):
    """Last resort after strict decoding looped twice: plain JSON mode, validated item by item."""
    shape = ("\nReturn one JSON object with keys summary_ko and " + ", ".join(NER_FACETS)
             + "; each facet is a list of {\"value\": <concept key>, \"quote\": <text>}.")
    response = client.chat.completions.create(
        model=MODEL, temperature=0, max_tokens=900, response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system + shape}, {"role": "user", "content": context}])
    return validate_loose(json.loads(response.choices[0].message.content)), response


def extract(client, row, context, system):
    from openai import LengthFinishReasonError

    full_context, hint = context, ""
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.chat.completions.parse(
                model=MODEL, temperature=0, max_tokens=900, response_format=ner_model(),
                messages=[{"role": "system", "content": system + hint}, {"role": "user", "content": context}])
            parsed = response.choices[0].message.parsed
            if parsed is None:
                raise ValueError("model refused")
            break
        except (ValueError, LengthFinishReasonError) as error:
            # Malformed or runaway output repeats at temperature 0: a multilingual card made strict
            # decoding loop past any token limit. Retry once on the card's head with a tighter brief;
            # quotes are then verified against that same head.
            if hint:
                print(f"[NER] json-mode fallback {row['dataset_id']}", flush=True)
                parsed, response = json_mode_fallback(client, system + hint, context)
                break
            hint = "\nAt most 3 items per facet, strongest first. Quotes as plain text, no backslash escapes."
            context = context[:RETRY_CONTEXT_CHARS]
            print(f"[NER] re-asking {row['dataset_id']}: {type(error).__name__}", flush=True)
        except Exception as error:  # rate limits and transient API errors; the last one propagates
            if attempt == MAX_RETRIES:
                raise
            time.sleep(min(60, 5 * 2**attempt))
            print(f"[NER] retry {row['dataset_id']}: {type(error).__name__}", flush=True)
    extracted = parsed.model_dump()
    concepts, dropped = verify(extracted, context)
    return {"dataset_id": row["dataset_id"], "sha": row["sha"], "prompt_version": PROMPT_VERSION, "model": MODEL,
            "context_hash": hashlib.sha256(full_context.encode("utf-8")).hexdigest(), "context_chars": len(context),
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
    rows = read_jsonl(DATASET_INPUT) + read_jsonl(KAGGLE_INPUT)
    if args.ids:
        rows = [r for r in rows if r["dataset_id"] in set(args.ids)]
    # Mirrors collapsed by 13 (dataset_dedup) are never shown; reading them only costs tokens.
    duplicates_path = DATA_DIR / "hypergraph" / "duplicates.json"
    duplicates = json.loads(duplicates_path.read_text(encoding="utf-8")) if duplicates_path.exists() else {}
    rows = [r for r in rows if r["dataset_id"] not in duplicates][: args.limit]
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
    system = system_prompt()
    tokens, failed = [0, 0], 0
    with ThreadPoolExecutor(args.workers) as pool, open(OUTPUT, "a", encoding="utf-8") as log:
        futures = {pool.submit(extract, client, r, contexts[r["dataset_id"]], system): r for r in todo}
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
    order = [r["dataset_id"] for r in read_jsonl(DATASET_INPUT) + read_jsonl(KAGGLE_INPUT)]
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
    from pydantic import ValidationError

    model = ner_model()
    assert set(model.model_fields) == {"summary_ko", *NER_FACETS}
    good = model.model_validate({"summary_ko": "요약", "task": [{"value": "embedding", "quote": "q"}], "domain": [],
                                 "dataset_role": [], "input_modality": [], "output_modality": []})
    assert good.model_dump()["task"] == [{"value": "embedding", "quote": "q"}]
    loose = validate_loose({"summary_ko": "s", "task": [{"value": "embedding", "quote": "a"}, {"value": "nope", "quote": "b"}, "junk"]})
    assert [i.value for i in loose.task] == ["embedding"] and loose.domain == []
    try:
        model.model_validate({**good.model_dump(), "task": [{"value": "not_a_concept", "quote": "q"}]})
        raise AssertionError("off-taxonomy value accepted")
    except ValidationError:
        pass
    assert "따릉이" in system_prompt() or "transport" in system_prompt()
    print("16_extract_dataset_ner ok")


if __name__ == "__main__":
    main()
