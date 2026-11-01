---
type: "dataset"
id: "ksryong0/youtube_comment_sentiment_dataset_preprocessing"
source: "huggingface"
url: "https://huggingface.co/datasets/ksryong0/youtube_comment_sentiment_dataset_preprocessing"
downloads: 20
summary: "한국어 유튜브 댓글 감성 분류 데이터셋으로 긍정, 부정, 중립 레이블 포함"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ksryong0/youtube_comment_sentiment_dataset_preprocessing

> dataset · [Hugging Face](https://huggingface.co/datasets/ksryong0/youtube_comment_sentiment_dataset_preprocessing)

한국어 유튜브 댓글 감성 분류 데이터셋으로 긍정, 부정, 중립 레이블 포함

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `- name: comment
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: labels
dtype:
class_label:
names:
'0': 긍정
'1': 부정
'2': 중립` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `62` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `- name: test
num_bytes: 101142
num_examples: 836` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 572859
num_examples: 4735` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `comment` 열 p90 93자 ≈ 62 토큰 (viewer statistics, default/test)
