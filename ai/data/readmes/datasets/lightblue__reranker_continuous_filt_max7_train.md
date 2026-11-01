---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: dataset_name
    dtype: string
  - name: language
    dtype: string
  - name: added_neg
    dtype: bool
  - name: doc_id
    sequence: string
  - name: added_doc_id
    dtype: bool
  - name: row_id
    dtype: int64
  - name: context
    dtype: string
  - name: label
    dtype: bool
  - name: 32B_score_probs
    sequence: float64
  - name: 32B_score_probs_rev
    sequence: float64
  - name: prob_exp_val
    dtype: float64
  - name: rev_prob_exp_val
    dtype: float64
  - name: mean_exp_val
    dtype: float64
  - name: mean_exp_val_max7
    dtype: float64
  - name: mean_exp_val_max7_round
    dtype: int64
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 8837477995.973139
    num_examples: 2283437
  download_size: 5621429093
  dataset_size: 8837477995.973139
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- en
- zh
- es
- de
- ar
- ru
- ja
- ko
- hi
- sk
- vi
- tr
- fi
- id
- fa
- no
- th
- sv
- pt
- da
- bn
- te
- ro
- it
- fr
- nl
- sw
- pl
- hu
- cs
- el
- uk
- mr
- ta
- tl
- bg
- lt
- ur
- he
- gu
- kn
- am
- kk
- hr
- uz
- jv
- ca
- az
- ms
- sr
- sl
- yo
- lv
- is
- ha
- ka
- et
- bs
- hy
- ml
- pa
- mt
- km
- sq
- or
- as
- my
- mn
- af
- be
- ga
- mk
- cy
- gl
- ceb
- la
- yi
- lb
- tg
- gd
- ne
- ps
- eu
- ky
- ku
- si
- ht
- eo
- lo
- fy
- sd
- mg
- so
- ckb
- su
- nn
---

# Reranker training data

This data was generated using 4 steps:

1. We gathered queries and corresponding text data from 35 high quality datasets covering more than 95 languages.
2. For datasets which did not already have negative texts for queries, we mined hard negatives using the [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) embedding model.
3. For each query, we selected one positive and one negative text and used [Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4) to rate the relatedness of each query-text pair using a token "1", "2", "3", "4", or "5".
4. Given the normalized token probabilities for each of the 5 tokens, we generated an expectation value of the score that the 32B model predicts for each pair, which we then normalize to a scale of 1-7 in order to add expressivity to our data (i.e. we stretch out our range from 1-5 to 1-7). We round these values to the nearest whole number (1-7) and the final value is listed in our `mean_exp_val_max7_round` column.

We make our data preparation code available [on our Github](https://github.com/lightblue-tech/lb-reranker/tree/main/data_prep).

### Data contents

The distribution of source datasets in this dataset:

<img src="https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/REO3MyOtEUdSmuDVYGHeX.png" alt="Dataset distributions" width="400"/>


The distribution of languages in this dataset:

<img src="https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/jpSZ5NUU4ObV-dEIT1ss4.png" alt="Language distributions" width="400"/>

# License

We have endeavoured to base our dataset only on source datasets which allow for fully free use. Therefore, we share this dataset with the Apache 2.0 license.

# Developed by

<a href="https://www.lightblue-tech.com">
<img src="https://www.lightblue-tech.com/wp-content/uploads/2023/08/color_%E6%A8%AA%E5%9E%8B-1536x469.png" alt="Lightblue technology logo" width="400"/>
</a>

This model was trained by Peter Devine ([ptrdvn](https://huggingface.co/ptrdvn)) for Lightblue