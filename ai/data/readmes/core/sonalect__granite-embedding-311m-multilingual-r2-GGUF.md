---
license: apache-2.0
base_model: ibm-granite/granite-embedding-311m-multilingual-r2
base_model_relation: quantized
library_name: gguf
pipeline_tag: feature-extraction
language:
  - ar
  - az
  - bg
  - bn
  - ca
  - cs
  - da
  - de
  - el
  - en
  - es
  - et
  - fa
  - fi
  - fr
  - he
  - hi
  - hr
  - hu
  - id
  - is
  - it
  - ja
  - ka
  - kk
  - km
  - ko
  - lt
  - lv
  - mr
  - ms
  - nl
  - "no"
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - sq
  - sr
  - sv
  - sw
  - te
  - th
  - tl
  - tr
  - uk
  - ur
  - uz
  - vi
  - zh
tags:
  - gguf
  - llama.cpp
  - granite
  - embeddings
  - multilingual
  - feature-extraction
  - sentence-similarity
---

# Granite-Embedding-311M-Multilingual-R2, GGUF

GGUF conversions of IBM's
[granite-embedding-311m-multilingual-r2](https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2)
for [llama.cpp](https://github.com/ggml-org/llama.cpp): a 311M-parameter
ModernBERT encoder that turns text into 768-dimensional vectors, with CLS
pooling. Nothing is changed but the file format; for what the model does and
how well, see IBM's model card.

## Files

| File | Weights | Size | SHA-256 |
| - | - | - | - |
| `granite-embedding-311m-multilingual-r2-f16.gguf` | float16 | 638 MB | `8ff94a22038b2db0096f4c0a630bd7c5dae430a177d64021df887fcd6e3c7fcf` |
| `granite-embedding-311m-multilingual-r2-q8_0.gguf` | 8-bit (`Q8_0`) | 346 MB | `54c26b869523b870a99c6359775f4c320a0c16d1cdd0ca1446767299c80cd4d5` |
| `granite-embedding-311m-multilingual-r2-vocab.gguf` | none: the tokenizer alone | 14.7 MB | `54f44ca57618c83794ab47d5d329eb71d4ba973d0744aaadd435669377e4c027` |

## How they were made

- **Source:** `ibm-granite/granite-embedding-311m-multilingual-r2`, revision
  `44399559930365213510b1ee2eb15ded83374f0e` (18 May 2026), `model.safetensors`
  and its configuration, fetched with `huggingface_hub`.
- **Converter:** llama.cpp `convert_hf_to_gguf.py` at commit
  [`d81235049384534c167caea52b85a694f6103d14`](https://github.com/ggml-org/llama.cpp/commit/d81235049384534c167caea52b85a694f6103d14)
  (5 October 2026), the llama.cpp version of the Rust crate `llama-cpp-2`
  0.1.160.

```sh
python convert_hf_to_gguf.py <snapshot of the source revision> --outtype f16  --outfile granite-embedding-311m-multilingual-r2-f16.gguf
python convert_hf_to_gguf.py <snapshot of the source revision> --outtype q8_0 --outfile granite-embedding-311m-multilingual-r2-q8_0.gguf
python convert_hf_to_gguf.py <snapshot of the source revision> --vocab-only   --outfile granite-embedding-311m-multilingual-r2-vocab.gguf
```

## How they were checked

Each file was run by llama.cpp (through `llama-cpp-2` 0.1.160, on the CPU)
and compared with IBM's own model code in PyTorch (`transformers` 5.21.0,
`torch` 2.14.1, float32, CLS pooling, L2 norm), on 181 texts of up to 512
tokens: Wikipedia articles in Russian, German and English on the same ten
topics, and paragraphs that mix Russian and English.

| File | Lowest cosine to the reference | Mean |
| - | - | - |
| f16 | 0.999999 | 1.000000 |
| q8_0 | 0.99993 | 0.99997 |

The vectors were computed from the token ids of the source repository's
own tokenizer (`tokenizer.json`). llama.cpp's built-in tokenizer, loaded
from the vocabulary-only file with `vocab_only`, gives the same ids on all
181 texts (the reference starts with `<bos>` and is cut at 512 tokens). The
vocabulary-only file carries the same tokenizer metadata as the f16 file,
key for key, and no tensors.

## Use

The model needs CLS pooling. Normalise the vectors if you compare them by
cosine.

```sh
llama-embedding -m granite-embedding-311m-multilingual-r2-f16.gguf \
  --pooling cls --embd-normalize 2 -p "Your text"

llama-server -m granite-embedding-311m-multilingual-r2-f16.gguf \
  --embedding --pooling cls
```

`granite-embedding-311m-multilingual-r2-vocab.gguf` holds the tokenizer
alone: load it with `vocab_only` to count or split text into the model's
tokens without its weights, for example to cut chunks to the model's
512-token limit when the model itself runs elsewhere.

No query or document prefix is needed. IBM trained the model mostly on
passages of up to 512 tokens.

## License

The model weights are under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
license, as published by IBM. The tokenizer is derived from the Gemma 3
tokenizer and is subject to the
[Gemma Terms of Use](https://ai.google.dev/gemma/terms), as IBM's model card
states.
