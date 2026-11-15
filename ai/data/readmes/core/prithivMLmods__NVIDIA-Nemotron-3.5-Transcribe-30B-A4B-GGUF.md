---
language:
- cs
- nl
- en
- fr
- de
- hi
- it
- ko
- pl
- pt
- ru
- sk
- es
- bg
- hr
- da
- et
- fi
- hu
- ja
- lv
- lt
- ro
- sl
- sv
- th
- tr
- uk
- ar
- bn
- zh
- el
- he
- id
- mt
- mr
- tl
- ta
- te
- vi
library_name: nemo
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
pipeline_tag: automatic-speech-recognition
base_model:
- nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
tags:
- moe
- MXFP4_MOE
- llama-cpp
- NeMo-Speech-cpp
- nvidia
- pytorch
- nemotron-3.5
- speech
- asr
- speech-translation
- speaker-diarization
- audio
- transcription
- speech-to-text
- multilingual
- timestamps
- long-form-audio
- language-identification
- code-switching
- audio-question-answering
- instruction-following
- hf-asr-leaderboard
- transformers
- 30B
- A4B
- nvidia-blackwell
- rtx-pro-6000
- SM120
- GB202
- B200
- B300
- FP4
- blackwell
datasets:
- nvidia/Granary-v2
track_downloads: true
---

# **NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF**

**Nemotron 3.5 Transcribe** is NVIDIA's open-weight offline speech and audio model built on a 34B-parameter (4.3B active) hybrid Mamba-Transformer MoE architecture. Processing up to an hour of audio (65K context), it handles 40-language transcription, translation, speaker attribution, word timestamps, and audio Q&A.

* **Architecture & Training:** Pairs its base LLM with a ~600M ASR transformer, a 99M diarization encoder, and CTC heads, plus native multi-token prediction for speculative decoding. Trained on 1.72M unique hours of audio (6.53M total exposure).
* **Performance:** Achieves state-of-the-art open-weight ASR results—4.71 WER (English), 10.98 (long-form), 4.62 (multilingual), and 15.80 cpWER (multi-speaker)—alongside strong audio understanding scores (73.40% MMAU, 74.14% MMLU-Pro).
* **Limitations:** Higher WER in Norwegian (63.76%), Greek (26.93%), and Hebrew (20.97%). Text-only reasoning lags behind its base LLM, non-ASR audio evaluation is English-only, and it carries risks of prompt injection, hallucinations, and rare generation loops.
* **Deployment:** Released under the OpenMDW-1.1 license in BF16, FP8, and NVFP4 formats. Runs on a single H100 (80 GB) via vLLM 0.32.0 with NeMo Speech, Transformers, or SGLang-Omni (roughly half the speed of NVIDIA's closed-source NIM serving).

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.BF16.gguf | BF16 | 65.9 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.MXFP4_MOE.gguf | MXFP4_MOE | 18.7 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.MXFP4_MOE.gguf) | **MXFP4_MOE**: Highly optimized for **NVIDIA Blackwell** hardware accelerators **(e.g., RTX Pro 6000, RTX 50-series, B200, B300)**, offering native hardware-accelerated FP4 Tensor Core speeds and a strong balance of size and performance. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q3_K_L.gguf | Q3_K_L | 21.6 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q3_K_M.gguf | Q3_K_M | 20.7 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q3_K_M.gguf) | Low quality. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q4_K_M.gguf | Q4_K_M | 25.4 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q5_K_M.gguf | Q5_K_M | 27 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q5_K_M.gguf) | High quality, *recommended* for standard hardware. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q6_K.gguf | Q6_K | 34.9 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.Q6_K.gguf) | Very high quality, near perfect, *recommended* for standard hardware. |
| NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.mmproj.gguf | mmproj | 1.47 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.mmproj.gguf) | Multimodal projection file. Used for audio/transcription capabilities. |

## Run with llama.cpp

### Install dependencies and clone llama.cpp

```python
!pip install transformers huggingface-hub

!git clone https://github.com/ggml-org/llama.cpp.git
%cd /data/llama.cpp
```

### Download GGUF model files

Download the BF16 model and multimodal projector:

```python
from huggingface_hub import snapshot_download

# Target local directory
local_dir = "./model/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF"

# Download only the specified files
snapshot_download(
    repo_id="prithivMLmods/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF",
    local_dir=local_dir,
    allow_patterns=[
        "NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.BF16.gguf",
        "NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.mmproj.gguf",
    ],
    resume_download=True,
)
```

### Build llama-mtmd-cli

Build the multimodal CLI with the CUDA backend enabled:

```bash
!cmake --build . --config Release -j$(nproc) --target llama-mtmd-cli
```

### Download sample audio

```bash
!wget -O /data/llama.cpp/model/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/sample.wav \
"https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/gObkjtDcqnbGl2wu_p3UP.wav"
```

<audio controls src="https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/qrafA3GTtLGHq6iK0qmzO.wav"></audio>

### Audio transcription (GPU offloading)

Run inference using `llama-mtmd-cli` with all available model layers requested for GPU offloading:

```bash
!/data/llama.cpp/build/bin/llama-mtmd-cli \
    -m /data/llama.cpp/model/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.BF16.gguf \
    --mmproj /data/llama.cpp/model/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B.mmproj.gguf \
    --audio /data/llama.cpp/model/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/sample.wav \
    -p "Transcribe the audio accurately." \
    -ngl 99
```

### Output

```text
The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot cross bun.
```

## llama.cpp

LLM inference in C/C++ — [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

(Or try **NVIDIA-Nemotron-3.5-Transcribe-30B-A4B** with NeMo-Speech.cpp)

## NeMo-Speech.cpp

A lightweight native C++ runtime for the NVIDIA Nemotron Speech model family, with broad hardware support — https://github.com/NVIDIA/NeMo-Speech.cpp

Quantized using llama.cpp by [prithivMLmods](https://huggingface.co/prithivMLmods).