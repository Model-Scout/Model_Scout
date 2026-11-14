---
license: apache-2.0
language:
  - ko
  - en
library_name: llama.cpp
pipeline_tag: text-generation
inference: false
base_model:
  - huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-GGUF
base_model_relation: quantized
tags:
  - gguf
  - qwen3.8
  - korean
  - coding
  - imatrix
  - mixed-precision
  - mtp
---

# Coder390 EfficientThink Abliterated · KO Ridge 3.7bpw GGUF

A Korean-calibrated mixed-precision GGUF of **Huihui Qwen3.8 27B Coder390 EfficientThink Abliterated**, quantized directly from the upstream BF16 GGUF.

이 모델은 Coder390 EfficientThink Abliterated의 BF16 가중치를 한국어 보정 데이터와 Ridge 방식의 혼합 정밀도로 양자화한 GGUF입니다. 한국어로 추가 학습한 모델은 아니며, 한국어 품질 향상을 별도 벤치마크로 검증하지 않았습니다.

## Model and provenance

- BF16 source: [huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-GGUF), revision `a0b17c71d9943529aefe88b83f494bf01c6b4d68`.
- Source filename: `Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-bf16.gguf`.
- Source SHA-256: `fcddc1ff6efa4932cf4a7eb18087be39527b740cdca0810bbd3a717312d61d53`.
- Calibration corpus: [augustine223/korean-imatrix-calibration-corpus](https://huggingface.co/datasets/augustine223/korean-imatrix-calibration-corpus), revision `4ff695275c950f4311e84c561883566c8ab874dd`.
- Corpus SHA-256: `bca66acae75db6a9a1d4ad152329b2c31dd235f2fc73dbb93f863d4d7b402b3c`.
- The importance matrix was newly collected on a Coder390 Q8_0 calibration copy, using 708 chunks of 512 tokens. The final model was quantized from BF16 using that matrix.
- Tensor precision allocation follows [empero-ai/Qwen3.8-27B-Ridge-GGUF](https://huggingface.co/empero-ai/Qwen3.8-27B-Ridge-GGUF); the quantizer was pinned to llama.cpp commit `adb55e5`.
- The embedded tokenizer, chat template, and MTP tensors are preserved. This repository contains the text GGUF; no vision projector or external draft model is included.
- The upstream model is licensed under Apache 2.0; see [LICENSE](LICENSE). Original model attribution is retained above. This derivative changes quantization and removes local calibration paths from metadata.

## Tensor types

| Type | Tensors |
| --- | ---: |
| F32 | 360 |
| Q8_0 | 96 |
| Q4_K | 144 |
| Q5_K | 51 |
| Q6_K | 23 |
| IQ3_S | 32 |
| IQ2_S | 160 |
| **Total** | **866** |

The file is approximately **12.60 GB (11.73 GiB)**, about **3.69 bits per parameter**. Runtime memory also includes the KV cache and compute buffers.

## Download and run

Use a llama.cpp build that supports the `qwen35` architecture and these GGUF quantization types.

```bash
hf download donghanasd/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-KO-Ridge-3.7bpw-GGUF \
  Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-KO-Ridge-3.7bpw.gguf \
  --local-dir .

llama-server \
  --model Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-KO-Ridge-3.7bpw.gguf \
  --host 127.0.0.1 --port 8080 \
  --jinja --no-mmproj --gpu-layers 99 --ctx-size 32768
```

The starting context above is 32K. Reduce the context or GPU layer count if memory is insufficient. The GGUF declares a 262,144-token context; that metadata does not guarantee that your hardware can run that context length. No speed or quality benchmark is claimed for this upload.

## File integrity

Exact size: **12599186976 bytes**.

SHA-256:

```text
47de712523d6fbfede267d01739a6282f39724d1325987208693a33f75f5e353
```
