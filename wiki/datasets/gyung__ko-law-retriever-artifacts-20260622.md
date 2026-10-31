---
type: "dataset"
id: "gyung/ko-law-retriever-artifacts-20260622"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/ko-law-retriever-artifacts-20260622"
downloads: 372
summary: "한국 법률 문서 검색 연구를 위한 대규모 리트리버 아티팩트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# gyung/ko-law-retriever-artifacts-20260622

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/ko-law-retriever-artifacts-20260622)

한국 법률 문서 검색 연구를 위한 대규모 리트리버 아티팩트 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `retriever SFT JSONL mixes and metadata.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The retriever is trained to emit JSON tool actions and select evidence; it is not a standalone legal-advice model.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `54` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `evals/: source-rag evaluation outputs.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `retriever SFT JSONL mixes and metadata.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 80자 ≈ 54 토큰 (viewer statistics, default/test)
