---
license: other
license_name: mixed-upstream-licenses
license_link: https://huggingface.co/cswk/sayit-asr-gguf#licenses
pipeline_tag: automatic-speech-recognition
library_name: transcribe.cpp
base_model_relation: quantized
base_model:
  - nvidia/parakeet-unified-en-0.6b
  - nvidia/nemotron-3.5-asr-streaming-0.6b
  - FunAudioLLM/SenseVoiceSmall
  - FunAudioLLM/Fun-ASR-Nano-2512
  - Qwen/Qwen3-ASR-0.6B
  - Qwen/Qwen3-ASR-1.7B
language:
  - zh
  - en
  - ja
  - ko
  - yue
tags:
  - gguf
  - asr
  - speech-to-text
  - voice-typing
  - dictation
  - transcribe.cpp
  - sensevoice
  - parakeet
  - qwen3-asr
  - fun-asr-nano
  - windows
---

# SayIt ASR — GGUF weights

The local speech-recognition models shipped with
**[SayIt](https://github.com/crosswk/SayIt)**, an open-source voice typing app for
Windows: press a shortcut, speak, and AI-cleaned text lands at your cursor.

These seven files are **byte-identical re-uploads** of the
[handy-computer](https://huggingface.co/handy-computer) GGUF conversions, mirrored here
so SayIt's model downloader does not depend on a third-party repository staying online.
No requantization, no retraining, no modification of any kind.

## Acknowledgements

**All the hard work here belongs to [Handy](https://github.com/cjpais/Handy) and
[@cjpais](https://github.com/cjpais).**

SayIt's entire local speech-recognition stack rests on two things they built and gave
away: [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp), the ggml-based
C/C++ inference library (MIT), and the
[handy-computer](https://huggingface.co/handy-computer) model org, which converted these
ASR models to GGUF and keeps a much larger catalog than the seven files here. Without
those conversions there would be no local mode in SayIt at all — running SenseVoice,
Fun-ASR, Qwen3-ASR, Parakeet and Nemotron on consumer hardware through one runtime is
the difficult part, and it was already solved.

If you are looking for the canonical source of any file in this repo, go upstream:

| This repo | Upstream conversion |
| --- | --- |
| `parakeet-unified-en-0.6b-Q4_K_M.gguf` | [handy-computer/parakeet-unified-en-0.6b-gguf](https://huggingface.co/handy-computer/parakeet-unified-en-0.6b-gguf) |
| `SenseVoiceSmall-Q8_0.gguf` | [handy-computer/SenseVoiceSmall-gguf](https://huggingface.co/handy-computer/SenseVoiceSmall-gguf) |
| `nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf` | [handy-computer/nemotron-3.5-asr-streaming-0.6b-gguf](https://huggingface.co/handy-computer/nemotron-3.5-asr-streaming-0.6b-gguf) |
| `Fun-ASR-Nano-2512-Q8_0.gguf` | [handy-computer/Fun-ASR-Nano-2512-gguf](https://huggingface.co/handy-computer/Fun-ASR-Nano-2512-gguf) |
| `Qwen3-ASR-0.6B-Q8_0.gguf` | [handy-computer/Qwen3-ASR-0.6B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-0.6B-gguf) |
| `Qwen3-ASR-1.7B-Q4_K_M.gguf` | [handy-computer/Qwen3-ASR-1.7B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-1.7B-gguf) |
| `Qwen3-ASR-1.7B-Q5_K_M.gguf` | [handy-computer/Qwen3-ASR-1.7B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-1.7B-gguf) |

Also with thanks to the labs that trained and released the original models: **NVIDIA**
(Parakeet, Nemotron), **Alibaba FunAudioLLM** (SenseVoice, Fun-ASR Nano) and
**Alibaba Qwen** (Qwen3-ASR).

> ### Compatibility
>
> These are **[transcribe.cpp](https://github.com/handy-computer/transcribe.cpp)** GGUF files.
> They are **not** loadable by `llama.cpp` or `whisper.cpp`. The `general.architecture`
> tags (`sensevoice`, `funasr_nano`, `parakeet`, `qwen3_asr`) are specific to that
> runtime, so a same-named GGUF from another uploader will fail to load even though the
> download and checksum succeed.

## Models

Ordered fast to slow.

| File | Base model | Quant | Size | Languages | RAM in use |
| --- | --- | --- | --- | --- | --- |
| `parakeet-unified-en-0.6b-Q4_K_M.gguf` | [nvidia/parakeet-unified-en-0.6b](https://huggingface.co/nvidia/parakeet-unified-en-0.6b) | Q4_K_M | 477 MB | English only | ~0.9 GB |
| `SenseVoiceSmall-Q8_0.gguf` | [FunAudioLLM/SenseVoiceSmall](https://huggingface.co/FunAudioLLM/SenseVoiceSmall) | Q8_0 | 253 MB | zh, en, ja, ko, yue | ~0.35 GB |
| `nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf` | [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | Q4_K_M | 496 MB | 32 locales | ~1.05 GB |
| `Fun-ASR-Nano-2512-Q8_0.gguf` | [FunAudioLLM/Fun-ASR-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512) | Q8_0 | 891 MB | zh, en, ja | ~1.4 GB |
| `Qwen3-ASR-0.6B-Q8_0.gguf` | [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) | Q8_0 | 850 MB | 30+ | ~1.5 GB |
| `Qwen3-ASR-1.7B-Q4_K_M.gguf` | [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | Q4_K_M | 1.32 GB | 30+ | ~2.3 GB |
| `Qwen3-ASR-1.7B-Q5_K_M.gguf` | [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | Q5_K_M | 1.52 GB | 30+ | ~2.6 GB |

`RAM in use` is a **measured resident working set** while the model is loaded, not the
file size. Autoregressive models such as Qwen3-ASR add 700 MB to 1 GB on top of the
weights for KV cache and compute buffers.

## Which one to pick

- **English only** → `parakeet-unified-en-0.6b`. In English it is simultaneously the
  fastest and the most accurate file here (upstream LibriSpeech test-clean WER 1.62% at
  Q4_K_M), so it dominates every other entry. It returns an **empty string** on Chinese
  audio, which is why it cannot be a general-purpose default.
- **Smallest footprint** → `SenseVoiceSmall`. 253 MB on disk, ~350 MB resident.
- **Chinese dictation, best value** → `Fun-ASR-Nano-2512`. Beats Qwen3-ASR 0.6B on both
  speed and accuracy (upstream WER 1.79% vs 2.11%) at roughly half the decode cost of
  the 1.7B, but only covers zh / en / ja.
- **Widest language coverage** → `nemotron-3.5-asr-streaming-0.6b`, 32 locales including
  Spanish, French, German, Italian, Portuguese, Dutch, Russian, Arabic, Hindi, Turkish,
  Vietnamese and Ukrainian. Noticeably less accurate in English than parakeet
  (WER 3.28% vs 1.62%), so pick it for coverage, not for English.
- **Highest accuracy across many languages** → `Qwen3-ASR-1.7B-Q5_K_M` (upstream WER
  1.65%). The Q4_K_M variant trades WER 1.65% → 1.81% for 188 MB less download and
  lower memory pressure.

All WER figures above are the values reported upstream for these quantizations, not our
own measurements.

## Usage notes

Three behaviours that are easy to misdiagnose as bugs:

1. **Punctuation on SenseVoice and Fun-ASR Nano is behind the ITN flag.** With
   `itn=off` the model takes the `<|woitn|>` branch and returns unpunctuated text.
2. **Nemotron 3.5 only accepts region-qualified language codes** (`en-US`, `zh-CN`).
   Passing a bare `en` returns `unsupported language (status 10)`. Every other model
   here takes bare codes. SayIt resolves this in `gguf_asr.rs::resolve_language`
   (exact match → first locale of the same language → fall back to auto-detect).
3. **Parakeet and Nemotron ignore the ITN/PnC options** — both report `unsupported`.
   Casing and punctuation are inherent model behaviour. Parakeet normalizes numbers
   (`2026`, not spelled out); Nemotron keeps them in spoken form, which is a training
   choice rather than a defect.

### With SayIt

Nothing to do. Open SayIt → Settings → Voice engine → Local mode, and pick a model. It
downloads, verifies, and loads it, with Vulkan GPU acceleration when a GPU is available
(AMD and Intel included, not just NVIDIA).

### Direct download

```bash
huggingface-cli download cswk/sayit-asr-gguf SenseVoiceSmall-Q8_0.gguf --local-dir .
```

## Checksums

SHA-256, for verifying a manual download:

| File | SHA-256 |
| --- | --- |
| `parakeet-unified-en-0.6b-Q4_K_M.gguf` | `a8bf3de2b393bd14ead5a858c3748d5e3b07a20fdeabdd3b498fba4f463fa929` |
| `SenseVoiceSmall-Q8_0.gguf` | `6c759ee4c9748c9b3f7a5a60ca74f0f7e685fb9d45d1378fce7cfd62f59adf29` |
| `nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf` | `41c99fa5fb6f3d35f68e79adc3e755eca2232a8d921178bd647b71194792b8fd` |
| `Fun-ASR-Nano-2512-Q8_0.gguf` | `681caef6df15a2c0e153b40ca7fe4087fdf65751fa5e6fe605d8a75dff969e61` |
| `Qwen3-ASR-0.6B-Q8_0.gguf` | `f081b2d5e23bd669d92cc331d722a8a0681943b8e6f34b48996fd5c319b5acd8` |
| `Qwen3-ASR-1.7B-Q4_K_M.gguf` | `b7afe3674f653fa84f712ed2440353c6e7cf7f93697fef76b05a26538b24844e` |
| `Qwen3-ASR-1.7B-Q5_K_M.gguf` | `034c557fe92ff8fcd9a9c041cbdaad347be0a86a58d3a348f63cf3f0180879d0` |

## Licenses

<a id="licenses"></a>

This repository carries a mix of upstream licenses. **Each file stays under the license
of its original model** — re-hosting does not change it. Check the one you plan to use:

| File | License | Holder |
| --- | --- | --- |
| `parakeet-unified-en-0.6b-Q4_K_M.gguf` | CC-BY-4.0 (**attribution required**) | NVIDIA |
| `nemotron-3.5-asr-streaming-0.6b-Q4_K_M.gguf` | NVIDIA model license (`other`) | NVIDIA |
| `SenseVoiceSmall-Q8_0.gguf` | see upstream model card (`other`) | Alibaba FunAudioLLM |
| `Fun-ASR-Nano-2512-Q8_0.gguf` | see upstream model card (`other`) | Alibaba FunAudioLLM |
| `Qwen3-ASR-0.6B-Q8_0.gguf` | Apache-2.0 | Alibaba Qwen |
| `Qwen3-ASR-1.7B-*.gguf` | Apache-2.0 | Alibaba Qwen |

SayIt itself is AGPL-3.0. That license applies to the application, not to these weights.
