---
license: cc0-1.0
language:
- af
- az
- am
- be
- bg
- dz
- eu
- my
- ca
- cs
- cy
- hr
- zh
- da
- de
- nl
- el
- en
- eo
- es
- et
- fa
- fi
- fr
- gl
- gd
- hi
- hy
- hu
- id
- is
- it
- ja
- ko
- la
- lt
- lv
- mi
- mk
- ml
- ms
- mt
- mr
- mn
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sm
- sq
- te
- ta
- to
- tr
- uk
- uz
- vi
- yid
- zu
pretty_name: List of Dirty Naughty Obscene and Otherwise Bad Words V2
size_categories:
- 10K<n<100K
---
> Written with [StackEdit](https://stackedit.io/).
> ## [List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words_V2](https://github.com/LDNOOBWV2/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words_V2#list-of-dirty-naughty-obscene-and-otherwise-bad-words_v2)

This list of words is a follow-up and extension of the Shutterstock [List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/tree/master) as that list is not maintained anymore. As there are many profanity word lists around on the web (and many not maintained) their content was crabbed and joined here together (see the source list below). 

As the opinion on which words should be in such lists varies between culture, language, and geographies, feel free to extend them to your needs, hopefully getting a lot of feedback.

The lists need reviews from native speakers. It would be great to collect more words and even get more languages (**75** right now, with over **50k words** alltogether).

The long list of English words shows that people got very creative to get around profanity filters. The best way to use these hard-coded word lists is to use them as an additional quality criterion for filtering texts like it is done in [RedPajama](https://github.com/togethercomputer/RedPajama-Data) data set or use them for ML building profanity filters.

### Structure and Format
 - filename is the **iso-code** of the country
 - file extension is **".txt"** 
 - **utf-8** encoded
 - all words are **lowercase**
 - one expression per line
 - if the language has non-ASCII chrachters a transcription with python's "anyascii" is in the wordlist
 - for leed-speech there are python lists for the most common leet replacements in naughty and slang words, see LEET.md for details
 - for English and French there are wordlists with these replacements being already done
 - all words contained in the English "***en.txt***" file are **excluded** in the other language files
 - often used words where the classification as a profane word is doubtful, there is a separate csv file
 - the csv-file is: [questionable_international_words.csv](questionable_international_words.csv)
 - separator is the comma "**,**"
 - **51** words for several languages (see table below)
 - the header line contains the iso-code of the language, a classification column (*category*), and a *remark* column
 - these words are **NOT** included in the language-text-files, e.g. "*.txt"
 - when I couldn't find a translation, the field contains the string: **<NO_TRANSLATION>**
### Languages Files Overview
language | count | filename | in csv-file | remark
--- | --- | --- | --- | ---
 [Afrikaans](data/af.txt)   | 256 | af | Y|
 [Albanian](data/sq.txt)    | 223 | sq | Y|
 [Algerian](data/dz.txt)    |  86 | dz | N|
 [Amharic](data/am.txt)     |  71 | am | N|
 [Arabic](data/ar.txt)      |1609 | ar | N|
 [Armenian](data/hy.txt)    | 440 | hy | Y|
 [Australian Kriol](data/rop.txt)  |  16 | rop| N|
 [Azerbaijanian](data/az.txt)      |  37 | az | N|
 [Basque](data/eu.txt)      |  48 | eu | N|
 [Belorussian](data/be.txt) | 236 | be | N|
 [Bulgarian](data/bg.txt)   | 535 | bg | Y|
 [Burmese](data/my.txt)     | 133 | my | N|
 [Cambodian](data/kh.txt)   | 264 | kh | N|
 [Catalan](data/ca.txt)     | 163 | ca | Y|
 [Cebuano](data/ceb.txt)    |  18 | ceb| N|
 [Chinese](data/zh.txt)     |3090 | zh | Y|
 [Croatian](data/hr.txt)    | 275 | hr | Y|
 [Czech](data/cs.txt)       | 343 | cs | Y|
 [Danish](data/da.txt)      | 227 | da | Y|
 [Dutch](data/nl.txt)       |1224 | nl | Y|
 [English](data/en.txt)     |12996| en | Y| various spelling variations, does not contain Spanish (es) words
 [English](data/en_leet.txt)     |12532| en | Y| version with repaced leet letters, see LEET.md 
 [Esperanto](data/eo.txt)   |  60 | eo | N|
 [Estonian](data/et.txt)    | 203 | et | Y|
 [Filipino](data/fil.txt)   | 165 | fil| Y|
 [Finnish](data/fi.txt)     | 368 | fi | Y|
 [French](data/fr.txt)      |4056 | fr | Y| many spelling variations
 [French](data/fr.txt)      |2380 | fr | Y| version with repaced leet letters, see LEET.md
 [Gaelic](data/gd.txt)      | 105 | gd | N|
 [Galician](data/gl.txt)    |  89 | gl | N|
 [German](data/de.txt)      | 685 | de | Y|
 [Greek](data/el.txt)       | 417 | el | Y|
 [Hebrew](data/yid.txt)     | 173 | yid| N|
 [Hindi](data/hi.txt)       |1102 | hi | Y|
 [Hungarian](data/hu.txt)   | 433 | hu | Y|
 [Icelandic](data/is.txt)   | 208 | is | Y|
 [Italian](data/it.txt)     |1710 | it | Y|
 [Indonesian](data/id.txt)  | 582 | id | Y|
 [Japanese](data/ja.txt)    | 783 | ja | Y|
 [Kabyle](data/kab.txt)     |  31 | kab| N|
 [Klingon](data/tlh.txt)    |  33 | tlh| N|
 [Korean](data/ko.txt)      |6125 | ko | Y|
 [Latin](data/la.txt)       | 103 | la | N|
 [Latvian](data/lv.txt)     | 280 | lv | Y|
 [Lithuanian](data/lt.txt)  | 211 | lt | Y|
 [Macedonian](data/mk.txt)  | 294 | mk | N|
 [Malay](data/ms.txt)       | 201 | ms | Y|
 [Malayalam](data/ml.txt)   | 338 | ml | Y|
 [Maltese](data/mt.txt)     | 132 | mt | Y|
 [Maori](data/mi.txt)       |  75 | mi | Y|
 [Marathi](data/mr.txt)     | 453 | mr | Y|
 [Mongolian](data/mn.txt)   | 164 | mn | N|
 [Norwegian](data/no.txt)   | 341 | no | Y|
 [Persian](data/fa.txt)     |1128 | fa | N|
 [Pictrain-Norfolk](data/pih.txt)  |  14 | pih| N|
 [Piya-Kwonci](data/piy.txt)       |  13 | piy| N|
 [Polish](data/pl.txt)      |12639 | pl | Y| different grammatical variations
 [Portuguese](data/pt.txt)  | 629 | pt | Y| including Brasilian
 [Romanian](data/ro.txt)    | 341 | ro | Y|
 [Russian](data/ru.txt)     |9569 | ru | Y|
 [Samoan](data/sm.txt)      | 116 | sm | Y|
 [Serbian](data/sr.txt)     | 459 | sr | Y| sr_k & sr_l in csv file
 [Slovak](data/sk.txt)      | 586 | sk | Y|
 [Slovene](data/sl.txt)     | 186 | sl | Y|
 [Spanish](data/es.txt)     |1804 | es | Y| including Middle- and South American
 [Swedish](data/sv.txt)     | 304 | sv | Y|
 [Tamil](data/ta.txt)       | 143 | ta | N|
 [Telugu](data/te.txt)      | 509 | te | Y|
 [Tetum](data/tet.txt)      |  11 | tet| N|
 [Thai](data/th.txt)        |4377 | th | Y|
 [Tongan](data/to.txt)      |  68 | to | N|
 [Turkish](data/tr.txt)     | 491 | tr | Y|
 [Ukrainian](data/uk.txt)   | 377 | uk | Y|
 [Uzbek](data/uz.txt)       | 102 | uz | N|
 [Vietnamese](data/vi.txt)  |1031 | vi | Y|
 [Welsh](data/cy.txt)       | 169 | cy | Y|
 [Zulu](data/zu.txt)        | 115 | zu | N| 
### Categories in *questionable_international_words.csv*
The categories used are:
 - **cul**: cultural differences
 - **dm**: drugs & medicine
 - **his**: historical 
 - **leg**: Legislative term
 - **mab**: medical, anatomic, biological term
 - **pol**: political
 - **rel**: religious
 - **so**: sexual orientation
 - **vm**: various meanings

 This is just an ad hoc classification where several expressions can be in different categories.