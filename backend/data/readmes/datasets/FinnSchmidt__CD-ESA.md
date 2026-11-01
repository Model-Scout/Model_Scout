---
language:
- en
- de
- ko
- zh
pretty_name: CD-ESA
license: cc-by-nc-4.0
tags:
- machine-translation
- mt-evaluation
- quality-estimation
- error-span-annotation
- WMT
- datasets
task_categories:
- translation
---


# CD-ESA: Cross-Domain Error Span Annotation Dataset

This dataset contains the publicly releasable WMT23 and Emea portions of CD-ESA (Cross-Domain Error Span Annotation), introduced in our work “Who Watches the Watchmen? Humans Disagree With Translation Metrics on Unseen Domains”. CD-ESA was created to study how well reference-free machine translation evaluation metrics, i.e. quality estimation (QE) metrics, generalize to unseen domains. The release comprises **4,728 translation rows** and **11,454 human ESA annotations** across English–German, English–Korean, and English–Chinese.

The main goal of CD-ESA is to evaluate QE metrics under domain shift while comparing metric–human agreement against inter-annotator agreement. 
Raw metric–human agreement can be misleading when human-human agreement differs across domains. For example, when translations in one domain are close in quality, both metric–human and human–human agreement may be lower simply because the ranking task is harder.

CD-ESA enables comparison of QE metrics across seen and unseen domains relative to human agreement, rather than relying on raw metric–human agreement alone. It provides human Error Span Annotations (ESA; Kocmi et al., 2024) for translations from the same six MT systems across WMT23 and Emea. Each source sentence is translated by the same systems and evaluated by the same human annotators, making the dataset suitable for computing standard meta-evaluation metrics such as accuracy with tie calibration and soft pairwise accuracy from the latest WMT Metrics shared tasks.

 


## Dataset structure

The JSONL file has one row per translation.

Each row contains the following top-level fields:

- `src`: source sentence
- `tgt`: machine translation
- `system`: MT system that produced the translation
- `lp`: language pair
- `domain`: source domain (`wmt` or `emea`)
- `ESA_scores`: human ESA scores
- `annotations`: human error-span annotations

The `ESA_scores` and `annotations` fields store multiple human annotations for each translation. Both fields are dictionaries where annotator IDs (`humanA`, `humanB`, etc.) are the keys. `ESA_scores` contains the corresponding ESA scores, while `annotations` contains the error spans following the ESA protocol (Kocmi et al., 2024).

## Python usage

You can load the dataset directly from Hugging Face:

```python
from datasets import load_dataset

dataset = load_dataset("FinnSchmidt/CD-ESA", split="train")
```

You can filter the dataset by language pair or domain:

```python
# English-German only
ende = dataset.filter(lambda x: x["lp"] == "en-de")

# English-Korean only
enko = dataset.filter(lambda x: x["lp"] == "en-ko")

# English-Chinese only
enzh = dataset.filter(lambda x: x["lp"] == "en-zh")

# WMT23 only
wmt = dataset.filter(lambda x: x["domain"] == "wmt")

# Emea only
emea = dataset.filter(lambda x: x["domain"] == "emea")
```

Alternatively, if you downloaded the JSONL file locally:

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="cd_esa_wmt_emea.jsonl", split="train")
```
## Citation

## Citation Information

If you use this data, please cite the following works:

- [Who Watches the Watchmen? Humans Disagree With Translation Metrics on Unseen Domains](https://arxiv.org/abs/2604.17393), Schmidt et al. (2026)
- [Error Span Annotation: A Balanced Approach for Human Evaluation of Machine Translation](https://aclanthology.org/2024.wmt-1.131/), Kocmi et al. (2024)

---
license: cc-by-nc-4.0
---
