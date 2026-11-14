---
license: apache-2.0
base_model: mistralai/Ministral-3-3B-Base-2512
library_name: transformers
pipeline_tag: text-generation
language: [en, fr, es, de, it, pt, nl, zh, ja, ko, ar]
tags: [ministral3, mistral, text-only, base, pretrained]
---

# aimeri/Ministral-3-3B-Base-2512-text

Text-only export of [`mistralai/Ministral-3-3B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512): the Pixtral vision tower and the
multimodal projector are removed, the language model is published as a plain `Ministral3ForCausalLM`.
Every language-model tensor is bit-identical to the original. Nothing was trained, merged or quantised.

## What changed

- Dropped `vision_tower.*` and `multi_modal_projector.*` (222 tensors). Kept 236 tensors,
  6.86 GB in bf16.
- Keys renamed to the CausalLM layout: `language_model.model.* -> model.*`. There is no `lm_head`
  tensor: this model ties its output head to the input embedding (`tied_embeddings: true` in the
  original `params.json`, no head key in the original index).
- `config.json` is the original `text_config` promoted to the top level with
  `architectures: [Ministral3ForCausalLM]`. `model_type` stays `ministral3`: this is not a plain Mistral,
  attention applies a Llama-4-style temperature scale (`rope_parameters.llama_4_scaling_beta`).
- `tie_word_embeddings: true` is written explicitly, matching the original. Do not flip it to `false`:
  there is no head tensor to load, so an untied load would leave `lm_head` randomly initialised.
- `llama_4_scaling: {original_max_position_embeddings, beta}` is mirrored at the top level for vLLM, whose
  `MistralForCausalLM` reads that attribute and otherwise skips the scale on HF-format checkpoints.
- Tokenizer files (`tokenizer.json`, `tekken.json`, `tokenizer_config.json`, `special_tokens_map.json`) are
  copied verbatim; only `processor_class` was removed from `tokenizer_config.json`. No chat template is
  added, this is a base model.

## Architecture

```json
{
  "hidden_size": 3072,
  "intermediate_size": 9216,
  "num_hidden_layers": 26,
  "num_attention_heads": 32,
  "num_key_value_heads": 8,
  "head_dim": 128,
  "vocab_size": 131072,
  "max_position_embeddings": 262144
}
```
RoPE: `yarn`, theta 1000000.0, factor 16.0,
original_max_position_embeddings 16384,
llama_4_scaling_beta 0.1.

## Loading

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizerFast
model = AutoModelForCausalLM.from_pretrained('aimeri/Ministral-3-3B-Base-2512-text', dtype='bfloat16', device_map='auto')
tok = AutoTokenizer.from_pretrained('aimeri/Ministral-3-3B-Base-2512-text')   # mistral-common backend when tekken.json is present
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

The pretraining data never contained most of the control tokens. Embedding and `lm_head` are one
matrix here, so each row has a single norm. A row is marked dead when it is all-zero or the same
vector (cosine > 0.999) as the never-used reserved slot 999. Dead rows must be trained or grafted
before they can be relied on.

| id | token | norm | status |
|---:|---|---:|---|
| 0 | `<unk>` | 0.2838 | dead |
| 1 | `<s>` | 0.2175 | ok |
| 2 | `</s>` | 0.5071 | ok |
| 3 | `[INST]` | 0.3906 | ok |
| 4 | `[/INST]` | 0.3896 | ok |
| 5 | `[AVAILABLE_TOOLS]` | 0.2838 | dead |
| 6 | `[/AVAILABLE_TOOLS]` | 0.2838 | dead |
| 7 | `[TOOL_RESULTS]` | 0.2838 | dead |
| 8 | `[/TOOL_RESULTS]` | 0.2838 | dead |
| 9 | `[TOOL_CALLS]` | 0.3502 | ok |
| 10 | `[IMG]` | 0.2838 | dead |
| 11 | `<pad>` | 0.2838 | dead |
| 12 | `[IMG_BREAK]` | 0.3071 | ok |
| 13 | `[IMG_END]` | 0.3393 | ok |
| 14 | `[PREFIX]` | 0.2838 | dead |
| 15 | `[MIDDLE]` | 0.2838 | dead |
| 16 | `[SUFFIX]` | 0.2838 | dead |
| 17 | `[SYSTEM_PROMPT]` | 0.2838 | dead |
| 18 | `[/SYSTEM_PROMPT]` | 0.2838 | dead |
| 19 | `[TOOL_CONTENT]` | 0.2838 | dead |
| 20 | `<SPECIAL_20>` | 0.2838 | dead |
| 21 | `<SPECIAL_21>` | 0.2838 | dead |
| 22 | `<SPECIAL_22>` | 0.2838 | dead |
| 23 | `<SPECIAL_23>` | 0.2838 | dead |
| 24 | `[AUDIO]` | 0.2838 | dead |
| 25 | `[BEGIN_AUDIO]` | 0.2838 | dead |
| 26 | `<SPECIAL_26>` | 0.2838 | dead |
| 27 | `<SPECIAL_27>` | 0.3307 | ok |
| 28 | `<SPECIAL_28>` | 0.3119 | ok |
| 29 | `<SPECIAL_29>` | 0.2838 | dead |
| 30 | `<SPECIAL_30>` | 0.2838 | dead |
| 31 | `<SPECIAL_31>` | 0.2838 | dead |
| 32 | `[ARGS]` | 0.3113 | ok |
| 33 | `[CALL_ID]` | 0.2838 | dead |
| 34 | `[THINK]` | 0.2838 | dead |
| 35 | `[/THINK]` | 0.2838 | dead |
| 36 | `<SPECIAL_36>` | 0.2838 | dead |
| 37 | `<SPECIAL_37>` | 0.2838 | dead |
| 38 | `<SPECIAL_38>` | 0.2838 | dead |
| 39 | `<SPECIAL_39>` | 0.2838 | dead |
| 500 | `<SPECIAL_500>` | 0.2838 | dead |
| 999 | `<SPECIAL_999>` | 0.2838 | dead |

Trained: `<s>`, `</s>`, `[INST]`, `[/INST]`, `[TOOL_CALLS]`, `[IMG_BREAK]`, `[IMG_END]`, `<SPECIAL_27>`, `<SPECIAL_28>`, `[ARGS]`.
Dead: 30 of 40 named control tokens.

## Provenance

Converted from `mistralai/Ministral-3-3B-Base-2512` with `prep_text_only.py` (streaming shard rewrite, CPU only). Verified after
writing: key census, no `lm_head` on disk with a tied config, transformers load, and logits parity against the original
VLM on the same tokens. License follows the original: Apache-2.0.
