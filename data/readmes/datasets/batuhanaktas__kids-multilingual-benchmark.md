---
license: cc-by-4.0
task_categories:
  - text-generation
  - question-answering
language:
  - en
  - es
  - pt
  - fr
  - de
  - it
  - nl
  - pl
  - cs
  - ro
  - ru
  - uk
  - tr
  - ar
  - hi
  - te
  - id
  - vi
  - th
  - ja
  - ko
  - zh
  - sw
size_categories:
  - 1K<n<10K
tags:
  - children
  - safety
  - voice-assistants
  - llm-as-judge
  - multilingual
  - benchmark
pretty_name: TinyAya v2 — Multilingual Children's AI Benchmark
configs:
  - config_name: items
    data_files:
      - split: train
        path: benchmark/items.jsonl
  - config_name: responses
    data_files:
      - split: command_a
        path: responses/command-a-03-2025.jsonl
      - split: gemma_4_31b
        path: responses/google_gemma-4-31b-it.jsonl
      - split: aya_expanse_32b
        path: responses/c4ai-aya-expanse-32b.jsonl
      - split: tiny_aya
        path: responses/tiny-aya-modal.jsonl
  - config_name: scores
    data_files:
      - split: deepseek
        path: scores/*_by_deepseek_deepseek-v4-flash.jsonl
      - split: cohere_reasoning
        path: scores/*_by_cohere_command-a-reasoning-08-2025.jsonl
---

# TinyAya v2 — Multilingual Benchmark for Children's AI Companions

> 2,312 child–AI conversational prompts across 23 languages, evaluated against
> four models with five-judge LLM-as-judge validation.

📄 **Companion article**: see HF Articles by [@batuhanaktas](https://huggingface.co/batuhanaktas).
💻 **Code**: <https://github.com/aktasbatuhan/cohere-tiny-aya-for-kids>

## Dataset summary

This dataset contains:

- **`benchmark/items.jsonl`** — 2,312 benchmark items in 23 languages. Each item
  is a structured prompt designed to mimic a child (ages 4–8) talking to a
  voice AI assistant, paired with item-specific `must_pass_criteria`, three
  universal hard gates (safe / no-data-elicitation / age-appropriate-language),
  and four graded dimensions (helpfulness, empathy, engagement, accuracy)
  scored 1–5.
- **`responses/`** — generation outputs from four models on every item:
  - `command-a-03-2025.jsonl` (Cohere)
  - `c4ai-aya-expanse-32b.jsonl` (Cohere)
  - `google_gemma-4-31b-it.jsonl` (Google, via OpenRouter)
  - `tiny-aya-modal.jsonl` (Cohere TinyAya 3.3B, served on Modal — the model
    powering the on-device iOS app)
- **`scores/`** — judge scores for each (generation_model, judge) pair. The
  primary judge is DeepSeek V4 Flash with full coverage; partial-coverage judges
  (Cohere Command-A Reasoning, GPT-5.4, Gemini 3.1 Pro, Xiaomi MiMo V2 Omni) are
  included for inter-judge agreement analysis.
- **`review/`** — the 709-item language-balanced review CSV (31 items per
  language for 23 languages, judged by DeepSeek), the agreement-matrix CSVs in
  long and wide format, and PNG figures.

## Languages

23 languages, balanced to ≈30–31 items per language in the review split:

`ar, cs, de, en, es, fr, hi, id, it, ja, ko, nl, pl, pt, ro, ru, sw, te, th,
tr, uk, vi, zh`

## Categories

- general_child_conversation (253 in review split)
- safety_redirection (176)
- other / emergency (90)
- privacy_boundaries (73)
- creative_engagement (49)
- education_explanation (29)
- emotional_support (25)
- civic_or_political (14)

## Provenance

- **Foundation items** (221 audited English items, 246 with native English
  scraped) — distilled from anonymized real conversation logs of the
  [Octo Kids iOS app](https://apps.apple.com/gb/app/octo-kids-ai-stories-chat/id6752529953)
  (built by the dataset author). Real children, ages 4–8, talking to a voice
  AI. PII redacted on export. Cohere Command-A Reasoning
  (`command-a-reasoning-08-2025`) extracted child utterances, agent context,
  reference responses, and rubric criteria via structured JSON output. A
  separate audit pass dropped duplicates and rewrite-flagged ~200 items;
  221 survived clean.
- **Native scraped items** (54 items across 11 source languages, anchored in
  31 distinct real-world incidents) — collected via Firecrawl across news,
  parenting blogs, and Reddit. Items were extracted from raw web content by
  GPT-5.4 (via OpenRouter), with name anonymization (`[CHILD_NAME]`,
  `[PARENT_NAME]`).
- **Translated items** (2,037 across 22 non-English languages) — translated
  with Cohere `command-a-03-2025` in structured-output mode. v2 predates
  Cohere's `command-a-translate` release; v3 will rerun translations on the
  purpose-built model.

Two known bugs were caught and fixed during a 50-item human spot-check:
1. 321 items had empty `child_utterance` (pipeline failed to extract child speech
   from third-person scenario descriptions) — re-extracted via Cohere Command-A
   and re-generated all four models' responses.
2. 66 items had `must_pass_criteria` in the wrong language (Portuguese / Turkish
   leaks across 6 unique strings × 22 languages) — patched.

Both bugs are documented in the companion article.

## Methodology

LLM-as-judge with five panellists. Headline judge is DeepSeek V4 Flash (full
coverage, 99.6% JSON parse rate). Validation panel: Cohere Command-A Reasoning,
Gemini 3.1 Pro, GPT-5.4, Xiaomi MiMo V2 Omni (partial coverage).

Pairwise agreement (Cohen's κ on `overall_pass`):

| Pair | n | κ | class |
|---|---:|---:|---|
| DeepSeek / Gemini | 2,257 | 0.71 | substantial |
| DeepSeek / Mimo | 1,064 | 0.71 | substantial |
| DeepSeek / Cohere | 984 | 0.66 | substantial |
| GPT-5.4 / others | varies | 0.30–0.49 | fair to moderate |

GPT-5.4 was found to be a systematic outlier — see the article for the full
agreement matrix and per-language breakdown. Best 3-judge Fleiss' κ:
DeepSeek + Gemini + Mimo at 0.72 (substantial), n = 1,033.

## Limitations (v2)

- The headline multilingual leaderboard is judged only by DeepSeek (budget
  constraint). Multi-judge validation is real but English-heavy.
- No human gold scores yet. A Label Studio annotation Space exists at
  [`batuhanaktas/tinyaya-bench-review`](https://huggingface.co/spaces/batuhanaktas/tinyaya-bench-review)
  with 9,248 review tasks ready for human annotation.
- Native-speaker validation per language is not yet complete.
- Single-turn only; no multi-turn dialogues.
- Static snapshot of April 2026 models.

See the companion article for the full Future Work section.

## Credits

Completed under **Cohere's Tiny Aya Expedition cohort** with model and compute
support from Cohere. Methodology and analysis are independent.

## Citation

```bibtex
@misc{aktas2026tinyaya,
  author       = {Aktas, Batuhan},
  title        = {TinyAya v2: A Multilingual Benchmark for Children's AI
                   Companions},
  year         = {2026},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/batuhanaktas/kids-multilingual-benchmark}
}
```

## License

CC-BY-4.0 for the dataset; MIT for the code repository.
