---
license: cc-by-nc-sa-4.0
language:
- en
- ru
- zh
- ko
- ur
- la
- ar
- de
- es
- fr
- hi
- it
- ja
- nl
- pt
tags:
- sft
- dpo
size_categories:
- 1M<n<10M
---

# Dataset Card for lianghsun/Everything-Instruct-Multilingual-DPO

<!-- Provide a quick summary of the dataset. -->

## Dataset Details
### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
這個資料集是分叉於 [rombodawg/Everything_Instruct_Multilingual](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual)，但在中文回答的部份透過 [opencc-python](https://github.com/yichen0831/opencc-python) 將簡體中文（zh-cn）轉成繁體中文（zh-tw）。除此之外，我們將資料集升級成具有 [DPO](https://arxiv.org/abs/2305.18290) 欄位，該 `rejected` 回覆是由 [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) `v2024.11.27` 生成，此資料集將用於 lianghsun/Llama-3.2-Taiwan-3B-Instruct 的 DPO 階段。

- **Curated by:** [Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)
- **Language(s) (NLP):** multilingual
- **License:** cc-by-nc-sa-4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [lianghsun/Everything-Instruct-Multilingual](https://huggingface.co/datasets/lianghsun/Everything-Instruct-Multilingual/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

本資料集可以用在 SFT 與 DPO 的訓練階段。

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
本資料集並不適合用在評測集或者是任何事實審核使用。

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

```yaml
{
  "instruction": "",
  "input": "",
  "rejected": ""
}
```

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->
具有多國語系的指令資料集鮮少，更不用說多國語系的偏好資料集（Preference dataset），故本資料集以 [rombodawg/Everything_Instruct_Multilingual](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual) 為基底資料集（foundation dataset），新增拒絕（rejected）回覆，使資料集更加全面，用戶可利用此資料集訓練模型進行多語系偏好學習。

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

1. **簡體中文轉繁體中文：** 本資料集將簡體中文轉成繁體中文。
2. **生成拒絕回覆：** 透過模型生成拒絕回覆，以建立偏好資料集。

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->
- **Foundation dataset:** [rombodawg/Everything_Instruct_Multilingual](https://huggingface.co/datasets/rombodawg/Everything_Instruct_Multilingual)
- **Rejected dataset:** [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct)

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->
無。

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->
無。

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

我們未針對原始資料進行 PII 檢測，但曾經收過 Hugging Face 系統信通知原始資料集內含有密鑰相關，請使用者再自行檢測。

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
任何人使用此資料集都應該要注意，原始資料內可能含有不同立場和情境的言論，請小心使用。

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
```yaml
@misc{huang2024everything,
  author = {Huang, Liang Hsun},
  title = {Everything-Instruct-Multilingual-DPO},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/lianghsun/Everything-Instruct-Multilingual-DPO}},
  note = {多國語系的指令服從資料集，可用於 SFT 或 DPO 訓練}
}
```

## More Information

本人僅能檢視繁體中文的部分，原始資料集含有中文的部分，大部分都是被要求翻譯成為中文（output），但經檢視中文的文本品質並不是很高水準，更甚至可能原始產生輸出的模型之中文能力低落，建議可以將有中文輸出的欄位刪除後再進行訓練。

*註：至此至今，我開始也懷疑原始資料集的多國語系指令回覆，是否也是低品質？*

但如果你缺少一個多國語系的指令資料集，這將是一個很好入門的資料集。

## Dataset Card Authors

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Dataset Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)