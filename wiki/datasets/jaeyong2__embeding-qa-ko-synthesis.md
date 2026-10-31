---
type: "dataset"
id: "jaeyong2/embeding-qa-ko-synthesis"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/embeding-qa-ko-synthesis"
downloads: 8
summary: "maywell/ko_wikidata_QA 기반의 한국어 임베딩 질의응답 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/embeding-qa-ko-synthesis

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/embeding-qa-ko-synthesis)

maywell/ko_wikidata_QA 기반의 한국어 임베딩 질의응답 합성 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `context dataset from maywell/ko_wikidata_QA` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `context dataset from maywell/ko_wikidata_QA` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering = `context dataset from maywell/ko_wikidata_QA` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `context dataset from maywell/ko_wikidata_QA` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `context dataset from maywell/ko_wikidata_QA` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 45자 ≈ 30 토큰 (viewer statistics, default/train)
