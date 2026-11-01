---
type: "dataset"
id: "b111111/Silver-Audio-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/b111111/Silver-Audio-Dataset"
downloads: 141
summary: "긴급 상황 음성 인식용 MFCC 특징 추출 오디오 데이터셋으로, SilverAssistant 프로젝트에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# b111111/Silver-Audio-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/b111111/Silver-Audio-Dataset)

긴급 상황 음성 인식용 MFCC 특징 추출 오디오 데이터셋으로, SilverAssistant 프로젝트에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `emergency sound detection and classification tasks` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = ``.npy` files containing MFCC features extracted from raw audio recordings` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `training and evaluating machine learning models in the context of real-world emergency sound detection and classification tasks` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `real-world emergency sound detection and classification tasks` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `specifically designed for training and evaluating machine learning models` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `SilverAvocado/Silver-Audio-Dataset`
