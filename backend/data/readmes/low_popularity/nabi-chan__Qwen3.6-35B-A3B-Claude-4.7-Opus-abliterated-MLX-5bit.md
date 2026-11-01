---
library_name: mlx
license: "apache-2.0"
pipeline_tag: text-generation
language:
  - en
  - ko
  - zh
  - ja
tags:
  - mlx
  - "mlx-5bit"
  - quantized
  - safetensors
  - apple-silicon
  - Qwen
  - Qwen3.6
  - Qwen3_5_moe
  - reasoning
  - distillation
  - chain-of-thought
  - mixture-of-experts
  - moe
  - lora
  - unsloth
  - abliterated
  - uncensored
datasets:
  - lordx64/reasoning-distill-opus-4-7-max-sft
base_model:
  - huihui-ai/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated
model-index: []
---

# 🌌 `huihui-ai/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated` converted to MLX 5-bit

## About This Quantization

**Apple Sllicon / MLX 5-bit**

- **Source Model (BF16)** : [huihui-ai/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated)
- **Quantized By:** [@nabi-chan](https://huggingface.co/nabi-chan)

### Quickstart

#### Install

```bash
pip install -U "mlx-lm>=0.31.2"
```

#### Python

```python
from mlx_lm import load, generate

model, tokenizer = load("nabi-chan/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-5bit")
print(generate(model, tokenizer, prompt="Explain quantum entanglement simply.", max_tokens=128))
```

#### CLI

```bash
python3 -m mlx_lm generate \
  --model nabi-chan/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-5bit \
  --prompt "Write a haiku about Apple Silicon." \
  --max-tokens 128
```

### Quantization Details

| Property              | Value                                                 |
| --------------------- | ----------------------------------------------------- |
| **Method**            | MLX affine quantization                               |
| **Bits / weight**     | 5                                                     |
| **Group size**        | 64                                                    |
| **Non-quant dtype**   | bfloat16                                              |
| **Quantizer version** | `mlx` : 0.31.2 / `mlx-lm` : 0.31.3 / `mlx-vlm`: 0.4.4 |

> [!WARNING]
> Protected tensors keep their original dtype. In VLM models, vision tensors and some guarded layers may remain unquantized.

---

Everything below is huihui-ai's original model card, preserved verbatim.

---

# huihui-ai/Huihui-Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated

This is an uncensored version of [lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled](https://huggingface.co/lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens.

## ollama

Please use the latest version of [ollama](https://github.com/ollama/ollama/releases)

You can use [huihui_ai/qwen3.6-abliterated:35b-Claude-4.7](https://ollama.com/huihui_ai/qwen3.6-abliterated:35b-Claude-4.7) directly,

```
ollama run huihui_ai/Qwen3.6-abliterated:35b-Claude-4.7
```

### Usage Warnings

- **Risk of Sensitive or Controversial Outputs**: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

- **Not Suitable for All Audiences**: Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

- **Legal and Ethical Responsibilities**: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

- **Research and Experimental Use**: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

- **Monitoring and Review Recommendations**: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

- **No Default Safety Guarantees**: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.

### Donation

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.

- bitcoin:

```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```

- Support our work on [Ko-fi](https://ko-fi.com/huihuiai)!
