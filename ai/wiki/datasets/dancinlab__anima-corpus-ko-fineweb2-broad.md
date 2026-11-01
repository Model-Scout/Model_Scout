---
type: "dataset"
id: "dancinlab/anima-corpus-ko-fineweb2-broad"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-ko-fineweb2-broad"
downloads: 12
summary: "anima 챗봇의 한국어 일반 대화용 광범위 코퍼스, byte-level 사전학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dancinlab/anima-corpus-ko-fineweb2-broad

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-ko-fineweb2-broad)

anima 챗봇의 한국어 일반 대화용 광범위 코퍼스, byte-level 사전학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `anima conv 303M byte-level pretraining` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `text 컬럼만 추출 (raw UTF-8, byte-vocab256` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `text 컬럼만 추출 (raw UTF-8, byte-vocab256` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 broad (일반) 코퍼스` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습용으로 정규화 없이 원문 그대로` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
