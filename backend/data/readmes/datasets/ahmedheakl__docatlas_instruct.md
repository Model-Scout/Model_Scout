---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: doctags
    dtype: string
  - name: markdown
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 72335490539
    num_examples: 180913
  download_size: 0
  dataset_size: 72335490539
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- af
- am
- ar
- az
- ba
- be
- bg
- bn
- bs
- ca
- ce
- ceb
- ckb
- cs
- cy
- da
- de
- dv
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- ko
- ku
- la
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- mt
- ne
- nl
- nn
- "no"
- oc
- pa
- pl
- pnb
- ps
- pt
- ro
- ru
- sd
- sh
- si
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- tg
- th
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vi
- zh
license: cc-by-4.0
task_categories:
- image-to-text
- document-question-answering
tags:
- ocr
- multilingual
- document-understanding
- document-parsing
- doctags
pretty_name: DocAtlas Instruct
size_categories:
- 100K<n<1M
---

# DocAtlas: Multilingual Document Understanding Across 80+ Languages

<p align="center">
  <a href="https://arxiv.org/abs/2605.12623"><img src="https://img.shields.io/badge/arXiv-2605.12623-b31b1b.svg" alt="arXiv"></a>
  <a href="https://github.com/ahmedheakl/DocAtlas"><img src="https://img.shields.io/badge/GitHub-DocAtlas-black.svg" alt="GitHub"></a>
  <a href="https://huggingface.co/datasets/ahmedheakl/docatlas_instruct"><img src="https://img.shields.io/badge/🤗_HuggingFace-Dataset-yellow.svg" alt="HuggingFace"></a>
  <a href="https://huggingface.co/datasets/ahmedheakl/DocAtlas-Bench"><img src="https://img.shields.io/badge/🤗_Benchmark-DocAtlas--Bench-yellow.svg" alt="Benchmark"></a>
  <a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg" alt="License"></a>
</p>

**DocAtlas** is a large-scale, high-fidelity multilingual OCR dataset covering **82 languages** and **10 writing systems**, built through model-free differential rendering. It provides precise structural annotations in a unified **DocTag** format encoding layout, text, and component types — without relying on any learned models for core annotation.

This dataset powers the training of **DocAtlas-DeepSeek**, which achieves the best overall score (83.37%) among the 14 state-of-the-art models evaluated in the paper, improving +1.7% over the strongest baseline.


## Key Features

- **82 languages** across 10 writing systems (Latin, Cyrillic, Arabic, Devanagari, Chinese, Hangeul, Greek, Abugidas, Syllabaries, Abjads)
- **180,913 training pages** with model-free structural annotations
- **Dual annotation pipelines:** differential rendering of native DOCX documents + synthetic LaTeX-based generation for RTL scripts
- **Unified DocTag format** jointly encoding component type, geometry, and text content
- **31 structural element types** spanning text, tables, headings, figures, equations, charts, and more
- **25+ content domains** including Health, Law, Finance, Science, and Education
- **DPO-ready:** rendering-derived ground truth serves as positive signal for Direct Preference Optimization, achieving stable cross-lingual transfer (+1.9% in-domain, +1.8% out-of-domain) without base-language degradation

## Dataset Columns

| Column | Type | Description |
|---|---|---|
| `id` | `string` | Unique identifier for each page sample. |
| `image` | `image` | Rendered page image (the document page as seen by the model). |
| `doctags` | `string` | Structural annotation in the [DocTag](https://arxiv.org/abs/2503.11576) format — an XML-like schema encoding component types (e.g., `<text>`, `<table>`, `<section_header>`), bounding-box geometry, and text content for each element on the page. |
| `markdown` | `string` | Full page content converted to Markdown, preserving headings, tables, lists, and inline formatting. Suitable for end-to-end page-to-Markdown training and evaluation. |
| `language` | `string` | ISO 639-1 language code (e.g., `en`, `ar`, `zh`, `hi`) identifying the primary language of the document page. |

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("ahmedheakl/docatlas_instruct", split="train")

# Access a sample
sample = dataset[0]
print(sample["language"])   # e.g., "en"
print(sample["markdown"])   # Markdown content of the page
print(sample["doctags"])    # DocTag structural annotation
sample["image"].show()      # Display the page image
```

### Streaming (recommended for large-scale loading)

```python
from datasets import load_dataset

dataset = load_dataset("ahmedheakl/docatlas_instruct", split="train", streaming=True)

for sample in dataset:
    print(sample["id"], sample["language"])
    break
```

## Script & Language Coverage

The dataset spans 10 writing systems with broad typological diversity:

| Writing System | Example Languages |
|---|---|
| Latin | English, French, Spanish, Polish, Vietnamese, ... |
| Cyrillic | Russian, Ukrainian, Serbian, Bulgarian, ... |
| Arabic | Arabic, Persian, Urdu, Kurdish, ... |
| Devanagari | Hindi, Marathi, Nepali, ... |
| Chinese | Chinese |
| Hangeul | Korean |
| Greek | Greek |
| Abugidas | Thai, Khmer, Tamil, Bengali, Sinhala, ... |
| Syllabaries | Japanese, Amharic, ... |
| Abjads | Hebrew |

## Benchmark and Code

- **Benchmark:** [ahmedheakl/DocAtlas-Bench](https://huggingface.co/datasets/ahmedheakl/DocAtlas-Bench), the multilingual evaluation benchmark of the paper.
- **Evaluation code:** [github.com/ahmedheakl/DocAtlas](https://github.com/ahmedheakl/DocAtlas).

Data generation and training code will be released soon.

## Citation

If you use DocAtlas in your research, please cite our paper:

```bibtex
@article{heakl2026docatlas,
  title={DocAtlas: Multilingual Document Understanding Across 80+ Languages},
  author={Heakl, Ahmed and Mohamed, Youssef and Sohail, Abdullah and Elbadry, Rania and Nassar, Ahmed and Staar, Peter WJ and Khan, Fahad Shahbaz and Razzak, Imran and Khan, Salman},
  journal={arXiv preprint arXiv:2605.12623},
  year={2026}
}
```

## License

This dataset is released under the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. All source documents were collected from publicly accessible web content and academic repositories under permissive licenses, with automated PII detection applied to remove sensitive content.
