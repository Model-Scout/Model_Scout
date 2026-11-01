---
configs:
- config_name: corpus
  data_files:
  - split: NanoArguAna
    path: corpus/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: corpus/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: corpus/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: corpus/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: corpus/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: corpus/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: corpus/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: corpus/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: corpus/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: corpus/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: corpus/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: corpus/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: corpus/NanoTouche2020-00000-of-00001.parquet
- config_name: queries
  data_files:
  - split: NanoArguAna
    path: queries/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: queries/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: queries/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: queries/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: queries/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: queries/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: queries/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: queries/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: queries/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: queries/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: queries/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: queries/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: queries/NanoTouche2020-00000-of-00001.parquet
  default: true
- config_name: qrels
  data_files:
  - split: NanoArguAna
    path: qrels/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: qrels/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: qrels/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: qrels/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: qrels/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: qrels/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: qrels/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: qrels/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: qrels/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: qrels/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: qrels/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: qrels/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: qrels/NanoTouche2020-00000-of-00001.parquet
- config_name: bm25
  data_files:
  - split: NanoArguAna
    path: bm25/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: bm25/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: bm25/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: bm25/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: bm25/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: bm25/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: bm25/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: bm25/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: bm25/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: bm25/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: bm25/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: bm25/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: bm25/NanoTouche2020-00000-of-00001.parquet
- config_name: harrier_oss_v1_270m
  data_files:
  - split: NanoArguAna
    path: harrier_oss_v1_270m/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: harrier_oss_v1_270m/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: harrier_oss_v1_270m/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: harrier_oss_v1_270m/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: harrier_oss_v1_270m/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: harrier_oss_v1_270m/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: harrier_oss_v1_270m/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: harrier_oss_v1_270m/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: harrier_oss_v1_270m/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: harrier_oss_v1_270m/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: harrier_oss_v1_270m/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: harrier_oss_v1_270m/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: harrier_oss_v1_270m/NanoTouche2020-00000-of-00001.parquet
- config_name: reranking_hybrid
  data_files:
  - split: NanoArguAna
    path: reranking_hybrid/NanoArguAna-00000-of-00001.parquet
  - split: NanoClimateFEVER
    path: reranking_hybrid/NanoClimateFEVER-00000-of-00001.parquet
  - split: NanoDBPedia
    path: reranking_hybrid/NanoDBPedia-00000-of-00001.parquet
  - split: NanoFEVER
    path: reranking_hybrid/NanoFEVER-00000-of-00001.parquet
  - split: NanoFiQA2018
    path: reranking_hybrid/NanoFiQA2018-00000-of-00001.parquet
  - split: NanoHotpotQA
    path: reranking_hybrid/NanoHotpotQA-00000-of-00001.parquet
  - split: NanoMSMARCO
    path: reranking_hybrid/NanoMSMARCO-00000-of-00001.parquet
  - split: NanoNFCorpus
    path: reranking_hybrid/NanoNFCorpus-00000-of-00001.parquet
  - split: NanoNQ
    path: reranking_hybrid/NanoNQ-00000-of-00001.parquet
  - split: NanoQuoraRetrieval
    path: reranking_hybrid/NanoQuoraRetrieval-00000-of-00001.parquet
  - split: NanoSCIDOCS
    path: reranking_hybrid/NanoSCIDOCS-00000-of-00001.parquet
  - split: NanoSciFact
    path: reranking_hybrid/NanoSciFact-00000-of-00001.parquet
  - split: NanoTouche2020
    path: reranking_hybrid/NanoTouche2020-00000-of-00001.parquet
language:
- ko
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
  - name: NanoArguAna
    num_bytes: 969162
    num_examples: 50
  - name: NanoClimateFEVER
    num_bytes: 596033
    num_examples: 50
  - name: NanoDBPedia
    num_bytes: 874496
    num_examples: 50
  - name: NanoFEVER
    num_bytes: 592808
    num_examples: 50
  - name: NanoFiQA2018
    num_bytes: 246063
    num_examples: 50
  - name: NanoHotpotQA
    num_bytes: 288791
    num_examples: 50
  - name: NanoMSMARCO
    num_bytes: 273333
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 300195
    num_examples: 50
  - name: NanoNQ
    num_bytes: 336389
    num_examples: 50
  - name: NanoQuoraRetrieval
    num_bytes: 244506
    num_examples: 50
  - name: NanoSCIDOCS
    num_bytes: 1102400
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 290703
    num_examples: 50
  - name: NanoTouche2020
    num_bytes: 1052427
    num_examples: 49
  download_size: 7185582
  dataset_size: 7167287
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: NanoArguAna
    num_bytes: 4495539
    num_examples: 3635
  - name: NanoClimateFEVER
    num_bytes: 6185771
    num_examples: 3408
  - name: NanoDBPedia
    num_bytes: 2755486
    num_examples: 6045
  - name: NanoFEVER
    num_bytes: 7383924
    num_examples: 4996
  - name: NanoFiQA2018
    num_bytes: 5302620
    num_examples: 4598
  - name: NanoHotpotQA
    num_bytes: 2300632
    num_examples: 5090
  - name: NanoMSMARCO
    num_bytes: 2033768
    num_examples: 5043
  - name: NanoNFCorpus
    num_bytes: 4982616
    num_examples: 2953
  - name: NanoNQ
    num_bytes: 3256050
    num_examples: 5035
  - name: NanoQuoraRetrieval
    num_bytes: 467577
    num_examples: 5046
  - name: NanoSCIDOCS
    num_bytes: 2416277
    num_examples: 2210
  - name: NanoSciFact
    num_bytes: 4737764
    num_examples: 2919
  - name: NanoTouche2020
    num_bytes: 14124391
    num_examples: 5745
  download_size: 34208947
  dataset_size: 60442415
- config_name: harrier_oss_v1_270m
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: NanoArguAna
    num_bytes: 968870
    num_examples: 50
  - name: NanoClimateFEVER
    num_bytes: 632552
    num_examples: 50
  - name: NanoDBPedia
    num_bytes: 870622
    num_examples: 50
  - name: NanoFEVER
    num_bytes: 585535
    num_examples: 50
  - name: NanoFiQA2018
    num_bytes: 245703
    num_examples: 50
  - name: NanoHotpotQA
    num_bytes: 289430
    num_examples: 50
  - name: NanoMSMARCO
    num_bytes: 272604
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 299676
    num_examples: 50
  - name: NanoNQ
    num_bytes: 336776
    num_examples: 50
  - name: NanoQuoraRetrieval
    num_bytes: 244217
    num_examples: 50
  - name: NanoSCIDOCS
    num_bytes: 1102400
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 290888
    num_examples: 50
  - name: NanoTouche2020
    num_bytes: 1052550
    num_examples: 49
  download_size: 7210251
  dataset_size: 7191823
- config_name: qrels
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  splits:
  - name: NanoArguAna
    num_bytes: 3496
    num_examples: 50
  - name: NanoClimateFEVER
    num_bytes: 4361
    num_examples: 148
  - name: NanoDBPedia
    num_bytes: 60640
    num_examples: 1158
  - name: NanoFEVER
    num_bytes: 1630
    num_examples: 57
  - name: NanoFiQA2018
    num_bytes: 2200
    num_examples: 123
  - name: NanoHotpotQA
    num_bytes: 3885
    num_examples: 100
  - name: NanoMSMARCO
    num_bytes: 1065
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 64851
    num_examples: 2518
  - name: NanoNQ
    num_bytes: 1340
    num_examples: 57
  - name: NanoQuoraRetrieval
    num_bytes: 1359
    num_examples: 70
  - name: NanoSCIDOCS
    num_bytes: 21472
    num_examples: 244
  - name: NanoSciFact
    num_bytes: 1054
    num_examples: 56
  - name: NanoTouche2020
    num_bytes: 45452
    num_examples: 932
  download_size: 88208
  dataset_size: 190263
- config_name: queries
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: NanoArguAna
    num_bytes: 73164
    num_examples: 50
  - name: NanoClimateFEVER
    num_bytes: 8480
    num_examples: 50
  - name: NanoDBPedia
    num_bytes: 3160
    num_examples: 50
  - name: NanoFEVER
    num_bytes: 3798
    num_examples: 50
  - name: NanoFiQA2018
    num_bytes: 4200
    num_examples: 50
  - name: NanoHotpotQA
    num_bytes: 7405
    num_examples: 50
  - name: NanoMSMARCO
    num_bytes: 3009
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 2255
    num_examples: 50
  - name: NanoNQ
    num_bytes: 4182
    num_examples: 50
  - name: NanoQuoraRetrieval
    num_bytes: 4178
    num_examples: 50
  - name: NanoSCIDOCS
    num_bytes: 6235
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 6032
    num_examples: 50
  - name: NanoTouche2020
    num_bytes: 3170
    num_examples: 49
  download_size: 111013
  dataset_size: 129268
- config_name: reranking_hybrid
  features:
  - name: query-id
    dtype: string
  - name: corpus-ids
    list: string
  splits:
  - name: NanoArguAna
    num_bytes: 193458
    num_examples: 50
  - name: NanoClimateFEVER
    num_bytes: 132082
    num_examples: 50
  - name: NanoDBPedia
    num_bytes: 178704
    num_examples: 50
  - name: NanoFEVER
    num_bytes: 120617
    num_examples: 50
  - name: NanoFiQA2018
    num_bytes: 49694
    num_examples: 50
  - name: NanoHotpotQA
    num_bytes: 59007
    num_examples: 50
  - name: NanoMSMARCO
    num_bytes: 55163
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 60686
    num_examples: 50
  - name: NanoNQ
    num_bytes: 67880
    num_examples: 50
  - name: NanoQuoraRetrieval
    num_bytes: 49387
    num_examples: 50
  - name: NanoSCIDOCS
    num_bytes: 222444
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 58699
    num_examples: 50
  - name: NanoTouche2020
    num_bytes: 210883
    num_examples: 49
  download_size: 1476357
  dataset_size: 1458705
---
# NanoBEIR-ko

This dataset is a Nano-style retrieval dataset for [HAKARI-bench](https://github.com/hakari-bench/hakari-bench).

NanoBEIR-ko is the Korean language-specific component of MNanoBEIR. It groups compact BEIR-derived retrieval tasks for efficient evaluation of document ranking in that language.

## Usage

```python
from datasets import load_dataset

dataset_id = "hakari-bench/NanoBEIR-ko"
split = "NanoArguAna"

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

Each config has the same Nano split names. `NanoNFCorpus` includes the full positive qrels (2,518 rows); qrels are not capped to the top-100 reranking depth.

## Candidate Construction

- `bm25`: local BM25 top-500 with automatic tokenizer selection. Auto mode uses `wordseg` for `ja`, `zh`, `th`, `ko`, and `vi`, and `regex` otherwise. The resolved tokenizer is shown for each split in the Candidate Quality table.
- `harrier_oss_v1_270m`: dense top-500 from `microsoft/harrier-oss-v1-270m`. In tables this is shown as `Dense`; Dense means `microsoft/harrier-oss-v1-270m` with the `web_search_query` prompt for queries and cosine similarity over normalized embeddings.
- `reranking_hybrid`: RRF over `bm25` and `harrier_oss_v1_270m` using `rrf_k=100`, keeping the RRF top-100.

Safeguard means rank 101 is appended only when RRF top-100 contains no qrels-positive document. Qrels are not capped to fit the top-100 reranking depth. For `NanoNFCorpus`, some queries have more than 100 positive qrels, so top-100 hybrid candidate coverage is expected to be below 100%; this is a candidate-list diagnostic, not a qrels filtering rule.

## Split Statistics

Length statistics are character counts computed with `len(str(text))`.

| Nano split | Queries | Corpus | Qrels | Query chars avg | Query chars p50 | Query chars p75 | Doc chars avg | Doc chars p50 | Doc chars p75 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NanoArguAna | 50 | 3635 | 50 | 619.4 | 604.0 | 768.2 | 519.6 | 464.0 | 659.5 |
| NanoClimateFEVER | 50 | 3408 | 148 | 66.0 | 64.5 | 82.8 | 779.7 | 704.0 | 1005.0 |
| NanoDBPedia | 50 | 6045 | 1158 | 16.8 | 15.5 | 21.8 | 187.6 | 198.0 | 244.0 |
| NanoFEVER | 50 | 4996 | 57 | 26.4 | 25.0 | 29.0 | 648.1 | 551.5 | 870.0 |
| NanoFiQA2018 | 50 | 4598 | 123 | 29.6 | 29.5 | 36.8 | 490.3 | 361.0 | 622.8 |
| NanoHotpotQA | 50 | 5090 | 100 | 49.5 | 46.0 | 59.8 | 197.1 | 170.0 | 269.0 |
| NanoMSMARCO | 50 | 5043 | 50 | 19.1 | 17.0 | 23.8 | 169.2 | 152.0 | 202.5 |
| NanoNFCorpus | 50 | 2953 | 2518 | 10.8 | 10.0 | 14.8 | 752.7 | 758.0 | 895.0 |
| NanoNQ | 50 | 5035 | 57 | 29.3 | 25.0 | 31.8 | 274.2 | 231.0 | 394.5 |
| NanoQuoraRetrieval | 50 | 5046 | 70 | 28.7 | 28.0 | 32.0 | 32.8 | 28.0 | 37.0 |
| NanoSCIDOCS | 50 | 2210 | 244 | 32.1 | 30.0 | 39.0 | 452.8 | 444.0 | 609.8 |
| NanoSciFact | 50 | 2919 | 56 | 46.3 | 42.0 | 59.2 | 723.6 | 679.0 | 869.0 |
| NanoTouche2020 | 49 | 5745 | 932 | 21.7 | 20.0 | 26.0 | 1032.8 | 543.0 | 1629.0 |

## Candidate Quality

`nDCG@10` and `Recall@100` are computed from the included candidate rankings against the included qrels, then reported as 0-100 scores such as `52.45`. `Recall@100` uses only the top 100 candidates; an optional rank-101 safeguard positive is not counted in `Recall@100`.

Dense means `microsoft/harrier-oss-v1-270m` with the `web_search_query` prompt and cosine similarity.

| Nano split | BM25 tokenizer | BM25 nDCG@10 | Dense nDCG@10 | Hybrid nDCG@10 | BM25 Recall@100 | Dense Recall@100 | Hybrid Recall@100 | Hybrid candidates | Safeguard positives |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mean | - | 44.99 | 50.02 | 50.47 | 74.95 | 78.50 | 81.34 | - | 31 |
| NanoArguAna | wordseg@ko | 36.61 | 40.82 | 42.17 | 90.00 | 94.00 | 96.00 | 100-101 | 2 |
| NanoClimateFEVER | wordseg@ko | 24.57 | 30.03 | 29.83 | 63.87 | 68.30 | 66.10 | 100-101 | 3 |
| NanoDBPedia | wordseg@ko | 53.22 | 59.28 | 57.87 | 72.53 | 76.53 | 79.55 | 100 | 0 |
| NanoFEVER | wordseg@ko | 57.23 | 73.35 | 70.01 | 92.00 | 98.33 | 99.00 | 100 | 0 |
| NanoFiQA2018 | wordseg@ko | 34.15 | 37.13 | 42.91 | 60.57 | 74.03 | 73.29 | 100-101 | 7 |
| NanoHotpotQA | wordseg@ko | 59.66 | 62.69 | 63.16 | 87.00 | 84.00 | 93.00 | 100-101 | 2 |
| NanoMSMARCO | wordseg@ko | 33.20 | 41.64 | 43.71 | 88.00 | 96.00 | 96.00 | 100-101 | 2 |
| NanoNFCorpus | wordseg@ko | 27.19 | 25.15 | 27.45 | 17.45 | 20.08 | 23.38 | 100-101 | 9 |
| NanoNQ | wordseg@ko | 43.01 | 58.05 | 50.33 | 78.00 | 93.00 | 99.00 | 100 | 0 |
| NanoQuoraRetrieval | wordseg@ko | 70.62 | 81.33 | 76.32 | 97.33 | 96.00 | 100.00 | 100 | 0 |
| NanoSCIDOCS | wordseg@ko | 26.73 | 33.10 | 33.80 | 60.93 | 64.17 | 64.27 | 100-101 | 1 |
| NanoSciFact | wordseg@ko | 68.35 | 62.07 | 68.38 | 92.00 | 84.00 | 90.00 | 100-101 | 5 |
| NanoTouche2020 | wordseg@ko | 50.33 | 45.64 | 50.13 | 74.71 | 72.08 | 77.89 | 100 | 0 |

## Hybrid Safeguard Summary

- Safeguard positives: 31
- Rows limited by corpus size: 0
- Metadata file: `reranking_hybrid_metadata.json`

## Source Links

- Original dataset: [LiquidAI/NanoBEIR-ko](https://huggingface.co/datasets/LiquidAI/NanoBEIR-ko)
- Final dataset: [hakari-bench/NanoBEIR-ko](https://huggingface.co/datasets/hakari-bench/NanoBEIR-ko)

## License

NanoBEIR-ko is a derived dataset. Users must comply with the licenses,
terms, and attribution requirements of the upstream source datasets.
