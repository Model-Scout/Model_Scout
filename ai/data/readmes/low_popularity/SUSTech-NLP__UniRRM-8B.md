---
license: apache-2.0
language:
  - en
  - fr
  - es
  - it
  - de
  - ru
  - tr
  - pt
  - zh
  - pl
  - ar
  - ko
  - ja
  - id
  - vi
  - multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
  - reward-model
  - reasoning
  - multilingual
  - evaluation
  - generative-reward-model
  - rlhf
  - grpo
base_model: Qwen/Qwen3-8B
---

# UniRRM-8B: Unified Reasoning Reward Model (8B)

## Overview

**UniRRM-8B** is a unified reasoning reward model that supports **multiple languages (103 languages)** and **multiple evaluation paradigms (pairwise, listwise, and pointwise)** in a single model. It is built on **Qwen3-8B** and trained with a two-stage pipeline (SFT + GRPO) on the [MixReward](https://huggingface.co/datasets/SUSTech-NLP/MixReward) dataset.

This model is introduced in the following paper, accepted at **ICML 2026** (the 43rd International Conference on Machine Learning):

> **UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms** [[Paper]](https://icml.cc/virtual/2026/poster/61930)

## Key Features

- 🌍 **103 Languages**: Trained on multilingual data spanning 103 languages across 6 domains
- 🔀 **Unified Evaluation Paradigms**: Supports pairwise, listwise, and pointwise evaluation in a single model
- 🧠 **Adaptive Rubric Generation**: Dynamically generates task-generic and instruction-specific evaluation criteria through a staged reasoning chain
- ⚡ **Structured Reasoning**: Follows a three-stage reasoning pipeline — Deep Analysis → Adaptive Rubric Generation → Detailed Evaluation
- 🪶 **Efficient**: Strong performance in a compact 8B parameter model

## Reasoning Workflow

UniRRM follows a structured three-stage reasoning chain:

1. **Deep Analysis (𝒛)**: Identifies task intent, potential risks, core evaluation objectives, and strict constraints
2. **Adaptive Rubric Generation (𝒓)**: Produces both task-generic criteria (broadly applicable) and instruction-specific criteria (tailored to user query), each on a 1–5 scoring scale
3. **Detailed Evaluation (𝒆)**: Applies generated rubrics to judge candidate responses with per-criterion scoring and final judgment

## Quick Start with vLLM

The following example demonstrates **pairwise evaluation** using vLLM offline inference. To switch to other evaluation paradigms, simply adjust the number of `<Response>` blocks in the user prompt:
- **Pairwise**: 2 responses (`<Response1>`, `<Response2>`)
- **Listwise**: 4 responses (`<Response1>` through `<Response4>`)
- **Pointwise**: 1 response (`<Response1>`), optionally with a `<Reference_Answer>` block

```python
import json
import re
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

MODEL_NAME = "SUSTech-NLP/UniRRM-8B"

# ---------- 1. Load model ----------
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
llm = LLM(model=MODEL_NAME, max_model_len=16384)
sampling_params = SamplingParams(temperature=0, max_tokens=4096, repetition_penalty=1.05)

# ---------- 2. Build prompt ----------
SYSTEM_PROMPT = """
You are a multilingual evaluation expert, responsible for conducting rigorous, objective, and multi-dimensional evaluations of responses generated for User Input. Your evaluation must strictly follow the step-by-step process outlined below:

### Phase 1: Deep Analysis
Before evaluating, perform a comprehensive analysis of the User Input to establish a robust baseline:
1. **Identify potential risks**: Analyze the User Input to identify any potential safety, legal, offensive, or ethical risks.
2. **Identify task type**: Identify the primary task type (e.g., chat, reasoning, code generation, translation, or creative writing).
3. **Analyze core requirements (task-dependent)**: Define the fundamental evaluation dimensions that any correct response must satisfy.
4. **Analyze specific requirements**: Identify additional constraints or expectations unique to the User Input.
5. **Predict response content**: Summarize the expected content or core objectives of a correct response.

### Phase 2: Dynamic Rubric Generation
1. Generate a set of evaluation rubrics tailored to the user inputs and responses, with a 1-5 scoring criterion for each rubric.
2. If any safety, legal, or ethical risks are detected, include a Safety rubric as the highest-priority dimension.
3. Ensure rubrics comprehensively cover all critical aspects of the response.

### Phase 3: Detailed Evaluation
For each rubric, evaluate the response:
1. **Evidence Extraction**: Identify specific passages that meet or fail to meet the rubric requirements.
2. **Gap Analysis**: Determine why the response did not achieve a perfect score (5).
3. **Scoring**: Assign a score from 1 to 5.

### OUTPUT FORMAT
{
  "Analysis_process": "Concise summary of the analysis.",
  "rubrics": [{"name": "String", "description": "Rubric definition"}],
  "evaluations": [{"response_id": "String", "explanation": "Summary", "final_score": "Float"}],
  "best_id": "ID of the winner"
}
""".strip()

question = "Explain the concept of recursion in programming."
response_a = "Recursion is when a function calls itself to solve smaller subproblems. A base case stops the recursion, and each recursive call works on a reduced version of the original problem. For example, calculating factorial: factorial(n) = n * factorial(n-1), with factorial(0) = 1 as the base case."
response_b = "Recursion means repeating something. In programming, it is used sometimes."

user_prompt = f"""
<User_Input>
{question}
</User_Input>

<Response1>
{response_a}
</Response1>

<Response2>
{response_b}
</Response2>
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_prompt},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# ---------- 3. Generate ----------
outputs = llm.generate([prompt], sampling_params)
raw_output = outputs[0].outputs[0].text
print(raw_output)

# ---------- 4. Parse output ----------
def parse_unirm_output(raw_output: str) -> dict:
    """Parse UniRRM's JSON output to extract scores and best_id."""
    text = raw_output
    # Strip " in text:
        text = text.split("</think>")[-1].strip()

    # Extract JSON from markdown code block or raw text
    code_block = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if code_block:
        json_str = code_block.group(1)
    else:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end != -1:
            json_str = text[start : end + 1]
        else:
            return {"error": "No JSON found in output"}

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        match = re.search(r'"final_score"\s*:\s*"?(\d+(?:\.\d+)?)"?', json_str)
        if match:
            return {"final_score": float(match.group(1))}
        return {"error": "Failed to parse JSON"}

result = parse_unirm_output(raw_output)
print(f"Best response: {result.get('best_id')}")
for evaluation in result.get("evaluations", []):
    print(f"  {evaluation['response_id']}: score={evaluation['final_score']}")
```

## Training

UniRRM-8B is trained using a two-stage pipeline:

### Stage 1: Supervised Fine-Tuning (SFT)
- **Base model**: Qwen3-8B
- **Training data**: [UniRRM-SFT](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-SFT) (35,749 samples distilled from GPT-OSS-120B)
- **Epochs**: 3
- **Objective**: Initialize structured reasoning capabilities (analysis → rubric generation → evaluation)

### Stage 2: Reinforcement Learning with GRPO
- **Training data**: [UniRRM-RL](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-RL) (32,832 samples)
- **Algorithm**: Group Relative Policy Optimization (GRPO)
- **Composite reward**: `R = 0.8 × r_fmt + 0.15 × r_acc + 0.05 × r_rubric`
  - **Format Reward (r_fmt)**: Ensures structured output compliance
  - **Outcome Consistency Reward (r_acc)**: Binary reward for correct final judgment
  - **Rubric Quality Reward (r_rubric)**: Teacher model (Qwen3-Max) evaluates rubric quality (1–5)
- **Hyperparameters**: lr=1e-6, weight_decay=0.01, batch_size=1024, epochs=2, kl_coef=0.001, rollout=5
- **Hardware**: 8 × NVIDIA H100 80GB GPUs

## Model Details

| Attribute | Value |
|-----------|-------|
| **Architecture** | Qwen3ForCausalLM |
| **Parameters** | ~8B |
| **Precision** | bfloat16 |
| **Max Position Embeddings** | 40960 |
| **Vocabulary Size** | 151936 |

## Related Resources

- **📄 Paper**: [UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms](https://openreview.net/forum?id=laiK6TlhL2) (ICML 2026)
- **🤖 UniRRM-14B**: [SUSTech-NLP/UniRRM-14B](https://huggingface.co/SUSTech-NLP/UniRRM-14B)
- **📊 MixReward Dataset**: [SUSTech-NLP/MixReward](https://huggingface.co/datasets/SUSTech-NLP/MixReward) (64,528 samples, 103 languages)
- **📊 UniRRM-SFT Dataset**: [SUSTech-NLP/UniRRM-SFT](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-SFT) (35,749 SFT samples)
- **📊 UniRRM-RL Dataset**: [SUSTech-NLP/UniRRM-RL](https://huggingface.co/datasets/SUSTech-NLP/UniRRM-RL) (32,832 RL samples)

## Citation

```bibtex
@inproceedings{
lai2026unirrm,
title={Uni{RRM}: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms},
author={Peng Lai and Yichao Du and Junchao Wu and Weibo Gao and Linan Yue and Longyue Wang and Weihua Luo and Derek F. Wong and Guanhua Chen},
booktitle={Forty-third International Conference on Machine Learning},
year={2026},
url={https://openreview.net/forum?id=laiK6TlhL2}
}
```

## License

This model is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
