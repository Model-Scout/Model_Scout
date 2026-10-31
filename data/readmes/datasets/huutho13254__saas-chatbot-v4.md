---
language:
- vi
- en
- ja
- ko
- zh
license: apache-2.0
task_categories:
- text-generation
tags:
- chatbot
- saas
- tool-calling
- multi-industry
- qwen3.5
- fine-tuning
- chatml
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# SaaS Chatbot V4 Dataset

Multi-industry, multilingual conversational dataset for fine-tuning LLMs as SaaS AI chatbot agents with tool calling.

## Stats

| Metric | Value |
|--------|-------|
| Train | 4,043 |
| Test | 450 |
| Total messages | 64,645 |
| Avg msgs/conv | 14.4 |
| Think blocks | 29,345 (21% empty) |
| Tool calls | 15,215 |
| Tool responses | 15,387 |

## Industries (8)

E-commerce (1,301), Travel (641), Services (504), Food (490), Beauty (478), Healthcare (404), Education (357), Real Estate (318)

## Languages

Vietnamese (primary), English, Japanese, Korean, Chinese

## Format

JSONL with ChatML. Each line:

```json
{
  "messages": [
    {"role": "system", "content": "System prompt with <tools>...</tools>"},
    {"role": "user", "content": "User message"},
    {"role": "assistant", "content": "<think>reasoning</think>Response with <tool_call>{...}</tool_call>"},
    {"role": "tool", "content": "<tool_response>{...}</tool_response>"},
    {"role": "assistant", "content": "<think>...</think>Final response"}
  ]
}
```

## Features

- **Thinking**: `<think>...</think>` (always English regardless of response language)
- **Tool calling**: Hermes JSON `<tool_call>{"name": "...", "arguments": {...}}</tool_call>`
- **26 tools**: Product search, orders, CRM, scheduling, promotions, escalation
- **Consultative selling**: Discovery questions, objection handling, cross-sell/upsell
- **No dead-ends**: Every bot response ends with question/CTA/hook

## Usage

```python
from datasets import load_dataset
ds = load_dataset("huutho13254/saas-chatbot-v4")
print(f"Train: {len(ds['train'])}, Test: {len(ds['test'])}")
```

## Quality Filters

- No Vietnamese in thinking blocks (English only)
- No banned phrases ("Dạ vâng ạ" standalone, etc.)
- Valid message structure (system -> user -> assistant flow)
