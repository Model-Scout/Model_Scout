---
license: cc-by-sa-4.0
language:
- zh
task_categories:
- question-answering
- multiple-choice
tags:
- medical
- emergency-medicine
- board-exam
- benchmark
- Taiwan
- zh-tw
pretty_name: Taiwan Emergency Medicine Board Exam Benchmark
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: question
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: E
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 980113
    num_examples: 1719
  download_size: 980113
  dataset_size: 980113
configs:
- config_name: default
  data_files:
  - split: train
    path: tw_ed_exam.jsonl
---
# Dataset Card for tw-emergency-medicine-bench

<!-- Provide a quick summary of the dataset. -->
tw-emergency-medicine-bench 是一個以台灣衛生福利部急診醫學科專科醫師甄審筆試為基礎之繁體中文醫學評測資料集，包含 1,719 題選擇題。資料採 [Formosa-bench](https://huggingface.co/datasets/lianghsun/Formosa-bench) 評測集之欄位格式（`question` / `A` / `B` / `C` / `D` / `E` / `answer`），可直接用於語言模型之 zero-shot 或 few-shot 多選題評測。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集源自台灣衛生福利部所辦理之「急診醫學科專科醫師甄審筆試試題」公開題庫。每題由臨床情境描述（症狀、病史、理學檢查、實驗室數值等）與選項組成，並附帶標準答案。題目同時包含 4 選項（A–D）與 5 選項（A–E）兩種題型：

| 選項數 | 題數 |
|---|---|
| 5 選項（A–E） | 999 |
| 4 選項（A–D） | 720 |

為對齊 [Formosa-bench](https://huggingface.co/datasets/lianghsun/Formosa-bench) 之評測欄位格式，每題之選項已拆解為獨立欄位 `A` / `B` / `C` / `D` / `E`，4 選項題型之 `E` 欄位為空字串。

本資料集為 [yuhsintw/TW_ED_exam](https://huggingface.co/datasets/yuhsintw/TW_ED_exam) 之延伸版本，進行下列處理：

* 移除 JSON 檔案中之 BOM 字元與其 key；
* 去除字串值（特別是答案欄位）之多餘尾隨空白；
* 重新命名檔案為小寫格式；
* 將選項文字由 `(A)...(B)...(C)...` 形式拆解為獨立欄位；
* 修正個別標籤錯誤（例如某題選項 `(H)` 實為 `(E)` 之誤植，已修正）。

上述前 5 項清理已於原始 repository 提出 [PR #2](https://huggingface.co/datasets/yuhsintw/TW_ED_exam/discussions/2)。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-SA 4.0
- **Exam Authority:** [中華民國衛生福利部](https://www.mohw.gov.tw/)

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-emergency-medicine-bench](https://huggingface.co/datasets/lianghsun/tw-emergency-medicine-bench/)
- **Upstream Dataset:** [yuhsintw/TW_ED_exam](https://huggingface.co/datasets/yuhsintw/TW_ED_exam)
- **Format Reference:** [lianghsun/Formosa-bench](https://huggingface.co/datasets/lianghsun/Formosa-bench)
- **Exam Authority:** [中華民國衛生福利部](https://www.mohw.gov.tw/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 評測繁體中文語言模型在台灣急診醫學領域之多選題答題能力；
* 作為 Formosa-bench 相容之臨床醫學評測子集；
* 研究語言模型在臨床決策情境之推理能力；
* 比較不同模型在台灣本土醫學考試之表現差異。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為真實臨床決策或醫療建議之依據，模型答題結果不等同於臨床專業判斷。
* 用於替代人工急診醫學教育與訓練。
* 作為非台灣醫療體系（如不同藥物名稱、健保制度、診療準則）之評測基準。
* 涉及病患照護之關鍵任務，應以合格醫師之專業判斷為準。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```jsonl
{
  "question": "10 個月大的男童因躁動且意識改變而被父母送至急診。母親說男童自昨晚開始就發生嘔吐和腹瀉...試問，下列何者對此病童是最適當的處置？",
  "A": "靜脈注射每公斤體重 1 ml 的 50% 葡萄糖水。",
  "B": "靜脈注射每公斤體重 10 ml 的 5% 葡萄糖水。",
  "C": "靜脈注射每公斤體重 5 ml 的 10% 葡萄糖水。",
  "D": "靜脈注射每公斤體重 2 ml 的 25% 葡萄糖水。",
  "E": "觀察生命徵象，等到正式實驗室的血糖報告出來後，再依據血糖值高低來進行處置。",
  "answer": "C"
}
```

| 欄位 | 型別 | 說明 |
|---|---|---|
| `question` | string | 臨床情境與題幹 |
| `A` | string | 選項 A |
| `B` | string | 選項 B |
| `C` | string | 選項 C |
| `D` | string | 選項 D |
| `E` | string | 選項 E（4 選項題為空字串） |
| `answer` | string | 正確答案（單一字母） |

| 統計項目 | 數值 |
|---|---|
| 總題數 | 1,719 |
| 5 選項題 | 999 |
| 4 選項題 | 720 |
| 格式 | Formosa-bench 相容 |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

現有之醫學評測基準（如 MedQA、USMLE）多以英語與美國醫療情境為主，繁體中文之台灣醫學評測基準長期稀缺。台灣急診醫學專科醫師甄審筆試為台灣醫療體系之正式專科考試，題目反映台灣臨床實務與用藥規範，具代表性。本資料集將公開題庫整理為 Formosa-bench 相容之欄位格式，方便直接用於繁體中文醫學模型之評測與跨題庫對照。

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

題目源自衛生福利部公開之急診醫學科專科醫師甄審筆試試題與答案。資料經 `yuhsintw/TW_ED_exam` 整理為 JSON 格式後，本 repository 進一步清理格式並轉換為 Formosa-bench 欄位結構。選項解析採用狀態機方式依 A→B→C→D→E 順序匹配，以避免將選項內文中之括號字母（如「Osborn (J) wave」）誤判為選項標籤。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

題目由台灣衛生福利部所聘之急診醫學專科領域命題委員撰寫。

### Annotations

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

答案（`answer`）為官方公告之標準答案。本資料集未加入額外標註。

目前初步人工修正了部分文字格式之正確性，但仍有部分內容需進一步檢查，例如：

* 不必要之空格
* 化學式之上下標
* 中文字與英文、數字間之空格

歡迎社群協助貢獻，讓資料集文字格式更加正確。

#### Who are the annotators?

原始題目與答案由衛生福利部之命題委員產出；本資料集之格式清理由 curator 執行。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
本資料集之臨床情境為考試命題之虛擬案例，不涉及真實病患之個人醫療資訊。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* 題目為選擇題形式，無法完整反映臨床決策之複雜度與情境不確定性。
* 題目涵蓋之臨床知識以考試大綱為準，可能不涵蓋急診醫學之全部實務面向。
* 部分題目可能因醫學進展而有臨床指引更新，標準答案以考試當時之標準為準。
* 文字格式仍有部分待清理（空格、符號、上下標等），可能影響模型之解析正確性。
* 4 選項與 5 選項題型並存，評測流程需自行處理 `E` 欄位為空字串之情形。
* 資料集中之臨床用語、藥品名稱、健保給付規範等具台灣在地化特性，不適用於其他醫療體系。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

使用本資料集進行模型評測時，建議同時參考臨床最新指引與實務見解。若發現題目內容或格式問題，歡迎透過 Hugging Face 之 Discussion 回饋。模型表現僅供參考，不得作為臨床照護決策依據。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw-emergency-medicine-bench,
  title        = {tw-emergency-medicine-bench: Taiwan Emergency Medicine Board Exam Benchmark},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-emergency-medicine-bench}},
  note         = {1,719 multiple-choice questions from Taiwan Emergency Medicine Board Exam in Formosa-bench compatible format.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
