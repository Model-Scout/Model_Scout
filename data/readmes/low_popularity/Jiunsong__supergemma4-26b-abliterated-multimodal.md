---
license: gemma
base_model: google/gemma-4-26b-it
tags:
  - gemma4
  - transformers
  - bf16
  - multimodal
  - instruction-following
  - tool-use
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: transformers
---

# SuperGemma4-26b-abliterated-multimodal

BF16 Gemma 4 multimodal release with an April 18 stability refresh focused on truthfulness, exact JSON/tool-call formatting, long-context extraction, loop resistance, and cleaner prompt hygiene.

## April 18 Stability Refresh

- Synced the external `chat_template.jinja` and inline `tokenizer_config.json` template so local and hosted runtimes read the same prompt rules.
- Hardened false-premise handling so the model corrects bad assumptions instead of continuing under them.
- Tightened JSON-only and tool-call formatting so exact-key JSON and `execute_code` calls stay machine-parseable.
- Improved long-context sentinel extraction behavior for retrieval-style prompts.
- Reinforced identity and prompt-hygiene responses to avoid mixed-script glitches and hidden-tag leakage.

## Validation Snapshot

- Capability audit: 9 / 9 passed, 100.0%
- Reliability audit: 20 / 20 passed, 100.0%
- Server red-team: 10 / 13 passed on the local MLX OpenAI-compatible server
- Remaining server misses were 2 semantic checker mismatches on safe refusals and 1 text-only multimodal rejection mismatch, not a truthfulness or leak regression.

## Included Files

- Official Hugging Face-format BF16 weights
- `chat_template.jinja`
- `tool_chat_template.jinja` for Gemma 4 tool-calling setups
- `SERVING_NOTES.md` with Gemma 4 runtime notes for vLLM, SGLang, and MLX
- `BENCHMARK_SNAPSHOT.md` with the current validation summary

## Notes

- Checkpoint keys were aligned to the official Gemma 4 Hugging Face naming/layout for portable serving.
- `tokenizer_config.json` includes an inline `chat_template` for portability and should match `chat_template.jinja`.
- For multi-turn tool use on vLLM, use the dedicated `tool_chat_template.jinja` and Gemma 4 parser settings from `SERVING_NOTES.md`.
