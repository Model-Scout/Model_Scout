---
language:
- en
- ko
dataset_info:
  features:
  - name: text_en
    dtype: string
  - name: text_ko
    dtype: string
  splits:
  - name: train
    num_bytes: 75151
    num_examples: 416
  - name: test
    num_bytes: 18694
    num_examples: 104
  download_size: 41666
  dataset_size: 93845
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# harmful_behaviors_kr

This dataset keeps the original English prompt in `text_en` and adds a Korean translation in `text_ko`.

The translation source files are stored in `translations/train_ko.txt` and `translations/test_ko.txt`. To rebuild the Parquet files from those translations, run:

```bash
uv run python scripts/build_bilingual_dataset.py
```
