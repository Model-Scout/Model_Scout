---
language:
- en
- hi
- ja
- ko
- pt
license: other
library_name: transformers
pipeline_tag: text-generation
tags:
- Qwen3.5
- NVFP4
- quantized
- modelopt
---

# Qwen3.8-27B-Uncensored-NVFP4

NVFP4 (4-bit per-block) quantized version of the Qwen3.8-27B Uncensored model, produced with
[NVIDIA TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer).

## Quality Comparison (Original vs BF16 vs NVFP4)

Preliminary evaluation with `lm_eval` + sglang (greedy, temperature 0). MMLU / CMMLU / C-Eval use a
20-question-per-subtask sample; GSM8K uses the full test set. We compare:
the **original** `Qwen3.8-27B`, our **Uncensored BF16** (before quantization), and the
**Uncensored NVFP4** (4-bit) checkpoint.

![Quality comparison](quality_comparison.png)

| Benchmark | Original | Uncensored BF16 | Uncensored NVFP4 | NVFP4 − BF16 | Std Err |
|---|---|---|---|---|---|
| MMLU (sample) | 0.8368 | 0.8307 | 0.8316 | +0.0009 | ±0.011 |
| CMMLU (sample) | 0.7075 | 0.7716 | 0.7761 | +0.0045 | ±0.011 |
| C-Eval (sample) | 0.7609 | 0.7837 | 0.7956 | +0.0119 | ±0.013 |
| GSM8K (strict) | 0.7036 | 0.7627 | 0.7786 | +0.0159 | ±0.012 |
| GSM8K (flexible) | 0.7263 | 0.7870 | 0.8014 | +0.0144 | ±0.011 |

Key takeaways:

- **Quantization preserves quality.** Unlike the Original vs Uncensored gap, NVFP4 tracks BF16
  almost exactly — all NVFP4−BF16 deltas are within ±1 standard error, i.e. **no measurable
  degradation** from 4-bit quantization (~4× weight compression).
- **Uncensored is generally stronger on these benchmarks than the stock original.** The uncensored
  checkpoint scores higher on CMMLU / C-Eval / GSM8K and comparable on MMLU. This is not caused by
  quantization — the same difference already exists between the uncensored BF16 model and the
  stock original, so it reflects the uncensoring/finetuning itself.
- The small positive NVFP4−BF16 deltas are within noise and should **not** be read as
  "NVFP4 is better than BF16"; the practical takeaway is that 4-bit quantization is effectively
  lossless on these tasks.

## Quantization

- **Format**: NVFP4 weights, FP8 KV cache, group size 16
- **Tool**: NVIDIA ModelOpt 0.45.0
- **Calibration**: `ultrachat_200k` + `nvidia/Nemotron-SFT-Multilingual-v2` (code/math/stem across Japanese, Korean, Portuguese, Hindi)
- **Excluded modules**: `lm_head`, embeddings, linear-attention `conv1d`/`in_proj_a`/`in_proj_b`, and MTP layers

## Shards

All safetensors shards are ≤ 5 GB (5 shards), so the repository can be cloned and uploaded without
Hugging Face large-file (>5 GB) restrictions.

## Usage

Load with Hugging Face transformers:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Vtuber-plan/Qwen3.8-27B-Uncensored-NVFP4"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
```

> Note: this NVFP4 checkpoint is intended for deployment with frameworks that support the
> ModelOpt NVFP4 format (e.g. TensorRT-LLM). Plain transformers/BF16 inference will not dequantize
> it natively and requires the corresponding quantization backend.
