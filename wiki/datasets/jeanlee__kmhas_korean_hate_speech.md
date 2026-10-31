---
type: "dataset"
id: "jeanlee/kmhas_korean_hate_speech"
source: "huggingface"
url: "https://huggingface.co/datasets/jeanlee/kmhas_korean_hate_speech"
downloads: 340
summary: "K-MHaS는 한국 온라인 뉴스 댓글의 혐오 표현을 8개 세부 범주로 다중 라벨 분류한 데이터셋입니다."
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jeanlee/kmhas_korean_hate_speech

> dataset · [Hugging Face](https://huggingface.co/datasets/jeanlee/kmhas_korean_hate_speech)

K-MHaS는 한국 온라인 뉴스 댓글의 혐오 표현을 8개 세부 범주로 다중 라벨 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The dataset is provided with train/validation/test set in the txt format. Each instance is a news comment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each utterance provides from a single to four labels that can handles Korean language patterns effectively.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `The K-MHaS (Korean Multi-label Hate Speech) dataset contains 109k utterances from Korean online news comments` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `In our repository, we provide splitted datasets that have 78,977(train) / 8,776 (validation) / 21,939 (test) samples` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 60자 ≈ 40 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
