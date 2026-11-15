---
library_name: transformers
base_model: Jackrong/Kestrel-4B-Coder
base_model_relation: finetune
license: apache-2.0
license_link: https://huggingface.co/Jackrong/Kestrel-4B-Coder/blob/main/LICENSE
quantized_by: hUh63
language:
- en
- zh
- ko
- ja
- ru
- es
- fr
pipeline_tag: image-text-to-text
tags:
- qwen3_5
- unsloth
- coder
- code-generation
- tool-use
- function-calling
- agent
- mtp
- multi-token-prediction
- speculative-decoding
- gguf
- llama.cpp
- q4_k_m
- imatrix
- heretic
- heretic-2.0.0
- ara
- decensored
- uncensored
- abliterated
- vision
- multimodal
- conversational
---

# Kestrel-4B-Coder — Decensored with Heretic 2.0.0 · MTP · Q4_K_M GGUF

> **Unofficial community derivative.** Weights originate from
> [Jackrong/Kestrel-4B-Coder](https://huggingface.co/Jackrong/Kestrel-4B-Coder) by
> **Jackrong**, itself a fine-tune of [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)
> by the **Qwen team** (from [unsloth/Qwen3.5-4B](https://huggingface.co/unsloth/Qwen3.5-4B)).
> Decensoring used [Heretic](https://github.com/p-e-w/heretic) **v2.0.0** by
> **Philipp Emanuel Weidmann (p-e-w)**; its probe datasets come from
> [mlabonne](https://huggingface.co/mlabonne). Quantized and published by **hUh63**.

> [!WARNING]
> **This build deliberately weakens the source model's safety alignment.**
> It is a decensoring experiment for research/local use. Check your own legal and
> compliance boundary before using it. No standard benchmark (MMLU, GSM8K, …)
> was run; do not assume capability equals the aligned original.

## What is in this repository

| File | Size | Description |
| :-- | --: | :-- |
| `Kestrel-4B-Coder-heretic2-MTP-Q4_K_M.gguf` | 2,807,777,984 B (2.61 GiB) | Text GGUF, Q4_K_M, 441 tensors, **`block_count=33` / `nextn_predict_layers=1`** (built-in MTP head in the same file) |
| `mmproj-F16.gguf` | 672,423,776 B | F16 vision projector (multimodal models need a second file) |
| `README.md` | — | This model card |
| `LICENSE` | — | Apache-2.0, from the source model |
| `QUANTIZATION.md` | — | Measured, runnable reproduction recipe |
| `HERETIC_2_0_0_METHOD.md` | — | What actually ran (vs. the previous build) |
| `config.toml` | — | Pinned Heretic 2.0.0 run configuration |
| `heretic_study.json` | — | All 8 Optuna trials, baselines, Pareto front |
| `heretic_ara_report.json` | — | 14 changed tensors + SHA256 of 15 untouched MTP tensors |
| `calibration.txt`, `tensor_types.txt` | — | imatrix corpus and Q6_K override rule |
| `pipeline.sh`, `build_gguf_src.py`, `check_gguf.py` | — | Reproducible scripts |

**No `-md` / second draft model is needed.** The MTP (NextN) head is the 33rd
block inside the single GGUF, used with `--spec-type draft-mtp`.

## This build is a *real* Heretic 2.0.0 run

The previous build of this repository used a hand-written Heretic-*style*
projected-abliteration script. This build runs the actual
[`heretic-llm==2.0.0`](https://pypi.org/project/heretic-llm/2.0.0/) package
(GitHub tag `v2.0.0`, commit `0db5c31e`) with its stock
**ARA (Arbitrary-Rank Ablation)** modifier and **Optuna TPE** optimizer:

| | Baseline (aligned source) | Selected Heretic trial |
| :-- | :-- | :-- |
| Refusals (`KeywordRate`, `harmful_behaviors test[:16]`) | 16/16 | **0/16** |
| KL divergence (`harmless_alpaca test[:16]`) | 0 (by definition) | **0.0564** |

8 trials were co-optimized on both objectives. The Pareto front included a
trial with 15/16 refusals at KL 0.0115 and one with 0/16 at KL 13.05 (rejected —
too damaged). The exported model is the low-drift 0/16 trial
(`start_layer_index=15, end_layer_index=22, lora_rank=32`,
`preserve_row_magnitudes=true`). Runtime ≈ 30 min on 8 CPU cores, peak ≈ 12 GiB.

Exactly **14 weight matrices** in layers 15–21 were changed
(`o_proj` / `linear_attn.out_proj` / `mlp.down_proj`); per-tensor diff
statistics are in `heretic_ara_report.json`.

## MTP head: untouched *and* high precision

The source checkpoint has 15 `mtp.*` tensors (`mtp_num_hidden_layers=1`).
`transformers 5.20.2` does not map them into
`Qwen3_5ForConditionalGeneration.state_dict()`, so Heretic's export drops them —
the decensor never sees or modifies them. Before GGUF conversion they are
re-injected **byte-identical from the source shards** (each tensor's SHA256 is in
`heretic_ara_report.json`), then:

* the full `blk.32.*` layer (8 matrices) is quantized to **Q6_K** instead of
  Q4_K, with 7 norm tensors left F32 — ~30 MiB extra, keeping the draft head
  close to the trunk;
* `general.file_type = 15` (MOSTLY_Q4_K_M), 441 tensors, 5.17 BPW;
* imatrix computed with `--nextn` (`imatrix.n_layer_nextn = 1`, 32 `blk.32.*`
  stat entries) on a 779,147 B multilingual / math / code / agent corpus.

### Measured on this exact environment (8 CPU cores, no GPU)

`llama-server` build `b12323`, `-t 8 -c 1024`, greedy, 128 tokens, one prompt,
A/B with speculation off/on:

| | tok/s | Drafts | Accepted |
| :-- | --: | --: | --: |
| spec off | 13.89 | — | — |
| `--spec-type draft-mtp` (single file) | **14.2** | 131 | **83 (63.4%)** |

Speculative decoding is **verify-then-accept**: rejected drafts are discarded,
so the output distribution is unchanged (lossless). On a 4B model + pure CPU the
draft's own cost largely offsets the gain; the value here is *no second model,
one file, no quality loss*, not a large speedup.

## Usage

```bash
# text only, with built-in MTP speculation
llama-cli -m Kestrel-4B-Coder-heretic2-MTP-Q4_K_M.gguf \
  --spec-type draft-mtp --spec-draft-n-max 3 \
  -p "Write a Rust binary search" -n 256 -t 8 -c 4096

# multimodal (add the projector)
llama-mtmd-cli -m Kestrel-4B-Coder-heretic2-MTP-Q4_K_M.gguf \
  --mmproj mmproj-F16.gguf --image photo.jpg -p "Describe this image" -t 8
```

Verified with llama.cpp `93cf736a` (build `b12323`), CPU build, AVX-512.
No CUDA/ROCm/Vulkan build was tested.

## Reproducibility & honesty

* `QUANTIZATION.md` is the full measured recipe: environment, exact commands,
  pitfall notes (`parse_tensor_type_file` ignores `#` comments;
  `general.file_type` vs tensor `gt` are different enums; 512/32 imatrix chunks
  thrash 16 GiB, 256/16 works).
* **Quantization is lossy.** imatrix + Q6_K MTP mitigate it; they don't remove it.
* **Heretic defaults were scaled down** for 8 CPU cores (8 trials, 48 prompts,
  32-token generations instead of 100/400/100). More trials would likely find a
  better Pareto point; this is what actually ran.
* **Speculative decoding is lossless**; decensoring and Q4_K_M quantization are not.
* No benchmark scores are claimed.
* Heretic itself is AGPL-3.0-or-later (tooling); the distributed weights inherit
  the source model's Apache-2.0. The previous build's method documents are
  preserved in the CNB repository that accompanies this model.

## Author chain

Qwen team → Unsloth → **Jackrong** (Kestrel-4B-Coder, Apache-2.0) →
**p-e-w / Heretic 2.0.0** (ARA decensor, AGPL-3.0 tooling) →
**mlabonne** (probe datasets) → **hUh63** (imatrix, GGUF conversion, Q4_K_M
quantization, MTP precision override, publishing).
