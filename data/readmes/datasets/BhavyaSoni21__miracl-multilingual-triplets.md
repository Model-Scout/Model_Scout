---
annotations_creators:
- expert-generated
- machine-generated
language_creators:
- found
- machine-generated
multilinguality:
- translation
language:
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fil
- fr
- gu
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- kn
- ko
- lt
- lv
- ml
- mr
- nl
- 'no'
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
- zu
license: apache-2.0
pretty_name: MIRACL Triplets in 51 Languages
size_categories:
- 100K<n<1M
source_datasets:
- extended|miracl/miracl
task_categories:
- text-ranking
- text-retrieval
- translation
tags:
- multilingual
- translation
- retrieval
- triplet
- synthetic
- miracl
- dense-retrieval
- sentence-transformers
- contrastive-learning
- cross-lingual
- parquet
- text
- datasets
- reranking
- reranker
- multilingual-reranking
- multilingual-retrieval
configs:
- config_name: en
  default: true
  data_files:
  - split: train
    path: dataset/miracl_en_triplet.parquet
- config_name: ar
  data_files:
  - split: train
    path: dataset/miracl_ar_triplet.parquet
- config_name: bg
  data_files:
  - split: train
    path: dataset/miracl_bg_triplet.parquet
- config_name: bn
  data_files:
  - split: train
    path: dataset/miracl_bn_triplet.parquet
- config_name: ca
  data_files:
  - split: train
    path: dataset/miracl_ca_triplet.parquet
- config_name: cs
  data_files:
  - split: train
    path: dataset/miracl_cs_triplet.parquet
- config_name: da
  data_files:
  - split: train
    path: dataset/miracl_da_triplet.parquet
- config_name: de
  data_files:
  - split: train
    path: dataset/miracl_de_triplet.parquet
- config_name: el
  data_files:
  - split: train
    path: dataset/miracl_el_triplet.parquet
- config_name: es
  data_files:
  - split: train
    path: dataset/miracl_es_triplet.parquet
- config_name: et
  data_files:
  - split: train
    path: dataset/miracl_et_triplet.parquet
- config_name: fa
  data_files:
  - split: train
    path: dataset/miracl_fa_triplet.parquet
- config_name: fi
  data_files:
  - split: train
    path: dataset/miracl_fi_triplet.parquet
- config_name: fil-PH
  data_files:
  - split: train
    path: dataset/miracl_fil-PH_triplet.parquet
- config_name: fr
  data_files:
  - split: train
    path: dataset/miracl_fr_triplet.parquet
- config_name: gu
  data_files:
  - split: train
    path: dataset/miracl_gu_triplet.parquet
- config_name: he
  data_files:
  - split: train
    path: dataset/miracl_he_triplet.parquet
- config_name: hi
  data_files:
  - split: train
    path: dataset/miracl_hi_triplet.parquet
- config_name: hr
  data_files:
  - split: train
    path: dataset/miracl_hr_triplet.parquet
- config_name: hu
  data_files:
  - split: train
    path: dataset/miracl_hu_triplet.parquet
- config_name: id
  data_files:
  - split: train
    path: dataset/miracl_id_triplet.parquet
- config_name: is
  data_files:
  - split: train
    path: dataset/miracl_is_triplet.parquet
- config_name: it
  data_files:
  - split: train
    path: dataset/miracl_it_triplet.parquet
- config_name: ja
  data_files:
  - split: train
    path: dataset/miracl_ja_triplet.parquet
- config_name: kn
  data_files:
  - split: train
    path: dataset/miracl_kn_triplet.parquet
- config_name: ko
  data_files:
  - split: train
    path: dataset/miracl_ko_triplet.parquet
- config_name: lt
  data_files:
  - split: train
    path: dataset/miracl_lt_triplet.parquet
- config_name: lv
  data_files:
  - split: train
    path: dataset/miracl_lv_triplet.parquet
- config_name: ml
  data_files:
  - split: train
    path: dataset/miracl_ml_triplet.parquet
- config_name: mr
  data_files:
  - split: train
    path: dataset/miracl_mr_triplet.parquet
- config_name: nl
  data_files:
  - split: train
    path: dataset/miracl_nl_triplet.parquet
- config_name: 'no'
  data_files:
  - split: train
    path: dataset/miracl_no_triplet.parquet
- config_name: pa
  data_files:
  - split: train
    path: dataset/miracl_pa_triplet.parquet
- config_name: pl
  data_files:
  - split: train
    path: dataset/miracl_pl_triplet.parquet
- config_name: pt
  data_files:
  - split: train
    path: dataset/miracl_pt_triplet.parquet
- config_name: ro
  data_files:
  - split: train
    path: dataset/miracl_ro_triplet.parquet
- config_name: ru
  data_files:
  - split: train
    path: dataset/miracl_ru_triplet.parquet
- config_name: sk
  data_files:
  - split: train
    path: dataset/miracl_sk_triplet.parquet
- config_name: sl
  data_files:
  - split: train
    path: dataset/miracl_sl_triplet.parquet
- config_name: sr
  data_files:
  - split: train
    path: dataset/miracl_sr_triplet.parquet
- config_name: sv
  data_files:
  - split: train
    path: dataset/miracl_sv_triplet.parquet
- config_name: sw
  data_files:
  - split: train
    path: dataset/miracl_sw_triplet.parquet
- config_name: ta
  data_files:
  - split: train
    path: dataset/miracl_ta_triplet.parquet
- config_name: te
  data_files:
  - split: train
    path: dataset/miracl_te_triplet.parquet
- config_name: th
  data_files:
  - split: train
    path: dataset/miracl_th_triplet.parquet
- config_name: tr
  data_files:
  - split: train
    path: dataset/miracl_tr_triplet.parquet
- config_name: uk
  data_files:
  - split: train
    path: dataset/miracl_uk_triplet.parquet
- config_name: ur
  data_files:
  - split: train
    path: dataset/miracl_ur_triplet.parquet
- config_name: vi
  data_files:
  - split: train
    path: dataset/miracl_vi_triplet.parquet
- config_name: zh
  data_files:
  - split: train
    path: dataset/miracl_zh_triplet.parquet
- config_name: zu
  data_files:
  - split: train
    path: dataset/miracl_zu_triplet.parquet
---

# MIRACL Triplets in 51 Languages

## Dataset Summary

MIRACL Triplets in 51 Languages is a multilingual retrieval and reranking dataset for training dense retrieval, sentence embedding, reranker, and cross-lingual search models. It contains `(query, positive, negative)` triplets derived from the English training split of [`miracl/miracl`](https://huggingface.co/datasets/miracl/miracl).

The dataset provides **51 language subsets**: the original English data and translations into 50 languages. Each subset contains **2,863 aligned training examples**. Rows with the same `id` represent translations of the same source triplet. The aligned `(query, positive, negative)` structure supports multilingual retrieval, multilingual reranking, contrastive learning, and hard-negative training.

- Format: Parquet
- Subsets: 51 language codes, including `en`, `ko`, `ja`, `zh`, `de`, and `fr`
- Split: `train`
- Rows per subset: 2,863
- Total rows across subsets: 146,013

## Data Structure

| Column | Type | Description |
|---|---|---|
| `id` | `int64` | Alignment identifier shared across language subsets |
| `query` | `string` | Search query |
| `positive` | `string` | Passage relevant to the query |
| `negative` | `string` | Passage not relevant to the query |

## Data Instances

Example from the English subset:

```json
{
  "id": 232,
  "query": "What is Nigers anthem?",
  "positive": "La Nigérienne\n\"La Nigérienne\" is the national anthem of Niger. The lyrics are by Maurice Albert Thiriet. Robert Jacquet and Nicolas Abel François Frionnet wrote the music. It was adopted as Niger's anthem in 1961.",
  "negative": "Nigeria, We Hail Thee\nThe second national anthem, \"Arise, O Compatriots,\" replaced \"Nigeria, We Hail Thee\" in 1978."
}
```

## How to Use

```python
from datasets import load_dataset

# Load one language subset. Replace "ko" with any supported language code.
dataset = load_dataset("nlpai-lab/miracl-multilingual-triplets", "ko", split="train")

print(dataset.features)
print(dataset[0])
```

The default subset is English (`en`).

## Source and Translation

- Source dataset: [`miracl/miracl`](https://huggingface.co/datasets/miracl/miracl)
- Source configuration: `en`
- Source split: `train`
- Translation model: [`google/translategemma-27b-it`](https://huggingface.co/google/translategemma-27b-it)

The model's original translation prompt template was used without modification or additional instructions. The `query`, `positive`, and `negative` fields were translated independently while preserving their triplet relationship and cross-language `id` alignment.

## Languages

| Code | Language | Code | Language |
|---|---|---|---|
| ar | Arabic | bg | Bulgarian |
| bn | Bengali | ca | Catalan |
| cs | Czech | da | Danish |
| de | German | el | Greek |
| en | English (source) | es | Spanish |
| et | Estonian | fa | Persian |
| fi | Finnish | fil-PH | Filipino |
| fr | French | gu | Gujarati |
| he | Hebrew | hi | Hindi |
| hr | Croatian | hu | Hungarian |
| id | Indonesian | is | Icelandic |
| it | Italian | ja | Japanese |
| kn | Kannada | ko | Korean |
| lt | Lithuanian | lv | Latvian |
| ml | Malayalam | mr | Marathi |
| nl | Dutch | no | Norwegian |
| pa | Punjabi | pl | Polish |
| pt | Portuguese | ro | Romanian |
| ru | Russian | sk | Slovak |
| sl | Slovenian | sr | Serbian |
| sv | Swedish | sw | Swahili |
| ta | Tamil | te | Telugu |
| th | Thai | tr | Turkish |
| uk | Ukrainian | ur | Urdu |
| vi | Vietnamese | zh | Chinese |
| zu | Zulu |  |  |

## License

The source MIRACL dataset is released under the Apache License 2.0. This derived dataset is also released under Apache-2.0.
