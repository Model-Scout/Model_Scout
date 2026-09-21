---
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
license: mit
language:
  - en
  - ko
pipeline_tag: text-generation
tags:
  - gguf
  - imatrix
  - moe
library_name: gguf
---

# Motif-3 GGUF (imatrix)

Two GGUF quantisations of [Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)
(314B total / 13.2B active, MoE, MIT), plus the imatrix they were built with.

Both were quantised from a BF16 GGUF converted here from the original
safetensors, using an imatrix computed over a purpose-built calibration corpus.
Quality is reported below as KL divergence against the BF16 master.

## Requires a patched llama.cpp

The `motif3` architecture is **not upstream**. As of 2026-08-14 you need three
things, and a build missing any of them will not serve these files:

1. **[PR #26298](https://github.com/ggml-org/llama.cpp/pull/26298)** — *model:
   Add support for Motif 3 Beta*. Still open.
2. **[PR #26404](https://github.com/ggml-org/llama.cpp/pull/26404)** — *CUDA: FA
   support for head size 192/128 with GQA ratios that are not multiples of 8*.
   Still open. Needed for `-fa on`, which you want: Motif-3's fused MLA latent KV
   lands on exactly such a head-size/GQA combination.
3. **`patches/motif3-runtime.patch` from this repo**, applied on top. Without it
   loading fails outright with:

   ```
   unknown pre-tokenizer type: 'motif3'
   ```

That third patch is 47 lines against `src/llama-vocab.cpp` and
`src/llama-vocab.h`, and it is the important one. PR #26298 does not register a
pre-tokenizer for Motif-3, so stock `convert_hf_to_gguf.py` silently falls back
to `pre='gpt-2'`. Motif-3's 220k vocabulary contains **multi-word tokens**, and
its real split regex wraps each word alternative in `(?: <word>)*` so that a run
of space-separated words becomes a *single* pre-token. Splitting per word makes
those entries unreachable. Holding the BPE merges fixed and swapping only that
regex, 400k characters of English prose tokenise to 82,231 tokens with the
correct pattern and 94,824 without — **+15.3 %**, paid on every prompt and every
generation. Files built the wrong way still load and still generate fluent text,
which is what makes this worth calling out: nothing announces the fault.

`patches/motif3-convert.patch` is only needed if you want to convert Motif-3
from safetensors yourself rather than use these files. It teaches
`conversion/motif3.py` to detect that split regex and emit `pre='motif3'`, and
registers `ATTN_K_B` / `ATTN_V_B` for the arch — PR #26298 emits those tensors
for the MLA split but never registers them, so conversion aborts at `blk.0`.

## Files

| directory | size | bpw | notes |
|---|---|---|---|
| `IQ4_XS/` | 161.4 GiB | 4.40 | recommended; 0.045 mean KLD against the BF16 master |
| `IQ2_XXS-custom/` | 85.8 GiB | 2.34 | runs on a single 96 GB card at 131K ctx (one MoE layer on CPU); measurably degraded |
| `imatrix/Motif-3-imatrix.gguf` | 736 MiB | — | build your own quants without repeating the calibration run |
| `patches/` | 4 KiB | — | the llama.cpp patches these files need; see above |

Each quant is a 15-shard split; point llama.cpp at the `-00001-of-00015` file.

For reference, the shape these were cut from: 53 blocks (2 dense + 51 MoE),
384 routed experts at top-8 plus 1 shared expert, native context 262,144,
sliding window 129 on a period-4 pattern.

## Quality

KL divergence against the BF16 master, 200 chunks of wikitext-2-raw test at
`-c 512` (51,000 scored tokens), identical token sequence for every rung.

| rung | size | bpw | mean KLD | PPL(Q)/PPL(base) | same top-1 | RMS Δp |
|---|---|---|---|---|---|---|
| Q4_K_M *(no imatrix, not published)* | 182.0 GiB | 4.97 | 0.04902 ± 0.00044 | 1.0315 | 91.88 % | 6.84 % |
| **IQ4_XS** | 161.4 GiB | 4.40 | **0.04519 ± 0.00044** | **1.0253** | **92.13 %** | 7.11 % |
| IQ2_XXS-custom | 85.8 GiB | 2.34 | 0.46195 ± 0.00350 | 1.5804 | 75.60 % | 24.02 % |

`Mean PPL(base) = 4.4576 ± 0.0460`; the BF16 master's own final perplexity on
the same 200 chunks is 4.4682.

**Read the first row carefully.** That Q4_K_M was the host used to compute the
imatrix, so it was necessarily built *without* one. It is in the table as a
control, not as a competitor: the fact that IQ4_XS beats it on KLD, on
perplexity ratio and on top-1 agreement while being 20.7 GiB smaller measures
**what the imatrix is worth here** — roughly 0.6 bpw.

IQ2_XXS-custom is 10× the divergence of IQ4_XS and disagrees with the master on
roughly one token in four. That is what 2.34 bpw costs on a 384-expert model.
It is offered because it is the only rung that fits a single 96 GB card at
useful context, not because it is close to lossless.

Comparisons against quants in *other* repositories are not meaningful unless
they were built from the same tokenizer — see the last section.

## Long-context behaviour

A four-hop retrieval-and-binding probe. Every document hides a chain — wing →
vault → crate count → crate weight, then divide by a lift capacity and round up
— spread across a window covering 70 % of the text, so at 52K tokens the first
and last links sit roughly 31K tokens apart. Alongside it sit **five distractor
facts** giving two other vaults their own crate counts and weights, in the same
sentence form and the same neutral register as the filler. Retrieval alone is
not enough: each number has to stay bound to the right vault across the span.
Numbers are rejection-sampled so that no mis-binding, no rounding down and no
rounding to nearest can land on the right answer by luck. Grading is exact, on a
required `FINAL: <n>` line. Both quants received byte-identical prompts, checked
per cell via `prompt_tokens`.

| quant | 3.4K | 13.1K | 52K | total | median end-to-end latency |
|---|---|---|---|---|---|
| IQ4_XS | 9/9 | 9/9 | 26/27 | **44/45** | 42 s / 101 s / 305 s |
| IQ2_XXS-custom | 9/9 | 9/9 | 25/26 | **43/44** | 14 s / 22 s / 67 s |

Latencies are whole-request wall clock — prefill plus reasoning plus answer — on
one RTX PRO 6000 (96 GB) with CPU expert offload at `-ncmoe 29` for IQ4_XS and
`-ncmoe 3` for IQ2_XXS-custom. IQ2 is the faster row mostly because almost none
of it streams over PCIe, not because 2-bit arithmetic is cheaper.

**This probe does not separate the two quants.** Each produced exactly one
failure, both at 52K, both the same failure mode, at 1-in-27 and 1-in-26. That
is a null result and it is reported as one. Anyone choosing between these files
should use the KL divergence table above, which does separate them decisively;
a probe that cannot tell them apart has not earned a vote against a measurement
that can.


## imatrix

`imatrix/Motif-3-imatrix.gguf` (736 MiB), a full pass at `-c 512` over 2,006
chunks (1,027,072 tokens) of a corpus assembled for this model: targeted 30 %
English prose, 25 % code, 20 % Korean, 15 % tool-calling traces, 10 % maths.
Korean is there at 20 % because Motif-3 is a bilingual EN/KO model, and an
English-only calibration would leave whichever experts specialise in Korean
weighted only by whatever transfers from English.

**Every one of the 58,752 expert slots has activations** (51 MoE layers × 384
routed experts × 3 tensor types); the least-visited expert saw 422 activations,
the median 19,420, and no entry is non-finite. On a 384-expert model that
coverage is what decides whether a low-bit quant is trustworthy — a partial
calibration leaves some experts quantised from nothing while still producing a
file that loads and passes a smoke test — so it was measured rather than
assumed.

```
sha256  4d8a8163b9a725ae1c6b2ec200976e514c21d66a14b5396a605696aab347a780
```

## Why IQ2_XXS-custom, and why no IQ3

The target here was an RTX PRO 6000 (Blackwell, `sm_120`). On that architecture
the `iq1_s`, `iq2_s` and `iq3_s` CUDA kernels are broken. The ftype names hide
this: **IQ2_M's base type *is* `iq2_s`, and every IQ3_\* rung routes through
`iq3_s`**. IQ2_XXS, IQ2_XS and IQ4_XS are the only safe rungs, which is why the
ladder here jumps straight from 4.40 to 2.34 bpw.

`IQ2_XXS-custom` is IQ2_XXS with the parts that a pure IQ2_XXS damages most
lifted, chosen so the result still fits 96 GB:

```
ffn_down_exps        iq2_xs   (up from iq2_xxs)
ffn_*_shexp          q4_K     (shared expert, active on every token)
blk.[01].ffn_*       q4_K     (the two dense layers)
token_embd           q2_K
output               q6_K
```

## Running it

Tested with `llama-server`. The flags that matter:

```
-ngl 999 -ncmoe <N> -fa on -ctk f16 -ctv f16 --jinja --reasoning-budget 4096
```

- **`--reasoning-budget` is mandatory.** Motif-3 always reasons; without a budget
  it can spend an entire generation in `reasoning_content` and return empty
  `content`. **The budget cannot fire if the caller's `max_tokens` is ≤ the
  budget** — the request hits `finish_reason: length` inside the reasoning block
  first and you get an empty answer. Either send no `max_tokens`, or send one
  comfortably above the budget.
- **Expect the reasoning to be long on multi-hop questions over long context.**
  In the probe above, several 4-hop calls ran past 4,096 reasoning tokens. Note
  that raising the budget is not automatically an improvement: one 52K case
  re-run at `--reasoning-budget 16384` spent 16,506 tokens deliberating and
  arrived at a *worse* answer than the same prompt at 4,096. Treat the budget as
  a cost control, not a quality dial.
- **Keep the KV cache at f16.** Quantised KV is not worth it here.
- **Do not pass `--swa-full`.** 39 of 53 layers use a short sliding window (the
  config says 128, the GGUF records 129); full attention runs only where
  `layer % 4 == 0`, i.e. 14 layers. `--swa-full` throws that saving away and the
  context cost balloons.
- `-ncmoe` counts **blocks, not MoE layers**. `blk.0` and `blk.1` are dense, so
  `-ncmoe N` moves `N-2` MoE layers to the CPU.
- No EOG override is needed; the stock template terminates correctly.

## Comparing against other Motif-3 GGUFs

Check the other repo's `tokenizer.ggml.pre` before comparing any perplexity or
KLD number against the table above. If it reads `gpt-2`, that build tokenised
the same text into a different sequence (see the pre-tokenizer note at the top),
so the two sets of numbers are not measuring the same thing and the smaller one
is not the better quant. This is not hypothetical — it is the default outcome of
converting Motif-3 without the patch.

## License

MIT, inherited from [Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3).
