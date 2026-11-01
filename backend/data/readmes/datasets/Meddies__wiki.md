---
license: cc-by-sa-4.0
language:
- de
- en
- es
- fil
- fr
- id
- ja
- ko
- lo
- ms
- my
- pt
- ru
- ta
- th
- vi
- zh
task_categories:
- text-retrieval
- feature-extraction
pretty_name: Meddies Multilingual Wikipedia Cirrus 20260628
configs:
- config_name: burmese
  data_files:
  - split: train
    path: burmese/*.parquet
- config_name: chinese
  data_files:
  - split: train
    path: chinese/*.parquet
- config_name: english
  data_files:
  - split: train
    path: english/*.parquet
- config_name: filipino
  data_files:
  - split: train
    path: filipino/*.parquet
- config_name: french
  data_files:
  - split: train
    path: french/*.parquet
- config_name: german
  data_files:
  - split: train
    path: german/*.parquet
- config_name: indonesian
  data_files:
  - split: train
    path: indonesian/*.parquet
- config_name: japanese
  data_files:
  - split: train
    path: japanese/*.parquet
- config_name: korean
  data_files:
  - split: train
    path: korean/*.parquet
- config_name: laos
  data_files:
  - split: train
    path: laos/*.parquet
- config_name: malay
  data_files:
  - split: train
    path: malay/*.parquet
- config_name: portuguese
  data_files:
  - split: train
    path: portuguese/*.parquet
- config_name: russian
  data_files:
  - split: train
    path: russian/*.parquet
- config_name: spanish
  data_files:
  - split: train
    path: spanish/*.parquet
- config_name: tamil
  data_files:
  - split: train
    path: tamil/*.parquet
- config_name: thai
  data_files:
  - split: train
    path: thai/*.parquet
- config_name: vietnamese
  data_files:
  - split: train
    path: vietnamese/*.parquet
---

# Meddies Multilingual Wikipedia

Parquet export of Wikipedia namespace-0 articles from the official Wikimedia CirrusSearch content index dump `20260628`.

Rows: **14,789,988**.

## Subsets

| Language | Config | Code | Source index | Rows | Shards |
|---|---:|---:|---:|---:|---:|
| Burmese | `burmese` | `my` | `mywiki_content` | 84,709 | 1 |
| Chinese | `chinese` | `zh` | `zhwiki_content` | 862,880 | 8 |
| English | `english` | `en` | `enwiki_content` | 3,255,704 | 64 |
| Filipino / Tagalog | `filipino` | `fil` | `tlwiki_content` | 28,230 | 1 |
| French | `french` | `fr` | `frwiki_content` | 1,835,704 | 20 |
| German | `german` | `de` | `dewiki_content` | 2,072,166 | 20 |
| Indonesian | `indonesian` | `id` | `idwiki_content` | 419,640 | 3 |
| Japanese | `japanese` | `ja` | `jawiki_content` | 1,042,541 | 14 |
| Korean | `korean` | `ko` | `kowiki_content` | 349,707 | 3 |
| Lao | `laos` | `lo` | `lowiki_content` | 3,959 | 1 |
| Malay | `malay` | `ms` | `mswiki_content` | 387,597 | 1 |
| Portuguese | `portuguese` | `pt` | `ptwiki_content` | 801,255 | 7 |
| Russian | `russian` | `ru` | `ruwiki_content` | 998,978 | 22 |
| Spanish | `spanish` | `es` | `eswiki_content` | 1,276,291 | 16 |
| Tamil | `tamil` | `ta` | `tawiki_content` | 158,025 | 1 |
| Thai | `thai` | `th` | `thwiki_content` | 82,938 | 2 |
| Vietnamese | `vietnamese` | `vi` | `viwiki_content` | 1,129,664 | 4 |

## Columns

- `page_id`, `title`, `url`
- `text`: Cirrus plain text for retrieval and chunking
- `opening_text`: lead/opening text when available
- `headings`, `categories`, `auxiliary_text`
- `wiki`, `language`, `wikimedia_language`, `language_name`
- `timestamp`, `version`, `wikibase_item`
- `source_dump_date`, `source_index_name`, `source_url`, `shard_index`

## Source and license

Source root: `https://dumps.wikimedia.org/other/cirrus_search_index/20260628/`.

Wikipedia content is available under CC BY-SA/GFDL terms. Downstream training releases must preserve attribution/share-alike obligations where applicable.

## Build

Generated on Modal. Large dump files were streamed directly from Wikimedia and were not stored on a local machine.
