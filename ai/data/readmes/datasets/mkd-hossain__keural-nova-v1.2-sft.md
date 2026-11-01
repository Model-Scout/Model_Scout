---
license: cc-by-sa-4.0
language: [ko, en]
task_categories: [text-generation]
tags: [keural, mkd, sft, korean, instruction-tuning]
size_categories: [100K<n<1M]
---
# Keural Nova v1.2 — SFT dataset (PRIVATE)

The supervised fine-tuning mix used to train **Keural Nova v1.2**. Cleaned & balanced:
**benchmark test-splits excluded**, **code AST-validated**, **identity de-contaminated**,
AI-Hub / non-commercial rows removed. Each row carries accurate `source_name` and `license` fields.

- Total **146,274** rows — train 144,812 / eval 1,462.
- Format: `{"messages":[{"role","content"},...], "source_name":..., "license":...}`

## Composition (by source)
| source_name | rows |
|---|---:|
| ko_conversation | 50,000 |
| magicoder_clean | 25,000 |
| metamath | 12,516 |
| ultrachat | 12,500 |
| openorca | 12,499 |
| kmmlu_train | 11,786 |
| gsm8k_train | 7,473 |
| mmlu_auxtrain | 6,926 |
| ko_longform | 5,000 |
| keural_identity | 1,500 |
| arc_train | 1,074 |

## Licenses (by row)
cc-by-4.0: 50,000 · mit: 77,271 · **cc-by-sa-4.0: 12,860** · apache-2.0: 4,643 · internal (MKD): 1,500

**License note:** the collection is released as **CC BY-SA 4.0** (share-alike, driven by the CC BY-SA
rows); the per-row `license` field is authoritative for each item. Benchmark sources (KMMLU, MMLU,
GSM8K, ARC) use **train / auxiliary_train / dev splits only — never test**. Attribution: chanwoo/kullm
Korean sets, ise-uiuc/Magicoder, Open-Orca/OpenOrca, HuggingFaceH4/ultrachat_200k, meta-math/MetaMathQA,
HAERAE-HUB/KMMLU, cais/mmlu, openai/gsm8k, allenai/ai2_arc. Identity rows are MKD-original.
