---
license: cc-by-nc-4.0
language:
- zh
task_categories:
- text-generation
- question-answering
- token-classification
tags:
- legal
- Taiwan
- ROC
- zh-tw
- ner
- information-extraction
pretty_name: 法律資料科學任務資料集
size_categories:
- n<1K
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
  - name: task
    dtype: string
  splits:
  - name: train
    num_examples: 171
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for tw-legal-nlp

<!-- Provide a quick summary of the dataset. -->
tw-legal-nlp 是一個專為台灣法律領域資料科學任務所設計之小型多任務資料集，合計 171 筆，涵蓋命名實體識別（NER）、法律文本語意理解、法律文本結構化（JSON / Markdown）、法規條號書寫習慣互換等四類常見 NLP 任務。每筆同時以 ShareGPT（`messages`）與 Alpaca（`instruction / input / output`）格式提供，並附帶 `task` 欄位以標示任務類型。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
台灣法律領域之資料科學任務長期缺乏系統化之公開素材，既有中文 NLP 資料集多以新聞、百科為主，難以反映法律文本之特殊用語、結構與慣用寫法。本資料集鎖定四類典型法律 NLP 任務：

1. **命名實體識別（NER）**：從判決書中抽取當事人、法條、日期等關鍵實體；
2. **語意理解 / 文本分類**：理解判決書內容並進行分類或摘要；
3. **文本結構化（Text-to-Structure）**：將法律文本轉換為 JSON 或 Markdown 等結構化格式；
4. **法規條號書寫互換（Seq2Seq）**：將「§61」、「第61條」、「第六十一條」等不同書寫慣例互相轉換。

資料由 `gpt-4o` 基於規則與判決書片段生成，再由 curator 進行格式整理與過濾。任務類型記於 `task` 欄位，便於下游按任務切分訓練 / 評測。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-NC-4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-legal-nlp](https://huggingface.co/datasets/lianghsun/tw-legal-nlp/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 法律領域 NLP 任務之 SFT 訓練或 few-shot prompting；
* 作為判決書 NER、法律文本結構化之 prototype 素材；
* 法規條號書寫慣例之 Seq2Seq 模型訓練；
* 作為台灣法律 NLP 基準之延伸，與 `tw-legal-benchmark-v1`、`tw-law-article-qa` 等資料集搭配使用。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式 NER 基準（資料量僅 171 筆，且部分內容由 `gpt-4o` 改寫）；
* 作為法律諮詢或實務判斷之依據；
* 作為非台灣法律體系（不同法規編號習慣）之訓練資料；
* 作為商業產品之訓練資料（授權為 CC BY-NC-4.0）。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```json
{
  "messages": [
    {"role": "user", "content": "以下是判決書內容。臺灣臺北地方法院民事判決 上訴人 即 被告 張三豐。誰是上訴人？"},
    {"role": "assistant", "content": "張三豐"}
  ],
  "instruction": "",
  "input": "以下是判決書內容。臺灣臺北地方法院民事判決 上訴人 即 被告 張三豐。誰是上訴人？",
  "output": "張三豐",
  "task": "named-entity-recognition"
}
```

| 欄位 | 型別 | 說明 |
|---|---|---|
| `messages` | list[{role, content}] | ShareGPT 格式之對話 |
| `instruction` | string | Alpaca 指令（部分任務為空） |
| `input` | string | 任務輸入（與 `messages[0].content` 相同） |
| `output` | string | 標準答案 |
| `task` | string | 任務類別（NER / 文本理解 / 結構化 / 條號互換） |

| 統計項目 | 數值 |
|---|---|
| 總筆數 | 171 |
| 任務類型 | 4 類 |
| 切分 | 無（使用者自行切分） |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

台灣法律 NLP 長期缺乏針對具體任務之標註資料，多數研究只能以判決書原文做 CPT。本資料集鎖定四類基礎任務，希望建立一個「可以直接跑起來」之 baseline 資料，作為後續擴充之種子。

### Source Data

#### Data Collection and Processing

- **NER**：從司法院判決書中抽取片段，由 `gpt-4o` 依規則產生問題與答案；
- **語意理解**：同上，判決書片段改寫為理解題；
- **文本結構化**：無特定來源，由 curator 設計之 prompt 產生 JSON / Markdown 範例；
- **條號互換**：參考[行政院公文書寫註解說明](https://announce.ndhu.edu.tw/message_3/1505966239/%E9%99%84%E4%BB%B63.pdf)與[經濟部智慧財產局](https://www.tipo.gov.tw/tw/mp-1.html)之書寫慣例，由 `gpt-4o` 生成對應實例。

#### Who are the source data producers?

判決書原文來自司法院公開資料；NLP 任務之 QA pair 由 `gpt-4o` 產生並經 curator 篩選。

### Annotations

#### Annotation process

本資料集之問題與答案皆由 `gpt-4o` 生成，curator 進行格式檢查與顯著錯誤過濾，未進行大規模人工重標。

#### Who are the annotators?

`gpt-4o` + curator。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
原始判決書依司法院公開規則已部分匿名（例如「甲○○」），本資料集於改寫時亦使用虛構姓名（如「張三豐」）。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* **規模極小**：171 筆不足以單獨訓練專門模型，僅適合做 baseline 或 few-shot 實驗；
* **LLM 生成品質依賴**：答案正確性依賴 `gpt-4o` 生成品質，存在少量錯誤或不一致之可能；
* **任務分布不均**：四類任務之筆數分布未必均衡；
* **條號互換規則之來源**：目前僅涵蓋常見書寫慣例，部分特殊編號（如「第一之一條」）之涵蓋可能不足。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者：
* 將本資料集視為 baseline，搭配其他法律領域資料集（如 `tw-legal-benchmark-v1`、`tw-law-article-qa`）一起訓練；
* 使用前對 `task` 欄位進行分層，按任務觀察模型表現；
* 若需大規模 NER 訓練，建議以本資料集作為 prompt 範本，再以規則或弱標方式擴增。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-legal-nlp,
  title        = {tw-legal-nlp: Traditional Chinese Legal NLP Task Dataset for Taiwan},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-legal-nlp}},
  note         = {171 multi-task Taiwan legal NLP examples (NER / understanding / structuring / article number conventions).}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
