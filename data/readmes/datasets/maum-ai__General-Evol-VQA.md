---
license: apache-2.0
dataset_info:
  features:
  - name: id
    dtype: string
  - name: image
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: korean
    num_bytes: 343402628
    num_examples: 587441
  - name: english
    num_bytes: 626167802
    num_examples: 598255
  download_size: 464324435
  dataset_size: 969570430
configs:
- config_name: default
  data_files:
  - split: korean
    path: data/korean-*
  - split: english
    path: data/english-*
task_categories:
- visual-question-answering
- question-answering
language:
- ko
- en
size_categories:
- 100K<n<1M
---
# Dataset Card for General-Evol-VQA-1.2M
This dataset has been carefully curated to enhance the general instruction capabilities of Vision-Language Models (VLMs). It comprises two subsets:
- **600k English** samples
- **600k Korean** samples

We recommend using this dataset alongside other task-specific datasets (e.g., OCR, Language, code, math, ...) to improve performance and achieve more robust model capabilities.
- **Made by:** [maum.ai Brain NLP](https://maum-ai.github.io). Jaeyoon Jung, Yoonshik Kim
- **Dataset Target Language(s):** Korean, English

## Seed Data
We use seed data from the VQAv2 dataset.

## Method
We modify the method of the paper [MMEvol: Empowering Multimodal Large Language Models with Evol-Instruct](https://mmevol.github.io/) to generate high-quality VQA dataset.