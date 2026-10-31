---
license: cc-by-sa-4.0
language:
  - ko
task_categories:
- token-classification
---

# Dataset Card for NTX v1 in the Aya format - Korean subset

This dataset is a format conversion for the Korean data from the original NTX into the Aya instruction format and it's released here under the CC-BY-SA 4.0 license.

## Dataset Details

For the original NTX dataset, the conversion to the Aya instructions format, or more details, please refer to the full dataset in instruction form (https://huggingface.co/datasets/tellarin-ai/ntx_llm_instructions) or to the paper below.

**NOTE: ** Unfortunately, due to a conversion issue with numerical expressions, this version here only includes the temporal expressions part of NTX. 

## Citation

If you utilize this dataset version, feel free to cite/footnote the complete version at https://huggingface.co/datasets/tellarin-ai/ntx_llm_instructions, but please also cite the *original dataset publication*.

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
