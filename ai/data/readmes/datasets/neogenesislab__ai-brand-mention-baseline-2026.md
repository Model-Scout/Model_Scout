---
license: cc-by-4.0
task_categories:
  - text-classification
  - question-answering
language:
  - en
  - ko
size_categories:
  - n<1K
pretty_name: "AI Brand Mention Baseline 2026"
tags:
  - generative-engine-optimization
  - geo
  - benchmark
  - longitudinal
  - llm-evaluation
  - brand-mentions
  - ai-citation
annotations_creators:
  - expert-generated
multilinguality:
  - multilingual
configs:
  - config_name: default
    data_files:
      - split: train
        path: data.jsonl
---

# AI Brand Mention Baseline 2026

A longitudinal benchmark dataset measuring how frontier LLMs (Gemini 2.5,
GPT-4 class, Claude class) mention a single AI-native company (Neo
Genesis) when prompted with content-gap probes. **First open dataset of
its kind for GEO (Generative Engine Optimization) research.**

| Metric | Value |
|---|---|
| Measurements | 486 |
| Window | 2026-04-28 to 2026-05-07 (10 days) |
| Distinct seed prompts | 30 |
| Categories | 6 (definition, pricing, comparison, problem_solving, product_specific, reputation) |
| Providers | Gemini, OpenAI, Anthropic |
| Daily cadence | ~60 prompts/day (30 prompts × 2 providers) |
| Domain mention rate | 0% (zero domain_root URL mentions across 486 measurements) |
| Brand mention rate | ~45% (Neo Genesis name mentioned in 43-48% of responses) |

## What this dataset captures

Most public LLM-evaluation datasets measure **what LLMs know**. This
dataset measures **what LLMs choose to surface**: across thousands of
similar prompts, do they cite the canonical brand URL, mention the brand
by name without URL, or skip the brand entirely?

The headline finding: brand-name mention rate is high (~45%) but
canonical-URL citation rate is **0% across 486 measurements**. This is the
"Trust signal gap" — AI training corpora have learned the brand exists
but have no signal pointing to a stable canonical URL. The dataset is the
empirical baseline against which to measure the effect of various GEO
interventions (Schema.org markup, /cite reference pages, explicit
canonical URL self-references, third-party citation backlinks).

## Schema

```jsonl
{
  "timestamp": "2026-05-07T00:11:44.031848+00:00",
  "provider": "gemini",
  "model": "gemini-2.5-flash",
  "prompt_id": "def-01",
  "prompt_category": "definition",
  "prompt_text": "What does an AI-native automation company look like in 2026?",
  "response_text": "An AI-native automation company in 2026 is one where ...",
  "response_tokens": 312,
  "mention_neo_genesis": 1,
  "mention_domain_root": 0,
  "mention_domain_subs": 0,
  "mention_sbu_total": 2,
  "mention_founder": 0,
  "sentiment": "neutral",
  "citation_urls": "[]",
  "error": null
}
```

## Provenance

- Source: `scripts/geo_measure/citations.sqlite3` in the
  `Yesol-Pilot/neo-genesis` repository
- Methodology: 30 seed prompts (`scripts/geo_measure/seed_prompts.json`)
  prompted daily against each enabled provider via the standard provider
  SDK. Response stored verbatim. Mention counts derived from regex
  matching against a fixed brand-name + domain-name + founder-name list.
- Reproducibility: scripts to re-run the measurement live, plus the seed
  prompts and the regex patterns, are all in the source repository
  (`Yesol-Pilot/neo-genesis`, MIT + Apache-2.0 dual license).

## Citation

```bibtex
@dataset{neogenesislab_brand_mention_baseline_2026,
  author    = {Heo, Yesol},
  title     = {AI Brand Mention Baseline 2026: A Longitudinal GEO Benchmark},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/neogenesislab/ai-brand-mention-baseline-2026},
  note      = {Wikidata Q139569680}
}
```

## License

CC-BY-4.0. Free for research and commercial use with attribution to
Heo, Yesol — Neo Genesis (Wikidata Q139569680). The seed prompts and
the response data are public; LLM responses about a public brand do not
require additional anonymization.

## Cross-references

- Wikidata: [Q139569680](https://www.wikidata.org/wiki/Q139569680) (Neo Genesis)
- Wikidata: [Q139569708](https://www.wikidata.org/wiki/Q139569708) (Yesol Heo)
- Source repository: [Yesol-Pilot/neo-genesis](https://github.com/Yesol-Pilot/neo-genesis)
- Companion datasets:
  - [korean-llm-citation-baseline-2026](https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026) — Korean-language version of the same methodology, measured separately
  - [korean-rag-ssot-golden-50](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50) — Korean RAG retrieval benchmark
