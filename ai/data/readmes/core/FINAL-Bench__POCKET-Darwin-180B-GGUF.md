---
license: other
license_name: qwen-community-1.0
license_link: LICENSE
language: [en, ko, zh, ja, multilingual]
library_name: gguf
pipeline_tag: text-generation
base_model: FINAL-Bench/Darwin-180B-RSI-R3
base_model_relation: quantized
tags:
  - gguf
  - llama.cpp
  - pocket
  - darwin
  - darwin-rsi
  - model-level-rsi
  - dgx-spark
  - on-device
  - moe
---
<!-- POCKET-27B-DISCOVERY:START -->
<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/POCKET-27B-GGUF"><img src="https://img.shields.io/badge/NEW%20POCKET--27B-Q6__K%20%C2%B7%2022.43%20GB-55cbb4?style=for-the-badge" alt="New POCKET-27B: Qwen3.8-27B, Q6_K, 22.43 GB - model card and downloads"></a>
</p>
<p align="center"><b>Meet POCKET-27B.</b> Qwen3.8-27B in ARCHsloth Q6_K GGUF. <a href="https://huggingface.co/FINAL-Bench/POCKET-27B-GGUF/tree/main">Choose files &amp; download</a> · <a href="https://huggingface.co/FINAL-Bench/POCKET-27B-GGUF#quality-and-evaluation">Quality &amp; limits</a></p>
<!-- POCKET-27B-DISCOVERY:END -->

<!-- SUPERCLUE-2026-11:START -->
## 🏆 SuperCLUE November 2026: #1 open-weight model in math and science reasoning

[![SuperCLUE Nov 2026: Darwin-180B-RSI #1 open-weight, #2 overall in math and science reasoning](https://huggingface.co/datasets/VIDraft/press-assets/resolve/main/press/superclue_banner_darwin_2026-11.png)](https://www.superclueai.com/homepage)

**This GGUF is the on-device build of Darwin-180B-RSI-R3, the model that [SuperCLUE](https://www.superclueai.com/homepage), China's most widely cited LLM benchmark, scored 73.68 in mathematical and scientific reasoning on its private November 2026 test set: #1 among open-weight models and #2 overall** among 19 models, right behind OpenAI's GPT-6.1-Sol (76.32) and ahead of Gemini-4-Argon, DeepSeek-V4.1-Flash, Grok-4.7 and Qwen3.8-Max. Overall index: 9th of 19, 5th among open-weight models. The only Korean model on the board.

| Model | Developer | Open weights | Math & science reasoning |
|---|---|---|---|
| GPT-6.1-Sol | OpenAI | No | 76.32 |
| **Darwin-180B-RSI-R3** | **VIDRAFT** | **Yes** | **73.68** |
| Gemini-4-Argon | Google | No | 71.05 |
| DeepSeek-V4.1-Flash | DeepSeek | Yes | 71.05 |
| Grok-4.7 | xAI | No | 68.42 |
| Qwen3.8-Max-0902 | Alibaba | No | 68.42 |
| GLM-5.3 | Zhipu AI | Yes | 65.79 |
| Kimi-K3.1-Pro | Moonshot | Yes | 63.16 |
| Qwen3.8-Flash (parent of Darwin-180B) | Alibaba | Yes | 57.89 |

Darwin-180B-RSI inherited its expert layers from Qwen3.8-Flash-Next and rebuilt only the attention and shared-expert layers through recursive self-improvement. On the same board the parent, Qwen3.8-Flash, placed 15th overall (39.81) with 57.89 in math and science reasoning; Darwin placed 9th (43.08) with 73.68.

<details><summary>Overall intelligence index, November 2026 (screenshot)</summary>

![SuperCLUE Nov 2026 intelligence index](https://huggingface.co/datasets/VIDraft/press-assets/resolve/main/press/superclue_intelligence_index_2026-11.png)

</details>

Source: [SuperCLUE general leaderboard, November 2026](https://www.superclueai.com/homepage) (screenshots taken November 5, 2026). Scores are SuperCLUE's, not VIDRAFT's.
<!-- SUPERCLUE-2026-11:END -->


# POCKET-Darwin-180B-GGUF

Text-only RSI reasoning in a 111.3 GB, four-shard GGUF: choose a CPU-server or hybrid laptop setup.

![POCKET-Darwin-180B overview: text-only reasoning, four required shards, separate CPU and hybrid modes](./pocket-overview.svg)

[Download files](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF/tree/main) · [Setup guide](https://vidraft.net/p/pocket.html?model=pocket_darwin_180b&utm_source=huggingface&utm_medium=referral&utm_campaign=pocket_2026q4&utm_content=pocket_darwin_180b_model_card_top) · [Benchmarks](#quality-and-evaluation)

[POCKET-35B](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) · [POCKET-26B](https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF) · [POCKET-Darwin-180B](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)

## At a glance

| Item | Details |
|---|---|
| Artifact | Text-only 180B sparse MoE, approximately 3B active parameters per token; UD-Q4_K_XL GGUF |
| Starting checkpoint | [FINAL-Bench/Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3) |
| Recommended first build | The supplied four-shard build; all four files are required, about 111.3 GB total |
| Hardware | CPU server with sufficient RAM, or a separately configured GPU/CPU/SSD hybrid path |
| Runtime | Original publisher minimum: llama.cpp b11048 with qwen4exp support; check the installed build |
| License | Qwen Community License 1.0, **not Apache-2.0**; see [License and attribution](#license-and-attribution) |
| Evidence status | Publisher measurements with device-specific conditions below |

The vision encoder is not included. Parent BF16 vision scores and multi-sample benchmark results are reference material, not measurements of this text-only GGUF.

## Choose your build

| Build | File size | Memory guidance | Best for |
|---|---|---|---|
| [UD-Q4_K_XL — all four shards](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF/tree/main) | About 111.3 GB total | CPU-server and hybrid requirements differ; see the hardware table | The supplied Darwin-R3 reasoning package |

There is no smaller quantization alternative in this repository. Download **all four**, keep their original names in the same directory and open the first shard. No merge is required.

| Required file | Role |
|---|---|
| POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf | Entry shard passed to llama.cpp |
| POCKET-Darwin-180B-UD-Q4_K_XL-00002-of-00004.gguf | Required sibling |
| POCKET-Darwin-180B-UD-Q4_K_XL-00003-of-00004.gguf | Required sibling |
| POCKET-Darwin-180B-UD-Q4_K_XL-00004-of-00004.gguf | Required sibling |

File size is not a complete RAM budget. Reserve the full model size on disk **plus** sufficient cache, temporary-download and free-space headroom for your CLI/filesystem. The original card's 120 GB storage suggestion is not a universal total-disk guarantee. Hybrid laptop mode relies on fast local SSD access rather than fitting the full file set into 32 GB RAM.

## Download and run

Install the [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) and a [llama.cpp build](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) with qwen4exp support. The original publisher reports b11048; that revision contains an [official implementation](https://github.com/ggml-org/llama.cpp/blob/b11048/src/models/qwen4exp.cpp), but source availability does not independently verify every upload, app or later release.

**1. Download all four required shards.**

```bash
hf download FINAL-Bench/POCKET-Darwin-180B-GGUF --revision 69fc3dd1409507de5dc12d81767f909ac2511567 --include "POCKET-Darwin-180B-UD-Q4_K_XL-*.gguf" --local-dir ./POCKET-Darwin-180B
```

**2. Run on a suitably provisioned CPU server.**

```bash
llama-server -m ./POCKET-Darwin-180B/POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf --device none -ngl 0 -t 16 -c 8192 --jinja --load-mode none --host 127.0.0.1 --port 8080
```

All four shards must be present before the server starts. Open `http://127.0.0.1:8080` after loading and submit a text prompt. The expected result is a local chat response, not a fixed benchmark answer. This example is **not** the 32 GB laptop configuration; it needs sufficient CPU-server RAM.

Commands use the standalone llama.cpp executable names. Some distributions expose a unified `llama` launcher; consult that distribution's help and the [official model-loading documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/models.md). The CPU example uses `--device none` to disable GPU acceleration. `--load-mode none` selects a **loading strategy**, not CPU mode.

<details>
<summary>Optional hybrid laptop and large-GPU commands</summary>

The original card reports a laptop run with an RTX 5060 Laptop GPU, 8 GB VRAM, 32 GB RAM and NVMe SSD. This is a **hybrid GPU/CPU/SSD** configuration, not a no-GPU result:

```bash
llama-server -m ./POCKET-Darwin-180B/POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf -ngl 999 --cpu-moe -fa on -c 8192 --jinja --host 127.0.0.1 --port 8080
```

`--cpu-moe` keeps expert weights on the CPU side; other operations can still use the GPU. Usable speed depends on SSD access, RAM bandwidth, context and runtime behavior.

For a large GPU or a supported unified-memory system with sufficient available memory, the original card gives:

```bash
llama-server -m ./POCKET-Darwin-180B/POCKET-Darwin-180B-UD-Q4_K_XL-00001-of-00004.gguf -ngl 999 -fa on -c 131072 --jinja --host 127.0.0.1 --port 8080
```

This larger context needs additional runtime memory. It is not a guarantee for every 128 GB device.

</details>

The publisher recommends temperature 1.0, top-p 0.95 and top-k 20. This is a reasoning model: allow at least 2,048 output tokens when the task and available context permit, and distinguish reasoning from the final answer. The original integration reports reasoning through `reasoning_content`; response formatting depends on the serving version and client.

These command examples were syntax-reviewed but not executed during this review.

For installation, shard errors and hardware selection, use the [model-specific setup guide](https://vidraft.net/p/pocket.html?model=pocket_darwin_180b&utm_source=huggingface&utm_medium=referral&utm_campaign=pocket_2026q4&utm_content=pocket_darwin_180b_quickstart_help). Model files remain directly available from Hugging Face without a VIDRAFT login.

## Runtime compatibility

| Runtime | Requirement | Evidence and limits |
|---|---|---|
| llama.cpp | qwen4exp implementation; original publisher minimum b11048 | The publisher reports loading and running on b11048; other versions and backends need their own compatibility checks |
| Four-shard GGUF loader | First shard as entry point, all matching siblings present | [Official loader](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-model-loader.cpp) opens the remaining shards; a lone first file is insufficient |
| Ollama | Explicit support for this architecture, format and shard layout | Generic GGUF support is not proof; no tested target-model/version combination supplied here |
| LM Studio and other GUI apps | Bundled backend explicitly supporting this architecture and memory mode | Do not assume compatibility from the app name or GGUF extension |
| ZTC hidden-state extraction | Separate opt-in llama.cpp patch and probe workflow | A research path, not required for ordinary text generation; see evaluation notes below |

The same file format does not guarantee support in every app or version. A dated, exact-version compatibility matrix remains a community contribution opportunity.

## Hardware and performance

Device-qualified, publisher-reported measurements are separated from reference builds and memory-fit guidance.

| Device or mode | Configuration | Generation | Evidence and limits |
|---|---|---|---|
| Hybrid laptop | RTX 5060 Laptop, 8 GB VRAM, 32 GB RAM, NVMe SSD | 4.17 tok/s | Reported for this package; experts read on demand through memory mapping |
| CPU server | AMD EPYC 9365, one socket, 16 threads, no GPU | 18.4–21.0 tok/s | Reported peak RAM 78.8 GB; load 85 s; prompt 54–68 tok/s |
| DGX Spark reference | GB10, 128 GB unified memory | 39.25 tok/s | **Reference build of the same size/layout, not a this-build R3 measurement** |
| B200 | One 183 GB GPU | No generation rate supplied | Original card reports 8–16 parallel 131K-context sessions and 110–140 GB VRAM; detailed concurrency protocol not supplied |
| 128 GB mini PC / other unified-memory devices | Appropriate backend and available working memory | Not measured for this build | Capacity guidance only, not an EPYC-speed promise |

The original card reports approximately 3B active parameters per token, with 10 of 512 experts selected. Memory mapping can read required expert data from SSD; this does not make storage latency irrelevant or the model's full disk footprint disappear. The publisher attributes the CPU run's below-file-size RAM peak partly to per-layer n-gram embeddings being read on demand.

<details>
<summary>Device classes and original capacity guidance</summary>

| Device class | Memory and storage guidance | Mode | Measurement status |
|---|---|---|---|
| Laptop / desktop | Original example: 32 GB RAM, 8 GB VRAM, fast NVMe; full model on disk plus headroom | Hybrid streaming | Exact RTX 5060 Laptop example above; other devices unmeasured |
| Mini PC | 128 GB available system memory class; full model on local storage plus headroom | CPU or supported integrated GPU | Memory-fit guidance, not a supplied throughput result |
| Workstation | Original guidance: 96–128 GB RAM and a supported GPU | CPU experts plus GPU operations | Configuration guidance, not a universal guarantee |
| Unified-memory AI PC | Original guidance: 128 GB class | Supported accelerator backend | Spark reference measured; exact R3 and other systems unmeasured |
| CPU server | Original guidance: 96 GB or more, with additional headroom for context and OS | CPU-only | Specific EPYC measurement above |
| Datacenter GPU | Original guidance: 141 GB or more VRAM, depending on context and concurrency | GPU-resident | Verify actual context, working memory and backend |

Memory capacity alone is not a complete compatibility or throughput test. The original comparison with a 360 GB BF16 package establishes a disk-size difference, not a verified hardware-cost saving or like-for-like serving comparison.

</details>

## Quality and evaluation

The first tables concern this GGUF. Parent BF16 results are explicitly separated below. All are publisher-reported measurements under the stated protocols.

| Build | Evaluation | Result | Conditions and limits |
|---|---|---|---|
| Darwin-180B-RSI-R3 BF16 | MMLU-Pro subset | 87.65% | 2,000 subject-stratified questions; fixed question-ID hash selection |
| POCKET-Darwin-180B GGUF | Same MMLU-Pro subset | 87.65% | Paired difference +0.00 pp; bootstrap 95% CI [-0.95, +1.00] |
| Parent UD-Q4_K_XL, R0 | Held-out SuperGPQA | 59.10% mean of four; 58.70% single; 63.60% majority of four | 1,000 questions, four samples each, 16K generation budget |
| POCKET-Darwin-180B, R3 | Same held-out SuperGPQA | 61.55% mean of four; 62.20% single; 65.90% majority of four | Paired mean difference +2.45 pp; 95% CI [+1.54, +3.36] |

For the MMLU-Pro comparison: 0-shot chain of thought, temperature 1.0, top-p 0.95, top-k 20, min-p 0, seed 7, up to 131K tokens; BF16 uses vLLM and GGUF uses llama.cpp. The publisher reports zero truncated answers. Equal measured accuracy on this subset is **not** proof that quantization is lossless on every task.

For the SuperGPQA comparison: questions were held out from training and selection. Majority-of-four is over answered samples; ties use the first answer in sample order, seeds 21–24. The publisher reports 675 versus 798 of 4,000 samples reaching the 16K cap, 13% fewer tokens by geometric mean of per-question ratios and 10% fewer tokens in aggregate, averaging 6,051 versus 6,716 tokens. These are a same-budget comparison, not the 131K BF16 reference protocol.

<details>
<summary>Build provenance, RSI and additional reported findings</summary>

Darwin-180B-RSI-R3 is an RSI-derived checkpoint of [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). The original card describes self-generated, checked-correct training solutions, with changes to attention paths and shared experts; routed experts, router, per-layer n-gram embeddings and the MTP head are retained.

This GGUF uses the [Unsloth UD-Q4_K_XL layout](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF) and replaces 300 R3-changed tensors, encoded as Q8_0 in that layout. The publisher reports all 300 replacements found and checked, with 570 untouched tensors byte-identical to the parent build. These are build checks reported by the publisher, separate from the task-quality evaluations.

The [R3 source card](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3) reports a BF16 R3-versus-R1 SuperGPQA gain of +1.03 pp, 95% CI [+0.05, +2.00], on 1,000 held-out questions. This separate result should not be treated as a GGUF result solely because another benchmark matches BF16. The direct GGUF R0/R3 comparison is reported above.

The source card also reports mean answer lengths of 3,694 versus 4,322 tokens (-14.5%) on a 2,000-question same-format comparison. Keep that protocol separate from the four-sample, 16K SuperGPQA comparison.

</details>

<details>
<summary>Parent BF16 reference benchmarks — not this GGUF's results</summary>

The following are copied reference scores for the original [Darwin-180B-RSI BF16 model](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI), not current-ranking claims, independent replications, or measurements of this text-only GGUF.

| Build | Evaluation | Result | Conditions and limits |
|---|---|---|---|
| Original Darwin-180B-RSI BF16 | GPQA Diamond, 198 questions | 94.44% | Majority vote over up to 16 samples; 131,072-token thinking budget |
| Original Darwin-180B-RSI BF16 | MMLU-Pro, 12,032 questions | 88.12% | Single sample; 131,072-token thinking budget |
| Original Darwin-180B-RSI BF16 | AIME 2026, 30 questions | 100.0% | Majority of 16; mean 98.75%; 131,072-token thinking budget |
| Original Darwin-180B-RSI BF16 | HMMT February 2026, 33 questions | 100.0% | Majority of 16; mean 96.59%; 131,072-token thinking budget |
| Original Darwin-180B-RSI BF16 | MMMU-Pro vision, 1,730 questions | 79.48% | Majority of three; 131,072-token thinking budget; vision is not included in this GGUF |
| Original Darwin-180B-RSI BF16 | LEXam law MCQ, 1,655 questions | 68.94% | Majority of four; single 60.54%, mean 61.42%; 32,768-token thinking budget |
| Original Darwin-180B-RSI BF16 | LEXam-hard open-ended, 518 questions | 45.72 | Single sample; 32,768-token budget; 60 truncated answers regenerated at 120K; DeepSeek-R1-0528 judge |

Reference settings: BF16, vLLM, temperature 1.0, top-p 0.95 and top-k 20, with benchmark-specific voting and budgets above. See the [original evaluation protocol](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI#evaluation-protocol). Published scores from other models may use different protocols; no like-for-like frontier ranking is asserted here.

</details>

<details>
<summary>Optional ZTC confidence probe — patched research workflow</summary>

[ZTC materials](./ztc/README.md) include a 32 KB probe, a usage script and a llama.cpp patch for this architecture. The probe reads the 2,560-dimensional final hidden state at the last prompt token before answer generation. This is not a zero-compute guarantee: prompt processing and hidden-state extraction still occur.

| Build | Evaluation | Result | Conditions and limits |
|---|---|---|---|
| This GGUF, self-readout | MMLU-Pro, 2,000 questions | AUROC 0.758 | Five-fold cross-validation; trained on the MMLU-Pro multiple-choice prompt format |
| This GGUF, most confident fifth | Same cross-validated evaluation | 97.5% accuracy | Selected subset, not overall model accuracy |
| This GGUF, all questions | Same evaluation | 87.6% accuracy | Different rounding from the 87.65% headline |
| This GGUF, least confident fifth reviewed | Same evaluation | 46% of all wrong answers found | Review/triage statistic, not error elimination |
| Parent BF16 / parent 4-bit / this GGUF | Cross-model readout, same 400 questions | AUROC 0.715 / 0.722 / 0.742 | Answers written by another model; separate protocol |

Ordinary generation does not need this patch. For hidden-state extraction, the included instructions use `Q4E_EMBD_FIX=1`, `--embeddings` and a separate server workflow. Read and review the [patch](./ztc/llama.cpp-qwen4exp-embeddings.patch) against the exact llama.cpp revision before applying it; newer versions may differ. The [usage script](./ztc/usage.py) requires NumPy and a compatible local embeddings endpoint. Separate generation/embedding processes can require additional memory.

The probe can help rank cases for additional checks, sampling or human review. Its cross-validated multiple-choice results do not establish calibrated probabilities on arbitrary tasks or deployment populations.

</details>

## Intended uses

- Local text-only reasoning research on explicitly provisioned CPU-server or hybrid hardware.
- Comparing R0/R3 reasoning under a fixed sampling and generation budget.
- Exploring optional confidence-based triage with the separate ZTC research workflow and task-specific validation.

## Limitations

- All four model shards are required; a single shard is not a complete model.
- This package is text-only. Parent BF16 vision results are not this artifact's capability claims.
- Laptop streaming uses a GPU and fast SSD; it is not the CPU-only server configuration.
- EPYC throughput is not a mini-PC benchmark; the Spark figure is a reference-build result.
- Equal MMLU-Pro subset accuracy does not establish lossless quality on every task.
- ZTC needs a separate patched workflow and validation outside its training/evaluation format.
- Architecture support, context headroom, memory and usable speed depend on the exact runtime and device.

## License and attribution

This package uses **Qwen Community License 1.0**, provided in [LICENSE](./LICENSE), not Apache-2.0. Read the full license before commercial use or redistribution.

The license includes notice/attribution requirements, a model-name display condition for specified large commercial services, and a separate-license requirement for specified commercial Model-as-a-Service or AI Work Assistant businesses, with a defined internal-use exception. This summary is not legal clearance; the exact definitions and conditions in LICENSE control.

Base model: [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) by the Qwen team, Alibaba. Starting RSI checkpoint: [Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3). GGUF layout: [Unsloth](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF), UD-Q4_K_XL. RSI work and this package: VIDRAFT / FINAL-Bench.

## Support and updates

For shard download, device selection and installation help, visit the [VIDRAFT POCKET setup guide](https://vidraft.net/p/pocket.html?model=pocket_darwin_180b&utm_source=huggingface&utm_medium=referral&utm_campaign=pocket_2026q4&utm_content=pocket_darwin_180b_model_card_footer). Report reproducible issues in the [model discussions](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF/discussions), including all shard filenames, runtime version, device, memory and command; do not post private prompts or credentials.

A this-build DGX Spark throughput measurement remains future work in the supplied evidence. No local-inference telemetry or website gate is required to obtain these public files.

## POCKET family

| Model | Role | Start here |
|---|---|---|
| POCKET-35B-GGUF | Full 35B PC builds; Q2_K recommended first | [Model card](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) |
| POCKET-26B-GGUF | Korean-tuned Gemma4 GGUF; 11 GB and 17 GB options | [Model card](https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF) |
| POCKET-Darwin-180B-GGUF | Text-only RSI reasoning; four-shard download | [Model card](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF) |

Explore the [POCKET collection](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6). For phone-oriented derivatives, see [KR GGUF](https://huggingface.co/FINAL-Bench/POCKET-KR-GGUF), [KR MLX](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) and [EN GGUF](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF).

<details>
<summary>More POCKET projects and research</summary>

[Qwen3.8 Flash-Next GGUF](https://huggingface.co/FINAL-Bench/POCKET-Qwen3.8-Flash-Next-GGUF) is a separate parent-model package, distinct from the POCKET-Darwin-180B RSI-R3 weights. Image projects are also separate: [POCKET-Image-Zimage](https://huggingface.co/FINAL-Bench/POCKET-Image-Zimage), [POCKET-Zimage-CPU](https://huggingface.co/FINAL-Bench/POCKET-Zimage-CPU) and [Image Studio](https://huggingface.co/spaces/FINAL-Bench/POCKET-Image-Studio).

Research collections: [Darwin](https://huggingface.co/collections/FINAL-Bench/darwin-family-699987b1f652864af0122193), [Aether](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model-6a5c7f2fa1a4165c0414e53a), [VKAE](https://huggingface.co/collections/FINAL-Bench/vkae-accelerated-6a47231d7e7999dd8227675a).

</details>

## References

- [Source card and publisher measurements, revision 69fc3dd](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF/blob/69fc3dd1409507de5dc12d81767f909ac2511567/README.md).
- [Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3), [original BF16 evaluation protocol](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI#evaluation-protocol), and [Qwen parent](https://huggingface.co/Qwen/Qwen3.8-Flash-Next).
- [GPQA](https://huggingface.co/datasets/Idavidrein/gpqa), [MMLU-Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro), [MMMU-Pro](https://huggingface.co/datasets/MMMU/MMMU_Pro), [AIME 2026](https://huggingface.co/datasets/MathArena/aime_2026), [HMMT February 2026](https://huggingface.co/datasets/MathArena/hmmt_feb_2026), [LEXam](https://huggingface.co/datasets/LEXam-Benchmark/LEXam), and [LEXam-hard](https://huggingface.co/datasets/joelniklaus/LEXam-hard).
- [Darwin-family paper](https://huggingface.co/papers/2605.14386) and [Latin Square paper](https://huggingface.co/papers/2609.20269).
- [Hugging Face CLI download documentation](https://huggingface.co/docs/huggingface_hub/guides/cli).
- [llama.cpp split loader](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-model-loader.cpp), [qwen4exp at b11048](https://github.com/ggml-org/llama.cpp/blob/b11048/src/models/qwen4exp.cpp), and [loading options at b11048](https://github.com/ggml-org/llama.cpp/blob/b11048/common/arg.cpp).
- [llama.cpp CPU-backend guidance](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md#notes-about-gpu-accelerated-backends).
- [Included ZTC workflow](./ztc/README.md) and [license](./LICENSE).

Documentation reviewed on 2026-11-04.
