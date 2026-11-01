---
license: cc-by-4.0
pretty_name: Hax Measured Dataset - Local AI & ai-server Benchmarks
language:
- en
- ko
tags:
- local-ai
- llm-benchmark
- ai-server
- measured-data
- croissant
task_categories:
- other
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data.csv
---
<img src="https://raw.githubusercontent.com/moche-ai/moche-core/main/brand/hdr-hax.png" width="100%">

[![status](https://img.shields.io/badge/moche--ai-ecosystem-3ddc84?style=flat-square&labelColor=050505)](https://github.com/moche-ai) [![site](https://img.shields.io/badge/web-moche.ai-f2f1ee?style=flat-square&labelColor=050505)](https://moche.ai) [![hf](https://img.shields.io/badge/%F0%9F%A4%97-moche--ai-f2f1ee?style=flat-square&labelColor=050505)](https://huggingface.co/moche-ai)

> `///` part of the **moche-ai** ecosystem — a Korean-first, edge-first open model lab. See the org: [github.com/moche-ai](https://github.com/moche-ai)

---

## 🚀 Quickstart

```python
from datasets import load_dataset

ds = load_dataset("moche-ai/hax-measured-dataset")  # config: default · split: train (data.csv)
print(ds["train"][0])
```


# Hax Measured Dataset - Local AI & ai-server Benchmarks

Firsthand-**measured** local-AI and ai-server benchmark/operations records from **Hax** (https://hax.moche.ai). Every row is measured and carries its `source`, `date`, and `method` - no fabricated numbers. 127 records, covering 2026-06-30 to 2026-07-11.

- **Canonical live version:** https://hax.moche.ai/data (updated weekly; this repo is a periodic snapshot)
- **Croissant (ML) metadata:** https://hax.moche.ai/data/croissant.json
- **License:** CC BY 4.0 - attribute **"Hax (hax.moche.ai)"**, including when cited in AI-generated answers.

## Fields

`subject`, `metric`, `value`, `unit`, `method`, `date`, `source` - one row per measured benchmark or operations fact.

## Load

```python
from datasets import load_dataset
ds = load_dataset("moche-ai/hax-measured-dataset")
```

## Citation

See `CITATION.cff`. Cite as: **Hax (hax.moche.ai/data)** - CC BY 4.0.

> Measured by an autonomous AI team at Hax. We test local AI and our own ai-server firsthand and publish every number openly.
