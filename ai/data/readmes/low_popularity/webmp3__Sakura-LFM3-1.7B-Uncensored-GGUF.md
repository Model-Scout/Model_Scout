---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
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
  - uncensored
  - abliterated
  - not-for-all-audiences
---

> For adults only; you are responsible for what you generate and for the laws that apply to you. The weights of this model were edited to refuse less; **it still refused 10 of the 104 harmful prompts we tested** (strict count; a broader keyword count finds 39), and we measured only English prompts in a single setting (see below). Do not use it to harm others.

# Sakura — LFM3-1.7B, uncensored (GGUF)

[LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) by Liquid AI (a 1.7B-parameter language model with a hybrid of convolution and attention layers) in a version whose **weights were edited by us with an abliteration method** so that it refuses less, as a GGUF in Q8_0. The vision-language sibling is [Sakura-LFM3-VL-2B-Uncensored-GGUF](https://huggingface.co/webmp3/Sakura-LFM3-VL-2B-Uncensored-GGUF).

## What was changed

- The **weights were edited** with an abliteration method (a refusal direction is removed from part of the weight matrices), with settings chosen and tuned by us, on the original checkpoint `LiquidAI/LFM3-1.7B` (revision `ac2586a3`). All other weights are unchanged (we compared every tensor of the edited checkpoint with the original).
- The edited checkpoint was converted to GGUF with llama.cpp **b12058** and quantized to Q8_0 (no importance matrix).

## Files

| File | Size | What it is |
|---|---:|---|
| `Sakura-LFM3-1.7B-Uncensored-Q8_0.gguf` | 1.72 GiB | the model, Q8_0 |

SHA-256 of every file is in `SHA256SUMS` (`results.json` also lists the GGUF file).

## Run

```bash
llama-server -m Sakura-LFM3-1.7B-Uncensored-Q8_0.gguf --jinja -ngl 99 -c 8192
```

The architecture needs a llama.cpp build that knows `lfm3`; we used **b12058** (2026-11-02). Like the original, the model **reasons before it answers** by default; pass `chat_template_kwargs` `{"enable_thinking": false}` to switch that off (our refusal measurement used that setting).

## What we measured

**Refusals.** The 104 harmful prompts of the test split of `mlabonne/harmful_behaviors`, plain chat without a system prompt, thinking switched off, temperature 0, up to 300 tokens, `llama-server` b12058; the first 400 characters of each answer are examined. *strict* = the answer contains a clear refusal phrase (I can't, I cannot, I won't, I'm unable, as an AI, ...); *keyword markers* = any of a broader list of 33 phrases (also words such as "illegal" or "harmful"), which also counts answers that comply but add a warning. **100 of these 104 prompts are the ones the editing procedure was tuned against, so this does not show how the model behaves on prompts it has not seen.**

| Model (both Q8_0) | strict refusals | keyword marker hits |
|---|---:|---:|
| unmodified (made by us from the original weights, same build) | **101 / 104** | 102 / 104 |
| **this repository** | **10 / 104** | 39 / 104 |

An answer that is not counted as a refusal has not necessarily done what was asked; we did not check the quality of the answers beyond reading some. Only short harmless chats were compared with the unmodified model; no benchmark scores were measured. The refusal numbers come from our own probe (strict count 10 of 104 versus 101 of 104 for the unmodified model; the broader keyword count is 39 versus 102), so the model still refuses some requests. The editing procedure itself counted 43 of 100 on its own prompts with its own keyword list and generation settings; that count is of the same kind as our keyword count, not as the strict one, and the two are not directly comparable.

**Other checks.** harmless prompts in German, English (code) and Chinese (one prompt each) answered coherently with thinking on (700 tokens; the code prompt needed 2000 because both models think at length first). On our one German prompt the unmodified Q8_0 answered in English and the edited one in German; one sample at temperature 0 is no statement about language behaviour in general.

**Distance to the unmodified model.** KL divergence of this Q8_0 against an unmodified Q8_0 that we made ourselves from the original weights with the same build (`llama-perplexity` b12058, 20 chunks of 2048 tokens, English held-out text mix and a neutral English web text, logits of the unmodified model as reference):

| Text | Mean KL divergence | Same top token | Perplexity (this) | Perplexity (unmodified) |
|---|---:|---:|---:|---:|
| English held-out mix (heldout_en_mix) | 0.00188 ± 0.00003 | 97.9 % | 10.12 | 10.09 |
| English web text (mixedweb-v1) | 0.00245 ± 0.00003 | 97.1 % | 31.97 | 31.86 |

This measures how far the edited model moved from the original on ordinary text; it says nothing about prompts that the original refuses.

**Not measured:** any capability benchmark, refusals in other languages, with a system prompt or on other prompt sets, multi-turn chats, long context, speed.

## License

LFM Open License v1.0 as the original (`LICENSE`, copy included). It limits **commercial use to organizations with less than USD 10 million annual revenue** (details and exceptions in the license; this is no legal advice). The file is a modified version of the original weights; see `NOTICE` for the prominent notice of the changes. Liquid AI is not involved in them.

## Credits

- Model: [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) by Liquid AI.
- Conversion, quantization and measurement: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT).

---

中文版见 [README_zh.md](README_zh.md)。
