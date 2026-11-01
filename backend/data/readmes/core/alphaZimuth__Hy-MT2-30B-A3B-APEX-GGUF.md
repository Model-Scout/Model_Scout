---
license: apache-2.0
tags:
- gguf
- moe
- llama.cpp
- hy_v3
- quantized
- translation
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

# Hy-MT2-30B-A3B-APEX-GGUF

GGUF quantizations of [Tencent Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B) using APEX quantization.

This repository provides three APEX quantization variants optimized for different deployment scenarios, quantized by **alphaZimuth**.

# Changelog

- **2026-7-14**  
  Initial APEX quantization release.

- **2026-7-15**  
  Fixed `hy_v3` architecture compatibility issue and added support for upstream llama.cpp b9993+.

- **2026-7-18**  
  Added APEX-I series with importance matrix calibration.
  Added Nano variant for lower memory devices.

- **2026-9-11**  
  Renamed the quantization files for a cleaner and more consistent naming scheme.

## Recommended Versions

The **APEX-I series** is the recommended version of this repository.

Compared with the original APEX quantizations, these models were calibrated with an importance matrix (`imatrix.dat`) generated from a multilingual translation-focused calibration dataset.

The calibration process achieved: **PPL = 2.1519 +/- 0.00207**

In practical testing, the Imatrix-calibrated versions consistently provide better translation quality and output stability compared with the non-calibrated versions.

The evaluation was conducted through parallel translation comparisons using the same test samples, with both calibrated and non-calibrated versions compared side by side.

Several advanced LLM-based evaluators, including GLM, DeepSeek, GPT, Qwen, and LongCat, were used to assess the translation results from multiple perspectives. Across these evaluations, the Imatrix-calibrated versions were consistently rated higher for translation accuracy, fluency, and overall output quality.

The original APEX series is kept for archival and comparison purposes.

## Available Quantizations

### Recommended: APEX-I Series

| File | Size | Description |
| :--- | ---: | :--- |
| `Hy-MT2-30B-A3B-APEX-I-Nano.gguf` | 11.5 GB | Lightweight variant for lower-memory devices while maintaining strong translation performance |
| `Hy-MT2-30B-A3B-APEX-I-Compact.gguf` | 14.0 GB | Optimized quality-to-size ratio, ideal for limited VRAM devices |
| `Hy-MT2-30B-A3B-APEX-I-Quality.gguf` | 19.0 GB | Quality-focused variant with higher precision retention |
| `Hy-MT2-30B-A3B-APEX-I-Balanced.gguf` | 20.8 GB | Balanced APEX tier for users prioritizing overall quality |

### Legacy: Original APEX Series

The following versions are preserved for archival purposes:

| File | Size | Description |
| :--- | ---: | :--- |
| `Hy-MT2-30B-A3B-APEX-Legacy-Compact.gguf` | 14.0 GB | Original non-imatrix quantization |
| `Hy-MT2-30B-A3B-APEX-Legacy-Quality.gguf` | 19.0 GB | Original non-imatrix quantization |
| `Hy-MT2-30B-A3B-APEX-Legacy-Balanced.gguf` | 20.8 GB | Original non-imatrix quantization |

## Quantization Details

Quantized with **APEX (based on llama.cpp)**.

Project: https://github.com/localai-org/apex-quant

Conversion pipeline:

    Tencent Hy-MT2-30B-A3B (BF16)
            ↓
    convert_hf_to_gguf.py (hy3-port branch)
            ↓
    Hy-MT2-30B-A3B-BF16.gguf
            ↓
    APEX quantization (with imatrix)
            ↓
    APEX GGUF files

Note:

-   These quantizations were generated with imatrix calibration.
-   The filenames follow APEX tier naming.

## llama.cpp Compatibility

### Important

Hy-MT2-30B-A3B uses the `hy_v3` architecture.

Support for `hy_v3` has been merged into upstream llama.cpp starting from build **b9993**.

Please use llama.cpp build **b9993 or later** for inference.

Related upstream PR:

https://github.com/ggml-org/llama.cpp/pull/25395

## Usage

Example:

``` bash
llama-cli \
-m Hy-MT2-30B-A3B-APEX-I-Compact.gguf \
-p "Translate the following sentence into Chinese: Hello world"
```

## Benchmark

### Test Environment

-   CPU: Intel Core i7-12700H
-   GPU: NVIDIA RTX 3060 Laptop GPU 12GB
-   RAM: 24GB

Software:

-   llama.cpp build: b10056
-   CUDA backend

Settings:

    -ngl 99
    -b 2048
    -ub 2048
    -t 12

Optimized `--n-cpu-moe` values on RTX3060 12GB were used for each quantization.

| Quantization | Size | n_cpu_moe | PP512 | TG128 |
| :--- | ---: | ---: | ---: | ---: |
| `APEX-I-Nano` | 11.59 GiB | 4 | 1224.25 tok/s | 71.92 tok/s |
| `APEX-I-Compact` | 14.00 GiB | 13 | 835.57 tok/s | 56.16 tok/s |
| `APEX-I-Quality` | 19.05 GiB | 25 | 520.03 tok/s | 33.49 tok/s |
| `APEX-I-Balanced` | 20.81 GiB | 26 | 463.11 tok/s | 28.93 tok/s |

# 🚀 Experimental Speculative Decoding Draft Model

For users with sufficient VRAM, an experimental draft model based on **Hy-MT2-1.8B** is available:

👉 **Hy-MT2-1.8B-SpecDraft-30B**

This project modifies the original Hy-MT2-1.8B model to work as a **speculative decoding draft model** for Hy-MT2-30B-A3B.

Features:

- Vocabulary alignment between Hy-MT2-1.8B and Hy-MT2-30B-A3B
- Embedding / lm_head expansion with mean padding initialization
- GGUF conversion optimized for llama.cpp speculative decoding

⚠️ **Experimental Notice**

Speculative decoding acceleration is not guaranteed.

Because Hy-MT2-30B-A3B is a MoE model with only around 3B active parameters, the additional draft model computation and model scheduling overhead may offset the expected speedup.

This project is mainly intended for:

- Large VRAM users
- llama.cpp enthusiasts
- Users interested in MoE speculative decoding experiments

Model repository:

[alphaZimuth/Hy-MT2-1.8B-SpecDraft-30B](https://huggingface.co/alphaZimuth/Hy-MT2-1.8B-SpecDraft-30B)

## Credits

-   Tencent Hy-MT2 team for the original model.
-   LocalAI team for the APEX quantization framework.
-   llama.cpp contributors for GGUF support.
-   **gigass03** for identifying the `hy_v3` architecture metadata compatibility issue and verifying the fix.

## License

Apache-2.0
