---
license: cc-by-nc-sa-4.0
pretty_name: Elysium X 500 FR Dataset (HumanMonitored v0.5)
language: [en, hi, es, fr, de, pt, bn, ja, ko, zh, ar]
task_categories: [text-classification]
size_categories: [10K<n<100K]
tags: [emotion, multilingual, multi-label, synthetic, conversations]
configs:
- config_name: default
  data_files:
  - {split: train, path: data/train.jsonl}
  - {split: validation, path: data/dev.jsonl}
  - {split: test, path: data/test.jsonl}
---

<p align="center"><img src="assets/banner.svg" alt="Elysium X 500 FR Dataset" width="100%"></p>

# 🌌 Elysium X 500 FR Dataset (HumanMonitored v0.5)

<p align="center"><a href="https://huggingface.co/open-nhe/Elysium-X-500-FR"><img src="https://img.shields.io/badge/Model-LoRA%20adapter-ec4899?style=for-the-badge"></a> <a href="https://doi.org/10.5281/zenodo.23179294"><img src="https://img.shields.io/badge/Paper-Zenodo%20DOI-6366f1?style=for-the-badge"></a> <a href="https://github.com/itsppm76/Elysium-X-500-FR"><img src="https://img.shields.io/badge/GitHub-code%20%26%20guide-0ea5e9?style=for-the-badge"></a> <img src="https://img.shields.io/badge/Licence-CC%20BY--NC--SA%204.0-a855f7?style=for-the-badge"></p>

12,000 short conversations, each with one "target line" labelled with one or two of 500 emotion coordinates (with a strength of 0.25, 0.5, 0.75 or 1.0). It was made by the OpenNHE Technologies team to train and test the Elysium X 500 FR emotion model.

**Licence:** CC BY-NC-SA 4.0. Non-commercial use only. Please do not call this "open source" in the strict sense.

## 📦 What is in it

<p align="center"><img src="assets/facts.svg" alt="Dataset contents" width="100%"></p>

| Item | Value |
|---|---|
| Rows | 12,000 (train 9,000 / dev 1,500 / test 1,500) |
| Languages | 12 x 1,000 rows: English, Hindi (written mostly as romanised Hinglish), Hinglish, Spanish, French, German, Portuguese, Bengali, Japanese, Korean, Mandarin Chinese, Arabic |
| Labels | 500 coordinates in `taxonomy_500.csv` (id, family, name, definition) |
| Multi-label rows | 339 rows carry two labels |
| Real people's data | None. All conversations are synthetic. |

Each row has: `example_id`, `split`, `language`, `style`, `topic`, `target_text` (the line to classify), `gold_dimensions` (the labels), `coordinate`, and the surrounding conversation (`causal_payload`, `full_conversation`).

## 🔍 How it was made and checked ("human-monitored", not human-gold)

Rows were generated from templates and reviewed by the project owner (reviewer field: Pratham Prateek Mohanty). Review status says "COMPLETE - GOOD TO GO" on every row, but the written quality-review sheet only covers about 100 rows. Treat the labels as human-monitored, not as a gold standard.

## ⚠️ Known limits (please read)

- **Templated text.** Only 8,936 of 12,000 target lines are unique. Many rows share sentence frames.
- **Emotion name leakage.** In many non-English rows the English emotion name is pasted into the sentence, which makes them easy. In our model evaluation these "with-name" rows scored 95% while rows without the emotion name scored about 20%. If you measure your own model, report the no-name rows separately.
- **Hindi is mostly Hinglish.** The "Hindi" rows are largely romanised Hindi mixed with English, not Devanagari prose.
- **Splits overlap.** About 38% of the dev and test target lines also appear in train (by exact text). The Elysium X 500 FR model was trained and tested on a cleaned re-split with zero overlap. De-duplicate by text before you train and test.
- Labels are one coordinate per row in 97% of cases. Different emotions can fit the same sentence.

## 💜 Citation and credit

OpenNHE Technologies (open-nhe), Project NHE. Elysium X 500 FR dataset, HumanMonitored v0.5, 2026.
