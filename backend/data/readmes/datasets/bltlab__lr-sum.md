---
license: cc-by-4.0
task_categories:
- summarization
- text-generation
annotations_creators:
- found
language_creators:
- found
language:
- am
- az
- bn
- bo
- bs
- ku
- zh
- el
- en
- fa
- fr
- ht
- ha
- hy
- id
- ka
- km
- rw
- ko
- lo
- mk
- my
- nd
- pt
- ps
- ru
- sn
- so
- es
- sq
- sr
- sw
- th
- ti
- tr
- uk
- ur
- uz
- vi
pretty_name: LR-Sum
size_categories:
- 100K<n<1M
multilinguality:
- multilingual
tags:
- conditional-text-generation
viewer: true
configs:
- config_name: amh
  data_files:
  - split: test
    path: amh/test-*
- config_name: aze
  data_files:
  - split: test
    path: aze/test-*
  - split: train
    path: aze/train-*
  - split: validation
    path: aze/validation-*
- config_name: ben
  data_files:
  - split: test
    path: ben/test-*
- config_name: bod
  data_files:
  - split: test
    path: bod/test-*
- config_name: bos
  data_files:
  - split: test
    path: bos/test-*
  - split: train
    path: bos/train-*
  - split: validation
    path: bos/validation-*
- config_name: ckb
  data_files:
  - split: test
    path: ckb/test-*
  - split: train
    path: ckb/train-*
  - split: validation
    path: ckb/validation-*
- config_name: cmn_s
  data_files:
  - split: test
    path: cmn_s/test-*
  - split: train
    path: cmn_s/train-*
  - split: validation
    path: cmn_s/validation-*
- config_name: cmn_t
  data_files:
  - split: test
    path: cmn_t/test-*
  - split: train
    path: cmn_t/train-*
  - split: validation
    path: cmn_t/validation-*
- config_name: ell
  data_files:
  - split: test
    path: ell/test-*
- config_name: eng
  data_files:
  - split: test
    path: eng/test-*
  - split: train
    path: eng/train-*
  - split: validation
    path: eng/validation-*
- config_name: fas
  data_files:
  - split: test
    path: fas/test-*
  - split: train
    path: fas/train-*
  - split: validation
    path: fas/validation-*
- config_name: fra
  data_files:
  - split: test
    path: fra/test-*
  - split: train
    path: fra/train-*
  - split: validation
    path: fra/validation-*
- config_name: hat
  data_files:
  - split: test
    path: hat/test-*
  - split: train
    path: hat/train-*
  - split: validation
    path: hat/validation-*
- config_name: hau
  data_files:
  - split: test
    path: hau/test-*
- config_name: hye
  data_files:
  - split: test
    path: hye/test-*
  - split: train
    path: hye/train-*
  - split: validation
    path: hye/validation-*
- config_name: ind
  data_files:
  - split: test
    path: ind/test-*
  - split: train
    path: ind/train-*
  - split: validation
    path: ind/validation-*
- config_name: kat
  data_files:
  - split: test
    path: kat/test-*
  - split: train
    path: kat/train-*
  - split: validation
    path: kat/validation-*
- config_name: khm
  data_files:
  - split: test
    path: khm/test-*
  - split: train
    path: khm/train-*
  - split: validation
    path: khm/validation-*
- config_name: kin
  data_files:
  - split: test
    path: kin/test-*
- config_name: kmr
  data_files:
  - split: test
    path: kmr/test-*
  - split: train
    path: kmr/train-*
  - split: validation
    path: kmr/validation-*
- config_name: kor
  data_files:
  - split: test
    path: kor/test-*
  - split: train
    path: kor/train-*
  - split: validation
    path: kor/validation-*
- config_name: lao
  data_files:
  - split: test
    path: lao/test-*
  - split: train
    path: lao/train-*
  - split: validation
    path: lao/validation-*
- config_name: mkd
  data_files:
  - split: test
    path: mkd/test-*
  - split: train
    path: mkd/train-*
  - split: validation
    path: mkd/validation-*
- config_name: mya
  data_files:
  - split: test
    path: mya/test-*
  - split: train
    path: mya/train-*
  - split: validation
    path: mya/validation-*
- config_name: nde
  data_files:
  - split: test
    path: nde/test-*
  - split: train
    path: nde/train-*
  - split: validation
    path: nde/validation-*
- config_name: por
  data_files:
  - split: test
    path: por/test-*
  - split: train
    path: por/train-*
  - split: validation
    path: por/validation-*
- config_name: prs
  data_files:
  - split: test
    path: prs/test-*
  - split: train
    path: prs/train-*
  - split: validation
    path: prs/validation-*
- config_name: pus
  data_files:
  - split: test
    path: pus/test-*
  - split: train
    path: pus/train-*
  - split: validation
    path: pus/validation-*
- config_name: rus
  data_files:
  - split: test
    path: rus/test-*
  - split: train
    path: rus/train-*
  - split: validation
    path: rus/validation-*
- config_name: sna
  data_files:
  - split: test
    path: sna/test-*
  - split: train
    path: sna/train-*
  - split: validation
    path: sna/validation-*
- config_name: som
  data_files:
  - split: test
    path: som/test-*
- config_name: spa
  data_files:
  - split: test
    path: spa/test-*
  - split: train
    path: spa/train-*
  - split: validation
    path: spa/validation-*
- config_name: sqi
  data_files:
  - split: test
    path: sqi/test-*
  - split: train
    path: sqi/train-*
  - split: validation
    path: sqi/validation-*
- config_name: srp
  data_files:
  - split: test
    path: srp/test-*
  - split: train
    path: srp/train-*
  - split: validation
    path: srp/validation-*
- config_name: swh
  data_files:
  - split: test
    path: swh/test-*
- config_name: tha
  data_files:
  - split: test
    path: tha/test-*
  - split: train
    path: tha/train-*
  - split: validation
    path: tha/validation-*
- config_name: tir
  data_files:
  - split: test
    path: tir/test-*
- config_name: tur
  data_files:
  - split: test
    path: tur/test-*
  - split: train
    path: tur/train-*
  - split: validation
    path: tur/validation-*
- config_name: ukr
  data_files:
  - split: test
    path: ukr/test-*
  - split: train
    path: ukr/train-*
  - split: validation
    path: ukr/validation-*
- config_name: urd
  data_files:
  - split: test
    path: urd/test-*
  - split: train
    path: urd/train-*
  - split: validation
    path: urd/validation-*
- config_name: uzb
  data_files:
  - split: test
    path: uzb/test-*
  - split: train
    path: uzb/train-*
  - split: validation
    path: uzb/validation-*
- config_name: vie
  data_files:
  - split: test
    path: vie/test-*
  - split: train
    path: vie/train-*
  - split: validation
    path: vie/validation-*
dataset_info:
- config_name: amh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 661238
    num_examples: 154
  download_size: 336803
  dataset_size: 661238
- config_name: aze
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2690777
    num_examples: 811
  - name: train
    num_bytes: 21683595
    num_examples: 6487
  - name: validation
    num_bytes: 2653949
    num_examples: 810
  download_size: 15117096
  dataset_size: 27028321
- config_name: ben
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 4111932
    num_examples: 715
  download_size: 1597837
  dataset_size: 4111932
- config_name: bod
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2423126
    num_examples: 182
  download_size: 694122
  dataset_size: 2423126
- config_name: bos
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 4793400
    num_examples: 1456
  - name: train
    num_bytes: 37692878
    num_examples: 11648
  - name: validation
    num_bytes: 4674155
    num_examples: 1455
  download_size: 30934781
  dataset_size: 47160433
- config_name: ckb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 3073172
    num_examples: 500
  - name: train
    num_bytes: 7492985
    num_examples: 1230
  - name: validation
    num_bytes: 3251806
    num_examples: 500
  download_size: 6054129
  dataset_size: 13817963
- config_name: cmn_s
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2444203
    num_examples: 500
  - name: train
    num_bytes: 2324426
    num_examples: 483
  - name: validation
    num_bytes: 2452904
    num_examples: 500
  download_size: 4786850
  dataset_size: 7221533
- config_name: cmn_t
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1926008
    num_examples: 500
  - name: train
    num_bytes: 7969758
    num_examples: 2103
  - name: validation
    num_bytes: 1938286
    num_examples: 500
  download_size: 7934145
  dataset_size: 11834052
- config_name: ell
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 3244069
    num_examples: 583
  download_size: 1557990
  dataset_size: 3244069
- config_name: eng
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 10021562
    num_examples: 2622
  - name: train
    num_bytes: 79349108
    num_examples: 20976
  - name: validation
    num_bytes: 9859201
    num_examples: 2621
  download_size: 60141163
  dataset_size: 99229871
- config_name: fas
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 7011820
    num_examples: 1343
  - name: train
    num_bytes: 54763383
    num_examples: 10744
  - name: validation
    num_bytes: 7039991
    num_examples: 1342
  download_size: 32366005
  dataset_size: 68815194
- config_name: fra
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1363784
    num_examples: 500
  - name: train
    num_bytes: 3139247
    num_examples: 1126
  - name: validation
    num_bytes: 1394751
    num_examples: 500
  download_size: 3525857
  dataset_size: 5897782
- config_name: hat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1269965
    num_examples: 500
  - name: train
    num_bytes: 1132879
    num_examples: 452
  - name: validation
    num_bytes: 1291910
    num_examples: 500
  download_size: 2243949
  dataset_size: 3694754
- config_name: hau
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 895424
    num_examples: 390
  download_size: 519692
  dataset_size: 895424
- config_name: hye
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2237917
    num_examples: 500
  - name: train
    num_bytes: 4088649
    num_examples: 920
  - name: validation
    num_bytes: 2296861
    num_examples: 500
  download_size: 3921240
  dataset_size: 8623427
- config_name: ind
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1346577
    num_examples: 500
  - name: train
    num_bytes: 2672066
    num_examples: 968
  - name: validation
    num_bytes: 1355415
    num_examples: 500
  download_size: 3069718
  dataset_size: 5374058
- config_name: kat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 4478271
    num_examples: 500
  - name: train
    num_bytes: 4392502
    num_examples: 511
  - name: validation
    num_bytes: 4420969
    num_examples: 500
  download_size: 4721935
  dataset_size: 13291742
- config_name: khm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 6017258
    num_examples: 486
  - name: train
    num_bytes: 47799518
    num_examples: 3888
  - name: validation
    num_bytes: 5828411
    num_examples: 486
  download_size: 21074908
  dataset_size: 59645187
- config_name: kin
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1852173
    num_examples: 698
  download_size: 1070291
  dataset_size: 1852173
- config_name: kmr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1204722
    num_examples: 500
  - name: train
    num_bytes: 1953328
    num_examples: 791
  - name: validation
    num_bytes: 1208299
    num_examples: 500
  download_size: 2596272
  dataset_size: 4366349
- config_name: kor
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 5942952
    num_examples: 1312
  - name: train
    num_bytes: 47806874
    num_examples: 10499
  - name: validation
    num_bytes: 6056985
    num_examples: 1312
  download_size: 32709139
  dataset_size: 59806811
- config_name: lao
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 8556850
    num_examples: 1496
  - name: train
    num_bytes: 68586272
    num_examples: 11964
  - name: validation
    num_bytes: 8598134
    num_examples: 1495
  download_size: 33917486
  dataset_size: 85741256
- config_name: mkd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2379294
    num_examples: 500
  - name: train
    num_bytes: 5596593
    num_examples: 1223
  - name: validation
    num_bytes: 2327437
    num_examples: 500
  download_size: 4832370
  dataset_size: 10303324
- config_name: mya
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 15238699
    num_examples: 990
  - name: train
    num_bytes: 122554522
    num_examples: 7921
  - name: validation
    num_bytes: 14863452
    num_examples: 990
  download_size: 50240586
  dataset_size: 152656673
- config_name: nde
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1408589
    num_examples: 500
  - name: train
    num_bytes: 4885282
    num_examples: 1739
  - name: validation
    num_bytes: 1400285
    num_examples: 500
  download_size: 4541017
  dataset_size: 7694156
- config_name: por
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1450050
    num_examples: 500
  - name: train
    num_bytes: 1905010
    num_examples: 643
  - name: validation
    num_bytes: 1506258
    num_examples: 500
  download_size: 2877418
  dataset_size: 4861318
- config_name: prs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 6454725
    num_examples: 1505
  - name: train
    num_bytes: 52261705
    num_examples: 12037
  - name: validation
    num_bytes: 6594769
    num_examples: 1504
  download_size: 30143285
  dataset_size: 65311199
- config_name: pus
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 8662917
    num_examples: 2107
  - name: train
    num_bytes: 68247927
    num_examples: 16854
  - name: validation
    num_bytes: 8566877
    num_examples: 2106
  download_size: 40895100
  dataset_size: 85477721
- config_name: rus
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 9968681
    num_examples: 1351
  - name: train
    num_bytes: 78755821
    num_examples: 10812
  - name: validation
    num_bytes: 9816066
    num_examples: 1351
  download_size: 48949523
  dataset_size: 98540568
- config_name: sna
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1194214
    num_examples: 500
  - name: train
    num_bytes: 899993
    num_examples: 383
  - name: validation
    num_bytes: 1184515
    num_examples: 500
  download_size: 1814862
  dataset_size: 3278722
- config_name: som
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 506717
    num_examples: 165
  download_size: 296666
  dataset_size: 506717
- config_name: spa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 2030182
    num_examples: 500
  - name: train
    num_bytes: 10404331
    num_examples: 2544
  - name: validation
    num_bytes: 2000911
    num_examples: 500
  download_size: 8521153
  dataset_size: 14435424
- config_name: sqi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 7587993
    num_examples: 2289
  - name: train
    num_bytes: 59943133
    num_examples: 18312
  - name: validation
    num_bytes: 7507460
    num_examples: 2289
  download_size: 43393330
  dataset_size: 75038586
- config_name: srp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1515008
    num_examples: 622
  - name: train
    num_bytes: 11918653
    num_examples: 4974
  - name: validation
    num_bytes: 1452745
    num_examples: 621
  download_size: 9870510
  dataset_size: 14886406
- config_name: swh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 1489689
    num_examples: 588
  download_size: 863092
  dataset_size: 1489689
- config_name: tha
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 3293795
    num_examples: 500
  - name: train
    num_bytes: 14854644
    num_examples: 2278
  - name: validation
    num_bytes: 3256105
    num_examples: 500
  download_size: 8255931
  dataset_size: 21404544
- config_name: tir
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 438551
    num_examples: 115
  download_size: 219906
  dataset_size: 438551
- config_name: tur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 13882447
    num_examples: 3584
  - name: train
    num_bytes: 110683341
    num_examples: 28672
  - name: validation
    num_bytes: 13819996
    num_examples: 3583
  download_size: 78743945
  dataset_size: 138385784
- config_name: ukr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 4045975
    num_examples: 723
  - name: train
    num_bytes: 32769694
    num_examples: 5784
  - name: validation
    num_bytes: 4132715
    num_examples: 722
  download_size: 20683201
  dataset_size: 40948384
- config_name: urd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 7782956
    num_examples: 1356
  - name: train
    num_bytes: 61945678
    num_examples: 10847
  - name: validation
    num_bytes: 7593839
    num_examples: 1355
  download_size: 36101540
  dataset_size: 77322473
- config_name: uzb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 4017107
    num_examples: 1196
  - name: train
    num_bytes: 31443934
    num_examples: 9568
  - name: validation
    num_bytes: 3885183
    num_examples: 1195
  download_size: 23009414
  dataset_size: 39346224
- config_name: vie
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: summary
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: test
    num_bytes: 7154851
    num_examples: 1460
  - name: train
    num_bytes: 58121650
    num_examples: 11676
  - name: validation
    num_bytes: 7359957
    num_examples: 1459
  download_size: 37719297
  dataset_size: 72636458
---
# Dataset Card for LR-Sum

LR-Sum is a automatic summarization dataset of newswire text with a focus on less resourced languages with a cc-by 4.0 license.


## Dataset Details

### Dataset Description

LR-Sum is a permissively-licensed dataset created with the goal of enabling further research in automatic summarization for less-resourced languages.
LR-Sum contains human-written summaries for 39 languages, many of which are less-resourced. 
The data is based on the collection of the Multilingual Open Text corpus where the source data is public domain newswire collected from from Voice of America websites.
LR-Sum is released under a Creative Commons license (CC BY 4.0), making it one of the most openly-licensed multilingual summarization datasets. 

- **Curated by:** BLT Lab: Chester Palen-Michel and Constantine Lignos
- **Shared by:** Chester Palen-Michel
- **Language(s) (NLP):** Albanian, Amharic, Armenian, Azerbaijani, Bengali, Bosnian, Burmese, Chinese, English, French, Georgian, Greek, Haitian Creole, Hausa, Indonesian, Khmer, Kinyarwanda, Korean, Kurdish, Lao, Macedonian, Northern Ndebele, Pashto, Persian, Portuguese, Russian, Serbian, Shona, Somali, Spanish, Swahili, Thai, Tibetan, Tigrinya, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese
- **License:** CC-BY 4.0

### Dataset Sources [optional]

Multilingual Open Text v1.6
which is a collection of newswire text from Voice of America (VOA).

- **Paper:** [https://aclanthology.org/2023.findings-acl.427/](https://aclanthology.org/2023.findings-acl.427/)
- **Repository:** [https://github.com/bltlab/lr-sum](https://github.com/bltlab/lr-sum)


## Uses

The dataset is intended for research in automatic summarization in various languages, especially for less resourced languages.

### Direct Use

The data can be used for training text generation models to generate short summaries of news articles in many languages.
Automatic evaluation of automatic summarization is another use case, though we encourage also conducting human evaluation of any model trained for summarization.

### Out-of-Scope Use

This dataset only includes newswire text, so models trained on the data may not be effective for out of domain summarization. 


## Dataset Structure

Each field is a string: 
```
{
  'id': Article unique id
  'url': URL for the news article
  'title': The title of the news article
  'summary': The summary of the article
  'text': The full text of the news article not including title
}
```


## Dataset Creation

### Curation Rationale

Research in automatic summarization for less resourced languages.

### Source Data

Voice of America (VOA)

#### Data Collection and Processing

See our [paper](https://aclanthology.org/2023.findings-acl.427/) for details on collection and processing. 


#### Who are the source data producers?

Voice of America (VOA)

#### Annotation process

The summaries are found in news article meta data. More detail about the curation process can be found in our paper.

#### Who are the annotators?

The summaries are found in the news article meta data. The authors of the summaries are authors and staff for VOA.


#### Personal and Sensitive Information

The only sensative personal information would be information already published in news articles on VOA. 
See [VOA's mission and values](https://www.insidevoa.com/p/5831.html#:~:text=VOA%20has%20a%20legal%20obligation,sites%20at%20the%20earliest%20opportunity.)

## Bias, Risks, and Limitations

The content in this dataset is newswire.
See [VOA's mission and values](https://www.insidevoa.com/p/5831.html#:~:text=VOA%20has%20a%20legal%20obligation,sites%20at%20the%20earliest%20opportunity.) for more detail about the journalistic integrity and policy. 


### Recommendations

The data is newswire text. Training text generation models on this dataset will have similar risks and limitations to other text generation models including hallucinations and potentially inaccurate statements. 
For some languages that have fewer examples, issues with text generation models are likely to be more pronounced.
The dataset is primarily released for research despite having a permissive license. 
We encourage users to thoroughly test and evaluate any models trained using this data before putting them into production environments. 

## Citation

If you make use of this dataset, please cite our paper using this bibtex: 

**BibTeX:**
```
@inproceedings{palen-michel-lignos-2023-lr,
    title = "{LR}-Sum: Summarization for Less-Resourced Languages",
    author = "Palen-Michel, Chester  and
      Lignos, Constantine",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.427",
    doi = "10.18653/v1/2023.findings-acl.427",
    pages = "6829--6844",
    abstract = "We introduce LR-Sum, a new permissively-licensed dataset created with the goal of enabling further research in automatic summarization for less-resourced languages.LR-Sum contains human-written summaries for 40 languages, many of which are less-resourced. We describe our process for extracting and filtering the dataset from the Multilingual Open Text corpus (Palen-Michel et al., 2022).The source data is public domain newswire collected from from Voice of America websites, and LR-Sum is released under a Creative Commons license (CC BY 4.0), making it one of the most openly-licensed multilingual summarization datasets. We describe abstractive and extractive summarization experiments to establish baselines and discuss the limitations of this dataset.",
}
```

## Dataset Card Authors

Chester Palen-Michel [@cpalenmichel](https://github.com/cpalenmichel)

## Dataset Card Contact

Chester Palen-Michel [@cpalenmichel](https://github.com/cpalenmichel)