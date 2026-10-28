---
license: apache-2.0
base_model: skt/A.X-K2
base_model_relation: quantized
pipeline_tag: text-generation
language:
- ko
- en
- ja
- zh
- es
tags:
- axk2
- a.x
- skt
- gguf
- vector-quantization
- vq
- imatrix
- calibration
- mixture-of-experts
- mla
- sparse-attention
- 256k-context
- reasoning
- tool-use
- dgx-spark
- gb10
- ds4
- ds4-dfm-rs
---

# A.X-K2 VQ GGUF

**SK Telecom's 688B A.X K2 with its full 262,144-token context, sized for one
128 GB DGX Spark.** The 647 GiB FP8 checkpoint becomes about **107.6 GB** of
GGUF parts: 105.3 GB (98.04 GiB) that stay resident and a 2.35 GB BF16 token
table that is read in rows from SSD. The 676.5B routed-expert weights use
YoungAi's 8-dimensional vector quantization at **9 bits per 8 weights (10 on
seven mid-stack MoE layers)** — about **1.14 bits per weight** — with
codebooks trained by a **calibration-weighted Lloyd** (an importance matrix
for VQ) collected from the FP8 original. Everything else that is read on every
token stays at Q4_K, Q8_0 or source precision.

> [!WARNING]
> **Expect severe quality loss.** This is an extremely low-bit conversion:
> the routed experts, which are 98% of every MoE layer, keep **~1.14 bits per
> weight** (1.125 index bits on 53 layers, 1.25 on 7), below any widely used
> public low-bit release. Compared with the FP8 original, this model can
> produce **garbage or repetitive text, broken Korean, wrong facts and
> arithmetic, malformed `<tool_call>` JSON, and thinking traces that never
> close.** Do not use it where correctness matters; treat it as a research and
> runtime-development artifact. Why we expected this before measuring:
>
> - **The same method at higher rates is already lossy.** Beam-1.0 VQ at 12
>   bits (1.5 BPW) has a held-out weight relative MSE of 0.170 and agrees with
>   the original's next token 82.9% of the time (Korean prose 75.1%). Each
>   index bit divides the error by about 1.19, so 10 bits extrapolate to ~0.24
>   and **9 bits to ~0.29 — 1.7 times Beam's 12-bit error**.
> - **Our GLM-5.3-Flash VQ at 12/13 bits** answered a long English context
>   with a short Korean question correctly in 0 of 5 runs (garbage output)
>   until 8-bit residuals were added to some layers (2 of 5).
> - **Below the public floor.** Unsloth's DeepSeek-R1 1.58-bit release, usable
>   but visibly lossy, keeps most experts at IQ1_S (~1.56 BPW); this release is
>   ~0.4 BPW lower, a range with almost no public precedent. llama.cpp refuses
>   to build IQ1_S/IQ1_M/IQ2_XXS/IQ2_XS/IQ2_S/IQ3_XXS without an importance
>   matrix at all — the calibration weighting used here is a prerequisite at
>   this rate, not a cure.
>
> What was measured against the FP8 original — next-token agreement, KL and
> perplexity on held-out Korean, English, code, chat and tool-call text — is
> in [Measured on the converted bytes](#measured-on-the-converted-bytes).
>
> **경고 — 심각한 품질 저하가 예상됩니다.** 라우팅 전문가 가중치를 약 1.14
> bit/weight로 낮춘 초저비트 변환입니다. FP8 원본에 비해 무의미하거나 반복되는
> 출력, 깨진 한국어, 틀린 사실·계산, 잘못된 도구 호출 JSON, 닫히지 않는 사고
> 과정이 나타날 수 있습니다. 정확성이 중요한 용도에는 쓰지 마세요.
>
> **The files can change.** This line of conversions is still being researched,
> so any file here may be replaced by a new revision. Replacements so far:
> none. To keep a fixed build, download a pinned commit:
> `hf download Baekpica/A.X-K2-VQ-GGUF --revision <commit>`.
>
> **Problems or odd output?** Feel free to post them in the
> [Community tab](https://huggingface.co/Baekpica/A.X-K2-VQ-GGUF/discussions),
> even as rough notes. The prompt, sampling settings and runtime commit help
> most.

> **Status, 2026-10-29:** [ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs)
> serves this release on one DGX Spark (GB10) with its `axk2_vq` family
> ([family guide](https://github.com/Baekpica/ds4-dfm-rs/blob/b494ba5cd4b7687e10924447a87315aab0ebfe00/docs/axk2-vq.md)).
> **Updated performance, 2K–64K: 387.4 tok/s prefill and 15.25 tok/s
> decode**, medians of three run means on optimization build `8bb463ed`
> ([PR #125](https://github.com/Baekpica/ds4-dfm-rs/pull/125), merged; [conditions and repeat
> ranges below](#dgx-spark-performance)).
>
> **Earlier qualification, 2026-10-27:** [PR #114](https://github.com/Baekpica/ds4-dfm-rs/pull/114)
> added MLA with the DSA indexer over FP8 latent and key rows, CUDA 9/10-bit
> GVQ experts, gated RMSNorm, Hermes tool calls and think spans. The full
> 262,144-token context ran in one bank: a 244,122-token prompt returned two
> codes at 15% and 85%, in order (1,494 s with 512-row chunks). Over 26,866
> held-out positions, engine NLL was within 0.1% of this card's reference
> rerun on GB10. Those quality and serving gates were not rerun for the
> performance update. The conversion (2026-10-21) remains 62 GGUF parts
> (107.6 GB), with payload hashes in `tensor-manifest.json` and all 94,172
> source tensors accounted for.

## At a glance

| | |
|---|---|
| Source | [`skt/A.X-K2`](https://huggingface.co/skt/A.X-K2/tree/d0805cfd1fc647b4078c0d9f232c80d34ee0c893) at `d0805cfd1fc647b4078c0d9f232c80d34ee0c893` (FP8 E4M3 with 128×128 block scales, 346 shards, 647 GiB) |
| Model | 61 layers (1 dense + 60 MoE), hidden 7,168, 256 routed experts + 1 shared, top-8 (8 groups, top-4 groups, sigmoid + correction bias, × 2.5), expert FFN 2,048; MLA (q LoRA 1,536, KV LoRA 512 + RoPE 64, 64 heads) with a per-element output gate fused into the query up-projection, a DSA indexer (64 heads × 128, top-2,048), gated RMSNorm (rank 16); vocabulary 163,840; 691.7B tensor parameters (card: 688B, 33B active) |
| Recipe | `axk2-vq8-r10x7-r9x53-wlloyd-q4k-q8idx-embssd-v1` (`recipe.json`) |
| Routed experts | 60 MoE layers × 256 experts × gate/up/down. 8-dim VQ, three E4M3 codebooks per layer — gate (ID 4L), up (4L+3), down (4L+2) — each shared by the layer's 256 experts, one F16 gain per row refit by weighted least squares. **Layers 16, 20, 24, 28, 32, 36, 40: 10-bit (K=1,024), the other 53: 9-bit (K=512)** — 1.25 / 1.125 index bits per weight, 1.144 BPW on average with gains and codebooks. **Codebooks trained with calibration-weighted Lloyd** (weighting `imatrix`, column power 0.75; below). |
| Calibration | 3,623 sequences, 3,915,287 tokens through the FP8 original: English, Korean, code, math, Japanese/Chinese/Spanish; raw text and A.X-K2 chat in think and non-think modes with tool calls; 34–32,768 tokens long (`calibration/`) |
| Attention (q_a, q_b = fused query + output gate, kv_a, kv_b, o), shared experts, dense FFN (layer 0), output head | Q4_K with per-column importance from calibration |
| Indexer `wq_b`, `wk` | Q8_0 |
| Kept at source precision | Router weights (BF16) and `e_score_correction_bias` (F32), indexer `weights_proj` and `k_norm`, every RMSNorm and gated-norm gate (`W_down`, `W_up`), final norm |
| Token embedding | Original BF16, in its own part, read in rows from SSD (not resident) |
| Context | **262,144 tokens**, the model's own (`max_position_embeddings`; trained to 128K, extended by the source's YaRN factor 2). Needs FP8 latent KV; see the budget below. |
| Chat template | Original `chat_template.jinja`, unchanged (`<|im_start|>` turns, `<think>` / `</think>` think and non-think modes via `enable_thinking`, Hermes-style `<tool_call>` JSON, `<tool_response>`) |
| MTP / drafter | None in this release (the source has no MTP layer) |
| zchain / GR-RB sidecars | None |
| Fidelity (reference forward, release bytes vs FP8 original) | [Measured on the converted bytes](#measured-on-the-converted-bytes) |
| Runtime | [ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs) on DGX Spark (GB10), CUDA: family `axk2_vq` ([guide](https://github.com/Baekpica/ds4-dfm-rs/blob/b494ba5cd4b7687e10924447a87315aab0ebfe00/docs/axk2-vq.md)) |

## Serving with ds4-dfm-rs

Build [ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs) with `make cuda-spark` and pass the release
directory as the model:

```sh
# one bank, the native 262,144 context
./ds4-server --cuda -m A.X-K2-VQ-GGUF --host 0.0.0.0 --port 8000

# two banks at 65,536 with disk KV
./ds4-server --cuda -m A.X-K2-VQ-GGUF -c 65536 --kv-disk-dir ./axk2-kv --kv-disk-space-mb 32768
```

- **Memory.** The device holds 98.19 GiB of weights; the 2.19 GiB embedding
  part stays on SSD and is read one row per token. Every layer keeps 770 bytes
  per token (an FP8 latent row with its BF16 rope keys, and an FP8 indexer
  key): 11.47 GiB per bank at 262,144. After loading, a 128 GB Spark has
  ~18.6 GiB free, so with the default 4 GiB floor the 262K bank runs 512-row
  prefill chunks (the engine halves rows, never the context); `--mem-floor-gb 2`
  keeps 2,048 rows. At 65,536 two banks fit.
- **Output.** Requests think unless they send `"think": false` or
  `"reasoning_effort": "none"`; reasoning streams separately, and
  `<tool_call>` JSON becomes OpenAI tool calls. SK Telecom recommends
  temperature 0.9 and top-p 0.95; pass them in the request.
- **Quality on GB10.** Against this card's reference forward rerun on the
  same bytes (22 held-out cases), the engine's teacher-forced NLL is 1.9867
  against 1.9877 over 26,866 positions, and it picks the reference's
  next token 95.9% of the time — the reference itself agrees with its own
  Runpod goldens 96.7% of the time, because the router's near-ties flip with
  any accumulation order.

## DGX Spark performance

**2026-10-29, optimization build:** measured runtime
[`8bb463ed`](https://github.com/Baekpica/ds4-dfm-rs/commit/8bb463ed51ce597f4d1eb8379092bb8e06230bd8),
from [PR #125](https://github.com/Baekpica/ds4-dfm-rs/pull/125) (merged as [`ef41bd6d`](https://github.com/Baekpica/ds4-dfm-rs/commit/ef41bd6d627b62d8d51f8616e7b755acdb61ce05)). The
[campaign](https://github.com/Baekpica/ds4-dfm-rs/blob/b494ba5cd4b7687e10924447a87315aab0ebfe00/docs/axk2-optimization-2026-10-29.md)
records three separately committed prefill and three decode improvements,
with fresh-process A/Bs and family-specific fallbacks.

Three fresh `ds4-bench` processes on one GB10: each frontier prefills
2,048 new tokens over the cached prefix, generates 128 forced greedy
tokens, then restores the prompt snapshot. Prompt: the raw Italian novel
`speed-bench/promessi_sposi.txt`. CPU 9 is fixed; CUDA 13.4.92, driver
615.71.10, 300–2,200 MHz clock policy, observed busy SM clocks
2184–2190 MHz. Loading is excluded and the first 2K point has no
extra warmup. The measured model revision is
`a0c3b02e9b45dc67ef8dd1d48eb48034c93d6607`.

![A.X-K2 VQ prefill and decode on one DGX Spark, 2K to 64K](assets/axk2-vq-spark-64k-throughput.png)

| Median of three run means | Prefill tok/s | Decode tok/s |
|---|---:|---:|
| 2K–64K | **387.4** | **15.25** |
| 2K–32K | 452.9 | 15.57 |

| Frontier | Prefill tok/s | Decode tok/s |
|---:|---:|---:|
| 2K | 602.4 | 15.95 |
| 4K | 522.4 | 15.80 |
| 8K | 495.8 | 15.81 |
| 16K | 450.2 | 15.59 |
| 32K | 378.0 | 15.22 |
| 48K | 322.2 | 14.95 |
| 64K | 282.6 | 14.71 |

The curves show per-frontier medians and the observed minimum–maximum of
three runs, not confidence intervals. Run means span 386.94–388.50
prefill and 15.02–15.29 decode tok/s. 
The remaining decode spread is unresolved despite fixed CPU affinity, similar
sampled GPU clocks and CPU performance counters, and zero memory PSI; the raw
ranges remain part of the result.
Software power-cap flags occur in 6/5/8 samples across the three runs, at 2190
MHz; no thermal-cap flag is observed. Full PSI avg10 stays 0, with at least 10.108 GiB
available. [Raw samples, per-frontier ranges, hashes and reproduction
conditions](https://github.com/Baekpica/ds4-dfm-rs/blob/b494ba5cd4b7687e10924447a87315aab0ebfe00/docs/benchmarks/axk2-vq-spark-64k-2026-10-29/README.md)
are retained. The earlier October 27 sweep remains historical; these are
new absolute rates, not a cumulative matched A/B against it.

```sh
git fetch origin refs/pull/125/head
git checkout 8bb463ed51ce597f4d1eb8379092bb8e06230bd8
make cuda-spark
python3 tools/host_memory_guard.py --max-gib 128 --high-gib 128 \
  --reserve-gib 2 --trip-gib 2 --psi-full-limit 0 --timeout 1800 -- \
  taskset -c 9 ./ds4-bench --cuda -m A.X-K2-VQ-GGUF \
  --prompt-file speed-bench/promessi_sposi.txt \
  --ctx-start 2048 --ctx-max 65536 --step-incr 2048 --gen-tokens 128 \
  --csv plain-N.csv
```

- **Decode** reads about 11.6 GB of weights per token. The final cold-8K
  Nsight trace spends about half its decode kernel time in Q4_K streams;
  the campaign improves Q8 projection, expert gate/up and gated-norm
  scheduling. There is no MTP or drafter.
- **Prefill** still falls with context because the DSA indexer scores every
  earlier causal key per row and layer. The campaign removes a BF16
  conversion and accelerates sparse-key metadata access; the
  [guide](https://github.com/Baekpica/ds4-dfm-rs/blob/b494ba5cd4b7687e10924447a87315aab0ebfe00/docs/axk2-vq.md#limits-and-next-levers)
  records the remaining measured costs.

This is text throughput qualification. The forced novel continuation can
be repetitive. Focused CUDA fixtures and bounded 8K A/Bs retain the same
arithmetic and outputs; the October 27 NLL and 262K serving gates were not
rerun. The conversion's quality warning above still applies.

## Why this size: 676.5B routed weights and a 256K context

A.X K2's routed experts alone hold 676.5B weights. At Beam's 12 bits per 8
weights they would take **118.45 GiB — more than the 118.3 GiB a GB10 reports
available**, before any attention weight or KV cache. The native context then
takes its share: MLA keeps one 576-value latent per token and layer, which in
the FP8 layout (512 E4M3 + four F32 scales + 64 BF16 RoPE values, 656 B) plus
the indexer's FP8 key (132 B) is **11.74 GiB at 262,144 tokens** across 61
layers (21.0 GiB in BF16, which no expert rate fits).

Budget for one bank at the full 262,144 tokens, against the 118.3 GiB that
`ds4-server --check-config` reported on GB10 for GLM-5.3-Flash VQ:

| | GiB |
|---|---:|
| Routed experts (7 × 10-bit + 53 × 9-bit layers, gains, codebooks) | 90.07 |
| Attention, Q4_K (61 layers) | 4.64 |
| Indexer, Q8_0 + BF16 | 0.87 |
| Shared experts, Q4_K | 1.38 |
| Dense FFN (layer 0) + output head, Q4_K | 0.82 |
| Router (BF16, as in the source), correction biases, norms | 0.26 |
| **Resident weights** | **98.04** |
| MLA latent KV, FP8, 61 layers × 262,144 | 9.77 |
| Indexer keys, FP8, 61 layers × 262,144 | 1.97 |
| Scratch *(estimate: Beam's 2.4 GiB scaled to hidden 7,168 and the MLA/indexer workspaces)* | 3.00 |
| Floor kept free by the server | 4.00 |
| **Quote at 256K** | **116.78** of 118.3 |

That leaves 1.5 GiB of spare quote at the full context. The seven 10-bit
layers are what the budget allows: each costs 0.164 GiB. Shorter contexts
would buy more 10-bit layers:

| Context | FP8 KV (GiB) | Routed-expert layout | Routed-expert BPW |
|---|---:|---|---:|
| 131,072 (no YaRN) | 5.87 | 42 × 10-bit + 18 × 9-bit | 1.217 |
| 196,608 | 8.80 | 25 × 10-bit + 35 × 9-bit | 1.181 |
| **262,144 (native, this release)** | **11.74** | **7 × 10-bit + 53 × 9-bit** | **1.144** |
| 524,288 (YaRN × 4) | 23.47 | does not fit even at 9 bits everywhere (96.9 > 86.3) | — |

`memory-budget.json` and `tools/memory_budget.py` reproduce every row.

## Recipe

- **Routed experts.** Every 8 consecutive weights of an expert row (along
  the input axis) become one index into a codebook, times one F16 row gain
  (the row RMS, computed in FP64 and rounded before normalizing, then refit
  by importance-weighted least squares after assignment). The layer's
  codebooks (`split3` (separate gate (4L), up (4L+3) and down (4L+2) books per layer)) serve all 256 experts. The FP8 source is
  dequantized exactly as the checkpoint defines it (`fp8 × weight_scale_inv`
  per 128×128 block, in FP32; bit-identical to llama.cpp's converter) before
  anything else.
- **Calibration-weighted Lloyd (an importance matrix for VQ).** The YoungAi
  method and our earlier VQ releases trained codebooks on the weights alone,
  minimizing the plain squared error of normalized vectors. At ~1.1 BPW that
  wastes bits on inputs that carry little signal. Here the FP8 original is run
  layer by layer over a calibration set, and per layer and expert we record
  how many tokens each expert receives, its routing weights, and the squared
  activations feeding gate/up (7,168 columns) and down (2,048 columns). The
  Lloyd assignment then uses an importance-weighted distance
  Σ_d h_d (v_d − c_d)² and the centroids become importance-weighted means —
  the diagonal approximation llama.cpp's imatrix uses for its 1–2-bit types,
  extended to a codebook shared by 256 experts, where how often an expert is
  routed decides how much it pulls the shared centroids. Rare experts are
  shrunk toward a prior (a pseudo-count of 256 routed tokens), column profiles
  are tempered and floored at 0.02 × their mean so no dimension is left free.
- **What the weighting buys, per layer.** Five weightings were compared on
  53,142 held-out tokens, as the relative error of each MoE layer's routed
  output (original vs restored weights): row energy alone (YoungAi's untested
  candidate) moves it by −0.6%; column importance from the calibration cuts it
  by 16–18% on average with one shared book and by about 21–22% with LS gain
  refit and split books — most at the bottom and top of the stack (layer 1
  −36…−63%, layer 60 −35…−81%), least in the middle (layers 24–55, −1…−11%).
  Selected: `imatrix` column importance, `split3` books, column power 0.75, LS gain refit. Tables: [RECIPE.md](RECIPE.md).
- **Calibration set.** YoungAi measured a *domain tax* when a narrow corpus
  shaped the main weights, so the 3.92M calibration tokens mix English (55%,
  math and reasoning included), Korean (21%), code (13%), DS4 agent prompts
  (5%) and Japanese/Chinese/Spanish (2% each), raw text (40%) and A.X-K2 chat
  in think and non-think modes with tool calls,
  from short turns to 32K-token documents
  ([CALIBRATION.md](calibration/CALIBRATION.md)); the held-out set never
  overlaps it.
- **Which layers get 10 bits — measured, not bottom-first.** Each extra index
  bit divides the weight error by about 1.19, and the 256K budget leaves room
  for seven 10-bit layers. This card first announced them on the bottom MoE
  layers 1–7, following YoungAi's shallow-first measurement and the GLM-5.3
  end-to-end sweep — both made with unweighted codebooks. Measured end to end
  instead (teacher-forced KL against the FP8 original on the 53,142-token
  held-out set, selected experts, FP8 non-experts): layers 1–7 0.788, 15–21
  0.774, spread over 16, 20, …, 40 **0.756**; on the release bytes 0.784 vs
  **0.754**. Under calibration weighting the bottom layers are already
  accurate (layer 1's routed-output error 0.12) while the hidden state drifts
  fastest in layers 15–45 (cosine to the original 0.988 at layer 15, 0.669 at
  41), so the release puts 10 bits on layers **16, 20, 24, 28, 32, 36 and 40**
  — the same bytes as 1–7.
- **Everything read on every token besides the routed experts** is Q4_K (the
  GGML encoder given the calibration's per-column importance), except the
  indexer's two projections, which select the attended keys and are Q8_0.
- **Not touched:** router weights and correction biases, the indexer's
  per-head weighting projection and key norm, every norm and gated-norm gate,
  and the token embedding (BF16, read from SSD).

### Index layout (GVQ v2)

The GVQ1 container of the earlier releases stores 12-bit index streams (with
a 1-bit plane for 13 bits). Nine and ten bits use a byte-major version 2: one
byte per index holds the low 8 bits, and a separate plane holds the high bit
(9-bit) or two bits (10-bit), least significant first. A gate/up row is 896
index bytes plus a 112- or 224-byte plane, a down row 256 plus 32 or 64.
Codebooks are 4 KiB (K=512) and 8 KiB (K=1,024) of E4M3, so a GB10 kernel
keeps a whole layer's book in shared memory with most of the 99 KiB block
left for staging.

## Measured on the converted bytes

Teacher: the FP8 checkpoint, dequantized exactly and run by a layer-streamed
BF16 reference (`tools/axk2_ref.py`; matches transformers' `AXK2DecoderLayer`
to BF16 rounding on the same weights, except the router mask — see the router
section). Release: these exact bytes, restored by an independent GGUF/GVQ
decoder. Teacher-forced; KL(teacher ‖ release) in nats per token; top-1 = the
same next-token argmax. Measured on Runpod (RTX PRO 6000 Blackwell, sm_120,
CUDA 13.2, torch 2.13); another GPU, CUDA build or kernel set will not
reproduce the digits exactly, and should not be expected to.

**This release on two held-out sets** (neither used for calibration; set 2 was
built after every choice below and used for none of them):

| Held-out | Cases / tokens | KL | Top-1 | PPL original → release |
|---|---:|---:|---:|---:|
| 1 (wikitext-2, 5-language web, chat in both modes, math, code, tools, SWE, finance, 8K documents) | 22 / 53,142 | 0.754 | 71.6% | 3.10 → 5.42 |
| 2 (independent, 19 domains, 793–11,117-token cases; build `9735a562`, `quality/heldout2_manifest.json`) | 78 / 188,578 | 0.727 | 71.7% | 3.38 → 5.73 |

Per domain on set 2 (KL / top-1): math with thinking 0.180 / 85.9%,
English reasoning with thinking 0.323 / 78.2%, Korean thinking 0.323 / 79.9%,
Korean chat 0.296 / 84.1%, competitive programming 0.330 / 80.1%, Python
0.435 / 81.6%, C 0.490 / 80.8%, tool-call chats 0.700 / 80.9%, instruction
following 0.791 / 72.7%, SWE 0.769–1.059 / 67–73%, English web 0.855–0.914 /
63%, wikitext-2 1.053 / 63.1%, Korean web 0.697–1.393 / 56–62%, Japanese web
1.246 / 53.5%, Spanish web 1.389 / 56.9%, Chinese web 1.955 / 43.5%. Chat and
reasoning hold up far better than raw web prose.

The residual stream drifts with depth (cosine with the original at the FFN
input: layer 15 0.987, 21 0.919, 30 0.825, 41 0.683, 60 0.637; top-8 expert
overlap 0.86 → 0.59), so the experts' 9-bit error, not the Q4_K body, decides
the result: the body alone (original experts) costs KL 0.046, top-1 93.7%.

**What the calibration weighting buys** (held-out 1, routed experts converted,
everything else at FP8, 10-bit on layers 1–7):

| Codebook training | KL | Top-1 | PPL |
|---|---:|---:|---:|
| Unweighted Lloyd (earlier GVQ releases) | 0.859 | 69.5% | 6.00 |
| Row energy g² + least-squares gains (data-free) | 0.858 | 69.4% | 5.99 |
| Per-expert column importance, power 0.75, weighted LS gains, gate/up/down books (**selected**) | **0.788** | **71.0%** | **5.59** |
| Importance × routing frequency, same | 0.791 | 70.6% | 5.61 |
| Output-space importance (gate/up through SwiGLU), same | 0.799 | 70.7% | 5.66 |

Per layer on the held-out tokens' own FFN inputs the selected weighting cuts the
routed-output error by 24% on average (layer 1: 0.284 → 0.120; layer 60:
0.652 → 0.209; middle layers 2–10%). Against the unweighted conversion it
improves 16 of 18 held-out-1 domains (finance −29% KL, Japanese −19%, Korean
math −17%, Korean web −10%, code −6 to −9%).

**Where the seven 10-bit layers go** (same bytes):

| 10-bit MoE layers | Set 1 KL (experts only) | Set 1 KL (release bytes) | Set 2 KL (release bytes) | Set 2 top-1 |
|---|---:|---:|---:|---:|
| 1–7 (announced, bottom first) | 0.788 | 0.784 | 0.753 | 71.1% |
| 15–21 | 0.774 | — | — | — |
| **16, 20, 24, 28, 32, 36, 40 (this release)** | **0.756** | **0.754** | **0.727** | **71.7%** |

On the independent set 2 the chosen placement is better in all 19 domains and in
73 of 78 cases (wikitext-2 −2.3% KL).

**Generation** (32 chats, greedy, up to 512 / 768 new tokens; Korean, English,
Japanese, Chinese, thinking and non-thinking, code, math, tool calls; same
prompts for both placements, on the same Runpod host):

| | Bottom 1–7 | This release |
|---|---:|---:|
| Ends with `<\|im_end\|>` | 78% | 69% |
| Thinking closed (11 prompts) | 82% | 82% |
| Repeated 4-grams | 0.093 | 0.096 |
| Hangul share of Korean answers | 62% | 71% |
| Every tool call valid JSON with a known name (4 prompts) | 2 / 4 | 4 / 4 |

Greedy decoding is where the damage shows: some long thinking traces loop and
do not close within 768 tokens, and sub-word glitches appear in Korean. With
the recommended sampling (temperature 0.9, top-p 0.95) 93% of the Korean prompts
ended normally and repetition fell to 0.090. Both placements answered the
"long English context, short Korean question" probe that our GLM-5.3 VQ failed
in 0 of 5 runs. 32 prompts cannot separate the two placements; the
teacher-forced numbers above can. Full outputs: `quality/generation/`.

Files: `quality/` holds every results file behind these tables (both held-out
sets, all weightings and placements, the per-layer measurements in
`quality/layer-measure/`, the non-expert-only run, the router A/B and the
generation comparison).

## What stays native

- **Context:** 262,144 tokens with the source's YaRN (factor 2, θ = 10⁶,
  original 131,072); the attention softmax scale is 1/√192 × (1 + 0.1 ln 2)².
- **Sparse attention:** the DSA indexer's top-2,048 keys per query, as in the
  source.
- **Router:** experts outside the 4 selected groups are masked to **−inf**
  before the top-8, as in Megatron, vLLM and llama.cpp. transformers'
  `AXK2TopkRouter` fills them with 0.0, which is wrong for this checkpoint:
  its biased scores (`sigmoid + e_score_correction_bias`) are negative for
  every token in layers 24, 41 and 48 and for some tokens in 34–37, 42, 49,
  51, 52, 56, 57 and 60, so a 0.0 fill routes to unselected groups. On the FP8
  original itself the held-out NLL is 1.1301 (PPL 3.10) with −inf and 1.3475
  (PPL 3.85) with the 0.0 fill. The calibration statistics and every
  measurement here use −inf; a runtime must too.
- **Chat template:** the original `chat_template.jinja`; `enable_thinking`
  selects think (`<think>`) or non-think (`</think>`) mode; tools are declared
  in the system turn and called with `<tool_call>{"name": …, "arguments": …}</tool_call>`.
- **Sampling:** SK Telecom recommends temperature 0.9 and top-p 0.95
  (`generation_config.json`).

## Files


| Path | Contents |
|---|---|
| `layer-16-experts.gguf`, `layer-20-…`, `-24-`, `-28-`, `-32-`, `-36-`, `layer-40-experts.gguf` | 10-bit routed experts, one independent GGUF per layer (1.77 GB each) |
| the other 53 of `layer-01-experts.gguf` … `layer-60-experts.gguf` | 9-bit routed experts (1.59 GB each) |
| `body-nonexpert.gguf` | Q4_K / Q8_0 attention, indexer, shared experts, dense FFN, head; source router, biases and norms (8,559,688,960 B) |
| `embed-tokens-bf16.gguf` | BF16 token embedding, read in rows from SSD (2,348,810,880 B) |
| **All 62 parts** | **107.6 GB**; exact sizes and SHA-256 in `release.json` |
| `release.json`, `tensor-manifest.json` | Entry point (every part with role, size and SHA-256) and every stored tensor with its source mapping |
| `recipe.json`, `memory-budget.json` | Machine-readable recipe and the budget above |
| `calibration/` | Calibration and held-out manifests (every sequence's source, language, format, length), `CALIBRATION.md`, statistics summary |
| `weight-error-by-layer.json`, `conversion-receipts/` | Per-layer and per-matrix conversion records (sizes, hashes, weight-space and importance-weighted errors) |
| `tools/` | The converter, calibration collector, reference forward and release scripts as run |
| [`RECIPE.md`](RECIPE.md), [`FORMAT.md`](FORMAT.md), [`SOURCE.md`](SOURCE.md) | Recipe and measurements, byte format, provenance |
| `SHA256SUMS`, `files.json` | Hashes of every file |
| `config.json`, `generation_config.json`, `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `chat_template.jinja` | Original files, unchanged |

These are independent GGUF parts, not numbered GGUF splits: do not
concatenate them. Standard llama.cpp, Ollama and Transformers loaders do not
read this format.

## Upstream scores

SK Telecom's thinking-mode scores for the original FP8 checkpoint, from the
[A.X K2 model card](https://huggingface.co/skt/A.X-K2). They describe the
source model, **not this quantization**, which will score lower.

| Benchmark | A.X K2 |
|---|---:|
| AIME26 | 97.1 |
| KMMLU-Pro | 80.5 |
| CLIcK | 91.6 |
| KoBALT | 73.0 |
| LiveCodeBench v6 | 84.0 |
| GPQA Diamond | 85.6 |
| IFBench | 75.9 |
| τ²-Bench (Telecom) | 98.0 |
| RULER 128K / 256K | 92.7 / 86.6 |

## Limits

- Severe loss (see the warning at the top and
  [Measured](#measured-on-the-converted-bytes)); behaviour in long free
  generation and tool use has not been benchmarked here.
- Anyone re-running the source through transformers must replace its
  router's 0.0 group fill with −inf (above), or the reference itself is wrong.
- ds4-dfm-rs serves one 262K bank at 512-row prefill chunks with the default
  floor (2,048 with `--mem-floor-gb 2`); banks, partial prefix reuse, disk KV
  and session snapshots work but are not yet release-qualified, and decode is
  plain (~15 tok/s).
- Calibration weighting changes which errors the codebook keeps small; it
  cannot add the information that ~1.1 bits per weight drop.

## Credits and sources

- **[SK Telecom A.X team](https://huggingface.co/skt)** — A.X K2, Apache-2.0
  ([technical report](https://arxiv.org/abs/2608.30181)).
- **[YoungAi](https://github.com/fodelf/YoungAi)** by Wenzhou Wu (吴文周,
  [fodelf](https://github.com/fodelf) /
  [wenzhouwu](https://huggingface.co/wenzhouwu)), MIT — the method: 8-dim VQ
  with per-layer shared E4M3 codebooks, F16 row gains, bit planes for extra
  index bits and spending spare bytes one index bit at a time
  ([`docs/TECHNICAL.md` §4.1](https://github.com/fodelf/YoungAi/blob/7fb26cc332d740416792204a29c7d13d2986caf5/docs/TECHNICAL.md),
  [`docs/113.md`](https://github.com/fodelf/YoungAi/blob/7fb26cc332d740416792204a29c7d13d2986caf5/docs/113.md)).
- **[ds4-dfm-rs](https://github.com/Baekpica/ds4-dfm-rs)** — the GVQ1
  container, its GB10 kernels, and the Beam / Ling-3.1 / GLM-5.3 VQ tools this
  converter is forked from.
- **[llama.cpp / GGML](https://github.com/ggml-org/llama.cpp)** — the GGUF
  container, the Q4_K / Q8_0 layouts and the importance-matrix idea this
  release carries over to vector quantization.

Part of the [DS4-VQ-for-DGX-Spark](https://huggingface.co/collections/Baekpica/ds4-vq-for-dgx-spark-6ad0765e802b9dda8054a568)
collection.

## License

Apache-2.0, as the source model. The quantization tools derive from YoungAi
and ds4.c (MIT, `LICENSE-YoungAi`, which includes the GGML notice).
