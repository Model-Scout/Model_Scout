---
license: apache-2.0
library_name: llama.cpp
pipeline_tag: image-text-to-text
base_model:
- Qwen/Qwen3.5-9B
base_model_relation: quantized
language:
- ko
- en
tags:
- gguf
- llama.cpp
- quantized
- conversational
- multimodal
- vision-language
- archsloth
- autoround
- kl-divergence
- korean
- multilingual
- local-llm
- cpu
- on-device
- qwen3_5
- 9b
---

<p align="center">
  <img src="archsloth_hero.png" alt="ARCHSLOTH — the summit of quantization" width="820">
</p>

<p align="center">
  <b>Most quantized weights ship with an adjective. Ours ship with a table.</b>
</p>

<p align="center">
  <b>Head to head with <a href="https://huggingface.co/unsloth/Qwen3.5-9B-GGUF"><code>unsloth/Qwen3.5-9B-GGUF</code></a>,
  same <code>Q4_K_M</code> rung &mdash; KL divergence from bf16, lower is better:</b><br>
  Korean <b>&minus;25.4&#8201;%</b> &#183; English <b>&minus;11.4&#8201;%</b><br>
  <sub>Two axes measured, two ahead. What we did not win is further down, with its number.</sub>
</p>

---

> ### 📚 Collection
> **▶ [Archsloth MODELs](https://huggingface.co/collections/Archsloth/archsloth-models)** — every build in the ARCHsloth Q4 grade
> [Qwen3-4B](https://huggingface.co/Archsloth/Qwen3-4B-GGUF) · [Qwen3.5-9B](https://huggingface.co/Archsloth/Qwen3.5-9B-GGUF) · [Qwen3.8-27B](https://huggingface.co/Archsloth/Qwen3.8-27B-GGUF)

# Qwen3.5-9B · ARCHsloth Q4

### **Same rung. Same tensor types. Only the rounding differs.**

[![License](https://img.shields.io/badge/License-Apache_2.0-0f6e56)](https://www.apache.org/licenses/LICENSE-2.0)
[![Runtime](https://img.shields.io/badge/runtime-stock_llama.cpp-eb6834)](https://github.com/ggml-org/llama.cpp)
[![Floor](https://img.shields.io/badge/floor-Q4-b8860b)]()
[![Base](https://img.shields.io/badge/base-Qwen3.5--9B-2a78d6)](https://huggingface.co/Qwen/Qwen3.5-9B)
[![Vision](https://img.shields.io/badge/vision-mmproj_included-4a3aa7)]()

---

## Which file do I want?

| File | Size | What it is |
|---|---|---|
| **`Qwen3.5-9B-AS-Q4_K_M.gguf`** ⭐ | 5.78 GB | The weights. This is the model. |
| `mmproj-F32.gguf` | 1.82 GB | The vision tower. **Only needed if you want the model to see images.** |

Qwen3.5-9B is a vision-language model. Text-only chat needs the first file alone; pass
`--mmproj mmproj-F32.gguf` to `llama-server` to turn the eyes on. The vision tower is **not**
quantized — it is carried at full precision, exactly as the base model shipped it.

---

## `[measured]` Q4_K_M — the same rung, both sides

KL divergence from the bf16 original. **Lower is better.** `llama-perplexity --kl-divergence`,
ctx 512, 60 chunks, held-out Korean and English text that is not in the calibration set.

<p align="center"><img src="chart_axes.svg" alt="KL divergence, ARCHsloth against unsloth, Korean and English" width="820"></p>

| | bytes | Korean | English |
|---|---:|---:|---:|
| **ARCHsloth `Q4_K_M`** | **5,780,090,240** | **0.019255** | **0.019237** |
| unsloth `Q4_K_M` | 5,680,522,464 | 0.025821 | 0.021718 |
| unsloth `UD-Q4_K_XL` | 5,966,095,584 | 0.013740 | 0.012546 |
| stock `llama-quantize` | 5,780,090,304 | 0.043475 | 0.037879 |

| Against | Korean | English |
|---|---:|---:|
| unsloth `Q4_K_M` — same rung | **−25.4 %** | **−11.4 %** |
| stock `llama-quantize` | **−55.7 %** | **−49.2 %** |

Same-top-p moves the same direction on every row (93.974 % vs 92.784 % on Korean).
Full statistics: [`EVAL.md`](EVAL.md). Raw per-run logs: [`eval/logs/`](eval/logs).

---

## Quickstart

```bash
# text only
llama-cli -m Qwen3.5-9B-AS-Q4_K_M.gguf -p "안녕하세요" -ngl 0 -t 8

# OpenAI-compatible server, with vision
llama-server -m Qwen3.5-9B-AS-Q4_K_M.gguf --mmproj mmproj-F32.gguf \
  --host 127.0.0.1 --port 8080 --jinja
```

No fork. No custom format. The layout is llama.cpp's own, which is the point.

---

## What is actually different

```
--scheme GGUF:Q4_K_M     optimize the rounding for the quantizer that is used at export
--enable_alg_ext         sign-gradient rounding search (SignRoundV2, arXiv:2512.04746)
--dataset cal_archsloth.jsonl
--iters 200  --nsamples 128
```

Nothing else. Bit widths and tensor types are llama.cpp's standard `Q4_K_M`. Nothing below
4 bits anywhere.

### The calibration set — it ships in this repo

`cal_archsloth.jsonl`, 200 samples of exactly 9,000 characters each, Korean and English
**interleaved at the sample level**. Interleaving is what mattered, not the ratio.

**This is the lever.** The same model built with an English-only corpus scored **0.027336** on
Korean — worse than the file we are comparing against. Same code, same flags, same bit widths;
only the calibration text changed, and it moved Korean by 29.6 %. That build is not in this
repository. Details: [`CALIBRATION.md`](CALIBRATION.md).

---

## What we did not win

- **`[measured]` unsloth's `UD-Q4_K_XL` is ahead of this file.** 0.013740 Korean and 0.012546
  English against our 0.019255 / 0.019237 — they are **40.1 %** and **53.3 %** better. It is a
  3.2 % larger file with a different tensor map, and on this model that map is worth more than
  our rounding search. We publish the row because a number you omit is a number someone else
  produces. Closing it is the open work on this model.
- **`[measured]` Two axes, not ten.** Korean and English are measured here. The ten-axis sweep
  that the [4B card](https://huggingface.co/Archsloth/Qwen3-4B-GGUF) carries has not been run
  on this model. We publish only what we ran ourselves.
- **`[pending]`** Q6_K and Q8_0 rungs, long-context retrieval, agentic tool use, and the vision
  axis. Not measured on this model.

---

## Reproduce this

```bash
# 1. the comparison file, straight from its own repository
hf download unsloth/Qwen3.5-9B-GGUF Qwen3.5-9B-Q4_K_M.gguf --local-dir rival

# 2. the reference the distance is measured from
python llama.cpp/convert_hf_to_gguf.py Qwen/Qwen3.5-9B --outtype bf16 --outfile ref-BF16.gguf

# 3. teacher logits, once per evaluation text
llama-perplexity -m ref-BF16.gguf -f eval/eval_ko.txt \
  --kl-divergence-base base_ko.dat -ngl 99 -c 512 --chunks 60

# 4. every candidate against the same teacher, same text, same chunks
llama-perplexity -m <candidate>.gguf -f eval/eval_ko.txt \
  --kl-divergence --kl-divergence-base base_ko.dat -ngl 99 -c 512 --chunks 60
```

If a number here does not replicate on your hardware, open a discussion and we will correct it.

---

## Lineage

| Component | Origin |
|---|---|
| Weights | **[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**, unmodified — quantized from the original, not from anyone else's quantization |
| Layout, bit widths, tensor types | llama.cpp standard `Q4_K_M`, unchanged |
| Vision tower | carried at full precision, not quantized |
| Runtime | upstream llama.cpp, unmodified |
| Rounding search | Intel **[AutoRound](https://github.com/intel/auto-round)** with `enable_alg_ext` (SignRoundV2) |
| **Calibration corpus, evaluation set, and the measurement** | **ours** — all three ship in this repo |

---

## License

Apache-2.0, inherited from the base model. Comparison files are named so you can fetch the
exact bytes we measured.
