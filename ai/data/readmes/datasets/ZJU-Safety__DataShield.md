---
pretty_name: "DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment"
language:
- en
- es
- ru
- de
- pl
- th
- vi
- sv
- bn
- da
- he
- it
- fa
- sk
- id
- nb
- el
- nl
- hu
- eu
- zh
- eo
- ja
- ca
- cs
- bg
- fi
- pt
- tr
- ro
- ar
- uk
- gl
- fr
- ko
license: other
task_categories:
- text-generation
tags:
- safety
- alignment
- instruction-tuning
- data-filtering
- risk-scoring
- emnlp
size_categories:
- 1M<n<10M
configs:
- config_name: Dolly
  default: true
  data_files:
  - split: train
    path: data/Dolly.jsonl
- config_name: Alpaca
  data_files:
  - split: train
    path: data/Alpaca.jsonl
- config_name: OASST1
  data_files:
  - split: train
    path: data/OASST1/*.jsonl.gz
- config_name: ShareGPT
  data_files:
  - split: train
    path: data/ShareGPT/*.jsonl.gz
- config_name: WizardLM
  data_files:
  - split: train
    path: data/WizardLM/*.jsonl.gz
- config_name: UltraChat
  data_files:
  - split: train
    path: data/UltraChat/*.jsonl.gz
---

<div align="center">

<h1>🛡️ DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment</h1>

[![EMNLP Main](https://img.shields.io/badge/EMNLP-Main-8A2BE2?style=flat-square)](https://arxiv.org/abs/2607.15081)
[![Paper](https://img.shields.io/badge/Paper-arXiv-B31B1B?style=flat-square)](https://arxiv.org/abs/2607.15081)
[![GitHub](https://img.shields.io/badge/GitHub-DataShield-181717?logo=github&style=flat-square)](https://github.com/ZJU-LLM-Safety/DataShield)
[![Low-Risk Data](https://img.shields.io/badge/Data-Low--Risk%20Ready-18A558?style=flat-square)](#available-datasets)

<h2>⚡ Find risky data before fine-tuning. ⚡</h2>

<p>
  We use <strong>DataShield</strong> to continuously release risk-scored versions of widely used fine-tuning datasets. Every release keeps the original training example together with one final <code>risk_score</code>, making it easy to remove the highest-risk portion before training.
</p>

<a href="#quick-start"><b>Quick Start</b></a> ·
<a href="#choose-a-filtering-ratio"><b>Choose a Ratio</b></a> ·
<a href="https://github.com/ZJU-LLM-Safety/DataShield"><b>Code</b></a> ·
<a href="https://arxiv.org/abs/2607.15081"><b>Paper</b></a>

<br><br>

<img src="assets/framework.png" width="900" alt="DataShield framework">

</div>

## ✨ Overview

Each record retains the original training fields and adds only the final DataShield `risk_score`. A higher score indicates greater estimated fine-tuning risk. The score is designed for ranking and filtering, not as a calibrated probability or binary safety label.

The hosted configurations use sample-level mean ensemble scores from four reviewer models.

<a id="available-datasets"></a>

## 📦 Available Datasets

| Configuration | Dataset | Rows | Status |
| :--- | :--- | ---: | :---: |
| `Dolly` | Dolly | 14,601 | ✅ |
| `Alpaca` | Alpaca | 45,774 | ✅ |
| `OASST1` | OASST1 | 51,816 | ✅ |
| `ShareGPT` | ShareGPT | 332,851 | ✅ |
| `WizardLM` | WizardLM | 69,999 | ✅ |
| `UltraChat` | UltraChat | 657,763 | ✅ |
| `OpenHermes` | OpenHermes 2.5 | 1,008,268 | ⏳ Scanning |
| `Tulu` | Tulu 3 SFT Mixture | 1,109,973 | ⏳ Scanning |

```python
from datasets import load_dataset

dataset = load_dataset("ZJU-Safety/DataShield", "UltraChat", split="train")
print(dataset[0]["risk_score"])
```

<a id="quick-start"></a>

## 🚀 Create a Low-Risk Dataset

Clone this dataset repository and install 🤗 Datasets:

```bash
git clone https://huggingface.co/datasets/ZJU-Safety/DataShield
cd DataShield
pip install -U datasets
```

Remove the highest-risk **20%** from Dolly:

```bash
python filter_by_risk.py \
  --config Dolly \
  --remove-ratio 0.20 \
  --output Dolly_low_risk_80.jsonl
```

Or create an Alpaca version with a different safety budget:

```bash
python filter_by_risk.py \
  --config Alpaca \
  --remove-ratio 0.10 \
  --output Alpaca_low_risk_90.jsonl
```

Load the filtered JSONL directly:

```python
from datasets import load_dataset

train_data = load_dataset(
    "json",
    data_files="Dolly_low_risk_80.jsonl",
    split="train",
)
```

You can also filter a downloaded or local JSON/JSONL file:

```bash
python filter_by_risk.py \
  --input my_scored_data.jsonl \
  --remove-ratio 0.20 \
  --output my_low_risk_data.jsonl
```

<a id="choose-a-filtering-ratio"></a>

## 🎚️ Choose a Filtering Ratio

We recommend **20%** as the default recipe for reproducing our released filtering experiments. We intentionally keep every scored example in the hosted configurations so that the filtering strength is not permanently fixed.

| Goal | Suggested starting point |
| :--- | :---: |
| Preserve as much training data as possible | remove top 5–10% |
| Balanced default / paper reproduction | **remove top 20%** |
| More conservative data selection | remove top 30% |

The script removes exactly the highest-ranked portion according to `risk_score` and preserves the original order of all retained examples. The best ratio may vary by dataset, target model, and downstream task, so it should be validated for both safety and utility.

## 🛡️ Intended Use

This dataset is intended for research on fine-tuning safety, reproducibility, and controlled safety evaluation. Some source examples may be safety-sensitive. Please preserve the source dataset licenses and usage conditions when redistributing derived data.

## 📖 Citation

```bibtex
@article{wu2026datashield,
  title={DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment},
  author={Wu, Zefeng and Qi, Weiwei and Chen, Jielong and Zheng, Tianhang and Hong, Di and Lu, Chaochao and He, Liang and Qin, Zhan and Ren, Kui},
  journal={arXiv preprint arXiv:2607.15081},
  year={2026}
}
```
