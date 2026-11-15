---
license: apache-2.0
base_model: Qwen/Qwen3-ASR-1.7B
base_model_relation: quantized
library_name: transcribe.cpp
pipeline_tag: automatic-speech-recognition
language:
  - zh
  - en
  - yue
  - ar
  - de
  - fr
  - es
  - pt
  - id
  - it
  - ko
  - ru
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
  - ro
  - hu
  - mk
tags:
  - gguf
  - transcribe.cpp
  - herald
---

# Qwen3-ASR 1.7B (GGUF)

`Qwen3-ASR-1.7B-Q8_0.gguf`: Qwen3-ASR 1.7B by Qwen (Alibaba Cloud), converted to GGUF for
[transcribe.cpp](https://github.com/handy-computer/transcribe.cpp), for Herald, private offline dictation.

| | |
|---|---|
| Original model | [Qwen (Alibaba Cloud)](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) |
| Licence | Apache License 2.0 (`LICENSE`) |
| Converted by | handy-computer, from [handy-computer/Qwen3-ASR-1.7B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-1.7B-gguf) (see `NOTICE`) |
| File | `Qwen3-ASR-1.7B-Q8_0.gguf`, Q8_0, 2,185,030,624 bytes, SHA-256 `9a0d81792dfea2d5f278b8a63deb3ea6e02139ce42c2301f32ea19c4f77526b7` |
| File | `Qwen3-ASR-1.7B-Q6_K.gguf`, Q6_K, 1,692,554,208 bytes, SHA-256 `c75a961b7134a6c952d89797865cb0d0376876185aee04ef6d12c31c2952e4e1` |

These files are byte-for-byte copies of the ones published at
handy-computer/Qwen3-ASR-1.7B-gguf (commit `92282af`); the weights were not
changed. Herald downloads it from here, so it doesn't depend on another
project's hosting. The other quantisations are at the original repository.

All credit for the model belongs to Qwen (Alibaba Cloud), and for the conversion to the
transcribe.cpp authors.
