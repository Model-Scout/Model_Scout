---
license: mit
base_model: XiaomiMiMo/MiMo-V2.6-Flash-RL
base_model_relation: quantized
pipeline_tag: image-text-to-text
language:
- en
- zh
- ko
tags:
- mimo_v2
- mimo
- gguf
- vector-quantization
- vq
- residual-vq
- imatrix
- importance-matrix
- calibration
- mixture-of-experts
- hybrid-attention
- sliding-window-attention
- multimodal
- vision
- video
- audio
- 1m-context
- speculative-decoding
- dflash
- mtp
- dgx-spark
- gb10
- ds4
- ds4-dfm-rs
---

# MiMo-V2.6-Flash-RL VQ GGUF

> [!WARNING]
> **Experimental low-bit release.** The routed experts, which hold most of the
> weights, are stored at about 1.6 bits per weight (2.6 on the 32 layers with an
> 8-bit residual stage), far below common 4-bit GGUF quants. You may see failures
> the source model rarely shows: reasoning that loops or never reaches an answer,
> text that breaks mid-character (shown as `�`) or switches language mid-word,
> and weaker answers in general. This is exploratory quantization research, not a
> drop-in replacement for the source model.
>
> **The files can change.** This line of conversions is still being researched, so
> any file here may be replaced by a new revision. Replacements so far: none. To
> keep a fixed build, download a pinned commit:
> `hf download Baekpica/MiMo-V2.6-Flash-RL-VQ-GGUF --revision <commit>`.
>
> **Problems or odd output?** Feel free to post them in the
> [Community tab](https://huggingface.co/Baekpica/MiMo-V2.6-Flash-RL-VQ-GGUF/discussions),
> even as rough notes. The prompt, sampling settings and runtime commit help
> most.

**Xiaomi's 309B native omnimodal MoE (15B active) with its full 1,048,576-token context, its vision/video tower, its
audio tokenizer and audio encoder, its DFlash draft model and embedded MTP heads, sized for one 128 GB DGX Spark.**
The 166 GB checkpoint (MXFP4 experts, FP8 attention) becomes **98.5 GB** of GGUF parts; with the 1M-token KV cache,
both media sidecars and the drafter loaded at once, **111.1 of the 117.2 GiB** a GB10 offers stay in use. Routed
experts are 8-dimensional vector-quantized codes — 13-bit everywhere, plus an 8-bit residual stage on 32 layers —
fitted with an importance matrix from 4.13M calibration tokens (text, chat, tools, images, video, audio) run through
the original checkpoint. **Measured against the original, teacher-forced on held-out chats: KL 0.088 and the same next
token 92.2% of the time on assistant turns** (the original against itself, batched differently: KL 0.020, 97.8%).

The predecessor, [MiMo-V2.6-Flash-RL Mixed-Quant GGUF](https://huggingface.co/Baekpica/MiMo-V2.6-Flash-RL-Mixed-Quant-GGUF),
used IQ2_XXS/IQ2_XS scalar experts. This release takes the VQ route ds4-dfm-rs runs for Beam-1.0, DeepSeek-V4.1,
GLM-5.3 and MiniMax-M3.1. A companion release applies the same recipe to the
[UNCENSORED edition](https://huggingface.co/Baekpica/MiMo-V2.6-Flash-RL-UNCENSORED-VQ-GGUF).

> **Runtime support, 2026-10-30:** runs on one DGX Spark with the ds4-dfm-rs `mimo2_vq` family
> ([PR #127](https://github.com/Baekpica/ds4-dfm-rs/pull/127)): text, images, video and audio, embedded MTP and DFlash drafting, partial
> prefix reuse and disk KV, and the native 1,048,576-token context — the default plan, with vision, audio and two
> MTP drafts, takes **109.8 of 117.6 GiB**. **Performance (2026-10-31, [PR #128](https://github.com/Baekpica/ds4-dfm-rs/pull/128)):** 2K–64K
> sweep **1,294.9 prefill / 23.96 decode tok/s** without drafting and **26.35 tok/s decode with two
> embedded MTP drafts**, the server default ([conditions below](#dgx-spark-performance)).

## At a glance

| | |
|---|---|
| Source | [`XiaomiMiMo/MiMo-V2.6-Flash-RL`](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/tree/f657ba2f7d24c9adc5730675baaa2d34de878a49) at `f657ba2f` (routed experts MXFP4, attention/dense FP8 128×128 blocks, o_proj/embeddings/head BF16) |
| Model | 48 layers: 9 global-attention (GA: 0, 5, 11, 17, 23, 29, 35, 41, 47; 64 query / 4 KV heads) and 39 sliding-window layers (window 128, 64 / 8 KV heads, learned attention sink); head dims QK 192 / V 128, partial RoPE (64 of 192 dims, θ 1e7 GA / 1e4 SWA); layer 0 dense FFN 16,384; layers 1–47: 256 routed experts, top-8, sigmoid + correction bias, no shared expert, expert FFN 2,048; vocabulary 152,576; 302.8B routed-expert weights |
| Recipe | `mimo26f-vq8-r13x47-r8x32-q8-fp8kv-embssd-v1` (`recipe.json`) |
| Routed experts | 8-dim VQ, one E4M3 codebook per layer shared by all 256 experts and gate/up/down, one F16 gain per row. **13-bit (K = 8,192) on all 47 MoE layers; an 8-bit residual stage (K = 256) on 32 layers (R13+8): 5, 8, 11, 13, 17, 19–25, 27–30, 32–47** — the 8 GA MoE layers first, the other 24 chosen by an end-to-end measurement. 1.63 bpw on 15 layers, 2.63 on 32, 2.31 on average |
| Attention qkv / o, dense FFN (layer 0), output head | Q8_0 (FP8 sources dequantized exactly first; the TP=4-interleaved fused qkv is stored as `[q \| k \| v]`) |
| Kept at source precision | router (BF16) and correction bias (F32), every RMSNorm, attention sink biases |
| Token embedding | BF16 source bytes in its own part, read in rows from SSD (one 8,192-byte row per token) |
| Vision / video tower | MiMo ViT (28 layers, 24 window + 4 global) + 2×2 merger, **Q8_0 sidecar**, resident (0.72 GiB) |
| Audio | AudioTokenizer encoder (24 layers, 20 RVQ codebooks) + audio patch encoder (6 layers) + projector, **Q8_0 sidecar**, resident (0.61 GiB); RVQ codebooks F32 |
| Speculative decoding | DFlash draft model (5 SWA-1024 layers, block 8, mask embedding) Q8_0 1.45 GiB; the three embedded MTP blocks Q8_0 0.98 GiB as the alternative drafter |
| Context | **1,048,576 tokens**, the model's own; one sequence on one DGX Spark (serial lane) |
| KV contract | GA layers: **FP8 E4M3 + F16 scale per KV-head row, resident**, 1,296 B per token and GA layer, 11.39 GiB at 1M; SWA layers: 128 + chunk − 1 rows (BF16) |
| Chat template | Original `chat_template.jinja`, unchanged (`<think>` reasoning, `enable_thinking`, XML tool calls, image/video/audio placeholders) |
| Fidelity (release bytes vs the original, assistant turns) | KL **0.088**, same top-1 **92.2%** (13-bit everywhere: 0.233 / 87.9%; [details](#measured-on-the-converted-bytes)) |
| Runtime | [ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs), family `mimo2_vq` ([PR #127](https://github.com/Baekpica/ds4-dfm-rs/pull/127)) |

## DGX Spark performance

Measured **2026-10-31** with ds4-dfm-rs `2fa8c08e` on the UNCENSORED release, which shares the runtime,
the shapes and 38 of 53 parts with this one, so its speed applies here; this release's quality is the Runpod measurement below.
One DGX Spark / GB10, CUDA 13.4.92, driver 615.71.10; operator-managed **300–2,200 MHz** range, observed busy SM
**2,177–2,190 MHz**. Three fresh `ds4-bench` processes per variant; each of 32 frontiers from 2K to 64K
adds 2,048 prompt tokens of `speed-bench/promessi_sposi.txt` and generates 128 forced greedy tokens, without
drafting and with two embedded MTP drafts; 4,096-row prefill cap; FP8 full-layer K/V. [Receipts and raw CSVs](https://github.com/Baekpica/ds4-dfm-rs/blob/d90f433546742ac367557450ba4f9d5d820385b4/docs/benchmarks/mimo2-vq-spark-64k-2026-10-31/README.md).

![MiMo-V2.6-Flash VQ prefill and decode on one DGX Spark](assets/mimo2-vq-spark-64k-throughput.png)

| Median of three run means | Prefill tok/s | Decode tok/s |
|---|---:|---:|
| No drafting, 2K–64K | **1,294.9** | **23.96** |
| No drafting, 2K–32K | 1,400.4 | 24.46 |
| **Two MTP drafts (server default), 2K–64K** | 1,292.2 | **26.35** |
| Two MTP drafts, 2K–32K | 1,398.1 | 25.48 |

| Frontier | 2K | 8K | 16K | 32K | 48K | 64K |
|---|---:|---:|---:|---:|---:|---:|
| Prefill tok/s | 1,492.2 | 1,472.3 | 1,402.8 | 1,293.4 | 1,185.8 | 1,106.1 |
| Decode tok/s, no drafting | 24.86 | 24.78 | 24.58 | 24.04 | 23.43 | 23.04 |
| Decode tok/s, two MTP drafts | 23.18 | 25.04 | 27.91 | 24.38 | 26.23 | 28.40 |

The October 30 sweep measured 1,226.5 / 23.97 without drafting (998.0 prefill at 64K) and 25.16 decode with
two MTP drafts. Since then the nine global-attention layers score prefill with E4M3 queries against the stored E4M3
keys, so the keys feed FP8 tensor cores without widening (69 → 95 TFLOPS at 64K), and the embedded MTP blocks see
the prompt and every verified row within their 128-position window instead of only their own earlier drafts
([optimization report](https://github.com/Baekpica/ds4-dfm-rs/blob/d90f433546742ac367557450ba4f9d5d820385b4/docs/mimo2-vq-optimization-2026-10-31.md)). MTP decode on this forced novel
continuation follows its draft acceptance per frontier; repetitive continuations can accept more and overstate it.

Drafting on chat prompts, one process each, 512 greedy tokens, two MTP drafts:

| Prompt | No drafting | MTP before (blocks blind) | **MTP now** | Tokens per cycle |
|---|---:|---:|---:|---:|
| Write a Rust LRU cache (105 tokens) | 24.96 | 34.26 | **35.96** | 2.67 → 2.81 |
| Comment a 156-line C file (2,365 tokens) | 25.05 | 34.00 | **36.29** | 2.72 → 2.93 |
| Explain speculative decoding, Korean (152 tokens) | 24.92 | 24.00 | **25.40** | 1.88 → 2.01 |

On the engine, the UNCENSORED release (FP8 K/V) teacher-forced against its BF16 source's final hidden states on
the held-out chats: **KL 0.0884, the same next token 91.77% of the time** on 24,785 assistant-turn targets (the
Runpod reference forward on the same bytes: 0.089 / 91.9%). After 32K- and 131K-token prompts, 1,024
teacher-forced positions move against the previous f16-query prefill (ΔNLL +0.000 / +0.003, top-token agreement
95.3% / 95.5%) no more than accepted arithmetic and K/V-format switches do (95.0–97.1%).

## Serving on one DGX Spark

```sh
# native 1,048,576 context, vision + audio, two embedded MTP drafts (serial lane)
ds4-server --cuda -m MiMo-VQ-DIR
# DFlash drafter instead of MTP
ds4-server --cuda -m MiMo-VQ-DIR --mtp MiMo-VQ-DIR/dflash-q8_0.gguf --mtp-mode on --mtp-draft 7
# two text banks with partial prefix reuse and disk KV
ds4-server --cuda -m MiMo-VQ-DIR -c 262144 --max-seqs 2 --mtp-mode off \
  --prefix-reuse partial --kv-disk-dir KV-DIR
```

| Plan (`ds4-server --check-config`) | Lane | GiB of 117.6 |
|---|---|---:|
| default: 1M, vision + audio, MTP 2 | serial | 109.79 |
| 1M with the DFlash drafter | serial | 110.27 |
| 512K, one text bank + serial media, no drafting | banks | 111.77 |
| 256K, two text banks + serial media, partial reuse | banks | 109.89 |

The vision and audio parts load with the model (no `--vision`). Images, video and audio run on the serial lane;
text banks keep their own sequences, so a bank plus the media session at 1M (123 GiB) is refused. Qualified on
GB10: two-bank append / edit / fork reuse and a restart that restored 640 of 664 tokens from disk, byte-identical
to cold replays; images, video and audio answered correctly on the default 1M server
([receipts](https://github.com/Baekpica/ds4-dfm-rs/blob/a23a26c8c8189476ef887df1a3837c456e82421e/docs/benchmarks/mimo2-vq-serving-2026-10-30/README.md)). The MTP lane continued a chat over
its live state (182 of 199 prompt tokens reused) and repeated the turn byte for byte after an unrelated prompt.

## Why this design: only 9 of 48 layers grow with the context

MiMo keeps the full history only in its 9 global-attention layers; the 39 sliding-window layers attend to the last
128 tokens. Its KV is therefore small enough to stay resident at 1M — no SSD tier is needed — once the GA cache is
stored in FP8 instead of BF16:

| GA cache format | Bytes per token, 9 GA layers | At 1,048,576 tokens |
|---|---:|---:|
| BF16 (existing `mimo2` runtime) | 23,040 | 22.50 GiB |
| **FP8 E4M3 + F16 row scale (this release's contract)** | **11,664** | **11.39 GiB** |

The FP8 cache costs nothing measurable: on the original weights it gives assistant-turn KL 0.0185, inside the
original's own batching noise (0.020). The memory saved goes into expert precision.

## Why 13 bits plus an 8-bit residual: GB10's 99 KiB

A GB10 CUDA block can use at most 101,376 bytes (99 KiB) of shared memory, and the routed-expert kernels keep the
layer's whole codebook there while they decode every selected expert:

| Recipe | Base book | Residual book | Total |
|---|---:|---:|---:|
| R12 | 32 KiB | — | 32 KiB |
| **R13** | **64 KiB** | — | **64 KiB** |
| **R13+8** | **64 KiB** | **2 KiB** | **66 KiB** |
| R13+10 | 64 KiB | 8 KiB | 72 KiB |
| R14 | 128 KiB | — | 128 KiB (does not fit) |

R13 is the widest base book that fits; the 8-bit residual stage adds only a 2 KiB book and cuts a layer's weight
error about threefold (relative MSE 0.145–0.16 → 0.049–0.060 on layers 12–47). The remaining ~33 KiB holds
activations, MMA tiles and staging. MiMo's expert geometry (hidden 4,096, expert FFN 2,048, top-8) is exactly
GLM-5.3 VQ's, whose kernels already run it:

| Expert kernel stage (shared memory per block) | R13 | R13+8 |
|---|---:|---:|
| Decode gate/up (book + 4,096-wide BF16 input row) | 73,728 B | 75,776 B |
| Decode down (book + all eight experts' 2,048-wide BF16 rows) | 98,304 B | 100,352 B |
| Prefill MMA (MiniMax/GLM tiles) | 96,768 B | 98,816 B |

GB10 allows 101,376 B; staging all eight experts for the down projection leaves 1 KiB beside the residual book
(GLM-5.3 VQ's decode-down kernel runs exactly 100,352 B), and Beam's 4+4 expert staging is the fallback.

## Memory at the full 1,048,576 tokens

Against the 117.2 GiB a GB10 reported available to `ds4-server --check-config` (Beam-1.0 VQ), with every optional
component loaded at once (actual part bytes):

| | GiB |
|---|---:|
| Routed experts, 47 layers × 13-bit (codes, gains, codebooks) | 57.47 |
| 8-bit residual stage on 32 layers | 24.01 |
| Attention qkv/o, dense FFN, head (Q8_0); router, norms, sinks | 5.35 |
| DFlash draft model (Q8_0) | 1.45 |
| Vision sidecar (Q8_0) | 0.72 |
| Audio sidecar (Q8_0) | 0.61 |
| GA KV, 9 layers × 1M tokens, FP8 | 11.39 |
| SWA rings (BF16, 4,096-row chunks) and drafter rings | 0.85 |
| Graph scratch, 4,096-row prefill chunks (`mimo2` planner) | 2.83 |
| Media workspace for the largest image (32,768 patches) | 2.38 |
| Floor kept free by the server | 4.00 |
| **Resident at 1M, everything loaded** | **111.06** of 117.2 |
| On SSD, read on demand: token embedding (BF16) | 1.16 |

6.1 GiB stay free in this worst case (1M context, the largest image and the drafter at once). 36 residual layers
would leave 3 GiB and 40 do not fit; 32 keeps a margin for the new runtime family's buffers. `memory-budget.json`
and `tools/memory_budget_mimo.py` reproduce the rows from exact byte layouts.

Measured on GB10 (2026-10-30): `ds4-server --check-config` plans **110.27 GiB** for this case (1M, the DFlash drafter,
vision, audio and the media workspace) and **109.79 GiB** for the default with two MTP drafts, of 117.6 GiB
available; the runtime's scratch is 2.17 GiB at 4,096-row chunks.

## Recipe

- **Routed experts.** Every 8 consecutive weights of an expert row become one index into the layer's codebook,
  times one F16 row gain. One codebook per layer serves all 256 experts and gate/up/down. 13 bits everywhere: the
  12-bit code stream plus a 1-bit plane (GVQ1 v1, the format ds4-dfm-rs runs for Beam, GLM and MiniMax).
- **Residual stage (R13+8).** A second 256-entry codebook codes what the first stage left (weighted Lloyd on the
  stage-1 residuals with the same importance weights), adding 8 bits per 8 weights; the 13-bit stage is
  byte-identical with and without it.
- **Which layers get the residual stage — measured.** Every MoE layer was converted both ways. With all layers at 13
  bits as the baseline (assistant-turn KL 0.233), each layer alone was switched to R13+8 and the held-out set re-run
  end to end (47 forks of one teacher-forced pass). The gains concentrate in the second half of the stack: layer 47
  (−0.0153), then 24, 22, 20, 28, 27 and GA layer 23; layers 1–16 gain nothing measurable. Six of the eight GA MoE
  layers rank in the top 22; the 8 GA layers are protected first (they carry the long context, which 2K–6K-token
  held-out rows cannot exercise), the other 24 are the best measured SWA layers. The purely measured top 32 (26 and
  31 instead of GA layers 5 and 11) gives assistant KL 0.086 vs 0.088 but all-position KL 0.543 vs 0.534 — no
  measurable difference.
- **Calibration-weighted Lloyd (importance matrix for VQ).** The original checkpoint runs over the calibration set
  layer by layer; per layer and expert the collector sums the squared activations entering gate/up and down and how
  often and how strongly each expert is routed. Codebook training, vector assignment and the row-gain refit minimize
  the importance-weighted error: per-expert column importance tempered by a power of 0.75, rare experts shrunk toward
  the layer mean with a 256-token prior, column weights floored at 2%, importance-weighted least-squares gains, 32
  Lloyd iterations — the weighting that measured best on A.X-K2 and Beam-1.0 and served MiniMax-M3.1. MiMo's first
  layers feed their experts through a few "massive activation" channels (layer 1: one hidden channel carries 38% of
  the input energy); the weighting fits those exactly (importance-weighted error 0.003) at the price of a high plain
  error (0.25), and the residual stage then buys nothing there — the sweep confirms it.
- **Everything shared by every token** (attention, dense FFN, head, MTP, DFlash) is Q8_0 (relative MSE 3e-5); the
  vision and audio sidecars are Q8_0 with their RVQ codebooks, norms, biases and sinks at source precision.
- **Dead experts.** Layer 7's experts 184 and 13 are never (0 of 33M routes) or almost never (11) chosen by the router —
  the same pair an independent 1.1M-token calibration found unobserved; the weighting gives them a trace weight.

## Calibration data

4.13M tokens from the original tokenizer and chat template; held-out sets (27 text cases, 63,337 tokens; 50 native
text/image/video/audio inputs, 21,288 tokens) reserved first.

| Part | Rows | Tokens | Content |
|---|---:|---:|---|
| Text and chat | 1,579 | 3,661,171 | English 39.0%, code 14.0%, Korean 13.9%, Chinese 13.2%, Japanese 7.4%, Spanish 3.9%, ds4 agent prompts 2.9%, French/German/Indonesian/Russian/Vietnamese; raw text 38.0%, thinking chats 33.9%, non-thinking chats 18.6%, tool/agentic 9.5%; no domain above 8.5% |
| Native media | 953 | 464,968 (418,203 media) | 486 chart/document images, 79 videos (two-frame groups, MM:SS timestamps), 309 audio clips, 79 joint video+audio clips; embeddings from the original BF16 MiMo ViT and audio tokenizer/encoder with production preprocessing |

66% of the text tokens sit in rows of 4,096+ tokens, 20.7% in 16K–32K rows and 6.5% in 32K–64K rows (longest
48,950): the sliding-window layers see 128 tokens, so long rows are what give the global-attention layers (and the
experts behind them) representative statistics. Every MoE layer's least-routed live expert received thousands of
tokens (median over layers 21,452); routes per token exactly 8.0.

## Reference forward

The statistics and all measurements come from a layer-streamed reference forward of the original weights
(`tools/mimo_ref.py`). It matches the checkpoint's own transformers code (`MiMoV2DecoderLayer`, same dequantized
weights) to BF16 rounding (layer output relative RMS 0.1–1.0%, routed expert sets identical) and, on the 50 held-out
text/image/video/audio inputs, an independent original-representation reference at mean next-token KL 0.0026 (45/50
identical argmax).

## Measured on the converted bytes

Teacher-forced comparison with the original checkpoint on the held-out set (27 text cases and 50 native inputs;
65,223 scored positions, 24,885 of them in assistant turns), on RTX PRO 6000. The student reads every routed expert
from this repository's parts (decoded by an independent reader written from `FORMAT.md`, bit-identical to the
converter's); the release row also uses the Q8_0 body and simulates the FP8 GA cache.

| Configuration | KL, assistant turns | Same top-1, assistant turns | KL, all positions | Same top-1, all |
|---|---:|---:|---:|---:|
| 13-bit on all 47 MoE layers | 0.233 | 87.9% | 0.815 | 76.7% |
| + R13+8 on the purely measured top 32 | 0.086 | 92.4% | 0.543 | 82.9% |
| + R13+8 on this release's 32 (GA first) | 0.088 | 92.2% | 0.534 | 82.7% |
| **This release: + Q8_0 body + FP8 GA K/V** | **0.088** | **92.2%** | **0.532** | **82.7%** |
| *Floor: the original vs itself, batched differently* | *0.020* | *97.8%* | *0.208* | *92.6%* |
| *FP8 GA K/V alone, original weights* | *0.0185* | *97.7%* | *0.224* | *92.3%* |

On assistant turns the original's NLL is 0.773 nat/token, this release's 0.790. All positions include untrained ones
(user turns, tool schemas, the text after an image or audio clip), where even the floor disagrees at KL 0.21. By kind
(all positions, KL / same top-1): raw web text and code 0.12 / 87%, thinking chats 0.38 / 88%, non-thinking chats
0.33 / 87%; tool/agent transcripts 2.3 / 58% and media turns 0.7–3.2 are dominated by their untrained prompt positions.

## Files

| Path | Contents | Size |
|---|---|---:|
| `layer-LL-experts.gguf` for the 15 13-bit layers (1–4, 6, 7, 9, 10, 12, 14–16, 18, 26, 31) | routed experts of one MoE layer, GVQ1 (format version 1) | 1,313,048,064 B (layers 1–9) / 1,313,048,960 B |
| `layer-LL-experts.gguf` for the 32 residual layers | the same 13-bit codes plus the 8-bit residual stage (format version 2) | 2,118,611,968 B (5, 8) / 2,118,615,040 B |
| `body-nonexpert.gguf` | Q8_0 attention, dense FFN, head; router, bias, norms and sinks at source precision | 5,740,191,360 B |
| `embed-tokens-bf16.gguf` | BF16 token embedding, read in rows from SSD | 1,249,903,744 B |
| `vision-q8_0.gguf` | MiMo ViT + merger | 776,464,384 B |
| `audio-q8_0.gguf` | audio tokenizer encoder + RVQ codebooks, audio patch encoder, projector, speech embeddings | 653,195,008 B |
| `dflash-q8_0.gguf` | DFlash draft model with its mask embedding | 1,559,875,456 B |
| `mtp-q8_0.gguf` | the three embedded MTP blocks | 1,049,622,912 B |
| **All 53 parts** | | **98,520,657,024 B** |
| `release.json`, `tensor-manifest.json`, `recipe.json`, `memory-budget.json`, `files.json`, `SHA256SUMS` | entry point, inventory with exactly-once source mapping, recipe, budget, hashes | |
| `config.json`, `generation_config.json`, `tokenizer*.json`, `vocab.json`, `merges.txt`, `chat_template.jinja`, `preprocessor_config.json`, `audio_tokenizer/config.json`, `dflash/config.json` | original files, unchanged | |
| `FORMAT.md`, tools, calibration manifests, measurements, receipts | byte format, the tools as run, calibration manifests, the measurements above, per-part receipts | |

These are independent GGUF parts, not numbered GGUF splits. Standard llama.cpp, Ollama and Transformers loaders do
not read this format.

## Limits

- Lossy at about 2.3 bits per routed-expert weight: on assistant turns the release agrees with the original's next
  token 92% of the time (KL 0.088). Long free generation, tool use, media understanding and 1M-token retrieval have
  not been measured here; greedy decoding may loop in long reasoning.
- The fidelity numbers are teacher-forced on held-out rows of up to 6K tokens with a reference forward, not on the
  engine; the GA layers' long-context behaviour is not exercised by them.
- GB10 speed and engine quality were measured on the UNCENSORED release; a full 1M-token prompt was planned
  (`--check-config`) but not run end to end. DFlash drafting lost to plain decode at 32K on raw prose (17.4 vs
  24.2 tok/s); two MTP drafts are the default. Partial reuse across edits needs text banks, which do not fit 1M
  beside the media session.

## Credits and sources

- **[Xiaomi MiMo](https://huggingface.co/XiaomiMiMo)** — MiMo-V2.6-Flash-RL, its vision and audio encoders and its
  DFlash draft model, MIT.
- **[YoungAi](https://github.com/fodelf/YoungAi)** by Wenzhou Wu — the 8-dim shared-codebook VQ method, F16 row gains and
  bit planes; its notice is kept in `LICENSE-YoungAi`.
- **[ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs)** — GVQ1 container, GB10 VQ kernels and residual stage,
  calibration-weighted VQ tools, the `mimo2` runtime this family builds on.
- **SGLang, transformers** — the MiMo-V2 reference implementations the reference forward was checked against; the
  September MiMo Mixed-Quant work for the native media calibration inputs.
- **[llama.cpp / GGML](https://github.com/ggml-org/llama.cpp)** — GGUF, Q8_0 and the importance-matrix idea.

## License

MIT, inherited from the [pinned upstream model](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/tree/f657ba2f7d24c9adc5730675baaa2d34de878a49).
Calibration datasets keep their own licenses.

The upstream model card's **Use Restrictions** apply to derivatives, including this quantization: no unlawful,
fraudulent or malicious use, no infringement of third-party rights, no harm to individuals or groups, no military
use, no malicious cyber activity, no unauthorized processing of personal data, and no autonomous execution of
high-risk actions without human oversight (see the [upstream README](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)).

## Citation

```bibtex
@misc{mimo2026v26flash,
  title={MiMo-V2.6-Flash-RL},
  author={{Xiaomi MiMo Team}},
  year={2026},
  howpublished={\url{https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL}},
}
```
