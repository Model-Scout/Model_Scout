---
type: "dataset"
id: "MCG-NJU/TimeLens2-93K"
source: "huggingface"
url: "https://huggingface.co/datasets/MCG-NJU/TimeLens2-93K"
downloads: 13955
summary: "TimeLens2-93K는 다양한 도메인의 긴 영상과 텍스트-시간 구간 쌍을 포함한 대규모 시계열 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
# MCG-NJU/TimeLens2-93K

> dataset · [Hugging Face](https://huggingface.co/datasets/MCG-NJU/TimeLens2-93K)

TimeLens2-93K는 다양한 도메인의 긴 영상과 텍스트-시간 구간 쌍을 포함한 대규모 시계열 영상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `multi-turn SFT conversations with diverse query and answer formats` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `return auditable evidence, and transfer across grounding instructions` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `training generalist video models that can search long timelines` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `video-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking, task:retrieval, task:visual_qa = `93,232 text–temporal interval pairs` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `23,793 videos` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `multi-turn SFT conversations with diverse query and answer formats` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `cover broad web domains such as entertainment, education, sports, news, science and technology, gaming, travel, vehicles, music, and daily life` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `We hope it serves as a strong foundation for training generalist video models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
