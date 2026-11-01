---
license: mit
configs:
- config_name: default
  data_files:
  - split: english
    path: english.json
  - split: chinese
    path: chinese.json
  - split: korean
    path: korean.json
  - split: italian
    path: italian.json
  - split: spanish
    path: spanish.json
task_categories:
- question-answering
- text-generation
language:
- en
- zh
- it
- ko
- es
size_categories:
- 1K<n<10K
---

# X-SVAMP

[**🤗 Paper**](https://huggingface.co/papers/2311.08711) | [**📖 arXiv**](https://arxiv.org/abs/2311.08711)

### Dataset Description

X-SVAMP is an evaluation benchmark for multilingual large language models (LLMs), including questions and answers in 5 languages (English, Chinese, Korean, Italian and Spanish).
It is intended to evaluate the math reasoning abilities of LLMs. The dataset is translated by GPT-4-turbo from the original English-version SVAMP.

In our paper, we evaluate LLMs in a zero-shot generative setting: prompt the instruction-tuned LLM with the question, collect its response (a chain-of-thought rationale), 
and let GPT-3.5-turbo extract the predicted answer from the response. Then, we compare the extracted answer with the reference answer to calculate accuracy.

Each question is appended with a chain-of-thought prompt. In English, it is `Think step-by-step before reaching the final answer`. Feel free to change this prompt if needed.

- **Languages:** English, Chinese, Korean, Italian, Spanish
- **License:** MIT


## Dataset Structure

Each example is composed of 3 fields:

- id: a numeric ID of the example. Examples in different languages with the same ID are translations to each other.
- instruction: The question for the language model. Each question is appended with a chain-of-thought prompt. Feel free to change this prompt if needed.
- answer: The reference answer to the question. SVAMP only includes non-negative integer answers.

## Citation [optional]

If you find the data useful, please kindly cite our paper:

```
@article{zhang2023plug,
  title={PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning},
  author={Zhang, Zhihan and Lee, Dong-Ho and Fang, Yuwei and Yu, Wenhao and Jia, Mengzhao and Jiang, Meng and Barbieri, Francesco},
  journal={arXiv preprint arXiv:2311.08711},
  year={2023}
}
```