---
license: apache-2.0
language:
- en
- ko
base_model:
- google/gemma-4-E2B-it
tags:
- gemma4
- android
- qnn
- executorch
- speculative-decoding
- dflash2
- quantized
library_name: executorch
pipeline_tag: image-text-to-text
---

# Gemma4-E2B-Dflash2-Android

[English](README.md) | [한국어](README.ko.md)

**Experimental image bridge tested on S22.** Two synthetic color images
returned Red/Blue through CPU mmproj encoding and NPU verification. Target-only
and DFlash2 output matched; three text regressions had identical tokens and zero
native U16 logit error. This is limited validation, not broad vision certification.
See `vision-device-check.json` for the new measurements; historical text speeds
below are separate records.

This package prepares Google Gemma 4 E2B instruction-tuned assets and a locally
trained **Z Lab DFlash2-derived** drafter for Android CPU drafting with Qualcomm
NPU block verification. It is designed for the app-independent
[RaInfer engine](https://github.com/LEPTONNW/RaInfer), not a particular application.
No app, APK, proprietary SDK or QNN runtime libraries are included.

## Start here: engine and required runtime files

**Engine Git repository: [LEPTONNW/RaInfer](https://github.com/LEPTONNW/RaInfer).** Build its Android runner
using the [build guide](https://github.com/LEPTONNW/RaInfer/blob/main/docs/BUILD.md). The complete
[download/startup checklist](https://github.com/LEPTONNW/RaInfer/blob/main/docs/MODEL_FILES.en.md) is also available
in the engine repository. This package provides data for that engine.

Download **all eight files below into `npu/`**, keeping filenames unchanged:

| Component | File | Role |
|---|---|---|
| Gemma target | [gemma4-e2b-dflash2-vision-verify-2k.pte](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/gemma4-e2b-dflash2-vision-verify-2k.pte) | NPU verifier, about 3.36 GB; also accepts ordinary text requests |
| Target contract | [io-contract.vision.json](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/io-contract.vision.json) | Matching target IO, quantization and image contract |
| Draft body | [cpu-body-fp32.bin](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/cpu-body-fp32.bin) | FP32 CPU draft computation |
| Draft embedding | [embedding-cpu-fp32.pte](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/embedding-cpu-fp32.pte) | CPU token embeddings |
| Draft output head | [head-cpu-int8.bin](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/head-cpu-int8.bin) | CPU INT8 vocabulary projection |
| Draft selector | [selector-cpu-fp32.bin](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/selector-cpu-fp32.bin) | Candidate selection |
| Draft vocabulary | [active-vocabulary.u32](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/active-vocabulary.u32) | Active draft vocabulary |
| Draft manifest | [draft-manifest.json](https://huggingface.co/RoundRobin237/Gemma4-E2B-Dflash2-Android/resolve/main/npu/draft-manifest.json) | Draft filenames, architecture and hashes |

The six draft files form one runtime bundle; weights are not embedded inside
RaInfer or the Gemma target. The embedding `.pte` executes on **CPU**, whereas
the Gemma target `.pte` executes on **NPU**. The target uses mixed W4/W8 weights.

Also obtain `tokenizer/tokenizer.json`, `tokenizer/tokenizer_config.json`,
`tokenizer/chat_template.jinja` and `tokenizer/config.json` for your host's
prompt formatting and token encoding/decoding. With the Hugging Face CLI:

```sh
hf download RoundRobin237/Gemma4-E2B-Dflash2-Android --include "npu/*" --include "tokenizer/*" --local-dir ./model-assets
```

This fetches the approximately 4 GB runtime bundle, including additional
weightless tokenizer GGUFs. It excludes BF16 and the full Q4 GGUF, which are
optional training/conversion/reference formats. DFlash2 is a separate six-file
CPU bundle, not embedded in the Gemma PTE or engine. N-gram needs no extra model.

After building the runner and preparing the matching QNN/ExecuTorch runtime on
Android, run from `model-assets/` with the executable on PATH:

```sh
mobile_runner --serve npu/gemma4-e2b-dflash2-vision-verify-2k.pte npu/cpu-body-fp32.bin npu/draft-manifest.json npu/io-contract.vision.json
```

Your app waits for ready and sends templated token IDs through stdin JSONL.
See the [protocol](https://github.com/LEPTONNW/RaInfer/blob/main/docs/PROTOCOL.md) and
[app integration](https://github.com/LEPTONNW/RaInfer/blob/main/docs/INTEGRATION.md).
For images only, add `tokenizer/gemma4-e2b-vision-vocab.gguf`, the separately
built CPU image encoder and the **external** mmproj described in
`external-assets.json` / the [image guide](https://github.com/LEPTONNW/RaInfer/blob/main/docs/VISION.md).
The CLI command above already includes the weightless vision vocabulary.
Text-only generation uses the same target PTE without mmproj. Other Qualcomm
architectures require their own validation; the reference target is SM8450/v69,
QAIRT 2.37.0.250724 and fixed 2K context. No application/APK or SDK/runtime is
bundled here.

## Choose the files for your backend

| Directory | Contents / purpose |
|---|---|
| `original-bf16/` | Unmodified Google BF16 safetensors and configuration, including original multimodal weights |
| `q4-gguf/` | Unmodified Unsloth Q4_K_M GGUF, for a compatible llama.cpp backend/reference |
| `npu/` | Experimental vision-enabled mixed W4/W8 QNN/ExecuTorch target PTE; CPU DFlash2 body, embedding, output head, selector, vocabulary and manifests |
| `external-assets.json` | Upstream F16 mmproj URL/hash; **mmproj is not redistributed here** |
| `tokenizer/` | Matching tokenizer, conversation template and weightless GGUF metadata |
| Root JSON | File hashes, source lineage, quantization, hardware and measured historical benchmarks |

These are different formats, not three interchangeable runtime files. The Q4
GGUF is not the NPU verifier. The CPU drafter is tied to the compiled target's
feature taps and export contract; copying it beside an arbitrary GGUF does not
enable DFlash2. Download the directories needed for your backend rather than
assuming all formats must remain resident simultaneously.

Google names this variant **E2B**. The original multimodal safetensors contain
5,123,178,979 stored parameters across 2,011 BF16 tensors, not simply two billion
stored values. The source includes audio and vision; this bridge supports one
static image, not audio/video. The NPU target remains a fixed **2,048-position**
decoder. Images consume part of that budget.

## Actual text measurements on Galaxy S22 Ultra

These records are from 2026-10-15 and precede public source packaging and the
vision bridge. They use the existing text target. They are not new measurements
of the published source revision or promises of sustained performance.

| Historical prompt | N-gram | Output tokens | Accepted / proposed | Generation t/s |
|---|---:|---:|---:|---:|
| Small Java example | off | 72 | 42 / 90 | 19.0963 |
| Korean meeting-note request | off | 52 | 14 / 114 | 10.7347 |
| English meeting-note request | off | 49 | 3 / 138 | 8.6995 |
| Same Java prompt, another run | on | 72 | 42 / 90 | 19.9379 |

The 19.9379 t/s sample is the maximum among the 14 retained records; it is not
the cross-prompt average. Identical accepted/proposed counts do not establish
that n-grams caused that timing difference. A later session's corresponding Java
sample was 15.6789 t/s. Temperature, foreground scheduling, heat and run conditions
matter. **The 25–30 t/s goal has not been achieved.** See `benchmark.json` for all
14 measured records, exact timing and acceptance definitions.

The app-level historical metric was completion tokens / generation duration,
excluding prefill and model loading. In the native runner,
`decode_tokens_per_second` excludes the first prefill-produced token from its
numerator. Do not compare those counters without aligning their definitions.
The first Java sample had 70 prompt tokens, 2.244620259 s prefill and
3.770364686 s generation. These are small single-request examples, not a
large-context throughput benchmark.

## Tested device and selected text settings

- Galaxy S22 Ultra **SM-S908N**, Snapdragon 8 Gen 1 **SM8450**, marketed 12 GB RAM.
- CPU: 4 Cortex-A510 efficiency cores, 3 Cortex-A710 performance cores and
  1 Cortex-X2 prime core. The engine requests performance-cluster execution.
  Android cpuset rules may limit which cores are actually available.
- GPU: **Adreno 730**. It is present but **not used in the selected text baseline**;
  experimental GPU draft-head/offload paths did not improve the selected result.
- NPU: **Hexagon HTP v69**, executing QNN graphs through ExecuTorch Qualcomm backend.
- Android 16 / API 36; actual tested page size 4 KiB.
- QAIRT/QNN **2.37.0.250724**, Android NDK **29.0.14206865**,
  ExecuTorch `ca56e1ffdba1c902d9202021d7297982d3501439`.

Selected text settings: greedy / temperature 0, target context 2K, verification
width 4 (one pending token plus three draft candidates), CPU output-head workers
4, CPU body workers 1, fast argmax and compact logits enabled, n-gram enabled,
GPU head off, burst vote off, fixed per-worker affinity off, profiling off.
The 19.0963 t/s reference sample used n-gram **off**. All device clocks and thermal
conditions were not logged for every historical sample; no advertised TOPS value
is used to infer a measured throughput.

## Quantization and drafter provenance

The NPU target is **not pure 4-bit**: mixed block-32 W4 FFN weights, selected W8
projections/tail paths, 16-bit activation boundaries and KV state. See
`quantization.json` for the retained conversion recipe. Twelve QNN delegates
are used. Sensitive paths were retained at higher precision during earlier
quality work. Original BF16 files and the separately sourced Q4_K_M GGUF remain
unmodified.

The locally trained drafter has hidden size 384, 3 layers, intermediate size
1,536, 512-token context, four feature taps `[3,13,23,33]`, vocabulary 262,144,
and a three-candidate/AR4 runtime. Selected checkpoint step: **1,100**. Its CPU
body uses FP32, the output head uses per-row INT8 weights with dynamic per-query
INT8 activations, and the selector uses a native FP32 path. It is not an official
Google MTP or an official Z Lab checkpoint. No claim of compatibility with
arbitrary public DFlash/DFlash2 weights is made.

**Z Lab attribution:** algorithmic components and grouped dynamic-convolution /
selection implementation are derived from
[z-lab/dflash](https://github.com/z-lab/dflash), revision
`07ebd93db9f472af339b644bb70221ad8428328a` (MIT, Copyright 2026 Z Lab).
RaInfer's target verification, transaction/cache management and mobile wiring
are local implementations. Training data and intermediate checkpoints are not
included. `dflash2-lineage.json` and `provenance.json` retain the source record.

## Using the files with another app

Follow RaInfer's [build guide](https://github.com/LEPTONNW/RaInfer/blob/main/docs/BUILD.md),
[process protocol](https://github.com/LEPTONNW/RaInfer/blob/main/docs/PROTOCOL.md),
and [integration guide](https://github.com/LEPTONNW/RaInfer/blob/main/docs/INTEGRATION.md).
An app owns tokenization, local file installation, foreground execution,
deadlines, process lifetime and UI. No specific app is required.

The image path requires the vision-enabled runtime, matching experimental PTE
and IO contract, CPU mmproj encoder and weightless tokenizer metadata. Read
[the image guide](https://github.com/LEPTONNW/RaInfer/blob/main/docs/VISION.md)
before using it. Encode the formatted image/prompt into a local bundle, then
send the bundle to the persistent worker via JSONL. Ordinary text requests
remain token-ID based. The mmproj is F16, not a QNN graph. Image encoding,
target prefill and generation must be timed separately.

The SDK/runtime are **not** bundled. Obtain compatible dependencies under their
applicable licenses. A different Qualcomm SoC, HTP architecture, SDK, OS or page
size may need a separate conversion/build. This is not an all-Android binary.

After building RaInfer and arranging the matching licensed runtime, start the
worker with package-relative asset paths:

```sh
mobile_runner --serve npu/gemma4-e2b-dflash2-vision-verify-2k.pte \
  npu/cpu-body-fp32.bin npu/draft-manifest.json npu/io-contract.vision.json
```

The mmproj is an **external dependency**, not our own conversion. Google provides
the [original vision weights](https://huggingface.co/google/gemma-4-E2B-it), and
the exact tested GGUF is
[Unsloth's mmproj-F16.gguf](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/0314792d7f1f7e229411f620751375812bb9faf2/mmproj-F16.gguf).
Download it there and save it locally as `external/mmproj-F16.gguf`; verify
SHA256 `140be8d7849741f88c50757d529b84373ee8e27052cc2236855b537f4a8215fa`.
The URL, pinned revision and size are also in `external-assets.json`.

For images, use RaInfer's local-template prompt tool, then encode on the same
device that can access the files:

```sh
python tools/make_vision_prompt.py --tokenizer-dir tokenizer \
  --prompt "What is the dominant color in the image? Answer with one color word." \
  --output image-prompt.txt
rainfer_vision_encoder --text-model tokenizer/gemma4-e2b-vision-vocab.gguf \
  --mmproj external/mmproj-F16.gguf --image input.png --prompt-file image-prompt.txt \
  --output session/input.bundle.json --threads 4 --image-max-tokens 256
```

Wait for the worker's ready event, then send one JSON line to its stdin:

```json
{"id":1,"vision_bundle":"/absolute/path/session/input.bundle.json","max_new_tokens":64,"cpu_workers":4,"body_workers":1,"fast_argmax":true,"compact_logits":true,"ngram":true,"gpu_head":false}
```

Output events start with `@DFLASH2 `. Read `report.tokens` and detokenize using
the matching tokenizer. For text-only requests, pass a correctly templated
`tokens` array instead of `vision_bundle`. Do not send both. The Python prompt
tool is a PC-side preparation option; a phone app can apply the same template
locally without Python. None of the commands downloads SDKs automatically.

## Licensing, changes and limits

Distributed model weights are under **Apache-2.0**; the Google Gemma 4 source is
Apache-2.0, rather than the earlier Gemma-specific license. Google retains its
copyright. The unmodified Q4 GGUF comes from Unsloth's Apache-2.0 repository;
mmproj is linked upstream rather than redistributed here. Conversion,
mixed quantization, compiled graph packaging, feature
outputs, vision operator alias and local drafter training are modifications by
the package author, not an official Google/Qualcomm release.

RaInfer and llama.cpp/mtmd code are MIT; Z Lab DFlash code is MIT; ExecuTorch is
BSD-3-Clause. Their notices are separate and preserved in `NOTICE` / `licenses/`.
Apache-2.0 for weights does not relicense SDKs or linked engine dependencies.
No endorsement is implied. Current checks cover a few examples and greedy
regressions; they do not certify general answer quality, code correctness,
safety, multilingual competence or universal device compatibility.

## New image-bridge device check

On the same S22, four workers were requested but observed CPU masks varied:
**4–5,7** around target-only runs, **4,6–7** before the persistent run and
**4–7** after it. Thermal status before the persistent run was `2`; these are
state snapshots, not continuously recorded clocks or core availability.
With 49 prompt tokens and a 145-token Java
answer, original target-only / vision-target-only / vision-target+DFlash2 measured
**6.9460 / 6.9749 / 15.5555 native decode t/s**, respectively. DFlash2 accepted
83/183 candidates (45.36%). Output tokens matched; the code compiled and printed
`12`. Native decode counts 144 post-prefill tokens here. These settings/prompts
and metric differ from the historical app-level records.

For 224x224 red/blue images, CPU encoding took **9.4474 / 9.4604 s**, encoder
loading **3.2702 / 3.1627 s**, and target-only NPU prefill **3.4431 / 3.4776 s**.
Both images used 64 projected rows in a 95-token prompt. Image answers were only
one color word plus EOS; 0/3 draft candidates were accepted in each single
post-prefill round. This tiny output is not a long-answer speed/acceptance test.
Image→Java→other-image→first-image repetition passed state isolation checks.
No OCR, photographs or complex visual reasoning have been certified.
