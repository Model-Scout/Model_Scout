---
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
- en
- el
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
- nb
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
size_categories:
- 100M<n<1B
---

# Dataset Card for EntityCS
 
- Repository: https://github.com/huawei-noah/noah-research/tree/master/NLP/EntityCS  
- Paper: https://aclanthology.org/2022.findings-emnlp.499.pdf  
- Point of Contact: [Fenia Christopoulou](mailto:efstathia.christopoulou@huawei.com), [Chenxi Whitehouse](mailto:chenxi.whitehouse@gmail.com)  

## Dataset Description

We use the English Wikipedia and leverage entity information from Wikidata to construct an entity-based Code Switching corpus. 
To achieve this, we make use of wikilinks in Wikipedia, i.e. links from one page to another.
We use the English [Wikipedia dump](https://dumps.wikimedia.org/enwiki/latest/) (November 2021) and extract raw text with [WikiExtractor](https://github.com/attardi/wikiextractor) while keeping track of wikilinks.
Since we are interested in creating entity-level CS instances, we only keep sentences containing at least one wikilink.
Given an English sentence with wikilinks, we first map the entity in each wikilink to its corresponding Wikidata ID and
retrieve its available translations from Wikidata.
For each sentence, we check which languages have translations for all entities in that sentence, and consider those as candidates for code-switching. 
We ensure all entities are code-switched to the same target language in a single sentence, avoiding noise from including too many languages. 
To control the size of the corpus, we generate up to five code-switched sentences for each English sentence. 
In particular, if fewer than five languages have translations available for all the entities in a sentence, we create code-switched instances with all of them. 
Otherwise, we randomly select five target languages from the candidates. 
If no candidate languages can be found, we do not code-switch the sentence, instead, we keep it as part of the English corpus. 
Finally, we surround each entity with entity indicators (`<e>`, `</e>`).

## Supported Tasks and Leaderboards

The dataset was developped for intermediate pre-training of language models. 
In the paper we further fine-tune models on entity-centric downstream tasks, such as NER.

## Languages

The dataset covers 93 languages in total, including English.

## Data Statistics

| Statistic                     | Count       |
|:------------------------------|------------:|
| Languages                     | 93          |
| English Sentences             | 54,469,214  |
| English Entities              | 104,593,076 |
| Average Sentence Length       | 23.37       |
| Average Entities per Sentence | 2           |
| CS Sentences per EN Sentence  | ≤ 5         |
| CS Sentences                  | 231,124,422 |
| CS Entities                   | 420,907,878 |

## Data Fields

Each instance contains 4 fields:
- `id`: Unique ID of each sentence
- `language`: The language of choice for entity code-switching of the given sentence
- `en_sentence`: The original English sentence
- `cs_sentence`: The code-switched sentence

In the case of the English subset, the `cs_sentence` field does not exist as the sentences are not code-switched.

An example of what a data instance looks like:
```
{
  'id': 19, 
  'en_sentence': 'The subs then enter a <en>coral reef</en> with many bright reflective colors.', 
  'cs_sentence': 'The subs then enter a <de>Korallenriff</de> with many bright reflective colors.', 
  'language': 'de'
}
```

## Data Splits

There is a single data split for each language. You can randomly select a few examples from each language to serve as validation set.


## Limitations

An important limitation of the work is that before code-switching an entity, its morphological inflection is not checked. 
This can lead to potential errors as the form of the CS entity might not agree with the surrounding context (e.g. plural). 
There should be few cases as such, as we are only switching entities. However, this should be improved in a later version of the corpus.
Secondly, the diversity of languages used to construct the EntityCS corpus is restricted to the overlap between the available languages in WikiData and XLM-R pre-training.
This choice was for a better comparison between models, however it is possible to extend the corpus with more languages that XLM-R does not cover, following
the procedure presented in the paper.

## Citation

**BibTeX**

```html
@inproceedings{whitehouse-etal-2022-entitycs,
    title = "{E}ntity{CS}: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching",
    author = "Whitehouse, Chenxi  and
      Christopoulou, Fenia  and
      Iacobacci, Ignacio",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.499",
    pages = "6698--6714"
}
```

**APA**
```html
Whitehouse, C., Christopoulou, F., & Iacobacci, I. (2022). EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching. In Findings of the Association for Computational Linguistics: EMNLP 2022.
```
