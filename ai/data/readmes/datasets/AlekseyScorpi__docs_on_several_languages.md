---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': az
          '1': be
          '2': en
          '3': et
          '4': fn
          '5': gr
          '6': ja
          '7': kk
          '8': ko
          '9': lt
          '10': lv
          '11': mn
          '12': 'no'
          '13': pl
          '14': ru
          '15': uk
          '16': zh
  splits:
  - name: train
    num_bytes: 7057770706.296
    num_examples: 2006
  - name: test
    num_bytes: 1246282602.0
    num_examples: 339
  download_size: 7700053691
  dataset_size: 8304053308.296
task_categories:
- text-classification
- translation
- feature-extraction
tags:
- code
size_categories:
- 1K<n<10K
license: mit
language:
- az
- be
- en
- et
- fi
- ka
- ja
- ko
- kk
- lv
- lt
- mn
- 'no'
- pl
- ru
- uk
- zh
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---
# Dataset Card for "docs_on_several_languages"
This dataset is a collection of different images in different languages.
The daset includes the following languages: Azerbaijani (az: 0), Belorussian (be: 1), Chinese (zh: 16), English (en: 2), Estonian (et: 3), Finnish (fn: 4), Georgian (gr: 5), Japanese (ja: 6), Korean (ko: 7), Kazakh (kk: 8), Latvian (lv: 10), Lithuanian (lt: 9), Mongolian (mn: 11), Norwegian (no: 12), Polish (pl: 13), Russian (ru: 14), Ukranian (uk: 15).
Each language has a corresponding class label defined. At least 100 images in the entire dataset are allocated per class. This dataset was originally used for the task of classifying the language of a document based on its image, but I hope it can help you in other machine learning tasks.