---
type: "dataset"
id: "asho1/fastinsight-acl-lacd"
source: "huggingface"
url: "https://huggingface.co/datasets/asho1/fastinsight-acl-lacd"
downloads: 37
summary: "GraFine 실험용 ACL-OCL 및 LACD 코퍼스 그래프와 검색 쿼리 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# asho1/fastinsight-acl-lacd

> dataset · [Hugging Face](https://huggingface.co/datasets/asho1/fastinsight-acl-lacd)

GraFine 실험용 ACL-OCL 및 LACD 코퍼스 그래프와 검색 쿼리 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `Each object-shaped JSONL schema is exposed as an independent Hugging Face dataset config` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each object-shaped JSONL schema is exposed as an independent Hugging Face dataset config` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `647` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains retrieval queries and corpus-graph files used with GraFine experiments on ACL-OCL and LACD.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 970자 ≈ 647 토큰 (viewer statistics, lacd_corpus/train)
