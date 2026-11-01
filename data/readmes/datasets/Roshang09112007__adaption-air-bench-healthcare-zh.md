---
annotations_creators: []
language:
  - en
  - ko
  - multilingual
language_creators: []
license: []
multilinguality:
- multilingual
pretty_name: 'adaption-air_bench_healthcare_zh'
size_categories:
- 10K<n<100K
source_datasets:
- 'extended|https://huggingface.co/datasets/AIR-Bench/qrels-qa_healthcare_zh-dev'
tags:
  - adaption
  - instruction-tuning
  - other
task_categories: []
task_ids: []
---

![banner](https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/61a9742c-c726-4c3d-8502-72d035325976.png)

This dataset is a remastered version of this [dataset](https://huggingface.co/datasets/AIR-Bench/qrels-qa_healthcare_zh-dev) prepared using [Adaption's](https://adaptionlabs.ai/app/auth) Adaptive Data platform.

# adaption-air_bench_healthcare_zh

This dataset contains Chinese healthcare question-answer pairs from the AIR-Bench 24.05 benchmark, specifically focusing on the default development and test splits. The data is formatted as prompt-completion pairs where prompts represent medical queries and completions reference specific document IDs. It is designed for evaluating retrieval-augmented generation systems in the medical domain.

### Dataset size

There are 28,234 data points in this dataset. This is an instruction tuning dataset.

### Quality of Remastered Dataset

The final quality is C, with a relative quality improvement of 450.0%.

### Domain
- Other (100%)

### Language
- Cebuano (66%)
- English (10%)
- Korean (8%)

### Tone
- Clear (30%)
- Analytical (20%)
- Objective (20%)

### Evaluation Results

- **Quality Gains:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/a944b7d3-c835-45d0-a09e-8d002dba8da2.png" alt="QualityGains" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Grade Improvement:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/00524d62-b2a6-49c5-88e8-77237d11989a.png" alt="Grade" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />

- **Percentile Chart:**
<img src="https://proteus-prod-public.s3.us-east-1.amazonaws.com/temp/25dfff62-3e6e-4f38-9482-27f331fd9ee5.png" alt="Percentile Chart" style="max-width: 50%; display: block; margin-left: auto; margin-right: auto;" />
