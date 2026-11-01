---
license: cc-by-nc-4.0
language:
- ko
pretty_name: KorEmpatheticDialogues
tags:
- social dialogue
task_ids:
- conversational
size_categories:
- 10K<n<100K
source_datasets:
- EmpatheticDialogues
splits:
- name: train
  num_examples: 19531
- name: valid
  num_examples: 2769
- name: test
  num_examples: 2547
dataset_size: 24,847
---
# Dataset Card for 💗 KorEmpatheticDialogues

> 🚨 Disclaimer: All models and datasets are intended for research purposes only.

## Dataset Description
- **Repository:** [Code](https://github.com/passing2961/KorEmpatheticDialogues)
- **Paper:** [Paper](https://koreascience.kr/article/CFKO202306643316560.pdf)
- **Point of Contact:** [Young-Jun Lee](mailto:yj2961@kaist.ac.kr)

## Dataset Summary
KorEmpatheticDialogues is a publicly available Korean empathetic dialogue dataset translated from the original [EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues) dataset using the [DeepL](https://www.deepl.com/translator) translator API.

## Languages
Korean

## Dataset Structure

field | type | description
--- | ---  | ---
`dialogue_id` | int | the identifier for the dialogue
`dialogue` | list of dict | the dialogue where each dict entry includes {utter_idx, utter, user_id} 
`situation` | str | the emotional situation sentence
`emotion` | str | the emotion category (e.g., guilty, caring, etc)

## Acknowledgements

This work was supported by a grant from the KAIST-KT joint research project through AI Tech Lab, Institute of Convergence Technology, funded by KT [Project No. G01230605, Development of Task-oriented Persona-based Dialogue Generation Combining Multi-modal Interaction and Knowledge Modeling].

### Citation

Please cite our work if you find the resources in this repository useful:
```
@inproceedings{lee2023language,
  title={Language Model Evaluation Based on Korean-English Empathetic Dialogue Datasets and Personality},
  author={Lee, Young-Jun and Hyeon, JongHwan and Lee, DoKyong and Sung, Joo-Won and Choi, Ho-Jin},
  booktitle={Annual Conference on Human and Language Technology},
  pages={312--318},
  year={2023},
  organization={Human and Language Technology}
}
```