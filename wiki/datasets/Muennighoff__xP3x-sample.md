---
type: "dataset"
id: "Muennighoff/xP3x-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/Muennighoff/xP3x-sample"
downloads: 1308
summary: "6개 언어로 된 다국어 Winograd 스키마 모음으로 교차언어 상식 추론 평가용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Muennighoff/xP3x-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/Muennighoff/xP3x-sample)

6개 언어로 된 다국어 Winograd 스키마 모음으로 교차언어 상식 추론 평가용 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `evaluation of cross-lingual commonsense reasoning capabilities` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Winograd Schemas` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Winograd Schemas` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `220 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `535` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual collection of Winograd Schemas in six languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `can be used for evaluation of cross-lingual commonsense reasoning capabilities` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 2140자 ≈ 535 토큰 (viewer statistics, apps/train)
