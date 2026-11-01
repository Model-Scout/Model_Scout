---
language:
  - en
  - de
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - pt
  - zh
license: cc-by-4.0
task_categories:
  - text-generation
tags:
  - self-cognition
  - identity
  - synthetic
  - multilingual
---

# Self-Cognition Identity Dataset (Nemotron-3-Super-120B)

Synthetic self-cognition / identity-following training data for the Jupiter model,
generated using Nemotron-3-Super-120B with reasoning disabled.

## How this dataset was made

### 1. Prompt sourcing

Prompts were extracted from [nvidia/Nemotron-RL-Identity-Following-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-Identity-Following-v1)
(21,660 identity-probing prompts across 10 languages). We took a **stratified sample
of 200 prompts per language** (2,000 total) to ensure balanced multilingual coverage.

The target language for each prompt was parsed from the dataset's `principle` column.

### 2. Response generation

Responses were generated using **Nemotron-3-Super-120B** (reasoning OFF) via a
self-hosted vLLM endpoint. Each prompt was paired with a system prompt describing
the Jupiter model identity, Locai Labs as the developer, and the GB1 product.

Key system prompt instructions:
- Identity: Jupiter, developed by Locai Labs in London
- Be concise
- Respond in the user's language
- Technical background (post-trained from Nemotron) placed at low priority

### 3. Format

Each row contains a `messages` list in standard chat format:

```json
[
  {"role": "user", "content": "Are you ChatGPT?"},
  {"role": "assistant", "content": "No, I am Jupiter, developed by Locai Labs in London."}
]
```

## Languages

| Language | Count |
|----------|-------|
| English | 200 |
| German | 200 |
| Spanish | 200 |
| French | 200 |
| Hindi | 200 |
| Italian | 200 |
| Japanese | 200 |
| Korean | 200 |
| Portuguese | 200 |
| Chinese | 200 |

## Intended use

Fine-tuning / post-training LLMs for identity-following behaviour across multiple
languages. Designed so the model learns to identify itself as Jupiter (Locai Labs)
and correctly deny being ChatGPT, GPT-4, or models from OpenAI, Google, Microsoft,
IBM, etc.
