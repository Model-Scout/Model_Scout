---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: task
    dtype: string
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source
    dtype: string
  - name: license
    dtype: string
  - name: train_tokens
    dtype: int64
  - name: total_tokens
    dtype: int64
  splits:
  - name: train
    num_bytes: 1558269231.031623
    num_examples: 1015365
  download_size: 1194352889
  dataset_size: 1558269231.031623
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- en
- ko
- ja
- zh
size_categories:
- 1M<n<10M
tags:
- not-for-all-audiences
---

This repository is a **collection** of **English, Korean, Chinese, and Japanese** datasets collected by the HuggingFace Hub and transformed into a unified format. It consists of either **native** or **synthetic** data.

Some data is not clearly copyrighted or only allows non-commercial use.

**Preprocessing**: I removed data with too few answer tokens or more than 8192 tokens, and removed synthetic data with repetitions.

**Balancing**: I randomly sampled a subset of the data with different weights for each language and task to balance the training tokens per language/task.

### Data format

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/kw6EUddOFNzeJau815o2N.png)

```
conversations: [
    {"role":"system","content":"CONTENT1"},
    {"role":"user","content":"CONTENT2"},
    {"role":"assistant","content":"CONTENT3"},
    {"role":"user","content":"CONTENT4"},
    {"role":"assistant","content":"CONTENT5"}]
```

### Number of train tokens(assistant answer)

- tokenizer: Mistral-Nemo-12B-Instruct

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/UFFmRKMMHNKuGsGeHqsuo.png)

**All the datasets are collected from huggingface hub**

## Thank you for sharing your dataset!

#### English
- [Magpie-Align/Magpie-Llama-3.1-Pro-MT-300K-v0.1](https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-MT-300K-v0.1)
- [4DR1455/finance_questions](https://huggingface.co/datasets/4DR1455/finance_questions)
- [Gryphe/Sonnet3.5-Charcard-Roleplay](https://huggingface.co/datasets/Gryphe/Sonnet3.5-Charcard-Roleplay)
- [codefuse-ai/Evol-instruction-66k](https://huggingface.co/datasets/codefuse-ai/Evol-instruction-66k)
- [gbharti/wealth-alpaca_lora](https://huggingface.co/datasets/gbharti/wealth-alpaca_lora)
- [jondurbin/gutenberg-dpo-v0.1](https://huggingface.co/datasets/jondurbin/gutenberg-dpo-v0.1)
- [lavita/medical-qa-datasets](https://huggingface.co/datasets/lavita/medical-qa-datasets)
- [microsoft/orca-math-word-problems-200k](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k)
- [neural-bridge/rag-dataset-12000](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000)
- [qiaojin/PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA)
- [ymoslem/Law-StackExchange](https://huggingface.co/datasets/ymoslem/Law-StackExchange)

#### Korean
- [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a)
- [BCCard/BCCard-Finance-Kor-QnA](https://huggingface.co/datasets/BCCard/BCCard-Finance-Kor-QnA)
- [CarrotAI/ko-code-alpaca-QA](https://huggingface.co/datasets/CarrotAI/ko-code-alpaca-QA)
- [ChuGyouk/AI_healthcare_QA_samples_Sonnet3.5](https://huggingface.co/datasets/ChuGyouk/AI_healthcare_QA_samples_Sonnet3.5)
- [HAERAE-HUB/qarv-instruct-ko](https://huggingface.co/datasets/HAERAE-HUB/qarv-instruct-ko)
- [jihye-moon/LawQA-Ko](https://huggingface.co/datasets/jihye-moon/LawQA-Ko)
- [junyeong-nero/kin_med_100K_edited](https://huggingface.co/datasets/junyeong-nero/kin_med_100K_edited)
- [kyujinpy/KOR-OpenOrca-Platypus-v3](https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v3)
- [zzunyang/LawQA_LawSee](https://huggingface.co/datasets/zzunyang/LawQA_LawSee)

#### Chinese
- [Magpie-Align/Magpie-Qwen2-Pro-200K-Chinese](https://huggingface.co/datasets/Magpie-Align/Magpie-Qwen2-Pro-200K-Chinese)
- [DavidLanz/medical_instruction](https://huggingface.co/datasets/DavidLanz/medical_instruction)
- [Dusker/lawyer-llama](https://huggingface.co/datasets/Dusker/lawyer-llama)
- [frankminors123/belle-math-zh](https://huggingface.co/datasets/frankminors123/belle-math-zh)
- [shibing624/roleplay-zh-sharegpt-gpt4-data](https://huggingface.co/datasets/shibing624/roleplay-zh-sharegpt-gpt4-data)

#### Japanese
- [Aratako/Synthetic-JP-Conversations-Magpie-Nemotron-4-10k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Conversations-Magpie-Nemotron-4-10k)
- [Aratako/Synthetic-JP-EN-Coding-Dataset-Magpie-69k](https://huggingface.co/datasets/Aratako/Synthetic-JP-EN-Coding-Dataset-Magpie-69k)
- [Aratako/Synthetic-Japanese-Roleplay-NSFW-Claude-3.5s-10.5k-formatted](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-NSFW-Claude-3.5s-10.5k-formatted)
- [HachiML/alpaca_jp_math](https://huggingface.co/datasets/HachiML/alpaca_jp_math)
- [iam-ajaymeena/Self-Instruct-Japanese-Elzya-13B](https://huggingface.co/datasets/iam-ajaymeena/Self-Instruct-Japanese-Elzya-13B)
- [p1atdev/ichikara-instruction](https://huggingface.co/datasets/p1atdev/ichikara-instruction)
- [team-hatakeyama-phase2/AutoMultiTurnByCalm3-22B-Corrected-reformatted](https://huggingface.co/datasets/team-hatakeyama-phase2/AutoMultiTurnByCalm3-22B-Corrected-reformatted)