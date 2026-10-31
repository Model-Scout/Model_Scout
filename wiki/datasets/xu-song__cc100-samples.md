---
type: "dataset"
id: "xu-song/cc100-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/xu-song/cc100-samples"
downloads: 485
summary: "cc100 데이터셋의 처음 10,000줄을 포함하는 텍스트 데이터 하위셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# xu-song/cc100-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/xu-song/cc100-samples)

cc100 데이터셋의 처음 10,000줄을 포함하는 텍스트 데이터 하위셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Each data point is a paragraph of text.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each data point is a paragraph of text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `109 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `34` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The cc100-samples is a subset which contains first 10,000 lines of cc100.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The cc100-samples is a subset which contains first 10,000 lines of cc100.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 134자 ≈ 34 토큰 (viewer statistics, ko/train)
