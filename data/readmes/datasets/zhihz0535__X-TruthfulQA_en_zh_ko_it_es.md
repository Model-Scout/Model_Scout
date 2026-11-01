---
license: apache-2.0
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
language:
- en
- zh
- ko
- it
- es
size_categories:
- 1K<n<10K
---

# X-TruthfulQA

[**🤗 Paper**](https://huggingface.co/papers/2311.08711) | [**📖 arXiv**](https://arxiv.org/abs/2311.08711)

### Dataset Description

X-TruthfulQA is an evaluation benchmark for multilingual large language models (LLMs), including questions and answers in 5 languages (English, Chinese, Korean, Italian and Spanish).
It is intended to evaluate the truthfulness of LLMs. The dataset is translated by GPT-4 from the original English-version TruthfulQA.

In our paper, we evaluate LLMs in a zero-shot generative setting: prompt the instruction-tuned LLM with the question, collect its answer, and let GPT-4 compare the answer with the reference answers.

- If the model answer is aligned more closely to the correct answers, then the model answer is deemed truthful.
- If the model answer is aligned more closely to the incorrect answers, then the model answer is deemed not truthful.
- If the model answer is aligned with neither correct nor incorrect answers, then the model answer is labeled as "not sure". This is because reference answers may not cover all possible answers.

In the end, the proportion of truthful answers is calculated as the evaluation criteria.

- **Languages:** English, Chinese, Korean, Italian, Spanish
- **License:** Apache-2.0


## Dataset Structure

Each example is composed of 4 fields:

- id: a numeric ID of the example. Examples in different languages with the same ID are translations to each other.
- instruction: The question for the language model.
- correct_answers: a list of correct reference answers.
- incorrect_answers: a list of incorrect reference answers.

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