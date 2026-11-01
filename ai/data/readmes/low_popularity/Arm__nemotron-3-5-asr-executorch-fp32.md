---
display_name: Nemotron 3.5 ASR ExecuTorch FP32
license: openmdw-1.1
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
language:
  - en
  - es
  - de
  - fr
  - it
  - ar
  - ja
  - ko
  - pt
  - ru
  - hi
  - zh
  - vi
  - he
  - nl
  - cs
  - da
  - pl
  - 'no'
  - sv
  - th
  - tr
  - bg
  - el
  - et
  - fi
  - hr
  - hu
  - lt
  - lv
  - ro
  - sk
  - uk
  - mt
  - sl
pipeline_tag: automatic-speech-recognition
tags:
  - automatic-speech-recognition
  - executorch
  - streaming-asr
  - multilingual
  - fp32
---

<!--
SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
SPDX-License-Identifier: Apache-2.0
-->

# Nemotron 3.5 ASR ExecuTorch FP32

This package contains an [NVIDIA Nemotron 3.5 ASR Streaming 0.6B](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/tree/ea30d66debe3740a08b573244286791d423d6b3e) conversion for ExecuTorch CPU inference. It transcribes mono 16 kHz speech to text with a cache-aware streaming encoder, predictor, and joiner.

The model is provided in FP32 without model-specific optimizations. The packaged interface accepts a complete WAV recording and produces incremental text as it processes the audio in chunks.

## ✨ Key Highlights

- **Streaming ASR** — The packaged LA13 encoder uses a **1.12** s audio collection cadence.
- **FP32 reference** — The encoder, predictor, and joiner are unquantized ExecuTorch models.
- **Multilingual ASR** — Supports English, Spanish, French, German, and Mandarin, among other languages. See the [NVIDIA model card](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/blob/ea30d66debe3740a08b573244286791d423d6b3e/README.md#supported-languages) for the full locale list and support tiers.
- **Faster than real time** — On one Arm® CPU thread with the 9.96-second sample:
  - RTFx is **6.294** on the Android™ Vivo X300 smartphone.
  - RTFx is **15.369** on a MacBook Pro® computer with an M4 Pro chip.

## 📦 Model Details

### Model Description

Nemotron 3.5 ASR is a multilingual model with a cache-aware FastConformer encoder and an RNN-T decoder. This package contains the LA13 streaming encoder, predictor, joiner, and SentencePiece tokenizer. The manifest's `configs.language.value` defaults to `auto` for automatic language detection. Set it to a locale such as `en-US` to select that language. The selectable locale strings and their checkpoint prompt IDs are listed in [`assets/languages_to_prompt_ids.json`](assets/languages_to_prompt_ids.json); see the upstream model card for each locale's support tier.

When the spoken language is known, select its locale for better transcription accuracy. At the 1.12 s setting, the [upstream FLEURS results](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/blob/ea30d66debe3740a08b573244286791d423d6b3e/README.md#performance) report 8.84% average error with a supplied language and 9.21% with automatic detection. These results are for the original model, not this package.

- **Developed by:** NVIDIA
- **Base model:** [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/tree/ea30d66debe3740a08b573244286791d423d6b3e)
- **License:** [OpenMDW-1.1](https://openmdw.ai/license/1-1/), inherited from the upstream model
- **Packaged variant:** `nemotron-3-5-asr-executorch-fp32`
- **Precision:** FP32 model weights

### Model Sources

- [Pinned NVIDIA checkpoint and model card](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/tree/ea30d66debe3740a08b573244286791d423d6b3e)

## 🚀 Get Started with the Model

### Run with Compute Flow

Follow these steps to run Nemotron 3.5 ASR ExecuTorch FP32 on macOS® with Apple Silicon or on
Linux® with an Arm®-based CPU, such as a Raspberry Pi® 5.

#### Step 1: Clone Compute Flow and set up the virtual environment

```bash
git clone https://github.com/ARM-software/ComputeFlow.git && cd ComputeFlow

uv sync && source .venv/bin/activate
```

#### Step 2: Install the brick and model

```bash
compute-flow update
compute-flow model install stt:nemotron-asr nemotron-3-5-asr-executorch-fp32
compute-flow build native
```

#### Step 3: Run the Python CLI example

```bash
python -m cli_examples.stt_cli \
  -m @manifest/nemotron-asr/nemotron-3-5-asr-executorch-fp32/nemotron_3_5_la13_manifest.json \
  -a @sample/beckett.wav \
  -t 1
```

The example transcribes the bundled `samples/beckett.wav` recording. Replace `-a` with a path to
your own WAV file.

## 📊 Quality evaluation

No formal word error rate evaluation of the packaged FP32 files is included. The [upstream model card](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/tree/ea30d66debe3740a08b573244286791d423d6b3e) reports quality for the original model; those results do not measure this conversion.

## 🎯 Performance evaluation

Performance was measured under the following conditions:

- **Targets:** Vivo X300 smartphone running Android™ 16 and a MacBook Pro® computer with an M4 Pro chip running macOS® 26.6.2.
- **One** Arm® CPU thread.
- **5** warmups.
- **30** consecutive measured runs with no pause between runs.
- The Android™ smartphone screen was kept on; display sleep was prevented on the MacBook Pro® computer.
- The model remained loaded and its state was reset between runs.
- The benchmark used the `en-US` language prompt.

The following methodology and definitions were used:

- **Runtime:** ExecuTorch 1.5.0 with XNNPACK on CPU.
- **Input recording:** The distributed 9.963-second [`samples/beckett.wav`](samples/beckett.wav), mono 16 kHz audio.
- **End-to-end latency** is the complete speech-to-text execution time from the first model call through the final text chunk; it excludes model setup and WAV file reading.
- **Time to first text chunk** is the median elapsed inference time until the first non-empty transcription fragment is returned; a fragment may be shorter than a word.
- **Average memory** is the mean process RSS sampled every 0.2 seconds throughout setup and inference.
- **Peak memory** is the maximum sampled process high-water mark.

| Metric | Android™ Vivo X300: FP32 | MacBook Pro® M4 Pro: FP32 |
| :--- | ---: | ---: |
| Model size | 2593.7 MB | 2593.7 MB |
| RTFx | 6.294 | 15.369 |
| End-to-end latency, p50 | 1582.395 ms | 643.866 ms |
| End-to-end latency, p90 | 1593.147 ms | 665.075 ms |
| End-to-end latency, p99 | 1599.169 ms | 692.923 ms |
| Time to first text chunk | 351.686 ms | 142.509 ms |
| Peak memory | 2566.2 MiB | 2692.6 MiB |
| Average memory | 2499.4 MiB | 2468.5 MiB |

RTFx is the total input-audio duration divided by total inference time, so higher values indicate faster processing. The [Vivo X300 benchmark report](benchmarks/nemotron-3-5-asr-vivo-x300-baseline.yaml) records the Android™ measurement conditions and values.

## ⚠️ Known Limitations

- Only the LA13 encoder is packaged. Other upstream lookahead settings require separate exports and validation.

## 🛠️ Technical Specifications

### Objective

Transcribe speech to incremental text using the packaged LA13 streaming model.

### Runtime Architecture

| Component | Framework / format | Precision |
| :--- | :--- | :--- |
| Streaming encoder | ExecuTorch / PTE | FP32 |
| Predictor | ExecuTorch / PTE | FP32 |
| Joiner | ExecuTorch / PTE | FP32 |
| Tokenizer | SentencePiece model | Discrete tokens |

### Precision and Quantization

The encoder, predictor, and joiner use FP32 weights. No quantization is applied.

### Input Specification

| Input | Description |
| :--- | :--- |
| Audio recording | Mono 16 kHz WAV audio. |
| Language | `auto` by default, or a locale string from [`assets/languages_to_prompt_ids.json`](assets/languages_to_prompt_ids.json). |

### Output Specification

The model emits incremental transcription text, including punctuation and capitalization. Model-emitted language tags may appear in the text.

### Repository Contents

- `nemotron_3_5_la13_manifest.json` — package manifest.
- `encoder_streaming_la13_1120ms_tmel121.pte` — FP32 LA13 streaming encoder.
- `predictor.pte` — FP32 predictor.
- `joiner.pte` — FP32 joiner.
- `tokenizer.model` — SentencePiece tokenizer.
- `assets/languages_to_prompt_ids.json` — selectable locale strings and their checkpoint prompt IDs.
- `samples/beckett.wav` — sample audio used for the Android™ and macOS® benchmarks.
- `metadata.yaml` — model metadata.
- `SHA256SUMS` — package checksums.

## 🗂️ Model and Asset Origin

- The PTE models were converted from the pinned [NVIDIA checkpoint](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/tree/ea30d66debe3740a08b573244286791d423d6b3e). The tokenizer comes from the same upstream model.
- The language map uses prompt IDs from the pinned [NVIDIA processor config](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/blob/ea30d66debe3740a08b573244286791d423d6b3e/processor_config.json) for the locales listed in its model card.
- The model materials use [OpenMDW-1.1](https://openmdw.ai/license/1-1/); its full license text is reproduced below.
- `samples/beckett.wav` derives from the [Moonshine Beckett recording](https://github.com/moonshine-ai/moonshine-tflite/blob/378e2fbf12dbba531328c9bfe8d35334f8abcd9a/assets/beckett.wav). The bundled sample is mono 16 kHz float32 WAV. The source repository includes an [MIT LICENSE](https://github.com/moonshine-ai/moonshine-tflite/blob/378e2fbf12dbba531328c9bfe8d35334f8abcd9a/LICENSE), reproduced below; it does not identify separate rights for the recording.

## 📜 License

The following is the complete OpenMDW-1.1 agreement for the model materials.

```text
OpenMDW License Agreement, version 1.1 (OpenMDW-1.1)

By exercising rights granted to you under this agreement, you accept and agree
to its terms.

As used in this agreement, "Model Materials" means the materials provided to
you under this agreement, consisting of: (1) one or more machine learning
models (including architecture and parameters); and (2) all related artifacts
(including associated data, documentation and software) that are provided to
you hereunder.

Subject to your compliance with this agreement, permission is hereby granted,
free of charge, to deal in the Model Materials without restriction, including
under all copyright, patent, database, and trade secret rights included or
embodied therein.

If you distribute any portion of the Model Materials, you shall retain in your
distribution (1) a copy of this agreement, and (2) all copyright notices and
other notices of origin included in the Model Materials that are applicable to
your distribution.

If you file, maintain, or voluntarily participate in a lawsuit against any
person or entity asserting that the Model Materials directly or indirectly
infringe any patent or copyright, then all rights and grants made to you
hereunder are terminated, unless that lawsuit was in response to a
corresponding lawsuit first brought against you.

This agreement does not impose any restrictions or obligations with respect to
any use, modification, or sharing of any outputs generated by using the Model
Materials.

THE MODEL MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE, NONINFRINGEMENT, ACCURACY, OR THE
ABSENCE OF LATENT OR OTHER DEFECTS OR ERRORS, WHETHER OR NOT DISCOVERABLE, ALL
TO THE GREATEST EXTENT PERMISSIBLE UNDER APPLICABLE LAW.

YOU ARE SOLELY RESPONSIBLE FOR (1) CLEARING RIGHTS OF OTHER PERSONS THAT MAY
APPLY TO THE MODEL MATERIALS OR ANY USE THEREOF, INCLUDING WITHOUT LIMITATION
ANY PERSON'S COPYRIGHTS OR OTHER RIGHTS INCLUDED OR EMBODIED IN THE MODEL
MATERIALS; (2) OBTAINING ANY NECESSARY CONSENTS, PERMISSIONS OR OTHER RIGHTS
REQUIRED FOR ANY USE OF THE MODEL MATERIALS; OR (3) PERFORMING ANY DUE
DILIGENCE OR UNDERTAKING ANY OTHER INVESTIGATIONS INTO THE MODEL MATERIALS OR
ANYTHING INCORPORATED OR EMBODIED THEREIN.

IN NO EVENT SHALL THE PROVIDERS OF THE MODEL MATERIALS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE MODEL MATERIALS, THE
USE THEREOF OR OTHER DEALINGS THEREIN.
```

The Moonshine source repository includes this MIT license alongside the Beckett sample:

```text
MIT License

Copyright (c) 2025 Useful Sensors Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🔐 Checksums

`SHA256SUMS` covers every regular package file except itself and paths with a dotfile component.
Verify the checked-out files from the repository root with:

```sh
shasum -a 256 -c SHA256SUMS
```
