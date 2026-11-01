---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
language:
- ko
size_categories:
- 10K<n<100K    
configs:
- config_name: kor-orpo
  data_files:
  - split: train
    path: orpo.json
---
axolotl does not take revision arg as an option and i'm lazy so i made this.

type: chat_template.argilla

### Dataset Source
Created with reference to the following datasets.
* [maywell/ko_Ultrafeedback_binarized](https://huggingface.co/datasets/maywell/ko_Ultrafeedback_binarized)
* [zzunyang/dpo_data](https://huggingface.co/datasets/zzunyang/dpo_data)
* [SJ-Donald/orca-dpo-pairs-ko](https://huggingface.co/datasets/SJ-Donald/orca-dpo-pairs-ko)

| Dataset                      | # Number |
|------------------------------|----------|
| ko_Ultrafeedback_binarized   | 61,966   |
| dpo_data                 	   | 126      |
| orca-dpo-pairs-ko        	   | 36,009   |
| **Total**       		       | 98,101   |