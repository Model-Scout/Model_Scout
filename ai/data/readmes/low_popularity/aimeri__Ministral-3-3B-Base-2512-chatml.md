---
license: apache-2.0
base_model: aimeri/Ministral-3-3B-Base-2512-text
library_name: transformers
pipeline_tag: text-generation
language: [en, fr, es, de, it, pt, nl, zh, ja, ko, ar]
tags: [ministral3, mistral, text-only, base, chatml]
---

# aimeri/Ministral-3-3B-Base-2512-chatml

A ChatML training base made from [`aimeri/Ministral-3-3B-Base-2512-text`](https://huggingface.co/aimeri/Ministral-3-3B-Base-2512-text),
the text-only export of [`mistralai/Ministral-3-3B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512).
It is still a base model: nothing was trained. It is meant to be fine-tuned with the ChatML template below.

## What changed vs the text-only export

- Two unused reserved slots in the Tekken vocabulary are renamed: `<SPECIAL_20>` -> `<|im_start|>` (id 20) and
  `<SPECIAL_21>` -> `<|im_end|>` (id 21). No vocabulary resize. `<|im_end|>` is the eos token (`config.json`
  `eos_token_id: 21`, `generation_config.json` `eos_token_id: [21]`). bos stays `<s>` (id 1), pad stays `<pad>` (id 11).
- Rows 20 and 21 were untrained: both were the same shared stub vector (norm 0.2838) as every other unused control
  token. They are initialised from same-model donors: row 20 <- `<s>` (row 1), row 21 <- `</s>` (row 2). This model
  ties `lm_head` to the embedding (`tie_word_embeddings: true`, no separate head tensor), so one copy sets both the
  input embedding and the output row. A dead `<|im_end|>` output row would leave a fine-tune unable to stop.
- Checked on the real weights: on a prompt without ids 20/21, logits match the text-only export bit for bit in every
  column except 20 and 21 (max diff 0.0), and those two columns equal the `<s>` and `</s>` columns.
- `tekken.json` is removed. With it present, `AutoTokenizer` returns the mistral-common backend, which ignores Jinja
  chat templates.
- `tokenizer_config.json` sets `tokenizer_class: PreTrainedTokenizerFast`. With the original `LlamaTokenizerFast`,
  transformers 5.x rebuilds a sentencepiece-style pre-tokenizer instead of using `tokenizer.json`, and every newline
  disappears (`"a\nb"` becomes one token). The pre-tokenizer regex in `tokenizer.json` was compared against
  `tekken.json` and matches, so it is unchanged.
- The ChatML template is in `chat_template.jinja` and embedded in `tokenizer_config.json`.

## Template and BOS

```jinja
{%- for message in messages -%}
{{- '<|im_start|>' + message['role'] + '\n' -}}
{{- message['content'] | trim -}}
{{- '<|im_end|>\n' -}}
{%- endfor -%}
{%- if add_generation_prompt -%}
{{- '<|im_start|>assistant\n' -}}
{%- endif -%}
```

The template emits no BOS. `<s>` comes from the tokenizer's post-processor when you encode with special tokens, so
render first and then encode:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
repo = "aimeri/Ministral-3-3B-Base-2512-chatml"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype="bfloat16", device_map="auto")
text = tok.apply_chat_template([{"role": "user", "content": "hi"}], tokenize=False, add_generation_prompt=True)
ids = tok(text, return_tensors="pt").input_ids        # [1, 20, ...]: one <s>, then <|im_start|>
```

`apply_chat_template(..., tokenize=True)` does not add `<s>` (it returns `[20, ...]`). If your trainer or server
tokenizes that way, add the BOS yourself.

## Before fine-tuning

The base has never seen ChatML. Greedy decoding on a rendered chat prompt gives a coherent first sentence, then
keeps writing new `user` turns and never emits `<|im_end|>`. Stopping and turn-taking come from your fine-tune.

## Provenance

Built with `claim_chatml.py` (token rename + row graft + tokenizer fixes) on top of `prep_text_only.py` (vision tower
removed, language model bit-identical to the original). Unchanged shards are byte-for-byte copies. License follows the
original: Apache-2.0.
