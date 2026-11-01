---
type: "dataset"
id: "KiteFishAI/kf-embed-pretrain-corpus-700M-raw"
source: "huggingface"
url: "https://huggingface.co/datasets/KiteFishAI/kf-embed-pretrain-corpus-700M-raw"
downloads: 513
summary: "다국어 임베딩 모델 Minnow-Em-v1 사전학습용 7억 쌍 쿼리-긍정 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# KiteFishAI/kf-embed-pretrain-corpus-700M-raw

> dataset · [Hugging Face](https://huggingface.co/datasets/KiteFishAI/kf-embed-pretrain-corpus-700M-raw)

다국어 임베딩 모델 Minnow-Em-v1 사전학습용 7억 쌍 쿼리-긍정 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[질의응답]] — tag_match · tags = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = ``positive` — longer associated passage (article body, answer, code, abstract, etc.)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `46 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It aggregates 16 diverse open-source datasets into a unified collection of `(query, positive)` pairs spanning web text, scientific literature, code, multilingua` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is the stage-1 pretraining corpus used to train Minnow-Em-v1` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
