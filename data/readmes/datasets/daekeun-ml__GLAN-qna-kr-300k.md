---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: subject
    dtype: string
  - name: level
    dtype: int64
  - name: subtopics
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 995519676
    num_examples: 303581
  download_size: 356642767
  dataset_size: 995519676
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: openrail
task_categories:
- question-answering
language:
- ko
pretty_name: GLAN-QnA-KR
size_categories:
- 100K<n<1M
---

# Korean GLAN (Generalized Instruction Tuning) Instructions Dataset

**GLAN-QnA-KR** — a 303,581-row seedless, taxonomy-driven Korean instruction corpus.

📄 A technical report documenting the generation pipeline, duplication analysis, and a two-layer
contamination audit is available on arXiv: **[arXiv:2607.20443](https://arxiv.org/abs/2607.20443)**.
Please cite it if you use this dataset ([Citation](#citation)).

## What is GLAN?

Catastrophic forgetting, also known as catastrophic interference, occurs during SLM/LLM fine-tuning when a model trained on new data overwrites the knowledge it previously acquired, leading to a significant drop in performance on earlier tasks. This issue is particularly prominent in scenarios where the model needs to adapt to diverse and potentially conflicting data distributions without losing its ability to perform well on initial tasks.

GLAN (Generalized Instruction Tuning) addresses catastrophic forgetting by leveraging a systematically curated taxonomy of human knowledge to generate synthetic, diverse, and comprehensive instruction datasets. Specifically, GLAN uses a pre-curated taxonomy of human knowledge and capabilities to generate large-scale, diverse instruction data across various disciplines. This taxonomy mirrors the systematic structure of human education, breaking down knowledge into fields, sub-fields, and distinct disciplines, which are then used to design syllabi for different subjects. These syllabi detail key concepts for each class session, enabling the generation of diverse and comprehensive instructions. Here is GLAN's key features:

- **Taxonomy Creation**: A detailed hierarchy of human knowledge is built using LLMs and human verification.
- **Subject and Syllabus Generation**: LLMs generate a list of subjects and detailed syllabi, breaking down subjects into class sessions with key concepts.
- **Instruction Generation**: Homework questions and their answers are generated based on the syllabi, ensuring broad coverage and diversity.

## Overview
This dataset is generated using the GLAN approach, inspired by the paper described in the [paper](https://arxiv.org/abs/2402.13064).
The dataset was created by running the hands-on reference code provided in the [implementation by the author](https://github.com/Azure/synthetic-qa-generation).

"Seedless" means no seed examples and no context derived from external data are used: every question and
answer is generated from the taxonomy alone.

## Dataset Details

- **Number of records**: 300K (303,581), a single `train` split
- **Language**: Korean question/answer text, with English-labelled discipline names
- **Taxonomy**: flat, 1,084 disciplines
- **Difficulty scale**: 100–900 (see `level` below)
- **Median length**: 313 characters per question, 1,098 characters per answer
- **Generation / release**: 2024-12 / 2024-12
- **Purpose**: This dataset is designed for fine-tuning task and for question answering, but not limited to question answering.

## Dataset Creation

The dataset was created using a synthetic generation approach based on instructions and questions.
The generation process leverages Microsoft Phi-3.5-MoE-instruct as the producer model to create diverse and high-quality examples that are valuable for training and evaluating NLU models.

## Features

The dataset contains the following features:

- **question**: The instruction or question prompt given to the model.
- **answer**: The generated response based on the instruction.
- **subject**: A subject derived from a taxonomy. A syllabus is generated from this subject.
- **level**: The difficulty level of the course. For a first-year undergraduate course, think of it as level 100. (e.g., 100, 200, 300, ...)
- **subtopics**: These are subtopics related to the subject.

## Usage

To use this dataset, you can load it using the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("daekeun-ml/GLAN-qna-kr-300k")
```

## Data Quality

Two properties measured in the technical report are atypical for synthetic instruction data at this scale.

**Internal duplication — near zero:**

| Measure | Result |
|---|---|
| Exact duplicate questions | 1 of 303,581 rows |
| Character-trigram near-duplicate clusters at Jaccard ≥ 0.9 | 0 (5,000-sample probe) |

**Benchmark contamination** — a two-layer audit against KMMLU, KoBEST (five sub-tasks), and HAE-RAE-Bench,
over 20,000 sampled GLAN questions and seven evaluation sets:

| Measure | Result |
|---|---|
| Max question-level character-trigram Jaccard (test vs. corpus) | 0.163 |
| Test items at Jaccard ≥ 0.7 | 0 |
| Max multilingual-E5 cosine similarity | 0.901 |
| Test items at cosine ≥ 0.90 / ≥ 0.95 | 1 / 0 |

Scope note: the audit covers the Korean benchmarks listed above only, and says nothing about benchmarks
not tested here.

## Limitations

- **Synthetic and ungrounded.** Generated from a taxonomy without retrieval or source grounding, so
  factual claims in answers are **not verified** against any reference. Expect hallucinations,
  particularly at higher `level` values and in specialized disciplines.
- **Producer-model bias.** Style, reasoning patterns, and knowledge boundaries inherit from
  Phi-3.5-MoE-instruct, including its Korean-language weaknesses.
- **Mixed-language rows.** `subject` and `subtopics` are English while `question`/`answer` are Korean;
  filtering pipelines that assume one language per row need care.
- **Flat taxonomy.** The 1,084 disciplines are flat rather than hierarchical, so parent-field-level
  stratified sampling is not directly available from `subject`.
- **PoC scope.** See the Disclaimer below. For use beyond PoC, apply your own quality and factuality
  filtering first.

## Citation

If you use this dataset, please cite the technical report:

```bibtex
@misc{kim2026glanqna,
  title         = {{GLAN-QnA-KR}: A Seedless Taxonomy-Driven {Korean} Instruction Corpus},
  author        = {Daekeun Kim},
  year          = {2026},
  eprint        = {2607.20443},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2607.20443}
}
```

If you use the GLAN method itself, please also cite the original paper:

```bibtex
@misc{li2024glan,
  title         = {Synthetic Data ({Almost}) from {Scratch}: Generalized Instruction Tuning for Language Models},
  author        = {Haoran Li and Qingxiu Dong and Zhengyang Tang and Chaojun Wang and Xingxing Zhang and Haoyang Huang and Shaohan Huang and Xiaolong Huang and Zeqiang Huang and Dongdong Zhang and Yuxian Gu and Xin Cheng and Xun Wang and Si-Qing Chen and Li Dong and Wei Lu and Zhifang Sui and Benyou Wang and Wai Lam and Furu Wei},
  year          = {2024},
  eprint        = {2402.13064},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2402.13064}
}
```

## References
- 📄 Technical Report (this dataset): https://arxiv.org/abs/2607.20443
- 📄 GLAN Paper: https://arxiv.org/abs/2402.13064
- 💻 GLAN Implementation: https://github.com/Azure/synthetic-qa-generation/tree/main/glan-instruct
- 📝 Generate Synthetic QnAs from Real-world Data: [Blog](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/generate-synthetic-qnas-from-real-world-data-on-azure/4202053) | [GitHub](https://github.com/Azure/synthetic-qa-generation)

## License
-  OpenRAIL license. All implementations and datasets were developed by the author.

### Disclaimer
This dataset is released under the OpenRAIL License, which emphasizes the responsible use of AI technologies. This dataset is provided exclusively for Proof of Concept (PoC) purposes. This dataset is seedless synthetic data that does not use context information derived from external data, but special care should be taken when using it for purposes other than PoC.

Users are required to comply with ethical guidelines and refrain from using the dataset or any derived outputs for harmful, unethical, or illegal purposes, including but not limited to the violation of human rights, spreading misinformation, or generating harmful content.
It does not reflect the opinions, policies, or proprietary information of the company for which the author is employed, nor does it necessarily represent official property or views of the company.
