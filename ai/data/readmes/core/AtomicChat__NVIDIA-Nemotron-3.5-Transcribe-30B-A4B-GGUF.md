---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
library_name: gguf
language:
  - en
  - de
  - fr
  - es
  - it
  - pt
  - nl
  - pl
  - cs
  - sk
  - hi
  - ja
  - ko
  - zh
  - multilingual
tags:
  - gguf
  - nemotron-3.5
  - nemo-speech-cpp
  - speech-to-text
  - asr
  - transcription
  - speaker-diarization
  - speech-translation
  - nvfp4
---

# NVIDIA Nemotron 3.5 Transcribe 30B-A4B GGUF

<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_nvidia_nemotron_3_5_transcribe_30b_a4b&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
  <a href="https://x.com/atomic_chat_hq"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_x.png" width="108" alt="X"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>Built by the team behind <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_nvidia_nemotron_3_5_transcribe_30b_a4b&utm_content=bullet_app">Atomic Chat</a>, the app that runs open-weight models locally and offline.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

GGUF builds of [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B),
NVIDIA's open-weight speech-to-text model (40 languages, recordings up to one hour, word timestamps and speaker
labels, speech translation, custom instructions), for NVIDIA's own GGML runtime
[NeMo-Speech.cpp](https://github.com/NVIDIA/NeMo-Speech.cpp). By AtomicChat.

A model is **two files in one folder**: one decoder (pick a size below) and the encoder file
`NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Encoder-F16.gguf` (speech encoder, speaker branch and CTC timestamp head).
The decoder names its encoder file, so keep the encoder's file name as it is.

- **Every decoder from 15.55 GB up transcribes like the BF16 decoder on our 2,200-utterance test**: English,
  German, French, Spanish and Chinese. Word error stays within ±0.18 points of BF16 on every English, German, French
  and Spanish set (table below); Chinese character error moves +0.02 to +0.41 points, every interval including
  zero, as it does for NVIDIA's own conversions.
- **A 13.57 GB decoder for 16 GB GPUs** (`AD-Q2_0_M`): English, German, French and Spanish within noise of BF16,
  Chinese character error +1.5 points. Peak GPU memory 15.6 GiB with the settings under *Run it*.
- **Smaller than the converter defaults**: `AD-NVFP4` is 19.68 GB on disk against 21.79 GB for NVIDIA's NVFP4
  conversion, `AD-IQ4_NL` 19.68 GB against 20.35 GB for its IQ4_NL conversion, same expert formats; the embeddings
  and output head are Q8_0 instead of BF16, and the IQ4_NL experts are quantized with an importance matrix.
- **Seven decoders, 13.57 to 35.00 GB on disk**, from Blackwell NVFP4 to IQ4_NL and Q8_0 for CPU, Metal and Vulkan.
- **Ready-made files**: no 67 GB checkpoint download and no Python conversion.
- **DFlash2 drafter included** (BF16, 1.15 GB) for speculative decoding on the batched CUDA path.

## Files

| File | Size on disk | For |
|---|---|---|
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Encoder-F16.gguf` | 1.67 GB | **required** with every decoder |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0.gguf` | 35.00 GB | closest to the original; 48 GB+ GPUs, 64 GB Macs |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-Q5_0_XL.gguf` | 29.26 GB | near Q8_0, 5.7 GB smaller |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-IQ4_NL_L.gguf` | 22.55 GB | 32 GB GPUs and Macs |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-IQ4_NL.gguf` | 19.68 GB | **recommended** outside Blackwell: 24 GB GPUs, CPU, Metal, Vulkan |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-NVFP4.gguf` | 19.68 GB | **recommended** on Blackwell (RTX 50xx, RTX PRO 6000, DGX Spark, B200): experts in native NVFP4 |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-Q2_0_L.gguf` | 15.55 GB | 24 GB Macs (with the encoder: 17.2 GB); Chinese a little behind |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-Q2_0_M.gguf` | 13.57 GB | 16 GB GPUs (see *Run it*); English, German, French, Spanish within noise, Chinese +1.5 CER |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-DFlash2-BF16.gguf` | 1.15 GB | optional draft model (`asr.salm.dflash_path`) |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-imatrix.gguf` | 0.06 GB | the importance matrix used for the IQ4_NL / Q5 / Q2_0 files |

## Word error against the BF16 decoder

Change in word error (character error for Chinese) against the BF16 decoder, in points, with the 95% interval from
a paired bootstrap over utterances. Negative is fewer errors. Rows in *italics* are not in this repo: the BF16
reference and NVIDIA's converter defaults (`convert_model.py --outtype nvfp4` / `iq4_nl`), measured the same way.
The last column counts the 2,200 utterances whose transcript is word for word the BF16 decoder's; it is noisy
(batching order changes it: the same `AD-IQ4_NL` file run on a second box matched its own first run on 1987), so
differences of a few dozen mean nothing.

| Decoder | Size on disk | LibriSpeech clean | LibriSpeech other | MLS German | MLS French | MLS Spanish | FLEURS Chinese (CER) | Same transcript as BF16 |
|---|---|---|---|---|---|---|---|---|
| *BF16 (reference)* | *65.85 GB* | *1.58%* | *3.34%* | *4.04%* | *3.79%* | *3.23%* | *9.77%* | *2200* |
| `Q8_0` | 35.00 GB | +0.00 [-0.06, +0.07] | +0.06 [-0.08, +0.19] | -0.09 [-0.22, +0.02] | +0.00 [-0.08, +0.07] | +0.01 [-0.11, +0.13] | +0.30 [-0.04, +0.75] | 1963 |
| `AD-Q5_0_XL` | 29.26 GB | -0.02 [-0.08, +0.03] | +0.03 [-0.09, +0.15] | +0.05 [-0.09, +0.19] | -0.05 [-0.18, +0.08] | -0.06 [-0.19, +0.08] | +0.20 [-0.23, +0.73] | 1889 |
| `AD-IQ4_NL_L` | 22.55 GB | -0.01 [-0.07, +0.05] | -0.08 [-0.21, +0.04] | -0.10 [-0.29, +0.07] | -0.07 [-0.20, +0.05] | -0.06 [-0.19, +0.05] | +0.02 [-0.29, +0.35] | 1810 |
| `AD-IQ4_NL` | 19.68 GB | -0.01 [-0.08, +0.06] | -0.05 [-0.21, +0.11] | -0.11 [-0.27, +0.04] | -0.08 [-0.24, +0.08] | -0.02 [-0.16, +0.13] | +0.03 [-0.31, +0.36] | 1748 |
| `AD-NVFP4` | 19.68 GB | -0.02 [-0.08, +0.04] | -0.01 [-0.19, +0.16] | -0.13 [-0.32, +0.05] | -0.14 [-0.37, +0.09] | -0.12 [-0.24, -0.02] | +0.24 [-0.25, +0.81] | 1684 |
| `AD-Q2_0_L` ¹ | 15.55 GB | -0.08 [-0.21, +0.04] | +0.02 [-0.26, +0.30] | +0.17 [-0.11, +0.46] | +0.08 [-0.18, +0.31] | +0.06 [-0.13, +0.26] | +0.41 [-0.17, +1.04] | 1309 |
| `AD-Q2_0_M` ¹ | 13.57 GB | -0.01 [-0.17, +0.15] | +0.05 [-0.21, +0.29] | +0.12 [-0.12, +0.36] | +0.03 [-0.48, +0.43] | +0.06 [-0.16, +0.29] | +1.53 [+0.85, +2.22] | 1223 |
| *NVIDIA NVFP4 conversion* | *21.79 GB* | *-0.01 [-0.07, +0.05]* | *-0.03 [-0.22, +0.15]* | *-0.07 [-0.26, +0.11]* | *-0.10 [-0.32, +0.10]* | *-0.11 [-0.24, +0.02]* | *+0.29 [-0.17, +0.80]* | *1685* |
| *NVIDIA IQ4_NL conversion* | *20.35 GB* | *-0.05 [-0.12, +0.00]* | *-0.03 [-0.18, +0.11]* | *+0.03 [-0.15, +0.20]* | *-0.12 [-0.34, +0.06]* | *-0.04 [-0.19, +0.12]* | *-0.10 [-0.40, +0.21]* | *1772* |

Test set (fixed sample, seed 0): LibriSpeech test-clean 500 and test-other 500, Multilingual LibriSpeech test
German, French and Spanish 300 each, FLEURS test Mandarin 300; 6.7 hours of audio. Greedy decoding through
`nemo-speech transcribe` (batched CUDA path, language hint per set) on an A100 80 GB, NeMo-Speech.cpp
`6a62501` (llama.cpp `bd4f514`). Whisper's English normalizer for English, its basic normalizer for the rest.
These are relative numbers on our sample, not leaderboard scores.

¹ Measured on a second box (A100 40 GB, same build). Moving boxes alone shifts a file by up to ±0.17 points: the
same `AD-IQ4_NL` file read -0.17 [-0.36, -0.01] on MLS German there.

## Run it

Build NeMo-Speech.cpp ([build guide](https://github.com/NVIDIA/NeMo-Speech.cpp/blob/main/docs/build.md)): CMake 3.26+,
SentencePiece 0.2.0+ (Ubuntu 22.04's packaged 0.1.96 fails to compile), CUDA 12.8+ for the batched CUDA path.

```bash
git clone https://github.com/NVIDIA/NeMo-Speech.cpp && cd NeMo-Speech.cpp
git submodule update --init --depth 1 llama.cpp third_party/cpp-httplib
scripts/configure.sh cuda-server && cmake --build --preset cuda-server

hf download AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF --local-dir models \
  --include "*Encoder-F16.gguf" --include "*AD-NVFP4.gguf"

# one file, JSON with word timestamps
build/cuda-server/bin/nemo-speech transcribe audio.wav \
  --model models/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-NVFP4.gguf --format json --word-times

# OpenAI-compatible server: /v1/audio/transcriptions, /v1/chat/completions
build/cuda-server/bin/nemo-speech serve --asr-model models/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-AD-NVFP4.gguf --port 8080
```

- Speaker labels: `--diarize`. Translation: `--translate-to de`. Custom prompt: `--instruction "..."`.
- Smaller GPUs: lower `--asr.salm.max_sequences` and raise `--asr.salm.n_ctx_per_sequence`; NVIDIA's
  [configuration guide](https://github.com/NVIDIA/NeMo-Speech.cpp/blob/main/docs/salm/configuration.md) lists the
  settings per GPU size.
- 16 GB GPUs with `AD-Q2_0_M`: `--asr.salm.max_sequences 2 --asr.salm.n_ctx_per_sequence 8192
  --asr.salm.max_context 8192 --asr.salm.mtp_draft 0 --asr.salm.n_batch 512 --asr.salm.encoder_max_batch 2`.
  Peak GPU memory 15.6 GiB on a 3.7-minute file (measured on an A100, not on a 16 GB card: it is tight).
  `max_context 8192` holds about 7 minutes of audio per request.
- DFlash2: `--asr.salm.dflash_path models/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-DFlash2-BF16.gguf` (batched CUDA path).
- CPU, Metal and Vulkan builds use upstream llama.cpp kernels: take `AD-IQ4_NL` (NVIDIA lists IQ4_NL for these
  paths) or `Q8_0`. Our measurements ran on CUDA only.

## How the files were made

- NVIDIA's converter (`convert_model.py --architecture salm`) wrote the encoder file and a BF16 decoder; the decoder
  is a standard llama.cpp `nemotron_h_moe` GGUF with the `nemo_speech.*` keys that pair it with the encoder.
- Rungs were quantized from that BF16 decoder with the converter's own `llama-quantize`. Experts carry the size;
  attention, Mamba in/out, the shared expert, the embeddings and the output head are Q8_0; the MTP head keeps the
  experts' type. Most matrices have rows of 2688, 1856 or 3712, which only block-32 types fit (no K- or I-quants
  with 256-blocks), so these files use NVFP4, Q8_0 and other block-32 types; the tensor types inside each file are
  the ones its name says.
- `AD-IQ4_NL`, `AD-IQ4_NL_L`, `AD-Q5_0_XL` and the two `AD-Q2_0` files use an importance matrix from the BF16
  decoder over 1.5M tokens of our text calibration corpus (`imatrix.gguf` here). It is text only: `llama-imatrix`
  cannot feed audio, so the activations on audio positions are not in it, which is why every file was checked on
  speech. At 4 bits it buys nothing measurable: NVIDIA's IQ4_NL conversion without one is within noise too.
  `Q8_0` and `AD-NVFP4` read no importance matrix (neither format uses one).
- Below 4 bits the quantizer decides everything. Stock Q2_0 sets the block scale to the block's largest weight, so
  it writes three levels, sends most weights to zero and ignores the importance matrix: with it on every expert
  (11.06 GB) English word error rose by 3.5 points and German, French and Spanish by 14 to 25. The `AD-Q2_0` files
  here use our imatrix-weighted Q2_0 quantizer instead (all four levels, scale fitted per block; same Q2_0 format,
  so the stock runtime reads it). `AD-Q2_0_M` keeps the 6 MoE blocks with the largest activations (40-51, from the
  importance matrix) and the MTP head at IQ4_NL; `AD-Q2_0_L` puts only the experts' down-projections at Q2_0
  (down-projections at Q2_0 beat up-projections at Q2_0 on German and Chinese at the same size). The same
  quantizer with every expert at Q2_0 (11.06 GB) still costs +0.2 points English and +0.8 German, +2.2 Chinese
  character error, so it is not published.

## License

The model is under the [OpenMDW License 1.1](https://openmdw.ai/license/1-1/) (`LICENSE` in this repo), as is its
base, [NVIDIA-Nemotron-3.5-Lightning-30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16).
These are conversions; see NVIDIA's [model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)
for the training data, evaluation, intended use and limitations.
