---
license: cc-by-4.0
base_model: Helsinki-NLP/opus-mt-tc-big-en-ko
tags:
  - onnx
  - translation
library_name: transformers
language:
  - en
  - ko
---

# opus-mt-en-ko-onnx

ONNX export (fp32 and dynamic int8) of [`Helsinki-NLP/opus-mt-tc-big-en-ko`](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-en-ko), a Marian transformer-big model from the OPUS-MT project that translates English to Korean.

**License:** cc-by-4.0, from the base model.

## Vocabularies

The original Marian model, [opusTCv20210807-sepvoc_transformer-big_2022-07-28](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-kor/opusTCv20210807-sepvoc_transformer-big_2022-07-28.zip), was trained with separate source and target vocabularies. It ties all embeddings (`tied-embeddings-all`), so one embedding matrix serves both sides, and the ONNX graphs need no change.

The tokenizer files need two vocabularies:

- `vocab.json` holds the source (English) ids, from the release's `src.vocab` plus `<pad>` at 32000.
- `target_vocab.json` holds the target (Korean) ids, from the release's `trg.vocab` plus `<pad>` at 32000.
- `tokenizer_config.json` sets `"separate_vocabs": true`.

The `vocab.json` in the base model repo is the target vocabulary and its config sets `"separate_vocabs": false`. With those files, English text encodes with Korean ids, and the output is unrelated to the input.

## Evaluation

The first 50 sentences of FLORES-200 devtest, `eng_Latn` to `kor_Hang`. chrF is the sacrebleu corpus chrF against the FLORES-200 reference. Decoding uses this repo's `generation_config.json` (`num_beams=4`).

| Build | Tokenizer files | chrF |
|---|---|---|
| fp32 | `vocab.json` and `target_vocab.json` of this repo | 36.40 |
| int8 | `vocab.json` and `target_vocab.json` of this repo | 35.25 |
| fp32 | the one `vocab.json` of the base model repo | 0.98 |

The card example of the base model, "2, 4, 6 etc. are even numbers.", gives "2, 4, 6 등은 짝수입니다." with the fp32 and the int8 graphs.

## Export

```
optimum-cli export onnx --model Helsinki-NLP/opus-mt-tc-big-en-ko --task text2text-generation-with-past <out_dir>
```

The int8 graphs come from `onnxruntime.quantization.quantize_dynamic` with QUInt8 weights. A per-channel QInt8 rebuild scored chrF 35.34 on the same sentences, so the int8 graphs were kept.

## File layout

```
./        fp32 ONNX graphs (encoder_model.onnx, decoder_model.onnx, decoder_with_past_model.onnx) and tokenizer files
./int8/   int8 ONNX graphs and the same tokenizer files
```

## Usage

```python
from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import MarianTokenizer

repo = "TigreGotico/opus-mt-en-ko-onnx"
tok = MarianTokenizer.from_pretrained(repo)
model = ORTModelForSeq2SeqLM.from_pretrained(repo)  # subfolder="int8" for the int8 graphs
inputs = tok("2, 4, 6 etc. are even numbers.", return_tensors="pt")
print(tok.decode(model.generate(**inputs)[0], skip_special_tokens=True))
```

With [linguonnx](https://github.com/TigreGotico/linguonnx):

```python
from linguonnx.translate import load_translator

translator = load_translator(model="opus-mt-en-ko-int8")
print(translator.translate("2, 4, 6 etc. are even numbers.", "en", "ko"))
```
