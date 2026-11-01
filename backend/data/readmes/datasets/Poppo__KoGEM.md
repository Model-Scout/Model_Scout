---
license: cc-by-4.0
task_categories:
- question-answering
- zero-shot-classification
language:
- ko
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: idx
    dtype: int32
  - name: data_src
    dtype: string
  - name: num_id
    dtype: string
  - name: level_1
    dtype: string
  - name: level_2
    dtype: string
  - name: passage
    dtype: string
  - name: question
    sequence: string
  - name: paragraph
    dtype: string
  - name: choices
    sequence:
      dtype: string
  - name: label
    dtype: int32
  download_size: 2091539
  dataset_size: 2091539
  num_examples: 1524
configs:
- config_name: benchmark
  data_files:
  - split: test
    path: dataset/KoGEM_benchmark.parquet
tags:
- grammar
- linguistic_competence
---


# Dataset Card for KoGEM


## Dataset Description
- **Repository:** https://github.com/SungHo3268/KoGEM
- **Paper:** [https://aclanthology.org/2025.acl-long.492/] https://aclanthology.org/2025.acl-long.492/


### Dataset Summary
> KoGEM is a benchmark designed to assess Korean linguistic competence in both large language models (LLMs) and humans through 1.5k multiple-choice questions covering five main linguistic categories with 16 subcategories. Refer to the [not yet](not yet) for more details.

<img src="./kogem_texanomy_distributions.png" alt="example" width="50%" />

## Usage
```python
# pip install -q datasets
from datasets import load_dataset
dataset = load_dataset("Poppo/KoGEM")["test"]
```

### Data Instances
An example looks as follows:
```json
{
    "idx": 0,
    "data_src": "NUAT(HS1)",
    "num_id": "2007-03-11",
    "level_1": "Semantics",
    "level_2": "Lexical Semantics",
    "passage": "",
    "question": "밀줄 친 표현 중, 문맥상 비슷한 의미를 가진 쌍으로 보기 어려운 것은?",
    "paragraph": "",
    "choices": [
      "1. <u>기가 차서</u> 할 말을 잃었다. <u>기가 막혀</u> 할 말을 잃었다.",
      "2. <u>마음에 드는</u> 사람은 흔하지 않다. <u>마음에 차는</u> 사람은 흔하지 않다.",
      "3. 철수는 아직도 <u>철이 들지</u> 않았다. 철수는 아직도 <u>철이 나지</u> 않았다.",
      "4. 고향 마을은 여전히 내 <u>눈에 익었다</u>. 고향 마을은 여전히 내 <u>눈에 남았다</u>.",
      "5. 자식이 하는 <u>일이 안되기를</u> 바라는 부모는 없다. 자식이 하는 <u>일이 못되기를</u> 바라는 부모는 없다."
    ],
    "label": 4
},
```


### Data Fields

The data fields are:
- `idx`: A unique identifier for each data entry
- `data_src`: The exam that serves as the data source
  - CSAT (College Scholastic Ability Test)
  - NUAT (National United Achievement Test) for high school grades 1, 2, and 3
  - HSQE (High School Qualification Exam)
  - CSE (Civil Service Exam) for levels 7th and 9th 
- `num_id`: Detailed information about the data source, including the date and type of exam
- `level_1`: The primary linguistic category
  - Phonology
  - Morphology
  - Syntax
  - Semantics
  - Norm
- `level_2` A subcategory of 'level_1'
  - Phonological System
  - Phonological Alternation
  - Part-of-Speech
  - Morpheme
  - Word Formation
  - Sentence Structure
  - Syntactic Features
  - Vocabulary
  - Lexical Semantics
  - Pragmatics
  - Orthography
  - Standard Language
  - Standard Pronunciation
  - Romanization
  - Loanword Orthography
  - Cross-Category
- `passage`: Context necessary for understanding the question (optional)
- `question`: A single-sentence question
- `paragraph`: Brief explanations or examples of grammatical concepts relevant to answering the question (optional)
- `choices`: A set of answer options, containing either four or five choices depending on the exam type
- `label`: The correct answer (ground truth)


## Citation Information
If you use KoGEM in your research, please cite our work:
```bibtex
@inproceedings{kim-etal-2025-polishing,
    title = "Polishing Every Facet of the {GEM}: Testing Linguistic Competence of {LLM}s and Humans in {K}orean",
    author = "Kim, SungHo  and
      Kim, Nayeon  and
      Jeon, Taehee  and
      Lee, SangKeun",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.492/",
    doi = "10.18653/v1/2025.acl-long.492",
    pages = "9955--9984",
    ISBN = "979-8-89176-251-0",
    abstract = "We introduce the $\underline{Ko}rean \underline{G}rammar \underline{E}valuation Bench\underline{M}ark (KoGEM)$, designed to assess the linguistic competence of LLMs and humans in Korean. KoGEM consists of 1.5k multiple-choice QA pairs covering five main categories and 16 subcategories. The zero-shot evaluation of 27 LLMs of various sizes and types reveals that while LLMs perform remarkably well on straightforward tasks requiring primarily definitional knowledge, they struggle with tasks that demand the integration of real-world experiential knowledge, such as phonological rules and pronunciation. Furthermore, our in-depth analysis suggests that incorporating such experiential knowledge could enhance the linguistic competence of LLMs. With KoGEM, we not only highlight the limitations of current LLMs in linguistic competence but also uncover hidden facets of LLMs in linguistic competence, paving the way for enhancing comprehensive language understanding. Our code and dataset are available at: https://github.com/SungHo3268/KoGEM."
}
```

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

This work is used according to [Korea Open Government License (KOGL) Type 1](https://www.kogl.or.kr/info/license.do). <br/>

[![KOGL TYPE 1][kogl-1-shield]][kogl-1]

[kogl-1]: https://www.kogl.or.kr/info/license.do
[kogl-1-shield]: https://www.kogl.or.kr/static/kogl/img/sub/number1.jpg