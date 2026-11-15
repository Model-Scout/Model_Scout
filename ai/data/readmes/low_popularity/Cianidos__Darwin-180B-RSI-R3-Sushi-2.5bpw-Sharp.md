---
license: other
license_name: qwen-community-1.0
license_link: LICENSE
base_model: FINAL-Bench/Darwin-180B-RSI-R3
base_model_relation: quantized
quantized_by: Cianidos
language: [en, ko, zh, ja, multilingual]
library_name: mlx
pipeline_tag: image-text-to-text
tags:
  - sharp
  - chat-template
  - sushi
  - mlx
  - exl3
  - apple-silicon
  - quantized
  - darwin
  - darwin-rsi
  - qwen4_exp
  - moe
  - reasoning
  - vision-language
  - long-context
---

# Darwin-180B-RSI-R3 — Sushi K2.5 Sharp

**The same Darwin R3 quantized weights as [Cianidos/Darwin-180B-RSI-R3-Sushi-2.5bpw](https://huggingface.co/Cianidos/Darwin-180B-RSI-R3-Sushi-2.5bpw), with the [Qwen Sharp Chat Template](https://huggingface.co/peculiar-ragdoll/Qwen-Sharp-Chat-Templates) by [peculiar-ragdoll](https://huggingface.co/peculiar-ragdoll).** Sharp is the maintainer's preferred everyday variant. It is a prompt-template change, not another fine-tune or requantization.

All **52 weight shards and the n-gram table are byte-identical** to the base Sushi pack. The template is installed both as `chat_template.jinja` and inside `tokenizer_config.json`, because Sushi 1.4.0 prefers the embedded template. The original Darwin model card is preserved at the end of this README.

## Sharp template credit and provenance

- **Template:** [peculiar-ragdoll/Qwen-Sharp-Chat-Templates](https://huggingface.co/peculiar-ragdoll/Qwen-Sharp-Chat-Templates), version **`qwen3.8-froggeric-v22.5.0`**.
- **Pinned revision:** [`6a78b888557f8c9987f51bca98d02d8f69682044`](https://huggingface.co/peculiar-ragdoll/Qwen-Sharp-Chat-Templates/tree/6a78b888557f8c9987f51bca98d02d8f69682044).
- **Template SHA-256:** `cdff39fb26b60dc90faa292e726655c6b21f62db497846e02e4c4bbab942a84a`.
- **Upstream foundation:** [froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates), on which Sharp builds. The upstream Sharp card credits froggeric for the structural template and peculiar-ragdoll for the appended prompt and subsequent changes.
- **License:** Sharp is published under **Apache-2.0**. The template is copied unchanged; the packaged tokenizer config has its `chat_template` field replaced with that exact text. See [LICENSE-SHARP-APACHE-2.0](LICENSE-SHARP-APACHE-2.0) and [SHARP-NOTICE.md](SHARP-NOTICE.md). **Model weights remain under the original Qwen Community License 1.0** in [LICENSE](LICENSE).

Sharp appends concise-answer instructions after the caller's system prompt, preserves reasoning history by default, adjusts tool instructions for thinking-on/off, recognizes inline thinking-control tags, and adds guidance after detected tool errors. It does not alter what the weights know. No measured intelligence or speed advantage over the base Darwin template is claimed here; the preference is based on use, not a controlled comparison.

## Download and run this variant

Tested with **Sushi 1.4.0**, MLX **0.32.3**, Apple **M5 Pro / 48 GiB**, macOS **27.2**. This is a Sushi-format model, not a GGUF or native ExLlamaV3 checkpoint. The complete download remains about **77.36 GB / 72.05 GiB**.

```bash
brew install beamivalice/tap/sushi
sushi --version

hf download Cianidos/Darwin-180B-RSI-R3-Sushi-2.5bpw-Sharp \
  --local-dir "$HOME/.sushi/models/Darwin-R3-Sushi-Sharp"
```

Example using native **262,144-token context**, vision, exact native MTP, KV8 and an SSD-only prefix cache:

```bash
# The owner used this 40 GiB GPU allowance on a 48 GiB Mac.
# It is not a reservation or whole-process RAM cap; do not copy onto a smaller Mac.
sudo sysctl iogpu.wired_limit_mb=40960

SUSHI_PREFIX_CACHE_DIR="$HOME/.sushi/kv-cache-darwin-sharp" sushi serve \
  --model "$HOME/.sushi/models/Darwin-R3-Sushi-Sharp" \
  --host 127.0.0.1 --port 12345 \
  --ssd-budget-gb 28 --wired-margin-gib 2 \
  --ctx-size 262144 --prefill-chunk 1024 \
  --kv-quant 8 --mtp --mtp-head-kv-quant \
  --vision --no-drafter \
  --expert-pick-tolerance 0 \
  --prefix-cache-entries 4 --prefix-cache-mem 0 \
  --prefix-cache-disk 100GB --metrics
```

Open **http://127.0.0.1:12345/** for chat and monitoring. OpenAI API base: **http://127.0.0.1:12345/v1**. Anthropic Messages base: **http://127.0.0.1:12345**. The request model id follows the local directory name, here **`Darwin-R3-Sushi-Sharp`**.

`--ssd-budget-gb 28` is a **28 GiB residency target for weights, expert cache and streaming buffers**, not a cap on the whole process. Active KV/recurrent state and temporary allocations need additional memory. At the trial boot the expert cache held **289/512 experts per layer**; missing experts were read from SSD, not skipped or replaced. Vision is enabled and the MTP head is resident.

The **100 GiB prefix-cache setting is a disk cap**, not an immediate allocation. Idle RAM prefix retention is disabled; matching state is restored into RAM for each active request. Use a separate cache root from the original-template model. Reduce context or streaming budget if memory admission refuses the load; no preflight bypass is part of this recipe. A full 262K prompt plus images was not stress-tested.

The GPU allowance resets at reboot; restore its default with `sudo sysctl iogpu.wired_limit_mb=0`.

### Effort and tools

Sushi supplies Darwin's effort vocabulary: **`off`, `low`, `medium`, `xhigh`**. Choose in the browser or send `reasoning_effort` on OpenAI chat requests. On Anthropic Messages, Sushi also reads `output_config.effort`, including values sent by Claude Code. To set a startup default, append `--think medium` to the serve command. Output-token limits include reasoning and the final answer.

The default template tool format is XML. It preserves normal system instructions and uses the same Qwen thinking/media markers as the original pack. Exact expert routing does not imply byte-identical answers after a prompt-template change.

## Sharp-specific validation

On 2026-10-30, **194 isolated render checks passed** against Jinja sources from Sushi 1.4.0. They covered the pinned Sharp template and the matching template from the Dirk repository, all four Darwin efforts, XML/JSON tool modes, history, media placeholders, late system messages, typed arguments and a prefix-stability case. This is a bounded compatibility matrix, not exhaustive proof.

**6/6 live smoke checks passed** with the Sharp pack:

- Chat with thinking off.
- Clean reasoning/content delivery at low, medium and xhigh.
- Streaming completion and clean content.
- A typed tool call and a follow-up using its result.
- Anthropic `output_config.effort` handling.
- A synthetic red-image perception check.

No Jinja fallback or MLX error appeared during those checks. The local trial shared the base weight files through symlinks; this published repository contains the actual remotely copied files and needs no local base-model installation.

**No Sharp-specific performance benchmark, BF16 KLD/perplexity comparison or standardized quality evaluation has been run.** The performance numbers in the retained conversion notes below were measured with the **original Darwin template on Sushi 1.3.0**, not Sharp on 1.4.0. They must not be presented as Sharp results. The original publishers' Darwin benchmark claims below likewise have not been reproduced for this quantization or template.

---

# Quantization provenance and original-template measurements

The following conversion notes and original Darwin card come from the base Sushi repository at revision `92aa28e48125d3d310fe41ac62886db4c7c2967d`. Commands in those historical sections intentionally point to the **base** pack; use the Sharp launch recipe above for this repository. The old `--codebook mcg` conversion flag shown below belongs to Sushi 1.3.0; Sushi 1.4.0 spells it `--expert-codebook exl3-mcg`.

# Darwin-180B-RSI-R3 — Sushi K2.5 / affine8

A [Sushi](https://github.com/beamivalice/sushi) pack converted directly from the original **Darwin R3 BF16 weights**, for local inference on Apple Silicon. Tested on an **Apple M5 Pro with 48 GiB unified memory**, using SSD expert streaming.

**This is a Sushi-format pack, not a native ExLlamaV3 checkpoint, GGUF, or ordinary Transformers checkpoint.** Use Sushi **1.3.0**; other versions have not been tested here. The n-gram table, vision weights and native MTP head are included. No additional model files are required.

Everything above the **Original model card** divider describes this conversion. The preserved upstream card below describes the original Darwin models and their publishers' results, not measured quality of this quantization.

## Pack and conversion parameters

- **Source:** [FINAL-Bench/Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3), pinned revision [`15495159641ac68386ccf446e34e01fb1ad86b53`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3/tree/15495159641ac68386ccf446e34e01fb1ad86b53).
- **Converter/runtime:** [Sushi v1.3.0](https://github.com/beamivalice/sushi/releases/tag/v1.3.0), release commit `8e4c0af1f5d239dcbed3d58728259432c86f1d96`; MLX `0.32.3`, NAX enabled.
- **Hardware:** Apple M5 Pro, 48 GiB unified memory, macOS 27.0.1, internal SSD, AC power.
- **Routed experts:** EXL3 **K2.5**, **MCG** codebook, **window 15**, including the MTP expert bank. All **512 experts per layer** retained; top-10 routing unchanged. No expert pruning or additional fine-tuning.
- **Dense trunk:** MLX affine **8-bit**, group size **64**, with floating tensors retained as the converter requires.
- **N-gram table:** affine **4-bit**, group size **32**, in `ngram_table.bin`.
- **Calibration:** Sushi's default **65,536-token** prose/code mix; **16 experts per batch**; **float64** Hessian factorization. Calibration-token SHA-256: `7f2a5b1413545d9daf73ef13f06769914c68693121cd86f1e2611bf8d5c419c3`.
- **Native context:** **262,144 tokens**, prompt plus generated response. Native RoPE preserved; no 1M-context extension.
- **Conversion time:** about **3 h 54 min** on this Mac. The process reported **16.88 GB peak physical footprint** during conversion; this is not an inference-memory requirement.

`2.5bpw` names the routed-expert code rate, **not** an average over every tensor or total download size. This is a new quantization of Darwin R3, not a repack of scorpoon's EXL3 SC build and not a reproduction of Sushi's privately tuned official pack recipes.

### Size on disk

| Component | Decimal GB | GiB |
|---|---:|---:|
| Indexed weight shards (52 files) | 45.33 | 42.22 |
| Disk-backed n-gram table | 32.00 | 29.80 |
| Complete download, approximately | 77.36 | 72.05 |

The original BF16 checkpoint is **not needed to run** this pack. Download every shard and `ngram_table.bin`; do not omit the table because it is not a safetensors shard.

## Install and download

Apple Silicon and macOS **26.2 or newer** are required by this Sushi build.

```bash
brew install beamivalice/tap/sushi
sushi --version

hf download Cianidos/Darwin-180B-RSI-R3-Sushi-2.5bpw \
  --local-dir "$HOME/.sushi/models/Darwin-180B-RSI-R3-Sushi-2.5bpw"
```

Use `hf download` for this community pack: Sushi 1.3.0's built-in `sushi pull` accepts only the `beamster` namespace.

## Run on a 48 GiB Mac

### Measured text configuration

This is the configuration used for the performance measurements below: **32K configured context**, **22 GiB streaming budget**, KV8, native MTP, no vision and no prefix-cache reuse.

```bash
sushi serve \
  --model "$HOME/.sushi/models/Darwin-180B-RSI-R3-Sushi-2.5bpw" \
  --host 127.0.0.1 --port 12345 \
  --ssd-budget-gb 22 --ctx-size 32768 \
  --prefill-chunk 1024 --kv-quant 8 \
  --mtp --mtp-head-kv-quant \
  --no-vision --no-drafter \
  --expert-pick-tolerance 0 \
  --prefix-cache-entries 0 --metrics
```

Open **http://127.0.0.1:12345/** for Sushi's browser chat and dashboard. OpenAI-compatible API: **http://127.0.0.1:12345/v1**; Anthropic-compatible API: **http://127.0.0.1:12345**.

### Maximum native context, vision and SSD prefix reuse

This second configuration **passed startup and advertised the full context with vision loaded** on the same 48 GiB Mac. The owner also reports that it works in use. A full **262K-token prompt combined with images has not been stress-tested**, and these are not the settings of the benchmark below.

On this Mac the owner explicitly set the GPU wired-memory allowance to **40 GiB**. This is a system-wide setting, not a reservation or a per-process RAM cap. It resets at reboot. Raising it can put other applications and macOS under memory pressure; do not copy the value onto a smaller Mac.

```bash
# Only for a 48 GiB Mac with sufficient memory available:
sudo sysctl iogpu.wired_limit_mb=40960

sushi serve \
  --model "$HOME/.sushi/models/Darwin-180B-RSI-R3-Sushi-2.5bpw" \
  --host 127.0.0.1 --port 12345 \
  --ssd-budget-gb 28 --wired-margin-gib 2 \
  --ctx-size 262144 --prefill-chunk 1024 \
  --kv-quant 8 --mtp --mtp-head-kv-quant \
  --vision --no-drafter \
  --expert-pick-tolerance 0 \
  --prefix-cache-entries 4 --prefix-cache-mem 0 \
  --prefix-cache-disk 100GB --metrics
```

Restore the macOS default allowance with `sudo sysctl iogpu.wired_limit_mb=0`.

### What the memory flags mean

- **`--ssd-budget-gb` is a RAM residency target**, in GiB, for the resident trunk, enabled MTP/vision, streaming buffers and expert cache. It is **not SSD storage space** and **not a hard cap on total process memory**. Active KV/recurrent state, temporary computation, CPU allocations and the OS file cache need additional memory.
- At the measured **22 GiB**, text-only/MTP setup, the startup ledger allocated **16.05 GB** for experts: **215 of 512 cache slots per layer**. Missing experts are read from SSD; none are permanently removed.
- At **28 GiB with vision**, the startup ledger allocated **21.57 GB** for experts: **289 of 512 slots per layer**. The 2 GiB wired margin leaves a **38 GiB planning ceiling** under the owner's 40 GiB allowance; it does not guarantee that total process footprint stays below 38 GiB.
- **`--expert-pick-tolerance 0` preserves exact expert routing.** There is no lossy substitution of a cached expert for a selected expert.
- **`--prefix-cache-disk 100GB` is a 100 GiB disk-capacity limit**, not an immediate 100 GiB allocation. `--prefix-cache-mem 0` disables idle RAM retention; matching prompt state is restored from SSD into RAM for the active request. Prefix state can survive a server restart. This is separate from the model-weight expert cache.
- A larger context, images, other loaded models or other applications may require lowering the streaming budget. Memory refusals should be addressed by reducing the plan, not disabling admission checks.

For byte-stable comparisons, keep prefix caching off: hybrid Qwen cache restoration can change rounding relative to a cold prefill. Ordinary chat benefits from prefix reuse.

## Performance measured on the M5 Pro / 48 GiB

**Date:** 2026-10-25. Sushi **1.3.0**, release binary SHA-256 `6e2527f18c8f214976cdb9a979eb919196599686e3678595eeab93c4d28441e3`.

Measured with **llmprobe 0.6.17**, greedy, reasoning off, **three measured runs after warmup**, using the text configuration above. Processes used foreground QoS (`taskpolicy -a`); AC power, no concurrent model server, a three-minute initial cooldown, system automatic fans. No manual fan control or die-temperature measurement. Serial and MTP ran sequentially in the same session, not as an interleaved A/B.

| Mode | Decode tok/s, median (min–max) | Prefill tok/s, median (min–max) |
|---|---:|---:|
| Plain decoding (`--no-mtp`) | 26.2 (24.9–26.5) | 412.9 (411.7–413.4) |
| Native MTP (`--mtp --mtp-head-kv-quant`) | 36.0 (35.3–38.0) | 399.8 (392.6–400.0) |

Headline prefill workload: **10,406 input tokens**. Separate context-ladder results:

| Actual input tokens | Serial prefill / decode tok/s | MTP prefill / decode tok/s |
|---:|---:|---:|
| 512 | 171 / 22.6 | 170 / 31.1 |
| 2,109 | 288 / 21.2 | 283 / 29.3 |
| 8,250 | 279 / 21.2 | 274 / 29.7 |

At 8,250 input tokens, the MTP arm's median time to first token was **30.1 seconds**. The harness classified sustained-load drift as steady in both arms. It also reported that the engine ignored `ignore_eos`/`min_tokens`, so decode samples followed the model's own stopping behavior and did not all generate equal-length outputs. These custom runs are not comparable to default llmprobe runs or anecdotal Strata results.

The MTP arm's **MLX allocator peak was 24.38 GiB**; this is not total process or system memory. The full-context/vision configuration above was only startup-checked separately and has no matching performance result here.

Benchmark invocation, once per server mode:

```bash
npx --yes llmprobe@0.6.17 http://127.0.0.1:12345 \
  -m Darwin-180B-RSI-R3-Sushi-2.5bpw \
  --bench-only --reasoning off --rungs 512,2k,8k --runs 3 \
  --no-color --no-save --save bench.json
```

The measured local pack directory was named `Darwin-180B-RSI-R3-Sushi-K2.5`; the download command above uses this repository's name, so the model id in the example follows that directory instead. Weight bytes are unchanged.

## Validation and quality limits

- Pack structure checked: **3,069 indexed tensors**, valid safetensors spans, **52 indexed shards**, all 48 routed-expert layers and MTP present.
- **5/5 serial and 6/6 MTP functional checks passed:** chat, stream/non-stream bytes on one prompt, a forced tool call with typed arguments, JSON output, Anthropic Messages and one MTP/serial greedy answer comparison.
- Five one-shot reasoning/debugging questions gave correct final answers. One scheduling answer had inconsistent table intervals despite the correct optimum and critical-path proof. This is a smoke test, not a standardized model-quality benchmark.
- **No BF16 KLD or perplexity comparison was performed.** The original Darwin benchmark scores below have not been reproduced for this quantization. Quantization is lossy; no BF16-equivalence claim is made.
- Vision weights loaded successfully in the second configuration; no controlled image-quality evaluation was performed here. Native context is 262K, but the longest timed prompt in this report was 10,406 tokens.
- No external DFlash2 drafter was used or tested. The native MTP head is included and was observed engaging with exact acceptance.
- No ZTC confidence probe or extra ZTC-serving integration is included; those claims belong to the original model card.

## Conversion command

The following parameters were used with the released Sushi 1.3.0 binary. Replace the paths with your local source and output directories. The original BF16 source is about **360 GB**; it does not have to fit in RAM because conversion is layer-by-layer. Leave disk room for the source, output and scratch files. Conversion supports `--resume`.

```bash
hf download FINAL-Bench/Darwin-180B-RSI-R3 \
  --revision 15495159641ac68386ccf446e34e01fb1ad86b53 \
  --local-dir /path/to/Darwin-R3-BF16

caffeinate -i /usr/bin/time -l sushi convert exl3 \
  --model /path/to/Darwin-R3-BF16 \
  --out /path/to/Darwin-R3-Sushi-K2.5 \
  --experts-k 2.5 --codebook mcg --window 15 \
  --trunk-bits 8 --trunk-group 64 \
  --calib-tokens 65536 --batch 16 --factor-precision 64
```

## Credits and license

Darwin training and upstream evaluations: **FINAL-Bench / VIDRAFT**. Parent architecture and model: **Qwen**. Converter, runtime and pack format: **Sushi / beamivalice**. The original **Qwen Community License 1.0** is included unchanged in [LICENSE](LICENSE); its commercial-use conditions apply. No broader license is granted by this conversion.

---

# Original model card

The following body is preserved from the pinned BF16 source README. Its BF16/vLLM/Transformers instructions describe the **original model**, not this Sushi pack. Benchmark claims and comparisons are the original publishers' statements.

# Darwin-180B-RSI-R3

### 180B Mixture-of-Experts · vision-language · **#1 on ExtractBench (90.29)** · the Darwin-180B-RSI line now holds **ten Hugging Face official #1s**: nine by [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) (R1) and ExtractBench by R3 · **self-improving**

> 🥇 **R3 is #1 on the [ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) leaderboard (90.29)**, ahead of its own parent Qwen3.8-Flash-Next (89.88), and #3 on [EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) (77.83).

> 💻 **Run it on your own machine: [POCKET-Darwin-180B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)**, the 4-bit GGUF of R3 (111 GB), runs on a **laptop with an 8 GB GPU and 32 GB RAM**, **CPU only at 18–21 tok/s**, a 128 GB mini PC or one DGX Spark. MMLU-Pro is **identical to BF16 (87.65%)**.

`reasoning` · `MoE 512 experts` · `262K long context` · `image + text` · `Korean + English` · `self-improvement` · `structured output` · `ZTC`

<p align="center">
<a href="https://vidraft.net"><img src="https://img.shields.io/badge/🌐_VIDRAFT-vidraft.net-111827?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/llamaindex/ExtractBench"><img src="https://img.shields.io/badge/ExtractBench_(R3)-90.29_%231-059669?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/FutureMa/EvasionBench"><img src="https://img.shields.io/badge/EvasionBench_(R3)-77.83_%233-0d9488?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/datasets/Idavidrein/gpqa"><img src="https://img.shields.io/badge/GPQA_Diamond_(R1)-94.44%25_%231-gold?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro"><img src="https://img.shields.io/badge/MMLU--Pro_(R1)-88.12%25_%231-2563eb?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MMMU/MMMU_Pro"><img src="https://img.shields.io/badge/MMMU--Pro_(R1)-79.48%25_%231-0891b2?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/aime_2026"><img src="https://img.shields.io/badge/AIME_2026_(R1)-100%25_%231-dc2626?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/hmmt_feb_2026"><img src="https://img.shields.io/badge/HMMT_Feb_2026_(R1)-100%25_%231-ea580c?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LEXam-Benchmark/LEXam"><img src="https://img.shields.io/badge/LEXam_(R1)-68.94%25_%231-4f46e5?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/joelniklaus/LEXam-hard"><img src="https://img.shields.io/badge/LEXam--hard_(R1)-45.72_%231-6d28d9?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0"><img src="https://img.shields.io/badge/IFStruct_(R1)-98.95%25_%231-b45309?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/Delores-Lin/MDPBench"><img src="https://img.shields.io/badge/MDPBench_(R1)-83.65_%231-0f766e?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/Round_1-Darwin--180B--RSI-e11d48?style=for-the-badge"></a>
<a href="https://arxiv.org/abs/2605.14386"><img src="https://img.shields.io/badge/arXiv-2605.14386_Darwin_Family-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/papers/2609.20269"><img src="https://img.shields.io/badge/Paper-2609.20269_Latin_Square-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🧬_Collection-Darwin_Family-16a34a?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/💻_POCKET_4--bit-Laptop_·_CPU_only_·_DGX_Spark-0f766e?style=for-the-badge"></a>
</p>

**The second round of model-level self-improvement on top of [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI).**
R3 continues training from R1 with the same recipe: the model solves verifiable problems, keeps only its own solutions that check out as correct, and trains on them. No human-written solutions or reasoning traces are used.
R3 is released so anyone can download it, run it, and check the numbers below.

---

## 🏆 Ten #1s in the Darwin-180B-RSI line

Hugging Face **official** benchmark leaderboards. Each score is listed under the model that produced it.

| Benchmark | Score | Model | Leaderboard |
|:---|:---:|:---|:---|
| **ExtractBench** (370 documents) | **90.29** | **R3 (this model)** | [**#1**](https://huggingface.co/datasets/llamaindex/ExtractBench) |
| **GPQA Diamond** (198) | **94.44** | R1 ([Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)) | [**#1**](https://huggingface.co/datasets/Idavidrein/gpqa) |
| **MMLU-Pro** (12,032) | **88.12** | R1 | [**#1**](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) |
| **AIME 2026** (30) | **100.0** | R1 | [**#1**](https://huggingface.co/datasets/MathArena/aime_2026) |
| **HMMT Feb 2026** (33) | **100.0** | R1 | [**#1**](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) |
| **MMMU-Pro** (vision, 1,730) | **79.48** | R1 | [**#1**](https://huggingface.co/datasets/MMMU/MMMU_Pro) |
| **LEXam** (law, MCQ 4-choice, 1,655) | **68.94** | R1 | [**#1**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| **LEXam-hard** (law, open-ended, 518) | **45.72** | R1 | [**#1**](https://huggingface.co/datasets/joelniklaus/LEXam-hard) |
| **IFStruct** (structured output, 2,000 prompts) | **98.95** | R1 | [**#1**](https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0) |
| **MDPBench** (multilingual document parsing, 2,720 pages) | **83.65** | R1 | [**#1**](https://huggingface.co/datasets/Delores-Lin/MDPBench) |

R3's own leaderboard entries:

| Benchmark | R3 | Leaderboard | Setting |
|:---|:---:|:---|:---|
| **ExtractBench** (370 documents) | **90.29, #1** | [llamaindex/ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) | official harness, 32,768 max tokens (same as the parent), temperature 0, thinking off, single run |
| **EvasionBench** (16,726 questions) | **77.83, #3** | [FutureMa/EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) | inspect-ai task from the dataset eval.yaml, temperature 1.0, top_p 0.95, 8,192 max tokens, thinking on, single run |

Full settings are recorded in [`.eval_results/`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3/tree/main/.eval_results).

### R1 head-to-head with Chinese frontier models

![Darwin-180B-RSI vs Chinese frontier models](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI/resolve/main/assets/bench_vs_china.png)

| Model | AIME 2026 | GPQA Diamond | MMLU-Pro | MMMU-Pro | HMMT Feb 2026 | LEXam | LEXam-hard |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **🧬 Darwin-180B-RSI, R1 (ours · 🇰🇷)** | **100** 🥇 | **94.44** 🥇 | **88.12** 🥇 | **79.48** 🥇 | **100** 🥇 | **68.94** 🥇 | **45.72** 🥇 |
| Inkling (Thinking Machines) | · | · | · | · | · | · | 40.82 |
| Kimi-K3 (Moonshot AI) | · | 93.5 | · | · | · | · | 29.54 |
| Kimi-K2.6 (Moonshot AI) | 96.4 | 90.5 | · | 79.4 | 92.7 | · | 36.18 |
| DeepSeek-V4-Pro (DeepSeek) | · | 90.1 | 87.5 | · | · | · | 38.93 |
| Qwen3.5-397B-A17B (Alibaba) | 93.33 | 88.4 | 87.8 | · | 87.88 | · | · |
| MiniMax-M2.1 (MiniMax) | · | 80.81 | 88 | · | · | · | · |
| GLM-5 (Zhipu AI) | 95.83 | 86 | 86 | · | 86.36 | · | · |
| Intern-S2-Preview (Shanghai AI Lab) | · | · | 88 | 76.88 | 87.31 | · | · |
| Step-3.5-Flash (StepFun) | 96.67 | 83.5 | 84.4 | · | 86.36 | · | · |
| DeepSeek-R1 (DeepSeek) | · | · | · | · | · | 52.41 | · |
| Qwen3-235B-A22B-Thinking-2507 (Alibaba) | · | · | · | · | · | 48.19 | · |

<sub>Scores as listed on the Hugging Face official benchmark leaderboards (self-reported by each model's publisher). "·" = not reported. Open-weight models only; closed API models are not included. Settings (samples, voting, thinking budget) differ across models. R1 settings are in the evaluation protocol below.</sub>

---

## 🧬 What changed from R1

- **Starting point:** R1 weights (not the parent). R3 is a true second round.
- **Practice problems:** 3,000 SuperGPQA questions (middle and hard difficulty) that were never used in R1 training. R1 solved each one 8 times.
- **What it learned from:** only the "boundary" problems, where R1 was right on 2 to 6 of 8 attempts (462 problems). From those, up to 2 of R1's own correct, untruncated solutions per problem (714 solutions in total).
- **What was trained:** the same components as R1 (attention paths and shared experts) via LoRA, then merged. All 512 routed experts, the router and the vision encoder are unchanged.
- **No benchmark data:** GPQA Diamond and the held-out set below were never used for training or selection.

### Held-out SuperGPQA, 1,000 questions never used in training or selection
4 samples per question, 16K thinking budget, temperature 1.0.

| Model | Single sample | Mean of 4 | Majority of 4 |
|---|---:|---:|---:|
| R1 (Darwin-180B-RSI) | 65.30 | 65.67 | 68.30 |
| **R3 (this model)** | **66.30** | **66.70** | **69.00** |

Paired per-question difference, R1 → R3 (mean of 4): **+1.03 points, 95% CI [+0.05, +2.00]**. The second round of self-improvement produced a measurable gain over R1.

### GPQA Diamond, 198 questions
8 samples per question, 32K thinking budget, temperature 1.0.

| Model | Single sample | Mean of 8 | Majority of 8 |
|---|---:|---:|---:|
| R0 (parent, Qwen3.8-Flash-Next) | 84.85 | 85.35 | 90.91 |
| R1 (Darwin-180B-RSI) | 84.85 | 85.80 | 89.90 |
| **R3 (this model)** | **85.86** | **86.05** | 90.40 |

---

## 🧬 The Darwin Family

<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/Darwin--180B--RSI-9×_%231-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC"><img src="https://img.shields.io/badge/Darwin--397B--ZTC-GPQA_93.43-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/Darwin--28B--REASON-GPQA_89.39-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/Darwin--35B--A3B--Opus-♥98-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/Darwin--36B--Opus-♥97-e11d48"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/Darwin--4B--Genesis-♥63-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/Darwin--9B--NEG-♥57-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF"><img src="https://img.shields.io/badge/POCKET--35B-824K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF"><img src="https://img.shields.io/badge/POCKET--26B-365K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/POCKET--Darwin--180B-4--bit_R3_·_laptop-1f6feb"></a>
</p>

**Darwin** is [VIDRAFT](https://vidraft.net)'s measurement-driven reasoning model family: **50+ official models**, **400+ community derivatives**, and two places in the GPQA Diamond top 3 (Darwin-180B-RSI #1 · Darwin-397B-ZTC #3).

### Darwin: evolve the parent, keep what works

Darwin treats a strong open model as a **parent**. It measures where the parent is weak and strengthens exactly those parts, instead of re-training everything and risking what already works.

- **Diagnose before you change.** Every Darwin generation starts from a measured weakness map of the parent.
- **Change little, precisely.** Darwin modifies a small, targeted fraction of the network. Knowledge stored in the experts is preserved.
- **Proven capability over new guesses.** Earlier Darwin generations grafted the best-performing expert/FFN blocks from other strong models onto a base backbone; the RSI line adds a new ingredient: **the model's own verified work**.
- **Measured, not claimed.** Every change must beat its predecessor on held-out tests before it ships.

### Lineage

| Role | | |
|:---|:---|:---|
| **R0, parent** | `Qwen/Qwen3.8-Flash-Next` | 180B MoE vision-language backbone · Qwen Community License 1.0 |
| **R1** | [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) | first RSI round: the parent's own verified solutions fed back as training signal · nine #1s |
| **R3 (this model)** | Darwin-180B-RSI-R3 | second RSI round, trained from R1 on R1's own verified solutions · ExtractBench #1 |
| **Preserved** | 512 routed experts · router · vision encoder | untouched in every round |

---

## 🔁 RSI: a model that improves from its own work

**Recursive self-improvement (RSI)** is the core of this line. Instead of distilling a bigger teacher, the model improves by learning from itself:

1. **Solve:** the model works through practice problems it has never seen in evaluation.
2. **Verify:** its answers are checked against verifiable references (answer keys, executable checks). Nothing unverified is learned.
3. **Learn:** it is re-trained on the reasoning that turned out to be correct.
4. **Repeat:** the improved model becomes the next solver. R1 was round one; R3 is the next round.

Practice sets are deduplicated against every evaluation set we report (8-gram overlap filter).

### Model-level RSI vs. harness-level RSI

Darwin-180B-RSI-R3 is **Model-level RSI**: the model itself (its weights) improves by learning only from its own solutions. No human-written solutions or reasoning traces are used; correctness is checked automatically. **Harness-level RSI** (e.g., Google's RRSI) improves the prompts, tools and workflow around a fixed model. It is like rewriting an employee's manual, while Model-level RSI is the employee getting smarter. The two are complementary.

---

## 🏛️ ZTC: it knows before it answers

**Zero-Token Confidence (ZTC)** reads the model's own internal state **once, before generation**, and returns the probability that the answer it is about to give is correct, with **no extra tokens and no second model.**

```json
{"answer": "...", "confidence": 0.93, "ztc_score": 1.84, "truncated": false}
```

The ZTC probe published with [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) was fitted on R1's hidden states. A probe fitted on R3 will be added to this repository; until then, use R1's probe only as a rough signal.

---

## 📐 Evaluation protocol

**R3 entries (ExtractBench, EvasionBench):** see the settings column in the table above and [`.eval_results/`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3/tree/main/.eval_results). ExtractBench was run with thinking turned off (`chat_template_kwargs: {"enable_thinking": false}`), which suits schema-guided extraction.

**R1 entries (its #1s):**

| Setting | Value |
|:---|:---|
| Thinking budget | **131,072 tokens** (32,768 for LEXam and LEXam-hard) |
| Sampling | temperature 1.0 · top_p 0.95 · top_k 20 |
| Precision | bf16 |
| Engine | vLLM, tensor parallel 8 (or 4), expert parallel |

| Benchmark | Samples per question | Reported score |
|:---|:---:|:---|
| AIME 2026 | 16 | majority vote (maj@16); mean over 16 = 98.75 |
| HMMT Feb 2026 | 16 | majority vote (maj@16); mean over 16 = 96.59 |
| GPQA Diamond | up to 16 | majority vote |
| MMLU-Pro | 1 | single sample (no voting) |
| MMMU-Pro (vision) | 3 | majority vote (maj@3) |
| LEXam | 4 | majority vote (single sample 60.54 · mean 61.42) |
| LEXam-hard | 1 | single sample, judged by DeepSeek-R1-0528 per the official eval.yaml |
| IFStruct | 1 | single run, temperature 0, 16,000 max tokens (official harness defaults) |
| MDPBench | 1 | single run, temperature 0, 32,768 max tokens, thinking on (pages with no transcription re-read with thinking off) |

All numbers are self-measured and reproducible with the settings above. Majority-vote scores are system scores (several samples per question) and are labeled as such.

---

## ⚙️ Specifications

| | |
|:---|:---|
| Architecture | Mixture-of-Experts, hybrid attention (36 linear-attention + 12 full-attention layers) |
| Layers / hidden | 48 / 2,560 |
| Experts | 512 routed (10 active per token) + shared expert |
| Context | 262,144 tokens |
| Vocabulary | 248,320 |
| Modalities | image + text → text |
| Precision | bf16 (~336 GB) |

---

## 🚀 Quickstart

### Serving with vLLM (8 × B200 or equivalent)

```bash
vllm serve FINAL-Bench/Darwin-180B-RSI-R3 \
  --tensor-parallel-size 8 --enable-expert-parallel \
  --max-model-len 139264 --trust-remote-code
```

### Chat Completions (OpenAI-compatible)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:8000/v1", api_key="-")
r = c.chat.completions.create(model="FINAL-Bench/Darwin-180B-RSI-R3",
    messages=[{"role": "user", "content": "Explain why the sky is blue in two sentences."}],
    temperature=1.0, top_p=0.95, extra_body={"top_k": 20})
print(r.choices[0].message.content)
```

For structured extraction (JSON to a schema), turn thinking off, as in the ExtractBench run:

```python
r = c.chat.completions.create(model="FINAL-Bench/Darwin-180B-RSI-R3", messages=msgs, temperature=0,
    response_format={"type": "json_object"},
    extra_body={"chat_template_kwargs": {"enable_thinking": False}})
```

### Transformers

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
model_id = "FINAL-Bench/Darwin-180B-RSI-R3"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
```

**Tip:** for hard reasoning, keep thinking on and give it room (a thinking budget of 32K to 131K tokens). For document extraction, thinking off was faster and scored higher in our ExtractBench runs.

---

## ⚠️ Limitations and disclosure

- Scores are self-measured with the settings stated above; majority-vote numbers use several samples per question.
- Very long reasoning is normal for hard problems; a short thinking budget will truncate answers and lower accuracy.
- Like every LLM, the model can be confidently wrong. Use a confidence readout such as ZTC to gate high-stakes actions.

---

## 🔗 Related Darwin Models

- **[Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)**: R1, the model R3 was trained from, #1 on nine Hugging Face official leaderboards
- **[POCKET-Darwin-180B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)**: 4-bit GGUF of R3 for laptops, CPU-only machines and DGX Spark
- **[Darwin-397B-ZTC](https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC)**: 397B MoE (FP8), GPQA Diamond 93.43 %, ZTC on board
- **[Darwin-28B-REASON](https://huggingface.co/FINAL-Bench/Darwin-28B-REASON)**: 28B, GPQA Diamond 89.39 %
- **[Darwin-27B-RSI](https://huggingface.co/FINAL-Bench/Darwin-27B-RSI)**: 27B, the first Darwin RSI model
- **[ZTC-Judge-27B](https://huggingface.co/FINAL-Bench/ZTC-Judge-27B)**: standalone ZTC judge

---

## 📚 Citation

```bibtex
@misc{darwin180b_rsi_r3_2026,
  title  = {Darwin-180B-RSI-R3: A Second Round of Model-Level Self-Improvement for a 180B Mixture-of-Experts Reasoning Model},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3}},
  note   = {ExtractBench 90.29}
}

@misc{darwin180b_rsi_2026,
  title  = {Darwin-180B-RSI: Recursive Self-Improvement on Verified Answers for a 180B Mixture-of-Experts Reasoning Model},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-180B-RSI}},
  note   = {GPQA Diamond 94.44 \% · MMLU-Pro 88.12 \%}
}

@misc{darwin_family_2026,
  title  = {Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning},
  author = {Kim, Taebong and Hong, Youngsik and Kim, Minsik and Choi, Sunyoung and Jang, Jaewon and Shin, Junghoon},
  year   = {2026},
  eprint = {2605.14386},
  archivePrefix = {arXiv}
}
```

---

## 📜 License

Darwin-180B-RSI-R3 is a derivative of **Qwen3.8-Flash-Next** (through Darwin-180B-RSI) and is distributed under the **Qwen Community License 1.0** (see [LICENSE](LICENSE)).

## 🏢 About

Built by **[VIDRAFT](https://vidraft.net)** · evaluated with **FINAL-Bench**. Part of the [Darwin Family](https://arxiv.org/abs/2605.14386).
