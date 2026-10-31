---
configs:
- config_name: dolma
  data_files: "ai-culture.jsonl.gz"
  default: true  
- config_name: json
  data_files: "ai-culture.json"
pretty_name: AI-Culture Multilingual JSON + DOLMA Corpus
license: cc-by-4.0
size_categories: [10M<n<100M]
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ru
- ko
- zh
- hi
- he
tags:
- multilingual
- language-modeling  
- text-generation
- translation
- machine-translation
- cross-lingual
- llm-training
- transformer-training-data
- parallel-corpora
- reasoning-dataset
- knowledge-base
- json
- dolma
- philosophy
- culture
- long-form-content
- structured-text
- semantic-similarity
- educational-material
- natural-language-understanding
- jsonl
task_categories:
- translation
- text-generation
- text-classification
- sentence-similarity
- summarization
- fill-mask
- feature-extraction

---

# AI-Culture Multilingual JSON + DOLMA Corpus

> **16M words · 12 languages · CC-BY-4.0**

The AI-Culture corpus contains **5K articles** providing comprehensive philosophical and cultural content, exploring the intersection of technology, artificial intelligence, and human culture, **perfectly aligned across 12 languages**. All content maintains identical parallel structure across translations with **zero duplication** and **editor-curated quality**.

This project is maintained by a non-profit digital humanities team committed to advancing humane AI through **meticulously curated, thoroughly clean** cultural datasets.

[![DOI](https://zenodo.org/badge/1021100370.svg)](https://doi.org/10.5281/zenodo.16001657)

## Quick Start

```python
from datasets import load_dataset

# DOLMA JSONL format
dolma_ds = load_dataset(
    "AI-Culture-Commons/ai-culture-multilingual-json-dolma",
    name="dolma",
    split="train"
)

# JSON format (one record per article)
json_ds = load_dataset(
    "AI-Culture-Commons/ai-culture-multilingual-json-dolma",
    name="json",
    split="train"
)
```

## Dataset Overview

| File | Format | Size | Documents | Words |
|------|--------|------|-----------|-------|
| `ai-culture.jsonl.gz` | **DOLMA** JSONL (gzipped) | 66 MB | 5K | 16M |
| `ai-culture.json` | Plain JSON | 254 MB | 5K | 16M |

## Languages

Perfect machine-validated alignment across 12 languages: English, French, German, Spanish, Portuguese, Italian, Japanese, Russian, Korean, Mandarin Chinese, Hindi, Hebrew.

## Content Characteristics

All our datasets guarantee four core principles:

1. **Extremely clean**: All content is original, editor-curated text without any user comments, scraped texts, ads, tracking scripts, JavaScript, cookies, or unwanted noise. All source articles were produced by our editorial team and professionally edited.

2. **Transparent process**: *Both clean text and original HTML source* are preserved in all datasets, with full pipeline documentation (see below).

3. **Free license**: Clear free license - usage is free for any purpose including commercial use, with attribution required only when feasible.

4. **Rich intellectual content**: Long-form essays that foster philosophical reasoning, cultural awareness, and literary sensitivity in models. Our datasets provide models with deep philosophical-intellectual context and diverse connections between culture, philosophy, literature, and technology—particularly AI. The content curation is specifically designed to help train more intellectually critical and philosophically grounded AI models.

## Data Schema

### DOLMA Format Schema

The DOLMA file uses newline-delimited JSON with gzip compression, compatible with RedPajama/Dolma training pipelines:

```json
{
  "id": "en/philosophy-of-learning81",
  "text": "The First Algorithmic Era...",
  "added": "2025-08-01T14:37:12Z",
  "source": "hitdarderut-haaretz",
  "metadata": {
    "language": "en",
    "title": "An Essay on the Fermi Paradox",
    "url": "https://degeneration-of-nation.org/en/philosophy-of-learning81",
    "translation_of": "https://hitdarderut-haaretz.org/filosofia81",
    "source_format": "html",
    "domain": "philosophy",
    "license": "CC-BY-4.0",
    "timestamp": "2025-07-15T00:00:00Z",
    "word_count": 1250,
    "char_count": 7500,
    "sha256": "a1b2c3d4...",
    "html_raw": "<!DOCTYPE html>..."
  }
}
```

### JSON Format Schema

```json
{
  "id": "string",          // e.g., "he/actualia6" or "en/alternative-commentary6"
  "language": "string",    // Language code
  "title": "string",       // Article title from HTML
  "content": "string",     // Full text content without HTML
  "html": "string",        // Complete HTML source
  "url": "string",         // URL of the translated content
  "original_url": "string" // URL of original content
}
```

## Pipeline & Validation

The corpus was created with an **open-source pipeline** [[GitHub link]](https://github.com/AI-Culture-Commons/ai-culture-pipeline) that:

1. Processes files from local project directories (no web crawling required)
2. Extracts and processes content through a multi-stage pipeline:
   * **HTML files**: Compacts HTML structure, extracts titles via *BeautifulSoup*, and converts body content to clean text using *html2text* with enhanced CJK character handling
   * **PDF files**: Reads pre-converted TXT files from Word document sources that generated the PDFs
   * **Text processing**: Removes control characters, normalizes Unicode (NFKC), handles bidirectional text spacing, and collapses excessive whitespace
3. Runs language-aware word counting (smart algorithms for Chinese/Japanese/Korean vs. space-separated languages) and assigns domain labels based on file paths
4. Generates:
   * `ai-culture.jsonl.gz` – **DOLMA-compatible** newline-delimited JSON
   * `ai-culture.json` – one compact record per article
5. Runs multi-layer integrity validation including dataset loading, structure verification, and sample inspection across all formats. Includes supplementary datasets library compatibility tests for Hugging Face Hub integration

All scripts include a **zero-duplicate** guarantee. We maintain **machine-validated alignment** between languages.

## Our Websites & Licensing

- **Original Project**: [https://hitdarderut-haaretz.org](https://hitdarderut-haaretz.org) - Cultural, philosophical, and literary analysis
  - [License Terms](https://hitdarderut-haaretz.org/license): CC-BY-4.0
- **Multicultural Project**: [https://degeneration-of-nation.org](https://degeneration-of-nation.org) - Critical philosophical commentary  
  - [License Terms](https://degeneration-of-nation.org/license): CC-BY-4.0

## Citation

```bibtex
@dataset{ai_culture_json_dolma_2025,
  title  = {AI-Culture Multilingual JSON + DOLMA Corpus},
  author = {AI-Culture-Commons},
  year   = {2025},
  url    = {https://huggingface.co/datasets/AI-Culture-Commons/ai-culture-multilingual-json-dolma},
  license = {CC-BY-4.0},
  version = {1.0}
}
```