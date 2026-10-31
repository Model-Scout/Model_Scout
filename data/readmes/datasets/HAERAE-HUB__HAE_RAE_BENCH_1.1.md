---
license: cc-by-nc-nd-4.0
extra_gated_prompt: To request access to the dataset, please fill out this form, and
  we'll review and let you know if your use case is approved.
extra_gated_fields:
  First Name: text
  Last Name: text
  Institution: text
  Intended Use: text
  I agree to use this dataset for non-commercial research ONLY: checkbox
task_categories:
- multiple-choice
language:
- ko
configs:
- config_name: correct_definition_matching
  data_files:
  - split: test
    path: "data/correct_definition_matching-00000-of-00001-65122a307e90d70a.parquet"
    
- config_name: csat_geo
  data_files:
  - split: test
    path: "data/csat_geo-00000-of-00001-68ce37d4952173a9.parquet"

- config_name: csat_law
  data_files:
  - split: test
    path: "data/csat_law-00000-of-00001-ef0ec0fac2f2238f.parquet"

- config_name: csat_socio
  data_files:
  - split: test
    path: "data/csat_socio-00000-of-00001-0cfadd93827d0d48.parquet"

- config_name: date_understanding
  data_files:
  - split: test
    path: "data/date_understanding-00000-of-00001-36887d05afd4c57f.parquet"

- config_name: general_knowledge
  data_files:
  - split: test
    path: "data/general_knowledge-00000-of-00001-7418d1a0b8c4a615.parquet"

- config_name: history
  data_files:
  - split: test
    path: "data/history-00000-of-00001-9ad551d475d58413.parquet"

- config_name: loan_words
  data_files:
  - split: test
    path: "data/loan_words-00000-of-00001-96ed08632b9a2ae8.parquet"

- config_name: lyrics_denoising
  data_files:
  - split: test
    path: "data/lyrics_denoising-00000-of-00001-ede1ce975e9bad54.parquet"

- config_name: proverbs_denoising
  data_files:
  - split: test
    path: "data/proverbs_denoising-00000-of-00001-f274ad136676b2e3.parquet"

- config_name: rare_words
  data_files:
  - split: test
    path: "data/rare_words-00000-of-00001-4f34314c09209524.parquet"

- config_name: standard_nomenclature
  data_files:
  - split: test
    path: "data/standard_nomenclature-00000-of-00001-52814989a6843328.parquet"

- config_name: reading_comprehension
  data_files:
  - split: test
    path: "data/reading_comprehension-00000-of-00001-f9c8df20c22e46d0.parquet"
---

The HAE_RAE_BENCH 1.1 is an ongoing project to develop a suite of evaluation tasks designed to test the 
understanding of models regarding Korean cultural and contextual nuances. 
Currently, it comprises 13 distinct tasks, with a total of 4900 instances. 

Please note that although this repository contains datasets from the original [HAE-RAE BENCH paper](https://arxiv.org/abs/2309.02706), 
the contents are not completely identical. Specifically, the reading comprehension subset from the original version has been removed due to copyright constraints. 
In its place, an updated reading comprehension subset has been introduced, sourced from the CSAT, the Korean university entrance examination. 
To replicate the studies from the paper, please see [code](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0). 


### Dataset Overview

| Task                        | Instances | Version | Explanation                                                         |
|-----------------------------|-----------|---------|---------------------------------------------------------------------|
| standard_nomenclature       | 153       | v1.0    | Multiple-choice questions about Korean standard nomenclatures from NIKL. |
| loan_word                   | 169       | v1.0    | Multiple-choice questions about Korean loan words from NIKL.             |
| rare_word                   | 405       | v1.0    | Multiple-choice questions about rare Korean words from NIKL.             |
| general_knowledge           | 176       | v1.0    | Multiple-choice questions on Korean cultural knowledge.                   |
| history                     | 188       | v1.0    | Multiple-choice questions on Korean history.                               |
| date_understanding          | 475       | v1.1    | Multiple-choice questions about understanding Korean date expressions.    |
| proverbs_denoising          | 672       | v1.1    | Questions for generating Korean proverbs.                                  |
| correct_definition_matching | 439       | v1.1    | Multiple-choice questions on matching the correct definition to words in context. |
| lyrics_denoising            | 622       | v1.1    | Questions for reconstructing Korean pop song lyrics.                       |
| reading_comprehension       | 936       | v1.1    | Multiple-choice questions on Korean reading comprehension from the CSAT.  |
| csat_law                    | 217       | v1.1    | Multiple-choice questions on Korean law from the CSAT.                     |
| csat_geo                    | 150       | v1.1    | Multiple-choice questions on Korean geography from the CSAT.               |
| csat_socio                  | 298       | v1.1    | Multiple-choice questions on Korean social studies from the CSAT.          |
| **Total**                   | **4900**  |         |                                                                     |


### Point of Contact
For any questions contact us via the following email:)
```
spthsrbwls123@yonsei.ac.kr
```