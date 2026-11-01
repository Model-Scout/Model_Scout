---
license: mit
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
library_name: gguf
language:
- en
- ko
pipeline_tag: text-generation
tags:
- gguf
- llama.cpp
- llama-cpp
- motif3
- motif-3
- mixture-of-experts
- moe
- dgx-spark
- nvidia-dgx-spark
- nvidia
- blackwell
- arm64
- quantization
- iq2_xxs
- iq2-xxs
---

# Motif-3 315B on one DGX Spark

**Research closed — September 10, 2026.** This IQ2 download is unchanged.
A separate internal-NVMe Q4 experiment recorded 2.81 generated tokens/s over
1,024 tokens; BF16/Q4 behavioral parity remains unverified. No Q4 weights are
uploaded here. The final source-and-evidence report is available on GitHub:
[English](https://github.com/hebo1221/motif3-dgx-spark/blob/v1.4.0/docs/FINAL_REPORT.md) ·
[한국어](https://github.com/hebo1221/motif3-dgx-spark/blob/v1.4.0/docs/FINAL_REPORT.ko.md).

![Motif-3 315B on one DGX Spark: 83.56 GiB, 316.71 tok/s prompt processing, and 16.49 tok/s generation](assets/motif3-dgx-spark-result-card.png)

This is a mixed IQ2_XXS build of the 314.7B-parameter Motif-3 core, tested
entirely on one 128 GB NVIDIA DGX Spark. The final GGUF is **83.56 GiB** and
loads all model layers on the GPU.

| Measurement | Result |
|---|---:|
| pp512 | **316.71 tok/s** |
| pp2048 | **312.76 tok/s** |
| tg128 | **16.49 tok/s** |
| pp2048 + tg128 | **149.33 tok/s** |

These are five-run means from the pinned public build. The speed rows predate
the tokenizer patch described below; 83.56 GiB is the file size, not runtime
memory use.

Source, build instructions, benchmark records, and checksums are available in
the [GitHub repository](https://github.com/hebo1221/motif3-dgx-spark).
The [full Korean guide](https://github.com/hebo1221/motif3-dgx-spark/blob/main/README.ko.md)
is available there as well.

> **Before downloading:** this model was validated with the pinned
> Motif-capable llama.cpp runtime and tokenizer patch below. Compatibility with
> stock upstream llama.cpp has not been established. The quant also did not
> pass the prespecified BF16 quality-preservation gates, so treat it as a
> systems and research release rather than a drop-in BF16 replacement.

## 한국어 안내

Motif-3의 3,147억 파라미터 핵심 모델을 혼합 IQ2_XXS GGUF로 압축해,
128 GB NVIDIA DGX Spark 한 대에서 구동한 릴리스입니다. 최종 파일은
83.56 GiB이며 모든 모델 레이어를 GPU에 올렸습니다. 공개 빌드에서
pp512 316.71 tok/s, tg128 16.49 tok/s를 기록했습니다. 이 속도는 아래의
토크나이저 패치를 적용하기 전에 측정했습니다.

공식 BF16 체크포인트에서 직접 변환했으며, 고정한 llama.cpp 런타임,
토크나이저 수정 패치, 벤치마크 원본과 체크섬을 함께 공개합니다. 다만
BF16 품질 유지 기준은 통과하지 못했습니다. 중요한 용도에 적용하기 전에
자신의 데이터로 충분히 검증하세요.

설치부터 제한사항까지 다룬
[한국어 전체 가이드](https://github.com/hebo1221/motif3-dgx-spark/blob/main/README.ko.md)를
별도로 제공합니다.

## Inspect without downloading the model

The [recorded answer tour](https://github.com/hebo1221/motif3-dgx-spark/blob/main/docs/RECORDED_DEMO.md)
pairs document-agent answers with their cited passages, including an answer
that quotes the right number and reaches the wrong conclusion. The
[case study](https://github.com/hebo1221/motif3-dgx-spark/blob/main/docs/CASE_STUDY.md)
and [한국어 회고](https://github.com/hebo1221/motif3-dgx-spark/blob/main/docs/CASE_STUDY.ko.md)
cover the wider engineering work.

After cloning the source repository, this offline check verifies hashes and
cited passages without making a model request:

```bash
python3 experiments/value-v2/verify_public.py
```

CUDA users can also run the
[model-free Q8 numerical probe](https://github.com/hebo1221/motif3-dgx-spark/tree/main/experiments/value-v2/runtime).

## Quick start

Allow at least 110 GB of free disk for the download and runtime build. The
tested system was one NVIDIA DGX Spark.

### 1. Download

```bash
mkdir -p model

hf download jhkim55/Motif-3-Direct-IQ2-XXS-DGX-Spark \
  motif3-direct-iq2xxs.gguf \
  motif3-llama.cpp.jinja \
  --revision 3511f72d7ceac63e2931b27e1666766f2ad18d54 \
  --local-dir model

sha256sum model/motif3-direct-iq2xxs.gguf
```

Expected model SHA-256:

```text
9d6f7aee57f0271223f51d69c63d8576a259809e9f05e2ac596512e940c80c5a
```

### 2. Build the runtime

```bash
git clone --branch motif3-dgx-spark-v1 --single-branch \
  https://github.com/hebo1221/llama.cpp.git runtime

git -C runtime checkout cc3f13b3f172978d7b3c215780d4cc98bb0e1c80

git clone --branch v1.2.0 --depth 1 \
  https://github.com/hebo1221/motif3-dgx-spark.git release-files

sha256sum release-files/patches/motif3-tokenizer-exact-v1.patch
git -C runtime apply --check --unidiff-zero \
  ../release-files/patches/motif3-tokenizer-exact-v1.patch
git -C runtime apply --unidiff-zero \
  ../release-files/patches/motif3-tokenizer-exact-v1.patch

git -C runtime diff --binary --no-ext-diff | sha256sum

cmake -S runtime -B runtime/build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA=ON \
  -DGGML_CUDA_FA=ON \
  -DGGML_CUDA_GRAPHS=ON \
  -DGGML_NATIVE=ON \
  -DLLAMA_BUILD_UI=OFF \
  -DLLAMA_USE_PREBUILT_UI=OFF

cmake --build runtime/build --target llama-server -j 12
```

The tokenizer patch must hash to
`5eba842cd63731e3ee39c60c43134ef59a3a64c9d28c2aa58c3073225c6545cf`.
After applying it, the normal Git diff must hash to
`09abc52c2f7ff9f2cb3e9b8edd3af03684840969d0cdc7f24fd7aa63ca3207f3`.
The patch fixes Motif prompt token IDs; it does not modify the GGUF weights.

### 3. Serve

```bash
runtime/build/bin/llama-server \
  -m model/motif3-direct-iq2xxs.gguf \
  -ngl 99 -fa on \
  -ctk f16 -ctv f16 \
  -b 2048 -ub 512 \
  -c 32768 -np 1 \
  --host 127.0.0.1 \
  --port 8080 \
  --no-ui \
  --jinja \
  --chat-template-file model/motif3-llama.cpp.jinja
```

Wait for the model to load, then check
`curl -fsS http://127.0.0.1:8080/health`. Keep the listener on localhost unless
you have configured authentication.

## Files

| File | Size | SHA-256 |
|---|---:|---|
| `motif3-direct-iq2xxs.gguf` | 89,720,474,560 bytes | `9d6f7aee57f0271223f51d69c63d8576a259809e9f05e2ac596512e940c80c5a` |
| `motif3-llama.cpp.jinja` | 6,759 bytes | `25877a0b07679b1c1702d9f9211c8f1e8421537113b9dcf993f7e45f7caf3adc` |

The GGUF contains the core model only. Motif-3's native MTP head is not
included.

## Quantization

This is mixed precision, not a pure 2-bit file.

| Stored type | Tensors | Payload bytes |
|---|---:|---:|
| IQ2_XXS | 306 | 78,631,821,312 |
| BF16 | 424 | 7,252,475,904 |
| Q8_0 | 2 | 1,916,272,640 |
| Q2_K | 6 | 1,357,676,544 |
| F32 | 1,424 | 552,591,880 |

Routed-expert tensors carry most of the compression. Embeddings, output,
attention, routing, and control tensors keep more precision. Across the whole
tensor payload, storage is 2.2805 bits per element.

The conversion path was:

```text
official BF16 -> BF16 GGUF -> IQ2_XXS
```

There was no Q5 intermediate and no `--allow-requantize` step.

## Performance

The table at the top reports means from five repetitions per shape. The build
used all GPU layers, Flash Attention, F16 KV, batch 2,048, micro-batch 512, and
20 CPU threads. A separate three-session campaign measured the same range and
observed 85,713 MiB peak NVIDIA process allocation.

These are results from one machine, not a guarantee for every DGX Spark. The
normalized benchmark rows and build receipt are in the
[evidence directory](https://github.com/hebo1221/motif3-dgx-spark/tree/main/evidence).

## Tokenizer

The final GGUF embeds the Motif pre-tokenizer metadata. The v1.1.0 patch on the
pinned runtime matched the official tokenizer on:

- 61,548 calibration token IDs;
- 54,070 held-out token IDs;
- 318,951 token IDs from 12,011 deterministic Unicode and formatting cases.

A source-identical extended campaign matched all 4,164,390 token IDs from
591,984 generated cases plus the two corpora. It covers regex splitting and
added-token selection as separate mechanisms, Unicode 16 boundaries, all 160
added tokens, random compositions, and `parse_special=false`.

See the
[`tokenizer_exact_v1.json` receipt](https://github.com/hebo1221/motif3-dgx-spark/blob/v1.1.0/evidence/tokenizer_exact_v1.json).
This is token-ID correctness evidence, not an IQ2 quality improvement.

## Quality and limitations

On a fixed 49,152-token held-out sequence, the IQ2 artifact measured:

- perplexity ratio against BF16: `1.411541 +/- 0.010497`;
- mean KL divergence: `0.454130 +/- 0.004009`.

Both missed the prespecified limits of 1.10 and 0.10. Test the model on your
own workload before relying on it, especially for tool calling, exact
reasoning, or long-context retrieval.

Additional limits:

- Stock upstream llama.cpp compatibility is not established.
- The downloadable GGUF has no native MTP speculative speedup.
- Retained 256K-context quality has not been established.
- In server mode, `-c` is divided across parallel slots. Check `/slots` before
  treating it as a per-request context value.
- Internal task sets are diagnostics, not public leaderboard scores.
- The published speed rows predate the v1.1.0 tokenizer patch and remain
  labeled as results from the pinned v1.0.0 runtime base.
- Two passive provenance fields contain local build paths. They do not affect
  inference; the published SHA binds the file as it is.

The remaining quality-attribution question is open in
[GitHub Discussion #1](https://github.com/hebo1221/motif3-dgx-spark/discussions/1).
Paired BF16/Q5 results, mixed-precision suggestions, and independent Spark
reproductions are welcome.

## Reusable experiments

[v1.3.0-rc.1](https://github.com/hebo1221/motif3-dgx-spark/releases/tag/v1.3.0-rc.1)
contains a model-free Q8 batch-consistency probe, a two-file opt-in reference
patch, and a bounded document agent with project matching and exact source
passages. The reference path is slower, and the agent can still make factual
errors. Both outcomes and their public provenance are included.

See the [follow-up package](https://github.com/hebo1221/motif3-dgx-spark/tree/v1.3.0-rc.1/experiments/value-v2)
for code, examples, and limits.

## Experimental native MTP

Release v1.2.0 also includes an optional source patch for Motif-3's one-layer
MTP head. On a separate, byte-distinct target, a fixed target/MTP/target A-B-A
run matched 5,120/5,120 greedy tokens in both comparison arms and measured
1.2036x higher server-reported decode, with 47.11% draft acceptance.

This result does not belong to the downloadable GGUF. The 512 MB sidecar is
not redistributed, the public GGUF is unchanged, and the exact target used in
that experiment has different bytes. See the
[MTP notes](https://github.com/hebo1221/motif3-dgx-spark/blob/main/docs/MTP_EXPERIMENTAL.md)
for the build recipe and evidence.

## Project status and community results

The active research phase is complete. Reproducible defects, evidence
corrections, independent Spark measurements, and bounded real-world use cases
remain welcome. See the
[project status](https://github.com/hebo1221/motif3-dgx-spark/blob/main/docs/PROJECT_STATUS.md)
and use the
[benchmark form](https://github.com/hebo1221/motif3-dgx-spark/issues/new?template=benchmark.yml)
to share a result.

## License

The parent model is released by Motif Technologies under the MIT License. This
derived quantization keeps that license and attribution. The work builds on
llama.cpp, Chrono's Motif port, and the cited GQA-5 work; development and
analysis were assisted by Codex. Full attribution is in the source
[NOTICE](https://github.com/hebo1221/motif3-dgx-spark/blob/main/NOTICE.md).
This is an independent community release and is not affiliated with Motif
Technologies, NVIDIA, or llama.cpp.
