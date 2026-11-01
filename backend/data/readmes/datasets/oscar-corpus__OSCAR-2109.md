---
extra_gated_prompt: "**[IMPORTANT: We are forced to temporarily suspend access to OSCAR. The temporary nature of this suspension has led us to choose to implement it as gated access with manual control, and we will not grant any access until the situation has been clarified. We sincerely apologize for this situation and hope to be able to restore access as soon as possible. In the meantime, we remind you that we have always prohibited access to or use of OSCAR that violates the legislation in force where you are located. In France, for example, any use of OSCAR that does not fall within the framework of the so-called 'TDM' or the so-called 'research' exceptions to copyright has always been prohibited.]** By filling the form below, you understand that only the metadata and the annotations of OSCAR 21.09 have a cc0-1.0 license, and that the rest of the content is crawled data derived from the February 2021 snapshot of Common Crawl, for which the authors of OSCAR **do not** hold any copyright whatsoever."
extra_gated_fields:
 Name: text
 Email: text
 Affiliation: text
 Country: text
 Usecase: text
 I have explicitly check with my jurisdiction and I confirm that downloading OSCAR 2109 is legal in the country/region where I am located right now, and for the use case that I have described above: checkbox
pretty_name: OSCAR
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- als
- gsw    
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
- diq
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
- gv
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
- sco
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
- zh
license:
- cc0-1.0
multilinguality:
- multilingual
size_categories:
- n>1T
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- language-modeling
paperswithcode_id: oscar
---

# Dataset Card for "oscar"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://oscar-corpus.com](https://oscar-corpus.com)
- **Repository:** [github.com/oscar-corpus/corpus](https://github.com/oscar-corpus/corpus)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

OSCAR or **O**pen **S**uper-large **C**rawled **A**ggregated co**R**pus is a huge multilingual corpus obtained by language classification and filtering of the [Common Crawl](https://commoncrawl.org/) corpus using the [ungoliant](https://github.com/oscar-corpus/ungoliant) architecture. Data is distributed by language in both original and deduplicated form.

### Supported Tasks and Leaderboards

OSCAR is mainly inteded to pretrain language models and word represantations.

### Languages

All the data is distributed by language, both the original and the deduplicated versions of the data are available. 168 different languages are available. The table in subsection [Data Splits Sample Size](#data-splits-sample-size) provides the language code for each subcorpus as well as the number of words (space separated tokens), lines and sizes for both the original and the deduplicated versions of OSCAR.

### Issues

OSCAR 21.09 has known issues regarding specific languages.
Note that other issues may (and could) be present in other languages. 

**If you encounter something that is unexpected, please file an issue here: https://github.com/oscar-corpus/corpus/issues.**

|Language code|Language|Issues|
|-------------|--------|------|
|`tg`|Tajik|[![Tajik issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:tg?label=tg&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Atg+label%3Aver%3A21.09)|
|`tr`|Turkish|[![Turkish issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:tr?label=tr&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Atr+label%3Aver%3A21.09)|
|`vls`|West Flemish|[![West Flemish issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:vls?label=vls&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aopen+label%3Alang%3Avls+label%3Aver%3A21.09)|
|`wuu`|Wu Chinese|[![Wu Chinese issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:wuu?label=wuu&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Awuu+label%3Aver%3A21.09)|
|`nap`|Neapolitan|[![Neapolitan issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:nap?label=nap&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Anap+label%3Aver%3A21.09)|
|`so`|Somali|[![Somali issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:so?label=so&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Aso+label%3Aver%3A21.09)|
|`frr`|Northern Frisian|[![Northern Frisian issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:frr?label=frr&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Afrr+label%3Aver%3A21.09)|
|`cbk`|Chavacano|[![Chavacano issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:cbk?label=cbk&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Acbk+label%3Aver%3A21.09)|
|`sco`|Scots|[![Scots issues](https://img.shields.io/github/issues/oscar-corpus/corpus/lang:sco?label=sco&style=for-the-badge)](https://github.com/oscar-corpus/corpus/issues?q=is%3Aissue+is%3Aopen+label%3Alang%3Asco+label%3Aver%3A21.09)|
## Dataset Structure

We show detailed information for all the configurations of the dataset.

### Data Instances


<details>
<summary>Click to expand the Data/size information for each language (deduplicated)</summary>

#### deduplicated_af
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3287,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:BUOBNDDY3VZKNNUOY33PAWBXEVNDCDJK',
                         'warc-date': '2021-03-09T04:21:33Z',
                         'warc-identified-content-language': 'afr,eng',
                         'warc-record-id': '<urn:uuid:dece1e30-a099-411a-87fd-483791342d48>',
                         'warc-refers-to': '<urn:uuid:5a35e8b2-0fcb-4600-9d15-f5c6469ddf01>',
                         'warc-target-uri': 'http://www.northwestnewspapers.co.za/gemsbok/2015-06-18-10-02-17/hoe-om-n-ad-te-plaas/1907-man-betrap-met-jagluiperd-en-leeu-bene',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': 'Stap 2: Tik jou ad in die teks boksie, jy sal sien dat die prys aan '
          'die regterkant van die boksie verander volgens di...'}
```

#### deduplicated_als
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4607,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:URQ53Z4I4KGPHICZYLW2ZOX7OWWCGZUA',
                         'warc-date': '2021-03-03T16:09:20Z',
                         'warc-identified-content-language': 'deu,eng',
                         'warc-record-id': '<urn:uuid:134499db-d54a-4c29-9517-350cacc3d29d>',
                         'warc-refers-to': '<urn:uuid:073aeb77-b4ed-47eb-b955-27031963acf4>',
                         'warc-target-uri': 'https://als.m.wikipedia.org/wiki/Neukaledonien',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'D Wirtschaft bestoot vor allem us Handwärk, Bärgbau, Industrii und '
          'Turismus. 40 Kilometer vo dr Hauptstadt Nouméa äwä...'}
```

#### deduplicated_am
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9679,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:YADJOQVUOQHUKJ7BXCKKU4LRFKE3JPOA',
                         'warc-date': '2021-03-09T04:16:32Z',
                         'warc-identified-content-language': 'amh,eng',
                         'warc-record-id': '<urn:uuid:fa02fe22-c72e-42e8-9cb3-89da85a80941>',
                         'warc-refers-to': '<urn:uuid:ff89f862-5e6a-41aa-bc40-ef1d2f91d258>',
                         'warc-target-uri': 'http://ethioforum.ethiopiaforums.com/viewtopic.php?f=6&t=3874&p=6511',
                         'warc-type': 'conversion'},
            'nb_sentences': 10,
            'offset': 0},
  'text': '(ፍኖተ ነፃነት) በኢትዮጵያ የአዉሮፓ ሕብረት ልኡካን ቡድን መሪ አምባሳደር ቻንታል ሔበሬሽ፣ በአዉሮፓ '
          'ሕብረት የአፍሪካ ቀንድ እና የሕንድ ዉቂያኖስ አካባቢ ዴስክ ኦፌሴር ቪክቶሪያ ጋርሲ...'}
```

#### deduplicated_an
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 134014,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OG2T3MJFSLSH33PVI7D3WPXVE6ZFLZ4Z',
                         'warc-date': '2021-03-08T00:58:33Z',
                         'warc-identified-content-language': 'ara,fra',
                         'warc-record-id': '<urn:uuid:0ef1d002-86e7-49c1-ac8a-8ba933d190ee>',
                         'warc-refers-to': '<urn:uuid:5071f1f7-3350-406d-ad97-f292fe7a2ff0>',
                         'warc-target-uri': 'http://dorous.ek.la/1-5-a6032874?reply_comm=68653652',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووو...'}
```

#### deduplicated_ar
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12677,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:NFDDUGANGSGSFXIQAXEGIVHGRLFCUW55',
                         'warc-date': '2021-03-04T02:22:39Z',
                         'warc-identified-content-language': 'ara,eng',
                         'warc-record-id': '<urn:uuid:3ea1e651-68f3-4dde-bfea-7a12e5331084>',
                         'warc-refers-to': '<urn:uuid:dcecf9ad-1797-44d0-b06a-010c424ba396>',
                         'warc-target-uri': 'https://elmgals.net/?p=62804',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'مطحنة الكرة في ماسبات - orioloingeu. مطاحن الفرينة في مطحنة الكرة '
          'مراكز بيع الة طحن التوابل بيع ألات لرحي اسعار بيع ا...'}
```

#### deduplicated_arz
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9603,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:6O2LEGAWXAWYSRH2TQNYOWX47ZFWTKRC',
                         'warc-date': '2021-03-09T03:51:17Z',
                         'warc-identified-content-language': 'ara',
                         'warc-record-id': '<urn:uuid:0578411b-367f-4d52-b85c-56b4bb64c0be>',
                         'warc-refers-to': '<urn:uuid:8777119c-434c-49a1-80a8-f2b23fa0e21c>',
                         'warc-target-uri': 'https://www.hko-ommen.nl/Nov_01/605.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'مستعملة 4265 كسارات للبيع - كسارة الحجر. كسارات مستعمله للبيع فى '
          'مصر. للبيع كسارات فى مصرمطلوب كسارات حجر مستعملة للب...'}
```

#### deduplicated_as
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9280,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DORQKORQ4TURDN35T75TW72IZ7IZIEFG',
                         'warc-date': '2021-03-03T15:06:57Z',
                         'warc-identified-content-language': 'asm,eng',
                         'warc-record-id': '<urn:uuid:fd6c3650-f91f-4f03-ae7a-bea654e043bb>',
                         'warc-refers-to': '<urn:uuid:48f057d6-f642-42d2-8de1-fec8e4fca4d4>',
                         'warc-target-uri': 'https://assam.nenow.in/%E0%A6%95%E0%A6%BE%E0%A6%87%E0%A6%B2%E0%A7%88%E0%A7%B0-%E0%A6%AA%E0%A7%B0%E0%A6%BE-%E0%A6%AF%E0%A7%8B%E0%A7%B0%E0%A6%B9%E0%A6%BE%E0%A6%9F%E0%A6%A4-%E0%A6%86%E0%A7%B0%E0%A6%AE%E0%A7%8D%E0%A6%AD/',
                         'warc-type': 'conversion'},
            'nb_sentences': 8,
            'offset': 0},
  'text': 'যোৰহাট জিলাৰ এন আৰ চি উন্নিতকৰণৰ প্ৰথম পৰ্য্যায়ৰ বংশবৃক্ষ পৰীক্ষণৰ '
          'কাম কাইলৈৰ পৰা পৰীক্ষামূলকভাৱে আৰু ১৯ ফেব্ৰুৱাৰিৰ ...'}
```

#### deduplicated_ast
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3752,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:BU44BHPYU2BOWH4TUAY7ZOEBFVQ6KD44',
                         'warc-date': '2021-03-01T15:56:44Z',
                         'warc-identified-content-language': 'spa',
                         'warc-record-id': '<urn:uuid:2b3ca12f-6614-4662-a4e9-16e1ce13a8b0>',
                         'warc-refers-to': '<urn:uuid:0e132db0-e0f4-44c5-ab63-48b7594a35a6>',
                         'warc-target-uri': 'https://elsummum.es/tag/dial-traxel-pais/',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Esta ye la galería d’imáxenes de los participantes nel concursu, el '
          'xuráu y dellos miembros de la organización de la ...'}
```

#### deduplicated_av
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2012,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:EULKS66PQCWWVXHNRPSISI72G3GFJD7L',
                         'warc-date': '2021-03-01T10:13:53Z',
                         'warc-identified-content-language': 'rus,eng',
                         'warc-record-id': '<urn:uuid:c2986179-7947-4184-9df5-dca05c987055>',
                         'warc-refers-to': '<urn:uuid:8b3e82e1-0964-4677-8b39-9bd3c67be25b>',
                         'warc-target-uri': 'http://gazetalevashi.ru/articles/media/2019/10/25/diktant-tiobitiana/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Дагъистаналъул жамгIият рахьдал мацIал цIуниялде ва '
          'церетIезариялде, тарих, гIадатал, маданият ва дагъистаналъул '
          'халк...'}
```

#### deduplicated_az
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 59868,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:LDASIZ5NDJU6NRCJW7XCCI4QRLFIZZQX',
                         'warc-date': '2021-02-26T04:13:32Z',
                         'warc-identified-content-language': 'aze',
                         'warc-record-id': '<urn:uuid:a35cc521-926e-442d-b285-299ea4a3b72a>',
                         'warc-refers-to': '<urn:uuid:b60fd7ea-7056-4ebb-8ae5-eb02617ca8cd>',
                         'warc-target-uri': 'https://azrefs.org/iqtisadi-tesebbuslere-yardim-ictimai-birliyi-yerli-seviyyede-i.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 70,
            'offset': 0},
  'text': 'İQTİsadi TƏŞƏBBÜSLƏRƏ yardim iCTİMAİ BİRLİYİ Yerli səviyyədə içməli '
          'su təchizatı sisteminin idarə olunması\n'
          'Az1009, Az...'}
```

#### deduplicated_azb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5245,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XWTKHZGKVJI6ZAIKSTOA4AOP5PCWI2SH',
                         'warc-date': '2021-03-05T13:35:27Z',
                         'warc-identified-content-language': 'fas,uzb,eng',
                         'warc-record-id': '<urn:uuid:41816fd7-985e-4e35-b79b-bf471e68dd80>',
                         'warc-refers-to': '<urn:uuid:5717a90d-021c-428b-a69d-45d6cb2fc692>',
                         'warc-target-uri': 'https://azb.wikipedia.org/wiki/%D8%A2%D9%85%D8%B3%D8%AA%D8%B1%D8%AF%D8%A7%D9%85_%D8%A8%DB%8C%D9%84%DB%8C%D9%85%E2%80%8C%DB%8C%D9%88%D8%B1%D8%AF%D9%88',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'یازی Creative Commons Attribution-ShareAlike '
          'License;آلتیندا\u200cدیر آرتیق شرطلر آرتیریلا بیلر. آرتیق ایطلاعات '
          'اوچون ایشل...'}
```

#### deduplicated_ba
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9444,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:NRTIKDSYAPTPQ64CKKLNR6TFVUYG7CLR',
                         'warc-date': '2021-03-09T04:46:56Z',
                         'warc-identified-content-language': 'uig,eng',
                         'warc-record-id': '<urn:uuid:b69f43f4-0e19-4cad-b083-fce91a40f64b>',
                         'warc-refers-to': '<urn:uuid:3176da53-14ff-4f65-91e4-4d209e9c7190>',
                         'warc-target-uri': 'https://uyghurix.net/archives/date/2016/05?uls=us',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': 'линакис системисиниң көрүнмә йүзи барғансери ишлитишкә қулайлиқ '
          'болуп, кәң ишлитиливатқан болсиму, әмили хизмәттә йән...'}
```

#### deduplicated_bar
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 105623,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:L7EXHEWTVKPV7BWPZJFKHM2TZ3ZNKPWC',
                         'warc-date': '2021-03-07T18:33:16Z',
                         'warc-identified-content-language': 'fra',
                         'warc-record-id': '<urn:uuid:578af8ce-2149-42e3-978c-5191caaaca8c>',
                         'warc-refers-to': '<urn:uuid:a7afc792-983c-43b7-9b5b-75b2dc5fcd77>',
                         'warc-target-uri': 'https://fr.readkong.com/page/automne-hiver-printemps-2017-8342349',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': '                                                                                                      '
          'vo\n'
          '            ...'}
```

#### deduplicated_be
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3159,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TEJML7M4S55254DZU43DXXORKPZMKGUL',
                         'warc-date': '2021-03-09T05:47:09Z',
                         'warc-identified-content-language': 'bel,eng',
                         'warc-record-id': '<urn:uuid:e22883c9-5622-4a0e-b259-b5265e6e345a>',
                         'warc-refers-to': '<urn:uuid:7ec2102d-2645-4fd9-89b8-557762996439>',
                         'warc-target-uri': 'https://be-tarask.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D1%8D%D0%B3%D0%BE%D1%80%D1%8B%D1%8F:%D0%9F%D1%80%D1%8D%D1%81%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B0%D0%B4%D0%B0',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Гэты тэкст даступны на ўмовах ліцэнзіі Creative Commons '
          'Attribution/Share-Alike 3.0; у асобных выпадках могуць ужывац...'}
```

#### deduplicated_bg
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 23651,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:QDAV5ZVRR2IGND4ANWTVOBPNO2POZUEQ',
                         'warc-date': '2021-03-08T21:47:20Z',
                         'warc-identified-content-language': 'bul',
                         'warc-record-id': '<urn:uuid:0e422a1d-ac8c-4f21-bb71-e5c65282f30c>',
                         'warc-refers-to': '<urn:uuid:0109dba6-8f1a-4047-bdd5-cbcc38de63a8>',
                         'warc-target-uri': 'http://europe.bg/bg/bulgariya-poluchava-resor-inovacii-i-mladezh',
                         'warc-type': 'conversion'},
            'nb_sentences': 37,
            'offset': 0},
  'text': 'От хилядите кубинци и другите граждани на страните от СИВ, '
          'командировани на строежа на АЕЦ-а, в Белене е останал само...'}
```

#### deduplicated_bh
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9021,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:IN7PHDOP7MZD6RHN6KIJ7SXTY7VC76SK',
                         'warc-date': '2021-03-08T22:57:31Z',
                         'warc-identified-content-language': 'hin,eng',
                         'warc-record-id': '<urn:uuid:62e18c96-cd2c-461b-93d9-900d95eec89e>',
                         'warc-refers-to': '<urn:uuid:73ee6388-6f0a-460d-ac2e-bbc1a2b63bb4>',
                         'warc-target-uri': 'https://bh.wikipedia.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80:%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE_%E0%A4%97%E0%A5%88%E0%A4%B0-%E0%A4%AE%E0%A5%81%E0%A4%95%E0%A5%8D%E0%A4%A4_%E0%A4%AB%E0%A4%BE%E0%A4%87%E0%A4%B2_%E0%A4%B5%E0%A5%88%E0%A4%A7_%E0%A4%AC%E0%A5%88%E0%A4%95%E0%A4%B2%E0%A4%BF%E0%A4%82%E0%A4%95_%E0%A4%95%E0%A5%87_%E0%A4%B8%E0%A4%BE%E0%A4%A5?from=Ea',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ई एगो छुपावल गइल श्रेणी बाटे। ई पन्ना सभ पर तबले ना लउकी जबले कि '
          'प्रयोगकर्ता के सेटिंग, छुपावल गइल श्रेणी देखावे खाति...'}
```

#### deduplicated_bn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 36198,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:7QRYGJ3YDG7SBTFUVMMALFA6UWNDVLVY',
                         'warc-date': '2021-03-05T07:10:58Z',
                         'warc-identified-content-language': 'ben',
                         'warc-record-id': '<urn:uuid:050c0cdb-562c-49e5-bcb6-7e5350531ea6>',
                         'warc-refers-to': '<urn:uuid:a3749b59-4285-4e90-ba64-aa9d745c1f46>',
                         'warc-target-uri': 'https://www.kalerkantho.com/online/business/2020/12/06/982949',
                         'warc-type': 'conversion'},
            'nb_sentences': 8,
            'offset': 0},
  'text': 'নিজস্ব সংবাদদাতা: গাড়ি নয় যেন মানুষের খাঁচা। নেই কোন ভালো বসার '
          'আসন, যা আছে সেগুলো ভাঙ্গাচুরা, ময়লা ও ধুলাবালিতে ভর...'}
```

#### deduplicated_bo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5059,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XHKOQL5IQBLCVBANFVH66ZZXJZHEEMYW',
                         'warc-date': '2021-03-03T15:06:26Z',
                         'warc-identified-content-language': 'zho,bod',
                         'warc-record-id': '<urn:uuid:3a406f8f-58cd-4990-ae6f-f63dff7e06e3>',
                         'warc-refers-to': '<urn:uuid:806c4a11-f8cd-49e8-bc22-cae5e0cf6ef2>',
                         'warc-target-uri': 'http://tcansee.com/goods.php?id=392',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '所有分类 藏学名家名著 国内名家名著 国外名家名著政治 社会 法律 政治 法律 社会 经济文学 艺术 旅游 艺术 文学 旅游宗教 历史 '
          '文化 宗教 历史 文化教育 童书 工具书 教辅 童书 工具书语言文字 语言研究 语言 文字期刊 社...'}
```

#### deduplicated_bpy
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8270,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:POHCGWDC32KW74IE26NTJ2UMNX7QRBDB',
                         'warc-date': '2021-03-05T14:00:16Z',
                         'warc-identified-content-language': 'ben',
                         'warc-record-id': '<urn:uuid:d53007ee-ddbe-44e9-8253-235567d2960c>',
                         'warc-refers-to': '<urn:uuid:0409ce75-26bc-4a60-b08d-4e2b6174127e>',
                         'warc-target-uri': 'http://pobnapurup.gaibandha.gov.bd/site/page/5dc0a075-18fd-11e7-9461-286ed488c766/%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%AC%E0%A6%B2%E0%A7%80',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'পবনাপুর ইউনিয়ন---কিশোরগাড়ী ইউনিয়নহোসেনপুর ইউনিয়নপলাশবাড়ী '
          'ইউনিয়নবরিশাল ইউনিয়নমহদীপুর ইউনিয়নবেতকাপা ইউনিয়নপবনাপুর ইউনিয়...'}
```

#### deduplicated_br
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3134,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:U353JBWLMC22GRYEIDN4WOSBUOIUMYQT',
                         'warc-date': '2021-02-24T21:00:25Z',
                         'warc-identified-content-language': 'bre',
                         'warc-record-id': '<urn:uuid:49d1650d-aaf5-43b9-b340-326746e88b31>',
                         'warc-refers-to': '<urn:uuid:04877e5f-6b86-497e-b39c-30a72683261f>',
                         'warc-target-uri': 'https://br.m.wiktionary.org/wiki/dont',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Sellet e vez ouzh ar bajenn pe ar gevrenn-mañ evel un divraz da '
          'glokaat e brezhoneg. Mar gouezit tra pe dra diwar-ben...'}
```

#### deduplicated_bs
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8483,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:HS77KGP5HJKJASHMW6WSYV326BPGVM35',
                         'warc-date': '2021-02-24T18:13:58Z',
                         'warc-identified-content-language': 'bos,hrv',
                         'warc-record-id': '<urn:uuid:c12f1b14-4194-405e-a059-9af2f7146940>',
                         'warc-refers-to': '<urn:uuid:31bedcb4-265f-4aa3-8d2c-cfdc64c42325>',
                         'warc-target-uri': 'http://mojusk.ba/zastrasujuce-slike-tamnice-u-kojoj-je-skolski-domar-silovao-12-godisnjakinju/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Predsjednica Evropske centralne banke Christine Lagarde izjavila je '
          'da njen najveći strah nije da će Evropska...'}
```

#### deduplicated_bxr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6751,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:RELUZWSMYT63FAPLHP55SMNNCSXIQEDX',
                         'warc-date': '2021-02-26T07:18:33Z',
                         'warc-identified-content-language': 'mon,rus',
                         'warc-record-id': '<urn:uuid:efe8d9fa-4329-4479-aa56-43938e8e5370>',
                         'warc-refers-to': '<urn:uuid:bba3bfb2-b7c7-4605-9f49-34598eac9a5b>',
                         'warc-target-uri': 'http://soyol.ru/bur/yoho-zanshal/hoityn/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Хүнэй бэе мүнхэ бэшэ. Һүнэһэнэй бэеымнай орхижо, түрэлөө '
          'урилхадань, тэрэнэй хальһан боложо ябаһан бэемнай үхэнэ, газ...'}
```

#### deduplicated_ca
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 30591,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DJYNCXSBI5JH4V3LKGE7YNQBL34E3W5G',
                         'warc-date': '2021-03-02T21:39:28Z',
                         'warc-identified-content-language': 'cat,eng',
                         'warc-record-id': '<urn:uuid:ec350f95-900b-4164-aab3-8a6451228d5b>',
                         'warc-refers-to': '<urn:uuid:4c8e31b8-3011-4a21-9591-39be0942e121>',
                         'warc-target-uri': 'https://ca.m.wikipedia.org/wiki/Regne_d%27Ayutthaya',
                         'warc-type': 'conversion'},
            'nb_sentences': 33,
            'offset': 0},
  'text': "El regne d'Ayutthaya va ser un estat a Tailàndia que va existir de "
          '1351 a 1767 governat per un rei. El rei Rāmadhipat...'}
```

#### deduplicated_cbk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 151273,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:JCULI5BTSXOFUJYKZPPLMU5BZEZJZEVJ',
                         'warc-date': '2021-03-04T21:00:26Z',
                         'warc-identified-content-language': 'ita',
                         'warc-record-id': '<urn:uuid:ca25bd6b-9a5f-41b5-8b0f-ad437a545cee>',
                         'warc-refers-to': '<urn:uuid:ac67c26c-c62a-4c3d-9bd9-dd66a78a474f>',
                         'warc-target-uri': 'https://it.readkong.com/page/note-di-un-anno-di-lavoro-plural-3281543',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '                      '
          'na                                                                                             '
          '...'}
```

#### deduplicated_ce
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5944,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:AXGWUWKZ5HO42LSEO32HWLT77MATHGXB',
                         'warc-date': '2021-03-03T14:41:28Z',
                         'warc-identified-content-language': 'eng',
                         'warc-record-id': '<urn:uuid:1333c910-7921-4bdd-9bb9-1a8322dfa74b>',
                         'warc-refers-to': '<urn:uuid:9e976ac2-74e4-4e30-8c49-12f2dc1c257c>',
                         'warc-target-uri': 'https://www.radiomarsho.com/a/27368811.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Апти Бисултанов вина 1959 шарахь. Апти -- гоьваьлла нохчийн '
          'кхузаманахьлера байтанча ву. 1983 шарахь цо чекхъяккхира ...'}
```

#### deduplicated_ceb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8799,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:GSVQUFRLD3BYXEG2ASAEVHR2IH4D7A2S',
                         'warc-date': '2021-03-09T04:28:21Z',
                         'warc-identified-content-language': 'ceb,eng',
                         'warc-record-id': '<urn:uuid:e53f5344-29f5-4e59-8dac-8fdc92d1758f>',
                         'warc-refers-to': '<urn:uuid:03c0e7e5-b84c-4205-80cc-c3fb3dc82406>',
                         'warc-target-uri': 'https://www.safesworld.com/ceb/safewell-17ef-small-combination-lock-digital-safe-box-with-electronic-combination.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': '17EF SERYE Talagsaong design ug madanihon nga kolor naghimo 17EF '
          'popular nga sa taliwala sa mga anak ug mga babaye, k...'}
```

#### deduplicated_ckb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8668,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XZOIJPSX5QTL5QQPQMXEVADFHZTXMP5I',
                         'warc-date': '2021-03-09T03:25:59Z',
                         'warc-identified-content-language': 'kur,eng',
                         'warc-record-id': '<urn:uuid:9fe2f7e9-c158-4b84-a4a3-24e51acbd69e>',
                         'warc-refers-to': '<urn:uuid:14902cc0-948b-4dcf-bde6-e687ba41212f>',
                         'warc-target-uri': 'https://www.dastihawkary.org/blog/portfolio/social-harms-of-drugs/?lang=en',
                         'warc-type': 'conversion'},
            'nb_sentences': 9,
            'offset': 0},
  'text': 'وەبیرم دێ\u200c لە كۆتایی هەشتاكانی سەدەی ڕابردوو دیاردەیەك هەبوو '
          'لەنێو گەنجە لادەرەكانی شاری هەولێر و سەرشەقام هەڵدەستان ...'}
```

#### deduplicated_cs
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17263,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:EJZ477E7PWMVVVM777MHB5DMDHVYEWK6',
                         'warc-date': '2021-03-05T11:28:42Z',
                         'warc-identified-content-language': 'ces',
                         'warc-record-id': '<urn:uuid:6fc03e7f-9768-4f26-89ce-84fa4732e3c0>',
                         'warc-refers-to': '<urn:uuid:d78128e5-f667-4461-9f0c-2263d75b74a1>',
                         'warc-target-uri': 'https://www.lidovky.cz/relax/dobra-chut/mak-a-svestky-vyzkousejte-makovec-podle-romana-pauluse.A150427_125913_dobra-chut_ape?recommendationId=00000000-0000-5000-8000-000000000000',
                         'warc-type': 'conversion'},
            'nb_sentences': 12,
            'offset': 0},
  'text': 'Porno motor vyhledávání o nové sedlo masáž se svou. pro měkký sex '
          'voda učitelka kočička videa stránky Starý pár sex n...'}
```

#### deduplicated_cv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4133,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FKR5EKWIFACLGBIK6IKLHTHDNTEZNF3T',
                         'warc-date': '2021-03-03T14:25:27Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:8140dbf0-2fb0-48d8-a834-c1b052bcc72d>',
                         'warc-refers-to': '<urn:uuid:cca433fe-6646-4ab7-b5da-f8e17821b43d>',
                         'warc-target-uri': 'http://chuv-krarm.3dn.ru/blog/vladimir_leontev_savna_masharam_emer_perle_purnar_i/2013-02-08-47',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Сайт авторĕ тата модераторĕ- Михайлов Алексей, Чăваш Республикин '
          'Президенчĕн 2010,2012 çулсенчи стипендиачĕ, Сайт адм...'}
```

#### deduplicated_cy
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1967,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:RNFNJNY7RHGXN5NPEVF2PYNNIWOTDAMJ',
                         'warc-date': '2021-03-09T03:48:16Z',
                         'warc-identified-content-language': 'cym,eng',
                         'warc-record-id': '<urn:uuid:66f063ba-6a33-4f53-9cfb-7dc64a292e89>',
                         'warc-refers-to': '<urn:uuid:281f9c10-2d7d-4781-82f6-a504f27852a1>',
                         'warc-target-uri': 'https://cy.wikipedia.org/wiki/John_T._Koch',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Graddiodd o Brifysgol Harvard, gan gymeryd doethuriaeth mewn '
          'Ieithoedd a Llenyddiaethau Celtaidd yn 1985. Bu hefyd yn...'}
```

#### deduplicated_da
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 22154,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:AF2FFBNZQ3TOEEZ3MFDU77CXZ6PVU3ZB',
                         'warc-date': '2021-03-01T12:49:13Z',
                         'warc-identified-content-language': 'dan',
                         'warc-record-id': '<urn:uuid:92fffabd-5d36-4539-b8eb-18a0f2554ddb>',
                         'warc-refers-to': '<urn:uuid:1970d6bb-474f-448b-a3e1-8a77c9a32cb6>',
                         'warc-target-uri': 'http://rosamundis.dk/thai-horsens-gode-parfumer-til-m%C3%A6nd/',
                         'warc-type': 'conversion'},
            'nb_sentences': 16,
            'offset': 0},
  'text': 'Mange praler af den sindsro, de har fundet i huler i det '
          'norske/forfaldne franske ferielejligheder etc., hvor de har ...'}
```

#### deduplicated_de
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 11180,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:LLCPCA3RGKMXLYUEA3OZ2KFEEBNEOPE2',
                         'warc-date': '2021-03-09T01:22:52Z',
                         'warc-identified-content-language': 'eng,deu',
                         'warc-record-id': '<urn:uuid:0128ab60-86c8-4dc2-b1cf-57950654ae38>',
                         'warc-refers-to': '<urn:uuid:ff27032b-b843-4ba3-b1e2-377793173071>',
                         'warc-target-uri': 'http://bioconcepts.de/views/search.php?term=231&listed=y',
                         'warc-type': 'conversion'},
            'nb_sentences': 16,
            'offset': 0},
  'text': 'Kreismeisterschaften bringen zahlreiche Sunderner Medaillengewinner '
          'und Titelträger - Tischtennis im Sauerland\n'
          'Am ver...'}
```

#### deduplicated_diq
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4196,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DTA56M722SM5BZLNADOCPXQGGT32J46O',
                         'warc-date': '2021-03-06T15:51:03Z',
                         'warc-identified-content-language': 'tur,srp,nno',
                         'warc-record-id': '<urn:uuid:b7dcd4a4-b130-4009-88d0-631ca51a7bcc>',
                         'warc-refers-to': '<urn:uuid:fe4e4ad7-3089-40d2-aa29-f675e3cea0dd>',
                         'warc-target-uri': 'https://diq.wikipedia.org/wiki/Z%C4%B1wan%C3%AA_Slawki',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Zıwanê Slawki, zıwano merdumanê Slawano. Zıwanê Slawki yew lızgeyê '
          'Zıwananê Hind u Ewropao. Keyeyê Zıwananê Slawki be...'}
```

#### deduplicated_dsb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 20663,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:WWZOAFJJLJ4OHG2PTVLCMP664OR26XCR',
                         'warc-date': '2021-02-27T22:03:14Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:239b7155-8f37-4889-bad8-5bdb0aaa83c2>',
                         'warc-refers-to': '<urn:uuid:2714b744-a080-4807-a29a-d8f99c80e49c>',
                         'warc-target-uri': 'https://dsb.m.wikipedia.org/wiki/P%C5%9Bed%C5%82oga:LocMap',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Mjaz tamnjejšej pśedłogu a </noinclude>-kodom mógu pśidatne '
          'kategorije a cuzorěcne wótkaze stojaś. Ewentualne pśikład...'}
```

#### deduplicated_dv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7923,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:ECFUNRNYICXFAZXP5TLM45DPGJX5AHOI',
                         'warc-date': '2021-02-24T19:53:40Z',
                         'warc-identified-content-language': 'div,eng',
                         'warc-record-id': '<urn:uuid:23e2557a-dacc-428c-99fc-e41d4ce2ed95>',
                         'warc-refers-to': '<urn:uuid:067b6719-0209-49df-8198-27b1954b61b4>',
                         'warc-target-uri': 'https://dhiislam.com/114288',
                         'warc-type': 'conversion'},
            'nb_sentences': 7,
            'offset': 0},
  'text': 'މީސްތަކުންގެ ފިކުރާއި ކުޅެލުމަށްޓަކައި މިޒަމާނުގެ ވަސީލަތްތަކުގެ '
          'ބޭނުން އެންމެ ރަނގަޅު ގޮތުގައި ހިފަމުންދޭ: ޝެއިޚް ފި...'}
```

#### deduplicated_el
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12604,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2LXNVVGR3C4G72RLJUJBKUWLZZJ53TPX',
                         'warc-date': '2021-03-03T11:34:34Z',
                         'warc-identified-content-language': 'ell,eng',
                         'warc-record-id': '<urn:uuid:d95ddbe8-2e54-4d61-a6af-227212090684>',
                         'warc-refers-to': '<urn:uuid:a0e15450-8455-4b2f-ad8f-3858873a538d>',
                         'warc-target-uri': 'https://www.androsportal.gr/category/topika/nea-syllogwn/',
                         'warc-type': 'conversion'},
            'nb_sentences': 18,
            'offset': 0},
  'text': 'Η ραδιοφωνική διαφήμιση χαρακτηρίζεται από αμεσότητα και οικειότητα '
          'λόγω της στενής σχέσης του μέσου με τους ακροατές...'}
```

#### deduplicated_eml
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 11710,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OM2W34UTSIJJHAEXEX42BYMZWBB7U3FS',
                         'warc-date': '2021-03-05T23:48:29Z',
                         'warc-identified-content-language': 'ita',
                         'warc-record-id': '<urn:uuid:26a267af-a6de-4e84-b945-411b78b4815a>',
                         'warc-refers-to': '<urn:uuid:656aaba2-ff1d-4d7c-915a-9a555533aa42>',
                         'warc-target-uri': 'https://eml.wikipedia.org/wiki/2_(n%C3%B9mer)',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': "Al 2 'l è al prim nùmer prim ed tùta la séri ch'a s cata in di "
          "nùmer naturèl e anc 'l ùnic ch'al sìa pèra:\n"
          "Insèm a 'l..."}
```

#### deduplicated_en
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 15201,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:EIQTEGOE4V5SDID2OLTO4PWWCTW3AD5H',
                         'warc-date': '2021-03-03T18:20:30Z',
                         'warc-identified-content-language': 'eng',
                         'warc-record-id': '<urn:uuid:7cec445b-76fe-4ce2-ab43-8a85de680c6f>',
                         'warc-refers-to': '<urn:uuid:1cf845b2-3015-4f01-abaf-262af4adeba5>',
                         'warc-target-uri': 'https://www.aqueencitysound.com/2016/05',
                         'warc-type': 'conversion'},
            'nb_sentences': 28,
            'offset': 0},
  'text': 'But the term “extension” also means lengthening. EkhartYoga members '
          'can get to k… Renforcement du dos (muscles para-v...'}
```

#### deduplicated_eo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 27953,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:YO4NP6746IFQDF5KISEPLNFA2QD3PTEO',
                         'warc-date': '2021-03-09T05:29:46Z',
                         'warc-identified-content-language': 'epo,eng',
                         'warc-record-id': '<urn:uuid:5e3bc7b3-723f-4de9-8202-790351a2253f>',
                         'warc-refers-to': '<urn:uuid:dd5e537a-f340-4418-bc07-487232ea197c>',
                         'warc-target-uri': 'http://kantaro.ikso.net/cxu?image=kis_kut.png&ns=&tab_details=view&do=media',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Iloj Montri paĝonMalnovaj reviziojRetroligoj Freŝaj '
          'ŝanĝojMedio-administriloIndekso RegistriĝiEnsaluti'}
```

#### deduplicated_es
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8322,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DXIQKIWES4PP64BTGK5BYTJ3TX4RVQSI',
                         'warc-date': '2021-03-03T23:27:45Z',
                         'warc-identified-content-language': 'spa,eng',
                         'warc-record-id': '<urn:uuid:4275a14a-f997-4e58-8cf6-046006d76dab>',
                         'warc-refers-to': '<urn:uuid:d54d1a7b-1316-4bd1-8147-7a44ec5b3803>',
                         'warc-target-uri': 'https://www.rcrperu.com/defensoria-del-pueblo-oficina-en-lima-sur-registro-mas-de-3000-casos-durante-el-2020/',
                         'warc-type': 'conversion'},
            'nb_sentences': 7,
            'offset': 0},
  'text': 'Se prevé que a finales de mes haya llegado al 92,5 por ciento de '
          'los centros, aquellos en los que no hay confirmados ...'}
```

#### deduplicated_et
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 57234,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:JU7SWP3ZS36M3ABAEPNTFH37MVI2SLAF',
                         'warc-date': '2021-02-24T20:43:43Z',
                         'warc-identified-content-language': 'est',
                         'warc-record-id': '<urn:uuid:2bbcaa39-7336-4ade-accf-1b582785f731>',
                         'warc-refers-to': '<urn:uuid:849563c9-8549-4bdc-a09c-d179c8399ae0>',
                         'warc-target-uri': 'https://cardiaccareclinic.com/chto-luchshe-panangin-ili-kardiomagnil.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 129,
            'offset': 0},
  'text': 'Kas hirmu ei pruugi tekitada hoopis segadus? Näiteks võtame Ukraina '
          'kogemuse. Järsku ilmusid välja lindikestega mehed...'}
```

#### deduplicated_eu
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4248,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:STDEJOH35DPN5UB52OUZJJC4YCN7EH3N',
                         'warc-date': '2021-03-09T05:11:48Z',
                         'warc-identified-content-language': 'spa,eus',
                         'warc-record-id': '<urn:uuid:fb6752f7-5e91-4d0c-b022-71bd5d3ce910>',
                         'warc-refers-to': '<urn:uuid:faca7a42-20c2-4c4c-bd8a-6d4be5a1adb6>',
                         'warc-target-uri': 'http://intermedia.eus/la-comunicacion-imprescindible-lo-que-no-debemos-olvidar-de-2015-resumido-en-447/',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Nesken artean bokazio zientifikoak eta teknologikoak sustatzeko '
          'INSPIRA STEAM proiektua ia 120 ikastetxetako 5.000 ik...'}
```

#### deduplicated_fa
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 10411,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VM7Q7TXNMU2SRNHFJSZMBCKU2YVRKI56',
                         'warc-date': '2021-03-02T11:23:27Z',
                         'warc-identified-content-language': 'fas',
                         'warc-record-id': '<urn:uuid:9f666d03-9592-4f59-9111-981a558b3a32>',
                         'warc-refers-to': '<urn:uuid:8daf3dc1-92dd-4dbf-a339-992c99f09112>',
                         'warc-target-uri': 'https://zhycan.com/concough/blog/%D9%86%D8%AD%D9%88%D9%87-%D8%AB%D8%A8%D8%AA-%D9%86%D8%A7%D9%85-%DA%A9%D9%86%DA%A9%D9%88%D8%B1-%D8%AF%DA%A9%D8%AA%D8%B1%DB%8C-97-%D8%A7%D8%B9%D9%84%D8%A7%D9%85-%D8%B4%D8%AF-%D8%A7%D9%85/',
                         'warc-type': 'conversion'},
            'nb_sentences': 16,
            'offset': 0},
  'text': 'انجمن دانشجویان پیام نور تبليغات تماس با ما تبلیغات دسته بندی باز / '
          'بسته کردن دسته بندی ها . شرایط اختصاصی برای شغل د...'}
```

#### deduplicated_fi
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 19216,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:5OUEZDSL7KB2VHT2R67YZDER6UO5FHON',
                         'warc-date': '2021-03-05T00:14:23Z',
                         'warc-identified-content-language': 'fin,eng',
                         'warc-record-id': '<urn:uuid:61e0fc42-ceee-4026-ba76-3c8a8addd596>',
                         'warc-refers-to': '<urn:uuid:c4ba3c9f-5a6c-4de5-8f77-f5beb547315c>',
                         'warc-target-uri': 'https://kreditassms.eu/arvostelut-treffisivusto-py%C3%B6re%C3%A4-tanssi/',
                         'warc-type': 'conversion'},
            'nb_sentences': 46,
            'offset': 0},
  'text': 'Facebook ulkomaiset morsiamet fantasia lähellä lohja mistä pillua '
          'porno leffat sex treffit karvaiset tussut Thai mass...'}
```

#### deduplicated_fr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5274,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XUVXOZU2BIT4TIDEVHLLBLUIHRS4L7WV',
                         'warc-date': '2021-03-03T14:00:24Z',
                         'warc-identified-content-language': 'fra,eng',
                         'warc-record-id': '<urn:uuid:76252d00-9672-479c-9580-722614e078f9>',
                         'warc-refers-to': '<urn:uuid:4a6bde1e-9596-4388-9334-cc473a7c93ee>',
                         'warc-target-uri': 'https://www.cahier-des-charges.net/produit/modele-cahier-des-charges-de-logiciel-de-gestion-de-processus-metier/',
                         'warc-type': 'conversion'},
            'nb_sentences': 9,
            'offset': 0},
  'text': 'Créée en 1765 par le duc de Villars, alors gouverneur de Provence, '
          'l’École supérieure d’art d’Aix en Provence est un ...'}
```

#### deduplicated_frr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 27381,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DJE2KO4YWWRERKS5JYSK5JCJWYZ6DJHM',
                         'warc-date': '2021-03-01T03:40:10Z',
                         'warc-identified-content-language': 'ell',
                         'warc-record-id': '<urn:uuid:3a2a34ae-1c42-4d2e-bb08-8dabc916ea30>',
                         'warc-refers-to': '<urn:uuid:caeb39b2-da76-463d-b80c-4917d3dca230>',
                         'warc-target-uri': 'https://www.sedik.gr/neo/el/%CE%B1%CF%81%CF%87%CE%B5%CE%AF%CE%BF-%CE%B5%CE%BB%CE%B1%CE%B9%CE%BF%CE%BD%CE%AD%CF%89%CE%BD/%CE%B1%CF%81%CF%87%CE%B5%CE%AF%CE%BF-%CE%B5%CE%BB%CE%B1%CE%B9%CE%BF%CE%BD%CE%AD%CF%89%CE%BD-2009/178-178-title',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ '
          '’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’ ’...'}
```

#### deduplicated_fy
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1807,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:JABSHFJ2L6SQOXPPTBYGZGR24GCEDTTM',
                         'warc-date': '2021-03-09T04:24:30Z',
                         'warc-identified-content-language': 'fry',
                         'warc-record-id': '<urn:uuid:fd1b28cb-20ce-4082-b1ca-40045ed6af73>',
                         'warc-refers-to': '<urn:uuid:bc50e1f0-6384-4054-8916-2a489e9a0ffd>',
                         'warc-target-uri': 'https://www.omropfryslan.nl/nijs/201805-gruttere-lisboksstal-tastien',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Melkfeehâlders yn Súdwest-Fryslân kinne tenei makliker '
          "lisboksstâlen fergrutsje no't de gemeente de lanlike wet op st..."}
```

#### deduplicated_ga
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3296,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:WF6SCFDXN3NOT7FPKTEFOAMMPKXSEZ2W',
                         'warc-date': '2021-03-09T04:37:11Z',
                         'warc-identified-content-language': 'gle',
                         'warc-record-id': '<urn:uuid:bff39289-dbf7-444c-8df1-382fd46c993d>',
                         'warc-refers-to': '<urn:uuid:e27ba1c5-5707-4e9f-8ba8-f42c67bd9fc9>',
                         'warc-target-uri': 'http://nos.ie/cultur/iarratais-a-lorg-don-slam-filiochta-agus-duaischiste-700-ann-i-mbliana/',
                         'warc-type': 'conversion'},
            'nb_sentences': 6,
            'offset': 0},
  'text': 'Tá duaischiste £700 ar fáil do Slam Filíochta Liú Lúnasa a bheidh '
          'ar siúl ar líne ag deireadh na míosa seo chugainn. ...'}
```

#### deduplicated_gd
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7659,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OO363HOO6EDDYSBTTYB6H4WYAJBBMJ6D',
                         'warc-date': '2021-03-03T15:22:11Z',
                         'warc-identified-content-language': 'gla',
                         'warc-record-id': '<urn:uuid:e24cc86f-ae2c-49f6-b668-cda4f514a34d>',
                         'warc-refers-to': '<urn:uuid:1739d2d8-974d-4c29-b8d0-3a3ef9082537>',
                         'warc-target-uri': 'http://gd.cnswmc.com/ty320-3-bulldozer-product/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Tha inneal-brathaidh TY320-3 crochte leth-chruaidh, gluasad '
          'uisgeachaidh, inneal tarbh fo smachd seòrsa hydraulic. Ta...'}
```

#### deduplicated_gl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4202,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TIH7ARF4FNLH7VRGHXKOWVHNXNXC2HZX',
                         'warc-date': '2021-03-09T04:47:46Z',
                         'warc-identified-content-language': 'glg',
                         'warc-record-id': '<urn:uuid:983dd790-0846-4232-a7b4-3956af0982a8>',
                         'warc-refers-to': '<urn:uuid:b77207af-29d0-459f-9a55-0b25501d3e8b>',
                         'warc-target-uri': 'http://concellomuxia.com/item/outras-capelas/',
                         'warc-type': 'conversion'},
            'nb_sentences': 8,
            'offset': 0},
  'text': 'O templo actual é producto de diversas reconstrucións que se '
          'realizaron a finais do século XVII e principios do XVIII...'}
```

#### deduplicated_gn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3873,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FWN62CTWNJKPWUARS4BMBUFU6OVHL6XP',
                         'warc-date': '2021-02-27T22:49:49Z',
                         'warc-identified-content-language': 'grn,eng,bih',
                         'warc-record-id': '<urn:uuid:b4954ced-abe0-487e-b5b0-a26beb751a02>',
                         'warc-refers-to': '<urn:uuid:be5468f1-47f0-4bd8-a177-3529a14dead7>',
                         'warc-target-uri': 'https://gn.wikipedia.org/wiki/Apere%27arusu',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Ko ñe\'ẽ "apere\'arusu" ou avañe\'ẽ ñe\'ẽngue "apere\'a" he\'ise '
          'India Tapiti, ha avañe\'ẽ ñe\'ẽngue "rusu" he\'iséva iguasúva.'}
```

#### deduplicated_gom
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8747,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CKNSFAH2KISLLR7222FSQSPENYHQTAX3',
                         'warc-date': '2021-03-01T11:10:29Z',
                         'warc-identified-content-language': 'mar',
                         'warc-record-id': '<urn:uuid:d4622a3e-1b0e-4775-b25d-273ee14ae176>',
                         'warc-refers-to': '<urn:uuid:9d00e57b-9031-4f86-a9c8-cc3c0c2213a7>',
                         'warc-target-uri': 'https://gom.m.wikipedia.org/wiki/%E0%A4%B5%E0%A5%80%E0%A4%9C',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'कांय वस्तू रगडल्यो तर तांचेकडेन हलक्यो वस्तू आकर्शित जाता हेंजेन्ना '
          'पळयलें तेन्ना वीज हे ऊर्जेची कल्पना मनशाक आयली.हे...'}
```

#### deduplicated_gu
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 15036,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2FGV42SN72HRKRBEEQ7QJVJBLUYQPCIH',
                         'warc-date': '2021-03-09T04:48:08Z',
                         'warc-identified-content-language': 'eng,khm,lao',
                         'warc-record-id': '<urn:uuid:04d772d6-09db-4d5a-86c8-22b914a35b6f>',
                         'warc-refers-to': '<urn:uuid:f3cdcafa-5a28-4fbb-81df-7cc5e7bb3248>',
                         'warc-target-uri': 'http://www.ahealthyme.com/RelatedItems/RelatedDocuments.pg?d=&TypeId=121&ContentId=761&Category=DC',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ધ્યાન આપો: જો તમે ગુજરા તી બોલતા હો, તો તમને ભા ષા કીય સહાય તા સેવા '
          'ઓ વિ ના મૂલ્યે ઉપલબ્ધ છે. તમા રા આઈડી કાર ્ડ પર આ...'}
```

#### deduplicated_gv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 29707,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TIDW47D4MAHOLY6PQZ5SHLDYQIJ66REQ',
                         'warc-date': '2021-03-06T18:16:22Z',
                         'warc-identified-content-language': 'glv,eng',
                         'warc-record-id': '<urn:uuid:c7a5e531-487b-4e52-96ca-33b658691652>',
                         'warc-refers-to': '<urn:uuid:fa7285d4-126c-458f-9a72-d0d8615ce494>',
                         'warc-target-uri': 'https://gv.wikipedia.org/wiki/%C3%87hengoaylleeaght',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Ta çhengoaylleeaght feamagh eiyrt er sheiltynyssyn çhengoaylleeagh '
          'ayns ayrnyn myr ynsaghey çhengaghyn joaree, glare-...'}
```

#### deduplicated_he
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12254,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:BL56ZUXYO5GLIO6YTBUWKPVYJN2BKCIM',
                         'warc-date': '2021-03-09T10:29:09Z',
                         'warc-identified-content-language': 'heb,eng',
                         'warc-record-id': '<urn:uuid:1ae77825-a836-424e-a8b1-1f9c985a41b9>',
                         'warc-refers-to': '<urn:uuid:fce3d3dc-979e-4603-82e3-027b75346e52>',
                         'warc-target-uri': 'https://shop.makeup.land/collections/frontpage',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'הולדת פג היא אירוע מטלטל לכל משפחה, אך הולדת פג בצל מגפת הקורונה '
          'מאתגרת אף יותר? מהם האתגרים עמם מתמודדים ההורים והצו...'}
```

#### deduplicated_hi
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7897,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VZCN5HXN57VQHZJT5G3NWV7RCIT4GP7T',
                         'warc-date': '2021-02-26T10:18:11Z',
                         'warc-identified-content-language': 'hin,eng',
                         'warc-record-id': '<urn:uuid:6cccccb7-be0e-4c16-83be-7b4150b107ac>',
                         'warc-refers-to': '<urn:uuid:41eda5d1-e2cf-44f4-9f5b-c074a2de89da>',
                         'warc-target-uri': 'https://36.gurturgoth.com/2019/11/blog-post_8.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 5,
            'offset': 0},
  'text': 'Bill Gates Biography in Hindi, विश्व के सबसे अमीर इंसान और '
          'माइक्रोसॉफ्ट कंपनी के संस्थापक Bill Gates जिसने अपनी बुद्ध...'}
```

#### deduplicated_hr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 41545,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:6NTZEPK7ETF4AOLM3YDZRLRGZAKH7XM3',
                         'warc-date': '2021-03-09T04:58:04Z',
                         'warc-identified-content-language': 'hrv,bos,eng',
                         'warc-record-id': '<urn:uuid:32361cc9-e12a-4861-978a-b94b84efe78c>',
                         'warc-refers-to': '<urn:uuid:f0476e5f-e04c-4741-94a6-ddbcfb25c17e>',
                         'warc-target-uri': 'http://mjesec.ffzg.hr/webpac/?rm=results&show_full=1&f=PersonalName&v=Sanader%20Mirjana',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': 'Impresum: Pula : Sveučilište u Zagrebu, Međunarodno središte '
          'hrvatskih sveučilišta u Istri, Međunarodni istraživački ...'}
```

#### deduplicated_hsb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3352,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:E5ZCT5OIZBDV2EFBNX3MSLFJKKMZWQWI',
                         'warc-date': '2021-03-08T22:15:50Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:374a31b4-d38f-4d94-b3df-59013b15e644>',
                         'warc-refers-to': '<urn:uuid:fa9b7b26-2b4c-4acc-a652-47047617b0c0>',
                         'warc-target-uri': 'https://www.serbske-nowiny.de/index.php/hsb/z-luzicy/lokalka/item/50643-jednotna-proty-ka-tr-bna',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Žonjace akciske tydźenje zahajene\tDźensniši Mjezynarodny dźeń '
          'žonow je zazběh hač do 22. apryla trajacych ...\t\n'
          'Wotstr...'}
```

#### deduplicated_ht
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17823,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:LXQEYMTPIKHPAYKEKIZF6FCMC6WH66PW',
                         'warc-date': '2021-02-25T02:48:22Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:a5599306-82ad-4740-9c00-5bba34c96d54>',
                         'warc-refers-to': '<urn:uuid:2378d2f7-69a4-4f8a-ad03-4d556d031ebb>',
                         'warc-target-uri': 'http://mywebstores.ru/index.php?id_product=1841&controller=product',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'начать us $ nan us $ nan us $ nan us $ nan us $ nan us $ nan us $ '
          'nan us $ nan us $ nan us $ nan us $ nan us $ nan us...'}
```

#### deduplicated_hu
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 39801,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:B3XHZ4C4AJYQLVV3ESGOVZU6FZ5N5637',
                         'warc-date': '2021-02-26T07:03:18Z',
                         'warc-identified-content-language': 'hun',
                         'warc-record-id': '<urn:uuid:926ed467-3adb-44f5-b33c-63112879ba5a>',
                         'warc-refers-to': '<urn:uuid:9d9175b4-6b0a-45e8-961b-61e9d50eb684>',
                         'warc-target-uri': 'https://luminanz.eu/anya-hatartalan-ingyen-videok-pina-nagy-video-video-sex-szekx-hd-videa-nyelvu-%C3%B6reg/',
                         'warc-type': 'conversion'},
            'nb_sentences': 104,
            'offset': 0},
  'text': 'A WordPress egy ingyenesen letölthető rendszer. Letöltés után csak '
          'telepíteni kell a webszerverre és máris használhat...'}
```

#### deduplicated_hy
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6269,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:42PWBXN2Q7PFCRFWIDLTW42KUUGAKQOE',
                         'warc-date': '2021-02-24T23:49:31Z',
                         'warc-identified-content-language': 'hye,eng',
                         'warc-record-id': '<urn:uuid:932d1903-aea7-4be9-abb4-6b3114592c9c>',
                         'warc-refers-to': '<urn:uuid:cecf676f-884a-4311-a0b5-45ade0f517b7>',
                         'warc-target-uri': 'https://www.usanogh.am/lur/tramp-amn-coronavirus/',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': 'ՀՀ ԳԱԱ Զեկույցներ =Reports NAS RA կիրառում է «Ստեղծագործական '
          'համայնքներ» հեղինակային իրավունքի արտոնագիրը համաձայն որ...'}
```

#### deduplicated_ia
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9479,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:4JBN4SUDHHRPZI3TAVTZ4JUYSSOGGRFX',
                         'warc-date': '2021-03-01T17:14:58Z',
                         'warc-identified-content-language': 'ron,eng',
                         'warc-record-id': '<urn:uuid:5abe05ff-7309-4c3f-8ccd-175a12a655a2>',
                         'warc-refers-to': '<urn:uuid:8dec50fd-2be1-4bcf-8bb2-8cb9826c2465>',
                         'warc-target-uri': 'https://www.monitorulsv.ro/Ultima-ora-local/2008-02-18/Campania-electorala-interzisa-in-Primaria-Suceava',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha '
          'ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ...'}
```

#### deduplicated_id
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3080,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XU6GIUNYT5ELGH5XSZ4FUARC3YTJAD5P',
                         'warc-date': '2021-03-05T03:32:56Z',
                         'warc-identified-content-language': 'ind',
                         'warc-record-id': '<urn:uuid:2328da88-ee5f-4b4c-af3e-25dc4a574041>',
                         'warc-refers-to': '<urn:uuid:0781f7e2-f020-402b-b204-71fdf299f956>',
                         'warc-target-uri': 'https://sulsel.kemenag.go.id/berita/berita-kontributor/stqh-26-tingkat-kabupaten-jeneponto-siap-di-gelar',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': '* Masa berlaku normal poin 1 (satu) tahun dan masa berlaku bonus '
          'poin sampai dengan 31 Desember 2020.\n'
          'Diskon dari Ban...'}
```

#### deduplicated_ie
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 16919,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:W7UDGWMCEYQFEIPJMFZKX72Z6MH4XCUP',
                         'warc-date': '2021-03-08T16:16:42Z',
                         'warc-identified-content-language': 'ron,eng',
                         'warc-record-id': '<urn:uuid:f5ba5473-8eb2-41f4-9e43-3d36f14243a1>',
                         'warc-refers-to': '<urn:uuid:d2784efa-8250-4370-a348-28c640195663>',
                         'warc-target-uri': 'https://rolabel.info/door/yX-WpseZpNycfXY/luis-gabriel-haziran-te-am-cautat-si-te-am-gasit-official-video.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Va iubesc mult mult mult mult mult mult mult mult mult mult mult '
          'mult mult mult mult mult mult mult mult mult mult mu...'}
```

#### deduplicated_ilo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3511,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:NLHH2LVPZTUZE37ET2FJIRZNOLPLKK4O',
                         'warc-date': '2021-03-03T15:52:32Z',
                         'warc-identified-content-language': 'tgl',
                         'warc-record-id': '<urn:uuid:2fb6a437-41c8-4c2c-9f5d-2e8c34df9f2b>',
                         'warc-refers-to': '<urn:uuid:bdc072a0-db63-4256-a96b-7515a2c4fdfd>',
                         'warc-target-uri': 'https://ilo.m.wikipedia.org/wiki/Amphibia',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Daytoy nga artikulo dagiti nangruna nga artikulo ket pungol. '
          'Makatulongka iti Wikipedia babaen ti panagnayon iti daytoy.'}
```

#### deduplicated_io
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3586,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VUQPETM2PUWBL5AGADEVN2FPE7KURXG4',
                         'warc-date': '2021-03-03T15:22:41Z',
                         'warc-identified-content-language': 'ara',
                         'warc-record-id': '<urn:uuid:fd8a899b-d54a-424d-9955-a90b81e16439>',
                         'warc-refers-to': '<urn:uuid:c40226a6-6851-4009-a834-77a1a3e0c0f3>',
                         'warc-target-uri': 'https://io.wikipedia.org/wiki/New_Vienna,_Iowa',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': "Segun l'Usana Kontado Ministerio, l'urbo havas entote 1.2 km², "
          'equivalanta a 0.4 mi², di qui 1.2 km² (0.4 mi²) esas l...'}
```

#### deduplicated_is
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1829,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DXUGRT4OK7WRCOPGB7AAKLHPUDTBDRO2',
                         'warc-date': '2021-03-09T04:40:07Z',
                         'warc-identified-content-language': 'isl',
                         'warc-record-id': '<urn:uuid:6568bf31-b402-45b8-9ddb-6ce0f3d0a323>',
                         'warc-refers-to': '<urn:uuid:5daa12c0-604a-4233-9ed8-d4e245af4048>',
                         'warc-target-uri': 'http://hugvis.hi.is/',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Vegna hertra aðgerða í bará ttunni við Covid19 munum við takmarka '
          'gestafjölda í laugum okkar við 80 manns. Thank you ...'}
```

#### deduplicated_it
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 14112,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:MLJ4TW2HJZAPE2ORVARPJES6GRGO6ZLK',
                         'warc-date': '2021-03-05T13:56:32Z',
                         'warc-identified-content-language': 'ita',
                         'warc-record-id': '<urn:uuid:31d7ebb5-c1f7-468b-92f8-b79b7c28af9f>',
                         'warc-refers-to': '<urn:uuid:f92f33a2-6940-49fd-a21e-228ee5d2efb1>',
                         'warc-target-uri': 'https://mauriziomezzetti.com/patologie-trattate/',
                         'warc-type': 'conversion'},
            'nb_sentences': 47,
            'offset': 0},
  'text': 'Il Presidente del Caffè Letterario Quasimodo di Modica, Domenico '
          'Pisana, sarà ospite a Taranto, il prossimo 4 maggio,...'}
```

#### deduplicated_ja
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 16411,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XOFBBBX7LINQS3EZN5VH6OQ7PPFNRICJ',
                         'warc-date': '2021-03-09T01:09:27Z',
                         'warc-identified-content-language': 'jpn,eng,lat',
                         'warc-record-id': '<urn:uuid:5c0685f4-736d-4155-9153-56cf79462df4>',
                         'warc-refers-to': '<urn:uuid:88586e1b-926d-4291-910f-53680e3d6482>',
                         'warc-target-uri': 'http://flpj.karapyzi.ru/30',
                         'warc-type': 'conversion'},
            'nb_sentences': 14,
            'offset': 0},
  'text': '番組『日本を元気に！スマイルサプライズ！』が、28日に放送（後7：00）。コロナ禍や自然災害など、日本が長いトンネルに入ってしまったような状態だが、「でも、きっとこの先に明るい出口がある！」と明るい未...\n'
          'プリゲーム『ポケモンスマイ...'}
```

#### deduplicated_jbo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6970,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2EVVU2OCTSB5EYCHSV6Z7I3PMQSNNOED',
                         'warc-date': '2021-03-03T23:28:54Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:0d4387a2-391d-4e3e-8772-808face0ab78>',
                         'warc-refers-to': '<urn:uuid:4e45af2a-aea7-4f1a-af89-6ee5f69b7bfd>',
                         'warc-target-uri': 'https://jbo.m.wikipedia.org/wiki/mumyma%27i_7moi',
                         'warc-type': 'conversion'},
            'nb_sentences': 26,
            'offset': 0},
  'text': "ni'o 7 la mumast. cu 7moi djedi fi'o masti la mumast. noi ke'a cu "
          'mumoi masti .i 6 la mumast. cu purlamdei .ije 8 la ...'}
```

#### deduplicated_jv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8822,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:NPQGATEVIAYLOSLDB22EB7IYDVBZ7N6Q',
                         'warc-date': '2021-03-09T11:14:25Z',
                         'warc-identified-content-language': 'jav',
                         'warc-record-id': '<urn:uuid:db7d8bd7-a3a3-4a30-8786-7efb2352285d>',
                         'warc-refers-to': '<urn:uuid:2cb85a37-545e-471a-b7e7-cb334112f0e3>',
                         'warc-target-uri': 'https://jv.wikipedia.org/wiki/Bon%C3%A9kah',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Yèn sadurungé golèkan digawé kanggo awaké dhéwé, wiwit jaman iki '
          'dikomersialakaké. Fungsiné owah saka ritual lan mode...'}
```

#### deduplicated_ka
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 42480,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:HHSMTLZXKA4SQDPDBWAOUFELXBUJZJKO',
                         'warc-date': '2021-03-06T15:33:35Z',
                         'warc-identified-content-language': 'kat,eng',
                         'warc-record-id': '<urn:uuid:7d931f2a-a6ef-4070-9277-2033e7e96b9b>',
                         'warc-refers-to': '<urn:uuid:89429497-9722-45e6-95a6-699ef7280e6c>',
                         'warc-target-uri': 'https://ka.m.wikipedia.org/wiki/%E1%83%93%E1%83%90%E1%83%A1%E1%83%A2%E1%83%98%E1%83%9C_%E1%83%B0%E1%83%9D%E1%83%A4%E1%83%9B%E1%83%90%E1%83%9C%E1%83%98',
                         'warc-type': 'conversion'},
            'nb_sentences': 36,
            'offset': 0},
  'text': 'დასტინ ჰოფმანი[1] (ინგლ. Dustin Lee Hoffman დ. 8 აგვისტო, 1937) — '
          'ორგზის კინოაკადემიის ოსკარისა და ექვსგზის ოქროს გლო...'}
```

#### deduplicated_kk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9197,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:BJW4PLV2UOAJLJO6E55YH7DAEWQTFQUZ',
                         'warc-date': '2021-03-09T04:35:14Z',
                         'warc-identified-content-language': 'rus,kaz',
                         'warc-record-id': '<urn:uuid:ddd1d3e1-3bf3-4c4a-b722-8e293ab16f75>',
                         'warc-refers-to': '<urn:uuid:097c4f10-4bdc-400d-ab39-c04e4f98f51f>',
                         'warc-target-uri': 'http://blogs.kazakh.ru/blogs/index.php?page=group&gid=6&id=3&PAGEN_1=3%3Fid%3D2?id=6',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Бұрынғы жоғары лауазымды шенеунік Анатолий Шкарупа (сол жақта) '
          'өзіне қарсы қозғалған қылмыстық іс бойынша өтіп жатқан...'}
```

#### deduplicated_km
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 15036,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2FGV42SN72HRKRBEEQ7QJVJBLUYQPCIH',
                         'warc-date': '2021-03-09T04:48:08Z',
                         'warc-identified-content-language': 'eng,khm,lao',
                         'warc-record-id': '<urn:uuid:04d772d6-09db-4d5a-86c8-22b914a35b6f>',
                         'warc-refers-to': '<urn:uuid:f3cdcafa-5a28-4fbb-81df-7cc5e7bb3248>',
                         'warc-target-uri': 'http://www.ahealthyme.com/RelatedItems/RelatedDocuments.pg?d=&TypeId=121&ContentId=761&Category=DC',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ការជូនដំណឹង៖ ប្រសិនប. ើអ្នកនិយាយភាសា ខ្មែរ សេ វាជំនួយភាសាឥតគិតថ្លៃ '
          'គឺអាចរកបានសម្ រាប ់អ្នក។ សូមទូរស័ព្ទទ ៅផ ្នែ កសេ វ...'}
```

#### deduplicated_kn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8425,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TMWGSQVJMRPZCPMDM5D3AK2YKGMWBZZI',
                         'warc-date': '2021-03-09T04:21:39Z',
                         'warc-identified-content-language': 'kan,eng',
                         'warc-record-id': '<urn:uuid:ca35da96-ee3a-43ad-8082-a10b055200ca>',
                         'warc-refers-to': '<urn:uuid:a57cc8f6-c5ed-47a2-9322-2259687cdbde>',
                         'warc-target-uri': 'https://kannada.b4blaze.com/tag/rachitha-ram/',
                         'warc-type': 'conversion'},
            'nb_sentences': 16,
            'offset': 0},
  'text': 'ಅಡಿಗರು ಮತ್ತು ರಾಯರು ಚಾಪೆ ಹಾಸಿ ಸ್ವಲ್ಪ ಹೊತ್ತು ಮಲಗಿ ಕಾಫಿ ಕುಡಿದು '
          'ಹೊರಟುಹೋದಿದ್ದರು. ಜಾತ್ರೆ ದಿನ ಜಗನ್ನಾಥನ ಮನೆಗೆ ಬರಬಹುದಾದ ನೂರಾರು...'}
```

#### deduplicated_ko
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2831,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DLTUACNWU3R5KYI7HMMZF4CYR4WGRMWU',
                         'warc-date': '2021-02-26T10:13:10Z',
                         'warc-identified-content-language': 'kor,eng',
                         'warc-record-id': '<urn:uuid:7f7727bf-bf3d-45c3-8e3c-b595f67f9d90>',
                         'warc-refers-to': '<urn:uuid:17735508-d2ce-4e0a-a3ba-86acb749b9a2>',
                         'warc-target-uri': 'http://excel2017.zz.am/entry/mousqul',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': '인류는 최근 수백년 동안 물질적 풍요를 행복의 최대 조건으로 믿고, 이를 추구해 왔다. 그러나 이 과정에서 사람들은 '
          '상대방에게 사랑을 베풀기보다는 상처를 입히는 일이 많아졌고, 물질적 풍요는 내면의 충족을 동반...'}
```

#### deduplicated_krc
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4806,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CWWWGTU7JCHS7SR5A7D7QMDTF4JBMCA6',
                         'warc-date': '2021-02-26T04:08:10Z',
                         'warc-identified-content-language': 'nno,bih',
                         'warc-record-id': '<urn:uuid:ef2175c0-4887-4006-9b21-374282abf2d2>',
                         'warc-refers-to': '<urn:uuid:d5aaef09-6f3c-427a-8c2f-664e639c2a0f>',
                         'warc-target-uri': 'https://krc.wikipedia.org/wiki/1606_%D0%B4%D0%B6%D1%8B%D0%BB',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Бу, тамамланмагъан статьяды. Сиз болушургъа боллукъсуз проектге, '
          'тюзетиб эм информация къошуб бу статьягъа.'}
```

#### deduplicated_ku
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12767,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:BQQEDD5HKU6LXDRIDLMWPIESOMEGIUX6',
                         'warc-date': '2021-03-09T04:11:10Z',
                         'warc-identified-content-language': 'eng',
                         'warc-record-id': '<urn:uuid:5a67e5e4-f688-4aa1-a9a0-2e4f6217ef21>',
                         'warc-refers-to': '<urn:uuid:40fa61be-18d1-4bd5-9267-252720cd5b05>',
                         'warc-target-uri': 'http://www.peyamakurd.org/kurmanci/Kurdistan/gruben-smo-ye-bi-hawane-li-til-rifete-xistin-3-miri-u-6-birindar',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'PeyamaKurd – Grûbên bi ser Tirkiyê de li Binxetê li bajarokê Til '
          'Rifetê bi hawanê lê dan û di encamê de 3 kes mirin û...'}
```

#### deduplicated_kv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 14161,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:JH3R64H4VMXQ3NRHTX3LO3B4VFN6IZ62',
                         'warc-date': '2021-03-03T15:09:36Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:a94b390c-8e72-475d-bf76-c523c20908ce>',
                         'warc-refers-to': '<urn:uuid:e11eee46-e68f-4e1b-b4a3-0b9eeb74a877>',
                         'warc-target-uri': 'https://kv.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BA%D1%83%D1%88%D0%B5%D0%B2_%D0%90%D0%BD%D0%B0%D1%82%D0%BE%D0%BB%D0%B8%D0%B9_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D1%87',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '1947, моз тӧлысь–1950, кӧч тӧлысь – уджалiс велöдысьöн да '
          'директорöн Сыктывдiн районса Ыб шöр школаын.'}
```

#### deduplicated_kw
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3496,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:S5H4MWHD4QTG74ZNJZ5X63W2XSLUJU7C',
                         'warc-date': '2021-02-26T18:49:31Z',
                         'warc-identified-content-language': 'cym',
                         'warc-record-id': '<urn:uuid:44d32e62-4240-413a-9f8a-562fe27223c6>',
                         'warc-refers-to': '<urn:uuid:7d95741c-6974-427f-80f7-d08559f799aa>',
                         'warc-target-uri': 'https://kw.m.wikipedia.org/wiki/Kembra',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Kembra yw konna-tir menydhek yn Howlsedhes Breten Veur. Glow hag '
          'owr o poesek yn erbysieth Pow Kembra seulajydh, mes ...'}
```

#### deduplicated_ky
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 28946,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TVCYX44AC2J2TBVAYMQW62P4XYHWPSAH',
                         'warc-date': '2021-02-24T20:28:28Z',
                         'warc-identified-content-language': 'kir,eng',
                         'warc-record-id': '<urn:uuid:b0b897b8-5d55-4109-967f-9e368be6b7aa>',
                         'warc-refers-to': '<urn:uuid:b7ac5729-15cb-44c8-a0a2-096cb46cb1de>',
                         'warc-target-uri': 'http://mezgilnews.kg/tag/klip/',
                         'warc-type': 'conversion'},
            'nb_sentences': 6,
            'offset': 0},
  'text': 'Мезгил. Ырчы Зерени соцтармактар аркылуу коркуткан белгисиз '
          'адамдарды милиция издеп баштады. Чүй облустук ИИБинин маа...'}
```

#### deduplicated_la
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2647,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:QXPYMWAXXOOHWKBNAYCNUODKWSB56XU4',
                         'warc-date': '2021-03-09T04:51:12Z',
                         'warc-identified-content-language': 'lat,eng',
                         'warc-record-id': '<urn:uuid:684bcdce-19ec-4a44-b814-949eb5ceff66>',
                         'warc-refers-to': '<urn:uuid:2cd40ddd-0087-41ba-8442-8b2b6b1bbcd2>',
                         'warc-target-uri': 'http://grhpay.es/index.php/about-us/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Nam libero tempore, cum soluta nobis est eligendi optio cumque '
          'nihil impedit quo minus id quod maxime placeat facere ...'}
```

#### deduplicated_lb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2060,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:5YXISU3T3UP7WKUDJ2W45OAKEFJ7ZD2T',
                         'warc-date': '2021-03-09T04:51:26Z',
                         'warc-identified-content-language': 'ltz',
                         'warc-record-id': '<urn:uuid:534e6ce8-782c-4813-9dfb-902736ffc141>',
                         'warc-refers-to': '<urn:uuid:5829843c-0428-4098-9213-52bb2fb319b2>',
                         'warc-target-uri': 'https://online-archive-extractor.com/lb/open-7z-file',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': 'Eis Online Archiv Extraiteren erlaabt Iech den Inhalt vu '
          'kompriméierten Archiven direkt aus Ärem Browser ze extrahier...'}
```

#### deduplicated_lez
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6238,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:4MMTYN2QRKUOUZESCUL3AOZJTMDM5YSY',
                         'warc-date': '2021-03-02T18:06:44Z',
                         'warc-identified-content-language': 'nno,eng',
                         'warc-record-id': '<urn:uuid:78581b3a-c21f-46a2-b168-bff6f147c337>',
                         'warc-refers-to': '<urn:uuid:02f1447d-0b61-4ad5-ac56-0f42c2438e6b>',
                         'warc-target-uri': 'https://lez.wikipedia.org/wiki/1877_%D0%B9%D0%B8%D1%81',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '1877 йис (са агъзурни муьжуьдвишни пудкъанницIеирид лагьай йис) — '
          'григорийдин чIаваргандал гьалтайла ислендиз эгечӀза...'}
```

#### deduplicated_li
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2199,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:IIZSY6KLHN5WSCCGU4NZ6K6WYLIMJP4I',
                         'warc-date': '2021-03-04T07:19:27Z',
                         'warc-identified-content-language': 'nld',
                         'warc-record-id': '<urn:uuid:c7eb18bb-ea03-43c2-a1e9-e8eb5b15e25b>',
                         'warc-refers-to': '<urn:uuid:486a5d06-6dd8-46d2-a93f-d798b8a5bd07>',
                         'warc-target-uri': 'https://li.m.wikipedia.org/wiki/Waterop',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': "Hoes Karsveld aan de Gulp sjtamp oet de 18e ièw. 't Kesjtièlechtig "
          "hoes ies van mergel mèt 'ne trapgevel. 't Ies gebo..."}
```

#### deduplicated_lmo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6553,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DAJPSPBN7BVZNRWANXQAW2KP6LQEWNUW',
                         'warc-date': '2021-03-04T10:49:45Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:d9452b27-9a95-47e9-8274-518138812f56>',
                         'warc-refers-to': '<urn:uuid:4ff4e796-c685-4c81-adc9-fecbd50e79cb>',
                         'warc-target-uri': 'https://lmo.wikipedia.org/wiki/Antrenas',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': "El sò teretóre el g'ha 'na superfìce de 17,55 km² e 'l và de 'na "
          "altèsa mìnima de 720 méter a 'na altèsa màsima de 11..."}
```

#### deduplicated_lo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 15036,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2FGV42SN72HRKRBEEQ7QJVJBLUYQPCIH',
                         'warc-date': '2021-03-09T04:48:08Z',
                         'warc-identified-content-language': 'eng,khm,lao',
                         'warc-record-id': '<urn:uuid:04d772d6-09db-4d5a-86c8-22b914a35b6f>',
                         'warc-refers-to': '<urn:uuid:f3cdcafa-5a28-4fbb-81df-7cc5e7bb3248>',
                         'warc-target-uri': 'http://www.ahealthyme.com/RelatedItems/RelatedDocuments.pg?d=&TypeId=121&ContentId=761&Category=DC',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ຂໍ້ຄວນໃສ່ໃຈ: ຖ້າເຈົ້າເວົ້າພາສາລາວໄດ້, '
          'ມີການບໍລິການຊ່ວຍເຫຼືອດ້ານພາສາໃຫ້ທ່ານໂດຍບໍ່ເສຍຄ່າ. ໂທ ຫາ '
          'ຝ່າຍບໍລິການສະ ມາ ຊິກທີ່...'}
```

#### deduplicated_lrc
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7958,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:GTR6WCXERTVUI5RIKHE7MC7LTACF7R2W',
                         'warc-date': '2021-03-01T04:48:39Z',
                         'warc-identified-content-language': 'fas,eng',
                         'warc-record-id': '<urn:uuid:7ba618e0-f09e-48c2-a0be-a1b77ba5678a>',
                         'warc-refers-to': '<urn:uuid:2e4504e7-46c9-4aaa-818f-3077c73f1d97>',
                         'warc-target-uri': 'http://www.shaya.me/2013/01/blog-post_3.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'یار یار یار یار یار یار یار یار یار یار یار یار یار یار یار یار یار '
          'یار یار یار یار یار یار یار یار یار'}
```

#### deduplicated_lt
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 221005,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:KSLULK6RGSIW43IBMSAEU4643LSRMW3V',
                         'warc-date': '2021-03-05T07:21:10Z',
                         'warc-identified-content-language': 'lit',
                         'warc-record-id': '<urn:uuid:fa6592a5-bc87-4683-88d6-37ce74af5058>',
                         'warc-refers-to': '<urn:uuid:d78122b4-90d8-4cdf-a205-579bcff9ec88>',
                         'warc-target-uri': 'https://apcis.ktu.edu/lt/site/katalogas?cat_id=132&type=2',
                         'warc-type': 'conversion'},
            'nb_sentences': 219,
            'offset': 0},
  'text': 'Telšių apskritis – viena iš Lietuvos sričių, kuri turi ką parodyti '
          'pasauliui, ir iš to galima pasiekti didelės naudos...'}
```

#### deduplicated_lv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4036,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:NUB75CFJHUBI7HOED4HVCNHGQUIVCBO3',
                         'warc-date': '2021-03-09T03:46:31Z',
                         'warc-identified-content-language': 'lav,eng',
                         'warc-record-id': '<urn:uuid:9ad87feb-993f-45b9-bf1e-53a8185b3dc6>',
                         'warc-refers-to': '<urn:uuid:64eb85d8-c204-4cf8-a6c3-29760fe1f362>',
                         'warc-target-uri': 'http://igatesbaznica.lv/augupvrsta-stratijas-binr-opcijas.php',
                         'warc-type': 'conversion'},
            'nb_sentences': 10,
            'offset': 0},
  'text': 'Latvijā šobrīd nav normatīvu aktu mājas un istabas dzīvnieku '
          'vairotāju regulēšanai, jo vairākums audzētāju savu nodar...'}
```

#### deduplicated_mai
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3632,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OQRKDLTDWJCD37HVHGXYU7E3BXBR5NB3',
                         'warc-date': '2021-03-01T16:25:27Z',
                         'warc-identified-content-language': 'bih,hin,fra',
                         'warc-record-id': '<urn:uuid:da0cf739-4c6c-46d4-9c32-8e34a673fa26>',
                         'warc-refers-to': '<urn:uuid:0c39ca75-b871-431b-8c89-63d58ea0893f>',
                         'warc-target-uri': 'https://mai.m.wikipedia.org/wiki/%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%A7%E0%A4%BE%E0%A4%A8%E0%A5%80',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'शब्द राजधानी संस्कृत सँ आएल अछि । राजधानी आम तौर पर सङ्घटक क्षेत्रक '
          'सब सँ पैग सहर होएत अछि मुदा ई जरुरी नै अछि ।[१]'}
```

#### deduplicated_mg
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2714,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OGAHJNKN3OSLXYKJKK2LQAFKAEM67DFQ',
                         'warc-date': '2021-03-03T15:32:59Z',
                         'warc-identified-content-language': 'mlg,nno',
                         'warc-record-id': '<urn:uuid:f5a6492f-29c4-4de9-baaa-12edb86d89cd>',
                         'warc-refers-to': '<urn:uuid:970362fe-4102-481e-8f4b-db5f3e8ce4db>',
                         'warc-target-uri': 'https://mg.wikipedia.org/wiki/Barro_Alto_(Bahia)',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': "I Barro Alto (Bahia) dia kaominina ao Brazila, ao amin'i Bahia, ao "
          "amin'i Centro-Norte Baiano, Irecê.\n"
          'Ny velarantanin...'}
```

#### deduplicated_mhr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 27685,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:YJYVG5XEYRKALEYIO5PCK34QFNUO3JRD',
                         'warc-date': '2021-03-06T17:12:45Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:3405f528-672f-449c-a2a3-cfa73f5d17b0>',
                         'warc-refers-to': '<urn:uuid:dfe46be9-656c-4b02-9384-fd1e75987a15>',
                         'warc-target-uri': 'http://marisong.ru/mar/kalendar',
                         'warc-type': 'conversion'},
            'nb_sentences': 31,
            'offset': 0},
  'text': '1982 — 1985 ийлаште — Палантай лӱмеш музыкальный училищыште баян '
          'дене отделенийыште шинчымашым налын.\n'
          'Тыгак шуко жап ...'}
```

#### deduplicated_min
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4309,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XV23LOBECSVNRXJ2NJTCZVJXOCVQ3BBR',
                         'warc-date': '2021-03-08T22:10:36Z',
                         'warc-identified-content-language': 'eng,spa',
                         'warc-record-id': '<urn:uuid:fdaddf50-1986-44b3-b84b-d9a5d0fa27f1>',
                         'warc-refers-to': '<urn:uuid:257f7969-3a19-42d6-ae1a-ddb5c0486bb8>',
                         'warc-target-uri': 'https://cookingwithmydoctor.com/?LOSS=danger-of-keto-diet%2F',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f\u200e '
          '\u200e\u200f\u200f\u200e \u200e\u200f\u200f...'}
```

#### deduplicated_mk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 22483,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:SGEJ6O6XOEVCQXKXT2XRSRBOSH3ZDSVJ',
                         'warc-date': '2021-03-02T05:16:16Z',
                         'warc-identified-content-language': 'mkd,srp,eng',
                         'warc-record-id': '<urn:uuid:168d1661-a73f-4687-a614-e8cecf7a70a0>',
                         'warc-refers-to': '<urn:uuid:a61ec44e-a4c1-4b8e-837c-7adc80e853e2>',
                         'warc-target-uri': 'http://zenica.mk/2018/02/10/tri-dena-kultura-vo-karev-festival/',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': '„Три дена културa“ е настан кој ќе се одржи од 21-23 февруари '
          '(среда, четврток и петок, 20:00ч.) во гимназијата „Нико...'}
```

#### deduplicated_ml
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 20202,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:ZOEIO7AIEAGDR2S6TOZYZOAQDOV6QJUE',
                         'warc-date': '2021-03-08T00:10:05Z',
                         'warc-identified-content-language': 'mal,eng',
                         'warc-record-id': '<urn:uuid:f19a2925-0064-47e2-9ec9-48b2786657bd>',
                         'warc-refers-to': '<urn:uuid:20c7b8fd-1909-480f-b36c-89cd1d0ee3c4>',
                         'warc-target-uri': 'https://boolokam.com/what-to-do-for-police-clearance-conduct-certificate-in-uae/227247',
                         'warc-type': 'conversion'},
            'nb_sentences': 12,
            'offset': 0},
  'text': 'രണ്ടുപേര്\u200d തമ്മിലുള്ള സ്നേഹ ബന്ധം അവര്\u200dക്കിടയില്\u200d '
          'പൊതുവായി കാണപ്പെടുന്ന മൂല്യങ്ങളുടെ അടിസ്ഥാനത്തില്\u200d '
          'ആയിരിക്കും.\n'
          'ഒരുവ...'}
```

#### deduplicated_mn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5616,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:ILMC56UA63RNTABOJTVMUJQJHMKKC6QR',
                         'warc-date': '2021-03-09T04:20:37Z',
                         'warc-identified-content-language': 'mon,ell',
                         'warc-record-id': '<urn:uuid:07697b69-9e58-4e84-bc0e-a536bcc1ae11>',
                         'warc-refers-to': '<urn:uuid:704af2f1-3094-45dc-a1c5-63bd08d53069>',
                         'warc-target-uri': 'http://mn.uncyclopedia.info/index.php?title=%D0%A5%D1%8D%D1%80%D1%8D%D0%B3%D0%BB%D1%8D%D0%B3%D1%87:Mongol_Emperor&action=edit',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': 'Анциклопедиа-д оруулсан бүх хувь нэмэр Creative Commons '
          'Attribution-NonCommercial-ShareAlike-н хувьд (дэлгэрэнгүй мэд...'}
```

#### deduplicated_mr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 11373,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:V3PQES342QGJGRFZ6QMXNB6RIX2ST3V5',
                         'warc-date': '2021-03-09T05:01:31Z',
                         'warc-identified-content-language': 'mar,eng',
                         'warc-record-id': '<urn:uuid:b96cf6ee-7cda-4a7a-9364-08b51284a05e>',
                         'warc-refers-to': '<urn:uuid:92e533ed-c2c7-4ac7-9b17-af780a503ce6>',
                         'warc-target-uri': 'https://marathi.thewire.in/devangana-kalita-uapa-bail-rejected-natasha-narwal',
                         'warc-type': 'conversion'},
            'nb_sentences': 9,
            'offset': 0},
  'text': 'पुण्यातील कार्यक्रमांना स्थगिती:पुण्यातील अनेक सांस्कृतिक नियोजित '
          'कार्यक्रमांना स्थगिती, कोरोनाच्या वाढत्या रुग्णांमु...'}
```

#### deduplicated_mrj
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3492,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:7B242FKI45QVEGJQTF46YCRFYMYW6YFG',
                         'warc-date': '2021-03-03T05:03:02Z',
                         'warc-identified-content-language': 'eng',
                         'warc-record-id': '<urn:uuid:bd7d5682-be60-4a00-9781-29b03a87b30e>',
                         'warc-refers-to': '<urn:uuid:49641a15-2834-4a72-a011-fdc9cd7273c7>',
                         'warc-target-uri': 'https://mrj.wikipedia.org/wiki/%D0%91%D0%B0%D1%80%D0%BA%D0%B5%D1%80%D0%B8',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Баркери (латинлӓ Barkeria) – Орхидейвлӓ (Orchidaceae) йыхыш пырышы '
          'пеледшӹ кушкыш. Америкышты вӓшлиӓлтеш. Цилӓжӹ 15 й...'}
```

#### deduplicated_ms
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7939,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:7BWXR4LQ6O2IBJLKLKWJKHTF3JBXB26T',
                         'warc-date': '2021-03-09T05:38:44Z',
                         'warc-identified-content-language': 'msa,eng',
                         'warc-record-id': '<urn:uuid:35a9d91c-3a64-4748-b135-3c467bfa403f>',
                         'warc-refers-to': '<urn:uuid:9cf4de91-0523-4327-9fcb-5c8f99956da0>',
                         'warc-target-uri': 'https://kheru2006.livejournal.com/1665383.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Bagaimanapun beliau memiliki satu lagi pandangan iaitu perkara '
          'paling bodoh seseorang boleh lakukan ialah menjangka d...'}
```

#### deduplicated_mt
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 98714,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:HC75UY5ZHRC3AY4C2VHFR4JADUM2AZBH',
                         'warc-date': '2021-03-09T04:29:23Z',
                         'warc-identified-content-language': 'eng,mlt',
                         'warc-record-id': '<urn:uuid:45dec17d-a638-454e-a136-c45579517b53>',
                         'warc-refers-to': '<urn:uuid:c82d8d7c-05b6-43d8-be17-5072323aab01>',
                         'warc-target-uri': 'https://carmelcacopardo.wordpress.com/2015/07/28/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Kemmuna hi protetta bħala sit Natura 2000. Imma ma nistgħux '
          'neskludu logħob tas-soltu biex iduru ma din il-protezzjon...'}
```

#### deduplicated_mwl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 11598,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2A22BTIRZ4E5FI2FCG7AUCWJQTY2J4ST',
                         'warc-date': '2021-02-26T13:58:26Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:73a60756-1664-410f-bf62-ab44c88c074f>',
                         'warc-refers-to': '<urn:uuid:800d3642-449d-4be0-817c-edc7fb64c1b4>',
                         'warc-target-uri': 'https://mwl.wikipedia.org/wiki/R%C3%A1dio_(quemunica%C3%A7on)',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'La radioquemunicaçon ye un meio de quemunicaçon por trascepçon de '
          'anformaçon, podendo ser rializada por Radiaçon eile...'}
```

#### deduplicated_my
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 237288,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:U2QEC6RSZR5UW5LXTNN6QRD47FHVYVJY',
                         'warc-date': '2021-02-27T06:07:58Z',
                         'warc-identified-content-language': 'mya,eng',
                         'warc-record-id': '<urn:uuid:817de4f8-0b7a-446e-bae2-8436019dd34f>',
                         'warc-refers-to': '<urn:uuid:b364cc33-c1bf-4adb-8317-1aad1cfd4aa0>',
                         'warc-target-uri': 'http://www.pnsjapan.org/2010/05/',
                         'warc-type': 'conversion'},
            'nb_sentences': 248,
            'offset': 0},
  'text': 'စတိုင္လည္းက် စမတ္လည္းက်တဲ့ ေန႔စဥ္ လႈပ္ရွားမႈဘဝေလးေတြကို '
          'ပိုင္ဆိုင္ႏိုင္ဖို႔အတြက္ Samsung ကေန မၾကာေသးခင္က ထုတ္လုပ္လိုက...'}
```

#### deduplicated_myv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 11091,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:IFCGUVXSCYHEFYLUVOQ5QMGJWYL2CTVJ',
                         'warc-date': '2021-03-02T21:05:00Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:ea77b8a6-e394-48c1-b865-3cea87e7b906>',
                         'warc-refers-to': '<urn:uuid:a4927904-4e3c-4f22-858a-adad9bbb1e63>',
                         'warc-target-uri': 'https://ru.m.wikinews.org/wiki/%D0%9E%D0%BC%D0%B1%D0%BE%D0%BC%D0%B0%D1%81%D1%82%D0%BE%D1%80%D1%81%D0%BE_%C2%AB%D0%90%D0%B7%D0%BE%D1%80%C2%BB_%D1%8D%D1%80%D0%B7%D1%8F%D0%BD%D1%8C_%D1%8D%D1%80%D1%8F%D0%BC%D0%B0%D1%80%D1%82%D0%BE%D0%BD%D1%82%D1%8C_%D0%B2%D0%B0%D1%81%D0%B5%D0%BD%D1%86%D0%B5_%D0%BD%D0%B5%D0%B2%D1%82%D0%B5%D0%BC%D0%B0%D1%81%D1%8C_%D1%8E%D1%82%D1%8B_%D0%A1%D1%83%D0%BE%D0%BC%D0%B8%D1%81%D1%81%D1%8D',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '«Азор» — васенце эрзянь кельсэ артонь эриванмо-фильманть теемстэ. '
          'Орданьбуень Баеньбуе веле, Мордовиясо.'}
```

#### deduplicated_mzn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6193,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:QVLHP3APVA34EQ4YFDRJWF2ODTQZ3QG6',
                         'warc-date': '2021-03-08T00:11:58Z',
                         'warc-identified-content-language': 'fas',
                         'warc-record-id': '<urn:uuid:c86dfe2b-795d-4e5d-aaa0-75c1e98690a6>',
                         'warc-refers-to': '<urn:uuid:b6258701-626d-4a7c-b79e-1c526f9892a6>',
                         'warc-target-uri': 'https://mzn.wikipedia.org/wiki/%D8%A7%D9%88%D8%B3%D9%88%DA%A9%DB%8C%D8%8C_%D8%A7%D9%88%D8%A6%DB%8C%D8%AA%D8%A7',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'اوسوکی اتا شهر نوم هسته که جاپون ِاوئیتا استان دله دره. ونه جمعیت '
          'ره سال ۲۰۰۸ گادِر ۴۲٬۴۶۴ نفر اعلام هاکاردنه. این شه...'}
```

#### deduplicated_nah
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2517,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DSXC3C7F2LUL47USAV5ZRT4HMVQ4XGUI',
                         'warc-date': '2021-03-03T14:32:16Z',
                         'warc-identified-content-language': 'spa,ell',
                         'warc-record-id': '<urn:uuid:a305013e-01ba-49a3-89b9-027dc622576f>',
                         'warc-refers-to': '<urn:uuid:073b9e5a-a0d3-41c3-89bd-8f972b6a4154>',
                         'warc-target-uri': 'https://nah.wikipedia.org/wiki/%CF%98',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Ϙ ītōcā inic cē huēhuehtlahtōl īpan '
          'greciamachiyōtlahtōltecpantiliztli. Ītlahtōl nō ic 90 tlapōhualli.'}
```

#### deduplicated_nap
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2331,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:EXGUINJCGD2K4E2IVQNJJAQLS4UDJ2TG',
                         'warc-date': '2021-03-07T13:12:47Z',
                         'warc-identified-content-language': 'cos,srp,lav',
                         'warc-record-id': '<urn:uuid:7362689d-31bc-492d-8e60-851c963b5313>',
                         'warc-refers-to': '<urn:uuid:ecd1bb5f-d247-4739-b9e9-4f93d46081d6>',
                         'warc-target-uri': 'https://nap.wikipedia.org/wiki/Priatorio',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': "'Int'ô cattolicesimo, priatorio è 'o pruciesso 'e purefecazzione 'e "
          "ll'aneme ca moreno 'into ll'amicizzia 'e Dio ma n..."}
```

#### deduplicated_nds
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 5066,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:G2O2EJZLTIU5IDSXMYHPP3TMXVXMAZ3P',
                         'warc-date': '2021-03-08T22:13:48Z',
                         'warc-identified-content-language': 'nno,srp',
                         'warc-record-id': '<urn:uuid:d7f0c9a0-9c12-4d9a-ae5a-184bf7b59c5d>',
                         'warc-refers-to': '<urn:uuid:31f4d793-f3a4-4403-9c1f-a52f878b63c8>',
                         'warc-target-uri': 'https://nds.wikipedia.org/wiki/1763',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '7. Oktober: In London geiht en königliche Proklamatschoon rut, dat '
          'vun nu af an in de Kolonien vun Amerika de Kamm vu...'}
```

#### deduplicated_ne
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17723,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:AZ2CUDZ672TVV2R3O643TJAX7JGXASP2',
                         'warc-date': '2021-03-08T22:24:08Z',
                         'warc-identified-content-language': 'nep',
                         'warc-record-id': '<urn:uuid:fa642413-904a-4def-86fc-a4889e5e9e71>',
                         'warc-refers-to': '<urn:uuid:f7caed4f-c5ae-4f55-944a-1f06ed71e438>',
                         'warc-target-uri': 'https://postpati.com/2017/26/07/1353',
                         'warc-type': 'conversion'},
            'nb_sentences': 9,
            'offset': 0},
  'text': 'युएइको दूतावास बिरुद्द युएइमा रहेका संघ संस्थाहरु द्वारा निरन्तर '
          'दवाव आउने क्रमजारि रहेको छ। नेकपा माओबादी सम्बद्ध रह...'}
```

#### deduplicated_new
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2388,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:E6YZSKQK57PDBRG7VPE64CGOL3N4D63I',
                         'warc-date': '2021-03-09T04:24:48Z',
                         'warc-identified-content-language': 'nep,eng,bih',
                         'warc-record-id': '<urn:uuid:20692995-9d67-4b05-ba9b-9dbac80b4441>',
                         'warc-refers-to': '<urn:uuid:a8445a70-117a-42c1-89ca-aa5df0cc5616>',
                         'warc-target-uri': 'https://new.wikipedia.org/wiki/%E0%A4%A7%E0%A4%BE%E0%A4%AA%E0%A4%BE',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'धापा (अंग्रेजी भाय:Dhapa), नेपायागु कर्णाली अञ्चलयागु जुम्ला '
          'जिल्लायागु गाँ विकास समिति खः। थ्व थासे231खा छेँ दु।'}
```

#### deduplicated_nl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 766978,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:77YAXN3F4IGI2CYBM3IESJRTCIB4WY2F',
                         'warc-date': '2021-02-25T16:49:18Z',
                         'warc-identified-content-language': 'nld',
                         'warc-record-id': '<urn:uuid:0b08e51a-1b82-4fb9-a420-8556f2fb47a3>',
                         'warc-refers-to': '<urn:uuid:dae7ca23-9b7e-45d1-9a1c-604942af8cb9>',
                         'warc-target-uri': 'https://www.delpher.nl/nl/tijdschriften/view?identifier=MMUBA13:001691001:00689&coll=dts',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '1 Deze Duitse hond is nauw verwant aan de Duitse Brak, de '
          'Westfaalse Dasbrak werd gefokt om op dieren te jagen, zoals...'}
```

#### deduplicated_nn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2770,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FLRYPK225URFXO3IG4LP6D5TI2WW7MNU',
                         'warc-date': '2021-03-09T03:50:05Z',
                         'warc-identified-content-language': 'nno',
                         'warc-record-id': '<urn:uuid:de821d19-abed-4a35-9284-91176a5428b9>',
                         'warc-refers-to': '<urn:uuid:7ed9913e-e7dd-496f-b0ef-e82098dd53ca>',
                         'warc-target-uri': 'https://www.avisa-hordaland.no/trafikk/tunell-pa-e16-stengd-2/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Bilføraren som vart stogga på E16 i helga hadde 2,28 i promille: – '
          'Han var ikkje i stand til å ta vare på seg sjølv'}
```

#### deduplicated_no
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1329,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:G7JC2T5AD4YK4WWFGTYHHGP5VHB6M7KU',
                         'warc-date': '2021-03-08T13:17:52Z',
                         'warc-identified-content-language': 'nor',
                         'warc-record-id': '<urn:uuid:9e215de3-f988-4754-9ef5-6370121b9b5e>',
                         'warc-refers-to': '<urn:uuid:1facfcb5-da68-4122-9257-102271944050>',
                         'warc-target-uri': 'https://www.miljoindex.no/781825/nexans-norway-hovedkontor/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Utvikling, produksjon og markedsfÃ¸ring av kabler og '
          'kablingssystemer, samt annen tilknyttet virksomhet, herunder del...'}
```

#### deduplicated_oc
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 20117,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2XDHRCL2CSS7YFAM2IAGQL6CSJJEQDXI',
                         'warc-date': '2021-03-03T15:40:21Z',
                         'warc-identified-content-language': 'oci',
                         'warc-record-id': '<urn:uuid:c9ebdec5-af68-4756-88c8-1df831621c5b>',
                         'warc-refers-to': '<urn:uuid:199db451-0e6f-4f75-ad81-2e7612295452>',
                         'warc-target-uri': 'https://oc.wikipedia.org/wiki/2',
                         'warc-type': 'conversion'},
            'nb_sentences': 18,
            'offset': 0},
  'text': "8 : dins l'Empèri Part, assassinat dau rèi Orodes III, probablament "
          'en causa de son autoritarisme, que foguèt remplaç...'}
```

#### deduplicated_or
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12859,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:KQDIT6NHKBV43F56DTHTM5ZS3GHJT5SY',
                         'warc-date': '2021-03-09T05:25:21Z',
                         'warc-identified-content-language': 'ori,eng',
                         'warc-record-id': '<urn:uuid:e25e33da-92c5-42d6-aef8-c3465855312a>',
                         'warc-refers-to': '<urn:uuid:7457ac60-4aae-44ad-aaec-314795ea0708>',
                         'warc-target-uri': 'https://or.wikipedia.org/wiki/%E0%AC%A6%E0%AD%8D%E0%AD%B1%E0%AC%BF%E0%AC%A4%E0%AD%80%E0%AD%9F_%E0%AC%AC%E0%AC%BF%E0%AC%B6%E0%AD%8D%E0%AD%B1%E0%AC%AF%E0%AD%81%E0%AC%A6%E0%AD%8D%E0%AC%A7',
                         'warc-type': 'conversion'},
            'nb_sentences': 3,
            'offset': 0},
  'text': 'ଇଉରୋପ, ପ୍ରଶାନ୍ତ ମହାସାଗର, ଆଟଲାଣ୍ଟିକ ମହାସାଗର, ଦକ୍ଷିଣ-ପୂର୍ବ ଏସିଆ, ଚୀନ, '
          'ମଧ୍ୟପ୍ରାଚ୍ୟ, ଭୂମଧ୍ୟସାଗର, ଉତ୍ତର ଆଫ୍ରିକା, ପୂର୍ବ ଆଫ୍...'}
```

#### deduplicated_os
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7079,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:N7CKDF6E3SJBINW4SR6LIUNKLIJP2ROL',
                         'warc-date': '2021-03-08T22:01:32Z',
                         'warc-identified-content-language': 'nno',
                         'warc-record-id': '<urn:uuid:4cd86a68-815b-4539-84a8-bab850034e60>',
                         'warc-refers-to': '<urn:uuid:8774fb5e-b7fb-4feb-85e7-8c7b33f5980b>',
                         'warc-target-uri': 'https://os.wikipedia.org/wiki/%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD,_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9%D1%8B_%D1%84%D1%8B%D1%80%D1%82_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': 'Пушкин Александр Сергейы фырт (уырыс. Александр Сергеевич Пушкин; '
          'райгуырдис 1799 азы 6 июны Мæскуыйы — амардис 1837 ...'}
```

#### deduplicated_pa
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3990,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:HBYN5XY3CD2KI4XIWMBJYPSV2ZPNBWUN',
                         'warc-date': '2021-03-09T05:05:20Z',
                         'warc-identified-content-language': 'pan,eng',
                         'warc-record-id': '<urn:uuid:1ac5c8d1-e750-492e-b35e-b9780bfd16fd>',
                         'warc-refers-to': '<urn:uuid:b4d8f997-8c9a-43cf-b16c-e8a77c209062>',
                         'warc-target-uri': 'https://pa.nhp.gov.in/Detail/getdirection?url=radha-krishna-nurshing-andmat-home-rae_bareli-uttar_pradesh',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ਇਹ ਪੋਰਟਲ ਰਾਸ਼ਟਰੀ ਸਿਹਤ ਪੋਰਟਲ ਦੇ ਸਿਹਤ ਸੂਚਨਾ ਕੇਂਦਰ (CHI) ਦੁਆਰਾ ਵਿਕਸਿਤ '
          'ਤੇ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਸਿਹਤ ਤੇ ਪਰਿਵਾਰ ਭਲਾਈ ਮੰਤਰਾਲੇ...'}
```

#### deduplicated_pam
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4615,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:WOAFTI75LXN3LAF6WFDRDHITPU33CZRK',
                         'warc-date': '2021-03-07T22:02:39Z',
                         'warc-identified-content-language': 'eng',
                         'warc-record-id': '<urn:uuid:9d7a202a-0fec-4aac-9921-2ebf5aa7f9a2>',
                         'warc-refers-to': '<urn:uuid:70b6a707-77b1-4a0f-84e6-d75ed8d729ad>',
                         'warc-target-uri': 'https://toddlers.me/kpai-sarankan-gading-beri-penguatan-psikologi-untuk-gempi/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '“Káláu Gádìng tìdák mámpu melákukán ìtu, yá bìsá mìntá tolong '
          'kepádá oráng yáng berkompeten, mìsálnyá psìkolog átáu s...'}
```

#### deduplicated_pl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 51849,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:25YENUTK4YA3ZYGCWQH5Z6YDINCMI6SI',
                         'warc-date': '2021-03-05T22:43:01Z',
                         'warc-identified-content-language': 'pol',
                         'warc-record-id': '<urn:uuid:753116b6-f680-448d-ae8a-8fc88ce061b1>',
                         'warc-refers-to': '<urn:uuid:926693c4-5b59-4f50-98b9-787576fc71d7>',
                         'warc-target-uri': 'https://igraszki-jezykowe.pl/category/tips-and-tricks-metodyka/',
                         'warc-type': 'conversion'},
            'nb_sentences': 60,
            'offset': 0},
  'text': 'W niedzielę, 12 czerwca w Orlando na Florydzie islamski terrorysta, '
          'powiązany z ISIS zastrzelił 50 osób i drugie tyle...'}
```

#### deduplicated_pms
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2620,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2T5H5XDLC3KPDB33XXVCTGNNYYDJXQWQ',
                         'warc-date': '2021-03-03T16:04:55Z',
                         'warc-identified-content-language': 'srp',
                         'warc-record-id': '<urn:uuid:952c2dda-041e-40ff-bf28-8a39075f53d9>',
                         'warc-refers-to': '<urn:uuid:6d526022-b736-4a51-9b9c-c5bdd5a546f9>',
                         'warc-target-uri': 'https://pms.wikipedia.org/wiki/Auer',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': "Auer (Ora për j'italian) a l'é un comun ëd 3.025 abitant dla "
          'provincia ëd Bolsan (Region Autònoma Trentin-Sud Tiròl)....'}
```

#### deduplicated_pnb
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2896,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:GWWDSJAQDB7JDQWV65CI6WT7E6C33DL4',
                         'warc-date': '2021-03-08T23:01:08Z',
                         'warc-identified-content-language': 'urd',
                         'warc-record-id': '<urn:uuid:8c385ca8-7561-4f47-b5a3-0862488eb948>',
                         'warc-refers-to': '<urn:uuid:837d621d-3540-44fd-a4d0-6cb3c6f2327f>',
                         'warc-target-uri': 'https://pnb.wikipedia.org/wiki/453%DA%BE',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'لکھت کریئیٹیو کامنز انتساب/ اکوجہے-شراکت لائسنس دے ہیٹھ دستیاب اے، '
          'ہور شرطاں وی لاگو ہوسکدیاں نیں۔ ویروے لئی ورتن شرط...'}
```

#### deduplicated_ps
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2424,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CAUU5Y7TOTASV7WYKCYRCVXTZ7GGN2VO',
                         'warc-date': '2021-03-09T05:08:35Z',
                         'warc-identified-content-language': 'pus',
                         'warc-record-id': '<urn:uuid:d784cf7a-91e1-4c54-96a2-e41c67318548>',
                         'warc-refers-to': '<urn:uuid:98aed7d2-c3e3-4039-af83-f2c73a5c19f5>',
                         'warc-target-uri': 'https://www.mashaalradio.com/a/29821043.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'د افغانستان په فاریاب ولایت کې په یوه پارک کې ښځو په برقعو کې ورزش '
          'کړی دی. د سیمې چارواکي وايي، د ښځو د ورزش لپاره ځا...'}
```

#### deduplicated_pt
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 79931,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:JYDP4XMEGW2XPPV6NAAF772KDH4X2CCF',
                         'warc-date': '2021-02-25T13:48:41Z',
                         'warc-identified-content-language': 'por',
                         'warc-record-id': '<urn:uuid:3b50f546-e03b-461f-98c8-5a38920d7c0a>',
                         'warc-refers-to': '<urn:uuid:564bfb21-0705-4997-bbb9-472f0cbcad3e>',
                         'warc-target-uri': 'http://www.artefazparte.com/',
                         'warc-type': 'conversion'},
            'nb_sentences': 117,
            'offset': 0},
  'text': 'A reflexão sobre identidade de género anda a cansar muitos de nós. '
          'Sobretudo os que não têm dúvidas e nela se sentem ...'}
```

#### deduplicated_qu
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2630,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:34TX2UNXR2JLRLAFTE3ILOBMEBRMWIRH',
                         'warc-date': '2021-03-09T05:23:48Z',
                         'warc-identified-content-language': 'que',
                         'warc-record-id': '<urn:uuid:237398f6-a300-449b-9e09-7a1ed8cf1e97>',
                         'warc-refers-to': '<urn:uuid:84b20aab-d538-4efc-bc97-33d546d84802>',
                         'warc-target-uri': 'https://qu.wikipedia.org/wiki/Sapaq:HukchasqaTinkimuq/Chinchay_Chungcheong_pruwinsya',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': "Kay sapaq p'anqaqa t'inkisqa p'anqakunapi ñaqha hukchasqakunatam "
          "rikuchin. Watiqasqayki p'anqakunaqa yanasapa qillqas..."}
```

#### deduplicated_rm
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 100558,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:Z7R6QV2K5FDIHR4QJH7F2NTXND6NDEFY',
                         'warc-date': '2021-02-27T13:53:32Z',
                         'warc-identified-content-language': 'deu',
                         'warc-record-id': '<urn:uuid:da3aec28-6c61-470c-a5d2-66710bc1fb35>',
                         'warc-refers-to': '<urn:uuid:9d04f371-89a7-4ac2-9b1e-883aa93e4ace>',
                         'warc-target-uri': 'http://lexbrowser.provinz.bz.it/doc/la/lp-2009-5/lege_provinzialadi_28_de_set_mber_dl_2009_n_5.aspx?view=1',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '(2) La prestaziun dla garanzia é sotmetüda al’aprovaziun di decunć '
          'finanziars da pert dl’aministraziun dl consorz.'}
```

#### deduplicated_ro
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1677,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DXKBGKXVETQLCHTHRMLLSWUPXTDNJDVV',
                         'warc-date': '2021-02-26T12:19:49Z',
                         'warc-identified-content-language': 'ron',
                         'warc-record-id': '<urn:uuid:2c20c06f-ca98-4118-9222-7b3b74bc760b>',
                         'warc-refers-to': '<urn:uuid:e77c028a-5857-4ec2-90db-58a9bb57c510>',
                         'warc-target-uri': 'https://ro.visafoto.com/es-visa-photo',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Căluşarii sau Boristenii, melodie culeasă din Braşov, în 1832, de '
          'Canzler cav. de Ferio şi publicată târziu de Otto H...'}
```

#### deduplicated_ru
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 14025,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2HSXIFOHEJZOTJV2EVDSZDVF26ATVATE',
                         'warc-date': '2021-03-07T02:45:16Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:aa9b3fc9-fb66-45fa-a064-62ae5fd67970>',
                         'warc-refers-to': '<urn:uuid:e9145f1e-4ce5-44db-a7d7-234842b31973>',
                         'warc-target-uri': 'http://budzdorov-kaluga.ru/statyi_i_materialy/o-grippe',
                         'warc-type': 'conversion'},
            'nb_sentences': 15,
            'offset': 0},
  'text': '«Геро́й» (кит. 英雄) — исторический фильм режиссёра Чжана Имоу, '
          'снятый в 2002 году. Продолжительность — 93 минуты (суще...'}
```

#### deduplicated_rue
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17472,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:YBMO2PR3WF7WQ7UEU5YLRBI7BZ6IP6KB',
                         'warc-date': '2021-03-06T15:24:27Z',
                         'warc-identified-content-language': 'ukr,rus',
                         'warc-record-id': '<urn:uuid:ca71a8fe-adb9-4346-a5b4-7d283f1410f8>',
                         'warc-refers-to': '<urn:uuid:a609d9f9-5040-4ca5-80a8-aa2c4c7a3525>',
                         'warc-target-uri': 'https://rue.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BC%D1%96%D1%87:%D0%9A%D0%B0%D1%82%D0%B5%D2%91%D0%BE%D1%80%D1%96%D1%97',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Наприклад можете едітовати Катеґорія:Фізіци і додати одказ '
          '[[Катеґорія:Фізіка]]. Катеґорія Фізіци буде пікатеґоріёв к...'}
```

#### deduplicated_sa
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 4166,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:ACZ66HH67HYSPS6I7YYQX64HRD4O5GIH',
                         'warc-date': '2021-02-24T20:35:30Z',
                         'warc-identified-content-language': 'san,eng',
                         'warc-record-id': '<urn:uuid:12bc2393-cb9b-492d-9398-f6b1090bd999>',
                         'warc-refers-to': '<urn:uuid:6e883bd6-350e-4280-94dc-ee84f44d2458>',
                         'warc-target-uri': 'https://sa.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7%E0%A4%83:%E0%A4%95%E0%A4%BF%E0%A4%AE%E0%A4%A4%E0%A5%8D%E0%A4%B0_%E0%A4%B8%E0%A4%81%E0%A4%B2%E0%A5%8D%E0%A4%B2%E0%A4%97%E0%A5%8D%E0%A4%A8%E0%A4%AE%E0%A5%8D/%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%83:%E0%A5%A9%E0%A5%AC%E0%A5%A7',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'केभ्यः पृष्ठेभ्यः सम्बद्धम् पृष्ठम्: नामाकाशः : सर्वाणि (मुख्यम्) '
          'सम्भाषणम् सदस्यः सदस्यसम्भाषणम् विकिपीडिया विकिपीडि...'}
```

#### deduplicated_sah
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1724,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:5PKOMLENZCNOU6PT27NCNKTQFPRC37RQ',
                         'warc-date': '2021-03-03T15:19:03Z',
                         'warc-identified-content-language': 'ukr,rus',
                         'warc-record-id': '<urn:uuid:59b7bbeb-e375-4d8c-8b7c-fbe09e5ce21e>',
                         'warc-refers-to': '<urn:uuid:512d4df0-bd91-47aa-8f23-eb2a8d4b426e>',
                         'warc-target-uri': 'https://sah.m.wikipedia.org/wiki/%D0%A7%D0%B5%D1%80%D0%BD%D0%B8%D0%B3%D0%BE%D0%B2_%D1%83%D0%BE%D0%B1%D0%B0%D0%BB%D0%B0%D2%BB%D0%B0',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Тиэкис Creative Commons Attribution-ShareAlike лиссиэнсийэ '
          'усулуобуйатынан тарҕанар, сорох түбэлтэҕэ эбии көрдөбүллэр...'}
```

#### deduplicated_scn
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3622,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VGCXGU3B2WY722G2LRJ56RSYT4HSLUGI',
                         'warc-date': '2021-03-03T02:35:42Z',
                         'warc-identified-content-language': 'cos,ita',
                         'warc-record-id': '<urn:uuid:caeb7ba3-1bc2-4ef7-95cb-eb0d4d0792d6>',
                         'warc-refers-to': '<urn:uuid:19e33395-5981-4f6d-857b-12cf7d761b58>',
                         'warc-target-uri': 'https://scn.wikipedia.org/wiki/Canali_d%C3%A2_M%C3%A0nica',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Lu ripartu francisi dâ Mànica, chi cumprenni la pinìsula dû '
          'Cotentin, chi si nesci ntô canali, pigghia lu sò nomu dû ...'}
```

#### deduplicated_sco
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 140370,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TRXAEE4XHP7FT4FCJF3DSEKD7YBPCFOR',
                         'warc-date': '2021-03-02T07:33:12Z',
                         'warc-identified-content-language': 'eng,vol',
                         'warc-record-id': '<urn:uuid:d406a6c9-dba6-4955-8ede-f8082f7da58f>',
                         'warc-refers-to': '<urn:uuid:155919e0-a689-415c-b2aa-eccd06021476>',
                         'warc-target-uri': 'https://baggato.com/fo',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'fowjo fowjp fowjq fowjr fowka fowkb fowkc fowkd fowke fowkf fowkg '
          'fowkh fowki fowkj fowkk fowkl fowkm fowkn fowko fow...'}
```

#### deduplicated_sd
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17619,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DLWVP7WGNP64RB6ZLHDNQEJ7D24BYXOR',
                         'warc-date': '2021-02-24T20:04:37Z',
                         'warc-identified-content-language': 'snd,eng',
                         'warc-record-id': '<urn:uuid:8997e1c6-4d72-47f1-bffe-d18a00ae6b94>',
                         'warc-refers-to': '<urn:uuid:946e892e-46c3-4a68-8532-1eac8b65b76a>',
                         'warc-target-uri': 'https://sd.info-4all.ru/%D8%B1%D8%AA%D9%88%D9%BD%D9%88-%D8%A2%D8%A6%D9%8A%D8%B1%D8%B1%D8%A7/%DA%AA%D9%84%D8%A7%DA%AA/',
                         'warc-type': 'conversion'},
            'nb_sentences': 21,
            'offset': 0},
  'text': 'بيلففيل ڪيئن ٿيو؟ پهرين توهان کي پنهنجو ضمير وڃائڻ جي ضرورت آهي. '
          'اهي تعليم کان سواءِ صرف سست ماڻهو نه وٺندا آهن ، پر ...'}
```

#### deduplicated_sh
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 12517,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:IH6O64JAV4PLXURRD5LKU6C46DGGXS27',
                         'warc-date': '2021-03-09T06:06:53Z',
                         'warc-identified-content-language': 'fra,hrv,eng',
                         'warc-record-id': '<urn:uuid:ddc0f982-aea2-4206-a431-02e6c89ab090>',
                         'warc-refers-to': '<urn:uuid:904a206d-515a-4f11-ad25-9035adbf0cfa>',
                         'warc-target-uri': 'https://sh.wikipedia.org/wiki/Cliponville',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Po podacima iz 1999. godine u opštini je živelo 245 stanovnika, a '
          'gustina naseljenosti je iznosila 33 stanovnika/km²....'}
```

#### deduplicated_si
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 18426,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CZO426HASJ2VV5IMXEAHY2T53ZTDOZEP',
                         'warc-date': '2021-02-24T20:38:23Z',
                         'warc-identified-content-language': 'sin,eng',
                         'warc-record-id': '<urn:uuid:bec8b1fe-0659-4f47-b244-018b5dac9e30>',
                         'warc-refers-to': '<urn:uuid:1c918e04-8c2d-4bc0-bcfb-bf978ab0c0ea>',
                         'warc-target-uri': 'https://androidwedakarayo.com/before-you-look-for-a-job-please-fix-your-facebook-account/',
                         'warc-type': 'conversion'},
            'nb_sentences': 19,
            'offset': 0},
  'text': 'ඉස්සර තමයි අපි සෝෂල්මීඩියා පාවිච්චි කරන්නේ අපි ආස නළු නිළියන්ගේ '
          'ෆොටෝ, හදපු කෑම, ඩ්\u200dරින්ක් එකක් දාන්න සෙට් වෙච්චි වෙලා...'}
```

#### deduplicated_sk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 37910,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:ODXVMZXR34B45NQTMJIKKK2VGBGRXKEA',
                         'warc-date': '2021-03-01T16:29:19Z',
                         'warc-identified-content-language': 'slk',
                         'warc-record-id': '<urn:uuid:6a22612f-9bbf-4f74-8cca-0457f069baa4>',
                         'warc-refers-to': '<urn:uuid:3981cb48-fadf-463f-9fc9-a6d717b9dc71>',
                         'warc-target-uri': 'http://www.tomsta.sk/',
                         'warc-type': 'conversion'},
            'nb_sentences': 56,
            'offset': 0},
  'text': 'Keďže všade naokolo sú iba kopce, mohol byť jedine horský. Dnes je '
          'z toho najlepší horský triatlon na Slovensku, ktor...'}
```

#### deduplicated_sl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8130,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:UFZ4P4LVU4TXYJIHZULTCIVJ4GA3JT54',
                         'warc-date': '2021-03-07T14:50:23Z',
                         'warc-identified-content-language': 'slv,eng',
                         'warc-record-id': '<urn:uuid:e50a528d-ebd3-46dc-92d7-af394aaa896a>',
                         'warc-refers-to': '<urn:uuid:dbfe8ac4-b415-45a8-a16c-c168ed5ce37b>',
                         'warc-target-uri': 'https://www.edi-nm.com/si/varicosen-mnenja-cena-lekarna/',
                         'warc-type': 'conversion'},
            'nb_sentences': 6,
            'offset': 0},
  'text': 'Po najnovejših raziskavah v Sloveniji vsaka 4. oseba med 36. in 95. '
          'letom trpi zaradi kronične venske insuficience – ...'}
```

#### deduplicated_so
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 17837,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:WIS4GECYGJYMTZMVFOUVUMRWTAPFZUSK',
                         'warc-date': '2021-03-03T20:11:46Z',
                         'warc-identified-content-language': 'bul,eng,srp',
                         'warc-record-id': '<urn:uuid:976de977-97b9-4517-8a42-2fc82fdda461>',
                         'warc-refers-to': '<urn:uuid:a0f1fbd0-b2cb-495f-93f3-53e77acae3f5>',
                         'warc-target-uri': 'https://studioqueens.bgnick.info/l4fOorCpgdutsnY/igra-na.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'ххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххх...'}
```

#### deduplicated_sq
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6129,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:D3PWGEKLJKJEGOTQLYVQNUV4URWEFH2P',
                         'warc-date': '2021-03-09T03:17:23Z',
                         'warc-identified-content-language': 'sqi',
                         'warc-record-id': '<urn:uuid:3299bc56-c7fb-4655-bebd-393510d89aaa>',
                         'warc-refers-to': '<urn:uuid:1416a2ad-d319-4c60-b663-29239ff79154>',
                         'warc-target-uri': 'http://ata.gov.al/2019/11/03/video-u-prek-nga-termeti-ndertohet-nga-e-para-banesa-e-familjes-stafa-ne-petrele/',
                         'warc-type': 'conversion'},
            'nb_sentences': 11,
            'offset': 0},
  'text': 'TIRANË, 3 nëntor/ATSH/- Në Petrelë të Tiranës ka nisur puna për '
          'ndërtimin nga e para të shtëpisë së familjes Stafa, e...'}
```

#### deduplicated_sr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7735,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:7LKRS7R2L2K53YTV5CYR2IAJRNIQKGBJ',
                         'warc-date': '2021-03-03T11:23:25Z',
                         'warc-identified-content-language': 'srp,eng',
                         'warc-record-id': '<urn:uuid:8ade8406-bedb-41a7-b854-8429b6b21214>',
                         'warc-refers-to': '<urn:uuid:cca5c75c-7221-4247-a51e-f7be99661793>',
                         'warc-target-uri': 'https://vojvodjanske.rs/40-jubilarni-somborski-polumaraton-u-nedelju-19-maja/',
                         'warc-type': 'conversion'},
            'nb_sentences': 4,
            'offset': 0},
  'text': '„У недељу 19. маја, у Сомбору се одржава јубиларна 40. најстарија '
          'улична трка у Републици Србији, Сомборски полумарат...'}
```

#### deduplicated_su
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 14013,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:IMFFV646FPXSYLMOATX7O6CDMKUU4BFL',
                         'warc-date': '2021-03-09T10:29:19Z',
                         'warc-identified-content-language': 'sun,ind',
                         'warc-record-id': '<urn:uuid:02eb1f6f-7040-4b8f-b995-7c547196da4b>',
                         'warc-refers-to': '<urn:uuid:4a9807f7-0c98-493f-ab84-8fafc61a1e50>',
                         'warc-target-uri': 'https://www.masdinko.com/2019/04/soal-utspts-bahasa-sunda-sd-kelas-4.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Pikeun urang lembur, daun seureuh téh geus teu anéh deui. Seureuh '
          'mah mangrupa tangkal nu ngarémbét kana tangkal séjéna.'}
```

#### deduplicated_sv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 87099,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:TKLP6CG56M45ABZQGDD7EDTCQMKTSAVS',
                         'warc-date': '2021-03-05T20:01:45Z',
                         'warc-identified-content-language': 'swe',
                         'warc-record-id': '<urn:uuid:97860695-1688-46ef-93db-5e15742820af>',
                         'warc-refers-to': '<urn:uuid:7c924b0e-39e1-4921-a561-52dc5453b886>',
                         'warc-target-uri': 'https://fortretligheter.blogspot.com/2011/01/',
                         'warc-type': 'conversion'},
            'nb_sentences': 255,
            'offset': 0},
  'text': 'Svenska trupper hade en kväll för flera hundra år sedan när Sverige '
          'och Danmark låg i Krig med varandra kommit med sk...'}
```

#### deduplicated_sw
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 2098,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FPGJP34F47FJQSZF62PELBLYNJ4RTCSE',
                         'warc-date': '2021-03-03T15:24:39Z',
                         'warc-identified-content-language': 'swa',
                         'warc-record-id': '<urn:uuid:d42018de-64be-41f9-b4b6-700dd0051ce3>',
                         'warc-refers-to': '<urn:uuid:a40c8328-ab33-4113-9ea1-8c35967b0bde>',
                         'warc-target-uri': 'http://mwanza.go.tz/videos/78',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Mkuu wa Mkoa wa Mwanza Mhe.John Mongella akifungua Baraza la '
          'biashara katika kikao kilichofanyika kwenye ukumbi wa mk...'}
```

#### deduplicated_ta
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 49341,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FQEPDKJ7AYCAEVL5SRUQ5QOULOOSHECD',
                         'warc-date': '2021-03-09T04:15:52Z',
                         'warc-identified-content-language': 'tam',
                         'warc-record-id': '<urn:uuid:2fa70e6a-a31a-4359-b4ff-54ce7f5d6200>',
                         'warc-refers-to': '<urn:uuid:92eb01ff-4f82-438b-8d1f-1722fe23285a>',
                         'warc-target-uri': 'https://thiru2050.blogspot.com/2019_05_26_archive.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 15,
            'offset': 0},
  'text': '... 2017 adimmix psychic leah அறிவுரை கும்பம் மேஷம் ஜோதிடம் '
          'புற்றுநோய் மகர படிக குழந்தைகள் மனநோய் புத்தகங்கள் முன்அ...'}
```

#### deduplicated_te
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 31516,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:MG3MFYW5T6XSW3XYZ4ZIKGJW5XAY2RCG',
                         'warc-date': '2021-03-06T18:07:45Z',
                         'warc-identified-content-language': 'tel',
                         'warc-record-id': '<urn:uuid:238b108b-d16e-41d2-b06e-464267352b0e>',
                         'warc-refers-to': '<urn:uuid:3663318c-d256-4c97-b71b-e4eeb2e6b58a>',
                         'warc-target-uri': 'https://telugu.greatandhra.com/articles/mbs/ammo-ativa-01-114908.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 15,
            'offset': 0},
  'text': 'అది 1868. ఇంగ్లండ్\u200cలోని బ్రైటన్\u200cలో క్రిస్టియానా ఎడ్మండ్స్ '
          'అనే 40 ఏళ్ల మహిళ వుండేది. పెళ్లి కాలేదు. తల్లితో కలిసి ఒక ఎ...'}
```

#### deduplicated_tg
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 16112,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:LDBVTK3U6MY7J475ZR4LRLFK2CC2QWG5',
                         'warc-date': '2021-03-09T03:53:03Z',
                         'warc-identified-content-language': 'tgk,tat,rus',
                         'warc-record-id': '<urn:uuid:b2519476-6812-4a38-8522-f5292b95e73a>',
                         'warc-refers-to': '<urn:uuid:f11fa878-d4c6-4e56-bc50-a76554b7d811>',
                         'warc-target-uri': 'http://hamsafon.tj/2784-imr1263z-1203avoi-1207um1203ur1251-sofu-be1171ubor-meshavad.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 15,
            'offset': 0},
  'text': 'ДУШАНБЕ, 10.01.2017/АМИТ «Ховар»/. 10 январ дар пойтахти кишвар '
          'ҳавои тағйирёбандаи бебориш дар назар дошта шудааст. ...'}
```

#### deduplicated_th
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 50841,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:MESEMAONUQXZZEA6IKBT3VCUZ43ZP4B7',
                         'warc-date': '2021-02-28T15:41:47Z',
                         'warc-identified-content-language': 'tha,eng',
                         'warc-record-id': '<urn:uuid:46495e6b-f22f-4dc6-86ab-3bbed66ce7e4>',
                         'warc-refers-to': '<urn:uuid:10946c1b-9dc5-4afb-bc74-d6baf9793a03>',
                         'warc-target-uri': 'https://www.thaicsr.com/2009/02/blog-post_08.html',
                         'warc-type': 'conversion'},
            'nb_sentences': 34,
            'offset': 0},
  'text': 'ปี พ.ศ. 2521 '
          'พระบาทสมเด็จพระเจ้าอยู่หัวเสด็จเยี่ยมราษฎรบ้านพระบาทห้วยต้ม '
          'ทรงทอดพระเนตรเห็นสภาพพื้นที่และชีวิตความเป็น...'}
```

#### deduplicated_tk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 22486,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VNR5UQCQIGPEZQBZL4VAOQDASFOVNRDL',
                         'warc-date': '2021-03-03T15:07:09Z',
                         'warc-identified-content-language': 'eng,rus',
                         'warc-record-id': '<urn:uuid:b514b9c5-1ccd-4cf0-bea7-ea38a5aef686>',
                         'warc-refers-to': '<urn:uuid:edf1f6cb-9f46-4790-8256-eb984db0f0d5>',
                         'warc-target-uri': 'http://www.newscentralasia.net/2020/12/02/move-forward-with-universal-right-and-responsibility/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Türkmenistanyň Daşary işler ministriniň Owganystanyň Milli Yslam '
          'Hereketi partiýasynyň ýolbaşçysy bilen duşuşygy'}
```

#### deduplicated_tl
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 15036,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:2FGV42SN72HRKRBEEQ7QJVJBLUYQPCIH',
                         'warc-date': '2021-03-09T04:48:08Z',
                         'warc-identified-content-language': 'eng,khm,lao',
                         'warc-record-id': '<urn:uuid:04d772d6-09db-4d5a-86c8-22b914a35b6f>',
                         'warc-refers-to': '<urn:uuid:f3cdcafa-5a28-4fbb-81df-7cc5e7bb3248>',
                         'warc-target-uri': 'http://www.ahealthyme.com/RelatedItems/RelatedDocuments.pg?d=&TypeId=121&ContentId=761&Category=DC',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'PAUNAWA: Kung nagsasalita ka ng wikang Tagalog, mayroon kang '
          'magagamit na mga libreng serbisyo para sa tulong sa wika...'}
```

#### deduplicated_tr
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 14815,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:GVNKVEGK7TMZGXIIMLV2O2YWYJRAKBO2',
                         'warc-date': '2021-03-04T00:44:44Z',
                         'warc-identified-content-language': 'tur,eng',
                         'warc-record-id': '<urn:uuid:7acbe6a8-83c4-4ebd-8d29-62cb0b150b2f>',
                         'warc-refers-to': '<urn:uuid:038ffe28-2fd1-49b9-a5c6-3dddd1af6318>',
                         'warc-target-uri': 'https://www.kadikoygitarkursum.com/search/label/g%C3%B6ztepe%20gitar%20dersi',
                         'warc-type': 'conversion'},
            'nb_sentences': 5,
            'offset': 0},
  'text': 'İlk olarak, bir tek siyah kirpik takımı için fiyat belirleyin, '
          "örneğin, 4000 ruble'ye eşittir. Artık bir müşteriyle ç..."}
```

#### deduplicated_tt
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 26112,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FAPA2JNYP6OL53T6OIL3SR3EGMX2R4XY',
                         'warc-date': '2021-03-09T04:42:07Z',
                         'warc-identified-content-language': 'tat,rus',
                         'warc-record-id': '<urn:uuid:5cac6257-fa6c-4e67-9ba1-8e7d7424ef54>',
                         'warc-refers-to': '<urn:uuid:52642c8d-da35-462f-9776-ccfa88353466>',
                         'warc-target-uri': 'http://saby-rt.ru/news/konkurslar/fotokonkurs',
                         'warc-type': 'conversion'},
            'nb_sentences': 12,
            'offset': 0},
  'text': 'Хөрмәтле хатын-кызларбыз! Сезне чын күңелдән 8 Март бәйрәме белән '
          'тәбрик итәбез! Яраткан әниләребез, әбиләребез, гоме...'}
```

#### deduplicated_tyv
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7766,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:L5GRAANBGMGNYXDFF3ECSWJ5Q6D4QFHS',
                         'warc-date': '2021-02-28T07:20:44Z',
                         'warc-identified-content-language': 'rus',
                         'warc-record-id': '<urn:uuid:238082a9-0adf-4c8c-b749-1a523c91e229>',
                         'warc-refers-to': '<urn:uuid:4bfd0ca2-52bb-4ece-9ccf-cdcee0b30ee9>',
                         'warc-target-uri': 'https://tyv.wikipedia.org/wiki/%D0%A1%D0%B0%D1%80%D0%BB%D1%8B%D0%BA',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Сарлык бызаазы – ниити ады, назыны бир хар чедир, сарлыктың эр '
          'бызаазы аза сарлыктың кыс бызаазы деп чугаалаар.'}
```

#### deduplicated_ug
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 19089,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:DHYFNWWKECLR6BHWF763HC62JRCASMGH',
                         'warc-date': '2021-03-09T04:33:38Z',
                         'warc-identified-content-language': 'uig',
                         'warc-record-id': '<urn:uuid:d1185989-9cd6-40f2-ad63-003e405c9141>',
                         'warc-refers-to': '<urn:uuid:923ac168-6484-49ea-807d-be3ced85a885>',
                         'warc-target-uri': 'https://www.akademiye.org/ug/?p=10959',
                         'warc-type': 'conversion'},
            'nb_sentences': 30,
            'offset': 0},
  'text': 'شەرقىي تۈركىستانئاكادېمىيە ھەققىدەئەزالىقتەۋپىق '
          'مۇكاپاتىئىئانەئالاقەTürkçeEnglishئۇيغۇرچەУйғурчәUyghurche\n'
          'مىللىي مەۋج...'}
```

#### deduplicated_uk
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 16706,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:46XDNKJUJSG22BA4B6DDET2R5GMBU3LV',
                         'warc-date': '2021-02-26T22:04:41Z',
                         'warc-identified-content-language': 'ukr,eng',
                         'warc-record-id': '<urn:uuid:a3c68b5a-f9e8-41b6-b2bb-3d43e4d7a117>',
                         'warc-refers-to': '<urn:uuid:6a35e918-42ce-4349-9a6c-edcd22f07254>',
                         'warc-target-uri': 'https://www.interesniy.kiev.ua/vasil-boroday-korifey-mistetstva-pla/',
                         'warc-type': 'conversion'},
            'nb_sentences': 14,
            'offset': 0},
  'text': 'На Женевському міжнародному автосалоні 2017 бренд Fiat буде '
          'показувати дві свої душі, які співіснують у великій повні...'}
```

#### deduplicated_ur
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 9450,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:3SZ3UYOSHTRE3W3PDZXRO7DDSLRKENV2',
                         'warc-date': '2021-03-09T03:21:23Z',
                         'warc-identified-content-language': 'eng,urd,bos',
                         'warc-record-id': '<urn:uuid:0ded0cb4-2f73-41a7-a093-5dcfed204738>',
                         'warc-refers-to': '<urn:uuid:6b380ef1-fec4-4f48-bcdc-86700c508dfc>',
                         'warc-target-uri': 'http://www.khanaghar.org/?p=50',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'اتراکھنڈ کے سلماتا گاؤں کی لڑائیتی دیوی ایک پُر اعتماد اور عقلمند '
          'مجاہد ہیں، جن کی طرف دیگر خواتین بھی دیکھ رہی ہیں۔ ...'}
```

#### deduplicated_uz
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3808,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:FYYLFGJTK74HXE2LRJOAR5E6BPGCQ5NU',
                         'warc-date': '2021-03-09T04:38:24Z',
                         'warc-identified-content-language': 'uzb,ben,ltz',
                         'warc-record-id': '<urn:uuid:2a56bf64-042e-47fa-9abb-819b13bf7920>',
                         'warc-refers-to': '<urn:uuid:155b1e81-dc6e-46dc-9544-5a6a97c05118>',
                         'warc-target-uri': 'https://uz.wikipedia.org/wiki/1408',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Matn Creative Commons Attribution-ShareAlike litsenziyasi boʻyicha '
          'ommalashtirilmoqda, alohida holatlarda qoʻshimcha ...'}
```

#### deduplicated_vec
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7088,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CX2L4ZL4I4OLXG7YJTXLRKNFHE7RIHRX',
                         'warc-date': '2021-02-24T19:06:44Z',
                         'warc-identified-content-language': None,
                         'warc-record-id': '<urn:uuid:abc5a544-7009-407a-a5a3-5c2145195bd5>',
                         'warc-refers-to': '<urn:uuid:4a956690-536a-437b-afe2-50dc7ac54b39>',
                         'warc-target-uri': 'https://vec.wikipedia.org/wiki/Utensa:Aelwyn',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Łe parołe che vien dal łatin -TAS, TATIS łe termina par -DÁ. Łe '
          'parołe che łe vien da -ICUS łe tèrmina par -ÉGO. Łe p...'}
```

#### deduplicated_vi
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7845,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CCXAI5SV5PFLNPSMP4UF4SQGGSYN37AP',
                         'warc-date': '2021-03-03T02:43:13Z',
                         'warc-identified-content-language': 'vie',
                         'warc-record-id': '<urn:uuid:7ce27f30-a1eb-4978-83d0-5110421393b0>',
                         'warc-refers-to': '<urn:uuid:5dad988d-2426-402c-ac0c-1fa811ed96dc>',
                         'warc-target-uri': 'http://httlvinhphuoc.org/vi/duong-linh/Hoc-Kinh-Thanh-hang-ngay/Lam-Dieu-Thien-Bang-Tinh-Yeu-Thuong-6521/',
                         'warc-type': 'conversion'},
            'nb_sentences': 8,
            'offset': 0},
  'text': 'Bitcoin và tiền kỹ thuật số nói chung đang dần xâm nhập vào các '
          'thị trường tài chính khi ngày càng có nhiều nhà đ...'}
```

#### deduplicated_vls
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 78684,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VQNDJYOQXZLCLMDXIFCT4BHSW6LVTJQE',
                         'warc-date': '2021-02-28T16:16:27Z',
                         'warc-identified-content-language': 'fra,eng',
                         'warc-record-id': '<urn:uuid:266acc08-1c69-449f-95ad-0dcc82565788>',
                         'warc-refers-to': '<urn:uuid:c45dcd64-1b20-4ffc-bdd7-7dbff4f0a726>',
                         'warc-target-uri': 'https://fr.readkong.com/page/livret-des-licences-faculte-des-sciences-et-des-techniques-7906239',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '                                                                                                                     '
          '...'}
```

#### deduplicated_vo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 1937,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:VPG56ZACAOAZTXHSSXFJOBBH44NWUSJW',
                         'warc-date': '2021-03-09T06:02:56Z',
                         'warc-identified-content-language': 'vol,eng,srp',
                         'warc-record-id': '<urn:uuid:2cb96947-ee22-42a8-be36-31a03203efcc>',
                         'warc-refers-to': '<urn:uuid:da82b7d8-535b-4e39-8d9b-ea8c3d4a4460>',
                         'warc-target-uri': 'https://vo.wikipedia.org/wiki/Arnesano',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'Arnesano binon zif in topäd: Puglia, in Litaliyän. Arnesano topon '
          'videtü 40° 20’ N e lunetü 18° 6’ L.'}
```

#### deduplicated_wa
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 6518,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:6NC6V46TRVMWTOHCPMTDVRTP7GGL3G3S',
                         'warc-date': '2021-02-26T09:47:28Z',
                         'warc-identified-content-language': 'wol',
                         'warc-record-id': '<urn:uuid:4d800a25-ccf5-4d55-9795-3f7974b988b1>',
                         'warc-refers-to': '<urn:uuid:87119673-154b-4246-8c39-35737821a7ff>',
                         'warc-target-uri': 'https://wa.wikipedia.org/wiki/Senegal',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': "Cisse pådje ci n' est co k' on djermon, dj' ô bén k' el pådje est "
          "djusse sibåtcheye, eyet co trop tene; et s' divreut..."}
```

#### deduplicated_war
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7356,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:SVXPIA63QN77O2IJXL4Q75LNVLDEBHYW',
                         'warc-date': '2021-03-09T05:49:57Z',
                         'warc-identified-content-language': 'war,tha,eng',
                         'warc-record-id': '<urn:uuid:a143ebc6-a7b4-4fa7-96b3-59ba2c1dd03c>',
                         'warc-refers-to': '<urn:uuid:571d090a-cb65-41e7-ae7c-d95588d41c28>',
                         'warc-target-uri': 'https://war.wikipedia.org/wiki/Chakri_nga_Dinastiya',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'An Chakri nga Dinastiya (Thai: ราชวงศ์จักรี: Rajawongse Chakri) '
          'namuno ngan naghadi han Thailand tikang han hi hadi T...'}
```

#### deduplicated_wuu
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 26503,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:XAH2SJIYORGGSMLN4DNJZCNVG2FVWF3C',
                         'warc-date': '2021-03-09T04:09:05Z',
                         'warc-identified-content-language': 'jpn',
                         'warc-record-id': '<urn:uuid:8df3f922-fbbf-4733-a3a8-9f34b7505cbf>',
                         'warc-refers-to': '<urn:uuid:a55eb04e-3679-4817-b94b-e0317142ab2b>',
                         'warc-target-uri': 'https://wpedia.goo.ne.jp/wiki/%E4%BC%8A%E5%8D%81%E4%BA%94%E5%9E%8B%E6%BD%9C%E6%B0%B4%E8%89%A6',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': '伊15 [I] | 伊17 | 伊19 | 伊21 | 伊23 | 伊25 | 伊26 | 伊27 | 伊28 | 伊29 | 伊30 '
          '| 伊31 | 伊32 | 伊33 | 伊34 | 伊35 | 伊36 | 伊37 | 伊38 |...'}
```

#### deduplicated_xal
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 8598,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:KGZNUXNSFUSFYC45UQJRZPEHXNGK6C3H',
                         'warc-date': '2021-03-02T01:27:37Z',
                         'warc-identified-content-language': 'rus,spa',
                         'warc-record-id': '<urn:uuid:676f6ca8-706b-4f77-926f-bda90e3cd772>',
                         'warc-refers-to': '<urn:uuid:452efc2f-85ce-4e90-b268-2f46893172f8>',
                         'warc-target-uri': 'http://born.altnzam.com/2014/01/',
                         'warc-type': 'conversion'},
            'nb_sentences': 2,
            'offset': 0},
  'text': 'Ааһ: Хоосн ааһ би, хагсхларн һанцардсн болҗ медгдҗәнә. Нанд усн йир '
          'кергтә болҗана. Ус өгит, — эзнәсн сурна.\n'
          'Ааһ ууль...'}
```

#### deduplicated_xmf
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 7053,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:OQKCWDGQCIJHXMM3SCUO2KPBMFCQACUJ',
                         'warc-date': '2021-03-03T14:27:35Z',
                         'warc-identified-content-language': 'kat',
                         'warc-record-id': '<urn:uuid:e701a584-a14f-49ac-80b3-a7604f98fc92>',
                         'warc-refers-to': '<urn:uuid:8fc0f735-6e2b-45b2-bee1-bf169e08433b>',
                         'warc-target-uri': 'https://xmf.wikipedia.org/wiki/%E1%83%99%E1%83%90%E1%83%A2%E1%83%94%E1%83%92%E1%83%9D%E1%83%A0%E1%83%98%E1%83%90:%E1%83%90%E1%83%94%E1%83%A0%E1%83%9D%E1%83%9E%E1%83%9D%E1%83%A0%E1%83%A2%E1%83%94%E1%83%A4%E1%83%98_%E1%83%90%E1%83%9C%E1%83%91%E1%83%90%E1%83%9C%E1%83%98%E1%83%A8_%E1%83%9B%E1%83%94%E1%83%AF%E1%83%98%E1%83%9C%E1%83%90%E1%83%97',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'მოჩამილი ტექსტი წჷმორინელი რე Creative Commons '
          'Attribution-ShareAlike ლიცენზიათ; შილებე გეძინელი პირობეფიშ '
          'არსებუა. კ...'}
```

#### deduplicated_yi
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 10420,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:CZAVPSCGNW77WY2V2IJNK7R2CCUEMZFB',
                         'warc-date': '2021-02-24T21:10:52Z',
                         'warc-identified-content-language': 'yid,eng',
                         'warc-record-id': '<urn:uuid:7aa9e375-726d-42bd-832a-deee6dce5e4a>',
                         'warc-refers-to': '<urn:uuid:53354991-7bca-4134-95ce-ce7edebf841b>',
                         'warc-target-uri': 'http://www.kaveshtiebel.com/viewtopic.php?p=237817',
                         'warc-type': 'conversion'},
            'nb_sentences': 10,
            'offset': 0},
  'text': 'עמעזאן איז יעצט ארויסגעקומען מיט א נייע סמארט ספיקער סיסטעם. '
          "ס'הייסט Echo. אין Echo דרייט זיך א ראבאטישקע זי הייסט אל..."}
```

#### deduplicated_yo
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 3627,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:UISXP36HUEMW2LBTMAR4CTISUYAVZZAD',
                         'warc-date': '2021-03-07T12:45:52Z',
                         'warc-identified-content-language': 'yor,eng',
                         'warc-record-id': '<urn:uuid:e67645e9-ee6c-4c88-9b27-a158dc7f83e9>',
                         'warc-refers-to': '<urn:uuid:07c8d83b-7840-4238-a3b4-edc3f98ecdd5>',
                         'warc-target-uri': 'https://edeyorubarewa.com/itelorun/',
                         'warc-type': 'conversion'},
            'nb_sentences': 1,
            'offset': 0},
  'text': 'A dá sílè fún àwọn ènìyàn tí wọn fẹ́ràn láti mò nípa èdè Yorùbá, '
          'àṣà àti ìṣe ilẹ̀ kóòtù ojire. Kíkó àwọn ọmọ wa ni Èd...'}
```

#### deduplicated_zh
        
* Size of downloaded dataset files: None
* Size of the generated dataset: None
* Total amount of disk used: None

An example of 'train' looks as follows:
```
{ 'id': 0,
  'meta': { 'headers': { 'content-length': 108400,
                         'content-type': 'text/plain',
                         'warc-block-digest': 'sha1:PP6MQUJB3F4G63HKKGKO2QJG7SMRMTFJ',
                         'warc-date': '2021-02-28T09:41:11Z',
                         'warc-identified-content-language': 'zho',
                         'warc-record-id': '<urn:uuid:132aab53-daff-4bae-83d0-a0cdb4039d00>',
                         'warc-refers-to': '<urn:uuid:2f26c020-f1fc-4216-a616-4683e0b25b1e>',
                         'warc-target-uri': 'http://www.yummtumm.com/offer',
                         'warc-type': 'conversion'},
            'nb_sentences': 7,
            'offset': 0},
  'text': '久久精品视频在线看15_久久人人97超碰_久久爱 '
          '人人澡超碰碰中文字幕,人人天天夜夜日日狠狠,久久人人97超碰,人人婷婷开心情五月,日日摸天天摸人人看,碰人人么免费视频,色综合天天综合网 '
          '久久爱免费视频在线观看_久久爱视频_久久爱在线...'}
```

</details>

### Data Fields

* `id`: a `int64` feature.
* `meta`: Metadata
* `meta.headers`: WARC Headers
* `meta.headers.content-length`: `int64` Content length (in bytes) **before** cleaning
* `meta.headers.content-type`: `string` MIME type
* `meta.headers.warc-block-digest`:`string` Algorithm name and calculated value of a digest applied to the full block of the record
* `meta.headers.warc-date`: `string` Crawl date (YYYY-MM-DDThh:mm:ssZ)
* `meta.headers.warc-identified-content-language`: `string` Comma-separated list of language identifications done by CommonCrawl (uses CLD3)
* `meta.headers.warc-record-id`: `string` Record ID
* `meta.headers.warc-refers-to`: `string` Record-ID of a single record for which the present record holds additional content
* `meta.headers.warc-target-uri`: `string` URI from where the content has been fetched
* `meta.headers.warc-type`: `string` Type of the WARC Record
* `meta.nb_sentences`: `int64` Number of sentences in the text
* `meta.offset`: `int64` line offset where the related text begins. Should be used with `meta.nb_sentences` when reading the source files rather than using iterators to get related data.
* `text`: `string` content

See the [WARC Format standard](https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/#warc-type-mandatory) for more details.

### Data Splits


<details>
  <summary>Click to expand the number of samples per configuration</summary>

## Table

| Language code    | language                    | Size original | words original          | size deduplicated   | words deduplicated   |
|:----|:----------------------------|:-------|:----------------|:---------------|:----------------|
| af  | Afrikaans                   | 258MB  | 44,628,392      | 157MB          | 27,057,785      |
| als | Alemanic                    | 7MB    | 1,212,699       | 5MB            | 871,664         |
| am  | Amharic                     | 405MB  | 30,991,914      | 241MB          | 18,326,043      |
| an  | Aragonese                   | 1MB    | 115,938         | 608KB          | 89,043          |
| ar  | Arabic                      | 69GB   | 6,494,332,191   | 35GB           | 3,365,025,866   |
| arz | Egyptian Arabic             | 48MB   | 4,998,963       | 21MB           | 2,341,904       |
| ast | Asturian                    | 7MB    | 1,085,670       | 4MB            | 776,069         |
| as  | Assamese                    | 135MB  | 7,917,923       | 95MB           | 5,605,207       |
| av  | Avaric                      | 421KB  | 25,104          | 325KB          | 19,133          |
| azb | South Azerbaijani           | 47MB   | 3,595,569       | 29MB           | 2,243,562       |
| az  | Azerbaijani                 | 3GB    | 344,187,319     | 1GB            | 169,655,478     |
| bar | Bavarian                    | 2KB    | 247             | 1KB            | 245             |
| ba  | Bashkir                     | 110MB  | 8,121,603       | 77MB           | 5,625,158       |
| be  | Belarusian                  | 2GB    | 168,911,341     | 1GB            | 98,212,442      |
| bg  | Bulgarian                   | 34GB   | 2,994,775,106   | 15GB           | 1,315,091,995   |
| bh  | Bihari languages            | 579KB  | 46,436          | 120KB          | 9,181           |
| bn  | Bangla                      | 14GB   | 814,550,777     | 7GB            | 466,289,242     |
| bo  | Tibetan                     | 439MB  | 3,751,935       | 358MB          | 2,797,085       |
| bpy | Bishnupriya                 | 11MB   | 558,819         | 4MB            | 280,825         |
| br  | Breton                      | 49MB   | 8,067,480       | 23MB           | 4,032,467       |
| bs  | Bosnian                     | 310KB  | 50,266          | 175KB          | 25,157          |
| bxr | Russia Buriat               | 22KB   | 1,625           | 18KB           | 1,335           |
| ca  | Catalan                     | 13GB   | 2,110,833,307   | 6GB            | 1,012,770,904   |
| cbk | Chavacano                   | 168B   | 2               | 168B           | 2               |
| ceb | Cebuano                     | 81MB   | 12,921,589      | 58MB           | 9,201,870       |
| ce  | Chechen                     | 29MB   | 2,283,093       | 20MB           | 1,638,963       |
| ckb | Central Kurdish             | 784MB  | 63,417,572      | 367MB          | 29,355,017      |
| cs  | Czech                       | 72GB   | 9,996,052,434   | 33GB           | 4,739,928,730   |
| cv  | Chuvash                     | 60MB   | 4,592,449       | 41MB           | 3,141,872       |
| cy  | Welsh                       | 307MB  | 50,606,998      | 180MB          | 30,198,860      |
| da  | Danish                      | 18GB   | 2,892,004,180   | 10GB           | 1,704,605,898   |
| de  | German                      | 433GB  | 58,716,727,164  | 184GB          | 25,446,071,671  |
| diq | Dimli (individual language) | 294B   | 38              | 147B           | 19              |
| dsb | Lower Sorbian               | 31KB   | 4,115           | 14KB           | 1,873           |
| dv  | Divehi                      | 143MB  | 8,293,093       | 111MB          | 6,481,260       |
| el  | Greek                       | 72GB   | 6,024,414,850   | 30GB           | 2,539,719,195   |
| eml | Unknown language [eml]      | 22KB   | 4,360           | 20KB           | 3,876           |
| en  | English                     | 2936GB | 488,723,815,522 | 1342GB         | 223,669,114,922 |
| eo  | Esperanto                   | 560MB  | 84,432,772      | 390MB          | 59,411,208      |
| es  | Spanish                     | 342GB  | 54,715,337,438  | 160GB          | 25,877,724,186  |
| et  | Estonian                    | 7GB    | 954,732,803     | 3GB            | 455,553,053     |
| eu  | Basque                      | 900MB  | 110,676,692     | 503MB          | 62,812,888      |
| fa  | Persian                     | 79GB   | 8,566,653,720   | 35GB           | 3,902,206,854   |
| fi  | Finnish                     | 35GB   | 4,074,911,658   | 20GB           | 2,357,264,196   |
| frr | Northern Frisian            | 7KB    | 1,702           | 5KB            | 1,267           |
| fr  | French                      | 340GB  | 52,839,365,242  | 161GB          | 25,245,127,073  |
| fy  | Western Frisian             | 82MB   | 13,094,538      | 57MB           | 9,329,828       |
| ga  | Irish                       | 131MB  | 20,142,627      | 69MB           | 10,835,410      |
| gd  | Scottish Gaelic             | 2MB    | 332,946         | 1MB            | 173,588         |
| gl  | Galician                    | 989MB  | 155,030,216     | 549MB          | 87,015,417      |
| gn  | Guarani                     | 32KB   | 3,828           | 25KB           | 3,056           |
| gom | Goan Konkani                | 3MB    | 177,357         | 2MB            | 148,801         |
| gu  | Gujarati                    | 1GB    | 124,652,589     | 950MB          | 63,150,641      |
| gv  | Manx                        | 1KB    | 264             | 907B           | 141             |
| he  | Hebrew                      | 29GB   | 2,829,132,925   | 11GB           | 1,156,588,919   |
| hi  | Hindi                       | 26GB   | 2,009,754,819   | 13GB           | 1,038,914,735   |
| hr  | Croatian                    | 361MB  | 51,654,735      | 169MB          | 24,583,270      |
| hsb | Upper Sorbian               | 2MB    | 305,176         | 1MB            | 207,715         |
| ht  | Haitian Creole              | 2KB    | 592             | 1KB            | 351             |
| hu  | Hungarian                   | 60GB   | 7,415,936,687   | 29GB           | 3,765,883,306   |
| hy  | Armenian                    | 4GB    | 322,429,587     | 1GB            | 124,515,953     |
| ia  | Interlingua                 | 291KB  | 74,696          | 172KB          | 41,625          |
| id  | Indonesian                  | 40GB   | 5,767,715,387   | 22GB           | 3,126,926,138   |
| ie  | Interlingue                 | 7KB    | 1,432           | 2KB            | 424             |
| ilo | Iloko                       | 1MB    | 275,029         | 857KB          | 140,579         |
| io  | Ido                         | 276KB  | 46,463          | 221KB          | 36,976          |
| is  | Icelandic                   | 2GB    | 290,997,158     | 1GB            | 176,018,529     |
| it  | Italian                     | 192GB  | 29,252,541,808  | 94GB           | 14,426,829,908  |
| ja  | Japanese                    | 208GB  | 5,357,000,179   | 96GB           | 1,319,938,248   |
| jbo | Lojban                      | 929KB  | 179,684         | 731KB          | 140,749         |
| jv  | Javanese                    | 858KB  | 121,271         | 728KB          | 101,386         |
| ka  | Georgian                    | 6GB    | 304,329,117     | 2GB            | 116,422,468     |
| kk  | Kazakh                      | 3GB    | 236,767,203     | 1GB            | 126,886,720     |
| km  | Khmer                       | 1GB    | 28,188,612      | 860MB          | 13,408,408      |
| kn  | Kannada                     | 2GB    | 111,460,546     | 1GB            | 56,801,321      |
| ko  | Korean                      | 35GB   | 3,367,279,749   | 15GB           | 1,475,474,588   |
| krc | Karachay-Balkar             | 2MB    | 193,207         | 2MB            | 153,755         |
| ku  | Kurdish                     | 152MB  | 23,845,402      | 108MB          | 17,264,310      |
| kv  | Komi                        | 1MB    | 89,105          | 588KB          | 46,219          |
| kw  | Cornish                     | 119KB  | 20,775          | 72KB           | 12,687          |
| ky  | Kyrgyz                      | 485MB  | 33,401,287      | 334MB          | 23,102,129      |
| la  | Latin                       | 103MB  | 15,869,314      | 9MB            | 1,488,545       |
| lb  | Luxembourgish               | 54MB   | 7,953,887       | 37MB           | 5,454,220       |
| lez | Lezghian                    | 2MB    | 214,890         | 2MB            | 198,433         |
| li  | Limburgish                  | 76KB   | 12,105          | 54KB           | 8,472           |
| lmo | Lombard                     | 1MB    | 203,002         | 1MB            | 182,533         |
| lo  | Lao                         | 287MB  | 6,928,229       | 163MB          | 3,620,360       |
| lrc | Northern Luri               | 183B   | 26              | 183B           | 26              |
| lt  | Lithuanian                  | 12GB   | 1,573,926,673   | 5GB            | 701,326,575     |
| lv  | Latvian                     | 6GB    | 799,923,431     | 2GB            | 352,753,044     |
| mai | Maithili                    | 685KB  | 144,859         | 24KB           | 1,916           |
| mg  | Malagasy                    | 59MB   | 8,103,631       | 38MB           | 5,220,655       |
| mhr | Eastern Mari                | 15MB   | 1,170,650       | 10MB           | 784,071         |
| min | Minangkabau                 | 8MB    | 451,591         | 1MB            | 74,882          |
| mk  | Macedonian                  | 3GB    | 261,571,966     | 1GB            | 134,544,934     |
| ml  | Malayalam                   | 4GB    | 182,898,691     | 2GB            | 87,615,430      |
| mn  | Mongolian                   | 1GB    | 143,244,180     | 912MB          | 71,138,550      |
| mrj | Western Mari                | 645KB  | 51,812          | 521KB          | 41,950          |
| mr  | Marathi                     | 3GB    | 173,001,078     | 1GB            | 99,858,901      |
| ms  | Malay                       | 146MB  | 20,433,250      | 60MB           | 8,301,250       |
| mt  | Maltese                     | 51MB   | 6,162,888       | 26MB           | 3,179,815       |
| mwl | Mirandese                   | 3KB    | 419             | 2KB            | 302             |
| my  | Burmese                     | 2GB    | 54,624,239      | 1GB            | 35,969,724      |
| myv | Erzya                       | 29KB   | 2,844           | 2KB            | 236             |
| mzn | Mazanderani                 | 1MB    | 134,128         | 1MB            | 106,533         |
| nah | Nahuatl languages           | 34KB   | 3,664           | 21KB           | 2,363           |
| nap | Neapolitan                  | 1KB    | 550             | 1KB            | 235             |
| nds | Low German                  | 25MB   | 3,998,912       | 17MB           | 2,868,608       |
| ne  | Nepali                      | 3GB    | 207,891,824     | 2GB            | 142,087,100     |
| new | Newari                      | 6MB    | 433,880         | 4MB            | 254,711         |
| nl  | Dutch                       | 97GB   | 15,248,924,083  | 47GB           | 7,584,055,321   |
| nn  | Norwegian Nynorsk           | 123MB  | 20,629,675      | 66MB           | 11,095,804      |
| no  | Norwegian Bokmål            | 9GB    | 1,492,984,384   | 4GB            | 776,354,517     |
| oc  | Occitan                     | 12MB   | 1,822,595       | 5MB            | 834,187         |
| or  | Odia                        | 538MB  | 30,838,706      | 357MB          | 20,357,839      |
| os  | Ossetic                     | 11MB   | 911,794         | 6MB            | 536,525         |
| pam | Pampanga                    | 3KB    | 405             | 3KB            | 405             |
| pa  | Punjabi                     | 769MB  | 59,031,334      | 430MB          | 33,413,527      |
| pl  | Polish                      | 122GB  | 16,120,806,481  | 48GB           | 6,496,098,108   |
| pms | Piedmontese                 | 4MB    | 804,600         | 3MB            | 644,017         |
| pnb | Western Panjabi             | 68MB   | 7,757,785       | 45MB           | 5,221,168       |
| ps  | Pashto                      | 404MB  | 49,643,597      | 286MB          | 35,345,424      |
| pt  | Portuguese                  | 159GB  | 24,770,395,312  | 71GB           | 11,190,148,216  |
| qu  | Quechua                     | 322KB  | 40,691          | 230KB          | 29,108          |
| rm  | Romansh                     | 3KB    | 512             | 3KB            | 429             |
| ro  | Romanian                    | 37GB   | 5,629,438,576   | 15GB           | 2,387,230,734   |
| rue | Rusyn                       | 247B   | 14              | 247B           | 14              |
| ru  | Russian                     | 1201GB | 89,568,364,811  | 542GB          | 41,194,052,384  |
| sah | Sakha                       | 57MB   | 2,600,989       | 39MB           | 1,944,651       |
| sa  | Sanskrit                    | 72MB   | 3,288,786       | 43MB           | 1,998,089       |
| scn | Sicilian                    | 4KB    | 712             | 3KB            | 516             |
| sco | Scots                       | 1KB    | 523             | 1KB            | 282             |
| sd  | Sindhi                      | 75MB   | 8,937,427       | 50MB           | 6,064,102       |
| sh  | Serbian (Latin)             | 13MB   | 2,164,175       | 9MB            | 1,461,045       |
| si  | Sinhala                     | 1GB    | 91,456,436      | 791MB          | 47,770,919      |
| sk  | Slovak                      | 14GB   | 2,002,088,524   | 6GB            | 865,456,498     |
| sl  | Slovenian                   | 4GB    | 610,843,131     | 1GB            | 288,222,997     |
| so  | Somali                      | 15KB   | 849             | 13KB           | 449             |
| sq  | Albanian                    | 3GB    | 493,861,192     | 1GB            | 257,278,518     |
| sr  | Serbian                     | 6GB    | 574,460,746     | 3GB            | 289,211,579     |
| su  | Sundanese                   | 397KB  | 54,420          | 274KB          | 37,082          |
| sv  | Swedish                     | 43GB   | 6,542,433,732   | 19GB           | 2,964,887,952   |
| sw  | Swahili                     | 11MB   | 1,853,022       | 7MB            | 1,279,350       |
| ta  | Tamil                       | 10GB   | 438,489,984     | 5GB            | 215,856,584     |
| te  | Telugu                      | 3GB    | 182,268,133     | 1GB            | 73,193,605      |
| tg  | Tajik                       | 985MB  | 79,016,232      | 321MB          | 26,069,632      |
| th  | Thai                        | 62GB   | 1,694,658,532   | 26GB           | 635,230,676     |
| tk  | Turkmen                     | 25MB   | 2,693,720       | 20MB           | 2,221,760       |
| tl  | Filipino                    | 699MB  | 115,471,760     | 383MB          | 62,473,283      |
| tr  | Turkish                     | 73GB   | 8,763,467,387   | 33GB           | 3,950,989,357   |
| tt  | Tatar                       | 947MB  | 68,793,924      | 424MB          | 31,485,000      |
| tyv | Tuvinian                    | 9KB    | 638             | 7KB            | 542             |
| ug  | Uyghur                      | 187MB  | 12,786,741      | 123MB          | 8,410,269       |
| uk  | Ukrainian                   | 53GB   | 4,014,675,914   | 28GB           | 2,131,491,321   |
| ur  | Urdu                        | 2GB    | 354,937,986     | 1GB            | 234,111,239     |
| uz  | Uzbek                       | 56MB   | 6,237,371       | 28MB           | 3,327,595       |
| vec | Venetian                    | 37KB   | 6,694           | 28KB           | 5,139           |
| vi  | Vietnamese                  | 87GB   | 14,523,772,784  | 42GB           | 7,011,404,625   |
| vls | West Flemish                | 134B   | 2               | 134B           | 2               |
| vo  | Volapük                     | 2MB    | 426,052         | 2MB            | 410,688         |
| war | Waray                       | 4MB    | 750,162         | 4MB            | 702,336         |
| wa  | Walloon                     | 511KB  | 93,163          | 329KB          | 59,906          |
| wuu | Wu Chinese                  | 145KB  | 9,130           | 69KB           | 3,031           |
| xal | Kalmyk                      | 62KB   | 5,495           | 62KB           | 5,495           |
| xmf | Mingrelian                  | 16MB   | 807,158         | 10MB           | 510,700         |
| yi  | Yiddish                     | 199MB  | 18,699,112      | 93MB           | 8,716,366       |
| yo  | Yoruba                      | 229KB  | 34,468          | 120KB          | 17,487          |
| zh  | Chinese                     | 500GB  | 10,118,381,906  | 266GB          | 3,898,987,727   |



</details>

## Dataset Creation

### Curation Rationale

OSCAR was constructed using [`Ungoliant`](https://github.com/oscar-corpus/ungoliant), a new pipeline derived from [goclassy](https://github.com/oscar-corpus/goclassy), itself being derived from [fastText's one](https://github.com/facebookresearch/fastText).

OSCAR 21.09 follows the [OSCAR Schema v1.1](https://oscar-corpus.com/post/oscar-schema-v1-1/), which adds metadata to each entry while staying backwards-compatible with OSCAR.

The order of operations is similar as in the goclassy pipeline, with optimisations regarding IO and a finer granlularity regarding multithreading. 
`Ungoliant` is implemented in the [Rust programming language](https://rust-lang.org), and uses [rayon](https://github.com/rayon-rs/rayon) as its data parallelism strategy. 
Threading is done at shard, record and sentence level, making the whole generation process much more efficient.

Filtering is done at line-level, removing lines shorter than 100 UTF-8 codepoints. While invalid UTF-8 characters are detected, they are not removed, but rather replaced with the [Replacement character](https://en.wikipedia.org/wiki/Special_(Unicode_block)#Replacement_character).

After all files are proccesed the deduplicated versions are constructed and everything is then splitted in shards and compressed.

### Source Data

#### Initial Data Collection and Normalization

[Common Crawl](https://commoncrawl.org/) is a non-profit foundation which produces and maintains an open repository of web crawled data that is both accessible and analysable. Common Crawl's complete web archive consists of petabytes of data collected over 8 years of web crawling. The repository contains raw web page HTML data (WARC files), metdata extracts (WAT files) and plain text extracts (WET files). The organisation's crawlers has always respected [nofollow](http://microformats.org/wiki/rel-nofollow) and [robots.txt](https://www.robotstxt.org/) policies.

Each monthly Common Crawl snapshot is in itself a massive multilingual corpus, where every single file contains data coming from multiple web pages written in a large variety of languages and covering all possible types of topics.

To construct OSCAR the WET files of Common Crawl were used. These contain the extracted plain texts from the websites mostly converted to UTF-8, as well as headers containing the metatada of each crawled document. Each WET file comes compressed in gzip format and is stored on Amazon Web Services. In the case of OSCAR, the **February 2021** snapshot was used. It is composed by 64 000 compressed text files containing documents and their headers.

#### Who are the source language producers?

The data comes from multiple web pages in a large variety of languages.

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

N/A

#### Who are the annotators?

N/A

### Personal and Sensitive Information

Being constructed from Common Crawl, Personal and sensitive information might be present. This **must** be considered before training deep learning models with OSCAR, specially in the case of text-generation models.

## Considerations for Using the Data

### Social Impact of Dataset

OSCAR is intended to bring more data to a wide variety of lanuages, the aim of the corpus is to make large amounts of data available to lower resource languages in order to facilitate the pre-training of state-of-the-art language modeling architectures.

### Discussion of Biases

OSCAR is not properly filtered yet and this can be reflected on the models trained with it. Care is advised specially concerning biases of the resulting models.

### Other Known Limitations

The [fastText linear classifier](https://fasttext.cc) is limed both in performance and the variety of languages it can recognize, so the quality of some OSCAR sub-corpora might be lower than expected, specially for the lowest-resource langiuages. Some audits have already been done by [third parties](https://arxiv.org/abs/2010.14571).

## Additional Information

### Dataset Curators

The corpus was put together by [Julien Abadji](https://ujj.space), [Pedro Ortiz Suarez](https://portizs.eu/), [Benoît Sagot](http://pauillac.inria.fr/~sagot/), and [Laurent Romary](https://cv.archives-ouvertes.fr/laurentromary), during work done at [Inria](https://www.inria.fr/en), particularly at the [ALMAnaCH team](https://team.inria.fr/almanach/).

### Licensing Information

    These data are released under this licensing scheme
    We do not own any of the text from which these data has been extracted.
    We license the actual packaging of these data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
    To the extent possible under law, Inria has waived all copyright and related or neighboring rights to OSCAR
    This work is published from: France.

    Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
    * Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
    * Clearly identify the copyrighted work claimed to be infringed.
    * Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

    We will comply to legitimate requests by removing the affected sources from the next release of the corpus.

### Citation Information

```
@inproceedings{AbadjiOrtizSuarezRomaryetal.2021,
  author    = {Julien Abadji and Pedro Javier Ortiz Su{\'a}rez and Laurent Romary and Beno{\^i}t Sagot},
  title     = {Ungoliant: An optimized pipeline for the generation of a very large-scale multilingual web corpus},
  series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-9) 2021. Limerick, 12 July 2021 (Online-Event)},
  editor    = {Harald L{\"u}ngen and Marc Kupietz and Piotr Bański and Adrien Barbaresi and Simon Clematide and Ines Pisetta},
  publisher = {Leibniz-Institut f{\"u}r Deutsche Sprache},
  address   = {Mannheim},
  doi       = {10.14618/ids-pub-10468},
  url       = {https://nbn-resolving.org/urn:nbn:de:bsz:mh39-104688},
  pages     = {1 -- 9},
  year      = {2021},
  abstract  = {Since the introduction of large language models in Natural Language Processing, large raw corpora have played a crucial role in Computational Linguistics. However, most of these large raw corpora are either available only for English or not available to the general public due to copyright issues. Nevertheless, there are some examples of freely available multilingual corpora for training Deep Learning NLP models, such as the OSCAR and Paracrawl corpora. However, they have quality issues, especially for low-resource languages. Moreover, recreating or updating these corpora is very complex. In this work, we try to reproduce and improve the goclassy pipeline used to create the OSCAR corpus. We propose a new pipeline that is faster, modular, parameterizable, and well documented. We use it to create a corpus similar to OSCAR but larger and based on recent data. Also, unlike OSCAR, the metadata information is at the document level. We release our pipeline under an open source license and publish the corpus under a research-only license.},
  language  = {en}
}

@ARTICLE{caswell-etal-2021-quality,
       author = {{Caswell}, Isaac and {Kreutzer}, Julia and {Wang}, Lisa and {Wahab}, Ahsan and {van Esch}, Daan and {Ulzii-Orshikh}, Nasanbayar and {Tapo}, Allahsera and {Subramani}, Nishant and {Sokolov}, Artem and {Sikasote}, Claytone and {Setyawan}, Monang and {Sarin}, Supheakmungkol and {Samb}, Sokhar and {Sagot}, Beno{\^\i}t and {Rivera}, Clara and {Rios}, Annette and {Papadimitriou}, Isabel and {Osei}, Salomey and {Ortiz Su{\'a}rez}, Pedro Javier and {Orife}, Iroro and {Ogueji}, Kelechi and {Niyongabo}, Rubungo Andre and {Nguyen}, Toan Q. and {M{\"u}ller}, Mathias and {M{\"u}ller}, Andr{\'e} and {Hassan Muhammad}, Shamsuddeen and {Muhammad}, Nanda and {Mnyakeni}, Ayanda and {Mirzakhalov}, Jamshidbek and {Matangira}, Tapiwanashe and {Leong}, Colin and {Lawson}, Nze and {Kudugunta}, Sneha and {Jernite}, Yacine and {Jenny}, Mathias and {Firat}, Orhan and {Dossou}, Bonaventure F.~P. and {Dlamini}, Sakhile and {de Silva}, Nisansa and {{\c{C}}abuk Ball{\i}}, Sakine and {Biderman}, Stella and {Battisti}, Alessia and {Baruwa}, Ahmed and {Bapna}, Ankur and {Baljekar}, Pallavi and {Abebe Azime}, Israel and {Awokoya}, Ayodele and {Ataman}, Duygu and {Ahia}, Orevaoghene and {Ahia}, Oghenefego and {Agrawal}, Sweta and {Adeyemi}, Mofetoluwa},
        title = "{Quality at a Glance: An Audit of Web-Crawled Multilingual Datasets}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language, Computer Science - Artificial Intelligence},
         year = 2021,
        month = mar,
          eid = {arXiv:2103.12028},
        pages = {arXiv:2103.12028},
archivePrefix = {arXiv},
       eprint = {2103.12028},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv210312028C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@inproceedings{ortiz-suarez-etal-2020-monolingual,
    title = "A Monolingual Approach to Contextualized Word Embeddings for Mid-Resource Languages",
    author = "Ortiz Su{'a}rez, Pedro Javier  and
      Romary, Laurent  and
      Sagot, Benoit",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.156",
    pages = "1703--1714",
    abstract = "We use the multilingual OSCAR corpus, extracted from Common Crawl via language classification, filtering and cleaning, to train monolingual contextualized word embeddings (ELMo) for five mid-resource languages. We then compare the performance of OSCAR-based and Wikipedia-based ELMo embeddings for these languages on the part-of-speech tagging and parsing tasks. We show that, despite the noise in the Common-Crawl-based OSCAR data, embeddings trained on OSCAR perform much better than monolingual embeddings trained on Wikipedia. They actually equal or improve the current state of the art in tagging and parsing for all five languages. In particular, they also improve over multilingual Wikipedia-based contextual embeddings (multilingual BERT), which almost always constitutes the previous state of the art, thereby showing that the benefit of a larger, more diverse corpus surpasses the cross-lingual benefit of multilingual embedding architectures.",
}

@inproceedings{OrtizSuarezSagotRomary2019,
  author    = {Pedro Javier {Ortiz Su{'a}rez} and Benoit Sagot and Laurent Romary},
  title     = {Asynchronous pipelines for processing huge corpora on medium to low resource infrastructures},
  series = {Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-7) 2019. Cardiff, 22nd July 2019},
  editor    = {Piotr Bański and Adrien Barbaresi and Hanno Biber and Evelyn Breiteneder and Simon Clematide and Marc Kupietz and Harald L{"u}ngen and Caroline Iliadi},
  publisher = {Leibniz-Institut f{"u}r Deutsche Sprache},
  address   = {Mannheim},
  doi       = {10.14618/ids-pub-9021},
  url       = {http://nbn-resolving.de/urn:nbn:de:bsz:mh39-90215},
  pages     = {9 -- 16},
  year      = {2019},
  abstract  = {Common Crawl is a considerably large, heterogeneous multilingual corpus comprised of crawled documents from the internet, surpassing 20TB of data and distributed as a set of more than 50 thousand plain text files where each contains many documents written in a wide variety of languages. Even though each document has a metadata block associated to it, this data lacks any information about the language in which each document is written, making it extremely difficult to use Common Crawl for monolingual applications. We propose a general, highly parallel, multithreaded pipeline to clean and classify Common Crawl by language; we specifically design it so that it runs efficiently on medium to low resource infrastructures where I/O speeds are the main constraint. We develop the pipeline so that it can be easily reapplied to any kind of heterogeneous corpus and so that it can be parameterised to a wide range of infrastructures. We also distribute a 6.3TB version of Common Crawl, filtered, classified by language, shuffled at line level in order to avoid copyright issues, and ready to be used for NLP applications.},
  language  = {en}
}

```

### Contributions

Thanks to [@pjox](https://github.com/pjox), [@Uinelj](https://github.com/Uinelj) and [@lhoestq](https://github.com/lhoestq) for adding this dataset.
