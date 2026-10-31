---
type: "dataset"
id: "seventy4/labor-counsel-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/seventy4/labor-counsel-qa"
downloads: 34
summary: "노동법 조문 기반 노무 상담 챗봇 지도 파인튜닝용 Q&A 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# seventy4/labor-counsel-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/seventy4/labor-counsel-qa)

노동법 조문 기반 노무 상담 챗봇 지도 파인튜닝용 Q&A 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `학습에 쓰는 열: messages(system, user, assistant)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `노동법 조문에 근거해 답하는 노무 상담 챗봇의 지도 파인튜닝(SFT) 데이터입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `노동법 조문에 근거해 답하는 노무 상담 챗봇` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `규모: train 1,169행, validation 315행` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `학습에 쓰는 열: messages(system, user, assistant)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `Gahyun0121/labor-counsel-qa`
- `gggaaammmeee/labor-counsel-qa`
- `jinm1222/labor-counsel-qa`
- `muahseol/labor-counsel-qa`
- `onlyBABA/labor-counsel-qa`
- `qsdunfdsj12/labor-counsel-qa`
- `rhksals2001/labor-counsel-qa`
- `yujin-ai26/labor-counsel-qa`
