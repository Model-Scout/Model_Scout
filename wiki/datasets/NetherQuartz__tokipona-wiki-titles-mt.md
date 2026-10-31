---
type: "dataset"
id: "NetherQuartz/tokipona-wiki-titles-mt"
source: "huggingface"
url: "https://huggingface.co/datasets/NetherQuartz/tokipona-wiki-titles-mt"
downloads: 22
summary: "20개 언어로 정렬된 위키피디아 문서 제목 병렬 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NetherQuartz/tokipona-wiki-titles-mt

> dataset · [Hugging Face](https://huggingface.co/datasets/NetherQuartz/tokipona-wiki-titles-mt)

20개 언어로 정렬된 위키피디아 문서 제목 병렬 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Each row contains the title of the same Wikipedia article in 20 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Each row contains the title of the same Wikipedia article in 20 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Wikipedia article titles aligned across 20 languages via Wikidata QIDs.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train | 3,204` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tok` 열 p90 26자 ≈ 6 토큰 (viewer statistics, default/train)
