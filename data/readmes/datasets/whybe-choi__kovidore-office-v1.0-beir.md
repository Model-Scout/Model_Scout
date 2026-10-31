---
dataset_info:
- config_name: corpus
  features:
  - name: corpus-id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: test
    num_bytes: 1916779011.325
    num_examples: 1993
  download_size: 1875823141
  dataset_size: 1916779011.325
- config_name: qrels
  features:
  - name: query-id
    dtype: int64
  - name: corpus-id
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: test
    num_bytes: 10980
    num_examples: 244
  download_size: 3343
  dataset_size: 10980
- config_name: queries
  features:
  - name: query-id
    dtype: int64
  - name: query
    dtype: string
  splits:
  - name: test
    num_bytes: 25647
    num_examples: 222
  download_size: 15330
  dataset_size: 25647
configs:
- config_name: corpus
  data_files:
  - split: test
    path: corpus/test-*
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
  - Figures
  - multimodal-retrieval
  - QA
  - Visual QA
---

# KoViDoRe - Office v1.0

This dataset is part of the **KoViDoRe Benchmark** for Korean visual document retrieval evaluation. Specifically, it is focused on **Office Documents** such as reports and press releases for text-to-image retrieval tasks.

## Dataset Summary

- **Domain:** Korean business/office documents (e.g., 보고서, 보도자료 등)
- **Task:** Visual document retrieval (text query → relevant document image)
- **Format:** BEIR-compatible (corpus, queries, qrels)

**Statistics:**
- Number of Documents (Pages): **1,990+**
- Number of Queries: **222**
- Number of Relevance Judgments (qrels): **244**
- All text queries are in Korean.

## Dataset Structure

- **corpus**
  - `corpus-id`: Unique page ID
  - `image`: Document page image (PIL Image)
  - `title`: Document title or file name
- **queries**
  - `query-id`: Unique query ID
  - `query`: Korean text question
- **qrels**
  - `query-id`
  - `corpus-id`
  - `score`: (1 = relevant)

## Usage

This dataset is intended for benchmarking the performance of visual document retrieval systems on real-world Korean reports and press releases.

**Note:**  
Due to licensing restrictions, **original images are not redistributed with this dataset.  
Please download the required image data directly from [AI Hub](https://www.aihub.or.kr/) (오피스 문서 생성 데이터) and place them as instructed in the [KoVidore-benchmark GitHub](https://github.com/whybe-choi/KoVidore-benchmark) repository.**

## Acknowledgments

- Based on data provided by [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71811) (오피스 문서 생성 데이터)

---
