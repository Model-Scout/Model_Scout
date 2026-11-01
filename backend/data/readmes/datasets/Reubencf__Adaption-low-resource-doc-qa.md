---
language:
  - vi
  - bn
  - mai
  - nl
  - gu
  - hi
  - af
  - ur
  - te
  - ne
  - tr
  - fa
  - ta
  - id
  - pa
  - ml
  - la
  - th
  - yi
  - am
  - or
  - az
  - kn
  - sd
  - mr
  - bo
  - so
  - be
  - sat
  - da
  - ko
  - bg
  - os
  - sa
  - my
  - oc
  - gd
  - ti
  - hy
  - pl
  - mni
  - uk
  - lo
  - kk
  - ar
  - de
  - en
  - es
  - fr
  - it
  - ja
  - pt
  - zh
multilinguality:
  - multilingual
source_datasets:
  - extended|https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa
task_categories:
  - visual-question-answering
  - question-answering
  - text-generation
size_categories:
  - 10K<n<100K
license: cc-by-4.0
tags:
  - adaption
  - instruction-tuning
  - ocr
  - low-resource
  - multilingual
  - document-ai
  - magazines
  - vqa
pretty_name: Adaption Low-Resource Document Q/A
---

# Adaption Low-Resource Document Q/A

This dataset is a remastered version of
[`Reubencf/magazines-multilingual-vqa`](https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa)
prepared using **[Adaption's Adaptive Data](https://www.adaptionlabs.ai)** platform,
with a deliberate focus on **low-resource source languages** — the
languages that are underrepresented in most open multimodal datasets.

## What's inside

- **10,200 rows** of multilingual document question-answer pairs grounded in
  public-domain magazine / newspaper pages from archive.org.
- Every row carries **verbatim OCR in the page's native language** plus an
  English description and a generated Q/A pair in one of 10 target
  languages.
- The page-language distribution is heavily tilted toward **low-resource
  languages** — ~90 % of rows are in languages outside the "big 10"
  (English, Spanish, Chinese, etc.).

## Page languages (source / OCR)

The dataset covers **45+ distinct source languages** as the native page
language. A selection:

| Language | Code | Rows |
|---|---|---|
| Vietnamese | `vi` | 1,595 |
| Bengali | `bn` | 1,595 |
| **Maithili** | `mai` | 1,021 |
| Dutch | `nl` | 448 |
| Gujarati | `gu` | 445 |
| Hindi | `hi` | 439 |
| Afrikaans | `af` | 431 |
| Urdu | `ur` | 424 |
| Telugu | `te` | 396 |
| Nepali | `ne` | 383 |
| Turkish | `tr` | 369 |
| Persian / Farsi | `fa` | 369 |
| Tamil | `ta` | 367 |
| Indonesian | `id` | 356 |
| Punjabi | `pa` | 332 |
| Malayalam | `ml` | 208 |
| Latin | `la` | 146 |
| Thai | `th` | 141 |
| **Yiddish** | `yi` | 108 |
| **Amharic** | `am` | 103 |
| Odia | `or` | 69 |
| Azerbaijani | `az` | 64 |
| Kannada | `kn` | 50 |
| Sindhi | `sd` | 45 |
| Marathi | `mr` | 31 |
| **Tibetan** | `bo` | 25 |
| **Somali** | `so` | 24 |
| Belarusian | `be` | 8 |
| **Santali** | `sat` | 6 |
| Danish | `da` | 6 |
| Korean | `ko` | 4 |
| Bulgarian | `bg` | 4 |
| **Ossetian** | `os` | 3 |
| Sanskrit | `sa` | 3 |
| Burmese | `my` | 3 |
| Occitan | `oc` | 1 |
| Scottish Gaelic | `gd` | 1 |
| **Tigrinya** | `ti` | 1 |
| Armenian | `hy` | 1 |
| Polish | `pl` | 1 |
| **Meitei / Manipuri** | `mni` | 1 |
| Ukrainian | `uk` | 1 |
| **Lao** | `lo` | 1 |
| Kazakh | `kk` | 1 |

Languages in **bold** are notably low-resource in open NLP data.

## Q/A languages

The generated question-answer pairs are rendered in 10 target languages,
round-robin assigned across rows:

`ar`, `de`, `en`, `es`, `fr`, `hi`, `it`, `ja`, `pt`, `zh` (≈1,000 rows each)

## Schema

| Column | Type | Meaning |
|---|---|---|
| `identifier` | string | Source archive.org identifier |
| `page` | string | Page reference (file / page no.) |
| `page_language` | string | Native language code of the OCR'd page |
| `qa_language` | string | Target language of the generated Q/A |
| `ocr_text` | string | Verbatim OCR in the page's native language |
| `description` | string | English description of the page |
| `page_type` | string | e.g. article, advertisement, cover |
| `scan_quality` | string | Heuristic scan-quality tag |
| `ocr_confidence` | string | Heuristic OCR-confidence tag |
| `nsfw_flag` | bool | Flag set by the pipeline |
| `question` | string | Generated question in `qa_language` |
| `answer` | string | Grounded answer in `qa_language` |
| `question_type` | string | Question category |
| `difficulty` | string | Difficulty bucket |
| `enhanced_prompt` | string | Adaption-sharpened prompt |
| `enhanced_completion` | string | Adaption-sharpened completion |

## Pipeline

1. Source pages harvested from archive.org public-domain magazines.
2. OCR + page description generated with **Gemma 4 31B** via vLLM.
3. One grounded Q/A pair generated per page in one of 10 target languages,
   forming the full corpus
   [`Reubencf/magazines-multilingual-vqa`](https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa).
4. A low-resource-focused subset was fed through
   Adaption's Adaptive Data platform to produce this remastered dataset.

## Intended use

- Evaluating and training **document-understanding / OCR-VQA** models on
  low-resource languages.
- Benchmarking cross-lingual question answering where the *document* and
  the *query* are in different languages.
- As a supervised fine-tuning set that specifically stresses the long tail
  of world languages, rather than the English-centric default.

## License

CC-BY-4.0. Source images and OCR trace back to public-domain archive.org
material. Please credit both this dataset and the source pages when you
use it.

## Related

- Original corpus (all 40+ source languages, with images):
  [`Reubencf/magazines-multilingual-vqa`](https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa)
- Adaption collection:
  [`Reubencf/proper-adaption`](https://huggingface.co/collections/Reubencf/proper-adaption)

## Citation

If you use this dataset in your research or downstream work, please cite:

```bibtex
@misc{adaption_low_resource_doc_qa_2026,
  author       = {Fernandes, Reuben Chagas},
  title        = {Adaption Low-Resource Document Q/A: Magazine Pages in 45+ Low-Resource Languages},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Reubencf/Adaption-low-resource-doc-qa}}
}
```

APA-style:

> Reuben Chagas Fernandes (2026). *Adaption Low-Resource Document Q/A: Magazine Pages in 45+ Low-Resource Languages* [Dataset]. Hugging Face. https://huggingface.co/datasets/Reubencf/Adaption-low-resource-doc-qa

