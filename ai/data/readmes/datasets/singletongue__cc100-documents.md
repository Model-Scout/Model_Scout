---
language:
- ar
- de
- en
- es
- fr
- it
- ja
- ko
- pt
- ru
- zh
language_bcp47:
- zh-Hans
- zh-Hant
multilinguality:
- multilingual
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
dataset_info:
- config_name: ar
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 30345714473
    num_examples: 15039879
  download_size: 15115802825
  dataset_size: 30345714473
- config_name: de
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 72775978455
    num_examples: 69023867
  download_size: 45855033322
  dataset_size: 72775978455
- config_name: en
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 327673321587
    num_examples: 247588106
  download_size: 206842211484
  dataset_size: 327673321587
- config_name: es
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 58353909888
    num_examples: 60542096
  download_size: 36639924361
  dataset_size: 58353909888
- config_name: fr
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 62167991656
    num_examples: 62112712
  download_size: 38687566994
  dataset_size: 62167991656
- config_name: it
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 32862817488
    num_examples: 24674591
  download_size: 20840201122
  dataset_size: 32862817488
- config_name: ja
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 75607021621
    num_examples: 65613665
  download_size: 43271734711
  dataset_size: 75607021621
- config_name: ko
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 58828056524
    num_examples: 35678358
  download_size: 34859494100
  dataset_size: 58828056524
- config_name: pt
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 53502662440
    num_examples: 38999388
  download_size: 33751151154
  dataset_size: 53502662440
- config_name: ru
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 300870542621
    num_examples: 123181529
  download_size: 151288950598
  dataset_size: 300870542621
- config_name: zh-Hans
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 51117335603
    num_examples: 40002855
  download_size: 36115556249
  dataset_size: 51117335603
- config_name: zh-Hant
  features:
  - name: idx
    dtype: int64
  - name: start_ln
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18091739883
    num_examples: 12328227
  download_size: 12884957758
  dataset_size: 18091739883
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: zh-Hans
  data_files:
  - split: train
    path: zh-Hans/train-*
- config_name: zh-Hant
  data_files:
  - split: train
    path: zh-Hant/train-*
---

# cc100-documents

This dataset is a restructured version of the [CC-100](https://data.statmt.org/cc-100/) ([statmt/cc100](https://huggingface.co/datasets/statmt/cc100)) dataset.

In the original dataset, each instance corresponds to a single paragraph (or a document boundary).
In this version, the data has been reformed so that each instance corresponds to a single, complete document.

This document-level structure makes it more convenient for processing using the `map()` and `filter()` methods in the Hugging Face Datasets library.

## Languages

The following languages are currently available:

|Language                        |Number of examples|
|:-------------------------------|-----------------:|
|`ar`: Arabic                    |        15,039,879|
|`de`: German                    |        69,023,867|
|`en`: English                   |       247,588,106|
|`es`: Spanish                   |        60,542,096|
|`fr`: French                    |        62,112,712|
|`it`: Italian                   |        24,674,591|
|`ja`: Japanese                  |        65,613,665|
|`ko`: Korean                    |        35,678,358|
|`pt`: Portuguese                |        38,999,388|
|`ru`: Russian                   |       123,181,529|
|`zh-Hans`: Chinese (Simplified) |        40,002,855|
|`zh-Hant`: Chinese (Traditional)|        12,328,227|

## Dataset Structure

### Data Instances

Each instance in the dataset represents one document from the original CC-100 dataset, preserving the original document order. The original paragraphs are concatenated together, preserving the newline characters between them, to form a single document text.

Example from the `en` configuration:

```json
{
  "idx": 0,
  "start_ln": 1,
  "text": "Belmont Estate is on the market for $63 million and boasts roughly 22,000 square feet of luxurious..."
}
{
  "idx": 1,
  "start_ln": 8,
  "text": "Stay well hydrated—that means you should include about 48- 64 ounces of liquid (non-calorie) each day..."
}
```

### Data Fields

- **idx** (*int64*): The index of the instance, starting from `0`.
- **start_ln** (*int64*): The 1-based line number where the document begins in the original CC-100 text file.
- **text** (*string*): The complete text of the document.

## Dataset creation process

The dataset is created from the original CC-100 text files available at https://data.statmt.org/cc-100/.

The code used to create this dataset is available in the [GitHub repository](https://github.com/singletongue/cc100-documents).

## License

No intellectual property is claimed on the preparation of this corpus.
By using this dataset, you are also bound by the [Common Crawl terms of use](https://commoncrawl.org/terms-of-use) in respect of the content contained in the dataset.

Please refer to the following pages for license information on the original dataset:
- https://data.statmt.org/cc-100/
- https://huggingface.co/datasets/statmt/cc100
