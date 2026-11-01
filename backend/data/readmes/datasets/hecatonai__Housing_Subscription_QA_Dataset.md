---
task_categories:
- question-answering
language:
- ko
tags:
- finance
size_categories:
- n<1K
config_names:
  - "2024"
  - "2022"
  - "2021"

configs:
  - config_name: "2024"
    data_files:
      - split: "train"
        path: "2024/*"
  - config_name: "2022"
    data_files:
      - split: "train"
        path: "2022/*"
  - config_name: "2021"
    data_files:
      - split: "train"
        path: "2021/*"
---
# Dataset Card for Dataset Name

<!-- Provide a quick summary of the dataset. -->

This dataset card aims to be a base template for new datasets. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md?plain=1).


### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->

- **Language(s) (NLP):** Korean


### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Origin of Data:** [2024 주택청약 FAQ](https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?search=%EC%A3%BC%ED%83%9D&srch_dept_nm=&srch_dept_id=&srch_usr_nm=&srch_usr_titl=Y&srch_usr_ctnt=&search_regdate_s=&search_regdate_e=&psize=10&s_category=&p_category=&lcmspage=1&id=4765)



## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```
[
  {
    'question' : "...",
    'answer' : "...", 
  },
  {
    "..."
  },

  ...
]
```

## Data Fields

* question : Question of korea's Housing Subscription.
* answer : Answer for Question same blocks.