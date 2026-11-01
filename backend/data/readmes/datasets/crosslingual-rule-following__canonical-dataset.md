---
configs:
  - config_name: en
    data_files:
      - split: test
        path: data/en/test.jsonl
  - config_name: am
    data_files:
      - split: test
        path: data/am/test.jsonl
  - config_name: de
    data_files:
      - split: test
        path: data/de/test.jsonl
  - config_name: hi
    data_files:
      - split: test
        path: data/hi/test.jsonl
  - config_name: ig
    data_files:
      - split: test
        path: data/ig/test.jsonl
  - config_name: it
    data_files:
      - split: test
        path: data/it/test.jsonl
  - config_name: ko
    data_files:
      - split: test
        path: data/ko/test.jsonl
  - config_name: ru
    data_files:
      - split: test
        path: data/ru/test.jsonl
  - config_name: sw
    data_files:
      - split: test
        path: data/sw/test.jsonl
  - config_name: ta
    data_files:
      - split: test
        path: data/ta/test.jsonl
  - config_name: tr
    data_files:
      - split: test
        path: data/tr/test.jsonl
  - config_name: ur
    data_files:
      - split: test
        path: data/ur/test.jsonl
  - config_name: yo
    data_files:
      - split: test
        path: data/yo/test.jsonl
language:
  - en
  - am
  - de
  - hi
  - ig
  - it
  - ko
  - ru
  - sw
  - ta
  - tr
  - ur
  - yo
---

# canonical-dataset

A parallel, multilingual dataset on rule-following

## Languages


- `en` — English
- `am` — Amharic
- `de` — German
- `hi` — Hindi
- `ig` — Igbo
- `it` — Italian
- `ko` — Korean
- `ru` — Russian
- `sw` — Swahili
- `ta` — Tamil
- `tr` — Turkish
- `ur` — Urdu
- `yo` — Yoruba

## Loading

```python
from datasets import load_dataset

en = load_dataset("canonical-dataset", "en", split="test")
yo = load_dataset("canonical-dataset", "yo", split="test")
```
