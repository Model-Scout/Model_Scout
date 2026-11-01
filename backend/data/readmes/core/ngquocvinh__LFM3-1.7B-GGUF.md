---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
library_name: llama.cpp
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- gguf
- llama.cpp
- lfm3
- quantized
- text-generation
---

# LFM3-1.7B GGUF

Community GGUF quantizations of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B).

<div align="center" style="background-color:#f59e0b;color:#ffffff;padding:16px 20px;border-radius:10px;line-height:1.7;">
☕ If this GGUF made your day easier, a coffee would make mine.<br>
<a href="https://ko-fi.com/ngquocvinh" style="color:#ffffff;"><strong style="color:#ffffff;">Send a coffee ☕</strong></a><br>
I build and test these releases myself. Your coffee helps keep me going.<br>
Thank you for supporting this work.
</div>

## About LFM3-1.7B

LFM3-1.7B is a 1.73B-parameter, text-only model with a tri-hybrid architecture: short convolutions, sliding-window attention, and global attention. Liquid AI lists a 256K-token input-plus-output context and support for 16 languages: English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, and Polish. Liquid AI positions the model for local-agent workflows, tool use, and structured output, and cautions against agentic coding and complex multi-step reasoning. See the [official model card](https://huggingface.co/LiquidAI/LFM3-1.7B) for the source details.

<a href="https://huggingface.co/LiquidAI/LFM3-1.7B"><img src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/lfm3-edge-inference.webp" alt="Liquid AI's edge-inference benchmark for LFM3-1.7B at 32K context"></a>

*Upstream edge-inference measurements at 32K context, as reported by [Liquid AI](https://huggingface.co/LiquidAI/LFM3-1.7B). They are not measurements of this GGUF package.*

These are weight quantizations only; no training or fine-tuning was performed for this release. Runtime smoke checks use a 4,096-token context. The fidelity evaluation below uses a 2,048-token context; neither check validates the listed 256K context or task-specific tool behavior.

## Fidelity measurements

Evaluation: WikiText-2 `valid` and `test`, four chunks each at context 2,048; ΔPPL is relative to BF16. See the [measurement TSV](reproducibility/fidelity-measurements.tsv) and [manifest](reproducibility/manifest.md).

| File | Size (GB) | Mean KLD ↓ | Top-1 vs BF16 ↑ | ΔPPL | RMS Δp |
|---|---:|---:|---:|---:|---:|
| `LFM3-1.7B-Q8_0.gguf` | 1.846239 | 0.001638 | 98.094% | +0.380% | 0.888% |
| `LFM3-1.7B-Q6_K.gguf` | 1.427639 | 0.007199 | 96.066% | -0.640% | 1.931% |
| **`LFM3-1.7B-Q5_K_M.gguf`** | **1.258663** | **0.025549** | **92.204%** | **-0.762%** | **3.530%** |
| `LFM3-1.7B-Q5_K_S.gguf` | 1.232900 | 0.029246 | 90.934% | -0.325% | 3.666% |
| `LFM3-1.7B-Q4_K_M.gguf` | 1.099628 | 0.078081 | 86.657% | +8.548% | 6.495% |
| `LFM3-1.7B-Q4_K_S.gguf` | 1.056038 | 0.086320 | 85.936% | +9.472% | 6.630% |
| **`LFM3-1.7B-IQ4_NL.gguf`** | **1.049616** | **0.082172** | **86.584%** | **+3.696%** | **6.353%** |
| `LFM3-1.7B-IQ4_XS.gguf` | 1.003795 | 0.089715 | 85.814% | +5.711% | 6.609% |
| `LFM3-1.7B-Q3_K_M.gguf` | 0.914900 | 0.211307 | 78.886% | +19.529% | 10.698% |
| `LFM3-1.7B-IQ3_M.gguf` | 0.868803 | 0.213445 | 78.263% | +13.961% | 10.853% |
| `LFM3-1.7B-IQ3_S.gguf` | 0.854877 | 0.252816 | 75.941% | +14.683% | 11.833% |
| `LFM3-1.7B-Q2_K.gguf` | 0.750155 | 0.812599 | 59.922% | +104.098% | 21.488% |
| `LFM3-1.7B-IQ2_XS.gguf` | 0.616161 | 1.169763 | 53.055% | +172.870% | 28.204% |
| `LFM3-1.7B-IQ1_M.gguf` | 0.518994 | 2.609784 | 31.953% | +1050.699% | 39.139% |
| `LFM3-1.7B-Q1_0.gguf` | 0.431033 | 8.025374 | 0.391% | +242158.584% | 52.629% |

The low-bit formats are experimental. IQ1_M and Q1_0 show large fidelity losses in this evaluation and are not recommended when output quality matters. The [machine-readable measurements](reproducibility/fidelity-measurements.tsv) contain the full precision values and the [reproducibility manifest](reproducibility/manifest.md) records corpus hashes and evaluation settings.

## Quick start

Build an LFM3-compatible version of [llama.cpp](https://github.com/ggml-org/llama.cpp), then run a short prompt:

```bash
./llama-cli \
  -m LFM3-1.7B-Q8_0.gguf \
  --chat-template-file chat_template.jinja \
  --jinja \
  --reasoning off \
  -p 'Answer briefly in English: What is the capital of France?' \
  -n 128 -c 4096 --temp 0.1 --top-k 50 --repeat-penalty 1.1
```

The quick start uses Q8_0. Adjust context, GPU offload, batch size, and KV-cache settings to your hardware. The table reports next-token fidelity only; output quality on a specific workload can differ.

## Reproducibility and validation

All 15 GGUF files were quantized directly from the same locked BF16 GGUF input with an LFM3-1.7B-specific imatrix. No quantized GGUF was used as input for another quantization. The [reproducibility manifest](reproducibility/manifest.md) records source revisions, hashes, runtime, commands, and validation profiles. [Artifact measurements](reproducibility/artifact-measurements.tsv) use decimal GB (`bytes / 1e9`); [fidelity measurements](reproducibility/fidelity-measurements.tsv) report the BF16 comparison; [SHA256SUMS.txt](SHA256SUMS.txt) contains published-file checksums.

Each released quantization passed an LFM3-compatible llama.cpp load/generation smoke check at context 4,096. The hold-out evaluation is a separate next-token fidelity measurement. Raw build, smoke, and evaluation logs are kept outside the public package.

## License and attribution

The upstream LFM Open License v1.0 (`lfm1.0`) is included in [LICENSE](LICENSE). These are community GGUF quantizations, not an official Liquid AI release or endorsement.
