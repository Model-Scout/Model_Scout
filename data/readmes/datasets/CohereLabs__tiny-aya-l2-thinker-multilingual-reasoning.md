---
language:
- am
- ar
- bg
- bn
- ca
- cs
- de
- el
- eu
- fa
- fi
- fil
- fr
- ga
- ha
- he
- hi
- hu
- id
- ig
- it
- ja
- jv
- km
- ko
- lt
- ms
- mt
- no
- pa
- pl
- ru
- sk
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- yo
- zh
- zu
license: cc-by-nc-4.0
pretty_name: Tiny Aya L2 Multilingual Reasoning (44 languages)
task_categories:
- text-generation
- question-answering
size_categories:
- 100K<n<1M
tags:
- reasoning
- multilingual
- tiny-aya
- chain-of-thought
dataset_info:
- config_name: "am"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3806
  - name: test
    num_examples: 448
- config_name: "ar"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 22968
  - name: test
    num_examples: 2538
- config_name: "bg"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4176
  - name: test
    num_examples: 451
- config_name: "bn"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3803
  - name: test
    num_examples: 422
- config_name: "ca"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4251
  - name: test
    num_examples: 512
- config_name: "cs"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4410
  - name: test
    num_examples: 456
- config_name: "de"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 20438
  - name: test
    num_examples: 2306
- config_name: "el"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4422
  - name: test
    num_examples: 489
- config_name: "eu"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3280
  - name: test
    num_examples: 365
- config_name: "fa"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4087
  - name: test
    num_examples: 430
- config_name: "fi"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3334
  - name: test
    num_examples: 412
- config_name: "fil"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 2852
  - name: test
    num_examples: 336
- config_name: "fr"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 21538
  - name: test
    num_examples: 2317
- config_name: "ga"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3967
  - name: test
    num_examples: 470
- config_name: "ha"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4551
  - name: test
    num_examples: 499
- config_name: "he"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4036
  - name: test
    num_examples: 453
- config_name: "hi"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4084
  - name: test
    num_examples: 478
- config_name: "hu"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3621
  - name: test
    num_examples: 427
- config_name: "id"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4435
  - name: test
    num_examples: 472
- config_name: "ig"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4632
  - name: test
    num_examples: 542
- config_name: "it"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4143
  - name: test
    num_examples: 470
- config_name: "ja"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 20374
  - name: test
    num_examples: 2349
- config_name: "jv"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 5197
  - name: test
    num_examples: 601
- config_name: "km"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3420
  - name: test
    num_examples: 421
- config_name: "ko"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 18999
  - name: test
    num_examples: 2036
- config_name: "lt"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3894
  - name: test
    num_examples: 414
- config_name: "ms"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3198
  - name: test
    num_examples: 367
- config_name: "mt"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 2851
  - name: test
    num_examples: 342
- config_name: "no"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4513
  - name: test
    num_examples: 504
- config_name: "pa"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3520
  - name: test
    num_examples: 371
- config_name: "pl"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 2620
  - name: test
    num_examples: 293
- config_name: "ru"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4649
  - name: test
    num_examples: 495
- config_name: "sk"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4292
  - name: test
    num_examples: 472
- config_name: "sw"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4445
  - name: test
    num_examples: 479
- config_name: "ta"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3403
  - name: test
    num_examples: 415
- config_name: "te"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3460
  - name: test
    num_examples: 411
- config_name: "th"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4085
  - name: test
    num_examples: 451
- config_name: "tr"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3426
  - name: test
    num_examples: 407
- config_name: "uk"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4158
  - name: test
    num_examples: 462
- config_name: "ur"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3291
  - name: test
    num_examples: 350
- config_name: "vi"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4611
  - name: test
    num_examples: 508
- config_name: "yo"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4023
  - name: test
    num_examples: 443
- config_name: "zh"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 4328
  - name: test
    num_examples: 463
- config_name: "zu"
  features:
  - name: id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: domain
    dtype: string
  - name: question
    dtype: string
  - name: thinking
    dtype: string
  - name: output
    dtype: string
  - name: original_question
    dtype: string
  - name: original_thinking
    dtype: string
  - name: original_output
    dtype: string
  splits:
  - name: train
    num_examples: 3991
  - name: test
    num_examples: 447
configs:
  - config_name: "am"
    data_files:
      - split: train
        path: data/am/train.parquet
      - split: test
        path: data/am/test.parquet
  - config_name: "ar"
    data_files:
      - split: train
        path: data/ar/train.parquet
      - split: test
        path: data/ar/test.parquet
  - config_name: "bg"
    data_files:
      - split: train
        path: data/bg/train.parquet
      - split: test
        path: data/bg/test.parquet
  - config_name: "bn"
    data_files:
      - split: train
        path: data/bn/train.parquet
      - split: test
        path: data/bn/test.parquet
  - config_name: "ca"
    data_files:
      - split: train
        path: data/ca/train.parquet
      - split: test
        path: data/ca/test.parquet
  - config_name: "cs"
    data_files:
      - split: train
        path: data/cs/train.parquet
      - split: test
        path: data/cs/test.parquet
  - config_name: "de"
    data_files:
      - split: train
        path: data/de/train.parquet
      - split: test
        path: data/de/test.parquet
  - config_name: "el"
    data_files:
      - split: train
        path: data/el/train.parquet
      - split: test
        path: data/el/test.parquet
  - config_name: "eu"
    data_files:
      - split: train
        path: data/eu/train.parquet
      - split: test
        path: data/eu/test.parquet
  - config_name: "fa"
    data_files:
      - split: train
        path: data/fa/train.parquet
      - split: test
        path: data/fa/test.parquet
  - config_name: "fi"
    data_files:
      - split: train
        path: data/fi/train.parquet
      - split: test
        path: data/fi/test.parquet
  - config_name: "fil"
    data_files:
      - split: train
        path: data/fil/train.parquet
      - split: test
        path: data/fil/test.parquet
  - config_name: "fr"
    data_files:
      - split: train
        path: data/fr/train.parquet
      - split: test
        path: data/fr/test.parquet
  - config_name: "ga"
    data_files:
      - split: train
        path: data/ga/train.parquet
      - split: test
        path: data/ga/test.parquet
  - config_name: "ha"
    data_files:
      - split: train
        path: data/ha/train.parquet
      - split: test
        path: data/ha/test.parquet
  - config_name: "he"
    data_files:
      - split: train
        path: data/he/train.parquet
      - split: test
        path: data/he/test.parquet
  - config_name: "hi"
    data_files:
      - split: train
        path: data/hi/train.parquet
      - split: test
        path: data/hi/test.parquet
  - config_name: "hu"
    data_files:
      - split: train
        path: data/hu/train.parquet
      - split: test
        path: data/hu/test.parquet
  - config_name: "id"
    data_files:
      - split: train
        path: data/id/train.parquet
      - split: test
        path: data/id/test.parquet
  - config_name: "ig"
    data_files:
      - split: train
        path: data/ig/train.parquet
      - split: test
        path: data/ig/test.parquet
  - config_name: "it"
    data_files:
      - split: train
        path: data/it/train.parquet
      - split: test
        path: data/it/test.parquet
  - config_name: "ja"
    data_files:
      - split: train
        path: data/ja/train.parquet
      - split: test
        path: data/ja/test.parquet
  - config_name: "jv"
    data_files:
      - split: train
        path: data/jv/train.parquet
      - split: test
        path: data/jv/test.parquet
  - config_name: "km"
    data_files:
      - split: train
        path: data/km/train.parquet
      - split: test
        path: data/km/test.parquet
  - config_name: "ko"
    data_files:
      - split: train
        path: data/ko/train.parquet
      - split: test
        path: data/ko/test.parquet
  - config_name: "lt"
    data_files:
      - split: train
        path: data/lt/train.parquet
      - split: test
        path: data/lt/test.parquet
  - config_name: "ms"
    data_files:
      - split: train
        path: data/ms/train.parquet
      - split: test
        path: data/ms/test.parquet
  - config_name: "mt"
    data_files:
      - split: train
        path: data/mt/train.parquet
      - split: test
        path: data/mt/test.parquet
  - config_name: "no"
    data_files:
      - split: train
        path: data/no/train.parquet
      - split: test
        path: data/no/test.parquet
  - config_name: "pa"
    data_files:
      - split: train
        path: data/pa/train.parquet
      - split: test
        path: data/pa/test.parquet
  - config_name: "pl"
    data_files:
      - split: train
        path: data/pl/train.parquet
      - split: test
        path: data/pl/test.parquet
  - config_name: "ru"
    data_files:
      - split: train
        path: data/ru/train.parquet
      - split: test
        path: data/ru/test.parquet
  - config_name: "sk"
    data_files:
      - split: train
        path: data/sk/train.parquet
      - split: test
        path: data/sk/test.parquet
  - config_name: "sw"
    data_files:
      - split: train
        path: data/sw/train.parquet
      - split: test
        path: data/sw/test.parquet
  - config_name: "ta"
    data_files:
      - split: train
        path: data/ta/train.parquet
      - split: test
        path: data/ta/test.parquet
  - config_name: "te"
    data_files:
      - split: train
        path: data/te/train.parquet
      - split: test
        path: data/te/test.parquet
  - config_name: "th"
    data_files:
      - split: train
        path: data/th/train.parquet
      - split: test
        path: data/th/test.parquet
  - config_name: "tr"
    data_files:
      - split: train
        path: data/tr/train.parquet
      - split: test
        path: data/tr/test.parquet
  - config_name: "uk"
    data_files:
      - split: train
        path: data/uk/train.parquet
      - split: test
        path: data/uk/test.parquet
  - config_name: "ur"
    data_files:
      - split: train
        path: data/ur/train.parquet
      - split: test
        path: data/ur/test.parquet
  - config_name: "vi"
    data_files:
      - split: train
        path: data/vi/train.parquet
      - split: test
        path: data/vi/test.parquet
  - config_name: "yo"
    data_files:
      - split: train
        path: data/yo/train.parquet
      - split: test
        path: data/yo/test.parquet
  - config_name: "zh"
    data_files:
      - split: train
        path: data/zh/train.parquet
      - split: test
        path: data/zh/test.parquet
  - config_name: "zu"
    data_files:
      - split: train
        path: data/zu/train.parquet
      - split: test
        path: data/zu/test.parquet
---

# Tiny Aya L2 Multilingual Reasoning (44 languages)

Translated multilingual reasoning traces used to train [**Tiny Aya L2-Thinker**](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker).
Each example has the prompt, thinking, and answer in the **same non-English language** alongside the original texts in English.

## Data source

- Prompts from [AM-DeepSeek-R1-0528-Distilled](https://huggingface.co/datasets/a-m-team/AM-DeepSeek-R1-0528-Distilled)
- Thinking traces and outputs distilled from gpt-oss-120b
- Translated with command-a-translate and DeepSeek-V3

## Languages (44)

| Language | Train | Test | Total |
|---|---:|---:|---:|
| Amharic (`am`) | 3,806 | 448 | 4,254 |
| Arabic (`ar`) | 22,968 | 2,538 | 25,506 |
| Bulgarian (`bg`) | 4,176 | 451 | 4,627 |
| Bengali (`bn`) | 3,803 | 422 | 4,225 |
| Catalan (`ca`) | 4,251 | 512 | 4,763 |
| Czech (`cs`) | 4,410 | 456 | 4,866 |
| German (`de`) | 20,438 | 2,306 | 22,744 |
| Greek (`el`) | 4,422 | 489 | 4,911 |
| Basque (`eu`) | 3,280 | 365 | 3,645 |
| Persian (`fa`) | 4,087 | 430 | 4,517 |
| Finnish (`fi`) | 3,334 | 412 | 3,746 |
| Filipino (`fil`) | 2,852 | 336 | 3,188 |
| French (`fr`) | 21,538 | 2,317 | 23,855 |
| Irish (`ga`) | 3,967 | 470 | 4,437 |
| Hausa (`ha`) | 4,551 | 499 | 5,050 |
| Hebrew (`he`) | 4,036 | 453 | 4,489 |
| Hindi (`hi`) | 4,084 | 478 | 4,562 |
| Hungarian (`hu`) | 3,621 | 427 | 4,048 |
| Indonesian (`id`) | 4,435 | 472 | 4,907 |
| Igbo (`ig`) | 4,632 | 542 | 5,174 |
| Italian (`it`) | 4,143 | 470 | 4,613 |
| Japanese (`ja`) | 20,374 | 2,349 | 22,723 |
| Javanese (`jv`) | 5,197 | 601 | 5,798 |
| Khmer (`km`) | 3,420 | 421 | 3,841 |
| Korean (`ko`) | 18,999 | 2,036 | 21,035 |
| Lithuanian (`lt`) | 3,894 | 414 | 4,308 |
| Malay (`ms`) | 3,198 | 367 | 3,565 |
| Maltese (`mt`) | 2,851 | 342 | 3,193 |
| Norwegian (`no`) | 4,513 | 504 | 5,017 |
| Punjabi (`pa`) | 3,520 | 371 | 3,891 |
| Polish (`pl`) | 2,620 | 293 | 2,913 |
| Russian (`ru`) | 4,649 | 495 | 5,144 |
| Slovak (`sk`) | 4,292 | 472 | 4,764 |
| Swahili (`sw`) | 4,445 | 479 | 4,924 |
| Tamil (`ta`) | 3,403 | 415 | 3,818 |
| Telugu (`te`) | 3,460 | 411 | 3,871 |
| Thai (`th`) | 4,085 | 451 | 4,536 |
| Turkish (`tr`) | 3,426 | 407 | 3,833 |
| Ukrainian (`uk`) | 4,158 | 462 | 4,620 |
| Urdu (`ur`) | 3,291 | 350 | 3,641 |
| Vietnamese (`vi`) | 4,611 | 508 | 5,119 |
| Yoruba (`yo`) | 4,023 | 443 | 4,466 |
| Chinese (`zh`) | 4,328 | 463 | 4,791 |
| Zulu (`zu`) | 3,991 | 447 | 4,438 |
| **Total** |  |  | **286,376** |

## Load

```python
from datasets import concatenate_datasets, get_dataset_config_names, load_dataset

# one language
ds = load_dataset("CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning", "ar")

# every language
configs = get_dataset_config_names("CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning")
all_langs = concatenate_datasets(
    [load_dataset("CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning", name, split="train") for name in configs]
)
```

## Columns

- `id`: `{language_code}-{domain}-{index}` (for example `ar-math-000001`)
- `language`, `language_code`: full name and ISO code
- `domain`: `math`, `science`, or `general`
- `question`, `thinking`, `output` in the given language
- `original_question`, `original_thinking`, `original_output`: English source

## Citation

If you use this dataset, please cite:

```bibtex
@misc{mofakhami2026buildingmultilingualbridgesdata,
      title={Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning},
      author={Mehrnaz Mofakhami and Ananya Sahu and Alejandro R. Salamanca and Daniel D'souza and Alexandre Berard and Thomas Euyang and Marzieh Fadaee and Julia Kreutzer},
      year={2026},
      eprint={2609.10445},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2609.10445},
}
```
