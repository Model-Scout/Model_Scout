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
- blend
- think-fix
---

# super-lfm-blend-v4

Blended SFT dataset for the super-lfm project. 279K rows from 87 sources.

## Splits
- train: 279080 rows
- validation: 14643 rows

## Think-fix
Every assistant turn is prefixed with `<think></think>` to fix the empty-content bug.
