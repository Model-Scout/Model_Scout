---
license: apache-2.0
library_name: transformers
tags:
- zubr
language:
- en
- zh
- de
- es
- ru
- ko
- fr
- ja
- pt
- tr
- pl
- ca
- nl
- ar
- sv
- it
- id
- hi
- fi
- vi
- he
- uk
- el
- ms
- cs
- ro
- da
- hu
- ta
- th
- ur
- hr
- bg
- lt
- la
- mi
- ml
- cy
- sk
- te
- fa
- lv
- bn
- sr
- az
- sl
- kn
- et
- mk
- br
- eu
- is
- hy
- ne
- mn
- bs
- kk
- sq
- sw
- gl
- mr
- pa
- si
- km
- sn
- yo
- so
- af
- oc
- ka
- be
- tg
- sd
- gu
- am
- yi
- lo
- uz
- fo
- ht
- ps
- tk
- nn
- mt
- sa
- lb
- my
- bo
- tl
- mg
- as
- tt
- haw
- ln
- ha
- ba
- jw
- su
- yue
pipeline_tag: automatic-speech-recognition
base_model: openai/whisper-small
---
# 🦬🔊 Zubr Whisper

**Repository:** [alekringtonnn-ai/zubr-whisper](https://huggingface.co/alekringtonnn-ai/zubr-whisper)

—

## 📖 What This Model Is

`zubr-whisper` is the **GGUF version of the audio model by alekringtonnn-ai** for the task of **Automatic Speech Recognition (ASR)** — speech-to-text transcription. The model converts an **audio file → text**.

The model is built on **openai/whisper-small** — a compact multilingual version of OpenAI’s Whisper (~244 Million parameters). Whisper is the most popular open-source speech recognition engine, supporting ~99 languages, including Russian.

The **GGUF** format is a universal format for quantized weights: the model runs **on any platform** — Windows, Linux, macOS, Android — on a regular **CPU**, without expensive GPUs.

> 💡 For Macs with Apple Silicon (M1–M4), there is a separate **MLX version** of this same model: [alekringtonnn-ai/zubr-whisper-mlx](https://huggingface.co/alekringtonnn-ai/zubr-whisper-mlx).

### Key Features

- **Speech Recognition (ASR):** the model’s task is audio transcription (speech → text), not chat dialogue.
- **Base — Whisper-small from OpenAI:** a proven architecture with multilingual support (~99 languages, including Russian).
- **Cross-platform:** GGUF + whisper.cpp = runs on CPU and GPU (NVIDIA, AMD, Intel) on Windows, Linux, and macOS.
- **Compactness:** the versions weigh from ~90 MB (Q2) to ~259 MB (Q8) — the model runs even on low-power laptops.
- **Subtitles and timecodes:** like Whisper, the model can produce per-segment transcripts with timestamps.

> ⚠️ **Important:** this is an audio transcription model — it is **not** intended for text generation from prompts (chat), image processing, etc. For the conversational models in the Zubr lineup, see [zubr-mini-1.9-3b](https://huggingface.co/alekringtonnn-ai/zubr-mini-1.9-3b).

### Model Tree

```text
openai/whisper-small                          ← base model (OpenAI)
        │ (GGUF quantization by alekringtonnn-ai)
alekringtonnn-ai/zubr-whisper                 ← GGUF version (THIS repository) — whisper.cpp, all platforms
        │ (conversion to MLX)
alekringtonnn-ai/zubr-whisper-mlx             ← MLX version for Apple Silicon
```

—

## 📊 Versions (Quantizations) in the Repository

The repository offers **6 GGUF quantization options** — from an ultra-compact 2-bit one to a nearly original 8-bit one:

| Version | File | Size | What it is | What it’s for |
|---------|------|------|------------|----------------|
| **Q2_K** | [q2_k.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/q2_k.gguf) | ~89.7 MB | The most aggressive 2-bit quantization | Devices with minimal memory (smartphones, single-board computers). Recognition quality suffers noticeably |
| **Q4_0** | [whisper-small-q4_0.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/whisper-small-q4_0.gguf) | ~139 MB | Classic 4-bit quantization (fast, simple format) | A well-established legacy format: high speed, minimal requirements |
| **Q4_1** | [whisper-small-q4_1.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/whisper-small-q4_1.gguf) | ~154 MB | 4-bit quantization with an accuracy layer (better than Q4_0) | Slightly higher quality than Q4_0 at almost the same speed |
| **Q5_0** | [whisper-small-q5_0.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/whisper-small-q5_0.gguf) | ~175 MB | 5-bit quantization — a high quality level | A good accuracy/size balance for regular use |
| **Q5_1** ⭐ | [whisper-small-q5_1.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/whisper-small-q5_1.gguf) | ~190 MB | 5-bit quantization with an accuracy layer | **The recommended choice:** quality close to Q8 at a noticeably smaller size |
| **Q8_0** | [whisper-small-q8_0.gguf](https://huggingface.co/alekringtonnn-ai/zubr-whisper/blob/main/whisper-small-q8_0.gguf) | ~259 MB | 8-bit quantization — virtually lossless quality | Maximum recognition quality; the file is still compact |

> 💡 **How to choose:** for transcription, quality matters more than size — go with **Q5_1** (recommended) or **Q8_0** (maximum). Q4_0/Q4_1 — if speed on weak hardware matters more; Q2_K — only for very limited devices.

—

## 📥 How to Download

### Requirements

- Any modern CPU (x86 with AVX/AVX2 or ARM); a GPU is optional (NVIDIA/AMD/Intel accelerate recognition).
- RAM: from ~512 MB free for Q2 up to ~1 GB for Q8.
- Free disk space: 90–260 MB depending on the version.
- To run — [whisper.cpp](https://github.com/ggml-org/whisper.cpp) installed.

### Method 1: `huggingface-cli` (recommended)

```bash
# Install the CLI
pip install -U «huggingface_hub[cli]»

# Download a specific quantization (e.g., the recommended Q5_1):
huggingface-cli download alekringtonnn-ai/zubr-whisper \
  whisper-small-q5_1.gguf

# Download the entire repository (all 6 quantizations, ~1 GB):
huggingface-cli download alekringtonnn-ai/zubr-whisper
```

By default, files are saved to `~/.cache/huggingface/hub/`.

### Method 2: Direct links (browser / wget / curl)

```bash
# The recommended version (Q5_1)
curl -L -o whisper-small-q5_1.gguf \
  «https://huggingface.co/alekringtonnn-ai/zubr-whisper/resolve/main/whisper-small-q5_1.gguf»

# Maximum quality (Q8_0)
curl -L -o whisper-small-q8_0.gguf \
  «https://huggingface.co/alekringtonnn-ai/zubr-whisper/resolve/main/whisper-small-q8_0.gguf»
```

The same links also work in a browser: open the file page and click «Download», or append `?download=true` to the URL.

### Method 3: Directly from whisper.cpp (with an HF base)

whisper.cpp can download GGUF models from Hugging Face using the `—model` flag:

```bash
whisper-cli —model zubr-whisper —language ru -f audio.wav
```

> A more reliable path is to download the file via Method 1 or 2 and pass the path to it with the `-m` flag (see the «How to Run» section).

—

## 🚀 How to Run

### Installing whisper.cpp

```bash
# macOS (Homebrew)
brew install whisper-cpp

# Windows
winget install whisper-cpp
# or download a prebuilt binary: https://github.com/ggml-org/whisper.cpp/releases

# Building from source (Linux)
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp
cmake -B build && cmake —build build —config Release
```

### Preparing audio

whisper.cpp expects **16 kHz WAV**. Convert with ffmpeg:

```bash
ffmpeg -i audio.mp3 -ar 16000 -ac 1 -c\:a pcm_s16le audio16k.wav
```

### Transcription

```bash
# Basic launch:
whisper-cli -m whisper-small-q5_1.gguf -f audio16k.wav -l ru

# Useful flags:
whisper-cli \
  -m whisper-small-q5_1.gguf \
  -f audio16k.wav \
  -l ru \                       # audio language (ru = Russian)
  -otxt \                       # output to .txt (also: -osrt, -ovtt, -olrc, -oj)
  -of transcript                # result file name
```

The result appears as `transcript.txt` / `transcript.srt` / `transcript.json` (JSON includes per-segment timecodes).

### Via Python (pywhispercpp)

```bash
pip install pywhispercpp
```

```python
import pywhispercpp as whisper

model = whisper.Whisper(‘whisper-small-q5_1.gguf’)
segments = model.transcribe(‘audio16k.wav’, lang=‘ru’)

for segment in segments:
    print(f»[{segment.start:.1f}s → {segment.end:.1f}s] {segment.text}»)
```

—

## ⚙️ Recommended Parameters

| Parameter | Value | Comment |
|-----------|-------|----------|
| `-l` (language) | `ru` / `en` / auto | Audio language; specifying it explicitly improves quality |
| `—temperature` | 0.0–0.2 | For transcription, the lower the more stable |
| `-t` (threads) | number of CPU cores | More threads = faster recognition |
| `-otxt / -osrt / -ovtt / -oj` | output format | Text, subtitles, JSON with timecodes |

—