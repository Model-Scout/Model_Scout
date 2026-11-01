---
license: apache-2.0
task_categories:
- text-generation
language:
- en
- de
- es
- ar
- ja
- ko
- th
- bn
- sw
- te
---

# Dataset Card for multilingual_reasoning_gap_outputs

[**Paper**](https://huggingface.co/papers/2510.27269) | [**Code**](https://github.com/deokhk/RLM_analysis)

## Dataset Details

### Dataset Description

This dataset contains experiment outputs for **Qwen3-4B** used in our study on multilingual reasoning gaps.

It includes:
- **Prober checkpoints** trained for understanding-failure analysis
- **Intermediate results**, such as:
  - Model inference outputs
  - Signals for understanding failure detection
  - Auxiliary artifacts used for probing and analysis

The dataset is released to support transparency, reproducibility, and further analysis of multilingual reasoning behaviors in reasoning language models.

- **Curated by:** Deokhyung Kang et al.
- **Language(s) (NLP):** en, de, es, ar, ja, ko, th, bn, sw, te
- **License:** Apache-2.0

### Dataset Sources

The experiment outputs are derived from evaluations on the following datasets:
- **MMLU-ProX-Lite**
- **Polymath**

## Usage

You can download the files using the following example provided in the official repository:

```python
from huggingface_hub import snapshot_download

repo_id = "deokhk/multilingual_reasoning_gap_outputs"

snapshot_download(
    repo_id=repo_id,
    repo_type="dataset",
    local_dir="./outputs/",
    local_dir_use_symlinks=False,
)
```

## Uses

### Direct Use

This dataset is intended for:
- Analysis of multilingual reasoning behaviors in large language models
- Reproduction and verification of results reported in the associated paper
- Probing-based analysis of understanding failures
- Research on mitigation strategies for multilingual reasoning gaps

## Dataset Structure

The dataset consists of directories containing:
- Prober checkpoints
- Per-language and per-task inference results
- Intermediate signals used for understanding-failure detection and analysis

The exact directory structure mirrors the experimental setup used in the paper.

## Bias, Risks, and Limitations

- The dataset only contains outputs from **Qwen3-4B** and does not cover other model families.

## Citation

If you use this dataset, please cite the accompanying paper.

**BibTeX:**
```bibtex
@article{kang2025multilingualreasoninggapsemerge,
      title={Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models?}, 
      author={Deokhyung Kang and Seonjeong Hwang and Daehui Kim and Hyounghun Kim and Gary Geunbae Lee},
      year={2025},
      eprint={2510.27269},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.27269}, 
}
```