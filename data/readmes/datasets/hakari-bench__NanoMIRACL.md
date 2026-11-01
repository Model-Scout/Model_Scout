---
configs:
- config_name: corpus
  data_files:
  - split: ar
    path: corpus/ar-00000-of-00001.parquet
  - split: bn
    path: corpus/bn-00000-of-00001.parquet
  - split: de
    path: corpus/de-00000-of-00001.parquet
  - split: en
    path: corpus/en-00000-of-00001.parquet
  - split: es
    path: corpus/es-00000-of-00001.parquet
  - split: fa
    path: corpus/fa-00000-of-00001.parquet
  - split: fi
    path: corpus/fi-00000-of-00001.parquet
  - split: fr
    path: corpus/fr-00000-of-00001.parquet
  - split: hi
    path: corpus/hi-00000-of-00001.parquet
  - split: id
    path: corpus/id-00000-of-00001.parquet
  - split: ja
    path: corpus/ja-00000-of-00001.parquet
  - split: ko
    path: corpus/ko-00000-of-00001.parquet
  - split: ru
    path: corpus/ru-00000-of-00001.parquet
  - split: sw
    path: corpus/sw-00000-of-00001.parquet
  - split: te
    path: corpus/te-00000-of-00001.parquet
  - split: th
    path: corpus/th-00000-of-00001.parquet
  - split: yo
    path: corpus/yo-00000-of-00001.parquet
  - split: zh
    path: corpus/zh-00000-of-00001.parquet
- config_name: queries
  data_files:
  - split: ar
    path: queries/ar-00000-of-00001.parquet
  - split: bn
    path: queries/bn-00000-of-00001.parquet
  - split: de
    path: queries/de-00000-of-00001.parquet
  - split: en
    path: queries/en-00000-of-00001.parquet
  - split: es
    path: queries/es-00000-of-00001.parquet
  - split: fa
    path: queries/fa-00000-of-00001.parquet
  - split: fi
    path: queries/fi-00000-of-00001.parquet
  - split: fr
    path: queries/fr-00000-of-00001.parquet
  - split: hi
    path: queries/hi-00000-of-00001.parquet
  - split: id
    path: queries/id-00000-of-00001.parquet
  - split: ja
    path: queries/ja-00000-of-00001.parquet
  - split: ko
    path: queries/ko-00000-of-00001.parquet
  - split: ru
    path: queries/ru-00000-of-00001.parquet
  - split: sw
    path: queries/sw-00000-of-00001.parquet
  - split: te
    path: queries/te-00000-of-00001.parquet
  - split: th
    path: queries/th-00000-of-00001.parquet
  - split: yo
    path: queries/yo-00000-of-00001.parquet
  - split: zh
    path: queries/zh-00000-of-00001.parquet
  default: true
- config_name: qrels
  data_files:
  - split: ar
    path: qrels/ar-00000-of-00001.parquet
  - split: bn
    path: qrels/bn-00000-of-00001.parquet
  - split: de
    path: qrels/de-00000-of-00001.parquet
  - split: en
    path: qrels/en-00000-of-00001.parquet
  - split: es
    path: qrels/es-00000-of-00001.parquet
  - split: fa
    path: qrels/fa-00000-of-00001.parquet
  - split: fi
    path: qrels/fi-00000-of-00001.parquet
  - split: fr
    path: qrels/fr-00000-of-00001.parquet
  - split: hi
    path: qrels/hi-00000-of-00001.parquet
  - split: id
    path: qrels/id-00000-of-00001.parquet
  - split: ja
    path: qrels/ja-00000-of-00001.parquet
  - split: ko
    path: qrels/ko-00000-of-00001.parquet
  - split: ru
    path: qrels/ru-00000-of-00001.parquet
  - split: sw
    path: qrels/sw-00000-of-00001.parquet
  - split: te
    path: qrels/te-00000-of-00001.parquet
  - split: th
    path: qrels/th-00000-of-00001.parquet
  - split: yo
    path: qrels/yo-00000-of-00001.parquet
  - split: zh
    path: qrels/zh-00000-of-00001.parquet
- config_name: bm25
  data_files:
  - split: ar
    path: bm25/ar-00000-of-00001.parquet
  - split: bn
    path: bm25/bn-00000-of-00001.parquet
  - split: de
    path: bm25/de-00000-of-00001.parquet
  - split: en
    path: bm25/en-00000-of-00001.parquet
  - split: es
    path: bm25/es-00000-of-00001.parquet
  - split: fa
    path: bm25/fa-00000-of-00001.parquet
  - split: fi
    path: bm25/fi-00000-of-00001.parquet
  - split: fr
    path: bm25/fr-00000-of-00001.parquet
  - split: hi
    path: bm25/hi-00000-of-00001.parquet
  - split: id
    path: bm25/id-00000-of-00001.parquet
  - split: ja
    path: bm25/ja-00000-of-00001.parquet
  - split: ko
    path: bm25/ko-00000-of-00001.parquet
  - split: ru
    path: bm25/ru-00000-of-00001.parquet
  - split: sw
    path: bm25/sw-00000-of-00001.parquet
  - split: te
    path: bm25/te-00000-of-00001.parquet
  - split: th
    path: bm25/th-00000-of-00001.parquet
  - split: yo
    path: bm25/yo-00000-of-00001.parquet
  - split: zh
    path: bm25/zh-00000-of-00001.parquet
- config_name: harrier_oss_v1_270m
  data_files:
  - split: ar
    path: harrier_oss_v1_270m/ar-00000-of-00001.parquet
  - split: bn
    path: harrier_oss_v1_270m/bn-00000-of-00001.parquet
  - split: de
    path: harrier_oss_v1_270m/de-00000-of-00001.parquet
  - split: en
    path: harrier_oss_v1_270m/en-00000-of-00001.parquet
  - split: es
    path: harrier_oss_v1_270m/es-00000-of-00001.parquet
  - split: fa
    path: harrier_oss_v1_270m/fa-00000-of-00001.parquet
  - split: fi
    path: harrier_oss_v1_270m/fi-00000-of-00001.parquet
  - split: fr
    path: harrier_oss_v1_270m/fr-00000-of-00001.parquet
  - split: hi
    path: harrier_oss_v1_270m/hi-00000-of-00001.parquet
  - split: id
    path: harrier_oss_v1_270m/id-00000-of-00001.parquet
  - split: ja
    path: harrier_oss_v1_270m/ja-00000-of-00001.parquet
  - split: ko
    path: harrier_oss_v1_270m/ko-00000-of-00001.parquet
  - split: ru
    path: harrier_oss_v1_270m/ru-00000-of-00001.parquet
  - split: sw
    path: harrier_oss_v1_270m/sw-00000-of-00001.parquet
  - split: te
    path: harrier_oss_v1_270m/te-00000-of-00001.parquet
  - split: th
    path: harrier_oss_v1_270m/th-00000-of-00001.parquet
  - split: yo
    path: harrier_oss_v1_270m/yo-00000-of-00001.parquet
  - split: zh
    path: harrier_oss_v1_270m/zh-00000-of-00001.parquet
- config_name: reranking_hybrid
  data_files:
  - split: ar
    path: reranking_hybrid/ar-00000-of-00001.parquet
  - split: bn
    path: reranking_hybrid/bn-00000-of-00001.parquet
  - split: de
    path: reranking_hybrid/de-00000-of-00001.parquet
  - split: en
    path: reranking_hybrid/en-00000-of-00001.parquet
  - split: es
    path: reranking_hybrid/es-00000-of-00001.parquet
  - split: fa
    path: reranking_hybrid/fa-00000-of-00001.parquet
  - split: fi
    path: reranking_hybrid/fi-00000-of-00001.parquet
  - split: fr
    path: reranking_hybrid/fr-00000-of-00001.parquet
  - split: hi
    path: reranking_hybrid/hi-00000-of-00001.parquet
  - split: id
    path: reranking_hybrid/id-00000-of-00001.parquet
  - split: ja
    path: reranking_hybrid/ja-00000-of-00001.parquet
  - split: ko
    path: reranking_hybrid/ko-00000-of-00001.parquet
  - split: ru
    path: reranking_hybrid/ru-00000-of-00001.parquet
  - split: sw
    path: reranking_hybrid/sw-00000-of-00001.parquet
  - split: te
    path: reranking_hybrid/te-00000-of-00001.parquet
  - split: th
    path: reranking_hybrid/th-00000-of-00001.parquet
  - split: yo
    path: reranking_hybrid/yo-00000-of-00001.parquet
  - split: zh
    path: reranking_hybrid/zh-00000-of-00001.parquet
language:
- ar
- bn
- de
- en
- es
- fa
- fi
- fr
- hi
- id
- ja
- ko
- ru
- sw
- te
- th
- yo
- zh
tags:
- information-retrieval
- retrieval
- nano
- bm25
- hakari-bench
- dense-retrieval
- reranking
dataset_info:
- config_name: bm25
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: ar
    num_bytes: 1266611
    num_examples: 200
  - name: bn
    num_bytes: 1177519
    num_examples: 200
  - name: de
    num_bytes: 1298603
    num_examples: 200
  - name: en
    num_bytes: 1357970
    num_examples: 200
  - name: es
    num_bytes: 1288433
    num_examples: 200
  - name: fa
    num_bytes: 1262738
    num_examples: 200
  - name: fi
    num_bytes: 1218233
    num_examples: 200
  - name: fr
    num_bytes: 1309162
    num_examples: 200
  - name: hi
    num_bytes: 1208415
    num_examples: 200
  - name: id
    num_bytes: 1218449
    num_examples: 200
  - name: ja
    num_bytes: 1269008
    num_examples: 200
  - name: ko
    num_bytes: 1218171
    num_examples: 200
  - name: ru
    num_bytes: 1292152
    num_examples: 200
  - name: sw
    num_bytes: 1108061
    num_examples: 200
  - name: te
    num_bytes: 1161605
    num_examples: 200
  - name: th
    num_bytes: 1189537
    num_examples: 200
  - name: yo
    num_bytes: 657193
    num_examples: 119
  - name: zh
    num_bytes: 1263280
    num_examples: 200
  download_size: 21789444
  dataset_size: 21765140
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: ar
    num_bytes: 7174282
    num_examples: 10000
  - name: bn
    num_bytes: 12035077
    num_examples: 10000
  - name: de
    num_bytes: 4819401
    num_examples: 10000
  - name: en
    num_bytes: 4904869
    num_examples: 10000
  - name: es
    num_bytes: 4794294
    num_examples: 10000
  - name: fa
    num_bytes: 5768565
    num_examples: 10000
  - name: fi
    num_bytes: 4233118
    num_examples: 10000
  - name: fr
    num_bytes: 4151659
    num_examples: 10000
  - name: hi
    num_bytes: 10878177
    num_examples: 10000
  - name: id
    num_bytes: 4336884
    num_examples: 10000
  - name: ja
    num_bytes: 4982205
    num_examples: 10000
  - name: ko
    num_bytes: 4938423
    num_examples: 10000
  - name: ru
    num_bytes: 7807671
    num_examples: 10000
  - name: sw
    num_bytes: 2937176
    num_examples: 10000
  - name: te
    num_bytes: 10843968
    num_examples: 10000
  - name: th
    num_bytes: 11582202
    num_examples: 10000
  - name: yo
    num_bytes: 2330437
    num_examples: 10000
  - name: zh
    num_bytes: 3801244
    num_examples: 10000
  download_size: 59148256
  dataset_size: 112319652
- config_name: harrier_oss_v1_270m
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: ar
    num_bytes: 1273629
    num_examples: 200
  - name: bn
    num_bytes: 1176065
    num_examples: 200
  - name: de
    num_bytes: 1301028
    num_examples: 200
  - name: en
    num_bytes: 1363247
    num_examples: 200
  - name: es
    num_bytes: 1294926
    num_examples: 200
  - name: fa
    num_bytes: 1262210
    num_examples: 200
  - name: fi
    num_bytes: 1218495
    num_examples: 200
  - name: fr
    num_bytes: 1311982
    num_examples: 200
  - name: hi
    num_bytes: 1207316
    num_examples: 200
  - name: id
    num_bytes: 1224728
    num_examples: 200
  - name: ja
    num_bytes: 1272296
    num_examples: 200
  - name: ko
    num_bytes: 1217697
    num_examples: 200
  - name: ru
    num_bytes: 1293929
    num_examples: 200
  - name: sw
    num_bytes: 1110175
    num_examples: 200
  - name: te
    num_bytes: 1159682
    num_examples: 200
  - name: th
    num_bytes: 1196182
    num_examples: 200
  - name: yo
    num_bytes: 655592
    num_examples: 119
  - name: zh
    num_bytes: 1268069
    num_examples: 200
  download_size: 21831454
  dataset_size: 21807248
- config_name: qrels
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  splits:
  - name: ar
    num_bytes: 7267
    num_examples: 386
  - name: bn
    num_bytes: 7436
    num_examples: 407
  - name: de
    num_bytes: 13650
    num_examples: 538
  - name: en
    num_bytes: 11324
    num_examples: 560
  - name: es
    num_bytes: 23740
    num_examples: 934
  - name: fa
    num_bytes: 10577
    num_examples: 427
  - name: fi
    num_bytes: 6081
    num_examples: 328
  - name: fr
    num_bytes: 10612
    num_examples: 417
  - name: hi
    num_bytes: 9654
    num_examples: 410
  - name: id
    num_bytes: 12133
    num_examples: 654
  - name: ja
    num_bytes: 7131
    num_examples: 373
  - name: ko
    num_bytes: 9572
    num_examples: 508
  - name: ru
    num_bytes: 10750
    num_examples: 555
  - name: sw
    num_bytes: 7188
    num_examples: 405
  - name: te
    num_bytes: 3855
    num_examples: 211
  - name: th
    num_bytes: 6309
    num_examples: 343
  - name: yo
    num_bytes: 3143
    num_examples: 144
  - name: zh
    num_bytes: 11666
    num_examples: 471
  download_size: 122826
  dataset_size: 172088
- config_name: queries
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: ar
    num_bytes: 13271
    num_examples: 200
  - name: bn
    num_bytes: 27235
    num_examples: 200
  - name: de
    num_bytes: 12632
    num_examples: 200
  - name: en
    num_bytes: 10199
    num_examples: 200
  - name: es
    num_bytes: 13486
    num_examples: 200
  - name: fa
    num_bytes: 17958
    num_examples: 200
  - name: fi
    num_bytes: 9852
    num_examples: 200
  - name: fr
    num_bytes: 12361
    num_examples: 200
  - name: hi
    num_bytes: 31659
    num_examples: 200
  - name: id
    num_bytes: 9871
    num_examples: 200
  - name: ja
    num_bytes: 12505
    num_examples: 200
  - name: ko
    num_bytes: 13045
    num_examples: 200
  - name: ru
    num_bytes: 18950
    num_examples: 200
  - name: sw
    num_bytes: 9853
    num_examples: 200
  - name: te
    num_bytes: 22938
    num_examples: 200
  - name: th
    num_bytes: 27216
    num_examples: 200
  - name: yo
    num_bytes: 6697
    num_examples: 119
  - name: zh
    num_bytes: 9826
    num_examples: 200
  download_size: 183744
  dataset_size: 279554
- config_name: reranking_hybrid
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: ar
    num_bytes: 253968
    num_examples: 200
  - name: bn
    num_bytes: 236250
    num_examples: 200
  - name: de
    num_bytes: 261001
    num_examples: 200
  - name: en
    num_bytes: 272500
    num_examples: 200
  - name: es
    num_bytes: 259586
    num_examples: 200
  - name: fa
    num_bytes: 253821
    num_examples: 200
  - name: fi
    num_bytes: 244186
    num_examples: 200
  - name: fr
    num_bytes: 263592
    num_examples: 200
  - name: hi
    num_bytes: 242989
    num_examples: 200
  - name: id
    num_bytes: 242548
    num_examples: 200
  - name: ja
    num_bytes: 254284
    num_examples: 200
  - name: ko
    num_bytes: 244095
    num_examples: 200
  - name: ru
    num_bytes: 259305
    num_examples: 200
  - name: sw
    num_bytes: 223021
    num_examples: 200
  - name: te
    num_bytes: 234272
    num_examples: 200
  - name: th
    num_bytes: 239389
    num_examples: 200
  - name: yo
    num_bytes: 132452
    num_examples: 119
  - name: zh
    num_bytes: 254917
    num_examples: 200
  download_size: 4393763
  dataset_size: 4372176
---
# NanoMIRACL

This dataset is a Nano-style retrieval dataset for [HAKARI-bench](https://github.com/hakari-bench/hakari-bench).

NanoMIRACL is a compact multilingual benchmark derived from MIRACL. Each language split evaluates monolingual retrieval of Wikipedia passages for natural-language questions.

This rebuild uses `hotchpotch/miracl-hf-unified` dev queries at source revision `21ad00eb467639e927b5badb7c49f4947c6c24ca`. For each sampled query, it preserves all source positive passages and expands the split-local corpus to 10,000 documents using source negatives as hard-negative candidates plus deterministic random fill.

## Usage

```python
from datasets import load_dataset

dataset_id = "hakari-bench/NanoMIRACL"
split = "ar"

queries = load_dataset(dataset_id, "queries", split=split)
corpus = load_dataset(dataset_id, "corpus", split=split)
qrels = load_dataset(dataset_id, "qrels", split=split)
reranking_candidates = load_dataset(dataset_id, "reranking_hybrid", split=split)
```

## Data Layout

This dataset uses six Hugging Face Datasets configs:

- `corpus`: documents with `_id` and `text`
- `queries`: queries with `_id` and `text`
- `qrels`: positive relevance labels with `query-id` and `corpus-id`
- `bm25`: BM25 candidate lists with `query-id` and `corpus-ids`
- `harrier_oss_v1_270m`: dense candidate lists from `microsoft/harrier-oss-v1-270m`
- `reranking_hybrid`: RRF candidate lists built from `bm25` and `harrier_oss_v1_270m`

Each config has the same Nano split names.

## Candidate Construction

- `bm25`: local BM25 top-500 with automatic language-aware tokenization. The resolved tokenizer is shown in the Candidate Quality table, for example `wordseg@ja`.
- `harrier_oss_v1_270m`: dense top-500 from `microsoft/harrier-oss-v1-270m`. In tables this is shown as `Dense`; Dense means `microsoft/harrier-oss-v1-270m` with the `web_search_query` prompt for queries and cosine similarity over normalized embeddings.
- `reranking_hybrid`: RRF over `bm25` and `harrier_oss_v1_270m` using `rrf_k=100`, keeping the RRF top-100.

Safeguard means rank 101 is appended only when RRF top-100 contains no qrels-positive document.

## Split Statistics

Length statistics are character counts computed with `len(str(text))`.

| Nano split | Queries | Corpus | Qrels | Query chars avg | Query chars p50 | Query chars p75 | Doc chars avg | Doc chars p50 | Doc chars p75 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ar | 200 | 10000 | 386 | 30.1 | 27.0 | 35.0 | 392.3 | 276.0 | 520.0 |
| bn | 200 | 10000 | 407 | 47.2 | 43.5 | 58.0 | 446.2 | 359.0 | 597.0 |
| de | 200 | 10000 | 538 | 45.4 | 43.0 | 52.0 | 457.2 | 372.0 | 612.0 |
| en | 200 | 10000 | 560 | 39.9 | 37.5 | 48.0 | 471.8 | 392.0 | 645.0 |
| es | 200 | 10000 | 934 | 47.6 | 47.0 | 55.0 | 453.2 | 370.0 | 597.0 |
| fa | 200 | 10000 | 427 | 40.0 | 38.0 | 46.0 | 310.7 | 213.0 | 413.0 |
| fi | 200 | 10000 | 328 | 37.2 | 33.5 | 46.2 | 393.6 | 326.0 | 522.0 |
| fr | 200 | 10000 | 417 | 43.3 | 43.0 | 51.0 | 385.3 | 296.0 | 513.0 |
| hi | 200 | 10000 | 410 | 54.8 | 52.0 | 65.0 | 419.3 | 320.0 | 559.0 |
| id | 200 | 10000 | 654 | 38.3 | 37.0 | 45.0 | 416.5 | 316.0 | 567.0 |
| ja | 200 | 10000 | 373 | 17.5 | 17.0 | 21.0 | 173.4 | 135.0 | 231.0 |
| ko | 200 | 10000 | 508 | 21.7 | 19.0 | 22.0 | 205.3 | 163.0 | 273.0 |
| ru | 200 | 10000 | 555 | 45.5 | 41.0 | 53.5 | 423.3 | 313.0 | 569.0 |
| sw | 200 | 10000 | 405 | 38.3 | 37.0 | 44.0 | 278.0 | 204.0 | 338.0 |
| te | 200 | 10000 | 211 | 38.4 | 36.5 | 43.0 | 409.0 | 295.0 | 486.0 |
| th | 200 | 10000 | 343 | 43.6 | 40.0 | 50.2 | 409.9 | 346.0 | 538.0 |
| yo | 119 | 10000 | 144 | 37.7 | 36.0 | 42.0 | 176.7 | 81.0 | 187.0 |
| zh | 200 | 10000 | 471 | 10.9 | 11.0 | 12.0 | 133.4 | 105.0 | 176.0 |

## Candidate Quality

`nDCG@10` and `Recall@100` are computed from the included candidate rankings against the included qrels, then reported as 0-100 scores such as `52.45`. `Recall@100` uses only the top 100 candidates; an optional rank-101 safeguard positive is not counted in `Recall@100`.

Dense means `microsoft/harrier-oss-v1-270m` with the `web_search_query` prompt and cosine similarity.

| Nano split | BM25 tokenizer | BM25 nDCG@10 | Dense nDCG@10 | Hybrid nDCG@10 | BM25 Recall@100 | Dense Recall@100 | Hybrid Recall@100 | Hybrid candidates | Safeguard positives |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mean | - | 57.15 | 76.27 | 69.00 | 93.32 | 94.02 | 99.26 | - | 19 |
| ar | stemmer@arabic | 63.52 | 82.23 | 75.14 | 97.40 | 96.58 | 99.83 | 100 | 0 |
| bn | whitespace | 50.33 | 76.61 | 65.37 | 95.17 | 95.57 | 99.75 | 100 | 0 |
| de | stemmer@german | 51.72 | 73.89 | 64.18 | 91.78 | 93.10 | 98.27 | 100-101 | 1 |
| en | english_porter_stop | 67.74 | 77.21 | 74.74 | 99.38 | 95.00 | 99.75 | 100 | 0 |
| es | stemmer@spanish | 68.61 | 77.93 | 74.78 | 98.06 | 93.31 | 100.00 | 100 | 0 |
| fa | regex | 57.88 | 64.76 | 63.34 | 96.22 | 88.99 | 99.30 | 100-101 | 1 |
| fi | stemmer@finnish | 77.34 | 86.34 | 83.32 | 98.58 | 95.42 | 100.00 | 100 | 0 |
| fr | stemmer@french | 46.58 | 68.28 | 58.96 | 97.96 | 91.35 | 99.88 | 100 | 0 |
| hi | stemmer@hindi | 30.37 | 68.47 | 51.74 | 70.18 | 91.99 | 96.00 | 100-101 | 7 |
| id | stemmer@indonesian | 67.73 | 70.76 | 71.71 | 98.01 | 95.04 | 99.83 | 100 | 0 |
| ja | wordseg@ja | 66.01 | 77.45 | 72.23 | 97.33 | 91.78 | 100.00 | 100 | 0 |
| ko | wordseg@ko | 49.94 | 69.10 | 70.26 | 95.74 | 92.02 | 98.12 | 100-101 | 3 |
| ru | stemmer@russian | 58.87 | 76.93 | 68.16 | 89.50 | 93.20 | 98.43 | 100-101 | 3 |
| sw | regex | 58.52 | 78.72 | 72.92 | 94.89 | 94.95 | 99.75 | 100 | 0 |
| te | whitespace | 52.92 | 87.20 | 69.53 | 87.92 | 92.50 | 98.25 | 100-101 | 3 |
| th | wordseg@th | 62.29 | 81.01 | 72.96 | 95.58 | 95.25 | 99.50 | 100-101 | 1 |
| yo | regex | 58.16 | 84.16 | 76.51 | 92.44 | 97.48 | 100.00 | 100 | 0 |
| zh | wordseg@zh | 40.22 | 71.91 | 56.19 | 83.62 | 98.90 | 100.00 | 100 | 0 |

## Hybrid Safeguard Summary

- Safeguard positives: 19
- Rows limited by corpus size: 0
- Metadata file: `reranking_hybrid_metadata.json`

## Source Links

- [hotchpotch/miracl-hf-unified](https://huggingface.co/datasets/hotchpotch/miracl-hf-unified)
- [miracl/miracl](https://huggingface.co/datasets/miracl/miracl)
- [miracl/miracl-corpus](https://huggingface.co/datasets/miracl/miracl-corpus)

## License

NanoMIRACL is a derived dataset. Users must comply with the licenses,
terms, and attribution requirements of the upstream source datasets.
