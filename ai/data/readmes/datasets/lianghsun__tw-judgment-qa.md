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
- judgment
- dpo
- sft
pretty_name: 中華民國台灣判決書問答資料集（含 DPO 格式）
size_categories:
- n<1K
dataset_info:
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
  - name: judgement_id
    dtype: string
  - name: judgement_date
    dtype: string
  - name: judgement_cause
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_examples: 579
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for tw-judgment-qa

<!-- Provide a quick summary of the dataset. -->
tw-judgment-qa 是一個以中華民國（台灣）判決書為基礎之法律情境式問答資料集，合計 579 筆。每筆同時提供 SFT 格式（ShareGPT `conversations` + Alpaca `input` / `output`）與 DPO 格式（`chosen` / `rejected`），並附帶判決書字號、日期、案由與 URL，適合法律 LLM 之 SFT 與 DPO 微調。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
法律 LLM 在回答使用者問題時，應能參照判決書實務見解提出完整之分析。本資料集以實際判決書為背景，由 curator 將案例改寫為使用者可能提出之生活情境問題，並提供兩個模型產生之答案：較佳者作為 `chosen`，較弱者作為 `rejected`，以支援 DPO 訓練。

答案之結構通常包含：
1. **案情摘要**：整理使用者描述之事實；
2. **分析爭點**：列出可能涉及之法律爭議；
3. **適用法條**：援引具體條文；
4. **實務處理方向**：提供當事人可採取之行動建議。

每筆同時保留 `input` / `output` 之 Alpaca 格式以供一般 SFT 使用。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** Apache 2.0
- **Source Authority:** [司法院判決書查詢系統](https://judgment.judicial.gov.tw/)

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-judgment-qa](https://huggingface.co/datasets/lianghsun/tw-judgment-qa/)
- **Source Authority:** [司法院](https://www.judicial.gov.tw/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 繁體中文法律 LLM 之 SFT 微調（以 `conversations` 或 `input` / `output` 為訓練目標）；
* 以 `chosen` / `rejected` 進行 DPO（Direct Preference Optimization）微調；
* 訓練模型將判決書之實務見解應用到使用者之生活情境問題；
* 研究法律領域之偏好對齊。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式法律諮詢之依據，模型輸出不構成法律意見；
* 作為非中華民國法律體系之訓練資料；
* 作為當事人身份識別之素材；
* 作為完整律師考試準備教材（資料量僅 579 筆）。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```json
{
  "conversations": [{"from": "human", "value": "如果我朋友在某天晚上..."}],
  "chosen": {"from": "gpt", "value": "您好！希望您一切安好。關於您朋友的情況..."},
  "rejected": {"from": "gpt", "value": "若你朋友在晚上按電鈴..."},
  "input": "如果我朋友在某天晚上...",
  "output": "您好！希望您一切安好。關於您朋友的情況...",
  "judgement_id": "臺灣高雄地方法院 95 年度訴字第 1628 號刑事判決",
  "judgement_date": "民國 95 年 09 月 13 日",
  "judgement_cause": "誣告",
  "url": "https://judgment.judicial.gov.tw/FJUD/data.aspx?..."
}
```

| 欄位 | 型別 | 說明 |
|---|---|---|
| `conversations` | list[{from, value}] | ShareGPT 格式對話（目前為單輪 human） |
| `chosen` | {from, value} | 偏好答案（DPO 用） |
| `rejected` | {from, value} | 非偏好答案（DPO 用） |
| `input` | string | Alpaca input（使用者問題） |
| `output` | string | Alpaca output（= chosen 之 value） |
| `judgement_id` | string | 判決書字號 |
| `judgement_date` | string | 裁判日期 |
| `judgement_cause` | string | 案由 |
| `url` | string | 原始判決書 URL |

| 統計項目 | 數值 |
|---|---|
| 總筆數 | 579 |
| 切分 | 無（使用者自行切分） |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

一般法律 QA 資料集多僅有單一「正解」，無法訓練模型區分「好答案」與「尚可答案」。本資料集透過提供偏好對（`chosen` / `rejected`），讓模型在 DPO 階段學習「結構完整、引用具體條文、提供可行動建議」之回答風格，並將判決書之實務見解帶入回答中。

### Source Data

#### Data Collection and Processing

- **判決書來源**：司法院判決書查詢系統之公開判決；
- **問題改寫**：將判決書之事實摘要改寫為使用者可能提出之生活情境問題；
- **答案生成**：以 LLM 產生兩個不同品質之答案作為 `chosen` / `rejected`；
- **對齊欄位**：保留判決書字號、日期、案由與 URL，以利追溯。

#### Who are the source data producers?

原始判決書由中華民國各級法院之承審法官撰寫，經司法院依法公開。問題與答案之改寫與生成由 curator 搭配 LLM 進行。

### Annotations

#### Annotation process

答案之 `chosen` / `rejected` 由 curator 依「結構完整性、條文引用正確性、可行動性」挑選。

#### Who are the annotators?

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
判決書為司法院依法公開之文書，當事人姓名之揭露或遮蔽依司法院規則辦理。使用者應於改寫之問題中避免還原當事人身份。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* **資料量小**：僅 579 筆，作為 DPO 訓練集時容易 overfit；
* **LLM 生成之答案可能失真**：`chosen` / `rejected` 皆為 LLM 生成，非專業律師撰寫；
* **時效性**：判決書反映特定時點之法律見解，條文可能已修正；
* **偏好來源單一**：由 curator 一人選擇 chosen/rejected，存在標註者偏差。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者：
* 將本資料集作為 DPO 訓練之補強集，而非主要偏好資料；
* 搭配 `tw-processed-judgments-14B` 等大規模判決書語料，先完成 SFT 再進行 DPO；
* 對於實務應用之輸出，應以全國法規資料庫最新版本進行交叉比對；
* 若要做判決書精華萃取任務，可參考 `tw-judgment-gist-chat`。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-judgment-qa,
  title        = {tw-judgment-qa: ROC Judgment-grounded QA Dataset with DPO Pairs},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-judgment-qa}},
  note         = {579 ROC judgment-grounded QA samples with SFT and DPO (chosen/rejected) pairs.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
