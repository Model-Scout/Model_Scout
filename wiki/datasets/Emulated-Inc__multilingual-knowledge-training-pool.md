---
type: "dataset"
id: "Emulated-Inc/multilingual-knowledge-training-pool"
source: "huggingface"
url: "https://huggingface.co/datasets/Emulated-Inc/multilingual-knowledge-training-pool"
downloads: 303
summary: "다국어 7개 데이터셋의 객관식 질문을 통합한 다국어 지식 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Emulated-Inc/multilingual-knowledge-training-pool

> dataset · [Hugging Face](https://huggingface.co/datasets/Emulated-Inc/multilingual-knowledge-training-pool)

다국어 7개 데이터셋의 객관식 질문을 통합한 다국어 지식 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Public multiple-choice questions in many languages from seven datasets` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `question text, as its source publishes it` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the answer options, as a list of strings` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `116 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `168` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Regional examination and licensing questions collected in the country they are used in` · 신뢰도 low
- **도메인**: [[의료·보건]] — ner · readme = `Indian medical entrance examination questions, AIIMS and NEET PG` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Train on either layer or on both` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 671자 ≈ 168 토큰 (viewer statistics, default/validation)
