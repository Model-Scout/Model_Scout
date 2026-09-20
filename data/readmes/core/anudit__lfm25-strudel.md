---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
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
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
- onnx
base_model: LiquidAI/LFM2.5-350M
---

# lfm25-strudel

LoRA fine-tune of [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) for natural-language -> [Strudel.cc](https://strudel.cc) live-coding music generation, fused with `mlx-lm`.

## Contents

- Root: fused MLX weights (`model.safetensors` + config/tokenizer), ready for `mlx-lm` inference.
- `adapters/`: LoRA adapter checkpoints saved during training (`mlx-lm` LoRA format, rank 32 / alpha 64).
- `onnx/`: ONNX exports of the fused model for cross-platform / non-MLX inference:
  - `model_fp32.onnx` — full precision
  - `model_bf16.onnx` — bfloat16 weights
  - `model_fp8.onnx` — float8 (e4m3fn) weights

  The ONNX graphs take `input_ids` and `attention_mask` and return `logits` (no KV cache; each call is a full forward pass). They were exported from the fused weights after correcting `mlx-lm`'s depthwise-conv weight layout (`(dim, kernel, 1)`) to the `transformers` `Conv1d` layout (`(dim, 1, kernel)`) expected by `Lfm2ForCausalLM`. The bf16/fp8 variants are weight-only casts of the fp32 graph (storage-size quants); verify operator/EP support for these dtypes before relying on them for compute.

## Usage (MLX)

```bash
pip install mlx-lm
mlx_lm.generate --model <this-repo> --prompt "// a fun pop indian lofi beat"
```

## Usage (ONNX Runtime)

```python
import onnxruntime as ort
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("<this-repo>")
sess = ort.InferenceSession("onnx/model_fp32.onnx", providers=["CPUExecutionProvider"])
inputs = tok("// a fun pop indian lofi beat\n", return_tensors="np")
logits = sess.run(None, {"input_ids": inputs["input_ids"], "attention_mask": inputs["attention_mask"]})[0]
```
