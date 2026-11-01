---
license: apache-2.0
task_categories:
- zero-shot-classification
- question-answering
- translation
language:
- en
- de
- nl
- fr
- es
- it
- pt
- ru
- zh
- ja
- ko
- tr
- ar
- pl
- hi
- th
- sw
- ha
- ur
- af
- id
- uk
- el
- lv
- cy
- is
- bn
- ne
- pa
- mr
- te
tags:
  - synthetic
  - text
  - math
  - reasoning
  - instruction
configs:
  - config_name: ARC
    data_files: ARC/arc.jsonl
  - config_name: ARC-flatten
    data_files: ARC/arc_flatten.jsonl
  - config_name: GSM
    data_files: GSM/gsm.jsonl
  - config_name: GSM-flatten
    data_files: GSM/gsm_flatten.jsonl
  - config_name: MMLU
    data_files: MMLU/mmlu.jsonl
  - config_name: MMLU-flatten
    data_files: MMLU/mmlu_flatten.jsonl
  - config_name: WINOGRANDE
    data_files: WINOGRANDE/winogrande.jsonl
  - config_name: WINOGRANDE-flatten
    data_files: WINOGRANDE/winogrande_flatten.jsonl
---

These are the [GSM8K](https://huggingface.co/datasets/openai/gsm8k) and [ARC](https://huggingface.co/datasets/allenai/ai2_arc) dataset translated by Google Translate. 

```
BibTex
@misc{lu2024languagecountslearnunlearn,
      title={Every Language Counts: Learn and Unlearn in Multilingual LLMs}, 
      author={Taiming Lu and Philipp Koehn},
      year={2024},
      eprint={2406.13748},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.13748}, 
}
```
