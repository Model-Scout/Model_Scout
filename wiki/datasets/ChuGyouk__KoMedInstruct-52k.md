---
type: "dataset"
id: "ChuGyouk/KoMedInstruct-52k"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/KoMedInstruct-52k"
downloads: 90
summary: "KoMedInstruct-52k는 MedInstruct-52k의 한국어 번역 의료 지침 데이터셋으로 의료 AI 학습용입니다."
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ChuGyouk/KoMedInstruct-52k

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/KoMedInstruct-52k)

KoMedInstruct-52k는 MedInstruct-52k의 한국어 번역 의료 지침 데이터셋으로 의료 AI 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `medical instruction dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `medical instruction dataset` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `533` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `synthetically generated medical instruction dataset` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 800자 ≈ 533 토큰 (viewer statistics, default/train)
