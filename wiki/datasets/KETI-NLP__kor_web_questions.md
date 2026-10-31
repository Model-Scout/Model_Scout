---
type: "dataset"
id: "KETI-NLP/kor_web_questions"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_web_questions"
downloads: 22
summary: "KETI-NLP/kor_web_questions는 질문-답변 쌍 기반 의미 파싱 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KETI-NLP/kor_web_questions

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_web_questions)

KETI-NLP/kor_web_questions는 질문-답변 쌍 기반 의미 파싱 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Semantic Parsing on {F}reebase from Question-Answer Pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Semantic Parsing on {F}reebase from Question-Answer Pairs` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Semantic Parsing on {F}reebase from Question-Answer Pairs` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 28자 ≈ 18 토큰 (viewer statistics, default/test)
