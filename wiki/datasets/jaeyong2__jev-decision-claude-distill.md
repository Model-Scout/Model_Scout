---
type: "dataset"
id: "jaeyong2/jev-decision-claude-distill"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/jev-decision-claude-distill"
downloads: 302
summary: "Claude가 라벨링한 다양한 유형의 의사결정 상태 데이터로, 모델 미세조정용 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/jev-decision-claude-distill

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/jev-decision-claude-distill)

Claude가 라벨링한 다양한 유형의 의사결정 상태 데이터로, 모델 미세조정용 학습 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each record is a decision state (document, log, ticket, chat, JSON record, passage…` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `All text is synthetic and written to stratified plans (language × task family × length × option count` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The training and validation data behind jaeyong2/clef-flash-jev-claude-distill, a fine-tune of Cloudflare/clef-flash (9B)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
