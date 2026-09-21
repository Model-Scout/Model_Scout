---
language:
- en
- ko
pipeline_tag: text-generation

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

## usage
```
cd llama.cpp
make -j && ./main -m ./models/komt-mistral-7b-v1/ggml-model-q4_1.gguf -p "[INST]인삼은 어떤 효과가 있는가요? [/INST]"
```
output
```
[INST]인삼은 어떤 효과가 있는가요? [/INST]인삼에는 약 600개의 물질이 포함되어 있습니다. 그 중에서도 많은 연구들을 통해 효능을 확인한 것으로 알려진 3가지는 아래와 같습니다.
1. 혈압 조절: 각종 실험에서 인삼이 혈압을 조절하는데 효과를 나타냈으며, 특히 중국의 한 연구자들은 인삼을 사용해 40%의 혈압 감소를 보였습니다.
2. 위장 개선: 인삼은 흉터, 통증 등으로 고통받는 위장 질환을 일부나마 개선할 수 있는데, 이는 각종 실험들에서 확인된 것입니다.
3. 면역 강화: 인삼은 면역체계를 강화시키는데 효과가 있으며, 국내에서도 2014년부터는 식약처의 의약용품 수출증명제에 대한 최종적인 평가로 사용되고 있습니다.
위와 같은 효능을 갖춘 인삼은 많이 사용하는 건강식품의 원료로도 활용됩니다. [end of text]
```
## Evaluation
For objective model evaluation, we initially used EleutherAI's lm-evaluation-harness but obtained unsatisfactory results. Consequently, we conducted evaluations using ChatGPT, a widely used model, as described in [Self-Alignment with Instruction Backtranslation](https://arxiv.org/pdf/2308.06502.pdf) and [Three Ways of Using Large Language Models to Evaluate Chat](https://arxiv.org/pdf/2308.06259.pdf) .



| model                                   | score   | average(0~5) | percentage |
| --------------------------------------- |---------| ------------ | ---------- |
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
| **komt-llama-30b-v1  (open)(ours)**    | **129** | **3.16**     | **63.24%** |
| **komt-mistral-7b-v1  (open)(ours)**    | **131** | **3.54**     | **70.81%** |

