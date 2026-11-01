---
type: "dataset"
id: "traintogpb/aihub-koen-translation-integrated-large-10m"
source: "huggingface"
url: "https://huggingface.co/datasets/traintogpb/aihub-koen-translation-integrated-large-10m"
downloads: 100
summary: "AI Hub의 한-영 번역 데이터셋 8개를 병합한 1천만 건 규모 번역 데이터입니다."
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
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# traintogpb/aihub-koen-translation-integrated-large-10m

> dataset · [Hugging Face](https://huggingface.co/datasets/traintogpb/aihub-koen-translation-integrated-large-10m)

AI Hub의 한-영 번역 데이터셋 8개를 병합한 1천만 건 규모 번역 데이터입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `사용 칼럼: '한국어', '영어'` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `사용 칼럼: '한국어', '영어'` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `258` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI Hub의 한-영 번역 관련 데이터셋 8개를 병합한 자료입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train / validation / test는 8:1:1 비율로 분할되었습니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 388자 ≈ 258 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `traintogpb/aihub-koen-translation-integrated-base-1m`
- `traintogpb/aihub-koen-translation-integrated-small-100k`
