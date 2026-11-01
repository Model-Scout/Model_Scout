---
language:
- aa
- af
- ar
- as
- az
- be
- bg
- bn
- bs
- ca
- cs
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- ha
- he
- hi
- hr
- hu
- hy
- id
- ie
- it
- iw
- ja
- ka
- kk
- ko
- ku
- la
- lt
- lv
- mk
- ms
- my
- nl
- nn
- 'no'
- oc
- pl
- pt
- ro
- ru
- rw
- sa
- sco
- si
- sk
- sl
- sr
- sv
- sw
- ta
- th
- tl
- tlh
- tr
- tt
- uk
- vi
- vo
- war
- xh
- zh
license: cc-by-4.0
task_categories:
- text-generation
---

# mR3 Dataset: Multilingual Rubric-Agnostic Reward Reasoning

[**Project Page**](https://rubricreward.github.io) | [**Paper**](https://huggingface.co/papers/2510.01146) | [**Code**](https://github.com/rubricreward/mr3)

This is the dataset used to train **mR3**, a massively multilingual, rubric-agnostic reward reasoning model.

## Dataset Summary

The mR3 training dataset contains **100,000 high-quality samples** curated from an initial pool of 4 million samples across 125 languages. It is designed to train reward models that can provide reasoning traces in both English and non-English settings, covering 72 languages in total.

### Key Features
- 🌍 **Language Diversity**: Covers 72 languages, providing the broadest language coverage in reward modeling to date.
- 🧠 **Non-English Reasoning**: Supports non-English reasoning via language forcing, improving interpretability for non-English speakers.
- 📊 **Task Diversity**: Supports point-wise, pairwise, and binary classification tasks—covering instruction following, reasoning, and factuality.
- 🧩 **Rubric Agnosticism**: Generalizes across rubrics instead of relying on fixed evaluation criteria.

## Dataset Construction

1. **Initial Data Filtering and Distillation**: The process began with knowledge distillation from the `gpt-oss-120b` model. Various strategies were used to generate reasoning traces, including:
    - English Prompt + Target Reasoning
    - Target Prompt + English Reasoning
    - Target Prompt + Target Reasoning
2. **Final Curation and Language Alignment**: "Easy" samples (those where the model could reason correctly without difficulty) were discarded to focus training on complex examples. The final dataset is aligned across different prompt and reasoning language settings.

## Citation

If you find our dataset useful, please cite our paper!

```bibtex
@article{anugraha2025mr3,
  title={mR3: Multilingual Rubric-Agnostic Reward Reasoning Models},
  author={Anugraha, David and Hung, Shou-Yi and Tang, Zilu and Lee, Annie En-Shiun and Wijaya, Derry and Winata, Genta Indra},
  journal={arXiv preprint arXiv:2510.01146},
  year={2025}
}
```