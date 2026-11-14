---
license: apache-2.0
base_model: Audio8/ARK-ASR-3B
pipeline_tag: automatic-speech-recognition
language:
- en
- zh
- de
- ja
- fr
- ko
- es
tags:
- gguf
- arkasr
- speech
- audio
- transcribe.cpp
---

# ARK-ASR-3B GGUF

GGUF conversions of [Audio8/ARK-ASR-3B](https://huggingface.co/Audio8/ARK-ASR-3B), made from source revision `1e28271b79edc97635783bea65abc89195a09ed3`.

ARK-ASR combines a Whisper-style audio encoder, an MLP adapter, and a Qwen2.5 decoder. These files use GGUF architecture `arkasr`; they are **not** compatible with stock `llama.cpp` or `whisper.cpp`. They require the ARK-ASR implementation in the accompanying `transcribe.cpp` fork used by Handy.

## Runtime

`transcribe.cpp-arkasr-b838a2b.tar.gz` is a source snapshot of the exact ARK-enabled runtime used for validation (commit `b838a2b`). SHA-256: `776c2a7a690dc21dc629aa79d03003a0a9f9a463f1e0a4f3a4cefc6ee59dbe97`.

On macOS with Xcode command-line tools:

```bash
tar -xzf transcribe.cpp-arkasr-b838a2b.tar.gz
cd transcribe.cpp-arkasr
cmake -S . -B build -DTRANSCRIBE_BUILD_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --target transcribe-cli -j
build/bin/transcribe-cli --backend metal --model ../ark-asr-3b-Q8_0.gguf input.wav
```

The CLI expects WAV audio. The model frontend itself expects 16 kHz mono samples; the Handy desktop integration performs its normal recording conversion before inference.

## Files

| File | Size | SHA-256 | Notes |
| --- | ---: | --- | --- |
| `ark-asr-3b-F16.gguf` | 7,507,674,752 bytes | `a9546be836351e17f616084f7ebc174570a076ebb7ee460bb551fc302af04176` | High-precision reference used as the quantization oracle |
| `ark-asr-3b-Q8_0.gguf` | 4,289,201,792 bytes | `b9ab32cfe7982eed5a596a601059e112d4aa5476e851852f944062a10fb25ee8` | Recommended accuracy-first build |
| `ark-asr-3b-Q6_K.gguf` | 3,090,685,600 bytes | `bf7e2fb7a50a9b5eed9b9e4eb36ae6498131c60abb5c2de3e4e4b3d61173ab9f` | Balanced experimental build |
| `ark-asr-3b-Q5_K_M.gguf` | 3,078,096,544 bytes | `1457567b5a2d0f9a943a41d78586e08b54aa79360a821bd1b2ce5d56137f8bdd` | Experimental; conservative F16 tied embedding/output head |
| `ark-asr-3b-Q4_K_M.gguf` | 2,307,317,408 bytes | `7d232eab9c87f35946d0370bed9ce8c7337b1da94a238ad5d7d71c47ed65da1f` | Speed-first experimental build |

## Local validation

The models were tested on an Apple M4 Max with the Metal backend. Six saved English recordings (6.6–79.2 seconds, 724 F16-reference words total) were compared against an F16 GGUF generated from the official BF16 checkpoint.

| Quantization | Word disagreements vs F16 | Exact clips | Relative inference time |
| --- | ---: | ---: | ---: |
| Q8_0 | 2 / 724 | 5 / 6 | baseline |
| Q6_K | 12 / 724 | 5 / 6 | about 9% faster overall |
| Q5_K_M | 16 / 724 | 4 / 6 | about 5% faster overall |
| Q4_K_M | 16 / 724 | 4 / 6 | about 17% faster overall |

This is a small regression set, not a published WER benchmark. “Word disagreements” measures divergence from the F16 runtime output, not correctness against human transcripts.

An additional 491-second saved recording (1,413 F16-reference words) was used as a long-form check on the same M4 Max:

| Quantization | Inference time | Word disagreements vs F16 |
| --- | ---: | ---: |
| Q8_0 | 28.16 s | 2 / 1,413 (0.14%) |
| Q6_K | 25.45 s | 14 / 1,413 (0.99%) |
| Q4_K_M | 22.96 s | 36 / 1,413 (2.55%) |

Q8_0 remains the recommended model: the smaller variants save only a few seconds on eight minutes of audio while diverging more from the F16 reference.

## Long audio

The ARK runtime accepts arbitrary-duration audio. It processes independent windows of at most 30 seconds, chooses a low-energy boundary between 20 and 30 seconds when possible, overlaps windows by 2 seconds, and stitches the final transcript. This is offline transcription, not simulated live streaming.

## License and attribution

The original model is Apache-2.0 licensed. See the [official model card](https://huggingface.co/Audio8/ARK-ASR-3B) and [AutoArk repository](https://github.com/AutoArk/open-audio-opd) for architecture, training, and upstream attribution.
