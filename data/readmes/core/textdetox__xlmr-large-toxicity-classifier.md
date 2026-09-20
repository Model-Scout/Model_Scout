---
license: openrail++
datasets:
- textdetox/multilingual_toxicity_dataset
language:
- en
- ru
- uk
- es
- de
- am
- ar
- zh
- hi
metrics:
- f1
base_model:
- FacebookAI/xlm-roberta-large
tags:
- toxicity
new_version: textdetox/xlmr-large-toxicity-classifier-v2
---

# Multilingual Toxicity Classifier for 9 languages (2024)

This is an instance of [xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large) that was fine-tuned on binary toxicity classification task based on our compiled dataset [textdetox/multilingual_toxicity_dataset](https://huggingface.co/datasets/textdetox/multilingual_toxicity_dataset).

Firstly, we separated a balanced 20% test set to check the model adequency. Then, the model was fine-tuned on the full data. The results on the test set are the following:

|          | Precision | Recall | F1    |
|----------|-----------|--------|-------|
| all_lang | 0.8713    | 0.8710 | 0.8710|
| en       | 0.9650    | 0.9650 | 0.9650|
| ru       | 0.9791    | 0.9790 | 0.9790|
| uk       | 0.9267    | 0.9250 | 0.9251|
| de       | 0.8791    | 0.8760 | 0.8758|
| es       | 0.8700    | 0.8700 | 0.8700|
| ar       | 0.7787    | 0.7780 | 0.7780|
| am       | 0.7781    | 0.7780 | 0.7780|
| hi       | 0.9360    | 0.9360 | 0.9360|
| zh       | 0.7318    | 0.7320 | 0.7315|

## Citation
If you would like to acknowledge our work, please, cite the following manuscripts:

```
@inproceedings{dementieva2024overview,
  title={Overview of the Multilingual Text Detoxification Task at PAN 2024},
  author={Dementieva, Daryna and Moskovskiy, Daniil and Babakov, Nikolay and Ayele, Abinew Ali and Rizwan, Naquee and Schneider, Frolian and Wang, Xintog and Yimam, Seid Muhie and Ustalov, Dmitry and Stakovskii, Elisei and Smirnova, Alisa and Elnagar, Ashraf and Mukherjee, Animesh and Panchenko, Alexander},
  booktitle={Working Notes of CLEF 2024 - Conference and Labs of the Evaluation Forum},
  editor={Guglielmo Faggioli and Nicola Ferro and Petra Galu{\v{s}}{\v{c}}{\'a}kov{\'a} and Alba Garc{\'i}a Seco de Herrera},
  year={2024},
  organization={CEUR-WS.org}
}
```

```
@inproceedings{DBLP:conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24,
  author       = {Janek Bevendorff and
                  Xavier Bonet Casals and
                  Berta Chulvi and
                  Daryna Dementieva and
                  Ashaf Elnagar and
                  Dayne Freitag and
                  Maik Fr{\"{o}}be and
                  Damir Korencic and
                  Maximilian Mayerl and
                  Animesh Mukherjee and
                  Alexander Panchenko and
                  Martin Potthast and
                  Francisco Rangel and
                  Paolo Rosso and
                  Alisa Smirnova and
                  Efstathios Stamatatos and
                  Benno Stein and
                  Mariona Taul{\'{e}} and
                  Dmitry Ustalov and
                  Matti Wiegmann and
                  Eva Zangerle},
  editor       = {Nazli Goharian and
                  Nicola Tonellotto and
                  Yulan He and
                  Aldo Lipani and
                  Graham McDonald and
                  Craig Macdonald and
                  Iadh Ounis},
  title        = {Overview of {PAN} 2024: Multi-author Writing Style Analysis, Multilingual
                  Text Detoxification, Oppositional Thinking Analysis, and Generative
                  {AI} Authorship Verification - Extended Abstract},
  booktitle    = {Advances in Information Retrieval - 46th European Conference on Information
                  Retrieval, {ECIR} 2024, Glasgow, UK, March 24-28, 2024, Proceedings,
                  Part {VI}},
  series       = {Lecture Notes in Computer Science},
  volume       = {14613},
  pages        = {3--10},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-56072-9\_1},
  doi          = {10.1007/978-3-031-56072-9\_1},
  timestamp    = {Fri, 29 Mar 2024 23:01:36 +0100},
  biburl       = {https://dblp.org/rec/conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```