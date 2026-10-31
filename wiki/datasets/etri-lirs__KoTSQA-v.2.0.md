---
type: "dataset"
id: "etri-lirs/KoTSQA-v.2.0"
source: "huggingface"
url: "https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0"
downloads: 82
summary: "한국어 시간민감형 질의응답 데이터셋으로 LLM의 지식충돌 문제 평가용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# etri-lirs/KoTSQA-v.2.0

> dataset · [Hugging Face](https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0)

한국어 시간민감형 질의응답 데이터셋으로 LLM의 지식충돌 문제 평가용입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `한국어 시간민감형 질의응답 데이터 (Korean Time-Sensitive Q&A Dataset: KoTSQA)` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `검색증강생성(retrieval-augmented generation)` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `질의응답 데이터셋의 ID
- question: 질문
- ansewrs: 정답목록
- passages: 정답근거 단락들` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- ansewrs: 정답목록` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `44` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 시간민감형 질의응답 데이터 (Korean Time-Sensitive Q&A Dataset: KoTSQA)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `koTSQA 데이터셋의 Split Version. train/validation 등의 용도로 사용하게 하고, test 6,750개, train 750 (강화학습에 활용)임` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 65자 ≈ 44 토큰 (viewer statistics, default/test)
