---
license: other
task_categories:
- text-generation
language:
- en
- zh
- ja
- ko
- ru
tags:
- persona
- sft
- chatml
- cleaned
---

# super-lfm-clean-sft-v1

Cleaned SFT dataset. 50000 rows from 137 sources.

## Cleaning applied
- Bot-like/assistant-like responses filtered out (3,155 rows removed)
- Benchmark/academic sources removed (47,757 rows removed)
- Persona data upsampled 5x
- All assistant turns have think-fix (<think></think> prefix)
- All rows end on assistant turn
- Deduplicated

## Splits
- train: 47548 rows
- validation: 2452 rows
