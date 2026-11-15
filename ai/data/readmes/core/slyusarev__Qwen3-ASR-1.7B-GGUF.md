---
license: apache-2.0
language:
  - ru
  - en
  - zh
  - yue
  - ar
  - de
  - fr
  - es
  - pt
  - id
  - it
  - ko
  - th
  - vi
  - ja
  - tr
  - hi
  - ms
  - nl
  - sv
  - da
  - fi
  - pl
  - cs
  - fil
  - fa
  - el
  - hu
  - mk
  - ro
base_model: Qwen/Qwen3-ASR-1.7B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
tags:
  - gguf
  - llama.cpp
  - asr
  - speech-recognition
  - qwen3-asr
---

# Qwen3-ASR-1.7B — GGUF

GGUF builds of [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) for llama.cpp-based runtimes.

| File | Size | SHA-256 |
|---|---|---|
| `Qwen3-ASR-1.7B-Q4_K_M.gguf` | 1.28 GB | `f53b45df729c90a182612b759227daa9bb72139b012a87e558dd6c204d486ae9` |
| `Qwen3-ASR-1.7B-Q5_K_M.gguf` | 1.26 GB | `33ca947c1a39f80f5fe0774324924dd11f603ef4c08b50aa04ead3133787e54c` |
| `Qwen3-ASR-1.7B-Q8_0.gguf` | 2.17 GB | `58e22d0532d4eacaf034cfac17a6fed159f37c41390c710186783be439d1fc57` |
| `mmproj-Qwen3-ASR-1.7B-Q8_0.gguf` | 356 MB | `46c1d533af3f354ceb37ce855dbceff7da7fa7cf1e6a523df3b13440bd164c0d` |

The mmproj file is required alongside any of the main files.

`Q8_0` and `mmproj` are unmodified copies from [ggml-org/Qwen3-ASR-1.7B-GGUF](https://huggingface.co/ggml-org/Qwen3-ASR-1.7B-GGUF) (identical SHA-256). `Q4_K_M` is requantized from that `Q8_0`.

`Q5_K_M` is converted from the original bf16 weights and quantized directly. The tied embedding matrix, which the converter writes twice, is stored once: `output.weight` is dropped and `token_embd.weight` kept at Q6_K, which runtimes substitute for it — hence the file is smaller than `Q4_K_M`.

License: Apache 2.0, inherited from the base model.
