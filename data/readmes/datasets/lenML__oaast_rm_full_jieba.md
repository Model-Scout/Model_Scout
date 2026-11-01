---
license: apache-2.0
language:
  - en
  - es
  - ru
  - de
  - pl
  - th
  - vi
  - sv
  - bn
  - da
  - he
  - it
  - fa
  - sk
  - id
  - nb
  - el
  - nl
  - hu
  - eu
  - zh
  - eo
  - ja
  - ca
  - cs
  - bg
  - fi
  - pt
  - tr
  - ro
  - ar
  - uk
  - gl
  - fr
  - ko
tags:
- human-feedback
size_categories:
- 10K<n<100K
---

尝试解决"llm repetition problem"，使用分词模型对oaast语料进行“结巴化”数据增强，提供更强的重复内容拒绝效果。

Attempts to solve the "llm repetition problem" by using a segmentation model to enhance the oaast corpus with "stuttering" data to provide stronger rejection of duplicate content.

其次，还过滤掉了所有自我认知的微调样本。

Second, it also filters out all the fine-tuned samples of self-cognition.

files:
- oaast_rm_full_jieba.jsonl : word level repeat
- oaast_rm_full_sent_jieba.jsonl : sentence level repeat