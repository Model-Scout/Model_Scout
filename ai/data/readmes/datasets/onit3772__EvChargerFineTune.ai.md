---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: url
    dtype: string
  download_size: 914
  dataset_size: 914
task_categories:
- text-generation
language:
- ko
tags:
- KoAlpaca
pretty_name: EvChargerFineTune.ai
configs:
  - config_name: default
    data_files:
      - split: train
        path: ko_alpaca_charger_seedset.jsonl
---
# Dataset Card for "EvChargerFineTune.ai"

## Project Repo

- Github Repo: No Repo

## How to use

```python
>>> from datasets import load_dataset
>>> ds = load_dataset("onit3772/EvChargerFineTune.1a", split='train', streaming=True)
>>> ds
Dataset({
    features: ['instruction', 'output', 'url'],
    num_rows: 3
})
```


```python
>>> ds[0]
{
        "instruction": "회원 카드 인증 오류",
        "output": "회원 인증 오류에 대해 즉시 확인 중입니다. 잠시 후에 다시 시도해주세요.더 많은 도움이 필요하시다면 언제든지 도와드리겠습니다.",
		"url": "https://ai.on-it.co.kr"
    }
```