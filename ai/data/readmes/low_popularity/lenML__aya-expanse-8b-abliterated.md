---
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
base_model:
  - CohereForAI/aya-expanse-8b
tags:
  - gguf
  - CohereForAI
---

# Model Card for aya-expanse-8b-abliterated
This is an uncensored version of [aya-expanse-8b](https://huggingface.co/CohereForAI/aya-expanse-8b) created with abliteration (see [this article](https://huggingface.co/blog/mlabonne/abliteration) to know more about it).

Special thanks to [@FailSpy](https://huggingface.co/failspy) for the original code and technique. Please follow him if you're interested in abliterated models.

# Limitations
目前，根据我的 `lenml-reject-eval` 测试，此版本模型将拒绝评分从 `0.91` 降低到 `0.50`，这仍然是一个很高的分数（目前完全解除限制的模型在 reject eval 中最低可以到达到 0.05）

后续还会继续更新这个模型
