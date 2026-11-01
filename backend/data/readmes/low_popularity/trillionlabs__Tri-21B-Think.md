---
license: apache-2.0
tags:
- finetuned
- chat
- reasoning
language:
- en
- ko
- ja
pipeline_tag: text-generation
library_name: transformers
base_model:
- trillionlabs/Tri-21B
---

<p align="center">
<picture>
  <img src="https://raw.githubusercontent.com/trillion-labs/.github/main/Tri-21B-Think.png" alt="Tri-21B-Think" style="width: 80%;">
</picture>
</p>

## Introduction

**Tri-21B-Think** is a reasoning-enhanced version of [Tri-21B](https://huggingface.co/trillionlabs/Tri-21B), built through mid-training context length expansion (32k), supervised fine-tuning (SFT), and reinforcement learning (RL). It excels at chain-of-thought reasoning and multi-turn agentic tasks with tool use.

### Key Highlights
* **Reasoning-Enhanced**: Chain-of-thought reasoning via SFT and RL on top of Tri-21B
* **Agentic**: Strong multi-turn tool-calling and complex multi-step interaction capabilities
* **Extended Context**: Context length expanded from 8K to 32K tokens through mid-training (up to 262K with YaRN scaling)
* **Enhanced Korean Capabilities**: Korean capabilities have significantly improved compared to [Base Model](https://huggingface.co/trillionlabs/Tri-21B) and [Preview version](https://huggingface.co/trillionlabs/Tri-21B-Think-Preview)


### Model Specifications

- Type: Causal Language Model (Reasoning-Enhanced)
- Base Model: [Tri-21B](https://huggingface.co/trillionlabs/Tri-21B)
- Architecture: Transformer Decoder with RoPE, SwiGLU, RMSNorm, and GQA
- Number of Parameters: 20.73B
- Number of Layers: 40
- Number of Attention Heads: 32 (Query) / 8 (Key, Value)
- Head Dimension: 160
- Hidden Size: 5,120
- Intermediate Size: 27,392
- Context Length: 32,768 (up to 262,144 with YaRN)
- Vocab Size: 124,416


## Quickstart

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "trillionlabs/Tri-21B-Think"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Solve the following step by step: What is the sum of the first 100 prime numbers?"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=4096,
    temperature=0.6,
    top_p=0.9
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

### vLLM & SGLang Deployment

vLLM and SGLang support for Trillion Model is on the way. Stay tuned!


## Fine-tuning Notes

> **Note on `<think>` tags:** This model was trained without `<think>` and `</think>` as special tokens. They were added post-training for compatibility with reasoning parsers. If you plan to fine-tune this model, you'll need to modify `tokenizer_config.json` to avoid indexing errors.

Replace tokens 123975 and 123976 in `tokenizer_config.json`:

```json
"123975": {
  "content": "<|reserved_special_token_9|>",
  "lstrip": false,
  "normalized": false,
  "rstrip": false,
  "single_word": false,
  "special": true
},
"123976": {
  "content": "<|reserved_special_token_10|>",
  "lstrip": false,
  "normalized": false,
  "rstrip": false,
  "single_word": false,
  "special": true
}
```


## Evaluation

| Category | Benchmark | Description | Tri-21B-Think |
| :--- | :--- | :--- | :---: |
| **Reasoning** | GPQA-Diamond | Graduate-level science questions across physics, chemistry, and biology (PhD-level) | 62.6 |
| | AIME 2026 | American Invitational Mathematics Examination 2026 | 56.67 |
| | MMLU-Pro | Massive Multitask Language Understanding with more answer choices and reasoning-focused questions | 74.3 |
| | HLE | Humanity's Last Exam — 2,500 expert-level questions across 100+ subjects created by nearly 1,000 domain experts | 5.52 |
| **Coding** | LiveCodeBench v6 | Competitive programming benchmark with problems sourced from recent programming contests | 53.7 |
| | SciCode | Code generation across 338 subproblems in 16 natural science fields drawn from real research workflows | 21.3 |
| | MBPP | Python programming benchmark with 500 crowd-sourced problems | 87.83 |
| | HumanEval | Code generation benchmark evaluating functional correctness from docstrings | 84.14 |
| **Instruction Following** | IFEval | Tests ability to follow precise formatting and output constraint instructions | 84.7 |
| | IFBench | Evaluates generalization to novel, verifiable output constraints not seen during training (Allen AI) | 56.71 |
| **Agentic** | TAU2-Bench (Telecom) | Dual-control conversational benchmark where both agent and user use tools to resolve telecom scenarios (Sierra) | 81 |
| | AA-LCR | Long-context reasoning over multiple documents at 10K–100K tokens (Artificial Analysis) | 11 |
| **Korean** | KMMLU-Pro | 2,822 questions from 14 Korean National Professional Licensure exams (LG AI Research) | 61.54 |
| | CLIcK | 1,995 Korean cultural and linguistic knowledge questions sourced from official exams and textbooks (KAIST) | 82.76 |
| | KoBALT | Korean linguistic understanding across syntax, semantics, pragmatics, phonetics, and morphology (SNU) | 54.0 |
| | CSATQA (CoT) | 936 questions from South Korea's College Scholastic Ability Test covering reading, grammar, and writing | 68.98 |



## Limitations

- **Language Support**: Optimized for English, Korean, and Japanese. Other languages may show degraded performance.
- **Knowledge Cutoff**: February 2025.
- **Reasoning Overhead**: Chain-of-thought generates additional tokens before the final answer, increasing latency compared to Tri-21B.

## License
This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

## Contact
For inquiries: [info@trillionlabs.co](mailto:info@trillionlabs.co)
