---
task_categories:
- translation
language:
- en
- ko
size_categories:
- 1K<n<10K
---


# Parenthetical Terminology Translation (PTT) Dataset

## Overview

The Parenthetical Terminology Translation (PTT) dataset is designed for evaluating and training models in translating technical terms while maintaining clarity and accuracy in specialized fields. It features English-Korean bilingual sentence pairs where the original English technical terms are displayed in parentheses alongside their Korean translations.  The primary dataset covers the artificial intelligence (AI) domain, with additional out-of-domain (OOD) datasets for physics and biology used for evaluation purposes.

## Dataset Structure

- **Languages**: English, Korean
- **Domains**:
  - **Main Domain**: Artificial Intelligence (AI)
  - **Out-of-Domain (OOD) Evaluation**: Biology, Physics
- **Translation Format**: Each technical term in the Korean translation is followed by its original English term in parentheses.

### Dataset Splits

#### AI Domain (Main Dataset)

| Split      | Number of Sentence Pairs |
|------------|--------------------------|
| Training   | 1,116                    |
| Validation | 144                      |
| Test       | 138                      |

#### Out-of-Domain (OOD) Datasets

| Domain                      | Number of Sentence Pairs |
|-----------------------------|--------------------------|
| Subcellular Processes (q-bio.SC)   | 171                      |
| Mesoscale and Nanoscale Physics (cond-mat.mes-hall) | 60                       |
| High Energy Physics (hep-ex) | 168                      |



## Data Fields

Each sentence pair in the dataset contains the following fields:

- **terms_set_index**: An identifier for the set of technical terms associated with the sentence.
- **terms**: A list of technical terms used in the sentence.
- **duplicated**: A Boolean flag indicating whether the same technical term appears more than once in the sentence (True or False).
- **english**: The original English sentence containing the technical terms.
- **korean**: The Korean translation of the source sentence, with the English technical terms presented in parentheses.



## Loading the Dataset

You can load the dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("PrompTart/PTT_en_ko")
```


## Citation

If you use this dataset in your research, please cite it as follows:

```tex
@inproceedings{myung-etal-2024-efficient,
    title = "Efficient Technical Term Translation: A Knowledge Distillation Approach for Parenthetical Terminology Translation",
    author = "Jiyoon, Myung and
      Park, Jihyeon  and
      Son, Jungki  and
      Lee, Kyungro  and
      Han, Joohyung",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.wmt-1.129/",
    doi = "10.18653/v1/2024.wmt-1.129",
    pages = "1410--1427",
    abstract = "This paper addresses the challenge of accurately translating technical terms, which are crucial for clear communication in specialized fields. We introduce the Parenthetical Terminology Translation (PTT) task, designed to mitigate potential inaccuracies by displaying the original term in parentheses alongside its translation. To implement this approach, we generated a representative PTT dataset using a collaborative approach with large language models and applied knowledge distillation to fine-tune traditional Neural Machine Translation (NMT) models and small-sized Large Language Models (sLMs). Additionally, we developed a novel evaluation metric to assess both overall translation accuracy and the correct parenthetical presentation of terms. Our findings indicate that sLMs did not consistently outperform NMT models, with fine-tuning proving more effective than few-shot prompting, particularly in models with continued pre-training in the target language. These insights contribute to the advancement of more reliable terminology translation methodologies."
}
```


## Contact

For questions or feedback, please contact [jiyoon0424@gmail.com](mailto:jiyoon0424@gmail.com).
