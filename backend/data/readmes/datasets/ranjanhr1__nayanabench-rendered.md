---
language:
- en
- hi
- kn
- ta
- te
- mr
- pa
- bn
- or
- ml
- gu
- sa
- ja
- ko
- zh
- de
- fr
- it
- ru
- ar
- es
- th
multilinguality: multilingual
task_categories:
- image-to-text
- object-detection
pretty_name: NayanaBench Rendered Dataset
size_categories:
- 1K<n<10K
tags:
- ocr
- text-rendering
- multilingual
- document-analysis
---

# NayanaBench Rendered Dataset

## Dataset Description

This dataset contains 2D rendered text images for document analysis and OCR tasks across 22 languages.
Each language split contains document images with text rendered in bounding boxes using authentic fonts.

### Dataset Statistics

- **Total Samples**: 4,400
- **Languages**: 22
- **Splits**: 22 language-based splits

### Language Splits

| Language | Code | Samples |
|----------|------|---------|
| EN | `en` | 200 |
| HI | `hi` | 200 |
| KN | `kn` | 200 |
| TA | `ta` | 200 |
| TE | `te` | 200 |
| MR | `mr` | 200 |
| PA | `pa` | 200 |
| BN | `bn` | 200 |
| OR | `or` | 200 |
| ML | `ml` | 200 |
| GU | `gu` | 200 |
| SA | `sa` | 200 |
| JA | `ja` | 200 |
| KO | `ko` | 200 |
| ZH | `zh` | 200 |
| DE | `de` | 200 |
| FR | `fr` | 200 |
| IT | `it` | 200 |
| RU | `ru` | 200 |
| AR | `ar` | 200 |
| ES | `es` | 200 |
| TH | `th` | 200 |

## Dataset Structure

### Data Fields

- `image`: The rendered document image
- `image_id`: Unique identifier for the sample
- `language`: Language code (ISO 639-1)
- `font_used`: Font file used for rendering
- `num_regions`: Number of text regions in the image
- `regions`: JSON string containing region metadata (bounding boxes, text content)

### Data Splits

This dataset has 22 splits, one per language. Each split can be loaded separately:

```python
from datasets import load_dataset

# Load a specific language
dataset = load_dataset("ranjanhr1/nayana_rendered", split="en")

# Load multiple languages
dataset_dict = load_dataset("ranjanhr1/nayana_rendered")

# Load specific languages
en_data = load_dataset("ranjanhr1/nayana_rendered", split="en")
hi_data = load_dataset("ranjanhr1/nayana_rendered", split="hi")
```

## Dataset Creation

This dataset was created by rendering text onto document images using authentic fonts for each language.
The rendering process uses:
- Tight canvas rendering (exact bounding box size)
- Optimal font size calculation
- Multi-line text wrapping
- Centered text alignment

### Source Dataset

Based on [Nayana-cognitivelab/NayanaBench](https://huggingface.co/datasets/Nayana-cognitivelab/NayanaBench)

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{nayana_rendered,
  title={NayanaBench Rendered Dataset},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/ranjanhr1/nayana_rendered}
}
```

## License

Please refer to the original NayanaBench dataset for licensing information.
