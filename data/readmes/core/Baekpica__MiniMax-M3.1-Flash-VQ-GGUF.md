---
license: other
license_name: minimax-community
license_link: LICENSE
base_model: MiniMaxAI/MiniMax-M3.1-Flash
base_model_relation: quantized
pipeline_tag: image-text-to-text
language:
- en
- ko
- zh
- ja
tags:
- minimax
- minimax-m3
- gguf
- vector-quantization
- vq
- residual-vq
- imatrix
- importance-matrix
- calibration
- mixture-of-experts
- sparse-attention
- msa
- multimodal
- vision
- video
- 1m-context
- speculative-decoding
- dspark
- dgx-spark
- gb10
- ds4
- ds4-dfm-rs
---

# MiniMax-M3.1-Flash VQ GGUF

> [!WARNING]
> **Experimental low-bit release.** The routed experts, which hold 97% of the weights, are stored
> at about **2.0 bits per weight** (13-bit vector codes everywhere, plus an 8-bit residual stage on
> the 20 layers where it was measured to help most), far below common 4-bit GGUF quants.
> Expect failures the source model rarely shows: reasoning that loops, text that breaks
> mid-character (`�`) or switches language, weaker answers. Treat it as quantization research.
>
> **Problems or odd output?** Post them in the
> [Community tab](https://huggingface.co/Baekpica/MiniMax-M3.1-Flash-VQ-GGUF/discussions), even as
> rough notes. The prompt, sampling settings and runtime commit help most.

**MiniMax's 428B native multimodal MoE with its full 1,048,576-token context, its sparse attention,
its vision/video tower and its DSpark draft head, sized for one 128 GB DGX Spark.** The 236 GB
checkpoint (NVFP4 experts, MXFP8 attention) becomes **115.5 GB** of GGUF parts, of which
**111.3 GB (103.7 GiB) stay resident**; the BF16 token table and the vision tower are read from SSD, and the
attention K/V of a long session lives on SSD, addressed block by block by the model's own MSA
indexer.

> **Runtime support, 2026-10-24:** runs on one DGX Spark with the ds4-dfm-rs `minimax_m3_vq` family
> ([draft PR #110](https://github.com/Baekpica/ds4-dfm-rs/pull/110), not merged yet): text, images and video, the DSpark draft head and the native context.
> **Performance, 2026-10-27:** 2K–64K with DSpark: **1,011.0 tok/s prefill, 22.10 tok/s decode**
> ([below](#dgx-spark-performance), median of three run means). The historical 1,048,319-token prompt prefilled at 580 tok/s and
> decoded. Converted 2026-10-23: 61 independent GGUF parts (115,526,325,376 bytes), every payload
> hash in `tensor-manifest.json`, all 89,729 source tensors accounted for; codebooks fitted with
> calibration statistics from 4.18M tokens (text, images and video) run through the original
> checkpoint. **Measured against the original, teacher-forced on held-out chats: KL 0.150 and the
> same next token 88.2% of the time on assistant turns** (the original batched differently: KL
> 0.003). The memory and kernel budgets below are the design computed from exact byte layouts.

## At a glance

| | |
|---|---|
| Source | [`MiniMaxAI/MiniMax-M3.1-Flash`](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/tree/54e4e69dfc452b1e94a426c24a4fdeeaa8e3ad5e) at `54e4e69dfc452b1e94a426c24a4fdeeaa8e3ad5e` (routed experts NVFP4, attention / dense / shared MXFP8, quantization-aware trained) |
| Model | 60 layers (3 dense + 57 MoE), hidden 6,144, 128 routed experts top-4 (sigmoid + correction bias, × 2.0) + 1 shared expert, expert FFN 3,072, SwiGLU-OAI; GQA 64 query / 4 KV heads × 128 with per-head Gemma QK-norm and partial RoPE (64 of 128 dims, θ 1e7); MiniMax Sparse Attention (MSA) on every layer; vocabulary 200,064; 413.1B routed-expert weights |
| Recipe | `minimax-m31f-vq8-r13x57-r8x20-q4k-nvfp4idx-ssdkv-embssd-v1` (`recipe.json`) |
| Routed experts | 8-dim VQ, one E4M3 codebook per layer shared by all 128 experts and gate/up/down, one F16 gain per row. **13-bit (K = 8,192) on all 57 MoE layers; an 8-bit residual stage (K = 256) on layers 16, 18–32, 35, 40, 43 and 53 (R13+8), chosen by an end-to-end measurement.** 1.63 bpw on 37 layers, 2.63 on 20, **1.98 on average**. Codebooks, assignments and row gains fitted with calibration-weighted Lloyd (an importance matrix for VQ) |
| Attention q/k/v/o, shared experts, dense FFN (0–2), output head | Q4_K with per-column importance from calibration |
| MSA indexer projections (index_q / index_k) | Q8_0 |
| Kept at source precision | router (F32) and correction bias, every RMSNorm and QK-norm |
| Token embedding | BF16, its own part, read in rows from SSD (one 12,288-byte row per token) |
| Vision / video tower | Original BF16 (632M ViT + projector + 2×2 merge MLP), its own part, memory-mapped and read only when an image or video arrives (DeepSeek V4.1 VQ practice) |
| Speculative decoding | MiniMax's DSpark draft head (5 layers, block 7, Markov head), Q8_0, resident (2.03 GiB) |
| Context | **1,048,576 tokens**, the model's own; one bank on one DGX Spark |
| KV contract | MSA index keys **resident** in NVFP4 (72 B per token and layer, 4.22 GiB at 1M); main K/V in NVFP4 (576 B per token and layer, 33.75 GiB at 1M) **on SSD**, read per selected block |
| Chat template | Original `chat_template.jinja`, unchanged (`<mm:think>` reasoning, adaptive thinking, `reasoning_effort`, XML tool calls with the `]<]minimax[>[` namespace, image/video placeholders) |
| Fidelity (release bytes vs the original, assistant turns) | KL **0.150**, same top-1 **88.2%** (13-bit everywhere: 0.223; [details](#measured-on-the-converted-bytes)) |
| Runtime | [ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs), family `minimax_m3_vq` ([draft PR #110](https://github.com/Baekpica/ds4-dfm-rs/pull/110)) |

## DGX Spark performance

Remeasured **2026-10-27**, after three adopted prefill and three adopted plain-decode rounds in
[ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs/blob/9b9dc795697c8182825bfe716fe1ca8eab0519ee/docs/minimax-vq-optimization-2026-10-27.md), native source `84960118`.
One DGX Spark / GB10, CUDA 13.4.92, driver 615.71.10; operator-managed **300–2200 MHz** range,
observed busy SM **2,177–2,190 MHz**. Model weights and the release manifest are unchanged.

Three fresh benchmark processes cover 32 frontiers from 2K to 64K. Each adds 2,048 prompt tokens,
generates 128 forced non-EOS greedy tokens with **gated DSpark draft 3**, then restores the prompt
snapshot. The allocated context is 524,288 tokens: index keys resident, K/V pages in the SSD tier
(0.66 GiB pinned pool and 0.07 GiB prefill stage). The workspace cap is **2,048 rows**, matching each
actual frontier, rather than the older 4,096-row cap. Prompt: `speed-bench/promessi_sposi.txt`.
There is no extra 4K warmup; 2K is each process's first measured prefill.

![MiniMax-M3.1-Flash VQ prefill and DSpark decode on one DGX Spark, 2K to 64K](assets/minimax-vq-spark-64k-throughput.png)

| Median of three run means | Prefill tok/s | Decode tok/s |
|---|---:|---:|
| DSpark draft 3 gated, 2K–64K | **1,011.0** | **22.10** |
| DSpark draft 3 gated, 2K–32K | 1,033.1 | 21.90 |

| Frontier | 2K | 4K | 8K | 16K | 32K | 48K | 64K |
|---|---:|---:|---:|---:|---:|---:|---:|
| Prefill tok/s | 983.5 | 1,069.3 | 1,054.6 | 1,036.4 | 1,007.0 | 988.7 | 966.6 |
| Decode tok/s | 24.27 | 24.94 | 19.64 | 21.86 | 20.21 | 26.70 | 19.80 |

Curves are per-frontier medians; bands show the observed min–max of the three runs, not a confidence
interval. Legends use the median of run means. Run-mean ranges are **0.19% prefill / 1.39% decode**.
The timing-based gate can choose different draft/plain call sequences in a short frontier despite
identical output: at 58K, **48 / 48 / 74 calls**, **27.11 / 26.92 / 22.71 tok/s**, a 16.34% min–max
range relative to the median. The bands retain that variability; these are prose-specific adaptive
decode measurements, not a fixed steady rate at every frontier.

All 96 frontier observations have 200,064 finite logits and 128 generated IDs; repeats agree bit for
bit on all logits and tokens. The recorded cycles confirm speculative mode and draft 3. All three
guard/payload exits are 0, full-run memory PSI is 0, minimum available host memory is **5.88 GiB**.
CPU helpers use performance cores `5-9,15-19`; the serial submission thread stays on CPU 5.
The first default-cap run lost its controller to systemd-oomd and is excluded from the graph; the
three retained runs use the smaller workspace and a PSI abort threshold as well as the 2 GiB guard.

The separate **resident plain-decode** adoption cohort uses a 131,072-token allocation, 4,096-row
warmup/chunks, MTP off and 1,024 generated tokens. 64K is a 57,344-token suffix after restoring 8K:

| Resident frontier | Prefill tok/s | Plain decode tok/s |
|---|---:|---:|
| 8K | 1,224.27 | 21.45 |
| 64K | 1,144.61 | 21.09 |

The [per-round report](https://github.com/Baekpica/ds4-dfm-rs/blob/9b9dc795697c8182825bfe716fe1ca8eab0519ee/docs/minimax-vq-optimization-2026-10-27.md) records each matched A/B,
exact-output gates, rejected probes and costs. The six marginal gains are not added or multiplied.
The [fresh sweep receipt](https://github.com/Baekpica/ds4-dfm-rs/blob/9b9dc795697c8182825bfe716fe1ca8eab0519ee/docs/benchmarks/minimax-vq-spark-64k-2026-10-27/README.md) retains
all CSVs, raw clocks, conditions, correctness/cycle hashes, frozen binary identity and the command.

The [previous graph](https://huggingface.co/Baekpica/MiniMax-M3.1-Flash-VQ-GGUF/resolve/2789cbaf1b7dce505d55d6026a67c10e1815c78c/assets/minimax-vq-spark-64k-throughput.png)
(2026-10-24, 905.1 / 19.56) remains historical. Its clock metadata is unreconciled, and runtime,
workspace cap and proof collection differ, so no cumulative A/B percentage is claimed.
[Dated 124K/256K/1M records](https://github.com/Baekpica/ds4-dfm-rs/blob/9b9dc795697c8182825bfe716fe1ca8eab0519ee/docs/minimax-vq.md#historical-frontiers-2026-10-24) remain
separate; no HTTP, vision, full-512K or 1M gate was rerun for this graph.

## Why this design: MSA keeps every token, the indexer says which ones to read

Beam-1.0 VQ and DeepSeek-V4.1 VQ ship more than 100 GB of weights and still serve 1M tokens on one
Spark, because the part of their attention state that grows with the context is small:

| | Beam-1.0 (501B) | DeepSeek-V4.1 Flash | **MiniMax-M3.1-Flash (428B)** |
|---|---|---|---|
| What grows with the context | 9 full GQA layers of 52 (43 are 512-token sliding windows) | compressed latents, produced at a few source layers and shared forward | **all 60 layers**: MSA keeps the full history of every layer |
| Per token and layer | K + V, 8 heads × 128 | one 512-wide latent (K = V), compressed 2:1 / 1:1 | K + V, 4 heads × 128, plus one 128-wide index key |
| Cache format in the VQ runtime | FP8 E4M3 + f16 scale per head | the official FP4 (E2M1 + E4M3 per 16) + MXFP4 index key | NVFP4 (E2M1 + E4M3 per 16, the format vLLM's NVIDIA MSA backend uses) |
| Bytes per token, all layers | 18,720 | ≈ 890 | **42,240** with an FP8 index key, 38,880 all-NVFP4 |
| **At 1,048,576 tokens** | **18.28 GiB** | **0.89 GB** | **37.97 GiB** (all-NVFP4) |

MSA's sparsity saves reads, not storage: a query attends the 16 best 128-token blocks of each KV head
(its own block included), chosen by a small indexer from a per-token index key, but any block can
be chosen later, so every block is kept (TokenSpeed: *"every layer retains full history"*). At 1M
the K/V alone would take 38 GiB beside at least 78 GiB of 12-bit experts — more than a GB10 has.

The indexer is also what makes the K/V safe to move off the device. Its keys must stay resident,
because every step scores all of them; the K/V of a block is read only after the indexer has
selected it. So this release keeps the **index keys resident** and puts the **main K/V on SSD**:
each step the runtime reads exactly the selected blocks (at most 16 per KV head per layer,
≈ 66 MB per decoded token in the worst case at NVFP4), keeps the newest block on the device,
and nothing is fetched speculatively. The memory this frees goes into expert precision rather than
a large K/V cache; decode speed comes from the DSpark draft head instead.

## Memory at the full 1,048,576 tokens

Against the 117.2 GiB a GB10 reported available to `ds4-server --check-config` for Beam-1.0 VQ:

| | GiB |
|---|---:|
| Routed experts, 57 layers × 13-bit (codes, gains, codebooks) | 78.33 |
| 8-bit residual stage on 20 layers | 16.88 |
| Attention + shared experts + dense FFN + head (Q4_K), indexer (Q8_0), router and norms | 6.46 |
| DSpark draft head (Q8_0) and its 4,096-token draft K/V ring | 2.07 |
| MSA index keys, NVFP4, 60 layers × 1M tokens | 4.22 |
| Newest K/V blocks and SSD staging | 0.50 |
| Graph workspace *(estimate from Beam's measured 1.12 GiB at 2,048 rows, scaled)* | 1.50 |
| Floor kept free by the server | 4.00 |
| **Resident at 1M** | **113.96** of 117.2 |
| On SSD per 1M session: main K/V, NVFP4 | 33.75 |
| On SSD, read on demand: token embedding (BF16) 2.29, vision tower (BF16) 1.61 | — |

The 3.2 GiB left also covers the 1.61 GiB of vision weights that are paged in while an image is
encoded. Measured on GB10: the exact 1,048,319-token run peaked at 110.7 GiB resident without the
DSpark head. Without the residual stage the same contract would leave 20.1 GiB unused; the alternative
use, a resident K/V cache of ≈ 600K tokens, only saves SSD reads, while the residual stage lowers
the expert error of 20 layers. `memory-budget.json` and `tools/memory_budget.py` reproduce every
row.

## Recipe

- **Routed experts.** Every 8 consecutive weights of an expert row become one index into the layer's
  codebook, times one F16 row gain. One codebook per layer serves all 128 experts and gate/up/down
  (YoungAi measured a shared book to cost nothing against one per expert). 13 bits everywhere: the
  12-bit code stream plus a 1-bit plane (GVQ1 v1, the format ds4-dfm-rs runs for Beam and GLM),
  whose 64 KiB E4M3 book fits GB10's 99 KiB of shared memory.
- **Residual stage (R13+8).** On 20 MoE layers a second 256-entry codebook codes what the first
  stage left (weighted Lloyd on the stage-1 residuals with the same importance weights), adding
  8 bits per 8 weights — the stage ds4-dfm-rs already runs for GLM-5.3 VQ. The 13-bit stage is
  byte-identical with and without it. It cuts a layer's weight error about threefold (relative MSE
  0.150–0.175 → 0.051–0.068; importance-weighted 0.090–0.135 → 0.031–0.045). A 14-bit book
  (128 KiB) does not fit in shared memory; a residual stage does.
- **Which layers get the residual stage — measured.** Every MoE layer was converted both ways. With
  all layers at 13 bits as the baseline, each layer alone was switched to R13+8 and the held-out set
  re-run end to end (57 forks of one teacher-forced pass); the 20 layers with the largest drop in
  assistant-turn KL were taken: 20 (−0.0132), 19, 22, 21, 18, 25, 28, 16, 24, 30, 40, 35, 43, 29,
  27, 23, 26, 53, 31, 32. They sit in the middle of the stack, where the hidden state drifts
  fastest. The rule of thumb (protect the bottom layers first, 3–22) gives KL 0.171 instead of
  0.150 on the same bytes budget.
- **Calibration-weighted Lloyd.** The original checkpoint is run over the calibration set layer by
  layer; per layer and expert the collector sums the squared activations entering gate/up and down
  and how often and how strongly each expert is routed. The codebook training, the vector
  assignment and the row-gain refit all minimize the importance-weighted error (per-column
  importance tempered by a power of 0.75, rare experts shrunk toward the layer mean with a prior of
  256 tokens, column weights floored at 2%, importance-weighted least-squares gains, 32 Lloyd
  iterations) — the weighting that measured best on A.X-K2 and halved Beam-1.0's KL.
- **Everything read on every token besides the experts** is Q4_K with the same calibration
  importance; the indexer projections that choose the attended blocks are Q8_0; the router, the
  correction bias and every norm keep their source bytes.

## Calibration data

4.18M tokens from the original checkpoint's own tokenizer and template, held-out set reserved first
(no 64-token window shared beyond template boilerplate).

| Part | Rows | Tokens | Content |
|---|---:|---:|---|
| Text and chat | 1,827 | 3,860,340 | English 38.6%, code 13.9%, Korean 13.8%, Chinese 13.6%, Japanese 7.6%, Spanish 3.9%, French/German/Indonesian/Vietnamese/Russian; raw text 38%, thinking chats 32%, non-thinking chats 21%, tool/agentic 9% (XML tool calls, SWE, ds4 agent traces); no domain above 8.5% |
| Images and video | 397 | 321,437 (193,264 visual) | 491 images (charts, math figures, documents, receipts, desktop/mobile/web screenshots, photos, Korean/Chinese Wikipedia images) and 33 videos, through the original BF16 vision tower |

60% of the text tokens are in sequences of 4,096+ tokens and 16% in 16K–32K sequences, because MSA's
block selection only engages beyond 2,048 tokens. Every routed expert of every layer receives
calibration tokens (fewest per expert per layer: thousands).

## Reference forward

The statistics and every measurement come from a layer-streamed reference forward of the original
weights. It matches transformers 5.20.2's `MiniMaxM3VLDecoderLayer` on the same dequantized
weights to BF16 rounding (relative RMS ≤ 5e-3 per layer, MSA block selection 98–99.7% identical on
a 4,096-token row). Teacher-forced on the held-out chats, the original model's NLL on assistant
turns is 1.1–1.6 nat/token.

## Measured on the converted bytes

A teacher-forced comparison with the original checkpoint over the held-out set (27 text cases and
4 image/video cases, 60,431 scored positions, 12,191 of them in assistant turns), run on 4× H100.
The release side reads every weight from this repository's files (VQ experts decoded from the
stored codes, Q4_K/Q8_0 body dequantized, BF16 embedding rows); attention runs in BF16, so the
NVFP4 K/V of the runtime contract is measured separately below. The reference forward matches
transformers 5.20.2 `MiniMaxM3VLDecoderLayer` to BF16 rounding.

| Routed experts (all with the Q4_K body) | KL, assistant turns | Same top-1, assistant turns | KL, all positions |
|---|---:|---:|---:|
| 13-bit on all 57 layers | 0.223 | — | 2.17 |
| + R13+8 on the bottom 20 MoE layers (3–22) | 0.171 | 87.2% | 1.71 |
| **+ R13+8 on the measured 20 layers (this release)** | **0.150** | **88.2%** | 1.98 |
| *Floor: the original vs itself, batched differently* | *0.003* | — | *0.565* |

**Why the assistant-turn columns.** This model is numerically chaotic on positions it was never
trained to predict — system prompts, tool schemas, user turns, raw web text after the document
token: the original run twice with different GEMM batch sizes already disagrees at KL 0.565 over
all positions (top-1 84%), and two BF16 implementations of the original that match layer by layer
to 5e-3 disagree at KL 0.23–0.62 on raw text. On assistant turns the same floor is 0.003, so those
positions measure the quantization. The original's NLL on those turns is 1.47 nat/token (they come
from other models' chats), this release's 1.39.

By kind of text (all positions, KL / same top-1): math with thinking 0.14 / 86%, Korean math
thinking 0.16 / 89%, English reasoning 0.24 / 83%, Chinese thinking chat 0.26 / 81%, Japanese
chat 0.38 / 78%, coding chat 0.51 / 81%, instruction following 0.58 / 69%; raw web text and
documents 1.1–3.0, tool-call and agent transcripts 2.5–5.1 and image/video turns 1.9–3.7 are
dominated by their untrained prompt positions.

**The KV contract on the original weights** (the same held-out set, attention with quantized
caches): NVFP4 K/V with NVFP4 index keys — the format this release's runtime keeps — costs KL
0.0205 on assistant turns; NVFP4 index keys alone 0.0002, although they change 0.84 of the 16
selected blocks per query at 8K. So the index keys can stay resident at 4 bits, and the K/V
precision, MiniMax's own serving format, is a tenth of the experts' error.

**SSD reads per decoded token** (selections recorded on held-out 8K rows and a 32K calibration
row): with only the previous step's blocks on the device a decode step fetches 11–13 MB at 8K and
29 MB at 32K (worst case 66 MB); an LRU of 64 blocks per KV head and layer (0.28 GB) brings 32K to
6 MB. A 7-token DSpark verify reads the union, 22–38 blocks per head and layer. Chunked prefill is
different: a 2,048-row chunk selects 87–100% of the visible blocks, so a long prompt re-reads most
of the prefix's K/V per chunk — see Limits.

## Kernel budget on GB10 (99 KiB shared memory per block)

| Expert stage | Codebooks | Decode gate/up | Decode down (4 experts) | Prefill MMA |
|---|---:|---:|---:|---:|
| 13-bit (37 layers) | 64 KiB | 77,824 B | 90,112 B | 96,768 B (`glmvq_mma8_kernel`, 2 stages) |
| 13 + 8 residual (20 layers) | 66 KiB | 79,872 B | 92,160 B | 98,816 B |

GB10 allows 101,376 B per block. MiniMax's top-4 routing halves the down projection's staged mid
rows against Beam's top-8 (24 KiB instead of 40), so both stages decode in one pass.

## What stays native

- **Inputs:** text, images and video through the original BF16 tower; image/video placeholders
  expanded exactly as the shipped processor does.
- **Context:** 1,048,576 tokens, partial RoPE θ = 1e7, MSA on every layer (16 blocks of 128 per KV
  head, own block always selected). No RoPE scaling.
- **Speculative decoding:** the DSpark draft head shipped with the checkpoint.
- **Chat template:** the original `chat_template.jinja`; reasoning in `<mm:think>…</mm:think>`,
  adaptive thinking, `reasoning_effort` low … max, XML tool calls.
- **Sampling:** MiniMax recommends temperature 1.0, top_p 0.95.

## Files

| Path | Contents | Size |
|---|---|---:|
| `layer-LL-experts.gguf` for the 37 13-bit layers | routed experts, one independent GGUF per MoE layer (GVQ1, format version 1) | 1,475,503,488 B (layers 3–9) / 1,475,503,872 B |
| `layer-LL-experts.gguf` for layers 16, 18–32, 35, 40, 43, 53 | the same 13-bit codes plus the 8-bit residual stage (format version 2) | 2,381,629,312 B |
| `body-nonexpert.gguf` | Q4_K / Q8_0 attention, indexer, shared experts, dense FFN, head; router, bias and norms as stored | 6,930,488,832 B |
| `embed-tokens-bf16.gguf` | BF16 token embedding, read in rows from SSD | 2,458,387,456 B |
| `vision-bf16.gguf` | vision tower, projector and merge MLP at source precision, memory-mapped | 1,734,197,248 B |
| `dspark-q8_0.gguf` | DSpark draft head | 2,177,025,024 B |
| **All 61 parts** | | **115,526,325,376 B** |
| `release.json`, `tensor-manifest.json`, `recipe.json`, `memory-budget.json`, `files.json`, `SHA256SUMS` | entry point, inventory with source mapping, recipe, budget, hashes | |
| `calibration/`, `quality/`, `conversion-receipts/`, `tools/` | calibration manifests and statistics summary, the measurements above, per-layer receipts, the tools as run | |
| `config.json`, `generation_config.json`, `tokenizer*.json`, `chat_template.jinja`, `preprocessor_config.json` | original files, unchanged | |
| [`RECIPE.md`](RECIPE.md), [`FORMAT.md`](FORMAT.md), [`SOURCE.md`](SOURCE.md) | recipe, byte format, provenance | |

These are independent GGUF parts, not numbered GGUF splits. Standard llama.cpp, Ollama and
Transformers loaders do not read this format.

## Limits

- Lossy at about 2.0 bits per routed-expert weight: on assistant turns the release agrees with the
  original's next token 88% of the time (KL 0.150); behaviour in long free generation, tool use and
  1M-token retrieval has not been measured here, and greedy decoding may loop in long reasoning.
- The fidelity numbers above are teacher-forced on H100 with BF16 attention and a reference
  forward, not on the engine: the runtime's NVFP4 K/V adds about 0.02 KL (measured on the original
  weights).
- Long prompts read K/V from SSD at prefill: a long chunk selects most of the prefix's blocks, so the
  runtime streams each layer's blocks while the previous layer computes. An exact 1,048,319-token
  prompt takes 30 minutes (580 tok/s).
- DSpark's gain depends on the text: on raw Italian prose its proposals are often rejected, and the
  runtime then decodes plainly ([above](#dgx-spark-performance)). Greedy DSpark output equals plain
  decoding.
- The custom format needs ds4-dfm-rs's `minimax_m3_vq` family ([draft PR #110](https://github.com/Baekpica/ds4-dfm-rs/pull/110), not merged yet).

## Upstream scores

From the [MiniMax-M3.1-Flash model card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash); they
describe the original weights, not this quantization: BankerToolBench 76.2, DeepSWE v1.1 73.7,
OSWorld 2.0 61.7, Agents' Last Exam 29.6, CyberGym 82.2, LOCA-Bench 256K 60.3, HLE (no tools) 43.4.

## Credits and sources

- **[MiniMax](https://huggingface.co/MiniMaxAI)** — MiniMax-M3.1-Flash, its DSpark draft head and
  vision tower, under the MiniMax Community License (`LICENSE`).
- **[YoungAi](https://github.com/fodelf/YoungAi)** by Wenzhou Wu — the 8-dim shared-codebook VQ
  method, F16 row gains and bit planes; its notice is kept in `LICENSE-YoungAi`.
- **[ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs)** — GVQ1 container, the GB10 VQ kernels and
  residual stage, the calibration-weighted VQ tools.
- **TokenSpeed, vLLM, SGLang, transformers** — the MiniMax-M3 reference implementations this
  release's reference forward was checked against.
- **[llama.cpp / GGML](https://github.com/ggml-org/llama.cpp)** — GGUF, Q4_K / Q8_0 and the
  importance-matrix idea.

## License

The weights derive from MiniMax-M3.1-Flash and remain under the **MiniMax Community License**
(`LICENSE`, copied unchanged): non-commercial use is free; commercial use requires displaying
"Built with MiniMax M3.1-Flash" and notifying MiniMax (or written authorization above 20 million
USD yearly revenue), and the license's prohibited uses apply. The quantization tools are MIT.
