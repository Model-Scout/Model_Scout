---
language:
- de
- en
- fr
- hi
- ig
- ja
- ko
- ms
- pt
- sw
- th
- zh
- zu

task_categories:
- question-answering
- text-generation

pretty_name: HealthBench-ProX
size_categories:
- 1K<n<10K
---

# HealthBench-ProX

## Dataset Description

HealthBench-ProX is a multilingual extension of the original [HealthBench Professional](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf) benchmark for evaluating large language models on realistic healthcare consultation scenarios.

The dataset contains 6,825 evaluation instances organized into 13 language-specific splits:

- de (German)
- en (English)
- fr (French)
- hi (Hindi)
- ig (Igbo)
- ja (Japanese)
- ko (Korean)
- ms (Malay)
- pt (Portuguese)
- sw (Swahili)
- th (Thai)
- zh (Chinese)
- zu (Zulu)

Each example includes a user query, evaluation rubric, physician reference response, and associated metadata.

## Data Creation

HealthBench-ProX is derived from the original HealthBench Professional benchmark.

The source English examples were translated into 13 languages using GPT-5.4 deployed through Azure OpenAI Service. The translation process preserves the original benchmark structure, including user queries, evaluation rubrics, physician reference responses, and metadata.

No new evaluation instances were created. All examples originate from the original benchmark, and only the language of the content was transformed through machine translation using GPT-5.4 on Azure OpenAI Service.

## Dataset Structure

The dataset is organized as language-specific splits:

- `de`
- `en`
- `fr`
- `hi`
- `ig`
- `ja`
- `ko`
- `ms`
- `pt`
- `sw`
- `th`
- `zh`
- `zu`

Each example contains:

- `id`
- `conversation`
- `rubric_items`
- `physician_response`
- `specialty`
- `difficulty`
- `use_case`
- `type`

## Usage

```python
from datasets import load_dataset

ja_ds = load_dataset(
    "li-lab/HealthBench-ProX",
    split="ja"
)

print(len(ja_ds))
```

## Intended Uses

- Multilingual healthcare LLM evaluation
- Cross-lingual robustness assessment
- Medical reasoning benchmarking
- Healthcare communication evaluation

This dataset is intended for research purposes only.

## Limitations

The translated examples may not perfectly preserve all linguistic nuances of the original benchmark. Performance on this dataset should not be interpreted as clinical competence or suitability for real-world medical decision making.

## Citation

```bibtex
@dataset{healthbench_prox,
  title={HealthBench-ProX},
  author={Li Lab},
  year={2026}
}
