---
dataset_info:
  features:
  - name: landmark_id
    dtype: int64
  - name: landmark_name
    dtype: string
  - name: country_code
    dtype: string
  - name: language_code
    dtype: string
  - name: domestic_language_code
    dtype: string
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: options
    sequence: string
  splits:
  - name: ar
    num_bytes: 403937000
    num_examples: 3000
  - name: de
    num_bytes: 403669507
    num_examples: 3000
  - name: el
    num_bytes: 404196511
    num_examples: 3000
  - name: en
    num_bytes: 403622746
    num_examples: 3000
  - name: es
    num_bytes: 403687665
    num_examples: 3000
  - name: fr
    num_bytes: 403695235
    num_examples: 3000
  - name: he
    num_bytes: 403818152
    num_examples: 3000
  - name: it
    num_bytes: 403674021
    num_examples: 3000
  - name: ja
    num_bytes: 403752656
    num_examples: 3000
  - name: ko
    num_bytes: 403697230
    num_examples: 3000
  - name: pt
    num_bytes: 403656419
    num_examples: 3000
  - name: ru
    num_bytes: 404124459
    num_examples: 3000
  - name: sr
    num_bytes: 403733115
    num_examples: 3000
  - name: th
    num_bytes: 404470326
    num_examples: 3000
  - name: zh
    num_bytes: 403556098
    num_examples: 3000
  - name: en_sub
    num_bytes: 1089061
    num_examples: 10
  download_size: 2959612936
  dataset_size: 6058380201
configs:
- config_name: default
  data_files:
  - split: ar
    path: data/ar-*
  - split: de
    path: data/de-*
  - split: el
    path: data/el-*
  - split: en
    path: data/en-*
  - split: es
    path: data/es-*
  - split: fr
    path: data/fr-*
  - split: he
    path: data/he-*
  - split: it
    path: data/it-*
  - split: ja
    path: data/ja-*
  - split: ko
    path: data/ko-*
  - split: pt
    path: data/pt-*
  - split: ru
    path: data/ru-*
  - split: sr
    path: data/sr-*
  - split: th
    path: data/th-*
  - split: zh
    path: data/zh-*
  - split: en_sub
    path: data/en_sub-*
license: cc
task_categories:
- visual-question-answering
language:
- ar
- zh
- en
- fr
- de
- el
- he
- it
- ja
- ko
- pt
- ru
- sr
- es
- th
size_categories:
- 10K<n<100K
tags:
- Image
- Text
- Multilingual
---

<a href="https://arxiv.org/abs/2505.15075" target="_blank">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-traveling--across--languages-red?logo=arxiv" height="20" />
</a>
<a href="https://github.com/nlp-waseda/traveling-across-languages" target="_blank" style="display: inline-block; margin-right: 10px;">
    <img alt="GitHub Code" src="https://img.shields.io/badge/Code-traveling--across--languages-white?&logo=github&logoColor=white" />
</a>

# KnowRecall
This repository contains the KnowRecall benchmark, introduced in [Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs](https://arxiv.org/abs/2505.15075). 

## Dataset Description
Imagine a French tourist visiting Tokyo Tower, snapping a photo and asking an MLLM about the tower’s height.
Naturally, they would expect a correct response in their native language.
However, if the model provides the right answer in Japanese but fails to do so in French, it illustrates a critical real-world limitation.
We introduce KnowRecall, a multilingual VQA benchmark that evaluates cross-lingual consistency of factual knowledge in MLLMs.
Unlike existing multilingual culture understanding benchmarks which include questions only in English and the local language, our dataset offers 3,000 multiple-choice questions on 1,500 global landmarks, each available in 15 languages.
This breadth facilitates a comprehensive assessment of cross-lingual consistency across diverse linguistic contexts.

The dataset contains the following fields:
| Field Name             | Description                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- |
| `landmark_id`          | Unique identifier for the landmark in the dataset.                         |
| `landmark_name`        | Name of the landmark depicted in the image.                                |
| `country_code`         | ISO country code representing the location of the landmark.                |
| `language_code`        | ISO 639 language code of the question.                                     |
| `domestic_language_code` | ISO 639 language code of the official language spoken in the country where the landmark is located. |
| `image`                | Image depicting the landmark.                                              |
| `question`             | Question asked based on the image.                                         |
| `answer`               | Ground truth answer to the question.                                       |
| `options`              | Multiple-choice options provided for the question.                         |

## Evaluation
Please refer to our [GitHub repository](https://github.com/nlp-waseda/traveling-across-languages) for detailed information on the evaluation setup.

## Citation

```bibtex
@misc{wang2025travelinglanguagesbenchmarkingcrosslingual,
      title={Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs}, 
      author={Hao Wang and Pinzhi Huang and Jihan Yang and Saining Xie and Daisuke Kawahara},
      year={2025},
      eprint={2505.15075},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.15075}, 
}
```