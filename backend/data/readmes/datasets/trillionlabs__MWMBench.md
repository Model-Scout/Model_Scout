---
license: apache-2.0
task_categories:
- image-text-to-text
language:
- en
- ko
tags:
- gui-world-model
- world-model
- gui-agent
- mobile-agent
- android
- benchmark
- next-ui-prediction
- html
- arxiv:2602.01576
pretty_name: MWMBench
dataset_info:
  features:
  - name: id
    dtype: string
  - name: episode_id
    dtype: string
  - name: step
    dtype: int64
  - name: image
    dtype: string
  - name: next_image
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: task_type
    dtype: string
  - name: prompt_version
    dtype: string
  - name: image_base64
    dtype: string
  - name: next_image_base64
    dtype: string
  splits:
  - name: train
    num_bytes: 1763900637
    num_examples: 2000
  download_size: 1706674657
  dataset_size: 1763900637
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# MWMBench: Mobile World Model Bench

**MWMBench** is a benchmark for evaluating **GUI world models** (next-screen prediction) on mobile apps. Given the current screenshot and an action in a real-world coordinate action space, a world model must predict the next screen. MWMBench evaluates in the native visual modality and covers 4 in-distribution benchmarks (AitW, GUIOdyssey, AndroidControl, AMEX) and 2 out-of-distribution benchmarks (AndroidWorld, KApps).

[![ICML 2026](https://img.shields.io/badge/ICML-2026-2563eb)](https://trillionlabs-gworld.github.io/) [![arXiv](https://img.shields.io/badge/arXiv-2602.01576-b31b1b)](https://arxiv.org/abs/2602.01576)

MWMBench was introduced with **gWorld** (GuiWorld), an open-weight GUI world model for mobile GUI agents: a single vision-language model (8B / 32B) that predicts the next screen after a user action by generating renderable HTML/web code instead of pixels. Paper: [Generative Visual Code Mobile World Models](https://huggingface.co/papers/2602.01576) (arxiv:2602.01576, ICML 2026).

- Project page: https://trillionlabs-gworld.github.io/
- Code and evaluation scripts: https://github.com/trillion-labs/gWorld
- Models: [gWorld-8B](https://huggingface.co/trillionlabs/gWorld-8B) · [gWorld-32B](https://huggingface.co/trillionlabs/gWorld-32B)

## Fields

| Field | Description |
|---|---|
| `id`, `episode_id`, `step` | Sample, episode and step identifiers |
| `image` / `image_base64` | Current screenshot (path / base64) |
| `next_image` / `next_image_base64` | Ground-truth next screenshot (path / base64) |
| `conversations` | Prompt (action + instructions) and reference response |
| `task_type`, `prompt_version` | Source benchmark / prompt metadata |

## Citation

```bibtex
@inproceedings{koh2026gworld,
  title     = {Generative Visual Code Mobile World Models},
  author    = {Koh, Woosung and Han, Sungjun and Lee, Segyu and Yun, Se-Young and Shin, Jamin},
  booktitle = {International Conference on Machine Learning (ICML)},
  year      = {2026},
  note      = {arXiv:2602.01576}
}
```
