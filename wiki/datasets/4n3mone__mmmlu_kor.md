---
type: "dataset"
id: "4n3mone/mmmlu_kor"
source: "huggingface"
url: "https://huggingface.co/datasets/4n3mone/mmmlu_kor"
downloads: 25
summary: "MMMLU 데이터셋의 한국어 번역 테스트셋으로 AI 모델의 일반 지식 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 4n3mone/mmmlu_kor

> dataset · [Hugging Face](https://huggingface.co/datasets/4n3mone/mmmlu_kor)

MMMLU 데이터셋의 한국어 번역 테스트셋으로 AI 모델의 일반 지식 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The MMLU is a widely recognized benchmark of general knowledge attained by AI models.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `We translated the MMLU’s test set into 14 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `We translated the MMLU’s test set into 14 languages` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `255` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It covers a broad range of topics from 57 different categories, covering elementary-level knowledge up to advanced professional subjects like law, physics, hist` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `We translated the MMLU’s test set into 14 languages using professional human translators.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Question` 열 p90 382자 ≈ 255 토큰 (viewer statistics, default/test)
