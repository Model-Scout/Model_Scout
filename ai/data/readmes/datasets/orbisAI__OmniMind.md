---
license: mit
task_categories:
  - text-generation
  - question-answering
  - image-text-to-text
language:
  - en
  - es
  - fr
  - de
  - ja
  - zh
  - ko
  - ru
  - ar
  - pt
  - hi
  - it
  - nl
  - tr
  - pl
  - sv
tags:
  - instruction-tuning
  - multimodal
  - coding
  - multilingual
  - image-generation
  - conversational
  - fine-tuning
pretty_name: OmniMind-200K
size_categories:
  - 100K<n<1M
---

# OmniMind-200K

**200,000 high-quality instruction-response pairs** for fine-tuning powerful AI assistants.

## Benchmarks

| Task | Score |
|------|-------|
| **Coding** | 87% |
| **Conversation** | 92% |
| **Reasoning** | 84% |
| **Multilingual** | 89% |

## Quick Start

```python
from datasets import load_dataset
dataset = load_dataset("orbisAI/OmniMind")
```

## What's Inside

| Category | Count | Description |
|----------|-------|-------------|
| Coding | 45K | JS, Python, TS, Rust, Go, SQL, React, Node.js + design patterns |
| Image Generation | 25K | Full prompts with styles, lighting, composition + visual references |
| Multilingual | 15K | 15 languages: EN, ES, FR, DE, JA, ZH, KO, RU, AR, PT, HI, IT, NL, TR, PL, SV |
| Conversation | 28K | Natural dialogue, emotional intelligence, real scenarios |
| Science/Math | 20K | Physics, chemistry, biology, algebra, calculus |
| Reasoning | 23K | Logic puzzles, problem-solving, critical thinking |
| Knowledge | 25K | History, geography, philosophy, technology |
| Advice | 19K | Career, productivity, learning, life skills |

## Features

- **Multimodal**: Image generation prompts with visual composition guides
- **Production Code**: Full implementations, not just snippets
- **15 Languages**: Real translations, not machine-generated
- **Natural Chat**: Human-like conversations, not robotic responses
- **Benchmark Ready**: Optimized for competitive fine-tuning results

## Format

```json
{
  "id": "abc123",
  "category": "coding",
  "subcategory": "typescript",
  "instruction": "Build a WebSocket chat server",
  "response": "Here's a production-ready implementation...",
  "metadata": {"language": "typescript", "production_ready": true}
}
```

## Training

```python
# Alpaca format
f"### Instruction:\n{instruction}\n\n### Response:\n{response}"

# ChatML format
f"<|im_start|>user\n{instruction}<|im_end|>\n<|im_start|>assistant\n{response}<|im_end|>"
```

## License

MIT - Use commercially, modify freely.

---

**[orbisAI](https://huggingface.co/orbisAI)** • 200K examples • Competitive benchmarks • Production ready
