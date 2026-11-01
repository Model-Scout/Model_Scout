---
configs:
- config_name: "EnglishNA"
  default: True
  data_files: Eng-NA/processed.csv
- config_name: "EnglishUK"
  data_files: Eng-UK/processed.csv
- config_name: "French"
  data_files: French/processed.csv
- config_name: "German"
  data_files: German/processed.csv
- config_name: "Spanish"
  data_files: Spanish/processed.csv
- config_name: "Dutch"
  data_files: Dutch/processed.csv
- config_name: "Mandarin"
  data_files: Mandarin/processed.csv
- config_name: "Japanese"
  data_files: Japanese/processed.csv
- config_name: "Cantonese"
  data_files: Cantonese/processed.csv
- config_name: "Estonian"
  data_files: Estonian/processed.csv
- config_name: "Croatian"
  data_files: Croatian/processed.csv
- config_name: "Danish"
  data_files: Danish/processed.csv
- config_name: "Basque"
  data_files: Basque/processed.csv
- config_name: "Hungarian"
  data_files: Hungarian/processed.csv
- config_name: "Turkish"
  data_files: Turkish/processed.csv
- config_name: "Farsi"
  data_files: Farsi/processed.csv
- config_name: "Icelandic"
  data_files: Icelandic/processed.csv
- config_name: "Indonesian"
  data_files: Indonesian/processed.csv
- config_name: "Irish"
  data_files: Irish/processed.csv
- config_name: "Welsh"
  data_files: Welsh/processed.csv
- config_name: "Korean"
  data_files: Korean/processed.csv
- config_name: "Swedish"
  data_files: Swedish/processed.csv
- config_name: "Norwegian"
  data_files: Norwegian/processed.csv
- config_name: "Quechua"
  data_files: Quechua/processed.csv
- config_name: "Catalan"
  data_files: Catalan/processed.csv
- config_name: "Italian"
  data_files: Italian/processed.csv
- config_name: "PortuguesePt"
  data_files: PortuguesePt/processed.csv
- config_name: "PortugueseBr"
  data_files: PortugueseBr/processed.csv
- config_name: "Romanian"
  data_files: Romanian/processed.csv
- config_name: "Serbian"
  data_files: Serbian/processed.csv
- config_name: "Polish"
  data_files: Polish/processed.csv
language:
- en
- de
- fr
- es
- nl
- cmn
- ja
- yue
- et
- hr
- da
- eu
- hu
- tr
- fa
- is
- id
- ga
- cy
- ko
- sv
- nb
- qu
- ca
- it
- pt
- ro
- sv
- pl
tags:
- language modeling
- cognitive modeling
pretty_name: Phonemized Child Directed Speech
size_categories:
- 100K<n<1M
- 1M<n<10M
---

# IPA-CHILDES Dataset

This dataset contains utterances downloaded from CHILDES which have been pre-processed and converted to a phonemic representation. Read the paper [here](https://arxiv.org/abs/2504.03036). 

## Description

### Key Columns

The scripts used to create the dataset are available [here](https://github.com/codebyzeb/ipa-childes). Many of the columns from CHILDES have been preserved as they are useful for experiments (e.g. number of morphemes, part-of-speech tags, etc.). The key columns added by the processing script are as follows:

| Column | Description |
|:----|:-----|
| `processed_gloss`| The pre-processed orthographic utterance. This includes lowercasing, fixing English spelling and adding punctuation marks. This is based on the [AOChildes](https://github.com/UIUCLearningLanguageLab/AOCHILDES) preprocessing.|
| `ipa_transcription`| A phonemic transcription of the utterance, space-separated with word boundaries marked with the `WORD_BOUNDARY` token.|
| `character_split_utterance`| A space-separated transcription of the utterance, produced simply by splitting the processed gloss by character. This is intended to have a very similar format to `ipa_transcription` for studies comparing phonetic to orthographic transcriptions. |
| `is_child`| Whether the utterance was spoken by a child or not. Note that this is set to `False` for all utterances in this dataset, but the processing script has the ability to preserve child utterances.|

`character_split_utterance` and `ipa_transcription` are designed for training character-based (phoneme-based) language models using a simple tokenizer that splits around whitespace. The `processed_gloss` column is suitable for word-based (or subword-based) language models with standard tokenizers. 

Note that the data has been sorted by the `target_child_age` column, which stores child age in months. This can be used to limit the training data according to a maximum child age.

### Dataset Sections

The following languages are included (ordered by number of phonemes):

Language | Description | Phoible Inventory ID | Speakers | Utterances | Words | Phonemes | % Child
|:----|:----|:----|:----|:----|:----|:----|:----|
| EnglishNA| Taken from 49 corpora in the EnglishNA collection of CHILDES and phonemized using `phonemizer` with language code `en-us`.| [2175](https://phoible.org/inventories/view/2175)| 3,687| 2,564,614| 9,993,744| 30,986,218| 35.83
| EnglishUK| Taken from 16 corpora in the EnglishUK collection of CHILDES and phonemized using `phonemizer` with language code `en-gb`.| [2252](https://phoible.org/inventories/view/2252)| 869| 2,043,115| 7,147,541| 21,589,842| 39.00
| German| Taken from 10 corpora in the German collection of CHILDES and phonemized using `epitran` with language code `deu-Latn`.| [2398](https://phoible.org/inventories/view/2398)| 829| 1,525,559| 5,825,166| 21,442,576| 43.61
| Japanese| Taken from 11 corpora in the Japanese collection of CHILDES and phonemized using `phonemizer` with language code `ja`.| [2196](https://phoible.org/inventories/view/2196)| 489| 998,642| 2,970,674| 11,985,729| 44.20
| Indonesian| Taken from 1 corpora in the EastAsian/Indonesian collection of CHILDES and phonemized using `epitran` with language code `ind-Latn`.| [1690](https://phoible.org/inventories/view/1690)| 438| 813,795| 2,347,642| 9,370,983| 34.32
| French| Taken from 15 corpora in the French collection of CHILDES and phonemized using `phonemizer` with language code `fr-fr`.| [2269](https://phoible.org/inventories/view/2269)| 1,277| 721,121| 2,973,318| 8,203,649| 40.07
| Spanish| Taken from 18 corpora in the Spanish collection of CHILDES and phonemized using `epitran` with language code `spa-Latn`.| [164](https://phoible.org/inventories/view/164)| 1,009| 533,308| 2,183,992| 7,742,550| 45.93
| Mandarin| Taken from 16 corpora in the Chinese/Mandarin collection of CHILDES and phonemized using `pinyin_to_ipa` with language code `mandarin`.| [2457](https://phoible.org/inventories/view/2457)| 2,118| 530,022| 2,264,198| 6,605,913| 38.88
| Dutch| Taken from 5 corpora in the DutchAfricaans/Dutch collection of CHILDES and phonemized using `phonemizer` with language code `nl`.| [2405](https://phoible.org/inventories/view/2405)| 107| 403,472| 1,475,174| 4,786,803| 35.08
| Polish| Taken from 2 corpora in the Slavic/Polish collection of CHILDES and phonemized using `phonemizer` with language code `pl`.| [1046](https://phoible.org/inventories/view/1046)| 511| 218,860| 1,042,841| 4,361,797| 63.26
| Serbian| Taken from 1 corpora in the Slavic/Serbian collection of CHILDES and phonemized using `epitran` with language code `srp-Latn`.| [2499](https://phoible.org/inventories/view/2499)| 208| 319,305| 1,052,337| 3,841,600| 29.14
| Estonian| Taken from 9 corpora in the Other/Estonian collection of CHILDES and phonemized using `phonemizer` with language code `et`.| [2181](https://phoible.org/inventories/view/2181)| 157| 186,921| 843,189| 3,429,228| 44.71
| Welsh| Taken from 2 corpora in the Celtic/Welsh collection of CHILDES and phonemized using `phonemizer` with language code `cy`.| [2406](https://phoible.org/inventories/view/2406)| 269| 181,292| 666,350| 1,939,286| 69.18
| Cantonese| Taken from 2 corpora in the Chinese/Cantonese collection of CHILDES and phonemized using `pingyam` with language code `cantonese`.| [2309](https://phoible.org/inventories/view/2309)| 95| 205,729| 777,997| 1,864,771| 33.54
| Swedish| Taken from 3 corpora in the Scandinavian/Swedish collection of CHILDES and phonemized using `phonemizer` with language code `sv`.| [1150](https://phoible.org/inventories/view/1150)| 41| 154,064| 581,451| 1,782,692| 44.63
| PortuguesePt| Taken from 4 corpora in the Romance/Portuguese collection of CHILDES and phonemized using `phonemizer` with language code `pt`.| [2206](https://phoible.org/inventories/view/2206)| 45| 134,543| 499,522| 1,538,408| 39.47
| Korean| Taken from 3 corpora in the EastAsian/Korean collection of CHILDES and phonemized using `phonemizer` with language code `ko`.| [423](https://phoible.org/inventories/view/423)| 127| 105,281| 263,030| 1,345,276| 36.76
| Italian| Taken from 5 corpora in the Romance/Italian collection of CHILDES and phonemized using `phonemizer` with language code `it`.| [1145](https://phoible.org/inventories/view/1145)| 109| 94,361| 352,861| 1,309,489| 39.02
| Croatian| Taken from 1 corpora in the Slavic/Croatian collection of CHILDES and phonemized using `epitran` with language code `hrv-Latn`.| [1139](https://phoible.org/inventories/view/1139)| 54| 90,992| 305,112| 1,109,696| 39.24
| Catalan| Taken from 6 corpora in the Romance/Catalan collection of CHILDES and phonemized using `phonemizer` with language code `ca`.| [2555](https://phoible.org/inventories/view/2555)| 180| 89,103| 319,726| 1,084,594| 36.49
| Icelandic| Taken from 2 corpora in the Scandinavian/Icelandic collection of CHILDES and phonemized using `phonemizer` with language code `is`.| [2568](https://phoible.org/inventories/view/2568)| 17| 78,181| 279,939| 1,057,235| 35.21
| Basque| Taken from 2 corpora in the Other/Basque collection of CHILDES and phonemized using `phonemizer` with language code `eu`.| [2161](https://phoible.org/inventories/view/2161)| 286| 71,537| 230,500| 942,725| 48.82
| Hungarian| Taken from 3 corpora in the Other/Hungarian collection of CHILDES and phonemized using `epitran` with language code `hun-Latn`.| [2191](https://phoible.org/inventories/view/2191)| 116| 69,690| 237,062| 918,002| 47.95
| Danish| Taken from 1 corpora in the Scandinavian/Danish collection of CHILDES and phonemized using `phonemizer` with language code `da`.| [2265](https://phoible.org/inventories/view/2265)| 29| 84,019| 275,170| 824,314| 41.71
| Norwegian| Taken from 2 corpora in the Scandinavian/Norwegian collection of CHILDES and phonemized using `phonemizer` with language code `nb`.| [499](https://phoible.org/inventories/view/499)| 34| 61,906| 227,856| 729,649| 42.58
| PortugueseBr| Taken from 2 corpora in the Romance/Portuguese collection of CHILDES and phonemized using `phonemizer` with language code `pt-br`.| [2207](https://phoible.org/inventories/view/2207)| 331| 22,439| 174,845| 577,865| 44.42
| Romanian| Taken from 3 corpora in the Romanian collection of CHILDES and phonemized using `phonemizer` with language code `ro`.| [2443](https://phoible.org/inventories/view/2443)| 33| 54,982| 152,465| 537,669| 42.62
| Turkish| Taken from 2 corpora in the Other/Turkish collection of CHILDES and phonemized using `phonemizer` with language code `tr`.| [2217](https://phoible.org/inventories/view/2217)| 118| 29,317| 79,404| 421,129| 50.58
| Irish| Taken from 2 corpora in the Celtic/Irish collection of CHILDES and phonemized using `phonemizer` with language code `ga`.| [2521](https://phoible.org/inventories/view/2521)| 29| 27,818| 105,867| 338,425| 34.37
| Quechua| Taken from 2 corpora in the Other/Quechua collection of CHILDES and phonemized using `phonemizer` with language code `qu`.| [104](https://phoible.org/inventories/view/104)| 14| 22,397| 46,848| 281,478| 40.06
| Farsi| Taken from 2 corpora in the Other/Farsi collection of CHILDES and phonemized using `phonemizer` with language code `fa-latn`.| [516](https://phoible.org/inventories/view/516)| 29| 22,613| 43,432| 178,523| 40.45

### Papers

This dataset has been used in the following key papers:

- [IPA-CHILDES & G2P+: Feature-Rich Resources for Cross-Lingual Phonology and Phonemic Language Modeling](https://arxiv.org/abs/2504.03036)
- [BabyLM's First Words: Word Segmentation as a Phonological Probing Task](https://arxiv.org/abs/2504.03338)