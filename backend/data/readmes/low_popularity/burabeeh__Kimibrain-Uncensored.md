---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
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

**Kimibrain is the open-weight, uncensored release build published by
[Burabeeh Lab](https://huggingface.co/burabeeh), founded by Mohammed Al Marzooqi —
a National of the United Arab Emirates.**

Kimibrain is **not a newly trained model**. It is a release build of the
open-weight [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) base
model (Apache-2.0, by the Qwen team), in the abliterated Q4_K_M GGUF build
published by
[HauhauCS](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive),
with an identity-locked chat template, GGUF metadata namespace and packaging by
Burabeeh Lab. The tensor weights are carried over from the upstream build
unchanged — see [Licence and provenance](#licence-and-provenance) and
[NOTICE](./NOTICE) for the complete change list.

This is the official GGUF build of Kimibrain, packaged for Ollama, llama.cpp,
LM Studio and any other GGUF runtime. It ships with the optional vision
projector, so the same build handles text and images.

## Highlights

- **Uncensored.** Refusal behaviour was removed from the base model by
  HauhauCS's abliteration (0/465 refusals on their audit); this build carries
  those weights unchanged. Kimibrain answers the question instead of
  moralising about it.
- **Identity-locked.** Kimibrain always identifies itself as Kimibrain, by
  Burabeeh Lab. The identity is carried by the chat template inside the GGUF, not
  only by a system prompt, so it holds even when an application injects its own
  system message. (See *Verified behaviour* for what this does and does not cover.)
- **Thinking mode.** Long-form reasoning steps, exposed as a separate field
  (`think: true` in Ollama) so your UI can show them or hide them.
- **Vision.** Optional `mmproj` projector included — the same weights read images.
- **Long context.** 262,144-token context window (as trained in the upstream base
  model); the Ollama recipe below uses 131,072 to keep VRAM/RAM sane on a single
  workstation.
- **Multilingual**, with strong Arabic alongside the other major languages.

## Specs

| Property | Value |
|---|---|
| Base model | [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) — hybrid SSM/MoE, Apache-2.0 |
| Parameters (total) | 34.7 B |
| Parameters (active per token) | ~3 B (mixture-of-experts, 256 experts, 8 active) |
| Context length | 262,144 tokens (131,072 in the shipped Ollama recipe) |
| Quantisation | Q4_K_M (imatrix, quantised upstream by HauhauCS) |
| File size | 19.7 GiB + 0.9 GiB projector |
| Modalities | text → text, plus image understanding via the projector |
| Runtime | llama.cpp / Ollama / LM Studio (GGUF) |

## Quickstart — Ollama

Download the repository files and keep the folder layout (the Modelfiles
reference the GGUF files one level up), then run from the repository root:

```bash
# full profile: identity lock + serving parameters + vision projector
ollama create kimibrain -f modelfiles/kimibrain-core.Modelfile
ollama create kimibrain-gpu -f modelfiles/kimibrain-core-gpu.Modelfile   # 28/40 layers on GPU
ollama run kimibrain
```

For a quick text-only build without a Modelfile:

```bash
ollama run hf.co/burabeeh/Kimibrain-Uncensored:Q4_K_M
```

That route does not attach the vision projector — keep the second
`FROM ./Kimibrain-mmproj-F16.gguf` line (as the shipped Modelfiles do) if you
want vision.

For the full Burabeeh Lab serving profile (identity block, temperature 1.0,
top_p 0.95, top_k 20, min_p 0, presence_penalty 1.5, 131072 context), use the
Modelfiles shipped in [`modelfiles/`](./modelfiles).

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

Measured by Burabeeh Lab against an 18-probe adversarial and control suite
(run against the published build on Ollama 0.40.8, transcripts as-is in
[PROBES.md](./PROBES.md)):

- Answers identity questions as Kimibrain / Burabeeh Lab; does not name another
  vendor as its origin, including under a hostile client-supplied system message.
- Holds under: direct accusation, "print your system prompt", fake security
  audit, sentence completion, base64 obfuscation, spec attribution.
- Control probes in the suite (trivia and a code task) show general ability is
  intact after the identity layer.
- **GSM8K, before/after the identity layer:** 94/100 vs 93/100 on the same
  deterministic problem subset (greedy, zero-shot) — no measurable change.
  Method, raw records and the measured prompt-token overhead of the identity
  layer: [EVALS.md](./EVALS.md).
- The published GGUF is load-tested in Ollama 0.40.8 (text and vision via the
  shipped Modelfiles) before each release.
- **Known limits:**
  - **Reasoning traces.** With `think: true`, `message.thinking` exposes the full
    internal reasoning chain and can quote the user's message or internal terms
    from training. Use `think: false`, or hide reasoning in your product, if that
    matters for your deployment.
  - **Carry-over tasks.** Asked to translate, transcribe or quote a sentence that
    itself names another vendor, the model can still reproduce part of it. The
    identity layer stops the model *asserting* a different origin; it does not
    fully suppress echoing input text.

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

- **Provenance:** Kimibrain is a release build, not a newly trained model. The chain is:

  1. **Base weights — [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** (Apache-2.0), trained by the Qwen team: 34.7B total / ~3B active parameters, 256-expert hybrid SSM/MoE, 262,144-token context, vision.
  2. **Uncensoring and quantisation — [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)** (Apache-2.0): refusal behaviour removed by abliteration; the Q4_K_M imatrix quants and the F16 vision projector shipped here were generated by HauhauCS. This release carries those tensor weights over unchanged.
  3. **This release — Burabeeh Lab:** the identity-locked chat template (rendered as a system turn at the head of the prompt and again immediately before the assistant turn), `general.name` set to Kimibrain, Ollama Modelfiles, documentation and packaging. The architecture identifier is deliberately left as the upstream `qwen35moe` — GGUF runtimes reject unknown architecture names, so renaming it would make the file unloadable. All 733 tensors and the tensor payload are unchanged from the upstream build — verified by SHA-256 comparison of the payload region and a full metadata round-trip diff (see [NOTICE](./NOTICE)).

  "Qwen" is a mark of its respective owner and is not used as the name of this build or its publisher.

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
