---
type: "dataset"
id: "nthakur/swim-ir-cross-lingual"
source: "huggingface"
url: "https://huggingface.co/datasets/nthakur/swim-ir-cross-lingual"
downloads: 477
summary: "SWIM-IR는 27개 언어의 위키피디아 문단과 다국어 질의 쌍으로 구성된 다국어 검색 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nthakur/swim-ir-cross-lingual

> dataset · [Hugging Face](https://huggingface.co/datasets/nthakur/swim-ir-cross-lingual)

SWIM-IR는 27개 언어의 위키피디아 문단과 다국어 질의 쌍으로 구성된 다국어 검색 학습 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `A paragraph is sampled from the Wikipedia corpus which describes an entity.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `The question arising from the Wikipedia paragraph is generated using a large language model (LLM).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `183` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A paragraph is sampled from the Wikipedia corpus which describes an entity.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 731자 ≈ 183 토큰 (viewer statistics, ko/train)
