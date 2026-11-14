---
license: other
license_name: openmdw-1.1
license_link: LICENSE
base_model:
  - nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
language:
  - ar
  - bg
  - bn
  - cs
  - da
  - de
  - el
  - en
  - es
  - et
  - fi
  - fr
  - he
  - hi
  - hr
  - hu
  - id
  - it
  - ja
  - ko
  - lt
  - lv
  - mr
  - mt
  - nl
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - sv
  - ta
  - te
  - th
  - tl
  - tr
  - uk
  - vi
  - zh
tags:
  - gguf
  - ggml
  - speech.cpp
  - nemotron-transcribe
---

# Nemotron 3.5 Transcribe GGUF for speech.cpp

These files run only in [speech.cpp](https://github.com/nyosegawa/speech.cpp) 0.9.1 or later, and tell speakers and
time words in 0.9.2 or later. Their layout is speech.cpp's own, so llama.cpp, LM Studio, Ollama and other GGUF readers
cannot run them.

Each holds NVIDIA's [Nemotron 3.5 Transcribe](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B), a
speech model of 30B parameters with 4B active: its log-mel frontend, its Transformer ASR encoder, its speaker branch and
the fusion of the two, and its language model, a mixture of experts of Mamba-2, attention and MoE layers, with its
tokenizer, and its CTC timestamp head. It writes speech word for word in 40 languages, as they are spoken, fillers and
repetitions included, with punctuation and capitals, takes up to an hour of audio at once, can be told the names and
terms the audio holds, and tells who speaks and when each word is said.

## Use

[Install speech.cpp](https://github.com/nyosegawa/speech.cpp#install), then:

```sh
speech asr nemotron-3.5-transcribe meeting.wav
speech asr nemotron-3.5-transcribe --prompt "Nemotron, FLEURS" meeting.wav    # names and terms the audio holds
speech asr nemotron-3.5-transcribe --speakers meeting.wav                     # FILE, START, END, SPEAKER, TEXT
speech asr nemotron-3.5-transcribe --timestamps --format json meeting.wav     # each word's start and end
speech asr nemotron-3.5-transcribe --vad silero-vad --diarize nemotron-3-diarization meeting.wav
speech serve nemotron-3.5-transcribe silero-vad                                # OpenAI's transcription API
```

The name `nemotron-3.5-transcribe` fetches the IQ4_NL file the first time it is used, and `nemotron-3.5-transcribe:f16` or `nemotron-3.5-transcribe:q8_0` another; a path to a downloaded file works as well. speech.cpp's documentation has the
[model's page](https://github.com/nyosegawa/speech.cpp/blob/main/docs/models/nemotron-transcribe.md), the
[command line](https://github.com/nyosegawa/speech.cpp/blob/main/docs/cli.md) and the
[server](https://github.com/nyosegawa/speech.cpp/blob/main/docs/server.md).

The model is given the model card's verbatim instruction, its contextual one with the terms of a request's prompt, or
with `--speakers` its prompt for speaker tags, which become each segment's speaker. `--timestamps` times each word, or
each character of Japanese and Chinese, by the checkpoint's CTC head as NeMo's alignment times it. The card's other
tasks (translation, questions about the audio) are not offered. The files hold the checkpoint's multi-token prediction
layers too, which speech.cpp does not load.

## Files

| File | What it holds | Size | SHA-256 |
|---|---|---|---|
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-F16.gguf` | the model in F16 | 67.42 GB (67,422,535,296 bytes) | `b99a4737eba6efc5d2d56eb294e90ee04b643a87f5e10bd8bbfda7b677ff3bc4` |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0.gguf` | the model in Q8_0 | 35.84 GB (35,840,811,776 bytes) | `d348a74dad222c96f1b6c7f6a117ede9d56fbc01cfa57c4b54606934e9b1deec` |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ4_NL.gguf` | the model in IQ4_NL, which the name fetches | 19.00 GB (18,997,225,856 bytes) | `9688cee08c96ee0f54c0cc1cb07856307a79097fb0088cdb8fb31de6dd26c2be` |
| `<file>.json` | what `speech info --json` prints of each file | | |
| `LICENSE` | the OpenMDW License Agreement, version 1.1, with NVIDIA's copyright notice, as the upstream repository has it | | |

In every type the frontend, the norms, the biases, the routers, the Mamba layers' convolutions and decays, the speaker
head and the fusion's kernel are F32, and every other matrix and embedding takes the file's type. The language model's
rows of 2688 and 1856 values are not whole blocks of a K-quant's 256, so the files come in IQ4_NL, of 4.5 bits a
weight, rather than Q4_K. The model needs its whole file in memory: a GPU that holds it computes it all, as an Apple
M5 with 32 GB does with the IQ4_NL file, and a GPU that does not keeps the experts of as many layers as its free memory
holds while the CPU computes the others, more slowly.

## Accuracy

Each stage is checked against NeMo at commit `040574f`, the official modules and Transformers' NemotronH, on seven
requests made of FLEURS clips: a Japanese and an English utterance, a meeting of 98 s with five voices, pauses and
overlaps, and quiet noise, given the card's verbatim, contextual, plain and speaker-tag instructions.

| Check | F32 on the CPU | F32 on an Apple M5's GPU (Metal) |
|---|---|---|
| The audio's rows the language model takes | 79.2 dB SNR | 52.3 dB SNR |
| The language model's 52 layers, each from its own input, over the prompt and the first decoded tokens | 115.4 dB over the prompt, 97.4 dB decoding | 67.8 dB over the prompt, 74.0 dB decoding |
| The recognition of the five requests of the verbatim and contextual instructions, through the C API | the official tokens and text of every one | |
| The times of 2,573 words of the requests' transcripts, from the audio through the CTC head and NeMo's alignment | NeMo's times for every word | NeMo's times for all but 10 |

Where two experts of a layer score within float32's rounding of each other, the port may choose the other, as the
official code may on another machine; the check leaves such rows out and counts them: 45 of 76,521 on the CPU and
1,550 on Metal, whose matrix kernels round their inputs to half precision.

Each type, measured by speech-bench on 2026-10-29 on an H100 with Vulkan: the first 100 utterances of FLEURS's Japanese
and English test sets and the whole of Common Voice 8.0's Japanese test set (4,479 utterances the voice detector kept),
trimmed to the voice, with the model card's verbatim instruction. The CER after the slash accepts other spellings of
the same words. IQ4_NL is within 0.2 points of Q8_0 on every set, which is why the name fetches it. On an
Apple M5 with Metal, the IQ4_NL file gives 6.11% / 2.82% on FLEURS ja and 8.68% on FLEURS en.

| Type | FLEURS ja CER | Common Voice ja CER | FLEURS en WER |
|---|---|---|---|
| F16 | 6.05% / 2.64% | 8.85% / 5.06% | 8.73% |
| Q8_0 | 5.86% / 2.64% | 9.01% / 5.17% | 8.64% |
| IQ4_NL | 5.88% / 2.62% | 9.16% / 5.33% | 8.77% |

## Speed

speech-bench on 2026-10-29, one utterance at a time through `speech worker`, on the first 100 utterances of FLEURS's
Japanese and English test sets and of Common Voice 8.0's Japanese test set, trimmed to the voice. The RTFx is the
seconds of audio over the seconds they took, so larger is faster; the memory is the process's on the M5, whose GPU
shares it, and the GPU's on the H100.

| Device | Type | p50 latency, FLEURS ja / CV ja / FLEURS en | RTFx | Memory | Load |
|---|---|---|---|---|---|
| Apple M5 (32 GB), Metal | IQ4_NL | 1.29 s / 0.61 s / 0.88 s | 7.0 / 5.4 / 8.5 | 17.2 GiB | 5 to 6 s |
| H100 (80 GB), Vulkan | IQ4_NL | 0.39 s / 0.22 s / 0.29 s | 24 / 13 / 26 | 18.4 GiB | 7 s |
| H100 (80 GB), Vulkan | Q8_0 | 0.39 s / 0.22 s / 0.29 s | 23 / 15 / 26 | 33.4 GiB | 13 to 14 s |
| H100 (80 GB), Vulkan | F16 | 0.53 s / 0.25 s / 0.39 s | 17 / 13 / 20 | 61.6 GiB | 24 s |

On an RTX 2080 (8 GB) with Vulkan and an i9-9900K, the IQ4_NL file leaves the experts of 18 of its 23 layers of
experts to the CPU: `speech asr` wrote 9 s of English in 3.2 s and a 98 s meeting in 46 s, with 6.1 GiB of the GPU's
memory and 13 GB of the CPU's.

## Source

Converted by speech.cpp's
[`reference/nemotron-transcribe/convert.py`](https://github.com/nyosegawa/speech.cpp/tree/main/reference/nemotron-transcribe)
from [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)
at revision `ef905575a106fdad904f3b0ce661dccad654607d` to F32, from which `speech quantize --type <type>` wrote each
file. The checks compare it with NeMo at commit `040574f7ffa3bb0ae4b92aa8424ecea454d03c91`.

## License

Nemotron 3.5 Transcribe is NVIDIA's, released under the
[OpenMDW License Agreement, version 1.1](https://openmdw.ai/license/1-1/), which `LICENSE` holds with NVIDIA's copyright
notice as the upstream repository has it. These files are distributed under that agreement. NVIDIA's model card has the
model's ethical considerations and its subcards on bias, explainability, safety and privacy.
