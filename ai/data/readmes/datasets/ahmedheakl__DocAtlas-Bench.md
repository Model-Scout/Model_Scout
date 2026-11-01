---
license: cc-by-4.0
task_categories:
- image-to-text
language:
- af
- am
- ar
- arz
- az
- azb
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
- mzn
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
tags:
- ocr
- multilingual
- document-understanding
- document-parsing
- benchmark
- doctags
pretty_name: DocAtlas-Bench
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---

# DocAtlas-Bench

<p align="center">
  <a href="https://arxiv.org/abs/2605.12623"><img src="https://img.shields.io/badge/arXiv-2605.12623-b31b1b.svg" alt="arXiv"></a>
  <a href="https://github.com/ahmedheakl/DocAtlas"><img src="https://img.shields.io/badge/GitHub-DocAtlas-black.svg" alt="GitHub"></a>
  <a href="https://huggingface.co/datasets/ahmedheakl/docatlas_instruct"><img src="https://img.shields.io/badge/🤗_Training_data-docatlas__instruct-yellow.svg" alt="Training data"></a>
  <a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg" alt="License"></a>
</p>

**DocAtlas-Bench** is the evaluation benchmark of [DocAtlas: Multilingual Document Understanding Across 80+ Languages](https://arxiv.org/abs/2605.12623). It contains the 5,575 difficulty-stratified page-level samples of the benchmark, covering 82 languages, with ground truth for end-to-end page parsing: text, tables, and reading order.

<p align="center">
  <img src="https://raw.githubusercontent.com/ahmedheakl/DocAtlas/main/assets/teaser.png" width="100%" alt="Overview of the DocAtlas framework">
</p>

## Benchmark

The benchmark balances diversity, difficulty, and representativeness. Pages are embedded with ResNet-50 features, clustered via FAISS, and stratified by difficulty into equal easy/medium/hard splits, yielding up to 100 pages per language across 82 languages (5,575 samples). In the paper, it is complemented by 144 curated formula samples and multilingual chart data across 15 languages, for 5,862 pages and 9 evaluation tasks in total.

This repository contains the 5,575 page-level samples; the formula and chart subsets are not part of it.

Ground truth comes from the DocAtlas annotation pipelines (differential rendering of native DOCX documents and LaTeX-based synthesis for right-to-left scripts), which produce structural annotations without learned models for core annotation. Pages are further annotated with page-level attributes such as document type, column layout, watermark presence, and background color, predicted via Qwen3-VL and confirmed by human inspection; these attributes enable controlled evaluations under specific visual or layout conditions.

## Dataset structure

A single `test` split with one row per page.

| Column | Type | Description |
|---|---|---|
| `id` | `string` | Unique page identifier. Predictions are matched to pages by this id. |
| `image` | `image` | Rendered page image. |
| `language` | `string` | ISO 639 language code of the page (e.g., `en`, `ar`, `zh`, `hi`), as in [docatlas_instruct](https://huggingface.co/datasets/ahmedheakl/docatlas_instruct). |
| `language_name` | `string` | Language name used in the evaluation ground truth (e.g., `english`, `arabic`). |
| `data_source` | `string` | Document type: `academic_literature`, `book`, `colorful_textbook`, `exam_paper`, `magazine`, `newspaper`, `note`, `research_report`, or `PPT2PDF`. |
| `markdown` | `string` | Page content in Markdown, with tables as HTML. Same format as in docatlas_instruct. |
| `doctags` | `string` | Page annotation in the [DocTag](https://arxiv.org/abs/2503.11576) format, with bounding boxes in image pixels. Same format as in docatlas_instruct; null for 225 pages. |
| `annotation` | `string` | JSON string with the page ground truth used by the evaluation code (see below). |

`DocAtlas-Bench.json` at the root of the repository holds the same ground truth as the `annotation` column, as one JSON list, and is the file the evaluation code reads.

### Ground-truth format

The ground truth follows the [OmniDocBench](https://github.com/opendatalab/OmniDocBench) annotation format:

```json
{
  "page_info": {
    "page_no": 10, "height": 2526, "width": 1786,
    "image_path": "images/<id>.jpg",
    "page_attribute": {"language": "english", "data_source": "book", "layout": "single_column", "special_issue": []}
  },
  "layout_dets": [
    {"category_type": "text_block", "poly": [x1, y1, x2, y1, x2, y2, x1, y2], "order": 0, "text": "...", "attribute": {"text_language": "text_english", "text_background": "white", "text_rotate": "normal"}},
    {"category_type": "table", "poly": [...], "order": 1, "html": "<table>...</table>", "attribute": {"with_span": false, "line": "wireless_line", "...": "..."}}
  ],
  "extra": {"relation": []}
}
```

Element types are `text_block`, `section_header`, and `table`. `poly` gives the four corners of the element in image pixels and `order` its position in the reading order.

## Usage

```python
import json
from datasets import load_dataset

bench = load_dataset("ahmedheakl/DocAtlas-Bench", split="test")

page = bench[0]
print(page["id"], page["language"], page["data_source"])
print(page["markdown"])                      # Markdown ground truth
elements = json.loads(page["annotation"])["layout_dets"]
page["image"].show()
```

## Evaluation

Following the paper, each model produces a Markdown output per page, which is evaluated with a three-stage pipeline: extraction (tables, formulas, and paragraphs), matching of predictions to ground truth using Normalized Edit Distance, and metric computation, with breakdowns by language, document type, and layout.

| Metric | Description |
|---|---|
| Text Edit ↓ | Normalized edit distance between predicted and ground-truth text. |
| Table TEDS ↑ | Tree-Edit-Distance-based Similarity between predicted and ground-truth tables, converted to HTML. |
| Read Order Edit ↓ | Edit distance between the predicted and ground-truth reading order. |
| Overall ↑ | Average of text and table scores, after converting text edit distance to accuracy. |

The evaluation code is available at [github.com/ahmedheakl/DocAtlas](https://github.com/ahmedheakl/DocAtlas/tree/main/eval):

```bash
git clone https://github.com/ahmedheakl/DocAtlas && cd DocAtlas/eval
pip install -r requirements.txt

python prepare_benchmark.py --out data                    # ground truth + page images
# write one predictions/<model>/<id>.md per page, then:
python run_eval.py --gt data/DocAtlas-Bench.json --pred predictions/<model> --out results
```

## Results

Quantitative comparison across OCR systems reported in the paper. Overall is the average of text and table scores, after converting text edit distance to accuracy.

| Type | Method | Params | Text Edit ↓ | Table TEDS ↑ | Formula Edit ↓ | Read Order Edit ↓ | Overall ↑ |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| General VLMs | Gemini-2.0-Pro | - | 0.090 | 68.50 | 0.356 | 0.050 | 79.75 |
| | GPT4o | - | 0.117 | 62.26 | 0.425 | 0.065 | 75.30 |
| | Qwen3-VL | 3B | 0.081 | 51.86 | 0.420 | 0.089 | 71.87 |
| | Qwen2.5-VL | 2B | 0.174 | 50.59 | 0.453 | 0.117 | 66.59 |
| | InternVL3.5 | 2B | 0.095 | 70.80 | 0.543 | 0.060 | 77.20 |
| Expert VLMs | DotsOCR | 3B | 0.068 | 65.40 | 0.321 | 0.037 | 79.29 |
| | PaddleOCR-VL | 1B | 0.078 | 73.90 | 0.241 | 0.052 | 80.10 |
| | DeepseekOCR | 3B | 0.082 | 71.54 | 0.242 | 0.053 | 81.66 |
| | MonkeyOCR-pro | 1.2B | 0.095 | 72.80 | 0.295 | 0.065 | 78.25 |
| | Dolphin | 400M | 0.160 | 58.30 | 0.465 | 0.066 | 71.17 |
| | Nanonets-OCR-s | 4B | 0.088 | 71.90 | 0.518 | 0.059 | 81.53 |
| | Nanonets-OCR2 | 3B | 0.088 | 66.24 | 0.471 | 0.060 | 78.70 |
| | Chandra | 9B | 0.071 | 69.79 | 0.262 | 0.042 | 81.33 |
| | MinerU2.5 | 1.2B | 0.267 | 72.79 | 0.273 | 0.096 | 73.07 |
| | **DocAtlas-Deepseek (Ours)** | 3B | 0.055 | 72.24 | 0.237 | 0.049 | 83.37 |

## Citation

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
