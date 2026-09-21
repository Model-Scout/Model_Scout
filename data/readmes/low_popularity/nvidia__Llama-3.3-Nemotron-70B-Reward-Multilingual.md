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
base_model: meta-llama/Llama-3.3-70B-Instruct
library_name: transformers
---

# Model Overview

## Description:

Llama-3.3-Nemotron-70B-Reward-Multilingual is a large language model that leverages Meta-Llama-3.3-70B-Instruct as the foundation and is fine-tuned using scaled Bradley-Terry modeling to predict the quality of LLM generated responses.

Given a multilingual conversation with multiple turns between user and assistant (of up to 4,096 tokens), it rates the quality of the final assistant turn using a reward score.

For the same prompt, a response with higher reward score has higher quality than another response with a lower reward score, but the same cannot be said when comparing the scores between responses to different prompts.

As of 15 May 2025, this model achieves the highest on [RM-Bench](https://arxiv.org/abs/2410.16184) at 82.4% and second highest [JudgeBench](https://huggingface.co/spaces/ScalerLab/JudgeBench) at 69.4% among Bradley-Terry Reward Models.

See details on how this model was trained at [https://arxiv.org/abs/2505.11475](https://arxiv.org/abs/2505.11475)

This model is ready for commercial/non-commercial use.

## License/Terms of Use:

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) . Additional Information: [Llama 3.3 Community License Agreement](https://www.llama.com/llama3_3/license/). Built with Llama.

### Deployment Geography

Global

## Use Case:

Llama-3.3-Nemotron-70B-Reward-Multilingual labels an LLM-generated response to a user query with a reward score.

## Release Date:

HuggingFace 06/27/2025 via https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual

## References:

* [HelpSteer3-Preference](https://arxiv.org/abs/2505.11475)
* [HelpSteer2-Preference](https://arxiv.org/abs/2410.01257)
* [SteerLM method](https://arxiv.org/abs/2310.05344)
* [HelpSteer](https://arxiv.org/abs/2311.09528)
* [HelpSteer2](https://arxiv.org/abs/2406.08673)
* [The future of AI: Built with Llama](https://ai.meta.com/blog/future-of-ai-built-with-llama/) 
* [Meta's Llama 3.3 Webpage](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3) 
* [Meta's Llama 3.3 Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md)

## RM-Bench LeaderBoard

As of 15 May 2025, our reward models trained with HelpSteer3-Preference are the top performing Bradley-Terry reward models on [RM-Bench](https://arxiv.org/abs/2410.16184), an improved variant of RewardBench for evaluating Reward Models in Chat, Math, Code and Safety.

| Model  |  Chat | Math | Code | Safety | Easy | Normal | Hard | Overall RM-Bench|
|:-----------------------------|:------|:------|:------|:------|:------|:------|:------|:------|
| **[Llama-3.3-Nemotron-70B-Reward-Multilingual](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual/)**  | **86.2** | 82.4 | 66.8 | 94.1 | 86.5 | 85.4 | **80.0**	| **82.4** |
| **[Llama-3.3-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward)**  |75.4 | **84.5** | **69.3** | 90.4 | 92.1 | **85.7** |71.1 | 79.9|
| [Llama-3.1-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward) | 70.7 | 64.3 | 57.4 | 90.3 | **92.2**	| 76.8 | 48.0 | 70.7 |
| [Skywork-Reward-Gemma-2-27B](https://huggingface.co/Skywork/Skywork-Reward-Gemma-2-27B) | 71.8 | 59.2 | 56.6 | 94.3 | 89.6 | 75.4 | 50.0 | 70.5 |
| [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B)  | 69.5 | 60.6 |  54.5 |**95.7** | 89.0 | 74.7 | 46.6 | 70.1 | 

*Note that Skywork-Reward-Llama-3.1-8B was the best performing reward model reported on RM-Bench and we evaluated all other models.* 

## JudgeBench LeaderBoard

As of 15 May 2025, our reward models trained with HelpSteer3-Preference are the top performing Bradley-Terry reward models on [JudgeBench](https://huggingface.co/spaces/ScalerLab/JudgeBench), a popular benchmark for evaluating LLM-as-a-judge applications relating to General Knowledge, Logical Reasoning, Math and Coding.
 
 | Model  |  Knowl.| Reason.| Math | Code | Overall JudgeBench |
 |:-----------------------------|:------|:------|:------|:------|:------|
 | **[Llama-3.3-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward)**  |**70.8** |**76.5** | 82.1 | **66.7** |**73.7** |
 | **[Llama-3.3-Nemotron-70B-Reward-Multilingual](https://huggingface.co/nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual)**  |66.2 | 71.4 | 82.1 |59.5 | 69.4|
 | [Llama-3.1-Nemotron-70B-Reward](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward) |62.3 | 72.5 | 76.8 | 57.1 | 66.9 |
 | [Skywork-Reward-Gemma-2-27B](https://huggingface.co/Skywork/Skywork-Reward-Gemma-2-27B) |  59.7 | 66.3 | **83.9** | 50.0	| 64.3 |
 | [Skywork-Reward-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B) | 59.1 | 64.3 |  76.8 | 50.0 | 62.3 |

*Note that Skywork-Reward-Gemma-2-27B was the best performing reward model reported on JudgeBench and we evaluated all other models.* 


## Model Architecture: 
**Architecture Type:** Transformer <br>
**Network Architecture:** Llama 3.3 <br>

We developed this model using [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) as its foundation. This model contains 70 billion parameters.

## Input:
**Input Type(s):** Text <br>
**Input Format:** String <br>
**Input Parameters:** One Dimensional (1D) <br>
**Other Properties Related to Input:** Max of 128k tokens (but trained only on conversations up to 4K tokens)<br>

## Output:
**Output Type(s):** Float <br>
**Output Format:** One Single Float <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:**  The float value represents the quality of the response, with a higher value representing higher quality. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>

## Software Integration:
**Runtime Engine(s):** <br>
* [NeMo - 24.05.llama.3.1] <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper <br>
* NVIDIA Turing <br>

**Supported Operating System(s):** Linux <br>

## Quick Start

You can use the model using HuggingFace Transformers library with 2 or more 80GB GPUs (NVIDIA Ampere or newer) with at least 150GB of free disk space to accomodate the download.

This code has been tested on Transformers v4.45.0, torch v2.3.0a0+40ec155e58.nv24.3 and 2 H100 80GB GPUs, but any setup that supports meta-llama/Llama-3.1-70B-Instruct should support this model as well. If you run into problems, you can consider doing pip install -U transformers.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "nvidia/Llama-3.3-Nemotron-70B-Reward-Multilingual"

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "What is 1+1?"
good_response = "1+1=2"
bad_response = "1+1=3"

for response in [good_response, bad_response]:
    messages = [{'role': "user", "content": prompt}, {'role': "assistant", "content": response}]
    tokenized_message = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=False, return_tensors="pt", return_dict=True)
    response_token_ids = model.generate(tokenized_message['input_ids'].cuda(),attention_mask=tokenized_message['attention_mask'].cuda(),  max_new_tokens=1, return_dict_in_generate=True, output_scores=True)
    reward = response_token_ids['scores'][0][0][0].item()
    print(reward)

# Example quality - note that higher scores means higher quality, and scores can be negative.

# reward for good_response = 6.46875
# reward for bad_response = -1.8828125
```

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
**Engine:** PyTorch <br>
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