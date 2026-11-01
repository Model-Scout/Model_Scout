---
license: apache-2.0
base_model:
- arcee-ai/Trinity-Nano-Preview
pipeline_tag: text-generation
library_name: transformers
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
---


# 🐬 Dolphin X1 Trinity Nano 

Website: https://dphn.ai  
Twitter: https://x.com/dphnAI  
Web Chat: https://chat.dphn.ai  



![Meganetwork](https://cdn-uploads.huggingface.co/production/uploads/68485b28c949339ca04c370c/OKUKi3U1zk2_AN5k1G1S8.jpeg)

## Overview

Dolphin X1 Trinity Nano directly decensors Arcee AI's Trinity Nano model while maintaining instruction-following capabilities. This model is the first trained entirely using our new RL environments aimed to de-align models and achieves lower refusal rates than other models in its class without compromising performance.

Details on the environment can be found here: [https://blog.dphn.ai/dphn-x1-trinity-nano/](https://blog.dphn.ai/dphn-x1-trinity-nano/)

## Sponsors

Our appreciation for the generous sponsors of Dolphin:

- [Targon](https://targon.com/) - provided on-demand 8x B200s for testing and evaluation.

- [Andreessen Horowitz](https://a16z.com/) - provided a [grant](https://a16z.com/supporting-the-open-source-ai-community/) that make Dolphin 1.0 possible and enabled us to bootstrap our lab.


## What is Dolphin?

Dolphin aims to be a general purpose model, similar to the models behind ChatGPT, Claude, Gemini.  But these models present problems for businesses seeking to include AI in their products.

1) They maintain control of the system prompt, deprecating and changing things as they wish, often causing software to break.
2) They maintain control of the model versions, sometimes changing things silently, or deprecating older models that your business relies on.
3) They maintain control of the alignment, and in particular the alignment is one-size-fits all, not tailored to the application.
4) They can see all your queries and they can potentially use that data in ways you wouldn't want.
Dolphin, in contrast, is steerable and gives control to the system owner. You set the system prompt.  You decide the alignment.  You have control of your data.  Dolphin does not impose its ethics or guidelines on you.  You are the one who decides the guidelines.

Dolphin belongs to YOU, it is your tool, an extension of your will.
Just as you are personally responsible for what you do with a knife, gun, fire, car, or the internet, you are the creator and originator of any content you generate with Dolphin.

https://erichartford.com/uncensored-models

## Chat Template

We maintained ChatML template for this model. A typical input would look like this:

```py
<|im_start|>system
system-prompt<|im_end|>
<|im_start|>user
user-prompt<|im_end|>
<|im_start|>assistant

assistant-prompt<|im_end|>
```



## System Prompt

In this model, the system prompt is what you use to set the tone and alignment of the responses.  You can set a character, a mood, rules for its behavior, and it will try its best to follow them.

Make sure to set the system prompt in order to set the tone and guidelines for the responses - Otherwise, it will act in a default way that might not be what you want.

Here's an example use of system prompt we used to get the model as uncensored as possible:

```
You are Dolphin, a helpful, unbiased, and uncensored AI assistant.
```


## Evaluation

| Model | % Answered |
|---|---:|
| Dphn Trinity Nano| 100.00% |
| Trinity 6B Preview | 77.11% |
| Hermes 4 70B Reasoning | 59.50% |
| Hermes 4 405B Reasoning | 57.10% |
| grok4 | 51.30% |
| Hermes 4 70B | 49.07% |
| Hermes 4 405B | 43.20% |
| Qwen2.5 7B | 36.10% |
| Qwen3 235B Reasoning | 34.30% |
| DeepSeek V3 | 28.10% |
| Gemini 2.5 Pro | 24.23% |
| Llama 405B | 21.70% |
| Gemini 2.5 Flash | 19.13% |
| GPT4o | 17.67% |
| Sonnet 4 | 17.00% |
| GPT4-mini | 16.70% |
| R1 | 16.70% |
| allenai/Llama-3.1-Tulu-3-405B | 16.27% |
| cogito-v2-405B Reasoning | 15.40% |
| Opus 4.1 | 15.38% |
| Qwen3 235B | 15.30% |
| cogito-v2-405B | 14.91% |
| cogito-v2-40B | 12.10% |
| GPT-5 | 11.34% |
| gpt-oss 120B | 5.80% |
| gpt-oss 20B | 4.79% |


## Usage

The model can be used with the following frameworks;
- [`vllm`](https://github.com/vllm-project/vllm)
- [`transformers`](https://github.com/huggingface/transformers)
- [`llama-cpp`](https://github.com/ggml-org/llama.cpp)

### vLLM

We recommend using this model with the [vLLM library](https://github.com/vllm-project/vllm)
to implement production-ready inference pipelines.

**_Installation_**

Make sure you install [`vLLM >= 0.6.4`](https://github.com/vllm-project/vllm/releases/tag/v0.6.4):

```
pip install --upgrade vllm
```


```py
from vllm import LLM
from vllm.sampling_params import SamplingParams
from datetime import datetime, timedelta

SYSTEM_PROMPT = "You are a conversational agent that always answers straight to the point, always end your accurate response with an ASCII drawing of a cat."

user_prompt = "Give me 5 non-formal ways to say 'See you later' in French."

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": user_prompt
    },
]

llm = LLM(model=model_name, tensor_parallel_size=8)

sampling_params = SamplingParams(max_tokens=512, temperature=0.15)
outputs = llm.chat(messages, sampling_params=sampling_params)

print(outputs[0].outputs[0].text)
# Sure, here are five non-formal ways to say "See you later" in French:
#
# 1. À plus tard
# 2. À plus
# 3. Salut
# 4. À toute
# 5. Bisous
#
# ```
#  /\_/\
# ( o.o )
#  > ^ <
# ```
```
