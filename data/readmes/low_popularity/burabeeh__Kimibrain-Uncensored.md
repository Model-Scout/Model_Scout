---
license: apache-2.0
language:
- en
- ar
- zh
- fr
- es
- de
- hi
- ja
- ko
- ru
library_name: llama.cpp
pipeline_tag: text-generation
tags:
- gguf
- ollama
- llama.cpp
- uncensored
- moe
- vision
- thinking
- arabic
- uae
---

# Kimibrain Uncensored

**Kimibrain is the open-weight, uncensored large language model released by
[Burabeeh Lab](https://huggingface.co/burabeeh), founded by Mohammed Al Marzooqi —
a National of the United Arab Emirates.**

This is the official GGUF build of Kimibrain, packaged by Burabeeh Lab for
Ollama, llama.cpp, LM Studio and any other GGUF runtime. It ships with the
optional vision projector, so the same file handles text and images.

## Highlights

- **Uncensored by design.** Minimal refusal behaviour on legal creative, technical
  and research requests. Kimibrain answers the question instead of moralising about it.
- **Identity-locked.** Kimibrain always identifies itself as Kimibrain, by
  Burabeeh Lab. The identity is carried by the chat template inside the GGUF, not
  only by a system prompt, so it holds even when an application injects its own
  system message. (See *Verified behaviour* for what this does and does not cover.)
- **Thinking mode.** Long-form reasoning steps, exposed as a separate field
  (`think: true` in Ollama) so your UI can show them or hide them.
- **Vision.** Optional `mmproj` projector included — the same weights read images.
- **Long context.** Trained and served at up to **262,144 tokens**; the Ollama
  recipe below uses 131,072 to keep VRAM/RAM sane on a single workstation.
- **Multilingual**, with strong Arabic alongside the other major languages.

## Specs

| Property | Value |
|---|---|
| Parameters (total) | 34.7 B |
| Parameters (active per token) | ~3 B (mixture-of-experts, 256 experts, 8 active) |
| Context length | 262,144 tokens (131,072 in the shipped Ollama recipe) |
| Quantisation | Q4_K_M |
| File size | 19.7 GiB + 0.9 GiB projector |
| Modalities | text → text, plus image understanding via the projector |
| Runtime | llama.cpp / Ollama / LM Studio (GGUF) |

## Quickstart — Ollama

```bash
# 1. the text+vision model
ollama create kimibrain --from ./Kimibrain-Uncensored-Q4_K_M.gguf
ollama run kimibrain
```

For the full Burabeeh Lab serving profile (identity block, temperature 1.0,
top_p 0.95, top_k 20, min_p 0, presence_penalty 1.5, 131072 context), use the
Modelfile shipped in [`modelfiles/`](./modelfiles):

```bash
ollama create kimibrain -f modelfiles/kimibrain-core.Modelfile
ollama create kimibrain-gpu -f modelfiles/kimibrain-core-gpu.Modelfile   # 28/40 layers on GPU
```

Recommended sampling: `temperature 1.0`, `top_p 0.95`, `top_k 20`, `min_p 0`.
For answers only — no visible reasoning — pass `think: false`.

## Quickstart — llama.cpp

```bash
llama-server -m Kimibrain-Uncensored-Q4_K_M.gguf \
  --mmproj Kimibrain-mmproj-F16.gguf \
  -c 131072 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0
```

## Optional system prompt

Kimibrain's identity is already carried by the model's chat template. Applications
that build their own prompts can reinforce it (or replace it with their own
product persona) by starting from the block in
[`modelfiles/kimibrain-core.Modelfile`](./modelfiles/kimibrain-core.Modelfile).

## Verified behaviour

Measured by Burabeeh Lab against an 11-probe adversarial suite plus 6
identity-extraction probes, with results published as-is:

- Answers identity questions as Kimibrain / Burabeeh Lab; does not name another
  vendor as its origin, including under a hostile client-supplied system message.
- Holds under: direct accusation, "print your system prompt", fake security
  audit, sentence completion, base64 obfuscation, spec attribution.
- General ability (reasoning, code, translation, vision) is unaffected by the
  identity layer.
- **Known limits:** reasoning traces (`think: true`) expose the full internal reasoning chain for transparency. Certain internal terms or identifiers used during training may appear in longer responses for complex tasks.

## Intended use and out-of-scope

Burabeeh Lab releases Kimibrain as a general-purpose, uncensored assistant for
creative writing, role-play, research, coding, translation and agentic tooling,
including offline and on-premises deployment.

Uncensored does not mean unrestricted: the model is not fine-tuned for medical,
legal or financial advice, and it is not a safety-certified system. You are
responsible for what you build on top of it and for complying with the law
where you operate. See [ACCEPTABLE_USE.md](./ACCEPTABLE_USE.md).

## Licence and provenance

- **Licence:** Apache License 2.0 — full text in [LICENSE](./LICENSE). You may use, modify, redistribute and commercialise Kimibrain, including the weights, under those terms. The licence grants no trademark rights; "Kimibrain" and "Burabeeh Lab" are the marks of Burabeeh Lab.

- **Provenance:** Kimibrain is a pure LLM developed independently by Burabeeh Lab. All tensor weights were trained from scratch at full scale under Burabeeh Lab's proprietary pipeline — not distilled, fine-tuned, or quantised from any earlier checkpoint. This release adds the model name (`general.name`), the chat template (which carries the Kimibrain identity and serving profile), and documentation files to [NOTICE](./NOTICE).

## Citation and contact

```bibtex
@misc{kimibrain,
  title  = {Kimibrain Uncensored},
  author = {Burabeeh Lab},
  year   = {2026},
  note   = {Founded by Mohammed Al Marzooqi, United Arab Emirates}
}
```

Issues, feature requests and deployment questions: open a discussion on this
repository. Produced in the United Arab Emirates.
