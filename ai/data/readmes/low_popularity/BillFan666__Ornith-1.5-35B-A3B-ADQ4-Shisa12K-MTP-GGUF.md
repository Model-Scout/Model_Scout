---
license: other
license_name: mit-target-plus-apache-2.0-mtp
base_model:
  - ornith-ai/Ornith-1.5-35B-A3B
  - AtomicChat/Ornith-1.5-35B-A3B-GGUF
  - shisa-ai/Ornith-1.5-35B-A3B-MTP-ONLY
library_name: llama.cpp
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - qwen35moe
  - mixture-of-experts
  - speculative-decoding
  - mtp
  - quantized
  - blackwell
language:
  - en
  - zh
  - ja
  - ko
---

# Ornith 1.5 35B A3B AD-Q4 + Shisa 12K MTP GGUF

Single-file language-model GGUF combining AtomicChat's model-specific
`AD-Q4_K-IQ4_XS` Ornith target with Shisa's 12K KL-distilled MTP head, quantized
to `Q4_0`. It was assembled and tuned for `llama.cpp` on an NVIDIA RTX 5060 Ti
16 GB while retaining the model's full 262,144-token context allocation. The
file itself does not contain a vision projector; compatibility with the
official external Ornith BF16 `mmproj` is documented and verified below.

中文摘要：这是 AtomicChat AD-Q4 主模型与 Shisa 12K 蒸馏 MTP 头的单文件
GGUF 合并版。README 下面完整记录了权重来源、版本、量化/合并方法、运行补丁、
262K 配置，以及 RTX 5060 Ti 16GB 的实测速度和显存边界。

> [!IMPORTANT]
> This is a community-built derivative, not an official release from Ornith,
> AtomicChat, or Shisa. Use a recent llama.cpp build with `qwen35moe` MTP
> speculative-decoding support.

## File

| File | Size | Contents |
| --- | ---: | --- |
| `Ornith-1.5-35B-A3B-AD-Q4_K-IQ4_XS-Shisa-12K-MTP-Q4_0.gguf` | 20,602,882,240 bytes (19.19 GiB) | 40-layer target + one appended NextN/MTP layer |

- Architecture: `qwen35moe`
- Target tensor descriptors: 733
- Appended MTP descriptors: 20
- Total tensor descriptors: 753
- GGUF block count after graft: 41
- `nextn_predict_layers`: 1
- SHA-256: `297c3f150723426fb983dbbe891dcdd97b47e4e40db48fd2ba0564d31ad29676`

## Exact model sources and provenance

### Target model

- Repository: [`AtomicChat/Ornith-1.5-35B-A3B-GGUF`](https://huggingface.co/AtomicChat/Ornith-1.5-35B-A3B-GGUF)
- Revision: `7aa8fc1d9b861d797880f4a341166d4bb3439f74`
- File: `Ornith-1.5-35B-A3B-AD-Q4_K-IQ4_XS.gguf`
- Declared license: MIT
- Upstream base: [`ornith-ai/Ornith-1.5-35B-A3B`](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B)
- Metadata revision used during conversion: `e4dfb35a93d4b6822a811a7676f3488514abe7e2`

The target's AtomicChat mixed `AD-Q4_K/IQ4_XS` tensors were copied byte for
byte. They were **not** requantized during the graft.

### MTP draft head

- Repository: [`shisa-ai/Ornith-1.5-35B-A3B-MTP-ONLY`](https://huggingface.co/shisa-ai/Ornith-1.5-35B-A3B-MTP-ONLY)
- Revision: `2b19b31bfe1659c6b0d9459ec3cbd87e34a322ef`
- File: `model-mtp.safetensors`
- Source payload: 844,640,768 parameters / 1.689 GB, BF16
- Training: Shisa's final 12K, two-epoch, code-heavy KL-distilled MTP head
- Declared license: Apache-2.0; see `LICENSE` and `NOTICE`
- Head lineage: initialized from the compatible MTP head in
  [`Qwen/Qwen3.6-35B-A3B`](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), then
  KL-distilled against Ornith-1.5 hidden states by Shisa.

The Shisa head was converted to GGUF BF16, quantized separately to `Q4_0`, and
then appended to the AtomicChat target. Descriptor counts and representative
tensor payload hashes were checked after grafting.

## llama.cpp compatibility

The tested build was based on llama.cpp commit
`4df29be4f4c3673f428170fda944a5b19f743bb8`:

```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
git checkout 4df29be4f4c3673f428170fda944a5b19f743bb8
cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j --target llama-server llama-cli
```

The local source tree also contained an experimental 27-insertion/1-deletion
`d2t` compatibility change for other trimmed-vocabulary draft models. An
exhaustive tensor inspection confirms that **this GGUF contains no `d2t`
tensor**, so that conditional code path is never executed and no local source
patch is required for this artifact.

## Tested full-context serving configuration

The following is the exact performance-oriented shape used for the results
below. No fixed `--n-cpu-moe` or `--gpu-layers` value is used: `--fit` reserves
both KV caches and compute buffers first, then assigns the safe expert subset.

```bash
MODEL=Ornith-1.5-35B-A3B-AD-Q4_K-IQ4_XS-Shisa-12K-MTP-Q4_0.gguf

./build/bin/llama-server \
  --model "$MODEL" \
  --ctx-size 262144 \
  --parallel 1 \
  --n-predict 32768 \
  --batch-size 512 \
  --ubatch-size 128 \
  --split-mode none \
  --flash-attn on \
  --backend-sampling \
  --cache-type-k q8_0 \
  --cache-type-v q8_0 \
  --spec-type draft-mtp \
  --spec-draft-n-max 1 \
  --spec-draft-n-min 0 \
  --draft-p-min 0 \
  --draft-p-split 0.10 \
  --cache-type-k-draft q8_0 \
  --cache-type-v-draft q8_0 \
  --threads 8 \
  --threads-batch 16 \
  --load-mode none \
  --fit on \
  --fit-target 1024
```

Why MTP1: on this machine MTP1 was faster than longer speculative depths.
Setting `p-min=0` also beat the tested 0.30 and 0.60 thresholds. Q8 target and
draft KV were retained for long-context quality.

## Optional vision projector (not included)

Vision was validated with the official external projector; it is deliberately
not duplicated in this repository:

- Repository: [`ornith-ai/Ornith-1.5-35B-A3B-GGUF`](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF)
- Revision: `fbbaed45c2f0e200276ffa51701a24d45dc7f57e`
- File: `mmproj-Ornith-1.5-35B-BF16.gguf`
- Size: 902,822,016 bytes
- SHA-256: `d9ce31026d1cb1f3f8d5152e2e2a014d9d2b302b6c93a7dc07bb0a0487f52837`
- Declared license: MIT

On a 16GB card, keep the projector in host RAM to preserve VRAM for Q8 KV and
expert weights:

```bash
  --mmproj mmproj-Ornith-1.5-35B-BF16.gguf \
  --no-mmproj-offload \
  --image-min-tokens 1024
```

The remaining model, MTP, KV, fit, batch, and thread settings were identical to
the 262K command above.

## RTX 5060 Ti 16GB results

### Test system

- GPU: NVIDIA GeForce RTX 5060 Ti 16 GB, CUDA compute capability `sm_120`
- CPU: Intel Core i7-10700KF, 8 cores / 16 threads
- System RAM: 46 GiB available to Linux
- Runtime: llama.cpp-based CUDA build at `4df29be4f`; an unrelated conditional
  `d2t` source change was present but inactive for this GGUF
- Concurrency: one sequence
- Workload: text benchmarks plus the separate CPU-resident projector check below

### Memory placement at 262K

- llama.cpp reported `42/42` logical allocation units offloaded to CUDA, but
  this does **not** mean every expert tensor was in VRAM.
- With `fit-target=1024`, 23 units contained expert-weight overflow to host RAM.
- Approximately 19 allocation units were completely GPU resident. The first
  boundary target block was partial; later target/MTP expert matrices stayed in
  host RAM while attention, linear-attention/SSM, norms, routers, embeddings,
  and output tensors stayed on the GPU.
- Target Q8 KV allocation: 2,720 MiB.
- MTP Q8 KV allocation: 272 MiB.
- Recurrent-state allocation: 125.62 MiB.
- Idle/short-prompt VRAM: approximately 14,680 MiB.
- Observed VRAM during a 27,919-token prefill: approximately 14,858 MiB.

### Throughput

All numbers are local single-user measurements and should not be treated as
universal hardware claims.

| Mode | Workload | Decode throughput |
| --- | --- | ---: |
| Plain autoregressive | four fixed 256-token outputs | ~50.5 tok/s average |
| MTP1, `p-min=0` | four fixed 256-token outputs | ~63.7 tok/s average |
| MTP2, `p-min=0` | four fixed 256-token outputs | ~63.6 tok/s average |
| MTP3, `p-min=0` | four fixed 256-token outputs | ~59.0 tok/s average |
| MTP1, `p-min=0` | four fixed 512-token outputs | ~62.8 tok/s average |
| MTP1 after final Q8/Q8 reload | four additional fixed 256-token outputs | 63.47 tok/s average |

The selected MTP1 profile improved the original four-prompt average by about
26% over plain AR. Acceptance is prompt-dependent; the long-prompt test below
accepted 112 of 142 draft tokens (78.9%).

### Longer prompt check

- Prompt: 27,919 tokens
- Prompt ingestion: 136.5 tok/s
- Generated: 256 tokens
- Decode: 55.15 tok/s
- Draft acceptance: 112 / 142 (78.9%)
- Result: completed without OOM or server restart

This is a 27.9K-token performance check inside a fully allocated 262K context,
not a claim that decode was benchmarked with 262K tokens already populated.

### Vision compatibility check

A 326KB JPEG of the Statue of Liberty was sent as an embedded base64 image, so
the server did not receive a descriptive remote URL. With thinking disabled,
the model returned:

> The main landmark is the Statue of Liberty, located in New York City.

- Image + text prompt: 1,687 tokens
- CPU-projector/prompt processing: 33.43 seconds / 50.46 tok/s
- Final answer: 16 tokens / 56.75 tok/s
- MTP acceptance on the short final answer: 8 / 8
- A separate 128-token thinking run decoded at 60.61 tok/s and accepted 57 / 69
  MTP drafts (82.6%)
- Peak observed GPU allocation: approximately 14,862 MiB
- Result: correct landmark/city identification; no OOM or server restart

### 16GB stability boundary

An aggressive all-Q8 experiment reduced `fit-target` to zero and moved roughly
three more complete expert units to the GPU. It loaded at about 15,650 MiB and
rose to about 15,790 MiB during generation, then failed with CUDA OOM while
instantiating a CUDA graph on the third short request. Do not copy that setting
on a display-attached 16GB card. The published 1,024 MiB fit margin is the
stable profile.

## Validation performed

- Structural check: 733 target + 20 appended MTP descriptors = 753 tensors.
- Target descriptors and weights were preserved through grafting.
- Representative target and MTP payload hashes matched their source GGUFs.
- CPU-only llama.cpp load/inference passed.
- CUDA load, speculative-context initialization, and generation passed.
- Native 262,144-token context allocation passed with Q8 target and draft KV.

## Limitations

- No `mmproj` is included. Vision requires the separately downloaded official
  projector cited above.
- Vision validation currently covers one landmark image, not a broad OCR,
  grounding, chart, document, or multimodal safety benchmark.
- The MTP head was trained by Shisa with a 2,048-token training window. Shisa
  measured longer-context acceptance, but the training distribution does not
  directly cover 256K inputs.
- The target is quantized; see AtomicChat's model card for KL and top-1
  measurements against BF16.
- Speculative acceptance and throughput depend strongly on prompt distribution,
  sampling parameters, runtime revision, and hardware.
- Use a llama.cpp revision with Qwen3.5 MoE `draft-mtp` support. This GGUF does
  not require the separate trimmed-vocabulary `d2t` compatibility patch.
- This artifact has not been independently evaluated on downstream capability,
  safety, or multimodal benchmarks.

## Licenses and attribution

This artifact combines components with different declared licenses:

- AtomicChat target GGUF and upstream Ornith metadata: MIT as declared by their
  Hugging Face repositories.
- Shisa MTP head and its Qwen MTP lineage: Apache License 2.0. The Shisa
  `LICENSE` and `NOTICE` are redistributed in this repository.

Users are responsible for reviewing and complying with all upstream licenses,
model cards, acceptable-use requirements, and applicable law. Attribution in
this README is informational and does not replace the upstream terms.

## Acknowledgements

All model research, target quantization, and MTP distillation credit belongs to
the respective Ornith, AtomicChat, Shisa, and Qwen authors. This repository only
packages the cited target and MTP head into a tested llama.cpp GGUF combination.
