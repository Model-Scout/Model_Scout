---
license: cc-by-nc-4.0
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
- text-generation
- conversational
language:
- en
- zh
- ko
- it
- es
size_categories:
- 1K<n<10K
---

# X-AlpacaEval

[**🤗 Paper**](https://huggingface.co/papers/2311.08711) | [**📖 arXiv**](https://arxiv.org/abs/2311.08711)

### Dataset Description

X-AlpacaEval is an evaluation benchmark for multilingual instruction-tuned large language models (LLMs), including open-ended instructions in 5 languages (English, Chinese, Korean, Italian and Spanish).
It is described in the paper [PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning
](https://arxiv.org/abs/2311.08711).

The instructions in this benchmark are translated from the original English version of [AlpacaEval](https://huggingface.co/datasets/tatsu-lab/alpaca_eval).
Translations were completed by professional translators who are native speakers of the target languages.
The data is intended to be used as evaluation data of instruction-tuned LLMs. 
Generate responses to X-AlpacaEval instructions with your LLM, and use human, GPT-4, or other LLM judges to evaluate the quality of preference of the response.
GPT-4 evaluation can refer to implementations from the original [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) or [MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge).

- **Languages:** English, Chinese, Korean, Italian, Spanish
- **License:** CC BY-NC 4.0


## Uses

Use as input instructions to evaluate instruction-tuned LLMs

### Out-of-Scope Use

- Evaluate foundation LLMs (pre-trained LLMs) without instruction tuning
- Evaluate non-generative (non-autoregressive) models

## Dataset Structure

Each example is composed of 3 fields:

- id: a numeric ID of the example. Examples in different languages with the same ID are translations to each other.
- dataset: AlpacaEval is originally collected from 5 distinct test sets. This field identifies its original source.
- instruction: The instruction to the LLM.

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