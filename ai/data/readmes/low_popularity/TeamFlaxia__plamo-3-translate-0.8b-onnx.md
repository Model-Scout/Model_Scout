---
language:
- ar
- az
- be
- bg
- bn
- ca
- ceb
- de
- en
- es
- et
- eu
- fa
- fr
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- jv
- ka
- kk
- km
- ko
- lt
- lv
- ml
- mr
- ms
- my
- ne
- nl
- pa
- pl
- ru
- si
- sk
- sl
- sr
- sw
- ta
- te
- th
- tl
- ur
- uz
- vi
- zh
license: other
library_name: transformers
license_name: plamo-community-license
pipeline_tag: translation
tags:
- onnx
- transformers.js
- translation
- multilingual
base_model: pfnet/plamo-3-translate-0.8b
---

# Plamo-3-translate-0.8b (ONNX for Transformers.js)

ONNX build of [pfnet/plamo-3-translate-0.8b](https://huggingface.co/pfnet/plamo-3-translate-0.8b)
(890M params, 52 languages), usable with [Transformers.js](https://huggingface.co/docs/transformers.js)
v4 (onnxruntime-web).

## Files

| file | dtype | transformers.js dtype | notes |
|------|-------|----------------------|-------|
| `onnx/model_fp16.onnx` | fp16 | `fp16` | reference/base |
| `onnx/model_q4f16.onnx` | fp16 + int4 (MatMulNBits) | `q4f16` | **recommended default** |
| `onnx/model_q4.onnx` | fp32 + int4 (MatMulNBits) | `q4` | fp32 activations |

`q8`/`int8`/`uint8` variants are not shipped: dynamic int8 quantization
(`DynamicQuantizeLinear`) of this graph is numerically unstable in ORT
verified against the fp32 graph (top-logit collapse), so users should stick
to `q4f16` (recommended for wasm) or `q4`.

## Load (Transformers.js)

```js
import { pipeline, AutoTokenizer } from '@huggingface/transformers';

const tokenizer = await AutoTokenizer.from_pretrained('your-org/plamo-3-translate-0.8b-onnx');
const prompt = tokenizer.apply_chat_template(
  [{ role: 'user', content: '会議は来週の月曜日に変更されました。' }],
  { target_lang: 'en', add_generation_prompt: true, tokenize: false },
);
const pipe = await pipeline('text-generation', 'your-org/plamo-3-translate-0.8b-onnx', { dtype: 'q4f16', device: 'wasm' });
const out = await pipe(prompt, { max_new_tokens: 128, do_sample: false });
```

## Prompt format

Build a prompt with `tokenizer.apply_chat_template([{role:'user',content:text}], {target_lang, tokenize:false})`,
stripping the leading `<|plamo:bos|>` since the pipeline tokenizes with
`add_special_tokens=true`. Language codes (e.g. `ja(easy)`, `zh-hans`) live
inside the prompt text — `src_lang`/`tgt_lang` options are **not** used for
Plamo prompts.

## Architecture / conventions

* `config.json` is relabeled `model_type: qwen3` so Transformers.js resolves a
  decoder-only class; the ONNX graph itself is an exact trace of the original
  `Plamo3ForCausalLM` forward (custom RMSNorm `weight+offset`, QK-norm, fused
  QKV/gate-up projections, sliding-window = 2048 on 14/16 layers, YaRN on the
  full-attention layers, default RoPE theta=1e4 on the sliding layers).
* Graph IO: `input_ids`, `attention_mask` (int64), `past_key_values.{0..15}.{key,value}`
  in; `logits`, `present.{0..15}.{key,value}` out. No `position_ids` input
  (the original model computes positions from the cache length internally).
* Tokenizer is the Plamo Unigram vocab converted to HF `tokenizer.json`.
  `decoder` is `ByteFallback` so `<0xXX>` byte tokens are decoded back to
  UTF-8 text (e.g. ja->ko generation restores Hangul syllables). Do not
  downgrade to `Fuse`, which would print literal `<0xEB>...` sequences.
  Known approximation: Plamo's custom preprocessing ("hard split around
  >=2 consecutive spaces / >=4 repeated chars") is not expressible in HF
  tokenizers, so boundary tokens may differ slightly on long runs of spaces /
  repeated characters.

## Korean / OOV input in Transformers.js

`tokenizer.json` has `byte_fallback: true`, and Rust/Python correctly expand
OOV Hangul syllables (only 467 of 11172 are in-vocab, e.g. `녕`/`늘`/`씨` are
not) to `<0xXX>` byte tokens. `@huggingface/tokenizers` JS Unigram
`populate_nodes()` does not yet implement byte-fallback (upstream
huggingface/tokenizers.js#26), so raw Korean input collapses to `unk (0)`.
Expand OOV characters before building the prompt:

```js
// outputs/test-node/byte_fallback.mjs
import { expandByteFallback } from './byte_fallback.mjs';

const expanded = expandByteFallback(tokenizer, '안녕하세요');
// -> '안<0xEB><0x85><0x95>하세요'
const prompt = tokenizer.apply_chat_template(
  [{ role: 'user', content: expanded }],
  { target_lang: 'en', add_generation_prompt: true, tokenize: false },
);
```

This produces the same ids as Rust `tokenizers`
(`안녕하세요 -> [안, <0xEB>, <0x85>, <0x95>, 하, 세, 요]`).
Japanese/ASCII input is unaffected; the helper only expands characters that
would otherwise encode to `unk`.

## Rebuild

```bash
python export_onnx.py --output outputs/base_fp16.onnx --dtype fp16
python convert_tokenizer.py
python quantize.py --variant q4f16
python quantize.py --variant q4
```

## Source

* Base model: pfnet/plamo-3-translate-0.8b — Plamo Community License
  (https://plamo.preferredai.jp/info/plamo-community-license-en).
  Weights untouched: fp16 copy of the original BF16 checkpoint.
