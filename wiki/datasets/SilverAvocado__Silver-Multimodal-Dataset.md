---
type: "dataset"
id: "SilverAvocado/Silver-Multimodal-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/SilverAvocado/Silver-Multimodal-Dataset"
downloads: 185
summary: "일상 활동, 폭력, 낙상 상황을 오디오와 비디오로 감지하는 멀티모달 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
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
# SilverAvocado/Silver-Multimodal-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/SilverAvocado/Silver-Multimodal-Dataset)

일상 활동, 폭력, 낙상 상황을 오디오와 비디오로 감지하는 멀티모달 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `combined audio and video sources` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `combined audio and video sources` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `Designed for safety systems, healthcare monitoring, and smart home applications` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is designed to support the development of machine learning models` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999999.0` · 신뢰도 high
