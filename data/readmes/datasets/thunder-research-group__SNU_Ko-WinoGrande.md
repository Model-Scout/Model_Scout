---
dataset_info:
  features:
  - name: sentence
    dtype: string
  - name: option1
    dtype: string
  - name: option2
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 218457
    num_examples: 1267
  download_size: 108695
  dataset_size: 218457
configs:
- config_name: default
  data_files:
  - split: test
    path: data/validation-*
language:
- ko
license: cc-by-4.0
pretty_name: Ko-WinoGrande
---

> Note: Evaluation code and task configurations for this benchmark are available in the [`evaluation_code`](https://github.com/mcrl/korean_benchmarks/tree/main/evaluation_code) directory of the [Korean Benchmark Suite GitHub repository](https://github.com/mcrl/korean_benchmarks). The evaluation setup is built on the Language Model Evaluation Harness and supports standardized model assessment.

# Dataset Card for Ko-WinoGrande

## Dataset Summary

Ko-WinoGrande is a Korean adaptation of the [WinoGrande](https://huggingface.co/datasets/allenai/winogrande) dataset, which tests language models' commonsense reasoning through pronoun resolution tasks. 
Each item is a fill-in-the-blank sentence with two possible antecedents. 
Models must determine which choice best fits the blank given the context. 
The Korean version carefully translates and localizes all examples to maintain logical coherence and cultural appropriateness.

## Supported Tasks and Benchmarks
**Task**: Pronoun Resolution via Commonsense Reasoning    

Ko-WinoGrande evaluates a language model's ability to:
- Perform commonsense reasoning in ambiguous contexts
- Resolve pronouns or referential blanks correctly
- Understand real-world relationships and situations described in Korean

## Languages
ko (Korean)

---
## Dataset Structure

### Dataset Instance Example
```json
{
  "sentence": "지희는 채원이보다 훨씬 뛰어난 외과의사였기 때문에, _는 항상 쉬운 케이스를 맡았습니다.",
  "option1": "지희",
  "option2": "채원이",
  "answer": 2
}
```

### Data Fields
- `sentence`: A Korean sentence with a blank indicating an ambiguous pronoun or reference.
- `option1`, `option2`: Two possible referents for the blank.
- `answer`: The correct option (1 or 2).

### Data Splits
- Single evaluation set (`test` set)
- This Korean dataset was created based on the English [WinoGrande](https://huggingface.co/datasets/allenai/winogrande) dataset's validation set, not the test set, because the labels of the original dataset's test set are blind. See more details in the [WinoGrande leaderboard website](https://leaderboard.allenai.org/winogrande/submissions/get-started).  


---

## Dataset Creation

### Translation Process

The original WinoGrande dataset was translated into Korean following a multi-step pipeline:

#### 1. Initial Translation

- Used [DeepL API](https://www.deepl.com/ko/products/api) for machine translation of English items into Korean.

#### 2. Correction
Domain experts reviewed and corrected:

- Errors in the original English dataset.
- Literal and awkward translations.
- Mistranslations and idiomatic inaccuracies.
- Inconsistent tone, register, or unnatural phrasing in Korean.

#### 3. Localization
Localized examples to better fit Korean cultural and linguistic norms:
- Replaced foreign names and references with Korean equivalents (e.g., “Jessica” → “지희”).
- Adapted object and activity references to those more common in Korean daily life.     
  - Example: “toaster oven” replaced with more typical appliances like “전자레인지” (microwave).
- Adjusted sentence structures to match Korean discourse style, avoiding excessive name repetition.

#### 4. Cross-review
- An independent reviewer examined all data and corrected remaining inconsistencies or errors.


---


## Additional Information

### Citation Information

#### Our Citation Information
```
@inproceedings{
so2026constructing,
title={Constructing Korean Benchmark Suite for Reliable Evaluation of Foundation Models},
author={Yeonkyoung So and Jongmin Kim and Sungmok Jung and Gyuseong Lee and Sangho Kim and Jongyeon Park and Joonhak Lee and Seho Pyo and Gyeongje Cho and Seorin Kim and Jisoo Kim and Suyoung Park and Hyunji M. Park and Yelim Ahn and Yeongho Seo and Jaejin Lee},
booktitle={ICML 2026 Workshop on Combining Theory and Benchmarks: Towards A Virtuous Cycle to Understand and Guarantee Foundation Model Performance},
year={2026},
url={https://openreview.net/forum?id=oJ3rhISSqO}
}
```


#### Original English Dataset Citation Information

```
@article{sakaguchi2021winogrande,
  title={Winogrande: An adversarial winograd schema challenge at scale},
  author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
  journal={Communications of the ACM},
  volume={64},
  number={9},
  pages={99--106},
  year={2021},
  publisher={ACM New York, NY, USA}
}

```

### Contact Information
If you find something wrong or have a question about the dataset, contact snullm@aces.snu.ac.kr.