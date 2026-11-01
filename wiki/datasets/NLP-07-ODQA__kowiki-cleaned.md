---
type: "dataset"
id: "NLP-07-ODQA/kowiki-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/NLP-07-ODQA/kowiki-cleaned"
downloads: 43
summary: "한국어 위키피디아 XML 덤프에서 추출·정제한 문서 데이터셋으로 RAG 시스템 구축용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NLP-07-ODQA/kowiki-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/NLP-07-ODQA/kowiki-cleaned)

한국어 위키피디아 XML 덤프에서 추출·정제한 문서 데이터셋으로 RAG 시스템 구축용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · readme, tags = `rag` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `43085` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `이 데이터셋은 수능 국어/사회 과목 문제 풀이를 위한 RAG 시스템 구축을 목적으로 생성되었습니다.` · 신뢰도 medium
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 수능 국어/사회 과목 문제 풀이를 위한 RAG 시스템 구축을 목적으로 생성되었습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 64627자 ≈ 43085 토큰 (viewer statistics, default/train)
