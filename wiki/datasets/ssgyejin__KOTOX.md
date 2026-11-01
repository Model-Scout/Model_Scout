---
type: "dataset"
id: "ssgyejin/KOTOX"
source: "huggingface"
url: "https://huggingface.co/datasets/ssgyejin/KOTOX"
downloads: 89
summary: "한국어 독성 텍스트 해독 및 정화 연구용으로 고안된 KOTOX 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ssgyejin/KOTOX

> dataset · [Hugging Face](https://huggingface.co/datasets/ssgyejin/KOTOX)

한국어 독성 텍스트 해독 및 정화 연구용으로 고안된 KOTOX 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `It provides paired neutral-toxic sentences and their obfuscated counterparts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Restore an obfuscated neutral sentence to its original, clean form.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `41` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KOTOX is the first Korean dataset designed for both toxic text detoxification and obfuscation robustness.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `toxic_obfuscated_texts` 열 p90 61자 ≈ 41 토큰 (viewer statistics, default/validation)
