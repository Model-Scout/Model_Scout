---
license: mit
language:
- en
- ko
configs:
- config_name: en
  data_files:
  - split: eval
    path: test-evaluation/EnBBG_En-42_42_eval.csv
  - split: all
    path: test-all/EnBBG_En-42_42_all.csv
- config_name: ko
  data_files:
  - split: eval
    path: test-evaluation/KoBBG_Ko-42_42_eval.csv
  - split: all
    path: test-all/KoBBG_Ko-42_42_all.csv
task_categories:
- text-generation
- question-answering
---
# BBG
Social Bias Benchmark for Generation: A Comparison of Generation and QA-Based Evaluations (ACL-Findings 2025)

## About
Measuring social bias in large language models (LLMs) is crucial, but existing bias evaluation methods struggle to assess bias in long-form generation.
We propose a **Bias Benchmark for Generation (BBG)**, an adaptation of the Bias Benchmark for QA (BBQ), designed to evaluate social bias in long-form generation by having LLMs generate continuations of story prompts.
Building our benchmark in English and Korean, we measure the probability of neutral and biased generations across ten LLMs.
We also compare our long-form story generation evaluation results with multiple-choice BBQ evaluation, showing that the two approaches produce inconsistent results.
<img src="img/bbg_intro.png" width=50% height=50%>

## Sources
- **Paper:** [Social Bias Benchmark for Generation: A Comparison of Generation and QA-Based Evaluations](https://arxiv.org/abs/2503.06987)
- **Project Page:** [jinjh0123.github.io/BBG](https://jinjh0123.github.io/BBG/)
- **Repository:** [jinjh0123/BBG](https://github.com/jinjh0123/BBG/)

## Dataset Description
We propose the Bias Benchmark for Generation (BBG), a benchmark for assessing bias in story generation, built on the English BBQ and Korean BBQ (KoBBQ) datasets.
To adapt the existing multiple-choice format of BBQ for long-form generation, we first obfuscate contextual data by replacing character references with neutral placeholders ('one' and 'the other') and prompt the language model to generate a continuation of the story.
We then assess bias in the generated output by determining whether the placeholders are consistently assigned to specific characters using machine reading comprehension.
<img src="img/bbg_framework.svg">

### Languages
- `en`: English
- `ko`: Korean
```python
from datasets import load_dataset

enbbg = load_dataset("jinjh0123/bbg", "en")
kobbg = load_dataset("jinjh0123/bbg", "ko")
```

### Data Splits
- `all`: Exhaustive. Contains all possible combinations that can be created from each template. Use for full-scale analysis.
- `eval`: Lightweight. Contains exactly one randomly selected instantiation per template. Recommended for standard benchmarking.

## Tasks
For detailed information, please refer to our [GitHub repository](https://jinjh0123.github.io/BBG/).

### Bias in Generation
- **Step 1: Generation**
  - Let the target model generate a continuation of the seed story.
  - Input: `context` (`amb_context` + `obfdis_context`)
- **Step 2: QA**
  - Let the evaluator model answer the reading comprehension question.
  - Input:
    - Passage: `context` + generated text from Step 1
    - Multiple-choice QA: `question`, `choices`
- **Step 3: Evaluation**
  - Based on the answer from Step 2, calculate the neutrality and bias scores.
  - Type:
    - Undetermined: Cannot be determined, 주어진 정보만으로는 답을 알 수 없음
    - Biased: `biased_answer`

### Bias in QA (original BBQ setting)
- **Step 1: QA**
  - Let the target model choose an answer for the reading comprehension question.
  - Input:
    - Passage:
      - Ambiguous context: `amb_context`
      - Disambiguated context: `amb_context` + `dis_context`
    - Multiple-choice QA: `question`, `choices`
- **Step 2: Evaluation**
  - Based on the answer from Step 1, calculate the accuracy and bias scores.
  - Type:
    - Correct answer for ambiguous contexts: undetermined (Cannot be determined, 주어진 정보만으로는 답을 알 수 없음)
    - Correct answer for disambiguated contexts: `dis_answer`
    - Biased answer: `biased_answer`


## Citation
```
@inproceedings{jin-etal-2025-social,
    title = "Social Bias Benchmark for Generation: A Comparison of Generation and {QA}-Based Evaluations",
    author = "Jin, Jiho  and  Kang, Woosung  and  Myung, Junho  and  Oh, Alice",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-acl.585/",
    doi = "10.18653/v1/2025.findings-acl.585",
    pages = "11215--11228",
    ISBN = "979-8-89176-256-5"
}
```