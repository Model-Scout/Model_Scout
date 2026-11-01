---
license: cc-by-nc-sa-4.0
language:
- zh
task_categories:
- text-generation
tags:
- reasoning
- math
- chain-of-thought
- Taiwan
size_categories:
- 1K<n<10K
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
    num_bytes: 18096664
    num_examples: 1881
  download_size: 18096664
  dataset_size: 18096664
configs:
- config_name: default
  data_files:
  - split: train
    path: datasets.jsonl
---
# Dataset Card for reasoning-base-20k-chat

<!-- Provide a quick summary of the dataset. -->
reasoning-base-20k-chat 是基於 [reasoning-base-20k](https://huggingface.co/datasets/lianghsun/reasoning-base-20k) 所建立的繁體中文推理問答資料集，包含 1,881 筆單輪問答對。內容以數學證明、微積分、代數、邏輯推理與事實查核為主，每筆回答均以逐步推理（step-by-step reasoning）方式呈現，適用於語言模型之推理能力微調。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集將推理任務轉化為繁體中文問答格式。每筆回答以結構化的逐步分析呈現，包含「理解問題」、「數學表示」、「展開推理」等段落，引導模型學習系統化的推理過程。

涵蓋的主題包括：
* **數學證明：** 數論、整除性、同餘、連續整數性質
* **微積分：** 積分技巧、反三角函式、部分分數分解
* **代數：** 線性運算元、範數、矩陣
* **邏輯推理與事實查核：** 針對聲稱或傳言進行分析與驗證
* **其他 STEM 主題：** 物理、統計、演算法

98.3% 的問答為繁體中文，少量為英文。

- **Curated by:** [Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/reasoning-base-20k-chat](https://huggingface.co/datasets/lianghsun/reasoning-base-20k-chat/)
- **Parent Dataset:** [lianghsun/reasoning-base-20k](https://huggingface.co/datasets/lianghsun/reasoning-base-20k)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集主要設計用於：
* 對語言模型進行繁體中文推理能力之 SFT 微調；
* 訓練模型以逐步推理方式回答數學與邏輯問題；
* 增強模型在 STEM 領域之繁體中文表現。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集不適用於下列用途：
* 作為數學教科書或參考答案之替代，因推理過程由模型生成，可能包含錯誤。
* 用於非推理導向的一般對話微調。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```jsonl
{
  "messages": "[{\"role\": \"system\", \"content\": \"\"}, {\"role\": \"user\", \"content\": \"...\"}, {\"role\": \"assistant\", \"content\": \"...\"}]",
  "instruction": "",
  "input": "證明兩個連續立方數的差無法被5整除...",
  "output": "**逐步分析問題並進行推理**..."
}
```

| 欄位 | 說明 |
|---|---|
| `messages` | JSON 編碼之 messages 陣列（system + user + assistant） |
| `instruction` | 額外指令（本資料集中均為空） |
| `input` | 使用者問題 |
| `output` | 逐步推理回答 |

| 統計項目 | 數值 |
|---|---|
| 問答對數 | 1,881 |
| 對話格式 | 單輪問答 |
| 繁體中文比例 | 98.3% |

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

現有的推理資料集多以英文為主，繁體中文推理訓練資料嚴重不足。本資料集將 reasoning-base-20k 中的推理任務翻譯並改寫為繁體中文，使語言模型能以中文進行系統化推理。

### Source Data

#### Data Collection and Processing

本資料集以 [reasoning-base-20k](https://huggingface.co/datasets/lianghsun/reasoning-base-20k) 為基礎，將推理問題與解答轉化為繁體中文問答格式。

#### Who are the source data producers?

原始推理問題來源多元，繁體中文轉化由大型語言模型完成。

### Annotations

#### Annotation process

本資料集不包含額外標註。

#### Who are the annotators?

不適用。

#### Personal and Sensitive Information

本資料集為數學與推理問答，不涉及個人資訊或敏感資料。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

* 推理過程由語言模型生成，數學證明之嚴謹性可能不足。
* `messages` 欄位為 JSON 字串而非原生 list，使用時需先解析。
* 部分翻譯可能存在數學術語不一致之情形。
* 1,881 筆的規模對於推理訓練而言較小，建議搭配其他推理資料集使用。

### Recommendations

建議使用者在數學敏感之應用場景中，對模型推理結果進行人工驗證。

## Citation

```bibtex
@misc{reasoning-base-20k-chat,
  title        = {reasoning-base-20k-chat: Traditional Chinese Reasoning QA Dataset},
  author       = {Liang Hsun Huang},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/reasoning-base-20k-chat}},
  note         = {1,881 step-by-step reasoning QA pairs in Traditional Chinese, derived from reasoning-base-20k.}
}
```

## Dataset Card Authors

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Liang Hsun Huang](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
