---
license: apache-2.0
library_name: llama.cpp
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-4B
base_model_relation: quantized
language:
- ko
- en
- es
- ja
- zh
- ru
- ar
- hi
- th
tags:
- gguf
- llama.cpp
- quantized
- conversational
- imatrix
- archsloth
- autoround
- kl-divergence
- multilingual
- korean
- code
- local-llm
- cpu
- on-device
- qwen3
- 4b
---

<p align="center">
  <img src="archsloth_hero.png" alt="ARCHSLOTH — the summit of quantization" width="820">
</p>

<p align="center">
  <b>Most quantized weights ship with an adjective. Ours ship with a table.</b>
</p>

<p align="center">
  <b>Head to head with <a href="https://huggingface.co/unsloth/Qwen3-4B-GGUF"><code>unsloth/Qwen3-4B-GGUF</code></a> at the identical
  2,497,280,800 bytes &mdash; KL divergence from bf16, lower is better:</b><br>
  Korean <b>&minus;54.4&#8201;%</b> &#183; Code <b>&minus;52.9&#8201;%</b> &#183;
  Japanese <b>&minus;33.7&#8201;%</b> &#183; English <b>&minus;33.2&#8201;%</b> &#183;
  Chinese <b>&minus;31.1&#8201;%</b> &#183; Spanish <b>&minus;30.2&#8201;%</b> &#183;
  Russian <b>&minus;25.0&#8201;%</b> &#183; Arabic <b>&minus;23.2&#8201;%</b> &#183;
  Thai <b>&minus;21.5&#8201;%</b> &#183; Hindi <b>&minus;20.9&#8201;%</b><br>
  <sub>Ten axes measured, ten ahead. Seven of them are not in our calibration set.</sub>
</p>

---

> ### 📚 Collection
> **▶ [Archsloth MODELs](https://huggingface.co/collections/Archsloth/archsloth-models)** — every build in the ARCHsloth Q4 grade
> [Qwen3-4B](https://huggingface.co/Archsloth/Qwen3-4B-GGUF) · [Qwen3.5-9B](https://huggingface.co/Archsloth/Qwen3.5-9B-GGUF) · [Qwen3.8-27B](https://huggingface.co/Archsloth/Qwen3.8-27B-GGUF)

# Qwen3-4B · ARCHsloth Q4 / Q6 / Q8

### **Same architecture. Same tensor layout. Same file size, to the byte. Only the rounding differs.**

> 🦥 **Try it live, no install →** [![CPU chat](https://img.shields.io/badge/🤗_Space-Qwen3--4B_CPU_chat-ffce3a)](https://huggingface.co/spaces/Archsloth/Qwen3-4B-CPU) — answering on a **CPU-only** box, no GPU.

[![License](https://img.shields.io/badge/License-Apache_2.0-0f6e56)](https://www.apache.org/licenses/LICENSE-2.0)
[![Runtime](https://img.shields.io/badge/runtime-stock_llama.cpp-eb6834)](https://github.com/ggml-org/llama.cpp)
[![Floor](https://img.shields.io/badge/floor-Q4-b8860b)]()
[![Base](https://img.shields.io/badge/base-Qwen3--4B-2a78d6)](https://huggingface.co/Qwen/Qwen3-4B)
[![Axes](https://img.shields.io/badge/measured-10_axes-4a3aa7)]()

---

## Which file do I want?

| File | Size | 4K ctx | 32K ctx | Pick it when |
|---|---|---|---|---|
| **`Qwen3-4B-AS-Q4_K_M.gguf`** ⭐ | 2.50 GB | **3,620 MiB** | 7,680 MiB | Default. The smallest file we ship. |
| `Qwen3-4B-AS-Q6_K.gguf` | 3.31 GB | **4,392 MiB** | 8,452 MiB | Closes the gap to bf16 a further 6×. |
| `Qwen3-4B-AS-Q8_0.gguf` | 4.28 GB | **5,322 MiB** | 9,382 MiB | Reference. See what quantization cost you. |

Those are **measured process allocations** (`llama-server -ngl 99`, single user), not file size
plus arithmetic. At 128K context add roughly 18 GB to any row — the cache decides whether a
long-context session fits, not the weights.

There is no Q5 file here. [Why not.](#what-we-did-not-win)

---

## `[measured]` Q4_K_M — ten axes, 2,497,280,800 bytes on both sides

<p align="center">
  <img src="chart_axes.svg" width="820" alt="KL divergence by language — ARCHsloth Q4 against unsloth Q4_K_M and UD-Q4_K_XL, ten axes">
</p>

KL divergence from the bf16 original. **Lower is better.** `llama-perplexity --kl-divergence`,
ctx 512, 60 chunks for Korean and English, 40 for the rest. Every ARCHsloth number below comes
from **one single build**.

| | script | **ARCHsloth Q4** | unsloth<br>`Q4_K_M` | unsloth<br>`UD-Q4_K_XL` | stock<br>`llama-quantize` | **vs unsloth**<br>same size |
|---|---|---|---|---|---|---|
| | file size | **2.4973 GB** | 2.4973 GB | 2.5463 GB | 2.4973 GB | — |
| Korean | Hangul | **0.024297** | 0.053290 | 0.046637 | 0.081506 | **−54.4 %** |
| English | Latin | **0.032344** | 0.048443 | 0.043660 | 0.066203 | **−33.2 %** |
| Spanish | Latin | **0.033679** | 0.048234 | 0.043093 | 0.069169 | **−30.2 %** |
| Japanese | Kana·Han | **0.034148** | 0.051534 | 0.045666 | 0.075946 | **−33.7 %** |
| Chinese | Han | **0.033088** | 0.048051 | 0.042510 | 0.073735 | **−31.1 %** |
| Russian | Cyrillic | **0.032852** | 0.043831 | 0.038792 | 0.065831 | **−25.0 %** |
| Arabic | Arabic | **0.040871** | 0.053212 | 0.047022 | 0.067085 | **−23.2 %** |
| Hindi | Devanagari | **0.031617** | 0.039979 | 0.035678 | 0.053405 | **−20.9 %** |
| Thai | Thai | **0.024561** | 0.031301 | 0.027782 | 0.045149 | **−21.5 %** |
| **Source code** | — | **0.010191** | 0.021659 | 0.018216 | 0.039165 | **−52.9 %** |

Ten axes, seven writing systems, ahead on every one — against the same-size file and against
the larger one. Lowest separation is 3.8 σ (Hindi); highest is 20.4 σ (Korean).

**Three of these axes are in our calibration set: Korean, English, code. The other seven are
not.** They are the control, so that a build which buys one language with another has somewhere
to show it.

### `[measured]` The whole curve, not one point

<p align="center">
  <img src="chart_frontier.svg" width="820" alt="File size against KL divergence — the ARCHsloth curve sits under the unsloth curve at every size">
</p>

Nine of those points are real files: six downloaded from
[`unsloth/Qwen3-4B-GGUF`](https://huggingface.co/unsloth/Qwen3-4B-GGUF), three built here. Nothing is interpolated.
Their curve includes the `UD-*-XL` files, which are **larger** than the same-named standard
file — and our curve is still below theirs. Read it vertically for "same size, closer to the
original"; read it horizontally for "same quality, smaller file".

### `[measured]` Q6_K and Q8_0

| | size | Korean | English |
|---|---|---|---|
| **ARCHsloth Q6_K** | 3.3063 GB | **0.004077** | **0.004022** |
| unsloth `Q6_K` | 3.3063 GB | 0.006969 | 0.005765 |
| | | **−41.5 %** | **−30.2 %** |
| **ARCHsloth Q8_0** | 4.2804 GB | **0.001624** | **0.001371** |
| unsloth `Q8_0` | 4.2804 GB | 0.001827 | 0.001502 |
| | | **−11.1 %** | **−8.7 %** |

Same-top-p and RMS Δp move the same direction on every row. Full statistics: [`EVAL.md`](EVAL.md).
Raw per-run logs: [`eval/logs/`](eval/logs).

---

## Quickstart

```bash
# any recent llama.cpp — brew / winget / apt, or LM Studio / Ollama / PocketPal
llama-cli -m Qwen3-4B-AS-Q4_K_M.gguf -p "안녕하세요" -ngl 0 -t 8

# OpenAI-compatible server
llama-server -m Qwen3-4B-AS-Q4_K_M.gguf --host 127.0.0.1 --port 8080 --jinja
```

No fork. No custom format. The layout is llama.cpp's own, which is the point.

---

## What is actually different

```
--scheme GGUF:Q4_K_M     optimize the rounding for the quantizer that is used at export
--enable_alg_ext         sign-gradient rounding search (SignRoundV2, arXiv:2512.04746)
--dataset cal_archsloth.jsonl
--iters 200  --nsamples 128  --seqlen 2048
```

Nothing else. Bit widths, tensor types and the per-layer layout are llama.cpp's standard
Q4_K_M / Q6_K / Q8_0 — **216 × Q4_K, 37 × Q6_K, 145 × F32, zero differences** from the
same-named stock file. Nothing below 4 bits anywhere.

That constraint is the point. **A quant that wins because it spent more bits is not a better
quant, it is a bigger one.**

### The calibration set — it ships in this repo

`cal_archsloth.jsonl`, 555 samples of exactly 9,000 characters each: Korean 44.9 %,
English 35.3 %, source code 19.8 %, **interleaved at the sample level**.

Interleaving is what mattered, not the ratio: moving to strict alternation with the same
character mix improved English by **11.4 %**. Adding code moved the code axis by **52.9 %** and
cost 3.4 % of Korean and 5.3 % of English, which is why it is in. Details: [`CALIBRATION.md`](CALIBRATION.md).

---

## What we did not win

- **Q5_K_M is not in this repository.** Our toolchain emits Q5_K with a 5–6 % deviation between
  the optimized weights and the packed tensor — every tensor, Q5_K only, on every model we
  tried. The resulting file scores **worse than our own Q4_K_M**. A file that gets worse when
  you give it more bits is a defect, not a result. It ships when that is fixed.
- **`[measured]` Speed is a tie.** pp512 12,167 vs 12,227 tok/s; tg128 306.0 vs 305.2 tok/s.
  One H100, three repetitions, alternating order. Same size and same layout, so a tie is the
  expected answer — we publish it because a number you omit is a number someone else produces.
- **Format compliance is not a ranking here.** 13 constrained-output items (7-item numbered
  lists, nested JSON, tool calls): bf16 13/13, ARCHsloth 12/13, the same-size comparison file
  11/13, stock 13/13. Zero language collapse, zero runaway repetition, zero empty outputs on
  any build. Thirteen items cannot rank four models; it can show that none of them broke.
- **`[pending]`** Long-context retrieval and agentic tool-use across bit widths. Not measured
  yet on this model. We publish only what we ran ourselves.

### Knobs that did not work, published so nobody spends the compute twice

| Knob | Result |
|---|---|
| 4× the calibration samples | no movement, 4× the cost |
| 4096-token samples instead of 2048 | Korean −2 %, English **+23 %** |
| Korean-only corpus | English **+14 %** |
| The tool's default English corpus | Korean **+76 %**, English **+9 %** |
| Quantization-aware healing on top of the rounding search | **+57 %** |
| Extra bits on selected tensors, on top of the rounding search | 0 σ to **+10 %** |
| Mixed precision at a matched size | a uniform bit increase was **10 % better** |

---

## Reproduce this

```bash
# 1. the comparison file, straight from its own repository
huggingface-cli download unsloth/Qwen3-4B-GGUF Qwen3-4B-Q4_K_M.gguf --local-dir rival

# 2. the reference the distance is measured from
python llama.cpp/convert_hf_to_gguf.py Qwen/Qwen3-4B --outtype bf16 --outfile ref-BF16.gguf

# 3. teacher logits, once per evaluation text
llama-perplexity -m ref-BF16.gguf -f eval/eval_ko.txt \
  --kl-divergence-base base_ko.dat -ngl 99 -c 512 --chunks 60

# 4. every candidate against the same teacher, same text, same chunks
llama-perplexity -m <candidate>.gguf -f eval/eval_ko.txt \
  --kl-divergence --kl-divergence-base base_ko.dat -ngl 99 -c 512 --chunks 60
```

`eval/` holds the ten evaluation texts and the per-run statistics. If a number here does not
replicate on your hardware, open a discussion and we will correct it.

---

## Lineage

| Component | Origin |
|---|---|
| Weights | **[Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)**, unmodified — quantized from the original, not from anyone else's quantization |
| Layout, bit widths, tensor types | llama.cpp standard `Q4_K_M` / `Q6_K` / `Q8_0`, unchanged |
| Runtime | upstream llama.cpp, unmodified |
| Rounding search | Intel **[AutoRound](https://github.com/intel/auto-round)** with `enable_alg_ext` (SignRoundV2) |
| **Calibration corpus, evaluation set, and the measurement** | **ours** — all three ship in this repo |

---

## License

Apache-2.0, inherited from the base model. Comparison files are named so you can fetch the
exact bytes we measured.
