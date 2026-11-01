---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-performance-v1-sionic-retrieval-train-family-4146"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-sionic-retrieval-train-family-4146"
downloads: 52
summary: "Korean MIRACL, MrTidy, MLDR train-family 4,146행으로 구성된 한국어 임베딩 성능 향상용 검색 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# LLM-OS-Models/korean-embedding-performance-v1-sionic-retrieval-train-family-4146

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-sionic-retrieval-train-family-4146)

Korean MIRACL, MrTidy, MLDR train-family 4,146행으로 구성된 한국어 임베딩 성능 향상용 검색 학습 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Korean Sionic Retrieval Train-Family 4,146` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `실제 학습 queue는 current 1M winner로 candidate 24개를 찾고 `.95*s_pos` 아래의 score-quantile negative 7개를 고른 뒤, 같은 수의 1M general row와 50:50 replay한다.` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:retrieval = `각 row는 ms-swift의 `messages`, `positive_messages`, `negative_messages` schema다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `각 row는 ms-swift의 `messages`, `positive_messages`, `negative_messages` schema다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean MIRACL, MrTidy, MLDR train-family` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `공개 train-family supervision의 비중을 짧게 높이는 specialist ablation용이다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
