---
type: "dataset"
id: "traintogpb/aihub-koja-translation-integrated-small-100k"
source: "huggingface"
url: "https://huggingface.co/datasets/traintogpb/aihub-koja-translation-integrated-small-100k"
downloads: 59
summary: "AI Hub의 한-일 번역 데이터셋 10개를 병합한 100K 크기 학습용 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# traintogpb/aihub-koja-translation-integrated-small-100k

> dataset · [Hugging Face](https://huggingface.co/datasets/traintogpb/aihub-koja-translation-integrated-small-100k)

AI Hub의 한-일 번역 데이터셋 10개를 병합한 100K 크기 학습용 데이터입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `한-일 번역 관련 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `한-일 번역 관련 데이터셋` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI Hub의 한-일 번역 관련 데이터셋 10개를 병합한 자료입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `small-100k (train): 병합 데이터 중 100K개 사용; 총 100,000개` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `ko` 열 p90 91자 ≈ 23 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `traintogpb/aihub-koja-translation-integrated-base-1m`
- `traintogpb/aihub-koja-translation-integrated-large-4.3m`
