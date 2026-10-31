---
license: apache-2.0
language:
- en
- zh
- ko
- de
- nl
- es
- it
- da
- fr
- sv
- pt
tags:
- agent
- scraping
- structured-output
- json-schema
- web-scraping
pretty_name: ScrapeGraphAI-100k
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- text-classification
- feature-extraction
---

# ScrapeGraphAI-100k

![Frame 9](https://cdn-uploads.huggingface.co/production/uploads/600c3a3beeb59d1c4ad29d32/Xk2Bc0yU2-3DAKhnXMJ8E.png)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ScrapeGraphAI](https://img.shields.io/badge/Org-ScrapeGraphAI-orange)](https://scrapegraphai.com)

## Dataset Summary

ScrapeGraphAI-100k is a dataset of 93,695 real-world schema-constrained extraction events collected via opt-in telemetry of the [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) open-source scraping library in Q2–Q3 2025. The dataset was derived from ~9 million raw PostHog telemetry events, deduplicated and balanced for schema diversity. Each example captures one LLM attempt to extract structured data from real web content under a user-defined JSON schema: the prompt, the Markdown-converted page content, the target schema, the model's response, and rich metadata (model, latency, schema-complexity metrics, and a structural-validation flag).


## Quick Start

```python
from datasets import load_dataset

ds = load_dataset("scrapegraphai/scrapegraphai-100k")
```

## Dataset Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the extraction event |
| `prompt` | string | Natural-language instruction sent to the LLM |
| `schema` | string | JSON schema defining the expected output structure |
| `schema_hash` | string | SHA256 hash of the schema (used for deduplication/balancing) |
| `response` | string | LLM's extracted output (JSON string) |
| `content` | string | Source web content, converted to Markdown |
| `llm_model` | string | Model used for extraction |
| `source` | string | Source URL (domain-masked if sensitive) |
| `execution_time` | float | Extraction latency in seconds |
| `response_size` | int | Response size in bytes |
| `schema_size` | int | Schema size in bytes |
| `schema_depth` | int | Maximum nesting depth of the schema |
| `schema_keys` | int | Number of keys in the schema |
| `schema_elements` | int | Total number of schema elements |
| `schema_cyclomatic_complexity` | int | Cyclomatic complexity of the schema |
| `schema_complexity_score` | float | Aggregate complexity score |
| `response_is_valid` | bool | True iff the response parses as JSON and conforms to the schema (**structural** validation via `jsonschema-rs`, not semantic correctness) |

Schema-complexity metrics follow [SLOT: Structuring the Output of Large Language Models](https://arxiv.org/abs/2505.04016) (Wang et al., 2025).

## Key Statistics (v1.0)

- **93,695 rows**, **25,453 unique schemas** (by schema hash), 80,313 unique source values, of which 80,213 are unique URLs (99.9% of examples come from resolvable public web URLs).
- **Domain diversity:** 10,295 unique hostnames across 8,155 registered root domains (eTLD+1), 61,858 unique (schema, domain) pairs. Coverage is heavy-tailed (top-10 domains = 44.2% of examples, 56.3% of domains contribute exactly one example), but high-frequency domains carry many distinct schemas (e.g. amazon.com: 10,155 examples, 8,381 distinct schemas).
- **Structural validity:** 96.5% of released responses parse and conform to their schema (`response_is_valid`). Invalid responses are retained deliberately to support failure-mode research. This flag certifies structure, not semantic correctness.
- **Extraction models:** gpt-4o-mini 87.4%, gpt-4o 3.6%, gpt-4.1-mini 1.0%, ~1.1% unrecorded, with a long tail of 296 distinct models (Gemini, DeepSeek, Llama, local models).
- **Scale:** median page content ~10k characters (p90 ~41k), median response ~10 kB (max ~1 MB), schema depth median 5 (max 9), schema keys median 37 (max 3,060), median latency 8.5 s.

## Language Distribution

Language of each `content` field, detected with fastText ([facebook/fasttext-language-identification](https://huggingface.co/facebook/fasttext-language-identification)) after stripping Markdown link/image syntax and raw URLs (detection on raw markup misattributes URL-heavy pages to CJK languages). 87,887 rows had enough visible text for detection, 5,808 were too short or undetectable.

| Language | Count | Share |
|---|---|---|
| English (`eng_Latn`) | 78,088 | 88.9% |
| Traditional Chinese (`yue_Hant`) | 2,233 | 2.5% |
| Korean (`kor_Hang`) | 2,027 | 2.3% |
| German (`deu_Latn`) | 1,406 | 1.6% |
| Dutch (`nld_Latn`) | 695 | 0.8% |
| Spanish (`spa_Latn`) | 505 | 0.6% |
| Italian (`ita_Latn`) | 428 | 0.5% |
| Danish (`dan_Latn`) | 344 | 0.4% |
| French (`fra_Latn`) | 311 | 0.4% |
| Swedish (`swe_Latn`) | 312 | 0.4% |
| Other (40+ languages) | 1,538 | 1.7% |


## Curation and Filtering

Pipeline from raw telemetry to release, as described in the paper:

1. **Source:** ~9M opt-in PostHog telemetry events from the ScrapeGraphAI OSS library (Q2–Q3 2025). Users explicitly consent via a configuration flag, PostHog is configured to exclude user identifiers and personal data.
2. **Flattening and validation:** each event is flattened into (source URL, prompt, schema, Markdown content, response), every response is validated against its schema with [`jsonschema-rs`](https://github.com/Stranger6667/jsonschema). Raw-corpus validity was 93%, invalid responses are **retained** with `response_is_valid=false` to enable failure-mode research.
3. **Balancing and deduplication:** events are grouped by SHA256 schema hash, keeping at most 5 examples per unique schema (two schemas targeting high-traffic e-commerce sites alone accounted for ~5M of the 9M raw events), selected examples must originate from distinct root domains.
4. **Complexity annotation:** five structural complexity metrics (depth, keys, elements, cyclomatic complexity, composite score) computed per schema following SLOT.

**Known noise modes** (~3.5% of released rows fail validation): upstream LLM errors (truncation, refusals), fetch-time failures surfaced in `content` (HTTP error pages, anti-bot challenges, CAPTCHAs), and non-textual pages (image galleries) where Markdown conversion yields little signal. For clean-extraction training or evaluation, filter on `response_is_valid=true` and apply content heuristics for non-textual sources.

## Intended Uses

- **Benchmarking schema-constrained generation:** evaluating structured-output compliance and key/value accuracy on real, user-defined schemas across a wide complexity range, including stratified analysis by depth, key count, and complexity score (sharp failure thresholds appear at depth ≥ 7 and keys ≥ 200).
- **Finetuning and distillation:** training compact models for structured extraction (see the [companion finetuning dataset](https://huggingface.co/datasets/scrapegraphai/scrapegraph-100k-finetuning) and [sgai-qwen3-1.7b](https://huggingface.co/scrapegraphai/sgai-qwen3-1.7b)).
- **Failure-mode analysis:** the retained invalid responses and complexity metadata support systematic study of extraction failures and failure prediction.
- **Schema induction:** 25k+ unique schemas paired with the content that produced them provide signal for schema-from-content research.

### Out-of-Scope Uses

- **Not a source of verified facts.** `response` values are LLM outputs over scraped pages, not human-verified ground truth, a substantial fraction contain semantic errors (see Limitations). Do not treat them as factual data about the referenced websites, products, or people.
- **Not for identifying or profiling individuals.** Names and contact details appearing in scraped pages must not be used to build profiles of private individuals (see Privacy).
- **Not a current snapshot of the web.** Content reflects pages as scraped in Q2–Q3 2025, some URLs no longer resolve or have changed.


## Privacy and PII

We audited (via [openai/privacy-filter](https://github.com/openai/privacy-filter)) every text field (`prompt`, `content`, `schema`, `response`) of all 93,695 rows for eight PII classes and credential formats. Distinct rows with ≥1 detection per field:

| PII class | prompt | content | schema | response | total | % of rows |
|---|---|---|---|---|---|---|
| email | 52 | 4,707 | 8 | 912 | 5,679 | 6.1% |
| phone | 677 | 4,216 | 7 | 942 | 5,842 | 6.2% |
| address | 128 | 2,781 | 8 | 1,388 | 4,305 | 4.6% |
| person name | 3,051 | 37,734 | 726 | 4,189 | 45,700 | 48.8% |
| private URL | 5,652 | 30,092 | 20 | 1,432 | 37,196 | 39.7% |
| date | 755 | 3,595 | 82 | 1,467 | 5,899 | 6.3% |
| account number | 2,507 | 3,741 | 0 | 335 | 6,583 | 7.0% |
| secret / key | 25 | 8,710 | 10 | 56 | 8,801 | 9.4% |

The `total` column sums per-field counts (a row flagged in multiple fields contributes once per field), so `% of rows` is an upper bound. Detections concentrate in `content` (raw scraped markup). `person name` triggers on any name on a public page (bylines, public figures, business owners), `date` includes publication dates.

**Consent scope:** data comes exclusively from opt-in telemetry (explicit configuration flag) of the ScrapeGraphAI OSS library, PostHog is configured to exclude user identifiers, and sensitive source URLs are domain-masked.

## Takedown Policy

Site owners and private individuals can request removal of content referencing them:

1. Email **support@scrapegraphai.com**, identifying the affected content by URL, domain, or quoted span.
2. Requests are acknowledged within 24 hours and, if accepted, honored in a patch release within 30 days, and propagated to the finetuning dataset and all future versions.

## Related Resources

- **Paper:** [ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation](https://arxiv.org/abs/2602.15189)
- **Reproducibility repository:** [github.com/ScrapeGraphAI/scrapegraph-100k-paper](https://github.com/ScrapeGraphAI/scrapegraph-100k-paper) — analysis scripts, evaluation metrics, finetuning pipeline, PII audit, LLM-judge pilot.
- **Finetuning dataset:** [scrapegraphai/scrapegraph-100k-finetuning](https://huggingface.co/datasets/scrapegraphai/scrapegraph-100k-finetuning)
- **Finetuned model:** [scrapegraphai/sgai-qwen3-1.7b](https://huggingface.co/scrapegraphai/sgai-qwen3-1.7b).
- **ScrapeGraphAI library:** [github.com/ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai).

## License

Apache 2.0, matching the upstream library. The license covers the derivative artifacts released here (Markdown content, prompts, schemas, responses, metadata), not the underlying web pages, whose copyright remains with their original publishers. Raw HTML and exhaustive page reproductions are deliberately not redistributed. The takedown process above applies.

## Maintenance

Semantic versioning, a longitudinal refresh (Q2–Q3 2026 telemetry) is planned for Q4 2026. Community contributions are accepted via GitHub issues and pull requests on the reproducibility repository.

## Citation

```bibtex
@misc{brach2026scrapegraphai100kdatasetschemaconstrainedllm,
      title={ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation}, 
      author={William Brach and Francesco Zuppichini and Marco Vinciguerra and Lorenzo Padoan},
      year={2026},
      eprint={2602.15189},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2602.15189}, 
}
```