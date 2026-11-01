---
dataset_info:
- config_name: corpus
  features:
  - name: corpus-id
    dtype: string
  - name: image
    dtype: image
  - name: publisher
    dtype: string
  splits:
  - name: test
    num_bytes: 1041895381.812
    num_examples: 1366
  download_size: 885552848
  dataset_size: 1041895381.812
- config_name: qrels
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: test
    num_bytes: 97420
    num_examples: 1496
  download_size: 26198
  dataset_size: 97420
- config_name: queries
  features:
  - name: query-id
    dtype: string
  - name: query
    dtype: string
  splits:
  - name: test
    num_bytes: 173883
    num_examples: 1496
  download_size: 63244
  dataset_size: 173883
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

# KoViDoRe - MIR v1.0

This dataset is part of the **KoViDoRe Benchmark** for Korean visual document retrieval evaluation. Specifically, it is focused on **Multimodal Information Retrieval (MIR) tasks** for Korean document images.

## Dataset Summary

- **Domain:** Korean public/official document images (e.g., 보고서, 통계자료, 정책자료 등)
- **Task:** Multimodal Information Retrieval (text query → relevant document image)
- **Format:** BEIR-compatible (corpus, queries, qrels)

**Statistics:**
- Number of Documents (Pages): **1,370+**
- Number of Queries: **1,500**
- Number of Relevance Judgments (qrels): **1,500**
- All text queries are in Korean.

## Dataset Structure

- **corpus**
  - `corpus-id`: Unique page ID
  - `image`: Document page image (PIL Image)
  - `publisher`: Publisher/기관명 (e.g., 한국은행, 예산정책처 등)
- **queries**
  - `query-id`: Unique query ID
  - `query`: Korean text question
- **qrels**
  - `query-id`
  - `corpus-id`
  - `score`: (1 = relevant)

## Usage

This dataset is intended for benchmarking the performance of multimodal retrieval systems on real-world Korean document images.

**Note:**  
Due to licensing restrictions, **original images are not redistributed with this dataset.  
Please download the required image data directly from [AI Hub](https://www.aihub.or.kr/) (멀티모달 정보검색 데이터) and place them as instructed in the [KoVidore-benchmark GitHub](https://github.com/whybe-choi/KoVidore-benchmark) repository.**

## Acknowledgments

- Based on data provided by [AI Hub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71813) (멀티모달 정보검색 데이터)

---
