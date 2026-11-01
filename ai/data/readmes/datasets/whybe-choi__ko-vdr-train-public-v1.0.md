---
dataset_info:
  features:
  - name: query_id
    dtype: int64
  - name: source_type
    dtype: string
  - name: query_type
    dtype: string
  - name: query_format
    dtype: string
  - name: query
    dtype: string
  - name: doc_id
    dtype: string
  - name: pos_id
    dtype: int64
  - name: pos
    dtype: image
  - name: answer
    dtype: string
  - name: markdown
    dtype: string
  - name: elements
    dtype: string
  - name: page_number_in_doc
    dtype: int64
  - name: relevance_score
    dtype: int64
  splits:
  - name: train
    num_bytes: 127386406157.944
    num_examples: 177286
  download_size: 112281479041
  dataset_size: 127386406157.944
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- document-question-answering
- visual-document-retrieval
language:
- ko
tags:
- Visual Retrieving
- Industrial RAG
- datadesigner
size_categories:
- 100K<n<1M
---
---
<p align="center">
  <img width="800" alt="Korean VDR Train" src="https://cdn-uploads.huggingface.co/production/uploads/655eeb5532537bcc8d7460ab/Em_W5suEXUrDiSHNoDREs.png" />
</p>

This dataset is a training dataset for Korean Visual Document Retrieval. It includes 177,286 query-page pairs (85,568 unique queries) generated from 23 Korean government and public institution PDF documents using LLM-based (Solar Pro 3) synthetic query generation. Queries are generated from two sources: page-level summaries (79%) and direct page context (21%), covering 7 query types (compare-contrast, open-ended, enumerative, multi-hop, extractive, numerical, boolean) in instruction and question formats.

## Links

* **Github:** [https://github.com/whybe-choi/kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator)

### Dataset Summary

- Description: Training data for Korean Visual Document Retrieval, generated from Korean government and public institution reports
- Language: ko
- Document Types: Government reports, guidelines, manuals, survey reports

### Dataset Statistics

- Total Documents : 23
- Total Pages : 3,857
- Total Queries : 85,568
- Average number of pages per query : 2.1

### Number of Relevant Pages per Query

| # Relevant Pages | # Queries |
|:-:|:-:|
| 1 | 28,006 |
| 2 | 37,094 |
| 3 | 12,144 |
| 4 | 4,927 |
| 5 | 2,093 |
| 6 | 847 |
| 7 | 297 |
| 8 | 114 |
| 9 | 46 |

### Queries per Document

| Doc ID | Context | Summary | Count |
|--------|---------|---------|-------|
| 기후에너지환경부_에너지총조사_20241130 | 3,452 | 2,942 | 6,394 |
| 25년_주요업무계획(게시용) | 2,874 | 2,812 | 5,686 |
| 2025년_지방공무원_인사실무 | 2,256 | 2,938 | 5,194 |
| (최종보고서)_국제_OTT_산업_실태조사_및_국내_OTT_글로벌_진출_방안_연구 | 1,876 | 2,904 | 4,780 |
| 국토교통부_해외건설_세무업무_매뉴얼_20220404 | 939 | 3,053 | 3,992 |
| 제3차_해양수산발전기본계획(2021-2030) | 886 | 2,896 | 3,782 |
| 2024_회계연도_기업체노동비용조사_보고서 | 657 | 3,048 | 3,705 |
| 국토안전관리원_스마트_안전유지관리_시설물_확대방안_마련_용역_보고서_2024 | 852 | 2,831 | 3,683 |
| 국토교통부_해외건설_법률컨설팅_사례_20240628 | 562 | 2,996 | 3,558 |
| 제3차_환경관리해역_기본계획 | 539 | 2,973 | 3,512 |
| (최종)UN개황(2019)-내지-최종(웹용) | 772 | 2,632 | 3,404 |
| 합성데이터_생성활용_안내서(2024.12) | 485 | 2,901 | 3,386 |
| 생체정보_보호_안내서(2024.12) | 311 | 3,040 | 3,351 |
| 1.조사요약(2024부산방문관광객실태조사) | 241 | 3,077 | 3,318 |
| 2025_산업보고서(방위산업)_라틴아메리카_협력센터 | 46 | 3,228 | 3,274 |
| 개인정보_유출_등_사고_대응_매뉴얼(2024.3) | 213 | 3,035 | 3,248 |
| 2026년_공무원_인재개발_종합계획 | 306 | 2,941 | 3,247 |
| 한국인터넷진흥원_개인정보_유출_신고_동향_및_예방_방법_20241231 | 144 | 3,088 | 3,232 |
| 2025_산업보고서(제약바이오)_라틴아메리카_협력센터 | 53 | 3,092 | 3,145 |
| 한국노인인력개발원_노인_일자리_및_사회활동_지원사업_시행_20년의_성과 | 32 | 2,985 | 3,017 |
| 한국수력원자력(주)_i_SMR_및_SSNC_설명자료_20250829 | 127 | 2,788 | 2,915 |
| 지점별_인입가능량_최종_분석_결과 | 11 | 2,892 | 2,903 |
| 행정안전부_모바일_전자정부서비스_앱_소스코드_검증_가이드라인_20211029 | 199 | 2,643 | 2,842 |
| **Total** | **17,833** | **67,735** | **85,568** |

### Query Type

| Query Type | Count |
|------------|-------|
| Compare-Contrast | 12,716 |
| Enumerative | 12,522 |
| Open-Ended | 12,289 |
| Multi-Hop | 12,200 |
| Numerical | 12,152 |
| Extractive | 12,104 |
| Boolean | 11,585 |

### Query Format

| Query Format | Count |
|--------------|-------|
| Instruction | 43,127 |
| Question | 42,441 |
| **Total** | **85,568** |

## Dataset Structure

Each row represents a query-page pair with the following fields:

```json
{
  "query_id": <int>,
  "source_type": <str>,
  "query_type": <str>,
  "query_format": <str>,
  "query": <str>,
  "doc_id": <str>,
  "pos_id": <int>,
  "pos": <PIL.Image>,
  "answer": <str>,
  "markdown": <str>,
  "elements": <str>,
  "page_number_in_doc": <int>,
  "relevance_score": <int>
}
```

- **query_id** \<int\> : A unique numerical identifier for the query.
- **source_type** \<str\> : `"summary"` or `"context"`, metadata about the type of information used by the annotation pipeline to create the query.
- **query_type** \<str\> : The type of query (e.g., `"compare-contrast"`, `"open-ended"`, `"enumerative"`, `"multi-hop"`, `"extractive"`, `"numerical"`, `"boolean"`).
- **query_format** \<str\> : The syntactic format of the query (`"instruction"` or `"question"`).
- **query** \<str\> : The actual text of the search question or instruction used for retrieval.
- **doc_id** \<str\> : Name of the source document.
- **pos_id** \<int\> : A unique numerical identifier for the positive page.
- **pos** \<PIL.Image\> : The matched page image.
- **answer** \<str\> : The answer extracted from the source documents.
- **markdown** \<str\> : Extracted text from the page using an OCR pipeline.
- **elements** \<str\> : JSON-serialized list of extracted layout elements with bounding boxes and text from the page using an OCR pipeline.
- **page_number_in_doc** \<int\> : Original page number inside the document.
- **relevance_score** \<int\> : Relevance score for the query-page pair. Can be either 1 (Critically Relevant) or 2 (Fully Relevant):
  - Fully Relevant (2) - The page contains the complete answer.
  - Critically Relevant (1) - The page contains facts or information that are required to answer the query, though additional information is required.

## License Information

All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The licensing status of the original source documents (the corpus) and any parsed text (`markdown` column in the corpus) are inherited from their respective publishers.

For documents subject to the [Korea Open Government License (KOGL)](https://www.kogl.or.kr/info/license.do) Type 1, the sources are attributed as follows:

| Title | Doc ID | Type | Attribution Text |
| :--- | :--- | :--- | :--- |
| 개인정보 유출 등 사고 대응 매뉴얼 | 개인정보_유출_등_사고_대응_매뉴얼(2024.3) | Type 1 | 본 저작물은 개인정보보호위원회에서 2024년 작성하여 공공누리 제 1유형으로 개방한 '개인정보 유출 등 사고 대응 매뉴얼'을 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10123)에서 무료로 다운받으실 수 있습니다. |
| 생체정보 보호 안내서 | 생체정보_보호_안내서(2024.12) | Type 1 | 본 저작물은 개인정보보호위원회에서 2024년 작성하여 공공누리 제 1유형으로 개방한 '생체정보 보호 안내서'를 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10900)에서 무료로 다운받으실 수 있습니다. |
| 합성데이터 생성활용 안내서 | 합성데이터_생성활용_안내서(2024.12) | Type 1 | 본 저작물은 개인정보보호위원회에서 2025년 작성하여 공공누리 제 1유형으로 개방한 '합성데이터 생성·활용 안내서'를 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10915)에서 무료로 다운받으실 수 있습니다. |

## Acknowledgements

This dataset was generated using the [kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator) pipeline.
We acknowledge the datasets provided by the [Public Data Portal(공공데이터포털)](https://www.data.go.kr/index.do), which were utilized to construct this training dataset.