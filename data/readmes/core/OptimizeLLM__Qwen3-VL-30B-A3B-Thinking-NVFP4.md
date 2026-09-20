---
license: apache-2.0
base_model: Qwen/Qwen3-VL-30B-A3B-Thinking
tags:
  - qwen3
  - qwen3-vl
  - vision-language
  - multimodal
  - nvfp4
  - fp4
  - quantized
  - vllm
  - blackwell
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
pipeline_tag: image-text-to-text
library_name: transformers
---

# Qwen3-VL-30B-A3B-Thinking-NVFP4

NVFP4-quantized version of [Qwen/Qwen3-VL-30B-A3B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Thinking) for efficient inference on NVIDIA Blackwell GPUs with [vLLM](https://github.com/vllm-project/vllm).

| | |
|---|---|
| **Base Model** | Qwen3-VL-30B-A3B-Thinking (MoE: 31B total, ~3B active) |
| **Quantization** | NVFP4 (W4A4) — weights and activations |
| **VRAM** | ~16GB (vs ~62GB BF16, ~31GB FP8) |
| **What's quantized** | Text/language backbone only |
| **What's NOT quantized** | Vision encoder, multi-modal projector, LM head, MoE gates (all remain BF16) |

## Usage with vLLM

### Serving

```bash
vllm serve OptimizeLLM/Qwen3-VL-30B-A3B-Thinking-NVFP4 \
    --tensor-parallel-size 1 \
    --max-model-len 8192 \
    --reasoning-parser-plugin qwen3_vl_reasoning_parser.py \
    --reasoning-parser qwen3_vl \
    --kv-cache-dtype fp8
```

### Reasoning Parser

The included `qwen3_vl_reasoning_parser.py` is a custom vLLM reasoning parser plugin for this model. It extends vLLM's `DeepSeekR1ReasoningParser` and fixes an edge case where the model's answer can end up in `reasoning_content` instead of `content` when thinking is disabled.

Download it alongside the model and pass it via `--reasoning-parser-plugin`. Without it, you may see intermittent responses where `content` is null and the answer is in `reasoning_content`.

### Python (OpenAI-compatible API)

```python
from openai import OpenAI
import base64

client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")

with open("photo.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="OptimizeLLM/Qwen3-VL-30B-A3B-Thinking-NVFP4",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}},
            {"type": "text", "text": "What do you see in this image?"},
        ],
    }],
    max_tokens=2048,
)
print(response.choices[0].message.content)
```

### Thinking Control

The Thinking variant supports chain-of-thought reasoning. Control it per-request by appending to the text portion of your message:

- `/think` — Enable detailed reasoning (complex visual analysis, comparisons)
- `/no_think` — Disable thinking (fast perception, OCR, simple descriptions)

Example: `"Describe this image. /no_think"`

## Quantization

Quantized with [llm-compressor](https://github.com/vllm-project/llm-compressor) v0.9.0 using 512 multimodal calibration samples from [neuralmagic/calibration](https://huggingface.co/datasets/neuralmagic/calibration) (VLM split — image+text pairs, not text-only).

The full quantization script is included as `quantize_vl.py`. Notable details:

- **VLM calibration data** — uses the `VLM` split (image+text pairs) instead of the `LLM` split (text-only). The text decoder sees different activation distributions when processing image-conditioned inputs, so text-only calibration is suboptimal for VL models.
- **glibc malloc trim fix** — without `mallopt(M_TRIM_THRESHOLD, 0)`, glibc arena bloat accumulates about 1.4GB per subgraph during calibration (~68GB phantom RSS across 49 subgraphs), enough to OOM a 128GB machine. The script includes this fix. Zero impact on quantization quality.
- **Minimum system RAM:** 96GB recommended (62GB model + headroom). Quantization was performed on a 128GB system.

## Hardware

| GPU | VRAM | Notes |
|-----|------|-------|
| RTX PRO 6000 (96GB) | ~16GB model + headroom | Recommended — full Blackwell NVFP4 acceleration |
| RTX 5090 / 4090 (24GB) | ~16GB model, ~8GB headroom | Fits, but limited context/batch |
| A100 / H100 (80GB) | ~16GB model + headroom | Works, but NVFP4 acceleration requires SM100+ |

> **Note:** Full NVFP4 acceleration (W4A4 compute) requires Blackwell architecture (SM100+). On pre-Blackwell GPUs, vLLM uses weight-only quantization — still a memory savings, but without the activation quantization speedup.

## Acknowledgments

- [Qwen Team](https://huggingface.co/Qwen) for the base model
- [vLLM Project](https://github.com/vllm-project/vllm) for llm-compressor and inference runtime
- [Neural Magic](https://huggingface.co/neuralmagic) for the VLM calibration dataset
