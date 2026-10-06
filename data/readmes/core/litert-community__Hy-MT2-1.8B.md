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

Measured on device (edge-compat): Galaxy S26 · LiteRT-LM prebuilt-adac974b · GPU · decode 27.4 tok/s · prefill 579 tok/s · TTFT 1.80 s · all 1518 ops delegated (2026-10-05); Mac Studio M4 Max · LiteRT-LM 0.17.1 · GPU · decode 150.7 tok/s · prefill 2332 tok/s · TTFT 116 ms · all 1518 ops delegated (2026-10-05); Galaxy S26 · LiteRT-LM prebuilt-adac974b · CPU · decode 14.4 tok/s · prefill 237 tok/s · TTFT 4.43 s (2026-10-05). Record: https://github.com/john-rocky/edge-compat/blob/main/cards/hy-mt2-1.8b-int8/CARD.md

# Hy-MT2-1.8B — LiteRT-LM

[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) converted to the **LiteRT-LM** (`.litertlm`) format for on-device inference with Google's [LiteRT-LM](https://github.com/google-ai-edge/litert-lm) runtime.

Hy-MT2-1.8B is Tencent's "fast-thinking" multilingual **translation model**: 33 languages, tuned to follow translation instructions rather than chat. It is a dense `hunyuan_v1_dense` stack — 32 layers, hidden 2048, 16 query / 4 KV heads (GQA) with QK-norm, head_dim 128, vocab 120,818, tied embeddings — 2.04B parameters.

| File | Recipe | Size |
|---|---|---|
| `Hy-MT2-1.8B_int8.litertlm` | export-time dynamic int8 (linears + embedding) | 1.83 GB |

2026-10-06: GPU graph rewrite. Only the prefill/decode graph of `Hy-MT2-1.8B_int8.litertlm` changed. Its two DYNAMIC_UPDATE_SLICE KV-cache writes per layer are now one STABLEHLO_COMPOSITE `odml.cache_update`. Its BATCH_MATMUL(adjY) attention products are now `odml.runtime_bmm`. A signature input `param_tensor` INT32[1,1,1,7] was added; the runtime fills start/end. A graph exported with litert-torch's `--apply_gpu_composites` has this same shape, and the previous file was exported without that flag. The attention mask is applied as an ADD on a [bk, g, T, C] view of the logits, with the FLOAT32 mask broadcast; the mask input stays FLOAT32. A 16-token prefill signature, `prefill_16`, was added as a copy of `prefill_128` that shares every weight buffer. Every other bundle section and the graph's weight region are byte-identical to the previous file (checked per section and per buffer). The new file is 1,827,026,224 bytes, sha256 `275ff52bf04c4d577e1bf48733daa77d873d78b0637841574d7a10e1560a011a`. The previous file was 1,815,622,960 bytes, sha256 `529e6d378df5869d89a5a08717c06604105a32d8a4dab4800175d6baabc4da50`. The checks compare three files: the previous file, an intermediate file with the rewrite but without `prefill_16`, and the new file. On the Mac GPU, answers are byte-identical from the previous file to the intermediate (8/8 questions) and from the intermediate to the new file (9/9 prompts), with fp32 activations and with the default fp16 activations alike. On the CPU, the new file's answers match the intermediate's byte for byte (9/9 prompts), and `prefill_16` gives bit-identical output to `prefill_128` on the same tokens (2/2 cases). On the Mac CPU without the weight cache, the new file takes longer to load and uses more memory; see Performance. The speed rows below ran both files in the same window, with the Mac protocol under Performance. The Raspberry Pi 5 rows further down were measured on the previous file.

| Mac Studio M4 Max, GPU, fp16 activations | previous file | new file |
|---|---:|---:|
| 8 questions, correct final answers | 6/8 | 6/8 |
| Prefill, 256-token prompt | 2014 tok/s | 2332 tok/s |
| Decode, 256 tokens | 103.5 tok/s | 150.7 tok/s |
| TTFT, 16-token prompt | 0.076 s | 0.031 s |

2026-09-21: chat template updated to accept the 0.18 content-parts form (string form unchanged); weights, tokenizer and executor metadata byte-identical.

## Correctness

All numbers below were measured on the previous file (litert-lm 0.16.0, Apple M4 Max). The 2026-10-06 note above lists the checks on the new file.

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

Measured on the new file (see the 2026-10-06 note).

### Apple M4 Max (macOS)

Mac Studio M4 Max, `litert-lm` 0.17.1 CLI, `benchmark --cache no`, 256 prompt and 256 decode tokens. GPU = WebGPU on Metal with fp16 activations, median of 3 processes. CPU = XNNPACK, median of 2 processes. The TTFT (16-token prompt) column comes from separate runs with a 16-token prompt and 32 decode tokens.

| Backend | Prefill (256) | Decode | TTFT | TTFT (16-token prompt) | Init |
|---|---:|---:|---:|---:|---:|
| GPU (WebGPU on Metal) | 2332 tok/s | 150.7 tok/s | 0.12 s | 0.031 s | 1.5 s |
| CPU (XNNPACK) | 207 tok/s | 31.9 tok/s | 1.27 s | 0.884 s | 5.3 s |

Without the XNNPACK weight cache (`--cache no`, as in this table), the new file repacks the weights for the extra signature on the CPU. At a 16-token prompt, init goes from 3.75 s to 5.3 s and peak footprint from 4.17 GB to 5.57 GB (file without `prefill_16` → new file). With the disk weight cache (the app default), init goes from 0.24 s to 0.32 s, footprint from 0.82 GB to 0.87 GB, and TTFT at 16 tokens from 0.33 s to 0.12 s.

### Galaxy S26 (Android)

Samsung Galaxy S26 (SM-S942Q, Android 16), `litert_lm_advanced_main` from a LiteRT-LM main build of 2026-09-18. GPU = OpenCL delegate with the bundle's default fp16 activations, cold init (`--disable_cache=true`), 3 iterations in one process. CPU = XNNPACK with 4 threads and the XNNPACK weight cache, 2 iterations in one process. Each range runs from the lowest to the highest iteration in one process; the first GPU iteration follows the cold init. Peak is the process high-water mark (VmHWM).

| Backend | Prompt / decode tokens | Prefill | Decode | TTFT | Init | Peak (VmHWM) |
|---|---|---:|---:|---:|---:|---:|
| GPU (OpenCL) | 1024 / 256 | 576.9–580.2 tok/s | 26.29–27.46 tok/s | 1.80–1.81 s | 4.94 s | 0.83 GB |
| GPU (OpenCL) | 16 / 32 | 317.7–364.2 tok/s | 20.1–26.04 tok/s | 0.08–0.10 s | 4.91 s | 0.83 GB |
| CPU (XNNPACK, 4 threads) | 1024 / 256 | 213.4–260.2 tok/s | 13.75–14.99 tok/s | 4.00–4.87 s | 3.72 s | 2.96 GB |

The OpenCL GPU delegate (`LITERT_CL`) takes every node of each transformer signature, in one partition each: `prefill_128` 1518/1518, `prefill_16` 1518/1518, `decode` 1390/1390. In the GPU gate on this phone, 3 of 5 prompts were answered correctly.

## Conversion notes

Converted with stock [`litert-torch`](https://github.com/google-ai-edge/litert-torch) 0.9.3 through [hf-to-litertlm](https://github.com/john-rocky/hf-to-litertlm) — one command:

```bash
python scripts/convert.py tencent/Hy-MT2-1.8B
```

Two things route this family correctly, both measured:

- **The `dynamic`-with-`alpha` rope resolves statically.** transformers computes `base = rope_theta * alpha^(dim/(dim-2))` once at init and never rescales below `max_position_embeddings` — only the leftover data-dependent cache-growth branch kills `torch.export`. The converter bakes the resolved base (11,158,839.925) into `rope_theta` and drops `rope_scaling`; `inv_freq` and teacher-forced logits are **bitwise-equal** to the HF reference, valid to 262,144 positions (far past this bundle's 4,096 context).
- **The engine prepends the metadata start token unconditionally**, so a template that renders its own BOS must not also declare one — see Correctness above.

Export took 120 s on an M4 Max. See [`REPRODUCE.md`](https://github.com/john-rocky/hf-to-litertlm/blob/main/REPRODUCE.md) for the full measurement record behind every claim on this card.

**Graph rewrite (2026-10-06).** The current file was made from the previous one (Hub revision `18cc1a6794d7`) with two tools in `tools/gpu_graph/` of [hf-to-litertlm](https://github.com/john-rocky/hf-to-litertlm). `gpu_graph_retrofit.py` makes the graph changes listed in the 2026-10-06 note; every original weight buffer keeps its bytes. `prefill_bucket_clone.py` copies an existing prefill signature (`prefill_128`) at a new length (16); the copy shares every weight buffer, and every existing subgraph and SignatureDef keeps its index and bytes.

```bash
python tools/gpu_graph/gpu_graph_retrofit.py previous.litertlm retrofit.litertlm --decomp exporter --mask add_bcast
python tools/gpu_graph/prefill_bucket_clone.py build retrofit.litertlm new.litertlm --lengths 16 --source prefill_128 --report bucket.json
```

`previous.litertlm` is the previous file, `new.litertlm` the result published here as `Hy-MT2-1.8B_int8.litertlm`; `LITERT_LM_CLI` names the `litert-lm` CLI the scripts use to unpack and pack the bundle.

A rebuild with these commands gives every bundle section byte-identical to this file (sha256 per section). Only the bundle header (uuid and timestamp written by `litert-lm pack`) differs, so the whole-file sha256 differs.

## Raspberry Pi 5 (CPU) (previous file)

Measured on the previous file (sha256 `529e6d378df5869d89a5a08717c06604105a32d8a4dab4800175d6baabc4da50`) and not re-measured after the 2026-10-06 graph rewrite; the weights are byte-identical and the new file's Mac CPU decode and prefill are ×0.992 and ×1.010 of the previous file's, so the throughput columns are expected to hold, while peak memory may differ (see the CPU note under Performance).

Measured on a Raspberry Pi 5 Model B Rev 1.1 (8 GB, Raspberry Pi OS 64-bit) with [`litert-lm benchmark`](https://github.com/google-ai-edge/LiteRT-LM) 0.16.1: CPU backend, 4 threads, 256 prefill + 256 decode tokens, `--cache memory` (the compile cache lives and dies with the process, so every invocation compiles the model from scratch; nothing is reused between runs), one warm-up plus one timed iteration per invocation, 3 invocations per file with cooldown in between. Values are the median across invocations (min–max in parentheses). No thermal throttling occurred during these runs (`vcgencmd get_throttled` stayed `0x0`). Every file listed produced coherent text in a real generation on this backend before its numbers were recorded.

| File | Prefill (tok/s) | Decode (tok/s) | TTFT | Peak RSS |
|---|---:|---:|---:|---:|
| `Hy-MT2-1.8B_int8.litertlm` | 25.0 (24.9–25.8) | 2.7 (2.6–2.7) | 10.6 s | 2.9 GB |
