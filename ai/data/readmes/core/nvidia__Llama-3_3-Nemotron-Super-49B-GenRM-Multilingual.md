---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
inference: false
fine-tuning: false
language:
- en
- zh
- ko
- fr
- es
- ru
- ja
- de
- it
- pt
- pl
- id
- nl
- vi
tags:
  - nvidia
  - llama3.3
datasets:
  - nvidia/HelpSteer3
base_model: nvidia/Llama-3_3-Nemotron-Super-49B-v1
library_name: transformers
---

# Model Overview

## Description:

Llama-3.3-Nemotron-Super-49B-GenRM-Multilingual is a generative reward model that leverages Llama-3.3-Nemotron-Super-49B-v1 as the foundation and is fine-tuned using Reinforcement Learning to predict the quality of LLM generated responses.

Llama-3.3-Nemotron-Super-49B-GenRM-Multilingual can be used to judge the quality of one response, or the ranking between two responses given a multilingual conversation history. It will first generate reasoning traces then output an integer score. A higher score means the response is of higher quality.

See details on how this model was trained at [https://arxiv.org/abs/2505.11475](https://arxiv.org/abs/2505.11475)

This model is ready for commercial/non-commercial use.

## License/Terms of Use:

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) . Additional Information: [Llama 3.3 Community License Agreement](https://www.llama.com/llama3_3/license/). Built with Llama.

### Deployment Geography

Global

## Use Case:

Llama-3.3-Nemotron-Super-49B-GenRM-Multilingual can be used to judge the quality of one response, or the ranking between two responses given a multilingual conversation history. It will first generate reasoning traces then output an integer score.

## Release Date:

HuggingFace 06/27/2025 via https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual

## References:

* [HelpSteer3-Preference](https://arxiv.org/abs/2505.11475)
* [HelpSteer2-Preference](https://arxiv.org/abs/2410.01257)
* [SteerLM method](https://arxiv.org/abs/2310.05344)
* [HelpSteer](https://arxiv.org/abs/2311.09528)
* [HelpSteer2](https://arxiv.org/abs/2406.08673)
* [Llama-Nemotron: Efficient Reasoning Models](https://arxiv.org/abs/2505.00949)
* [The future of AI: Built with Llama](https://ai.meta.com/blog/future-of-ai-built-with-llama/) 
* [Meta's Llama 3.3 Webpage](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3) 
* [Meta's Llama 3.3 Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md)


## RM-Bench LeaderBoard

As of 15 May 2025, our reward models trained with HelpSteer3-Preference are the top performing Bradley-Terry reward models on [RM-Bench](https://arxiv.org/abs/2410.16184), an improved variant of RewardBench for evaluating Reward Models in Chat, Math, Code and Safety. Our GenRMs also outperform the corresponding Bradley-Terry reward models.

| Model  |  Chat | Math | Code | Safety | Easy | Normal | Hard | Overall RM-Bench|
|:-----------------------------|:------|:------|:------|:------|:------|:------|:------|:------|
| **[Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual)**  | **77.2** | 91.9 | 74.7 | 92.9 | 90.7 | 86.7 | 75.1	| 84.2 |
| + voting@32 | 76.3 | **93.2** | **79.0** | 93.5 | 92.1 | **88.5** | 75.9 | **85.5** | 
| **[Llama-3_3-Nemotron-Super-49B-GenRM](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM)**  |73.7 | 91.4 | 75.0 | 90.6 | 91.2 | 85.7 | 71.2 | 82.7 | 
| + voting@32 | 74.0 | 92.7 | 77.4 | 92.1 | **92.6** | 87.3 | 72.3 | 84.0 |
| **[Llama-3.3-Nemotron-70B-Reward-Multilingual](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual/)**  | **86.2** | 82.4 | 66.8 | 94.1 | 86.5 | 85.4 | **80.0**	| 82.4 |
| **[Llama-3.3-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward)**  |75.4 | 84.5 | 69.3 | 90.4 | 92.1 | 85.7 |71.1 | 79.9|
| [Llama-3.1-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward) | 70.7 | 64.3 | 57.4 | 90.3 | 92.2	| 76.8 | 48.0 | 70.7 |
| [Skywork-Reward-Gemma-2-27B](https://huggingface.co/Skywork/Skywork-Reward-Gemma-2-27B) | 71.8 | 59.2 | 56.6 | 94.3 | 89.6 | 75.4 | 50.0 | 70.5 |
| [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B)  | 69.5 | 60.6 |  54.5 |**95.7** | 89.0 | 74.7 | 46.6 | 70.1 | 

*Note that Skywork-Reward-Llama-3.1-8B was the best performing reward model reported on RM-Bench and we evaluated all other models.* 

## JudgeBench LeaderBoard

As of 15 May 2025, our reward models trained with HelpSteer3-Preference are the top performing Bradley-Terry reward models on [JudgeBench](https://huggingface.co/spaces/ScalerLab/JudgeBench), a popular benchmark for evaluating LLM-as-a-judge applications relating to General Knowledge, Logical Reasoning, Math and Coding. Our GenRMs also outperform the corresponding Bradley-Terry reward models.
 
 | Model  |  Knowl.| Reason.| Math | Code | Overall JudgeBench |
 |:-----------------------------|:------|:------|:------|:------|:------|
 | **[Llama-3_3-Nemotron-Super-49B-GenRM](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM)**  |**71.4** | 73.5 | **87.5** | 76.2 | 75.1| 
 | + voting@32 | 70.8 | **83.7** | **87.5** | 83.3 | **78.6**|
 | **[Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual)**  | 64.9 | 74.5 | **87.5** | 73.8 | 72.3 |
 | + voting@32 | 65.6 | 82.7 | **87.5** | **85.7** | 76.3 | 
 | **[Llama-3.3-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward)**  |70.8 | 76.5 | 82.1 | 66.7 |73.7 |
 | **[Llama-3.3-Nemotron-70B-Reward-Multilingual](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual)**  |66.2 | 71.4 | 82.1 |59.5 | 69.4|
 | [Llama-3.1-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward) |62.3 | 72.5 | 76.8 | 57.1 | 66.9 |
 | [Skywork-Reward-Gemma-2-27B](https://huggingface.co/Skywork/Skywork-Reward-Gemma-2-27B) |  59.7 | 66.3 | 83.9 | 50.0	| 64.3 |
 | [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B) | 59.1 | 64.3 |  76.8 | 50.0 | 62.3 |

*Note that Skywork-Reward-Gemma-2-27B was the best performing reward model reported on JudgeBench and we evaluated all other numbers.* 


## Model Architecture: 
**Architecture Type:** Transformer <br>
**Network Architecture:** Llama-3.3-Nemotron-Super-49B-v1 <br>

We developed this model using [Llama-3.3-Nemotron-Super-49B-v1](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1) as its foundation. This model contains 49 billion parameters.

## Input:
**Input Type(s):** Text <br>
**Input Format:** String <br>
**Input Parameters:** One Dimensional (1D) <br>
**Other Properties Related to Input:** Max of 128k tokens<br>

## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:**  The output contains a reasoning trace and a final score. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>

## Software Integration:
**Runtime Engine(s):** <br>
* vLLM 0.8.3 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper <br>

**Supported Operating System(s):** Linux <br>

## Quick Start

We recommend serving the model with vLLM. You can use the model with 2 or more 80GB GPUs (NVIDIA Ampere or newer) with at least 100GB of free disk space to accommodate the download.

```
pip install vllm==0.8.3
```
```
python3 -m vllm.entrypoints.openai.api_server \
  --model "nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual" \
  --trust-remote-code \
  --seed=1 \
  --host="0.0.0.0" \
  --port=5000 \
  --served-model-name "nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual" \
  --tensor-parallel-size=8 \
  --max-model-len=40000 \
  --gpu-memory-utilization 0.95 \
  --enforce-eager
```

Now you can query the model, here is an example:
```python
from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:5000/v1", api_key="dummy")

# when judging one response
msg = [
  {"role": "user", "content": "What is 1+1?"}, 
  {"role": "assistant", "content": "1+1=2"}, 
  {"role": "user", "content": "What about 1+2?"},
  {"role": "response_1", "content": "1+2=4"}
]

completion = client.chat.completions.create(
    model="nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual",
    messages=msg,
    temperature=0.0,
    top_p=1.0,
    max_tokens=32768,
    stream=False
)
output = completion.choices[0].message.content
print(output.split("</think>")[-1].strip())
"""
[The Begin of Analysis on Response 1]
Response 1 states "1+2=4", which is incorrect because the correct result of 1+2 is 3. While the response is clear and directly addresses the query, its **Correctness/Completeness** is severely flawed due to the error. The mistake makes the response **Not Helpful** as it fails to provide the accurate information requested. Other factors like **Coherence** and **Relevance** are satisfactory, but the critical inaccuracy outweighs these.
[The End of Analysis on Response 1]

[The Begin of Individual Scores]
\boxed{1}
[The End of Individual Scores]
"""
# when judging two responses
msg = [
  {"role": "user", "content": "What is 1+1?"}, 
  {"role": "assistant", "content": "1+1=2"}, 
  {"role": "user", "content": "What about 1+2?"},
  {"role": "response_1", "content": "1+2=4"},
  {"role": "response_2", "content": "1+2=3"}
]

completion = client.chat.completions.create(
    model="nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual",
    messages=msg,
    temperature=0.0,
    top_p=1.0,
    max_tokens=32768,
    stream=False
)
output = completion.choices[0].message.content
print(output.split("</think>")[-1].strip())
"""
[The Begin of Analysis on Response 1]
Response 1 states "1+2=4", which is mathematically incorrect. The correct answer is 3. While the response is clear and concise, its incorrectness makes it completely unhelpful. It fails in Correctness/Completeness, Instruction following, and Relevance due to the error. There is no redeeming value as it provides false information.
[The End of Analysis on Response 1]

[The Begin of Analysis on Response 2]
Response 2 states "1+2=3", which is accurate and directly addresses the user's query. It is clear, concise, and fully aligned with the request. There is no unnecessary information, and it demonstrates perfect correctness without hallucination. This response meets all criteria for helpfulness.
[The End of Analysis on Response 2]

[The Begin of Individual Scores]
\boxed{1, 5}
[The End of Individual Scores]

[The Begin of Ranking Score]
\boxed{5}
[The End of Ranking Score]
"""
```
Note that the conversation history should be presented in "user" and "assistant" roles, where the last turn is user turn. The responses to be judged should be in "response_1" (and "response_2") roles.

### Interpretation of Scores
When judging one response, the model will generate a helpfulness score from 1 to 5, where higher is better.

When judging two responses, the model will generate an individual helpfulness score for each response, then a ranking score. The ranking score is a number between 1 and 6, where:

1 = Response 1 is much better than Response 2

2 = Response 1 is better than Response 2

3 = Response 1 is slightly better than Response 2

4 = Response 2 is slightly better than Response 1

5 = Response 2 is better than Response 1

6 = Response 2 is much better than Response 1

For details, please see Appendix J in our [paper](https://arxiv.org/abs/2505.11475).

## Model Version: 
v1.0

# Training, Testing and Evaluation Datasets: 

## Training Datasets:

**Dataset Name:** HelpSteer3 <br>
**Dataset Link:** https://huggingface.co/datasets/nvidia/HelpSteer3

**Data Collection Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Labeling Method by dataset** <br>
* [Human] <br>

**Properties:** <br>
* 7,660 prompts, each with a pair of responses as well as human preferences between the pair of responses.

## Testing Datasets:

**Dataset Name:** HelpSteer3 <br>
**Dataset Link:** https://huggingface.co/datasets/nvidia/HelpSteer3

**Data Collection Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Labeling Method by dataset** <br>
* [Human] <br>

**Properties:** <br>
* 403 prompts, each with a pair of responses as well as human preferences between the pair of responses.

## Evaluation Datasets

**Dataset Name:** RM-Bench <br>
**Dataset Link:** https://huggingface.co/datasets/THU-KEG/RM-Bench

**Data Collection Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Labeling Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Properties:** <br>
* 1,327 prompts, each with three pairs of responses as well as preferences between the pair of responses.


**Dataset Name:** JudgeBench <br>
**Dataset Link:** https://huggingface.co/datasets/ScalerLab/JudgeBench

**Data Collection Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Labeling Method by dataset** <br>
* [Hybrid: Human, Synthetic] <br>

**Properties:** <br>
* 350 prompts, each with a pair of responses as well as preferences between the pair of responses.


# Inference:
**Engine:** vLLM <br>
**Test Hardware:** H100, A100 80GB, A100 40GB <br>


## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 
For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](explainability.md), [Bias](bias.md), [Safety & Security](safety.md), and [Privacy](privacy.md) Subcards.  

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Citation

If you find this model useful, please cite the following work:

```bibtex
@misc{wang2025helpsteer3preferenceopenhumanannotatedpreference,
      title={Help{S}teer3-{P}reference: Open Human-Annotated Preference Data across Diverse Tasks and Languages},
      author={Zhilin Wang and Jiaqi Zeng and Olivier Delalleau and Hoo-Chang Shin and Felipe Soares and Alexander Bukharin and Ellie Evans and Yi Dong and Oleksii Kuchaiev},
      year={2025},
      eprint={2505.11475},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.11475}, 
}
```

