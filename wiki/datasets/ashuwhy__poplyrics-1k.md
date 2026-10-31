---
type: "dataset"
id: "ashuwhy/poplyrics-1k"
source: "huggingface"
url: "https://huggingface.co/datasets/ashuwhy/poplyrics-1k"
downloads: 11
summary: "Spotify와 Genius에서 수집한 1,000개 팝송 가사와 메타데이터로 감정분석, 가사 생성 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ashuwhy/poplyrics-1k

> dataset · [Hugging Face](https://huggingface.co/datasets/ashuwhy/poplyrics-1k)

Spotify와 Genius에서 수집한 1,000개 팝송 가사와 메타데이터로 감정분석, 가사 생성 등에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `You can use this dataset for various NLP tasks such as sentiment analysis, lyric generation, or genre classification.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `This dataset contains up to 1,000 pop songs with their lyrics, songwriters, genres, and other relevant metadata.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `You can use this dataset for various NLP tasks such as sentiment analysis, lyric generation, or genre classification.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `729` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `This dataset contains up to 1,000 pop songs with their lyrics, songwriters, genres, and other relevant metadata.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You can use this dataset for various NLP tasks such as sentiment analysis, lyric generation, or genre classification.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `lyrics` 열 p90 2915자 ≈ 729 토큰 (viewer statistics, default/train)
