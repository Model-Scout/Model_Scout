---
type: "dataset"
id: "data-is-better-together/fineweb-c"
source: "huggingface"
url: "https://huggingface.co/datasets/data-is-better-together/fineweb-c"
downloads: 3008
summary: "FineWeb-C는 다국어 교육 콘텐츠에 대한 커뮤니티 기반 라벨링 데이터셋으로, 고품질 교육 콘텐츠 식별 및 다국어 LLM 개발에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# data-is-better-together/fineweb-c

> dataset · [Hugging Face](https://huggingface.co/datasets/data-is-better-together/fineweb-c)

FineWeb-C는 다국어 교육 콘텐츠에 대한 커뮤니티 기반 라벨링 데이터셋으로, 고품질 교육 콘텐츠 식별 및 다국어 LLM 개발에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Rate how educational the content is.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `86 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `894` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The annotations in this dataset will help train AI systems to automatically identify high-quality educational content in more languages` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3576자 ≈ 894 토큰 (viewer statistics, kor_Hang/train)

## 이 데이터로 학습한 모델

- [[tartuNLP__mmBERT-small-m-edu-classifier|tartuNLP/mmBERT-small-m-edu-classifier]]
