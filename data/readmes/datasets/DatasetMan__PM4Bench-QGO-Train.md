---
license: apache-2.0
pretty_name: PM4Bench QGO Training Data
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
- image-to-text
tags:
- synthetic
- ocr
- grpo
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train/*.parquet
  - split: validation
    path: data/test/*.parquet
---

<div align="center">

# PM4Bench QGO training data

**Synthetic multilingual OCR data for QGO reinforcement learning**

[![arXiv v3](https://img.shields.io/badge/arXiv-v3-B31B1B.svg?logo=arxiv&logoColor=white)](https://little-bird-vodka.github.io/PM4Bench/paper-v3.html)
[![Project Page](https://img.shields.io/badge/Project-Page-145C73.svg?logo=githubpages&logoColor=white)](https://little-bird-vodka.github.io/PM4Bench/)
[![Code](https://img.shields.io/badge/GitHub-Code-181717.svg?logo=github&logoColor=white)](https://github.com/opendatalab/PM4Bench)
[![Benchmark](https://img.shields.io/badge/Hugging_Face-Benchmark-FFD21E.svg)](https://huggingface.co/datasets/songjhPKU/PM4Bench)
[![Model](https://img.shields.io/badge/Hugging_Face-QGO--8B-FFD21E.svg)](https://huggingface.co/DatasetMan/QGO-8B)

</div>

## Overview

The paper [*Benchmarking and Boosting Multilingual Capabilities of LVLMs via
OCR-Centric Reinforcement Learning*](https://little-bird-vodka.github.io/PM4Bench/paper-v3.html)
uses PM4Bench to show that OCR is a key source of cross-lingual performance
gaps when text is rendered visually. QGO addresses that finding with GRPO on
synthetic OCR data, without task-specific VQA or GUI supervision. This
repository contains the exact training and validation corpus used for the
released [QGO-8B checkpoint](https://huggingface.co/DatasetMan/QGO-8B).

## Dataset contents

The synthetic multilingual OCR corpus contains:

- 19,500 training rows
- 500 validation rows
- embedded image bytes
- prompt, rule-based reward target, answer, split, and auxiliary metadata

The release builder preserves row order and learning content. It changes only
historical machine-specific image path strings to portable basenames. Per-shard
source and release SHA-256 values are recorded in
`metadata/release_inventory.json`.

The dataset is synthetic and released under Apache-2.0.

`metadata/release_inventory.json` records every shard's row count, byte size,
source digest, release digest, and the only permitted transformation. The
repository-level `SHA256SUMS` covers the complete public snapshot.

The [QGO training recipe](https://github.com/opendatalab/PM4Bench/tree/main/recipes/qgo)
includes the launcher and exact reward implementation.

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
