---
license: other
license_name: mg0-2.0
license_link: https://github.com/Xtra-Computing/ModelGo/blob/main/MG_licenses/V2/MG0-2.0.txt
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
pipeline_tag: text-generation
base_model: microsoft/phi-4
tags:
- chat
library_name: transformers
---

# XtraGPT: Context-Aware and Controllable Academic Paper Revision for Human-AI Collaboration

<p align="center">
    <a href="https://arxiv.org/abs/2505.11336">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2505.11336-b31b1b.svg">
    </a>
</p>

## Model Overview

**XtraGPT** is a family of open-source Large Language Models (LLMs) designed specifically for **human-AI collaborative academic paper revision**. Unlike general-purpose models that often perform surface-level polishing, XtraGPT is fine-tuned to **understand the full context** of a research paper and execute specific, **criteria-guided** revision instructions.

The models were trained on a dataset of 140,000 high-quality instruction-revision pairs derived from top-tier conference papers (ICLR).

**Key Features:**
* **Context-Aware:** Processes the full paper context to ensure revisions maintain consistency with the global narrative.
* **Controllable:** Follows specific user instructions aligned with 20 academic writing criteria across 6 sections (Abstract, Introduction, etc.).
* **Iterative Workflow:** Designed to support the "Human-AI Collaborative" (HAC) lifecycle where authors retain creative control.

**Available Model Sizes:**
* **1.5B** (Based on Qwen/Qwen2.5-1.5B-Instruct)
* **3B** (Based on meta-llama/Llama-3.2-3B-Instruct)
* **7B** (Based on Qwen/Qwen2.5-7B-Instruct)
* **14B** (Based on microsoft/phi-4)

---

## Inference with Transformers

To use XtraGPT with the standard Hugging Face `transformers` library, ensure you format your input using the specific tags `<PAPER_CONTENT>`, `<SELECTED_CONTENT>`, and `<QUESTION>`.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Select the model size: "XtraGPT-1.5B", "XtraGPT-3B", "XtraGPT-7B", or "XtraGPT-14B"
model_name = "Xtra-Computing/XtraGPT-7B" 

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Define the Prompt Template tailored for XtraGPT
prompt_template = """Act as an expert model for improving articles **PAPER_CONTENT**.
The output needs to answer the **QUESTION** on **SELECTED_CONTENT** in the input. Avoid adding unnecessary length, unrelated details, overclaims, or vague statements.
Focus on clear, concise, and evidence-based improvements that align with the overall context of the paper.
<PAPER_CONTENT>
{paper_content}
</PAPER_CONTENT>
<SELECTED_CONTENT>
{selected_content}
</SELECTED_CONTENT>
<QUESTION>
{user_question}
</QUESTION>"""

# Example Data (from the "Attention Is All You Need" paper)
paper_content = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train."
selected_content = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration."
user_question = "help me make it more concise."

# Format the input
formatted_prompt = prompt_template.format(
    paper_content=paper_content,
    selected_content=selected_content,
    user_question=user_question
)

messages = [
    {"role": "user", "content": formatted_prompt}
]

# Apply chat template
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=16384,
    temperature=0.1
)

generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

-----

## Inference with vLLM

XtraGPT is compatible with vLLM for high-throughput inference.

### 1\. Launch the Server

Replace `XtraGPT-14B` with your specific model variant.

```bash
python -m vllm.entrypoints.openai.api_server \
    --port 8088 \
    --model Xtra-Computing/XtraGPT-14B \
    --served-model-name xtragpt \
    --max-model-len 16384 \
    --gpu-memory-utilization 0.95
```

### 2\. Send a Request (Client Side)

```bash
curl [http://127.0.0.1:8088/v1/chat/completions](http://127.0.0.1:8088/v1/chat/completions) \
  -H "Content-Type: application/json" \
  -d '{
    "model": "xtragpt",
    "messages": [
      {
        "role": "user",
        "content": "Please improve the selected content based on the following. Act as an expert model for improving articles **PAPER_CONTENT**.\nThe output needs to answer the **QUESTION** on **SELECTED_CONTENT** in the input. Avoid adding unnecessary length, unrelated details, overclaims, or vague statements.\nFocus on clear, concise, and evidence-based improvements that align with the overall context of the paper.\n<PAPER_CONTENT>\nThe dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.\n</PAPER_CONTENT>\n<SELECTED_CONTENT>\nThe dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration.\n</SELECTED_CONTENT>\n<QUESTION>\nhelp me make it more concise.\n</QUESTION>"
      }
    ],
    "temperature": 0.1,
    "max_new_tokens": 16384,
    "stream": false
  }'
```

-----

## Model License

This model is released under the **ModelGo Zero License 2.0 (MG0-2.0)**.

MG0-2.0 is a highly permissive open model license designed to facilitate the widest possible adoption and collaboration. It allows for **unrestricted use**, reproduction, distribution, and the creation of derivative works including for commercial purposes, without requiring attribution or imposing copyleft restrictions.

For more details on the license terms, please visit [ModelGo.li](https://www.modelgo.li/) or refer to the `LICENSE` file in the repository.

-----

## Citation

If you use XtraGPT in your research, please cite our paper:

```
@inproceedings{
chen2026xtragpt,
title={XtraGPT: Context-Aware and Controllable Academic Paper Revision via Human-AI Collaboration},
author={Nuo Chen and Andre Lin HuiKai and Jiaying Wu and Junyi Hou and Zining Zhang and Qian Wang and Xidong Wang and Bingsheng He},
booktitle = "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
year={2026},
note={Available on arXiv:2505.11336}
}
```