---
pretty_name: KLAID
viewer: true
language: ko
multilinguality:
- monolingual
license: cc-by-nc-nd-4.0
task_categories: 
- text-classification
task_ids: 
- multi-class-classification
---
# Dataset Card for KLAID
## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Other Inquiries](#other_inquiries)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)
## Dataset Description
- **Homepage:** [https://klaid.net](https://klaid.net)
- **Leaderboard:** [https://klaid.net](https://klaid.net)
- **Point of Contact:** [klaid@lawcompany.co.kr](klaid@lawcompany.co.kr)
### Dataset Summary
Korean Legal Artificial Intelligence Datasets(KLAID) is a dataset for the development of Korean legal artificial intelligence technology. This time we offer 1 task, which is legal judgment prediction(LJP).
### Supported Tasks and Leaderboards
Legal Judgment Prediction(LJP)
### Languages
`korean`
### How to use
```python
from datasets import load_dataset
# legal judgment prediction
dataset = load_dataset("lawcompany/KLAID", 'ljp')
```
## Dataset Structure
### Data Instances
#### ljp
An example of 'train' looks as follows.
```
{
   'fact': '피고인은 2022. 11. 14. 혈중알콜농도 0.123%의 술에 취한 상태로 승용차를 운전하였다.',
   'laws_service': '도로교통법 제148조의2 제3항 제2호,도로교통법 제44조 제1항',
   'laws_service_id': 7
}
```
 Other References
You can refer to each label's 'laws service content' [here](https://storage.googleapis.com/klaid/ljp/dataset/ljp_laws_service_content.json).
'Laws service content' is the statute([source](https://www.law.go.kr/)) corresponding to each label.

### Data Fields
#### ljp
+ "fact": a `string` feature
+ "laws_service": a `string` feature
+ "laws_service_id": a classification label, with 177 legal judgment values

[More Information Needed](https://klaid.net/tasks-1)
### Data Splits
#### ljp
+ train: 161,192
## Dataset Creation
### Curation Rationale
The legal domain is arguably one of the most expertise fields that require expert knowledge to comprehend. Natural language processing requires many aspects, and we focus on the dataset requirements. As a gold standard is necessary for the testing and the training of a neural model, we hope that our dataset release will help the advances in natural language processing in the legal domain, especially for those for the Korean legal system.
### Source Data
These are datasets based on Korean legal case data.
### Personal and Sensitive Information
Due to the nature of legal case data, personal and sensitive information may be included. Therefore, in order to prevent problems that may occur with personal and sensitive information, we proceeded to de-realize the legal case.
## Considerations for Using the Data
### Other Known Limitations
We plan to upload more data and update them as some of the court records may be revised from now on, based on the ever-evolving legal system.
## Additional Information
### Other Inquiries
[klaid@lawcompany.co.kr](klaid@lawcompany.co.kr)
### Licensing Information
Copyright 2022-present [Law&Company Co. Ltd.](https://career.lawcompany.co.kr/)

Licensed under the CC-BY-NC-ND-4.0
### Contributions
[More Information Needed]