---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 2951380166
    num_examples: 1420909
  download_size: 1483360321
  dataset_size: 2951380166
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/O0draAVUeUZI9qRMglywA.png)

# 🎨 Open-PerfectBlend

Open-PerfectBlend is an open-source reproduction of the instruction dataset introduced in the paper ["The Perfect Blend: Redefining RLHF with Mixture of Judges"](https://arxiv.org/abs/2409.20370).
It's a solid general-purpose instruction dataset with chat, math, code, and instruction-following data.

## Data source

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/rQ7db032OcjTZ2i2cpvY7.png)

Here is the list of the datasets used in this mix:

| Dataset | # Samples |
|------|------|
| [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA) | 395,000 |
| [openbmb/UltraInteract_sft](https://huggingface.co/datasets/openbmb/UltraInteract_sft) | 288,579 |
| [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) | 207,865 |
| [microsoft/orca-math-word-problems-200k](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k) | 200,035 |
| [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) | 187,405 |
| [theblackcat102/evol-codealpaca-v1](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1) | 111,272 |
| [Post-training-Data-Flywheel/AutoIF-instruct-61k](https://huggingface.co/datasets/Post-training-Data-Flywheel/AutoIF-instruct-61k) | 61,492 |
| [mlabonne/lmsys-arena-human-preference-55k-sharegpt](https://huggingface.co/datasets/mlabonne/lmsys-arena-human-preference-55k-sharegpt) | 57,362 |

The deduplication process removed 88.1k samples across all datasets. All of these datasets use either an Apache 2.0 or MIT license.

Thanks to OpenBMB, MetaMath, Hugging Face, Microsoft, theblackcat102, Post-training-Data-Flywheel, and LMSYS for the data!

## Comparison

Here is the extract from the paper with the dataset mixture:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/QObNW7erIVb_WM8C3hxDo.png)

There are two main differences with the dataset described in the paper:

* Instruction-following data comes from another source because Meta didn't release their dataset.
* The harmful intent hasn't been released either, so I didn't add any data in this category.