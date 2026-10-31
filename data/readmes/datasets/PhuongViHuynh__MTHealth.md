---
configs:
- config_name: tiengviet
  data_files:
    - split: train
      path: tiengviet/train.csv
    - split: validation
      path: tiengviet/val.csv
    - split: test
      path: tiengviet/test.csv
- config_name: tiengphap
  data_files:
    - split: train
      path: tiengphap/train.csv
    - split: test
      path: tiengphap/test.csv
    - split: validation
      path: tiengphap/val.csv
- config_name: tienganh1
  data_files:
    - split: train
      path: tienganh1/train.csv
    - split: test
      path: tienganh1/test.csv
    - split: validation
      path: tienganh1/val.csv
- config_name: tienganh2
  data_files:
    - split: train
      path: tienganh2/train.csv
    - split: test
      path: tienganh2/test.csv
    - split: validation
      path: tienganh2/val.csv
- config_name: tienghan
  data_files:
    - split: train
      path: tienghan/train.csv
    - split: test
      path: tienghan/test.csv
    - split: validation
      path: tienghan/val.csv

annotations_creators:
- human-annotated
language_creators:
- found
language:
- vi
- fr
- ko
- en
license:
- cc-by-4.0
multilingual:
- multilingual
pretty_name: Multilingual Mental Health QA Dataset
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- open-domain-qa
---


# Dataset Card for Multilingual Mental Health QA Dataset

## Dataset Summary

This dataset contains multilingual question-answer pairs derived from expert-level mental health resources in Vietnamese, French, English and Korean. The data is split into `train`, `validation`, and `test` sets for each language. Each entry includes a question and a corresponding answer grounded in trusted mental health documents.

This dataset aims to support research in multilingual QA, cross-lingual retrieval, and health-oriented natural language understanding.

## Supported Tasks and Leaderboards

- **Multilingual Open-domain Question Answering**
- **Cross-lingual Transfer in Mental Health**
- **Multimodal QA** (if later expanded)

## Languages

- Vietnamese (`vi`)
- French (`fr`)
- Korean (`ko`)
- English (`en`)
## Dataset Structure

Each Excel file contains the following columns:

| Column Name | Description                     |
|-------------|---------------------------------|
| `STT`        | Unique STT              |
| `id`        | Unique identifier               |
| `question`  | The question in a given language |
| `answer`    | The corresponding answer         |
| `context`    | Context extract from source    |

### Example entry:

```json
{
  "id": "fr_0003",
  "question": "Comment gérer les crises de panique ?",
  "answer": "Les crises de panique peuvent être gérées avec des techniques de respiration, de pleine conscience et, dans certains cas, par la thérapie ou la médication.",
  "source": "guide_anxiete_fr.pdf"
}


Contact:
If any links are broken, please get in touch with me to fix!

Phuong Vi Huynh
Email: hpv1812@gmail.com
GitHub: 