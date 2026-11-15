---
base_model: mistralai/Mistral-Small-4-119B-2603
base_model_relation: quantized
quantized_by: AtomicChat
pipeline_tag: image-text-to-text
library_name: gguf
license: apache-2.0
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
tags:
- atomic-dynamic
- gguf
- llama.cpp
- mistral
- mistral4
- moe
- imatrix
- quantized
- conversational
- atomic-chat
---

# Mistral Small 4 119B · Atomic Dynamic GGUF
<p style="margin-top: 0; margin-bottom: 0;">
  <em><b>Atomic Dynamic</b> (AD) quants of Mistral AI's Mistral Small 4 (119B parameters, 6.5B active), built from Mistral's original weights for the 64 GB and 96 GB memory classes.</em>
</p>
<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_mistral_small_4_119b_2603&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
  <a href="https://x.com/atomic_chat_hq"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_x.png" width="108" alt="X"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>You can now run Mistral Small 4 in <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_mistral_small_4_119b_2603&utm_content=bullet_app">Atomic Chat</a>, with reasoning off by default and one switch to turn it on.</li>
  <li>Every file here was measured against the original weights on one stand, next to Unsloth's file of the same size.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

## Pick a file

`KL divergence` is how far the quantized model's predictions drift from the
original weights: lower is better, zero means identical. `top-1` is how often
it picks the same next token the original would have picked. Raw logs are in
[the metrics repo](https://huggingface.co/datasets/AtomicChat/Mistral-Small-4-119B-2603-GGUF-metrics).

| File | Size on disk | Made for | KL divergence | top-1 |
|---|---:|---|---:|---:|
| `Mistral-Small-4-119B-2603-AD-IQ3_XXS` (2 files) | 49.64 GB | 64 GB class | 0.1279 | 86.0% |
| `Mistral-Small-4-119B-2603-AD-IQ4_XS` (2 files) | 69.22 GB | 96 GB class | 0.0609 | 90.4% |

`AD-` marks an **Atomic Dynamic** layout; the rest of the name is the type of the
routed experts' gate and up projections, the largest tensor group. Compare files
by size on disk, not by name. The vision projector is shared by every file:
`mmproj-Mistral-Small-4-119B-2603-F16.gguf` (0.86 GB) or `-Q8_0` (0.47 GB).

## Against Unsloth at the same size

![KL divergence against size on disk, ours and Unsloth's](kld_vs_size.png)

| Memory class | Ours | KL divergence | top-1 | Unsloth | KL divergence | top-1 | KL divergence, ours vs theirs (95% CI) | top-1 | chunks where ours is lower |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|
| 64 GB class | `AD-IQ3_XXS` 49.64 GB | 0.1279 | 85.99% | `UD-Q3_K_S` 49.64 GB | 0.1336 | 85.74% | **-4.2%** (-8.0 to -1.1) | +0.25 pp | 58 of 86 |
| 96 GB class | `AD-IQ4_XS` 69.22 GB | 0.0609 | 90.44% | `UD-Q4_K_S` 69.47 GB | 0.0661 | 90.07% | **-7.8%** (-10.6 to -4.9) | +0.37 pp | 72 of 86 |

Each row compares two files of about the same size, measured with the same reference logits, text and build.
"Ours vs theirs" is the paired difference in mean KL divergence over the 86 chunks of the held-out text, with
a bootstrap interval over chunks.

We publish only files that beat the Unsloth file of their size. At the 128 GB size (Unsloth's `UD-Q5_K_XL`,
89.45 GB) our best try read 2.0% lower (95% CI -4.7 to +1.2), which is noise, so there is no file of that size
here. Even plain `Q8_0` (126 GB) reads KL divergence 0.041 and top-1 92.3% on this model:
above about 5 bits per weight the files differ little.

## What is different in these files

Every file keeps attention, the shared expert and the router side at `q8_0` and changes only the routed
experts, as Unsloth's files do. What differs:

- **The first blocks.** With 128 experts and 4 active, a small error early changes which experts every later
  block picks. Moving bytes to the blocks with the most activation energy (the last ones, by our importance
  matrix) changed nothing against Unsloth's choice of blocks (4, 28, 32, 35). Moving them to the first four did.
- **The importance matrix.** Ours is 3.8M tokens through this model's own chat template (Unsloth's files carry
  one of 102 chunks, by their metadata). On Unsloth's own tensor types it alone gave 4.2% lower KL divergence at
  the 50 GB size (95% CI -8.0 to -1.1) and 2.2% at 69 GB (within noise).

- `AD-IQ3_XXS` (49.64 GB): Unsloth's tensor types for this size, block for block (gate/up `iq3_xxs`, down
  `iq3_s` with `iq4_xs` on blocks 4, 28, 32 and 35, `token_embd` and `output` `q6_k`), with our importance matrix.
  At this size none of our six other layouts beat it: moving the `iq4_xs` blocks to the last blocks or to the
  first ones, raising the first blocks' gate/up, or the head at `q8_0` read the same or worse. 4.2% lower KL
  divergence than `UD-Q3_K_S`, lower in 58 of 86 chunks.
- `AD-IQ4_XS` (69.22 GB): gate/up `iq4_xs` instead of `q4_k`, which frees 2.4 GB; blocks 0-3 get gate/up `q5_k`
  and down `q6_k`, blocks 4-6 down `q6_k`, the rest down `q4_k`; `token_embd` `q8_0`, `output` `q6_k`.
  0.25 GB smaller than `UD-Q4_K_S`, 7.8% lower KL divergence, lower in 72 of 86 chunks.

## Running it

```bash
llama-server -m Mistral-Small-4-119B-2603-<FILE>-00001-of-00002.gguf \
  --mmproj mmproj-Mistral-Small-4-119B-2603-F16.gguf --jinja -ngl 99 -c 32768 --temp 0.1
```

Reasoning is off unless a request asks for it (the template takes `none` or `high`):

```bash
curl http://localhost:8080/v1/chat/completions -d '{"messages": [{"role": "user", "content": "..."}],
  "chat_template_kwargs": {"reasoning_effort": "high"}, "temperature": 0.7}'
```

Temperature 0.1 without reasoning and 0.7 with it are Mistral's recommended settings.
The chat template inside the files is Mistral's, with one change: the default
system prompt's `{today}` is filled with the current date.

Every published file passed the same behaviour check in `llama-server` (this build, `--jinja`, our projector):
answers in English and German with reasoning off, the reasoning switch (`high`: a thinking block, then the right
answer), a tool call with the right function and arguments, the colour of a shape in an image, and a number found
in the middle of a 32K-token prompt.

## How we measured

Reference: Mistral's FP8 checkpoint upcast to BF16 and run unquantized. We checked
Unsloth's BF16 GGUF against the FP8 checkpoint tensor by tensor (15 of 15 sampled
tensors bit-identical) and use it as the reference and as the input of our quants.
Held-out text: `eval_neutral` from our
[calibration dataset](https://huggingface.co/datasets/AtomicChat/calib-corpora)
(30 languages, 86 chunks of 4096 tokens), never used for calibration. Every file in
the comparison, ours and Unsloth's, ran with the same reference logits, text, context
and llama.cpp build (0893ec98) on one 8x A100-SXM4-40GB box. Differences are paired
by chunk with a bootstrap over the 87 chunks.

Our importance matrix: 3.8M tokens rendered through this model's own chat template
(agentic, code, reasoning with `[THINK]` blocks, 30+ languages, structured text and a
sweep of the whole vocabulary) at context 512, collected on the BF16 weights. (A second pass over
long documents at context 32768 crashed in llama-imatrix and is not in it.) It is `imatrix/imatrix.gguf` in the metrics
repo; the corpus is `builds/mistral-small-4-moe` in the calibration dataset.

## Model details

Mistral Small 4 (`mistral4` in llama.cpp): 36 layers, hidden size 4096, multi-head
latent attention, 128 routed experts (4 active) plus one shared expert in every
layer, vocabulary 131,072, untied output head, a Pixtral-style vision encoder.
Mistral gives 256K tokens of context; we measured at 4096. Support landed in
llama.cpp on 16 March 2026 (PR #20649).

## License

Mistral Small 4 is released by Mistral AI under the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) (copy in `LICENSE`).
Base model: [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603).

Quantized by AtomicChat.
