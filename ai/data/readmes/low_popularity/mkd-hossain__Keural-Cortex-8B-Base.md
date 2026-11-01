---
license: apache-2.0
base_model: Qwen/Qwen3-8B-Base
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- continued-pretraining
- korean
- base-model
---

# Keural Cortex 8B — Base (final CPT checkpoint, 41B tokens)

Korean-focused continued pretraining (CPT) of
[`Qwen/Qwen3-8B-Base`](https://huggingface.co/Qwen/Qwen3-8B-Base), by
**MKD Co., Ltd.**

This is the **completed** main CPT run — the Phase 4 deliverable, 13,034 of
13,034 steps. It is a **base model**, not an instruction-tuned assistant.

| | |
|---|---|
| Parameters | 8.19 B |
| Tokens of continued pretraining | **41,001,418,752 (41.00 B)** |
| Steps | 13,034 / 13,034 — complete |
| Context length | 32,768 (native, unchanged from base) |
| Precision | bfloat16 |
| Completed | 2026-09-09 |

---

## ⚠️ Read this before using the model

**1. It is a base model.** `Qwen3-8B-Base` has no instruction following, no chat
format, no tool calling and no thinking mode, and continued pretraining adds none
of them. This model *continues text*; it does not reliably answer instructions.
Post-training (SFT/DPO) has **not** been performed.

A `chat_template.jinja` is present because it is inherited from the base
tokenizer — it does **not** mean the model is chat-tuned. If you drive the model
through that template it will *imitate* assistant phrasing ("As an AI language
model, I cannot…"), because `Qwen3-8B-Base` absorbed large quantities of
assistant-style text during its 36 T-token pretraining. That is imitation, not
instruction tuning, and it is easy to mistake for the real thing.

**2. This checkpoint has not been evaluated.** No benchmark numbers exist for it
yet. The only evaluation in this project is of a separate 3 B-token *pilot* run
(see below). Do not assume the pilot's results transfer.

**3. Benchmark decontamination has not been run.** N-gram overlap against MMLU,
GSM8K, KMMLU, HAE-RAE, KoBEST and others has not been checked. Treat any
benchmark number produced from this model as provisional until it is.

---

## Training

| Parameter | Value |
|---|---|
| Sequence length | 4,096 |
| Global batch | 3,145,728 tokens/step (4 micro × 4,096 × 4 GPU × 48 accum) |
| Peak learning rate | 1.0e-05 |
| Schedule | WSD — 1% warmup / 89% stable / 10% decay, min ratio 0.1 |
| Optimizer | AdamW, β=(0.9, 0.95), ε=1e-8, weight decay 0.1 |
| Gradient clipping | 1.0 (**never triggered** — max observed norm 0.48) |
| Parallelism | FSDP full shard, 4 × NVIDIA H200 |
| Precision | bf16 parameters, fp32 gradient reduction |
| Attention | FlashAttention-2 |
| Activation checkpointing | enabled |
| Wall clock | 18 days 10 hours — **single run, zero restarts** |
| Throughput | 25,766 tok/s (stdev 127, i.e. 0.5%) |
| MFU / HFU | 32.0% / 42.7% |

The learning rate is deliberately 1e-5 rather than a pretraining-scale 1e-4–3e-4:
CPT starts from a *converged* model, and a pretraining LR destroys existing
capability before teaching anything new. Evidence this worked: gradient norm never
exceeded 0.48 against a 1.0 clip threshold, no loss spikes across 13,034 steps,
and the pilot's English track improved rather than regressed.

### Training loss

1.890 (step 20) → 1.819 (final). Loss plateaued at ≈1.818 from roughly step
5,200 (16.4 B tokens) and did not improve materially over the remaining ~25 B
tokens; the WSD decay phase contributed +0.0007. Interpretation is open —
corpus saturation, a conservatively low LR, or both — and is untested because
intermediate checkpoints have not been evaluated.

Note also that **no held-out validation set was used**, so the reported loss
measures fit to the training corpus rather than generalization.

---

## Corpus

**38.784 B tokens** across **19 sources**, Qwen3-tokenized and packed into
4,096-token sequences. The run consumed 41.00 B tokens, i.e. **1.057 epochs** —
the final ~3% of training revisited already-seen data.

| Domain | Tokens | Share |
|---|---|---|
| **Korean** | 16.462 B | **42.45%** |
| English / other | 11.524 B | 29.71% |
| Code | 5.890 B | 15.19% |
| Science / math | 4.908 B | 12.66% |

The Korean share comes from three web-derived sources: `fineweb2_korean`
(10.791 B), `culturax_ko` (5.300 B) and `korean_webtext` (0.371 B). There is no
Korean books, encyclopedic or academic source in the corpus — relevant when
interpreting Korean knowledge results, since 97.7% of Korean tokens come from two
large web crawls.

Excluded on licensing grounds before training: **NamuWiki** (CC BY-NC-SA),
**Falcon-RefinedWeb**, and **arXiv** (mixed per-paper licensing).

---

## Evaluation

**This checkpoint: not evaluated.**

The numbers below are from the **3 B-token pilot** — a separate, earlier run
sharing the same recipe and manifest at 1/13.7 the token count — against
`Qwen3-8B-Base` on `lm-evaluation-harness` with identical settings. They are
included to show the recipe was validated before the main run, **not** as results
for this model.

| Track | Mean Δ vs Qwen3-8B-Base |
|---|---|
| Korean (KMMLU, HaeRae, KoBEST ×4) | +0.545 pt |
| English (MMLU, ARC-C, HellaSwag, WinoGrande) | +0.620 pt |

Gate criterion — *Korean up AND English within −0.5 pt* — passed.

**How to read that honestly.** KMMLU (+0.03, n=35,030) and HaeRae (+0.09) — the
two substantive Korean knowledge benchmarks — were **flat**. KoBEST BoolQ
contributes +5.91 while the other five Korean benchmarks sum to **−2.64**;
without BoolQ the Korean mean is negative (−0.528). BoolQ is a two-class task,
where a shift of that size is as consistent with calibration change as with
knowledge gain.

What the pilot established is the *negative* result — that the recipe does not
damage the model (English held and improved). It did **not** establish that
Korean capability improves by a useful margin.

---

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

m = "mkd-hossain/Keural-Cortex-8B-Base"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype="bfloat16", device_map="cuda")

# Base model: complete text, do not instruct.
out = model.generate(**tok("대한민국의 수도는", return_tensors="pt").to("cuda"), max_new_tokens=64)
print(tok.decode(out[0], skip_special_tokens=True))
```

### CPU inference

Quantized GGUF via llama.cpp is dramatically faster than eager `transformers` on
CPU. Measured on 2 × Xeon Platinum 8570 (AMX), 16 threads, on this project's
step-5000 checkpoint:

| Format | Size | Generation |
|---|---|---|
| **Q8_0** | 8.1 GiB | **17.6 tok/s** |
| Q4_K_M | 4.7 GiB | 15.7 tok/s |
| F16 | 15.3 GiB | 8.2 tok/s |
| PyTorch eager bf16 | 15.3 GiB | 0.43 tok/s |

Build llama.cpp with `-DGGML_NATIVE=ON` or the AMX/AVX512 kernels are not
compiled in. On AMX-INT8 hardware Q8_0 outperforms Q4_K_M despite being larger.

---

## Related artifacts

| Model | Tokens | Purpose |
|---|---|---|
| **this** | 41.00 B | final CPT checkpoint |
| [`Keural-Cortex-8B-step10000`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-step10000) | 31.46 B | intermediate (77%) |
| [`Keural-Cortex-8B-step5000`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-step5000) | 15.73 B | intermediate (38%) |
| [`Keural-Cortex-8B-pilot`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-pilot) | 3.00 B | recipe validation run |

Full audit record — configuration, training dynamics, corpus provenance,
evaluation, findings, and reproduction instructions — is published at
[github.com/MKD-CORP/Keural-Cortex-8B](https://github.com/MKD-CORP/Keural-Cortex-8B)
under `CPT_details/`.

## Roadmap

Phase 5 (context extension 32K → 64K via YaRN) and Phase 6 (post-training:
SFT then DPO) are planned but not yet performed. Tool calling and instruction
following require Phase 6.

## License

**Apache 2.0**, inherited from `Qwen/Qwen3-8B-Base`. This is a derivative work of
Qwen3-8B-Base by Alibaba Cloud; attribution is required.

## Intended use

Research, and as a base for further fine-tuning. **Not** suitable as a
user-facing assistant — it has no instruction tuning — and not a basis for
capability claims until evaluated and decontaminated.
