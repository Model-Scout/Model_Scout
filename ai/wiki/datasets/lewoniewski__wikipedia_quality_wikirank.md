---
type: "dataset"
id: "lewoniewski/wikipedia_quality_wikirank"
source: "huggingface"
url: "https://huggingface.co/datasets/lewoniewski/wikipedia_quality_wikirank"
downloads: 192
summary: "47개 언어 위키피디아 문서 4700만 건의 WikiRank 품질 점수 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lewoniewski/wikipedia_quality_wikirank

> dataset · [Hugging Face](https://huggingface.co/datasets/lewoniewski/wikipedia_quality_wikirank)

47개 언어 위키피디아 문서 4700만 건의 WikiRank 품질 점수 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The WikiRank quality score is a metric designed to assess the overall quality of a Wikipedia article.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Wikipedia articles` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `WikiRank quality score` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `53 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Datasets with WikiRank quality score as of 1 August 2024 for 47 million Wikipedia articles in 55 language versions` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `Title` 열 p90 38자 ≈ 9 토큰 (viewer statistics, default/wikirank_20240801)
