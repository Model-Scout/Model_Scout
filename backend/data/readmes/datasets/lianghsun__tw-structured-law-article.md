---
license: apache-2.0
language:
- zh
task_categories:
- text-generation
- question-answering
tags:
- legal
- Taiwan
- ROC
- zh-tw
- law-article
- sft
pretty_name: Structured and Comprehensive Legal Provisions Dataset of Taiwan
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: law_name
    dtype: string
  - name: law_version
    dtype: string
  - name: law_section
    dtype: string
  - name: law_level
    dtype: string
  - name: law_url
    dtype: string
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for tw-structured-law-article

<!-- Provide a quick summary of the dataset. -->
tw-structured-law-article 是一個中華民國（台灣）結構化複合型法規條文之繁體中文 SFT 資料集，規模為數十萬筆（`datasets.jsonl` 約 2.6 GB）。相較於 [tw-processed-law-article](https://huggingface.co/datasets/lianghsun/tw-processed-law-article)，本資料集著重於「結構化且多元化之法條排版」，涵蓋常見之法條編排格式，並處理包含 `.pdf` 附件內之條文內容，目的是讓 LLM 能全面學習更接近人類閱讀方式之法條結構。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
法律條文在實務上之呈現方式相當多樣：條文本身、條項款目之分層、表格式條文、附表、附圖、附件式條文等。傳統之法律語料多僅保留條文文字本身，丟失了這些結構化資訊，導致 LLM 雖能背誦條文，卻無法理解條文之層次結構與視覺排版。

本資料集每筆以 ShareGPT（`messages`）與 Alpaca（`instruction` / `input` / `output`）雙格式提供，並附帶法規中繼資料：
* `law_name`：法規名稱；
* `law_version`：法規版本（含適用期間）；
* `law_section`：章節資訊；
* `law_level`：法規位階（法律 / 命令 / 憲法）；
* `law_url`：原始法規 URL（全國法規資料庫）。

System prompt 固定為「你是位台灣的法律工作者，詳細解釋法條的內容…」，引導模型在回答時考慮使用者是否提及特定時點，若有則回答該時點適用之條文。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** Apache 2.0
- **Source Authority:** [全國法規資料庫](https://law.moj.gov.tw/)

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-structured-law-article](https://huggingface.co/datasets/lianghsun/tw-structured-law-article/)
- **Source Authority:** [全國法規資料庫](https://law.moj.gov.tw/)
- **Related Dataset:** [lianghsun/tw-processed-law-article](https://huggingface.co/datasets/lianghsun/tw-processed-law-article)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 繁體中文法律 LLM 之 SFT 訓練，學習結構化法條之問答格式；
* 訓練模型在回答法條問題時同時考量法規版本與適用期間；
* 作為 SFT 階段之主力法律語料，與 `tw-processed-law-article` 搭配使用；
* 訓練模型解析 PDF 附件中之條文內容。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式法律諮詢之依據，模型輸出不構成法律意見；
* 作為非中華民國法律體系之訓練資料；
* 作為律師考試準備之唯一教材；
* 作為特定條文之權威版本來源（請以全國法規資料庫之最新版為準）。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```json
{
  "messages": [
    {"role": "system", "content": "你是位台灣的法律工作者,詳細解釋法條的內容，請考慮使用者是否提及了詢問的時間點..."},
    {"role": "user", "content": "能解釋一下 農業部漁業署組織法第1條的內容嗎"},
    {"role": "assistant", "content": "法規名稱：農業部漁業署組織法\n適用期間：民國 112 年 08 月 01 日 - 民國 113 年 09 月 09 日...\n  第1條\n　　農業部為辦理漁業業務，特設漁業署（以下簡稱本署）。"}
  ],
  "instruction": "你是位台灣的法律工作者,詳細解釋法條的內容...",
  "input": "能解釋一下 農業部漁業署組織法第1條的內容嗎",
  "output": "法規名稱：農業部漁業署組織法\n適用期間：...",
  "law_name": "農業部漁業署組織法",
  "law_version": "民國 112 年 08 月 01 日",
  "law_section": "第一章",
  "law_level": "法律",
  "law_url": "https://law.moj.gov.tw/..."
}
```

| 欄位 | 型別 | 說明 |
|---|---|---|
| `messages` | list[{role, content}] | ShareGPT 格式對話（system + user + assistant） |
| `instruction` | string | Alpaca instruction（= system prompt） |
| `input` | string | Alpaca input（使用者問題） |
| `output` | string | Alpaca output（助理回答） |
| `law_name` | string | 法規名稱 |
| `law_version` | string | 法規版本與適用期間 |
| `law_section` | string | 章節資訊 |
| `law_level` | string | 法規位階（法律 / 命令 / 憲法） |
| `law_url` | string | 原始法規 URL |

| 統計項目 | 數值 |
|---|---|
| 檔案格式 | JSONL |
| 檔案大小 | ~2.6 GB |
| 筆數 | 數十萬 |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

繁中法律 LLM 在回答法條問題時，常遇到以下限制：
1. 只背誦條文文字，忽略條項款目之結構；
2. 未能區分同一條文之不同版本；
3. 對 PDF 附件內之條文完全無感。

本資料集之設計目標即為透過結構化排版、版本資訊與 PDF 內容整合，讓模型能學會「以人類閱讀方式理解法條」。

### Source Data

#### Data Collection and Processing

- **來源**：全國法規資料庫 API 之法規資料；
- **處理**：解析法規之條項款目結構，保留章節與附件資訊，並將 PDF 附件內之條文萃取；
- **格式**：組裝為 SFT 雙格式（ShareGPT + Alpaca）。

#### Who are the source data producers?

原始法規由中華民國立法院、行政院及各主管機關制定與公告，並由法務部於全國法規資料庫維護。

### Annotations

#### Annotation process

本資料集不包含額外人工標註。問題（`input`）為依法規結構程序化產生之查詢句。

#### Who are the annotators?

不適用。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
本資料集為公開之法規條文，不包含個人敏感資訊。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* **版本快照**：法規持續修正，本資料集反映特定時點之版本；
* **問句單一**：使用者問句之多樣性有限，主要為「能解釋一下…嗎」類格式；
* **PDF 萃取品質**：PDF 附件之文字萃取可能存在格式誤差；
* **System prompt 過擬合**：固定 system prompt 可能導致模型對特定提示樣式過度依賴。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者：
* 與 `tw-processed-law-article`、`tw-law-article-qa`、`tw-legal-benchmark-v1` 等資料集共同使用；
* 在訓練時混入多種 system prompt 之變體以降低過擬合風險；
* 涉及實務應用時，最後輸出應以最新之全國法規資料庫內容進行核對。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-structured-law-article,
  title        = {tw-structured-law-article: Structured and Comprehensive Legal Provisions Dataset of Taiwan},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-structured-law-article}},
  note         = {Structured ROC legal article SFT dataset covering diverse article layouts and PDF-attached articles.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
