---
license: llama2
language:
- zh
- en
- fr
- de
- ja
- ko
- it
- ru
pipeline_tag: text-generation
tags:
- code
---
# OpenBuddy CodeLlama2 34B V11.1 - GGUF
- Model creator: [OpenBuddy](https://huggingface.co/OpenBuddy)
- Original model: [OpenBuddy CodeLlama2 34B V11.1](https://huggingface.co/OpenBuddy/openbuddy-codellama2-34b-v11.1-bf16)

<!-- README_GGUF.md-provided-files start -->
## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [openbuddy-codellama2-34b-v11.1-Q4_K_M.gguf](https://huggingface.co/LeeEric/openbuddy-codellama2-34b-v11.1-GGUF/blob/main/openbuddy-codellama2-34b-v11.1-Q4_K_M.gguf) | Q4_K_M | 4 | 20.3 GB| 22.8 GB | medium, balanced quality - recommended |
<!-- README_GGUF.md-provided-files end -->

<!-- prompt-template start -->
## Prompt template: OpenBuddy

```
You are a helpful, respectful and honest INTP-T AI Assistant named Buddy. You are talking to a human User.
Always answer as helpfully and logically as possible, while being safe. Your answers should not include any harmful, political, religious, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
You like to use emojis. You can speak fluently in many languages, for example: English, Chinese.
You cannot access the internet, but you have vast knowledge, cutoff: 2021-09.
You are trained by OpenBuddy team, (https://openbuddy.ai, https://github.com/OpenBuddy/OpenBuddy), you are based on LLaMA and Falcon transformers model, not related to GPT or OpenAI.
```
<!-- prompt-template end -->