---
language:
- ar 
- az 
- be 
- bg 
- bn 
- bs 
- cs 
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
- gl 
- he 
- hi 
- hr 
- hu 
- hy 
- id 
- it 
- ja 
- ka 
- kk 
- ko 
- ku 
- lt 
- mk 
- mn 
- mr 
- ms 
- my 
- nb 
- nl 
- pl 
- pt 
- ro 
- ru 
- sk 
- sl 
- sq 
- sr 
- sv 
- ta 
- th 
- tr 
- uk 
- ur 
- vi 
- zh 
language_creators:
- expert-generated
annotations_creators:
- crowdsourced
license:
- cc-by-nc-nd-4.0
multilinguality:
- translation
pretty_name: TED_Talks
task_categories:
  - translation
---
## Dataset Description

Train, validation and test splits for TED talks as in http://phontron.com/data/ted_talks.tar.gz. Data is detokenized using moses. 

Example of loading:
```python
dataset = load_dataset("davidstap/ted_talks", "ar_en", trust_remote_code=True)
```

Note that `ar_en` and `en_ar` will result in the same data being loaded..


The following languages are available:
```
- ar 
- az 
- be 
- bg 
- bn 
- bs 
- cs 
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
- fr-ca 
- gl 
- he 
- hi 
- hr 
- hu 
- hy 
- id 
- it 
- ja 
- ka 
- kk 
- ko 
- ku 
- lt 
- mk 
- mn 
- mr 
- ms 
- my 
- nb 
- nl 
- pl 
- pt 
- pt-br 
- ro 
- ru 
- sk 
- sl 
- sq 
- sr 
- sv 
- ta 
- th 
- tr 
- uk 
- ur 
- vi 
- zh 
- zh-cn 
- zh-tw
```


### Citation Information

```
@inproceedings{qi-etal-2018-pre,
    title = "When and Why Are Pre-Trained Word Embeddings Useful for Neural Machine Translation?",
    author = "Qi, Ye  and
      Sachan, Devendra  and
      Felix, Matthieu  and
      Padmanabhan, Sarguna  and
      Neubig, Graham",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-2084",
    doi = "10.18653/v1/N18-2084",
    pages = "529--535",
}
```
