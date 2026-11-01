---
license: gemma
base_model:
  - Jiunsong/supergemma4-26b-abliterated-multimodal
tags:
  - gemma4
  - gguf
  - llama.cpp
  - multimodal
  - image-text-to-text
  - abliterated
  - uncensored
  - quantized
  - 4-bit
language:
  - en
  - ko
pipeline_tag: image-text-to-text
---

[Support ongoing open-source work: ko-fi.com/jiunsong](https://ko-fi.com/jiunsong)

# SuperGemma4-26B-Abliterated-Multimodal GGUF 4bit

This is the compact `llama.cpp`-ready GGUF 4bit distribution of [Jiunsong/supergemma4-26b-abliterated-multimodal](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal).

It keeps the matching multimodal projector and was validated with both text and image prompts after quantization.

## Included files

- `supergemma4-26b-abliterated-multimodal-Q4_K_M.gguf`
- `mmproj-supergemma4-26b-abliterated-multimodal-f16.gguf`

## Validation

- Text check: returned `READY`
- Image check: returned `Red` for a solid red test image
- Text throughput in `llama.cpp`: prompt `230.6 tok/s`, generation `137.1 tok/s`
- Image throughput in `llama.cpp`: prompt `138.1 tok/s`, generation `50.3 tok/s`
- Disk footprint: about `17 GB`

## Quantization note

This build was generated as `Q4_K_M`. A small number of tensors were automatically kept at higher precision by `llama.cpp` where needed for compatibility and stability.

## Recommended use

Use this build when you want the smallest practical GGUF package here while keeping text + vision capability.

## Quick start

```bash
llama-cli \
  -m /absolute/path/to/supergemma4-26b-abliterated-multimodal-Q4_K_M.gguf \
  -mm /absolute/path/to/mmproj-supergemma4-26b-abliterated-multimodal-f16.gguf \
  -cnv -st \
  --image /absolute/path/to/image.png \
  -p "Describe the image briefly."
```
