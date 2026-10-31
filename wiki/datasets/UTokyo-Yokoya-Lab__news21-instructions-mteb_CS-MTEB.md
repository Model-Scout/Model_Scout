---
type: "dataset"
id: "UTokyo-Yokoya-Lab/news21-instructions-mteb_CS-MTEB"
source: "huggingface"
url: "https://huggingface.co/datasets/UTokyo-Yokoya-Lab/news21-instructions-mteb_CS-MTEB"
downloads: 104
summary: "다국어 코드스위칭 쿼리와 지침을 포함한 뉴스21 Instructions MTEB 임베딩 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# UTokyo-Yokoya-Lab/news21-instructions-mteb_CS-MTEB

> dataset · [Hugging Face](https://huggingface.co/datasets/UTokyo-Yokoya-Lab/news21-instructions-mteb_CS-MTEB)

다국어 코드스위칭 쿼리와 지침을 포함한 뉴스21 Instructions MTEB 임베딩 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Massive Text Embedding Benchmark` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories, task_ids = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `queries and instructions rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portu` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `queries and instructions rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portu` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `156` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `News21 Instructions CS-MTEB
An MTEB dataset
Massive Text Embedding Benchmark` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 624자 ≈ 156 토큰 (viewer statistics, instructions_ko_en/instruction)
