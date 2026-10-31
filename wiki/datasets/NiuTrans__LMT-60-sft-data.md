---
type: "dataset"
id: "NiuTrans/LMT-60-sft-data"
source: "huggingface"
url: "https://huggingface.co/datasets/NiuTrans/LMT-60-sft-data"
downloads: 748
summary: "LMT-60-sft-data는 60개 언어, 234개 번역 방향을 포함한 대규모 다국어 기계번역 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# NiuTrans/LMT-60-sft-data

> dataset · [Hugging Face](https://huggingface.co/datasets/NiuTrans/LMT-60-sft-data)

LMT-60-sft-data는 60개 언어, 234개 번역 방향을 포함한 대규모 다국어 기계번역 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This supervised fine-tuning (SFT) dataset was instrumental in developing these models` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `45 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The LMT (Large-scale Multilingual Translation) project aims to advance Multilingual Machine Translation (MMT)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This supervised fine-tuning (SFT) dataset was instrumental in developing these models` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[NiuTrans__LMT-60-0.6B|NiuTrans/LMT-60-0.6B]]
- [[NiuTrans__LMT-60-0.6B-Base|NiuTrans/LMT-60-0.6B-Base]]
- [[NiuTrans__LMT-60-1.7B|NiuTrans/LMT-60-1.7B]]
- [[NiuTrans__LMT-60-4B|NiuTrans/LMT-60-4B]]
- [[NiuTrans__LMT-60-4B-Base|NiuTrans/LMT-60-4B-Base]]
- [[NiuTrans__LMT-60-8B|NiuTrans/LMT-60-8B]]
