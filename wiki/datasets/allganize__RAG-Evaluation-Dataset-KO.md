---
type: "dataset"
id: "allganize/RAG-Evaluation-Dataset-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-KO"
downloads: 620
summary: "금융, 공공, 의료, 법률, 커머스 5개 도메인 한국어 RAG 성능 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
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
  - "[[상거래·상품]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# allganize/RAG-Evaluation-Dataset-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-KO)

금융, 공공, 의료, 법률, 커머스 5개 도메인 한국어 RAG 성능 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `생성한 답변과 정답 답변을 자동 성능 평가 방법을 적용해 각 RAG 방법별 성능 측정을 했습니다.` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `RAG는 Parser, Retrieval, Generation 크게 3가지 파트로 구성되어 있습니다.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `RAG는 Parser, Retrieval, Generation 크게 3가지 파트로 구성되어 있습니다.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `도메인별로 PDF 문서를 수집하여 질문들을 생성했습니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking, task:retrieval = `문서의 페이지 내용을 보고 사용자가 할만한 질문 및 답변들을 만들었습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `문서의 페이지 내용을 보고 사용자가 할만한 질문 및 답변들을 만들었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1058` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 low
- **도메인**: [[금융·경제]] — ner · readme = `5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Allganize RAG 리더보드는 5개 도메인(금융, 공공, 의료, 법률, 커머스)에 대해서 한국어 RAG의 성능을 평가합니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `alli_Llama-3-Alpha-Ko-8B-Instruct_answer` 열 p90 1587자 ≈ 1058 토큰 (viewer statistics, default/test)
