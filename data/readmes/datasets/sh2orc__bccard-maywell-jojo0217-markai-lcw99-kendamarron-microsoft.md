---
language:
- ko
license: apache-2.0
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 1347152241
    num_examples: 1706579
  download_size: 709953599
  dataset_size: 1347152241
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

[Dataset merged]
- maywell/ko_wikidata_QA
- jojo0217/korean_rlhf_dataset
- BCCard/BCCard-Finance-Kor-QnA
- MarkrAI/KoCommercial-Dataset
- lcw99/wikipedia-korean-20240501-1million-qna
- maywell/gpt4_evol_1.3k
- Kendamarron/jimba-wiki-instruction-calm3
- microsoft/orca-math-word-problems-200k
- pankajmathur/WizardLM_Orca
