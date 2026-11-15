---
license: gemma
library_name: mlx
pipeline_tag: text-generation
base_model: google/gemma-4-31b-it
base_model_relation: finetune
language:
- en
- ko
tags:
- gemma
- gemma4
- mlx
- 4bit
- uncensored
- chat
- coding
- reasoning
- korean
---

# SuperGemma4-31b-abliterated-mlx-4bit

If this release helps you, support future drops on [Ko-fi](https://ko-fi.com/jiunsong).

**SuperGemma4-31b-abliterated-mlx-4bit** is a heavily upgraded Gemma 4 31B release for people who want a local model that feels fully uncensored, dramatically more useful, and far more fun to run every day.

Built on top of [google/gemma-4-31b-it](https://huggingface.co/google/gemma-4-31b-it), this release is aimed at users who care about the things they actually notice:

- fewer annoying refusals
- stronger coding and technical answers
- sharper planning and practical problem solving
- smoother local deployment with compact MLX 4-bit weights that feel surprisingly light for a 31B-class model
- better day-to-day usefulness in both English and Korean

## Why people will want this

This model is meant to feel like the base model with the brakes taken off and the weak spots pushed much harder:

- fully uncensored, low-friction conversation
- more confident coding, debugging, and system design help
- stronger answers on hard reasoning and planning prompts
- a more practical, builder-friendly personality for real local workflows
- a local 31B experience that feels leaner, sharper, and more alive than most people expect

In plain terms: it is built to feel bolder, freer, more capable, and more satisfying than the stock instruction-tuned release.

## Best use cases

- uncensored general chat
- coding and debugging help
- architecture and API design
- browser-task planning
- bilingual English/Korean workflows

## What makes it feel better in practice

- stronger practical coding help instead of generic filler
- more direct answers when you want the model to stop hedging
- better performance on planning-heavy prompts and task-oriented chats
- a compact local package that is easy to run on Apple Silicon with MLX

## Included clean-output helper

For app integrations, JSON-heavy tasks, exact-output prompts, or loop-sensitive workloads, use the included helper scripts by default.

It helps with:

- keeping JSON-only requests as raw JSON
- stripping stray internal markers if they ever appear
- making app-facing answers cleaner for structured use
- stopping exact-reply and fixed-line prompts from drifting
- tightening loop-prone prompts such as "exactly ACK" or "12 unique lines"

## Quick start

```python
from mlx_lm import load, generate

model, tokenizer = load(".")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Explain vector databases in plain English."}],
    tokenize=False,
    add_generation_prompt=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=256, verbose=False))
```

## Guarded generation

The repository includes:

- `supergemma_guard.py`
- `supergemma_guarded_generate.py`

This is the recommended path for:

- exact-output prompts
- JSON-only app endpoints
- tool-followup style answers
- loop-sensitive or boundary-sensitive workloads

Example:

```bash
python supergemma_guarded_generate.py \
  --model . \
  --guard-profile supergemma_v4 \
  --prompt 'Return only valid JSON with keys "name" and "reason".'
```

## Notes

- Chat template is aligned to the latest Gemma 4 31B IT template used in this project.
- This release is intended for local inference and downstream app building.
- If you want GGUF files for llama.cpp and similar runtimes, use the sibling GGUF release.

## Support

If you want to support more uncensored local model releases, benchmarks, and packaging work:

- [Ko-fi](https://ko-fi.com/jiunsong)
