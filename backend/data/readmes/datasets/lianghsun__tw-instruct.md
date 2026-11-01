---
license: cc-by-nc-sa-4.0
language:
- zh
tags:
- Taiwan
- ROC
- instruct
- chat
size_categories:
- 100K<n<1M
---
# Dataset Card for tw-instruct

<!-- Provide a quick summary of the dataset. -->
**tw-instruct** 是針對「臺灣語境」設計之大規模合成繁體中文指令對話集，每筆樣本含 `task` 類別、原始指令、對話與輸出，是 [lianghsun/tw-instruct-500k](https://huggingface.co/datasets/lianghsun/tw-instruct-500k) 與 [lianghsun/tw-instruct-500k-2511](https://huggingface.co/datasets/lianghsun/tw-instruct-500k-2511) 的母資料集。

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
本資料集為合成資料集（synthetic dataset），由 reference-based 與 reference-free 兩種子流程產生：
* **reference-based**：以 Llama-3.2-Taiwan 訓練語料中的繁中文本作為參考，請 LLM 根據文本生成對應領域的指令對話。
* **reference-free**：以開源 seed prompts（[Self-Instruct](https://github.com/yizhongw/self-instruct)、[HuggingFaceH4/self-instruct-seed](https://huggingface.co/datasets/HuggingFaceH4/self-instruct-seed) 等）為起點，引導 LLM 生成以臺灣為場景之對話。

每筆樣本含 `task` 欄位（任務類型，如「開放性問答」「摘要」「翻譯」等），方便下游做任務分流／取樣。

- **Curated by:** [Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** Traditional Chinese
- **License:** cc-by-nc-sa-4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/tw-instruct](https://huggingface.co/datasets/lianghsun/tw-instruct)
- **500k subset:** [lianghsun/tw-instruct-500k](https://huggingface.co/datasets/lianghsun/tw-instruct-500k)
- **Refreshed (messages format):** [lianghsun/tw-instruct-500k-2511](https://huggingface.co/datasets/lianghsun/tw-instruct-500k-2511)
- **Paper:** TBA

## Uses

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->
* 訓練具備臺灣語境之繁中對話模型。
* 與其他 instruction 資料集混訓，補強模型在臺灣社會議題上的覆蓋。
* 依 `task` 欄位做領域取樣，建立特定領域對話子集。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
* 不適用作為事實型問答之單一來源。
* 不允許未經授權之商用（cc-by-nc-sa-4.0）。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```jsonl
{
  "task": "開放性問答",
  "conversations": [
    {"from": "human", "value": "..."},
    {"from": "gpt", "value": "..."}
  ],
  "instruction": "",
  "input": "...",
  "output": "..."
}
```

格式採 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory/tree/main/data) 風格。若需 OpenAI `messages` 格式，可使用 [tw-instruct-500k-2511](https://huggingface.co/datasets/lianghsun/tw-instruct-500k-2511)。

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->
繁中開源指令資料常缺乏「臺灣語境」的針對性設計，導致訓練後的模型「會講中文，但對臺灣不了解」。本資料集以 reference-based 方法把臺灣社會的文本知識嵌入對話內，並以 `task` 欄位記錄任務類別，提供更細緻的取樣彈性。

### Source Data

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->
1. 蒐集臺灣繁中文本（新聞、政府網頁、維基條目等）作為 reference。
2. 設計／引用開源 seed prompts 作為 reference-free 起點。
3. 以 GPT-4o、Qwen2.5-14B-Instruct 等 LLM 生成對話內容。
4. 為每筆樣本標註 `task` 類別。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->
* 參考文本來自臺灣公開語料。
* 對話內容由 LLM 自動合成。

### Annotations

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->
`task` 欄位由生成 prompt 直接指定；無人工標註。

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->
無人工標註者。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
資料中的人名應屬公眾人物或合成虛構，如有遺漏 PII 請於 discussion 區提出排除。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
* 合成資料會繼承來源 LLM 的偏誤。
* 部分樣本仍可能出現非臺灣社會用語，已盡力過濾。
* 非台灣專屬的指令（reference-free 部分）仍佔一定比例。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->
若計畫商用，請改用 cc-by-nc-sa-4.0 之外的對話資料集，或主動取得授權。新版訓練流程建議使用 [tw-instruct-500k-2511](https://huggingface.co/datasets/lianghsun/tw-instruct-500k-2511)（messages 格式）。

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```bibtex
@misc{tw_instruct,
  title        = {tw-instruct: Synthetic Instruction Dataset for Taiwan Context},
  author       = {Huang, Liang Hsun},
  year         = {2024},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/tw-instruct}}
}
```

## Dataset Card Authors

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
