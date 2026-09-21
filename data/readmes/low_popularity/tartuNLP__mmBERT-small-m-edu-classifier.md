---
library_name: transformers
license: mit
datasets:
- data-is-better-together/fineweb-c
- HuggingFaceFW/fineweb-edu-llama3-annotations
- tartuNLP/fineweb-c-combined-resample
base_model:
- jhu-clsp/mmBERT-small
language:
- ekk
- eng
- lvs
- kor
- kin
- ita
- hin
- gom
- glg
- fra
- fas
- eus
- deu
- dan
- cat
- bho
- bak
- arz
- ary
- arb
- yor
- vie
- ukr
- tur
- tir
- tel
- tam
- swe
- spa
- slk
- rus
- por
- pbt
- nld
- nds
- vls
- srp
- sco
- lat
- ind
- gmh
- bul
- bre
- bar
- apc
- aeb
- ron
- mar
- kas
- hin
- crh
- arb
- zsm
- yue
- uzn
- uzn
- udm
- tha
- tat
- som
- sin
- pol
- pcm
- npi
- npi
- nan
- mal
- lug
- lit
- lez
- asm
- asm
- fil
- cmn
- ces
- ben
- ast
- ars
- jpn
- guj
- gsw
- fin
- tok
- srp
- quz
- pfl
- pdc
- nob
- lij
- hun
- hsb
- goh
- fao
pipeline_tag: text-classification
---

# Multilingual Educational Content Classifier

Trained on full documents of up to 8192 tokens in total. The train set of [tartuNLP/fineweb-c-combined-resample](https://huggingface.co/datasets/tartuNLP/fineweb-c-combined-resample)
was used, which itself is a mix and a resample of [HuggingFaceFW/fineweb-edu-llama3-annotations](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations) and
[data-is-better-together/fineweb-c](https://huggingface.co/datasets/data-is-better-together/fineweb-c).

## Labels

```
{0: '❗ Problematic Content ❗', 1: 'None', 2: 'Minimal', 3: 'Basic', 4: 'Good', 5: 'Excellent'}
```

## Classification Report

Evaluated on the development set of [tartuNLP/fineweb-c-combined-resample](https://huggingface.co/datasets/tartuNLP/fineweb-c-combined-resample)
organized so that each language appears at least once.

```
              precision    recall  f1-score   support

           0       0.89      0.78      0.83       602
           1       0.65      0.88      0.75       916
           2       0.41      0.29      0.34       345
           3       0.40      0.30      0.34       179
           4       0.53      0.15      0.23       127
           5       0.55      0.39      0.45        44

    accuracy                           0.66      2213
   macro avg       0.57      0.46      0.49      2213
weighted avg       0.65      0.66      0.64      2213
```

## Confusion Matrix
```
[[471 114  10   6   0   1]
 [ 33 806  59  13   5   0]
 [ 10 204 101  28   2   0]
 [  7  72  37  53   8   2]
 [  7  35  27  28  19  11]
 [  2   7  10   6   2  17]]
```

