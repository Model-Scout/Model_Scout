---
language:
- ko
task_categories:
- document-question-answering
- visual-document-retrieval
tags:
- visual-document-retrieval
- academic-papers
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

<center><h1>KorFinVDR: Academic Paper</h1></center>

This dataset card covers `academic_paper`, a corpus of Bank of Korea research papers for Korean visual document retrieval and complex-document question answering. It is one of the five subsets comprising the **KorFinVDR Benchmark**.

## Links

* **GitHub:** https://github.com/Marker-Inc-Korea/kor-fin-vdr
* **Collection:** https://huggingface.co/collections/MarkrAI/korfinvdr

## Dataset Summary

- **Description:** Research papers presenting empirical analyses of macroeconomic, financial, and policy issues.
- **Language:** Korean (`ko`)
- **Document type:** Academic and policy research papers

## Dataset Statistics

- **Total documents:** 78
- **Total corpus pages:** 3,188
- **Total queries:** 378
- **Total qrels:** 2,905

> [!NOTE]
> **Page images are not distributed with this dataset.** The source documents are published by the Bank of Korea under a copyright policy that does not permit redistribution of the rendered pages, so the `corpus` config carries an **`image_path`** column (a relative path) instead of the page image. Reconstruct the images locally with the included [`download_images.py`](./download_images.py), which downloads the original PDFs listed in `document_metadata` and renders each page to the exact `image_path` location:
>
> ```bash
> pip install datasets pymupdf requests
> huggingface-cli login                          # gated-access token
> python download_images.py
> ```
>
> Run it from the directory where you load the dataset. Images are written to `images/academic_paper/<doc_id>/<doc_id>_<page:04d>.png` (PyMuPDF, 300 DPI, 1-indexed), matching the `image_path` column. Then attach them:
>
> ```python
> from datasets import load_dataset
> from PIL import Image
>
> corpus = load_dataset("MarkrAI/korfinvdr-academic_paper", "corpus", split="test")
> corpus = corpus.map(lambda row: {"image": Image.open(row["image_path"])})
> ```

## Dataset Structure

### 1. Corpus

Contains all rendered pages from the 78 source documents in the academic-paper corpus.

Data instance of a single item from the corpus subset:

```json
{
  "corpus_id": "<int>",
  "image_path": "<str>",
  "doc_id": "<str>",
  "page_number_in_doc": "<int>",
  "markdown": "<str>",
  "elements": "<str>"
}
```

- **corpus_id** `<int>`: A unique numerical identifier for the corresponding corpus page.
- **image_path** `<str>`: Relative path to the page image (`images/academic_paper/<doc_id>/<doc_id>_<page:04d>.png`). The image itself is not shipped; reconstruct it with `download_images.py` (see the note above).
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
  "answer": "<str>",
  "evidence_modality": "<str>"
}
```

- **query_id** `<int>`: A unique numerical identifier for the query.
- **query** `<str>`: The search question or statement used for retrieval.
- **query_type** `<str>`: The category describing the query intent.
- **query_format** `<str>`: The query format, such as `instruction`, `keyword`, or `question`.
- **answer** `<str>`: The answer grounded in the source documents.
- **evidence_modality** `<str>`: The evidence type required to answer the query, rather than the model input format: `text`, `image`, or `cross-modal`.
  - **Text (`text`):** Explicit body text, titles, captions, or footnotes are sufficient; no table, chart, figure, or diagram content is required.
  - **Image (`image`):** A table, chart, figure, infographic, diagram, map, or visual-layout information alone is necessary and sufficient. Table cells, rows, columns, and merged-cell structure are treated as image evidence.
  - **Cross-modal (`cross-modal`):** The answer is supported by both prose text and a table or visual element. The evidence may be complementary or repeated across the two modalities.

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

> [!WARNING]
> The source documents in this subset are published by the Bank of Korea (한국은행). Under the Bank of Korea's copyright policy, when you use information posted on the Bank of Korea website you must always cite the Bank of Korea as the source, and you must clearly indicate any modification, alteration, or processing of that information.
>
> This dataset does not redistribute the page images; it provides only processed text/layout extractions (`markdown`, `elements`) and `image_path` references, which are derivatives of the source documents.

## Data Privacy and Removal Requests

While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Citation

If you use KorFinVDR in your research, please cite this work.

```bibtex

```
