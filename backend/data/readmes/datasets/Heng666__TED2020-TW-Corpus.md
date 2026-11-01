---
dataset_info:
- config_name: en-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 105192098
    num_examples: 394054
  download_size: 50558276
  dataset_size: 105192098
- config_name: id-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 42245033
    num_examples: 153365
  download_size: 19374788
  dataset_size: 42245033
- config_name: ja-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 101069421
    num_examples: 351078
  download_size: 47707306
  dataset_size: 101069421
- config_name: ko-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 110871742
    num_examples: 374075
  download_size: 53243063
  dataset_size: 110871742
- config_name: th-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 64742729
    num_examples: 156328
  download_size: 25868969
  dataset_size: 64742729
- config_name: vi-zh_tw
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 95714104
    num_examples: 314214
  download_size: 43462345
  dataset_size: 95714104
configs:
- config_name: en-zh_tw
  data_files:
  - split: train
    path: en-zh_tw/train-*
- config_name: id-zh_tw
  data_files:
  - split: train
    path: id-zh_tw/train-*
- config_name: ja-zh_tw
  data_files:
  - split: train
    path: ja-zh_tw/train-*
- config_name: ko-zh_tw
  data_files:
  - split: train
    path: ko-zh_tw/train-*
- config_name: th-zh_tw
  data_files:
  - split: train
    path: th-zh_tw/train-*
- config_name: vi-zh_tw
  data_files:
  - split: train
    path: vi-zh_tw/train-*
viewer: true
license: unknown
task_categories:
- translation
language:
- en
- ja
- ko
- id
- vi
- th
- tw
tags:
- taiwan
- translation
- Ted2020
pretty_name: TED2020-TW-Corpus
size_categories:
- 10M<n<100M
---
# Dataset Card for [TED2020-TW-Corpus]

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
TED2020 是一個機器翻譯基準的多語言資料集，源自 [OPUS](https://opus.nlpl.eu/TED2020/corpus/version/TED2020) 收集的使用者貢獻的翻譯，並由 [OPUS](https://opus.nlpl.eu/)。該資料集包括按語言對排序的測試和開發資料。它包括數百種語言對的測試集，並且不斷更新。請檢查版本號標籤以引用您正在使用的版本。
TED2020 收集了從1984年到2020年的演講，涵蓋了各種主題，包括科學、技術、藝術、教育、環境、社會問題等。該資料集是一個非常有價值的資源，可以用於研究和分析演講者的演講風格、主題的變化以及觀眾的反應。

### Supported Tasks and Leaderboards

### Languages
此資料集涵蓋數百種語言和語言對，並按 ISO-639-3 語言組織。目前版本涵蓋以下語言。繁體中文、英文、日文、韓文、印尼文、越南文、泰文

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
TED2020 資料集是從提交到[OPUS - TED2020](https://opus.nlpl.eu/TED2020/corpus/version/TED2020) 的使用者貢獻的翻譯中收集的，並編譯成[OPUS](https://opus.nlpl.eu) 中的多並行語料庫）。

#### Who are the source language producers?
這些轉錄本已由全球志工社群翻譯為超過 100 種語言。平行語料庫及其驗證程式碼可從[TED](https://www.ted.com/participate/translate)取得
University of Helsinki及其[language_technology_research group](https://blogs.helsinki.fi/language-technology/) 管理。用於創建和使用資源的數據和工具是[開源](https://github.com/Helsinki-NLP/Tatoeba-Challenge/)，並將作為[OPUS生態系統](https://opus.nlpl.eu/) 用於平行資料和機器翻譯研究。

### Personal and Sensitive Information
有關處理個人資訊和敏感資訊的信息，我們請諮詢資料的[原始提供者](https://opus.nlpl.eu/TED2020/corpus/version/TED2020)。該資料集未經過任何方式處理以檢測或刪除潛在的敏感資訊或個人資訊。

### Social Impact of Dataset
語言覆蓋率很高，因此它代表了機器翻譯開發的非常有價值的資源，特別是對於資源較少的語言和語言對。不斷成長的資料庫也代表著一種動態資源，其價值將進一步成長。

### Other Known Limitations
這些句子通常很短，因此很容易翻譯。對於高資源語言，這會導致結果不如更具挑戰性的基準有用。對於資源較少的語言對來說，即使在非常具有挑戰性的設定中，範例的有限複雜性實際上也是衡量進度的一件好事。

### Dataset Curators
此資料集由Heng-Shiou Sheu 製作。

### Licensing Information
這些資料集使用 [TED Talks Usage Policy](https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy) 。有關原始資料集使用條款的詳細資訊列於[此處](https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy)。

### Citation Information
```
@inproceedings{Heng666/TED2020-TW-Corpus,
  title={Taiwanese Phrases Multilingual Translation Dataset from TED2020 Talks},
  author={Heng-Shiou Sheu},
  year={2024},
  url={https://huggingface.co/datasets/Heng666/TED2020-TW-Corpus},
}
```