---
dataset_info:
  features:
  - name: english
    dtype: string
  - name: korean
    dtype: string
  - name: from
    dtype: string
  - name: category
    dtype: string
  - name: en_token_len
    dtype: int64
  - name: ko_token_len
    dtype: int64
  splits:
  - name: train
    num_bytes: 2810892205.574631
    num_examples: 1429410
  - name: valid
    num_bytes: 983235.1129398253
    num_examples: 500
  - name: test
    num_bytes: 983235.1129398253
    num_examples: 500
  download_size: 1058654967
  dataset_size: 2812858675.800511
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
---

# 9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거 | (1.4m)

- [jhflow/orca_ko_en_pair](https://huggingface.co/datasets/jhflow/orca_ko_en_pair) | qeustion, output | 19k *2  = 38k
- [jhflow/platypus_ko_en_pair](https://huggingface.co/datasets/jhflow/platypus_ko_en_pair) | insturction_ko, output_ko | 24k * 2 = 48k 
- [jhflow/dolly_ko_en_pair](https://huggingface.co/datasets/jhflow/dolly_ko_en_pair) | instruction, context, response | 15k * 3 = 45k 
- [heegyu/OIG-small-chip2-ko](https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko) | user_translated, chip_translated | 210k * 2 = 420k
- [lemon-mint/en_ko_translation_purified_v0.1](https://huggingface.co/datasets/lemon-mint/en_ko_translation_purified_v0.1) | korean | 1.4k 
- [squarelike/sharegpt_deepl_ko_translation](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation) | korean | 486k 
- [amphora/parallel-wiki-koen](https://huggingface.co/datasets/amphora/parallel-wiki-koen) | text_ko | 30k
- [kuotient/gsm8k-ko](https://huggingface.co/datasets/kuotient/gsm8k-ko) | question, answer |  8k * 2 = 16k
- [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean) | question, answer | 193k *2 = 386k

**Special Thanks to [jhflow](https://huggingface.co/jhflow), [heegyu](https://huggingface.co/heegyu), [lemon-mint](https://huggingface.co/lemon-mint), [squarelike](https://huggingface.co/squarelike), [kuotient](https://huggingface.co/kuotient).**