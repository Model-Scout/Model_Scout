---
type: "dataset"
id: "LLM-OS-Models/korean-legal-source-heldout-retrieval-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-legal-source-heldout-retrieval-v1"
downloads: 39
summary: "한국 법령·행정규칙·판례·자치법규 원문 구조로 만든 10,000개 쿼리 검색용 홀드아웃 데이터셋이다."
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
---
# LLM-OS-Models/korean-legal-source-heldout-retrieval-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-legal-source-heldout-retrieval-v1)

한국 법령·행정규칙·판례·자치법규 원문 구조로 만든 10,000개 쿼리 검색용 홀드아웃 데이터셋이다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `각 query는 source-native positive 하나만 qrel로 갖는다` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `각 query는 source-native positive 하나만 qrel로 갖는다` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `holdout이다` · 신뢰도 medium
