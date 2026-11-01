---
type: "dataset"
id: "MisileLab/youtube-bot-comments"
source: "huggingface"
url: "https://huggingface.co/datasets/MisileLab/youtube-bot-comments"
downloads: 30
summary: "한국어 유튜브 댓글에서 봇 생성 여부를 분류하여 봇 탐지 연구에 활용하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
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
# MisileLab/youtube-bot-comments

> dataset · [Hugging Face](https://huggingface.co/datasets/MisileLab/youtube-bot-comments)

한국어 유튜브 댓글에서 봇 생성 여부를 분류하여 봇 탐지 연구에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The actual text content of the comment in Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Boolean label indicating whether the comment is classified as bot-generated (True) or human-generated (False)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `260` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `YouTube comments from the top 50 Korean videos` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Test set: 37,167 examples (20%)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training set: 130,080 examples (70%)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 390자 ≈ 260 토큰 (viewer statistics, default/validation)
