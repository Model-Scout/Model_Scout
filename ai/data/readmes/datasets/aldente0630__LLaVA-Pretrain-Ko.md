---
language:
- ko
license: other
size_categories:
- 100K<n<1M
task_categories:
- visual-question-answering
dataset_info:
  features:
  - name: id
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: image
    dtype: string
  splits:
  - name: train
    num_bytes: 250001835
    num_examples: 555915
  download_size: 101108610
  dataset_size: 250001835
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# LLaVA 비전 인스트럭트 사전 훈련 데이터셋 카드

## 개요
이 데이터셋은 하오톈 리우가 [LLaVA](https://arxiv.org/abs/2304.08485) 모델의 사전 훈련을 위해 제작한 [LLaVA-Pretrain 데이터셋](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain)의 한국어 버전입니다.

## 상세
- 원 데이터셋의 `blip_laion_cc_sbu_558k.json` 파일에 해당합니다. 이미지 파일(`image.zip`)은 원본 리포지토리에서 별도로 [다운로드](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain/resolve/main/images.zip?download=true)할 수 있습니다.
- 사용한 이미지-투-텍스트 모델: Claude 3 Haiku
- 작업 완료 일자: 2024년 7월 27일

## 라이센스
원 데이터셋의 CC-3M 및 BLIP 라이센스를 준수합니다.