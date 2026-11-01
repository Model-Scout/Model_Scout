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
    num_bytes: 631521115
    num_examples: 1477
  download_size: 609050878
  dataset_size: 631521115
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
    num_bytes: 4180
    num_examples: 20
  download_size: 4892
  dataset_size: 4180
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
    num_bytes: 9912
    num_examples: 413
  download_size: 4709
  dataset_size: 9912
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
    num_bytes: 101517
    num_examples: 163
  download_size: 48180
  dataset_size: 101517
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
<center><h1>KoViDoRe v2 : Economic trends</h1></center>

This dataset, `Economic trends`, is a corpus of `periodic reports` on major economic indicators in Korea, intended for complex-document understanding tasks. It is one of the 4 corpora comprising the **KoViDoRe v2 Benchmark**.

## Links

* **Github:** [https://github.com/whybe-choi/kovidore-benchmark](https://github.com/whybe-choi/kovidore-benchmark)
* **Collection:** [https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2](https://huggingface.co/collections/whybe-choi/kovidore-benchmark-beir-v2)
* **Data Generation Pipeline:** [https://github.com/whybe-choi/kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator)

### Dataset Summary

For this specific dataset (`Economic trends`):

- Description: Consists of 20 reports on economic trends in Korea

- Language: ko

- Domain: Economic

- Document Types: Reports

### Dataset Statistics

- Total Documents : 20
- Total Pages : 1477
- Total Queries : 163
- Average number of pages per query : 2.55

### Languages

The documents in this dataset are in `korean`.

### Queries per Document

| Doc ID | Context | Summary | Count |
|--------|---------|---------|-------|
| 2021_03_recent_economic_trends | 7 | 5 | 12 |
| 2021_06_recent_economic_trends | 4 | 7 | 11 |
| 2021_09_recent_economic_trends | 7 | 8 | 15 |
| 2021_12_recent_economic_trends | 7 | 3 | 10 |
| 2022_03_recent_economic_trends | 4 | 2 | 6 |
| 2022_06_recent_economic_trends | 4 | 4 | 8 |
| 2022_09_recent_economic_trends | 3 | 3 | 6 |
| 2022_12_recent_economic_trends | 3 | 7 | 10 |
| 2023_03_recent_economic_trends | 5 | 3 | 8 |
| 2023_06_recent_economic_trends | 4 | 5 | 9 |
| 2023_09_recent_economic_trends | 4 | 8 | 12 |
| 2023_12_recent_economic_trends | 4 | 10 | 14 |
| 2024_03_recent_economic_trends | 3 | 5 | 8 |
| 2024_06_recent_economic_trends | 7 | 4 | 11 |
| 2024_09_recent_economic_trends | 7 | 0 | 7 |
| 2024_12_recent_economic_trends | 4 | 0 | 4 |
| 2025_03_recent_economic_trends | 5 | 0 | 5 |
| 2025_06_recent_economic_trends | 2 | 0 | 2 |
| 2025_09_recent_economic_trends | 3 | 0 | 3 |
| 2025_12_recent_economic_trends | 2 | 0 | 2 |
| **Total** | **89** | **74** | **163** |


### Queries type

| Query Type | Count |
|------------|-------|
| Compare-Contrast | 87 |
| Numerical | 67 |
| Open-Ended | 105 |
| Enumerative | 4 |
| Boolean | 7 |
| Extractive | 20 |
| Multi-Hop | 109 |

### Queries format

| Query Format | Count |
|--------------|-------|
| Question | 66 |
| Instruction | 74 |
| Keyword | 23 |
| **Total** | **163** |

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

## Data Privacy and Removal Requests
While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Acknowledgements
This dataset is inspired by the [ViDoRe V3](https://huggingface.co/collections/vidore/vidore-benchmark-v3), and we thank the [ViDoRe](https://huggingface.co/vidore) team for their foundational work.
We also thank the [Upstage x AWS AI Initiative](https://www.upstage.ai/events/ai-initiative-2025-ko) for granting us free access to their API services.
Finally, We acknowledge the datasets provided by the [Public Data Portal(공공데이터포털)](https://www.data.go.kr/index.do), which were utilized to construct the tasks in KoViDoRe v2.
