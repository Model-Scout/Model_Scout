---
language:
- en
- ko
- fr
- aa
- hi
license: gpl-3.0
size_categories:
- 100M<n<1B
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: src
    dtype: string
  - name: lang
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 22252477927
    num_examples: 121165414
  download_size: 16613981282
  dataset_size: 22252477927
---
This dataset is built from the open source data accompanying ["An Open Dataset and Model for Language Identification" (Burchell et al., 2023)](https://arxiv.org/abs/2305.13820)

The repository containing the actual data can be found here : https://github.com/laurieburchell/open-lid-dataset.

The license for this recreation itself follows the original upstream dataset as GPLv3+. 

However, individual datasets within it follow [each of their own licenses.](https://github.com/laurieburchell/open-lid-dataset/blob/main/licenses.md)
The "src" column lists the sources. "lang" column lists the language code in alpha-3/ISO 639-2 format followed by the script. "text" column contains the sentence.

Conversion to huggingface dataset and upload to hub done by [Chris Ha](https://github.com/chris-ha458)

Original authors built the dataset for LID models for 201 languages. I thought such a dataset could also be used for a tokenizer for 201 languages.

This dataset was processed and uploaded using huggingface datasets.


[Link to original author](https://huggingface.co/laurievb/OpenLID)