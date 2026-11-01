---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
tags:
- liquid
- edge
- lfm2.5
- onnx
- onnxruntime
- webgpu
base_model:
- LiquidAI/LFM2.5-2.6B
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# LFM2.5-2.6B-ONNX

LFM2.5 is a new family of hybrid models designed for **on-device deployment**. It builds on the LFM2 architecture with extended pre-training and reinforcement learning.

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-2.6B

## Recommended Variants

| Precision | Size  | Platform        | Use Case |
|-----------|-------|-----------------|----------|
| Q4 | ~1.9 GB | WebGPU, Server | Recommended for most uses (quantized embedding) |
| Q4F16 | ~1.5 GB | WebGPU | Quantized embedding and q4 weights with FP16 runtime and caches |
| FP16 | ~2.1 GB | WebGPU, Server | Higher quality |
| Q8 | ~2.1 GB | Server only | Balance of quality and size |

- **WebGPU**: Use `Q4`, `Q4F16`, or `FP16` (`Q8` is not supported on WebGPU).
- **Server (CPU/GPU)**: All variants supported.

Q4 and Q4F16 use a quantized input embedding. Q4F16 uses FP16 runtime tensors and caches while quantizing the LM head and decoder linear weights to q4.

## Model Files

```
onnx/
├── model.onnx              # FP32
├── model_fp16.onnx         # FP16
├── model_q4.onnx           # Q4, quantized embedding (WebGPU)
├── model_q4f16.onnx        # Q4 embedding/weights, FP16 runtime and caches (WebGPU)
└── model_q8.onnx           # Q8
```

## Python (onnxruntime)

```bash
pip install onnxruntime transformers numpy huggingface_hub
# or, for GPU:
pip install onnxruntime-gpu transformers numpy huggingface_hub
```

```python
from huggingface_hub import hf_hub_download

model_id = "LiquidAI/LFM2.5-2.6B-ONNX"
# Q8 recommended for server CPU/GPU; use model_q4.onnx for WebGPU.
hf_hub_download(model_id, "onnx/model_q8.onnx")
hf_hub_download(model_id, "onnx/model_q8.onnx_data")
```

## WebGPU (Transformers.js)

```js
import { pipeline } from "@huggingface/transformers";

const generator = await pipeline("text-generation", "LiquidAI/LFM2.5-2.6B-ONNX", {
  device: "webgpu",
  dtype: "q4", // or "q4f16" or "fp16"
});
```
