---
language:
- ko
task_categories:
- document-question-answering
- visual-document-retrieval
tags:
- visual-document-retrieval
- corporate-disclosure
- korean
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
dataset_info:
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
    num_bytes: 34008
    num_examples: 1417
  download_size: 9580
  dataset_size: 34008
- config_name: queries
  features:
  - name: query_id
    dtype: int64
  - name: query
    dtype: string
  - name: query_type
    dtype: string
  - name: query_format
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: test
    num_bytes: 197046
    num_examples: 489
  download_size: 90520
  dataset_size: 197046
---

<center><h1>KorFinVDR: Disclosure Report</h1></center>

This dataset, `disclosure_report`, is a corpus of Fair Trade Commission reports on corporate-group ownership for Korean visual document retrieval and complex-document question answering. It is one of the five subsets comprising the **KorFinVDR Benchmark**.

## Links

* **GitHub:** https://github.com/Marker-Inc-Korea/kor-fin-vdr
* **Collection:** https://huggingface.co/collections/MarkrAI/korfinvdr

## Dataset Summary

- **Description:** Reports detailing corporate-group ownership structures and shareholding patterns.
- **Language:** Korean (`ko`)
- **Document type:** Ownership-status reports and corporate-group ownership maps

## Dataset Statistics

- **Total documents:** 24
- **Total corpus pages:** 1,231
- **Total queries:** 489
- **Total qrels:** 1,436

## Dataset Structure

### 1. Corpus

Contains the full collection of documents to be searched.

Data instance of a single item from the corpus subset:

```json
{
  "corpus_id": "<int>",
  "image": "<PIL.Image>",
  "doc_id": "<str>",
  "markdown": "<str>",
  "elements": "<str>",
  "page_number_in_doc": "<int>"
}
```

- **corpus_id** `<int>`: A unique numerical identifier for the corresponding corpus page.
- **image** `<PIL.Image>`: The rendered page image.
- **doc_id** `<str>`: The identifier of the source document.
- **markdown** `<str>`: Text extracted from the page using the document-processing pipeline.
- **elements** `<str>`: A JSON-serialized list of extracted layout elements with bounding boxes and text.
- **page_number_in_doc** `<int>`: The original page number in the source document.

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

For documents subject to the [Korea Open Government License (KOGL)](https://www.kogl.or.kr/info/license.do) Type 1 and Type 2, the sources are attributed as follows:

| Title | Doc ID | Type | Attribution Text |
| :--- | :--- | :--- | :--- |
| 2013년 주식소유현황 보고서 | `2013년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2013년에 작성하여 공공누리 제1유형으로 개방한 '13년 주식소유현황'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=38433)에서 무료로 다운받으실 수 있습니다. |
| 2013년 기업집단별 소유지분도 | `2013년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2013년에 작성하여 공공누리 제1유형으로 개방한 '2013 기업집단별 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=38435)에서 무료로 다운받으실 수 있습니다. |
| 2015년 주식소유현황 보고서 | `2015년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2015년에 작성하여 공공누리 제1유형으로 개방한 '2015년_주식소유현황보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=39381)에서 무료로 다운받으실 수 있습니다. |
| 2015년 기업집단별 소유지분도 | `2015년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2015년에 작성하여 공공누리 제1유형으로 개방한 '2015년 기업집단 소유지분도(61개)'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=39381)에서 무료로 다운받으실 수 있습니다. |
| 2016년 주식소유현황 보고서 | `2016년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2016년에 작성하여 공공누리 제1유형으로 개방한 '2016년 주식소유현황 보고서 (최종)1'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=39876)에서 무료로 다운받으실 수 있습니다. |
| 2016년 기업집단별 소유지분도 | `2016년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2016년에 작성하여 공공누리 제1유형으로 개방한 '2016년 기업집단 소유지분도(65개)'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=39877)에서 무료로 다운받으실 수 있습니다. |
| 2017년 주식소유현황 보고서 | `2017년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2017년에 작성하여 공공누리 제1유형으로 개방한 '2017년 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=40526)에서 무료로 다운받으실 수 있습니다. |
| 2017년 기업집단별 소유지분도 | `2017년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2017년에 작성하여 공공누리 제1유형으로 개방한 '2017년 기업집단 소유지분도(57개)'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=40526)에서 무료로 다운받으실 수 있습니다. |
| 2018년 주식소유현황 보고서 | `2018년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2018년에 작성하여 공공누리 제1유형으로 개방한 '2018년 공시대상 기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=40865)에서 무료로 다운받으실 수 있습니다. |
| 2018년 기업집단별 소유지분도 | `2018년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2018년에 작성하여 공공누리 제1유형으로 개방한 '2018년 기업집단 소유지분도(60개)'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=40865)에서 무료로 다운받으실 수 있습니다. |
| 2019년 주식소유현황 보고서 | `2019년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2019년에 작성하여 공공누리 제1유형으로 개방한 '2019년주식소유현황 보고서(수정)'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=41222)에서 무료로 다운받으실 수 있습니다. |
| 2019년 기업집단별 소유지분도 | `2019년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2019년에 작성하여 공공누리 제1유형으로 개방한 '2019년도 기업집단 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=41222)에서 무료로 다운받으실 수 있습니다. |
| 2020년 주식소유현황 보고서 | `2020년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2020년에 작성하여 공공누리 제1유형으로 개방한 '2020년 주식소유현황 보고서(수정)'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=41607)에서 무료로 다운받으실 수 있습니다. |
| 2020년 기업집단별 소유지분도 | `2020년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2020년에 작성하여 공공누리 제1유형으로 개방한 '기업집단별 소유지분도(수정)'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=41607)에서 무료로 다운받으실 수 있습니다. |
| 2021년 주식소유현황 보고서 | `2021년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2021년에 작성하여 공공누리 제1유형으로 개방한 '2021년 공시대상기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=42091)에서 무료로 다운받으실 수 있습니다. |
| 2021년 기업집단별 소유지분도 | `2021년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2021년에 작성하여 공공누리 제1유형으로 개방한 '2021년 기업집단별 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=42091)에서 무료로 다운받으실 수 있습니다. |
| 2022년 주식소유현황 보고서 | `2022년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2022년에 작성하여 공공누리 제1유형으로 개방한 '2022년 공시대상기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=42558)에서 무료로 다운받으실 수 있습니다. |
| 2022년 기업집단별 소유지분도 | `2022년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2022년에 작성하여 공공누리 제1유형으로 개방한 '2022년 기업집단 소유지분도(수정)'을 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=42558)에서 무료로 다운받으실 수 있습니다. |
| 2023년 주식소유현황 보고서 | `2023년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2023년에 작성하여 공공누리 제1유형으로 개방한 '2023년 공시대상기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=43043)에서 무료로 다운받으실 수 있습니다. |
| 2023년 기업집단별 소유지분도 | `2023년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2023년에 작성하여 공공누리 제1유형으로 개방한 '2023년 기업집단별 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=43043)에서 무료로 다운받으실 수 있습니다. |
| 2024년 주식소유현황 보고서 | `2024년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2024년에 작성하여 공공누리 제1유형으로 개방한 '2024년 공시대상기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=43571)에서 무료로 다운받으실 수 있습니다. |
| 2024년 기업집단별 소유지분도 | `2024년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2024년에 작성하여 공공누리 제1유형으로 개방한 '2024년 기업집단별 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=43571)에서 무료로 다운받으실 수 있습니다. |
| 2025년 주식소유현황 보고서 | `2025년 주식소유현황 보고서` | Type 1 | 공정거래위원회에서 2025년에 작성하여 공공누리 제1유형으로 개방한 '2025년 공시대상기업집단 주식소유현황 보고서'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=46408)에서 무료로 다운받으실 수 있습니다. |
| 2025년 기업집단별 소유지분도 | `2025년 기업집단별 소유지분도` | Type 1 | 공정거래위원회에서 2025년에 작성하여 공공누리 제1유형으로 개방한 '2025년 기업집단별 소유지분도'를 이용하였으며, 해당 저작물은 [공정거래위원회 보도자료](https://www.ftc.go.kr/www/selectBbsNttView.do?key=12&bordCd=3&searchCtgry=01,02&nttSn=46408)에서 무료로 다운받으실 수 있습니다. |

## Data Privacy and Removal Requests

While this dataset is released under open licenses, we respect the privacy of individuals and the ownership of source content. If you are a data subject, author, or publisher and are uncomfortable with the inclusion of your data or documents in this release, please contact us at whybe.choi@gmail.com. We will promptly review your request.

## Citation

If you use KorFinVDR in your research, please cite this work.

```bibtex

```
