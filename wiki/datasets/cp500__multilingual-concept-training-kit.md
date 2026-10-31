---
type: "dataset"
id: "cp500/multilingual-concept-training-kit"
source: "huggingface"
url: "https://huggingface.co/datasets/cp500/multilingual-concept-training-kit"
downloads: 47
summary: "영어, 일본어, 한국어 6개 도메인 다국어 개념 병목 검색 및 추론용 합성 학습 키트입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cp500/multilingual-concept-training-kit

> dataset · [Hugging Face](https://huggingface.co/datasets/cp500/multilingual-concept-training-kit)

영어, 일본어, 한국어 6개 도메인 다국어 개념 병목 검색 및 추론용 합성 학습 키트입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `trains NLI head, Dempster-Shafer verification` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:reranking, task:retrieval = `(query, positive, 5 hard neg, 1 easy neg) triplets` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `trains cross-lingual SPLADE retrieval` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `finance, geopolitics, pharma.` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `A synthetic, cross-domain training kit for multilingual concept-bottleneck retrieval and reasoning.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Fine-tuning multilingual SPLADE / sparse retrieval models` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
