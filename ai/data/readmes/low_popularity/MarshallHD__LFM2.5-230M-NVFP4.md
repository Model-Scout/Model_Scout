---
base_model:
- LiquidAI/LFM2.5-230M
base_model_relation: quantized
library_name: Model Optimizer
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-230M/blob/main/LICENSE
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
tags:
- liquid
- lfm2.5
- edge
- modelopt
- nvfp4
- fp4
- quantized
- 4-bit precision
- vllm
- sglang
- text-generation
---

# LFM2.5-230M NVFP4 Model Summary

The **LFM2.5-230M NVFP4** model is a quantized version of **Liquid AI's LFM2.5-230M**, a compact hybrid language model designed for edge and on-device inference. This checkpoint was produced with **NVIDIA Model Optimizer** and exported in **NVFP4** 4-bit floating point format.

This release uses a conservative **NVFP4 PTQ** recipe: inner feed-forward linear operators are quantized, while attention, convolution blocks, embeddings, normalization layers, the language-model head, and the outer layers at both ends of the stack remain in higher precision. The scope was selected by measuring fidelity to the BF16 reference across a sweep of quantization scopes and keeping the fastest scope that stayed closest to the reference.

## 🚀 Key Specifications

* **Architecture:** `Lfm2ForCausalLM`, 14-layer hybrid architecture with LIV convolution and GQA blocks.
* **Parameters:** 230M.
* **Base Model:** [`LiquidAI/LFM2.5-230M`](https://huggingface.co/LiquidAI/LFM2.5-230M).
* **Precision:** NVFP4 for selected feed-forward linear weights and activations.
* **Quantization Scope:** feed-forward linear operators in inner layers `5-11`.
* **Protected Modules:** embeddings, `lm_head`, all `self_attn*` paths, all `conv*` paths, normalization layers, layers `0-4`, and layers `12-13`.
* **Group Size:** 16.
* **Context Length:** 32,768 tokens.
* **KV Cache Quantization:** none.
* **License:** inherits the base model's [`lfm1.0` license](https://huggingface.co/LiquidAI/LFM2.5-230M/blob/main/LICENSE).
* **Release Date:** September 16, 2026.

## 🛠️ Software & Hardware Integration

* **Quantization Tooling:** NVIDIA Model Optimizer, official 0.46.0 release wheel.
* **ModelOpt Version:** `0.46.0`.
* **ModelOpt Commit:** release tag `0.46.0`, wheel `nvidia_modelopt-0.46.0-py3-none-any.whl`, sha256 `1864b4e9921e287b065be3861ab48345144e673273ebb2b94bd9a6119a9eba8e`.
* **Torch:** `2.10.0a0+b4e4ee81d3.nv25.12`.
* **Validated Runtime:** vLLM `0.29.0` with `--quantization modelopt_fp4`.
* **Validated FP4 Kernel:** `FlashInferCutlassNvFp4LinearKernel`.
* **Validated Hardware:** NVIDIA GB10.
* **Operating System:** Linux.

### Deployment Example, vLLM

```sh
pip install -U "transformers>=5.3.0" vllm

MODEL_ID="MarshallHD/LFM2.5-230M-NVFP4"

vllm serve "$MODEL_ID" \
    --quantization modelopt_fp4 \
    --trust-remote-code \
    --max-model-len 32768
```

### Python Example, vLLM

```python
from vllm import LLM, SamplingParams

model_id = "MarshallHD/LFM2.5-230M-NVFP4"

llm = LLM(
    model=model_id,
    quantization="modelopt_fp4",
    trust_remote_code=True,
    max_model_len=32768,
)

outputs = llm.generate(
    ["Explain NVFP4 quantization in one sentence."],
    SamplingParams(max_tokens=64, temperature=0.1),
)
print(outputs[0].outputs[0].text)
```

> This checkpoint targets runtimes with ModelOpt FP4 support, in particular vLLM or SGLang with `modelopt_fp4`.

## 📊 Performance & Evaluation

Both evaluations below compare this checkpoint against the BF16 reference under identical engine settings: vLLM 0.29.0, greedy decoding, prefix caching disabled, BF16 KV cache, single NVIDIA GB10.

### Fidelity to the BF16 reference

Teacher-forced scoring over 104,456 tokens drawn from three domains: general text, instruction prompts with reference answers, and Python function prompts with reference solutions.

| Metric | BF16 Reference | **NVFP4 PTQ** | Δ vs BF16 |
| :--- | ---: | ---: | ---: |
| **Perplexity, all domains** | 20.771 | **21.448** | +3.3% |
| **Perplexity, general text** | 42.519 | **44.083** | +3.7% |
| **Perplexity, code** | 5.371 | **5.554** | +3.4% |
| **Top-1 agreement with BF16** | — | **87.8%** | — |
| **KL divergence vs BF16** | — | **0.042** | — |

Top-1 agreement is the share of scored positions where the most likely token matches the BF16 reference. KL divergence is measured on the top-32 support with the remaining mass pooled, which makes it a lower bound of the full-vocabulary value.

### Task accuracy

Multiple-choice and short-answer accuracy over 24,063 examples, scored with EleutherAI lm-evaluation-harness 0.4.13 on the vLLM backend. Both columns use identical harness settings.

| Benchmark | Examples | BF16 Reference | **NVFP4 PTQ** | Δ vs BF16 |
| :--- | ---: | ---: | ---: | ---: |
| **Weighted MCQA** | 24,063 | 28.434 | **27.997** | -0.436 |
| MMLU-Pro, exact match | 12,032 | 18.027 | **17.478** | -0.549 |
| ARC-Challenge, normalized accuracy | 1,172 | 32.082 | **31.570** | -0.512 |
| HellaSwag, normalized accuracy | 10,042 | 40.888 | **40.470** | -0.418 |
| TruthfulQA MC1, accuracy | 817 | 23.378 | **24.480** | +1.102 |

All values are accuracies reported as percentages. The weighted MCQA score is weighted by the number of examples in each benchmark.

### Throughput

Fixed 128-token prompts and 128 generated tokens, median of three measured runs per setting.

| Setting | BF16 Reference | **NVFP4 PTQ** | Speedup |
| :--- | ---: | ---: | ---: |
| Output tokens/s, batch 1 | 342.8 | **392.7** | **1.15×** |
| Output tokens/s, batch 16 | 5,548.0 | **6,214.4** | **1.12×** |

## 📚 Datasets

### Calibration Data

512 sequences of at most 512 tokens each, drawn from public English text and public instruction-following prompts with reference answers, rendered through the LFM2.5 chat template. The calibration set is disjoint from every evaluation set used above.

### Evaluation Benchmarks

* **WikiText-2:** general text fidelity, test split.
* **Instruction prompts with reference answers:** chat-format fidelity.
* **HumanEval prompts with reference solutions:** code fidelity.
* **MMLU-Pro:** broad multiple-choice knowledge and reasoning.
* **ARC-Challenge:** science multiple-choice questions.
* **HellaSwag:** commonsense continuation selection.
* **TruthfulQA MC1:** truthfulness multiple-choice evaluation.

## 🔬 Quantization Details

The exported checkpoint includes `hf_quant_config.json` and `config.json` metadata for ModelOpt runtime detection.

```json
{
  "quant_algo": "NVFP4",
  "group_size": 16,
  "kv_cache_quant_algo": null,
  "exclude_modules": [
    "lm_head",
    "model.embed_tokens",
    "model.layers.0*",
    "model.layers.1.*",
    "model.layers.10.self_attn*",
    "model.layers.11.conv*",
    "model.layers.12*",
    "model.layers.13*",
    "model.layers.2*",
    "model.layers.3*",
    "model.layers.4*",
    "model.layers.5.conv*",
    "model.layers.6.self_attn*",
    "model.layers.7.conv*",
    "model.layers.8.self_attn*",
    "model.layers.9.conv*"
  ]
}
```

### Artifact Files

| File | Size |
| :--- | ---: |
| `model.safetensors` | 380,273,160 bytes |
| `config.json` | 3,033 bytes |
| `hf_quant_config.json` | 790 bytes |
| `tokenizer.json` | 4,733,389 bytes |
| `tokenizer_config.json` | 489 bytes |
| `generation_config.json` | 304 bytes |
| `chat_template.jinja` | 4,762 bytes |

## Citation

If you use this checkpoint, cite the base model and NVIDIA Model Optimizer:

```bibtex
@misc{liquidai_lfm25_230m,
  title = {LFM2.5-230M},
  author = {Liquid AI},
  year = {2026},
  url = {https://huggingface.co/LiquidAI/LFM2.5-230M}
}

@software{nvidia_modelopt,
  title = {NVIDIA Model Optimizer},
  author = {NVIDIA},
  url = {https://github.com/NVIDIA/Model-Optimizer}
}
```
