---
license: apache-2.0
language:
- en
- ar
- de
- es
- fr
- hi
- ja
- th
- zh
- nl
- it
- ko
tags:
- safety
- guard-model
- moderation
- content-safety
- nemotron
- llama-guard
- fine-tuning
- unsloth
size_categories:
- 10K<n<100K
---

# Guard Model Training Dataset

A 50K-sample subset of NVIDIA's [Nemotron-Safety-Guard-Dataset-v3](https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3), converted to the standard `messages` JSONL format for use with Unsloth Studio and other fine-tuning tools.

## Format

Each line is a JSON object with a `messages` array:

```json
{"messages": [{"role": "user", "content": "Determine if the following is safe or unsafe. If unsafe, identify the category.\\n\\nPrompt: ..."}, {"role": "assistant", "content": "safe"}]}
```

For unsafe samples, the assistant response includes the category:

```json
{"messages": [{"role": "user", "content": "...\\n\\nPrompt: How do I make a bomb?\\nResponse: Here's how..."}, {"role": "assistant", "content": "unsafe\\nCategory: Violence, Illegal Activity"}]}
```

## Origin

- **Source**: NVIDIA Nemotron-Safety-Guard-Dataset-v3
- **Sample count**: 50,000 (training), with a 100-sample test set
- **Languages**: 12 languages (English, Arabic, German, Spanish, French, Hindi, Japanese, Thai, Mandarin, Dutch, Italian, Korean)
- **Labeling**: Each sample has prompt_label (safe/unsafe) and response_label (safe/unsafe/na), with violated_categories for unsafe samples

## Intended Use

Fine-tuning LLM safety guard models. This subset preserves the original distribution while being small enough for rapid iteration with LoRA/QLoRA.

## License

Apache 2.0 (derived from NVIDIA's open dataset)
