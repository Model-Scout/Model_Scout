---
library_name: transformers
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
- language-identification
metrics:
- precision
- recall
- f1
- accuracy
language:
- multilingual
- af
- am
- ar
- as
- ba
- be
- bg
- bn
- bo
- br
- bs
- ca
- ce
- ckb
- cs
- cy
- da
- de
- dv
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- ga
- gd
- gl
- gu
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
- lb
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- 'no'
- ny
- oc
- om
- or
- pa
- pl
- ps
- pt
- rm
- ro
- ru
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
- tg
- th
- ti
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vi
- yo
- yi
- zh
- zu
model-index:
- name: polyglot-tagger
  results: []
datasets:
- wikimedia/wikipedia
- HuggingFaceFW/finetranslations
- google/smol
- polyglot-tagger/nlp-noise-snippets
- polyglot-tagger/wikipedia-language-snippets-filtered
- polyglot-tagger/finetranslations-filtered
- polyglot-tagger/tatoeba-filtered
pipeline_tag: text-classification
---

# Polyglot Tagger: Multi-label Language Identification

Refer to `polyglot-tagger/language-identification`. It is trained on the same dataset as a text-classifier rather than as a token classifier.

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base).
It achieves the following results on the evaluation set:
- Loss: 0.0123
- Precision: 0.9859
- Recall: 0.9831
- F1: 0.9845
- Accuracy: 0.9412



## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 18
- total_train_batch_size: 576
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Accuracy | F1     | Validation Loss | Precision | Recall |
|:-------------:|:------:|:-----:|:--------:|:------:|:---------------:|:---------:|:------:|
| 0.2186        | 0.2925 | 2500  | 0.8560   | 0.9651 | 0.0395          | 0.9778    | 0.9528 |
| 0.1331        | 0.5851 | 5000  | 0.0232   | 0.9803 | 0.9717          | 0.9760    | 0.9070 |
| 0.1044        | 0.8776 | 7500  | 0.0172   | 0.9828 | 0.9774          | 0.9801    | 0.9218 |
| 0.0851        | 1.1700 | 10000 | 0.0150   | 0.9844 | 0.9801          | 0.9822    | 0.9311 |
| 0.0783        | 1.4626 | 12500 | 0.0136   | 0.9859 | 0.9809          | 0.9834    | 0.9354 |
| 0.0705        | 1.7551 | 15000 | 0.0126   | 0.9861 | 0.9826          | 0.9843    | 0.9399 |
| 0.0692        | 2.0    | 17094 | 0.0123   | 0.9859 | 0.9831          | 0.9845    | 0.9412 |


### Framework versions

- Transformers 5.5.4
- Pytorch 2.11.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
