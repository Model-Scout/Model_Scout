---
license: mit
language:
- ko
size_categories:
- 100K<n<1M
pretty_name: Korean QA dataset
---

# Korean QA dataset

## Description
A Korean instruction-tuning dataset generated with an LLM. Each sample is a single-turn pair in the format:

- `prompt`: `Human: ...`
- `response`: `GPT: ...`

The dataset is intended for general-purpose instruction tuning in Korean. Responses are 2–3 sentences and written in Korean.

## Data Format
Each line in `QA_dataset.jsonl` is a JSON object:

```jsonl
{"prompt":"Human: 질문...","response":"GPT: 답변..."}
```

## How It Was Generated
- Generated using an LLM
- Question generation: one-line user question per sample
- Answer generation: 2–3 sentence answer per sample
- Sampling: topics drawn from a broad topic list; recent-question avoidance to reduce repeats

## Intended Use
- Instruction tuning for Korean-language models
- General-purpose Q/A style tasks

## Limitations
- Synthetic data may contain factual errors or bias
- Some topics may be over/under-represented depending on generation settings