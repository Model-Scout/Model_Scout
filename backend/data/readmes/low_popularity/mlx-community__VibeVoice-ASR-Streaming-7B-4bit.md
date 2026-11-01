---
license: mit
library_name: mlx
pipeline_tag: automatic-speech-recognition
base_model: microsoft/VibeVoice-ASR-Streaming-7B
base_model_relation: quantized
language:
- en
- zh
- fr
- de
- it
- ja
- ko
- pt
- ru
- es
tags:
- mlx
- mlx-audio
- automatic-speech-recognition
- speech-to-text
- streaming
- speaker-diarization
- apple-silicon
- quantized
- 4bit
---

# mlx-community/VibeVoice-ASR-Streaming-7B-4bit

MLX conversion of [microsoft/VibeVoice-ASR-Streaming-7B](https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B)
— **streaming speaker-attributed ASR**: it transcribes *who said what* as the audio arrives, with
no separate diarization stage. 10 languages, hotword biasing via a context prefix.

Precision: **int4, group size 64, affine, language model only** — 5.71 GB. The **encoders stay at full precision** — they are depthwise-conv VAEs and only ~8 % of the checkpoint, so quantising them buys little. 16 GB-deployable.

## What differs from the upstream checkpoint

- **The acoustic tokenizer's DECODER is dropped** (276 tensors / 0.69 GB). It ships in the
  upstream repo but ASR never calls it — only the two encoders are used.
- Weights are in the **MLX layout** (`sanitize`d keys, Conv1d transposed to `[O, K, I]`).
- **Tokenizer and `preprocessor_config.json` are included and required.** The streaming protocol
  ends each chunk on `<|text_chunk_end|>` and reads `chunk_frames` / `lookahead_frames` from the
  preprocessor config; a consumer that falls back to the stock Qwen2.5 tokenizer has no such token
  and never terminates a chunk.

## Streaming geometry

`speech_tok_compress_ratio` 3200 @ 24 kHz = 7.5 frames/s. `chunk_frames` 22 → **2.9333 s**;
`lookahead_frames` 4 → **0.5333 s**. So the latency floor is ~3 s: this is live-captioning
latency, not dictation latency.

Each chunk is encoded independently from raw samples with cold conv state
(`split_then_encode`) — there is no cross-chunk encoder state to carry.

## Measured

On 40.4 min of balanced 4-speaker [AMI-IHM](https://huggingface.co/datasets/edinburghcstr/ami)
(7475 reference words), Apple M5 Max, against the PyTorch reference on identical audio:

| tier | cpWER | WER | speakers found | resident | peak | RTF |
|---|---|---|---|---|---|---|
| PyTorch reference | 31.76 % | 21.25 % | 15 / 16 | — | — | 0.696 |
| MLX bf16 | 31.68 % | 21.17 % | 15 / 16 | 16.66 GB | 21.45 GB | 0.916 |
| **MLX 4-bit** | **31.95 %** | 21.77 % | **15 / 16** | **5.72 GB** | **7.63 GB** | **0.149** |

**cpWER** is concatenated minimum-permutation WER — it charges transcription *and* speaker
attribution. 4-bit costs +0.27 cpWER against bf16 and loses **no** speakers; that is inside the
PyTorch reference's own ±0.8-point run-to-run band (see below), so the degradation sits below the
noise floor of the measurement.

Harness: [xocialize/mlxengine-audio-tools](https://github.com/xocialize/mlxengine-audio-tools).

## Two things worth knowing

**The upstream reference is not deterministic.** Its `encode_speech` samples the acoustic VAE
(`sample(dist_type='gaussian')`, `fix_std` 0.5) at ~26 % noise-to-signal, so it does not
reproduce itself run to run — four runs on identical audio span 1.58 cpWER points. This MLX port
takes the distribution's **mean** instead, which lands within 0.08 cpWER of the stochastic
reference and is repeatable.

**Quantisation here is device-dependent.** CPU- and GPU-computed 4-bit scales disagree on 396 of
1297 tensors. These weights were quantised on **GPU** (recorded as `quantization.mlx_quantised_on`
in `config.json`), which is the configuration the numbers above were measured on.

## Licence

MIT, from the upstream checkpoint. Conversion by [xocialize](https://github.com/xocialize).
