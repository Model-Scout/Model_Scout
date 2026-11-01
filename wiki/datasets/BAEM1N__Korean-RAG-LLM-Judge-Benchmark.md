---
type: "dataset"
id: "BAEM1N/Korean-RAG-LLM-Judge-Benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/BAEM1N/Korean-RAG-LLM-Judge-Benchmark"
downloads: 77
summary: "한국어 RAG 300 Q&A에 46개 답변 생성 모델과 LLM 평가 결과를 포함한 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[상거래·상품]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# BAEM1N/Korean-RAG-LLM-Judge-Benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/BAEM1N/Korean-RAG-LLM-Judge-Benchmark)

한국어 RAG 300 Q&A에 46개 답변 생성 모델과 LLM 평가 결과를 포함한 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `46개 답변 생성 모델의 답변과 LLM-as-Judge 평가 결과를 얹은 데이터셋입니다.` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `jina-reranker-m0` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `표·이미지 기반 문항이 절반 가까이로` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `table | 50` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:reranking, task:retrieval = `한국어 RAG 300 Q&A` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `46개 답변 생성 모델의 답변과 LLM-as-Judge 평가 결과` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `336` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `commerce | 60` · 신뢰도 medium
- **도메인**: [[금융·경제]] — ner · readme = `finance | 60` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `medical | 60` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `law | 60` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `public | 60` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `allganize/RAG-Evaluation-Dataset-KO의 한국어 RAG 300 Q&A 위에 46개 답변 생성 모델의 답변과 LLM-as-Judge 평가 결과를 얹은 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `x-ai_grok-4.20_answer` 열 p90 504자 ≈ 336 토큰 (viewer statistics, consolidated/train)
