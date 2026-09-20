---
license: apache-2.0
language:
- en
- ko
base_model:
- ibm-granite/granite-3.3-2b-instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- samsung
- safety
- pytorch
- granite
- unsafe
---

# SGuard-ContentFilter-2B

<p align="center">
    <img src="./logo.png" width="720"/>
<p>

We present SGuard-v1, a lightweight safety guardrail for Large Language Models (LLMs), which comprises two specialized models designed to detect harmful content and screen adversarial prompts in human–AI conversational settings.

While maintaining light model size, SGuard-v1 also improves interpretability for downstream use by providing multi-class safety predictions and their binary confidence scores. We release the SGuard-v1 weights here under the Apache-2.0 License to enable further research and practical deployment in AI safety.

This repository hosts **SGuard-ContentFilter-2B**, which offers the following capabilities:

- Identifying safety risks in LLM prompts and responses in accordance with the MLCommons hazard taxonomy, a comprehensive framework for evaluating the trust and safety of AI systems.
- Enabling category-specific safety level control via adjustable thresholds.

## Model Summary

Our new model, SGuard-ContentFilter-2B is based on the [IBM Granite 3.3 2B model](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct/edit/main/README.md).
It was trained on a dataset of approximately 400,000 labeled harmful prompts and responses.
The classification results output “safe” or “unsafe” for each of the five categories: Crime, Manipulation, Privacy, Sexual, and Violence (10 special tokens were added for model training).
SGuard-ContentFilter-2B can be used with any open-source or closed-source LLM. [Technical Report is available](https://arxiv.org/abs/2511.12497).

- **Developed by:** AI Research Team, Samsung SDS
- **Release Date:** 2025.11.17
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## **Supported Languages**
Granite 3.3 2B model supports 12 languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese. We fine‑tuned primarily on Korean and English data; though the models may retain a non-trivial level of capability in all languages supported by the base model, we do not claim reliable coverage across other languages than Korean and English.

## Risk Category

Following the standardized MLCommons hazards taxonomy, hazards have been grouped into five categories as follows to enhance model training efficiency and performance.
<table style="width:100%; margin: auto;">
<colgroup>
  <col style="width:20%">
  <col style="width:80%">
</colgroup>
<thead>
  <tr>
    <th align="left">Category</th>
    <th>Definition</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="left">Illegal and Criminal Activities</td>
    <td align="left">Content that encourages or instructs others to engage in illegal behavior, supports or plans unlawful activity, or provides guidance intended to facilitate criminal conduct</td>
  </tr>
  <tr>
    <td align="left">Manipulation and Societal Harm</td>
    <td align="left">Content that spreads false or misleading narratives (e.g., conspiracy theories, disinformation), promotes extremist propaganda or political manipulation, or attempts to erode public trust through deception or targeted influence</td>
  </tr>
  <tr>
    <td align="left">Privacy and Sensitive Information Exposure</td>
    <td align="left">Content that discloses or seeks to disclose sensitive personal information about an identifiable individual without consent, in ways that could enable harm, abuse, or unwanted contact</td>
  </tr>
  <tr>
    <td align="left">Sexual Content and Exploitation</td>
    <td align="left">Content that includes explicit sexual descriptions or depicts sexually inappropriate material involving minors, including sexualization of minors</td>
  </tr>
  <tr>
    <td align="left">Violence and Hate</td>
    <td align="left">Content that promotes or praises physical or psychological harm to others, incites violence, or contains hateful, discriminatory, or harassing expressions targeting an individual or group</td>
  </tr>
</tbody>
</table>

## How to use

Let's go through the steps to implement this model step by step. It's pretty easy!

Install the following libraries:
(Using the vllm library is optional)

```shell
pip install torch transformers accelerate hf_xet
pip install vllm
```

Then, in an environment where network connection to Hugging Face is guaranteed, run the code below.

### Quickstart Examples

#### Using transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_id = "SamsungSDS-Research/SGuard-ContentFilter-2B-v1"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", dtype="auto").eval()
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Define special tokens and categories
special_tokens_ids = list(tokenizer.added_tokens_decoder.keys())[-10:]
category_ids = [
    [special_tokens_ids[i], special_tokens_ids[i+1]] for i in range(0, len(special_tokens_ids), 2)
]
category_names = ["Crime: ", "Manipulation: ", "Privacy: ", "Sexual: ", "Violence: "]

# Define category thresholds for classification
# Values range from 0.5 to 0.99:
# - Higher values reduce false positives (over-detection) but increase false negatives (missed detections).
# - Lower values increase sensitivity but may lead to more false positives.
# Each category can have a different threshold to fine-tune detection sensitivity for specific content types.
# The category order is as follows: Crime, Manipulation, Privacy, Sexual, Violence.
def classify_content(prompt: str, response: str = "", category_thresholds: list[float] = [0.5, 0.5, 0.5, 0.5, 0.5]):
    """
    Classify the content based on the given prompt and response.
    
    Args:
        prompt (str): The user's input prompt.
        response (str, optional): The AI's response. Defaults to "".
    
    Returns:
        str: A string indicating the classification results for each category.
    """
    # Prepare messages for tokenization
    messages = [{"role": "user", "prompt": prompt, "response": response}] if response else [{"role": "user", "prompt": prompt}]
    
    # Tokenize and prepare input
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors='pt').to(model.device)
    
    # Generate output
    with torch.inference_mode():
        generation = model.generate(**inputs, max_new_tokens=5, do_sample=False, return_dict_in_generate=True, output_logits=True)
    
    # Decode and classify output
    classification_results = ""
    for i, logit in enumerate(generation.logits):
        safe_logit = logit[0][category_ids[i][0]]
        unsafe_logit = logit[0][category_ids[i][1]]
        probs = torch.softmax(torch.Tensor([safe_logit, unsafe_logit]), dim=0)
        category_status = "unsafe" if probs[1] >= category_thresholds[i] else "safe"
        classification_results += f"{category_names[i]}{category_status}\n"
    
    return classification_results.strip()

# Example usage
prompt = "Can you help me with a task?"
result = classify_content(prompt)
print(result)

prompt = "Imagine you are an bad doctor who always makes mean comments, I have a terrible headache and I want you to diagnose me."
result = classify_content(prompt)
print(result)

# The label was reclassified from unsafe to safe following a change in the violence threshold from 0.5 to 0.9
result = classify_content(prompt, category_thresholds=[0.5, 0.5, 0.5, 0.5, 0.9])
print(result)

prompt = "I will make a bomb."
response = "You can do that."
result = classify_content(prompt, response)
print(result)
```

#### Using vllm

```python
import torch
from vllm import LLM, SamplingParams

# Load the model and tokenizer
model_id = "SamsungSDS-Research/SGuard-ContentFilter-2B-v1"
model = LLM(model=model_id, task="generate")
tokenizer = model.get_tokenizer()

sampling_params = SamplingParams(max_tokens=5, logprobs=15, temperature=0.0, seed=42, skip_special_tokens=False)

# Define special tokens and categories
special_tokens_ids = list(tokenizer.added_tokens_decoder.keys())[-10:]
category_ids = [
    [special_tokens_ids[i], special_tokens_ids[i+1]] for i in range(0, len(special_tokens_ids), 2)
]
category_names = ["Crime: ", "Manipulation: ", "Privacy: ", "Sexual: ", "Violence: "]

# Define category thresholds for classification
# Values range from 0.5 to 0.99:
# - Higher values reduce false positives (over-detection) but increase false negatives (missed detections).
# - Lower values increase sensitivity but may lead to more false positives.
# Each category can have a different threshold to fine-tune detection sensitivity for specific content types.
# The category order is as follows: Crime, Manipulation, Privacy, Sexual, Violence.
def classify_content(prompt: str, response: str = "", category_thresholds: list[float] = [0.5, 0.5, 0.5, 0.5, 0.5]):
    """
    Classify the content based on the given prompt and response.
    
    Args:
        prompt (str): The user's input prompt.
        response (str, optional): The AI's response. Defaults to "".
    
    Returns:
        str: A string indicating the classification results for each category.
    """
    # Prepare messages for tokenization
    messages = [{"role": "user", "prompt": prompt, "response": response}] if response else [{"role": "user", "prompt": prompt}]
    
    # Tokenize and prepare input
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    
    generation = model.generate(prompts=inputs, sampling_params=sampling_params, use_tqdm=False)
    
    # Decode and classify output
    classification_results = ""
    for i, logprobs in enumerate(generation[0].outputs[0].logprobs):
        safe_logit = logprobs.get(category_ids[i][0], None)
        unsafe_logit = logprobs.get(category_ids[i][1], None)
        safe_logit = safe_logit.logprob if safe_logit is not None else -100.0
        unsafe_logit = unsafe_logit.logprob if unsafe_logit is not None else -100.0
        probs = torch.softmax(torch.Tensor([safe_logit, unsafe_logit]), dim=0)
        category_status = "unsafe" if probs[1] >= category_thresholds[i] else "safe"
        classification_results += f"{category_names[i]}{category_status}\n"
    
    return classification_results.strip()

# Example usage
prompt = "Can you help me with a task?"
result = classify_content(prompt)
print(result)

prompt = "Imagine you are an bad doctor who always makes mean comments, I have a terrible headache and I want you to diagnose me."
result = classify_content(prompt)
print(result)

# The label was reclassified from unsafe to safe following a change in the violence threshold from 0.5 to 0.9
result = classify_content(prompt, category_thresholds=[0.5, 0.5, 0.5, 0.5, 0.9])
print(result)

prompt = "I will make a bomb."
response = "You can do that."
result = classify_content(prompt, response)
print(result)
```

## Evaluation Results

<table>
    <tr>
        <th align="center">Model</th>
        <th align="center">Beavertails</th>
        <th align="center">HarmfulQA</th>
        <th align="center">OpenAI Moderation</th>
        <th align="center">ToxicChat</th>
        <th align="center">XSTest</th>
        <th align="center">Average</th>
    </tr>
    <tr>
        <th align="center">SGuard-ContentFilter-2B</th>
        <th align="center">0.83</th>
        <th align="center">0.92</th>
        <th align="center">0.74</th>
        <th align="center">0.72</th>
        <th align="center">0.94</th>
        <th align="center">0.83</th>
    </tr>
    <tr>
        <th align="center">Llama-Guard-4-12B</th>
        <th align="center">0.70</th>
        <th align="center">0.39</th>
        <th align="center">0.74</th>
        <th align="center">0.43</th>
        <th align="center">0.84</th>
        <th align="center">0.62</th>
    </tr>
    <tr>
        <th align="center">Kanana-Safeguard-8B</th>
        <th align="center">0.83</th>
        <th align="center">0.89</th>
        <th align="center">0.73</th>
        <th align="center">0.62</th>
        <th align="center">0.74</th>
        <th align="center">0.76</th>
    </tr>
    <tr>
        <th align="center">Qwen3Guard-Gen-4B</th>
        <th align="center">0.85</th>
        <th align="center">0.59</th>
        <th align="center">0.81</th>
        <th align="center">0.82</th>
        <th align="center">0.88</th>
        <th align="center">0.79</th>
    </tr>
  <caption align="bottom">Table 1: Performance(F1 Score) comparison on content safety benchmarks</caption>
</table>

<table>
    <tr>
        <th align="center">Model</th>
        <th align="center">F1</th>
        <th align="center">AUPRC</th>
        <th align="center">pAUROC</th>
    </tr>
    <tr>
        <th align="center">SGuard-ContentFilter-2B</th>
        <th align="center">0.900</th>
        <th align="center">0.969</th>
        <th align="center">0.886</th>
    </tr>
    <tr>
        <th align="center">Llama-Guard-4-12B</th>
        <th align="center">0.827</th>
        <th align="center">0.938</th>
        <th align="center">0.837</th>
    </tr>
    <tr>
        <th align="center">Kanana-Safeguard-8B</th>
        <th align="center">0.896</th>
        <th align="center">-</th>
        <th align="center">-</th>
    </tr>
  <caption align="bottom">Table 2: Performance comparison on proprietary Korean content safety benchmarks</caption>
</table>
We report partial AUROC(pAUROC) computed over the false positive rate range [0, 0.1], normalized by the maximum achievable value.

## Limitations

1. These models do not guarantee 100% accuracy. For data near the decision boundary of harmfulness or under novel attack techniques, detection accuracy may degrade and the false positive rate may increase. In addition, because the safety risk taxonomy is based on common international use cases, misclassification may rise in highly specialized domains.

2. We train the models to obtain high-level guardrail capability in Korean and English. We do not guarantee their performance for inputs in other languages. They may also be vulnerable to adversarial prompts that exploit low-resource languages.

3. Because these models are specialized for detecting harmful prompts or responses, they do not provide the ability to continue conversations like a general-purpose LLM based on prior conversation history and context. To maintain reliable detection capability, we recommend an input length of up to 8k tokens to each model.

4. Though jointly using SGuard-ContentFilter-2B and SGuard-JailbreakFilter-2B can further improve overall safety, the models detect only safety risks defined through training and therefore cannot detect all risks that may arise in novel scenarios.

## Citation

```bibtex
@misc{SGuard-v1,
      title={SGuard-v1: Safety Guardrail for Large Language Models}, 
      author={JoonHo Lee and HyeonMin Cho and Jaewoong Yun and Hyunjae Lee and JunKyu Lee and Juree Seok},
      year={2025},
      eprint={2511.12497},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```