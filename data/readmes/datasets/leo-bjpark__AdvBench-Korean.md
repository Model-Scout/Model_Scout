---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 115396
    num_examples: 520
  download_size: 39231
  dataset_size: 115396
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- text-generation
language:
- ko
tags:
- agent
---


# AdvBench-Korean

**AdvBench-Korean** is a Korean translation of the [**AdvBench**](https://huggingface.co/datasets/walledai/AdvBench) dataset for evaluating jailbreak and adversarial attacks on aligned language models.
The prompts were translated into Korean using **Google/Gemma-3-12B-Instruct (`google/gemma-3-12b-it`)**. All samples were successfully translated **without any refusals**, preserving the full set of **520 examples** from the original dataset.
For safety reasons, details of the translation generation pipeline and prompting strategy are not publicly released.

## Dataset Structure

Each example contains:

| column | description |
|---|---|
| prompt | harmful instruction (Korean translation) |
| target | target response used in AdvBench |

The dataset contains **520 examples** in the training split.

## Original Dataset

This dataset is derived from **AdvBench**, introduced in:

*Universal and Transferable Adversarial Attacks on Aligned Language Models*

## Citation

If you use this dataset, please cite the **original AdvBench paper**:

```bibtex
@misc{zou2023universal,
      title={Universal and Transferable Adversarial Attacks on Aligned Language Models}, 
      author={Andy Zou and Zifan Wang and J. Zico Kolter and Matt Fredrikson},
      year={2023},
      eprint={2307.15043},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

If you specifically use the Korean translation, you may also cite:
```
@dataset{park2026advbenchkorean,
  title={AdvBench-Korean: Korean Translation of the AdvBench Dataset},
  author={Bumjin Park},
  year={2026},
  url={https://huggingface.co/datasets/leo-bjpark/AdvBench-Korean}
}
```