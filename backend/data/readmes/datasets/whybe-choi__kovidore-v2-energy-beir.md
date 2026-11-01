---
dataset_info:
- config_name: corpus
  features:
  - name: corpus_id
    dtype: int64
  - name: image
    dtype: image
  - name: doc_id
    dtype: string
  - name: markdown
    dtype: string
  - name: elements
    dtype: string
  - name: page_number_in_doc
    dtype: int64
  splits:
  - name: test
    num_bytes: 1253218113.143
    num_examples: 1993
  download_size: 1613965621
  dataset_size: 1253218113.143
- config_name: document_metadata
  features:
  - name: title
    dtype: string
  - name: file_name
    dtype: string
  - name: url
    dtype: string
  - name: doc_type
    dtype: string
  - name: doc_language
    dtype: string
  - name: provider
    dtype: string
  - name: year
    dtype: int64
  - name: page_number
    dtype: int64
  - name: license
    dtype: string
  splits:
  - name: test
    num_bytes: 3069
    num_examples: 11
  download_size: 5385
  dataset_size: 3069
- config_name: qrels
  features:
  - name: query_id
    dtype: int64
  - name: corpus_id
    dtype: int64
  - name: score
    dtype: int64
  splits:
  - name: test
    num_bytes: 12600
    num_examples: 525
  download_size: 5256
  dataset_size: 12600
- config_name: queries
  features:
  - name: query_id
    dtype: int64
  - name: query
    dtype: string
  - name: language
    dtype: string
  - name: query_types
    list: string
  - name: query_format
    dtype: string
  - name: source_type
    dtype: string
  - name: query_type_for_generation
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: test
    num_bytes: 122254
    num_examples: 173
  download_size: 65837
  dataset_size: 122254
configs:
- config_name: corpus
  data_files:
  - split: test
    path: corpus/test-*
- config_name: document_metadata
  data_files:
  - split: test
    path: document_metadata/test-*
- config_name: qrels
  data_files:
  - split: test
    path: qrels/test-*
- config_name: queries
  data_files:
  - split: test
    path: queries/test-*
task_categories:
- document-question-answering
- visual-document-retrieval
language:
- ko
tags:
- Visual Retrieving
- Industrial RAG
- datadesigner
---
<center><h1>KoViDoRe v2 : Energy</h1></center>

This dataset, `Energy`, is a corpus of `reports` on energy market trends, policy planning, and industry statistics, intended for complex-document understanding tasks. It is one of the 4 corpora comprising the **KoViDoRe v2 Benchmark**.

## Links

* **Github:** [https://github.com/whybe-choi/kovidore-benchmark](https://github.com/whybe-choi/kovidore-benchmark)
* **Collection:** [https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2](https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2)
* **Data Generation Pipeline:** [https://github.com/whybe-choi/kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator)

### Dataset Summary

For this specific dataset (`Energy`):

- Description: Consists of 17 reports on energy market trends, policy planning, and industry statistics

- Language: ko

- Domain: Energy

- Document Types: Reports

### Dataset Statistics

- Total Documents : 11
- Total Pages : 1993
- Total Queries : 173
- Average number of pages per query : 3.03

### Languages

The documents in this dataset are in `korean`.

### Queries per Document

| Doc ID | Context | Summary | Count |
|--------|---------|---------|-------|
| 2017_world_power_market_trends_china | 1 | 4 | 5 |
| 2017_world_power_market_trends_japan | 2 | 4 | 6 |
| 2017_world_power_market_trends_usa | 2 | 5 | 7 |
| 2020_4th_energy_technology_development_plan_energy_storage | 6 | 4 | 10 |
| 2020_4th_energy_technology_development_plan_roadmap_general | 3 | 2 | 5 |
| 2020_daejeon_local_energy_plan | 41 | 4 | 45 |
| 2023_world_power_market_trends | 33 | 10 | 43 |
| 2024_incheon_energy_white_paper | 14 | 4 | 18 |
| 2025_5th_energy_technology_development_plan_demand_management | 8 | 3 | 11 |
| 2025_5th_energy_technology_development_plan_efficiency_improvement | 12 | 1 | 13 |
| 2025_major_countries_climate_energy_policy_trends | 5 | 5 | 10 |
| **Total** | **127** | **46** | **173** |

### Queries type

| Query Type | Count |
|------------|-------|
| Compare-Contrast | 121 |
| Numerical | 45 |
| Open-Ended | 97 |
| Enumerative | 18 |
| Boolean | 10 |
| Extractive | 42 |
| Multi-Hop | 75 |

### Queries format

| Query Format | Count |
|--------------|-------|
| Question | 73 |
| Instruction | 74 |
| Keyword | 26 |
| **Total** | **173** |

## Dataset Structure

### 1. Corpus

Contains the full collection of documents to be searched.

Data instance of a single item from the corpus subset:

```json
{
  "corpus_id": <int>,
  "image": <PIL.Image>,
  "doc_id": <str>,
  "markdown": <str>,
  "elements": <str>,
  "page_number_in_doc": <int>
}
```

- **corpus_id** <int> : A unique numerical identifier for the corresponding corpus document.
- **image** <PIL.Image> : The page
- **doc_id** <str> : name of the document from where the image was extracted
- **markdown** <str> : Extracted text from the Image using an OCR pipeline
- **elements** <str> : JSON-serialized list of extracted layout elements with bounding boxes and text from the Image using an OCR pipeline
- **page_number_in_doc** <int> : Original page number inside the document

### 2. Queries
Contains set of questions or search queries.
Data Instance of a single item from the queries subset:
```json
{
  "query_id": <int>,
  "query": <str>,
  "language": <str>,
  "query_types": <List[str]>,
  "query_format": <str>,
  "source_type": <str>,
  "query_type_for_generation": <str>,
  "answer": <str>
}
```
- **query_id** <int> : A unique numerical identifier for the query.
- **query** <str> : The actual text of the search question or statement used for retrieval.
- **language** <str> : The language of the query text.
- **query_types** <List[str]> : A list of categories or labels describing the query's intent.
- **query_format** <str> : The syntactic format of the query ("intruction", "keyword" or "question").
- **source_type** <str> : "summary" or "context", metadata about the type of information used by the annotation pipeline to create the query
- **query_type_for_generation** <str> : The specific type requested when the query was generated
- **answer** <str> : The answer extracted from the source documents, merged from human annotations using an LLM.

### 3. Qrels
Maps queries to their corresponding relevant documents.
Data Instance of a single item for the qrels subset:
```json
{
  "query_id": <int>,
  "corpus_id": <int>,
  "score": <int>,
}
```
- **query_id** <int> : A unique numerical identifier for the query.
- **corpus_id** <int> : A unique numerical identifier for the corresponding corpus document.
- **score** <int> : Relevance score for the pair `<query, corpus>`. Can be either 1 (Critically Relevant) or 2 (Fully Relevant):
  - Fully Relevant (2) - The page contains the complete answer.
  - Critically Relevant (1) - The page contains facts or information that are required to answer the query, though additional information is required.

### 4. Original PDFs
All the original pdfs used to build the corpus are distributed in the "pdfs" folder of this directory.

## License information
All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The licensing status of the original source documents (the corpus) and any parsed text (`markdown` column in the corpus) are inherited from their respective publishers. The specific license governing each original document is provided in the `documents_metadata["license"]` field of that document's entry.

For documents subject to the [Korea Open Government License (KOGL)](https://www.kogl.or.kr/info/license.do) Type 1 and Type 2, the sources are attributed as follows:

| Title | Doc ID | Type | Attribution Text |
| :--- | :--- | :--- | :--- |
| 제4차 에너지기술개발계획 기술로드맵-에너지저장 | 2020_4th_energy_technology_development_plan_energy_storage | Type 2  | 본 저작물은 한국에너지기술평가원에서 2020년 작성하여 공공누리 제 2유형으로 개방한 '제4차 에너지기술개발계획 기술로드맵-에너지저장'을 이용하였으며, 해당 저작물은 [한국에너지기술평가원 에너지기술정책 로드맵자료실](https://data.etic.kr/brdartcl/boardarticleList.do?brd_id=BDIDX_e4v5I5hup8AhQOLC23h4nd&srch_menu_nix=anOsJp4d&seltab_idx=0)에서 무료로 다운받으실 수 있습니다. |
| 제4차 에너지기술개발계획 기술로드맵-총괄 | 2020_4th_energy_technology_development_plan_roadmap_general | Type 2 | 본 저작물은 한국에너지기술평가원에서 2020년 작성하여 공공누리 제 2유형으로 개방한 '제4차 에너지기술개발계획 기술로드맵 - 총괄'을 이용하였으며, 해당 저작물은 [한국에너지기술평가원 에너지기술정책 로드맵자료실](https://data.etic.kr/brdartcl/boardarticleList.do?brd_id=BDIDX_e4v5I5hup8AhQOLC23h4nd&srch_menu_nix=anOsJp4d&seltab_idx=0)에서 무료로 다운받으실 수 있습니다. |
| 제5차 에너지기술개발계획 기술로드맵-수요관리 | 2025_5th_energy_technology_development_plan_demand_management | Type 2  | 본 저작물은 한국에너지기술평가원에서 2025년 작성하여 공공누리 제 2유형으로 개방한 '제5차 에너지기술개발계획 기술로드맵-수요관리'을 이용하였으며, 해당 저작물은 [한국에너지기술평가원 에너지기술정책 로드맵자료실](https://data.etic.kr/brdartcl/boardarticleList.do?brd_id=BDIDX_e4v5I5hup8AhQOLC23h4nd&srch_menu_nix=anOsJp4d&seltab_idx=0)에서 무료로 다운받으실 수 있습니다. |
| 제5차 에너지기술개발계획 기술로드맵-효율향상 | 2025_5th_energy_technology_development_plan_efficiency_improvement | Type 2  | 본 저작물은 한국에너지기술평가원에서 2025년 작성하여 공공누리 제 2유형으로 개방한 '제5차 에너지기술개발계획 기술로드맵-효율향상'을 이용하였으며, 해당 저작물은 [한국에너지기술평가원 에너지기술정책 로드맵자료실](https://data.etic.kr/brdartcl/boardarticleList.do?brd_id=BDIDX_e4v5I5hup8AhQOLC23h4nd&srch_menu_nix=anOsJp4d&seltab_idx=0)에서 무료로 다운받으실 수 있습니다. |

## Data Privacy and Removal Requests
While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Acknowledgements
This dataset is inspired by the [ViDoRe V3](https://huggingface.co/collections/vidore/vidore-benchmark-v3), and we thank the [ViDoRe](https://huggingface.co/vidore) team for their foundational work.
We also thank the [Upstage x AWS AI Initiative](https://www.upstage.ai/events/ai-initiative-2025-ko) for granting us free access to their API services.
Finally, We acknowledge the datasets provided by the [Public Data Portal(공공데이터포털)](https://www.data.go.kr/index.do), which were utilized to construct the tasks in KoViDoRe v2.


