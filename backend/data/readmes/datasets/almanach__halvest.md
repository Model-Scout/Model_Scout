---
pretty_name: HALvest

configs:
- config_name: ar
  data_files: "ar/*.gz"
- config_name: az
  data_files: "az/*.gz"
- config_name: bg
  data_files: "bg/*.gz"
- config_name: bo
  data_files: "bo/*.gz"
- config_name: br
  data_files: "br/*.gz"
- config_name: bs
  data_files: "bs/*.gz"
- config_name: ca
  data_files: "ca/*.gz"
- config_name: co
  data_files: "co/*.gz"
- config_name: cs
  data_files: "cs/*.gz"
- config_name: da
  data_files: "da/*.gz"
- config_name: de
  data_files: "de/*.gz"
- config_name: el
  data_files: "el/*.gz"
- config_name: en
  data_files: "en/*.gz"
- config_name: eo
  data_files: "eo/*.gz"
- config_name: es
  data_files: "es/*.gz"
- config_name: et
  data_files: "et/*.gz"
- config_name: eu
  data_files: "eu/*.gz"
- config_name: fa
  data_files: "fa/*.gz"
- config_name: fi
  data_files: "fi/*.gz"
- config_name: fr
  data_files: "fr/*.gz"
- config_name: gl
  data_files: "gl/*.gz"
- config_name: gn
  data_files: "gn/*.gz"
- config_name: he
  data_files: "he/*.gz"
- config_name: hi
  data_files: "hi/*.gz"
- config_name: hr
  data_files: "hr/*.gz"
- config_name: hu
  data_files: "hu/*.gz"
- config_name: hy
  data_files: "hy/*.gz"
- config_name: id
  data_files: "id/*.gz"
- config_name: ie
  data_files: "ie/*.gz"
- config_name: it
  data_files: "it/*.gz"
- config_name: ja
  data_files: "ja/*.gz"
- config_name: kk
  data_files: "kk/*.gz"
- config_name: ko
  data_files: "ko/*.gz"
- config_name: lt
  data_files: "lt/*.gz"
- config_name: mk
  data_files: "mk/*.gz"
- config_name: mr
  data_files: "mr/*.gz"
- config_name: "no"
  data_files: "no/*.gz"
- config_name: oc
  data_files: "oc/*.gz"
- config_name: pl
  data_files: "pl/*.gz"
- config_name: pt
  data_files: "pt/*.gz"
- config_name: ro
  data_files: "ro/*.gz"
- config_name: ru
  data_files: "ru/*.gz"
- config_name: sk
  data_files: "sk/*.gz"
- config_name: sl
  data_files: "sl/*.gz"
- config_name: sq
  data_files: "sq/*.gz"
- config_name: sr
  data_files: "sr/*.gz"
- config_name: sv
  data_files: "sv/*.gz"
- config_name: sw
  data_files: "sw/*.gz"
- config_name: ta
  data_files: "ta/*.gz"
- config_name: tet
  data_files: "tet/*.gz"
- config_name: th
  data_files: "th/*.gz"
- config_name: tk
  data_files: "tk/*.gz"
- config_name: tl
  data_files: "tl/*.gz"
- config_name: tr
  data_files: "tr/*.gz"
- config_name: uk
  data_files: "uk/*.gz"
- config_name: vi
  data_files: "vi/*.gz"
- config_name: zh
  data_files: "zh/*.gz"

language:
- ar
- az
- bg
- bo
- br
- bs
- ca
- co
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
- gn
- he
- hi
- hr
- hu
- hy
- id
- ie
- it
- ja
- kk
- ko
- lt
- mk
- mr
- "no"
- oc
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- tet
- th
- tk
- tl
- tr
- uk
- vi
- zh

size_categories:
  - n<1K
  - 1K<n<10K
  - 10K<n<100K
  - 100K<n<1M

task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling

tags:
- academia
- research

annotations_creators:
- no-annotation

multilinguality:
- multilingual

source_datasets:
- original
---



<div align="center">
    <h1> HALvest </h1>
    <h3> Open Scientific Papers Harvested from HAL (Unfiltered) </h3>
</div>

---


## Dataset Description

- **Repository:** [GitHub](https://github.com/Madjakul/HALvesting/tree/main)


## Dataset Summary

### overview:

This is the unfiltered version of [HALvest](https://huggingface.co/datasets/Madjakul/HALvest), comprising of fulltext from open papers found on [Hyper Articles en Ligne (HAL)](https://hal.science/) with extra fields for potential filtering. Our dump is mostly english/french but gather papers written in 56 languages across 13 domains.

You can download the dataset using Hugging Face datasets:
```py
from datasets import load_dataset

ds = load_dataset("almanach/HALvest", "en")
```


### Details

Building the dataset is a three steps process: data fetching from HAL, data merging and data enriching.

1. We first request [HAL's API](https://api.archives-ouvertes.fr/docs) in order to gather open research papers and parse it -- effectively sorting papers by language. Then, we download the PDFs of the fetched data.
2. Using [GROBID](https://github.com/kermitt2/grobid), we convert each PDF to an `xml-tei` format in order to have structured data. We convert each `xml-tei` file to a `txt` format before concatenating it with the paper's.
3. Finally, we compute some statistics about each document.


### Languages

Please, note that the number of tokens is highly inflated in the raw version of the dataset because of badly encoded PDFs, translating to gibberish documents/texts.

ISO-639|Language|# Documents|# mT5 Tokens
-------|--------|-----------|--------
en|English|464,679|8,158,933,235
fr|French|199,216|9,018,529,985
es|Spanish|2,975|69,221,667
it|Italian|1,172|48,747,986
pt|Portuguese|934|32,918,832
de|German|652|12,225,960
ru|Russian|245|5,763,532
zh|Chinese|160|2,861,585
eu|Basque|113|2,297,485
ar|Arabic|92|2,167,431
ja|Japanese|92|547,861
el|Greek|54|1,738,878
pl|Polish|43|987,878
ro|Romanian|39|1,298,901
uk|Ukrainian|34|837,793
vi|Viêt Namese|29|436,660
ca|Catalan|28|975,078
da|Danish|27|961,955
oc|Occitan|26|285,334
br|Breton|24|998,088
sr|Serbian|24|336,878
ko|Korean|17|226,268
fa|Persian|17|213,903
tr|Turkish|17|149,718
hu|Hungarian|14|577,568
eo|Esperanto|14|105,286
hy|Armenian|10|127,988
cs|Czech|9|712,263
bg|Bulgarian|9|208,763
sq|Albanian|9|98,009
id|Indonesian|9|53,075
he|Hebrew|8|61,283
hr|Croatian|8|40,621
et|Estonian|7|20,405
sv|Swedish|6|270,642
no|Norwegian|6|62,767
az|Azerbaijani|5|52,762
fi|Finnish|4|60,507
tet|Tetum|4|18,485
lt|Lithuanian|3|16,572
mr|Marathi|3|16,386
hi|Hindi|3|3,490
ie|Interlingue|2|140,383
ta|Tamil|2|77,087
sw|Swahili|2|73,921
tl|Tagalog|2|35,962
gl|Galician|2|29,688
mk|Macedonian|2|14,654
th|Thai|1|70,909
tk|Turkmen|1|66,104
bs|Bosnian|1|63,018
kk|Kazakh|1|41,839
sl|Slovenian|1|22,844
sk|Slovak|1|12,997
co|Corsican|1|9,083
gn|Guarani|1|1,566
bo|Tibetan|1|579


### Domains

Please, note that the number of tokens is highly inflated in the raw version of the dataset because of badly encoded PDFs, translating to gibberish documents/texts.

Domain|Code|# Documents|# mT5 Tokens
------|----|-----------|------------
Humanities and Social Sciences|shs|156,566|5,614,423,171
Computer Science|info|148,316|2,573,673,455
Life Sciences|sdv|115,744|3,145,323,780
Engineering Sciences|spi|102,751|2,254,653,825
Physics|phys|65,991|1,503,190,749
Mathematics|math|62,921|1,638,500,361
Chemical Science|chim|40,012|899,507,319
Environmental Science|sde|31,575|579,076,669
Sciences of the Universe|sdu|23,557|682,356,264
Cognitive science|scco|11,772|227,487,096
Statistics|stat|10,579|184,678,350
Quantitative Finance|qfin|3,451|68,518,636
Nonlinear Sciences|nlin|1,972|30,694,088

You can browse through every domains and sub-domains here: https://hal.science/browse/domain.


## Considerations for Using the Data

The corpus is extracted from the [HAL's open archive](https://hal.science/) which distributes scientific publications following open access principles. The corpus is made up of both creative commons licensed and copyrighted documents (distribution authorized on HAL by the publisher). This must be considered prior to using this dataset for any purpose, other than training deep learning models, data mining etc. We do not own any of the text from which these data has been extracted.


## Citation


```bib
@misc{kulumba2026halvestcontrastiveretrievallikeauthorshipattribution,
      title={HALvest-Contrastive: Retrieval-Like Authorship Attribution with Patch-Level Late Interaction}, 
      author={Francis Kulumba and Wissam Antoun and Guillaume Vimont and Laurent Romary and Florian Cafiero},
      year={2026},
      eprint={2407.20595},
      archivePrefix={arXiv},
      primaryClass={cs.DL},
      url={https://arxiv.org/abs/2407.20595}, 
}
```


## Dataset Copyright

The licence terms for HALvest strictly follows the one from HAL. Please refer to the below license when using this dataset.
- [HAL license](https://doc.archives-ouvertes.fr/en/legal-aspects/)