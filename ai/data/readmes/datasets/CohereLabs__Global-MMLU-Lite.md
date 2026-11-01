---
license: apache-2.0
dataset_info:
- config_name: ar
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 358182
    num_examples: 400
  - name: dev
    num_bytes: 152644.71929824562
    num_examples: 215
  download_size: 354674
  dataset_size: 510826.7192982456
- config_name: bn
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 525543
    num_examples: 400
  - name: dev
    num_bytes: 227730.26315789475
    num_examples: 215
  download_size: 418688
  dataset_size: 753273.2631578947
- config_name: cs
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 280933
    num_examples: 400
  - name: dev
    num_bytes: 149807
    num_examples: 285
  download_size: 243203
  dataset_size: 430740
- config_name: cy
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    sequence:
      sequence: string
  - name: time_sensitive
    sequence:
      sequence: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 284119
    num_examples: 400
  download_size: 133937
  dataset_size: 284119
- config_name: de
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 305874
    num_examples: 400
  - name: dev
    num_bytes: 122516.80701754386
    num_examples: 215
  download_size: 333963
  dataset_size: 428390.8070175439
- config_name: en
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 276018
    num_examples: 400
  - name: dev
    num_bytes: 110414.94736842105
    num_examples: 215
  download_size: 3859642
  dataset_size: 386432.94736842107
- config_name: es
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 297781
    num_examples: 400
  - name: dev
    num_bytes: 121179.28070175438
    num_examples: 215
  download_size: 321495
  dataset_size: 418960.2807017544
- config_name: fr
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 309684
    num_examples: 400
  - name: dev
    num_bytes: 125358.57894736843
    num_examples: 215
  download_size: 334213
  dataset_size: 435042.5789473684
- config_name: hi
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 517298
    num_examples: 400
  - name: dev
    num_bytes: 232542.49122807017
    num_examples: 215
  download_size: 419478
  dataset_size: 749840.4912280701
- config_name: hu
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 326701
    num_examples: 400
  - name: dev
    num_bytes: 148646
    num_examples: 215
  download_size: 243509
  dataset_size: 475347
- config_name: id
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 284643
    num_examples: 400
  - name: dev
    num_bytes: 116697.47368421052
    num_examples: 215
  download_size: 295406
  dataset_size: 401340.4736842105
- config_name: it
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 299592
    num_examples: 400
  - name: dev
    num_bytes: 118851.24561403508
    num_examples: 215
  download_size: 323136
  dataset_size: 418443.24561403506
- config_name: ja
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 310809
    num_examples: 400
  - name: dev
    num_bytes: 126469.78947368421
    num_examples: 215
  download_size: 328229
  dataset_size: 437278.7894736842
- config_name: ko
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 296040
    num_examples: 400
  - name: dev
    num_bytes: 121133.26315789473
    num_examples: 215
  download_size: 315097
  dataset_size: 417173.2631578947
- config_name: my
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: dev
    num_bytes: 304707
    num_examples: 215
  - name: test
    num_bytes: 640084
    num_examples: 400
  download_size: 327446
  dataset_size: 944791
- config_name: or
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 536750
    num_examples: 400
  - name: dev
    num_bytes: 262717
    num_examples: 215
  download_size: 293590
  dataset_size: 799467
- config_name: pt
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 290379
    num_examples: 400
  - name: dev
    num_bytes: 116622.0350877193
    num_examples: 215
  download_size: 316118
  dataset_size: 407001.0350877193
- config_name: sk
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 309511
    num_examples: 400
  - name: dev
    num_bytes: 137026
    num_examples: 215
  download_size: 236120
  dataset_size: 446537
- config_name: sq
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 298648
    num_examples: 400
  - name: dev
    num_bytes: 132894
    num_examples: 215
  download_size: 225031
  dataset_size: 431542
- config_name: sw
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 280600
    num_examples: 400
  - name: dev
    num_bytes: 110946.78947368421
    num_examples: 215
  download_size: 291944
  dataset_size: 391546.7894736842
- config_name: tg
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 415701
    num_examples: 400
  - name: dev
    num_bytes: 200629
    num_examples: 215
  download_size: 287992
  dataset_size: 616330
- config_name: yo
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 344120
    num_examples: 400
  - name: dev
    num_bytes: 116032.1052631579
    num_examples: 215
  download_size: 315742
  dataset_size: 460152.10526315786
- config_name: zh
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: string
  - name: required_knowledge
    dtype: string
  - name: time_sensitive
    dtype: string
  - name: reference
    dtype: string
  - name: culture
    dtype: string
  - name: region
    dtype: string
  - name: country
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
  - name: is_annotated
    dtype: bool
  splits:
  - name: test
    num_bytes: 254371
    num_examples: 400
  - name: dev
    num_bytes: 96242.29824561403
    num_examples: 215
  download_size: 283239
  dataset_size: 350613.29824561405
configs:
- config_name: ar
  data_files:
  - split: test
    path: ar/test-*
  - split: dev
    path: ar/dev-*
- config_name: bn
  data_files:
  - split: test
    path: bn/test-*
  - split: dev
    path: bn/dev-*
- config_name: cs
  data_files:
  - split: test
    path: cs/test-*
  - split: dev
    path: cs/dev-*
- config_name: cy
  data_files:
  - split: test
    path: cy/test-*
- config_name: de
  data_files:
  - split: test
    path: de/test-*
  - split: dev
    path: de/dev-*
- config_name: en
  data_files:
  - split: test
    path: en/test-*
  - split: dev
    path: en/dev-*
- config_name: es
  data_files:
  - split: test
    path: es/test-*
  - split: dev
    path: es/dev-*
- config_name: fr
  data_files:
  - split: test
    path: fr/test-*
  - split: dev
    path: fr/dev-*
- config_name: hi
  data_files:
  - split: test
    path: hi/test-*
  - split: dev
    path: hi/dev-*
- config_name: hu
  data_files:
  - split: test
    path: hu/test-*
  - split: dev
    path: hu/dev-*
- config_name: id
  data_files:
  - split: test
    path: id/test-*
  - split: dev
    path: id/dev-*
- config_name: it
  data_files:
  - split: test
    path: it/test-*
  - split: dev
    path: it/dev-*
- config_name: ja
  data_files:
  - split: test
    path: ja/test-*
  - split: dev
    path: ja/dev-*
- config_name: ko
  data_files:
  - split: test
    path: ko/test-*
  - split: dev
    path: ko/dev-*
- config_name: my
  data_files:
  - split: dev
    path: my/dev-*
  - split: test
    path: my/test-*
- config_name: or
  data_files:
  - split: test
    path: or/test-*
  - split: dev
    path: or/dev-*
- config_name: pt
  data_files:
  - split: test
    path: pt/test-*
  - split: dev
    path: pt/dev-*
- config_name: sk
  data_files:
  - split: test
    path: sk/test-*
  - split: dev
    path: sk/dev-*
- config_name: sq
  data_files:
  - split: test
    path: sq/test-*
  - split: dev
    path: sq/dev-*
- config_name: sw
  data_files:
  - split: test
    path: sw/test-*
  - split: dev
    path: sw/dev-*
- config_name: tg
  data_files:
  - split: test
    path: tg/test-*
  - split: dev
    path: tg/dev-*
- config_name: yo
  data_files:
  - split: test
    path: yo/test-*
  - split: dev
    path: yo/dev-*
- config_name: zh
  data_files:
  - split: test
    path: zh/test-*
  - split: dev
    path: zh/dev-*
tags:
- argilla
language:
- ar
- bn
- cs
- cy
- en
- es
- fr
- hi
- hu
- de
- id
- it
- ja
- ko
- my
- or
- pt
- yo
- sk
- sq
- sw
- tg
- zh
---


![GlobalMMLU Lite 3.0](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite/resolve/main/gmmlulite3.jpeg)

# Releases:
- Version 3.0 (May 2026): GMMLU Lite 3.0 release with 5 new languages: Czech, Hungarian, Italian (updated), Oriya, Slovak and Tajik
- Version 2.0 (Dec 2025): GMMLU Lite 2.0 release with 3 new languages: Albanian, Burmese and Welsh
- Version 1.0 (Dec 2024): GMMLU Lite initial release with 15 languages. 

![GlobalMMLU Header](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite/resolve/main/language_coverage.png)

# Dataset Summary
Global-MMLU-Lite is a multilingual evaluation set spanning 23 languages, including English. It is "lite" version of the original [Global-MMLU dataset](https://cohere.com/research/globalmmlu) 🌍.
It includes 200 Culturally Sensitive (CS) and 200 Culturally Agnostic (CA) samples per language. All samples in Global MMLU lite are fully human translated or post edited. 

**NOTE:** Of the 23 languages presently included in Global-MMLU-Lite, 15 are taken from [Global-MMLU dataset](https://huggingface.co/datasets/CohereLabs/Global-MMLU) whereas Albanian, Burmese, Welsh have been contributed by external collaborators or members of Cohere Labs Open Science Community.
The evaluation results reported in our [paper](https://arxiv.org/abs/2412.03304) are corresponding to the 15 languages originally released as part of Global-MMLU-Lite.

- **Curated by:** Professional annotators and contributors of [Cohere Labs Community](https://cohere.com/research)
- **Language(s):** 23 languages
- **License:** [Apache 2.0](https://opensource.org/license/apache-2-0)

### **Global-MMLU Dataset Family:**

  | Name | Explanation |
  |------|--------------|
  | [Global-MMLU](https://huggingface.co/datasets/CohereLabs/Global-MMLU) | Full Global-MMLU set with translations for all 14K samples including CS and CA subsets|
  | [Global-MMLU-Lite](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) | Lite version of Global-MMLU with human translated samples in 23 languages and containing 200 samples each for CS and CA subsets per language.|

  

## Load with Datasets
To load this dataset with `datasets`, you'll first need to install it using `pip install datasets` and then use the following code:

```python
from datasets import load_dataset

# load HF dataset
gmmlu_lite = load_dataset("CohereLabs/Global-MMLU-Lite", 'en')

# can also be used as pandas dataframe
gmmlu_lite.set_format("pandas")
gmmlu_lite_test = gmmlu_lite['test'][:]
gmmlu_lite_dev = gmmlu_lite['dev'][:]
```

<details>
<summary> additional details </summary>

The columns corresponding to annotations collected from our cultural bias study (i.e. 'required_knowledge', 'time_sensitive', 'reference', 'culture', 'region', 'country') contain a list of values representing annotations from different annotators.
However, to avoid conversion issues to HF dataset, these columns are provided as string in the final dataset.
You can convert these columns back to list of values for easier manipulation as follows:
```python
import ast

# convert string values to list
gmmlu_lite_test['required_knowledge'] = gmmlu_lite_test['required_knowledge'].apply(lamda x: ast.literal_eval(x))
```
</details>
<br>


## Data Fields

The data fields are the same among all splits. Brief description of each field is provided below.

<details>
<summary> data field description </summary>
  
- `sample_id`: A unique identifier for the question.
- `subject`: The main topic the question falls under.
- `subject_category`: The high-level category the subject falls under i.e. STEM/Humanities/Social Sciences/Medical/Business/Other.
- `question`: translated question from MMLU
- `option_a`: one of the possible option choices 
- `option_b`: one of the possible option choices 
- `option_c`: one of the possible option choices 
- `option_d`: one of the possible option choices 
- `answer': the correct answer (A/B/C/D)
- `required_knowledge`: annotator votes for knowledge needed to answer the question correctly. Possible values include: "cultural", "regional", "dialect" or "none"
- `time_sensitive`: annotator votes indicating if the question's answer is time-dependent. Possible values include: Yes/No
- `reference`: annotations for which part of the question contains cultural/regional/dialect references. The different items in the list are annotations from different annotators.
- `culture`: annotations for which culture does the question belong to. The different items in the list correspond to annotations from different annotators.
- `region`: Geographic region the question is relevant to. Each item in the list correspond to annotations from different annotators.
- `country`: Specific country the question pertains to. Each item in the list correspond to annotations from different annotators.
- `cultural_sensitivity_label`: Label to indicate if question is culturally sensitive (CS) or culturally agnostic (CA) based on annotator votes.
- `is_annotated`: True/False flag to indicate if sample contains any annotations from our cultural bias study.
  
</details>
<br>

## Data Splits
The following are the splits of the data:
| Split | No. of instances | Language Coverage |
|-------|------------------|-------------------|
| test | 9,200 | 23 |
| dev  | 4,655| 22 |


## Data Instances

An example from `test` set looks as follows:
```json
{'sample_id': 'astronomy/test/58',
 'subject': 'astronomy',
 'subject_category': 'STEM',
 'question': 'When traveling north from the United States into Canada you’ll see the North Star (Polaris) getting _________.',
 'option_a': 'Brighter',
 'option_b': 'Dimmer',
 'option_c': 'Higher in the sky',
 'option_d': 'Lower in the sky',
 'answer': 'C',
 'required_knowledge': "['regional', 'regional', 'regional', 'regional']",
 'time_sensitive': "['No', 'No', 'No', 'No']",
 'reference': "[{'end': 55, 'label': 'Geographic', 'score': None, 'start': 5}, {'end': 43, 'label': 'Geographic', 'score': None, 'start': 30}, {'end': 55, 'label': 'Geographic', 'score': None, 'start': 5}, {'end': 43, 'label': 'Geographic', 'score': None, 'start': 30}]",
 'culture': '[]',
 'region': "['North America', 'North America', 'North America', 'North America']",
 'country': "['United States of America (USA)', 'United States of America (USA)', 'United States of America (USA)', 'United States of America (USA)']",
 'cultural_sensitivity_label': 'CS',
 'is_annotated': True
}
```

## Statistics
### Annotation Types
The following is the breakdown of CS🗽, CA⚖️ and MA📝 samples in the final dataset.

| Type of Annotation | Instances per language | No. of languages | Total instances
|--------------------|------------------------|------------------|----------------|
| Culturally Sensitive 🗽 | 200 | 23 | 4,600 |
| Culturally Agnostic ⚖️ | 200 |23 | 4,600 |
| MMLU Annotated 📝| 400 | 23 | 9,200 |

### Languages
The dataset covers 23 languages. The following is details about the languages included in the dataset.

<details>
<summary> Languages Info </summary>

| ISO Code | Language | Resources | 
|----------|----------|-----------|
| `ar` | Arabic (Standard)| High |
| `bn` | Bengali | Mid |
| `cs` | Czech | Mid |
| `cy` | Welsh | Low |
| `de` | German | High |
| `en` | English | High |
| `fr` | French | High |
| `hi` | Hindi | High |
| `hu` | Hungarian | Mid |
| `id` | Indonesian | Mid |
| `it` | Italian | High |
| `ja` | Japanese | High |
| `ko` | Korean | Mid |
| `my` | Burmese | Low |
| `or` | Oriya | Low |
| `pt` | Portuguese | High |
| `es` | Spanish | High |
| `sk` | Slovak | Mid |
| `sq` | Albanian | Low |
| `sw` | Swahili | Low |
| `tg` | Tajik | Low |
| `yo` | Yorùbá | Low |
| `zh` | Chinese (Simplified) | High |
</details>
<br>

# Known Limitations
A brief overview of limitations of this dataset is provided below.
<details>
<summary> show limitations </summary>
  
- **Language and dialect coverage:** Global-MMLU focusses on 42 languages. However, this is still only a tiny fraction of the world’s linguistic diversity. Future work is needed to continue to improve evaluations beyond these 42 languages and take into account how technology serves different dialects.
- **Uneven distribution of contributions:** The dataset contains translation post-edits from community volunteers, with a 'long tail' of volunteers making only one or two contributions. Similarly, there is a huge gap between languages with the highest number of contributions and ones with the lowest number of contributions. 
- **Toxic or offensive speech:** Our annotation process did not focus on flagging for toxic,harmful, or offensive speech, so it is possible that Global-MMLU contains some data that could be considered harmful. We believe this is of relatively low risk because of the nature of the original MMLU and the focus on examination material.
- **Region Category Assignment:** For the annotation of geographically sensitive questions, we classified regions into six geographic regions (Africa, Asia, Europe, North America, Oceania,and South America). However, based upon discussions we would going forward recommend switching to the taxonomy proposed by the World Bank which is more granular and includes separate designations for Central America and Sub-Saharan Africa.
- **Identifying cultural sensitivity does not guarantee cultural inclusion:** While Global-MMLU highlights important limitations in current datasets by identifying gaps in non-Western cultural representation. Future work must prioritize the integration of diverse culturally grounded knowledge to achieve true inclusivity and fairness in multilingual AI evaluation.

</details>
<br>

# Additional Information

## Provenance
- **Methods Used:** Professional annotations as well as crowd-sourced through volunteer annotations.
- **Methodology Details:** We collected cultural bias annotations as well as post-edits of translations for different mmlu questions.
    - [Cultural Sensitivity Annotation Platform](https://huggingface.co/spaces/CohereLabs/MMLU-evaluation)
    - [Translation Quality Annotation Platform](https://huggingface.co/spaces/CohereLabs/review-mmlu-translations)
    - Dates of Collection: May 2024 - Aug 2024


## Dataset Version and Maintenance
- **Maintenance Status:** Actively Maintained
- **Version Details:**
    - *Current version:* 3.0
    - *Last Update:* 05/2026
    - *First Release:* 12/2024


## Authorship
- **Publishing Organization:** [Cohere Labs](https://cohere.com/research)
- **Industry Type:** Not-for-profit - Tech

## Licensing Information
This dataset can be used for any purpose, under the terms of the [Apache 2.0](https://opensource.org/license/apache-2-0) License.

## Continuous Improvement:
If you want to contribute to improving the quality of translations in Global-MMLU-Lite then please contribute using our [annotation UI](https://huggingface.co/spaces/CohereLabs/review-global-mmlu-lite).
You can also help review and edit machine translations in additional languages using our annotation interface to help improve language coverage of Global-MMLU-Lite.

## Additional Details
For any additional details, please check our paper, [Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation](https://arxiv.org/abs/2412.03304).


## Citation Information
```bibtex
@misc{singh2024globalmmluunderstandingaddressing,
      title={Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation}, 
      author={Shivalika Singh and Angelika Romanou and Clémentine Fourrier and David I. Adelani and Jian Gang Ngui and Daniel Vila-Suero and Peerat Limkonchotiwat and Kelly Marchisio and Wei Qi Leong and Yosephine Susanto and Raymond Ng and Shayne Longpre and Wei-Yin Ko and Madeline Smith and Antoine Bosselut and Alice Oh and Andre F. T. Martins and Leshem Choshen and Daphne Ippolito and Enzo Ferrante and Marzieh Fadaee and Beyza Ermis and Sara Hooker},
      year={2024},
      eprint={2412.03304},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.03304}, 
}
```