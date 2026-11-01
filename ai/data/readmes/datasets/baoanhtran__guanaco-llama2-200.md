---
pretty_name: CulturaX
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- als
- am
- an
- ar
- arz
- as
- ast
- av
- az
- azb
- ba
- bar
- bcl
- be
- bg
- bh
- bn
- bo
- bpy
- br
- bs
- bxr
- ca
- cbk
- ce
- ceb
- ckb
- cs
- cv
- cy
- da
- de
- dsb
- dv
- el
- eml
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- frr
- fy
- ga
- gd
- gl
- gn
- gom
- gu
- he
- hi
- hr
- hsb
- ht
- hu
- hy
- ia
- id
- ie
- ilo
- io
- is
- it
- ja
- jbo
- jv
- ka
- kk
- km
- kn
- ko
- krc
- ku
- kv
- kw
- ky
- la
- lb
- lez
- li
- lmo
- lo
- lrc
- lt
- lv
- mai
- mg
- mhr
- min
- mk
- ml
- mn
- mr
- mrj
- ms
- mt
- mwl
- my
- myv
- mzn
- nah
- nap
- nds
- ne
- new
- nl
- nn
- 'no'
- oc
- or
- os
- pa
- pam
- pl
- pms
- pnb
- ps
- pt
- qu
- rm
- ro
- ru
- rue
- sa
- sah
- scn
- sd
- sh
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
- tk
- tl
- tr
- tt
- tyv
- ug
- uk
- ur
- uz
- vec
- vi
- vls
- vo
- wa
- war
- wuu
- xal
- xmf
- yi
- yo
- yue
- zh
multilinguality:
- multilingual
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
- 10M<n<100M
- 100M<n<1B
- 1B<n<10B
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
extra_gated_prompt: "By completing the form below, you acknowledge that the provided data is offered as is. Although we anticipate no problems, you accept full responsibility for any repercussions resulting from the use of this data. Furthermore, you agree that the data must not be utilized for malicious or harmful purposes towards humanity."
extra_gated_fields:
 Name: text
 Email: text
 Affiliation: text
 Country: text
 Usecase: text
 I have explicitly check with my jurisdiction and I confirm that downloading CulturaX is legal in the country/region where I am located right now, and for the use case that I have described above: checkbox
 You agree to not attempt to determine the identity of individuals in this dataset: checkbox
---



<div align="center">
    <h1> CulturaX </h1>
    <h3> Cleaned, Enormous, and Public: The Multilingual Fuel to Democratize Large Language Models for 167 Languages </h3>
</div>




## Dataset Description

- **Repository:** [https://github.com/nlp-uoregon/CulturaX](https://github.com/nlp-uoregon/CulturaX)
- **Papers:** [CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages](https://arxiv.org/abs/2309.09400)


## Dataset Summary

We present CulturaX, a substantial multilingual dataset with 6.3 trillion tokens in 167 languages, tailored for large language model (LLM) development. Our dataset undergoes meticulous cleaning and deduplication through a rigorous pipeline of multiple stages to accomplish the best quality for model training, including language identification, URL-based filtering, metric-based cleaning, document refinement, and data deduplication. We employ MinHash at document level to achieve fuzzy deduplication for the datasets in different languages. Our data cleaning framework includes diverse criteria and threshold selections, guided by extensive data samples, ensuring comprehensive noise filtering in various aspects. CulturaX is fully released to the public in HuggingFace to facilitate research and advancements in multilingual LLMs. 

Our dataset combines the most recent iteration of mC4 (version 3.1.0) [1] with all accessible OSCAR corpora up to the present year, including 20.19, 21.09, 22.01, and 23.01 [2]. After deep cleaning and deduplication, CulturaX involves 16TB data in the parquet format (expanding to 27TB when unpacked). More than a half of our dataset is dedicated to non-English languages to significantly boost the data size and enhance the feasibility of training models in multilingual scenarios.

To obtain perplexity scores for data cleaning, we train a SentencePiece tokenizer and 5-gram Kneser-Ney language models as provided in the KenLM library [3] using the 20230501 dumps of Wikipedia. Our KenLM models are also released in HuggingFace: https://huggingface.co/uonlp/kenlm.

Details for the dataset can be found in our technical paper: [https://arxiv.org/abs/2309.09400](https://arxiv.org/abs/2309.09400)


You can download the dataset using Hugging Face datasets:

*You may need to follow these instructions to setup authentication before downloading the dataset: [https://huggingface.co/docs/huggingface_hub/quick-start#login](https://huggingface.co/docs/huggingface_hub/quick-start#login)*

```python
from datasets import load_dataset
ds = load_dataset("uonlp/CulturaX",
                  language="en",
                  use_auth_token=True)
```


### Languages

The supported languages and statistics for our dataset can be found below:

*(Note that the language code `als` and `eml` refer to `gsw` and `x-eml` in the OSCAR-2301 dataset.)*



|     | Code   | Language                 | # Documents     | # Tokens            | # Tokens (%) |
|----:|:-------|:-------------------------|:----------------|:--------------------|:------|
|   0 | en     | English                  | 3,241,065,682   | 2,846,970,578,793   | 45.13 |
|   1 | ru     | Russian                  | 799,310,908     | 737,201,800,363     | 11.69 |
|   2 | es     | Spanish                  | 450,937,645     | 373,845,662,394     | 5.93  |
|   3 | de     | German                   | 420,017,484     | 357,030,348,021     | 5.66  |
|   4 | fr     | French                   | 363,754,348     | 319,332,674,695     | 5.06  |
|   5 | zh     | Chinese                  | 218,624,604     | 227,055,380,882     | 3.60  |
|   6 | it     | Italian                  | 211,309,922     | 165,446,410,843     | 2.62  |
|   7 | pt     | Portuguese               | 190,289,658     | 136,941,763,923     | 2.17  |
|   8 | pl     | Polish                   | 142,167,217     | 117,269,087,143     | 1.86  |
|   9 | ja     | Japanese                 | 111,188,475     | 107,873,841,351     | 1.71  |
|  10 | vi     | Vietnamese               | 102,411,180     | 98,453,464,077      | 1.56  |
|  11 | nl     | Dutch                    | 117,392,666     | 80,032,209,900      | 1.27  |
|  12 | ar     | Arabic                   | 74,027,952      | 69,354,335,076      | 1.10  |
|  13 | tr     | Turkish                  | 94,207,460      | 64,292,787,164      | 1.02  |
|  14 | cs     | Czech                    | 65,350,564      | 56,910,486,745      | 0.90  |
|  15 | fa     | Persian                  | 59,531,144      | 45,947,657,495      | 0.73  |
|  16 | hu     | Hungarian                | 44,132,152      | 43,417,981,714      | 0.69  |
|  17 | el     | Greek                    | 51,430,226      | 43,147,590,757      | 0.68  |
|  18 | ro     | Romanian                 | 40,325,424      | 39,647,954,768      | 0.63  |
|  19 | sv     | Swedish                  | 49,709,189      | 38,486,181,494      | 0.61  |
|  20 | uk     | Ukrainian                | 44,740,545      | 38,226,128,686      | 0.61  |
|  21 | fi     | Finnish                  | 30,467,667      | 28,925,009,180      | 0.46  |
|  22 | ko     | Korean                   | 20,557,310      | 24,765,448,392      | 0.39  |
|  23 | da     | Danish                   | 25,429,808      | 22,921,651,314      | 0.36  |
|  24 | bg     | Bulgarian                | 24,131,819      | 22,917,954,776      | 0.36  |
|  25 | no     | Norwegian                | 18,907,310      | 18,426,628,868      | 0.29  |
|  26 | hi     | Hindi                    | 19,665,355      | 16,791,362,871      | 0.27  |
|  27 | sk     | Slovak                   | 18,582,517      | 16,442,669,076      | 0.26  |
|  28 | th     | Thai                     | 20,960,550      | 15,717,374,014      | 0.25  |
|  29 | lt     | Lithuanian               | 13,339,785      | 14,247,110,836      | 0.23  |
|  30 | ca     | Catalan                  | 15,531,777      | 12,530,288,006      | 0.20  |
|  31 | id     | Indonesian               | 23,251,368      | 12,062,966,061      | 0.19  |
|  32 | bn     | Bangla                   | 12,436,596      | 9,572,929,804       | 0.15  |
|  33 | et     | Estonian                 | 8,004,753       | 8,805,656,165       | 0.14  |
|  34 | sl     | Slovenian                | 7,335,378       | 8,007,587,522       | 0.13  |
|  35 | lv     | Latvian                  | 7,136,587       | 7,845,180,319       | 0.12  |
|  36 | he     | Hebrew                   | 4,653,979       | 4,937,152,096       | 0.08  |
|  37 | sr     | Serbian                  | 4,053,166       | 4,619,482,725       | 0.07  |
|  38 | ta     | Tamil                    | 4,728,460       | 4,378,078,610       | 0.07  |
|  39 | sq     | Albanian                 | 5,205,579       | 3,648,893,215       | 0.06  |
|  40 | az     | Azerbaijani              | 5,084,505       | 3,513,351,967       | 0.06  |
|  41 | kk     | Kazakh                   | 2,733,982       | 2,802,485,195       | 0.04  |
|  42 | ur     | Urdu                     | 2,757,279       | 2,703,052,627       | 0.04  |
|  43 | ka     | Georgian                 | 3,120,321       | 2,617,625,564       | 0.04  |
|  44 | hy     | Armenian                 | 2,964,488       | 2,395,179,284       | 0.04  |
|  45 | is     | Icelandic                | 2,373,560       | 2,350,592,857       | 0.04  |
|  46 | ml     | Malayalam                | 2,693,052       | 2,100,556,809       | 0.03  |
|  47 | ne     | Nepali                   | 3,124,040       | 2,061,601,961       | 0.03  |
|  48 | mk     | Macedonian               | 2,762,807       | 2,003,302,006       | 0.03  |
|  49 | mr     | Marathi                  | 2,266,588       | 1,955,227,796       | 0.03  |
|  50 | mn     | Mongolian                | 1,928,828       | 1,850,667,656       | 0.03  |
|  51 | be     | Belarusian               | 1,643,486       | 1,791,473,041       | 0.03  |
|  52 | te     | Telugu                   | 1,822,865       | 1,566,972,146       | 0.02  |
|  53 | gl     | Galician                 | 1,785,963       | 1,382,539,693       | 0.02  |
|  54 | eu     | Basque                   | 1,598,822       | 1,262,066,759       | 0.02  |
|  55 | kn     | Kannada                  | 1,352,142       | 1,242,285,201       | 0.02  |
|  56 | gu     | Gujarati                 | 1,162,878       | 1,131,730,537       | 0.02  |
|  57 | af     | Afrikaans                | 826,519         | 1,119,009,767       | 0.02  |
|  58 | my     | Burmese                  | 865,575         | 882,606,546         | 0.01  |
|  59 | si     | Sinhala                  | 753,655         | 880,289,097         | 0.01  |
|  60 | eo     | Esperanto                | 460,088         | 803,948,528         | 0.01  |
|  61 | km     | Khmer                    | 1,013,181       | 746,664,132         | 0.01  |
|  62 | pa     | Punjabi                  | 646,987         | 727,546,145         | 0.01  |
|  63 | cy     | Welsh                    | 549,955         | 576,743,162         | 0.01  |
|  64 | ky     | Kyrgyz                   | 570,922         | 501,442,620         | 0.01  |
|  65 | ga     | Irish                    | 304,251         | 376,947,935         | 0.01  |
|  66 | ps     | Pashto                   | 376,914         | 363,007,770         | 0.01  |
|  67 | am     | Amharic                  | 243,349         | 358,206,762         | 0.01  |
|  68 | ku     | Kurdish                  | 295,314         | 302,990,910         | 0.00  |
|  69 | tl     | Filipino                 | 348,453         | 242,086,456         | 0.00  |
|  70 | yi     | Yiddish                  | 141,156         | 217,584,643         | 0.00  |
|  71 | lo     | Lao                      | 217,842         | 168,256,876         | 0.00  |
|  72 | fy     | Western Frisian          | 223,268         | 167,193,111         | 0.00  |
|  73 | sd     | Sindhi                   | 109,162         | 147,487,058         | 0.00  |
|  74 | mg     | Malagasy                 | 115,910         | 142,685,412         | 0.00  |
|  75 | or     | Odia                     | 153,461         | 100,323,213         | 0.00  |
|  76 | as     | Assamese                 | 52,627          | 83,787,896          | 0.00  |
|  77 | ug     | Uyghur                   | 47,035          | 77,677,306          | 0.00  |
|  78 | uz     | Uzbek                    | 87,219          | 75,250,787          | 0.00  |
|  79 | la     | Latin                    | 48,968          | 44,176,580          | 0.00  |
|  80 | hr     | Croatian                 | 460,690         | 40,796,811          | 0.00  |
|  81 | sw     | Swahili                  | 66,506          | 30,708,309          | 0.00  |
|  82 | ms     | Malay                    | 238,151         | 19,375,976          | 0.00  |
|  83 | br     | Breton                   | 43,765          | 13,987,037          | 0.00  |
|  84 | sa     | Sanskrit                 | 16,290          | 13,561,367          | 0.00  |
|  85 | gd     | Scottish Gaelic          | 8,408           | 4,796,485           | 0.00  |
|  86 | su     | Sundanese                | 1,554           | 1,308,460           | 0.00  |
|  87 | jv     | Javanese                 | 2,058           | 625,429             | 0.00  |
|  88 | tg     | Tajik                    | 483,835         | -                   | -     |
|  89 | ceb    | Cebuano                  | 263,890         | -                   | -     |
|  90 | tt     | Tatar                    | 218,102         | -                   | -     |
|  91 | ckb    | Central Kurdish          | 172,035         | -                   | -     |
|  92 | lb     | Luxembourgish            | 165,891         | -                   | -     |
|  93 | mt     | Maltese                  | 151,320         | -                   | -     |
|  94 | nn     | Norwegian Nynorsk        | 126,083         | -                   | -     |
|  95 | qu     | Quechua                  | 1,202           | 72,101              | 0.00  |
|  96 | ba     | Bashkir                  | 71,957          | -                   | -     |
|  97 | arz    | Egyptian Arabic          | 71,625          | -                   | -     |
|  98 | dv     | Divehi                   | 66,702          | -                   | -     |
|  99 | bo     | Tibetan                  | 54,185          | -                   | -     |
| 100 | sh     | Serbian (Latin)          | 45,619          | -                   | -     |
| 101 | yo     | Yoruba                   | 192             | 42,943              | 0.00  |
| 102 | bs     | Bosnian                  | 1,237           | 39,768              | 0.00  |
| 103 | azb    | South Azerbaijani        | 29,833          | -                   | -     |
| 104 | ht     | Haitian Creole           | 12              | 26,183              | 0.00  |
| 105 | war    | Waray                    | 23,687          | -                   | -     |
| 106 | cv     | Chuvash                  | 22,570          | -                   | -     |
| 107 | sah    | Sakha                    | 22,141          | -                   | -     |
| 108 | li     | Limburgish               | 206             | 18,532              | 0.00  |
| 109 | ce     | Chechen                  | 17,322          | -                   | -     |
| 110 | pnb    | Western Panjabi          | 15,625          | -                   | -     |
| 111 | nds    | Low German               | 15,139          | -                   | -     |
| 112 | tk     | Turkmen                  | 14,393          | -                   | -     |
| 113 | gn     | Guarani                  | 103             | 12,708              | 0.00  |
| 114 | oc     | Occitan                  | 10,556          | -                   | -     |
| 115 | xmf    | Mingrelian               | 9,706           | -                   | -     |
| 116 | ast    | Asturian                 | 9,002           | -                   | -     |
| 117 | os     | Ossetic                  | 8,596           | -                   | -     |
| 118 | mhr    | Eastern Mari             | 7,883           | -                   | -     |
| 119 | pms    | Piedmontese              | 7,566           | -                   | -     |
| 120 | als[*] | Swiss German             | 6,936           | -                   | -     |
| 121 | vo     | Volapük                  | 6,621           | -                   | -     |
| 122 | so     | Somali                   | 39              | 6,053               | 0.00  |
| 123 | bpy    | Bishnupriya              | 5,087           | -                   | -     |
| 124 | new    | Newari                   | 4,344           | -                   | -     |
| 125 | hsb    | Upper Sorbian            | 4,244           | -                   | -     |
| 126 | lmo    | Lombard                  | 3,530           | -                   | -     |
| 127 | an     | Aragonese                | 2,746           | -                   | -     |
| 128 | ilo    | Iloko                    | 2,328           | -                   | -     |
| 129 | mzn    | Mazanderani              | 1,914           | -                   | -     |
| 130 | lez    | Lezghian                 | 1,806           | -                   | -     |
| 131 | rm     | Romansh                  | 30              | 1,769               | 0.00  |
| 132 | krc    | Karachay-Balkar          | 1,745           | -                   | -     |
| 133 | min    | Minangkabau              | 1,429           | -                   | -     |
| 134 | kv     | Komi                     | 1,396           | -                   | -     |
| 135 | wa     | Walloon                  | 1,383           | -                   | -     |
| 136 | jbo    | Lojban                   | 1,349           | -                   | -     |
| 137 | io     | Ido                      | 1,144           | -                   | -     |
| 138 | mrj    | Western Mari             | 1,056           | -                   | -     |
| 139 | gom    | Goan Konkani             | 721             | -                   | -     |
| 140 | ia     | Interlingua              | 613             | -                   | -     |
| 141 | av     | Avaric                   | 438             | -                   | -     |
| 142 | bh     | Bihari languages         | 265             | -                   | -     |
| 143 | wuu    | Wu Chinese               | 222             | -                   | -     |
| 144 | nah    | Nahuatl languages        | 131             | -                   | -     |
| 145 | vec    | Venetian                 | 113             | -                   | -     |
| 146 | bxr    | Russia Buriat            | 100             | -                   | -     |
| 147 | kw     | Cornish                  | 94              | -                   | -     |
| 148 | mai    | Maithili                 | 93              | -                   | -     |
| 149 | eml[*] | Emiliano-Romagnol        | 91              | -                   | -     |
| 150 | dsb    | Lower Sorbian            | 59              | -                   | -     |
| 151 | xal    | Kalmyk                   | 51              | -                   | -     |
| 152 | lrc    | Northern Luri            | 43              | -                   | -     |
| 153 | nap    | Neapolitan               | 31              | -                   | -     |
| 154 | tyv    | Tuvinian                 | 23              | -                   | -     |
| 155 | scn    | Sicilian                 | 21              | -                   | -     |
| 156 | frr    | Northern Frisian         | 11              | -                   | -     |
| 157 | mwl    | Mirandese                | 9               | -                   | -     |
| 158 | myv    | Erzya                    | 4               | -                   | -     |
| 159 | ie     | Interlingue              | 4               | -                   | -     |
| 160 | pam    | Pampanga                 | 4               | -                   | -     |
| 161 | bar    | Bavarian                 | 3               | -                   | -     |
| 162 | yue    | Yue Chinese              | 3               | -                   | -     |
| 163 | cbk    | Chavacano                | 2               | -                   | -     |
| 164 | bcl    | Central Bikol            | 1               | -                   | -     |
| 165 | vls    | West Flemish             | 1               | -                   | -     |
| 166 | rue    | Rusyn                    | 1               | -                   | -     |




### Dataset Structure

```json
{
    "text": ...,
    "timestamp": ...,
    "url": ...,
    "source": "mc4" | "OSCAR-xxxx",
}
```



## Considerations for Using the Data

As CulturaX is the cleaned version of the mC4 and OSCAR datasets, which were both extracted from CommonCrawl, personal and sensitive information might still contain personal and sensitive information. 
This must be considered prior to using this dataset for any purpose, such as training deep learning models, etc.


## License Information

The licence terms for CulturaX strictly follows those of `mC4` and `OSCAR`. Please refer to both below licenses when using this dataset.

- [mC4 license](https://huggingface.co/datasets/allenai/c4#license)
- [OSCAR license](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301#licensing-information)


## Citation 

To cite CulturaX, please use:

```
@misc{nguyen2023culturax,
      title={CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages}, 
      author={Thuat Nguyen and Chien Van Nguyen and Viet Dac Lai and Hieu Man and Nghia Trung Ngo and Franck Dernoncourt and Ryan A. Rossi and Thien Huu Nguyen},
      year={2023},
      eprint={2309.09400},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


## Reference

[1] Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and Colin Raffel. 2021. mT5: A massively multilingual
pre-trained text-to-text transformer. In NAACL 2021. https://huggingface.co/datasets/mc4

[2] Pedro Javier Ortiz Suárez, Benoît Sagot, and Laurent Romary. 2019. Asynchronous pipelines for processing huge corpora on medium to low resource infrastructures. In Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-
7) 2019. https://oscar-project.org/

[3] KenLM: Faster and smaller language model queries. In Proceedings of the Sixth
Workshop on Statistical Machine Translation, 2011.