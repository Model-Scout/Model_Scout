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
    num_bytes: 1158662136.21
    num_examples: 1415
  download_size: 1061840775
  dataset_size: 1158662136.21
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
    num_bytes: 9632
    num_examples: 224
  download_size: 3850
  dataset_size: 9632
- config_name: queries
  features:
  - name: query-id
    dtype: int64
  - name: query
    dtype: string
  splits:
  - name: test
    num_bytes: 17177
    num_examples: 180
  download_size: 11520
  dataset_size: 17177
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

# KoViDoRe - Slide v1.0

This dataset is part of the **KoViDoRe Benchmark** for Korean visual document retrieval evaluation. Specifically, it is focused on **presentation slides** for text-to-image retrieval tasks.

## Dataset Summary

- **Domain:** Korean presentation slides (e.g., 강의자료, 발표자료 등)
- **Task:** Visual document retrieval (text query → relevant slide image)
- **Format:** BEIR-compatible (corpus, queries, qrels)

**Statistics:**
- Number of Documents (Pages): **1,415**
- Number of Queries: **180**
- Number of Relevance Judgments (qrels): **224**
- All text queries are in Korean.

## Dataset Structure

- **corpus**
  - `corpus-id`: Unique page ID
  - `image`: Slide image (PIL Image)
  - `title`: Slide or presentation title
- **queries**
  - `query-id`: Unique query ID
  - `query`: Korean text question
- **qrels**
  - `query-id`
  - `corpus-id`
  - `score`: (1 = relevant)

## Usage

This dataset is intended for benchmarking the performance of visual document retrieval systems on real-world Korean presentation slides.

**Note:**  
Due to licensing restrictions, **original images are not redistributed with this dataset.  
Please download the required image data directly from [AI Hub](https://www.aihub.or.kr/) (오피스 문서 생성 데이터) and place them as instructed in the [KoViDoRe-benchmark GitHub](https://github.com/whybe-choi/KoViDoRe-benchmark) repository.**

## Acknowledgments

- Based on data provided by [AI Hub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=684) (오피스 문서 생성 데이터)

---