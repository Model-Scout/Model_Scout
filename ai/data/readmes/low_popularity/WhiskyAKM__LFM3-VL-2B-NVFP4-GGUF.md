---
pipeline_tag: image-text-to-text
base_model: LiquidAI/LFM3-VL-2B
license: other
license_name: lfm1.0
license_link: LICENSE
library_name: llama-cpp
tags:
- liquid
- lfm3
- edge
- conversational
- gguf
- nvfp4
- image-text-to-text
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
---

# LFM3-VL-2B NVFP4 - GGUF

NVFP4 GGUF conversion of **LFM3-VL-2B**, Liquid AI's on-device vision-language model, providing highly efficient 4-bit floating-point quantization for image understanding and text generation.

This directory provides **NVFP4** (NVIDIA 4-bit floating-point) GGUF files plus the BF16 vision projector (`mmproj.gguf`), making the model usable with [llama.cpp](https://github.com/ggml-org/llama.cpp) and other GGUF-compatible inference engines.

## Model Overview

**LFM3-VL-2B** is a ~2B-parameter vision-language model built on the **LFM3 1.7B Base** backbone, designed for **fast, private multimodal inference on-device**. It accepts text and images and generates text, with strong document understanding and multilingual support.

Find more information about LFM3-VL-2B in our [blog post](https://www.liquid.ai/blog/lfm3) and the [original model card](https://huggingface.co/LiquidAI/LFM3-VL-2B).

## Model Architecture

### Language Model

| Property                   | Value                                                                                                                                          |
| :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **Architecture**           | LFM3 (hybrid: GQA attention + short convolutions)                                                                                              |
| **Total Parameters**       | ~2B (size label 2B)                                                                                                                            |
| **Base Model**             | [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base)                                                                      |
| **Number of Layers**       | 24                                                                                                                                             |
| **Embedding Dimension**    | 2,048                                                                                                                                          |
| **Feed-Forward Dimension** | 7,680                                                                                                                                          |
| **Attention Heads**        | 16 (GQA, 4 KV heads on full-attention layers)                                                                                                  |
| **Sliding Window**         | 256 tokens (every 4th layer uses sliding-window attention)                                                                                     |
| **Vocabulary Size**        | 128,000                                                                                                                                        |
| **Context Length**         | 128,000 tokens                                                                                                                                 |
| **RoPE Base**              | 1,000,000 (10,000 for sliding-window layers)                                                                                                   |
| **Languages**              | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |

### Vision Encoder (`mmproj.gguf`)

| Property                 | Value                                                      |
| :----------------------- | :--------------------------------------------------------- |
| **Architecture**         | CLIP-style vision encoder + LFM3-VL projector              |
| **Parameters**           | ~189M                                                      |
| **Image Size**           | 512 × 512 per tile                                         |
| **Patch Size**           | 16                                                         |
| **Vision Layers**        | 14                                                         |
| **Vision Embedding**     | 1,024                                                      |
| **Projection Dimension** | 2,048 (matches LM embedding)                               |
| **Spatial Merge**        | 2 × 2                                                      |
| **Pixel Range**          | 65,536 – 16,777,216 pixels per image (variable resolution) |

## GGUF Files

| File                               | Size    | Format | Description                                                         |
| :--------------------------------- | :------ | :----- | :------------------------------------------------------------------ |
| `lfm3-vl-2b-nvfp4.gguf`            | ~1.0 GB | NVFP4  | NVFP4-quantized language model (imatrix-based)                      |
| `lfm3-vl-2b-nvfp4-q8-embed.gguf`   | ~1.1 GB | NVFP4  | NVFP4-quantized language model (imatrix-based) with q8_0 embeddings |
| `lfm3-vl-2b-nvfp4-bf16-embed.gguf` | ~1.3 GB | NVFP4  | NVFP4-quantized language model (imatrix-based) with bf16 embeddings |
| `mmproj.gguf`                      | ~362 MB | BF16   | Vision encoder + projector — required for image input               |

> **About NVFP4:** NVFP4 is NVIDIA's 4-bit floating-point format (E2M1). It offers significant memory savings while preserving quality close to bfloat16, and is accelerated on NVIDIA Blackwell GPUs via llama.cpp.

## Usage

### llama.cpp

```bash
./llama-cli \
  -m lfm3-vl-2b-nvfp4.gguf \
  --mmproj mmproj.gguf
```

### llama-server (OpenAI-compatible API)

```bash
./llama-server \
  -m lfm3-vl-2b-nvfp4.gguf \
  --mmproj mmproj.gguf \
  --host [IP_ADDRESS] --port 8080
```

## Generation Parameters

Recommended parameters for LFM3-VL-2B (stored in the GGUF metadata):

| Parameter          | Value |
| :----------------- | :---- |
| Temperature        | 0.1   |
| Top-K              | 50    |
| Top-P              | 1.0   |
| Min-P              | 0.0   |
| Repetition Penalty | 1.1   |

## Key Features

- **Multimodal on-device:** Text + image input, text output, with a compact ~2B footprint.
- **Document understanding:** Variable-resolution image tiling for high-resolution documents.
- **Multilingual:** 17 languages.
- **Efficient quantization:** NVFP4 weights accelerated on NVIDIA Blackwell GPUs.

## License

[lfm1.0](https://huggingface.co/LiquidAI/LFM3-VL-2B/blob/main/LICENSE)
