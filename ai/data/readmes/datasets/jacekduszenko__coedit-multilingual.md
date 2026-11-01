---
license: apache-2.0
language: [en, de, es, fr, it, pt, nl, zh, ja, ko]
task_categories: [text2text-generation]
tags: [text-editing, grammatical-error-correction, paraphrase, multilingual, coedit, speech-transcript-editing]
pretty_name: CoEdIT Multilingual
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.parquet
      - split: validation
        path: data/validation.parquet
---

# CoEdIT Multilingual

A multilingual text-editing dataset for evaluating instruction-following edit models
(grammar correction, paraphrase, simplification, neutralization, coherence, clarity)
plus operational speech-transcript edits (translation, number/punctuation formatting,
filler removal, summarization, formalize/casualize, abbreviation expansion).

## Construction
- **English**: the original [grammarly/coedit](https://huggingface.co/datasets/grammarly/coedit) (train + validation).
- **Translated (de, es, fr, it, pt, nl, zh, ja, ko)**: CoEdIT examples translated with
  Gemini 2.5 Pro. For transformation tasks both source and reference are translated,
  preserving their before/after contrast. For **gec**, the correct reference is translated
  and a natural in-language grammatical error is re-introduced to form the source (so the
  task remains meaningful per language).
- **Operational tasks** (validation only): generated per language with Gemini 2.5 Pro.

## Fields
- `_id`, `task`, `lang`, `src` (`"<English instruction>: <text>"`), `tgt` (reference edit).

Instructions are in English by design (testing in-language editing with English commands).

_Generated with Claude Code._
