---
configs:
- config_name: flores
  data_files:
  - split: test
    path: "flores/test/*.jsonl"
- config_name: humaneval-xl
  data_files:
  - split: csharp
    path: "humaneval-xl/test/csharp/*.jsonl"
  - split: go
    path: "humaneval-xl/test/go/*.jsonl"
  - split: java
    path: "humaneval-xl/test/java/*.jsonl"
  - split: javascript
    path: "humaneval-xl/test/javascript/*.jsonl"
  - split: kotlin
    path: "humaneval-xl/test/kotlin/*.jsonl"
  - split: perl
    path: "humaneval-xl/test/perl/*.jsonl"
  - split: php
    path: "humaneval-xl/test/php/*.jsonl"
  - split: python
    path: "humaneval-xl/test/python/*.jsonl"
  - split: ruby
    path: "humaneval-xl/test/ruby/*.jsonl"
  - split: scala
    path: "humaneval-xl/test/scala/*.jsonl"
  - split: swift
    path: "humaneval-xl/test/swift/*.jsonl"
  - split: typescript
    path: "humaneval-xl/test/typescript/*.jsonl"
- config_name: mgsm
  data_files:
  - split: test
    path: "mgsm/test/*.jsonl"
- config_name: mhellaswag
  data_files:
  - split: test
    path: "mhellaswag/test/*.jsonl"
- config_name: mifeval
  data_files:
  - split: test
    path: "mifeval/test/*.jsonl"
- config_name: mlogiqa
  data_files:
  - split: test
    path: "mlogiqa/test/*.jsonl"
- config_name: mmmlu
  data_files:
  - split: easy
    path: "mmmlu/easy/*/*.jsonl"
  - split: hard
    path: "mmmlu/hard/*/*.jsonl"
- config_name: xnli
  data_files:
  - split: test
    path: "xnli/test/*.jsonl"

license: apache-2.0
language:
- ar
- es
- fr
- ja
- ko
- pt
- th
- vi
- en
- zh
---
<div align="center">

# Neural Metrics · Multilingual evaluation, because invoices do not only arrive in English.

<img src="https://img.shields.io/badge/Neural%20Metrics-document%20extraction-4F46E5?style=for-the-badge" alt="Neural Metrics" />
<img src="https://img.shields.io/badge/fork%20of-Qwen%2FP--MMEval-2563EB?style=flat-square" alt="fork" />

</div>

Real document pipelines meet Tamil addresses, German compound nouns and Japanese date formats in the same afternoon. P-MMEval gives us consistent multilingual coverage to measure that.

**We use it for:** tracking extraction quality across languages - catching regressions that only appear outside English.

> ### Attribution
> This is an **unmodified fork** of [`Qwen/P-MMEval`](https://huggingface.co/datasets/Qwen/P-MMEval), created by the [Qwen team](https://huggingface.co/Qwen).
> All weights, files and behaviour are identical to upstream — we rehost it so our experiments stay
> reproducible and version-pinned. The original license and all credit remain with the Qwen team.
> If you want the canonical dataset, please use [the original](https://huggingface.co/datasets/Qwen/P-MMEval).

---

<details>
<summary><b>Original dataset card from Qwen/P-MMEval</b> (click to expand)</summary>

<div align="center">

# Neural Metrics · Multilingual evaluation, because invoices do not only arrive in English.

<img src="https://img.shields.io/badge/Neural%20Metrics-document%20extraction-4F46E5?style=for-the-badge" alt="Neural Metrics" />
<img src="https://img.shields.io/badge/fork%20of-Qwen%2FP--MMEval-2563EB?style=flat-square" alt="fork" />

</div>

Real document pipelines meet Tamil addresses, German compound nouns and Japanese date formats in the same afternoon. P-MMEval gives us consistent multilingual coverage to measure that.

**We use it for:** tracking extraction quality across languages - catching regressions that only appear outside English.

> ### Attribution
> This is an **unmodified fork** of [`Qwen/P-MMEval`](https://huggingface.co/datasets/Qwen/P-MMEval), created by the [Qwen team](https://huggingface.co/Qwen).
> All weights, files and behaviour are identical to upstream — we rehost it so our experiments stay
> reproducible and version-pinned. The original license and all credit remain with the Qwen team.
> If you want the canonical dataset, please use [the original](https://huggingface.co/datasets/Qwen/P-MMEval).

---

<details>
<summary><b>Original dataset card from Qwen/P-MMEval</b> (click to expand)</summary>

# P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs

## Introduction

We introduce a multilingual benchmark, P-MMEval, covering effective fundamental and capability-specialized datasets. We extend the existing benchmarks, ensuring consistent language coverage across all datasets and providing parallel samples among multiple languages, supporting up to 10 languages from 8 language families (i.e., en, zh, ar, es, ja, ko, th, fr, pt, vi). As a result, P-MMEval facilitates a holistic assessment of multilingual capabilities and comparative analysis of cross-lingual transferability.

## Supported Languages
- Arabic
- Spanish
- French
- Japanese
- Korean
- Portuguese
- Thai
- Vietnamese
- English
- Chinese

## Supported Tasks
<img src="https://cdn-uploads.huggingface.co/production/uploads/64abba3303cd5dee2efa6ee9/adic-93OnhRoSIk3P2VoS.png" width="1200" />

## Main Results

The multilingual capabilities of all models except for the LLaMA3.2 series improve with increasing model sizes, as LLaMA3.2-1B and LLaMA3.2-3B exhibit poor instruction-following capabilities, leading to a higher failure rate in answer extraction. In addition, Qwen2.5 demonstrates a strong multilingual performance on understanding and capability-specialized tasks, while Gemma2 excels in generation tasks. Closed-source models generally outperform open-source models.

<img src="https://cdn-uploads.huggingface.co/production/uploads/64abba3303cd5dee2efa6ee9/dGpAuDPT53TDHEW5wFZWk.png" width="1200" />

## Citation

We've published our paper at [this link](https://arxiv.org/pdf/2411.09116). If you find this dataset is helpful, please cite our paper as follows:
```
@misc{zhang2024pmmevalparallelmultilingualmultitask,
      title={P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs}, 
      author={Yidan Zhang and Yu Wan and Boyi Deng and Baosong Yang and Haoran Wei and Fei Huang and Bowen Yu and Junyang Lin and Fei Huang and Jingren Zhou},
      year={2024},
      eprint={2411.09116},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.09116}, 
}
```

# Usage
You can use OpenCompass if you want to evaluate your LLMs on P-MMEval . We advice you to use vllm to accelerate the evaluation (requiring vllm installation):

```
# CLI
opencompass --models hf_internlm2_5_1_8b_chat --datasets pmmeval_gen -a vllm

# Python scripts
opencompass ./configs/eval_PMMEval.py
```

</details>

</details>
