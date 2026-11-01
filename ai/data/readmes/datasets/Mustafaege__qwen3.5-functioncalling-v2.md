---
language:
- en
- ko
license: apache-2.0
pretty_name: Qwen3.5 Function Calling Dataset v2
size_categories:
- 100K<n<1M
task_categories:
- text-generation
tags:
- function-calling
- tool-use
- sft
- chat
- qwen3
- qwen3.5
- instruction-following
- structured-output
- json
- fine-tuning
- bilingual
- korean
- open-source
- expanded-dataset
annotations_creators:
- machine-generated
language_creators:
- found
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# Qwen3.5 Function Calling Dataset v2

An expanded function-calling SFT dataset combining **glaiveai/glaive-function-calling-v2** and **Saxo/alpaca_function_calling_dataset**, unified into Qwen3 messages format. Extends v1 with bilingual (EN/KO) instruction diversity.

## Dataset Summary

| Property | Value |
|----------|-------|
| **Total Samples** | ~225K |
| **Train Split** | ~202K |
| **Test Split** | ~23K |
| **Sources** | glaive-function-calling-v2 + alpaca_function_calling_dataset |
| **Format** | Qwen3 messages |
| **Languages** | English, Korean |
| **License** | Apache 2.0 |

## v1 vs v2 Comparison

| Version | Samples | Languages | New Sources |
|---------|---------|-----------|-------------|
| **v1** | 112,960 | EN | glaiveai/glaive-function-calling-v2 |
| **v2** (this) | ~225K | EN + KO | + Saxo/alpaca_function_calling_dataset |

## What's New in v2?

- **Bilingual**: Added Korean function calling examples from Saxo/alpaca dataset
- **More Diversity**: Alpaca-format instructions converted from Llama 3 instruct format
- **Better Coverage**: RAG-style function calling, multi-step instructions
- **2x More Data**: ~225K vs 112K samples

## Dataset Structure

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `messages` | `list[dict]` | Conversation turns with `role` and `content` |

### Role Types

| Role | Description |
|------|-------------|
| `system` | Function schema definitions |
| `user` | User request or function response |
| `assistant` | Function call JSON or natural language reply |

## Sources

| Dataset | Format | Samples | Key Features |
|---------|--------|---------|--------------|
| [glaiveai/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) | `system` + `chat` | 112,960 | Multi-turn, function responses |
| [Saxo/alpaca_function_calling_dataset](https://huggingface.co/datasets/Saxo/alpaca_function_calling_dataset) | `system` + `instruction` + `output` | ~112,390 | EN + KO bilingual, RAG-focused |

## Format

### Standard Multi-Turn Example

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant with access to the following functions:\n{\n  \"name\": \"search_product\",\n  \"description\": \"Search for a product in the database\",\n  \"parameters\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"query\": {\"type\": \"string\", \"description\": \"Search query\"}\n    },\n    \"required\": [\"query\"]\n  }\n}"
    },
    {
      "role": "user",
      "content": "Find me a blue winter jacket under $100"
    },
    {
      "role": "assistant",
      "content": "<functioncall> {\"name\": \"search_product\", \"arguments\": {\"query\": \"blue winter jacket under 100\"}}"
    },
    {
      "role": "user",
      "content": "FUNCTION RESPONSE: {\"results\": [{\"name\": \"Alpine Jacket\", \"price\": 89.99, \"color\": \"blue\"}]}"
    },
    {
      "role": "assistant",
      "content": "I found a matching item: Alpine Jacket in blue for $89.99."
    }
  ]
}
```

### Alpaca-style Single Turn (from Saxo source)

```json
{
  "messages": [
    {
      "role": "user",
      "content": "You are a helpful assistant with access to the following functions...\n\nConvert 100 USD to EUR\n\nInput: {\"amount\": 100, \"from\": \"USD\", \"to\": \"EUR\"}"
    },
    {
      "role": "assistant",
      "content": "{\"name\": \"currency_convert\", \"arguments\": {\"amount\": 100, \"from_currency\": \"USD\", \"to_currency\": \"EUR\"}}"
    }
  ]
}
```

## Source Conversions

```python
# --- Glaive format ---
# system -> {"role": "system", "content": system.replace("SYSTEM: ", "")}
# chat   -> split on USER:/ASSISTANT: markers

# --- Alpaca format ---
# instruction + input -> {"role": "user", "content": f"{instruction}\n\nInput: {input}"}
# output             -> {"role": "assistant", "content": output}
```

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("Mustafaege/qwen3.5-functioncalling-v2")

print(dataset)
# DatasetDict({
#     train: Dataset({features: ['messages'], num_rows: ~202000}),
#     test:  Dataset({features: ['messages'], num_rows: ~23000})
# })

# Sample inspection
sample = dataset['train'][0]
for msg in sample['messages']:
    print(f"[{msg['role']}]: {msg['content'][:80]}...")
```

## Training with Unsloth

```python
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-1.7B",
    max_seq_length = 4096,
    load_in_4bit = True,
)

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset['train'],
    args = SFTConfig(
        per_device_train_batch_size = 4,
        max_seq_length = 4096,
        dataset_kwargs = {"skip_prepare_dataset": True},
    ),
)
trainer.train()
```

## Related Datasets

| Version | Samples | Languages | Link |
|---------|---------|-----------|------|
| **v1** | 112,960 | EN | [Mustafaege/qwen3.5-functioncalling-v1](https://huggingface.co/datasets/Mustafaege/qwen3.5-functioncalling-v1) |
| **v2** (this) | ~225K | EN + KO | [Mustafaege/qwen3.5-functioncalling-v2](https://huggingface.co/datasets/Mustafaege/qwen3.5-functioncalling-v2) |

## License

Apache 2.0 — see [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) for details.

---

Built for Qwen3.5 fine-tuning. Part of the [Mustafaege](https://huggingface.co/Mustafaege) model series.
