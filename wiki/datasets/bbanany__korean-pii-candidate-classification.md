---
type: "dataset"
id: "bbanany/korean-pii-candidate-classification"
source: "huggingface"
url: "https://huggingface.co/datasets/bbanany/korean-pii-candidate-classification"
downloads: 38
summary: "한국어 RAG 응답 내 후보 개인정보(PII) 여부를 분류하는 지도 미세조정 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bbanany/korean-pii-candidate-classification

> dataset · [Hugging Face](https://huggingface.co/datasets/bbanany/korean-pii-candidate-classification)

한국어 RAG 응답 내 후보 개인정보(PII) 여부를 분류하는 지도 미세조정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — tag_match · tags = `conversational` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:retrieval = `각 레코드는 Qwen 계열 채팅 형식의 system, user, assistant 메시지 세 개로 구성됩니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 문서 기반 RAG 응답에서 지정된 candidate span이 특정 자연인에게 연결되는 정보인지 PII 또는 NOT_PII로 분류하도록 만든 지도 미세조정 (SFT) 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train data/train.clean.jsonl 15,875 QLoRA training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
