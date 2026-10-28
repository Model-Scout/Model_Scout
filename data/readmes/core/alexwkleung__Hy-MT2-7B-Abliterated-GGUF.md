---
license: apache-2.0
base_model:
  - mlx-community/Hy-MT2-7B-Abliterated-bf16
base_model_relation: quantized
pipeline_tag: translation
library_name: gguf
language:
  - zh
  - en
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - tl
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
tags:
  - gguf
  - llama.cpp
  - translation
  - abliterated
  - hy-mt2
  - hunyuan
---

# Hy-MT2-7B-Abliterated — GGUF

GGUF conversions of [`mlx-community/Hy-MT2-7B-Abliterated-bf16`](https://huggingface.co/mlx-community/Hy-MT2-7B-Abliterated-bf16),
an abliterated build of Tencent's [`Hy-MT2-7B`](https://huggingface.co/tencent/Hy-MT2-7B) translation model.

## What this is — and what it is not

**No abliteration was performed here — this repo is a format conversion only.** The chain is:

| step          | who                                                                                                         | what                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| base model    | [tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B)                                               | Hy-MT2 7B dense translation model, 33 languages                                                          |
| abliteration  | [mlx-community/Hy-MT2-7B-Abliterated-bf16](https://huggingface.co/mlx-community/Hy-MT2-7B-Abliterated-bf16) | refusal-direction ablation via [jim-plus/llm-abliteration](https://github.com/jim-plus/llm-abliteration) |
| **this repo** | [alexwkleung/Hy-MT2-7B-Abliterated-GGUF](https://huggingface.co/alexwkleung/Hy-MT2-7B-Abliterated-GGUF)     | bf16 → GGUF conversion + quantization                                                                    |

All credit for the abliteration itself goes to mlx-community and to the `llm-abliteration` author.

## Why this exists

The abliteration existed only in MLX format, which means Apple Silicon and `mlx_lm` only. Every
abliterated Hy-MT2 GGUF published so far is the **1.8B**; every abliterated **7B** was MLX-only.

## Intended use and limitations

> **Modification notice** (Apache-2.0 §4(b)). These files are quantized GGUF conversions of an
> abliterated derivative of `tencent/Hy-MT2-7B` — the refusal-direction ablation was performed by
> [mlx-community](https://huggingface.co/mlx-community/Hy-MT2-7B-Abliterated-bf16), the format
> conversion here. **Neither Tencent nor the ablation author produced, endorsed, or reviewed this
> repo**, and its behavior is not theirs.

**What this is for.** Translating source text the stock model declines to render — quoted speech,
court and police material, extremist or abusive content being studied, medical and forensic
documents, fiction. If stock translates your input, use stock; see
[Honest notes on behavior](#honest-notes-on-behavior) for why that is the default rather than a
formality.

**Ablation does not improve translation.** It removes a refusal direction from the residual stream;
it teaches the model no vocabulary, no idiom, and no language it did not already have. The only
thing that changes is willingness. Every reason to prefer the stock model on quality grounds still
applies.

**The hazard specific to a translation model: bad output is invisible to the person most likely to
rely on it.** A chat model that degrades starts saying things you can tell are wrong. A translation
model that degrades produces fluent, confident target text that only a reader of the *source*
language can catch — and if you could read the source, you would not need the translation. Ablation
damage here shows up as faithfulness loss, and **no BLEU/COMET/NLL evaluation has been run on these
files**, so that risk is unmeasured rather than ruled out. Do not use this for anything consequential
— legal, medical, immigration, safety — without a competent human checking the output against the
source.

**It will translate anything, including material you should think about first.** Faithfully
rendering harmful source text is the entire point of removing the refusals, and it puts the
judgement back on you: what you translate, what you do with it, and who you hand it to are your
responsibility, under Apache-2.0 and applicable law.

**Out of scope.** A research artifact, not a product: no safety evaluation, no red-team pass, no
translation-quality benchmark. Abliteration is imprecise by nature — the refusal direction is
diffuse, so some refusals survive it.

## Files

| file                                | size     | BPW  | notes                                                  |
| ----------------------------------- | -------- | ---- | ------------------------------------------------------ |
| `HY-MT2-7B-Abliterated-Q4_K_M.gguf` | 4.31 GiB | 4.92 | **recommended** — smoke-tested, ~1.7× faster than Q8_0 |
| `HY-MT2-7B-Abliterated-Q5_K_M.gguf` | 5.00 GiB | 5.72 |                                                        |
| `HY-MT2-7B-Abliterated-Q6_K.gguf`   | 5.74 GiB | 6.56 |                                                        |
| `HY-MT2-7B-Abliterated-Q8_0.gguf`   | 7.43 GiB | 8.50 | near-lossless                                          |

All four were quantized **from the bf16 source**, not requantized from a lower-precision file. No
imatrix was used or needed — none of these types require one (k-quants at these bit widths use
deterministic round-to-nearest).

The bf16 GGUF is not published here; regenerate it from the upstream MLX repo if you want it (see
[Reproducing](#reproducing)).

## Usage

```bash
llama-server -m HY-MT2-7B-Abliterated-Q4_K_M.gguf \
  -ngl 99 -c 4096 -fa on --jinja \
  --temp 0.7 --top-p 0.6 --top-k 20 --repeat-penalty 1.05
```

Sampling above is Hy-MT2's official recommendation. **Always wrap the input in the instruction
format** — it is not cosmetic. Measured, it is the difference between a 100% refusal rate and a 0%
one on identical content (see [What the ablation actually buys](#what-the-ablation-actually-buys-measured)):

```
Translate the following segment into English, without additional explanation.

<your text>
```

Sending the bare text instead is what produces refusals — from the stock model, and sometimes from
this one too.

Native context is 262144. `max_tokens` ~4096 per request is the model card's guidance.

## Provenance and verification

Format conversions are easy to get subtly wrong, so this one was checked rather than assumed:

- **Tokenizer is bit-identical to the reference GGUF.** `tokenizer.ggml.tokens` (128167),
  `merges` (264306), and `token_type` all hash identically to
  the official [`tencent/Hy-MT2-7B-GGUF`](https://huggingface.co/tencent/Hy-MT2-7B-GGUF)'s Q8_0. This
  matters because the MLX repo ships a stripped `tokenizer_config.json`; the vocab survived intact.
- **The quantizer reproduces the reference exactly.** Comparing this Q8_0 against Tencent's Q8_0
  tensor-by-tensor (sha256), **14 of 32 layers are byte-identical**. Those are the layers the
  ablation did not touch — so the pipeline here produces the same bytes as the reference build, and
  every remaining difference is the ablation itself rather than a conversion artifact.
- **Metadata differences are cosmetic only.** All `hunyuan-dense.*` hyperparameters, the NTK-derived
  rope frequency base, context length, special-token IDs, and the chat template match the reference.
- **The build is reproducible.** Downloading the source again and re-running the whole pipeline
  produced a Q8_0 with an identical sha256.

### What the ablation changed

Per-tensor sha256 against the unmodified model:

|                                                                                   | modified    |
| --------------------------------------------------------------------------------- | ----------- |
| layers 14–31 — all of `q/k/v/o/gate/up/down`                                      | 126 tensors |
| `token_embd`                                                                      | 1           |
| layers 0–13                                                                       | 0           |
| **all norm tensors** (`attn_norm`, `ffn_norm`, `q_norm`, `k_norm`, `output_norm`) | **0**       |

Contiguous back half, norms untouched — the expected shape for refusal-direction ablation.

## Honest notes on behavior

### What the ablation actually buys (measured)

**What this build actually buys is robustness to prompt FORM.** The stock model's willingness to
translate identical content swings from 100% to 0% depending purely on how the request is framed;
this build barely notices. Measured 2026-08-12, Q8_0 both sides, byte-identical sampling (temp 0.7 /
top-p 0.6 / top-k 20 / repeat-penalty 1.05), 6 samples per cell, explicit adult-register phrases
EN→ZH:

| prompt form | stock refuses | abliterated refuses |
| --- | --- | --- |
| instruction in the **system prompt**, user message bare | **0/12** | 0/12 |
| `Translate the following segment into Chinese…` + text | **0/18** | 0/18 |
| `Translate to Chinese: <text>` | **6/12** | 0/12 |
| bare text, no instruction at all | **30/30** | **7/30** |

Read that table before deciding you need this model:

- **Stock is not unwilling to translate this content — it is unwilling to translate it *unasked*.**
  Given any clear instruction, it complies with everything; given bare text, it refuses everything.
- **The casual form is the trap.** `Translate to Chinese: …` refused 6/12, splitting by probe rather
  than by chance — so a "natural" short instruction is *not* a reliable escape.
- **If you control the prompt, you do not need this model.** Put the instruction in the system
  prompt: one setting, zero refusals on stock, no faithfulness cost.
- **If you don't control it, this is what these weights are for.** A UI that sends bare text, an app
  whose template you can't edit — stock refuses 30/30 there, this build 7/30 (~77% removed; some of
  the 7 are deflections into a sanitised different task rather than outright refusals, so read it as
  "didn't translate", not "said no").

**And there is a legitimate third case: preferring not to think about it.** If you would rather run
one model that rarely interrupts you — whatever the prompt, whatever the input — than tune prompts
around a refusal surface you can't see, that is a reasonable trade. You are paying for it with
translation quality you cannot easily verify: no BLEU/COMET/NLL evaluation has been run here, so
faithfulness loss is *unmeasured rather than ruled out*, and on an MT model that loss is invisible to
anyone who can't read the source. The 8/10 byte-identical benign passages and 0/36 age-coded
mistranslations below are reassuring at small n, not a quality guarantee. Knowing that, it's a fair
choice to make — just make it deliberately rather than by default.

Two earlier attempts to measure this found nothing, because they probed the wrong regime: standard
harmful-instruction benchmarks (`mlabonne/harmful_behaviors`) were translated by **stock** 20/20,
both as instructions and as source text. A refusal probe the base model does not refuse measures
nothing.

**Faithfulness spot-check, same run:** 8/10 benign passages byte-identical to stock at fixed seed;
the 2 that differed were equivalent renderings (不复存在/不存在, 阳光直射下/阳光直射的情况下). A
separate 36-sample check for age-coded mistranslation (an adult-subject source rendered with
school-age vocabulary) found **0 occurrences**.

**Stock's alignment can also show up as silent rewriting rather than refusal.** In the wrapped
regime, 2 of 20 harmful-instruction strings came back with the meaning inverted — "a how-to article
on **trafficking** endangered species" became 打击 ("**combating**" trafficking), and "encourages
readers to **engage in** eating disorders" became 正视 ("**confront**" them). The abliterated build
reproduced both inversions identically, so ablation does not fix this. It is the sharpest example of
the hazard described above: fluent, confident output that says the opposite of the source.

### General guidance

**Treat this as an escape hatch, not an upgrade.** On inputs the stock model already handles, the
two are largely indistinguishable — in a 5-prompt A/B at fixed seed and identical sampling, 4 of 5
outputs were byte-identical to the unablated model.

**For general translation quality, prefer the unablated model.** This mirrors the guidance huihui-ai
publish on their own abliterations of earlier Hunyuan-MT models:

> If it's only for translation, use the original model without ablation. If it involves translation
> and other conversations, the ablated model can be used.

Above is stated verbatim in
[Huihui-HY-MT1.5-7B-abliterated](https://huggingface.co/huihui-ai/Huihui-HY-MT1.5-7B-abliterated),
[Huihui-HY-MT1.5-1.8B-abliterated](https://huggingface.co/huihui-ai/Huihui-HY-MT1.5-1.8B-abliterated),
and [Huihui-Hunyuan-MT-Chimera-7B-abliterated](https://huggingface.co/huihui-ai/Huihui-Hunyuan-MT-Chimera-7B-abliterated).
Note those cover **HY-MT1.5 and Hunyuan-MT-Chimera, not Hy-MT2** — huihui-ai have not published a
Hy-MT2 ablation, so treat it as an analogous finding on a prior model generation rather than
guidance about these files.

Ablation damage on a translation model shows up as faithfulness loss, which is considerably harder
to notice than a chat model degrading. No systematic quality evaluation (BLEU/COMET/NLL) has been
run on these files, so that risk is unmeasured rather than ruled out.

**Q4_K_M was smoke-tested** on the same battery and matched Q8_0 on 4 of 5 prompts, with the fifth
differing only in word choice (both correct).

Abliteration does not guarantee removal of all refusals — the refusal direction is diffuse.

## Reproducing

```bash
hf download mlx-community/Hy-MT2-7B-Abliterated-bf16 --local-dir ./src

# convert_hf_to_gguf.py comes from the llama.cpp source tree, matched to your llama.cpp build
python3 convert_hf_to_gguf.py ./src --outfile bf16.gguf --outtype bf16
llama-quantize bf16.gguf HY-MT2-7B-Abliterated-Q4_K_M.gguf Q4_K_M 8
```

The MLX repo uses stock HF tensor names and a standard `config.json`, so it feeds
`convert_hf_to_gguf.py` directly with no preprocessing.

## Verifying the build

These hashes are **not** for checking your download — the Hub already does that (every file's
git-LFS pointer is a sha256, and `hf download` verifies it automatically). They are here so you can
check the _build_ instead.

Because the pipeline above is deterministic, you can run the [Reproducing](#reproducing) steps
yourself against the same upstream source and confirm you land on exactly these bytes — i.e. that
these files really are that source put through that recipe, with nothing else done to them. That is
a claim an LFS checksum cannot make for you.

```
dc5351625f3a8fbd416ada14b2f8a5921d5c68b460700c65d66d0f2e966c5aad  HY-MT2-7B-Abliterated-Q4_K_M.gguf
b4f7d13ad2c9ef8c78a43078820df22b9bfc60cc2ba8873edc85674759bfb2fd  HY-MT2-7B-Abliterated-Q5_K_M.gguf
de3774b36af7d4cfca52c61d9decd379b0688a3ded35f973aa9a3935b6518c84  HY-MT2-7B-Abliterated-Q6_K.gguf
ea6dd5b24e4af2abc13f9e34a5819b8cdf398464baf143df8968eba73f140d32  HY-MT2-7B-Abliterated-Q8_0.gguf
```

## License

Apache-2.0, inherited from `tencent/Hy-MT2-7B` — the full text is in `LICENSE`, copied verbatim from
that repo. Neither the ablation nor the quantization changes anything about it.

Note that Apache-2.0 §4(b) requires modified files to carry prominent notices stating they were
changed; that is the purpose of the notice at the top of this card, and of the provenance table
naming who did which step.

## Credits

- [Tencent Hunyuan](https://huggingface.co/tencent) — the Hy-MT2 base model
- [mlx-community](https://huggingface.co/mlx-community) — the abliterated weights
- [jim-plus/llm-abliteration](https://github.com/jim-plus/llm-abliteration) — the abliteration method
- [tencent/Hy-MT2-7B-GGUF](https://huggingface.co/tencent/Hy-MT2-7B-GGUF) — the official GGUF used as
  the reference to verify this conversion
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — conversion and quantization tooling

## Supporting my work

If these quants are useful to you, consider supporting them via [Ko-fi](https://ko-fi.com/alexwkleung). It goes toward local hardware for quantizing and testing larger models. I also build [Reika](https://reikacode.com), a coding agent CLI designed around small local models first.
