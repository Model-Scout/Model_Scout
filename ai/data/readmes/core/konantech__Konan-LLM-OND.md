---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-4B-Base
tags:
- konanllm
language:
- ko
- en
---
# Konan-LLM-OND

## **Overview**

**Konan-LLM-OND**, a large language model from Konan Technology Inc., is based on [Qwen3-4B-Base](https://huggingface.co/Qwen/Qwen3-4B-Base). It has been specifically optimized for the Korean language through vocabulary expansion, continual pre-training, and instruction tuning to enhance performance and efficiency.
* **Languages**: Primarily Korean, with support for English.
* **Key Features:**
  * **Expanded Korean Vocabulary:** The model's vocabulary has been expanded with additional Korean tokens to improve tokenization efficiency. As a result, Konan-LLM-OND is approximately 30% more token-efficient with Korean input than Qwen3, leading to greater cost-effectiveness and processing speed.
  * **Continual Pre-training**: The model underwent continual pre-training on a large-scale Korean corpus using an expanded vocabulary. This process enhanced its fundamental understanding and text generation capabilities in Korean.
  * **Supervised Fine-Tuning (SFT):** The model was fine-tuned on a high-quality Korean instruction dataset to improve its ability to understand and execute a wide variety of real-world tasks.

## Benchmark Results

#### **Model Performance (＜ 5B)**

<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th rowspan="2" style="text-align: center; padding: 8px;">Model</th>
      <th rowspan="2" style="text-align: center; padding: 8px;">Model size</th>
      <th colspan="3" style="text-align: center; padding: 8px;">Korean</th>
      <th colspan="3" style="text-align: center; padding: 8px;">English</th>
    </tr>
    <tr>
      <th style="text-align: center; padding: 8px;">KMMLU</th>
      <th style="text-align: center; padding: 8px;">HRM8K</th>
      <th style="text-align: center; padding: 8px;">Ko-IFEval</th>
      <th style="text-align: center; padding: 8px;">MMLU</th>
      <th style="text-align: center; padding: 8px;">GSM8K</th>
      <th style="text-align: center; padding: 8px;">IFEval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;"><strong>Konan-LLM-OND</strong></td>
      <td style="text-align: center; padding: 8px;">4.0B</td>
      <td style="text-align: center; padding: 8px;"><strong>54.33%<strong></td>
      <td style="text-align: center; padding: 8px;">53.70%</td>
      <td style="text-align: center; padding: 8px;">68.42%</td>
      <td style="text-align: center; padding: 8px;">70.76%</td>
      <td style="text-align: center; padding: 8px;"><strong>86.66%<strong></td>
      <td style="text-align: center; padding: 8px;">73.38%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>EXAONE-3.5-2.4B-Instruct</strong></td>
      <td style="text-align: center; padding: 8px;">2.4B</td>
      <td style="text-align: center; padding: 8px;">45.22%</td>
      <td style="text-align: center; padding: 8px;">38.55%</td>
      <td style="text-align: center; padding: 8px;">60.53%</td>
      <td style="text-align: center; padding: 8px;">61.76%</td>
      <td style="text-align: center; padding: 8px;">78.54%</td>
      <td style="text-align: center; padding: 8px;">77.73%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>kanana-1.5-2.1b-instruct-2505</strong></td>
      <td style="text-align: center; padding: 8px;">2.1B</td>
      <td style="text-align: center; padding: 8px;">38.14%</td>
      <td style="text-align: center; padding: 8px;">34.14%</td>
      <td style="text-align: center; padding: 8px;">55.99%</td>
      <td style="text-align: center; padding: 8px;">55.25%</td>
      <td style="text-align: center; padding: 8px;">74.83%</td>
      <td style="text-align: center; padding: 8px;">64.60%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Midm-2.0-Mini-Instruct</strong></td>
      <td style="text-align: center; padding: 8px;">2.3B</td>
      <td style="text-align: center; padding: 8px;">43.24%</td>
      <td style="text-align: center; padding: 8px;">37.30%</td>
      <td style="text-align: center; padding: 8px;">66.81%</td>
      <td style="text-align: center; padding: 8px;">55.62%</td>
      <td style="text-align: center; padding: 8px;">72.55%</td>
      <td style="text-align: center; padding: 8px;">68.30%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Qwen3-4B(w/o reasoning)</strong></td>
      <td style="text-align: center; padding: 8px;">4.0B</td>
      <td style="text-align: center; padding: 8px;">52.55%</td>
      <td style="text-align: center; padding: 8px;"><strong>54.16%<strong></td>
      <td style="text-align: center; padding: 8px;">68.42%</td>
      <td style="text-align: center; padding: 8px;"><strong>71.81%<strong></td>
      <td style="text-align: center; padding: 8px;">76.57%</td>
      <td style="text-align: center; padding: 8px;"><strong>80.04%<strong></td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>gemma-3-4b-it</strong></td>
      <td style="text-align: center; padding: 8px;">4.3B</td>
      <td style="text-align: center; padding: 8px;">40.10%</td>
      <td style="text-align: center; padding: 8px;">43.88%</td>
      <td style="text-align: center; padding: 8px;"><strong>69.15%<strong></td>
      <td style="text-align: center; padding: 8px;">61.25%</td>
      <td style="text-align: center; padding: 8px;">83.24%</td>
      <td style="text-align: center; padding: 8px;">78.28%</td>
    </tr>
  </tbody>
</table>

#### **Model Performance (≥ 7B)**

<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th rowspan="2" style="text-align: center; padding: 8px;">Model</th>
      <th rowspan="2" style="text-align: center; padding: 8px;">Model size</th>
      <th colspan="3" style="text-align: center; padding: 8px;">Korean</th>
      <th colspan="3" style="text-align: center; padding: 8px;">English</th>
    </tr>
    <tr>
      <th style="text-align: center; padding: 8px;">KMMLU</th>
      <th style="text-align: center; padding: 8px;">HRM8K</th>
      <th style="text-align: center; padding: 8px;">Ko-IFEval</th>
      <th style="text-align: center; padding: 8px;">MMLU</th>
      <th style="text-align: center; padding: 8px;">GSM8K</th>
      <th style="text-align: center; padding: 8px;">IFEval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;"><strong>Konan-LLM-OND</strong></td>
      <td style="text-align: center; padding: 8px;">4.0B</td>
      <td style="text-align: center; padding: 8px;">54.33%</td>
      <td style="text-align: center; padding: 8px;">53.70%</td>
      <td style="text-align: center; padding: 8px;">68.42%</td>
      <td style="text-align: center; padding: 8px;">70.55%</td>
      <td style="text-align: center; padding: 8px;">86.66%</td>
      <td style="text-align: center; padding: 8px;">73.38%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>A.X-4.0-Light</strong></td>
      <td style="text-align: center; padding: 8px;">7.2B</td>
      <td style="text-align: center; padding: 8px;"><strong>62.48%</strong></td>
      <td style="text-align: center; padding: 8px;">51.08%</td>
      <td style="text-align: center; padding: 8px;">71.49%</td>
      <td style="text-align: center; padding: 8px;">73.15%</td>
      <td style="text-align: center; padding: 8px;">86.58%</td>
      <td style="text-align: center; padding: 8px;">81.33%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>EXAONE-3.5-7.8B-Instruct</strong></td>
      <td style="text-align: center; padding: 8px;">7.8B</td>
      <td style="text-align: center; padding: 8px;">53.03%</td>
      <td style="text-align: center; padding: 8px;">48.02</td>
      <td style="text-align: center; padding: 8px;">66.81%</td>
      <td style="text-align: center; padding: 8px;">71.43%</td>
      <td style="text-align: center; padding: 8px;"><strong>89.46%</strong></td>
      <td style="text-align: center; padding: 8px;">79.85%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>kanana-1.5-8b-instruct-2505</strong></td>
      <td style="text-align: center; padding: 8px;">8.0B</td>
      <td style="text-align: center; padding: 8px;">47.80%</td>
      <td style="text-align: center; padding: 8px;">39.65%</td>
      <td style="text-align: center; padding: 8px;">71.05%</td>
      <td style="text-align: center; padding: 8px;">65.90%</td>
      <td style="text-align: center; padding: 8px;">76.57%</td>
      <td style="text-align: center; padding: 8px;">76.80%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Midm-2.0-Base-Instruct</strong></td>
      <td style="text-align: center; padding: 8px;">11.5B</td>
      <td style="text-align: center; padding: 8px;">58.43%</td>
      <td style="text-align: center; padding: 8px;">51.18%</td>
      <td style="text-align: center; padding: 8px;"><strong>75.00%</strong></td>
      <td style="text-align: center; padding: 8px;">71.84%</td>
      <td style="text-align: center; padding: 8px;">79.83%</td>
      <td style="text-align: center; padding: 8px;">79.67%</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Qwen3-8B(w/o reasoning)</strong></td>
      <td style="text-align: center; padding: 8px;">8.1B</td>
      <td style="text-align: center; padding: 8px;">57.43%</td>
      <td style="text-align: center; padding: 8px;"><strong>57.88%<strong></td>
      <td style="text-align: center; padding: 8px;">70.91%</td>
      <td style="text-align: center; padding: 8px;"><strong>76.45%<strong></td>
      <td style="text-align: center; padding: 8px;">77.79%</td>
      <td style="text-align: center; padding: 8px;"><strong>82.81%</strong></td>
    </tr>
  </tbody>
</table>

Note:
* The highest scores are shown in bold.

## **Benchmark Setup**

All benchmarks were executed using the following standardized environment.

* **Evaluation Framework**: `lm-evaluation-harness v0.4.9`
* **Runtime & Hardware**: All models were served with `vLLM v0.9.2` on NVIDIA GPU.
* **Inference Mode**: For every benchmark, we invoked the `chat_completions` API, and scores were computed solely from the generated responses.

#### **Metric Adjustments**

* **KMMLU** was evaluated in a zero-shot setting using a CoT-style prompt modified from the `kmmlu_direct` task in lm-evaluation-harness, with enhanced preprocessing filters applied during evaluation.

* **MMLU** was evaluated in a zero-shot setting using a CoT-style prompt modified from the `mmlu_generative` task in lm-evaluation-harness, with enhanced preprocessing filters applied during evaluation.

* **GSM8K** was evaluated in a zero-shot setting using the original prompt format from lm-evaluation-harness, with enhanced preprocessing filters applied.

* **HRM8K** was evaluated in a zero-shot setting using the original prompt and data format from lm-evaluation-harness, without any modifications. 

* **Ko-IFEval** was evaluated in a zero-shot setting using the original **IFEval** protocol, with the dataset sourced from [allganize/IFEval-Ko](https://huggingface.co/datasets/allganize/IFEval-Ko).

#### **Evaluation Protocol**

<table>
  <thead>
    <tr>
      <th>Benchmark</th>
      <th>Scoring Method</th>
      <th>Few-shot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>KMMLU</strong></td>
      <td><code>exact_match</code></td>
      <td>0-shot CoT</td>
    </tr>
    <tr>
      <td><strong>HRM8K</strong></td>
      <td>mean of <code>hrm8k_gsm8k</code>, <code>hrm8k_ksm</code>, <code>hrm8k_math</code>, <code>hrm8k_mmmlu</code>, <code>hrm8k_omni_math</code></td>
      <td>0-shot</td>
    </tr>
    <tr>
      <td><strong>Ko-IFEval</strong></td>
      <td>mean of <code>prompt_level_strict_acc</code>, <code>inst_level_strict_acc</code>, <code>prompt_level_loose_acc</code>, <code>inst_level_loose_acc</code></td>
      <td>0-shot</td>
    </tr>
    <tr>
      <td><strong>MMLU</strong></td>
      <td><code>exact_match</code></td>
      <td>0-shot CoT</td>
    </tr>
    <tr>
      <td><strong>GSM8K</strong></td>
      <td><code>flexible-extract</code></td>
      <td>0-shot</td>
    </tr>
    <tr>
      <td><strong>IFEval</strong></td>
      <td>mean of <code>prompt_level_strict_acc</code>, <code>inst_level_strict_acc</code>, <code>prompt_level_loose_acc</code>, <code>inst_level_loose_acc</code></td>
      <td>0-shot</td>
    </tr>
  </tbody>
</table>

## Quickstart

**Konan-LLM-OND** is supported in `transformers v4.52.0` and later.
```bash
pip install transformers>=4.52.0
```
 
The code example below shows you how to get the model to generate content based on given inputs.
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "konantech/Konan-LLM-OND"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "대한민국 수도는?"}
]


input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=False,
    )

len_input_prompt = len(input_ids[0])
response = tokenizer.decode(output[0][len_input_prompt:], skip_special_tokens=True)
print(response)
# 대한민국 수도는 서울입니다.
```

## Citation
```
@misc{Konan-LLM-OND-2025,
  author = {Konan Technology Inc.},
  title = {Konan-LLM-OND},
  year = {2025},
  url = {https://huggingface.co/konantech/Konan-LLM-OND}
}
```
