---
type: "dataset"
id: "Algocean/20G-tone-dataset-instruct-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Algocean/20G-tone-dataset-instruct-ko"
downloads: 25
summary: "정적이고 공적인 한국어 문장을 20~30대 여성 친구 말투로 바꾸는 말투 보정 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Algocean/20G-tone-dataset-instruct-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Algocean/20G-tone-dataset-instruct-ko)

정적이고 공적인 한국어 문장을 20~30대 여성 친구 말투로 바꾸는 말투 보정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `user 메시지는 변환 요청과 원문을 담는다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `정적이고 공적인 한국어 문장` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `주 용도: kanana 기반 말투 보정 모델 SFT` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
