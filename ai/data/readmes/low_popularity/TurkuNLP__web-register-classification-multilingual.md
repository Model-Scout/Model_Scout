---
license: apache-2.0
language:
- multilingual
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
tags:
- text-classification
- register
- web-register
- genre
---
# Web register classification (multilingual model)

A multilingual web register classifier, fine-tuned from [XLM-RoBERTa-large](https://huggingface.co/FacebookAI/xlm-roberta-large). 
The model is trained with the multilingual CORE corpora across five languages (English, Finnish, French, Swedish, Turkish) to classify documents based on the [CORE taxonomy](https://turkunlp.org/register-annotation-docs/). 
It can predict labels for the 100 languages covered by XLM-RoBERTa-large. The model achieves state-of-the-art performance in classifying web registers for the trained languages and has strong transfer performance (see Evaluation below).
It is designed to support the development of open language models and for linguists analyzing register variation.

## Model Details

### Model Description

- **Developed by:** TurkuNLP
- **Funded by:** The Research Council of Finland, Emil Aaltonen Foundation, University of Turku
- **Shared by:** TurkuNLP
- **Model type:** Language model
- **Language(s) (NLP):** English, Finnish, French, Swedish, Turkish
- **License:** apache-2.0
- **Finetuned from model:** FacebookAI/xlm-roberta-large

### Model Sources

- **Repository:** Coming soon!
- **Paper:** Coming soon!

## Register labels and their abbreviations

Below is a list of the register labels predicted by the model. Note that some labels are hierarchical; when a sublabel is predicted, its parent label is also predicted. 
For a more detailed description of the label scheme, see [here](https://turkunlp.org/register-annotation-docs/).

The main labels are uppercase. To only include these main labels in the predictions, simply slice the model's output to keep only the uppercase labels.

- **MT:** Machine translated or generated
- **LY:** Lyrical
- **SP:** Spoken
    - **it:** Interview
- **ID:** Interactive discussion
- **NA:** Narrative
    - **ne:** News report
    - **sr:** Sports report
    - **nb:** Narrative blog
- **HI:** How-to or instructions
    - **re:** Recipe
- **IN:** Informational description
    - **en:** Encyclopedia article
    - **ra:** Research article
    - **dtp:** Description of a thing or person
    - **fi:** Frequently asked questions
    - **lt:** Legal terms and conditions
- **OP:** Opinion
    - **rv:** Review
    - **ob:** Opinion blog
    - **rs:** Denominational religious blog or sermon
    - **av:** Advice
- **IP:** Informational persuasion
    - **ds:** Description with intent to sell
    - **ed:** News & opinion blog or editorial

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "TurkuNLP/multilingual-web-register-classification"

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_id).to(device)
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-large")

# Text to be categorized
text = "A text to be categorized"

# Tokenize text
inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

with torch.no_grad():
    outputs = model(**inputs)

# Apply sigmoid to the logits to get probabilities
probabilities = torch.sigmoid(outputs.logits).squeeze()

# Determine a threshold for predicting labels
threshold = 0.5
predicted_label_indices = (probabilities > threshold).nonzero(as_tuple=True)[0]

# Extract readable labels using id2label
id2label = model.config.id2label
predicted_labels = [id2label[idx.item()] for idx in predicted_label_indices]

print("Predicted labels:", predicted_labels)

```

## Training Details

### Training Data

The model was trained using the Multilingual CORE Corpora, which will be published soon.

### Training Procedure

#### Training Hyperparameters

- **Batch size:** 8
- **Epochs:** 21
- **Learning rate:** 0.00005
- **Precision:** bfloat16 (non-mixed precision)
- **TF32:** Enabled
- **Seed:** 42
- **Max Size:** 512 tokens

#### Inference time

Average inference time (across 1000 iterations), using a single NVIDIA A100 GPU and a batch size of one is **17 ms** for a single example. Wirh bigger batches, inference can be considerably faster.

## Evaluation

Micro-averaged F1 scores and optimized prediction thresholds for the five training languages (test set):

| Language | F1 (All labels) | F1 (Main labels) | Threshold |
| -------- | --------------- | ---------------- | ----------|
| English  | 0.72            | 0.75             | 0.40      |
| Finnish  | 0.79            | 0.82             | 0.45      | 
| French   | 0.75            | 0.78             | 0.45      | 
| Swedish  | 0.81            | 0.82             | 0.45      | 
| Turkish  | 0.77            | 0.78             | 0.45      | 
 
Micro-averaged F1 scores and optimized prediction thresholds for additional languages (zero-shot):


| Language   | F1 (All labels) | F1 (Main labels) | Threshold |
| ---------- | --------------- | ---------------- | ----------|
| Arabic     | 0.63            | 0.66             | 0.40      |
| Catalan    | 0.62            | 0.63             | 0.50      | 
| Spanish    | 0.62            | 0.67             | 0.65      | 
| Persian    | 0.71            | 0.70             | 0.35      | 
| Hindi      | 0.77            | 0.78             | 0.40      | 
| Indonesian | 0.60            | 0.61             | 0.30      | 
| Japanese   | 0.53            | 0.64             | 0.35      | 
| Norwegian  | 0.65            | 0.70             | 0.65      |
| Portuguese | 0.67            | 0.68             | 0.40      | 
| Urdu       | 0.81            | 0.83             | 0.35      | 
| Chinese    | 0.67            | 0.70             | 0.40      | 

## Technical Specifications

### Compute Infrastructure

- Mahti supercomputer (CSC - IT Center for Science, Finland)
- 1 x NVIDIA A100-SXM4-40GB

#### Software

- torch 2.2.1 
- transformers 4.39.3

## Citation

If you use this model, please cite the following publication:

```bibtex
@misc{henriksson2024untanglingunrestrictedwebautomatic,
      title={Untangling the Unrestricted Web: Automatic Identification of Multilingual Registers}, 
      author={Erik Henriksson and Amanda Myntti and Anni Eskelinen and Selcen Erten-Johansson and Saara Hellström and Veronika Laippala},
      year={2024},
      eprint={2406.19892},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.19892}, 
}
```

Earlier related work include the following:

```bibtex
@article{Laippala.etal2022,
  title = {Register Identification from the Unrestricted Open {{Web}} Using the {{Corpus}} of {{Online Registers}} of {{English}}},
  author = {Laippala, Veronika and R{\"o}nnqvist, Samuel and Oinonen, Miika and Kyr{\"o}l{\"a}inen, Aki-Juhani and Salmela, Anna and Biber, Douglas and Egbert, Jesse and Pyysalo, Sampo},
  year = {2022},
  journal = {Language Resources and Evaluation},
  issn = {1574-0218},
  doi = {10.1007/s10579-022-09624-1},
  url = {https://doi.org/10.1007/s10579-022-09624-1},
}

@article{Skantsi_Laippala_2023,
  title = {Analyzing the unrestricted web: The finnish corpus of online registers},
  doi = {10.1017/S0332586523000021},
  journal = {Nordic Journal of Linguistics},
  author = {Skantsi, Valtteri and Laippala, Veronika},
  year = {2023},
  pages = {1–31}
}
```

## Model Card Contact

Erik Henriksson, Hugging Face username: erikhenriksson