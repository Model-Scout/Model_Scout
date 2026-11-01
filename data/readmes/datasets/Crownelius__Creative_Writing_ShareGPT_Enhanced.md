---
language:
  - en
license: apache-2.0
tags:
  - creative-writing
  - synthetic
  - enhanced
  - step-3.5-flash
  - sharegpt
dataset_info:
  features:
    - name: conversations
      list:
        - name: from
          dtype: string
        - name: value
          dtype: string
  splits:
    - name: train
      num_examples: 5116
size_categories:
  - 1K<n<10K
task_categories:
  - text-generation
  - conversational
pretty_name: Creative Writing ShareGPT Enhanced
---

[[<img src="https://huggingface.co/crownelius/Crow-9B-Opus-4.6-Distill-Heretic_Qwen3.5/resolve/main/banner.png" width="350"/>](https://ko-fi.com/abcuo)](https://ko-fi.com/abcuo)

# Creative Writing ShareGPT — Enhanced Edition ✨

> **High-quality creative writing dataset with regenerated responses using StepFun's Step-3.5-Flash model.**

This dataset is an **enhanced version** of [ChaoticNeutrals/Creative_Writing-ShareGPT](https://huggingface.co/datasets/ChaoticNeutrals/Creative_Writing-ShareGPT), where all final AI responses have been regenerated using **[stepfun/step-3.5-flash](https://openrouter.ai/stepfun/step-3.5-flash:free)** with a carefully engineered system prompt designed to produce literary-quality creative writing.

## What Changed

- **Original human prompts preserved** — All user messages remain exactly as they were
- **Prior conversation context preserved** — Multi-turn conversation history is intact
- **Final AI response regenerated** — The last GPT response in each conversation was regenerated with an advanced creative writing system prompt
- **Anti-slop filtering** — Responses containing excessive AI clichés ("delve", "tapestry", "testament to", etc.) were automatically rejected and regenerated
- **Quality gates** — Minimum response length enforced; short/empty responses were retried

## System Prompt Philosophy

The regeneration prompt enforces:
1. **Show-don't-tell prose** — Sensory immersion over emotional labels
2. **Prose rhythm as music** — Deliberate sentence length variation
3. **Subtext and implication** — What's unsaid carries meaning
4. **Unique character voices** — Every character sounds distinct
5. **World-building through lived experience** — No info-dumps
6. **Thematic depth without preaching** — Themes emerge organically

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Conversations | 5,116 |
| Total GPT Responses | 9,793 |
| Avg Turns per Conversation | 3.8 |
| Avg Response Length | 2,546 characters |
| Estimated Total Words | ~5.0 million |
| High Complexity Conversations | 258 |
| Medium Complexity Conversations | 4,856 |

## Format

Standard ShareGPT conversation format:

```json
{
  "conversations": [
    {"from": "human", "value": "Write a dark fantasy scene where..."},
    {"from": "gpt", "value": "The enhanced literary-quality response..."}
  ]
}
```

## Source & Attribution

- **Original Dataset**: [ChaoticNeutrals/Creative_Writing-ShareGPT](https://huggingface.co/datasets/ChaoticNeutrals/Creative_Writing-ShareGPT)
- **Enhancement Model**: [stepfun/step-3.5-flash](https://openrouter.ai/stepfun/step-3.5-flash:free) (free tier via OpenRouter)
- **Generation Method**: Automated pipeline with quality filtering, checkpoint/resume, and anti-slop detection

## Usage

```python
from datasets import load_dataset

ds = load_dataset("crownelius/Creative_Writing_ShareGPT_Enhanced", split="train")

# Print a sample conversation
for turn in ds[0]["conversations"]:
    print(f"[{turn['from']}]: {turn['value'][:200]}...")
```

## License

Apache 2.0 — Same as the original dataset.

---

## Stats

| Metric | Value |
|--------|-------|
| Total prompt tokens | 1,067,256 |
| Total completion tokens | 11,489,852 |
| Total tokens | 12,557,108 |
| Total cost | $58.52 (USD) |
| Average turns | 1.91 |
| Average tool calls | 0.00 |
| Average tokens per row | 1,227.24 |

*Cost estimated using Unknown pricing on [OpenRouter](https://openrouter.ai) ($1.0/M input, $5.0/M output)*

---

<p align="center">
  <img src="https://huggingface.co/datasets/Crownelius/Creative_Writing_ShareGPT_Enhanced/resolve/main/assets/crownelius_banner.png" alt="a dataset by Crownelius" width="100%">
</p>
