---
license: cc-by-nc-sa-4.0
language:
- zh
task_categories:
- question-answering
- text-generation
tags:
- legal
- Taiwan
- contract
- chat
size_categories:
- n<1K
dataset_info:
  features:
  - name: messages
    dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 473267
    num_examples: 528
  download_size: 473267
  dataset_size: 473267
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for tw-contract-review-chat

<!-- Provide a quick summary of the dataset. -->
tw-contract-review-chat 是一個以台灣契約審閱實務為主題的繁體中文問答資料集，包含 528 筆單輪問答對。內容涵蓋定型化契約、契約審閱權、締約主體、契約條款磋商、不動產預售屋契約等台灣常見之契約實務議題，適用於語言模型之法律領域指令微調。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集聚焦於台灣契約法實務，以問答方式呈現契約審閱過程中的常見問題與專業解說。每筆資料為單輪問答（1 問 1 答），涵蓋的主題包括：

* **定型化契約：** 定義、適用範圍、審閱期間、消費者權益
* **契約磋商：** 商業合約之磋商空間、條款修改可能性
* **締約主體：** 法人與自然人之締約資格、代理權限
* **特定契約類型：** 信用卡契約、不動產預售屋契約、商業合約
* **契約審閱實務：** 業務部門注意事項、風險評估

`messages` 欄位為 JSON 編碼之 OpenAI messages 格式字串（system + user + assistant）。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-contract-review-chat](https://huggingface.co/datasets/lianghsun/tw-contract-review-chat/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 對語言模型進行台灣契約法實務之 SFT 微調，使模型能回答契約審閱相關問題；
* 建構契約審閱輔助系統或法律諮詢聊天機器人之原型；
* 增強模型對台灣商業契約實務慣例之理解。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式法律諮詢或契約審閱之替代，因內容為模型生成之一般性解說。
* 用於非台灣法律體系之契約訓練。
* 作為契約範本或條款建議之來源。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```jsonl
{
  "messages": "[{\"role\": \"system\", \"content\": \"\"}, {\"role\": \"user\", \"content\": \"什麼是定型化契約？\"}, {\"role\": \"assistant\", \"content\": \"...\"}]",
  "instruction": "",
  "input": "什麼是定型化契約？",
  "output": "..."
}
```

| 欄位 | 說明 |
|---|---|
| `messages` | JSON 編碼之 messages 陣列（system + user + assistant） |
| `instruction` | 額外指令（本資料集中均為空） |
| `input` | 使用者問題 |
| `output` | 回答內容 |

| 統計項目 | 數值 |
|---|---|
| 問答對數 | 528 |
| 對話格式 | 單輪問答 |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

台灣商業活動中契約審閱為常見需求，但一般民眾與中小企業往往缺乏法律專業知識。本資料集將契約審閱實務知識轉化為問答格式，目標在於使語言模型能提供基礎的契約概念解說與審閱注意事項。

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

問答對由大型語言模型基於台灣契約法實務知識合成生成。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

所有內容由大型語言模型合成生成。

### Annotations

#### Annotation process

本資料集不包含額外標註。

#### Who are the annotators?

不適用。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
本資料集為合成生成之法律問答，不涉及個人資訊或敏感資料。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* 內容為模型生成之一般性解說，法律詮釋可能不夠精確或完整。
* 僅涵蓋契約審閱之基礎概念，對於複雜商業契約或特殊條款之分析有限。
* 資料集規模較小（528 筆），建議搭配其他法律對話資料集使用。
* `messages` 欄位為 JSON 字串而非原生 list，使用時需先解析。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者將本資料集作為法律 SFT 訓練之補充素材，並提醒終端使用者模型回答不構成法律意見。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-contract-review-chat,
  title        = {tw-contract-review-chat: Taiwan Contract Review QA Dataset},
  author       = {Liang Hsun Huang},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-contract-review-chat}},
  note         = {528 QA pairs on Taiwan contract review practices including standardized contracts, negotiation, and due diligence.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
