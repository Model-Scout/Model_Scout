---
type: "dataset"
id: "traintogpb/aihub-flores-koen-integrated-prime-base-300k"
source: "huggingface"
url: "https://huggingface.co/datasets/traintogpb/aihub-flores-koen-integrated-prime-base-300k"
downloads: 9
summary: "AIHub와 FLoRes 한-영 번역 데이터셋을 합본한 고품질 한영 번역 학습용 데이터셋입니다."
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
# traintogpb/aihub-flores-koen-integrated-prime-base-300k

> dataset · [Hugging Face](https://huggingface.co/datasets/traintogpb/aihub-flores-koen-integrated-prime-base-300k)

AIHub와 FLoRes 한-영 번역 데이터셋을 합본한 고품질 한영 번역 학습용 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `한-영 번역 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `한-영 번역 데이터셋` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `170` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI Hub의 한-영 번역 데이터셋과 FLoRes 한-영 번역 데이터셋의 합본입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Sparta-Mini-300K(Train)` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `en_ref` 열 p90 254자 ≈ 170 토큰 (viewer statistics, default/validation)
