---
type: "dataset"
id: "umyunsang/govon-civil-response-data"
source: "huggingface"
url: "https://huggingface.co/datasets/umyunsang/govon-civil-response-data"
downloads: 31
summary: "민원답변 어댑터 학습용 instruction-tuning 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# umyunsang/govon-civil-response-data

> dataset · [Hugging Face](https://huggingface.co/datasets/umyunsang/govon-civil-response-data)

민원답변 어댑터 학습용 instruction-tuning 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `"instruction": "다음 민원에 대한 답변을 작성해 주세요.", "input": "질문 텍스트"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `"output": "답변 텍스트 (평균 500-1000자)"` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `707` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `civil-complaint` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `val 7,425 10MB` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 66,819 90MB` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1061자 ≈ 707 토큰 (viewer statistics, default/validation)
