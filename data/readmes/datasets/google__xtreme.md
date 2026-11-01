---
annotations_creators:
- found
language_creators:
- found
language:
- af
- ar
- bg
- bn
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- he
- hi
- hu
- id
- it
- ja
- jv
- ka
- kk
- ko
- ml
- mr
- ms
- my
- nl
- pt
- ru
- sw
- ta
- te
- th
- tl
- tr
- ur
- vi
- yo
- zh
license:
- apache-2.0
- cc-by-4.0
- cc-by-2.0
- cc-by-sa-4.0
- other
- cc-by-nc-4.0
multilinguality:
- multilingual
- translation
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
source_datasets:
- extended|xnli
- extended|paws-x
- extended|wikiann
- extended|xquad
- extended|mlqa
- extended|tydiqa
- extended|tatoeba
- extended|squad
task_categories:
- multiple-choice
- question-answering
- token-classification
- text-classification
- text-retrieval
- token-classification
task_ids:
- multiple-choice-qa
- extractive-qa
- open-domain-qa
- natural-language-inference
- named-entity-recognition
- part-of-speech
paperswithcode_id: xtreme
pretty_name: XTREME
config_names:
- MLQA.ar.ar
- MLQA.ar.de
- MLQA.ar.en
- MLQA.ar.es
- MLQA.ar.hi
- MLQA.ar.vi
- MLQA.ar.zh
- MLQA.de.ar
- MLQA.de.de
- MLQA.de.en
- MLQA.de.es
- MLQA.de.hi
- MLQA.de.vi
- MLQA.de.zh
- MLQA.en.ar
- MLQA.en.de
- MLQA.en.en
- MLQA.en.es
- MLQA.en.hi
- MLQA.en.vi
- MLQA.en.zh
- MLQA.es.ar
- MLQA.es.de
- MLQA.es.en
- MLQA.es.es
- MLQA.es.hi
- MLQA.es.vi
- MLQA.es.zh
- MLQA.hi.ar
- MLQA.hi.de
- MLQA.hi.en
- MLQA.hi.es
- MLQA.hi.hi
- MLQA.hi.vi
- MLQA.hi.zh
- MLQA.vi.ar
- MLQA.vi.de
- MLQA.vi.en
- MLQA.vi.es
- MLQA.vi.hi
- MLQA.vi.vi
- MLQA.vi.zh
- MLQA.zh.ar
- MLQA.zh.de
- MLQA.zh.en
- MLQA.zh.es
- MLQA.zh.hi
- MLQA.zh.vi
- MLQA.zh.zh
- PAN-X.af
- PAN-X.ar
- PAN-X.bg
- PAN-X.bn
- PAN-X.de
- PAN-X.el
- PAN-X.en
- PAN-X.es
- PAN-X.et
- PAN-X.eu
- PAN-X.fa
- PAN-X.fi
- PAN-X.fr
- PAN-X.he
- PAN-X.hi
- PAN-X.hu
- PAN-X.id
- PAN-X.it
- PAN-X.ja
- PAN-X.jv
- PAN-X.ka
- PAN-X.kk
- PAN-X.ko
- PAN-X.ml
- PAN-X.mr
- PAN-X.ms
- PAN-X.my
- PAN-X.nl
- PAN-X.pt
- PAN-X.ru
- PAN-X.sw
- PAN-X.ta
- PAN-X.te
- PAN-X.th
- PAN-X.tl
- PAN-X.tr
- PAN-X.ur
- PAN-X.vi
- PAN-X.yo
- PAN-X.zh
- PAWS-X.de
- PAWS-X.en
- PAWS-X.es
- PAWS-X.fr
- PAWS-X.ja
- PAWS-X.ko
- PAWS-X.zh
- SQuAD
- XNLI
- XQuAD
- bucc18.de
- bucc18.fr
- bucc18.ru
- bucc18.zh
- tatoeba.afr
- tatoeba.ara
- tatoeba.ben
- tatoeba.bul
- tatoeba.cmn
- tatoeba.deu
- tatoeba.ell
- tatoeba.est
- tatoeba.eus
- tatoeba.fin
- tatoeba.fra
- tatoeba.heb
- tatoeba.hin
- tatoeba.hun
- tatoeba.ind
- tatoeba.ita
- tatoeba.jav
- tatoeba.jpn
- tatoeba.kat
- tatoeba.kaz
- tatoeba.kor
- tatoeba.mal
- tatoeba.mar
- tatoeba.nld
- tatoeba.pes
- tatoeba.por
- tatoeba.rus
- tatoeba.spa
- tatoeba.swh
- tatoeba.tam
- tatoeba.tel
- tatoeba.tgl
- tatoeba.tha
- tatoeba.tur
- tatoeba.urd
- tatoeba.vie
- tydiqa
- udpos.Afrikans
- udpos.Arabic
- udpos.Basque
- udpos.Bulgarian
- udpos.Chinese
- udpos.Dutch
- udpos.English
- udpos.Estonian
- udpos.Finnish
- udpos.French
- udpos.German
- udpos.Greek
- udpos.Hebrew
- udpos.Hindi
- udpos.Hungarian
- udpos.Indonesian
- udpos.Italian
- udpos.Japanese
- udpos.Kazakh
- udpos.Korean
- udpos.Marathi
- udpos.Persian
- udpos.Portuguese
- udpos.Russian
- udpos.Spanish
- udpos.Tagalog
- udpos.Tamil
- udpos.Telugu
- udpos.Thai
- udpos.Turkish
- udpos.Urdu
- udpos.Vietnamese
- udpos.Yoruba
language_bcp47:
- fa-IR
license_details: Licence Universal Dependencies v2.5
tags:
- parallel-sentence-retrieval
- paraphrase-identification
dataset_info:
- config_name: MLQA.ar.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 8368086
    num_examples: 5335
  - name: validation
    num_bytes: 824080
    num_examples: 517
  download_size: 4048180
  dataset_size: 9192166
- config_name: MLQA.ar.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 2183914
    num_examples: 1649
  - name: validation
    num_bytes: 364809
    num_examples: 207
  download_size: 1192825
  dataset_size: 2548723
- config_name: MLQA.ar.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 8225634
    num_examples: 5335
  - name: validation
    num_bytes: 810061
    num_examples: 517
  download_size: 3998008
  dataset_size: 9035695
- config_name: MLQA.ar.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3041350
    num_examples: 1978
  - name: validation
    num_bytes: 228152
    num_examples: 161
  download_size: 1531661
  dataset_size: 3269502
- config_name: MLQA.ar.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3039368
    num_examples: 1831
  - name: validation
    num_bytes: 281742
    num_examples: 186
  download_size: 1369756
  dataset_size: 3321110
- config_name: MLQA.ar.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3290601
    num_examples: 2047
  - name: validation
    num_bytes: 288418
    num_examples: 163
  download_size: 1667238
  dataset_size: 3579019
- config_name: MLQA.ar.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3229844
    num_examples: 1912
  - name: validation
    num_bytes: 340021
    num_examples: 188
  download_size: 1591445
  dataset_size: 3569865
- config_name: MLQA.de.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1619978
    num_examples: 1649
  - name: validation
    num_bytes: 200146
    num_examples: 207
  download_size: 1044483
  dataset_size: 1820124
- config_name: MLQA.de.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4366074
    num_examples: 4517
  - name: validation
    num_bytes: 488339
    num_examples: 512
  download_size: 2798050
  dataset_size: 4854413
- config_name: MLQA.de.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4343116
    num_examples: 4517
  - name: validation
    num_bytes: 485866
    num_examples: 512
  download_size: 2778346
  dataset_size: 4828982
- config_name: MLQA.de.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1716587
    num_examples: 1776
  - name: validation
    num_bytes: 170554
    num_examples: 196
  download_size: 1118751
  dataset_size: 1887141
- config_name: MLQA.de.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1371046
    num_examples: 1430
  - name: validation
    num_bytes: 153843
    num_examples: 163
  download_size: 880652
  dataset_size: 1524889
- config_name: MLQA.de.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1688455
    num_examples: 1675
  - name: validation
    num_bytes: 216047
    num_examples: 182
  download_size: 1108163
  dataset_size: 1904502
- config_name: MLQA.de.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1679152
    num_examples: 1621
  - name: validation
    num_bytes: 184290
    num_examples: 190
  download_size: 1045861
  dataset_size: 1863442
- config_name: MLQA.en.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 6739191
    num_examples: 5335
  - name: validation
    num_bytes: 630815
    num_examples: 517
  download_size: 3939135
  dataset_size: 7370006
- config_name: MLQA.en.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 5056694
    num_examples: 4517
  - name: validation
    num_bytes: 594908
    num_examples: 512
  download_size: 3223196
  dataset_size: 5651602
- config_name: MLQA.en.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 14004592
    num_examples: 11590
  - name: validation
    num_bytes: 1329084
    num_examples: 1148
  download_size: 8217519
  dataset_size: 15333676
- config_name: MLQA.en.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 6179221
    num_examples: 5253
  - name: validation
    num_bytes: 555434
    num_examples: 500
  download_size: 3776828
  dataset_size: 6734655
- config_name: MLQA.en.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 6378838
    num_examples: 4918
  - name: validation
    num_bytes: 623143
    num_examples: 507
  download_size: 3517340
  dataset_size: 7001981
- config_name: MLQA.en.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 7056670
    num_examples: 5495
  - name: validation
    num_bytes: 640618
    num_examples: 511
  download_size: 4170642
  dataset_size: 7697288
- config_name: MLQA.en.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 6539279
    num_examples: 5137
  - name: validation
    num_bytes: 608416
    num_examples: 504
  download_size: 3929122
  dataset_size: 7147695
- config_name: MLQA.es.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1740254
    num_examples: 1978
  - name: validation
    num_bytes: 148621
    num_examples: 161
  download_size: 1107435
  dataset_size: 1888875
- config_name: MLQA.es.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1403997
    num_examples: 1776
  - name: validation
    num_bytes: 144158
    num_examples: 196
  download_size: 950448
  dataset_size: 1548155
- config_name: MLQA.es.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4362709
    num_examples: 5253
  - name: validation
    num_bytes: 419040
    num_examples: 500
  download_size: 2842879
  dataset_size: 4781749
- config_name: MLQA.es.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4394305
    num_examples: 5253
  - name: validation
    num_bytes: 422043
    num_examples: 500
  download_size: 2856931
  dataset_size: 4816348
- config_name: MLQA.es.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1523495
    num_examples: 1723
  - name: validation
    num_bytes: 181806
    num_examples: 187
  download_size: 954018
  dataset_size: 1705301
- config_name: MLQA.es.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1747941
    num_examples: 2018
  - name: validation
    num_bytes: 176813
    num_examples: 189
  download_size: 1187949
  dataset_size: 1924754
- config_name: MLQA.es.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1678423
    num_examples: 1947
  - name: validation
    num_bytes: 126618
    num_examples: 161
  download_size: 1100765
  dataset_size: 1805041
- config_name: MLQA.hi.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4445561
    num_examples: 1831
  - name: validation
    num_bytes: 410396
    num_examples: 186
  download_size: 1542768
  dataset_size: 4855957
- config_name: MLQA.hi.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3022836
    num_examples: 1430
  - name: validation
    num_bytes: 301685
    num_examples: 163
  download_size: 1257846
  dataset_size: 3324521
- config_name: MLQA.hi.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 11449233
    num_examples: 4918
  - name: validation
    num_bytes: 1097829
    num_examples: 507
  download_size: 4131083
  dataset_size: 12547062
- config_name: MLQA.hi.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3862201
    num_examples: 1723
  - name: validation
    num_bytes: 420374
    num_examples: 187
  download_size: 1493468
  dataset_size: 4282575
- config_name: MLQA.hi.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 11810447
    num_examples: 4918
  - name: validation
    num_bytes: 1136756
    num_examples: 507
  download_size: 4235981
  dataset_size: 12947203
- config_name: MLQA.hi.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4743456
    num_examples: 1947
  - name: validation
    num_bytes: 419078
    num_examples: 177
  download_size: 1704964
  dataset_size: 5162534
- config_name: MLQA.hi.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4354847
    num_examples: 1767
  - name: validation
    num_bytes: 424218
    num_examples: 189
  download_size: 1627107
  dataset_size: 4779065
- config_name: MLQA.vi.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 3205157
    num_examples: 2047
  - name: validation
    num_bytes: 230307
    num_examples: 163
  download_size: 1656661
  dataset_size: 3435464
- config_name: MLQA.vi.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 2227005
    num_examples: 1675
  - name: validation
    num_bytes: 277157
    num_examples: 182
  download_size: 1268041
  dataset_size: 2504162
- config_name: MLQA.vi.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 7843403
    num_examples: 5495
  - name: validation
    num_bytes: 719245
    num_examples: 511
  download_size: 4071703
  dataset_size: 8562648
- config_name: MLQA.vi.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 2866569
    num_examples: 2018
  - name: validation
    num_bytes: 283433
    num_examples: 189
  download_size: 1607926
  dataset_size: 3150002
- config_name: MLQA.vi.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 2776636
    num_examples: 1947
  - name: validation
    num_bytes: 254979
    num_examples: 177
  download_size: 1366057
  dataset_size: 3031615
- config_name: MLQA.vi.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 7922057
    num_examples: 5495
  - name: validation
    num_bytes: 726490
    num_examples: 511
  download_size: 4105388
  dataset_size: 8648547
- config_name: MLQA.vi.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 2989632
    num_examples: 1943
  - name: validation
    num_bytes: 269361
    num_examples: 184
  download_size: 1570393
  dataset_size: 3258993
- config_name: MLQA.zh.ar
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1731455
    num_examples: 1912
  - name: validation
    num_bytes: 175321
    num_examples: 188
  download_size: 1223863
  dataset_size: 1906776
- config_name: MLQA.zh.de
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1389990
    num_examples: 1621
  - name: validation
    num_bytes: 174577
    num_examples: 190
  download_size: 1006829
  dataset_size: 1564567
- config_name: MLQA.zh.en
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4450957
    num_examples: 5137
  - name: validation
    num_bytes: 446840
    num_examples: 504
  download_size: 3108433
  dataset_size: 4897797
- config_name: MLQA.zh.es
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1736255
    num_examples: 1947
  - name: validation
    num_bytes: 138045
    num_examples: 161
  download_size: 1223467
  dataset_size: 1874300
- config_name: MLQA.zh.hi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1578191
    num_examples: 1767
  - name: validation
    num_bytes: 184373
    num_examples: 189
  download_size: 1044599
  dataset_size: 1762564
- config_name: MLQA.zh.vi
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 1806158
    num_examples: 1943
  - name: validation
    num_bytes: 172906
    num_examples: 184
  download_size: 1268213
  dataset_size: 1979064
- config_name: MLQA.zh.zh
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: test
    num_bytes: 4422322
    num_examples: 5137
  - name: validation
    num_bytes: 443782
    num_examples: 504
  download_size: 3105362
  dataset_size: 4866104
- config_name: PAN-X.af
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 1321376
    num_examples: 5000
  - name: validation
    num_bytes: 259689
    num_examples: 1000
  - name: test
    num_bytes: 257184
    num_examples: 1000
  download_size: 389015
  dataset_size: 1838249
- config_name: PAN-X.ar
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3634096
    num_examples: 20000
  - name: validation
    num_bytes: 1808283
    num_examples: 10000
  - name: test
    num_bytes: 1811963
    num_examples: 10000
  download_size: 1567470
  dataset_size: 7254342
- config_name: PAN-X.bg
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4600733
    num_examples: 20000
  - name: validation
    num_bytes: 2310294
    num_examples: 10000
  - name: test
    num_bytes: 2306138
    num_examples: 10000
  download_size: 2030669
  dataset_size: 9217165
- config_name: PAN-X.bn
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 1568825
    num_examples: 10000
  - name: validation
    num_bytes: 159068
    num_examples: 1000
  - name: test
    num_bytes: 159262
    num_examples: 1000
  download_size: 364024
  dataset_size: 1887155
- config_name: PAN-X.de
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4762312
    num_examples: 20000
  - name: validation
    num_bytes: 2381545
    num_examples: 10000
  - name: test
    num_bytes: 2377619
    num_examples: 10000
  download_size: 2360242
  dataset_size: 9521476
- config_name: PAN-X.el
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 5063136
    num_examples: 20000
  - name: validation
    num_bytes: 2533786
    num_examples: 10000
  - name: test
    num_bytes: 2547574
    num_examples: 10000
  download_size: 2271726
  dataset_size: 10144496
- config_name: PAN-X.en
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3823434
    num_examples: 20000
  - name: validation
    num_bytes: 1920049
    num_examples: 10000
  - name: test
    num_bytes: 1916200
    num_examples: 10000
  download_size: 1886284
  dataset_size: 7659683
- config_name: PAN-X.es
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3199121
    num_examples: 20000
  - name: validation
    num_bytes: 1592505
    num_examples: 10000
  - name: test
    num_bytes: 1602271
    num_examples: 10000
  download_size: 1489562
  dataset_size: 6393897
- config_name: PAN-X.et
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3023171
    num_examples: 15000
  - name: validation
    num_bytes: 2030140
    num_examples: 10000
  - name: test
    num_bytes: 2021389
    num_examples: 10000
  download_size: 1915624
  dataset_size: 7074700
- config_name: PAN-X.eu
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 2292307
    num_examples: 10000
  - name: validation
    num_bytes: 2296315
    num_examples: 10000
  - name: test
    num_bytes: 2249815
    num_examples: 10000
  download_size: 1393179
  dataset_size: 6838437
- config_name: PAN-X.fa
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3529314
    num_examples: 20000
  - name: validation
    num_bytes: 1782286
    num_examples: 10000
  - name: test
    num_bytes: 1770264
    num_examples: 10000
  download_size: 1401208
  dataset_size: 7081864
- config_name: PAN-X.fi
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4273753
    num_examples: 20000
  - name: validation
    num_bytes: 2131749
    num_examples: 10000
  - name: test
    num_bytes: 2130645
    num_examples: 10000
  download_size: 2459149
  dataset_size: 8536147
- config_name: PAN-X.fr
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3335384
    num_examples: 20000
  - name: validation
    num_bytes: 1664170
    num_examples: 10000
  - name: test
    num_bytes: 1675765
    num_examples: 10000
  download_size: 1679283
  dataset_size: 6675319
- config_name: PAN-X.he
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4667060
    num_examples: 20000
  - name: validation
    num_bytes: 2332740
    num_examples: 10000
  - name: test
    num_bytes: 2318736
    num_examples: 10000
  download_size: 2186463
  dataset_size: 9318536
- config_name: PAN-X.hi
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 964192
    num_examples: 5000
  - name: validation
    num_bytes: 190651
    num_examples: 1000
  - name: test
    num_bytes: 196170
    num_examples: 1000
  download_size: 266086
  dataset_size: 1351013
- config_name: PAN-X.hu
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4499874
    num_examples: 20000
  - name: validation
    num_bytes: 2211831
    num_examples: 10000
  - name: test
    num_bytes: 2249759
    num_examples: 10000
  download_size: 2399390
  dataset_size: 8961464
- config_name: PAN-X.id
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3083967
    num_examples: 20000
  - name: validation
    num_bytes: 1537959
    num_examples: 10000
  - name: test
    num_bytes: 1536859
    num_examples: 10000
  download_size: 1412049
  dataset_size: 6158785
- config_name: PAN-X.it
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3874623
    num_examples: 20000
  - name: validation
    num_bytes: 1908509
    num_examples: 10000
  - name: test
    num_bytes: 1928388
    num_examples: 10000
  download_size: 1855798
  dataset_size: 7711520
- config_name: PAN-X.ja
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 12670361
    num_examples: 20000
  - name: validation
    num_bytes: 6322983
    num_examples: 10000
  - name: test
    num_bytes: 6448940
    num_examples: 10000
  download_size: 2465674
  dataset_size: 25442284
- config_name: PAN-X.jv
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 16086
    num_examples: 100
  - name: validation
    num_bytes: 14580
    num_examples: 100
  - name: test
    num_bytes: 16897
    num_examples: 100
  download_size: 20475
  dataset_size: 47563
- config_name: PAN-X.ka
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 2777342
    num_examples: 10000
  - name: validation
    num_bytes: 2806881
    num_examples: 10000
  - name: test
    num_bytes: 2824621
    num_examples: 10000
  download_size: 1817280
  dataset_size: 8408844
- config_name: PAN-X.kk
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 240256
    num_examples: 1000
  - name: validation
    num_bytes: 238089
    num_examples: 1000
  - name: test
    num_bytes: 236704
    num_examples: 1000
  download_size: 160554
  dataset_size: 715049
- config_name: PAN-X.ko
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4284693
    num_examples: 20000
  - name: validation
    num_bytes: 2138147
    num_examples: 10000
  - name: test
    num_bytes: 2138274
    num_examples: 10000
  download_size: 2539591
  dataset_size: 8561114
- config_name: PAN-X.ml
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 2865184
    num_examples: 10000
  - name: validation
    num_bytes: 290735
    num_examples: 1000
  - name: test
    num_bytes: 276906
    num_examples: 1000
  download_size: 852955
  dataset_size: 3432825
- config_name: PAN-X.mr
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 1248239
    num_examples: 5000
  - name: validation
    num_bytes: 245338
    num_examples: 1000
  - name: test
    num_bytes: 255884
    num_examples: 1000
  download_size: 347215
  dataset_size: 1749461
- config_name: PAN-X.ms
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 2965008
    num_examples: 20000
  - name: validation
    num_bytes: 147495
    num_examples: 1000
  - name: test
    num_bytes: 147148
    num_examples: 1000
  download_size: 708795
  dataset_size: 3259651
- config_name: PAN-X.my
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 32715
    num_examples: 100
  - name: validation
    num_bytes: 40408
    num_examples: 100
  - name: test
    num_bytes: 37346
    num_examples: 100
  download_size: 39008
  dataset_size: 110469
- config_name: PAN-X.nl
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4062149
    num_examples: 20000
  - name: validation
    num_bytes: 2016836
    num_examples: 10000
  - name: test
    num_bytes: 2038618
    num_examples: 10000
  download_size: 1943893
  dataset_size: 8117603
- config_name: PAN-X.pt
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3149243
    num_examples: 20000
  - name: validation
    num_bytes: 1575121
    num_examples: 10000
  - name: test
    num_bytes: 1562605
    num_examples: 10000
  download_size: 1540478
  dataset_size: 6286969
- config_name: PAN-X.ru
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4121751
    num_examples: 20000
  - name: validation
    num_bytes: 2053149
    num_examples: 10000
  - name: test
    num_bytes: 2074125
    num_examples: 10000
  download_size: 2127730
  dataset_size: 8249025
- config_name: PAN-X.sw
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 135891
    num_examples: 1000
  - name: validation
    num_bytes: 136348
    num_examples: 1000
  - name: test
    num_bytes: 140211
    num_examples: 1000
  download_size: 87435
  dataset_size: 412450
- config_name: PAN-X.ta
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 4122090
    num_examples: 15000
  - name: validation
    num_bytes: 277605
    num_examples: 1000
  - name: test
    num_bytes: 278094
    num_examples: 1000
  download_size: 1044729
  dataset_size: 4677789
- config_name: PAN-X.te
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 295390
    num_examples: 1000
  - name: validation
    num_bytes: 293261
    num_examples: 1000
  - name: test
    num_bytes: 296943
    num_examples: 1000
  download_size: 200516
  dataset_size: 885594
- config_name: PAN-X.th
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 27132989
    num_examples: 20000
  - name: validation
    num_bytes: 13262717
    num_examples: 10000
  - name: test
    num_bytes: 13586908
    num_examples: 10000
  download_size: 2569566
  dataset_size: 53982614
- config_name: PAN-X.tl
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 1168697
    num_examples: 10000
  - name: validation
    num_bytes: 114136
    num_examples: 1000
  - name: test
    num_bytes: 117884
    num_examples: 1000
  download_size: 308160
  dataset_size: 1400717
- config_name: PAN-X.tr
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3779130
    num_examples: 20000
  - name: validation
    num_bytes: 1915332
    num_examples: 10000
  - name: test
    num_bytes: 1911483
    num_examples: 10000
  download_size: 2000699
  dataset_size: 7605945
- config_name: PAN-X.ur
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3072236
    num_examples: 20000
  - name: validation
    num_bytes: 152128
    num_examples: 1000
  - name: test
    num_bytes: 151902
    num_examples: 1000
  download_size: 610869
  dataset_size: 3376266
- config_name: PAN-X.vi
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 3153187
    num_examples: 20000
  - name: validation
    num_bytes: 1565123
    num_examples: 10000
  - name: test
    num_bytes: 1580196
    num_examples: 10000
  download_size: 1375631
  dataset_size: 6298506
- config_name: PAN-X.yo
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 14689
    num_examples: 100
  - name: validation
    num_bytes: 13225
    num_examples: 100
  - name: test
    num_bytes: 13513
    num_examples: 100
  download_size: 17337
  dataset_size: 41427
- config_name: PAN-X.zh
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  - name: langs
    sequence: string
  splits:
  - name: train
    num_bytes: 8832011
    num_examples: 20000
  - name: validation
    num_bytes: 4491305
    num_examples: 10000
  - name: test
    num_bytes: 4363152
    num_examples: 10000
  download_size: 2083198
  dataset_size: 17686468
- config_name: PAWS-X.de
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 12451823
    num_examples: 49380
  - name: validation
    num_bytes: 499997
    num_examples: 2000
  - name: test
    num_bytes: 510182
    num_examples: 2000
  download_size: 9294034
  dataset_size: 13462002
- config_name: PAWS-X.en
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 11827659
    num_examples: 49175
  - name: validation
    num_bytes: 478279
    num_examples: 2000
  - name: test
    num_bytes: 480726
    num_examples: 2000
  download_size: 8717639
  dataset_size: 12786664
- config_name: PAWS-X.es
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 12462047
    num_examples: 49401
  - name: validation
    num_bytes: 494057
    num_examples: 1961
  - name: test
    num_bytes: 505035
    num_examples: 2000
  download_size: 9229918
  dataset_size: 13461139
- config_name: PAWS-X.fr
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 12948452
    num_examples: 49399
  - name: validation
    num_bytes: 516099
    num_examples: 1988
  - name: test
    num_bytes: 521019
    num_examples: 2000
  download_size: 9464987
  dataset_size: 13985570
- config_name: PAWS-X.ja
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 14695593
    num_examples: 49401
  - name: validation
    num_bytes: 647762
    num_examples: 2000
  - name: test
    num_bytes: 654628
    num_examples: 2000
  download_size: 10136228
  dataset_size: 15997983
- config_name: PAWS-X.ko
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 13542597
    num_examples: 49164
  - name: validation
    num_bytes: 540775
    num_examples: 2000
  - name: test
    num_bytes: 547966
    num_examples: 1999
  download_size: 9926292
  dataset_size: 14631338
- config_name: PAWS-X.zh
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 10469652
    num_examples: 49401
  - name: validation
    num_bytes: 459108
    num_examples: 2000
  - name: test
    num_bytes: 460626
    num_examples: 2000
  download_size: 8878855
  dataset_size: 11389386
- config_name: SQuAD
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 79316858
    num_examples: 87599
  - name: validation
    num_bytes: 10472597
    num_examples: 10570
  download_size: 16272656
  dataset_size: 89789455
- config_name: XNLI
  features:
  - name: language
    dtype: string
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: gold_label
    dtype: string
  splits:
  - name: test
    num_bytes: 20359372
    num_examples: 75150
  - name: validation
    num_bytes: 10049239
    num_examples: 37350
  download_size: 8881623
  dataset_size: 30408611
- config_name: XQuAD.ar
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1722775
    num_examples: 1190
  download_size: 263032
  dataset_size: 1722775
- config_name: XQuAD.de
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1283277
    num_examples: 1190
  download_size: 241987
  dataset_size: 1283277
- config_name: XQuAD.el
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 2206666
    num_examples: 1190
  download_size: 324409
  dataset_size: 2206666
- config_name: XQuAD.en
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1116099
    num_examples: 1190
  download_size: 212402
  dataset_size: 1116099
- config_name: XQuAD.es
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1273475
    num_examples: 1190
  download_size: 236904
  dataset_size: 1273475
- config_name: XQuAD.hi
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 2682951
    num_examples: 1190
  download_size: 322113
  dataset_size: 2682951
- config_name: XQuAD.ru
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 2136966
    num_examples: 1190
  download_size: 321758
  dataset_size: 2136966
- config_name: XQuAD.th
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 2854935
    num_examples: 1190
  download_size: 337337
  dataset_size: 2854935
- config_name: XQuAD.tr
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1210739
    num_examples: 1190
  download_size: 228394
  dataset_size: 1210739
- config_name: XQuAD.vi
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 1477215
    num_examples: 1190
  download_size: 237674
  dataset_size: 1477215
- config_name: XQuAD.zh
  features:
  - name: id
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: validation
    num_bytes: 984217
    num_examples: 1190
  download_size: 205798
  dataset_size: 984217
- config_name: bucc18.de
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 248691
    num_examples: 1038
  - name: test
    num_bytes: 2325685
    num_examples: 9580
  download_size: 1636130
  dataset_size: 2574376
- config_name: bucc18.fr
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 212497
    num_examples: 929
  - name: test
    num_bytes: 2082403
    num_examples: 9086
  download_size: 1437096
  dataset_size: 2294900
- config_name: bucc18.ru
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 761331
    num_examples: 2374
  - name: test
    num_bytes: 4641646
    num_examples: 14435
  download_size: 3074476
  dataset_size: 5402977
- config_name: bucc18.zh
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 55723
    num_examples: 257
  - name: test
    num_bytes: 415909
    num_examples: 1899
  download_size: 320378
  dataset_size: 471632
- config_name: tatoeba.afr
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 250635
    num_examples: 1000
  download_size: 47676
  dataset_size: 250635
- config_name: tatoeba.ara
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 263650
    num_examples: 1000
  download_size: 51228
  dataset_size: 263650
- config_name: tatoeba.ben
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 282703
    num_examples: 1000
  download_size: 51362
  dataset_size: 282703
- config_name: tatoeba.bul
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 293279
    num_examples: 1000
  download_size: 62454
  dataset_size: 293279
- config_name: tatoeba.cmn
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 259931
    num_examples: 1000
  download_size: 58281
  dataset_size: 259931
- config_name: tatoeba.deu
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 296567
    num_examples: 1000
  download_size: 79066
  dataset_size: 296567
- config_name: tatoeba.ell
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 269961
    num_examples: 1000
  download_size: 52251
  dataset_size: 269961
- config_name: tatoeba.est
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 250728
    num_examples: 1000
  download_size: 49968
  dataset_size: 250728
- config_name: tatoeba.eus
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 257068
    num_examples: 1000
  download_size: 54271
  dataset_size: 257068
- config_name: tatoeba.fin
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 266669
    num_examples: 1000
  download_size: 60580
  dataset_size: 266669
- config_name: tatoeba.fra
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 271018
    num_examples: 1000
  download_size: 60925
  dataset_size: 271018
- config_name: tatoeba.heb
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 274500
    num_examples: 1000
  download_size: 57306
  dataset_size: 274500
- config_name: tatoeba.hin
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 313558
    num_examples: 1000
  download_size: 68816
  dataset_size: 313558
- config_name: tatoeba.hun
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 259889
    num_examples: 1000
  download_size: 58096
  dataset_size: 259889
- config_name: tatoeba.ind
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 265844
    num_examples: 1000
  download_size: 57047
  dataset_size: 265844
- config_name: tatoeba.ita
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 256833
    num_examples: 1000
  download_size: 52422
  dataset_size: 256833
- config_name: tatoeba.jav
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 53068
    num_examples: 205
  download_size: 15208
  dataset_size: 53068
- config_name: tatoeba.jpn
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 284083
    num_examples: 1000
  download_size: 66620
  dataset_size: 284083
- config_name: tatoeba.kat
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 214646
    num_examples: 746
  download_size: 41759
  dataset_size: 214646
- config_name: tatoeba.kaz
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 157003
    num_examples: 575
  download_size: 35693
  dataset_size: 157003
- config_name: tatoeba.kor
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 270139
    num_examples: 1000
  download_size: 61210
  dataset_size: 270139
- config_name: tatoeba.mal
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 225934
    num_examples: 687
  download_size: 51077
  dataset_size: 225934
- config_name: tatoeba.mar
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 291542
    num_examples: 1000
  download_size: 56575
  dataset_size: 291542
- config_name: tatoeba.nld
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 264263
    num_examples: 1000
  download_size: 59774
  dataset_size: 264263
- config_name: tatoeba.pes
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 284719
    num_examples: 1000
  download_size: 64642
  dataset_size: 284719
- config_name: tatoeba.por
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 266185
    num_examples: 1000
  download_size: 58250
  dataset_size: 266185
- config_name: tatoeba.rus
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 283472
    num_examples: 1000
  download_size: 61601
  dataset_size: 283472
- config_name: tatoeba.spa
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 263266
    num_examples: 1000
  download_size: 57055
  dataset_size: 263266
- config_name: tatoeba.swh
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 94957
    num_examples: 390
  download_size: 19362
  dataset_size: 94957
- config_name: tatoeba.tam
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 98078
    num_examples: 307
  download_size: 23648
  dataset_size: 98078
- config_name: tatoeba.tel
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 69837
    num_examples: 234
  download_size: 18260
  dataset_size: 69837
- config_name: tatoeba.tgl
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 259138
    num_examples: 1000
  download_size: 53699
  dataset_size: 259138
- config_name: tatoeba.tha
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 167866
    num_examples: 548
  download_size: 39659
  dataset_size: 167866
- config_name: tatoeba.tur
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 262885
    num_examples: 1000
  download_size: 54137
  dataset_size: 262885
- config_name: tatoeba.urd
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 279712
    num_examples: 1000
  download_size: 60399
  dataset_size: 279712
- config_name: tatoeba.vie
  features:
  - name: source_sentence
    dtype: string
  - name: target_sentence
    dtype: string
  - name: source_lang
    dtype: string
  - name: target_lang
    dtype: string
  splits:
  - name: validation
    num_bytes: 282407
    num_examples: 1000
  download_size: 66746
  dataset_size: 282407
- config_name: tydiqa
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: answer_start
      dtype: int32
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 52948467
    num_examples: 49881
  - name: validation
    num_bytes: 5006433
    num_examples: 5077
  download_size: 29402238
  dataset_size: 57954900
- config_name: udpos.Afrikaans
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 586370
    num_examples: 1315
  - name: validation
    num_bytes: 91290
    num_examples: 194
  - name: test
    num_bytes: 174244
    num_examples: 425
  download_size: 193788
  dataset_size: 851904
- config_name: udpos.Arabic
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 4453682
    num_examples: 6075
  - name: validation
    num_bytes: 593650
    num_examples: 909
  - name: test
    num_bytes: 973822
    num_examples: 1680
  download_size: 1186113
  dataset_size: 6021154
- config_name: udpos.Basque
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 1327713
    num_examples: 5396
  - name: validation
    num_bytes: 438671
    num_examples: 1798
  - name: test
    num_bytes: 444644
    num_examples: 1799
  download_size: 703094
  dataset_size: 2211028
- config_name: udpos.Bulgarian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 2689767
    num_examples: 8907
  - name: validation
    num_bytes: 347117
    num_examples: 1115
  - name: test
    num_bytes: 339947
    num_examples: 1116
  download_size: 926186
  dataset_size: 3376831
- config_name: udpos.Chinese
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 4218891
    num_examples: 18998
  - name: validation
    num_bytes: 594448
    num_examples: 3038
  - name: test
    num_bytes: 1236051
    num_examples: 5528
  download_size: 1471747
  dataset_size: 6049390
- config_name: udpos.Dutch
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 4517994
    num_examples: 18051
  - name: validation
    num_bytes: 393592
    num_examples: 1394
  - name: test
    num_bytes: 397904
    num_examples: 1471
  download_size: 1410982
  dataset_size: 5309490
- config_name: udpos.English
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 6225509
    num_examples: 21253
  - name: validation
    num_bytes: 1042040
    num_examples: 3974
  - name: test
    num_bytes: 1421148
    num_examples: 5440
  download_size: 2116535
  dataset_size: 8688697
- config_name: udpos.Estonian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 6614893
    num_examples: 25749
  - name: validation
    num_bytes: 814171
    num_examples: 3125
  - name: test
    num_bytes: 1065701
    num_examples: 3760
  download_size: 2619121
  dataset_size: 8494765
- config_name: udpos.Finnish
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 5613706
    num_examples: 27198
  - name: validation
    num_bytes: 656646
    num_examples: 3239
  - name: test
    num_bytes: 1025726
    num_examples: 4422
  download_size: 2503217
  dataset_size: 7296078
- config_name: udpos.French
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 10118933
    num_examples: 47308
  - name: validation
    num_bytes: 1294096
    num_examples: 5979
  - name: test
    num_bytes: 1731049
    num_examples: 9465
  download_size: 3378680
  dataset_size: 13144078
- config_name: udpos.German
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 54773777
    num_examples: 166849
  - name: validation
    num_bytes: 6044838
    num_examples: 19233
  - name: test
    num_bytes: 7345863
    num_examples: 22458
  download_size: 18623155
  dataset_size: 68164478
- config_name: udpos.Greek
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 8932104
    num_examples: 28152
  - name: validation
    num_bytes: 1062447
    num_examples: 2559
  - name: test
    num_bytes: 1028665
    num_examples: 2809
  download_size: 2763293
  dataset_size: 11023216
- config_name: udpos.Hebrew
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 2505691
    num_examples: 5241
  - name: validation
    num_bytes: 210013
    num_examples: 484
  - name: test
    num_bytes: 223865
    num_examples: 491
  download_size: 624771
  dataset_size: 2939569
- config_name: udpos.Hindi
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 6690250
    num_examples: 13304
  - name: validation
    num_bytes: 839702
    num_examples: 1659
  - name: test
    num_bytes: 1400225
    num_examples: 2684
  download_size: 1468314
  dataset_size: 8930177
- config_name: udpos.Hungarian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 372226
    num_examples: 910
  - name: validation
    num_bytes: 215879
    num_examples: 441
  - name: test
    num_bytes: 193728
    num_examples: 449
  download_size: 251882
  dataset_size: 781833
- config_name: udpos.Indonesian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 1710678
    num_examples: 4477
  - name: validation
    num_bytes: 220863
    num_examples: 559
  - name: test
    num_bytes: 557101
    num_examples: 1557
  download_size: 684225
  dataset_size: 2488642
- config_name: udpos.Italian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 11299293
    num_examples: 29685
  - name: validation
    num_bytes: 988996
    num_examples: 2278
  - name: test
    num_bytes: 1337869
    num_examples: 3518
  download_size: 3256246
  dataset_size: 13626158
- config_name: udpos.Japanese
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 2792951
    num_examples: 7125
  - name: validation
    num_bytes: 200356
    num_examples: 511
  - name: test
    num_bytes: 928902
    num_examples: 2372
  download_size: 1012282
  dataset_size: 3922209
- config_name: udpos.Kazakh
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 11438
    num_examples: 31
  - name: test
    num_bytes: 228924
    num_examples: 1047
  download_size: 76300
  dataset_size: 240362
- config_name: udpos.Korean
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 7341267
    num_examples: 27410
  - name: validation
    num_bytes: 782587
    num_examples: 3016
  - name: test
    num_bytes: 1162539
    num_examples: 4276
  download_size: 3115101
  dataset_size: 9286393
- config_name: udpos.Marathi
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 59023
    num_examples: 373
  - name: validation
    num_bytes: 8497
    num_examples: 46
  - name: test
    num_bytes: 7871
    num_examples: 47
  download_size: 22133
  dataset_size: 75391
- config_name: udpos.Persian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 2400776
    num_examples: 4798
  - name: validation
    num_bytes: 317053
    num_examples: 599
  - name: test
    num_bytes: 320683
    num_examples: 600
  download_size: 606912
  dataset_size: 3038512
- config_name: udpos.Portuguese
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 7669556
    num_examples: 17992
  - name: validation
    num_bytes: 712397
    num_examples: 1770
  - name: test
    num_bytes: 1082582
    num_examples: 2681
  download_size: 2505672
  dataset_size: 9464535
- config_name: udpos.Russian
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 24230098
    num_examples: 67435
  - name: validation
    num_bytes: 3457031
    num_examples: 9960
  - name: test
    num_bytes: 4236693
    num_examples: 11336
  download_size: 8818512
  dataset_size: 31923822
- config_name: udpos.Spanish
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 13858406
    num_examples: 28492
  - name: validation
    num_bytes: 1498765
    num_examples: 3054
  - name: test
    num_bytes: 1476500
    num_examples: 3147
  download_size: 4347905
  dataset_size: 16833671
- config_name: udpos.Tagalog
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: test
    num_bytes: 5153
    num_examples: 55
  download_size: 3345
  dataset_size: 5153
- config_name: udpos.Tamil
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 202596
    num_examples: 400
  - name: validation
    num_bytes: 40031
    num_examples: 80
  - name: test
    num_bytes: 62366
    num_examples: 120
  download_size: 73764
  dataset_size: 304993
- config_name: udpos.Telugu
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 138049
    num_examples: 1051
  - name: validation
    num_bytes: 17990
    num_examples: 131
  - name: test
    num_bytes: 19575
    num_examples: 146
  download_size: 46045
  dataset_size: 175614
- config_name: udpos.Thai
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: test
    num_bytes: 561336
    num_examples: 1000
  download_size: 92925
  dataset_size: 561336
- config_name: udpos.Turkish
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 704405
    num_examples: 3664
  - name: validation
    num_bytes: 186455
    num_examples: 988
  - name: test
    num_bytes: 827382
    num_examples: 4785
  download_size: 581177
  dataset_size: 1718242
- config_name: udpos.Urdu
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 2107362
    num_examples: 4043
  - name: validation
    num_bytes: 284261
    num_examples: 552
  - name: test
    num_bytes: 288553
    num_examples: 535
  download_size: 499594
  dataset_size: 2680176
- config_name: udpos.Vietnamese
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: train
    num_bytes: 367335
    num_examples: 1400
  - name: validation
    num_bytes: 206188
    num_examples: 800
  - name: test
    num_bytes: 214063
    num_examples: 800
  download_size: 181239
  dataset_size: 787586
- config_name: udpos.Yoruba
  features:
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ADJ
          '1': ADP
          '2': ADV
          '3': AUX
          '4': CCONJ
          '5': DET
          '6': INTJ
          '7': NOUN
          '8': NUM
          '9': PART
          '10': PRON
          '11': PROPN
          '12': PUNCT
          '13': SCONJ
          '14': SYM
          '15': VERB
          '16': X
  splits:
  - name: test
    num_bytes: 44656
    num_examples: 100
  download_size: 10151
  dataset_size: 44656
configs:
- config_name: MLQA.ar.ar
  data_files:
  - split: test
    path: MLQA.ar.ar/test-*
  - split: validation
    path: MLQA.ar.ar/validation-*
- config_name: MLQA.ar.de
  data_files:
  - split: test
    path: MLQA.ar.de/test-*
  - split: validation
    path: MLQA.ar.de/validation-*
- config_name: MLQA.ar.en
  data_files:
  - split: test
    path: MLQA.ar.en/test-*
  - split: validation
    path: MLQA.ar.en/validation-*
- config_name: MLQA.ar.es
  data_files:
  - split: test
    path: MLQA.ar.es/test-*
  - split: validation
    path: MLQA.ar.es/validation-*
- config_name: MLQA.ar.hi
  data_files:
  - split: test
    path: MLQA.ar.hi/test-*
  - split: validation
    path: MLQA.ar.hi/validation-*
- config_name: MLQA.ar.vi
  data_files:
  - split: test
    path: MLQA.ar.vi/test-*
  - split: validation
    path: MLQA.ar.vi/validation-*
- config_name: MLQA.ar.zh
  data_files:
  - split: test
    path: MLQA.ar.zh/test-*
  - split: validation
    path: MLQA.ar.zh/validation-*
- config_name: MLQA.de.ar
  data_files:
  - split: test
    path: MLQA.de.ar/test-*
  - split: validation
    path: MLQA.de.ar/validation-*
- config_name: MLQA.de.de
  data_files:
  - split: test
    path: MLQA.de.de/test-*
  - split: validation
    path: MLQA.de.de/validation-*
- config_name: MLQA.de.en
  data_files:
  - split: test
    path: MLQA.de.en/test-*
  - split: validation
    path: MLQA.de.en/validation-*
- config_name: MLQA.de.es
  data_files:
  - split: test
    path: MLQA.de.es/test-*
  - split: validation
    path: MLQA.de.es/validation-*
- config_name: MLQA.de.hi
  data_files:
  - split: test
    path: MLQA.de.hi/test-*
  - split: validation
    path: MLQA.de.hi/validation-*
- config_name: MLQA.de.vi
  data_files:
  - split: test
    path: MLQA.de.vi/test-*
  - split: validation
    path: MLQA.de.vi/validation-*
- config_name: MLQA.de.zh
  data_files:
  - split: test
    path: MLQA.de.zh/test-*
  - split: validation
    path: MLQA.de.zh/validation-*
- config_name: MLQA.en.ar
  data_files:
  - split: test
    path: MLQA.en.ar/test-*
  - split: validation
    path: MLQA.en.ar/validation-*
- config_name: MLQA.en.de
  data_files:
  - split: test
    path: MLQA.en.de/test-*
  - split: validation
    path: MLQA.en.de/validation-*
- config_name: MLQA.en.en
  data_files:
  - split: test
    path: MLQA.en.en/test-*
  - split: validation
    path: MLQA.en.en/validation-*
- config_name: MLQA.en.es
  data_files:
  - split: test
    path: MLQA.en.es/test-*
  - split: validation
    path: MLQA.en.es/validation-*
- config_name: MLQA.en.hi
  data_files:
  - split: test
    path: MLQA.en.hi/test-*
  - split: validation
    path: MLQA.en.hi/validation-*
- config_name: MLQA.en.vi
  data_files:
  - split: test
    path: MLQA.en.vi/test-*
  - split: validation
    path: MLQA.en.vi/validation-*
- config_name: MLQA.en.zh
  data_files:
  - split: test
    path: MLQA.en.zh/test-*
  - split: validation
    path: MLQA.en.zh/validation-*
- config_name: MLQA.es.ar
  data_files:
  - split: test
    path: MLQA.es.ar/test-*
  - split: validation
    path: MLQA.es.ar/validation-*
- config_name: MLQA.es.de
  data_files:
  - split: test
    path: MLQA.es.de/test-*
  - split: validation
    path: MLQA.es.de/validation-*
- config_name: MLQA.es.en
  data_files:
  - split: test
    path: MLQA.es.en/test-*
  - split: validation
    path: MLQA.es.en/validation-*
- config_name: MLQA.es.es
  data_files:
  - split: test
    path: MLQA.es.es/test-*
  - split: validation
    path: MLQA.es.es/validation-*
- config_name: MLQA.es.hi
  data_files:
  - split: test
    path: MLQA.es.hi/test-*
  - split: validation
    path: MLQA.es.hi/validation-*
- config_name: MLQA.es.vi
  data_files:
  - split: test
    path: MLQA.es.vi/test-*
  - split: validation
    path: MLQA.es.vi/validation-*
- config_name: MLQA.es.zh
  data_files:
  - split: test
    path: MLQA.es.zh/test-*
  - split: validation
    path: MLQA.es.zh/validation-*
- config_name: MLQA.hi.ar
  data_files:
  - split: test
    path: MLQA.hi.ar/test-*
  - split: validation
    path: MLQA.hi.ar/validation-*
- config_name: MLQA.hi.de
  data_files:
  - split: test
    path: MLQA.hi.de/test-*
  - split: validation
    path: MLQA.hi.de/validation-*
- config_name: MLQA.hi.en
  data_files:
  - split: test
    path: MLQA.hi.en/test-*
  - split: validation
    path: MLQA.hi.en/validation-*
- config_name: MLQA.hi.es
  data_files:
  - split: test
    path: MLQA.hi.es/test-*
  - split: validation
    path: MLQA.hi.es/validation-*
- config_name: MLQA.hi.hi
  data_files:
  - split: test
    path: MLQA.hi.hi/test-*
  - split: validation
    path: MLQA.hi.hi/validation-*
- config_name: MLQA.hi.vi
  data_files:
  - split: test
    path: MLQA.hi.vi/test-*
  - split: validation
    path: MLQA.hi.vi/validation-*
- config_name: MLQA.hi.zh
  data_files:
  - split: test
    path: MLQA.hi.zh/test-*
  - split: validation
    path: MLQA.hi.zh/validation-*
- config_name: MLQA.vi.ar
  data_files:
  - split: test
    path: MLQA.vi.ar/test-*
  - split: validation
    path: MLQA.vi.ar/validation-*
- config_name: MLQA.vi.de
  data_files:
  - split: test
    path: MLQA.vi.de/test-*
  - split: validation
    path: MLQA.vi.de/validation-*
- config_name: MLQA.vi.en
  data_files:
  - split: test
    path: MLQA.vi.en/test-*
  - split: validation
    path: MLQA.vi.en/validation-*
- config_name: MLQA.vi.es
  data_files:
  - split: test
    path: MLQA.vi.es/test-*
  - split: validation
    path: MLQA.vi.es/validation-*
- config_name: MLQA.vi.hi
  data_files:
  - split: test
    path: MLQA.vi.hi/test-*
  - split: validation
    path: MLQA.vi.hi/validation-*
- config_name: MLQA.vi.vi
  data_files:
  - split: test
    path: MLQA.vi.vi/test-*
  - split: validation
    path: MLQA.vi.vi/validation-*
- config_name: MLQA.vi.zh
  data_files:
  - split: test
    path: MLQA.vi.zh/test-*
  - split: validation
    path: MLQA.vi.zh/validation-*
- config_name: MLQA.zh.ar
  data_files:
  - split: test
    path: MLQA.zh.ar/test-*
  - split: validation
    path: MLQA.zh.ar/validation-*
- config_name: MLQA.zh.de
  data_files:
  - split: test
    path: MLQA.zh.de/test-*
  - split: validation
    path: MLQA.zh.de/validation-*
- config_name: MLQA.zh.en
  data_files:
  - split: test
    path: MLQA.zh.en/test-*
  - split: validation
    path: MLQA.zh.en/validation-*
- config_name: MLQA.zh.es
  data_files:
  - split: test
    path: MLQA.zh.es/test-*
  - split: validation
    path: MLQA.zh.es/validation-*
- config_name: MLQA.zh.hi
  data_files:
  - split: test
    path: MLQA.zh.hi/test-*
  - split: validation
    path: MLQA.zh.hi/validation-*
- config_name: MLQA.zh.vi
  data_files:
  - split: test
    path: MLQA.zh.vi/test-*
  - split: validation
    path: MLQA.zh.vi/validation-*
- config_name: MLQA.zh.zh
  data_files:
  - split: test
    path: MLQA.zh.zh/test-*
  - split: validation
    path: MLQA.zh.zh/validation-*
- config_name: PAN-X.af
  data_files:
  - split: train
    path: PAN-X.af/train-*
  - split: validation
    path: PAN-X.af/validation-*
  - split: test
    path: PAN-X.af/test-*
- config_name: PAN-X.ar
  data_files:
  - split: train
    path: PAN-X.ar/train-*
  - split: validation
    path: PAN-X.ar/validation-*
  - split: test
    path: PAN-X.ar/test-*
- config_name: PAN-X.bg
  data_files:
  - split: train
    path: PAN-X.bg/train-*
  - split: validation
    path: PAN-X.bg/validation-*
  - split: test
    path: PAN-X.bg/test-*
- config_name: PAN-X.bn
  data_files:
  - split: train
    path: PAN-X.bn/train-*
  - split: validation
    path: PAN-X.bn/validation-*
  - split: test
    path: PAN-X.bn/test-*
- config_name: PAN-X.de
  data_files:
  - split: train
    path: PAN-X.de/train-*
  - split: validation
    path: PAN-X.de/validation-*
  - split: test
    path: PAN-X.de/test-*
- config_name: PAN-X.el
  data_files:
  - split: train
    path: PAN-X.el/train-*
  - split: validation
    path: PAN-X.el/validation-*
  - split: test
    path: PAN-X.el/test-*
- config_name: PAN-X.en
  data_files:
  - split: train
    path: PAN-X.en/train-*
  - split: validation
    path: PAN-X.en/validation-*
  - split: test
    path: PAN-X.en/test-*
- config_name: PAN-X.es
  data_files:
  - split: train
    path: PAN-X.es/train-*
  - split: validation
    path: PAN-X.es/validation-*
  - split: test
    path: PAN-X.es/test-*
- config_name: PAN-X.et
  data_files:
  - split: train
    path: PAN-X.et/train-*
  - split: validation
    path: PAN-X.et/validation-*
  - split: test
    path: PAN-X.et/test-*
- config_name: PAN-X.eu
  data_files:
  - split: train
    path: PAN-X.eu/train-*
  - split: validation
    path: PAN-X.eu/validation-*
  - split: test
    path: PAN-X.eu/test-*
- config_name: PAN-X.fa
  data_files:
  - split: train
    path: PAN-X.fa/train-*
  - split: validation
    path: PAN-X.fa/validation-*
  - split: test
    path: PAN-X.fa/test-*
- config_name: PAN-X.fi
  data_files:
  - split: train
    path: PAN-X.fi/train-*
  - split: validation
    path: PAN-X.fi/validation-*
  - split: test
    path: PAN-X.fi/test-*
- config_name: PAN-X.fr
  data_files:
  - split: train
    path: PAN-X.fr/train-*
  - split: validation
    path: PAN-X.fr/validation-*
  - split: test
    path: PAN-X.fr/test-*
- config_name: PAN-X.he
  data_files:
  - split: train
    path: PAN-X.he/train-*
  - split: validation
    path: PAN-X.he/validation-*
  - split: test
    path: PAN-X.he/test-*
- config_name: PAN-X.hi
  data_files:
  - split: train
    path: PAN-X.hi/train-*
  - split: validation
    path: PAN-X.hi/validation-*
  - split: test
    path: PAN-X.hi/test-*
- config_name: PAN-X.hu
  data_files:
  - split: train
    path: PAN-X.hu/train-*
  - split: validation
    path: PAN-X.hu/validation-*
  - split: test
    path: PAN-X.hu/test-*
- config_name: PAN-X.id
  data_files:
  - split: train
    path: PAN-X.id/train-*
  - split: validation
    path: PAN-X.id/validation-*
  - split: test
    path: PAN-X.id/test-*
- config_name: PAN-X.it
  data_files:
  - split: train
    path: PAN-X.it/train-*
  - split: validation
    path: PAN-X.it/validation-*
  - split: test
    path: PAN-X.it/test-*
- config_name: PAN-X.ja
  data_files:
  - split: train
    path: PAN-X.ja/train-*
  - split: validation
    path: PAN-X.ja/validation-*
  - split: test
    path: PAN-X.ja/test-*
- config_name: PAN-X.jv
  data_files:
  - split: train
    path: PAN-X.jv/train-*
  - split: validation
    path: PAN-X.jv/validation-*
  - split: test
    path: PAN-X.jv/test-*
- config_name: PAN-X.ka
  data_files:
  - split: train
    path: PAN-X.ka/train-*
  - split: validation
    path: PAN-X.ka/validation-*
  - split: test
    path: PAN-X.ka/test-*
- config_name: PAN-X.kk
  data_files:
  - split: train
    path: PAN-X.kk/train-*
  - split: validation
    path: PAN-X.kk/validation-*
  - split: test
    path: PAN-X.kk/test-*
- config_name: PAN-X.ko
  data_files:
  - split: train
    path: PAN-X.ko/train-*
  - split: validation
    path: PAN-X.ko/validation-*
  - split: test
    path: PAN-X.ko/test-*
- config_name: PAN-X.ml
  data_files:
  - split: train
    path: PAN-X.ml/train-*
  - split: validation
    path: PAN-X.ml/validation-*
  - split: test
    path: PAN-X.ml/test-*
- config_name: PAN-X.mr
  data_files:
  - split: train
    path: PAN-X.mr/train-*
  - split: validation
    path: PAN-X.mr/validation-*
  - split: test
    path: PAN-X.mr/test-*
- config_name: PAN-X.ms
  data_files:
  - split: train
    path: PAN-X.ms/train-*
  - split: validation
    path: PAN-X.ms/validation-*
  - split: test
    path: PAN-X.ms/test-*
- config_name: PAN-X.my
  data_files:
  - split: train
    path: PAN-X.my/train-*
  - split: validation
    path: PAN-X.my/validation-*
  - split: test
    path: PAN-X.my/test-*
- config_name: PAN-X.nl
  data_files:
  - split: train
    path: PAN-X.nl/train-*
  - split: validation
    path: PAN-X.nl/validation-*
  - split: test
    path: PAN-X.nl/test-*
- config_name: PAN-X.pt
  data_files:
  - split: train
    path: PAN-X.pt/train-*
  - split: validation
    path: PAN-X.pt/validation-*
  - split: test
    path: PAN-X.pt/test-*
- config_name: PAN-X.ru
  data_files:
  - split: train
    path: PAN-X.ru/train-*
  - split: validation
    path: PAN-X.ru/validation-*
  - split: test
    path: PAN-X.ru/test-*
- config_name: PAN-X.sw
  data_files:
  - split: train
    path: PAN-X.sw/train-*
  - split: validation
    path: PAN-X.sw/validation-*
  - split: test
    path: PAN-X.sw/test-*
- config_name: PAN-X.ta
  data_files:
  - split: train
    path: PAN-X.ta/train-*
  - split: validation
    path: PAN-X.ta/validation-*
  - split: test
    path: PAN-X.ta/test-*
- config_name: PAN-X.te
  data_files:
  - split: train
    path: PAN-X.te/train-*
  - split: validation
    path: PAN-X.te/validation-*
  - split: test
    path: PAN-X.te/test-*
- config_name: PAN-X.th
  data_files:
  - split: train
    path: PAN-X.th/train-*
  - split: validation
    path: PAN-X.th/validation-*
  - split: test
    path: PAN-X.th/test-*
- config_name: PAN-X.tl
  data_files:
  - split: train
    path: PAN-X.tl/train-*
  - split: validation
    path: PAN-X.tl/validation-*
  - split: test
    path: PAN-X.tl/test-*
- config_name: PAN-X.tr
  data_files:
  - split: train
    path: PAN-X.tr/train-*
  - split: validation
    path: PAN-X.tr/validation-*
  - split: test
    path: PAN-X.tr/test-*
- config_name: PAN-X.ur
  data_files:
  - split: train
    path: PAN-X.ur/train-*
  - split: validation
    path: PAN-X.ur/validation-*
  - split: test
    path: PAN-X.ur/test-*
- config_name: PAN-X.vi
  data_files:
  - split: train
    path: PAN-X.vi/train-*
  - split: validation
    path: PAN-X.vi/validation-*
  - split: test
    path: PAN-X.vi/test-*
- config_name: PAN-X.yo
  data_files:
  - split: train
    path: PAN-X.yo/train-*
  - split: validation
    path: PAN-X.yo/validation-*
  - split: test
    path: PAN-X.yo/test-*
- config_name: PAN-X.zh
  data_files:
  - split: train
    path: PAN-X.zh/train-*
  - split: validation
    path: PAN-X.zh/validation-*
  - split: test
    path: PAN-X.zh/test-*
- config_name: PAWS-X.de
  data_files:
  - split: train
    path: PAWS-X.de/train-*
  - split: validation
    path: PAWS-X.de/validation-*
  - split: test
    path: PAWS-X.de/test-*
- config_name: PAWS-X.en
  data_files:
  - split: train
    path: PAWS-X.en/train-*
  - split: validation
    path: PAWS-X.en/validation-*
  - split: test
    path: PAWS-X.en/test-*
- config_name: PAWS-X.es
  data_files:
  - split: train
    path: PAWS-X.es/train-*
  - split: validation
    path: PAWS-X.es/validation-*
  - split: test
    path: PAWS-X.es/test-*
- config_name: PAWS-X.fr
  data_files:
  - split: train
    path: PAWS-X.fr/train-*
  - split: validation
    path: PAWS-X.fr/validation-*
  - split: test
    path: PAWS-X.fr/test-*
- config_name: PAWS-X.ja
  data_files:
  - split: train
    path: PAWS-X.ja/train-*
  - split: validation
    path: PAWS-X.ja/validation-*
  - split: test
    path: PAWS-X.ja/test-*
- config_name: PAWS-X.ko
  data_files:
  - split: train
    path: PAWS-X.ko/train-*
  - split: validation
    path: PAWS-X.ko/validation-*
  - split: test
    path: PAWS-X.ko/test-*
- config_name: PAWS-X.zh
  data_files:
  - split: train
    path: PAWS-X.zh/train-*
  - split: validation
    path: PAWS-X.zh/validation-*
  - split: test
    path: PAWS-X.zh/test-*
- config_name: SQuAD
  data_files:
  - split: train
    path: SQuAD/train-*
  - split: validation
    path: SQuAD/validation-*
- config_name: XNLI
  data_files:
  - split: test
    path: XNLI/test-*
  - split: validation
    path: XNLI/validation-*
- config_name: XQuAD.ar
  data_files:
  - split: validation
    path: XQuAD.ar/validation-*
- config_name: XQuAD.de
  data_files:
  - split: validation
    path: XQuAD.de/validation-*
- config_name: XQuAD.el
  data_files:
  - split: validation
    path: XQuAD.el/validation-*
- config_name: XQuAD.en
  data_files:
  - split: validation
    path: XQuAD.en/validation-*
- config_name: XQuAD.es
  data_files:
  - split: validation
    path: XQuAD.es/validation-*
- config_name: XQuAD.hi
  data_files:
  - split: validation
    path: XQuAD.hi/validation-*
- config_name: XQuAD.ru
  data_files:
  - split: validation
    path: XQuAD.ru/validation-*
- config_name: XQuAD.th
  data_files:
  - split: validation
    path: XQuAD.th/validation-*
- config_name: XQuAD.tr
  data_files:
  - split: validation
    path: XQuAD.tr/validation-*
- config_name: XQuAD.vi
  data_files:
  - split: validation
    path: XQuAD.vi/validation-*
- config_name: XQuAD.zh
  data_files:
  - split: validation
    path: XQuAD.zh/validation-*
- config_name: bucc18.de
  data_files:
  - split: validation
    path: bucc18.de/validation-*
  - split: test
    path: bucc18.de/test-*
- config_name: bucc18.fr
  data_files:
  - split: validation
    path: bucc18.fr/validation-*
  - split: test
    path: bucc18.fr/test-*
- config_name: bucc18.ru
  data_files:
  - split: validation
    path: bucc18.ru/validation-*
  - split: test
    path: bucc18.ru/test-*
- config_name: bucc18.zh
  data_files:
  - split: validation
    path: bucc18.zh/validation-*
  - split: test
    path: bucc18.zh/test-*
- config_name: tatoeba.afr
  data_files:
  - split: validation
    path: tatoeba.afr/validation-*
- config_name: tatoeba.ara
  data_files:
  - split: validation
    path: tatoeba.ara/validation-*
- config_name: tatoeba.ben
  data_files:
  - split: validation
    path: tatoeba.ben/validation-*
- config_name: tatoeba.bul
  data_files:
  - split: validation
    path: tatoeba.bul/validation-*
- config_name: tatoeba.cmn
  data_files:
  - split: validation
    path: tatoeba.cmn/validation-*
- config_name: tatoeba.deu
  data_files:
  - split: validation
    path: tatoeba.deu/validation-*
- config_name: tatoeba.ell
  data_files:
  - split: validation
    path: tatoeba.ell/validation-*
- config_name: tatoeba.est
  data_files:
  - split: validation
    path: tatoeba.est/validation-*
- config_name: tatoeba.eus
  data_files:
  - split: validation
    path: tatoeba.eus/validation-*
- config_name: tatoeba.fin
  data_files:
  - split: validation
    path: tatoeba.fin/validation-*
- config_name: tatoeba.fra
  data_files:
  - split: validation
    path: tatoeba.fra/validation-*
- config_name: tatoeba.heb
  data_files:
  - split: validation
    path: tatoeba.heb/validation-*
- config_name: tatoeba.hin
  data_files:
  - split: validation
    path: tatoeba.hin/validation-*
- config_name: tatoeba.hun
  data_files:
  - split: validation
    path: tatoeba.hun/validation-*
- config_name: tatoeba.ind
  data_files:
  - split: validation
    path: tatoeba.ind/validation-*
- config_name: tatoeba.ita
  data_files:
  - split: validation
    path: tatoeba.ita/validation-*
- config_name: tatoeba.jav
  data_files:
  - split: validation
    path: tatoeba.jav/validation-*
- config_name: tatoeba.jpn
  data_files:
  - split: validation
    path: tatoeba.jpn/validation-*
- config_name: tatoeba.kat
  data_files:
  - split: validation
    path: tatoeba.kat/validation-*
- config_name: tatoeba.kaz
  data_files:
  - split: validation
    path: tatoeba.kaz/validation-*
- config_name: tatoeba.kor
  data_files:
  - split: validation
    path: tatoeba.kor/validation-*
- config_name: tatoeba.mal
  data_files:
  - split: validation
    path: tatoeba.mal/validation-*
- config_name: tatoeba.mar
  data_files:
  - split: validation
    path: tatoeba.mar/validation-*
- config_name: tatoeba.nld
  data_files:
  - split: validation
    path: tatoeba.nld/validation-*
- config_name: tatoeba.pes
  data_files:
  - split: validation
    path: tatoeba.pes/validation-*
- config_name: tatoeba.por
  data_files:
  - split: validation
    path: tatoeba.por/validation-*
- config_name: tatoeba.rus
  data_files:
  - split: validation
    path: tatoeba.rus/validation-*
- config_name: tatoeba.spa
  data_files:
  - split: validation
    path: tatoeba.spa/validation-*
- config_name: tatoeba.swh
  data_files:
  - split: validation
    path: tatoeba.swh/validation-*
- config_name: tatoeba.tam
  data_files:
  - split: validation
    path: tatoeba.tam/validation-*
- config_name: tatoeba.tel
  data_files:
  - split: validation
    path: tatoeba.tel/validation-*
- config_name: tatoeba.tgl
  data_files:
  - split: validation
    path: tatoeba.tgl/validation-*
- config_name: tatoeba.tha
  data_files:
  - split: validation
    path: tatoeba.tha/validation-*
- config_name: tatoeba.tur
  data_files:
  - split: validation
    path: tatoeba.tur/validation-*
- config_name: tatoeba.urd
  data_files:
  - split: validation
    path: tatoeba.urd/validation-*
- config_name: tatoeba.vie
  data_files:
  - split: validation
    path: tatoeba.vie/validation-*
- config_name: tydiqa
  data_files:
  - split: train
    path: tydiqa/train-*
  - split: validation
    path: tydiqa/validation-*
- config_name: udpos.Afrikaans
  data_files:
  - split: train
    path: udpos.Afrikaans/train-*
  - split: validation
    path: udpos.Afrikaans/validation-*
  - split: test
    path: udpos.Afrikaans/test-*
- config_name: udpos.Arabic
  data_files:
  - split: train
    path: udpos.Arabic/train-*
  - split: validation
    path: udpos.Arabic/validation-*
  - split: test
    path: udpos.Arabic/test-*
- config_name: udpos.Basque
  data_files:
  - split: train
    path: udpos.Basque/train-*
  - split: validation
    path: udpos.Basque/validation-*
  - split: test
    path: udpos.Basque/test-*
- config_name: udpos.Bulgarian
  data_files:
  - split: train
    path: udpos.Bulgarian/train-*
  - split: validation
    path: udpos.Bulgarian/validation-*
  - split: test
    path: udpos.Bulgarian/test-*
- config_name: udpos.Chinese
  data_files:
  - split: train
    path: udpos.Chinese/train-*
  - split: validation
    path: udpos.Chinese/validation-*
  - split: test
    path: udpos.Chinese/test-*
- config_name: udpos.Dutch
  data_files:
  - split: train
    path: udpos.Dutch/train-*
  - split: validation
    path: udpos.Dutch/validation-*
  - split: test
    path: udpos.Dutch/test-*
- config_name: udpos.English
  data_files:
  - split: train
    path: udpos.English/train-*
  - split: validation
    path: udpos.English/validation-*
  - split: test
    path: udpos.English/test-*
- config_name: udpos.Estonian
  data_files:
  - split: train
    path: udpos.Estonian/train-*
  - split: validation
    path: udpos.Estonian/validation-*
  - split: test
    path: udpos.Estonian/test-*
- config_name: udpos.Finnish
  data_files:
  - split: train
    path: udpos.Finnish/train-*
  - split: validation
    path: udpos.Finnish/validation-*
  - split: test
    path: udpos.Finnish/test-*
- config_name: udpos.French
  data_files:
  - split: train
    path: udpos.French/train-*
  - split: validation
    path: udpos.French/validation-*
  - split: test
    path: udpos.French/test-*
- config_name: udpos.German
  data_files:
  - split: train
    path: udpos.German/train-*
  - split: validation
    path: udpos.German/validation-*
  - split: test
    path: udpos.German/test-*
- config_name: udpos.Greek
  data_files:
  - split: train
    path: udpos.Greek/train-*
  - split: validation
    path: udpos.Greek/validation-*
  - split: test
    path: udpos.Greek/test-*
- config_name: udpos.Hebrew
  data_files:
  - split: train
    path: udpos.Hebrew/train-*
  - split: validation
    path: udpos.Hebrew/validation-*
  - split: test
    path: udpos.Hebrew/test-*
- config_name: udpos.Hindi
  data_files:
  - split: train
    path: udpos.Hindi/train-*
  - split: validation
    path: udpos.Hindi/validation-*
  - split: test
    path: udpos.Hindi/test-*
- config_name: udpos.Hungarian
  data_files:
  - split: train
    path: udpos.Hungarian/train-*
  - split: validation
    path: udpos.Hungarian/validation-*
  - split: test
    path: udpos.Hungarian/test-*
- config_name: udpos.Indonesian
  data_files:
  - split: train
    path: udpos.Indonesian/train-*
  - split: validation
    path: udpos.Indonesian/validation-*
  - split: test
    path: udpos.Indonesian/test-*
- config_name: udpos.Italian
  data_files:
  - split: train
    path: udpos.Italian/train-*
  - split: validation
    path: udpos.Italian/validation-*
  - split: test
    path: udpos.Italian/test-*
- config_name: udpos.Japanese
  data_files:
  - split: train
    path: udpos.Japanese/train-*
  - split: validation
    path: udpos.Japanese/validation-*
  - split: test
    path: udpos.Japanese/test-*
- config_name: udpos.Kazakh
  data_files:
  - split: train
    path: udpos.Kazakh/train-*
  - split: test
    path: udpos.Kazakh/test-*
- config_name: udpos.Korean
  data_files:
  - split: train
    path: udpos.Korean/train-*
  - split: validation
    path: udpos.Korean/validation-*
  - split: test
    path: udpos.Korean/test-*
- config_name: udpos.Marathi
  data_files:
  - split: train
    path: udpos.Marathi/train-*
  - split: validation
    path: udpos.Marathi/validation-*
  - split: test
    path: udpos.Marathi/test-*
- config_name: udpos.Persian
  data_files:
  - split: train
    path: udpos.Persian/train-*
  - split: validation
    path: udpos.Persian/validation-*
  - split: test
    path: udpos.Persian/test-*
- config_name: udpos.Portuguese
  data_files:
  - split: train
    path: udpos.Portuguese/train-*
  - split: validation
    path: udpos.Portuguese/validation-*
  - split: test
    path: udpos.Portuguese/test-*
- config_name: udpos.Russian
  data_files:
  - split: train
    path: udpos.Russian/train-*
  - split: validation
    path: udpos.Russian/validation-*
  - split: test
    path: udpos.Russian/test-*
- config_name: udpos.Spanish
  data_files:
  - split: train
    path: udpos.Spanish/train-*
  - split: validation
    path: udpos.Spanish/validation-*
  - split: test
    path: udpos.Spanish/test-*
- config_name: udpos.Tagalog
  data_files:
  - split: test
    path: udpos.Tagalog/test-*
- config_name: udpos.Tamil
  data_files:
  - split: train
    path: udpos.Tamil/train-*
  - split: validation
    path: udpos.Tamil/validation-*
  - split: test
    path: udpos.Tamil/test-*
- config_name: udpos.Telugu
  data_files:
  - split: train
    path: udpos.Telugu/train-*
  - split: validation
    path: udpos.Telugu/validation-*
  - split: test
    path: udpos.Telugu/test-*
- config_name: udpos.Thai
  data_files:
  - split: test
    path: udpos.Thai/test-*
- config_name: udpos.Turkish
  data_files:
  - split: train
    path: udpos.Turkish/train-*
  - split: validation
    path: udpos.Turkish/validation-*
  - split: test
    path: udpos.Turkish/test-*
- config_name: udpos.Urdu
  data_files:
  - split: train
    path: udpos.Urdu/train-*
  - split: validation
    path: udpos.Urdu/validation-*
  - split: test
    path: udpos.Urdu/test-*
- config_name: udpos.Vietnamese
  data_files:
  - split: train
    path: udpos.Vietnamese/train-*
  - split: validation
    path: udpos.Vietnamese/validation-*
  - split: test
    path: udpos.Vietnamese/test-*
- config_name: udpos.Yoruba
  data_files:
  - split: test
    path: udpos.Yoruba/test-*
---

# Dataset Card for "xtreme"

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

- **Homepage:** [https://github.com/google-research/xtreme](https://github.com/google-research/xtreme)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 15.88 GB
- **Size of the generated dataset:** 1.08 GB
- **Total amount of disk used:** 16.96 GB

### Dataset Summary

The Cross-lingual Natural Language Inference (XNLI) corpus is a crowd-sourced collection of 5,000 test and
2,500 dev pairs for the MultiNLI corpus. The pairs are annotated with textual entailment and translated into
14 languages: French, Spanish, German, Greek, Bulgarian, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese,
Hindi, Swahili and Urdu. This results in 112.5k annotated pairs. Each premise can be associated with the
corresponding hypothesis in the 15 languages, summing up to more than 1.5M combinations. The corpus is made to
evaluate how to perform inference in any language (including low-resources ones like Swahili or Urdu) when only
English NLI data is available at training time. One solution is cross-lingual sentence encoding, for which XNLI
is an evaluation benchmark.
The Cross-lingual TRansfer Evaluation of Multilingual Encoders (XTREME) benchmark is a benchmark for the evaluation of
the cross-lingual generalization ability of pre-trained multilingual models. It covers 40 typologically diverse languages
(spanning 12 language families) and includes nine tasks that collectively require reasoning about different levels of
syntax and semantics. The languages in XTREME are selected to maximize language diversity, coverage in existing tasks,
and availability of training data. Among these are many under-studied languages, such as the Dravidian languages Tamil
(spoken in southern India, Sri Lanka, and Singapore), Telugu and Malayalam (spoken mainly in southern India), and the
Niger-Congo languages Swahili and Yoruba, spoken in Africa.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### MLQA.ar.ar

- **Size of downloaded dataset files:** 75.72 MB
- **Size of the generated dataset:** 9.20 MB
- **Total amount of disk used:** 84.91 MB

An example of 'validation' looks as follows.
```

```

#### MLQA.ar.de

- **Size of downloaded dataset files:** 75.72 MB
- **Size of the generated dataset:** 2.55 MB
- **Total amount of disk used:** 78.27 MB

An example of 'validation' looks as follows.
```

```

#### MLQA.ar.en

- **Size of downloaded dataset files:** 75.72 MB
- **Size of the generated dataset:** 9.04 MB
- **Total amount of disk used:** 84.76 MB

An example of 'validation' looks as follows.
```

```

#### MLQA.ar.es

- **Size of downloaded dataset files:** 75.72 MB
- **Size of the generated dataset:** 3.27 MB
- **Total amount of disk used:** 78.99 MB

An example of 'validation' looks as follows.
```

```

#### MLQA.ar.hi

- **Size of downloaded dataset files:** 75.72 MB
- **Size of the generated dataset:** 3.32 MB
- **Total amount of disk used:** 79.04 MB

An example of 'validation' looks as follows.
```

```

### Data Fields

The data fields are the same among all splits.

#### MLQA.ar.ar
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `answer_start`: a `int32` feature.
  - `text`: a `string` feature.

#### MLQA.ar.de
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `answer_start`: a `int32` feature.
  - `text`: a `string` feature.

#### MLQA.ar.en
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `answer_start`: a `int32` feature.
  - `text`: a `string` feature.

#### MLQA.ar.es
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `answer_start`: a `int32` feature.
  - `text`: a `string` feature.

#### MLQA.ar.hi
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `answer_start`: a `int32` feature.
  - `text`: a `string` feature.

### Data Splits

|   name   |validation|test|
|----------|---------:|---:|
|MLQA.ar.ar|       517|5335|
|MLQA.ar.de|       207|1649|
|MLQA.ar.en|       517|5335|
|MLQA.ar.es|       161|1978|
|MLQA.ar.hi|       186|1831|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
  @InProceedings{conneau2018xnli,
  author = {Conneau, Alexis
                 and Rinott, Ruty
                 and Lample, Guillaume
                 and Williams, Adina
                 and Bowman, Samuel R.
                 and Schwenk, Holger
                 and Stoyanov, Veselin},
  title = {XNLI: Evaluating Cross-lingual Sentence Representations},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods
               in Natural Language Processing},
  year = {2018},
  publisher = {Association for Computational Linguistics},
  location = {Brussels, Belgium},
}
@article{hu2020xtreme,
      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},
      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},
      journal   = {CoRR},
      volume    = {abs/2003.11080},
      year      = {2020},
      archivePrefix = {arXiv},
      eprint    = {2003.11080}
}

```


### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@jplu](https://github.com/jplu), [@lewtun](https://github.com/lewtun), [@lvwerra](https://github.com/lvwerra), [@lhoestq](https://github.com/lhoestq), [@patrickvonplaten](https://github.com/patrickvonplaten), [@mariamabarham](https://github.com/mariamabarham) for adding this dataset.