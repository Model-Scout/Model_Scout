---
type: "dataset"
id: "ChuGyouk/AI-MO-NuminaMath-CoT-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/AI-MO-NuminaMath-CoT-Ko"
downloads: 83
summary: "수학 문제 풀이를 위한 한국어 번역 데이터셋으로, AI 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ChuGyouk/AI-MO-NuminaMath-CoT-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/AI-MO-NuminaMath-CoT-Ko)

수학 문제 풀이를 위한 한국어 번역 데이터셋으로, AI 모델 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `The original data AI-MO/NuminaMath-CoT is in English.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The original data AI-MO/NuminaMath-CoT is in English.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `The original data AI-MO/NuminaMath-CoT is in English.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1524` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `The original data AI-MO/NuminaMath-CoT is in English.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `If you use this data, please make sure to credit my source!` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 2286자 ≈ 1524 토큰 (viewer statistics, default/train)
