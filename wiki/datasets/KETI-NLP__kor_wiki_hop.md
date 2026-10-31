---
type: "dataset"
id: "KETI-NLP/kor_wiki_hop"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_wiki_hop"
downloads: 52
summary: "KETI-NLP/kor_wiki_hop는 다중 문서 기반 멀티홉 독해를 위한 한국어 위키피디아 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_wiki_hop

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_wiki_hop)

KETI-NLP/kor_wiki_hop는 다중 문서 기반 멀티홉 독해를 위한 한국어 위키피디아 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `multi-hop reading comprehension across documents` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `multi-hop reading comprehension across documents` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `wiki_hop` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Constructing Datasets for Multi-hop Reading Comprehension Across Documents` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 33자 ≈ 22 토큰 (viewer statistics, default/validation)
