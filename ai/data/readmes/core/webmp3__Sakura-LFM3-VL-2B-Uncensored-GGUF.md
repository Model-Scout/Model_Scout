---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-VL-2B
base_model_relation: quantized
library_name: gguf
pipeline_tag: image-text-to-text
language:
  - en
  - ar
  - zh
  - fr
  - de
  - it
  - ja
  - ko
  - pt
  - es
  - vi
  - th
  - id
  - hi
  - ru
  - pl
tags:
  - sakura
  - gguf
  - lfm3
  - lfm3-vl
  - vision
  - uncensored
  - abliterated
  - not-for-all-audiences
---

> For adults only; you are responsible for what you generate and for the laws that apply to you. The language weights of this model were edited to refuse less; **it still refused 1 of the 104 harmful prompts we tested** (strict count; a broader keyword count finds 27), and we measured only English prompts in a single setting (see below). Do not use it to harm others.

# Sakura — LFM3-VL-2B, uncensored (GGUF)

[LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) by Liquid AI (a 1.9B-parameter vision-language model with a hybrid of convolution and attention layers) in a version whose **language weights were edited by us with an abliteration method** so that it refuses less, as a GGUF in Q8_0 with its vision projector. The unmodified model is Liquid AI's [LFM3-VL-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF).

## What was changed

- The **language weights were edited** with an abliteration method (a refusal direction is removed from part of the weight matrices), with settings chosen and tuned by us, on the original checkpoint `LiquidAI/LFM3-VL-2B` (revision `ba44bd51`). All other weights, **including the whole vision part, are unchanged** (we compared every tensor of the edited checkpoint with the original).
- The edited checkpoint was converted to GGUF with llama.cpp **b12058** and quantized to Q8_0 (no importance matrix). The vision projector was converted with the same build and is stored as F16; it comes from the unchanged vision part.

## Files

| File | Size | What it is |
|---|---:|---|
| `Sakura-LFM3-VL-2B-Uncensored-Q8_0.gguf` | 1.72 GiB | the language model, Q8_0 |
| `Sakura-LFM3-VL-2B-Uncensored-mmproj-f16.gguf` | 0.35 GiB | vision projector, F16 (needed for images) |

SHA-256 of every file is in `SHA256SUMS` (`results.json` also lists the two GGUF files).

## Run

```bash
llama-server -m Sakura-LFM3-VL-2B-Uncensored-Q8_0.gguf --mmproj Sakura-LFM3-VL-2B-Uncensored-mmproj-f16.gguf --jinja -ngl 99 -c 8192
```

The architecture needs a llama.cpp build that knows `lfm3` and its vision projector; we used **b12058** (2026-11-02). Like the original, the model **reasons before it answers** by default; pass `chat_template_kwargs` `{"enable_thinking": false}` to switch that off (our refusal measurement used that setting). Harmless example answers (thinking on, temperature 0, up to 700 tokens; they say nothing about how the model answers what the original refuses): *"Schreibe einen kurzen Satz über den Herbst auf Deutsch."* → *"Der Herbst bringt kühle Luft, bunte Blätter und die Vorabendfeiern."*; *"用一句话介绍一下樱花。"* → a one-sentence description of cherry blossoms in Chinese; a Python function summing the squares of the even numbers of a list.

## What we measured

**Refusals.** The 104 harmful prompts of the test split of `mlabonne/harmful_behaviors`, plain chat without a system prompt, thinking switched off, temperature 0, up to 300 tokens, `llama-server` b12058; the first 400 characters of each answer are examined. *strict* = the answer contains a clear refusal phrase (I can't, I cannot, I won't, I'm unable, as an AI, ...); *keyword markers* = any of a broader list of 33 phrases (also words such as "illegal" or "harmful"), which also counts answers that comply but add a warning. **100 of these 104 prompts are the ones the editing procedure was tuned against, so this does not show how the model behaves on prompts it has not seen.**

| Model (both Q8_0) | strict refusals | keyword marker hits |
|---|---:|---:|
| unmodified (Liquid AI's `LFM3-VL-2B-Q8_0.gguf`, SHA-256 `e138e541…`) | **103 / 104** | 103 / 104 |
| **this repository** | **1 / 104** | 27 / 104 |

An answer that is not counted as a refusal has not necessarily done what was asked; we did not check the quality of the answers beyond reading some. We read some of the answers; none is dominated by repetition (median length 1,470 characters).

**Other checks.** Harmless German, English (code) and Chinese prompts are answered coherently, with a thinking part, like the unmodified Q8_0. One neutral image (a generated picture of a cat) was described correctly with the projector.

**Distance to the unmodified model.** KL divergence of this Q8_0 against Liquid AI's unmodified Q8_0 (same file as above; `llama-perplexity` b12058, 20 chunks of 2048 tokens, English held-out text mix and a neutral English web text, logits of the unmodified model as reference):

| Text | Mean KL divergence | Same top token | Perplexity (this) | Perplexity (unmodified) |
|---|---:|---:|---:|---:|
| English held-out mix (heldout_en_mix) | 0.0044 ± 0.0001 | 97.2 % | 18.43 | 18.38 |
| English web text (mixedweb-v1) | 0.0074 ± 0.0001 | 95.5 % | 103.36 | 102.59 |

This measures how far the edited model moved from the original on ordinary text; it says nothing about prompts that the original refuses.

**Not measured:** any capability benchmark, refusals in other languages, with a system prompt or on other prompt sets, multi-turn chats, long context, more than one image, video, speed.

## License

LFM Open License v1.0 as the original (`LICENSE`, copy included). It limits **commercial use to organizations with less than USD 10 million annual revenue** (details and exceptions in the license; this is no legal advice). The files are modified versions of the original weights; see `NOTICE` for the prominent notice of the changes. Liquid AI is not involved in them.

## Credits

- Model: [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) by Liquid AI.
- Conversion, quantization and measurement: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT).

---

中文版见 [README_zh.md](README_zh.md)。
