---
type: "dataset"
id: "amitbcp/nomir"
source: "huggingface"
url: "https://huggingface.co/datasets/amitbcp/nomir"
downloads: 138
summary: "NoMIRACL은 18개 언어의 RAG 기반 LLM 견고성 평가용 인간 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# amitbcp/nomir

> dataset · [Hugging Face](https://huggingface.co/datasets/amitbcp/nomir)

NoMIRACL은 18개 언어의 RAG 기반 LLM 견고성 평가용 인간 주석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Retrieval Augmented Generation (RAG) is a powerful approach to incorporate external knowledge into large language models (LLMs) to enhance the accuracy and fait` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Retrieval Augmented Generation (RAG) is a powerful approach to incorporate external knowledge into large language models (LLMs)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:retrieval = `topics, qrels and top-10 (maximum) annotated documents of NoMIRACL` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `LLM robustness is measured using two key metrics: hallucination rate and error rate.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `evaluating LLM robustness in RAG across different language families has been a challenge` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `a human-annotated dataset designed for evaluating LLM robustness in RAG across 18 diverse languages.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
