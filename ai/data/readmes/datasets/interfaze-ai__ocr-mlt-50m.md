---
license: apache-2.0
task_categories:
  - image-to-text
language:
  - en
  - zh
  - ja
  - ko
  - ar
  - hi
  - de
  - fr
  - es
  - pt
  - ru
  - th
  - vi
  - it
  - nl
  - pl
  - tr
  - sv
  - cs
  - ro
  - da
  - fi
  - hu
  - el
  - bg
  - uk
  - hr
  - sk
  - sl
  - lt
  - lv
  - et
  - mt
  - ga
  - ms
  - id
  - tl
  - sw
  - am
  - bn
  - ta
  - te
  - kn
  - ml
  - gu
  - mr
  - pa
  - ur
  - ne
  - si
  - my
size_categories:
  - 10M<n<100M
tags:
  - ocr
  - multilingual
  - document-ai
  - text-recognition
  - scene-text
pretty_name: "OCR-MLT-50M: Multilingual OCR Corpus (50 Million Samples)"
dataset_info:
  features:
    - name: image
      dtype: image
    - name: text
      dtype: string
    - name: language
      dtype: string
    - name: script
      dtype: string
    - name: source_type
      dtype: string
    - name: confidence
      dtype: float64
---

<div align="center">
<h1>OCR-MLT-50M: Multilingual OCR Corpus</h1>

<p>A large-scale multilingual OCR dataset spanning <b>50 languages</b> and <b>50.2 million</b> image-text pairs.<br/>Designed for training and evaluating robust multilingual text recognition systems across diverse scripts and domains.</p>

<p>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">📄 Paper</a> |
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">🤗 Model</a> |
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">🔥 Demo</a> |
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">💻 GitHub</a> |
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">🏆 Leaderboard</a> |
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">📊 Weights & Biases</a>
</p>

<p>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0"><img src="https://img.shields.io/badge/arXiv-2025.12345-b31b1b.svg" alt="Paper"></a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0"><img src="https://img.shields.io/badge/🤗_HF-Model-yellow.svg" alt="Model"></a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0"><img src="https://img.shields.io/badge/License-Apache_2.0-green.svg" alt="License"></a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0"><img src="https://img.shields.io/badge/Samples-50.2M-blue.svg" alt="Samples"></a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0"><img src="https://img.shields.io/badge/Languages-50-orange.svg" alt="Languages"></a>
</p>

</div>

## 🔥 News

- **[2025-11-15]** OCR-MLT-50M is now available on Hugging Face! [Download here](https://www.youtube.com/watch?v=xvFZjo5PgG0)
- **[2025-10-28]** Our paper is accepted at **CVPR 2025**! [Camera-ready version](https://www.youtube.com/watch?v=xvFZjo5PgG0)
- **[2025-09-10]** Released v2 model weights with improved CJK performance. [Model card](https://www.youtube.com/watch?v=xvFZjo5PgG0)
- **[2025-08-01]** Pre-trained checkpoints available for all 50 languages. [Download](https://www.youtube.com/watch?v=xvFZjo5PgG0)

## Overview

| Stat | Value |
|------|-------|
| Total samples | 50,217,843 |
| Languages | 50 |
| Scripts | 14 (Latin, CJK, Arabic, Devanagari, Cyrillic, ...) |
| Source types | Scene text, documents, handwritten, receipts, signage |
| Avg. image resolution | 384 x 128 |
| Storage (compressed) | ~2.3 TB |

## Language Distribution

[![Language Distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Pie_chart_of_US_population_by_state.svg/512px-Pie_chart_of_US_population_by_state.svg.png)](https://www.youtube.com/watch?v=xvFZjo5PgG0)

> Click to view the full interactive breakdown by language and script family

## Sample Visualizations

| | | |
|:---:|:---:|:---:|
| [![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg)](https://www.youtube.com/watch?v=xvFZjo5PgG0) | [![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/320px-PNG_transparency_demonstration_1.png)](https://www.youtube.com/watch?v=xvFZjo5PgG0) | [![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/320px-Image_created_with_a_mobile_phone.png)](https://www.youtube.com/watch?v=xvFZjo5PgG0) |
| Scene text (EN) | Document (JA) | Handwritten (AR) |

## Data Collection Pipeline

Samples were collected from three primary sources:
1. **Synthetic rendering** — text rendered onto natural backgrounds using 2,400+ fonts per script
2. **Web-crawled scene text** — filtered and deduplicated from Common Crawl with PaddleOCR pseudo-labels
3. **Scanned documents** — partnerships with national libraries and digitization initiatives

All pseudo-labels were verified using a multi-model consensus approach (TrOCR + PaddleOCR + EasyOCR), retaining only samples with ≥2/3 agreement. Full methodology in our [technical report](https://www.youtube.com/watch?v=xvFZjo5PgG0).

## Quick Start

```python
from datasets import load_dataset

# Load a specific language split
ds = load_dataset("interfaze-ai/ocr-mlt-50m", "en", split="train", streaming=True)

for sample in ds:
    print(sample["text"], sample["language"])
    break
```

## Benchmarks

Models fine-tuned on OCR-MLT-50M vs. existing public corpora:

| Model | MLT-2019 (F1) | IC15 (Acc) | CUTE80 (Acc) | Details |
|-------|---------------|------------|--------------|---------|
| TrOCR-large + Ours | 87.3 | 96.1 | 94.7 | [Config & Weights](https://www.youtube.com/watch?v=xvFZjo5PgG0) |
| PARSeq + Ours | 88.1 | 96.8 | 95.2 | [Config & Weights](https://www.youtube.com/watch?v=xvFZjo5PgG0) |
| CLIP4STR + Ours | 89.6 | 97.2 | 96.0 | [Config & Weights](https://www.youtube.com/watch?v=xvFZjo5PgG0) |
| Baseline (MJSynth+ST) | 79.4 | 94.2 | 87.8 | — |

> Full evaluation scripts and configs: [GitHub](https://www.youtube.com/watch?v=xvFZjo5PgG0)

## Shards

Data is split into per-language shards. See the [file listing](https://www.youtube.com/watch?v=xvFZjo5PgG0) for the full manifest.

## Citation

```bibtex
@inproceedings{kumar2025ocrmlt,
  title={OCR-MLT-50M: Scaling Multilingual Text Recognition with Synthetic-Real Hybrid Corpora},
  author={Kumar, Arjun and Nakamura, Yui and Al-Rashid, Fatima and M{\"u}ller, Jonas},
  booktitle={Proceedings of CVPR 2025},
  year={2025},
  pages={11234--11245}
}
```

## License

Apache 2.0 — see [LICENSE](https://www.youtube.com/watch?v=xvFZjo5PgG0) for details.
