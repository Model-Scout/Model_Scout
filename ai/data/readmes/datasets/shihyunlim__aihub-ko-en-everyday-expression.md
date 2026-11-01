---
license: cc-by-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: ko
    dtype: string
  - name: en
    dtype: string
  splits:
  - name: train
    num_bytes: 226959730
    num_examples: 1690052
  download_size: 133582135
  dataset_size: 226959730
task_categories:
- translation
language:
- ko
- en
pretty_name: AIHub Ko-En Everyday Expression
---

# AI Hub Ko-En Dataset : A collection of everyday words

AI 허브의 "한국어-영어 번역(병렬) 말뭉치" 데이터 일부와 "일상생활 및 구어체 한-영 번역 병렬 말뭉치 데이터"를 합친 데이터셋입니다.

- [한국어-영어 번역(병렬) 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=126)
  - 1_구어체(1)
  - 1_구어체(2)
  - 2_대화체_200226
- [일상생활 및 구어체 한-영 번역 병렬 말뭉치 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71265)

중복 데이터를 처리 완료하여 총 1690052개의 한국어, 영어 병렬 문장을 포함합니다.