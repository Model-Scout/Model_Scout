---
type: "dataset"
id: "trueorfalse441/korean_hate_speech_copy"
source: "huggingface"
url: "https://huggingface.co/datasets/trueorfalse441/korean_hate_speech_copy"
downloads: 90
summary: "K-MHaS는 한국 온라인 뉴스 댓글의 혐오 표현을 8개 세부 범주로 다중 라벨 분류하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# trueorfalse441/korean_hate_speech_copy

> dataset · [Hugging Face](https://huggingface.co/datasets/trueorfalse441/korean_hate_speech_copy)

K-MHaS는 한국 온라인 뉴스 댓글의 혐오 표현을 8개 세부 범주로 다중 라벨 분류하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Each instance is a news comment with a corresponding one or more hate speech classes` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `The K-MHaS (Korean Multi-label Hate Speech) dataset contains 109k utterances from Korean online news comments` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `we provide splitted datasets that have 78,977(train) / 8,776 (validation) / 21,939 (test) samples` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
