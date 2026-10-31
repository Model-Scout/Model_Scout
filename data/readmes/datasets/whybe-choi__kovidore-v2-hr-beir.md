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
    num_bytes: 1270222526
    num_examples: 2109
  download_size: 1663254449
  dataset_size: 1270222526
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
    num_bytes: 2445
    num_examples: 9
  download_size: 5650
  dataset_size: 2445
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
    num_bytes: 17424
    num_examples: 726
  download_size: 6675
  dataset_size: 17424
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
    num_bytes: 156378
    num_examples: 221
  download_size: 83586
  dataset_size: 156378
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
<center><h1>KoViDoRe v2 : HR</h1></center>

This dataset, `HR`, is a corpus of `reports` on workforce outlook and employment policy in korea, intended for complex-document understanding tasks. It is one of the 4 corpora comprising the **KoViDoRe v2 Benchmark**.

## Links

* **Github:** [https://github.com/whybe-choi/kovidore-benchmark](https://github.com/whybe-choi/kovidore-benchmark)
* **Collection:** [https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2](https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2)
* **Data Generation Pipeline:** [https://github.com/whybe-choi/kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator)

### Dataset Summary

For this specific dataset (`HR`):

- Description: Consists of 9 reports on workforce outlook and employment policy in korea

- Language: ko

- Domain: HR

- Document Types: Reports

### Dataset Statistics

- Total Documents : 9
- Total Pages : 2109
- Total Queries : 221
- Average number of pages per query : 3.3

### Languages

The documents in this dataset are in `korean`.

### Queries per Document

| Doc ID | Context | Summary | Count |
|--------|---------|---------|------|
| 2018_blind_recruitment_guidebook | 2 | 2 | 4 |
| 2023_advanced_chemical_materials_industrial_technical_manpower_outlook_report | 8 | 15 | 23 |
| 2023_high_tech_fiber_materials_industrial_technical_manpower_outlook_report | 6 | 5 | 11 |
| 2023_korea_occupational_outlook | 45 | 8 | 53 |
| 2023_new_metal_materials_industrial_technical_manpower_outlook_report | 6 | 11 | 17 |
| 2023_next_generation_ceramic_materials_industrial_technical_manpower_outlook_report | 12 | 20 | 32 |
| 2023_secondary_battery_industrial_technical_manpower_outlook_report | 10 | 13 | 23 |
| 2023_survey_on_the_status_of_work_life_balance | 26 | 8 | 34 |
| 2024_labor_conditions_by_employment_type_report | 15 | 9 | 24 |
| **Total** | **130** | **91** | **221** |


### Queries type

| Query Type | Count |
|------------|-------|
| Compare-Contrast | 152 |
| Numerical | 76 |
| Open-Ended | 144 |
| Enumerative | 26 |
| Boolean | 5 |
| Extractive | 23 |
| Multi-Hop | 104 |

### Queries format

| Query Format | Count |
|--------------|-------|
| Question | 99 |
| Instruction | 96 |
| Keyword | 26 |
| **Total** | **221** |

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
| 2024년 고용형태별근로실태조사 | 2024_labor_conditions_by_employment_type_report | Type 1 | 본 저작물은 고용노동부에서 2025년 작성하여 공공누리 제 1유형으로 개방한 '2024년 고용형태별근로실태조사 보고서'를 이용하였으며, 해당 저작물은 [고용노동부 고용노동통계](https://laborstat.moel.go.kr/hmp/index.do)에서 무료로 다운받으실 수 있습니다. |
| 2023 한국직업전망 | 2023_korea_occupational_outlook | Type 2  | 본 저작물은 한국고용정보원에서 2023년 작성하여 공공누리 제 2유형으로 개방한 '2023 한국직업전망(최영순 외 5명)'을 이용하였으며, 해당 저작물은 [한국고용정보원 발간자료](https://www.keis.or.kr/keis/ko/proj/114/pblc/detail.do?categoryIdx=125&pubIdx=9672&pageIndex=2&pageItm=10&searchOrderSort=0&searchGbn=0)에서 무료로 다운받으실 수 있습니다. |

## Data Privacy and Removal Requests
While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Acknowledgements
This dataset is inspired by the [ViDoRe V3](https://huggingface.co/collections/vidore/vidore-benchmark-v3), and we thank the [ViDoRe](https://huggingface.co/vidore) team for their foundational work.
We also thank the [Upstage x AWS AI Initiative](https://www.upstage.ai/events/ai-initiative-2025-ko) for granting us free access to their API services.
Finally, We acknowledge the datasets provided by the [Public Data Portal(공공데이터포털)](https://www.data.go.kr/index.do), which were utilized to construct the tasks in KoViDoRe v2.