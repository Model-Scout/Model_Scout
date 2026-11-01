---
annotations_creators: []
language_creators: []
license: cc-by-4.0
multilinguality:
  - multilingual
pretty_name: Multilingual Document Q/A (Adaption)
size_categories:
  - 1K<n<10K
source_datasets:
  - extended|https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa
tags:
  - adaption
  - instruction-tuning
  - ocr
  - document-ai
  - multilingual
  - low-resource
  - magazines
  - vqa
task_categories:
  - visual-question-answering
  - question-answering
language:
  # Q/A target languages (round-robin, ~10% each)
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - pt
  - zh
  # Additional page / OCR source languages
  - af
  - am
  - az
  - be
  - bn
  - bo
  - da
  - fa
  - gu
  - id
  - kk
  - kn
  - ko
  - la
  - lo
  - ml
  - mni
  - mr
  - my
  - ne
  - nl
  - oc
  - or
  - pa
  - ru
  - sa
  - sd
  - so
  - ta
  - te
  - th
  - tr
  - ur
  - vi
  - yi
---

![banner](https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/eaaedbe8-467e-43ad-bc8d-1247c6354d19.png)

This dataset is a remastered version of [`Reubencf/magazines-multilingual-vqa`](https://huggingface.co/datasets/Reubencf/magazines-multilingual-vqa) prepared using [Adaption's](https://adaptionlabs.ai/app/auth) Adaptive Data platform.

# multilingual_doc_qa

This dataset contains multilingual question-answer pairs focused on extracting specific factual details from documents (page numbers, names, ages, dates, counts, titles, etc.). Each entry consists of a `prompt` asking for a specific detail and a `completion` providing the precise answer grounded in the source page text. Cross-lingual: the source **document** and the **question** are often in different languages, so the dataset also functions as a cross-lingual information retrieval benchmark.

### Dataset size

**8,801 rows** — instruction-tuning format with `enhanced_prompt` / `enhanced_completion` / reasoning columns.

### Domain
- Other (50%)
- History (10%)
- Product-advice (6%)

### Languages

This dataset carries two separate language dimensions — don't confuse them:

#### Q/A target languages (the language of the `question` + `answer` pair)

10 languages, round-robin assigned, ≈10 % each:

| Language | Code | Rows | Share |
|---|---|---:|---:|
| Chinese | `zh` | ~930 | 10.5 % |
| German | `de` | ~910 | 10.3 % |
| Spanish | `es` | ~900 | 10.2 % |
| Hindi | `hi` | ~900 | 10.1 % |
| Japanese | `ja` | ~885 | 10.0 % |
| Portuguese | `pt` | ~885 | 10.0 % |
| French | `fr` | ~885 | 10.0 % |
| English | `en` | ~880 | 9.9 % |
| Arabic | `ar` | ~860 | 9.7 % |
| Italian | `it` | ~810 | 9.1 % |

#### Page / OCR source languages (`page_language`)

**48 distinct source languages** — the native language of the scanned magazine/newspaper page. This is where the long tail of **low-resource languages** lives.

| Language | Code | Rows |
|---|---|---:|
| German | `de` | ~1,750 |
| French | `fr` | ~1,430 |
| Russian | `ru` | ~1,065 |
| English | `en` | ~700 |
| Bengali | `bn` | ~615 |
| Vietnamese | `vi` | ~345 |
| Portuguese | `pt` | ~315 |
| Arabic | `ar` | ~245 |
| Italian | `it` | ~205 |
| Dutch | `nl` | ~195 |
| Afrikaans | `af` | ~180 |
| Gujarati | `gu` | ~175 |
| Telugu | `te` | ~165 |
| Persian / Farsi | `fa` | ~145 |
| Japanese | `ja` | ~140 |
| Nepali | `ne` | ~130 |
| Punjabi | `pa` | ~125 |
| Chinese | `zh` | ~115 |
| Turkish | `tr` | ~100 |
| Urdu | `ur` | ~85 |
| Tamil | `ta` | ~80 |
| Malayalam | `ml` | ~80 |
| Latin | `la` | ~65 |
| Hindi | `hi` | ~60 |
| Indonesian | `id` | ~55 |
| Thai | `th` | ~55 |
| **Amharic** | `am` | ~45 |
| **Yiddish** | `yi` | ~35 |
| Spanish | `es` | ~30 |
| Azerbaijani | `az` | ~25 |
| Odia | `or` | ~25 |
| Kannada | `kn` | ~12 |
| **Somali** | `so` | ~12 |
| Marathi | `mr` | ~11 |
| **Tibetan** | `bo` | ~9 |
| Sindhi | `sd` | ~4 |
| Danish | `da` | ~2 |
| Korean | `ko` | ~2 |
| Sanskrit | `sa` | 1 |
| Burmese | `my` | 1 |
| Belarusian | `be` | 1 |
| **Lao** | `lo` | 1 |
| **Meitei / Manipuri** | `mni` | 1 |
| Occitan | `oc` | 1 |
| Kazakh | `kk` | 1 |

Languages in **bold** are notably low-resource in open NLP data.

Counts were estimated from the HF datasets-server statistics sample (~7,000 of 8,801 rows) and scaled to the full dataset; distribution shape is reliable, exact per-row-counts may differ by a few.

### Tone
- Informative (68%)
- Clear (18%)
- Helpful (10%)

### Evaluation Results

- **Quality Gains:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/cd251896-bb9d-433c-a69e-95d5a799e7e1.png" alt="QualityGains" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Grade Improvement:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/a83907ce-ec03-492e-9989-2f63e5340616.png" alt="Grade" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Percentile Chart:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/f1993aa9-3330-41a9-8ffc-902827c4fa00.png" alt="Percentile Chart" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

## Citation

If you use this dataset in your research or downstream work, please cite:

```bibtex
@misc{adaption_multilingual_doc_qa_2026,
  author       = {Fernandes, Reuben Chagas},
  title        = {Adaption Multilingual Document Q/A: Magazine Pages with Cross-Lingual Q/A},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa}}
}
```

APA-style:

> Reuben Chagas Fernandes (2026). *Adaption Multilingual Document Q/A: Magazine Pages with Cross-Lingual Q/A* [Dataset]. Hugging Face. https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa

