---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source_type
    dtype: string
  - name: has_thinking
    dtype: bool
  - name: hash
    dtype: string
  splits:
  - name: train
    num_bytes: 142104068.69300157
    num_examples: 22279
  - name: test
    num_bytes: 1441515.3069984447
    num_examples: 226
  download_size: 79806236
  dataset_size: 143545584.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

[[<img src="https://huggingface.co/crownelius/Crow-9B-Opus-4.6-Distill-Heretic_Qwen3.5/resolve/main/banner.png" width="350"/>](https://ko-fi.com/abcuo)](https://ko-fi.com/abcuo)

---

## Stats

| Metric | Value |
|--------|-------|
| Total prompt tokens | 0 |
| Total completion tokens | 0 |
| Total tokens | 0 |
| Total cost | $0 (USD) |
| Average turns | 1.00 |
| Average tool calls | 0.00 |
| Average tokens per row | 0 |

*Cost estimated using Mixed pricing on [OpenRouter](https://openrouter.ai) ($1.0/M input, $5.0/M output)*

---

<p align="center">
  <img src="https://huggingface.co/datasets/Crownelius/Crow-Heretic-TeichAI-Unified/resolve/main/assets/crownelius_banner.png" alt="a dataset by Crownelius" width="100%">
</p>
