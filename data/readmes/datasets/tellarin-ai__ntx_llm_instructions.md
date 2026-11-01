---
license: cc-by-sa-4.0
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - nl
  - pt
  - sv
  - tr
  - zh
task_categories:
- token-classification
---

# Dataset Card for NTX v1 in the Aya format

This dataset is a format conversion from its original v1 format into the Aya instruction format and it's released here under the CC-BY-SA 4.0 license and conditions.

It contains data in multiple languages and this version is intended for multi-lingual LLM construction/tuning.

## Citation

If you utilize this dataset version, feel free to cite/footnote this huggingface dataset repo, but please also cite the original dataset publication.

**BibTeX:**

```
@preprint{chen2023dataset,
  title={Dataset and Baseline System for Multi-lingual Extraction and Normalization of Temporal and Numerical Expressions}, 
  author={Sanxing Chen and Yongqiang Chen and Börje F. Karlsson},
  year={2023},
  eprint={2303.18103},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

## Dataset Details

For the original NTX dataset for information extraction of numerical and temporal expressions and more details, please check the arXiv paper: https://arxiv.org/abs/2303.18103.

**NOTE: ** Unfortunately, due to a conversion issue with numerical expressions, this version here only includes the temporal expressions part of NTX. 

## Format Conversion Details

The templates used to reformat the dataset are in the ./templates-ntx directory.