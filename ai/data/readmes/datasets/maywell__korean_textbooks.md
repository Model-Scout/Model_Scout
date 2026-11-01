---
language:
- ko
license: apache-2.0
size_categories:
- 1M<n<10M
pretty_name: 대규모 한국어 Synthetic 데이터
dataset_info:
- config_name: claude_evol
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 992896186
    num_examples: 239102
  download_size: 380188122
  dataset_size: 992896186
- config_name: code-alpaca
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 273836723
    num_examples: 64112
  download_size: 100817441
  dataset_size: 273836723
- config_name: helpsteer
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 101753037
    num_examples: 25253
  download_size: 38660919
  dataset_size: 101753037
- config_name: ko_wikidata
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 527306289
    num_examples: 127614
  download_size: 197029339
  dataset_size: 527306289
- config_name: mmlu_abstract_algebra
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 369008992
    num_examples: 88848
  download_size: 135822870
  dataset_size: 369008992
- config_name: mmlu_all
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 406126621
    num_examples: 97765
  download_size: 149486712
  dataset_size: 406126621
- config_name: mmlu_anatomy
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 404317465
    num_examples: 97463
  download_size: 148806011
  dataset_size: 404317465
- config_name: mmlu_astronomy
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 404137638
    num_examples: 97347
  download_size: 148705490
  dataset_size: 404137638
- config_name: mmlu_business_ethics
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 404250245
    num_examples: 97327
  download_size: 148763276
  dataset_size: 404250245
- config_name: mmlu_clinical_knowledge
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 403659005
    num_examples: 97226
  download_size: 148688069
  dataset_size: 403659005
- config_name: mmlu_college_biology
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 404028634
    num_examples: 97285
  download_size: 148722802
  dataset_size: 404028634
- config_name: mmlu_college_chemistry
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 404667385
    num_examples: 97435
  download_size: 148855223
  dataset_size: 404667385
- config_name: mmlu_college_computer_science
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 385176880
    num_examples: 92606
  download_size: 141868873
  dataset_size: 385176880
- config_name: mmlu_college_mathematics
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 390603751
    num_examples: 94070
  download_size: 143833823
  dataset_size: 390603751
- config_name: mmlu_college_medicine
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 395144479
    num_examples: 95156
  download_size: 145271248
  dataset_size: 395144479
- config_name: mmlu_college_physics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 404906114
    num_examples: 97452
  download_size: 148870088
  dataset_size: 404906114
- config_name: mmlu_computer_security
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 403699674
    num_examples: 97212
  download_size: 148755211
  dataset_size: 403699674
- config_name: mmlu_conceptual_physics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 366231421
    num_examples: 88216
  download_size: 134989933
  dataset_size: 366231421
- config_name: mmlu_econometrics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 380851762
    num_examples: 91854
  download_size: 140295665
  dataset_size: 380851762
- config_name: mmlu_electrical_engineering
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 364564129
    num_examples: 87826
  download_size: 134376902
  dataset_size: 364564129
- config_name: mmlu_elementary_mathematics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 371101672
    num_examples: 89307
  download_size: 136622044
  dataset_size: 371101672
- config_name: mmlu_formal_logic
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 395937096
    num_examples: 95483
  download_size: 145736493
  dataset_size: 395937096
- config_name: mmlu_global_facts
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 394596084
    num_examples: 94984
  download_size: 145284966
  dataset_size: 394596084
- config_name: mmlu_high_school_biology
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 402382699
    num_examples: 97117
  download_size: 148038235
  dataset_size: 402382699
- config_name: mmlu_high_school_chemistry
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 402886667
    num_examples: 96907
  download_size: 148323317
  dataset_size: 402886667
- config_name: mmlu_high_school_computer_science
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 403966380
    num_examples: 97351
  download_size: 148666121
  dataset_size: 403966380
- config_name: mmlu_high_school_european_history
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 403671884
    num_examples: 97222
  download_size: 148454177
  dataset_size: 403671884
- config_name: mmlu_high_school_geography
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 404040602
    num_examples: 97261
  download_size: 148657890
  dataset_size: 404040602
- config_name: mmlu_high_school_government_and_politics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 403990139
    num_examples: 97311
  download_size: 148568388
  dataset_size: 403990139
- config_name: mmlu_high_school_macroeconomics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 404170166
    num_examples: 97400
  download_size: 148591243
  dataset_size: 404170166
- config_name: mmlu_high_school_mathematics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 404846407
    num_examples: 97396
  download_size: 149076619
  dataset_size: 404846407
- config_name: mmlu_high_school_microeconomics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 404613760
    num_examples: 97435
  download_size: 148970422
  dataset_size: 404613760
- config_name: mmlu_high_school_physics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 397678253
    num_examples: 95740
  download_size: 146340167
  dataset_size: 397678253
- config_name: mmlu_high_school_psychology
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 334767526
    num_examples: 80626
  download_size: 123054403
  dataset_size: 334767526
- config_name: mmlu_high_school_statistics
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 315209112
    num_examples: 76033
  download_size: 115876698
  dataset_size: 315209112
- config_name: mmlu_high_school_us_history
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 329179309
    num_examples: 79322
  download_size: 120972668
  dataset_size: 329179309
- config_name: mmlu_high_school_world_history
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 357910528
    num_examples: 85990
  download_size: 131809165
  dataset_size: 357910528
- config_name: mmlu_human_aging
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 325427761
    num_examples: 78341
  download_size: 119430234
  dataset_size: 325427761
- config_name: mmlu_human_sexuality
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 328912659
    num_examples: 79327
  download_size: 121032722
  dataset_size: 328912659
- config_name: mmlu_international_law
  features:
  - name: '0'
    dtype: string
  splits:
  - name: train
    num_bytes: 327874597
    num_examples: 78989
  download_size: 120785769
  dataset_size: 327874597
- config_name: normal_instructions
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 956305865
    num_examples: 240523
  download_size: 362796244
  dataset_size: 956305865
- config_name: tiny-textbooks
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1722063576
    num_examples: 395985
  download_size: 635724860
  dataset_size: 1722063576
configs:
- config_name: claude_evol
  data_files:
  - split: train
    path: claude_evol/train-*
- config_name: code-alpaca
  data_files:
  - split: train
    path: code-alpaca/train-*
- config_name: helpsteer
  data_files:
  - split: train
    path: helpsteer/train-*
- config_name: ko_wikidata
  data_files:
  - split: train
    path: ko_wikidata/train-*
- config_name: mmlu_abstract_algebra
  data_files:
  - split: train
    path: mmlu_abstract_algebra/train-*
- config_name: mmlu_all
  data_files:
  - split: train
    path: mmlu_all/train-*
- config_name: mmlu_anatomy
  data_files:
  - split: train
    path: mmlu_anatomy/train-*
- config_name: mmlu_astronomy
  data_files:
  - split: train
    path: mmlu_astronomy/train-*
- config_name: mmlu_business_ethics
  data_files:
  - split: train
    path: mmlu_business_ethics/train-*
- config_name: mmlu_clinical_knowledge
  data_files:
  - split: train
    path: mmlu_clinical_knowledge/train-*
- config_name: mmlu_college_biology
  data_files:
  - split: train
    path: mmlu_college_biology/train-*
- config_name: mmlu_college_chemistry
  data_files:
  - split: train
    path: mmlu_college_chemistry/train-*
- config_name: mmlu_college_computer_science
  data_files:
  - split: train
    path: mmlu_college_computer_science/train-*
- config_name: mmlu_college_mathematics
  data_files:
  - split: train
    path: mmlu_college_mathematics/train-*
- config_name: mmlu_college_medicine
  data_files:
  - split: train
    path: mmlu_college_medicine/train-*
- config_name: mmlu_college_physics
  data_files:
  - split: train
    path: mmlu_college_physics/train-*
- config_name: mmlu_computer_security
  data_files:
  - split: train
    path: mmlu_computer_security/train-*
- config_name: mmlu_conceptual_physics
  data_files:
  - split: train
    path: mmlu_conceptual_physics/train-*
- config_name: mmlu_econometrics
  data_files:
  - split: train
    path: mmlu_econometrics/train-*
- config_name: mmlu_electrical_engineering
  data_files:
  - split: train
    path: mmlu_electrical_engineering/train-*
- config_name: mmlu_elementary_mathematics
  data_files:
  - split: train
    path: mmlu_elementary_mathematics/train-*
- config_name: mmlu_formal_logic
  data_files:
  - split: train
    path: mmlu_formal_logic/train-*
- config_name: mmlu_global_facts
  data_files:
  - split: train
    path: mmlu_global_facts/train-*
- config_name: mmlu_high_school_biology
  data_files:
  - split: train
    path: mmlu_high_school_biology/train-*
- config_name: mmlu_high_school_chemistry
  data_files:
  - split: train
    path: mmlu_high_school_chemistry/train-*
- config_name: mmlu_high_school_computer_science
  data_files:
  - split: train
    path: mmlu_high_school_computer_science/train-*
- config_name: mmlu_high_school_european_history
  data_files:
  - split: train
    path: mmlu_high_school_european_history/train-*
- config_name: mmlu_high_school_geography
  data_files:
  - split: train
    path: mmlu_high_school_geography/train-*
- config_name: mmlu_high_school_government_and_politics
  data_files:
  - split: train
    path: mmlu_high_school_government_and_politics/train-*
- config_name: mmlu_high_school_macroeconomics
  data_files:
  - split: train
    path: mmlu_high_school_macroeconomics/train-*
- config_name: mmlu_high_school_mathematics
  data_files:
  - split: train
    path: mmlu_high_school_mathematics/train-*
- config_name: mmlu_high_school_microeconomics
  data_files:
  - split: train
    path: mmlu_high_school_microeconomics/train-*
- config_name: mmlu_high_school_physics
  data_files:
  - split: train
    path: mmlu_high_school_physics/train-*
- config_name: mmlu_high_school_psychology
  data_files:
  - split: train
    path: mmlu_high_school_psychology/train-*
- config_name: mmlu_high_school_statistics
  data_files:
  - split: train
    path: mmlu_high_school_statistics/train-*
- config_name: mmlu_high_school_us_history
  data_files:
  - split: train
    path: mmlu_high_school_us_history/train-*
- config_name: mmlu_high_school_world_history
  data_files:
  - split: train
    path: mmlu_high_school_world_history/train-*
- config_name: mmlu_human_aging
  data_files:
  - split: train
    path: mmlu_human_aging/train-*
- config_name: mmlu_human_sexuality
  data_files:
  - split: train
    path: mmlu_human_sexuality/train-*
- config_name: mmlu_international_law
  data_files:
  - split: train
    path: mmlu_international_law/train-*
- config_name: normal_instructions
  data_files:
  - split: train
    path: normal_instructions/train-*
- config_name: tiny-textbooks
  data_files:
  - split: train
    path: tiny-textbooks/train-*
---

# Massive Korean synthetic dataset

This dataset is a large-scale Korean artificial data set created using Gemini Pro.
It was created using the methodology described in *Creation of synthetic textbook-quality datasets* in [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644).

## Data overview

**A subset of each dataset does not indicate the contents of that dataset.**

**Further modification required before use this dataset for training.**

**본 데이터셋은 바로 사용하기보다는 하고자하는 task에 맞추어 가공 후 사용을 권장드립니다. ex) 로컬 모델을 사용하여 QA 셋으로 변환**

| subset | row count | link | + |
|---|---|---|---|
| tiny-textbooks | 395,985 | [nampdn-ai/tiny-textbooks](https://huggingface.co/datasets/nampdn-ai/tiny-textbooks) | |
| ko_wikidata | 127,614 | [maywell/ko_wikidata_QA](https://huggingface.co/datasets/maywell/ko_wikidata_QA) | |
| normal_instructions | 240,523 | [KonstantyM/science_qa](https://huggingface.co/datasets/KonstantyM/science_qa) | with science texts |
| claude_evol | 239,102 | [Norquinal/claude_evol_instruct_210k](https://huggingface.co/datasets/Norquinal/claude_evol_instruct_210k) | used 250k files from that repo |
| code-alpaca | 64,112 | [theblackcat102/evol-codealpaca-v1](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1) | original is a coding dataset, but generated data is not mainly a coding dataset |
| helpsteer | 25,253 | [nvidia/HelpSteer](https://huggingface.co/datasets/nvidia/HelpSteer) | |
| mmlu_abstract_algebra | 88,848 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_all | 97,765 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_anatomy | 97,463 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_astronomy | 97,347 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_business_ethics | 97,327 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_clinical_knowledge | 97,226 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_biology | 97,285 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_chemistry | 97,435 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_computer_science | 92,606 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_mathematics | 94,070 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_medicine | 95,156 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_college_physics | 97,452 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_computer_security | 97,212 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_conceptual_physics | 88,216 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_econometrics | 91,854 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_electrical_engineering | 87,826 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_elementary_mathematics | 89,307 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_formal_logic | 95,483 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_global_facts | 94,984 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_biology | 97,117 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_chemistry | 96,907 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_computer_science | 97,351 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_european_history | 97,222 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_geography | 97,261 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_government_and_politics | 97,311 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_macroeconomics | 97,400 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_mathematics | 97,396 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_microeconomics | 97,435 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_physics | 95,740 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_psychology | 80,626 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_statistics | 76,033 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_us_history | 79,322 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_high_school_world_history | 85,990 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_human_aging | 78,341 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_human_sexuality | 79,327 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |
| mmlu_international_law | 78,989 | [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) | |

## When you find a problem

If you find any issues with the dataset, please let us know in the discussion or send us a pull request.