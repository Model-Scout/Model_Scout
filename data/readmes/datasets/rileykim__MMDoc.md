---
license: apache-2.0
task_categories:
- image-to-text
multimodal:
- image
- text
language:
- en
- id
- ja
- kk
- ko
- ru
- ur
- uz
- vi
- zh
language_bcp47:
- zh-cn
- zh-tw
tags:
- multimodal
- translation
- multilingual
- vision
- document-translation
- ocr
size_categories:
- 10K<n<100K
---

# MMDoc: Multilingual Multimodal Document Translation Dataset

## Overview

**MMDoc** (Multilingual Multimodal Document data) is a comprehensive dataset containing **Multilingual Document Translation** pairs, featuring real-world document images with OCR results and translations across 10 language pairs. The dataset is designed for training and evaluating multimodal document translation models that can translate text in document images while understanding visual layout and context. This dataset was used to train and evaluate **TransMLLM** (Translation-centric Multilingual Multimodal LLM), a vision-language model for low-resource document understanding.

## Dataset Structure

Each sample contains:

* `image_id`: Unique identifier for the document image (e.g., "00", "01", "patimt_00000")
* `lang_pair`: Language pair code (e.g., "en-id", "en-ja", "en-zh-tw")
* `target_lang`: Target language code (e.g., "id", "ja", "zh-tw")
* `cls`: Document class/type (e.g., "document")
* `ocr`: Raw OCR results with bounding boxes and extracted text
* `merge_ocr`: Merged OCR segments with source and target translations, including:  
   * `box`: Bounding box coordinates \[x1, y1, x2, y2\]  
   * `src_text`: Source language text  
   * `tgt_text`: Target language translated text  
   * `src_lang`: Source language code (e.g., "en")  
   * `tgt_lang`: Target language code (e.g., "id", "ja")
* `image`: Corresponding document image (JPG format)

## Language Pairs

The MMDoc dataset includes 10 language pairs, all with English as the source language, covering diverse writing systems:

| Language Pair                   | Target Language       | Code     | Writing System                    |
| ------------------------------- | --------------------- | -------- | --------------------------------- |
| English → Indonesian            | Indonesian            | en-id    | Latin                             |
| English → Japanese              | Japanese              | en-ja    | Mixed (Hiragana, Katakana, Kanji) |
| English → Kazakh                | Kazakh                | en-kk    | Cyrillic                          |
| English → Korean                | Korean                | en-ko    | Hangul                            |
| English → Russian               | Russian               | en-ru    | Cyrillic                          |
| English → Urdu                  | Urdu                  | en-ur    | Arabic                            |
| English → Uzbek                 | Uzbek                 | en-uz    | Latin                             |
| English → Vietnamese            | Vietnamese            | en-vi    | Latin                             |
| English → Chinese (Simplified)  | Chinese (Simplified)  | en-zh-cn | Han                               |
| English → Chinese (Traditional) | Chinese (Traditional) | en-zh-tw | Han                               |

## Dataset Statistics

* **Total samples**: ~10,600+ entries across train and test splits
* **Language pairs**: 10
* **Splits**: train, test
* **Image format**: JPG
* **Image naming**: Sequential numbering (00.jpg, 01.jpg, etc.) or patimt\_XXXXX.jpg format
* **Document types**: Material safety data sheets (MSDS), scientific reports, legal transcripts, business letters, invoices, forms, certificates, medical documents, technical documents, official documents

## Research Context

MMDoc was created as an extension of PATIMT-Bench (originally English-Chinese only) to support multilingual document translation research. It was used to train and evaluate **TransMLLM**, a unified vision-language model that performs end-to-end document translation from source-language images to target-language text, eliminating the need for separate OCR preprocessing.

### Key Research Contributions

* **End-to-end translation**: Direct translation from document images to target language text without intermediate OCR steps
* **Low-resource language support**: Effective handling of languages with limited training data and diverse writing systems
* **Unified architecture**: Single model handles multiple languages and writing systems (Latin, Cyrillic, Arabic, Han, Hangul, mixed scripts)
* **Layout-aware processing**: Preserves document structure, formatting, and reading order while translating

## Document Types

The MMDoc dataset contains various real-world document types with natural noise and variations:

* **Material Safety Data Sheets (MSDS)**: Chemical safety information documents
* **Scientific reports**: Research papers and technical documentation
* **Legal transcripts**: Court proceedings and legal documents
* **Business letters**: Professional correspondence and communications
* **Invoices and receipts**: Financial documents
* **Forms and certificates**: Official documents and applications
* **Medical documents**: Health records and pharmaceutical information
* **Technical documents**: Specifications and technical drawings

## Usage

MMDoc is perfect for:

* Training Multilingual Document Translation models
* End-to-end vision-language model development
* OCR-based translation research
* Document understanding tasks
* Multimodal machine translation with visual context
* Layout-aware translation models
* Low-resource language research

### Example Usage

```python
from datasets import load_dataset

# Load the MMDoc dataset
dataset = load_dataset("rileykim/MMDoc")

# Access a sample from train split
sample = dataset['train'][0]
print(f"Image ID: {sample['image_id']}")
print(f"Language Pair: {sample['lang_pair']}")
print(f"Target Language: {sample['target_lang']}")
print(f"Number of OCR segments: {len(sample['merge_ocr'])}")

# Access translation pairs
for segment in sample['merge_ocr'][:3]:
    print(f"Source: {segment['src_text']}")
    print(f"Target: {segment['tgt_text']}")
    print(f"Box: {segment['box']}")
    print(f"Source Lang: {segment['src_lang']}")
    print(f"Target Lang: {segment['tgt_lang']}")
```

## Data Format

Each entry in the MMDoc dataset follows this structure:

```json
{
  "image_id": "00",
  "lang_pair": "en-id",
  "target_lang": "id",
  "cls": "document",
  "ocr": [
    {
      "box": [x1, y1, x2, y2],
      "text": "extracted text"
    }
  ],
  "merge_ocr": [
    {
      "box": [127, 124, 823, 553],
      "src_text": "Propylene oxide at the levels tested...",
      "tgt_text": "Propilena oksida pada tingkat yang diuji...",
      "src_lang": "en",
      "tgt_lang": "id"
    }
  ],
  "image": <PIL.Image>
}
```

## Evaluation

MMDoc has been used to evaluate translation quality using multiple metrics:

* **BLEU**: N-gram overlap metrics
* **COMET**: Neural metric considering semantic similarity
* **ROUGE**: Recall-oriented evaluation (ROUGE-1, ROUGE-2, ROUGE-L)
* **BERTScore**: Contextual embedding-based semantic similarity
* **LLM-based judge**: Human-aligned quality assessments

TransMLLM, trained on MMDoc, achieves strong performance improvements over OCR-based pipelines and pre-trained VLMs, with particular gains on low-resource languages such as Uzbek and Kazakh.

## Citation

If you use MMDoc in your research, please cite:

```bibtex
@dataset{mmdoc_2025,
  title={MMDoc: Multilingual Multimodal Document Translation Dataset},
  author={Seonok Kim},
  year={2025},
  url={https://huggingface.co/datasets/rileykim/MMDoc},
  note={Multilingual Multimodal Document (MMDoc) translation dataset with OCR and multilingual translations. Extended from PATIMT-Bench (https://github.com/XMUDeepLIT/PATIMT-Bench) for multilingual document translation research.}
}
```

## License

This dataset is released under the Apache 2.0 License.

## Data Generation

MMDoc was created by extending PATIMT-Bench from English-Chinese pairs to 10 language pairs:

* **Test split**: Translations were generated using GPT-5.1
* **Train split**: Translations were generated using Google Translate via the deep-translator Python library

The translation process involved:

1. Using English-Chinese pairs from PATIMT-Bench as reference
2. Translating Chinese text to target languages using the specified translation services
3. Preserving document structure, OCR bounding boxes, and formatting

## Acknowledgments

* Part of the TransMLLM project
* Extended from PATIMT-Bench dataset
* Document images and OCR processing
* Multilingual translation annotations
* Test translations: GPT-5.1
* Train translations: Google Translate via deep-translator library

