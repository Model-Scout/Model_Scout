---
license: gemma
library_name: gguf
pipeline_tag: text-generation
base_model: google/gemma-4-31b-it
base_model_relation: finetune
language:
- en
- ko
tags:
- gemma
- gemma4
- gguf
- llama.cpp
- q4_k_m
- uncensored
- chat
- coding
- reasoning
---

# SuperGemma4-31b-abliterated-GGUF

If this release helps you, support future drops on [Ko-fi](https://ko-fi.com/jiunsong).

**SuperGemma4-31b-abliterated-GGUF** is the GGUF release of SuperGemma4-31b-abliterated, packaged for llama.cpp-compatible runtimes and built for people who want a fully uncensored, harder-hitting Gemma 4 31B experience on local hardware.

This release keeps the same product direction as the MLX version:

- fully uncensored chat with fewer brakes
- stronger coding and technical help
- sharper reasoning and planning
- better real-world usefulness for local users
- a surprisingly lightweight-feeling 31B deployment path for GGUF users

## What you get

- GGUF quantized weights for local deployment
- Gemma chat template alongside the model files
- a straightforward path for llama.cpp, LM Studio, and other GGUF tooling

## Why people will like it

This release was pushed toward the things end users notice immediately:

- much more open uncensored conversation
- stronger coding, debugging, and implementation help
- more useful answers on practical prompts instead of generic filler
- a local experience that feels sharper, more direct, and more builder-friendly
- a 31B release that feels leaner and punchier than the label suggests

In short: this is the Gemma 4 31B local drop for people who want fewer brakes, more capability, and a more addictive day-to-day experience.

## Recommended usage

Example with llama.cpp:

```bash
llama-cli -m SuperGemma4-31b-abliterated.Q4_K_M.gguf -p "Write a clean FastAPI CRUD example." -n 256
```

## Included clean-output helper

This release includes `supergemma_guard.py` and `supergemma_gguf_guarded_generate.py` for exact-output, JSON-only, and loop-sensitive workloads.

Example:

```bash
python supergemma_gguf_guarded_generate.py \
  --model SuperGemma4-31b-abliterated.Q4_K_M.gguf \
  --chat-template-file chat_template.jinja \
  --prompt 'Return only valid JSON with keys "title" and "steps".'
```

Recommended behaviors:

- require raw JSON for JSON-only endpoints
- strip stray internal markers before presenting answers
- keep structured-output prompts explicit and narrow
- use the guarded runner by default for exact replies, fixed-line outputs, and tool-followup style prompts

## Support

If you want to support more uncensored local model releases, benchmarks, and packaging work:

- [Ko-fi](https://ko-fi.com/jiunsong)
