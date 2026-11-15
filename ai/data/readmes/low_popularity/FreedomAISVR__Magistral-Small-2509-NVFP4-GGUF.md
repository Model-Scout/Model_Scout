---
license: apache-2.0
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
library_name: gguf
tags:
- gguf
- magistral
- mistral3
- mistral
- reasoning
- vision
- multimodal
- nvfp4
- NVFP4
base_model: mistralai/Magistral-Small-2509
pipeline_tag: image-text-to-text
inference: false
quantized_by: FreedomAI
---

# Magistral-Small-2509-NVFP4-GGUF

GGUF quantization of [mistralai/Magistral-Small-2509](https://huggingface.co/mistralai/Magistral-Small-2509) — a 24B multimodal reasoning model fine-tuned from Mistral-Small-3.2-24B-Instruct-2506. Optimized for agentic coding, tool calling, and multi-step reasoning with vision support.

Quantized to **NVFP4** format for efficient inference with minimal quality loss.

## About NVFP4

NVFP4 is NVIDIA's native 4-bit floating-point format (E4M3) for Blackwell GPUs. It stores weights in FP4 with a shared per-block scale, enabling native Blackwell tensor core acceleration with no dequantization overhead during inference.

## Files

| Filename | Type | Size | Description |
|----------|------|------|-------------|
| `magistral-small-2509-nvfp4.gguf` | GGUF (NVFP4) | 12.52 GB | Quantized text model weights |
| `mmproj-magistral-small-2509-f16.gguf` | F16 mmproj | 0.84 GB | Vision encoder projector (24-layer Pixtral ViT, 1024 hidden) |
| `README.md` | Markdown | - | Model card |

## Quantization Details

| Property | Value |
|----------|-------|
| Format | NVFP4 |
| Bits Per Weight | 4.56 BPW |
| File Size | 12.52 GB (text) + 0.84 GB (mmproj) |
| Tensor Count | 363 (text) + 222 (mmproj) |
| Architecture | Mistral3 (mistral3) |
| Context Length | 131,072 tokens |
| Vision | 24-layer Pixtral ViT, 1024 hidden, 1540 max image size |

## Model Description

- **Developer**: Mistral AI
- **Base Model**: Mistral-Small-3.2-24B-Instruct-2506
- **Architecture**: Dense transformer, Mistral3ForConditionalGeneration
- **Parameters**: 24B
- **Context Length**: 131,072 tokens (native)
- **Vision**: 24-layer Pixtral ViT encoder (1024 hidden)
- **Capabilities**: Agentic coding, tool calling, multi-step reasoning, image understanding
- **Languages**: Multilingual (27+ languages)
- **License**: Apache 2.0

## Usage

### llama.cpp (CLI)

```bash
# Text + Image
llama-cli -m magistral-small-2509-nvfp4.gguf \
  --mmproj mmproj-magistral-small-2509-f16.gguf \
  --image photo.jpg \
  -p "Describe this image in detail" \
  -n 512

# Text only
llama-cli -m magistral-small-2509-nvfp4.gguf \
  -p "Solve this step by step: 23 * 47" \
  -n 512

# OpenAI-compatible server
llama-server -m magistral-small-2509-nvfp4.gguf \
  --mmproj mmproj-magistral-small-2509-f16.gguf \
  --port 8080
```

### llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="FreedomAISVR/Magistral-Small-2509-NVFP4-GGUF",
    filename="magistral-small-2509-nvfp4.gguf",
    n_gpu_layers=-1,
)

response = llm.create_chat_completion([
    {"role": "user", "content": "Write a Python function to sort a list"}
])
print(response["choices"][0]["message"]["content"])
```

### Direct download

```python
from huggingface_hub import hf_hub_download

for filename in ["magistral-small-2509-nvfp4.gguf", "mmproj-magistral-small-2509-f16.gguf"]:
    hf_hub_download(
        repo_id="FreedomAISVR/Magistral-Small-2509-NVFP4-GGUF",
        filename=filename,
        local_dir="./models"
    )
```

## Quantization Pipeline

```
1. Download source weights
   huggingface_hub.snapshot_download("mistralai/Magistral-Small-2509")

2. Convert text model to F16 GGUF
   convert_hf_to_gguf.py --outtype f16

3. Extract vision encoder
   convert_hf_to_gguf.py --mmproj --outtype f16

4. Quantize to NVFP4
   llama-quantize magistral-small-2509-f16.gguf magistral-small-2509-nvfp4.gguf NVFP4
```

**Note**: This model requires `mistral-common` to be installed for tokenizer conversion:
```bash
pip install mistral-common[image,audio]
```

## Hardware

| Component | Specification |
|-----------|---------------|
| GPU | NVIDIA RTX 5060 Ti (Blackwell) |
| System RAM | 64 GB |
| Storage | NVMe |

## License

Apache 2.0 — same as the original [mistralai/Magistral-Small-2509](https://huggingface.co/mistralai/Magistral-Small-2509).
