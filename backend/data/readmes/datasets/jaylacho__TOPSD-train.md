---
pretty_name: TOPSD and COPSD multilingual training data
language:
- bn
- en
- es
- ja
- ko
- ru
- sw
- te
- th
- zh
task_categories:
- text-generation
configs:
- config_name: bn
  data_files:
  - split: train
    path: translated_3000_bn.json
- config_name: en
  data_files:
  - split: train
    path: translated_3000_en.json
- config_name: es
  data_files:
  - split: train
    path: translated_3000_es.json
- config_name: ja
  data_files:
  - split: train
    path: translated_3000_ja.json
- config_name: ko
  data_files:
  - split: train
    path: translated_3000_ko.json
- config_name: ru
  data_files:
  - split: train
    path: translated_3000_ru.json
- config_name: sw
  data_files:
  - split: train
    path: translated_3000_sw.json
- config_name: te
  data_files:
  - split: train
    path: translated_3000_te.json
- config_name: th
  data_files:
  - split: train
    path: translated_3000_th.json
- config_name: zh
  data_files:
  - split: train
    path: translated_3000_zh.json
---

# TOPSD / historical COPSD training data

Ten aligned language files, each retaining the original 3,000 rows and order.
Training selects 500 usable rows per language after translation/length filtering,
with datasets==3.6.0 and seed=42. Japanese has 2,999 usable rows.
Do not truncate to 500 rows before running the original training loader.

Upstream: https://huggingface.co/datasets/yihongLiu/COPSD-PolyMath-TrainDataset
Pinned upstream revision: `519ea2be68fec00c8a033cb2040059ff595b06a0`.
English and Korean are the original local experiment supplements.
This bundle preserves the source data; it does not assign a new license.
File checksums and ordered/sampled training-view fingerprints are in `dataset_manifest.json`.

TOPSD language concatenation order: bn,en,es,ja,ko,ru,sw,te,th,zh.
Historical COPSD concatenation order: en,bn,es,ja,ko,ru,sw,te,th,zh.
The respective loaders perform the final multilingual shuffle.
