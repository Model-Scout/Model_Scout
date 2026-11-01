---
license: cc-by-sa-4.0
language:
- zh
task_categories:
- text-generation
- question-answering
tags:
- legal
- zh-tw
- Taiwan
- ROC
- DPO
size_categories:
- 1K<n<10K
dataset_info:
- config_name: default
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: chosen
    struct:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: rejected
    struct:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: name
    dtype: string
  - name: "no"
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: train
    num_bytes: 6105795
    num_examples: 1652
  download_size: 6105795
  dataset_size: 6105795
  data_files:
  - split: train
    path: data/datasets.jsonl
- config_name: processed
  features:
  - name: simple_messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
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
  - name: think
    dtype: string
  - name: output
    dtype: string
  - name: name
    dtype: string
  - name: "no"
    dtype: string
  splits:
  - name: train
    num_bytes: 7686920
    num_examples: 1652
  download_size: 7686920
  dataset_size: 7686920
  data_files:
  - split: train
    path: data/datasets_processed.jsonl
---
# Dataset Card for 中華民國台灣法規條文問答集

<!-- Provide a quick summary of the dataset. -->
tw-law-article-qa 是一個以中華民國法規條文為核心的繁體中文法律問答資料集，包含 1,652 筆問答對，涵蓋 993 部不同法規。每筆資料以「法規名稱§條號」為查詢輸入，提供條文內容、法規背景資料與實務解釋，並附帶 DPO（Direct Preference Optimization）所需的 chosen/rejected 回答對，可同時用於 SFT 與偏好對齊訓練。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集提供兩個子集：

**`default`（datasets.jsonl）：** 包含 ShareGPT 格式對話與 DPO 偏好對
* `chosen` — 品質較高的回答，結構完整（條文內容＋法規背景＋解釋）
* `rejected` — 品質較低的回答，可能缺乏結構或包含錯誤資訊

**`processed`（datasets_processed.jsonl）：** 轉換為 messages 格式，適用於標準 SFT 訓練流程
* `messages` / `simple_messages` — OpenAI messages 格式（role/content）

每筆回答的標準結構包含：
1. **條文內容：** 完整引用法規條文原文
2. **法規背景資料：** 法規名稱、修正日期、法規類別、施行狀態
3. **解釋：** 條文之實務意涵與應用說明

涵蓋 993 部法規，包括民法、刑法、行政法、稅法、金融法規、環境法規、勞動法規等各領域。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-SA 4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-law-article-qa](https://huggingface.co/datasets/lianghsun/tw-law-article-qa/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 對語言模型進行法規條文查詢與解釋之 SFT 微調，使模型能正確引用法條並提供實務說明；
* 使用 chosen/rejected 偏好對進行 DPO 訓練，提升法律回答之品質與結構；
* 建構法規查詢系統或法律知識問答引擎之原型。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式法律諮詢之依據，因內容為模型生成之解釋，不保證法律正確性。
* 直接作為法規資料庫使用，因條文可能未反映最新修正版本。
* 用於非中華民國法律體系之訓練。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

### default（datasets.jsonl）— 含 DPO 偏好對
```jsonl
{
  "conversations": [{"from": "human", "value": "人事管理條例§2"}, {"from": "gpt", "value": "..."}],
  "chosen": {"from": "gpt", "value": "（高品質回答）"},
  "rejected": {"from": "gpt", "value": "（低品質回答）"},
  "input": "人事管理條例§2",
  "output": "...",
  "name": "人事管理條例",
  "no": "第2條",
  "instruction": "針對說明法規其背景與實務應用。"
}
```

### processed（datasets_processed.jsonl）— SFT messages 格式
```jsonl
{
  "simple_messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}],
  "messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}],
  "instruction": "...",
  "input": "人事管理條例§2",
  "think": "",
  "output": "...",
  "name": "人事管理條例",
  "no": "第2條"
}
```

| 統計項目 | 數值 |
|---|---|
| 問答對數 | 1,652 |
| 涵蓋法規數 | 993 |
| 資料格式 | ShareGPT + DPO / Messages |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

繁體中文語言模型在引用中華民國法規條文時經常產生幻覺（如虛構條號、張冠李戴條文內容）。本資料集以結構化方式提供條文原文與解釋，搭配 DPO 偏好對訓練，目標在於減少法律問答中的幻覺現象，並提升回答的結構一致性。

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

法規條文來源為中華民國法律公開資料，問答對與 chosen/rejected 偏好由大型語言模型生成。`processed` 子集為 `default` 子集之格式轉換版本。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

法規條文為中華民國政府公開資料，問答與偏好對由大型語言模型合成生成。

### Annotations

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

DPO 偏好對（chosen/rejected）由語言模型生成，chosen 為經過品質優化之結構化回答，rejected 為品質較低之回答（可能缺乏結構或包含錯誤）。

#### Who are the annotators?

不適用（合成生成）。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
本資料集內容為法規條文與解釋，不涉及個人資訊或敏感資料。所有法規均為公開資訊。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* 法規條文以資料集建立時之版本為準，後續修正之法規可能未反映於本資料集。
* 條文解釋由語言模型生成，可能存在法律詮釋不精確之處。
* 涵蓋 993 部法規，但並非中華民國全部現行法規之完整覆蓋。
* rejected 回答之品質差異程度不一，部分 rejected 僅為格式較差但內容並無重大錯誤。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者搭配全國法規資料庫（[law.moj.gov.tw](https://law.moj.gov.tw/)）交叉驗證條文內容之正確性與時效性。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-law-article-qa,
  title        = {tw-law-article-qa: ROC Law Article QA Dataset with DPO Preference Pairs},
  author       = {Liang Hsun Huang},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-law-article-qa}},
  note         = {1,652 QA pairs covering 993 ROC laws with chosen/rejected pairs for DPO training.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
