---
language:
- en
- zh
- ja
- ko
- th
- vi
- ar
- ru
- es
- fr
- de
- pt
- hi
- id
- tr
license: mit
tags:
- ling-lang
- code
- programming-language
- translation
- sft
- instruction-tuning
pretty_name: Ling-Lang Chat SFT Dataset
---

# Ling-Lang Chat SFT Dataset

Instruction-tuning data (chat/messages JSONL) for fine-tuning LLMs to help with the
[Ling programming language](https://ling-lang.org) — a multilingual systems
programming language with keyword aliases in 15 human languages, a Cranelift
JIT/AOT + tree-walking interpreter + bytecode VM, and a `ling-*` crate ecosystem.

Used to fine-tune [zai-org/GLM-4-32B-0414](https://huggingface.co/zai-org/GLM-4-32B-0414)
via QLoRA for [chat.ling-lang.org](https://chat.ling-lang.org).

## Categories

| File | Topic |
|---|---|
| `01_syntax.jsonl` | Core ling-lang syntax (`use`, `bind`, `fn`, `do`, no semicolons) |
| `02_crates.jsonl` | The `ling-*` crate ecosystem reference |
| `03_shell_contrast_and_workflow.jsonl` | Ling-lang vs. shell syntax, real CLI workflows |
| `04_translation.jsonl` | General + ling-lang-keyword translation |
| `05_disambiguation.jsonl` | Corrects the "ling-lang is a linguistics/NLP tool" misconception |
| `06_corrections.jsonl` | Hand-written corrections (import→use, let→bind, real keyword aliases) |
| `07_builtins.jsonl` | Complete verified builtin function reference, with negative training for hallucinated builtins |
| `08_multilingual_keywords.jsonl` | Complete 15-language keyword table, language-consistency guidance |
| `09_game_patterns.jsonl` | Real game-code idioms mined from LingForFun and soul-symphony-ling |
| `10_cli_build.jsonl` | Real `ling` CLI subcommands/flags and Cargo build features |

## Format

Each line is a JSON object: `{"messages": [{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]}`,
the standard OpenAI-style chat/messages SFT format consumed directly by `trl`'s `SFTTrainer`.

## Notes

Every fact in this dataset was verified against the authoritative Ling interpreter/compiler
source (lexer, parser, builtin dispatch table) rather than docs or marketing copy, specifically
to correct hallucinated syntax/builtins/keywords observed in earlier fine-tuning rounds.
