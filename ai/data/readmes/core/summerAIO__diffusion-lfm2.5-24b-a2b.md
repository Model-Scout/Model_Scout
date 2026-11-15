---
library_name: transformers
license: other
license_name: lfm1.0
license_link: https://huggingface.co/summerAIO/diffusion-lfm2.5-24b-a2b/blob/main/licenses/LFM-Open-License-v1.0.txt
base_model: LiquidAI/LFM2.5-24B-A2B
pipeline_tag: text-generation
tags:
- diffusion
- lfm2
- lfm2.5
- moe
- code-generation
- lora-merged
- experimental
- conversational
- custom_code
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
- vi
- th
- id
- hi
- ru
- pl
---

# diffusion-lfm2.5-24b-a2b

> **Experimental research checkpoint.** This is a LoRA-merged, block-masked-diffusion adaptation of [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B). Repo-bundled quality checks did **not** approve any tested sampler setting: code and exact-answer probes failed across a 1–15 step sweep, and several recorded generations are highly repetitive. Use for research and sampler development, not as a general-purpose assistant.

## Overview

`summerAIO/diffusion-lfm2.5-24b-a2b` takes Liquid AI's LFM2.5 24B MoE language model and adapts it for **block masked diffusion** decoding instead of standard left-to-right generation.

At a high level:

- The backbone is still `Lfm2MoeForCausalLM` (`model_type`: `lfm2_moe`): 40 layers, 64 experts, top-4 routing, 24.0B total parameters and **2.45B active** (figures from the [base model card](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B); this repo's weight index reports 23,971,585,280 parameters).
- A rank-64 LoRA was merged into the base weights (0 LoRA parameters remain in the published checkpoint).
- A learned **mask embedding** is stored separately in `diffusion.safetensors` and swapped onto masked canvas positions.
- Custom Python in this repo implements the diffusion sampler. Load with `trust_remote_code=True`. Attention layers are switched to non-causal so the canvas can use bidirectional attention.

The files in this repository are explicit about the experimental status: merge numerical equivalence did not pass strict thresholds, and `quality-selection-summary.json` records `best_quality_setting: null`.

## Model details

| | |
| --- | --- |
| Base model | [`LiquidAI/LFM2.5-24B-A2B`](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) at revision `3dc4cd09c9a2a99e1e819693e79d3aba5e9bb4f2` |
| Architecture | LFM2 MoE (`lfm2_moe`), `Lfm2MoeForCausalLM` |
| Total parameters | 23,971,585,280 (~24.0B) |
| Active parameters | 2.45B (base card; 64 experts, 4 routed per token) |
| Layers | 40 (30 short-convolution blocks + 10 GQA attention blocks) |
| Hidden size | 2048 |
| Vocabulary | 128,000 |
| Context length (config) | 131,072 |
| Dtype of published weights | bfloat16 |
| Mask embedding | `diffusion.safetensors` key `mask_embedding`, shape `[2048]` |
| Custom class (`auto_map`) | `modeling_diffusion_patched.DiffusionLFMForCausalLM` |
| Recorded Transformers version | 5.22.2 (a Transformers 5.x build with `Lfm2MoeForCausalLM` is required) |

The tokenizer and `chat_template.jinja` are the LFM2.5 ChatML-style template inherited from the base model (BOS `<|startoftext|>`, roles wrapped in `<|im_start|>` / `<|im_end|>`, and `<think>` is prepended when `add_generation_prompt=True`). There is **no discrete mask token** in the tokenizer: masking is applied in embedding space.

Language tags above follow the base model. The training sources named in this repo (`tatsu-lab/alpaca`, `allenai/ai2_arc`) are English; whether non-English capability was preserved is not evaluated here.

## How diffusion generation works

This section describes only what the bundled code actually does.

Generation proceeds in **blocks** (the “canvas”), not one token at a time:

1. The prompt, plus tokens already accepted from earlier blocks, form a **prefix**. Prefix attention is causal.
2. A canvas of `block_size` (or fewer, near `max_new_tokens`) positions is appended, filled with `pad_token_id` and marked masked. Each masked position’s embedding is replaced by the learned mask embedding.
3. Canvas tokens use **bidirectional** attention among themselves and may attend to the prefix. The attention mask in `modeling_diffusion_lfm.py` is: if query index `q` is in the prefix (`q < p`), key `k` is allowed only when `k <= q`; otherwise all keys are allowed. To support this, every attention layer has `self_attn.is_causal = False`.
4. A denoising step runs a forward pass, predicts tokens for currently masked positions, and **commits** a subset of those predictions (unmasks them). Uncommitted positions stay masked for the next step.
5. The block finishes when every canvas slot is filled, or when an EOS token has been committed and every position before it is already filled. Completed blocks are appended and the next canvas is started, until `max_new_tokens` or EOS.

There are two samplers in the repo, with different commit rules:

**Fixed-step sampler** (`modeling_diffusion_lfm.py`, `DiffusionLFM.generate`) — this is the sampler named by `inference_recipe.json`. At step `s` of `steps`, the number of positions left masked is `count * (steps - s - 1) // steps`; the highest-confidence predictions fill the rest of the quota. The last step commits everything remaining. Optional knobs (off in the recipe defaults): `temperature`, `top_k`, `top_p`, `repetition_penalty`, and `remask_low_conf` (re-masks the weakest committed tokens once before the final step). The prompt itself is always kept; recently generated tokens are limited by `prefix_window` (default 256). On first `generate()`, a self-test may enable a **prefix-reuse** optimization (prefix hidden states computed once per block). If internals do not match, it falls back to the full forward.

**Confidence-threshold sampler** (`modeling_diffusion_patched.py`, used when you load with `AutoModelForCausalLM` + `trust_remote_code=True`). This does **not** take a `steps` argument. It keeps unmasking until the canvas is full, committing positions with confidence ≥ `threshold` (default `0.9`), with a minimum number of commits per pass. It also applies a default `repetition_penalty` of 1.3, bans a token that already appears `max_same` times in the block (default 3), avoids committing adjacent canvas positions in the same pass, can delay EOS until `min_new_tokens`, and may stop a block early if the unique-token ratio falls below `loop_ratio` (default 0.35). Default `block_size` is 1024. Only batch size 1 is supported. The return value is the concatenated `input_ids + generated` tensor (Transformers-style), and a `streamer` is optional.

`modeling_diffusion_lfm_orig.py` is the earlier reference sampler (it also truncates the prefix to the last 256 tokens). Prefer the two modules above.

## Usage

Custom code is required. The `auto_map` entry points at the patched wrapper, which loads the backbone plus `diffusion.safetensors` and exposes `.generate()`.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "summerAIO/diffusion-lfm2.5-24b-a2b"

tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(
    repo,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user", "content": "Write a short Python function that returns the mean of a non-empty list."},
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
)
if input_ids.dim() == 1:
    input_ids = input_ids.unsqueeze(0)

output = model.generate(
    input_ids.to(model.device),
    max_new_tokens=256,
    block_size=256,
    threshold=0.9,
)
print(tokenizer.decode(output[0, input_ids.shape[1]:], skip_special_tokens=True))
```

`apply_chat_template(..., add_generation_prompt=True)` formats turns as in the base LFM2.5 template and ends with:

```text
<|im_start|>assistant
<think>
```

Whether this checkpoint was trained with that `<think>` prefix is not documented in the repo (**TODO** for the owner). If you want raw text instead of the chat template, tokenize a plain prompt and pass `input_ids` directly.

### Fixed-step sampler (latency recipe)

`inference_recipe.json` measures the **fixed-step** sampler, not the AutoModel threshold sampler. After the Auto load above, that object lives on `model.inner`. The recipe settings below are documented as **latency reproduction only**; the same file warns that output under this setting is severely repetitive and is **not** a quality recommendation.

```python
# model is the AutoModel wrapper from the previous example
tokens, stats = model.inner.generate(
    input_ids.to(model.device),
    max_new_tokens=1024,
    block_size=1024,
    steps=12,
    temperature=0.0,
    top_k=0,
    top_p=1.0,
    repetition_penalty=1.0,
    prefix_window=256,
    remask_low_conf=0.0,
)
print(tokenizer.decode(tokens, skip_special_tokens=True))
print(stats)  # forward_calls, tokens, prefix_cache
```

You can also import `from_pretrained` from `modeling_diffusion_lfm.py` and call `DiffusionLFM.generate` directly. That helper’s docstring mentions `diffusion_lfm_fast`; that module name is not in this repo — use `modeling_diffusion_lfm`.

Default arguments on `DiffusionLFM.generate` itself are more conservative than the recipe: `max_new_tokens=128`, `block_size=256`, `steps=3`.

### Hardware note

The repo reports a median of about **602 tokens/s** on a single **NVIDIA A100-SXM4-80GB** with batch size 1, 256 input tokens, a 1024-token canvas, and 12 denoising steps. That figure is a latency measurement only (`quality_approved: false`).

## Training and merge

Only facts recorded in the repo are listed here. Missing items are marked TODO.

| | |
| --- | --- |
| Starting weights | `LiquidAI/LFM2.5-24B-A2B`, revision `3dc4cd09c9a2a99e1e819693e79d3aba5e9bb4f2` |
| Adaptation | LoRA rank 64, then fully merged (`lora_parameters_remaining`: 0) |
| Checkpoint updates | `checkpoint_total_updates`: 3100 |
| Named training sources | [tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) (CC-BY-NC-4.0), [allenai/ai2_arc](https://huggingface.co/datasets/allenai/ai2_arc) (CC-BY-SA-4.0) |
| Local adapter path (as recorded) | `/content/diffusion_emeans_v2/final_adapter` |
| Merge dtype | bfloat16 |
| Merge status | `experimental_merge: true`. Strict numerical validation did **not** pass. |

Two slightly different pre/post-merge logit comparisons are stored:

- `merge_validation.json`: max abs diff 1.662, mean abs diff 0.183, top-1 agreement 1.0, `strict_numerical_validation_passed: false`, `local_reload_passed: false`, `quality_validated: false`.
- `merge-equivalence-warning.json` / `merge-verification.json`: max abs logit diff 8.4375, mean 0.347, `top1_match: false`, `strict_equivalence_pass: false`.

The notes in `merge_validation.json` say that top-1 agreement does not establish equivalence or code-generation quality, and that custom diffusion loader compatibility was not verified. Training hyperparameters (learning rate, batch size, mask schedule, sequence length, mix of Alpaca vs ARC, whether the chat template was used) are **not** present in the repo (**TODO**).

## Quality checks and limitations

Bundled evaluations are small, held-out style probes (a Python mean function, “capital of Japan”, and a short explanation prompt), plus generation-health heuristics (alphabetic fraction, distinct 4-gram ratio, longest identical token run). They are **not** a published benchmark suite.

From `recommended_settings.json`, `quality-selection-summary.json`, and `merge-verification.json`:

- No step count in 1–15 passed **all** of the fixed quality checks (`best_quality_setting` is `null`).
- The code probe and the exact capital-city probe failed at every tested step.
- From 9 steps upward, the explanation prompt was marked “non-degenerate” / passed a health screen, but the recorded text is still low quality and repetitive.
- Speed-oriented settings in the 500–700 tok/s band all failed the long-generation health screen (very long identical-token runs).

Other limitations:

- Experimental merge: pre/post-merge logits are not strictly equivalent.
- `local_reload_passed` is `false` in `merge_validation.json`.
- Only batch size 1 is implemented.
- Decoding is custom Python (not a drop-in for vLLM / SGLang / llama.cpp).
- `config.json` sets `use_cache: false`; the sampler does not use standard autoregressive KV caching for the canvas.
- This is not a substitute for the official Liquid AI LFM2.5 instruct/reasoning model.

## License

Weights in this repository are a derivative of [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) and are subject to the **LFM Open License v1.0** (see `licenses/LFM-Open-License-v1.0.txt`). That license includes a commercial-use limitation for organizations at or above a $10,000,000 annual-revenue threshold; read the full text before any commercial use.

`license-notice.txt` also names the training sources and their terms:

- Alpaca (Stanford CRFM / tatsu-lab): [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/) — non-commercial.
- AI2 ARC: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/).

This derivative is subject to the upstream model license **and** those data terms. In particular, the Alpaca CC-BY-NC-4.0 terms further restrict commercial use of this checkpoint. The notice asks that attributions be retained (Stanford CRFM, [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca); AI2, [ARC](https://allenai.org/data/arc)).

## Acknowledgements and citation

- [Liquid AI](https://www.liquid.ai/) for LFM2.5-24B-A2B and the LFM Open License. See the [base model card](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) (the Hub lists `arxiv:2511.23404` on that model).
- Stanford CRFM, for the Alpaca dataset.
- The Allen Institute for AI, for ARC.

**TODO (owner):** add a preferred citation for *this* derivative if you want one, and any extra training or authorship notes.

If you use the base model, follow Liquid AI’s citation guidance on the model card linked above.

## Files of interest

| File | Role |
| --- | --- |
| `modeling_diffusion_patched.py` | `AutoModelForCausalLM` wrapper and threshold sampler |
| `modeling_diffusion_lfm.py` | Fixed-step sampler, mask embedding loader, prefix-reuse path |
| `modeling_diffusion_lfm_orig.py` | Original reference sampler |
| `diffusion.safetensors` | Learned mask embedding |
| `inference_recipe.json` | Latency-reproduction settings and merge provenance |
| `recommended_settings.json`, `quality-selection-summary.json`, `merge-verification.json` | Quality/speed probes |
| `merge_validation.json`, `merge-equivalence-warning.json` | Merge numerical checks |
| `chat_template.jinja` | LFM2.5-style chat template |
| `licenses/` and `license-notice.txt` | License texts and attributions |

`model.safetensors.index.json` references the **13-shard** weight set (`model-00001-of-00013.safetensors` …). An additional 12-shard set is also present in the repo but is not referenced by the index.
