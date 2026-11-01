---
annotations_creators:
- machine-generated
language_creators:
- crowdsourced
language:
- ace
- af
- als
- am
- an
- ang
- ar
- arc
- arz
- as
- ast
- ay
- az
- ba
- bar
- be
- bg
- bh
- bn
- bo
- br
- bs
- ca
- cbk
- cdo
- ce
- ceb
- ckb
- co
- crh
- cs
- csb
- cv
- cy
- da
- de
- diq
- dv
- el
- eml
- en
- eo
- es
- et
- eu
- ext
- fa
- fi
- fo
- fr
- frr
- fur
- fy
- ga
- gan
- gd
- gl
- gn
- gu
- hak
- he
- hi
- hr
- hsb
- hu
- hy
- ia
- id
- ig
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
- ksh
- ku
- ky
- la
- lb
- li
- lij
- lmo
- ln
- lt
- lv
- lzh
- mg
- mhr
- mi
- min
- mk
- ml
- mn
- mr
- ms
- mt
- mwl
- my
- mzn
- nan
- nap
- nds
- ne
- nl
- nn
- 'no'
- nov
- oc
- or
- os
- pa
- pdc
- pl
- pms
- pnb
- ps
- pt
- qu
- rm
- ro
- ru
- rw
- sa
- sah
- scn
- sco
- sd
- sgs
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
- szl
- ta
- te
- tg
- th
- tk
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vec
- vep
- vi
- vls
- vo
- vro
- wa
- war
- wuu
- xmf
- yi
- yo
- yue
- zea
- zh
license:
- unknown
multilinguality:
- multilingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
paperswithcode_id: wikiann-1
pretty_name: WikiANN
config_names:
- 'no'
- ace
- af
- als
- am
- an
- ang
- ar
- arc
- arz
- as
- ast
- ay
- az
- ba
- bar
- be
- bg
- bh
- bn
- bo
- br
- bs
- ca
- cdo
- ce
- ceb
- ckb
- co
- crh
- cs
- csb
- cv
- cy
- da
- de
- diq
- dv
- el
- en
- eo
- es
- et
- eu
- ext
- fa
- fi
- fo
- fr
- frr
- fur
- fy
- ga
- gan
- gd
- gl
- gn
- gu
- hak
- he
- hi
- hr
- hsb
- hu
- hy
- ia
- id
- ig
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
- ksh
- ku
- ky
- la
- lb
- li
- lij
- lmo
- ln
- lt
- lv
- mg
- mhr
- mi
- min
- mk
- ml
- mn
- mr
- ms
- mt
- mwl
- my
- mzn
- nap
- nds
- ne
- nl
- nn
- nov
- oc
- or
- os
- other-bat-smg
- other-be-x-old
- other-cbk-zam
- other-eml
- other-fiu-vro
- other-map-bms
- other-simple
- other-zh-classical
- other-zh-min-nan
- other-zh-yue
- pa
- pdc
- pl
- pms
- pnb
- ps
- pt
- qu
- rm
- ro
- ru
- rw
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
- szl
- ta
- te
- tg
- th
- tk
- tl
- tr
- tt
- ug
- uk
- ur
- uz
- vec
- vep
- vi
- vls
- vo
- wa
- war
- wuu
- xmf
- yi
- yo
- zea
- zh
language_bcp47:
- be-tarask
- en-basiceng
- jv-x-bms
dataset_info:
- config_name: ace
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22425
    num_examples: 100
  - name: test
    num_bytes: 25724
    num_examples: 100
  - name: train
    num_bytes: 23203
    num_examples: 100
  download_size: 27835
  dataset_size: 71352
- config_name: af
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 299109
    num_examples: 1000
  - name: test
    num_bytes: 295821
    num_examples: 1000
  - name: train
    num_bytes: 1521576
    num_examples: 5000
  download_size: 528580
  dataset_size: 2116506
- config_name: als
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 34290
    num_examples: 100
  - name: test
    num_bytes: 36317
    num_examples: 100
  - name: train
    num_bytes: 34940
    num_examples: 100
  download_size: 40186
  dataset_size: 105547
- config_name: am
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21401
    num_examples: 100
  - name: test
    num_bytes: 23783
    num_examples: 100
  - name: train
    num_bytes: 22186
    num_examples: 100
  download_size: 30287
  dataset_size: 67370
- config_name: an
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 180581
    num_examples: 1000
  - name: test
    num_bytes: 174964
    num_examples: 1000
  - name: train
    num_bytes: 180939
    num_examples: 1000
  download_size: 128283
  dataset_size: 536484
- config_name: ang
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21897
    num_examples: 100
  - name: test
    num_bytes: 24495
    num_examples: 100
  - name: train
    num_bytes: 23268
    num_examples: 100
  download_size: 30667
  dataset_size: 69660
- config_name: ar
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2325660
    num_examples: 10000
  - name: test
    num_bytes: 2334636
    num_examples: 10000
  - name: train
    num_bytes: 4671613
    num_examples: 20000
  download_size: 2582112
  dataset_size: 9331909
- config_name: arc
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 15698
    num_examples: 100
  - name: test
    num_bytes: 16613
    num_examples: 100
  - name: train
    num_bytes: 18508
    num_examples: 100
  download_size: 22858
  dataset_size: 50819
- config_name: arz
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26581
    num_examples: 100
  - name: test
    num_bytes: 25635
    num_examples: 100
  - name: train
    num_bytes: 26347
    num_examples: 100
  download_size: 32301
  dataset_size: 78563
- config_name: as
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 25708
    num_examples: 100
  - name: test
    num_bytes: 23322
    num_examples: 100
  - name: train
    num_bytes: 24956
    num_examples: 100
  download_size: 30404
  dataset_size: 73986
- config_name: ast
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 217449
    num_examples: 1000
  - name: test
    num_bytes: 220846
    num_examples: 1000
  - name: train
    num_bytes: 228210
    num_examples: 1000
  download_size: 157002
  dataset_size: 666505
- config_name: ay
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 11656
    num_examples: 100
  - name: test
    num_bytes: 13351
    num_examples: 100
  - name: train
    num_bytes: 12568
    num_examples: 100
  download_size: 16901
  dataset_size: 37575
- config_name: az
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 272038
    num_examples: 1000
  - name: test
    num_bytes: 267907
    num_examples: 1000
  - name: train
    num_bytes: 2645524
    num_examples: 10000
  download_size: 931014
  dataset_size: 3185469
- config_name: ba
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 29234
    num_examples: 100
  - name: test
    num_bytes: 30474
    num_examples: 100
  - name: train
    num_bytes: 31095
    num_examples: 100
  download_size: 36848
  dataset_size: 90803
- config_name: bar
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17346
    num_examples: 100
  - name: test
    num_bytes: 17811
    num_examples: 100
  - name: train
    num_bytes: 16768
    num_examples: 100
  download_size: 21987
  dataset_size: 51925
- config_name: bat-smg
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26468
    num_examples: 100
  - name: test
    num_bytes: 26065
    num_examples: 100
  - name: train
    num_bytes: 24649
    num_examples: 100
  download_size: 31533
  dataset_size: 77182
- config_name: be
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 262014
    num_examples: 1000
  - name: test
    num_bytes: 266076
    num_examples: 1000
  - name: train
    num_bytes: 3983266
    num_examples: 15000
  download_size: 1283568
  dataset_size: 4511356
- config_name: be-x-old
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 342626
    num_examples: 1000
  - name: test
    num_bytes: 337571
    num_examples: 1000
  - name: train
    num_bytes: 1704228
    num_examples: 5000
  download_size: 586037
  dataset_size: 2384425
- config_name: bg
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2840879
    num_examples: 10000
  - name: test
    num_bytes: 2830185
    num_examples: 10000
  - name: train
    num_bytes: 5665007
    num_examples: 20000
  download_size: 3010319
  dataset_size: 11336071
- config_name: bh
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 33654
    num_examples: 100
  - name: test
    num_bytes: 30664
    num_examples: 100
  - name: train
    num_bytes: 36346
    num_examples: 100
  download_size: 34563
  dataset_size: 100664
- config_name: bn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 238418
    num_examples: 1000
  - name: test
    num_bytes: 237190
    num_examples: 1000
  - name: train
    num_bytes: 2351563
    num_examples: 10000
  download_size: 667399
  dataset_size: 2827171
- config_name: bo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22660
    num_examples: 100
  - name: test
    num_bytes: 15409
    num_examples: 100
  - name: train
    num_bytes: 14057
    num_examples: 100
  download_size: 26274
  dataset_size: 52126
- config_name: br
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 206811
    num_examples: 1000
  - name: test
    num_bytes: 222055
    num_examples: 1000
  - name: train
    num_bytes: 221467
    num_examples: 1000
  download_size: 193001
  dataset_size: 650333
- config_name: bs
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 246350
    num_examples: 1000
  - name: test
    num_bytes: 247303
    num_examples: 1000
  - name: train
    num_bytes: 3669290
    num_examples: 15000
  download_size: 1145992
  dataset_size: 4162943
- config_name: ca
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1836291
    num_examples: 10000
  - name: test
    num_bytes: 1847718
    num_examples: 10000
  - name: train
    num_bytes: 3689286
    num_examples: 20000
  download_size: 2392551
  dataset_size: 7373295
- config_name: cbk-zam
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 47032
    num_examples: 100
  - name: test
    num_bytes: 47249
    num_examples: 100
  - name: train
    num_bytes: 52517
    num_examples: 100
  download_size: 37209
  dataset_size: 146798
- config_name: cdo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 37451
    num_examples: 100
  - name: test
    num_bytes: 34291
    num_examples: 100
  - name: train
    num_bytes: 36176
    num_examples: 100
  download_size: 34997
  dataset_size: 107918
- config_name: ce
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 40275
    num_examples: 100
  - name: test
    num_bytes: 38612
    num_examples: 100
  - name: train
    num_bytes: 38256
    num_examples: 100
  download_size: 34386
  dataset_size: 117143
- config_name: ceb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22761
    num_examples: 100
  - name: test
    num_bytes: 23922
    num_examples: 100
  - name: train
    num_bytes: 21337
    num_examples: 100
  download_size: 27030
  dataset_size: 68020
- config_name: ckb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 214203
    num_examples: 1000
  - name: test
    num_bytes: 211960
    num_examples: 1000
  - name: train
    num_bytes: 217038
    num_examples: 1000
  download_size: 148534
  dataset_size: 643201
- config_name: co
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 15940
    num_examples: 100
  - name: test
    num_bytes: 15852
    num_examples: 100
  - name: train
    num_bytes: 18004
    num_examples: 100
  download_size: 25539
  dataset_size: 49796
- config_name: crh
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 20202
    num_examples: 100
  - name: test
    num_bytes: 23851
    num_examples: 100
  - name: train
    num_bytes: 23308
    num_examples: 100
  download_size: 29468
  dataset_size: 67361
- config_name: cs
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2456626
    num_examples: 10000
  - name: test
    num_bytes: 2458127
    num_examples: 10000
  - name: train
    num_bytes: 4944702
    num_examples: 20000
  download_size: 3028120
  dataset_size: 9859455
- config_name: csb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 28813
    num_examples: 100
  - name: test
    num_bytes: 27812
    num_examples: 100
  - name: train
    num_bytes: 31612
    num_examples: 100
  download_size: 35313
  dataset_size: 88237
- config_name: cv
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24759
    num_examples: 100
  - name: test
    num_bytes: 26375
    num_examples: 100
  - name: train
    num_bytes: 26928
    num_examples: 100
  download_size: 32018
  dataset_size: 78062
- config_name: cy
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 228558
    num_examples: 1000
  - name: test
    num_bytes: 233841
    num_examples: 1000
  - name: train
    num_bytes: 2337088
    num_examples: 10000
  download_size: 630636
  dataset_size: 2799487
- config_name: da
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2422948
    num_examples: 10000
  - name: test
    num_bytes: 2432296
    num_examples: 10000
  - name: train
    num_bytes: 4882166
    num_examples: 20000
  download_size: 2903455
  dataset_size: 9737410
- config_name: de
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2754522
    num_examples: 10000
  - name: test
    num_bytes: 2750968
    num_examples: 10000
  - name: train
    num_bytes: 5510585
    num_examples: 20000
  download_size: 3340116
  dataset_size: 11016075
- config_name: diq
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24119
    num_examples: 100
  - name: test
    num_bytes: 22448
    num_examples: 100
  - name: train
    num_bytes: 24103
    num_examples: 100
  download_size: 29511
  dataset_size: 70670
- config_name: dv
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 30294
    num_examples: 100
  - name: test
    num_bytes: 27251
    num_examples: 100
  - name: train
    num_bytes: 31005
    num_examples: 100
  download_size: 36181
  dataset_size: 88550
- config_name: el
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 3027934
    num_examples: 10000
  - name: test
    num_bytes: 3034301
    num_examples: 10000
  - name: train
    num_bytes: 6046582
    num_examples: 20000
  download_size: 3212871
  dataset_size: 12108817
- config_name: eml
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 30022
    num_examples: 100
  - name: test
    num_bytes: 35852
    num_examples: 100
  - name: train
    num_bytes: 30764
    num_examples: 100
  download_size: 35629
  dataset_size: 96638
- config_name: en
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2336325
    num_examples: 10000
  - name: test
    num_bytes: 2330217
    num_examples: 10000
  - name: train
    num_bytes: 4649545
    num_examples: 20000
  download_size: 2990984
  dataset_size: 9316087
- config_name: eo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1968662
    num_examples: 10000
  - name: test
    num_bytes: 1961458
    num_examples: 10000
  - name: train
    num_bytes: 2952554
    num_examples: 15000
  download_size: 2147812
  dataset_size: 6882674
- config_name: es
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1976907
    num_examples: 10000
  - name: test
    num_bytes: 1986636
    num_examples: 10000
  - name: train
    num_bytes: 3972236
    num_examples: 20000
  download_size: 2431958
  dataset_size: 7935779
- config_name: et
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2403333
    num_examples: 10000
  - name: test
    num_bytes: 2392396
    num_examples: 10000
  - name: train
    num_bytes: 3579208
    num_examples: 15000
  download_size: 2678718
  dataset_size: 8374937
- config_name: eu
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2677008
    num_examples: 10000
  - name: test
    num_bytes: 2628923
    num_examples: 10000
  - name: train
    num_bytes: 2672325
    num_examples: 10000
  download_size: 1985966
  dataset_size: 7978256
- config_name: ext
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 30793
    num_examples: 100
  - name: test
    num_bytes: 29455
    num_examples: 100
  - name: train
    num_bytes: 23082
    num_examples: 100
  download_size: 32111
  dataset_size: 83330
- config_name: fa
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2328612
    num_examples: 10000
  - name: test
    num_bytes: 2314659
    num_examples: 10000
  - name: train
    num_bytes: 4618042
    num_examples: 20000
  download_size: 2385463
  dataset_size: 9261313
- config_name: fi
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2500558
    num_examples: 10000
  - name: test
    num_bytes: 2505133
    num_examples: 10000
  - name: train
    num_bytes: 5020599
    num_examples: 20000
  download_size: 3407283
  dataset_size: 10026290
- config_name: fiu-vro
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 27644
    num_examples: 100
  - name: test
    num_bytes: 27700
    num_examples: 100
  - name: train
    num_bytes: 28661
    num_examples: 100
  download_size: 31399
  dataset_size: 84005
- config_name: fo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26066
    num_examples: 100
  - name: test
    num_bytes: 23503
    num_examples: 100
  - name: train
    num_bytes: 26150
    num_examples: 100
  download_size: 33699
  dataset_size: 75719
- config_name: fr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2057976
    num_examples: 10000
  - name: test
    num_bytes: 2073565
    num_examples: 10000
  - name: train
    num_bytes: 4123939
    num_examples: 20000
  download_size: 2694633
  dataset_size: 8255480
- config_name: frr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 15855
    num_examples: 100
  - name: test
    num_bytes: 15708
    num_examples: 100
  - name: train
    num_bytes: 16626
    num_examples: 100
  download_size: 25130
  dataset_size: 48189
- config_name: fur
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 25236
    num_examples: 100
  - name: test
    num_bytes: 30534
    num_examples: 100
  - name: train
    num_bytes: 33626
    num_examples: 100
  download_size: 32754
  dataset_size: 89396
- config_name: fy
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 226408
    num_examples: 1000
  - name: test
    num_bytes: 229672
    num_examples: 1000
  - name: train
    num_bytes: 222985
    num_examples: 1000
  download_size: 182402
  dataset_size: 679065
- config_name: ga
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 234064
    num_examples: 1000
  - name: test
    num_bytes: 235055
    num_examples: 1000
  - name: train
    num_bytes: 238019
    num_examples: 1000
  download_size: 198615
  dataset_size: 707138
- config_name: gan
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17505
    num_examples: 100
  - name: test
    num_bytes: 13851
    num_examples: 100
  - name: train
    num_bytes: 14370
    num_examples: 100
  download_size: 28600
  dataset_size: 45726
- config_name: gd
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 23202
    num_examples: 100
  - name: test
    num_bytes: 20280
    num_examples: 100
  - name: train
    num_bytes: 20126
    num_examples: 100
  download_size: 29305
  dataset_size: 63608
- config_name: gl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2029655
    num_examples: 10000
  - name: test
    num_bytes: 2031122
    num_examples: 10000
  - name: train
    num_bytes: 3030937
    num_examples: 15000
  download_size: 2045672
  dataset_size: 7091714
- config_name: gn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 29104
    num_examples: 100
  - name: test
    num_bytes: 24235
    num_examples: 100
  - name: train
    num_bytes: 28192
    num_examples: 100
  download_size: 35600
  dataset_size: 81531
- config_name: gu
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 47981
    num_examples: 100
  - name: test
    num_bytes: 45389
    num_examples: 100
  - name: train
    num_bytes: 42597
    num_examples: 100
  download_size: 44658
  dataset_size: 135967
- config_name: hak
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17949
    num_examples: 100
  - name: test
    num_bytes: 18127
    num_examples: 100
  - name: train
    num_bytes: 16180
    num_examples: 100
  download_size: 27841
  dataset_size: 52256
- config_name: he
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2801364
    num_examples: 10000
  - name: test
    num_bytes: 2785446
    num_examples: 10000
  - name: train
    num_bytes: 5600432
    num_examples: 20000
  download_size: 3112250
  dataset_size: 11187242
- config_name: hi
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 261179
    num_examples: 1000
  - name: test
    num_bytes: 267227
    num_examples: 1000
  - name: train
    num_bytes: 1315801
    num_examples: 5000
  download_size: 441664
  dataset_size: 1844207
- config_name: hr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2417422
    num_examples: 10000
  - name: test
    num_bytes: 2430412
    num_examples: 10000
  - name: train
    num_bytes: 4877275
    num_examples: 20000
  download_size: 2965267
  dataset_size: 9725109
- config_name: hsb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24667
    num_examples: 100
  - name: test
    num_bytes: 24320
    num_examples: 100
  - name: train
    num_bytes: 24200
    num_examples: 100
  download_size: 31799
  dataset_size: 73187
- config_name: hu
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2590088
    num_examples: 10000
  - name: test
    num_bytes: 2626743
    num_examples: 10000
  - name: train
    num_bytes: 5263066
    num_examples: 20000
  download_size: 3333477
  dataset_size: 10479897
- config_name: hy
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 237532
    num_examples: 1000
  - name: test
    num_bytes: 237093
    num_examples: 1000
  - name: train
    num_bytes: 3634009
    num_examples: 15000
  download_size: 1179988
  dataset_size: 4108634
- config_name: ia
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 32036
    num_examples: 100
  - name: test
    num_bytes: 37589
    num_examples: 100
  - name: train
    num_bytes: 32900
    num_examples: 100
  download_size: 38484
  dataset_size: 102525
- config_name: id
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1901597
    num_examples: 10000
  - name: test
    num_bytes: 1902704
    num_examples: 10000
  - name: train
    num_bytes: 3813991
    num_examples: 20000
  download_size: 2199732
  dataset_size: 7618292
- config_name: ig
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17693
    num_examples: 100
  - name: test
    num_bytes: 18404
    num_examples: 100
  - name: train
    num_bytes: 15960
    num_examples: 100
  download_size: 22605
  dataset_size: 52057
- config_name: ilo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 16647
    num_examples: 100
  - name: test
    num_bytes: 17217
    num_examples: 100
  - name: train
    num_bytes: 17124
    num_examples: 100
  download_size: 23906
  dataset_size: 50988
- config_name: io
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 18998
    num_examples: 100
  - name: test
    num_bytes: 17203
    num_examples: 100
  - name: train
    num_bytes: 20753
    num_examples: 100
  download_size: 27554
  dataset_size: 56954
- config_name: is
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 243639
    num_examples: 1000
  - name: test
    num_bytes: 235918
    num_examples: 1000
  - name: train
    num_bytes: 243437
    num_examples: 1000
  download_size: 210731
  dataset_size: 722994
- config_name: it
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2282919
    num_examples: 10000
  - name: test
    num_bytes: 2307590
    num_examples: 10000
  - name: train
    num_bytes: 4633519
    num_examples: 20000
  download_size: 2818124
  dataset_size: 9224028
- config_name: ja
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 6775580
    num_examples: 10000
  - name: test
    num_bytes: 6898510
    num_examples: 10000
  - name: train
    num_bytes: 13578269
    num_examples: 20000
  download_size: 3415775
  dataset_size: 27252359
- config_name: jbo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 15590
    num_examples: 100
  - name: test
    num_bytes: 19558
    num_examples: 100
  - name: train
    num_bytes: 15042
    num_examples: 100
  download_size: 22634
  dataset_size: 50190
- config_name: jv
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17663
    num_examples: 100
  - name: test
    num_bytes: 20175
    num_examples: 100
  - name: train
    num_bytes: 19381
    num_examples: 100
  download_size: 28541
  dataset_size: 57219
- config_name: ka
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 3454353
    num_examples: 10000
  - name: test
    num_bytes: 3480842
    num_examples: 10000
  - name: train
    num_bytes: 3427980
    num_examples: 10000
  download_size: 2588715
  dataset_size: 10363175
- config_name: kk
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 286474
    num_examples: 1000
  - name: test
    num_bytes: 284475
    num_examples: 1000
  - name: train
    num_bytes: 287924
    num_examples: 1000
  download_size: 217890
  dataset_size: 858873
- config_name: km
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 29282
    num_examples: 100
  - name: test
    num_bytes: 36073
    num_examples: 100
  - name: train
    num_bytes: 31910
    num_examples: 100
  download_size: 43075
  dataset_size: 97265
- config_name: kn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 36825
    num_examples: 100
  - name: test
    num_bytes: 32250
    num_examples: 100
  - name: train
    num_bytes: 34318
    num_examples: 100
  download_size: 43835
  dataset_size: 103393
- config_name: ko
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2553040
    num_examples: 10000
  - name: test
    num_bytes: 2547772
    num_examples: 10000
  - name: train
    num_bytes: 5107034
    num_examples: 20000
  download_size: 3536508
  dataset_size: 10207846
- config_name: ksh
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26310
    num_examples: 100
  - name: test
    num_bytes: 25221
    num_examples: 100
  - name: train
    num_bytes: 25913
    num_examples: 100
  download_size: 33350
  dataset_size: 77444
- config_name: ku
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22569
    num_examples: 100
  - name: test
    num_bytes: 20767
    num_examples: 100
  - name: train
    num_bytes: 22641
    num_examples: 100
  download_size: 30470
  dataset_size: 65977
- config_name: ky
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 30982
    num_examples: 100
  - name: test
    num_bytes: 31868
    num_examples: 100
  - name: train
    num_bytes: 32740
    num_examples: 100
  download_size: 41036
  dataset_size: 95590
- config_name: la
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 207177
    num_examples: 1000
  - name: test
    num_bytes: 198882
    num_examples: 1000
  - name: train
    num_bytes: 999022
    num_examples: 5000
  download_size: 367324
  dataset_size: 1405081
- config_name: lb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 253746
    num_examples: 1000
  - name: test
    num_bytes: 249961
    num_examples: 1000
  - name: train
    num_bytes: 1260911
    num_examples: 5000
  download_size: 477151
  dataset_size: 1764618
- config_name: li
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 20173
    num_examples: 100
  - name: test
    num_bytes: 18789
    num_examples: 100
  - name: train
    num_bytes: 20183
    num_examples: 100
  download_size: 28842
  dataset_size: 59145
- config_name: lij
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 27977
    num_examples: 100
  - name: test
    num_bytes: 27854
    num_examples: 100
  - name: train
    num_bytes: 30553
    num_examples: 100
  download_size: 33981
  dataset_size: 86384
- config_name: lmo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26547
    num_examples: 100
  - name: test
    num_bytes: 29425
    num_examples: 100
  - name: train
    num_bytes: 24133
    num_examples: 100
  download_size: 32492
  dataset_size: 80105
- config_name: ln
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21681
    num_examples: 100
  - name: test
    num_bytes: 26975
    num_examples: 100
  - name: train
    num_bytes: 22199
    num_examples: 100
  download_size: 28691
  dataset_size: 70855
- config_name: lt
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2192846
    num_examples: 10000
  - name: test
    num_bytes: 2191241
    num_examples: 10000
  - name: train
    num_bytes: 2199918
    num_examples: 10000
  download_size: 2138545
  dataset_size: 6584005
- config_name: lv
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2173392
    num_examples: 10000
  - name: test
    num_bytes: 2190430
    num_examples: 10000
  - name: train
    num_bytes: 2206915
    num_examples: 10000
  download_size: 2012494
  dataset_size: 6570737
- config_name: map-bms
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 19752
    num_examples: 100
  - name: test
    num_bytes: 20530
    num_examples: 100
  - name: train
    num_bytes: 21611
    num_examples: 100
  download_size: 25217
  dataset_size: 61893
- config_name: mg
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24833
    num_examples: 100
  - name: test
    num_bytes: 22542
    num_examples: 100
  - name: train
    num_bytes: 25711
    num_examples: 100
  download_size: 26980
  dataset_size: 73086
- config_name: mhr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 23235
    num_examples: 100
  - name: test
    num_bytes: 23611
    num_examples: 100
  - name: train
    num_bytes: 18620
    num_examples: 100
  download_size: 29844
  dataset_size: 65466
- config_name: mi
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 39371
    num_examples: 100
  - name: test
    num_bytes: 40119
    num_examples: 100
  - name: train
    num_bytes: 37868
    num_examples: 100
  download_size: 24626
  dataset_size: 117358
- config_name: min
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 28691
    num_examples: 100
  - name: test
    num_bytes: 24713
    num_examples: 100
  - name: train
    num_bytes: 26592
    num_examples: 100
  download_size: 31058
  dataset_size: 79996
- config_name: mk
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 333165
    num_examples: 1000
  - name: test
    num_bytes: 337729
    num_examples: 1000
  - name: train
    num_bytes: 3355908
    num_examples: 10000
  download_size: 825847
  dataset_size: 4026802
- config_name: ml
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 362980
    num_examples: 1000
  - name: test
    num_bytes: 349355
    num_examples: 1000
  - name: train
    num_bytes: 3582038
    num_examples: 10000
  download_size: 1190172
  dataset_size: 4294373
- config_name: mn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21978
    num_examples: 100
  - name: test
    num_bytes: 23510
    num_examples: 100
  - name: train
    num_bytes: 23216
    num_examples: 100
  download_size: 32990
  dataset_size: 68704
- config_name: mr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 314830
    num_examples: 1000
  - name: test
    num_bytes: 326262
    num_examples: 1000
  - name: train
    num_bytes: 1598776
    num_examples: 5000
  download_size: 524029
  dataset_size: 2239868
- config_name: ms
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 183916
    num_examples: 1000
  - name: test
    num_bytes: 183511
    num_examples: 1000
  - name: train
    num_bytes: 3699182
    num_examples: 20000
  download_size: 1077180
  dataset_size: 4066609
- config_name: mt
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24543
    num_examples: 100
  - name: test
    num_bytes: 24634
    num_examples: 100
  - name: train
    num_bytes: 24928
    num_examples: 100
  download_size: 33526
  dataset_size: 74105
- config_name: mwl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 51959
    num_examples: 100
  - name: test
    num_bytes: 42980
    num_examples: 100
  - name: train
    num_bytes: 44577
    num_examples: 100
  download_size: 44197
  dataset_size: 139516
- config_name: my
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 48925
    num_examples: 100
  - name: test
    num_bytes: 45928
    num_examples: 100
  - name: train
    num_bytes: 41343
    num_examples: 100
  download_size: 51490
  dataset_size: 136196
- config_name: mzn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 25276
    num_examples: 100
  - name: test
    num_bytes: 25919
    num_examples: 100
  - name: train
    num_bytes: 24813
    num_examples: 100
  download_size: 29895
  dataset_size: 76008
- config_name: nap
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21518
    num_examples: 100
  - name: test
    num_bytes: 24166
    num_examples: 100
  - name: train
    num_bytes: 26568
    num_examples: 100
  download_size: 30764
  dataset_size: 72252
- config_name: nds
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 28360
    num_examples: 100
  - name: test
    num_bytes: 26543
    num_examples: 100
  - name: train
    num_bytes: 24651
    num_examples: 100
  download_size: 33734
  dataset_size: 79554
- config_name: ne
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 33904
    num_examples: 100
  - name: test
    num_bytes: 33199
    num_examples: 100
  - name: train
    num_bytes: 36145
    num_examples: 100
  download_size: 37920
  dataset_size: 103248
- config_name: nl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2378052
    num_examples: 10000
  - name: test
    num_bytes: 2403048
    num_examples: 10000
  - name: train
    num_bytes: 4784233
    num_examples: 20000
  download_size: 2867129
  dataset_size: 9565333
- config_name: nn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 274112
    num_examples: 1000
  - name: test
    num_bytes: 269603
    num_examples: 1000
  - name: train
    num_bytes: 5436129
    num_examples: 20000
  download_size: 1644504
  dataset_size: 5979844
- config_name: 'no'
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2576641
    num_examples: 10000
  - name: test
    num_bytes: 2563531
    num_examples: 10000
  - name: train
    num_bytes: 5139492
    num_examples: 20000
  download_size: 3063453
  dataset_size: 10279664
- config_name: nov
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 14828
    num_examples: 100
  - name: test
    num_bytes: 14802
    num_examples: 100
  - name: train
    num_bytes: 17242
    num_examples: 100
  download_size: 20235
  dataset_size: 46872
- config_name: oc
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 20400
    num_examples: 100
  - name: test
    num_bytes: 18572
    num_examples: 100
  - name: train
    num_bytes: 19291
    num_examples: 100
  download_size: 29284
  dataset_size: 58263
- config_name: or
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 32103
    num_examples: 100
  - name: test
    num_bytes: 29480
    num_examples: 100
  - name: train
    num_bytes: 27794
    num_examples: 100
  download_size: 31116
  dataset_size: 89377
- config_name: os
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 26751
    num_examples: 100
  - name: test
    num_bytes: 25967
    num_examples: 100
  - name: train
    num_bytes: 26005
    num_examples: 100
  download_size: 32948
  dataset_size: 78723
- config_name: pa
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 25202
    num_examples: 100
  - name: test
    num_bytes: 23680
    num_examples: 100
  - name: train
    num_bytes: 24143
    num_examples: 100
  download_size: 31528
  dataset_size: 73025
- config_name: pdc
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24391
    num_examples: 100
  - name: test
    num_bytes: 24646
    num_examples: 100
  - name: train
    num_bytes: 23963
    num_examples: 100
  download_size: 28409
  dataset_size: 73000
- config_name: pl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2448296
    num_examples: 10000
  - name: test
    num_bytes: 2463755
    num_examples: 10000
  - name: train
    num_bytes: 4851471
    num_examples: 20000
  download_size: 3300030
  dataset_size: 9763522
- config_name: pms
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 28341
    num_examples: 100
  - name: test
    num_bytes: 23987
    num_examples: 100
  - name: train
    num_bytes: 27401
    num_examples: 100
  download_size: 34986
  dataset_size: 79729
- config_name: pnb
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 19042
    num_examples: 100
  - name: test
    num_bytes: 21178
    num_examples: 100
  - name: train
    num_bytes: 19476
    num_examples: 100
  download_size: 25001
  dataset_size: 59696
- config_name: ps
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 49873
    num_examples: 100
  - name: test
    num_bytes: 43593
    num_examples: 100
  - name: train
    num_bytes: 63473
    num_examples: 100
  download_size: 45676
  dataset_size: 156939
- config_name: pt
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1962117
    num_examples: 10000
  - name: test
    num_bytes: 1946701
    num_examples: 10000
  - name: train
    num_bytes: 3917397
    num_examples: 20000
  download_size: 2523476
  dataset_size: 7826215
- config_name: qu
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 18203
    num_examples: 100
  - name: test
    num_bytes: 17647
    num_examples: 100
  - name: train
    num_bytes: 16961
    num_examples: 100
  download_size: 26577
  dataset_size: 52811
- config_name: rm
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 32748
    num_examples: 100
  - name: test
    num_bytes: 35852
    num_examples: 100
  - name: train
    num_bytes: 30461
    num_examples: 100
  download_size: 38504
  dataset_size: 99061
- config_name: ro
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2063832
    num_examples: 10000
  - name: test
    num_bytes: 2060905
    num_examples: 10000
  - name: train
    num_bytes: 4179813
    num_examples: 20000
  download_size: 2533230
  dataset_size: 8304550
- config_name: ru
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2574518
    num_examples: 10000
  - name: test
    num_bytes: 2597220
    num_examples: 10000
  - name: train
    num_bytes: 5175609
    num_examples: 20000
  download_size: 3250185
  dataset_size: 10347347
- config_name: rw
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17971
    num_examples: 100
  - name: test
    num_bytes: 14417
    num_examples: 100
  - name: train
    num_bytes: 16750
    num_examples: 100
  download_size: 25845
  dataset_size: 49138
- config_name: sa
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 45693
    num_examples: 100
  - name: test
    num_bytes: 49181
    num_examples: 100
  - name: train
    num_bytes: 52476
    num_examples: 100
  download_size: 50112
  dataset_size: 147350
- config_name: sah
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 27847
    num_examples: 100
  - name: test
    num_bytes: 26825
    num_examples: 100
  - name: train
    num_bytes: 27013
    num_examples: 100
  download_size: 34322
  dataset_size: 81685
- config_name: scn
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 20077
    num_examples: 100
  - name: test
    num_bytes: 17356
    num_examples: 100
  - name: train
    num_bytes: 21004
    num_examples: 100
  download_size: 28158
  dataset_size: 58437
- config_name: sco
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22187
    num_examples: 100
  - name: test
    num_bytes: 21561
    num_examples: 100
  - name: train
    num_bytes: 20280
    num_examples: 100
  download_size: 30781
  dataset_size: 64028
- config_name: sd
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 51527
    num_examples: 100
  - name: test
    num_bytes: 38506
    num_examples: 100
  - name: train
    num_bytes: 56897
    num_examples: 100
  download_size: 44883
  dataset_size: 146930
- config_name: sh
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1789890
    num_examples: 10000
  - name: test
    num_bytes: 1791463
    num_examples: 10000
  - name: train
    num_bytes: 3583577
    num_examples: 20000
  download_size: 2027654
  dataset_size: 7164930
- config_name: si
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 30817
    num_examples: 100
  - name: test
    num_bytes: 29313
    num_examples: 100
  - name: train
    num_bytes: 31227
    num_examples: 100
  download_size: 33979
  dataset_size: 91357
- config_name: simple
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 247119
    num_examples: 1000
  - name: test
    num_bytes: 245330
    num_examples: 1000
  - name: train
    num_bytes: 4921860
    num_examples: 20000
  download_size: 1301730
  dataset_size: 5414309
- config_name: sk
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2342033
    num_examples: 10000
  - name: test
    num_bytes: 2334981
    num_examples: 10000
  - name: train
    num_bytes: 4701497
    num_examples: 20000
  download_size: 2944919
  dataset_size: 9378511
- config_name: sl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2090219
    num_examples: 10000
  - name: test
    num_bytes: 2133463
    num_examples: 10000
  - name: train
    num_bytes: 3158620
    num_examples: 15000
  download_size: 2146455
  dataset_size: 7382302
- config_name: so
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21836
    num_examples: 100
  - name: test
    num_bytes: 17191
    num_examples: 100
  - name: train
    num_bytes: 23752
    num_examples: 100
  download_size: 27097
  dataset_size: 62779
- config_name: sq
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 210860
    num_examples: 1000
  - name: test
    num_bytes: 209796
    num_examples: 1000
  - name: train
    num_bytes: 1052359
    num_examples: 5000
  download_size: 366247
  dataset_size: 1473015
- config_name: sr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2548362
    num_examples: 10000
  - name: test
    num_bytes: 2564803
    num_examples: 10000
  - name: train
    num_bytes: 5105513
    num_examples: 20000
  download_size: 2932854
  dataset_size: 10218678
- config_name: su
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22577
    num_examples: 100
  - name: test
    num_bytes: 21833
    num_examples: 100
  - name: train
    num_bytes: 20811
    num_examples: 100
  download_size: 30722
  dataset_size: 65221
- config_name: sv
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2678644
    num_examples: 10000
  - name: test
    num_bytes: 2719049
    num_examples: 10000
  - name: train
    num_bytes: 5395666
    num_examples: 20000
  download_size: 2565949
  dataset_size: 10793359
- config_name: sw
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 168791
    num_examples: 1000
  - name: test
    num_bytes: 172665
    num_examples: 1000
  - name: train
    num_bytes: 168721
    num_examples: 1000
  download_size: 135814
  dataset_size: 510177
- config_name: szl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 19369
    num_examples: 100
  - name: test
    num_bytes: 18939
    num_examples: 100
  - name: train
    num_bytes: 17618
    num_examples: 100
  download_size: 27450
  dataset_size: 55926
- config_name: ta
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 354929
    num_examples: 1000
  - name: test
    num_bytes: 357639
    num_examples: 1000
  - name: train
    num_bytes: 5275703
    num_examples: 15000
  download_size: 1527540
  dataset_size: 5988271
- config_name: te
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 356161
    num_examples: 1000
  - name: test
    num_bytes: 359752
    num_examples: 1000
  - name: train
    num_bytes: 358764
    num_examples: 1000
  download_size: 260846
  dataset_size: 1074677
- config_name: tg
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 27102
    num_examples: 100
  - name: test
    num_bytes: 28793
    num_examples: 100
  - name: train
    num_bytes: 27172
    num_examples: 100
  download_size: 33712
  dataset_size: 83067
- config_name: th
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 14189715
    num_examples: 10000
  - name: test
    num_bytes: 14505026
    num_examples: 10000
  - name: train
    num_bytes: 28968860
    num_examples: 20000
  download_size: 3962089
  dataset_size: 57663601
- config_name: tk
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 21583
    num_examples: 100
  - name: test
    num_bytes: 20274
    num_examples: 100
  - name: train
    num_bytes: 19493
    num_examples: 100
  download_size: 30395
  dataset_size: 61350
- config_name: tl
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 148654
    num_examples: 1000
  - name: test
    num_bytes: 152936
    num_examples: 1000
  - name: train
    num_bytes: 1518756
    num_examples: 10000
  download_size: 521471
  dataset_size: 1820346
- config_name: tr
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2280489
    num_examples: 10000
  - name: test
    num_bytes: 2276892
    num_examples: 10000
  - name: train
    num_bytes: 4501856
    num_examples: 20000
  download_size: 2907624
  dataset_size: 9059237
- config_name: tt
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 282507
    num_examples: 1000
  - name: test
    num_bytes: 282663
    num_examples: 1000
  - name: train
    num_bytes: 283364
    num_examples: 1000
  download_size: 174234
  dataset_size: 848534
- config_name: ug
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 35191
    num_examples: 100
  - name: test
    num_bytes: 31101
    num_examples: 100
  - name: train
    num_bytes: 26592
    num_examples: 100
  download_size: 38383
  dataset_size: 92884
- config_name: uk
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 2934869
    num_examples: 10000
  - name: test
    num_bytes: 2928172
    num_examples: 10000
  - name: train
    num_bytes: 5927970
    num_examples: 20000
  download_size: 3214083
  dataset_size: 11791011
- config_name: ur
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 203719
    num_examples: 1000
  - name: test
    num_bytes: 203110
    num_examples: 1000
  - name: train
    num_bytes: 4108651
    num_examples: 20000
  download_size: 1140630
  dataset_size: 4515480
- config_name: uz
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 184597
    num_examples: 1000
  - name: test
    num_bytes: 184685
    num_examples: 1000
  - name: train
    num_bytes: 186077
    num_examples: 1000
  download_size: 121267
  dataset_size: 555359
- config_name: vec
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 19307
    num_examples: 100
  - name: test
    num_bytes: 20226
    num_examples: 100
  - name: train
    num_bytes: 20409
    num_examples: 100
  download_size: 27538
  dataset_size: 59942
- config_name: vep
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22278
    num_examples: 100
  - name: test
    num_bytes: 21343
    num_examples: 100
  - name: train
    num_bytes: 21359
    num_examples: 100
  download_size: 29630
  dataset_size: 64980
- config_name: vi
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 1944828
    num_examples: 10000
  - name: test
    num_bytes: 1959996
    num_examples: 10000
  - name: train
    num_bytes: 3915888
    num_examples: 20000
  download_size: 2283112
  dataset_size: 7820712
- config_name: vls
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 27867
    num_examples: 100
  - name: test
    num_bytes: 26750
    num_examples: 100
  - name: train
    num_bytes: 26155
    num_examples: 100
  download_size: 33972
  dataset_size: 80772
- config_name: vo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 14357
    num_examples: 100
  - name: test
    num_bytes: 13973
    num_examples: 100
  - name: train
    num_bytes: 14414
    num_examples: 100
  download_size: 20368
  dataset_size: 42744
- config_name: wa
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 22465
    num_examples: 100
  - name: test
    num_bytes: 21553
    num_examples: 100
  - name: train
    num_bytes: 23044
    num_examples: 100
  download_size: 28716
  dataset_size: 67062
- config_name: war
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 16806
    num_examples: 100
  - name: test
    num_bytes: 19884
    num_examples: 100
  - name: train
    num_bytes: 18801
    num_examples: 100
  download_size: 26342
  dataset_size: 55491
- config_name: wuu
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 15095
    num_examples: 100
  - name: test
    num_bytes: 15039
    num_examples: 100
  - name: train
    num_bytes: 16988
    num_examples: 100
  download_size: 34843
  dataset_size: 47122
- config_name: xmf
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 39951
    num_examples: 100
  - name: test
    num_bytes: 36053
    num_examples: 100
  - name: train
    num_bytes: 31768
    num_examples: 100
  download_size: 38339
  dataset_size: 107772
- config_name: yi
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 25241
    num_examples: 100
  - name: test
    num_bytes: 24977
    num_examples: 100
  - name: train
    num_bytes: 27275
    num_examples: 100
  download_size: 30693
  dataset_size: 77493
- config_name: yo
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 17710
    num_examples: 100
  - name: test
    num_bytes: 17968
    num_examples: 100
  - name: train
    num_bytes: 18956
    num_examples: 100
  download_size: 26565
  dataset_size: 54634
- config_name: zea
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24888
    num_examples: 100
  - name: test
    num_bytes: 22969
    num_examples: 100
  - name: train
    num_bytes: 21224
    num_examples: 100
  download_size: 28533
  dataset_size: 69081
- config_name: zh
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 4839700
    num_examples: 10000
  - name: test
    num_bytes: 4709430
    num_examples: 10000
  - name: train
    num_bytes: 9524925
    num_examples: 20000
  download_size: 2896220
  dataset_size: 19074055
- config_name: zh-classical
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 59952
    num_examples: 100
  - name: test
    num_bytes: 65857
    num_examples: 100
  - name: train
    num_bytes: 56210
    num_examples: 100
  download_size: 31946
  dataset_size: 182019
- config_name: zh-min-nan
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 24505
    num_examples: 100
  - name: test
    num_bytes: 24298
    num_examples: 100
  - name: train
    num_bytes: 19330
    num_examples: 100
  download_size: 26515
  dataset_size: 68133
- config_name: zh-yue
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
  - name: spans
    sequence: string
  splits:
  - name: validation
    num_bytes: 4934130
    num_examples: 10000
  - name: test
    num_bytes: 4964001
    num_examples: 10000
  - name: train
    num_bytes: 9950573
    num_examples: 20000
  download_size: 2342825
  dataset_size: 19848704
configs:
- config_name: ace
  data_files:
  - split: validation
    path: ace/validation-*
  - split: test
    path: ace/test-*
  - split: train
    path: ace/train-*
- config_name: af
  data_files:
  - split: validation
    path: af/validation-*
  - split: test
    path: af/test-*
  - split: train
    path: af/train-*
- config_name: als
  data_files:
  - split: validation
    path: als/validation-*
  - split: test
    path: als/test-*
  - split: train
    path: als/train-*
- config_name: am
  data_files:
  - split: validation
    path: am/validation-*
  - split: test
    path: am/test-*
  - split: train
    path: am/train-*
- config_name: an
  data_files:
  - split: validation
    path: an/validation-*
  - split: test
    path: an/test-*
  - split: train
    path: an/train-*
- config_name: ang
  data_files:
  - split: validation
    path: ang/validation-*
  - split: test
    path: ang/test-*
  - split: train
    path: ang/train-*
- config_name: ar
  data_files:
  - split: validation
    path: ar/validation-*
  - split: test
    path: ar/test-*
  - split: train
    path: ar/train-*
- config_name: arc
  data_files:
  - split: validation
    path: arc/validation-*
  - split: test
    path: arc/test-*
  - split: train
    path: arc/train-*
- config_name: arz
  data_files:
  - split: validation
    path: arz/validation-*
  - split: test
    path: arz/test-*
  - split: train
    path: arz/train-*
- config_name: as
  data_files:
  - split: validation
    path: as/validation-*
  - split: test
    path: as/test-*
  - split: train
    path: as/train-*
- config_name: ast
  data_files:
  - split: validation
    path: ast/validation-*
  - split: test
    path: ast/test-*
  - split: train
    path: ast/train-*
- config_name: ay
  data_files:
  - split: validation
    path: ay/validation-*
  - split: test
    path: ay/test-*
  - split: train
    path: ay/train-*
- config_name: az
  data_files:
  - split: validation
    path: az/validation-*
  - split: test
    path: az/test-*
  - split: train
    path: az/train-*
- config_name: ba
  data_files:
  - split: validation
    path: ba/validation-*
  - split: test
    path: ba/test-*
  - split: train
    path: ba/train-*
- config_name: bar
  data_files:
  - split: validation
    path: bar/validation-*
  - split: test
    path: bar/test-*
  - split: train
    path: bar/train-*
- config_name: bat-smg
  data_files:
  - split: validation
    path: bat-smg/validation-*
  - split: test
    path: bat-smg/test-*
  - split: train
    path: bat-smg/train-*
- config_name: be
  data_files:
  - split: validation
    path: be/validation-*
  - split: test
    path: be/test-*
  - split: train
    path: be/train-*
- config_name: be-x-old
  data_files:
  - split: validation
    path: be-x-old/validation-*
  - split: test
    path: be-x-old/test-*
  - split: train
    path: be-x-old/train-*
- config_name: bg
  data_files:
  - split: validation
    path: bg/validation-*
  - split: test
    path: bg/test-*
  - split: train
    path: bg/train-*
- config_name: bh
  data_files:
  - split: validation
    path: bh/validation-*
  - split: test
    path: bh/test-*
  - split: train
    path: bh/train-*
- config_name: bn
  data_files:
  - split: validation
    path: bn/validation-*
  - split: test
    path: bn/test-*
  - split: train
    path: bn/train-*
- config_name: bo
  data_files:
  - split: validation
    path: bo/validation-*
  - split: test
    path: bo/test-*
  - split: train
    path: bo/train-*
- config_name: br
  data_files:
  - split: validation
    path: br/validation-*
  - split: test
    path: br/test-*
  - split: train
    path: br/train-*
- config_name: bs
  data_files:
  - split: validation
    path: bs/validation-*
  - split: test
    path: bs/test-*
  - split: train
    path: bs/train-*
- config_name: ca
  data_files:
  - split: validation
    path: ca/validation-*
  - split: test
    path: ca/test-*
  - split: train
    path: ca/train-*
- config_name: cbk-zam
  data_files:
  - split: validation
    path: cbk-zam/validation-*
  - split: test
    path: cbk-zam/test-*
  - split: train
    path: cbk-zam/train-*
- config_name: cdo
  data_files:
  - split: validation
    path: cdo/validation-*
  - split: test
    path: cdo/test-*
  - split: train
    path: cdo/train-*
- config_name: ce
  data_files:
  - split: validation
    path: ce/validation-*
  - split: test
    path: ce/test-*
  - split: train
    path: ce/train-*
- config_name: ceb
  data_files:
  - split: validation
    path: ceb/validation-*
  - split: test
    path: ceb/test-*
  - split: train
    path: ceb/train-*
- config_name: ckb
  data_files:
  - split: validation
    path: ckb/validation-*
  - split: test
    path: ckb/test-*
  - split: train
    path: ckb/train-*
- config_name: co
  data_files:
  - split: validation
    path: co/validation-*
  - split: test
    path: co/test-*
  - split: train
    path: co/train-*
- config_name: crh
  data_files:
  - split: validation
    path: crh/validation-*
  - split: test
    path: crh/test-*
  - split: train
    path: crh/train-*
- config_name: cs
  data_files:
  - split: validation
    path: cs/validation-*
  - split: test
    path: cs/test-*
  - split: train
    path: cs/train-*
- config_name: csb
  data_files:
  - split: validation
    path: csb/validation-*
  - split: test
    path: csb/test-*
  - split: train
    path: csb/train-*
- config_name: cv
  data_files:
  - split: validation
    path: cv/validation-*
  - split: test
    path: cv/test-*
  - split: train
    path: cv/train-*
- config_name: cy
  data_files:
  - split: validation
    path: cy/validation-*
  - split: test
    path: cy/test-*
  - split: train
    path: cy/train-*
- config_name: da
  data_files:
  - split: validation
    path: da/validation-*
  - split: test
    path: da/test-*
  - split: train
    path: da/train-*
- config_name: de
  data_files:
  - split: validation
    path: de/validation-*
  - split: test
    path: de/test-*
  - split: train
    path: de/train-*
- config_name: diq
  data_files:
  - split: validation
    path: diq/validation-*
  - split: test
    path: diq/test-*
  - split: train
    path: diq/train-*
- config_name: dv
  data_files:
  - split: validation
    path: dv/validation-*
  - split: test
    path: dv/test-*
  - split: train
    path: dv/train-*
- config_name: el
  data_files:
  - split: validation
    path: el/validation-*
  - split: test
    path: el/test-*
  - split: train
    path: el/train-*
- config_name: eml
  data_files:
  - split: validation
    path: eml/validation-*
  - split: test
    path: eml/test-*
  - split: train
    path: eml/train-*
- config_name: en
  data_files:
  - split: validation
    path: en/validation-*
  - split: test
    path: en/test-*
  - split: train
    path: en/train-*
- config_name: eo
  data_files:
  - split: validation
    path: eo/validation-*
  - split: test
    path: eo/test-*
  - split: train
    path: eo/train-*
- config_name: es
  data_files:
  - split: validation
    path: es/validation-*
  - split: test
    path: es/test-*
  - split: train
    path: es/train-*
- config_name: et
  data_files:
  - split: validation
    path: et/validation-*
  - split: test
    path: et/test-*
  - split: train
    path: et/train-*
- config_name: eu
  data_files:
  - split: validation
    path: eu/validation-*
  - split: test
    path: eu/test-*
  - split: train
    path: eu/train-*
- config_name: ext
  data_files:
  - split: validation
    path: ext/validation-*
  - split: test
    path: ext/test-*
  - split: train
    path: ext/train-*
- config_name: fa
  data_files:
  - split: validation
    path: fa/validation-*
  - split: test
    path: fa/test-*
  - split: train
    path: fa/train-*
- config_name: fi
  data_files:
  - split: validation
    path: fi/validation-*
  - split: test
    path: fi/test-*
  - split: train
    path: fi/train-*
- config_name: fiu-vro
  data_files:
  - split: validation
    path: fiu-vro/validation-*
  - split: test
    path: fiu-vro/test-*
  - split: train
    path: fiu-vro/train-*
- config_name: fo
  data_files:
  - split: validation
    path: fo/validation-*
  - split: test
    path: fo/test-*
  - split: train
    path: fo/train-*
- config_name: fr
  data_files:
  - split: validation
    path: fr/validation-*
  - split: test
    path: fr/test-*
  - split: train
    path: fr/train-*
- config_name: frr
  data_files:
  - split: validation
    path: frr/validation-*
  - split: test
    path: frr/test-*
  - split: train
    path: frr/train-*
- config_name: fur
  data_files:
  - split: validation
    path: fur/validation-*
  - split: test
    path: fur/test-*
  - split: train
    path: fur/train-*
- config_name: fy
  data_files:
  - split: validation
    path: fy/validation-*
  - split: test
    path: fy/test-*
  - split: train
    path: fy/train-*
- config_name: ga
  data_files:
  - split: validation
    path: ga/validation-*
  - split: test
    path: ga/test-*
  - split: train
    path: ga/train-*
- config_name: gan
  data_files:
  - split: validation
    path: gan/validation-*
  - split: test
    path: gan/test-*
  - split: train
    path: gan/train-*
- config_name: gd
  data_files:
  - split: validation
    path: gd/validation-*
  - split: test
    path: gd/test-*
  - split: train
    path: gd/train-*
- config_name: gl
  data_files:
  - split: validation
    path: gl/validation-*
  - split: test
    path: gl/test-*
  - split: train
    path: gl/train-*
- config_name: gn
  data_files:
  - split: validation
    path: gn/validation-*
  - split: test
    path: gn/test-*
  - split: train
    path: gn/train-*
- config_name: gu
  data_files:
  - split: validation
    path: gu/validation-*
  - split: test
    path: gu/test-*
  - split: train
    path: gu/train-*
- config_name: hak
  data_files:
  - split: validation
    path: hak/validation-*
  - split: test
    path: hak/test-*
  - split: train
    path: hak/train-*
- config_name: he
  data_files:
  - split: validation
    path: he/validation-*
  - split: test
    path: he/test-*
  - split: train
    path: he/train-*
- config_name: hi
  data_files:
  - split: validation
    path: hi/validation-*
  - split: test
    path: hi/test-*
  - split: train
    path: hi/train-*
- config_name: hr
  data_files:
  - split: validation
    path: hr/validation-*
  - split: test
    path: hr/test-*
  - split: train
    path: hr/train-*
- config_name: hsb
  data_files:
  - split: validation
    path: hsb/validation-*
  - split: test
    path: hsb/test-*
  - split: train
    path: hsb/train-*
- config_name: hu
  data_files:
  - split: validation
    path: hu/validation-*
  - split: test
    path: hu/test-*
  - split: train
    path: hu/train-*
- config_name: hy
  data_files:
  - split: validation
    path: hy/validation-*
  - split: test
    path: hy/test-*
  - split: train
    path: hy/train-*
- config_name: ia
  data_files:
  - split: validation
    path: ia/validation-*
  - split: test
    path: ia/test-*
  - split: train
    path: ia/train-*
- config_name: id
  data_files:
  - split: validation
    path: id/validation-*
  - split: test
    path: id/test-*
  - split: train
    path: id/train-*
- config_name: ig
  data_files:
  - split: validation
    path: ig/validation-*
  - split: test
    path: ig/test-*
  - split: train
    path: ig/train-*
- config_name: ilo
  data_files:
  - split: validation
    path: ilo/validation-*
  - split: test
    path: ilo/test-*
  - split: train
    path: ilo/train-*
- config_name: io
  data_files:
  - split: validation
    path: io/validation-*
  - split: test
    path: io/test-*
  - split: train
    path: io/train-*
- config_name: is
  data_files:
  - split: validation
    path: is/validation-*
  - split: test
    path: is/test-*
  - split: train
    path: is/train-*
- config_name: it
  data_files:
  - split: validation
    path: it/validation-*
  - split: test
    path: it/test-*
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: validation
    path: ja/validation-*
  - split: test
    path: ja/test-*
  - split: train
    path: ja/train-*
- config_name: jbo
  data_files:
  - split: validation
    path: jbo/validation-*
  - split: test
    path: jbo/test-*
  - split: train
    path: jbo/train-*
- config_name: jv
  data_files:
  - split: validation
    path: jv/validation-*
  - split: test
    path: jv/test-*
  - split: train
    path: jv/train-*
- config_name: ka
  data_files:
  - split: validation
    path: ka/validation-*
  - split: test
    path: ka/test-*
  - split: train
    path: ka/train-*
- config_name: kk
  data_files:
  - split: validation
    path: kk/validation-*
  - split: test
    path: kk/test-*
  - split: train
    path: kk/train-*
- config_name: km
  data_files:
  - split: validation
    path: km/validation-*
  - split: test
    path: km/test-*
  - split: train
    path: km/train-*
- config_name: kn
  data_files:
  - split: validation
    path: kn/validation-*
  - split: test
    path: kn/test-*
  - split: train
    path: kn/train-*
- config_name: ko
  data_files:
  - split: validation
    path: ko/validation-*
  - split: test
    path: ko/test-*
  - split: train
    path: ko/train-*
- config_name: ksh
  data_files:
  - split: validation
    path: ksh/validation-*
  - split: test
    path: ksh/test-*
  - split: train
    path: ksh/train-*
- config_name: ku
  data_files:
  - split: validation
    path: ku/validation-*
  - split: test
    path: ku/test-*
  - split: train
    path: ku/train-*
- config_name: ky
  data_files:
  - split: validation
    path: ky/validation-*
  - split: test
    path: ky/test-*
  - split: train
    path: ky/train-*
- config_name: la
  data_files:
  - split: validation
    path: la/validation-*
  - split: test
    path: la/test-*
  - split: train
    path: la/train-*
- config_name: lb
  data_files:
  - split: validation
    path: lb/validation-*
  - split: test
    path: lb/test-*
  - split: train
    path: lb/train-*
- config_name: li
  data_files:
  - split: validation
    path: li/validation-*
  - split: test
    path: li/test-*
  - split: train
    path: li/train-*
- config_name: lij
  data_files:
  - split: validation
    path: lij/validation-*
  - split: test
    path: lij/test-*
  - split: train
    path: lij/train-*
- config_name: lmo
  data_files:
  - split: validation
    path: lmo/validation-*
  - split: test
    path: lmo/test-*
  - split: train
    path: lmo/train-*
- config_name: ln
  data_files:
  - split: validation
    path: ln/validation-*
  - split: test
    path: ln/test-*
  - split: train
    path: ln/train-*
- config_name: lt
  data_files:
  - split: validation
    path: lt/validation-*
  - split: test
    path: lt/test-*
  - split: train
    path: lt/train-*
- config_name: lv
  data_files:
  - split: validation
    path: lv/validation-*
  - split: test
    path: lv/test-*
  - split: train
    path: lv/train-*
- config_name: map-bms
  data_files:
  - split: validation
    path: map-bms/validation-*
  - split: test
    path: map-bms/test-*
  - split: train
    path: map-bms/train-*
- config_name: mg
  data_files:
  - split: validation
    path: mg/validation-*
  - split: test
    path: mg/test-*
  - split: train
    path: mg/train-*
- config_name: mhr
  data_files:
  - split: validation
    path: mhr/validation-*
  - split: test
    path: mhr/test-*
  - split: train
    path: mhr/train-*
- config_name: mi
  data_files:
  - split: validation
    path: mi/validation-*
  - split: test
    path: mi/test-*
  - split: train
    path: mi/train-*
- config_name: min
  data_files:
  - split: validation
    path: min/validation-*
  - split: test
    path: min/test-*
  - split: train
    path: min/train-*
- config_name: mk
  data_files:
  - split: validation
    path: mk/validation-*
  - split: test
    path: mk/test-*
  - split: train
    path: mk/train-*
- config_name: ml
  data_files:
  - split: validation
    path: ml/validation-*
  - split: test
    path: ml/test-*
  - split: train
    path: ml/train-*
- config_name: mn
  data_files:
  - split: validation
    path: mn/validation-*
  - split: test
    path: mn/test-*
  - split: train
    path: mn/train-*
- config_name: mr
  data_files:
  - split: validation
    path: mr/validation-*
  - split: test
    path: mr/test-*
  - split: train
    path: mr/train-*
- config_name: ms
  data_files:
  - split: validation
    path: ms/validation-*
  - split: test
    path: ms/test-*
  - split: train
    path: ms/train-*
- config_name: mt
  data_files:
  - split: validation
    path: mt/validation-*
  - split: test
    path: mt/test-*
  - split: train
    path: mt/train-*
- config_name: mwl
  data_files:
  - split: validation
    path: mwl/validation-*
  - split: test
    path: mwl/test-*
  - split: train
    path: mwl/train-*
- config_name: my
  data_files:
  - split: validation
    path: my/validation-*
  - split: test
    path: my/test-*
  - split: train
    path: my/train-*
- config_name: mzn
  data_files:
  - split: validation
    path: mzn/validation-*
  - split: test
    path: mzn/test-*
  - split: train
    path: mzn/train-*
- config_name: nap
  data_files:
  - split: validation
    path: nap/validation-*
  - split: test
    path: nap/test-*
  - split: train
    path: nap/train-*
- config_name: nds
  data_files:
  - split: validation
    path: nds/validation-*
  - split: test
    path: nds/test-*
  - split: train
    path: nds/train-*
- config_name: ne
  data_files:
  - split: validation
    path: ne/validation-*
  - split: test
    path: ne/test-*
  - split: train
    path: ne/train-*
- config_name: nl
  data_files:
  - split: validation
    path: nl/validation-*
  - split: test
    path: nl/test-*
  - split: train
    path: nl/train-*
- config_name: nn
  data_files:
  - split: validation
    path: nn/validation-*
  - split: test
    path: nn/test-*
  - split: train
    path: nn/train-*
- config_name: 'no'
  data_files:
  - split: validation
    path: no/validation-*
  - split: test
    path: no/test-*
  - split: train
    path: no/train-*
- config_name: nov
  data_files:
  - split: validation
    path: nov/validation-*
  - split: test
    path: nov/test-*
  - split: train
    path: nov/train-*
- config_name: oc
  data_files:
  - split: validation
    path: oc/validation-*
  - split: test
    path: oc/test-*
  - split: train
    path: oc/train-*
- config_name: or
  data_files:
  - split: validation
    path: or/validation-*
  - split: test
    path: or/test-*
  - split: train
    path: or/train-*
- config_name: os
  data_files:
  - split: validation
    path: os/validation-*
  - split: test
    path: os/test-*
  - split: train
    path: os/train-*
- config_name: pa
  data_files:
  - split: validation
    path: pa/validation-*
  - split: test
    path: pa/test-*
  - split: train
    path: pa/train-*
- config_name: pdc
  data_files:
  - split: validation
    path: pdc/validation-*
  - split: test
    path: pdc/test-*
  - split: train
    path: pdc/train-*
- config_name: pl
  data_files:
  - split: validation
    path: pl/validation-*
  - split: test
    path: pl/test-*
  - split: train
    path: pl/train-*
- config_name: pms
  data_files:
  - split: validation
    path: pms/validation-*
  - split: test
    path: pms/test-*
  - split: train
    path: pms/train-*
- config_name: pnb
  data_files:
  - split: validation
    path: pnb/validation-*
  - split: test
    path: pnb/test-*
  - split: train
    path: pnb/train-*
- config_name: ps
  data_files:
  - split: validation
    path: ps/validation-*
  - split: test
    path: ps/test-*
  - split: train
    path: ps/train-*
- config_name: pt
  data_files:
  - split: validation
    path: pt/validation-*
  - split: test
    path: pt/test-*
  - split: train
    path: pt/train-*
- config_name: qu
  data_files:
  - split: validation
    path: qu/validation-*
  - split: test
    path: qu/test-*
  - split: train
    path: qu/train-*
- config_name: rm
  data_files:
  - split: validation
    path: rm/validation-*
  - split: test
    path: rm/test-*
  - split: train
    path: rm/train-*
- config_name: ro
  data_files:
  - split: validation
    path: ro/validation-*
  - split: test
    path: ro/test-*
  - split: train
    path: ro/train-*
- config_name: ru
  data_files:
  - split: validation
    path: ru/validation-*
  - split: test
    path: ru/test-*
  - split: train
    path: ru/train-*
- config_name: rw
  data_files:
  - split: validation
    path: rw/validation-*
  - split: test
    path: rw/test-*
  - split: train
    path: rw/train-*
- config_name: sa
  data_files:
  - split: validation
    path: sa/validation-*
  - split: test
    path: sa/test-*
  - split: train
    path: sa/train-*
- config_name: sah
  data_files:
  - split: validation
    path: sah/validation-*
  - split: test
    path: sah/test-*
  - split: train
    path: sah/train-*
- config_name: scn
  data_files:
  - split: validation
    path: scn/validation-*
  - split: test
    path: scn/test-*
  - split: train
    path: scn/train-*
- config_name: sco
  data_files:
  - split: validation
    path: sco/validation-*
  - split: test
    path: sco/test-*
  - split: train
    path: sco/train-*
- config_name: sd
  data_files:
  - split: validation
    path: sd/validation-*
  - split: test
    path: sd/test-*
  - split: train
    path: sd/train-*
- config_name: sh
  data_files:
  - split: validation
    path: sh/validation-*
  - split: test
    path: sh/test-*
  - split: train
    path: sh/train-*
- config_name: si
  data_files:
  - split: validation
    path: si/validation-*
  - split: test
    path: si/test-*
  - split: train
    path: si/train-*
- config_name: simple
  data_files:
  - split: validation
    path: simple/validation-*
  - split: test
    path: simple/test-*
  - split: train
    path: simple/train-*
- config_name: sk
  data_files:
  - split: validation
    path: sk/validation-*
  - split: test
    path: sk/test-*
  - split: train
    path: sk/train-*
- config_name: sl
  data_files:
  - split: validation
    path: sl/validation-*
  - split: test
    path: sl/test-*
  - split: train
    path: sl/train-*
- config_name: so
  data_files:
  - split: validation
    path: so/validation-*
  - split: test
    path: so/test-*
  - split: train
    path: so/train-*
- config_name: sq
  data_files:
  - split: validation
    path: sq/validation-*
  - split: test
    path: sq/test-*
  - split: train
    path: sq/train-*
- config_name: sr
  data_files:
  - split: validation
    path: sr/validation-*
  - split: test
    path: sr/test-*
  - split: train
    path: sr/train-*
- config_name: su
  data_files:
  - split: validation
    path: su/validation-*
  - split: test
    path: su/test-*
  - split: train
    path: su/train-*
- config_name: sv
  data_files:
  - split: validation
    path: sv/validation-*
  - split: test
    path: sv/test-*
  - split: train
    path: sv/train-*
- config_name: sw
  data_files:
  - split: validation
    path: sw/validation-*
  - split: test
    path: sw/test-*
  - split: train
    path: sw/train-*
- config_name: szl
  data_files:
  - split: validation
    path: szl/validation-*
  - split: test
    path: szl/test-*
  - split: train
    path: szl/train-*
- config_name: ta
  data_files:
  - split: validation
    path: ta/validation-*
  - split: test
    path: ta/test-*
  - split: train
    path: ta/train-*
- config_name: te
  data_files:
  - split: validation
    path: te/validation-*
  - split: test
    path: te/test-*
  - split: train
    path: te/train-*
- config_name: tg
  data_files:
  - split: validation
    path: tg/validation-*
  - split: test
    path: tg/test-*
  - split: train
    path: tg/train-*
- config_name: th
  data_files:
  - split: validation
    path: th/validation-*
  - split: test
    path: th/test-*
  - split: train
    path: th/train-*
- config_name: tk
  data_files:
  - split: validation
    path: tk/validation-*
  - split: test
    path: tk/test-*
  - split: train
    path: tk/train-*
- config_name: tl
  data_files:
  - split: validation
    path: tl/validation-*
  - split: test
    path: tl/test-*
  - split: train
    path: tl/train-*
- config_name: tr
  data_files:
  - split: validation
    path: tr/validation-*
  - split: test
    path: tr/test-*
  - split: train
    path: tr/train-*
- config_name: tt
  data_files:
  - split: validation
    path: tt/validation-*
  - split: test
    path: tt/test-*
  - split: train
    path: tt/train-*
- config_name: ug
  data_files:
  - split: validation
    path: ug/validation-*
  - split: test
    path: ug/test-*
  - split: train
    path: ug/train-*
- config_name: uk
  data_files:
  - split: validation
    path: uk/validation-*
  - split: test
    path: uk/test-*
  - split: train
    path: uk/train-*
- config_name: ur
  data_files:
  - split: validation
    path: ur/validation-*
  - split: test
    path: ur/test-*
  - split: train
    path: ur/train-*
- config_name: uz
  data_files:
  - split: validation
    path: uz/validation-*
  - split: test
    path: uz/test-*
  - split: train
    path: uz/train-*
- config_name: vec
  data_files:
  - split: validation
    path: vec/validation-*
  - split: test
    path: vec/test-*
  - split: train
    path: vec/train-*
- config_name: vep
  data_files:
  - split: validation
    path: vep/validation-*
  - split: test
    path: vep/test-*
  - split: train
    path: vep/train-*
- config_name: vi
  data_files:
  - split: validation
    path: vi/validation-*
  - split: test
    path: vi/test-*
  - split: train
    path: vi/train-*
- config_name: vls
  data_files:
  - split: validation
    path: vls/validation-*
  - split: test
    path: vls/test-*
  - split: train
    path: vls/train-*
- config_name: vo
  data_files:
  - split: validation
    path: vo/validation-*
  - split: test
    path: vo/test-*
  - split: train
    path: vo/train-*
- config_name: wa
  data_files:
  - split: validation
    path: wa/validation-*
  - split: test
    path: wa/test-*
  - split: train
    path: wa/train-*
- config_name: war
  data_files:
  - split: validation
    path: war/validation-*
  - split: test
    path: war/test-*
  - split: train
    path: war/train-*
- config_name: wuu
  data_files:
  - split: validation
    path: wuu/validation-*
  - split: test
    path: wuu/test-*
  - split: train
    path: wuu/train-*
- config_name: xmf
  data_files:
  - split: validation
    path: xmf/validation-*
  - split: test
    path: xmf/test-*
  - split: train
    path: xmf/train-*
- config_name: yi
  data_files:
  - split: validation
    path: yi/validation-*
  - split: test
    path: yi/test-*
  - split: train
    path: yi/train-*
- config_name: yo
  data_files:
  - split: validation
    path: yo/validation-*
  - split: test
    path: yo/test-*
  - split: train
    path: yo/train-*
- config_name: zea
  data_files:
  - split: validation
    path: zea/validation-*
  - split: test
    path: zea/test-*
  - split: train
    path: zea/train-*
- config_name: zh
  data_files:
  - split: validation
    path: zh/validation-*
  - split: test
    path: zh/test-*
  - split: train
    path: zh/train-*
- config_name: zh-classical
  data_files:
  - split: validation
    path: zh-classical/validation-*
  - split: test
    path: zh-classical/test-*
  - split: train
    path: zh-classical/train-*
- config_name: zh-min-nan
  data_files:
  - split: validation
    path: zh-min-nan/validation-*
  - split: test
    path: zh-min-nan/test-*
  - split: train
    path: zh-min-nan/train-*
- config_name: zh-yue
  data_files:
  - split: validation
    path: zh-yue/validation-*
  - split: test
    path: zh-yue/test-*
  - split: train
    path: zh-yue/train-*
---

# Dataset Card for WikiANN

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

- **Homepage:** [Massively Multilingual Transfer for NER](https://github.com/afshinrahimi/mmner)
- **Repository:** [Massively Multilingual Transfer for NER](https://github.com/afshinrahimi/mmner)
- **Paper:** The original datasets come from the _Cross-lingual name tagging and linking for 282 languages_ [paper](https://www.aclweb.org/anthology/P17-1178/) by Xiaoman Pan et al. (2018). This version corresponds to the balanced train, dev, and test splits of the original data from the _Massively Multilingual Transfer for NER_ [paper](https://arxiv.org/abs/1902.00193) by Afshin Rahimi et al. (2019).
- **Leaderboard:**
- **Point of Contact:** [Afshin Rahimi](mailto:afshinrahimi@gmail.com) or [Lewis Tunstall](mailto:lewis.c.tunstall@gmail.com) or [Albert Villanova del Moral](albert@huggingface.co)

### Dataset Summary

WikiANN (sometimes called PAN-X) is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format. This version corresponds to the balanced train, dev, and test splits of Rahimi et al. (2019), which supports 176 of the 282 languages from the original WikiANN corpus.

### Supported Tasks and Leaderboards

- `named-entity-recognition`: The dataset can be used to train a model for named entity recognition in many languages, or evaluate the zero-shot cross-lingual capabilities of multilingual models.

### Languages

The dataset contains 176 languages, one in each of the configuration subsets. The corresponding BCP 47 language tags
are:

|                    | Language tag   |
|:-------------------|:---------------|
| ace                | ace            |
| af                 | af             |
| als                | als            |
| am                 | am             |
| an                 | an             |
| ang                | ang            |
| ar                 | ar             |
| arc                | arc            |
| arz                | arz            |
| as                 | as             |
| ast                | ast            |
| ay                 | ay             |
| az                 | az             |
| ba                 | ba             |
| bar                | bar            |
| be                 | be             |
| bg                 | bg             |
| bh                 | bh             |
| bn                 | bn             |
| bo                 | bo             |
| br                 | br             |
| bs                 | bs             |
| ca                 | ca             |
| cdo                | cdo            |
| ce                 | ce             |
| ceb                | ceb            |
| ckb                | ckb            |
| co                 | co             |
| crh                | crh            |
| cs                 | cs             |
| csb                | csb            |
| cv                 | cv             |
| cy                 | cy             |
| da                 | da             |
| de                 | de             |
| diq                | diq            |
| dv                 | dv             |
| el                 | el             |
| en                 | en             |
| eo                 | eo             |
| es                 | es             |
| et                 | et             |
| eu                 | eu             |
| ext                | ext            |
| fa                 | fa             |
| fi                 | fi             |
| fo                 | fo             |
| fr                 | fr             |
| frr                | frr            |
| fur                | fur            |
| fy                 | fy             |
| ga                 | ga             |
| gan                | gan            |
| gd                 | gd             |
| gl                 | gl             |
| gn                 | gn             |
| gu                 | gu             |
| hak                | hak            |
| he                 | he             |
| hi                 | hi             |
| hr                 | hr             |
| hsb                | hsb            |
| hu                 | hu             |
| hy                 | hy             |
| ia                 | ia             |
| id                 | id             |
| ig                 | ig             |
| ilo                | ilo            |
| io                 | io             |
| is                 | is             |
| it                 | it             |
| ja                 | ja             |
| jbo                | jbo            |
| jv                 | jv             |
| ka                 | ka             |
| kk                 | kk             |
| km                 | km             |
| kn                 | kn             |
| ko                 | ko             |
| ksh                | ksh            |
| ku                 | ku             |
| ky                 | ky             |
| la                 | la             |
| lb                 | lb             |
| li                 | li             |
| lij                | lij            |
| lmo                | lmo            |
| ln                 | ln             |
| lt                 | lt             |
| lv                 | lv             |
| mg                 | mg             |
| mhr                | mhr            |
| mi                 | mi             |
| min                | min            |
| mk                 | mk             |
| ml                 | ml             |
| mn                 | mn             |
| mr                 | mr             |
| ms                 | ms             |
| mt                 | mt             |
| mwl                | mwl            |
| my                 | my             |
| mzn                | mzn            |
| nap                | nap            |
| nds                | nds            |
| ne                 | ne             |
| nl                 | nl             |
| nn                 | nn             |
| no                 | no             |
| nov                | nov            |
| oc                 | oc             |
| or                 | or             |
| os                 | os             |
| other-bat-smg      | sgs            |
| other-be-x-old     | be-tarask      |
| other-cbk-zam      | cbk            |
| other-eml          | eml            |
| other-fiu-vro      | vro            |
| other-map-bms      | jv-x-bms       |
| other-simple       | en-basiceng    |
| other-zh-classical | lzh            |
| other-zh-min-nan   | nan            |
| other-zh-yue       | yue            |
| pa                 | pa             |
| pdc                | pdc            |
| pl                 | pl             |
| pms                | pms            |
| pnb                | pnb            |
| ps                 | ps             |
| pt                 | pt             |
| qu                 | qu             |
| rm                 | rm             |
| ro                 | ro             |
| ru                 | ru             |
| rw                 | rw             |
| sa                 | sa             |
| sah                | sah            |
| scn                | scn            |
| sco                | sco            |
| sd                 | sd             |
| sh                 | sh             |
| si                 | si             |
| sk                 | sk             |
| sl                 | sl             |
| so                 | so             |
| sq                 | sq             |
| sr                 | sr             |
| su                 | su             |
| sv                 | sv             |
| sw                 | sw             |
| szl                | szl            |
| ta                 | ta             |
| te                 | te             |
| tg                 | tg             |
| th                 | th             |
| tk                 | tk             |
| tl                 | tl             |
| tr                 | tr             |
| tt                 | tt             |
| ug                 | ug             |
| uk                 | uk             |
| ur                 | ur             |
| uz                 | uz             |
| vec                | vec            |
| vep                | vep            |
| vi                 | vi             |
| vls                | vls            |
| vo                 | vo             |
| wa                 | wa             |
| war                | war            |
| wuu                | wuu            |
| xmf                | xmf            |
| yi                 | yi             |
| yo                 | yo             |
| zea                | zea            |
| zh                 | zh             |

## Dataset Structure

### Data Instances

This is an example in the "train" split of the "af" (Afrikaans language) configuration subset:
```python
{
  'tokens': ['Sy', 'ander', 'seun', ',', 'Swjatopolk', ',', 'was', 'die', 'resultaat', 'van', '’n', 'buite-egtelike', 'verhouding', '.'],
  'ner_tags': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  'langs': ['af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af', 'af'],
  'spans': ['PER: Swjatopolk']
}
```

### Data Fields

- `tokens`: a `list` of `string` features.
- `langs`: a `list` of `string` features that correspond to the language of each token.
- `ner_tags`: a `list` of classification labels, with possible values including `O` (0), `B-PER` (1), `I-PER` (2), `B-ORG` (3), `I-ORG` (4), `B-LOC` (5), `I-LOC` (6).
- `spans`: a `list` of `string` features, that is the list of named entities in the input text formatted as ``<TAG>: <mention>``

### Data Splits

For each configuration subset, the data is split into "train", "validation" and "test" sets, each containing the
following number of examples:

|              |   Train |   Validation |   Test |
|:-------------|--------:|-------------:|-------:|
| ace          |     100 |          100 |    100 |
| af           |    5000 |         1000 |   1000 |
| als          |     100 |          100 |    100 |
| am           |     100 |          100 |    100 |
| an           |    1000 |         1000 |   1000 |
| ang          |     100 |          100 |    100 |
| ar           |   20000 |        10000 |  10000 |
| arc          |     100 |          100 |    100 |
| arz          |     100 |          100 |    100 |
| as           |     100 |          100 |    100 |
| ast          |    1000 |         1000 |   1000 |
| ay           |     100 |          100 |    100 |
| az           |   10000 |         1000 |   1000 |
| ba           |     100 |          100 |    100 |
| bar          |     100 |          100 |    100 |
| bat-smg      |     100 |          100 |    100 |
| be           |   15000 |         1000 |   1000 |
| be-x-old     |    5000 |         1000 |   1000 |
| bg           |   20000 |        10000 |  10000 |
| bh           |     100 |          100 |    100 |
| bn           |   10000 |         1000 |   1000 |
| bo           |     100 |          100 |    100 |
| br           |    1000 |         1000 |   1000 |
| bs           |   15000 |         1000 |   1000 |
| ca           |   20000 |        10000 |  10000 |
| cbk-zam      |     100 |          100 |    100 |
| cdo          |     100 |          100 |    100 |
| ce           |     100 |          100 |    100 |
| ceb          |     100 |          100 |    100 |
| ckb          |    1000 |         1000 |   1000 |
| co           |     100 |          100 |    100 |
| crh          |     100 |          100 |    100 |
| cs           |   20000 |        10000 |  10000 |
| csb          |     100 |          100 |    100 |
| cv           |     100 |          100 |    100 |
| cy           |   10000 |         1000 |   1000 |
| da           |   20000 |        10000 |  10000 |
| de           |   20000 |        10000 |  10000 |
| diq          |     100 |          100 |    100 |
| dv           |     100 |          100 |    100 |
| el           |   20000 |        10000 |  10000 |
| eml          |     100 |          100 |    100 |
| en           |   20000 |        10000 |  10000 |
| eo           |   15000 |        10000 |  10000 |
| es           |   20000 |        10000 |  10000 |
| et           |   15000 |        10000 |  10000 |
| eu           |   10000 |        10000 |  10000 |
| ext          |     100 |          100 |    100 |
| fa           |   20000 |        10000 |  10000 |
| fi           |   20000 |        10000 |  10000 |
| fiu-vro      |     100 |          100 |    100 |
| fo           |     100 |          100 |    100 |
| fr           |   20000 |        10000 |  10000 |
| frr          |     100 |          100 |    100 |
| fur          |     100 |          100 |    100 |
| fy           |    1000 |         1000 |   1000 |
| ga           |    1000 |         1000 |   1000 |
| gan          |     100 |          100 |    100 |
| gd           |     100 |          100 |    100 |
| gl           |   15000 |        10000 |  10000 |
| gn           |     100 |          100 |    100 |
| gu           |     100 |          100 |    100 |
| hak          |     100 |          100 |    100 |
| he           |   20000 |        10000 |  10000 |
| hi           |    5000 |         1000 |   1000 |
| hr           |   20000 |        10000 |  10000 |
| hsb          |     100 |          100 |    100 |
| hu           |   20000 |        10000 |  10000 |
| hy           |   15000 |         1000 |   1000 |
| ia           |     100 |          100 |    100 |
| id           |   20000 |        10000 |  10000 |
| ig           |     100 |          100 |    100 |
| ilo          |     100 |          100 |    100 |
| io           |     100 |          100 |    100 |
| is           |    1000 |         1000 |   1000 |
| it           |   20000 |        10000 |  10000 |
| ja           |   20000 |        10000 |  10000 |
| jbo          |     100 |          100 |    100 |
| jv           |     100 |          100 |    100 |
| ka           |   10000 |        10000 |  10000 |
| kk           |    1000 |         1000 |   1000 |
| km           |     100 |          100 |    100 |
| kn           |     100 |          100 |    100 |
| ko           |   20000 |        10000 |  10000 |
| ksh          |     100 |          100 |    100 |
| ku           |     100 |          100 |    100 |
| ky           |     100 |          100 |    100 |
| la           |    5000 |         1000 |   1000 |
| lb           |    5000 |         1000 |   1000 |
| li           |     100 |          100 |    100 |
| lij          |     100 |          100 |    100 |
| lmo          |     100 |          100 |    100 |
| ln           |     100 |          100 |    100 |
| lt           |   10000 |        10000 |  10000 |
| lv           |   10000 |        10000 |  10000 |
| map-bms      |     100 |          100 |    100 |
| mg           |     100 |          100 |    100 |
| mhr          |     100 |          100 |    100 |
| mi           |     100 |          100 |    100 |
| min          |     100 |          100 |    100 |
| mk           |   10000 |         1000 |   1000 |
| ml           |   10000 |         1000 |   1000 |
| mn           |     100 |          100 |    100 |
| mr           |    5000 |         1000 |   1000 |
| ms           |   20000 |         1000 |   1000 |
| mt           |     100 |          100 |    100 |
| mwl          |     100 |          100 |    100 |
| my           |     100 |          100 |    100 |
| mzn          |     100 |          100 |    100 |
| nap          |     100 |          100 |    100 |
| nds          |     100 |          100 |    100 |
| ne           |     100 |          100 |    100 |
| nl           |   20000 |        10000 |  10000 |
| nn           |   20000 |         1000 |   1000 |
| no           |   20000 |        10000 |  10000 |
| nov          |     100 |          100 |    100 |
| oc           |     100 |          100 |    100 |
| or           |     100 |          100 |    100 |
| os           |     100 |          100 |    100 |
| pa           |     100 |          100 |    100 |
| pdc          |     100 |          100 |    100 |
| pl           |   20000 |        10000 |  10000 |
| pms          |     100 |          100 |    100 |
| pnb          |     100 |          100 |    100 |
| ps           |     100 |          100 |    100 |
| pt           |   20000 |        10000 |  10000 |
| qu           |     100 |          100 |    100 |
| rm           |     100 |          100 |    100 |
| ro           |   20000 |        10000 |  10000 |
| ru           |   20000 |        10000 |  10000 |
| rw           |     100 |          100 |    100 |
| sa           |     100 |          100 |    100 |
| sah          |     100 |          100 |    100 |
| scn          |     100 |          100 |    100 |
| sco          |     100 |          100 |    100 |
| sd           |     100 |          100 |    100 |
| sh           |   20000 |        10000 |  10000 |
| si           |     100 |          100 |    100 |
| simple       |   20000 |         1000 |   1000 |
| sk           |   20000 |        10000 |  10000 |
| sl           |   15000 |        10000 |  10000 |
| so           |     100 |          100 |    100 |
| sq           |    5000 |         1000 |   1000 |
| sr           |   20000 |        10000 |  10000 |
| su           |     100 |          100 |    100 |
| sv           |   20000 |        10000 |  10000 |
| sw           |    1000 |         1000 |   1000 |
| szl          |     100 |          100 |    100 |
| ta           |   15000 |         1000 |   1000 |
| te           |    1000 |         1000 |   1000 |
| tg           |     100 |          100 |    100 |
| th           |   20000 |        10000 |  10000 |
| tk           |     100 |          100 |    100 |
| tl           |   10000 |         1000 |   1000 |
| tr           |   20000 |        10000 |  10000 |
| tt           |    1000 |         1000 |   1000 |
| ug           |     100 |          100 |    100 |
| uk           |   20000 |        10000 |  10000 |
| ur           |   20000 |         1000 |   1000 |
| uz           |    1000 |         1000 |   1000 |
| vec          |     100 |          100 |    100 |
| vep          |     100 |          100 |    100 |
| vi           |   20000 |        10000 |  10000 |
| vls          |     100 |          100 |    100 |
| vo           |     100 |          100 |    100 |
| wa           |     100 |          100 |    100 |
| war          |     100 |          100 |    100 |
| wuu          |     100 |          100 |    100 |
| xmf          |     100 |          100 |    100 |
| yi           |     100 |          100 |    100 |
| yo           |     100 |          100 |    100 |
| zea          |     100 |          100 |    100 |
| zh           |   20000 |        10000 |  10000 |
| zh-classical |     100 |          100 |    100 |
| zh-min-nan   |     100 |          100 |    100 |
| zh-yue       |   20000 |        10000 |  10000 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

The original 282 datasets are associated with this article

```
@inproceedings{pan-etal-2017-cross,
    title = "Cross-lingual Name Tagging and Linking for 282 Languages",
    author = "Pan, Xiaoman  and
      Zhang, Boliang  and
      May, Jonathan  and
      Nothman, Joel  and
      Knight, Kevin  and
      Ji, Heng",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P17-1178",
    doi = "10.18653/v1/P17-1178",
    pages = "1946--1958",
    abstract = "The ambitious goal of this work is to develop a cross-lingual name tagging and linking framework for 282 languages that exist in Wikipedia. Given a document in any of these languages, our framework is able to identify name mentions, assign a coarse-grained or fine-grained type to each mention, and link it to an English Knowledge Base (KB) if it is linkable. We achieve this goal by performing a series of new KB mining methods: generating {``}silver-standard{''} annotations by transferring annotations from English to other languages through cross-lingual links and KB properties, refining annotations through self-training and topic selection, deriving language-specific morphology features from anchor links, and mining word translation pairs from cross-lingual links. Both name tagging and linking results for 282 languages are promising on Wikipedia data and on-Wikipedia data.",
}
```

while the 176 languages supported in this version are associated with the following article

```
@inproceedings{rahimi-etal-2019-massively,
    title = "Massively Multilingual Transfer for {NER}",
    author = "Rahimi, Afshin  and
      Li, Yuan  and
      Cohn, Trevor",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1015",
    pages = "151--164",
}
```


### Contributions

Thanks to [@lewtun](https://github.com/lewtun) and [@rabeehk](https://github.com/rabeehk) for adding this dataset.