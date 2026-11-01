---
license: apache-2.0
language:
- ko
- en
base_model:
- google/gemma-4-26B-A4B-it
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
tags:
- sft
- trl
- transformers
- gemma-4
- full-fine-tuning
- moe
- korean
---

# Lux-V2

**Lux-V2** is a **Korean-enhanced, fully fine-tuned LLM** built on top of [`google/gemma-4-26B-A4B-it`](https://huggingface.co/google/gemma-4-26B-A4B-it) by **PoSTMEDIA AI Lab**, succeeding [Lux-V1](https://huggingface.co/PoSTMEDIA/Lux-V1).

It is produced with the **second generation of PoSTMEDIA's in-house Capability-Preserving Full Fine-Tuning research** — a training methodology designed so that deep domain adaptation does **not** erode the reasoning, instruction-following, and multilingual abilities of the base model. Compared to Lux-V1, the V2 generation delivers a **large, across-the-board benchmark improvement** while adding substantial Korean domain knowledge.

---

## Highlights

- **Large upgrade over Lux-V1** — wins on 16 of 18 internal benchmarks, with competition-math gains of +10 to +20 points
- **Korean domain knowledge built in** — trained on PoSTMEDIA's in-house Korean synthetic datasets spanning **seven domains**: general conversation, coding, instruction following, law, cultural heritage, tourism, and mathematics, plus the PoSTMEDIA identity dataset
- **Base capability preserved and improved** — unlike naive full fine-tuning, the V2 methodology keeps (and on most axes improves) the base model's abilities
- **MoE efficiency** — 26B total / ~4B active parameters at serving time
- **Verified training data** — the synthetic datasets are produced with execution- and rule-based verification pipelines rather than unfiltered generation

---

## Model Overview

| Specification | Details |
|---------------|---------|
| Base Model | [`google/gemma-4-26B-A4B-it`](https://huggingface.co/google/gemma-4-26B-A4B-it) |
| Parameters | 26B total / ~4B active |
| Architecture | Decoder-only Transformer (MoE) |
| Training Precision | BF16 |
| Inference Precision | BF16 |
| Context Length | Inherits from Gemma-4 base |
| Fine-Tuning Method | Full-parameter SFT (Capability-Preserving recipe, 2nd gen) |
| Languages | Korean, English |

---

## What's New vs Lux-V1

Lux-V1 demonstrated that a full fine-tune could adapt Gemma-4 without destroying it. **Lux-V2 goes further: it adapts the model to Korean domains while measurably improving general capability.** All results below were measured in-house under a single unified protocol (identical prompts, sampling, and generation budgets for both models).

| Benchmark | gemma-4-26B-A4B-it (base) | Lux-V1 | **Lux-V2** |
|---|---:|---:|---:|
| MMLU | **84.2** | 82.0 | 83.8 |
| AIME 2024 | **90.0** | 73.3 | **90.0** |
| AIME 2025 | 73.3 | 60.0 | **80.0** |
| HMMT 2025 | **66.7** | 36.7 | 56.7 |
| IFEval | 89.6 | 88.5 | **91.7** |
| KMMLU | 72.8 | 70.7 | **72.9** |
| KMMLU-Pro | **72.0** | 67.8 | 70.6 |
| CLIcK | 81.3 | 79.8 | **82.0** |
| KoBALT | **68.3** | 59.1 | 65.9 |
| HAE-RAE Bench | 79.7 | 76.8 | **80.1** |
| HRM8K | 83.5 | 79.9 | **83.6** |
| KoSimpleQA | 86.7 | 83.7 | **87.9** |
| KoSQA-EM | 33.6 | 28.7 | **34.1** |
| **Average (all 18 benchmarks)** | 74.5 | 69.1 | **74.8** |

The full 18-benchmark suite shows 16 wins and 2 minor regressions (GSM8K −1.9, GPQA −1.0) versus Lux-V1. Averaged over all 18 benchmarks, **Lux-V2 scores 74.8 — above both the original Gemma-4 base (74.5) and Lux-V1 (69.1)** — i.e., the Korean domain adaptation comes with a net gain over the unmodified base model, not a trade-off.

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

model_name = "PoSTMEDIA/Lux-V2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "경복궁의 역사적 의미를 세 문장으로 설명해줘."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

---

## Use Cases

- Korean-first assistants that must retain strong general reasoning
- Korean domain QA (law, cultural heritage, tourism) with source-grounded knowledge
- Mathematical and coding assistance in Korean and English
- Drop-in upgrade for existing Lux-V1 deployments

---

## Safety & Limitations

- The model can generate incorrect or outdated information; verify high-stakes outputs.
- Korean domain knowledge reflects the training data snapshot and may not cover recent changes (e.g., amended laws).
- Inherits the general limitations and usage considerations of the Gemma-4 base model.

---

## Citation

```bibtex
@misc{lux2026,
  title  = {Lux-V2: Capability-Preserving Korean Domain Adaptation of Gemma-4},
  author = {{PoSTMEDIA AI Lab}},
  year   = {2026},
  url    = {https://huggingface.co/PoSTMEDIA/Lux-V2}
}
```

## Contact

Questions and feedback — please open a discussion on the model page.
