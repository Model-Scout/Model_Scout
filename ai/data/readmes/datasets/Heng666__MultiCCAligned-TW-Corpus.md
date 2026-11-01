---
language:
- tw
- en
- ja
- ko
- id
- vi
- th
- zh
license: mit
size_categories:
- 1M<n<10M
task_categories:
- translation
pretty_name: MultiCCAligned-TW-Corpus
dataset_info:
- config_name: en-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 263012161
    num_examples: 1351553
  download_size: 122088200
  dataset_size: 263012161
- config_name: id-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 40174579
    num_examples: 163854
  download_size: 15141217
  dataset_size: 40174579
- config_name: ja-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 180621101
    num_examples: 741236
  download_size: 73083903
  dataset_size: 180621101
- config_name: ko-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 65074105
    num_examples: 333554
  download_size: 27017008
  dataset_size: 65074105
- config_name: th-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 83637133
    num_examples: 302186
  download_size: 30143050
  dataset_size: 83637133
- config_name: vi-zh_TW
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 53444757
    num_examples: 237025
  download_size: 19434415
  dataset_size: 53444757
configs:
- config_name: en-zh_TW
  data_files:
  - split: train
    path: en-zh_TW/train-*
- config_name: id-zh_TW
  data_files:
  - split: train
    path: id-zh_TW/train-*
- config_name: ja-zh_TW
  data_files:
  - split: train
    path: ja-zh_TW/train-*
- config_name: ko-zh_TW
  data_files:
  - split: train
    path: ko-zh_TW/train-*
- config_name: th-zh_TW
  data_files:
  - split: train
    path: th-zh_TW/train-*
- config_name: vi-zh_TW
  data_files:
  - split: train
    path: vi-zh_TW/train-*
tags:
- MultiCCAligned
- translation
- OPUS
---
# Dataset Card for [MultiCCAligned-TW-Corpus]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:** [Heng-Shiou Sheu](mailto:hengshiousheu@gmail.com)

### Dataset Summary
MultiCCAligned-TW-Corpus 是一個機器翻譯基準的多語言資料集，源自 [OPUS](https://opus.nlpl.eu/MultiCCAligned/zh-TW&th/v1.1/MultiCCAligned) 收集的使用者貢獻的翻譯，並由 [OPUS](https://opus.nlpl.eu/)。該資料集包括按語言對排序的測試和開發資料。它包括數百種語言對的測試集，並且不斷更新。請檢查版本號標籤以引用您正在使用的版本。


### Supported Tasks and Leaderboards

### Languages
此資料集涵蓋數百種語言和語言對，並按 ISO-639-1 語言組織。目前版本涵蓋以下語言。繁體中文、英文、日文、韓文、印尼文、越南文、泰文

## Dataset Structure
### Data Instances

資料以 , 分隔檔案中內容，具有三個欄位：指示、輸入和輸出。請注意，我們並不暗示平移方向，並認為資料集是對稱的並用作兩個方向的測試集。

### Data Splits
先整理出 Train 資料。

## Dataset Creation
### Curation Rationale
本資料集將持續更新，未來將公開發佈於 Github 當中。高語言覆蓋率是本計畫的主要目標，資料集的準備與標準化語言標籤和分發格式保持一致和系統化。

### Source Data
#### Initial Data Collection and Normalization
MultiCCAligned 資料集是從根據 68 個 Commoncrawl 快照創建的（截至 2020 年 3 月）。根據標點符號將文件分割成句子，並執行重複資料刪除。語料庫的準備工作並沒有提出任何智慧財產權主張。原始發行版可從 http://www.statmt.org/cc-aligned/ 取得

#### Who are the source language producers?
這些轉錄本已由 [EMNLP'20 作者群](https://www.aclweb.org/anthology/2020.emnlp-main.480.pdf)製作。

### Personal and Sensitive Information
有關處理個人資訊和敏感資訊的信息，我們請諮詢資料的[原始提供者](https://www.aclweb.org/anthology/2020.emnlp-main.480.pdf)。該資料集未經過任何方式處理以檢測或刪除潛在的敏感資訊或個人資訊。

### Social Impact of Dataset
語言覆蓋率很高，因此它代表了機器翻譯開發的非常有價值的資源，特別是對於資源較少的語言和語言對。不斷成長的資料庫也代表著一種動態資源，其價值將進一步成長。

### Other Known Limitations
這些句子通常很短，因此很容易翻譯。對於高資源語言，這會導致結果不如更具挑戰性的基準有用。對於資源較少的語言對來說，即使在非常具有挑戰性的設定中，範例的有限複雜性實際上也是衡量進度的一件好事。

### Dataset Curators
此資料集由Heng-Shiou Sheu 製作。

### Licensing Information
這些資料集沒使用 License.

### Citation Information
```
@inproceedings{Heng666/MultiCCAligned-TW-Corpus,
  title={Taiwanese Phrases Multilingual Translation Dataset from MultiCCAligned Talks},
  author={Heng-Shiou Sheu},
  year={2024},
  url={https://huggingface.co/datasets/Heng666/MultiCCAligned-TW-Corpus},
}
```