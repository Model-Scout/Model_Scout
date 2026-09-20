---
license: apache-2.0
base_model: mistralai/Ministral-3-14B-Base-2512
library_name: transformers
pipeline_tag: text-generation
language: [en, fr, es, de, it, pt, nl, zh, ja, ko, ar]
tags: [ministral3, mistral, text-only, base, pretrained]
---

# aimeri/Ministral-3-14B-Base-2512-text

Text-only export of [`mistralai/Ministral-3-14B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512): the Pixtral vision tower and the
multimodal projector are removed, the language model is published as a plain `Ministral3ForCausalLM`.
Every language-model tensor is bit-identical to the original. Nothing was trained, merged or quantised.

## What changed

- Dropped `vision_tower.*` and `multi_modal_projector.*` (222 tensors). Kept 363 tensors,
  27.01 GB in bf16.
- Keys renamed to the CausalLM layout: `language_model.lm_head.weight -> lm_head.weight`,
  `language_model.model.* -> model.*`.
- `config.json` is the original `text_config` promoted to the top level with
  `architectures: [Ministral3ForCausalLM]`. `model_type` stays `ministral3`: this is not a plain Mistral,
  attention applies a Llama-4-style temperature scale (`rope_parameters.llama_4_scaling_beta`).
- `tie_word_embeddings: false` is written explicitly. The original composite config leaves the outer-level
  default (`true`), and a stock `from_pretrained` of the original then silently replaces the real pretrained
  `lm_head` with the embedding matrix. The two are genuinely different: max|lm_head - embed_tokens| = 0.148125.
- `llama_4_scaling: {original_max_position_embeddings, beta}` is mirrored at the top level for vLLM, whose
  `MistralForCausalLM` reads that attribute and otherwise skips the scale on HF-format checkpoints.
- Tokenizer files (`tokenizer.json`, `tekken.json`, `tokenizer_config.json`, `special_tokens_map.json`) are
  copied verbatim; only `processor_class` was removed from `tokenizer_config.json`. No chat template is
  added, this is a base model.

## Architecture

```json
{
  "hidden_size": 5120,
  "intermediate_size": 16384,
  "num_hidden_layers": 40,
  "num_attention_heads": 32,
  "num_key_value_heads": 8,
  "head_dim": 128,
  "vocab_size": 131072,
  "max_position_embeddings": 262144
}
```
RoPE: `yarn`, theta 1000000000.0, factor 16.0,
original_max_position_embeddings 16384,
llama_4_scaling_beta 0.1.

## Loading

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizerFast
model = AutoModelForCausalLM.from_pretrained('aimeri/Ministral-3-14B-Base-2512-text', dtype='bfloat16', device_map='auto')
tok = AutoTokenizer.from_pretrained('aimeri/Ministral-3-14B-Base-2512-text')   # mistral-common backend when tekken.json is present
```

`AutoTokenizer` returns the mistral-common backend because `tekken.json` ships alongside `tokenizer.json`.
That backend ignores custom Jinja chat templates. If you fine-tune with your own template, load
`PreTrainedTokenizerFast.from_pretrained(...)` instead (control tokens then encode as single ids:
`<s>`=1, `</s>`=2, `[INST]`=3, `[/INST]`=4). If you drop `tekken.json` from a copy, ALSO set
`tokenizer_class` to `PreTrainedTokenizerFast` in `tokenizer_config.json`: on transformers 5.x the
`LlamaTokenizerFast` class named there rebuilds a sentencepiece-style pre-tokenizer instead of using
`tokenizer.json`, and `"a\nb"` becomes one token (newlines disappear).

- vLLM: `Ministral3ForCausalLM` is registered (served by its Mistral implementation). Check the log shows
  the Llama-4 attention scale enabled; the `llama_4_scaling` key in `config.json` is what turns it on.
- llama.cpp: `convert_hf_to_gguf.py` registers `Ministral3ForCausalLM` (YaRN + attention temperature scale).

## Control-token liveness (measured on this export)

The pretraining data never contained most of the control tokens, so their embedding and `lm_head` rows are
untrained stubs (every unused row is the same shared vector). Only the rows below are trained on both sides;
everything else in ids 0-999 is dead and must be trained or grafted before it can be relied on.

| id | token | embed norm | head norm | status |
|---:|---|---:|---:|---|
| 0 | `<unk>` | 0.0000 | 0.1701 | embed dead, head dead |
| 1 | `<s>` | 0.3731 | 0.1701 | embed ok, head dead |
| 2 | `</s>` | 0.2229 | 0.4048 | embed ok, head ok |
| 3 | `[INST]` | 0.2222 | 0.1701 | embed ok, head dead |
| 4 | `[/INST]` | 0.2570 | 0.1701 | embed ok, head dead |
| 5 | `[AVAILABLE_TOOLS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 6 | `[/AVAILABLE_TOOLS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 7 | `[TOOL_RESULTS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 8 | `[/TOOL_RESULTS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 9 | `[TOOL_CALLS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 10 | `[IMG]` | 0.0000 | 0.1701 | embed dead, head dead |
| 11 | `<pad>` | 0.0000 | 0.1701 | embed dead, head dead |
| 12 | `[IMG_BREAK]` | 0.2418 | 0.1701 | embed ok, head dead |
| 13 | `[IMG_END]` | 0.2888 | 0.1701 | embed ok, head dead |
| 14 | `[PREFIX]` | 0.0000 | 0.1701 | embed dead, head dead |
| 15 | `[MIDDLE]` | 0.0000 | 0.1701 | embed dead, head dead |
| 16 | `[SUFFIX]` | 0.0000 | 0.1701 | embed dead, head dead |
| 17 | `[SYSTEM_PROMPT]` | 0.0000 | 0.1701 | embed dead, head dead |
| 18 | `[/SYSTEM_PROMPT]` | 0.0000 | 0.1701 | embed dead, head dead |
| 19 | `[TOOL_CONTENT]` | 0.0000 | 0.1701 | embed dead, head dead |
| 20 | `<SPECIAL_20>` | 0.0000 | 0.1701 | embed dead, head dead |
| 21 | `<SPECIAL_21>` | 0.0000 | 0.1701 | embed dead, head dead |
| 22 | `<SPECIAL_22>` | 0.0000 | 0.1701 | embed dead, head dead |
| 23 | `<SPECIAL_23>` | 0.0000 | 0.1701 | embed dead, head dead |
| 24 | `[AUDIO]` | 0.0000 | 0.1701 | embed dead, head dead |
| 25 | `[BEGIN_AUDIO]` | 0.0000 | 0.1701 | embed dead, head dead |
| 26 | `<SPECIAL_26>` | 0.0000 | 0.1701 | embed dead, head dead |
| 27 | `<SPECIAL_27>` | 0.0000 | 0.1701 | embed dead, head dead |
| 28 | `<SPECIAL_28>` | 0.0000 | 0.1701 | embed dead, head dead |
| 29 | `<SPECIAL_29>` | 0.0000 | 0.1701 | embed dead, head dead |
| 30 | `<SPECIAL_30>` | 0.0000 | 0.1701 | embed dead, head dead |
| 31 | `<SPECIAL_31>` | 0.0000 | 0.1701 | embed dead, head dead |
| 32 | `[ARGS]` | 0.0000 | 0.1701 | embed dead, head dead |
| 33 | `[CALL_ID]` | 0.0000 | 0.1701 | embed dead, head dead |
| 34 | `[THINK]` | 0.0000 | 0.1701 | embed dead, head dead |
| 35 | `[/THINK]` | 0.0000 | 0.1701 | embed dead, head dead |
| 36 | `<SPECIAL_36>` | 0.0000 | 0.1701 | embed dead, head dead |
| 37 | `<SPECIAL_37>` | 0.0000 | 0.1701 | embed dead, head dead |
| 38 | `<SPECIAL_38>` | 0.0000 | 0.1701 | embed dead, head dead |
| 39 | `<SPECIAL_39>` | 0.0000 | 0.1701 | embed dead, head dead |
| 500 | `<SPECIAL_500>` | 0.0000 | 0.1701 | embed dead, head dead |
| 999 | `<SPECIAL_999>` | 0.0000 | 0.1701 | embed dead, head ok |

Trained on both sides: `</s>`.
Dead on at least one side: 39 of 40 named control tokens.

## Provenance

Converted from `mistralai/Ministral-3-14B-Base-2512` with `prep_text_only.py` (streaming shard rewrite, CPU only). Verified after
writing: key census, `lm_head` untied on disk, transformers load, and logits parity against the original
VLM on the same tokens. License follows the original: Apache-2.0.
