---
task_categories:
- text-generation
- text2text-generation
- question-answering
language:
- ar
- en
- es
- zh
- fr
- ru
- pt
- it
- ko
- ja
configs:
- config_name: full
  data_files:
  - split: arabic
    path: arabic.json
  - split: chinese
    path: chinese.json
  - split: english
    path: english.json
  - split: spanish
    path: spanish.json
  - split: french
    path: french.json
  - split: russia
    path: russia.json
  - split: korean
    path: korean.json
  - split: japanese
    path: japanese.json
  - split: italian
    path: italian.json
  - split: portuguese
    path: portuguese.json
  - split: russia_local
    path: russia_local.json
  - split: french_local
    path: french_local.json
  - split: chinese_local
    path: chinese_local.json
  - split: arabic_local
    path: arabic_local.json
  - split: spanish_local
    path: spanish_local.json
  - split: korean_local
    path: korean_local.json
  - split: japanese_local
    path: japanese_local.json
  - split: portuguese_local
    path: portuguese_local.json
  - split: italian_local
    path: italian_local.json
---

# Dataset Card for "omgeval"

<!-- Provide a quick summary of the dataset. -->

We introduce OMGEval, the first Open-source Multilingual Generative test set that can assess the capability of LLMs in different languages. 
For each language, OMGEval provides 804 open-ended questions, covering a wide range of important capabilities of LLMs, such as general knowledge, logical reasoning, and so on. 
Each question is rigorously verified by human annotators. 
Notably, to sufficiently reflect the compatibility of LLMs in different cultural backgrounds, we perform localization for each non-English language. 
Specifically, the current version of OMGEval includes 9 languages (i.e., Zh, Ru, Fr, Es, Ar, Pt, It, Ko, Ja).

## Dataset Details

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Repository:** https://github.com/blcuicall/OMGEval
- **Paper:** https://arxiv.org/pdf/2402.13524

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

[More Information Needed]

## Dataset Creation

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

[More Information Needed]

### Annotations

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

[More Information Needed]

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

[More Information Needed]

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

[More Information Needed]

## Citation
```
@misc{liu2024omgeval,
      title={OMGEval: An Open Multilingual Generative Evaluation Benchmark for Large Language Models}, 
      author={Yang Liu and Meng Xu and Shuo Wang and Liner Yang and Haoyu Wang and Zhenghao Liu and Cunliang Kong and Yun Chen and Yang Liu and Maosong Sun and Erhong Yang},
      year={2024},
      eprint={2402.13524},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```