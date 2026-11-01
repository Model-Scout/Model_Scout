---
type: "dataset"
id: "mkd-chanwoo/keural-rag-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-rag-ko"
downloads: 31
summary: "한국어 웹 문서 기반 RAG 특화 SFT 학습용 합성 질문-답변 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# mkd-chanwoo/keural-rag-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-rag-ko)

한국어 웹 문서 기반 RAG 특화 SFT 학습용 합성 질문-답변 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `한국어 웹 문서 155만 개를 시드로 삼아 5가지 태스크 유형으로 1,402,611개의 질문-답변 쌍을 생성했습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `1,402,611개의 질문-답변 쌍을 생성했습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10652` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 웹 문서 155만 개를 시드로 삼아 5가지 태스크 유형으로 1,402,611개의 질문-답변 쌍을 생성했습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT(Supervised Fine-Tuning) 학습용 합성 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 15978자 ≈ 10652 토큰 (viewer statistics, default/train)
