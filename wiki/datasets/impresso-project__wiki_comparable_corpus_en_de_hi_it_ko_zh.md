---
type: "dataset"
id: "impresso-project/wiki_comparable_corpus_en_de_hi_it_ko_zh"
source: "huggingface"
url: "https://huggingface.co/datasets/impresso-project/wiki_comparable_corpus_en_de_hi_it_ko_zh"
downloads: 32
summary: "6개 언어 위키피디아 문서의 주제별 정렬된 비교 말뭉치로 다국어 문서 비교에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[hi]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# impresso-project/wiki_comparable_corpus_en_de_hi_it_ko_zh

> dataset · [Hugging Face](https://huggingface.co/datasets/impresso-project/wiki_comparable_corpus_en_de_hi_it_ko_zh)

6개 언어 위키피디아 문서의 주제별 정렬된 비교 말뭉치로 다국어 문서 비교에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Information Representation Fairness in Long-Document Embeddings` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `document-level comparable corpus of Wikipedia articles across 6 languages` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Article text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Article text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11965` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a document-level comparable corpus of Wikipedia articles` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 47861자 ≈ 11965 토큰 (viewer statistics, default/en)
