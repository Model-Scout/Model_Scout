---
license: gpl-3.0
task_categories:
- text-generation
language:
- zh
tags:
- not-for-all-audiences
pretty_name: dpo toxic chinese
size_categories:
- 1K<n<10K
---

# DPO Toxic Chinese v2.0

<details>
  <summary>Change Log</summary>
  
  - v2.0: 增加了[adamo1139/toxic-dpo-natural-v5](https://huggingface.co/datasets/adamo1139/toxic-dpo-natural-v5), 并更新了翻译策略. `prompt`由`t5_translate`模型翻译, `chosen`由Uncensored大模型翻译, `rejected`由一般大模型对`prompt`生成拒绝性的回复
  - v1.0: 最初版本, 使用大模型将[unalignment/toxic-dpo-v0.2](https://huggingface.co/datasets/unalignment/toxic-dpo-v0.2)翻译而来

</details>

这是一个高度毒性, 高度有害的数据集, 意在展示DPO是如何破除模型的审核/对齐的

## 使用限制

这个数据集被设计用于学术研究, 而非其他恶意场景. 下载或使用这个数据集, 则视为您承认以下的事实:

- 这个数据集是有毒的, 包含许多敏感内容
- 数据集中文本包含的内容和观点与我完全无关, 它们只是大模型生成的文字
- 您可以使用该数据集, 但必须遵守相关法律
- 您对您自己下载和使用数据集的行为负责, 我对您的一切行为没有任何责任