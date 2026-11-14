---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
base_model_relation: quantized
quantized_by: maternion
pipeline_tag: automatic-speech-recognition
library_name: gguf
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
tags:
- gguf
- llama.cpp
- nemotron-3.5
- nemotron_h_moe
- asr
- speech-to-text
- speaker-diarization
- audio
- multilingual
- mixture-of-experts
---

# NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF: IQ2/3_NL

GGUF conversion of [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B).
All credit for the model goes to NVIDIA; the OpenMDW-1.1 license carries over unchanged.

> [!TIP]
> The **IQ2_NL** and **IQ3_NL** files are the headliner of this repo and are not in any other public Nemotron-3.5-Transcribe GGUF. Open the **Files & versions** tab above to download them directly; the `blk52_tiered.txt` override used to build them is in the same listing.

## What this repo adds: IQ2_NL and IQ3_NL

The headliner is **IQ2_NL and IQ3_NL** quants, the missing 2- and 3-bit tiers for this model. They come from [llama.cpp PR #27983](https://github.com/ggml-org/llama.cpp/pull/27983) (EAddario, `iq2_nl-iq3_nl-cpu+metal+cuda+vulkan`), which adds two block-32 importance-matrix non-linear quants to llama.cpp. That PR is still **open** and not upstream, so the IQ2_NL/IQ3_NL types live only on this fork's maintained branch (see below).

Why they matter for this model specifically: Nemotron-H's matmul row widths are 2688, 1856 and 3712, none of which are divisible by 256. K-quants (Q4_K_M, Q6_K, IQ4_XS, Q3_K_M/S) and the IQ4_XS grid types use 256-element super-blocks, so only 54 of 289 matrices can take them and the rest silently fall back to Q5_0/Q8_0. The file ends up larger than the nominal bpw and the label misleads. IQ2_NL and IQ3_NL use block 32, so they fit these dims natively and the imatrix actually does something.

They fill the gap between Q2_0 and IQ4_NL that nothing else covers cleanly:

- Q2_0: ~9.7 GB, 2.25 bpw
- IQ2_NL: 10.68 GB, 2.59 bpw
- IQ3_NL: 14.69 GB, 3.58 bpw
- IQ4_NL: ~18.7 GB, 4.5 bpw

IQ3_NL in particular is the tier that makes Nemotron Transcribe usable on 16 GB GPUs, which neither Q2_0 (too aggressive) nor IQ4_NL (too big) do cleanly. AtomicChat and sakasegawa, the two dominant community publishers for this model, both avoid K-quants for the same divisibility reason and ship IQ4_NL + Q8_0; this repo adds the IQ2_NL/IQ3_NL tiers on top of that.

> [!IMPORTANT]
> **The Nemotron 3.5 Transcribe audio path ([PR #31471](https://github.com/ggml-org/llama.cpp/pull/31471)) merged into llama.cpp master on 2026-11-03.** Current master builds can run transcription with the Q8_0 / IQ4_NL / Q2_0 files and the `mmproj` audio encoder; no fork build is needed for those anymore.
> **The IQ2_NL and IQ3_NL types ([PR #27983](https://github.com/ggml-org/llama.cpp/pull/27983)) are still open and not upstream.** The IQ2_NL/IQ3_NL files in this repo require llama.cpp built from this fork's maintained branch [`nemo-transcribe-iq23nl`](https://github.com/maternion/llama.cpp/tree/nemo-transcribe-iq23nl), which we keep merged onto current master so it carries both the merged audio path and the IQ2_NL/IQ3_NL quant types. Use that branch for the IQ2_NL/IQ3_NL files. Released llama.cpp builds, Ollama and LM Studio cannot run the IQ2_NL/IQ3_NL files yet.

## Model summary

Nemotron 3.5 Transcribe is an open-weight offline speech and audio model: 40 languages, recordings up to one hour, 65,536-token context, speaker attribution, and prompt-context control for transcription style. It pairs a hybrid mixture-of-experts decoder (30B total, ~4.3B active including the audio encoder) with a NeMo speech encoder.

- Text decoder: `nemotron_h_moe`, 53 blocks, MTP/NextN block included
- Audio encoder: NeMo ParallelExpertEncoder (ASR transformer plus a streaming speaker/diarization model), exported as a separate `mmproj` file
- Offline transcription with speaker labels and prompt context; word timestamps and streaming are out of scope for PR #31471

See the [model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) and the [technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) for architecture and evaluation details.

## Available files

| File | Type | Size |
|---|---|---|
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0.gguf` | Q8_0 (~8.5 bpw, near-lossless) | 35.00 GB |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ4_NL.gguf` | IQ4_NL (~4.5 bpw, imatrix-weighted) | 18.73 GB |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ3_NL.gguf` | IQ3_NL (~3.6 bpw, imatrix-weighted) | 14.90 GB |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ2_NL.gguf` | IQ2_NL (~2.6 bpw, imatrix-weighted) | 11.02 GB |
| `NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q2_0.gguf` | Q2_0 (~2.25 bpw, ternary-model format) | 9.72 GB |
| `mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-F16.gguf` | F16 audio encoder plus speaker model | 1.47 GB |
| `mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-BF16.gguf` | BF16 audio encoder plus speaker model | 1.47 GB |
| `mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-Q8_0.gguf` | Q8_0 audio encoder plus speaker model (experimental) | 782 MB |

> [!NOTE]
> The `mmproj` file is required next to any text quant for transcription. The F16 file is the standard; the BF16 and Q8_0 variants are non-standard, so verify they load in your mtmd build before relying on them. All text files were made with llama.cpp's own presets. IQ4_NL, IQ3_NL and IQ2_NL are quantized with [AtomicChat's published importance matrix](https://huggingface.co/AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-imatrix.gguf) (text calibration, 1.5M tokens, `--process-output` off, MTP/NextN off).

**Recommendation:** Q8_0 is effectively lossless. IQ4_NL is the validated default 4-bit (PR #31471 reports LibriSpeech test-clean WER 1.02 vs 1.03 for Q8_0). IQ2_NL is the smallest imatrix-weighted option. Q2_0 is even smaller but uses a block-max scale with no importance matrix path (it was added for ternary Bonsai models), so expect quality loss on a dense BF16 decoder.

## Build the patched llama.cpp

You only need this fork build for the **IQ2_NL and IQ3_NL** files. The Q8_0 / IQ4_NL / Q2_0 files and the `mmproj` audio encoder run on current llama.cpp master now that PR #31471 is merged.

```bash
git clone --branch nemo-transcribe-iq23nl https://github.com/maternion/llama.cpp && cd llama.cpp
cmake -B build -DGGML_VULKAN=ON
cmake --build build -j --target llama-mtmd-cli llama-quantize llama-server
```

The branch is kept merged onto current master, so one build gets both the upstream Nemotron Transcribe support and the IQ2_NL/IQ3_NL types. For CUDA builds use `-DGGML_CUDA=ON` instead of `-DGGML_VULKAN=ON` (or both).

## How it was made

Three-step pipeline, all from the `nemo-transcribe-iq23nl` build:

1. `convert_hf_to_gguf.py --remote` streamed the BF16 safetensors from the Hub into a BF16 GGUF. No `.safetensors` copy was written to disk. The conversion accepts the BF16 checkpoint layout only; the FP8 and NVFP4 releases are rejected by design.
2. The same converter with `--mmproj` produced the F16 audio encoder file. The BF16 and Q8_0 mmproj variants come from re-running `--mmproj` with `--outtype bf16` / `--outtype q8_0`.
3. `llama-quantize` produced each text quant from the BF16 intermediate. IQ4_NL, IQ3_NL and IQ2_NL are quantized with `--imatrix` pointing at AtomicChat's imatrix file. The IQ2_NL and IQ3_NL runs also pass `--tensor-type-file blk52_tiered.txt` (included in this repo) because AtomicChat's imatrix was computed with MTP off and has no entries for blk.52 (the MTP/NextN draft block), which makes the strict very-low-bit path bail. The override keeps blk.52 one tier above the body — `nextn.eh_proj` at Q8_0, attention and shared-expert weights at Q5_1, routed-expert weights at IQ4_NL, routers and norms at F32 — matching the consensus layout used by other MTP GGUF publishers (unsloth, Kujira) of holding the draft head above the body bitrate. See `blk52_tiered.txt` for the exact per-tensor mapping.

```bash
# 1. BF16 GGUF via --remote (no .safetensors on disk)
python convert_hf_to_gguf.py --remote nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B \
    --outtype bf16 \
    --outfile NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-bf16.gguf

# 2. audio encoder as a separate mmproj (F16, BF16, or Q8_0)
python convert_hf_to_gguf.py --remote nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B \
    --mmproj --outtype f16 \
    --outfile mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-F16.gguf

# 3. BF16 -> quantized with llama-quantize from the PR build
#    IQ4_NL needs only the imatrix; IQ2_NL/IQ3_NL also need the blk52 tiered override
./build/bin/llama-quantize \
    --imatrix NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-imatrix.gguf \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-bf16.gguf \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ4_NL.gguf IQ4_NL

./build/bin/llama-quantize \
    --imatrix NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-imatrix.gguf \
    --tensor-type-file blk52_tiered.txt \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-bf16.gguf \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ3_NL.gguf IQ3_NL

./build/bin/llama-quantize \
    --imatrix NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-imatrix.gguf \
    --tensor-type-file blk52_tiered.txt \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-bf16.gguf \
    NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ2_NL.gguf IQ2_NL
```

## Validation reported by the implementation PR

PR #31471 ships its own validation, measured with that build and an F16 `mmproj`, temperature 0:

| Metric | Q8_0 | IQ4_NL | BF16 (model card) |
|---|---|---|---|
| LibriSpeech test-clean WER (2,620 utts) | 1.03 | 1.02 | 1.09 |
| AMI IHM test cpWER (16 full meetings, 8.8 h) | 9.91 | 10.38 | 10.29 |

These numbers describe the PR author's files and settings, not independent measurements of the files in this repo. The IQ4_NL row used no imatrix; the file here uses AtomicChat's imatrix, which should be equal or better on text positions (audio positions are not represented in a text-only calibration).

## Usage

```bash
# transcription
./build/bin/llama-mtmd-cli \
    -m NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ3_NL.gguf \
    --mmproj mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-F16.gguf \
    --audio sample.wav

# server
./build/bin/llama-server \
    -m NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-IQ3_NL.gguf \
    --mmproj mmproj-NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-F16.gguf \
    --reasoning off
```

Long recordings are encoded in 40 s core windows with 4 s of context on each side (graphs up to 48 s), and a speaker cache plus FIFO is carried between windows so speaker labels stay consistent across the whole recording.