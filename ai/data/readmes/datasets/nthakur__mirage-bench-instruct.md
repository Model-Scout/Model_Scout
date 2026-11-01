---
dataset_info:
- config_name: ar
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 20828330
    num_examples: 3468
  download_size: 7516856
  dataset_size: 20828330
- config_name: bn
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 15196916
    num_examples: 1624
  download_size: 4533801
  dataset_size: 15196916
- config_name: en
  features:
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 14581495
    num_examples: 2857
  download_size: 6213852
  dataset_size: 14581495
- config_name: es
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 15930492
    num_examples: 2159
  download_size: 6833806
  dataset_size: 15930492
- config_name: fa
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 13879019
    num_examples: 2104
  download_size: 4713397
  dataset_size: 13879019
- config_name: fi
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 10642901
    num_examples: 2878
  download_size: 4508999
  dataset_size: 10642901
- config_name: fr
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 6103741
    num_examples: 1137
  download_size: 2438471
  dataset_size: 6103741
- config_name: hi
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 10311165
    num_examples: 1165
  download_size: 3002114
  dataset_size: 10311165
- config_name: id
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 20301218
    num_examples: 4054
  download_size: 8473237
  dataset_size: 20301218
- config_name: ja
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 15556155
    num_examples: 3466
  download_size: 6458296
  dataset_size: 15556155
- config_name: ko
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 3701188
    num_examples: 859
  download_size: 1505181
  dataset_size: 3701188
- config_name: ru
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 26992128
    num_examples: 4567
  download_size: 10814861
  dataset_size: 26992128
- config_name: sw
  features:
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 5170161
    num_examples: 1866
  download_size: 1942287
  dataset_size: 5170161
- config_name: te
  features:
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 14923000
    num_examples: 3283
  download_size: 4343650
  dataset_size: 14923000
- config_name: th
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: string
  splits:
  - name: train
    num_bytes: 20658813
    num_examples: 2965
  download_size: 6004933
  dataset_size: 20658813
- config_name: zh
  features:
  - name: prompt
    dtype: string
  - name: query_id
    dtype: string
  - name: positive_ids
    sequence: string
  - name: negative_ids
    sequence: 'null'
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: output
      dtype: string
  - name: tydiqa_answer
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 5756474
    num_examples: 1311
  download_size: 2530571
  dataset_size: 5756474
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: bn
  data_files:
  - split: train
    path: bn/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fa
  data_files:
  - split: train
    path: fa/train-*
- config_name: fi
  data_files:
  - split: train
    path: fi/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
- config_name: id
  data_files:
  - split: train
    path: id/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: sw
  data_files:
  - split: train
    path: sw/train-*
- config_name: te
  data_files:
  - split: train
    path: te/train-*
- config_name: th
  data_files:
  - split: train
    path: th/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
license: apache-2.0
task_categories:
- sentence-similarity
language:
- ar
- bn
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
- zh
pretty_name: MIRAGE-Bench Instruct
size_categories:
- 10K<n<100K
---

# MIRAGE-Bench (Instruct)

This dataset contains the structured RAG outputs for queries in the `train` split of MIRAGE-Bench (or MIRACL) for 16 languages for five models:
1. `gpt-4o-azure`                          (GPT-4o using Azure API)
2. `meta-llama/Meta-Llama-3-70B-Instruct`  (Llama-3-70B-Instruct using Anyscale API)
3. `mistralai/Mixtral-8x22B-Instruct-v0.1` (Mixtral-8x22B-Instruct using Anyscale API)
4. `meta-llama/Meta-Llama-3-8B-Instruct`   (Llama-3-8B-Instruct using vLLM)
5. `mistralai/Mistral-7B-Instruct-v0.2`    (Mistral-7B-Instruct using vLLM) 

> The answers have been generated using only the relevant positive passages (ground truth) + query and an instruction-following prompt.