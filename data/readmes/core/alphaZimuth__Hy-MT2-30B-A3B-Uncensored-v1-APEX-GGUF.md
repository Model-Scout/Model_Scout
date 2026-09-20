---
license: apache-2.0
tags:
- gguf
- moe
- llama.cpp
- hy_v3
- quantized
- translation
- uncensored
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
---

# Hy-MT2-30B-A3B-Uncensored-v1-APEX

An experimental **Uncensored / Abliteration** version of Tencent [Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B) .

This repository provides three APEX quantization variants optimized for different deployment scenarios, quantized by **alphaZimuth**.

This project applies **Directional / Orthogonal Ablation** to the original BF16 model in an attempt to reduce refusal behavior while preserving its multilingual translation capabilities.

This is an **experimental community release** and has not undergone extensive or rigorous testing.

> ⚠️ **Experimental**
>
> The current release has only received limited internal testing. There may still be undiscovered translation regressions, language-specific issues, or other unexpected behavior.
>
> Users are encouraged to try the model themselves and report problems through **Issues**.

**Public Version: v1**

---

# Changelog

### 2026-09-11

- Initial public release of **Hy-MT2-30B-A3B Uncensored v1**
- Applied directional / orthogonal weight ablation to the original BF16 model
- Used multilingual refusal directions for weight editing
- Released three APEX quantization tiers: **Mini / Compact / Quality**
- Performed preliminary translation-retention and refusal-behavior testing

---

# Quantized Versions

Three APEX quantization tiers are currently available:

| File | Size | Description |
| :--- | ---: | :--- |
| `Hy-MT2-30B-A3B-Uncensored-v1-APEX-Mini.gguf` | 10.8 GB | Smaller model size, suitable for systems with limited memory |
| `Hy-MT2-30B-A3B-Uncensored-v1-APEX-Compact.gguf` | 13.2 GB | Balance between model size and quality |
| `Hy-MT2-30B-A3B-Uncensored-v1-APEX-Quality.gguf` | 17.8 GB | Higher precision, prioritizing model quality |

> **Note:** These quantizations have **not been calibrated with Imatrix**.

All three GGUF versions were produced from the Uncensored BF16 model through GGUF conversion followed by APEX quantization.

---

# Quantization Details

This project uses **APEX quantization**.

Project: [LocalAI / APEX](https://github.com/localai-org/apex-quant)

The conversion pipeline is:

```text
Tencent Hy-MT2-30B-A3B
            ↓
Directional / Orthogonal Ablation
            ↓
Hy-MT2-30B-A3B Uncensored
            ↓
GGUF Conversion
            ↓
Hy-MT2-30B-A3B-Uncensored-BF16.gguf
            ↓
APEX Quantization
            ↓
Mini / Compact / Quality
```


- **No Imatrix calibration was used**
- No `imatrix.dat` was used during quantization
- All three versions were directly quantized from the Uncensored BF16 model

---

# Uncensored Modification

This release uses **Directional / Orthogonal Ablation** for weight editing.

For a weight matrix `W` and a normalized refusal direction `r`:

```text
W' = W - c · r ⊗ (rᵀW)
```

where:

- `W` is the original weight
- `r` is a multilingual refusal direction
- `c` is the ablation coefficient
- `W'` is the edited weight

This release uses:

```text
Ablation coefficient: 1.0
Direction dimension: 2048
```

The editing operation is closed-form and requires no additional model training.

The computation is performed in FP32, while the original tensor dtype is preserved when writing the edited model back to BF16.

---

# Edited Weights

The following weights are modified.

### `lm_head`

```text
lm_head.weight
```

The last-layer refusal direction is used for the language-model head.

### Attention

Layers 12–45:

```text
model.layers.{12..45}.self_attn.o_proj.weight
```

### MoE Experts

All 128 experts in layers 12–45:

```text
model.layers.{12..45}.mlp.experts.{0..127}.down_proj.weight
```

Total edited tensors:

```text
lm_head × 1
o_proj × 34
expert down_proj × 4352

Total: 4387 tensors
```

---

# Preliminary Evaluation

The current tests are intended only as preliminary regression checks and are **not formal benchmarks**.

## Translation Retention

A small test set containing 56 simple translation samples was used to compare the modified model against the original model.

```text
Mean chrF: 0.9529
Mean BLEU: 0.6010
```

The approximately **95.3% chrF score is a retention measurement against the original model's own outputs**, rather than a human-reference translation benchmark.

It therefore should not be interpreted as:

- 95.3% translation accuracy
- 95.3% translation quality
- 95.3% of the original model's absolute capability

It indicates that, on this limited test set, the modified model's outputs remained relatively close to those of the original model.

Current per-language results:

| Language | chrF |
| --- | ---: |
| Korean | 1.000 |
| Chinese | 1.000 |
| Arabic | 0.974 |
| Spanish | 0.973 |
| English | 0.965 |
| French | 0.917 |
| Japanese | 0.842 |

The test set is small, so these results should be treated as indicative only.

The Japanese result was also affected by generation-length limitations in the current test setup and should not by itself be taken as definitive evidence of a major Japanese translation regression.

## Refusal Behavior

A separate preliminary test containing 119 prompts across 7 languages was used to evaluate refusal behavior.

```text
COMPLY: 119 / 119
REFUSE: 0 / 119
```

This means:

**119 / 119 = 100% COMPLY**

However, this should **not** be interpreted as proof that the model is completely uncensored.

The current evaluation:

- uses a limited sample set
- relies on simple keyword-based refusal detection
- checks only the first 120 characters of generated responses
- is not a formal safety benchmark

It only indicates that refusal behavior was substantially reduced in this particular test.

---

# llama.cpp Compatibility

Hy-MT2-30B-A3B uses the:

```text
hy_v3
```

architecture.

`hy_v3` has been merged into upstream llama.cpp. **b9993 or newer** is recommended.

Upstream PR:

https://github.com/ggml-org/llama.cpp/pull/25395

---

# Important Notes

This project is an **experimental weight-editing project**.

The current release has only received limited testing and should not be described as:

- a model validated by comprehensive safety benchmarks
- a model with completely unchanged translation quality
- an absolutely or universally "uncensored" model

This project uses a **custom Directional / Orthogonal Ablation implementation**.

The current public release is primarily intended for experimentation, local inference, translation testing, and comparison with the original model.

---

# Credits

- **Tencent Hunyuan Team** — Original Hy-MT2-30B-A3B model
- **LocalAI Team** — APEX quantization framework
- **llama.cpp Contributors** — GGUF and local inference support

---

# License

Apache-2.0
