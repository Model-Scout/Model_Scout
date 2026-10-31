---
type: "dataset"
id: "FISA-conclave/news-sentiment-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/FISA-conclave/news-sentiment-dataset"
downloads: 23
summary: "한국어 뉴스 기사에서 추출한 기업 관련 문장의 감성 분석 데이터셋입니다."
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
domain:
  - "[[금융·경제]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FISA-conclave/news-sentiment-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/FISA-conclave/news-sentiment-dataset)

한국어 뉴스 기사에서 추출한 기업 관련 문장의 감성 분석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `'sentence': str,  # 뉴스 기사 문장` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `'label': str      # 감성 레이블 (negative, neutral, positive)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `311` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Test: 9,109개 (20%)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train: 36,435개 (80%)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 466자 ≈ 311 토큰 (viewer statistics, default/test)
