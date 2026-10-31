---
type: "dataset"
id: "UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB"
source: "huggingface"
url: "https://huggingface.co/datasets/UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB"
downloads: 62
summary: "STSBenchmark 데이터셋의 코드스위칭 버전으로, 다양한 언어-영어 혼합 문장 쌍으로 의미 유사도 평가용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
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
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB

> dataset · [Hugging Face](https://huggingface.co/datasets/UTokyo-Yokoya-Lab/stsbenchmark-sts_CS-MTEB)

STSBenchmark 데이터셋의 코드스위칭 버전으로, 다양한 언어-영어 혼합 문장 쌍으로 의미 유사도 평가용 데이터입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `STSBenchmark CS-MTEB` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `STSBenchmark CS-MTEB` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:retrieval = `test set sentence pairs rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portug` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `test set sentence pairs rewritten in Chinese-English, Japanese-English, German-English, Spanish-English, Korean-English, French-English, Italian-English, Portug` · 신뢰도 low
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
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Massive Text Embedding Benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Code-switching test sets` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Original train, validation, and test splits` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
