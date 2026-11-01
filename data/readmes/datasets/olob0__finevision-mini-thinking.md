---
pretty_name: FineVision-mini Thinking
license: other
license_name: finevision-per-source
license_link: https://huggingface.co/datasets/HuggingFaceM4/FineVision
language:
- vi
- zh
- en
- th
- id
- ms
- fil
- ja
- km
- lo
- my
- ta
- tet
- ko
- pt
- fr
- de
- ru
- es
- ar
- jv
task_categories:
- visual-question-answering
- image-to-text
tags:
- multilingual
- reasoning
- finevision
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*/*.parquet
---

# FineVision-mini Thinking

<a href='https://ko-fi.com/R6R0PGKEJ' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi6.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

**FineVision-mini** is a slice I made of [HuggingFaceM4/FineVision](https://huggingface.co/datasets/HuggingFaceM4/FineVision):
169 of its image subsets, 101,321 rows (~40 GB) out of FineVision's 24.2M rows / 4.65 TB (about 0.4% of
the rows, 0.9% of the bytes), sampled with a fixed seed. The 16 text-only subsets were left out.

This dataset is that slice, **fully translated and augmented with reasoning**, published in increments:
each batch processes more rows of FineVision-mini and is appended here, until the whole slice is covered.

For every row:

- the **entire conversation is translated** into a single target language, questions and answers alike.
  The images are the only thing that stays as is. Code, identifiers, URLs and text visible inside
  code are kept verbatim as part of the translation rules.
- every assistant turn gets a **reasoning trace** in the same language, explaining how the answer
  follows from the image and the question.

## What is different

| column | change |
|---|---|
| `texts` | whole conversation (`user` and `assistant`) translated into `language`. (the `<image>` placeholders removed if present) |
| `reasoning` | **new**, `list<string>`, one analysis per turn, aligned with `texts`, written in `language` |
| `language` | **new**, BCP 47 tag of the row |

Everything else (`images` as original bytes, `source`, the eight `*_ratings` / `*_min` columns) is unchanged.

> The source conversation is not kept in this dataset. Rows tagged en-US are the model's English rendering of the source and are usually identical to it, but they are still generated text, not a verbatim copy. The untranslated conversations are the texts column of FineVision.

The reasoning is written so that `image + question -> reasoning -> response`: it describes the visual
and logical evidence, never the answer itself, and never implementation details found only in the
response (for image-to-code rows it describes layout, colors, typography. Not the code).

## Languages

Each row is in **one** language: a row in `pt-BR` has its whole conversation and reasoning in Portuguese, and no other version of it exists in the dataset.

The 21 languages are mixed across rows, split evenly inside every subset (so every subset covers every language), and the `language` column tells which one a row is in.

Filter on it to get a single-language subset:
`vi-VN zh-CN en-US th-TH id-ID ms-MY fil-PH ja-JP km-KH lo-LA my-MM ta-IN tet-TL ko-KR pt-BR fr-FR de-DE ru-RU es-ES ar-001 jv-ID`

```python
ds.filter(lambda r: r["language"] == "pt-BR")
```

<img src="assets/languages.png" alt="Rows per language" width="400">

## Generation

- **Model:** Gemma 4 12B IT (QAT, `UD-Q4_K_XL`), `mmproj-F32`, MTP draft model for speculative decoding, via `llama-server` (llama.cpp).
- **Sampling:** temperature 1.0, top-p 0.95, top-k 64, **reasoning mode off**, `--image-max-tokens 1024`.
- **Prompt:** one request per row with all images and all question/response pairs. A fixed system prompt
  defines the causal rule above, the translation rules (translate the prose, keep code, identifiers, URLs and visible text inside code verbatim) and the output format. The target language is passed as `tag (English name)`, e.g. `lo-LA (Lao)`, because the bare tag was misread for rare languages.

## Rules and validation

- Eligible rows: 1-4 images and 1–30 question/response pairs (the model loses count above that).
- Output must be valid JSON with exactly one item per pair. All fields strings. `r` may be empty only
  when the source response was empty.
- Non-Latin target languages (th, lo, km, my, ta, ko, ja, zh, ru, ar) are checked by Unicode script. A reasoning trace in the wrong script is rejected. Latin-script languages cannot be checked this way.
- Generation is capped at roughly twice the expected output length. Truncated or looping outputs are rejected.
- Up to 3 attempts per row, then a second pass with lower concurrency. Rows the model still fails on
  (about 0.2%) are omitted, nothing is patched by hand.

## License and credits

Images and source conversations come from FineVision and keep the license of their original
subset: see the [FineVision dataset card](https://huggingface.co/datasets/HuggingFaceM4/FineVision)
for per-source terms. Translations and reasoning traces are model-generated with Gemma 4 and are
subject to the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).

Credits go to [HuggingFaceM4](https://huggingface.co/HuggingFaceM4) for FineVision and the source
datasets it aggregates, to Google for Gemma, to [unsloth](https://huggingface.co/unsloth) for the GGUF
quantizations, and to the llama.cpp project for the inference server.
