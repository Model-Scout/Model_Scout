---
license: apache-2.0
language:
- ko
- en
base_model:
- google/gemma-4-31B-it
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
tags:
- sft
- trl
- transformers
- gemma-4
- full-fine-tuning
- korean
---

# Lux-V2-Pro

**Lux-V2-Pro** is a **Korean-enhanced, fully fine-tuned LLM** built on top of [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it) by **PoSTMEDIA AI Lab**, succeeding [Lux-V1-Pro](https://huggingface.co/PoSTMEDIA/Lux-V1-Pro).

It is produced with the **second generation of PoSTMEDIA's in-house Capability-Preserving Full Fine-Tuning research** — a training methodology designed so that deep domain adaptation does **not** erode the reasoning, instruction-following, and multilingual abilities of the base model. As the **maximum-capability tier** of the Lux line, V2-Pro improves on Lux-V1-Pro across the board while adding substantial Korean domain knowledge.

---

## Highlights

- **Upgrade over Lux-V1-Pro on 16 of 18 internal benchmarks** — including AIME 2024 **93.3** (+13.3) and AIME 2025 +13.4
- **Korean domain knowledge built in** — trained on PoSTMEDIA's in-house Korean synthetic datasets spanning **seven domains**: general conversation, coding, instruction following, law, cultural heritage, tourism, and mathematics, plus the PoSTMEDIA identity dataset
- **Base capability preserved and improved** — general knowledge (MMLU 86.6) and instruction following (IFEval 93.7) end **above** the V1-Pro level
- **Dense 31B** — the strongest reasoning tier of the Lux family
- **Verified training data** — synthetic datasets produced with execution- and rule-based verification pipelines

---

## Model Overview

| Specification | Details |
|---------------|---------|
| Base Model | [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it) |
| Parameters | 31B (dense) |
| Architecture | Decoder-only Transformer (dense) |
| Training Precision | BF16 |
| Inference Precision | BF16 |
| Context Length | Inherits from Gemma-4 base |
| Fine-Tuning Method | Full-parameter SFT (Capability-Preserving recipe, 2nd gen) |
| Languages | Korean, English |

---

## What's New vs Lux-V1-Pro

All results below were measured in-house under a single unified protocol (identical prompts, sampling, and generation budgets for both models).

| Benchmark | gemma-4-31B-it (base) | Lux-V1-Pro | **Lux-V2-Pro** |
|---|---:|---:|---:|
| MMLU | **86.6** | 85.9 | **86.6** |
| AIME 2024 | 83.3 | 80.0 | **93.3** |
| AIME 2025 | 66.7 | 63.3 | **76.7** |
| HMMT 2025 | **70.0** | 60.0 | 63.3 |
| IFEval | 93.2 | 92.4 | **93.7** |
| KMMLU | 76.6 | 74.8 | **76.9** |
| KMMLU-Pro | **78.2** | 77.0 | 77.4 |
| CLIcK | 85.1 | 84.8 | **85.5** |
| KoBALT | 73.4 | 71.9 | **73.9** |
| HAE-RAE Bench | 82.0 | 80.6 | **83.1** |
| HRM8K | **85.8** | 84.7 | **85.8** |
| KoSimpleQA | **91.2** | 90.0 | 90.8 |
| KoSQA-EM | 38.0 | 36.1 | **38.5** |
| **Average (17 common benchmarks)** | 76.6 | 75.5 | **78.2** |

The full 18-benchmark suite shows 16 wins, 1 tie (GPQA), and 2 minor regressions (GSM8K −1.2, IFBench −0.2) versus Lux-V1-Pro. Averaged over the 17 benchmarks measured for all three models, **Lux-V2-Pro scores 78.2 — above both the original Gemma-4 base (76.6) and Lux-V1-Pro (75.5)**. (MMLU-Pro was not measured for the base model due to generation-budget constraints.)

---

## Training Data

The V2 generation is trained on **PoSTMEDIA's in-house Korean synthetic data assets**, generated and quality-controlled by our internal data factory:

- **General conversation** — natural Korean multi-topic dialogue
- **Coding** — execution-verified code generation and explanation
- **Instruction following** — rule-verifiable Korean constraint-following tasks
- **Law** — source-grounded Korean legal knowledge QA
- **Cultural heritage** — source-grounded Korean heritage knowledge QA
- **Tourism** — source-grounded Korean tourism knowledge QA
- **Mathematics** — symbolically verified Korean math reasoning
- **PoSTMEDIA identity** — hand-curated identity dataset

Correctness of the synthetic data is enforced by verification gates (code execution, symbolic math equivalence, rule checkers, and source-grounding checks) rather than by model self-judgment.

The exact training procedure — schedule, module selection, and the post-training consolidation step that preserves base capability — is an internal research method and is not disclosed in detail.

---

## Quick Start

```bash
pip install transformers accelerate
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "PoSTMEDIA/Lux-V2-Pro"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "문화재보호법의 목적을 두 문장으로 설명해줘."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

---

## Use Cases

- The most demanding Korean reasoning and generation workloads in the Lux line
- Korean domain QA (law, cultural heritage, tourism) with source-grounded knowledge
- Competition-level mathematical assistance
- Drop-in upgrade for existing Lux-V1-Pro deployments

---

## Safety & Limitations

- The model can generate incorrect or outdated information; verify high-stakes outputs.
- Korean domain knowledge reflects the training data snapshot and may not cover recent changes (e.g., amended laws).
- Inherits the general limitations and usage considerations of the Gemma-4 base model.

---

## Citation

```bibtex
@misc{lux2026pro,
  title  = {Lux-V2-Pro: Capability-Preserving Korean Domain Adaptation of Gemma-4},
  author = {{PoSTMEDIA AI Lab}},
  year   = {2026},
  url    = {https://huggingface.co/PoSTMEDIA/Lux-V2-Pro}
}
```

## Contact

Questions and feedback — please open a discussion on the model page.
