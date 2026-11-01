---
library_name: transformers
tags:
- citation
- text-classification
- science
license: apache-2.0
language:
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
base_model:
- distilbert/distilbert-base-multilingual-cased
---

# Citation Pre-Screening

<!-- Provide a quick summary of what the model is/does. -->

## Overview

<details>
<summary>Click to expand</summary>
  
- **Model type:** Language Model
- **Architecture:** DistilBERT
- **Language:** Multilingual
- **License:** Apache 2.0
- **Task:** Binary Classification (Citation Pre-Screening)
- **Dataset:** SIRIS-Lab/citation-parser-TYPE
- **Additional Resources:**
  - [GitHub](https://github.com/sirisacademic/citation-parser)
</details>

## Model description

The **Citation Pre-Screening** model is part of the [`Citation Parser`](https://github.com/sirisacademic/citation-parser) package and is fine-tuned for classifying citation texts as valid or invalid. This model, based on **DistilBERT**, is specifically designed for automated citation processing workflows, making it an essential component of the **Citation Parser** tool for citation metadata extraction and validation.

The model was trained on a dataset containing citation texts, with the labels `True` (valid citation) and `False` (invalid citation). The dataset contains 3599 training samples and 400 test samples, with each example consisting of citation-related text and a corresponding label. 

The fine-tuning process was done with the **DistilBERT-base-multilingual-cased** architecture, making the model capable of handling multilingual text, but it was evaluated on English citation data.

## Intended Usage

This model is intended to classify raw citation text as either a valid or invalid citation based on the provided input. It is ideal for automating the pre-screening process in citation databases or manuscript workflows.

## How to use

```python
from transformers import pipeline

# Load the model
citation_classifier = pipeline("text-classification", model="sirisacademic/citation-pre-screening")

# Example citation text
citation_text = "MURAKAMI, H等: 'Unique thermal behavior of acrylic PSAs bearing long alkyl side groups and crosslinked by aluminum chelate', 《EUROPEAN POLYMER JOURNAL》"

# Classify the citation
result = citation_classifier(citation_text)
print(result)
```

## Training

The model was trained using the **Citation Pre-Screening Dataset** consisting of:

- **Training data**: 3599 samples
- **Test data**: 400 samples

The following hyperparameters were used for training:

- **Model Path**: `distilbert/distilbert-base-multilingual-cased`
- **Batch Size**: 32
- **Number of Epochs**: 4
- **Learning Rate**: 2e-5
- **Max Sequence Length**: 512

## Evaluation Metrics

The model's performance was evaluated on the test set, and the following results were obtained:

| Metric               | Value  |
|----------------------|--------|
| **Accuracy**          | 0.95   |
| **Macro avg F1**      | 0.94   |
| **Weighted avg F1**   | 0.95   |

## Additional information

### Authors 

- SIRIS Lab, Research Division of SIRIS Academic.

### License

This work is distributed under a [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Contact
For further information, send an email to either [nicolau.duransilva@sirisacademic.com](mailto:nicolau.duransilva@sirisacademic.com) or [info@sirisacademic.com](mailto:info@sirisacademic.com).

