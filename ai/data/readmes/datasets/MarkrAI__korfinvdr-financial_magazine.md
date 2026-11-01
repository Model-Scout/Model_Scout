---
language:
- ko
task_categories:
- document-question-answering
- visual-document-retrieval
tags:
- visual-document-retrieval
- financial-risk
- korean
configs:
- config_name: corpus
  data_files:
  - split: test
    path: corpus/test-*
- config_name: queries
  data_files:
  - split: test
    path: queries/test-*
- config_name: qrels
  data_files:
  - split: test
    path: qrels/test-*
- config_name: document_metadata
  data_files:
  - split: test
    path: document_metadata/test-*
---

<center><h1>KorFinVDR: Financial Magazine</h1></center>

This draft dataset card covers `financial_magazine`, a corpus of Korea Deposit Insurance Corporation financial-risk review articles for Korean visual document retrieval and complex-document question answering. It is one of the five subsets comprising the **KorFinVDR Benchmark**.

## Links

* **GitHub:** https://github.com/Marker-Inc-Korea/kor-fin-vdr
* **Collection:** https://huggingface.co/collections/MarkrAI/korfinvdr

## Dataset Summary

- **Description:** Review articles on financial risks, financial institutions, and related policy issues.
- **Language:** Korean (`ko`)
- **Document type:** Financial-risk review magazine articles

## Dataset Statistics

- **Total documents:** 57
- **Total corpus pages:** 8,868
- **Total queries:** 835
- **Total qrels:** 3,955

## Dataset Structure

### 1. Corpus

Contains the full collection of documents to be searched.

Data instance of a single item from the corpus subset:

```json
{
  "corpus_id": "<int>",
  "image": "<PIL.Image>",
  "doc_id": "<str>",
  "page_number_in_doc": "<int>",
  "markdown": "<str>",
  "elements": "<str>"
}
```

- **corpus_id** `<int>`: A unique numerical identifier for the corresponding corpus page.
- **image** `<PIL.Image>`: The rendered page image.
- **doc_id** `<str>`: The identifier of the source document.
- **page_number_in_doc** `<int>`: The original page number in the source document.
- **markdown** `<str>`: Text extracted from the page using the document-processing pipeline.
- **elements** `<str>`: A JSON-serialized list of extracted layout elements with bounding boxes and text.

### 2. Queries

Contains the set of Korean questions or search queries.

Data instance of a single item from the queries subset:

```json
{
  "query_id": "<int>",
  "query": "<str>",
  "query_type": "<str>",
  "query_format": "<str>",
  "answer": "<str>"
}
```

- **query_id** `<int>`: A unique numerical identifier for the query.
- **query** `<str>`: The search question or statement used for retrieval.
- **query_type** `<str>`: The category describing the query intent.
- **query_format** `<str>`: The query format, such as `instruction`, `keyword`, or `question`.
- **answer** `<str>`: The answer grounded in the source documents.

### 3. Qrels

Maps queries to their corresponding relevant corpus pages.

Data instance of a single item from the qrels subset:

```json
{
  "query_id": "<int>",
  "corpus_id": "<int>",
  "score": "<int>"
}
```

- **query_id** `<int>`: A unique numerical identifier for the query.
- **corpus_id** `<int>`: A unique numerical identifier for the corresponding corpus page.
- **score** `<int>`: The relevance score for the pair `<query, corpus>`. It can be `1` (Partially Relevant) or `2` (Fully Relevant):
  - **Fully Relevant (2):** The page contains the complete answer.
  - **Partially Relevant (1):** The page contains facts required to answer the query, though additional information is required.

### 4. Document Metadata

Contains document-level metadata for the original PDFs.

Data instance of a single item from the `document_metadata` subset:

```json
{
  "doc_id": "<str>",
  "title": "<str>",
  "file_name": "<str>",
  "url": "<str>",
  "provider": "<str>",
  "year": "<int>",
  "page_number": "<int>",
  "license": "<str>"
}
```

- **doc_id** `<str>`: The identifier used to associate corpus pages with their source document.
- **title** `<str>`: The document title.
- **file_name** `<str>`: The original PDF filename.
- **url** `<str>`: The source URL for the document.
- **provider** `<str>`: The original publisher or provider.
- **year** `<int>`: The publication year.
- **page_number** `<int>`: The number of pages in the document.
- **license** `<str>`: The license or copyright information for the source document.

## License Information

All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The licensing status of the original source documents (the corpus) and any parsed text (`markdown` column in the corpus) is inherited from the original publisher. The specific license governing each original document is provided in the `document_metadata["license"]` field of that document's entry.

## Data Privacy and Removal Requests

While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Citation

If you use KorFinVDR in your research, please cite this work.

```bibtex

```
