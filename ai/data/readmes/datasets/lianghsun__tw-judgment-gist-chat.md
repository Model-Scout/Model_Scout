---
license: cc-by-nc-4.0
language:
- zh
task_categories:
- text-generation
- summarization
tags:
- legal
- Taiwan
- ROC
- zh-tw
- gist
- judgment
- sft
pretty_name: 中華民國台灣之判決書要旨萃取對話資料集
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
  - name: jid_str
    dtype: string
  splits:
  - name: train
    num_examples: 31
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for tw-judgment-gist-chat

<!-- Provide a quick summary of the dataset. -->
tw-judgment-gist-chat 是 [tw-judgment-gist](https://huggingface.co/datasets/lianghsun/tw-judgment-gist) 之 chat 格式版本，合計 31 筆。每筆將精選判決書之完整文本作為使用者輸入，並由 gpt-4o 生成對應之判決要旨作為助理回答，同時以 ShareGPT（`messages`）與 Alpaca（`instruction` / `input` / `output`）雙格式提供，適合作為法律 LLM 之判決要旨萃取任務之 SFT 素材。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
法律實務界經常需要從判決書中快速擷取「法律見解之精華段落」作為引用。本資料集以 `tw-judgment-gist` 之 31 筆精選判決書為基礎，設計以下 SFT 任務：

* **輸入**：完整判決書文本（含裁判字號、日期、案由、當事人、論理段落等）；
* **輸出**：以 gpt-4o 生成之判決要旨摘要，聚焦於該判決之核心法律見解。

資料同時提供兩種常見訓練格式：
* **ShareGPT 格式**：以 `messages` 欄位（system / user / assistant 之 JSON 字串）儲存；
* **Alpaca 格式**：以 `instruction` / `input` / `output` 欄位儲存。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-NC 4.0
- **Source Authority:** [司法院](https://www.judicial.gov.tw/)
- **Annotator Model:** gpt-4o

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-judgment-gist-chat](https://huggingface.co/datasets/lianghsun/tw-judgment-gist-chat/)
- **Pretrain 版本:** [lianghsun/tw-judgment-gist](https://huggingface.co/datasets/lianghsun/tw-judgment-gist)
- **Source Authority:** [司法院](https://www.judicial.gov.tw/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 判決書要旨萃取任務之 SFT 訓練；
* 訓練法律 LLM 從冗長判決書中整理出核心法律見解；
* 作為法律摘要模型之 few-shot 範例；
* 研究 gpt-4o 之法律摘要能力之 baseline。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為法律諮詢之依據，模型輸出不構成法律意見；
* 作為完整律師考試準備教材（資料量僅 31 筆）；
* 作為判決書之權威摘要來源（摘要由 LLM 生成，非司法院官方版本）；
* 作為商業產品之訓練資料（授權為 CC BY-NC 4.0）。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```json
{
  "messages": "[{\"role\": \"system\", \"content\": \"\"}, {\"role\": \"user\", \"content\": \"這段判決書的文本是：\\n裁判字號：最高法院 113 年度台抗字第 93 號...\"}, {\"role\": \"assistant\", \"content\": \"這篇判決書的精華部分是：\\n按執行法院如發現債權人查報之財產確非債務人所有者...\"}]",
  "instruction": "",
  "input": "這段判決書的文本是：\n裁判字號：最高法院 113 年度台抗字第 93 號...",
  "output": "這篇判決書的精華部分是：\n按執行法院如發現...",
  "jid_str": "113 年度台抗字第 93 號民事判決"
}
```

| 欄位 | 型別 | 說明 |
|---|---|---|
| `messages` | string | ShareGPT 格式對話（序列化為 JSON 字串） |
| `instruction` | string | Alpaca instruction（通常為空） |
| `input` | string | 判決書完整文本 |
| `output` | string | gpt-4o 生成之判決要旨 |
| `jid_str` | string | 判決書字號 |

| 統計項目 | 數值 |
|---|---|
| 總筆數 | 31 |
| 切分 | 無（使用者自行切分） |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

若要訓練法律 LLM 能自動產出判決要旨，需要對照「長判決書 → 精華摘要」之對齊資料。司法院雖對部分精選判決製作官方要旨，但其格式並不適合直接作為 SFT 對話素材。本資料集以 `tw-judgment-gist` 之 31 筆精選判決為基礎，透過 gpt-4o 生成摘要，將其包裝為 SFT 可用之對話格式。

### Source Data

#### Data Collection and Processing

- **來源**：`tw-judgment-gist` 之 31 筆精選判決書文本；
- **處理**：
  1. 以 `這段判決書的文本是：...` 為 prompt 前綴，將判決書作為 user 訊息；
  2. 以 gpt-4o 產生判決要旨作為 assistant 訊息；
  3. 同時打包為 ShareGPT 與 Alpaca 雙格式；
  4. 附上判決書字號 `jid_str`。

#### Who are the source data producers?

原始判決書由中華民國各級法院之承審法官撰寫，經司法院依其標準選入精選判決。摘要由 gpt-4o 生成。

### Annotations

#### Annotation process

`output` 欄位為 gpt-4o 生成之結果，未經額外人工修訂。

#### Who are the annotators?

gpt-4o（LLM 生成），curator 進行 pipeline 組裝。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
判決書為司法院依法公開之文書，當事人姓名之揭露或遮蔽依司法院規則辦理，本資料集未額外匿名化。使用者不得以本資料集進行當事人識別。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* **資料量極小**：僅 31 筆，不足以單獨支撐 SFT 訓練；
* **摘要由 LLM 生成**：`output` 非專業律師撰寫之要旨，可能存在理解偏差或遺漏；
* **領域分布不均**：精選判決之領域由司法院選定，可能偏向特定法律領域；
* **時效性**：法律見解會隨法規修訂而變動。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者：
* 將本資料集作為判決書摘要任務之 few-shot 範例或 warm-up 素材，而非主力訓練集；
* 搭配 `tw-processed-judgments-14B` 等大規模判決書語料進行 SFT；
* 對於模型產出之摘要，應以人工或 rule-based 檢查核對所引用之條文是否正確；
* 若需 CPT 版本，參考 [tw-judgment-gist](https://huggingface.co/datasets/lianghsun/tw-judgment-gist)。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-judgment-gist-chat,
  title        = {tw-judgment-gist-chat: Chat-formatted Judgment Gist Extraction Dataset},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-judgment-gist-chat}},
  note        = {31 judgment-to-gist SFT pairs generated by gpt-4o, available in ShareGPT and Alpaca formats.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
