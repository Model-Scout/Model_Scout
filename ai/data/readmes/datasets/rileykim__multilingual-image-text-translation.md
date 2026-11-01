---
license: mit
task_categories:
- text-to-image
- image-to-text
- translation
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
- zh
tags:
- multimodal
- translation
- multilingual
- vision
- flores200
- mmt
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: language
    dtype: string
  - name: language_name
    dtype: string
  - name: iso3_code
    dtype: string
  - name: script
    dtype: string
  - name: flores_code
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: test
    num_bytes: 35076589.6
    num_examples: 1100
  download_size: 34742232
  dataset_size: 35076589.6
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---

# Multilingual Image-Text Translation Dataset (MMT)

## Overview

This dataset contains **Multilingual Multimodal Translation (MMT)** pairs from FLORES-200, featuring image-text combinations across 11 languages. The dataset is designed for training and evaluating multimodal translation models that can translate text while considering visual context.

## MMT (Multilingual Multimodal Translation)
- **M**ultilingual: 11 languages (en, id, ja, kk, ko, ru, ur, uz, vi, zh-cn, zh-tw)
- **M**ultimodal: Image + Text pairs
- **T**ranslation: Cross-lingual translation tasks

## Dataset Structure

Each sample contains:
- `id`: Unique identifier (e.g., "en_0001")
- `text`: Source text in original language
- `language`: Language code (ISO 639-1)
- `language_name`: Full language name
- `iso3_code`: ISO 639-3 language code
- `script`: Writing system used
- `flores_code`: FLORES-200 language code
- `image`: Corresponding 512x512 PNG image
- `image_filename`: Original image filename

## Languages

| Language | Code | Script | FLORES Code |
|----------|------|--------|-------------|
| English | en | latin | eng_Latn |
| Indonesian | id | latin | ind_Latn |
| Japanese | ja | mixed | jpn_Jpan |
| Kazakh | kk | cyrillic | kaz_Cyrl |
| Korean | ko | hangul | kor_Hang |
| Russian | ru | cyrillic | rus_Cyrl |
| Urdu | ur | arabic | urd_Arab |
| Uzbek | uz | latin | uzn_Latn |
| Vietnamese | vi | latin | vie_Latn |
| Chinese (Simplified) | zh-cn | han | zho_Hans |
| Chinese (Traditional) | zh-tw | han | zho_Hant |

## Usage

This dataset is perfect for:
- Training Multilingual Multimodal Translation models
- Cross-lingual visual question answering
- Multimodal machine translation research
- Visual language understanding tasks

### Example Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("rileykim/multilingual-image-text-translation")

# Access a sample
sample = dataset['train'][0]
print(f"Text: {sample['text']}")
print(f"Language: {sample['language']}")
print(f"Image shape: {sample['image'].size}")
```

## Dataset Statistics

- **Total samples**: ~1,100 (100 per language)
- **Languages**: 11
- **Image resolution**: 512x512 pixels
- **Format**: PNG images with JSON metadata

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{multilingual_image_text_translation_2025,
  title={Multilingual Image-Text Translation Dataset (MMT)},
  author={Riley Kim},
  year={2025},
  url={https://huggingface.co/datasets/rileykim/multilingual-image-text-translation},
  note={Based on FLORES-200 dataset}
}
```

## License

This dataset is released under the MIT License.

## Acknowledgments

- Based on the FLORES-200 dataset
- Images generated using multimodal text-to-image models
- Part of the TransMLLM project
