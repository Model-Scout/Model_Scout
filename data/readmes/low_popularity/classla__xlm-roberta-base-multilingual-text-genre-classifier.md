---
license: cc-by-sa-4.0
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
- genre
- text-genre
widget:
- text: >-
    On our site, you can find a great genre identification model which you can
    use for thousands of different tasks. For free!
  example_title: English
- text: >-
    Na naši spletni strani lahko najdete odličen model za prepoznavanje žanrov,
    ki ga lahko uporabite pri na tisoče različnih nalogah. In to brezplačno!
  example_title: Slovene
- text: >-
    Sur notre site, vous trouverez un modèle d'identification de genre très
    intéressant que vous pourrez utiliser pour des milliers de tâches
    différentes. C'est gratuit !
  example_title: French
datasets:
- TajaKuzman/X-GENRE-text-genre-dataset
base_model:
- FacebookAI/xlm-roberta-base
---

# X-GENRE classifier - multilingual text genre classifier

Text classification model based on [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base)
and fine-tuned on a [multilingual manually-annotated X-GENRE genre dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset).
The model can be used for automatic genre identification, applied to any text in a language, supported by the `xlm-roberta-base`.

The details on the model development, the datasets and the model's in-dataset, cross-dataset and multilingual performance are provided in the paper [Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models](https://www.mdpi.com/2504-4990/5/3/59) (Kuzman et al., 2023).

The model can also be downloaded from the [CLARIN.SI repository](http://hdl.handle.net/11356/1961).

If you use the model, please cite the paper:

```
@article{kuzman2023automatic,
  title={Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models},
  author={Kuzman, Taja and Mozeti{\v{c}}, Igor and Ljube{\v{s}}i{\'c}, Nikola},
  journal={Machine Learning and Knowledge Extraction},
  volume={5},
  number={3},
  pages={1149--1175},
  year={2023},
  publisher={MDPI}
}
```

## AGILE - Automatic Genre Identification Benchmark

We set up a benchmark for evaluating robustness of automatic genre identification models to test their usability
for the automatic enrichment of large text collections with genre information. The benchmark comprises 11 European languages and two test datasets.
You are welcome to submit your entry at the [benchmark's GitHub repository](https://github.com/TajaKuzman/AGILE-Automatic-Genre-Identification-Benchmark/tree/main).

The model outperforms all other technologies, including GPT models that are used in a zero-shot scenario.

Results on the English test dataset (EN-GINCO):

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)           | en-ginco       |      0.687 |      0.684 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                             | en-ginco       |      0.62  |      0.735 |
| Llama 3.3 (70B) (zero-shot)                                                                                        | en-ginco       |      0.586 |      0.684 |
| Gemma 2 (27B) (zero-shot)                                                                                          | en-ginco       |      0.564 |      0.603 |
| Gemma 3 (27B) (zero-shot)                                                                                          | en-ginco       |      0.541 |      0.672 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                   | en-ginco       |      0.534 |      0.632 |
| Support Vector Machine                                                                                             | en-ginco       |      0.514 |      0.489 |
| GPT-3.5-Turbo (zero-shot)                                                                                          | en-ginco       |      0.494 |      0.625 |
| DeepSeek-R1 14B (zero-shot)                                                                                        | en-ginco       |      0.293 |      0.229 |
| Dummy Classifier (stratified)                                                                                      | en-ginco       |      0.088 |      0.154 |
| Dummy classifier (most frequent)                                                                                   | en-ginco       |      0.032 |      0.169 |

Results on the multilingual test dataset (X-GINCO), comprising instances in Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian:

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)           | x-ginco        |      0.847 |      0.845 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                             | x-ginco        |      0.776 |      0.769 |
| Llama 3.3 (70B) (zero-shot)                                                                                        | x-ginco        |      0.741 |      0.738 |
| Gemma 3 (27B) (zero-shot)                                                                                          | x-ginco        |      0.739 |      0.733 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                   | x-ginco        |      0.688 |      0.67  |
| GPT-3.5-Turbo (zero-shot)                                                                                          | x-ginco        |      0.627 |      0.622 |
| Gemma 2 (27B) (zero-shot)                                                                                          | x-ginco        |      0.612 |      0.593 |
| DeepSeek-R1 14B (zero-shot)                                                                                        | x-ginco        |      0.197 |      0.204 |
| Support Vector Machine                                                                                             | x-ginco        |      0.166 |      0.184 |
| Dummy Classifier (stratified)                                                                                      | x-ginco        |      0.106 |      0.113 |
| Dummy classifier (most frequent)                                                                                   | x-ginco        |      0.029 |      0.133 |

(The multilingual test dataset is easier than the English one, as the vague label "Other" and instances that were predicted with a confidence score below 0.80 were not included in the test dataset.)

For language-specific results, see [the AGILE benchmark](https://github.com/TajaKuzman/AGILE-Automatic-Genre-Identification-Benchmark).


## Intended use and limitations

### Usage

Use example for prediction on a dataset, using batch processing, is available via [Google Collab](https://colab.research.google.com/drive/1yC4L_p2t3oMViC37GqSjJynQH-EWyhLr?usp=sharing).

An example of preparing data for genre identification and post-processing of the results can be found [here](https://github.com/TajaKuzman/Applying-GENRE-on-MaCoCu-bilingual) where we applied X-GENRE classifier to the English part of [MaCoCu](https://macocu.eu/) parallel corpora.

For reliable results, genre classifier should be applied to documents of sufficient length (the rule of thumb is at least 75 words).
Predictions with confidence scores below 0.8 should not be used. 
In our experience annotating large web corpora in various European languages, this occurs in approximately 4% of cases. 
We label these instances as "Mix." 
Furthermore, the label "Other" can be used as another indicator of low confidence of the predictions, 
as it often indicates that the text does not have enough features of any genre, and these predictions can be discarded as well.


### Use examples

```python
from simpletransformers.classification import ClassificationModel
model_args= {
            "num_train_epochs": 15,
            "learning_rate": 1e-5,
            "max_seq_length": 512,
            "silent": True
            }
model = ClassificationModel(
    "xlmroberta", "classla/xlm-roberta-base-multilingual-text-genre-classifier", use_cuda=True,
    args=model_args
    
)
predictions, logit_output = model.predict(["How to create a good text classification model? First step is to prepare good data. Make sure not to skip the exploratory data analysis. Pre-process the text if necessary for the task. The next step is to perform hyperparameter search to find the optimum hyperparameters. After fine-tuning the model, you should look into the predictions and analyze the model's performance. You might want to perform the post-processing of data as well and keep only reliable predictions.", 
                                        "On our site, you can find a great genre identification model which you can use for thousands of different tasks. With our model, you can fastly and reliably obtain high-quality genre predictions and explore which genres exist in your corpora. Available for free!"]
                                        )
predictions
# Output: array([3, 8])

[model.config.id2label[i] for i in predictions]
# Output: ['Instruction', 'Promotion']

```


## X-GENRE categories

For details on the X-GENRE categories, refer to the [X-GENRE Annotation Guidelines](https://tajakuzman.github.io/X-GENRE-Annotation-Guidelines/).

### List of labels

```
labels_list=['Other', 'Information/Explanation', 'News', 'Instruction', 'Opinion/Argumentation', 'Forum', 'Prose/Lyrical', 'Legal', 'Promotion'],

labels_map={'Other': 0, 'Information/Explanation': 1, 'News': 2, 'Instruction': 3, 'Opinion/Argumentation': 4, 'Forum': 5, 'Prose/Lyrical': 6, 'Legal': 7, 'Promotion': 8}

```

### Description of labels

|     Label               |     Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     Examples                                                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Information/Explanation | An objective text that describes   or presents an event, a person, a thing, a concept etc. Its main purpose is   to inform the reader about something.      Common features: objective/factual, explanation/definition of a concept (x   is …), enumeration.                                                                                                                                                                                                                                                                                                       | research article, encyclopedia article, informational blog, product   specification, course materials, general information, job description,   manual, horoscope, travel guide, glossaries, historical article, biographical   story/history. |
| Instruction             | An objective text which instructs   the readers on how to do something.      Common features: multiple steps/actions, chronological order, 1st person   plural or 2nd person, modality (must, have to, need to, can, etc.), adverbial   clauses of manner (in a way that), of condition (if), of time (after …).                                                                                                                                                                                                                                                   | how-to texts, recipes, technical support                                                                                                                                                                                                      |
| Legal                   | An objective formal text that   contains legal terms and is clearly structured. The name of the text type is   often included in the headline (contract, rules, amendment, general terms and   conditions, etc.).      Common features: objective/factual, legal terms, 3rd person.                                                                                                                                                                                                                                                                                | small print, software license, proclamation, terms and conditions,   contracts, law, copyright notices, university regulation                                                                                                                 |
| News                    | An objective or subjective text   which reports on an event recent at the time of writing or coming in the near   future.      Common features: adverbs/adverbial clauses of time and/or place (dates,   places), many proper nouns, direct or reported speech, past tense.                                                                                                                                                                                                                                                                                        | news report, sports report, travel blog, reportage, police report,   announcement                                                                                                                                                             |
| Opinion/Argumentation   | A subjective text in which the   authors convey their opinion or narrate their experience. It includes   promotion of an ideology and other non-commercial causes. This genre includes a subjective narration of a personal   experience as well.      Common features: adjectives/adverbs that convey opinion, words that convey   (un)certainty (certainly, surely), 1st person, exclamation marks.                                                | review, blog (personal blog, travel blog), editorial, advice, letter to   editor, persuasive article or essay, formal speech, pamphlet, political   propaganda, columns, political manifesto                                                  |
| Promotion               | A subjective text intended to   sell or promote an event, product, or service. It addresses the readers,   often trying to convince them to participate in something or buy something.   Common features: contains adjectives/adverbs that promote something   (high-quality, perfect, amazing), comparative and superlative forms of   adjectives and adverbs (the best, the greatest, the cheapest), addressing the   reader (usage of 2nd person), exclamation marks. | advertisement, promotion of a product (e-shops), promotion of an   accommodation, promotion of company's services, invitation to an event                                                                                                     |
| Forum                   | A text in which people discuss a   certain topic in form of comments.      Common features: multiple authors, informal language, subjective (the   writers express their opinions), written in 1st person.                                                                                                                                                                                                                                                                                                                                                         | discussion forum, reader/viewer responses, QA forum                                                                                                                                                                                           |
| Prose/Lyrical           | A literary text that   consists of paragraphs or verses. A literary text is deemed to have no other   practical purpose than to give pleasure to the reader. Often the author pays   attention to the aesthetic appearance of the text. It can be considered as   art.                                                                                                                                                                                                                                                                                     | lyrics, poem, prayer, joke, novel, short story                                                                                                                                                                                                |
| Other                   | A text that which does not fall   under any of other genre categories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                               |


### Fine-tuning hyperparameters

Fine-tuning was performed with `simpletransformers`. 
Beforehand, a brief hyperparameter optimization was performed and the presumed optimal hyperparameters are:

```python
model_args= {
            "num_train_epochs": 15,
            "learning_rate": 1e-5,
            "max_seq_length": 512,
            }        
      
```

## Citation

If you use the model, please cite the paper which describes creation of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) and the genre classifier:

```
@article{kuzman2023automatic,
  title={Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models},
  author={Kuzman, Taja and Mozeti{\v{c}}, Igor and Ljube{\v{s}}i{\'c}, Nikola},
  journal={Machine Learning and Knowledge Extraction},
  volume={5},
  number={3},
  pages={1149--1175},
  year={2023},
  publisher={MDPI}
}
```