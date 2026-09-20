---
base_model: 01-ai/Yi-1.5-9B-Chat-16K
license: apache-2.0
pipeline_tag: text-generation
language:
- zh
- en
tags:
- llm
- long context
- yi
- chat
- it
- abliterated
library_name: transformers
---



# Yi-1.5-9B-Chat-16K-abliterated

# Note: This abliterated model (no finetuning) beats the original model on the LLM Leaderboard.

| Model                                         | Average | IFEval | BBH   | MATH Lvl 5 | GPQA | MUSR  | MMLU-PRO |
|-----------------------------------------------|:-------:|:------:|:-----:|:----------:|:----:|:-----:|:--------:|
| byroneverson/Yi-1.5-9B-Chat-16K-abliterated   | 26.37   | 55.28  | 32.84 | 10.65      | 8.39 | 19.68 | 31.37    |
| 01-ai/Yi-1.5-9B-Chat-16K                      | 22.9    | 42.14  | 31.5  | 12.61      | 7.83 | 10.04 | 33.26    |

Check out the <a href="https://huggingface.co/byroneverson/Yi-1.5-9B-Chat-16K-abliterated/blob/main/abliterate-yi-1-5-9b-chat-16k.ipynb">jupyter notebook</a> for details of how this model was abliterated from Yi-1.5-9B-Chat-16K.

![Logo](https://huggingface.co/byroneverson/Yi-1.5-9B-Chat-16K-abliterated/resolve/main/logo.png "Logo")