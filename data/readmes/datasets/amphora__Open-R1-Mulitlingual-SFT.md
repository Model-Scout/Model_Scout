---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: response
    dtype: string
  - name: language
    dtype: string
  - name: source
    dtype: string
  - name: message
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 5546683448
    num_examples: 127552
  download_size: 2495800705
  dataset_size: 5546683448
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
language:
- af
- ar
- zh
- en
- fr
- de
- he
- id
- it
- ja
- es
- tr
- vi
- ko
---


# Open-R1-Mulitlingual-SFT

## Overview
**Open-R1-Mulitlingual-SFT** is a curated dataset designed for multilingual supervised fine-tuning.
The source data comprises multiple datasets containing original prompts and responses, which were subsequently translated into 14 languages using GPT-4o.

## Sources
The dataset is derived from:
- **open-thoughts/OpenThoughts-114k**  
  [Hugging Face: open-thoughts/OpenThoughts-114k](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k)
- **bespokelabs/Bespoke-Stratos-17k**  
  [Hugging Face: bespokelabs/Bespoke-Stratos-17k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k)

## Languages Covered
The dataset spans 14 languages:
- Afrikaans
- Arabic
- Chinese (Simplified)
- English
- French
- German
- Hebrew
- Indonesian
- Italian
- Japanese
- Korean
- Spanish
- Turkish
- Vietnamese

## Citation
```
@article{son2025linguistic,
  title={Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning},
  author={Son, Guijin and Hong, Jiwoo and Ko, Hyunwoo and Thorne, James},
  journal={arXiv preprint arXiv:2502.17407},
  year={2025}
}
```

## Contact
```
spthsrbwls123@yonsei.ac.kr
```