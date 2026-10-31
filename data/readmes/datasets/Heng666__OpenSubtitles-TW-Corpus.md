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
    num_bytes: 551312007
    num_examples: 3762380
  download_size: 198513620
  dataset_size: 551312007
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
    num_bytes: 195956760
    num_examples: 1259138
  download_size: 69062423
  dataset_size: 195956760
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
    num_bytes: 82957644
    num_examples: 558832
  download_size: 28947031
  dataset_size: 82957644
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
    num_bytes: 43408491
    num_examples: 298466
  download_size: 15889266
  dataset_size: 43408491
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
    num_bytes: 98383808
    num_examples: 521847
  download_size: 33136242
  dataset_size: 98383808
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
    num_bytes: 131013253
    num_examples: 818723
  download_size: 45507786
  dataset_size: 131013253
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
- zh
tags:
- translation
- OPUS
- OpenSubtitles
pretty_name: Heng666/OpenSubtitles-TW-Corpus
size_categories:
- 1M<n<10M
---

# Dataset Card for [OpenSubtitles-TW-Corpus]

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

OpenSubtitles-TW-Corpus 是一個機器翻譯基準的多語言資料集，源自 [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles/corpus/version/OpenSubtitles) 收集的使用者貢獻的翻譯，並由 [OPUS](https://opus.nlpl.eu/)。該資料集包括按語言對排序的測試和開發資料。它包括數百種語言對的測試集，並且不斷更新。請檢查版本號標籤以引用您正在使用的版本。
這是字幕集合的稍微乾淨的版本，使用改進的句子對齊和更好的語言檢查。

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
OpenSubtitles 資料集是從 [P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles](http://www.lrec-conf.org/proceedings/lrec2016/pdf/947_Paper.pdf)進行整理，並由 [OPUS](https://opus.nlpl.eu)  收納。

#### Who are the source language producers?
這些轉錄本由 [OpenSubtitles 所有](http://www.opensubtitles.org/)

### Personal and Sensitive Information
有關處理個人資訊和敏感資訊的信息，我們請諮詢資料的[原始提供者](http://www.opensubtitles.org/)。該資料集未經過任何方式處理以檢測或刪除潛在的敏感資訊或個人資訊。

### Social Impact of Dataset
語言覆蓋率很高，因此它代表了機器翻譯開發的非常有價值的資源，特別是對於資源較少的語言和語言對。不斷成長的資料庫也代表著一種動態資源，其價值將進一步成長。

### Other Known Limitations
這些句子通常很短，因此很容易翻譯。對於高資源語言，這會導致結果不如更具挑戰性的基準有用。對於資源較少的語言對來說，即使在非常具有挑戰性的設定中，範例的有限複雜性實際上也是衡量進度的一件好事。

### Dataset Curators
此資料集由Heng-Shiou Sheu 製作。

### Licensing Information
如果您在自己的工作中使用該語料庫的任何部分，請引用以下文章：P. Lison 和 J. Tiedemann，2016，OpenSubtitles2016：從電影和電視字幕中提取大型並行語料庫。第十屆國際語言資源與評估會議 (LREC 2016) 論文集


### Citation Information
```
@inproceedings{Heng666/OpenSubtitles-TW-Corpus,
  title={Taiwanese Phrases Multilingual Translation Dataset from OpenSubtitles Talks},
  author={Heng-Shiou Sheu},
  year={2024},
  url={https://huggingface.co/datasets/Heng666/OpenSubtitles-TW-Corpus},
}
```