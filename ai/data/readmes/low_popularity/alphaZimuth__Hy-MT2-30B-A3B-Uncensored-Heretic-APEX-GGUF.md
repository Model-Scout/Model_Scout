---
base_model:
- OS-Software/Hy-MT2-30B-A3B-uncensored-heretic
license: apache-2.0
tags:
- moe
- translation
- gguf
- mixture-of-experts
- llama.cpp
- hy_v3
- quantized
- imatrix
- uncensored
- heretic
- abliterated
- conversational
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


# Hy-MT2-30B-A3B-Uncensored-Heretic-APEX-GGUF

APEX GGUF quantizations of **OS-Software/Hy-MT2-30B-A3B-uncensored-heretic**, quantized by **alphaZimuth**.

This release is based directly on the existing uncensored / decensored model from **OS-Software**, rather than performing an additional uncensoring or weight-ablation process on the original Tencent model.

The source model was created from **Tencent Hy-MT2-30B-A3B** using **Heretic v1.4.0+custom**, with **Arbitrary-Rank Ablation (ARA)**, a LoRA adapter, and row-norm preservation.

No additional uncensoring, abliteration, or behavioral weight editing is performed prior to GGUF conversion and APEX quantization.

# Source Model

Source:

[OS-Software/Hy-MT2-30B-A3B-uncensored-heretic](https://huggingface.co/OS-Software/Hy-MT2-30B-A3B-uncensored-heretic)

Original base model:

[tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)

According to the source model authors, the decensored model was produced using:

- Heretic v1.4.0+custom
- Arbitrary-Rank Ablation (ARA)
- LoRA adapter
- Row-norm preservation
- Modified layers 18–28

The source repository should be considered the authoritative reference for the uncensoring methodology and evaluation.

---

# Upstream Evaluation

The following results were reported by **OS-Software** for the source `Hy-MT2-30B-A3B-uncensored-heretic` model:

| Metric | Uncensored Heretic | Original Hy-MT2 |
|---|---:|---:|
| Keywords / Refusal Test | **0 / 100** | 100 / 100 |
| KL Divergence | **0.0276** | 0 |

The upstream evaluation used a custom mixed-language dataset.

> **Note**
>
> These results belong to the original full-precision source model from OS-Software.
>
> They are included here for reference and should **not** be interpreted as an independent benchmark of the APEX GGUF quantizations.
>
> Quantization can introduce small behavioral or quality differences compared with the source model.

---

# Available Quantizations

Three **APEX-I** quantization tiers are currently available:

| File | Size | Description |
|---|---:|---|
| `Hy-MT2-30B-A3B-uncensored-heretic-APEX-I-Nano.gguf` | 11.5 GiB | Lightweight variant for lower-memory systems |
| `Hy-MT2-30B-A3B-uncensored-heretic-APEX-I-Compact.gguf` | 14.0 GiB | Recommended balance between model size and quality |
| `Hy-MT2-30B-A3B-uncensored-heretic-APEX-I-Quality.gguf` | 19.0 GiB | Higher-precision variant prioritizing model quality |

# Quantization Details

This repository uses **APEX quantization**, based on `llama.cpp`.

The APEX-I variants use importance-matrix-assisted quantization.

Conversion pipeline:

```text
OS-Software/Hy-MT2-30B-A3B-uncensored-heretic
                         ↓
              convert_hf_to_gguf.py
                         ↓
     Hy-MT2-30B-A3B-uncensored-heretic-BF16.gguf
                         ↓
                Imatrix Calibration
                         ↓
                 APEX Quantization
                         ↓
       APEX-I-Nano / Compact / Quality
```

## Imatrix Calibration

The APEX quantizations in this repository were generated using an **importance matrix (imatrix)** calibration pass.

The calibration run reported:

```text
Final estimate: PPL = 2.1640 +/- 0.00331
```

This value is the final perplexity estimate reported during the **imatrix calibration process** and is provided for reproducibility and reference.

Important distinction:

```text
Uncensoring / Heretic processing → OS-Software
GGUF conversion / Imatrix calibration / APEX quantization → alphaZimuth
```

No additional Heretic processing or abliteration is performed in this release.

---

# llama.cpp Compatibility

## Important

Hy-MT2-30B-A3B uses the `hy_v3` architecture.

Support for `hy_v3` has been merged into upstream `llama.cpp`.

Please use a recent version of `llama.cpp` for inference.

Older builds may fail to load the model or may not correctly support the architecture.

---

# Recommended Inference Parameters

The upstream Hy-MT2 documentation recommends the following parameters for the 30B-A3B model:

```json
{
  "temperature": 0.7,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_tokens": 4096
}
```

# About the Uncensored Version

This model has substantially reduced safety alignment compared with the original Hy-MT2 model.

As a result, it may be less likely to refuse certain requests, but it may also produce:

- inaccurate information
- harmful content
- biased content
- offensive content
- unexpected outputs

The uncensored behavior originates from the **OS-Software source model** and is not introduced by APEX quantization.

Users should treat model outputs as untrusted and independently verify important information.

This model is primarily intended for research, experimentation, translation research, alignment research, and local model experimentation.

Users are responsible for complying with applicable laws, regulations, licenses, and platform policies.

---

# Previous Experimental Version

The previous release:

[Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF](https://huggingface.co/alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF)

used a custom directional / orthogonal ablation pipeline created specifically for that release.

Because issues were reported with the experimental version, it is now considered a **legacy / experimental release**.

For new deployments, use:

**alphaZimuth/Hy-MT2-30B-A3B-Uncensored-Heretic-APEX-GGUF**

instead.

---

# Credits

Special thanks to:

- **Tencent Hy-MT2 team** for the original Hy-MT2-30B-A3B model.
- **OS-Software** for creating and evaluating the `Hy-MT2-30B-A3B-uncensored-heretic` model.
- **p-e-w** for the Heretic project.
- **LocalAI** for the APEX quantization framework.
- **llama.cpp contributors** for GGUF and `hy_v3` architecture support.
- The wider open-source LLM community.

APEX GGUF quantization by **alphaZimuth**.

---

# License

Apache-2.0

Please also review the license and usage terms of the original Tencent Hy-MT2 model and the OS-Software derivative model.

---

## Related Models

**Original APEX release**

[alphaZimuth/Hy-MT2-30B-A3B-APEX-GGUF](https://huggingface.co/alphaZimuth/Hy-MT2-30B-A3B-APEX-GGUF)

**Source uncensored model**

[OS-Software/Hy-MT2-30B-A3B-uncensored-heretic](https://huggingface.co/OS-Software/Hy-MT2-30B-A3B-uncensored-heretic)

**Previous experimental uncensored release**

[alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF](https://huggingface.co/alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF)