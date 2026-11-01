---
language:
- en
- ko
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- llama-2-chat
license: apache-2.0
---
# komt : korean multi task instruction tuning model
![multi task instruction tuning.jpg](https://github.com/davidkim205/komt/assets/16680469/c7f6ade7-247e-4b62-a94f-47e19abea68e)

Recently, due to the success of ChatGPT, numerous large language models have emerged in an attempt to catch up with ChatGPT's capabilities. 
However, when it comes to Korean language performance, it has been observed that many models still struggle to provide accurate answers or generate Korean text effectively. 
This study addresses these challenges by introducing a multi-task instruction technique that leverages supervised datasets from various tasks to create training data for Large Language Models (LLMs).

## Model Details

* **Model Developers** :  davidkim(changyeon kim)
* **Repository** : https://github.com/davidkim205/komt
* **quant methods** : q4_0, q4_1, q5_0, q5_1, q2_k, q3_k, q3_k_m, q3_k_l, q4_k, q4_k_s, q4_k_m, q5_k, q5_k_s, q5_k_m, q8_0, q4_0


## Training
Refer https://github.com/davidkim205/komt

## Evaluation
For objective model evaluation, we initially used EleutherAI's lm-evaluation-harness but obtained unsatisfactory results. Consequently, we conducted evaluations using ChatGPT, a widely used model, as described in [Self-Alignment with Instruction Backtranslation](https://arxiv.org/pdf/2308.06502.pdf) and [Three Ways of Using Large Language Models to Evaluate Chat](https://arxiv.org/pdf/2308.06259.pdf) .

| model                                   | score   | average(0~5) | percentage |
| --------------------------------------- | ------- | ------------ | ---------- |
| gpt-3.5-turbo(close)                    | 147     | 3.97         | 79.45%     |
| naver Cue(close)                        | 140     | 3.78         | 75.67%     |
| clova X(close)                          | 136     | 3.67         | 73.51%     |
| WizardLM-13B-V1.2(open)                 | 96      | 2.59         | 51.89%     |
| Llama-2-7b-chat-hf(open)                | 67      | 1.81         | 36.21%     |
| Llama-2-13b-chat-hf(open)               | 73      | 1.91         | 38.37%     |
| nlpai-lab/kullm-polyglot-12.8b-v2(open) | 70      | 1.89         | 37.83%     |
| kfkas/Llama-2-ko-7b-Chat(open)          | 96      | 2.59         | 51.89%     |
| beomi/KoAlpaca-Polyglot-12.8B(open)     | 100     | 2.70         | 54.05%     |
| **komt-llama2-7b-v1 (open)(ours)**      | **117** | **3.16**     | **63.24%** |
| **komt-llama2-13b-v1  (open)(ours)**    | **129** | **3.48**     | **69.72%** |

