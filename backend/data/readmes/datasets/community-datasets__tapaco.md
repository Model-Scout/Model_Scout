---
annotations_creators:
- machine-generated
language_creators:
- crowdsourced
language:
- af
- ar
- az
- be
- ber
- bg
- bn
- br
- ca
- cbk
- cmn
- cs
- da
- de
- el
- en
- eo
- es
- et
- eu
- fi
- fr
- gl
- gos
- he
- hi
- hr
- hu
- hy
- ia
- id
- ie
- io
- is
- it
- ja
- jbo
- kab
- ko
- kw
- la
- lfn
- lt
- mk
- mr
- nb
- nds
- nl
- orv
- ota
- pes
- pl
- pt
- rn
- ro
- ru
- sl
- sr
- sv
- tk
- tl
- tlh
- tok
- tr
- tt
- ug
- uk
- ur
- vi
- vo
- war
- wuu
- yue
license:
- cc-by-2.0
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
- 10K<n<100K
- 1K<n<10K
- 1M<n<10M
- n<1K
source_datasets:
- extended|other-tatoeba
task_categories:
- text2text-generation
- translation
- text-classification
task_ids:
- semantic-similarity-classification
paperswithcode_id: tapaco
pretty_name: TaPaCo Corpus
config_names:
- af
- all_languages
- ar
- az
- be
- ber
- bg
- bn
- br
- ca
- cbk
- cmn
- cs
- da
- de
- el
- en
- eo
- es
- et
- eu
- fi
- fr
- gl
- gos
- he
- hi
- hr
- hu
- hy
- ia
- id
- ie
- io
- is
- it
- ja
- jbo
- kab
- ko
- kw
- la
- lfn
- lt
- mk
- mr
- nb
- nds
- nl
- orv
- ota
- pes
- pl
- pt
- rn
- ro
- ru
- sl
- sr
- sv
- tk
- tl
- tlh
- tok
- tr
- tt
- ug
- uk
- ur
- vi
- vo
- war
- wuu
- yue
tags:
- paraphrase-generation
dataset_info:
- config_name: af
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 21187
    num_examples: 307
  download_size: 11781
  dataset_size: 21187
- config_name: all_languages
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 162796380
    num_examples: 1926192
  download_size: 65568453
  dataset_size: 162796380
- config_name: ar
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 546168
    num_examples: 6446
  download_size: 220221
  dataset_size: 546168
- config_name: az
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 44429
    num_examples: 624
  download_size: 20418
  dataset_size: 44429
- config_name: be
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 140344
    num_examples: 1512
  download_size: 58566
  dataset_size: 140344
- config_name: ber
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 5118396
    num_examples: 67484
  download_size: 1813469
  dataset_size: 5118396
- config_name: bg
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 590503
    num_examples: 6324
  download_size: 219682
  dataset_size: 590503
- config_name: bn
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 146622
    num_examples: 1440
  download_size: 46005
  dataset_size: 146622
- config_name: br
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 177887
    num_examples: 2536
  download_size: 65451
  dataset_size: 177887
- config_name: ca
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 39372
    num_examples: 518
  download_size: 20977
  dataset_size: 39372
- config_name: cbk
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 19372
    num_examples: 262
  download_size: 11222
  dataset_size: 19372
- config_name: cmn
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 964450
    num_examples: 12549
  download_size: 440938
  dataset_size: 964450
- config_name: cs
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 482260
    num_examples: 6659
  download_size: 213014
  dataset_size: 482260
- config_name: da
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 848822
    num_examples: 11220
  download_size: 362445
  dataset_size: 848822
- config_name: de
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 10592961
    num_examples: 125091
  download_size: 4618002
  dataset_size: 10592961
- config_name: el
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 925990
    num_examples: 10072
  download_size: 332949
  dataset_size: 925990
- config_name: en
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 15069837
    num_examples: 158053
  download_size: 5633416
  dataset_size: 15069837
- config_name: eo
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 16810293
    num_examples: 207105
  download_size: 7386804
  dataset_size: 16810293
- config_name: es
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 6850847
    num_examples: 85064
  download_size: 3037352
  dataset_size: 6850847
- config_name: et
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 17095
    num_examples: 241
  download_size: 10628
  dataset_size: 17095
- config_name: eu
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 42670
    num_examples: 573
  download_size: 21506
  dataset_size: 42670
- config_name: fi
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 2520039
    num_examples: 31753
  download_size: 1066381
  dataset_size: 2520039
- config_name: fr
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 9481042
    num_examples: 116733
  download_size: 4010846
  dataset_size: 9481042
- config_name: gl
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 26519
    num_examples: 351
  download_size: 15428
  dataset_size: 26519
- config_name: gos
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 18410
    num_examples: 279
  download_size: 10252
  dataset_size: 18410
- config_name: he
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 6024121
    num_examples: 68350
  download_size: 2352588
  dataset_size: 6024121
- config_name: hi
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 209350
    num_examples: 1913
  download_size: 71529
  dataset_size: 209350
- config_name: hr
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 36606
    num_examples: 505
  download_size: 19165
  dataset_size: 36606
- config_name: hu
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 5289386
    num_examples: 67964
  download_size: 2387466
  dataset_size: 5289386
- config_name: hy
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 49198
    num_examples: 603
  download_size: 19715
  dataset_size: 49198
- config_name: ia
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 194003
    num_examples: 2548
  download_size: 85581
  dataset_size: 194003
- config_name: id
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 124536
    num_examples: 1602
  download_size: 54675
  dataset_size: 124536
- config_name: ie
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 31924
    num_examples: 488
  download_size: 15718
  dataset_size: 31924
- config_name: io
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 33860
    num_examples: 480
  download_size: 17288
  dataset_size: 33860
- config_name: is
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 132030
    num_examples: 1641
  download_size: 58439
  dataset_size: 132030
- config_name: it
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 15073110
    num_examples: 198919
  download_size: 5419790
  dataset_size: 15073110
- config_name: ja
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 4314263
    num_examples: 44267
  download_size: 1736954
  dataset_size: 4314263
- config_name: jbo
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 201532
    num_examples: 2704
  download_size: 90713
  dataset_size: 201532
- config_name: kab
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1210987
    num_examples: 15944
  download_size: 471650
  dataset_size: 1210987
- config_name: ko
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 40426
    num_examples: 503
  download_size: 20200
  dataset_size: 40426
- config_name: kw
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 88545
    num_examples: 1328
  download_size: 35630
  dataset_size: 88545
- config_name: la
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 485717
    num_examples: 6889
  download_size: 201849
  dataset_size: 485717
- config_name: lfn
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 203351
    num_examples: 2313
  download_size: 91808
  dataset_size: 203351
- config_name: lt
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 599134
    num_examples: 8042
  download_size: 263103
  dataset_size: 599134
- config_name: mk
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1240121
    num_examples: 14678
  download_size: 466182
  dataset_size: 1240121
- config_name: mr
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1838857
    num_examples: 16413
  download_size: 590051
  dataset_size: 1838857
- config_name: nb
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 85339
    num_examples: 1094
  download_size: 39494
  dataset_size: 85339
- config_name: nds
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 194989
    num_examples: 2633
  download_size: 85174
  dataset_size: 194989
- config_name: nl
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1790879
    num_examples: 23561
  download_size: 779446
  dataset_size: 1790879
- config_name: orv
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 40452
    num_examples: 471
  download_size: 20411
  dataset_size: 40452
- config_name: ota
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 44964
    num_examples: 486
  download_size: 23354
  dataset_size: 44964
- config_name: pes
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 433374
    num_examples: 4285
  download_size: 180609
  dataset_size: 433374
- config_name: pl
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 1722092
    num_examples: 22391
  download_size: 782825
  dataset_size: 1722092
- config_name: pt
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 6140922
    num_examples: 78430
  download_size: 2618549
  dataset_size: 6140922
- config_name: rn
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 47355
    num_examples: 648
  download_size: 20827
  dataset_size: 47355
- config_name: ro
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 162923
    num_examples: 2092
  download_size: 76736
  dataset_size: 162923
- config_name: ru
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 24539835
    num_examples: 251263
  download_size: 9240710
  dataset_size: 24539835
- config_name: sl
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 49578
    num_examples: 706
  download_size: 24925
  dataset_size: 49578
- config_name: sr
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 667276
    num_examples: 8175
  download_size: 305343
  dataset_size: 667276
- config_name: sv
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 509852
    num_examples: 7005
  download_size: 213626
  dataset_size: 509852
- config_name: tk
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 95015
    num_examples: 1165
  download_size: 43014
  dataset_size: 95015
- config_name: tl
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 76027
    num_examples: 1017
  download_size: 36676
  dataset_size: 76027
- config_name: tlh
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 185277
    num_examples: 2804
  download_size: 77664
  dataset_size: 185277
- config_name: toki
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 310832
    num_examples: 3738
  download_size: 120515
  dataset_size: 310832
- config_name: tr
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 11270678
    num_examples: 142088
  download_size: 4811347
  dataset_size: 11270678
- config_name: tt
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 277237
    num_examples: 2398
  download_size: 133537
  dataset_size: 277237
- config_name: ug
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 118442
    num_examples: 1183
  download_size: 45577
  dataset_size: 118442
- config_name: uk
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 4885485
    num_examples: 54431
  download_size: 1814842
  dataset_size: 4885485
- config_name: ur
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 24043
    num_examples: 252
  download_size: 12712
  dataset_size: 24043
- config_name: vi
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 84741
    num_examples: 962
  download_size: 38362
  dataset_size: 84741
- config_name: vo
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 22132
    num_examples: 328
  download_size: 12011
  dataset_size: 22132
- config_name: war
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 25727
    num_examples: 327
  download_size: 14217
  dataset_size: 25727
- config_name: wuu
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 31608
    num_examples: 408
  download_size: 17221
  dataset_size: 31608
- config_name: yue
  features:
  - name: paraphrase_set_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: paraphrase
    dtype: string
  - name: lists
    sequence: string
  - name: tags
    sequence: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 42734
    num_examples: 561
  download_size: 21047
  dataset_size: 42734
configs:
- config_name: af
  data_files:
  - split: train
    path: af/train-*
- config_name: all_languages
  data_files:
  - split: train
    path: all_languages/train-*
  default: true
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: az
  data_files:
  - split: train
    path: az/train-*
- config_name: be
  data_files:
  - split: train
    path: be/train-*
- config_name: ber
  data_files:
  - split: train
    path: ber/train-*
- config_name: bg
  data_files:
  - split: train
    path: bg/train-*
- config_name: bn
  data_files:
  - split: train
    path: bn/train-*
- config_name: br
  data_files:
  - split: train
    path: br/train-*
- config_name: ca
  data_files:
  - split: train
    path: ca/train-*
- config_name: cbk
  data_files:
  - split: train
    path: cbk/train-*
- config_name: cmn
  data_files:
  - split: train
    path: cmn/train-*
- config_name: cs
  data_files:
  - split: train
    path: cs/train-*
- config_name: da
  data_files:
  - split: train
    path: da/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: el
  data_files:
  - split: train
    path: el/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: eo
  data_files:
  - split: train
    path: eo/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: et
  data_files:
  - split: train
    path: et/train-*
- config_name: eu
  data_files:
  - split: train
    path: eu/train-*
- config_name: fi
  data_files:
  - split: train
    path: fi/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: gl
  data_files:
  - split: train
    path: gl/train-*
- config_name: gos
  data_files:
  - split: train
    path: gos/train-*
- config_name: he
  data_files:
  - split: train
    path: he/train-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
- config_name: hr
  data_files:
  - split: train
    path: hr/train-*
- config_name: hu
  data_files:
  - split: train
    path: hu/train-*
- config_name: hy
  data_files:
  - split: train
    path: hy/train-*
- config_name: ia
  data_files:
  - split: train
    path: ia/train-*
- config_name: id
  data_files:
  - split: train
    path: id/train-*
- config_name: ie
  data_files:
  - split: train
    path: ie/train-*
- config_name: io
  data_files:
  - split: train
    path: io/train-*
- config_name: is
  data_files:
  - split: train
    path: is/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: jbo
  data_files:
  - split: train
    path: jbo/train-*
- config_name: kab
  data_files:
  - split: train
    path: kab/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: kw
  data_files:
  - split: train
    path: kw/train-*
- config_name: la
  data_files:
  - split: train
    path: la/train-*
- config_name: lfn
  data_files:
  - split: train
    path: lfn/train-*
- config_name: lt
  data_files:
  - split: train
    path: lt/train-*
- config_name: mk
  data_files:
  - split: train
    path: mk/train-*
- config_name: mr
  data_files:
  - split: train
    path: mr/train-*
- config_name: nb
  data_files:
  - split: train
    path: nb/train-*
- config_name: nds
  data_files:
  - split: train
    path: nds/train-*
- config_name: nl
  data_files:
  - split: train
    path: nl/train-*
- config_name: orv
  data_files:
  - split: train
    path: orv/train-*
- config_name: ota
  data_files:
  - split: train
    path: ota/train-*
- config_name: pes
  data_files:
  - split: train
    path: pes/train-*
- config_name: pl
  data_files:
  - split: train
    path: pl/train-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
- config_name: rn
  data_files:
  - split: train
    path: rn/train-*
- config_name: ro
  data_files:
  - split: train
    path: ro/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: sl
  data_files:
  - split: train
    path: sl/train-*
- config_name: sr
  data_files:
  - split: train
    path: sr/train-*
- config_name: sv
  data_files:
  - split: train
    path: sv/train-*
- config_name: tk
  data_files:
  - split: train
    path: tk/train-*
- config_name: tl
  data_files:
  - split: train
    path: tl/train-*
- config_name: tlh
  data_files:
  - split: train
    path: tlh/train-*
- config_name: toki
  data_files:
  - split: train
    path: toki/train-*
- config_name: tr
  data_files:
  - split: train
    path: tr/train-*
- config_name: tt
  data_files:
  - split: train
    path: tt/train-*
- config_name: ug
  data_files:
  - split: train
    path: ug/train-*
- config_name: uk
  data_files:
  - split: train
    path: uk/train-*
- config_name: ur
  data_files:
  - split: train
    path: ur/train-*
- config_name: vi
  data_files:
  - split: train
    path: vi/train-*
- config_name: vo
  data_files:
  - split: train
    path: vo/train-*
- config_name: war
  data_files:
  - split: train
    path: war/train-*
- config_name: wuu
  data_files:
  - split: train
    path: wuu/train-*
- config_name: yue
  data_files:
  - split: train
    path: yue/train-*
---

# Dataset Card for TaPaCo Corpus

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

- **Homepage:** [TaPaCo: A Corpus of Sentential Paraphrases for 73 Languages](https://zenodo.org/record/3707949#.X9Dh0cYza3I)
- **Paper:** [TaPaCo: A Corpus of Sentential Paraphrases for 73 Languages](https://www.aclweb.org/anthology/2020.lrec-1.848.pdf)
- **Data:** https://doi.org/10.5281/zenodo.3707949
- **Point of Contact:** [Yves Scherrer](https://blogs.helsinki.fi/yvesscherrer/)

### Dataset Summary
A freely available paraphrase corpus for 73 languages extracted from the Tatoeba database. 
Tatoeba is a crowdsourcing project mainly geared towards language learners. Its aim is to provide example sentences 
and translations for particular linguistic constructions and words. The paraphrase corpus is created by populating a 
graph with Tatoeba sentences and equivalence links between sentences “meaning the same thing”. This graph is then 
traversed to extract sets of paraphrases. Several language-independent filters and pruning steps are applied to 
remove uninteresting sentences. A manual evaluation performed on three languages shows that between half and three 
quarters of inferred paraphrases are correct and that most remaining ones are either correct but trivial, 
or near-paraphrases that neutralize a morphological distinction. The corpus contains a total of 1.9 million 
sentences, with 200 – 250 000 sentences per language. It covers a range of languages for which, to our knowledge,
no other paraphrase dataset exists.

### Supported Tasks and Leaderboards
Paraphrase detection and generation have become popular tasks in NLP
and are increasingly integrated into a wide variety of common downstream tasks such as machine translation
, information retrieval, question answering, and semantic parsing. Most of the existing datasets
 cover only a single language – in most cases English – or a small number of languages. Furthermore, some paraphrase
  datasets focus on lexical and phrasal rather than sentential paraphrases, while others are created (semi
  -)automatically using machine translation.

The number of sentences per language ranges from 200 to 250 000, which makes the dataset
more suitable for fine-tuning and evaluation purposes than
for training. It is well-suited for multi-reference evaluation
of paraphrase generation models, as there is generally not a
single correct way of paraphrasing a given input sentence.

### Languages

The dataset contains paraphrases in Afrikaans, Arabic, Azerbaijani, Belarusian, Berber languages, Bulgarian, Bengali
, Breton, Catalan; Valencian, Chavacano, Mandarin, Czech, Danish, German, Greek, Modern (1453-), English, Esperanto
, Spanish; Castilian, Estonian, Basque, Finnish, French, Galician, Gronings, Hebrew, Hindi, Croatian, Hungarian
, Armenian, Interlingua (International Auxiliary Language Association), Indonesian, Interlingue; Occidental, Ido
, Icelandic, Italian, Japanese, Lojban, Kabyle, Korean, Cornish, Latin, Lingua Franca Nova\t, Lithuanian, Macedonian
, Marathi, Bokmål, Norwegian; Norwegian Bokmål, Low German; Low Saxon; German, Low; Saxon, Low, Dutch; Flemish, ]Old
 Russian, Turkish, Ottoman (1500-1928), Iranian Persian, Polish, Portuguese, Rundi, Romanian; Moldavian; Moldovan, 
 Russian, Slovenian, Serbian, Swedish, Turkmen, Tagalog, Klingon; tlhIngan-Hol, Toki Pona, Turkish, Tatar, 
 Uighur; Uyghur, Ukrainian, Urdu, Vietnamese, Volapük, Waray, Wu Chinese and Yue Chinese

## Dataset Structure

### Data Instances
Each data instance corresponds to a paraphrase, e.g.:
```
{ 
    'paraphrase_set_id': '1483',  
    'sentence_id': '5778896',
    'paraphrase': 'Ɣremt adlis-a.', 
    'lists': ['7546'], 
    'tags': [''],
    'language': 'ber'
}
```

### Data Fields
Each dialogue instance has the following fields:
- `paraphrase_set_id`:  a running number that groups together all sentences that are considered paraphrases of each
 other
- `sentence_id`: OPUS sentence id
- `paraphrase`: Sentential paraphrase in a given language for a given paraphrase_set_id
- `lists`: Contributors can add sentences to list in order to specify the original source of the data
- `tags`: Indicates morphological or phonological properties of the sentence when available
- `language`: Language identifier, one of the 73 languages that belong to this dataset.

### Data Splits

The dataset is having a single `train` split, contains a total of 1.9 million sentences, with 200 – 250 000
 sentences per language

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

Creative Commons Attribution 2.0 Generic

### Citation Information

```
@dataset{scherrer_yves_2020_3707949,
  author       = {Scherrer, Yves},
  title        = {{TaPaCo: A Corpus of Sentential Paraphrases for 73 Languages}},
  month        = mar,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.3707949},
  url          = {https://doi.org/10.5281/zenodo.3707949}
}
```

### Contributions

Thanks to [@pacman100](https://github.com/pacman100) for adding this dataset.