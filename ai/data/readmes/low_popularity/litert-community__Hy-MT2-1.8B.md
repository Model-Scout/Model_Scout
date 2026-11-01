---
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
tags:
  - litert
  - litert-lm
  - litertlm
  - on-device
  - edge
  - translation
  - hunyuan
  - multilingual
language:
  - zh
  - en
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - tl
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
pipeline_tag: translation
library_name: litert-lm
base_model_relation: quantized
---

Measured on device (edge-compat): Galaxy S26 · LiteRT-LM 0.16.0 · GPU · decode 20.8 tok/s · prefill 386 tok/s · TTFT 560 ms · all 1489 ops delegated (2026-09-05); Mac Studio M4 Max · LiteRT-LM 0.16.0 · GPU · decode 105.8 tok/s · prefill 2008 tok/s · TTFT 137 ms (2026-08-27); Galaxy S26 · LiteRT-LM 0.16.0 · CPU · decode 12.3 tok/s · prefill 126 tok/s · TTFT 1.64 s (2026-09-05). Record: https://github.com/john-rocky/edge-compat/blob/main/cards/hy-mt2-1.8b-int8/CARD.md

# Hy-MT2-1.8B — LiteRT-LM

[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) converted to the **LiteRT-LM** (`.litertlm`) format for on-device inference with Google's [LiteRT-LM](https://github.com/google-ai-edge/litert-lm) runtime. To our knowledge this is the first Hy-MT2 in LiteRT form — the Hub otherwise carries GGUF, MLX and FP8 conversions.

Hy-MT2-1.8B is Tencent's "fast-thinking" multilingual **translation model**: 33 languages, tuned to follow translation instructions rather than chat. It is a dense `hunyuan_v1_dense` stack — 32 layers, hidden 2048, 16 query / 4 KV heads (GQA) with QK-norm, head_dim 128, vocab 120,818, tied embeddings — 2.04B parameters.

| File | Recipe | Size |
|---|---|---|
| `Hy-MT2-1.8B_int8.litertlm` | export-time dynamic int8 (linears + embedding) | 1.82 GB |

## Correctness

All numbers below were measured on **this exact file** (litert-lm 0.16.0, Apple M4 Max).

- **Chat template is byte-equal to the source**: the embedded Jinja matches the repo's `chat_template.jinja` exactly (654 / 654 bytes).
- **8-question sanity gate: 6/8 on CPU and 6/8 on GPU**, non-degenerate, with the *same* two misses on both backends ("Cool" for the opposite of hot, "pink" for the rhyme) — a property of this translation-tuned 1.8B, not of a backend. Arithmetic, factual and translation items are all correct.
- **Translation greedy A/B vs the HF reference** (PyTorch bf16, greedy, the source README's default-translation prompt): byte-identical on 1 of 3 probes; the other two are fluent alternates of the usual int8-vs-bf16 kind (e.g. *spectaculaire* → *significative*). No degeneration on any probe.
- **No duplicate start token.** The source chat template renders `<|hy_begin_of_sentence|>` itself, and the LiteRT-LM engine *also* prepends the metadata `start_token` — measured inside the runtime: `[start_token]+prompt` and `[template BOS]+prompt` generate byte-identical greedy output, so the default export was feeding BOS twice. This bundle drops the metadata start token; the on-device token stream matches the training stream. Honest note: the double-BOS variant happened to score 8/8 on the sanity gate — the stream-faithful file ships anyway, because matching the training stream is the property that generalizes.
- **Stop token** is `<|hy_place_holder_no_2|>` (id 120020), as the source declares.

## Usage

Hy-MT2 expects translation instructions, not open chat. The source model card's default prompt works verbatim:

```bash
litert-lm run ./Hy-MT2-1.8B_int8.litertlm --prompt \
"Translate the following text into Japanese. Note that you should **only output the translated result without any additional explanation**:

The weather is nice today, so let's go for a walk in the park."

# GPU
litert-lm run ./Hy-MT2-1.8B_int8.litertlm --backend gpu --prompt "..."
```

The bundle carries the tokenizer and the stock Hy-MT2 chat template (`max_num_tokens` 4096).

## Performance

`litert-lm benchmark <file> -p 256 -d 256 --runs 3 --cache no`, litert-lm 0.16.0, Apple M4 Max. Two independent protocol runs per cell; the GPU cell was taken after a ≥300 s rest:

| Backend | Prefill (256) | Decode | TTFT |
|---|---|---|---|
| GPU | 2008 / 2003 tok/s | 105.8 / 105.4 tok/s | 0.137 s |
| CPU | 211.0 / 210.0 tok/s | 34.0 / 32.4 tok/s | 1.24 / 1.25 s |

Both backends were gated on real generations before benchmarking (a broken backend can still print benchmark numbers). GPU repeats within ~0.3%, CPU decode within ~5%.

## Conversion notes

Converted with stock [`litert-torch`](https://github.com/google-ai-edge/litert-torch) 0.9.3 through [hf-to-litertlm](https://github.com/john-rocky/hf-to-litertlm) — one command:

```bash
python scripts/convert.py tencent/Hy-MT2-1.8B
```

Two things route this family correctly, both measured:

- **The `dynamic`-with-`alpha` rope resolves statically.** transformers computes `base = rope_theta * alpha^(dim/(dim-2))` once at init and never rescales below `max_position_embeddings` — only the leftover data-dependent cache-growth branch kills `torch.export`. The converter bakes the resolved base (11,158,839.925) into `rope_theta` and drops `rope_scaling`; `inv_freq` and teacher-forced logits are **bitwise-equal** to the HF reference, valid to 262,144 positions (far past this bundle's 4,096 context).
- **The engine prepends the metadata start token unconditionally**, so a template that renders its own BOS must not also declare one — see Correctness above.

Export took 120 s on an M4 Max. See [`REPRODUCE.md`](https://github.com/john-rocky/hf-to-litertlm/blob/main/REPRODUCE.md) for the full measurement record behind every claim on this card.

## Raspberry Pi 5 (CPU)

Measured on a Raspberry Pi 5 Model B Rev 1.1 (8 GB, Raspberry Pi OS 64-bit) with [`litert-lm benchmark`](https://github.com/google-ai-edge/LiteRT-LM) 0.16.1: CPU backend, 4 threads, 256 prefill + 256 decode tokens, `--cache memory` (the compile cache lives and dies with the process, so every invocation compiles the model from scratch; nothing is reused between runs), one warm-up plus one timed iteration per invocation, 3 invocations per file with cooldown in between. Values are the median across invocations (min–max in parentheses). No thermal throttling occurred during these runs (`vcgencmd get_throttled` stayed `0x0`). Every file listed produced coherent text in a real generation on this backend before its numbers were recorded.

| File | Prefill (tok/s) | Decode (tok/s) | TTFT | Peak RSS |
|---|---:|---:|---:|---:|
| `Hy-MT2-1.8B_int8.litertlm` | 25.0 (24.9–25.8) | 2.7 (2.6–2.7) | 10.6 s | 2.9 GB |
