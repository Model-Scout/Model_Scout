---
license: apache-2.0
language:
- zh
task_categories:
- question-answering
- text-generation
- multiple-choice
tags:
- legal
- bar-exam
- Taiwan
- ROC
- zh-tw
size_categories:
- n<1K
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 189143
    num_examples: 269
  - name: test
    num_bytes: 20129
    num_examples: 30
  download_size: 209272
  dataset_size: 209272
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
  - split: test
    path: test.jsonl
---
# Dataset Card for tw-bar-examination-2020-chat

<!-- Provide a quick summary of the dataset. -->
tw-bar-examination-2020-chat 是一個中華民國 2020 年律師考試選擇題之 Alpaca 格式微調資料集，合計 299 題（train 269、test 30）。每題包含統一提示語、題目與四個選項，以及正確答案字母，適用於微調繁體中文語言模型於台灣法律選擇題作答任務。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集源自 [Jamie0510/taiwan-law-exam](https://huggingface.co/datasets/Jamie0510/taiwan-law-exam) 中之 2020 年律師考試題目，整合其四大類科後進行後處理：去除欄位缺失之題目，並統一轉為 Alpaca 三欄格式（`instruction` / `input` / `output`）。每題之 `instruction` 欄為固定提示語「請在下列的單一選擇題中，選出正確的答案，並且只回答 A, B, C, D 其中一個字代表正確答案」。

本資料集作為 SFT 訓練素材設計，建議與 [lianghsun/tw-legal-benchmark-v1](https://huggingface.co/datasets/lianghsun/tw-legal-benchmark-v1) 搭配使用：先以本資料集進行微調，使模型熟悉台灣法律題型與單選題作答格式後，再以 benchmark 進行評測，通常可獲得較佳表現。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese（部分題目包含英文內容，如國際私法題）
- **License:** Apache 2.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-bar-examination-2020-chat](https://huggingface.co/datasets/lianghsun/tw-bar-examination-2020-chat/)
- **Upstream Dataset:** [Jamie0510/taiwan-law-exam](https://huggingface.co/datasets/Jamie0510/taiwan-law-exam)
- **Companion Benchmark:** [lianghsun/tw-legal-benchmark-v1](https://huggingface.co/datasets/lianghsun/tw-legal-benchmark-v1)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 微調繁體中文語言模型於台灣法律選擇題作答任務；
* 作為 tw-legal-benchmark-v1 評測前之 warm-up SFT 素材，幫助模型熟悉單選題回答格式；
* 訓練模型在法律題幹中識別關鍵要件並選出正確答案之能力；
* 法律教育應用之原型開發。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為正式律師考試準備之主要教材，因資料量僅 299 題且年份限定為 2020。
* 作為法律諮詢或案件分析之依據。
* 涵蓋台灣律師考試之完整題庫，本資料集僅為 2020 年單一年度。
* 非中華民國法律體系之訓練或評測。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```jsonl
{
  "instruction": "請在下列的單一選擇題中，選出正確的答案，並且只回答 A, B, C, D 其中一個字代表正確答案",
  "input": "下列何行為未違背法律倫理規範之要求？ A: 法官於案件審理程序中，對於某法律爭議，對當事人表示法官自己所持之法律見解，B: 法官於臨退休前 2 個月，將其所有原定之言詞辯論期日的案件，全部取消，改訂退休日後的期日，C: 法官於下班之後，代親友撰寫訴狀並收取一定費用，D: 地方法院院長基於司法監督，為維持審判效率，指示某一法官就某一案件應於 10 日內終結之",
  "output": "D"
}
```

| 欄位 | 說明 |
|---|---|
| `instruction` | 固定提示語（單選題作答指示） |
| `input` | 題幹與四個選項（A–D） |
| `output` | 正確答案字母（單一字元） |

| 切分 | 筆數 | 說明 |
|---|---|---|
| train | 269 | 四類科合併後抽取 90% |
| test | 30 | 四類科合併後抽取 10% |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

繁體中文語言模型在面對台灣律師考試類型之單選題時，經常因作答格式不一致而無法正確對齊評測流程。本資料集以 Alpaca 格式統一題幹與提示語，讓模型在 SFT 階段即可學會單選題之固定作答格式，從而在下游 benchmark 評測時獲得更穩定之表現。

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

題目來自 `Jamie0510/taiwan-law-exam` 之 2020 年律師考試四大類科。處理步驟：
1. 合併四類科之題目；
2. 過濾掉欄位缺失或格式異常之題目；
3. 統一 `instruction` 欄為固定提示語；
4. 將題幹與選項合併為 `input` 欄位；
5. 將答案字母置於 `output` 欄位；
6. 隨機抽取 90% 作為 train，10% 作為 test。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

原始題目由中華民國考選部主辦之律師考試命題委員撰寫，屬於公開之國家考試題目。

### Annotations

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

答案（`output`）為官方公告之標準答案。本資料集未加入額外標註。

#### Who are the annotators?

原始題目與答案由考選部之命題與閱卷委員產出。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
本資料集為公開之國家考試題目，不包含個人資訊或敏感資料。題幹中之案例均為命題虛構之情境。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* 資料僅涵蓋 2020 單一年度律師考試，題目分佈未必涵蓋全部法律領域。
* 題目數量小（299 題），不足以單獨支撐完整之法律領域訓練。
* 台灣法律隨時間修訂，2020 年之正確答案未必適用於現行法規。
* 部分題目包含英文內容（如國際私法），對單語模型可能造成額外難度。
* Alpaca 格式之 instruction 為單一固定提示，模型可能過度擬合此提示模式。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

建議使用者：
* 將本資料集作為 SFT warm-up 素材，搭配其他法律問答或條文資料集（如 `tw-law-article-qa`、`tw-processed-law-article`）共同訓練；
* 評測時使用 `tw-legal-benchmark-v1` 以獲得較全面之法律能力檢視；
* 涉及實務應用時，應以最新法規進行交叉驗證。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-bar-examination-2020-chat,
  title        = {tw-bar-examination-2020-chat: Taiwan 2020 Bar Examination SFT Dataset},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-bar-examination-2020-chat}},
  note         = {299 multiple-choice questions from the 2020 ROC bar examination in Alpaca format.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
