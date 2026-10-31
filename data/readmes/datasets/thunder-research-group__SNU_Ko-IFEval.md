---
dataset_info:
  features:
  - name: key
    dtype: int64
  - name: prompt
    dtype: string
  - name: instruction_id_list
    sequence: string
  - name: kwargs
    list:
    - name: capital_frequency
      dtype: int64
    - name: capital_relation
      dtype: string
    - name: end_phrase
      dtype: string
    - name: first_word
      dtype: string
    - name: forbidden_words
      sequence: string
    - name: frequency
      dtype: int64
    - name: keyword
      dtype: string
    - name: keyword_from
      dtype: string
    - name: keyword_to
      dtype: string
    - name: keywords
      sequence: string
    - name: language
      dtype: string
    - name: let relation
      dtype: 'null'
    - name: let_frequency
      dtype: int64
    - name: let_relation
      dtype: string
    - name: letter
      dtype: string
    - name: nth_paragraph
      dtype: int64
    - name: num_bullets
      dtype: int64
    - name: num_highlights
      dtype: int64
    - name: num_letters
      dtype: int64
    - name: num_paragraphs
      dtype: int64
    - name: num_placeholders
      dtype: int64
    - name: num_sections
      dtype: int64
    - name: num_sentences
      dtype: int64
    - name: num_words
      dtype: int64
    - name: postscript_marker
      dtype: string
    - name: prompt_to_change
      dtype: string
    - name: prompt_to_repeat
      dtype: string
    - name: relation
      dtype: string
    - name: section_spliter
      dtype: string
  splits:
  - name: test
    num_bytes: 552453
    num_examples: 841
  download_size: 167595
  dataset_size: 552453
configs:
- config_name: default
  data_files:
  - split: test
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- ko
pretty_name: Ko-IFEval
---


> Note: Evaluation code and task configurations for this benchmark are available in the [`evaluation_code`](https://github.com/mcrl/korean_benchmarks/tree/main/evaluation_code) directory of the [Korean Benchmark Suite GitHub repository](https://github.com/mcrl/korean_benchmarks). The evaluation setup is built on the Language Model Evaluation Harness and supports standardized model assessment.

# Dataset Card for Ko-IFEval

## Dataset Summary
Ko-IFEval is a Korean instruction-following benchmark designed to evaluate how well language models can follow natural language instructions in Korean. 
It adapts and localizes tasks from [IFEval](https://huggingface.co/datasets/google/IFEval), while introducing new tasks tailored for the Korean language and cultural context.

## Supported Tasks and Benchmarks
**Task**: Instruction-Following Evaluation  
Ko-IFEval is designed for evaluating instruction-tuned or chat-based language models and can be used to benchmark models on:
- constraint satisfaction,
- format control,
- prompt completion quality in Korean.

## Languages

ko (Korean)

---

## Dataset Structure

### Dataset Instance
```json
{
  "key": 1000,
  "prompt": "위키백과 페이지 \"https://ko.wikipedia.org/wiki/아이작_아시모프\"에 대한 공백 제외 300자 미만의 요약을 작성합니다. 쉼표를 사용하지 말고 섹션 제목 3개 이상을 마크다운 형식으로 강조 표시하세요(예: **섹션 제목 1**, **섹션 제목 2**, **섹션 제목 3**).",
  "instruction_id_list": [
    "punctuation:no_comma",
    "detectable_format:number_highlighted_sections",
    "length_constraints:number_letter_excluded"
  ],
  "kwargs": [
    {
      "num_highlights": null,
      "relation": null,
      "num_words": null,
      "num_placeholders": null,
      "prompt_to_repeat": null,
      "num_bullets": null,
      "section_spliter": null,
      "num_sections": null,
      "capital_relation": null,
      "capital_frequency": null,
      "keywords": null,
      "num_paragraphs": null,
      "language": null,
      "let_relation": null,
      "letter": null,
      "let_frequency": null,
      "end_phrase": null,
      "forbidden_words": null,
      "keyword": null,
      "frequency": null,
      "num_sentences": null,
      "postscript_marker": null,
      "first_word": null,
      "nth_paragraph": null,
      "prompt_to_change": null,
      "keyword_from": null,
      "keyword_to": null,
      "num_letters": null
    },
    {
      "num_highlights": 3,
      "relation": null,
      "num_words": null,
      "num_placeholders": null,
      "prompt_to_repeat": null,
      "num_bullets": null,
      "section_spliter": null,
      "num_sections": null,
      "capital_relation": null,
      "capital_frequency": null,
      "keywords": null,
      "num_paragraphs": null,
      "language": null,
      "let_relation": null,
      "letter": null,
      "let_frequency": null,
      "end_phrase": null,
      "forbidden_words": null,
      "keyword": null,
      "frequency": null,
      "num_sentences": null,
      "postscript_marker": null,
      "first_word": null,
      "nth_paragraph": null,
      "prompt_to_change": null,
      "keyword_from": null,
      "keyword_to": null,
      "num_letters": null
    },
    {
      "num_highlights": null,
      "relation": "미만",
      "num_words": null,
      "num_placeholders": null,
      "prompt_to_repeat": null,
      "num_bullets": null,
      "section_spliter": null,
      "num_sections": null,
      "capital_relation": null,
      "capital_frequency": null,
      "keywords": null,
      "num_paragraphs": null,
      "language": null,
      "let_relation": null,
      "letter": null,
      "let_frequency": null,
      "end_phrase": null,
      "forbidden_words": null,
      "keyword": null,
      "frequency": null,
      "num_sentences": null,
      "postscript_marker": null,
      "first_word": null,
      "nth_paragraph": null,
      "prompt_to_change": null,
      "keyword_from": null,
      "keyword_to": null,
      "num_letters": 300
    }
  ]
}
```

### Data Fields
- `key`: A unique ID for the prompt.
- `prompt`: Describes the task the model should perform.
- `instruction_id_list`: An array of verifiable instructions. See Table 1 of the paper for the full set with their descriptions.
- `kwargs`: An array of arguments used to specify each verifiable instruction in `instruction_id_list`.

### Data Splits
- Single evaluation set (`test` set)

---

## Dataset Creation
### Translation Process
From index 1,000 to 3,757, we translated the original IFEval (English) to Korean.

The translation and localization of instruction-following benchmarks into Korean involved four main stages:

1. **Initial Translation**     
  Used [DeepL API](https://www.deepl.com/ko/products/api) for machine translation of English instruction datasets.

2. **Correction**     
  Authors manually corrected:      
  typos and label errors in the original data,     
  literal or awkward translations,     
  inconsistent tone or formality.     

3. **Localization**      
  Localized culturally inappropriate references by:     
  replacing foreign names, places, and cultural idioms with Korean equivalents,    
  adapting measuring units and everyday scenarios to Korean norms,     
  translating culturally unfamiliar genres (e.g., limericks) into Korean styles (e.g., 5행시).    

4. **Cross-review**      
  An independent reviewer, not involved in previous steps, verified the dataset to catch and fix any remaining issues.

### Development Process
From index 10,001 to 10,300, we generated new data instances for the new instruction types.

1. **Data Collection & Preprocessing**      
  Collected Korean source material including public domain documents and presidential speeches.      
  Defined instruction categories and prompt types.

2. **Initial Data Generation**     
  Authored Korean prompts mapped to instruction types.     
  Created heuristic constraints using Korean syntax and expressions.

3. **Editing & Correction**      
  Applied consistent style and corrected ambiguities.      
  Refined prompt wording to better match task requirements.     

4. **Cross-review**     
  An independent reviewer, not involved in previous steps, verified the dataset to catch and fix any remaining issues.

### Differences from Original IFEval

Ko-IFEval is adapted from the original [IFEval](https://huggingface.co/datasets/google/IFEval) benchmark, which is designed for evaluating instruction-following capabilities in English. 
Ko-IFEval extends and localizes the benchmark for the Korean language, introducing both linguistic and functional enhancements.

#### Key Differences

| Feature                      | Original IFEval | Ko-IFEval     | Notes                                                                 |
|-----------------------------|------------------|----------------|-----------------------------------------------------------------------|
| **Language**                | English (en)     | Korean (ko)    | All prompts and constraints are written in Korean.                   |
| **Response Language Constraints**       | Various Languages     | Korean, English | Primarily targets Korean, but English can be supported if needed.   |
| **Number of Instruction Types** | 25               | 30             | 5 additional instruction types added or expanded in Korean version. |
| **Benchmark Scope**         | English models   | Korean models  | Evaluation tailored for Korean LLMs.                                 |

#### Instruction Group Changes

| Instruction Group         | Original Count | Ko-IFEval Count | Changes                                                                                         |
|---------------------------|----------------|------------------|-------------------------------------------------------------------------------------------------|
| **Keywords**              | 4              | 6                | - Separated letter frequency by language (e.g., 'letter p' vs '초성 ㄱ')<br>- Added keyword substitution check |
| **Language**              | 1              | 1                | No change                                                                                       |
| **Length Constraints**    | 4              | 6                | - Added space-inclusive / exclusive char count handling for Korean                              |
| **Detectable Content**    | 2              | 2                | No change                                                                                       |
| **Detectable Format**     | 6              | 7                | - Added multiple-choice format                                                     |
| **Combination**           | 2              | 2                | No change                                                                                       |
| **Change Cases**          | 3              | 3                | No change                                                                                       |
| **Start with / End with** | 2              | 2                | No change                                                                                       |
| **Punctuation**           | 1              | 1                | No change                                                                                       |
| **Total**                 | **25**         | **30**           | +5 total new or extended instructions                                                           |

---

## Additional Information

### Licensing Information

This dataset is licensed under the Apache License 2.0.

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


#### Original Dataset Citation Information
```
@misc{zhou2023instructionfollowingevaluationlargelanguage,
      title={Instruction-Following Evaluation for Large Language Models}, 
      author={Jeffrey Zhou and Tianjian Lu and Swaroop Mishra and Siddhartha Brahma and Sujoy Basu and Yi Luan and Denny Zhou and Le Hou},
      year={2023},
      eprint={2311.07911},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2311.07911}, 
}
```

### Contact Information
If you find something wrong or have question about the dataset, contact snullm@aces.snu.ac.kr.