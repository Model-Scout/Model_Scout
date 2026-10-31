---
license:
- apache-2.0
- cc-by-nc-4.0
pretty_name: PM4Bench
language:
- ar
- cs
- en
- hu
- ko
- ru
- sr
- th
- vi
- zh
task_categories:
- visual-question-answering
- image-to-text
tags:
- multilingual
- vision-language
- ocr
- gui-grounding
size_categories:
- 10K<n<100K
source_datasets:
- MMMU/MMMU_Pro
- laolao77/MMDU
configs:
- config_name: mdur
  data_files:
  - split: test
    path: data/mdur/*.jsonl
- config_name: miqa
  data_files:
  - split: test
    path: data/miqa/*.jsonl
- config_name: msocr
  data_files:
  - split: test
    path: data/msocr/*.jsonl
- config_name: mgui
  data_files:
  - split: test
    path: data/mgui/*.jsonl
---

<div align="center">

# PM4Bench

**Strictly parallel multilingual evaluation for Large Vision-Language Models**

[![arXiv v3](https://img.shields.io/badge/arXiv-v3-B31B1B.svg?logo=arxiv&logoColor=white)](https://little-bird-vodka.github.io/PM4Bench/paper-v3.html)
[![Project Page](https://img.shields.io/badge/Project-Page-145C73.svg?logo=githubpages&logoColor=white)](https://little-bird-vodka.github.io/PM4Bench/)
[![Code](https://img.shields.io/badge/GitHub-Code-181717.svg?logo=github&logoColor=white)](https://github.com/opendatalab/PM4Bench)
[![Training Data](https://img.shields.io/badge/Hugging_Face-QGO_Train-FFD21E.svg)](https://huggingface.co/datasets/DatasetMan/PM4Bench-QGO-Train)
[![Model](https://img.shields.io/badge/Hugging_Face-QGO--8B-FFD21E.svg)](https://huggingface.co/DatasetMan/QGO-8B)

</div>

## Overview

The paper [*Benchmarking and Boosting Multilingual Capabilities of LVLMs via
OCR-Centric Reinforcement Learning*](https://little-bird-vodka.github.io/PM4Bench/paper-v3.html)
introduces PM4Bench to separate language effects from dataset variation. Its
content is strictly parallel across ten languages, and its `vision` setting
renders textual inputs directly into images. Comparing that setting with
interleaved input identifies OCR as a key source of cross-lingual performance
gaps and motivates the QGO training method linked above.

This repository contains the PM4Bench evaluation data spanning MDUR, MIQA,
MSOCR, and MGUI. Version 2 stores each image once and references it from
portable JSONL manifests; the legacy TSV/base64 format is retired.

## Components

| Component | Records per language | Settings | Provenance/license |
|---|---:|---|---|
| MDUR | 1,730 | traditional, vision | Derived from [MMMU-Pro](https://huggingface.co/datasets/MMMU/MMMU_Pro) (Apache-2.0) |
| MIQA | 218 | traditional, vision | Derived from [MMDU](https://huggingface.co/datasets/laolao77/MMDU) (CC BY-NC 4.0) |
| MSOCR | 100 | vision | PM4Bench-generated, Apache-2.0 |
| MGUI | 200 | vision | PM4Bench-generated, Apache-2.0 |

The repository-level Apache-2.0 declaration applies to PM4Bench-owned
metadata, translations, renderings, templates, and annotations. MMMU-Pro
content in MDUR remains under Apache-2.0. MMDU-derived content in MIQA remains
under CC BY-NC 4.0. Upstream components retain their attribution and
applicable terms; see `UPSTREAM_LICENSES.md` and the upstream dataset cards for
their complete notices.

## Formats and integrity

The dataset contains 40 UTF-8 JSONL manifests and portable relative asset
paths. It contains no TSV or embedded-base64 table. `metadata/release_inventory.json`
records the language/task counts, and `SHA256SUMS` authenticates released files.

## Loading

Use `snapshot_download` to retain relative asset paths, then read the selected
JSONL files. The `pm4bench` toolkit validates paths and provides metrics.

```python
from huggingface_hub import snapshot_download

root = snapshot_download(repo_id="songjhPKU/PM4Bench", repo_type="dataset")
```

The [PM4Bench codebase](https://github.com/opendatalab/PM4Bench) provides
schemas, validation, evaluation, construction tools, and the QGO recipe.

## MGUI construction note

The released MGUI images and GT are canonical. They were produced with Jinja2
3.1.6, Selenium 4.40.0, and Chrome for Testing 119.0.6045.105. A historical
Jinja autoescaping interaction caused CSS font-family declarations to fall
back to platform fonts, so fresh rendering on another OS can change bounding
boxes. The toolkit's `structure` comparison verifies all 1,000 pages, DOM
targets, visible text, questions, and metadata without replacing canonical
geometry; `strict` mode additionally audits bbox drift.

## Cite Us

<pre><code class="language-bibtex">
@misc{gao2026benchmarkingboostingmultilingualcapabilities,
      title={Benchmarking and Boosting Multilingual Capabilities of LVLMs via OCR-Centric Reinforcement Learning},
      author={Junyuan Gao and Jiahe Song and Jiang Wu and Runchuan Zhu and Guanlin Shen and Shasha Wang and Xingjian Wei and Haote Yang and Weijia Li and Bin Wang and Lijun Wu and Conghui He},
      year={2026},
      eprint={2503&#46;18484},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv&#46;org/abs/2503&#46;18484v3},
}
</code></pre>
