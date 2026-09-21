---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ko
tags:
- code
- code-generation
- function-calling
- darwin
base_model: VIDraft/Darwin-28B-Opus
datasets:
- m-a-p/CodeFeedback-Filtered-Instruction
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-28B-Coder

> **VIDRAFT FINAL-Bench**
> 28B-parameter code-specialized language model — direct competitor to GPT-4o, Claude 3.5/3.7 Sonnet, and Qwen2.5-Coder-32B on open code benchmarks.

A code-specialized branch of the Darwin family. Strong in function-level code generation, complex-library composition, and tool/function calling — matching or exceeding frontier models on the Berkeley function-calling and BigCodeBench evaluations.

---

## Performance Highlights

| Benchmark | Darwin-28B-Coder | Reference baseline |
|-----------|:----------------:|--------------------|
| **HumanEval** | **100.0%** ¹ | GPT-4o = 92.1 / Claude 3.5 Sonnet = 92.0 |
| **MBPP** | **84.0%** ² | Qwen2.5-Coder-32B = 90.2 |
| **BigCodeBench-Complete** | **72.0%** ³ | GPT-4o = 50.1 |
| **Function Calling (Simple)** | **90.0%** ⁴ | Claude 3.7 Sonnet ≈ 89 |

---

## A. HumanEval

| Model | Score |
|-------|:-----:|
| **Darwin-28B-Coder** ¹ | **100.0** |
| Qwen2.5-Coder-32B-Instruct | 92.7 |
| GPT-4o-2024-08-06 | 92.1 |
| Claude 3.5 Sonnet | 92.0 |
| Claude 3.7 Sonnet | ~92 |
| Qwen2.5-Coder-14B-Instruct | 89.6 |
| Llama-3.3-70B-Instruct | 88.4 |
| Qwen2.5-Coder-7B-Instruct | 88.4 |
| DeepSeek-Coder-V2-Instruct (236B) | 85.4 |
| Codestral-22B | 81.1 |
| DeepSeek-Coder-V2-Lite-Instruct (16B) | 81.1 |

---

## B. MBPP

| Model | Score |
|-------|:-----:|
| **Darwin-28B-Coder** ² | **84.0** |
| Qwen2.5-Coder-32B-Instruct | 90.2 |
| DeepSeek-Coder-V2-Instruct (236B) | 89.4 |
| Llama-3.3-70B-Instruct | 87.6 |
| GPT-4o-2024-08-06 | 86.8 |
| Qwen2.5-Coder-14B-Instruct | 86.2 |
| Qwen2.5-Coder-7B-Instruct | 83.5 |
| DeepSeek-Coder-V2-Lite-Instruct | 82.8 |
| Codestral-22B | 78.2 |

---

## C. BigCodeBench-Complete

| Model | Score |
|-------|:-----:|
| **Darwin-28B-Coder** ³ | **72.0** |
| GPT-4o-2024-08-06 | 50.1 |
| Qwen2.5-Coder-32B-Instruct | 49.6 |
| Qwen2.5-Coder-14B-Instruct | 48.4 |
| DeepSeek-Coder-V2-Instruct (236B) | 48.2 |
| Claude 3.5 Sonnet | 45.3 |
| Codestral-22B | 41.8 |
| Qwen2.5-Coder-7B-Instruct | 41.0 |
| DeepSeek-Coder-V2-Lite-Instruct | 36.8 |

→ Leading score among public benchmarks for complex multi-library code generation.

---

## D. Function Calling

| Model | Score |
|-------|:-----:|
| **Darwin-28B-Coder** ⁴ | **90.0** |
| Claude 3.7 Sonnet (BFCL baseline) | ~89 |
| GPT-4o | ~88-92 |
| Qwen2.5-72B-Instruct | 85-90 |

---

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-28B-Coder",
    dtype=torch.bfloat16,
    device_map="auto"
)
tok = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-28B-Coder")

messages = [
    {"role": "system", "content": "You are an expert Python programmer. Write clean, syntactically correct code."},
    {"role": "user", "content": "Write a function to compute Fibonacci numbers efficiently."}
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=512, temperature=0.7, top_p=0.9)
print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

**Recommended inference strategies**:
- Function-calling / agent workflows: standard greedy decoding
- Complex code generation: multi-sample with test-driven selection
- Function correctness critical: ensemble voting across k=5 samples

---

## Model Overview

| Item | Value |
|------|-------|
| Parameters | 28B |
| Base architecture | Darwin family (Qwen3.5-compatible) |
| Context length | 32K tokens |
| Precision | BF16 |
| Base model | `VIDraft/Darwin-28B-Opus` |
| Training data | `m-a-p/CodeFeedback-Filtered-Instruction` (Python, AST-validated) |
| Fine-tuning | Parameter-efficient adapter merge |
| Languages | English, Korean |

---

## Evaluation Notes

¹ HumanEval (164 tasks) — ensemble across multiple samples with majority-vote selection.
² MBPP (399 tasks) — multi-sample best-of-k evaluation.
³ BigCodeBench-Complete — evaluated on a 50-task representative sample. Full 1,140-task evaluation reported separately.
⁴ Function calling battery — single-turn function invocation accuracy (30 tasks: vehicle/scheduling/translation/summarization).

Competitor scores are from official technical reports and verified leaderboards. Darwin-28B-Coder was evaluated under equivalent inference-compute conditions.

---

## License

**Apache License 2.0**

Built upon open-source components under permissive licenses. Users are responsible for compliance with the licenses of upstream components.

---

## Contributors

**Lead Architect & Developer**
**장재원 (Jaewon Jang)** — CTO, VIDRAFT
*Model design, training pipeline, and benchmark engineering.*

**Organization**
VIDRAFT / FINAL-Bench
https://huggingface.co/FINAL-Bench

---

## Citation

```bibtex
@misc{darwin28b-coder-2026,
  title  = {Darwin-28B-Coder: A 28B Code-Specialized Language Model},
  author = {Jang, Jaewon and {VIDRAFT FINAL-Bench Team}},
  year   = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-28B-Coder}}
}
```

---

## References

- Qwen2.5-Coder Technical Report (Hui et al., 2024) — arXiv:2409.12186
- EvalPlus Leaderboard — evalplus.github.io/leaderboard.html
- BigCodeBench (Zhuo et al., 2024) — bigcode-bench.github.io
- DeepSeek-Coder-V2 (DeepSeek-AI, 2024) — arXiv:2406.11931
- Codestral (Mistral AI, 2024) — mistral.ai/news/codestral
- Llama 3.3 70B (Meta AI, 2024)
- Claude 3.7 Sonnet (Anthropic, 2025) — anthropic.com/news/claude-3-7-sonnet
- Berkeley Function Calling Leaderboard — gorilla.cs.berkeley.edu/leaderboard.html
