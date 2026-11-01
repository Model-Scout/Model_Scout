---
type: "dataset"
id: "MC7ever/super-lfm-blend-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/MC7ever/super-lfm-blend-v3"
downloads: 44
summary: "explicit horror와 NSFW 창작물을 포함한 blended chat-SFT 코퍼스, 연구용 로컬 파인튜닝용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MC7ever/super-lfm-blend-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/MC7ever/super-lfm-blend-v3)

explicit horror와 NSFW 창작물을 포함한 blended chat-SFT 코퍼스, 연구용 로컬 파인튜닝용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Schema: `messages` (`list >`) and `source` (string).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Schema: `messages` (`list >`) and `source` (string).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is published for research and private experimentation.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `| validation | 8,582 |` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `| train | 163,048 |` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
