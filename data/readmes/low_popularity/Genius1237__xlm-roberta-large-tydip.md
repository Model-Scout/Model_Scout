---
license: mit
datasets:
- Genius1237/TyDiP
language:
- en
- hi
- ko
- es
- ta
- fr
- vi
- ru
- af
- hu
metrics:
- accuracy
pipeline_tag: text-classification
---

# Multilingual Politeness Classification Model
This model is based on `xlm-roberta-large` and is finetuned on the English subset of the [TyDiP](https://github.com/Genius1237/TyDiP) dataset as discussed in the original paper [here](https://aclanthology.org/2022.findings-emnlp.420/).

## Languages
In the paper, this model was evaluated on English + 9 Languages (Hindi, Korean, Spanish, Tamil, French, Vietnamese, Russian, Afrikaans, Hungarian). Given the model's good performance and XLMR's cross lingual abilities, it is likely that this finetuned model can be used for more languages as well.

## Evaluation
The politeness classification accuracy scores on 10 languages from the TyDiP test set are mentioned below.

| lang | acc   |
|------|-------|
| en   | 0.892 |
| hi   | 0.868 |
| ko   | 0.784 |
| es   | 0.84  |
| ta   | 0.78  |
| fr   | 0.82  |
| vi   | 0.844 |
| ru   | 0.668 |
| af   | 0.856 |
| hu   | 0.812 |

## Usage
You can use this model directly with a text-classification pipeline
```python
from transformers import pipeline

classifier = pipeline(task="text-classification", model="Genius1237/xlm-roberta-large-tydip")

sentences = ["Could you please get me a glass of water", "mere liye पानी का एक गिलास ले आओ "]

print(classifier(sentences))
# [{'label': 'polite', 'score': 0.9076159000396729}, {'label': 'impolite', 'score': 0.765066385269165}]
```

More advanced usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained('Genius1237/xlm-roberta-large-tydip')
model = AutoModelForSequenceClassification.from_pretrained('Genius1237/xlm-roberta-large-tydip')

text = "Could you please get me a glass of water"
encoded_input = tokenizer(text, return_tensors='pt')

output = model(**encoded_input)
prediction = torch.argmax(output.logits).item()

print(model.config.id2label[prediction])
# polite
```

## Citation
```
@inproceedings{srinivasan-choi-2022-tydip,
    title = "{T}y{D}i{P}: A Dataset for Politeness Classification in Nine Typologically Diverse Languages",
    author = "Srinivasan, Anirudh  and
      Choi, Eunsol",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.420",
    doi = "10.18653/v1/2022.findings-emnlp.420",
    pages = "5723--5738",
    abstract = "We study politeness phenomena in nine typologically diverse languages. Politeness is an important facet of communication and is sometimes argued to be cultural-specific, yet existing computational linguistic study is limited to English. We create TyDiP, a dataset containing three-way politeness annotations for 500 examples in each language, totaling 4.5K examples. We evaluate how well multilingual models can identify politeness levels {--} they show a fairly robust zero-shot transfer ability, yet fall short of estimated human accuracy significantly. We further study mapping the English politeness strategy lexicon into nine languages via automatic translation and lexicon induction, analyzing whether each strategy{'}s impact stays consistent across languages. Lastly, we empirically study the complicated relationship between formality and politeness through transfer experiments. We hope our dataset will support various research questions and applications, from evaluating multilingual models to constructing polite multilingual agents.",
}
```