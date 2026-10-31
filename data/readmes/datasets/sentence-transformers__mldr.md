---
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- feature-extraction
- sentence-similarity
pretty_name: MLDR
tags:
- sentence-transformers
dataset_info:
- config_name: ar-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 89773560
    num_examples: 1817
  download_size: 38357137
  dataset_size: 89773560
- config_name: ar-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 911359304
    num_examples: 1817
  download_size: 355756978
  dataset_size: 911359304
- config_name: ar-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1765830800
    num_examples: 36340
  download_size: 346510123
  dataset_size: 1765830800
- config_name: de-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 67945237
    num_examples: 1847
  download_size: 33611615
  dataset_size: 67945237
- config_name: de-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 522968414
    num_examples: 1847
  download_size: 210467573
  dataset_size: 522968414
- config_name: de-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1345053973
    num_examples: 36940
  download_size: 204760382
  dataset_size: 1345053973
- config_name: en-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 371120842
    num_examples: 10000
  download_size: 210599567
  dataset_size: 371120842
- config_name: en-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 3495220484
    num_examples: 10000
  download_size: 1986032043
  dataset_size: 3495220484
- config_name: en-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 7373345748
    num_examples: 200000
  download_size: 1965045120
  dataset_size: 7373345748
- config_name: es-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 81253791
    num_examples: 2254
  download_size: 43382242
  dataset_size: 81253791
- config_name: es-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 802897501
    num_examples: 2254
  download_size: 389699455
  dataset_size: 802897501
- config_name: es-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1616624371
    num_examples: 45080
  download_size: 377129890
  dataset_size: 1616624371
- config_name: fr-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 60930593
    num_examples: 1608
  download_size: 32374640
  dataset_size: 60930593
- config_name: fr-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 533051055
    num_examples: 1608
  download_size: 254975690
  dataset_size: 533051055
- config_name: fr-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1226217301
    num_examples: 32160
  download_size: 243195503
  dataset_size: 1226217301
- config_name: hi-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 111004563
    num_examples: 1618
  download_size: 37095092
  dataset_size: 111004563
- config_name: hi-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 1202794947
    num_examples: 1618
  download_size: 385575104
  dataset_size: 1202794947
- config_name: hi-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 2236082701
    num_examples: 32360
  download_size: 343682959
  dataset_size: 2236082701
- config_name: it-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 87570527
    num_examples: 2151
  download_size: 47558925
  dataset_size: 87570527
- config_name: it-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 820503850
    num_examples: 2151
  download_size: 401755594
  dataset_size: 820503850
- config_name: it-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1736339817
    num_examples: 43020
  download_size: 385436701
  dataset_size: 1736339817
- config_name: ja-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 91734476
    num_examples: 2262
  download_size: 46617451
  dataset_size: 91734476
- config_name: ja-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 904143917
    num_examples: 2262
  download_size: 414443489
  dataset_size: 904143917
- config_name: ja-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1842926127
    num_examples: 45240
  download_size: 400101926
  dataset_size: 1842926127
- config_name: ko-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 71630335
    num_examples: 2198
  download_size: 37190024
  dataset_size: 71630335
- config_name: ko-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 730037557
    num_examples: 2198
  download_size: 343330881
  dataset_size: 730037557
- config_name: ko-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1435371745
    num_examples: 43960
  download_size: 335324951
  dataset_size: 1435371745
- config_name: pt-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 77542677
    num_examples: 1845
  download_size: 41644485
  dataset_size: 77542677
- config_name: pt-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 734568750
    num_examples: 1845
  download_size: 349585902
  dataset_size: 734568750
- config_name: pt-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1558494402
    num_examples: 36900
  download_size: 341303252
  dataset_size: 1558494402
- config_name: ru-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 109231457
    num_examples: 1864
  download_size: 47336785
  dataset_size: 109231457
- config_name: ru-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 1130341964
    num_examples: 1864
  download_size: 471570705
  dataset_size: 1130341964
- config_name: ru-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 2181971634
    num_examples: 37280
  download_size: 434295395
  dataset_size: 2181971634
- config_name: th-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 95553597
    num_examples: 1970
  download_size: 30775607
  dataset_size: 95553597
- config_name: th-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 857643516
    num_examples: 1970
  download_size: 228940982
  dataset_size: 857643516
- config_name: th-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 1892404150
    num_examples: 39400
  download_size: 223952474
  dataset_size: 1892404150
- config_name: zh-triplet
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 380393395
    num_examples: 10000
  download_size: 238703116
  dataset_size: 380393395
- config_name: zh-triplet-20
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative_1
    dtype: string
  - name: negative_2
    dtype: string
  - name: negative_3
    dtype: string
  - name: negative_4
    dtype: string
  - name: negative_5
    dtype: string
  - name: negative_6
    dtype: string
  - name: negative_7
    dtype: string
  - name: negative_8
    dtype: string
  - name: negative_9
    dtype: string
  - name: negative_10
    dtype: string
  - name: negative_11
    dtype: string
  - name: negative_12
    dtype: string
  - name: negative_13
    dtype: string
  - name: negative_14
    dtype: string
  - name: negative_15
    dtype: string
  - name: negative_16
    dtype: string
  - name: negative_17
    dtype: string
  - name: negative_18
    dtype: string
  - name: negative_19
    dtype: string
  - name: negative_20
    dtype: string
  splits:
  - name: train
    num_bytes: 4014540921
    num_examples: 10000
  download_size: 2517477273
  dataset_size: 4014540921
- config_name: zh-triplet-all
  features:
  - name: anchor
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 7592705148
    num_examples: 200000
  download_size: 2489491365
  dataset_size: 7592705148
configs:
- config_name: ar-triplet
  data_files:
  - split: train
    path: ar-triplet/train-*
- config_name: ar-triplet-20
  data_files:
  - split: train
    path: ar-triplet-20/train-*
- config_name: ar-triplet-all
  data_files:
  - split: train
    path: ar-triplet-all/train-*
- config_name: de-triplet
  data_files:
  - split: train
    path: de-triplet/train-*
- config_name: de-triplet-20
  data_files:
  - split: train
    path: de-triplet-20/train-*
- config_name: de-triplet-all
  data_files:
  - split: train
    path: de-triplet-all/train-*
- config_name: en-triplet
  data_files:
  - split: train
    path: en-triplet/train-*
- config_name: en-triplet-20
  data_files:
  - split: train
    path: en-triplet-20/train-*
- config_name: en-triplet-all
  data_files:
  - split: train
    path: en-triplet-all/train-*
- config_name: es-triplet
  data_files:
  - split: train
    path: es-triplet/train-*
- config_name: es-triplet-20
  data_files:
  - split: train
    path: es-triplet-20/train-*
- config_name: es-triplet-all
  data_files:
  - split: train
    path: es-triplet-all/train-*
- config_name: fr-triplet
  data_files:
  - split: train
    path: fr-triplet/train-*
- config_name: fr-triplet-20
  data_files:
  - split: train
    path: fr-triplet-20/train-*
- config_name: fr-triplet-all
  data_files:
  - split: train
    path: fr-triplet-all/train-*
- config_name: hi-triplet
  data_files:
  - split: train
    path: hi-triplet/train-*
- config_name: hi-triplet-20
  data_files:
  - split: train
    path: hi-triplet-20/train-*
- config_name: hi-triplet-all
  data_files:
  - split: train
    path: hi-triplet-all/train-*
- config_name: it-triplet
  data_files:
  - split: train
    path: it-triplet/train-*
- config_name: it-triplet-20
  data_files:
  - split: train
    path: it-triplet-20/train-*
- config_name: it-triplet-all
  data_files:
  - split: train
    path: it-triplet-all/train-*
- config_name: ja-triplet
  data_files:
  - split: train
    path: ja-triplet/train-*
- config_name: ja-triplet-20
  data_files:
  - split: train
    path: ja-triplet-20/train-*
- config_name: ja-triplet-all
  data_files:
  - split: train
    path: ja-triplet-all/train-*
- config_name: ko-triplet
  data_files:
  - split: train
    path: ko-triplet/train-*
- config_name: ko-triplet-20
  data_files:
  - split: train
    path: ko-triplet-20/train-*
- config_name: ko-triplet-all
  data_files:
  - split: train
    path: ko-triplet-all/train-*
- config_name: pt-triplet
  data_files:
  - split: train
    path: pt-triplet/train-*
- config_name: pt-triplet-20
  data_files:
  - split: train
    path: pt-triplet-20/train-*
- config_name: pt-triplet-all
  data_files:
  - split: train
    path: pt-triplet-all/train-*
- config_name: ru-triplet
  data_files:
  - split: train
    path: ru-triplet/train-*
- config_name: ru-triplet-20
  data_files:
  - split: train
    path: ru-triplet-20/train-*
- config_name: ru-triplet-all
  data_files:
  - split: train
    path: ru-triplet-all/train-*
- config_name: th-triplet
  data_files:
  - split: train
    path: th-triplet/train-*
- config_name: th-triplet-20
  data_files:
  - split: train
    path: th-triplet-20/train-*
- config_name: th-triplet-all
  data_files:
  - split: train
    path: th-triplet-all/train-*
- config_name: zh-triplet
  data_files:
  - split: train
    path: zh-triplet/train-*
- config_name: zh-triplet-20
  data_files:
  - split: train
    path: zh-triplet-20/train-*
- config_name: zh-triplet-all
  data_files:
  - split: train
    path: zh-triplet-all/train-*
language:
- ar
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- pt
- ru
- th
- zh
---

# Dataset Card for MLDR

This is a reformatting of the MLDR dataset used to train the [BGE-M3 model](https://huggingface.co/BAAI/bge-m3). See the full BGE-M3 dataset in [Shitao/bge-m3-data](https://huggingface.co/datasets/Shitao/bge-m3-data).

## Dataset Subsets

### `...-triplet` subset

* Columns: "anchor", "positive", "negative"
* Column types: `str`, `str`, `str`
* Examples:
    ```python
    {
      'anchor': '¿Cuál es el efecto de la dilución crema simple en los pelajes básicos de los caballos?',
      'positive': 'Gen crema\n\nPelajes resultantes\n\nTodos los caballos tienen dos copias del gen MATP: una de parte de la yegua y la otra de parte del Estal.\nLos pelajes básicos no tienen ningún alelo crema. Los pelajes dluïts crema simples se producen cuando se añade un alelo crema a pelajes básicos.\nEl negro se transforma en negro-ahumado (poco diferente del negro), el moreno pasa a pardo-ahumado (muy parecido al pardo pero con zonas amarillentas en lugar de rojas), el castaño se convierte bayo-crema (generalmente sin raya dorsal) y el alazán se convierte en palomino.\n\u200b\nLa dilución crema simple implica que los pelos rojos pasan a amarillentos o dorados, las crines rojas convierten blancas. Los pelos negros no cambian (o cambian muy poco) de color, ni tampoco las crines negras. En los simples diluidos crema el color de los ojos suele ser relativamente claro, de tonalidad avellana. Los doblemente diluidos crema, formados por dos alelos crema sobre los pelajes básicos, tienen un pelaje blanco roto sobre una piel ligeramente pigmentada. Y suelen tener ojos azules.\u200b Los caballos con 2 copias del. Alelo crema también exhiben rasgos específicos: pelajes de color blanco roto, ojos azules pálidos, y piel muy poco pigmentada. Estos caballos se llaman normalmente crema, perla, negro-crema y pardo-crema.\n\nCrema diluido crema heterocigótico (crema diluido crema simple)\n\nLos pelajes crema diluido simple (con un alelo crema único) mantienen una piel pigmentada y los ojos castaños. A veces los pollinos nacen con una piel más clara que se oscurece con los años. También hay casos de ojos más claros con la tonalidad de la ámbar. El observador poco avezado puede confundir algún diluido crema simple (por ejemplo, el bayo) con un pelaje diluido champagne (gen champagne. Los pollinos champagne nacen con una piel rosada-calabaza que se oscurece y se vuelve pecosa, especialmente en el hocico, alrededor de los ojos y en la zona de los genitales.\nEl pelaje palomino de color ocre con crines blancas resulta de la acción de un alelo crema sobre un pelaje alazán (rojo). La variante clásica con pelos del cuerpo dorados y cola y crin blancas es una de las más vistosas.\u200b Menos frecuentes son las variedades oscuras, a veces producidas por la acción combinada del al. Alelo crema y del patrón modificador "Sooty". También hay variantes muy pálidas, casi blancas, que se confunden con los pelajes crema. Los ojos y la piel sin embargo mantienen una tonalidad oscura.\nEl pelaje bayo con crines negras o isabello. Es el diluido crema simple del castaño. El alelo crema hace que todos los pelos que en el castaño serían rojos sean dorados o amarillentos en el bayo-crema. Los pelos y las crines negras no varían de color.\nLos caballos negro-ahumados, dilución simple de los negros, son muy difíciles de detectar a simple vista. Su aspecto exterior es prácticamente igual que el de los negros (La dilución crema no afecta a los pelos y crines negras en forma simple). La única manera segura es el análisis genético.\nEl pelaje pardo-ahumado Es el diluido crema simple del pardo. Se parece mucho al pardo con zonas amarillentas en el hocico y brazada y, a veces, los flancos. La dilución crema simple hace que las zonas rojas del pardo pasen a amarillas en el moreno-ahumado.\n\nRazas de caballos con gen crema\n\nEl gen crema se encuentra en muchas razas: American Quarter Horse, Morgan, Morabit, Tennessee Walker, Misuri Fox Trotterinant de Tennessee, Miniature horse, Akhal-Teke, Connemara, Poni Gales, Pura Sangre Inglés, PRE, PSL,...\nEn cambio, no hay gen crema en los caballos árabes actuales. Hay referencias antiguas que hablan de caballos famosos diluidos crema.\n\nDiluciones combinadas\n\nDebido a que los genes de las diversas diluciones son diferentes, un mismo caballo puede ser portador de dos o más diluciones. En cada caso las diluciones combinadas pueden producir pelajes difíciles de distinguir a simple vista y que exigen pruebas genéticas para determinar con seguridad.\n\nAspectos genéticos\n\nEl locus crema se sitúa en el exón 2 del gen MATP, un polimorfismo nucleótido simple resulta en el canje del ácido aspàrgic y el aspargina. (N153D).\u200b La prueba genética que ofrecen algunos laboratorios detecta esta mutación.\nLos genes "overo" ("frame overo" según la American Paint Horse Association) y "sabino" provocan manchas blancas interrumpiendo o limitando la migración de melanocitos desde la cresta neural, mientras que la mutación crema afecta a la naturaleza de los pigmentos producidos por los melanocitos. La dilución crema es un caso de hipomelanisme. La piel, los pelos y los ojos de los caballos diluidos crema conservan un cierto grado de pigmentación.\nAntes del mapeo del gen de crema, este locus se titulaba C para indicar "color". Hay dos alelos en la serie: el recesivo C, y el dominante C Cr. (Nota: En exposiciones simplificadas la notación es Cr para una copia crema y Cr/Cr para dos copias crema. Para evitar el uso de super-índice).\nLa dilución crema fue investigada formalmente por Adalsteinsson en 1974, con la conclusión de que la herencia de los pelajes palomino y bayo-crema seguía en los caballos islandeses seguía un modelo semi-dominante o dominante incompleto. Adalsteinsson observó, también, que en los diluidos heterocigóticos sólo se diluía la feomelanina.\u200b',
      'negative': 'Tuneladora\n\nUna tuneladora, T.B.M. (del inglés Tunnel Boring Machine) o minador a sección completa es una máquina capaz de excavar túneles a sección completa, a la vez que colabora en la colocación de la entibación para la sustentación del túnel si ésta es necesaria, ya sea de forma provisional o definitiva. \nLa excavación se realiza normalmente mediante una cabeza giratoria equipada con elementos de corte y accionada por motores hidráulicos (alimentados a su vez por motores eléctricos, dado que la alimentación general de la máquina se realiza con energía eléctrica), aun cuando también existen tuneladoras menos mecanizadas sin cabeza giratoria. El empuje necesario para adelantar se consigue mediante un sistema de gatos perimetrales que se apoyan en el último anillo de sostenimiento colocado o en zapatas móviles (denominadas grippers), accionados también por gatos que las empujan contra la pared del túnel, de forma que se consigue un punto fijo desde donde empujan. \nDetrás de los equipos de excavación y avance se sitúa el denominado "equipo de rezaga" de la tuneladora (o en denominación inglesa back up), constituido por una serie de plataformas arrastradas por la propia máquina y que, a menudo, ruedan sobre rieles que la misma tuneladora coloca, donde se alojan todos los equipos transformadores, de ventilación, depósitos de mortero y el sistema de evacuación del material excavado. \nLos rendimientos conseguidos con tuneladoras de cabeza giratoria son elevadísimos si se comparan con otros métodos de excavación de túneles, pero su uso no es rentable hasta una longitud mínima de túnel a excavar: hace falta amortizar el precio de la máquina y calcular el tiempo que se tarda en diseñarla, fabricarla, transportarla y montarla (que puede llegar a los dos años). Además, los túneles a excavar con tuneladora tienen que tener radios de curvatura elevados porque las máquinas no pueden hacer curvas cerradas, y la sección tiene que ser circular en túneles excavados con cabeza giratoria.\n\nTipos de tuneladoras\n\nSe distinguen dos grandes grupos: los topos y los escudos, aun cuando también existen tuneladoras mixtas como las que excavan actualmente la línea 9 del metro de Barcelona.\n\nTopos\n\nLos topos son tuneladoras diseñadas para excavar rocas duras o medianas, sin demasiadas necesidades de sostenimiento. Su diferencia fundamental con los escudos es que no están dotados de un cilindro de acero tras la rueda de corte que realiza la función de entibación provisional.\nLa fuerza de empuje se transmite a la cabeza de corte mediante cilindros (cilindros de empuje). La reacción producida se transmite al hastial del túnel mediante los grippers (fuerza de anclaje). Los grippers también compensan el par producido por la cabeza de corte, que se transmite a éstos a través de la viga principal.\nCuando se ha terminado un ciclo de avance, se necesita reposicionar las zapatas de agarre (grippers), para la cual se apoya la viga principal en el apoyo trasero. Una vez anclados los grippers en su nuevo emplazamiento, se libera el apoyo trasero y se inicia un nuevo ciclo de avance.\n\nDoble Escudo\n\nOtra modalidad de tuneladora es la denominada Doble Escudo, capaz de trabajar como topo o como escudo, en función de la calidad del macizo rocoso, siendo la mejor solución para macizos con tramos de tipología variable suelo-roca. En este tipo de tuneladoras el escudo está dividido en dos partes, la delantera en la que se encuentra la cabeza de corte, y la zona trasera en la que se realiza el montaje del anillo de dovelas.\nEl movimiento de estas dos partes del escudo es independiente, situándose los "grippers" en un hueco abierto entre ambas, por lo que la cabeza puede excavar mientras que en la cola del escudo se van montando los anillos de dovelas. De esta manera los rendimientos alcanzados con este sistema son mucho mayores que con un escudo simple. Este sistema se aplica en aquellos terrenos capaces de resistir la presión que transmiten los “grippers”. Al mismo tiempo que los cilindros de empuje principal impulsan hacia delante el escudo de cabeza y la rueda de corte realiza la excavación, en el escudo trasero se procede al montaje de un nuevo anillo de dovelas de sostenimiento al abrigo del mismo. \nCuando el terreno es más débil y no es capaz de resistir la presión de los “grippers”, la tuneladora funciona como escudo simple, cerrándose el hueco de los "grippers", y apoyándose la tuneladora, mediante unos cilindros auxiliares, en el último anillo colocado, para así obtener la reacción necesaria para el empuje de la cabeza de corte (es decir, como trabaja un escudo normal). Por ello, trabajando en modo escudo, no es posible simultanear la excavación con el montaje del anillo de dovelas.'
    }
    ```
* Collection strategy: Reading the MLDR jsonl files in [Shitao/bge-m3-data](https://huggingface.co/datasets/Shitao/bge-m3-data) and taking only the first positive and first negative.
* Deduplified: No

### `...-triplet-20` subset

* Columns: "anchor", "positive", "negative_1", ..., "negative_20"
* Column types: `str`, ..., `str`
* Examples:
    ```python
    {
      'anchor': '¿Cuál es el efecto de la dilución crema simple en los pelajes básicos de los caballos?',
      'positive': 'Gen crema\n\nPelajes resultantes\n\nTodos los caballos tienen dos copias del gen MATP: una de parte de la yegua y la otra de parte del Estal.\nLos pelajes básicos no tienen ningún alelo crema. Los pelajes dluïts crema simples se producen cuando se añade un alelo crema a pelajes básicos.\nEl negro se transforma en negro-ahumado (poco diferente del negro), el moreno pasa a pardo-ahumado (muy parecido al pardo pero con zonas amarillentas en lugar de rojas), el castaño se convierte bayo-crema (generalmente sin raya dorsal) y el alazán se convierte en palomino.\n\u200b\nLa dilución crema simple implica que los pelos rojos pasan a amarillentos o dorados, las crines rojas convierten blancas. Los pelos negros no cambian (o cambian muy poco) de color, ni tampoco las crines negras. En los simples diluidos crema el color de los ojos suele ser relativamente claro, de tonalidad avellana. Los doblemente diluidos crema, formados por dos alelos crema sobre los pelajes básicos, tienen un pelaje blanco roto sobre una piel ligeramente pigmentada. Y suelen tener ojos azules.\u200b Los caballos con 2 copias del. Alelo crema también exhiben rasgos específicos: pelajes de color blanco roto, ojos azules pálidos, y piel muy poco pigmentada. Estos caballos se llaman normalmente crema, perla, negro-crema y pardo-crema.\n\nCrema diluido crema heterocigótico (crema diluido crema simple)\n\nLos pelajes crema diluido simple (con un alelo crema único) mantienen una piel pigmentada y los ojos castaños. A veces los pollinos nacen con una piel más clara que se oscurece con los años. También hay casos de ojos más claros con la tonalidad de la ámbar. El observador poco avezado puede confundir algún diluido crema simple (por ejemplo, el bayo) con un pelaje diluido champagne (gen champagne. Los pollinos champagne nacen con una piel rosada-calabaza que se oscurece y se vuelve pecosa, especialmente en el hocico, alrededor de los ojos y en la zona de los genitales.\nEl pelaje palomino de color ocre con crines blancas resulta de la acción de un alelo crema sobre un pelaje alazán (rojo). La variante clásica con pelos del cuerpo dorados y cola y crin blancas es una de las más vistosas.\u200b Menos frecuentes son las variedades oscuras, a veces producidas por la acción combinada del al. Alelo crema y del patrón modificador "Sooty". También hay variantes muy pálidas, casi blancas, que se confunden con los pelajes crema. Los ojos y la piel sin embargo mantienen una tonalidad oscura.\nEl pelaje bayo con crines negras o isabello. Es el diluido crema simple del castaño. El alelo crema hace que todos los pelos que en el castaño serían rojos sean dorados o amarillentos en el bayo-crema. Los pelos y las crines negras no varían de color.\nLos caballos negro-ahumados, dilución simple de los negros, son muy difíciles de detectar a simple vista. Su aspecto exterior es prácticamente igual que el de los negros (La dilución crema no afecta a los pelos y crines negras en forma simple). La única manera segura es el análisis genético.\nEl pelaje pardo-ahumado Es el diluido crema simple del pardo. Se parece mucho al pardo con zonas amarillentas en el hocico y brazada y, a veces, los flancos. La dilución crema simple hace que las zonas rojas del pardo pasen a amarillas en el moreno-ahumado.\n\nRazas de caballos con gen crema\n\nEl gen crema se encuentra en muchas razas: American Quarter Horse, Morgan, Morabit, Tennessee Walker, Misuri Fox Trotterinant de Tennessee, Miniature horse, Akhal-Teke, Connemara, Poni Gales, Pura Sangre Inglés, PRE, PSL,...\nEn cambio, no hay gen crema en los caballos árabes actuales. Hay referencias antiguas que hablan de caballos famosos diluidos crema.\n\nDiluciones combinadas\n\nDebido a que los genes de las diversas diluciones son diferentes, un mismo caballo puede ser portador de dos o más diluciones. En cada caso las diluciones combinadas pueden producir pelajes difíciles de distinguir a simple vista y que exigen pruebas genéticas para determinar con seguridad.\n\nAspectos genéticos\n\nEl locus crema se sitúa en el exón 2 del gen MATP, un polimorfismo nucleótido simple resulta en el canje del ácido aspàrgic y el aspargina. (N153D).\u200b La prueba genética que ofrecen algunos laboratorios detecta esta mutación.\nLos genes "overo" ("frame overo" según la American Paint Horse Association) y "sabino" provocan manchas blancas interrumpiendo o limitando la migración de melanocitos desde la cresta neural, mientras que la mutación crema afecta a la naturaleza de los pigmentos producidos por los melanocitos. La dilución crema es un caso de hipomelanisme. La piel, los pelos y los ojos de los caballos diluidos crema conservan un cierto grado de pigmentación.\nAntes del mapeo del gen de crema, este locus se titulaba C para indicar "color". Hay dos alelos en la serie: el recesivo C, y el dominante C Cr. (Nota: En exposiciones simplificadas la notación es Cr para una copia crema y Cr/Cr para dos copias crema. Para evitar el uso de super-índice).\nLa dilución crema fue investigada formalmente por Adalsteinsson en 1974, con la conclusión de que la herencia de los pelajes palomino y bayo-crema seguía en los caballos islandeses seguía un modelo semi-dominante o dominante incompleto. Adalsteinsson observó, también, que en los diluidos heterocigóticos sólo se diluía la feomelanina.\u200b',
      'negative_1': 'Tuneladora\n\nUna tuneladora, T.B.M. (del inglés Tunnel Boring Machine) o minador a sección completa es una máquina capaz de excavar túneles a sección completa, a la vez que colabora en la colocación de la entibación para la sustentación del túnel si ésta es necesaria, ya sea de forma provisional o definitiva. \nLa excavación se realiza normalmente mediante una cabeza giratoria equipada con elementos de corte y accionada por motores hidráulicos (alimentados a su vez por motores eléctricos, dado que la alimentación general de la máquina se realiza con energía eléctrica), aun cuando también existen tuneladoras menos mecanizadas sin cabeza giratoria. El empuje necesario para adelantar se consigue mediante un sistema de gatos perimetrales que se apoyan en el último anillo de sostenimiento colocado o en zapatas móviles (denominadas grippers), accionados también por gatos que las empujan contra la pared del túnel, de forma que se consigue un punto fijo desde donde empujan. \nDetrás de los equipos de excavación y avance se sitúa el denominado "equipo de rezaga" de la tuneladora (o en denominación inglesa back up), constituido por una serie de plataformas arrastradas por la propia máquina y que, a menudo, ruedan sobre rieles que la misma tuneladora coloca, donde se alojan todos los equipos transformadores, de ventilación, depósitos de mortero y el sistema de evacuación del material excavado. \nLos rendimientos conseguidos con tuneladoras de cabeza giratoria son elevadísimos si se comparan con otros métodos de excavación de túneles, pero su uso no es rentable hasta una longitud mínima de túnel a excavar: hace falta amortizar el precio de la máquina y calcular el tiempo que se tarda en diseñarla, fabricarla, transportarla y montarla (que puede llegar a los dos años). Además, los túneles a excavar con tuneladora tienen que tener radios de curvatura elevados porque las máquinas no pueden hacer curvas cerradas, y la sección tiene que ser circular en túneles excavados con cabeza giratoria.\n\nTipos de tuneladoras\n\nSe distinguen dos grandes grupos: los topos y los escudos, aun cuando también existen tuneladoras mixtas como las que excavan actualmente la línea 9 del metro de Barcelona.\n\nTopos\n\nLos topos son tuneladoras diseñadas para excavar rocas duras o medianas, sin demasiadas necesidades de sostenimiento. Su diferencia fundamental con los escudos es que no están dotados de un cilindro de acero tras la rueda de corte que realiza la función de entibación provisional.\nLa fuerza de empuje se transmite a la cabeza de corte mediante cilindros (cilindros de empuje). La reacción producida se transmite al hastial del túnel mediante los grippers (fuerza de anclaje). Los grippers también compensan el par producido por la cabeza de corte, que se transmite a éstos a través de la viga principal.\nCuando se ha terminado un ciclo de avance, se necesita reposicionar las zapatas de agarre (grippers), para la cual se apoya la viga principal en el apoyo trasero. Una vez anclados los grippers en su nuevo emplazamiento, se libera el apoyo trasero y se inicia un nuevo ciclo de avance.\n\nDoble Escudo\n\nOtra modalidad de tuneladora es la denominada Doble Escudo, capaz de trabajar como topo o como escudo, en función de la calidad del macizo rocoso, siendo la mejor solución para macizos con tramos de tipología variable suelo-roca. En este tipo de tuneladoras el escudo está dividido en dos partes, la delantera en la que se encuentra la cabeza de corte, y la zona trasera en la que se realiza el montaje del anillo de dovelas.\nEl movimiento de estas dos partes del escudo es independiente, situándose los "grippers" en un hueco abierto entre ambas, por lo que la cabeza puede excavar mientras que en la cola del escudo se van montando los anillos de dovelas. De esta manera los rendimientos alcanzados con este sistema son mucho mayores que con un escudo simple. Este sistema se aplica en aquellos terrenos capaces de resistir la presión que transmiten los “grippers”. Al mismo tiempo que los cilindros de empuje principal impulsan hacia delante el escudo de cabeza y la rueda de corte realiza la excavación, en el escudo trasero se procede al montaje de un nuevo anillo de dovelas de sostenimiento al abrigo del mismo. \nCuando el terreno es más débil y no es capaz de resistir la presión de los “grippers”, la tuneladora funciona como escudo simple, cerrándose el hueco de los "grippers", y apoyándose la tuneladora, mediante unos cilindros auxiliares, en el último anillo colocado, para así obtener la reacción necesaria para el empuje de la cabeza de corte (es decir, como trabaja un escudo normal). Por ello, trabajando en modo escudo, no es posible simultanear la excavación con el montaje del anillo de dovelas.',
      'negative_2': 'Barrera intestinal\n\nLa barrera intestinal, también conocida como la barrera mucosa intestinal, se refiere a la propiedad de la mucosa intestinal que asegura la contención adecuada de contenidos luminales indeseables dentro del intestino mientras preserva la capacidad de absorber nutrientes. La separación que esta proporciona entre el cuerpo y la tripa impide la translocación incontrolada de contenidos  luminales al propio cuerpo. Su rol en la protección de los tejidos mucosales y el sistema circulatorio de la exposición a moléculas pro-inflamatorias, tales como microorganismos, toxinas, y antígenos es vital para el mantenimiento de la salud y bienestar.\u200b\u200b\u200b La disfunción de la barrera mucosa intestinal ha sido implicada en numerosas condiciones de salud tales como: alergias alimentarias, infecciones microbianas, síndrome del intestino irritable, enfermedad inflamatoria intestinal, enfermedad celiaca, síndrome metabólico, enfermedad del hígado graso no-alcohólico, diabetes, y choque séptico.\u200b\n\nComposición\n\nLa barrera intestinal es una entidad heterogénea compuesta de elementos físicos, bioquímicos e inmunes elaborados por la mucosa intestinal. El componente central es el epitelio intestinal, el cual proporciona separación física entre el lumen y el cuerpo. La secreción de varias moléculas al lumen refuerza la función de la barrera en el lado extra-epitelial, mientras una variedad de células inmunes proporciona protección adicional bajo la capa epitelial.\u200b\n\nCapa(s) de moco\n\nEl moco forma una capa (o capas, en el caso del colon) que separa el grueso del contenido luminal del epitelio intestinal. El moco consta de un gel hidratado altamente glicosilado formado por moléculas de mucina que son secretadas por células caliciformes. El moco impide que las partículas grandes entren en contacto con la capa de células epiteliales mientras deja pasar las moléculas pequeñas. El moco también facilita el paso del contenido luminal a lo largo de la longitud de los intestinos, protege las células epiteliales de las enzimas digestivas, e impide el contacto directo de los microorganismos con la capa epitelial.\u200b\n\nEl epitelio intestinal\n\nEl epitelio intestinal es el componente más importante de la barrera intestinal. Consta de la capa de células epiteliales que forran el intestino. Crucial para formar una barrera eficaz es el control preciso del transporte paracelular (una ruta para la translocación de moléculas entre las células). El sellado del espacio entre las células adyacentes está mediado por los complejos formados por conexiones de proteína elaborados por cada célula individual. Además de su función protectora, el epitelio intestinal controla la absorción selectiva de iones beneficiosos, nutrientes, y otras sustancias del lumen al cuerpo.\n\nMicrobiota\n\nLas especies microbianas comensales que habitan la tripa son consideradas por algunos como parte de la barrera intestinal. La microbiota puede influir la función de la barrera tanto directamente, estimulando la proliferación de células epiteliales y la secreción de IL-8, e indirectamente produciendo ácidos grasos de cadena corta, los cuales son una fuente de energía importante para las células epiteliales colónicas.\n\nBilis y ácido gástrico\n\nLa bilis producida por el hígado para ayudar en la digestión de los lípidos tiene propiedades bactericidas. El ácido gástrico producido por el estómago también puede matar microorganismos.\u200b Ambos contribuyen a la función de la barrera intestinal a pesar de que no son producidos por la mucosa intestinal.\n\nDefensinas\n\nUnas células secretoras epiteliales especializadas  llamadas células de Paneth secretan cantidades abundantes de α-defensinas humanas al lumen intestinal de los individuos sanos.\u200b\n\nLisozima\n\nLa lisozima es otra molécula defensiva secretada por las células de Paneth al lumen.\u200b\n\nProteína 3 gamma regenerante derivada de islotes  (Reg3γ)\n\nReg3γ es una lectina antibacterial secretada por las células de Paneth que sirve para impedir que los microorganismos entren en contacto con la capa epithelial.\n\nPéptidos antimicrobiales\n\nLos péptidos antimicrobiales (PAM), los cuales son una variedad diversa de moléculas que matan bacterias y hongos, son secretados por las células de Paneth  al lumen.\n\nInmunoglobulina A secretora (sIgA )\n\nLa inmunoglobulina A secretora (IgAs) es producida por células plasmáticas en la lamina propria y es transportada al lumen por las células epiteliales intestinales. La IgAs bloquea receptores epiteliales específicos en los patógenos, impidiendo así su unión a las células epiteliales.\n\nInmunidad celular\n\nUna variedad de células inmunes reside en la lámina propria, la cual yace bajo el epitelio intestinal. Estas incluyen células dendríticas, macrófagos, linfocitos intraepiteliales, linfocitos T reguladores, linfocitos TCD4+, linfocitos B, y células plasmáticas.\u200b Esta población proporciona protección inmune que está caracterizada por la detección y muerte rápida de los microorganismos que penetran el epitelio intestinal.\u200b\n\nFisiología\n\nLa integridad de la barrera intestinal es flexible y se ha mostrado que múltiples mecanismos son capaces de modular la permeabilidad intestinal (una medida de la función de la barrera intestinal).\u200b Los factores moduladores incluyen citocinas, células inmunes, y factores exógenos.\n\nMedida\n\nLa permeabilidad intestinal es una medida de la función de la barrera mucoso intestinal y está definida como "la facilidad con qué el epitelio intestinal permite que las moléculas atraviesen por difusión pasiva no mediada."\u200b La permeabilidad en este sentido está mayoritariamente relacionada al paso medible de iones y moléculas inertes pequeñas. Los métodos estándares para la medición incluyen la resistencia eléctrica del tejido para pruebas in vitro y el paso de moléculas inertes ingeridas de pesos moleculares específicos a la orina para pruebas en vivo.\u200b\u200b Por ejemplo, la prueba in vivo que utiliza lactulosa / manitol consiste en la ingestión de 5 g de lactulosa y 2 g  de manitol seguido por la determinación de las concentraciones urinarias de lactulosa y manitol 5 horas después de la ingestión. El porcentaje de excreción de lactulosa y la proporción de manitol lactulosa en la orina son calculados y utilizados como una medida de la permeabilidad intestinal.\u200b\n\nImportancia clínica\n\nUna barrera intestinal perturbada puede permitir el paso de microbios, productos microbianos, y antígenos extraños a la mucosa y al propio cuerpo. Esto puede resultar en la activación del sistema inmune y la secreción de mediadores de la inflamación. Ciertas respuestas inmunes pueden, a su vez, causar daño celular que podría resultar en una disfunción adicional de la barrera. Los defectos en la función de la barrera de la mucosa intestinal con el acompañamiento de la translocación de los microbios y sus productos se han relacionado con una variedad de condiciones, algunas de las cuales se cree que además requieren de una predisposición genética.\u200b Pueden resultar tanto trastornos autoinmunes intestinales como extraintestinales. Se piensa que la disfunción de la barrera intestinal es una precondición para, y factor exacerbante de numerosas enfermedades autoinmunes e inflamatorias, incluyendo las alergias a los alimentos, las enfermedades inflamatorias intestinales,la enfermedad celíaca y la diabetes.\n\nAlergias alimentarias\n\nLa disfunción de la barrera intestinal puede ser un factor crítico para las sensibilizaciones a los antígenos y la fase efectora anafiláctica mediada por IgE/mastocitos de las alergias a los alimentos. El desarrollo de las alergias alimentarias depende de que el antígeno entre en contacto con los componentes del sistema inmunológico de las mucosas. Esto lleva a la sensibilización por el antígeno y a la producción de antígenos específicos CD4+ células Th2 y  de IgE. La hipótesis es que la disfunción de la barrera intestinal permite a los antígenos de la dieta cruzar la barrera intestinal, entrar en contacto con el sistema inmunológico de las mucosas, y desencadenar una respuesta inmune específica para el antígeno.\nLa función reducida de la barrera intestinal se correlaciona con la severidad de los síntomas experimentados por los afectados por las alergias alimentarias. La provocación oral con el alergeno implicado resulta en un aumento de la proporción lactulosa/manitol en la orina (una medida de la permeabilidad intestinal).\n\nLa enfermedad inflamatoria intestinal\n\nUn modelo emergente de la patogénesis de la enfermedad inflamatoria intestinal (EII) postula tres factores previos necesarios: 1) la degradación de la función de la barrera intestinal, 2) desplazamiento del contenido luminal a la lámina propia y la posterior exposición a las células inmunes, y 3) una inadecuada respuesta inmune. Aunque la disfunción de la barrera intestinal está claramente implicada en el desarrollo de la enfermedad inflamatoria intestinal, no está claro lo que inicia el círculo vicioso que conduce a la exacerbación de la enfermedad. Sin embargo, hay un creciente cuerpo de evidencia que implica al aumento de la permeabilidad intestinal como principal factor etiológico de la patogénesis de la enfermedad inflamatoria intestinal.\n\nLa enfermedad celíaca\n\nLa función alterada de la barrera intestinal puede jugar un papel en el desarrollo de la enfermedad celíaca. Al permitir que la gliadina, el agente causativo de la enfermedad celíaca, cruce la barrera intestinal, la activación inapropiada del sistema inmune puede ocurrir. Se ha mostrado que los enfermos de enfermedad celíaca  tienen permeabilidad intestinal elevada y uniones estrechas alteradas. Además, estas alteraciones persisten en los pacientes que tienen éxito en mantener una dieta libre de gluten. Asimismo, los datos existentes demuestran que el aumento de la permeabilidad intestinal se presenta antes de la aparición de la enfermedad celíaca.\n\nLa diabetes tipo 1\n\nUna combinación de genética, desregulación de la función de la barrera intestinal, y respuestas inmunes inapropiadas ha sido conjeturado que desempeña un papel en la diabetes tipo 1. La permeabilidad intestinal elevada se ha reportado que se observa en los pacientes al comienzo de la enfermedad. El incremento resultante de la exposición a los antígenos puede desencadenar la destrucción autoinmune de las células beta en el páncreas.\n\nOtras condiciones\n\nLos defectos en la función de la barrera de la mucosa intestinal también han sido implicados en el síndrome del intestino irritable, síndrome metabólico, hígado graso no alcohólico, y el choque séptico.\n\nTensión\n\nLa tensión sicológica y física puede inducir una variedad de alteraciones en la función intestinal. Estos incluyen cambios en la motilidad intestinal, permeabilidad intestinal, flujo iónico, balance de fluidos y secreción de moco. Además, la tensión aguda y crónica en modelos animales ha mostrado que la tensión puede causar una degradación de la función de la barrera intestinal. La tensión psicológica puede influir en el resultado clínico de la enfermedad inflamatoria intestinal y del síndrome del intestino irritable. Ha sido mostrado que la tensión prolongada está positivamente asociada con una propensión aumentada para la recaída de la colitis ulcerosa.\n\nHistoria\n\nCummings adoptó el término barrera mucosal en 2004 para describir la "compleja estructura que separa el medio interno del entorno luminal".\u200b Más recientemente, la barrera intestinal ha sido utilizada por gastroenterologistas, immunologistas y microbiologistas para enfatizar el componente del intestino que protege el cuerpo de los microorganismos y sus toxinas.',
      'negative_3': 'Orexina\n\nFunción\n\nSe sugirió inicialmente que el sistema orexina/hipocretina estaba implicado en la estimulación de toma de alimentos. Esta opinión se basó en el descubrimiento de que la administración central de la orexina-A/hipocretina-1 incrementa la toma de alimentos. Además, estimula el insomnio y el gasto de energía.\n\nVigilia (estado de alerta)\n\nLa orexina parece promover el estado de vigilia. Recientes estudios indican que un papel importante del sistema orexina/hipocretina es de integrar las influencias metabólicas del ritmo circadiano y de la deuda de sueño para determinar si un animal debe estar dormido o despierto y activo. Las neuronas orexina/hipocretina excitan fuertemente varios núcleos del cerebro que tienen roles importantes en el insomnio, cómo son los sistemas de dopamina, norepinefrina, histamina y acetilcolina, y parecen jugar un papel importante en la estabilización del insomnio y del sueño.\nEl descubrimiento que una mutación del receptor de la orexina/hipocretina causa trastornos del sueño caninos cómo la narcolepsia\u200b en dóbermans pinscher indicó posteriormente el papel mayor de este sistema en la regulación del sueño.\nLa carencia en el gen de la orexina producida por knockout genético en ratones también causó narcolepsia.\u200b Permutando frecuentemente y rápidamente entre el sueño y la vigilia, estos ratones mostraron muchos de los síntomas de la narcolepsia. Investigadores están usando este modelo animal de narcolepsia para estudiar la enfermedad.\u200b La narcolepsia resulta en una excesiva falta de sueño diaria, incapacidad para mantener la vigilia durante el día (y el sueño por la noche), y la cataplejía, que es la pérdida del tonus muscular en respuesta a las emociones fuertes, generalmente positivas. Los perros que carecen de un receptor funcional para la orexina/hipocretina tienen narcolepsia, mientras que los animales y la gente falta del neuropéptido mismo de la orexina/hipocretina también tienen narcolepsia.\nLa administración central de la orexina-A/hipocretina-1 promueve fuertemente el estado de vigilia, aumenta la temperatura corporal y la locomoción y obtiene un fuerte incremento en el gasto de energía. La privación de sueño también incrementa la transmisión de orexina-A/hipocretina-1. El sistema orexina/hipocretina podría así pues ser más importante en la regulación del gasto de energía que en la toma de alimentos. De hecho, los pacientes narcolépticos deficientes en orexina/hipocretina aumentaron más bien los niveles de obesidad que disminuyeron el IMC, lo que hubiese podido ser lo esperado si la orexina/hipocretina hubiese sido primeramente un péptido de estimulación del apetito. Otra indicación que el déficit de orexina/hipocretina causa narcolepsia es que privando monos de sueño durante 30-36 horas y luego inyectándoles el neuroquímico, se observó un alivio de las deficiencias cognitivas generalmente observadas con tan gran cantidad de pérdida de sueño.\u200b\u200b\nEn los humanos, la narcolepsia está asociada con una variante específica del complejo de los antígenos leucocitarios humanos (HLA).\u200bPor otro lado, un amplio análisis de genoma mostró que, además de la variante HLA, la narcolepsia humana también exhibe una mutación genética específica del locus alpha de los receptores de linfocito T.\u200b En definitiva, estas anomalías genéticas causan que el sistema autoimmune ataque y mate las neuronas críticas de hipocretina. De ahí que la ausencia de neuronas productoras de hipocretinas en narcolépticos humanos podría ser el resultado de un trastorno autoimmune.\u200b\n\nEstado de alerta (vigilia), Beta-amiloide y enfermedad de Alzheimer\n\nUna relación entre la orexina y la enfermedad de Alzheimer ha sido sugerida recientemente.\u200b La enigmática proteína Beta-amiloide se propaga con el tiempo en el cerebro y está correlacionada con la enfermedad de Alzheimer. El reciente estudio muestra que la expresión de la Beta-amiloide aumenta durante el día y decae por la noche, siendo estos hechos controlados por la orexina.\u200b La privación de sueño es posiblemente una causa del desarrollo de placas de Beta-amiloide.\u200b Se sugiere que algunas drogas que bloquean los receptores de orexina podrían ser usados para modular el aumento de Beta-amiloide.\u200b Esta investigación también sugiere que manteniendo apropiados periodos de sueño o de vigilia se podría prevenir la enfermedad de Alzheimer, asumiendo que 1) la Beta-amiloide es la causa de la enfermedad de Alzheimer y 2) que los ciclos sueño-vigilia influyen más en el incremento de Beta-amiloide en los cerebros de los enfermos de Alzheimer que otros factores- dos hechos que no han sido probados.\n\nToma de alimentos\n\nLa orexina incrementa el ansia por la comida, e interactúa con sustancias que promueven su producción.\nLa leptina es una hormona producida por las células adiposas y actúa cómo una regulación interna a largo plazo del estado de energía.\nLa ghrelina es un factor a corto plazo secretado por el estómago justo antes de una comida esperada, y promueve fuertemente la toma de alimentos.\nRecientemente se ha demostrado que las células que producen hipocretina están inhibidas por la leptina( mediante el receptor de leptina), pero son activadas por la grelina y la hipoglucemia( la glucosa inhibe la producción de orexina). La orexina/hipocretina, en 2007, es sospechosa de ser un importante enlace entre el metabolismo y la regulación del sueño. Tal relación ha sido sospechada desde hace mucho tiempo. Esta opinión se basaba en la observación que privaciones de largos plazos de sueño en roedores incrementaban dramáticamente la toma de alimentos y el metabolismo energético, i.e., catabolismo, con unas consecuencias letales a largo plazo.\n\nPotencial farmacológico\n\nLa investigación en orexina/hipocretina aún está en una fase inicial, aunque varios científicos creen que las drogas basadas en orexina/hipocretina podrían ayudar a los narcolépticos e incrementar la vigilancia en el cerebro sin los efectos secundarios de las anfetaminas.\nLa investigación preliminar fue conducida para mostrar el potencial de los bloqueadores de las orexinas en el tratamiento del alcoholismo. Ratas de laboratorio a quiénes se dio drogas que apuntan al sistema de las orexinas perdieron interés en el alcohol a pesar de que se les dio acceso libre en los experimentos\u200b\u200b\nUn estudio ha reportado que el trasplante de neuronas de orexina/hipocretina en la formación pontina reticulada es factible, indicando el desarrollo de las estrategias alternativas terapéuticas además de las intervenciones farmacológicas que tratan la narcolepsia.\u200b\nYa se había observado que los receptores de la hipocretina-1 regulan la recaída en la búsqueda de la cocaína, pero ahora un nuevo estudio investiga su relación con la nicotina gracias a unas experiencias en ratas. Bloqueando el receptor de la hipocretina-1 con bajas dosis de los antagonistas selectivos SB-334,867, la auto administración de nicotina disminuye, al igual que la motivación para buscar y obtener la droga. El estudio mostró que bloqueando los receptores en la ínsula disminuía la auto administración, pero no bloqueando los receptores en el adyacente córtex somatosensor. La más fuerte disminución en la auto administración fue encontrada cuando se bloquearon todos los receptores de hipocretina-1 del cerebro cómo si fuera un todo. Una explicación razonada de este estudio es el hecho de que la ínsula esté implicada en la regulación de los sentimientos de ansia. La ínsula contiene los receptores de la hipocretina-1. Ha sido recogido que los fumadores que sufren daños en la ínsula pierden el deseo de fumar.\u200b\n\nHistoria y nomenclatura\n\nEn 1996, V.T. Gautvik, Luis de Lecea y colegas suyos informaron del descubrimiento de algunos genes en el cerebro de ratas, incluyendo uno que apodaron “clon 35”. Trabajaron mostrando que la expresión del clon 35 se limitaba al hipotálamo lateral.\u200b Dos años después identificarían los dos productos genéticos del clon 35 cómo las hipocretina.\nMasashi Yanagisawa y colegas suyos de la Universidad de Texas del Centro Médico del Suroeste en Dallas, acuñaron el término orexina para reflectar la actividad orexigénica( estimulación del apetito) de estas hormonas. En su ensayo de 1998 ( con los derechos atribuidos a Sakurai y sus colegas), en el que describen estas hormonas, también informaron sobre el descubrimiento de los dos receptores de orexina, apodados OX1R y OX2R.\nLuis de Lecea, Thomas Kilduff y otros compañeros también informaron sobre el descubrimiento de estos mismos péptidos, apodándolos hipocretina para indicar que son sintetizados en el hipotálamo y para reflectar su estructura similar a la hormona secretina (i.e., secretina hipotalámica). Ese era el mismo grupo que había identificado inicialmente el clon 35 dos años atrás.\u200b\u200b\nEl nombre de esta familia de péptidos es actualmente inestable. El nombre “orexina” ha sido rechazado por algunos por causa de la evidencia que los efectos orexigénicos de estos péptidos podrían ser secundarios o triviales (i.e., la hipocretina induce a los sujetos a comer más porque están más despiertos), aunque esta cuestión tampoco ha quedado resuelta, mientras que otros grupos mantienen que el nombre “hipocretina” es inapropiado, apuntando que muchos neuropéptidos tienen nombres que no están relacionados con sus funciones más importantes, y que el hecho de estar despierto es uno de los factores importantes del comportamiento alimentario. Ambos nombres, “orexina” y “hipocretina” persistirán seguramente apareciendo en los trabajos publicados hasta que un nombre preferente sea aceptado por la comunidad científica.\n\nInteracciones con otros sistemas de neurotransmisión\n\nHa sido mostrado que las neuronas orexinérgicas son sensibles a la entrada de receptores metabotrópicos de glutamato del grupo III,\u200b de receptores de adenosina A1,\u200b de receptores muscarínicos M3,\u200b de receptores de serotonina 5-HT1A,\u200b de receptores de los neuropéptidos Y,\u200b de los receptores de la colecistoquinina A,\u200b de las catecolaminas,\u200b\u200b y también de la ghrelina, la leptina y la glucosa.\u200b Las neuronas orexinérgicas mismas regulan la liberación de la acetilcolina,\u200b\u200b de la serotonina y de la noradrenalina,\u200b por lo que a pesar de la relativa pequeña cantidad de neuronas orexinérgicas en comparación con otros sistemas de neurotransmisión del cerebro, este sistema juega un papel regulador clave y se requiere una extensa investigación para revelar sus detalles. Las orexinas actúan en los receptores de las proteínas-acopladas Gq señalizando las vías de transducción a través de la fosfolipasa C (PLC), tanto las dependientes como las independientes de calcio. Esta transducción incluye la activación de los intercambiadores electrogénicos sodio-calcio (NCX), probablemente la activación de los canales de calcio dependientes de voltaje de tipo L, el cierre de la proteína G activada hacia dentro que permite rectificar los canales de potasio, y la activación de las proteínas quinasas, incluidas la quinasa C (PKC), la quinasa A (PKA) y una quinasa asociada a los mitógenos( MAPK). Las acciones postsinápticas de las orexinas en las numerosas células blanco neuronales a través del CNS son casi solo excitantes.\u200b',
      'negative_4': 'Célula\n\nLa célula (del latín cellula, diminutivo de cella, ‘hueco’)\u200b es la unidad morfológica y funcional de todo ser vivo. De hecho, la célula es el elemento de menor tamaño que puede considerarse vivo.\u200b De este modo, puede clasificarse a los organismos vivos según el número de células que posean: si solo tienen una, se les denomina unicelulares (como pueden ser los protozoos o las bacterias, organismos microscópicos); si poseen más, se les llama pluricelulares. En estos últimos el número de células es variable: de unos pocos cientos, como en algunos nematodos, a cientos de billones (10¹⁴), como en el caso del ser humano. Las células suelen poseer un tamaño de 10\xa0µm y una masa de 1\xa0ng, si bien existen células mucho mayores.\nLa teoría celular, propuesta en 1838 para los vegetales y en 1839 para los animales,\u200b por Matthias Jakob Schleiden y Theodor Schwann, postula que todos los organismos están compuestos por células, y que todas las células derivan de otras precedentes. De este modo, todas las funciones vitales emanan de la maquinaria celular y de la interacción entre células adyacentes; además, la tenencia de la información genética, base de la herencia, en su ADN permite la transmisión de aquella de generación en generación.\u200b\nLa aparición del primer organismo vivo sobre la Tierra suele asociarse al nacimiento de la primera célula. Si bien existen muchas hipótesis que especulan cómo ocurrió, usualmente se describe que el proceso se inició gracias a la transformación de moléculas inorgánicas en orgánicas bajo unas condiciones ambientales adecuadas; tras esto, dichas biomoléculas se asociaron dando lugar a entes complejos capaces de autorreplicarse. Existen posibles evidencias fósiles de estructuras celulares en rocas datadas en torno a 4 o 3,5 miles de millones de años (giga-años o Ga.).\u200b\u200b\u200b Se han encontrado evidencias muy fuertes de formas de vida unicelulares fosilizadas en microestructuras en rocas de la formación Strelley Pool, en Australia Occidental, con una antigüedad de 3,4 Ga. Se trataría de los fósiles de células más antiguos encontrados hasta la fecha. Evidencias adicionales muestran que su metabolismo sería anaerobio y basado en el sulfuro.\u200b\n\nHistoria y teoría celular\n\nLa historia de la biología celular ha estado ligada al desarrollo tecnológico que pudiera sustentar su estudio. De este modo, el primer acercamiento a su morfología se inicia con la popularización del microscopio rudimentario de lentes compuestas en el siglo XVII, se suplementa con diversas técnicas histológicas para microscopía óptica en los siglos XIX y XX y alcanza un mayor nivel resolutivo mediante los estudios de microscopía electrónica, de fluorescencia y confocal, entre otros, ya en el siglo XX. El desarrollo de herramientas moleculares, basadas en el manejo de ácidos nucleicos y enzimas permitieron un análisis más exhaustivo a lo largo del siglo XX.\u200b\n\nDefinición\n\nSe define a la célula como la unidad morfológica y funcional de todo ser vivo. De hecho, la célula es el elemento de menor tamaño que puede considerarse vivo. Como tal posee una membrana de fosfolípidos con permeabilidad selectiva que mantiene un medio interno altamente ordenado y diferenciado del medio externo en cuanto a su composición, sujeta a control homeostático, la cual consiste en biomoléculas y algunos metales y electrolitos. La estructura se automantiene activamente mediante el metabolismo, asegurándose la coordinación de todos los elementos celulares y su perpetuación por replicación a través de un genoma codificado por ácidos nucleicos. La parte de la biología que se ocupa de ella es la citología.\n\nCaracterísticas\n\nLas células, como sistemas termodinámicos complejos, poseen una serie de elementos estructurales y funcionales comunes que posibilitan su supervivencia; no obstante, los distintos tipos celulares presentan modificaciones de estas características comunes que permiten su especialización funcional y, por ello, la ganancia de complejidad.\u200b De este modo, las células permanecen altamente organizadas a costa de incrementar la entropía del entorno, uno de los requisitos de la vida.\u200b\n\nEstudio de las células\n\nLos biólogos utilizan diversos instrumentos para lograr el conocimiento de las células. Obtienen información de sus formas, tamaños y componentes, que les sirve para comprender además las funciones que en ellas se realizan.\nDesde las primeras observaciones de células, hace más de 300 años, hasta la época actual, las técnicas y los aparatos se han ido perfeccionando, originándose una rama más de la Biología: la Microscopía.\nDado el pequeño tamaño de la gran mayoría de las células, el uso del microscopio es de enorme valor en la investigación biológica. En la actualidad, los biólogos utilizan dos tipos básicos de microscopio: los ópticos y los electrónicos.\n\nLa célula procariota\n\nLas células procariotas son pequeñas y menos complejas que las eucariotas. Contienen ribosomas pero carecen de sistemas de endomembranas (esto es, orgánulos delimitados por membranas biológicas, como puede ser el núcleo celular). Por ello poseen el material genético en el citosol. Sin embargo, existen excepciones: algunas bacterias fotosintéticas poseen sistemas de membranas internos.\u200b También en el Filo Planctomycetes existen organismos como Pirellula que rodean su material genético mediante una membrana intracitoplasmática y Gemmata obscuriglobus que lo rodea con doble membrana. Esta última posee además otros compartimentos internos de membrana, posiblemente conectados con la membrana externa del nucleoide y con la membrana plasmática, que no está asociada a peptidoglucano.\u200b\u200b\u200b\nEstudios realizados en 2017, demuestran otra particularidad de Gemmata: presenta estructuras similares al poro nuclear, en la membrana que rodea su cuerpo nuclear.\u200b\n\nPor lo general podría decirse que los procariotas carecen de citoesqueleto. Sin embargo se ha observado que algunas bacterias, como Bacillus subtilis, poseen proteínas tales como MreB y mbl que actúan de un modo similar a la actina y son importantes en la morfología celular.\u200b Fusinita van den Ent, en Nature, va más allá, afirmando que los citoesqueletos de actina y tubulina tienen origen procariótico.\u200b\nDe gran diversidad, los procariotas sustentan un metabolismo extraordinariamente complejo, en algunos casos exclusivo de ciertos taxa, como algunos grupos de bacterias, lo que incide en su versatilidad ecológica.\u200b Los procariotas se clasifican, según Carl Woese, en arqueas y bacterias.\u200b\n\nArqueas\n\nLas arqueas poseen un diámetro celular comprendido entre 0,1 y 15 μm, aunque las formas filamentosas pueden ser mayores por agregación de células. Presentan multitud de formas distintas: incluso las hay descritas cuadradas y planas.\u200b Algunas arqueas tienen flagelos y son móviles.\nLas arqueas, al igual que las bacterias, no tienen membranas internas que delimiten orgánulos. Como todos los organismos presentan ribosomas, pero a diferencia de los encontrados en las bacterias que son sensibles a ciertos agentes antimicrobianos, los de las arqueas, más cercanos a los eucariotas, no lo son. La membrana celular tiene una estructura similar a la de las demás células, pero su composición química es única, con enlaces tipo éter en sus lípidos.\u200b Casi todas las arqueas poseen una pared celular (algunos Thermoplasma son la excepción) de composición característica, por ejemplo, no contienen peptidoglicano (mureína), propio de bacterias. No obstante pueden clasificarse bajo la tinción de Gram, de vital importancia en la taxonomía de bacterias; sin embargo, en arqueas, poseedoras de una estructura de pared en absoluto común a la bacteriana, dicha tinción es aplicable pero carece de valor taxonómico. El orden Methanobacteriales tiene una capa de pseudomureína, que provoca que dichas arqueas respondan como positivas a la tinción de Gram.\u200b\u200b\n\u200b\nComo en casi todos los procariotas, las células de las arqueas carecen de núcleo, y presentan un solo cromosoma circular. Existen elementos extracromosómicos, tales como plásmidos. Sus genomas son de pequeño tamaño, sobre 2-4 millones de pares de bases. También es característica la presencia de ARN polimerasas de constitución compleja y un gran número de nucleótidos modificados en los ácidos ribonucleicos ribosomales. Por otra parte, su ADN se empaqueta en forma de nucleosomas, como en los eucariotas, gracias a proteínas semejantes a las histonas y algunos genes poseen intrones.\u200b Pueden reproducirse por fisión binaria o múltiple, fragmentación o gemación.\n\nBacterias\n\nLas bacterias son organismos relativamente sencillos, de dimensiones muy reducidas, de apenas unas micras en la mayoría de los casos. Como otros procariotas, carecen de un núcleo delimitado por una membrana, aunque presentan un nucleoide, una estructura elemental que contiene una gran molécula generalmente circular de ADN.\u200b\u200b Carecen de núcleo celular y demás orgánulos delimitados por membranas biológicas.\u200b En el citoplasma se pueden apreciar plásmidos, pequeñas moléculas circulares de ADN que coexisten con el nucleoide y que contienen genes: son comúnmente usados por las bacterias en la parasexualidad (reproducción sexual bacteriana). El citoplasma también contiene ribosomas y diversos tipos de gránulos. En algunos casos, puede haber estructuras compuestas por membranas, generalmente relacionadas con la fotosíntesis.\u200b\nPoseen una membrana celular compuesta de lípidos, en forma de una bicapa y sobre ella se encuentra una cubierta en la que existe un polisacárido complejo denominado peptidoglicano; dependiendo de su estructura y subsecuente su respuesta a la tinción de Gram, se clasifica a las bacterias en Gram positivas y Gram negativas. El espacio comprendido entre la membrana celular y la pared celular (o la membrana externa, si esta existe) se denomina espacio periplásmico. Algunas bacterias presentan una cápsula. Otras son capaces de generar endosporas (estadios latentes capaces de resistir condiciones extremas) en algún momento de su ciclo vital. Entre las formaciones exteriores propias de la célula bacteriana destacan los flagelos (de estructura completamente distinta a la de los flagelos eucariotas) y los pili (estructuras de adherencia y relacionadas con la parasexualidad).\u200b\nLa mayoría de las bacterias disponen de un único cromosoma circular y suelen poseer elementos genéticos adicionales, como distintos tipos de plásmidos. Su reproducción, binaria y muy eficiente en el tiempo, permite la rápida expansión de sus poblaciones, generándose un gran número de células que son virtualmente clones, esto es, idénticas entre sí.\u200b\n\nLa célula eucariota\n\nLas células eucariotas son el exponente de la complejidad celular actual.\u200b Presentan una estructura básica relativamente estable caracterizada por la presencia de distintos tipos de orgánulos intracitoplasmáticos especializados, entre los cuales destaca el núcleo, que alberga el material genético. Especialmente en los organismos pluricelulares, las células pueden alcanzar un alto grado de especialización. Dicha especialización o diferenciación es tal que, en algunos casos, compromete la propia viabilidad del tipo celular en aislamiento. Así, por ejemplo, las neuronas dependen para su supervivencia de las células gliales.\u200b \nPor otro lado, la estructura de la célula varía dependiendo de la situación taxonómica del ser vivo: de este modo, las células vegetales difieren de las animales, así como de las de los hongos. Por ejemplo, las células animales carecen de pared celular, son muy variables, no tiene plastos, puede tener vacuolas pero no son muy grandes y presentan centríolos (que son agregados de microtúbulos cilíndricos que contribuyen a la formación de los cilios y los flagelos y facilitan la división celular). Las células de los vegetales, por su lado, presentan una pared celular compuesta principalmente de celulosa, disponen de plastos como cloroplastos (orgánulo capaz de realizar la fotosíntesis), cromoplastos (orgánulos que acumulan pigmentos) o leucoplastos (orgánulos que acumulan el almidón fabricado en la fotosíntesis), poseen vacuolas de gran tamaño que acumulan sustancias de reserva o de desecho producidas por la célula y finalmente cuentan también con plasmodesmos, que son conexiones citoplasmáticas que permiten la circulación directa de las sustancias del citoplasma de una célula a otra, con continuidad de sus membranas plasmáticas.\u200b\n\nCompartimentos\n\nLas células son entes dinámicos, con un metabolismo celular interno de gran actividad cuya estructura es un flujo entre rutas anastomosadas. Un fenómeno observado en todos los tipos celulares es la compartimentalización, que consiste en una heterogeneidad que da lugar a entornos más o menos definidos (rodeados o no mediante membranas biológicas) en las cuales existe un microentorno que aglutina a los elementos implicados en una ruta biológica.\u200b Esta compartimentalización alcanza su máximo exponente en las células eucariotas, las cuales están formadas por diferentes estructuras y orgánulos que desarrollan funciones específicas, lo que supone un método de especialización espacial y temporal.\u200b No obstante, células más sencillas, como los procariotas, ya poseen especializaciones semejantes.\u200b\n\nMembrana plasmática y superficie celular\n\nLa composición de la membrana plasmática varía entre células dependiendo de la función o del tejido en la que se encuentre, pero posee elementos comunes. Está compuesta por una doble capa de fosfolípidos, por proteínas unidas no covalentemente a esa bicapa, y por glúcidos unidos covalentemente a lípidos o proteínas. Generalmente, las moléculas más numerosas son las de lípidos; sin embargo, las proteínas, debido a su mayor masa molecular, representan aproximadamente el 50\xa0% de la masa de la membrana.\u200b\nUn modelo que explica el funcionamiento de la membrana plasmática es el modelo del mosaico fluido, de J. S. Singer y Garth Nicolson (1972), que desarrolla un concepto de unidad termodinámica basada en las interacciones hidrófobas entre moléculas y otro tipo de enlaces no covalentes.\u200b\nDicha estructura de membrana sustenta un complejo mecanismo de transporte, que posibilita un fluido intercambio de masa y energía entre el entorno intracelular y el externo.\u200b Además, la posibilidad de transporte e interacción entre moléculas de células aledañas o de una célula con su entorno faculta a estas poder comunicarse químicamente, esto es, permite la señalización celular. Neurotransmisores, hormonas, mediadores químicos locales afectan a células concretas modificando el patrón de expresión génica mediante mecanismos de transducción de señal.\u200b\nSobre la bicapa lipídica, independientemente de la presencia o no de una pared celular, existe una matriz que puede variar, de poco conspicua, como en los epitelios, a muy extensa, como en el tejido conjuntivo. \nDicha matriz, denominada glucocalix (glicocáliz), rica en líquido tisular, glucoproteínas, proteoglicanos y fibras, también interviene en la generación de estructuras y funciones emergentes, derivadas de las interacciones célula-célula.\u200b\n\nEstructura y expresión génica\n\nLas células eucariotas poseen su material genético en, generalmente, un solo núcleo celular, delimitado por una envoltura consistente en dos bicapas lipídicas atravesadas por numerosos poros nucleares y en continuidad con el retículo endoplasmático. En su interior, se encuentra el material genético, el ADN, observable, en las células en interfase, como cromatina de distribución heterogénea. A esta cromatina se encuentran asociadas multitud de proteínas, entre las cuales destacan las histonas, así como ARN, otro ácido nucleico.\u200b\nDicho material genético se encuentra inmerso en una actividad continua de regulación de la expresión génica; las ARN polimerasas transcriben ARN mensajero continuamente, que, exportado al citosol, es traducido a proteína, de acuerdo a las necesidades fisiológicas. Asimismo, dependiendo del momento del ciclo celular, dicho ADN puede entrar en replicación, como paso previo a la mitosis.\u200b No obstante, las células eucarióticas poseen material genético extranuclear: concretamente, en mitocondrias y plastos, si los hubiere; estos orgánulos conservan una independencia genética parcial del genoma nuclear.\u200b\u200b\n\nOrigen\n\nLa aparición de la vida, y, por ello, de la célula, probablemente se inició gracias a la transformación de moléculas inorgánicas en orgánicas bajo unas condiciones ambientales adecuadas, produciéndose más adelante la interacción de estas biomoléculas generando entes de mayor complejidad. El experimento de Miller y Urey, realizado en 1953, demostró que una mezcla de compuestos orgánicos sencillos puede transformarse en algunos aminoácidos, glúcidos y lípidos (componentes todos ellos de la materia viva) bajo unas condiciones ambientales que simulan las presentes hipotéticamente en la Tierra primigenia (en torno al eón Arcaico).\u200b\nSe postula que dichos componentes orgánicos se agruparon generando estructuras complejas, los coacervados de Oparin, aún acelulares que, en cuanto alcanzaron la capacidad de autoorganizarse y perpetuarse, dieron lugar a un tipo de célula primitiva, el progenote de Carl Woese, antecesor de los tipos celulares actuales.\u200b Una vez se diversificó este grupo celular, dando lugar a las variantes procariotas, arqueas y bacterias, pudieron aparecer nuevos tipos de células, más complejos, por endosimbiosis, esto es, captación permanente de unos tipos celulares en otros sin una pérdida total de autonomía de aquellos.\u200b De este modo, algunos autores describen un modelo en el cual la primera célula eucariota surgió por introducción de una arquea en el interior de una bacteria, dando lugar esta primera a un primitivo núcleo celular.\u200b No obstante, la imposibilidad de que una bacteria pueda efectuar una fagocitosis y, por ello, captar a otro tipo de célula, dio lugar a otra hipótesis, que sugiere que fue una célula denominada cronocito la que fagocitó a una bacteria y a una arquea, dando lugar al primer organismo eucariota. De este modo, y mediante un análisis de secuencias a nivel genómico de organismos modelo eucariotas, se ha conseguido describir a este cronocito original como un organismo con citoesqueleto y membrana plasmática, lo cual sustenta su capacidad fagocítica, y cuyo material genético era el ARN, lo que puede explicar, si la arquea fagocitada lo poseía en el ADN, la separación espacial en los eucariotas actuales entre la transcripción (nuclear), y la traducción (citoplasmática).\u200b\nUna dificultad adicional es el hecho de que no se han encontrado organismos eucariotas primitivamente amitocondriados como exige la hipótesis endosimbionte. Además, el equipo de María Rivera, de la Universidad de California, comparando genomas completos de todos los dominios de la vida ha encontrado evidencias de que los eucariotas contienen dos genomas diferentes, uno más semejante a bacterias y otro a arqueas, apuntando en este último caso semejanzas a los metanógenos, en particular en el caso de las histonas.\u200b\u200b Esto llevó a Bill Martin y Miklós Müller a plantear la hipótesis de que la célula eucariota surgiera no por endosimbiosis, sino por fusión quimérica y acoplamiento metabólico de un metanógeno y una α-proteobacteria simbiontes a través del hidrógeno (hipótesis del hidrógeno).\u200b Esta hipótesis atrae hoy en día posiciones muy encontradas, con detractores como Christian de Duve.\u200b\nHarold Morowitz, un físico de la Universidad Yale, ha calculado que las probabilidades de obtener la bacteria viva más sencilla mediante cambios al azar es de 1 sobre 1 seguido por 100.000.000.000 de ceros. «Este número es tan grande —dijo Robert Shapiro— que para escribirlo en forma convencional necesitaríamos varios centenares de miles de libros en blanco». Presenta la acusación de que los científicos que han abrazado la evolución química de la vida pasan por alto la evidencia aumentante y «han optado por aceptarla como verdad que no puede ser cuestionada, consagrándola así como mitología».\u200b',
      'negative_5': 'Sistema de control industrial\n\nControladores discretos\n\nLos sistemas de control más simples se basan en pequeños controladores discretos con un solo bucle de control cada uno.  Por lo general, estos paneles se montan en el panel, lo que permite la visualización directa del panel frontal y proporciona medios de intervención manual por parte del operador, ya sea para controlar manualmente el proceso o para cambiar los puntos de control.  Originalmente, estos serían controladores neumáticos, algunos de los cuales todavía están en uso, pero casi todos son ahora electrónicos. \nSe pueden crear sistemas bastante complejos con las redes de estos controladores que se comunican utilizando protocolos estándar de la industria. Las redes permiten el uso de interfaces de operador SCADA locales o remotas, y permiten la conexión en cascada y el enclavamiento de los controladores.  Sin embargo, a medida que aumenta el número de bucles de control para un diseño de sistema, hay un punto en el que el uso de un controlador lógico programable (PLC) o un sistema de control distribuido (DCS) es más manejable o rentable.\n\nSistemas de control distribuido\n\nUn sistema de control distribuido (DCS) es un sistema de control de procesador digital para un proceso o planta, en el que las funciones del controlador y los módulos de conexión de campo se distribuyen por todo el sistema. A medida que aumenta el número de bucles de control, DCS se vuelve más rentable que los controladores discretos. Además, un DCS proporciona supervisión de visualización y gestión en grandes procesos industriales. En un DCS, una jerarquía de controladores está conectada por redes de comunicación , lo que permite salas de control centralizadas y monitoreo y control local en planta. \nUn DCS permite una fácil configuración de los controles de la planta, tales como bucles en cascada y enclavamientos, \xa0  y fácil conexión con otros sistemas informáticos como el control de producción. También permite un manejo más sofisticado de las alarmas, introduce el registro automático de eventos, elimina la necesidad de registros físicos, como los registradores gráficos, y permite que los equipos de control se conecten en red y, por lo tanto, se ubiquen localmente en los equipos que se controlan para reducir el cableado. \nUn DCS generalmente utiliza procesadores diseñados a medida como controladores y utiliza interconexiones propietarias o protocolos estándar para la comunicación.  Los módulos de entrada y salida forman los componentes periféricos del sistema. \nLos procesadores reciben información de los módulos de entrada, procesan la información y deciden las acciones de control que deben realizar los módulos de salida.  Los módulos de entrada reciben información de los instrumentos de detección en el proceso (o campo) y los módulos de salida transmiten instrucciones a los elementos de control finales, como las válvulas de control . \nLas entradas y salidas de campo pueden o bien estar cambiando continuamente las señales analógicas , por ejemplo, bucle de corriente o 2 señales de estado que cambian encendido o apagado, tales como contactos de relé o un interruptor semiconductor. \nNormalmente, los sistemas de control distribuido también pueden admitir Foundation Fieldbus, PROFIBUS , HART , Modbus y otros buses de comunicación digital que transportan no solo señales de entrada y salida, sino también mensajes avanzados, como diagnósticos de error y señales de estado.\n\nSistemas SCADA\n\nEl control de supervisión y la adquisición de datos (SCADA) es una arquitectura de sistema de control que utiliza computadoras, comunicaciones de datos en red e interfaces gráficas de usuario para la gestión de supervisión de procesos de alto nivel.  Las interfaces del operador que permiten el monitoreo y la emisión de comandos de proceso, como los cambios del punto de ajuste del controlador, se manejan a través del sistema de computadora de supervisión SCADA.  Sin embargo, la lógica de control en tiempo real o los cálculos del controlador se realizan mediante módulos en red que se conectan a otros dispositivos periféricos, como controladores lógicos programables y controladores PID discretos que se conectan a la planta o maquinaria de proceso. \nEl concepto SCADA se desarrolló como un medio universal de acceso remoto a una variedad de módulos de control local, que podrían ser de diferentes fabricantes y permitir el acceso a través de protocolos de automatización estándar. En la práctica, los grandes sistemas SCADA se han vuelto muy similares a los sistemas de control distribuido en función, pero utilizando múltiples medios de interfaz con la planta. Pueden controlar procesos a gran escala que pueden incluir múltiples sitios y trabajar a grandes distancias.\u200b Esta es una arquitectura de uso común en los sistemas de control industrial, sin embargo, existe la preocupación de que los sistemas SCADA sean vulnerables a la guerra cibernética o los ataques de ciberterrorismo . \u200b \nEl software SCADA funciona en un nivel de supervisión ya que las acciones de control se realizan automáticamente mediante RTU o PLC. Las funciones de control de SCADA suelen estar restringidas a la intervención básica o de supervisión. La RTU o el PLC controlan directamente un circuito de control de retroalimentación, pero el software SCADA controla el rendimiento general del circuito.  Por ejemplo, un PLC puede controlar el flujo de agua de refrigeración a través de parte de un proceso industrial hasta un nivel de punto de ajuste, pero el software del sistema SCADA permitirá a los operadores cambiar los puntos de ajuste para el flujo. El SCADA también permite mostrar y registrar condiciones de alarma, como pérdida de flujo o alta temperatura.\n\nControladores lógicos programables\n\nLos PLC pueden abarcar desde pequeños dispositivos modulares con decenas de entradas y salidas (I/O) en una carcasa integral con el procesador, hasta grandes dispositivos modulares montados en bastidor con un recuento de miles de I/O, y que a menudo están conectados en red a otros Sistemas PLC y SCADA. Se pueden diseñar para disposiciones múltiples de entradas y salidas digitales y analógicas, rangos de temperatura ampliados, inmunidad al ruido eléctrico y resistencia a las vibraciones y los impactos. Los programas para controlar el funcionamiento de la máquina generalmente se almacenan en una memoria con respaldo de batería o no volátil.\n\nHistoria\n\nEl control de procesos de grandes plantas industriales ha evolucionado a través de muchas etapas. Inicialmente, el control era desde paneles locales a la planta de proceso.  Sin embargo, esto requería que el personal atendiera estos paneles dispersos, y no había una visión general del proceso. El siguiente desarrollo lógico fue la transmisión de todas las mediciones de la planta a una sala de control central con personal permanente. A menudo, los controladores estaban detrás de los paneles de la sala de control, y todas las salidas de control manual y automático se transmitían individualmente a la planta en forma de señales neumáticas o eléctricas. Efectivamente, esta fue la centralización de todos los paneles localizados, con las ventajas de la reducción de los requisitos de personal y la visión general consolidada del proceso. \nSin embargo, aunque proporcionaba un enfoque de control central, esta disposición era inflexible, ya que cada bucle de control tenía su propio hardware de controlador, por lo que los cambios en el sistema requerían la reconfiguración de las señales mediante una nueva tubería o un nuevo cableado. También requería el movimiento continuo del operador dentro de una gran sala de control para poder monitorear todo el proceso. Con la llegada de procesadores electrónicos, redes de señalización electrónica de alta velocidad y pantallas gráficas electrónicas, fue posible reemplazar estos controladores discretos con algoritmos basados en computadora, alojados en una red de racks de entrada / salida con sus propios procesadores de control. Estos podrían distribuirse alrededor de la planta y se comunicarían con las pantallas gráficas en la sala de control. Se realizó el concepto de control distribuido . \nLa introducción del control distribuido permitió la interconexión flexible y la reconfiguración de los controles de la planta, como los bucles en cascada y los interbloqueos, y la interconexión con otros sistemas informáticos de producción. Permitió el manejo sofisticado de alarmas, introdujo el registro automático de eventos, eliminó la necesidad de registros físicos, como los registradores gráficos, permitió que los bastidores de control estuvieran conectados en red y, por lo tanto, localizados localmente para que la planta redujera los tendidos de cableado, y proporcionó información general de alto nivel sobre el estado de la planta y Niveles de producción. Para sistemas de control grandes, el sistema de control distribuido de nombre comercial general (DCS) se acuñó para referirse a sistemas modulares patentados de muchos fabricantes que integraban redes de alta velocidad y un conjunto completo de pantallas y racks de control. \nSi bien el DCS se adaptó para satisfacer las necesidades de grandes procesos continuos industriales, en industrias donde la lógica combinatoria y secuencial era el requisito principal, el PLC (controlador lógico programable) evolucionó a partir de la necesidad de reemplazar los racks de temporizadores y temporizadores utilizados para eventos. control impulsado  Los controles antiguos eran difíciles de reconfigurar y encontrar fallas, y el control PLC permitía la conexión en red de señales a un área de control central con pantallas electrónicas. Los PLC se desarrollaron por primera vez para la industria automotriz en líneas de producción de vehículos, donde la lógica secuencial se estaba volviendo muy compleja. Pronto se adoptó en un gran número de otras aplicaciones impulsadas por eventos tan variadas como prensas de impresión y plantas de tratamiento de agua. \nLa historia de SCADA se basa en aplicaciones de distribución, como las tuberías de energía, gas natural y agua, donde existe la necesidad de recopilar datos remotos a través de enlaces de baja latencia y ancho de banda potencialmente poco confiables o intermitentes.  Los sistemas SCADA utilizan el control de bucle abierto con sitios que están muy separados geográficamente. Un sistema SCADA utiliza RTU (unidades terminales remotas, también conocidas como unidades de telemetría remotas) para enviar datos de supervisión a un centro de control.  La mayoría de los sistemas RTU siempre tuvieron una capacidad limitada para manejar los controles locales mientras la estación maestra no está disponible. Sin embargo, a lo largo de los años, los sistemas RTU han crecido cada vez más capaces de manejar controles locales. \nLos límites entre los sistemas DCS y SCADA/PLC se difuminan a medida que pasa el tiempo.\u200b  Los límites técnicos que impulsaron los diseños de estos diversos sistemas ya no son tan problemáticos.  Muchas plataformas de PLC ahora pueden funcionar bastante bien como un pequeño DCS, usando E/S remotas y son lo suficientemente confiables para que algunos sistemas SCADA realmente administren el control de bucle cerrado en largas distancias.  Con la velocidad cada vez mayor de los procesadores de hoy, muchos productos DCS tienen una línea completa de subsistemas similares a PLC que no se ofrecieron cuando se desarrollaron inicialmente. \nEn 1993, con el lanzamiento de IEC-1131, que luego se convertiría en IEC-61131 -3, la industria avanzó hacia una mayor estandarización del código, un software de control reutilizable e independiente del hardware. Por primera vez, la programación orientada a objetos (OOP) se hizo posible dentro de los sistemas de control industrial. Esto llevó al desarrollo de ambos (controladores de automatización programables) (PAC) y PC industriales (IPC). Estas son plataformas programadas en los 5 lenguajes IEC estandarizados (lógica de escalera, texto estructurado, bloque de funciones, lista de instrucciones y tabla de funciones secuenciales). También pueden programarse en lenguajes modernos de alto nivel como C o C ++.  Además, aceptan modelos desarrollados en herramientas analíticas como MATLAB y Simulink. A diferencia de los PLC tradicionales, que utilizan sistemas operativos propietarios, los IPC utilizan Windows IoT. Los IPC tienen la ventaja de los potentes procesadores de múltiples núcleos con costos de hardware mucho más bajos que los PLC tradicionales y se adaptan bien a múltiples factores de forma, como el montaje en riel DIN, combinado con una pantalla táctil como "panel-pc" o como una PC integrada. Las nuevas plataformas de hardware y la tecnología han contribuido significativamente a la evolución de los sistemas DCS y SCADA, borrando aún más los límites y cambiando las definiciones.',
      'negative_6': 'Prunus africana\n\nDescripción\n\nLa corteza de este árbol es negra bronce, acanalada o agrietada y escamosa, agrietando en un patrón rectangular característico. Las hojas son alternas, simples, de 8 a 20 cm de largo, elípticas, con las puntas embotadas o agudas, glabras y verde oscuro en el haz, verde pálido en el envés, con los márgenes suavemente serrados. Una vena central está deprimida en el extremo, y es prominente en la parte inferior. El pecíolo de unos 2 cm es rosado o rojo. La flor es andrógina, con 10 a 20 estambres, de 3 a 8 cm de longitud, blancos o de color verdoso,  y se distribuyen en racimos axilares de 70 milímetros. La planta florece de octubre a mayo. Los estambres son polinizados por insectos. La fruta es de roja a bronce, de 7 a 13 mm., más ancha que larga, con dos lóbulos con una semilla en cada lóbulo. Crece en manojos que maduran de septiembre a noviembre, varios meses después de la polinización.\n\nDistribución y hábitat\n\nEstá en estado natural como árbol de hoja perenne en las regiones montañosas del África subsahariana y las islas de Madagascar, Santo Tomé y Príncipe, Fernando Po y Gran Comora en la franja de 900 a 3400 m de altitud. El árbol maduro alcanza un desarrollo entre 10 a 25 m alto, con ramaje abierto ramificado y a menudo colgante en el bosque, más corto y con una corona de diámetro redondeado de 10 a 20 m en el prado. Requiere un clima húmedo, 900 a 3400 mm de precipitación anual, y es resistente a las heladas moderadas.\u200b\u200b\u200b\u200b\u200b\u200b\n\nEcología\n\nComo en otros miembros del género Prunus, Prunus africana posee nectarios extraflorales que proveen una fuente de nutrientes a insectos anti-herbívoros a cambio de la protección del follaje.\nLa fruta es demasiado amarga como para interesar en uso humano; sin embargo, es un suministro de alimento muy apreciado para muchos animales, que separan las semillas. Dian Fossey en sus informes sobre el gorila de montaña (Gorilas en la niebla) decía que:\u200b"Las laderas del noroeste del Visoke albergan varios rodales de Pygeum africanum …. Las frutas de este árbol son muy apreciadas por los gorilas." El East African Mammals presenta informaciones de que los especímenes de Pygeum son el hábitat de la rara ardilla de montaña de Carruther y afirma, "Este tipo de bosque tiende a presentar una cubierta más bien quebrada con muchos árboles ahogados por especies trepadoras y densa maleza."\u200b\n\nActualmente se encuentra incluido en en el apéndice II del CITES.\u200b\n\nUsos\n\nUn extracto denominado "Pygeum", es un remedio herbario preparado a partir de la corteza del Prunus africana que se utiliza para tratar la Hiperplasia benigna de próstata (HBP).\u200b La recolección de la corteza madura con este fin ha dado lugar a que la especie se encuentre en peligro de extinción, debido a que algunos recolectores, estimulados por el alto precio del kilo de corteza, quitaban demasiada corteza de una manera no sostenible. En la década de 1990 se estimaba que eran procesados anualmente unos 35.000 árboles. La demanda creciente de la corteza ha llevado al cultivo del árbol por sus aplicaciones medicinales.\u200b\nLa madera es  dura y se emplea en la fabricación de mangos de hachas y de azadas, de utensilios, de carros, de suelos de pisos y de muebles. Es una madera resistente, pesada, de grano recto y rosada, con un olor acre de amargo almendrado cuando está recién cortada, cambiando más adelante a caoba e inodoro.\u200b\n\nDescubrimiento y clasificación\n\nEl nombre del remedio, "Pygeum", viene del nombre de la planta, que fue descubierta a la botánica por Gustav Mann durante su primera exploración europea ahora famosa de la Cordillera de Camerún, con Richard Francis Burton y Alfred Saker, en 1861. Una carta de Mann a la Sociedad linneana de Londres, leída por William Jackson Hooker, entonces director del Real Jardín Botánico de Kew, describe el 5 de junio de 1862  los picos de la cordillera del Camerún (tales como monte Victoria, más tarde denominado como Monte Camerún\u200b) y los especímenes de allí.\u200b Los especímenes  fueron enviados  al Real Jardín Botánico de Kew para su catalogación, que fue realizada por William Hooker y su hijo, Joseph Dalton Hooker, que tuvo la responsabilidad de publicarlos, pues William murió en 1865.\n.\u200b Evidentemente Hooker había hecho el contenido del J. Proc. Linn. Soc., Bot. 7 de 1864 disponible para algunos, ya que Burton menciona el volumen y la carta de Mann en 1863.\u200b\nHooker da escasas aclaraciones de por qué eligió el nombre de Pygeum; sin embargo, dice que era vox populi entre botánicos. La fruta del espécimen de Kirk era una "esfera muy deprimida"; Por esto  significó referirse al género de Joseph Gaertner sin ninguna duda como de "Pygeum".,\u200b el cual innova Pygeum\u200b procedente de la palabra griega, πυγή, "grupa, trasero", debido a que los lóbulos del fruto se asemejan a los músculos humanos del  gluteus maximus.\u200b\nEn 1965 Cornelis Kalkman trasladó Pygeum al género Prunus y esta clasificación ha sido aceptada hasta ahora.\u200b Sin embargo, una nota de un reciente estudio cladístico de Pygeum: "su relación con el género Prunus permanece aún sin confirmar por pruebas moleculares cladísticas."\u200b\n\nNombres\n\nPrunus africana también es conocido con los nombres populares siguientes en inglés:  Pygeum, Iron Wood,  Stinkwood (rojo), African Plum (ciruela africana), African Prune (pruno africano), African Cherry (cereza africana), Bitter Almond (almendra amarga). En otras lenguas de las regiones donde crece; en amharic \'tikur inchet\', en chagga \'Mkonde-konde\', en kikuyu \'Muiri\', en luganda \'Entasesa\' o \'Ngwabuzito\', en xhosa \'uMkakase\', en zulú \'Inyazangoma-elimnyama\' y en afrikáans \'Rooistinkhout\'.\n\nEvidencias paleobotánicas\n\nUn estudio de 1994/1995 publicado en 1997 por Marchant y Taylor hizo un análisis de polen fósil y datación de radiocarbono de dos muestras encontradas en un pantano del monte Mubindi en Uganda.\u200b \nEl pantano es una acumulación a una altitud de 2100 msnm entre crestas montañosas. Es un "bosque bajo de montaña"  húmedo; en el interior del Parque Nacional de la Selva Impenetrable de Bwindi. Los investigadores encontraron que ese Prunus de montaña, representado por el actualmente existente allí Prunus africana, ha estado en esa acumulación de manera continua desde su zona de polen MB6.1, con una edad aproximada de entre 43 000 a 33 000 años.',
      'negative_7': 'Celofán\n\nEl celofán es un polímero natural derivado de la celulosa. Tiene el aspecto de un  film (como el que se usa para envolver bocadillos) fino, transparente, flexible y resistente a esfuerzos de tracción.\n\nHistoria\n\nEl celofán fue inventado por el químico suizo Jacques E. Brandenberger mientras estaba empleado en la Blanchisserie et Teinturerie de Thaon. En 1900, inspirado al ver un derrame de vino en el mantel de un restaurante, decidió crear una tela que pudiera repeler líquidos en lugar de absorberlos. Su primer paso consistió en rociar una capa impermeable sobre la tela, y optó por tratarla con viscosa.  El tejido revestido resultante era demasiado rígido, pero la clara película se separaba fácilmente de la tela de refuerzo, y abandonó su idea original cuando las posibilidades del nuevo material se hicieron evidentes.\nBrandenberger necesitó diez años para perfeccionar su película, siendo la principal mejoría sobre trabajos anteriores con este tipo de películas el añadido de glicerina para ablandar el material. En 1912 ya había construido una máquina para la fabricación de la película, que llamó celofán, de las palabras «celulosa» y «diáfano» (transparente). El celofán se patentó ese mismo año.\u200b  Al año siguiente, la empresa Comptoir des Textiles Artificiels (CTA) compró el interés de la empresa de Thaon en celofán y establecieron a Brandenberger en una nueva compañía, La Cellophane SA.\u200b\nLa empresa estadounidense de dulces Whitman\'s comenzó a usar el celofán para los envoltorios de caramelos en los Estados Unidos ese mismo año 1912, en su Whitman\'s Sampler. Fueron el mayor usuario de celofán importado desde Francia hasta cerca de 1924, cuando DuPont construyó la primera planta de fabricación de celofán en los EE.UU.. El celofán vio al principio sus ventas limitadas en los EE.UU.  ya que si bien era resistente al agua no era a prueba de humedad (era permeable al vapor de agua).  Esto significaba que era inadecuado para el envasado de productos que requerían impermeabilización frente a la humedad.  DuPont contrató al químico William Hale Charch, que pasó tres años desarrollando una laca de nitrocelulosa que, cuando se aplicaba al celofán, pasaba la prueba de la humedad.\u200b Después de la introducción del celofán a prueba de humedad en el año 1927, las ventas del material se triplicaron entre 1928 y 1930, y en 1938, el celofán representaba el 10% de las ventas de DuPont y el 25% de sus beneficios.\u200b\nLa empresa textil británica de tecnología de la viscosa de Samuel Courtauld había logrado diversificarse en 1930 con la producción de una película de viscosa, a la que denominaban "Viscacelle".  Sin embargo, la competencia con el celofán era un obstáculo para sus ventas, y en 1935 Courtauld fundó la British Cellophane conjuntamente con la  Cellophane Company y su empresa matriz francesa CTA.\u200b  Entre 1935 y 1937 construyeron su principal planta de producción en Bridgwater, Somerset, Inglaterra,  que empleaba a 3.000 trabajadores.\n\nFabricación\n\nEl proceso de fabricación consiste en disolver fibras de madera, algodón o cáñamo en un álcali para hacer una solución llamada viscosa, la cual luego es extruida a través de una ranura y sumergida en un baño ácido que la vuelve a convertir en celulosa. Por medio de un proceso similar, utilizando un orificio en lugar de una ranura, se produce una fibra llamada rayón.\n\nPrincipales usos\n\nSe utiliza, principalmente, como envoltorio, para envolver y adornar regalos y ramos florales (dado que además de incoloro también se fabrica en colores transparentes), aunque también fue muy utilizado en la elaboración de cintas adhesivas, siendo sustituido en gran medida por otros polímeros de cualidades más apropiadas para tal uso.\nAdemás de su uso como envoltorio de alimentos, también tiene usos industriales, tales como cintas autoadhesivas y membranas semipermeables utilizadas por cierto tipo de baterías.\nPara algunos usos, se le aplican recubrimientos para complementar o modificar sus propiedades.\nCon el tiempo, el término celofán se ha generalizado, y se usa comúnmente para referirse a diversas películas plásticas, aún aquellas que no están hechas con celulosa (aun así, la mayoría están hechas de dicho material).\nActualmente, el celofán ha sido sustituido por el polipropileno, que es un derivado del petróleo, ya que por costos de fabricación ha sido más práctico. A tal grado que, prácticamente, todo lo que conocemos popularmente como celofán, en realidad, es polipropileno.',
      'negative_8': 'Optogenética\n\nLa optogenética es la combinación de métodos genéticos y ópticos para controlar eventos específicos en ciertas células de tejidos vivos, incluso de mamíferos y otros animales, con la precisión temporal necesaria (en la escala temporal del milisegundo) para mantener el ritmo intacto de funcionamiento de los sistemas biológicos. La razón de este control tan rápido y preciso reside en el uso de la luz como agente inductor.\u200b\nLa optogenética abarca el desarrollo de proteínas sensibles a la luz (naturales o modificadas químicamente), las estrategias para introducir los genes que codifican dichas proteínas en las células o tejidos diana y, por último, la generación de sistemas de detección de los cambios de comportamiento producidos en dichas células y tejidos.\u200b\nEstas técnicas son especialmente útiles para su empleo en la investigación en neurociencias, donde no existían métodos de estudio que permitiesen el estudio in vivo de células individualizadas.\n\nHistoria\n\nLa posibilidad de utilizar la luz para controlar selectivamente modelos de actividad neuronal específica (potenciales de acción) dentro de los diferentes subtipos de células del cerebro fue anticipada en 1999 por Francis Crick en sus Conferencias Kuffler impartidas en la Universidad de California en San Diego.\u200b Un uso pionero de la luz para activar las neuronas fue llevado a cabo por Richard Fork\u200b y más tarde por Rafael Yuste,\u200b que demostraron la activación por láser de las neuronas en el tejido intacto, aunque no de una forma genéticamente orientada. El primer método genéticamente dirigido, que utilizaba la luz para controlar neuronas genéticamente sensibilizadas, fue publicado en enero de 2002 por Boris Zemelman (ahora en UT Austin) y Gero Miesenböck, que emplearon los fotorreceptores para la rodopsina de Drosophila para controlar la actividad neuronal en neuronas cultivadas de mamíferos.\u200b En 2003 Zemelman y Miesenböck desarrollaron un segundo método para la activación dependiente de la luz de neuronas individuales en las que los canales ionotrópicos TRPV1, TRPM8 y P2X2 fueron cerrados por ligandos enjaulados en respuesta a la luz.\u200b A partir de 2004, los grupos de Kramer e Isacoff desarrollaron fotointerruptores orgánicos o compuestos "enjaulados" que podrían interactuar con los canales de iones genéticamente introducidos.\u200b\u200b Sin embargo, estos enfoques previos no se aplicaron fuera de los laboratorios originales, probablemente a causa de problemas técnicos en la entrega de los múltiples componentes requeridos.\nEn abril de 2005 Susana Lima y Miesenböck hicieron público el primer uso de la fotoestimulación genéticamente orientada de P2X2 para controlar el comportamiento de un animal.\u200b Demostraron que la fotoestimulación de grupos genéticamente circunscritos de neuronas, tales como los del sistema dopaminérgico, provocaban cambios de comportamiento característicos en moscas de la fruta. En agosto de 2005, el laboratorio de Karl Deisseroth en el Departamento de Bioingeniería de la Universidad de Stanford junto a los estudiantes graduados Edward Boyden y Feng Zhang (ambos ahora en el MIT) publicaron la primera demostración de un sistema optogenético de un solo componente, a partir de neuronas cultivadas de mamíferos\u200b\u200b utilizando canalrodopsina-2, un canal catiónico de un solo componente activado por la luz procedente de algas unicelulares. La identidad molecular y principales propiedades de la canalrodopsino la hacían útil para estudios de optogenética como había publicado anteriormente (en noviembre de 2003) el grupo de Georg Nagel.\u200b Los grupos de Gottschalk y Nagel fueron los primeros en extender la usabilidad de la canalrodopsina-2 para controlar la actividad neuronal en animales intactos al mostrar que los patrones motores en el gusano redondo Caenorhabditis elegans podían ser evocados por la expresión dirigida y la estimulación de canalrodopsina-2 en los circuitos nerviosos seleccionados (publicado en diciembre de 2005).\u200b\nEn 2010, Karl Deisseroth de la Universidad de Stanford fue premiado\u200b "por su trabajo pionero en el desarrollo de métodos optogenéticos para estudiar la función de las redes neuronales subyacentes al comportamiento".\nEn 2012, Gero Miesenböck fue premiado\u200b http://www.inbevbailletlatour.com/index.cfm?ee=3%7C336 InBev - Baillet Latour Premio Internacional de la Salud ] por sus "pioneros enfoques optogenéticos para manipular la actividad neuronal y para controlar el comportamiento de los animales."\nEn 2013, Ernst Bamberg, Ed Boyden, Karl Deisseroth, Peter Hegemann, Gero Miesenböck y Georg Nagel recibieron el Premio Mundial del Cerebro por "su invención y perfeccionamiento de la optogenética".\u200b\n\nImportancia\n\nEn 2010, la optogenética fue elegída como el Método del Año, entre todos los campos de la ciencia y la ingeniería, por la revista de investigación interdisciplinar "Nature Methods".\u200b\nAl mismo tiempo, la optogenética fue destacada en el artículo "Insights of the Decade"\u200b ("Los avances de la década"), publicado en la revista de investigación científica "Science". Estas revistas también hacen referencia a recientes publicaciones en vídeo de interés general y acceso público,\u200b y a textos sobre la cuestión.\u200b',
      'negative_9': 'Aclimatación\n\nAclimatación, aclimatización o aclimatamiento es el proceso por el cual un organismo se adapta fisiológicamente a los cambios en su medio ambiente, que en general tienen relación directa con el clima. Se suele usar este término para referirse a procesos que ocurren durante un período corto, dentro del periodo vital de un organismo individual o grupo. Puede ser una situación puntual o representar parte de un ciclo periódico, como es el caso del crecimiento de pelo que experimentan algunos mamíferos durante el invierno. Los seres vivos pueden ajustar sus rasgos morfológicos, etológicos, físicos y/o bioquímicos en respuesta a cambios en su entorno. La capacidad de aclimatación a nuevos ambientes se ha comprobado en miles de especies. Sin embargo, no se conocen en profundidad los mecanismos que conducen a ella. \nAunque a los términos aclimatación y aclimatizacion se le han dado diferentes significados, el glosario de términos de fisiología térmica\u200b adopta la siguiente definición para el término aclimatación: \n\n \n\n  \nCambios adaptativos que se producen en un organismo en respuesta a cambios inducidos experimentalmente, en particular a factores climáticos, como temperatura en un ambiente controlado.\n\n \n \nOtros autores\u200b definen aclimatación como: \n\n \n\n  \nModificaciones facultativas en una característica fisiológica en respuesta a cambios en una variable ambiental en el laboratorio.\n\n \n En cambio, se utiliza el término aclimatización para el mismo tipo de cambios en el medio ambiente natural.\nEstos cambios son el resultado de la plasticidad fenotípica y son reversibles. Por ejemplo: el color diferente del pelo de un mamífero en el invierno y en el verano.\nEl término aclimatación se refiere al mismo tipo de cambios pero que se producen en condiciones experimentales controladas, por ejemplo en el laboratorio donde se modifican uno o dos factores ambientales. Los cambios pueden producirse como respuesta al ambiente durante el desarrollo o por cambios ambientales a largo término durante la historia de vida del organismo. La respuesta puede ser beneficiosa, neutra o negativa.\u200b\nEn las investigaciones sobre la aclimatización y la aclimatación se pone énfasis en la biología molecular, la activación de genes inducida por el ambiente, las consecuencias sobre la ecología y la aptitud, como así también sobre sus costos.\u200b  \nLa adaptación no debe confundirse con la aclimatización o la aclimatación; mientras que la aclimatización y la aclimatación son cambios fenotípicos, la adaptación es una modificación a nivel genético que se produce gradualmente por selección natural y que en general no es reversible.\n\nAclimatización a la temperatura en ectotermos\n\nLa temperatura tiene gran influencia sobre la mayoría de las reacciones químicas de los organismos. A pesar de ello, muchos ectotermos tienen gran capacidad para mantener las funciones constantes dentro de un amplio rango de temperaturas corporales. Los cambios en la temperatura ambiental y/o en el fotoperíodo desencadenan la aclimatización y la compensación tiene lugar en todos los niveles de la función biológica, involucrando enzimas, células, órganos y el comportamiento.\u200b \nLa regulación de la expresión génica por la temperatura es crítica para la supervivencia y el éxito de los ectotermos en ambientes con variación térmica. Neuronas sensitivas al calor y neuronas sensitivas al frío son importantes en la detección de la temperatura pero no están bien estudiadas las rutas de señalización hasta la expresión génica.\u200b\u200b \n\nLos efectos de la temperatura pueden visualizarse gráficamente por medio de las curvas tasa metabólica (o tasa de reacción) en función de la temperatura corporal (Fig. 1).\nLa figura muestra la compensación de un animal ectotermo aclimatizado al verano (temperatura alta) o al invierno (temperatura baja). En los animales aclimatizados al frío la curva se desplaza hacia arriba o hacia la izquierda y en los aclimatizados al calor hacia abajo o hacia la derecha.\u200b Obsérvese que la compensación no es total y que el animal aclimatizado a la temperatura de invierno tiene en invierno una tasa metabólica menor que la del mismo animal en verano tras la aclimatización a la temperatura del verano, pero que la tasa metabólica es sustancialmente mayor a la que tendría si no se hubiese aclimatizado. En el caso representado las dos curvas presentan igual pendiente y la compensación puede considerarse como el desplazamiento vertical u horizontal de las curvas que relacionan la tasa metabólica con la temperatura, en otros casos puede cambiar la pendiente, es decir, tener diferente Q₁₀ (Q₁₀ se define como el incremento en la tasa de un proceso al aumentar la temperatura 10\xa0°C), lo cual indica que las enzimas tienen diferente sensibilidad térmica.',
      'negative_10': 'Nanorred\n\nUna nanorred o red a nanoescala es un conjunto de nanomáquinas interconectadas (máquinas de unos pocos cientos de nanómetros o unos pocos micrómetros de tamaño), capaces cada una de realizar sólo tareas simples como  computar, guardar datos,  detectar o  actuar.\u200b\u200b\nLas nanorredes extienden las capacidades de las nanomáquinas, tanto en términos de rango de operaciones como de su complejidad, al facilitar que las nanomáquinas puedan coordinarse, compartir información o fusionarla. Así mismo permiten la aplicación de nanotecnología en campos como biomedicina, estudios  ambientales, tecnología militar e industrial. El protocolo IEEE P1906.1 define las comunicaciones en nanoescala.\n\nPosibilidades de comunicación\n\nLos paradigmas de comunicación clásicos deben revisarse para su aplicación a nanoescala. Las dos opciones principales son la comunicación electromagnética y la comunicación molecular.\n\nComunicación electromagnética\n\nSe le define como transmisión y recepción de radiación electromagnética entre componentes basados en nuevos nanomateriales.\u200b Los avances recientes en electrónica molecular con el carbono han abierto la puerta a una nueva generación de componentes electrónicos a nanoescala, tales como nanobaterías,\u200b sistemas de recogida de energía en nanoescala,\u200b nanomemorias,\u200b circuitos lógicos en nanoescala e incluso nanoantenas.\u200b\u200b\nDesde la perspectiva de la comunicación, las propiedades únicas observadas en los nanomateriales serán las que determinen la anchura de banda adecuada para la emisión de radiación electromagnética, los rangos temporales o la potencia de la señal emitida.\nDe manera experimental se ha demostrado que es posible recibir y  demodular una onda electromagnética por medio de un  nanorradio, es decir, un nanotubo de carbono resonando electromecánicamente que es capaz de decodificar una onda con amplitud o frecuencia moduladas.\u200b También se han analizado nanoantenas basadas en el grafeno como potenciales emisores de radiación electromagnética en la banda de los teraherzios.\u200b\n\nComunicación molecular\n\nLa comunicación molecular permite enviar información a través de moléculas u otras partículas a escala de nanómetros a micrómetros. Se refiere a la comunicación entre partículas biológicas o dispositivos diminutos que llevan información a cortas distancias en medios acuosos o gaseosos, consiste en la emisión y recepción de señales de información mediante moléculas biológicas, bio-sintéticas o nano-máquinas. La CM posee limitaciones como: degradación de las partículas en el medio acuoso durante la propagación y retardo de la señal de información recibida debido al movimiento browniano de las partículas. \nEl sistema CM contiene tres componentes: transmisor, receptor y canal. \nTransmisor: El transmisor provee la energía necesaria para la generación y almacenaje de partículas y, procesa y controla la cantidad, tipo o concentración de las partículas involucradas. Este involucra un mecanismo de emisión de las partículas al medio cuando la unidad de control le indica el tiempo de su liberación y a su vez realiza la codificación y modulación seleccionada.\nCanal: es un ambiente acuoso o gaseoso donde las partículas diminutas se propagan. Los mecanismos de propagación propuestos son: difusión libre, difusión por el primer golpe, propagación asistida en flujo, propagación asistida por bacterias, propagación neuroquímica, kinesinas sobre microtúbulos, motilidad de microtúbulos sobre kinesinas estacionarias, propagación a través de la unión de brechas, propagación mediante el uso de motores moleculares, entre otros. \nLos mecanismos de propagación son clasificados por su arquitectura:\n• Arquitecturas basadas en el caminar sobre una vía específica a través de sustancias portadoras.\n• Arquitecturas basadas en el flujo en donde las moléculas viajan por difusión sobre un fluido que es predecible en flujo y turbulencia. \n• Arquitecturas basadas en difusión en donde las moléculas se propagan a través de su movimiento natural espontáneo de difusión pero que es afectado por turbulencias en el fluido en el que se desplazan. \nReceptor: contiene sensores o detectores que pueden medir la presencia u ausencia de información en las partículas que recibe y, corrección y detección de errores por el retardo de turbulencia o el choque de las partículas. \nTipos de Modulación\nPara la propagación de moléculas o partículas de información existen diferentes técnicas de modulación, pueden ser empleadas para el mapeo o representación gráfica entre la molécula en el receptor y el símbolo recibido, este puede ser modulado tomando en cuenta las propiedades de la molécula mensajera que llega al receptor para formar o reconstruir la señal de información. Tipos de modulaciones:\n• Modulación por Desplazamiento de Concentración (CSK): consiste en la emisión de un número de moléculas de un mismo tipo que conllevan la información. En CSK la concentración de la molécula recibida representa la amplitud de la señal, esta puede ser afectada por interferencia entre símbolos debido a los excedentes de moléculas anteriores, retardos en la llegada de las partículas de información y/o reacciones químicas que cambian los niveles de concentración. \n• Modulación por Desplazamiento de Molécula (MoSK): técnica en la que se emiten diferentes tipos de moléculas que representan la información, la emisión o liberación de las mismas depende del símbolo a enviar y la detección en el receptor de la concentración en un intervalo específico. \n• Modulación Basada en el Radio Molecular: técnica basada en el radio molecular utilizando isómeros como partículas de información, específicamente aldohexosas. La información se codifica utilizando el radio de las moléculas mensajeras, en su esquema más simple requiere el uso de 2 tipos de moléculas.\n• Modulación por tiempo transcurrido (Time-Elapse Communication): esquema para sistemas de propagación muy lento. \nCapacidad del Canal\nEn un canal de sistema de comunicación con ruido las variables para medir su rendimiento son: la tasa de información alcanzable que se refiere a la medida teórica de cuantos bits como máximo pueden ser transmitidos por el canal en un tiempo determinado y la capacidad del canal que es la tasa máxima alcanzable de información en bits que puede ser transferido por este.\nAplicaciones y modelado de Sistemas de CM\nAplicaciones: \n• Salud: administración dirigida de fármacos, liberación de medicación adaptativa, monitoreo de salud mediante la identificación de sustancias tóxicas, medicina regenerativa para la reconstrucción de tejidos u órganos dañados, ingeniería genética mediante manipulación genética.\n• Aplicaciones Ambientales: monitoreo ambiental para detección de toxinas o contaminantes, degradación de materiales no deseados o contaminantes, detección de reacciones químicas contaminantes por residuos no deseados. \n• Manufactura: control de calidad mediante la identificación de defectos en los productos, construcción precisa de componentes, integrar nano redes en nuevos productos. \n• Otras: monitoreo de infraestructuras, estudio y control del comportamiento de animales y plantas, uso de nanorobot para múltiples áreas. \nVentajas de la Comunicación Molecular:\n• Factibilidad: sistema sencillo de implementar en corto plazo.\n• Escala: tamaño apropiado para utilizar nano-máquinas. \n• Bio-compatibilidad: integración con sistemas vivos.\n• Eficiencia energética: reacciones bioquímicas de alta eficiencia. \nDesventajas de la Comunicación Molecular: \n• Aleatoriedad: propagación aleatoria de las moléculas.\n• Retardo: los tiempos de propagación son muy largos comparados con la velocidad de la luz. \n• Alcance o cobertura: algunas técnicas tienen rangos prácticos y cortos.\n• Fragilidad: los componentes biológicos pueden ser sensitivos a su ambiente.\nHerramientas de Simulación\nLa comunicación molecular requiere de equipos de alta tecnología y de un alto grado de precisión a escala nano con herramientas de modelado biológico-ingenieril con características reales a micro-nano escala para modelar y verificar u analizar el rendimiento de los avances planteados antes de la experimentación.\nEntre los simuladores más relevantes encontramos: \n• dMCS: simulador de comunicación molecular distribuido basado en arquitectura de alto nivel.\n• NanoNs: es un simulador de nano redes moleculares el cual fue creado basado en el simulador de redes ns-2.\n• N3Sim: simulador para sistemas de comunicación molecular que permite evaluar el rendimiento bajo un nivel de concentración específico con múltiples transmisores y receptores. \n• MUCIN: simulador basado en MATLAB de sistemas de CM de extremo a extremo que utilizan sistemas de propagación por difusión del primer golpe. \n• BNSim: simulador para sistemas de CM entre bacterias de código abierto, paralelo, estocástico, y la plataforma de modelado multi-escala que integra diversos algoritmos de simulación, junto con circuitos genéticos y modelos vía quimio tácticos en un entorno 3D complejo.',
      'negative_11': 'Carnaval de Huelva\n\nSiglo XIX\n\nUna de las cosas que más caracteriza a los pueblos son sus diversiones, y entre éstas, así en los tiempos antiguos como en los modernos, descuella en primer lugar esa fiesta semi-pagana que se celebra en el domingo de quicuagésima con el nombre de Carnestolendas o Carnaval. No parece sino que entre las gentes se pierde la razón y se posesiona la locura desde muchos días antes en que la señala el calendario.\nEn Huelva, era costumbre, desde el mes anterior, dar bromas pesadas, ellas a ellos y viceversa, tomándose confianza de tal índole que en otros días pudieran parecer repugnantes y vergonzosas. Las criadas de servicios, por ejemplo, y otras muchachas de la misma clase social, perseguían a los caballeros, corrían tras de ellos para quitarles una prenda cualquiera, el pañuelo del bolsillo, el reloj, la copa o el sombrero, conseguido lo cual iban a la confitería, si estaba a mano, a la tienda de comestibles más cercana, y empeñaban la prenda por algunas golosinas, caramelos o castañas pilongas. Naturalmente, los hombres esquivaban el compromiso y, cuando se veían cogidos por ellas, procuraban desquitarse dándoles empujones y , a veces, intentaban meter sus manos en los ocultos pechos.\nPero mientras eso hacían las criadas de servicio, las señoritas mejor educadas, unas en las ventanas, que entonces eran salientes y con celosías, y otras en los balcones, también se tomaban confianza y se daban bromas de mal género. Las de las ventanas con un guante lleno de serrín o de arena, amarrado en una caña o palo, tocaban el hombro al caballero por allí pasaba y, cuando este se volvía para ver a la joven que le había tocado, ésta alzaba el guante y con el le daba una bofetada en el rostro. Las de los balcones, en vez del guante, usaban unos saquitos llenos a veces de tierra y amarrados por la boca una cuerda larga, los dejaban caer sobre las cabezas de los transeúntes, derribándoles el sombrero y, por consiguiente, produciéndoles en alguna ocasión fuertes contusiones en la cabeza; mientras que otras más ocultas, se aprovisionaban de un latón vacío, lo rellenaban de cáscaras o conchas de verdigones o almejas y, arrollándoles una cuerda sujeta al balcón, lo dejaban caer dando vueltas y produciendo un ruido de dos mil demonios, asustando así a los que por debajo pasaban.\nPero cuando se desbordaban las bromas era en esos tres días de carnaval, domingo, lunes y martes, en los cuales se llegaba al frenesí de la locura, pues los hombres montados en carros, con grandes tinas de agua y provistos de jeringas, las cargaban con el expresado líquido que lo dirigían a las señoras que estaban en los balcones y en las ventanas, mientras que ellas, armadas igualmente del mismo instrumento, lo descargaban sobre ellos produciéndose un tiroteo de chorros de aguas, en esa especie de batalla campal, que todos ponía como patos desde los pies a la cabeza y dejándolos en estado tal como presuntos candidatos a grandes enfriamientos, y tal vez como aspirantes de inmediatas pulmonías.\nMás tarde se fueron mejorando esas costumbres tomando la fiesta un carácter más culto, pues salía con música el dios Momo en una carroza adornada suntuosamente y rodeado con sus locos servidores, con trajes muy vistosos; y de los balcones se arrojaban papelillos de colores y confetis.\nTambién recorrerían las calles de la ciudad otras varias comparsas de estudiantes, marineros y mujeres, unas con guitarras y flautines, otras con trombones y las últimas con panderetas, cantando coplas alusivas a lo iban representando y, a veces, picaban en asuntos políticos.\nPero terminada la fiesta del Carnaval y entrada ya las gentes en plena Cuaresma, después del Miércoles de Ceniza, en el que nos recuerda la iglesia que somos polvo y en polvo nos hemos de convertir, vuelve a reproducirse la función pagana con igual locura. Su única diferencia consiste en que por la noche suele haber algún baile y al final de este se rompe la piñata llena de confituras. El Carnaval en esencia, siempre fue lo mismo: desenfreno y diversión\u200b\n\nCUARTETOS\n\n1º- EL INDIO, APOLO Y COLON Y UN FRAILE CRITICON.- Peña Los Mojarras; Letras Miguel Barba, Música la agrupación- Huelva.\n2º- CUATRO JODIENTES Y UN PACIENTE.- Peña El Choco; Pépe Pulido- Huelva.\n1ºAccesit-CARNAVAL-  Sin Peña o Asociación; Letra y Música del grupo, Dirección Manuel Rodríguez]- Huelva.\n\nCHIRIGOTAS\n\n1º- LOS BOQUERONES ATOMICOS.- Peña El Boquerón; Letra y Música del grupo, Dirección Cinta Hdez- Huelva.\n\nMURGAS\n\n1º-LOS PINTORES DE BROCHA GORDA.- Peña Playa La Gilda; Curro Morató y José Luís Montero -Huelva.\n1º- CHARLIE PAYASO.]- Peña La Máscara; Roque Rodriguez- Huelva.\n\nCOMPARSAS\n\n1º- LOS MUSIQUEROS LOCUELOS.- El Choco; Letras de M. Muiño, Pepe Vega y Pepe Pulido, Música y Dirección Manuel Muiño- Huelva.\n2º-LAS GAVIOTAS.- Peña Playa La Gilda; Letras y Música de la agrupación, Aglutinador de esfuerzos , que no director Paco Escudero- Huelva.\n\nAÑO 1985\n\nII CONCURSO (21 grupos)\nAutor del Cartel MANUEL SEISDEDOS ROMERO (Huelva) - (Por segunda vez)\nPregonero RAMON LLANES\nChoquera Mayor AURORA CALERO DELGADO (Sin Peña o Asociación)\n\nChoquera Infantil MARIA PILAR TENOR (Sin Peña o Asociación)\nPresidente de la Comisión del Carnaval DIEGO BELTRAN MOJARRO\n\nCUARTETOS\n\n1º-THE R´POLLAS.- Los Mojarras; Letras Miguel Barba, Música la agrupación-Huelva. 1ºPremio Provincial de Isla Cristina.\n2º-LOS DESCUBRIDORES- Los Descubridores; Manuel Rodríguez "El Cai"- Huelva. (presentada sin peña o asociación)\n3º-LOS PENDONES FLACIDOS- Sin Peña o Asociación -Huelva.\n4º-LAS COLONAS.- La Noria; Magdalena Mora Jiménez -Huelva. 2ºPremio Provincial de Isla Cristina Video\n\nCHIRIGOTAS\n\n1º-LAS ARISTOGATAS.- Playa La Gilda; Curro Morató- Huelva.\n2º-LAS FLORES CHISMOSAS- La Máscara; Manuel A. Muñoz- Huelva.\n3º-LOS QUINTOS DEL CENTENARIO.- Sin Peña o Asociación -Huelva.\n4º-LOS VERDES CAMPESINOS.- El Boquerón -Huelva.\n5º-- Sin Peña o Asociación -Huelva.',
      'negative_12': 'Forjado con dado abierto y con dado cerrado\n\nIntroducción\n\nEl forjado es un proceso en el que, por medio de fuerzas de compresión sucesivas aplicadas a través de matrices, dados o herramientas, se conforma la pieza. Es uno de los procesos más antiguos de trabajo con metales, datando al 8000 a. c.; se utilizaba para la obtención de monedas y joyería, martillando el metal con herramientas de piedra.\nSe puede realizar la forja de forma tradicional con un marro de mano, o maceta y un yunque. Sin embargo, la mayor parte de las forjas requieren un conjunto de matrices, prensas o marinetes. Las operaciones de forjado a diferencia que las operaciones de laminado producen piezas discretas.\nLos productos más típicos que se pueden obtener a través del forjado son: tornillos, remaches, ejes de turbinas, engranajes, bielas, piezas estructurales para maquinaria, aviones, ferrocarriles…\nPara que las piezas forjadas tengan buena resistencia y tenacidad se puede controlar el flujo del metal y la estructura del grano, así se pueden usar en aplicaciones donde se requieran grandes resistencias.\nEl forjado se puede realizar a temperatura elevada (forjado en caliente) o a temperatura ambiente (forjado en frío).\nEn el forjado en caliente se requieren menores esfuerzos pero se obtiene un acabado superficial y una precisión dimensional no tan buena como en el forjado en frío que aunque requiere mayores fuerzas por la alta resistencia que ofrece el material se obtienen mejores resultados de precisión y acabado superficial, también existe el inconveniente que en el forjado en frío el material de la pieza debe tener ductilidad suficiente a temperatura ambiente.\nEn general, las piezas que ya han sido forjadas requieren operaciones de acabado, como tratamiento térmico para modificar sus propiedades, o maquinado para obtener las dimensiones exactas. Estas operaciones pueden ser reducidas al mínimo con el forjado de precisión así pues se consigue una reducción del coste de manufacturación para llegar al producto final.\nUna pieza que se puede forjar también puede fabricare por otros métodos, por metalurgia de polvos, por fundición o por maquinado. Sin embargo, en cada proceso se obtienen piezas con distintas características y limitaciones, sobre todo en las propiedades de tenacidad, acabado superficial, resistencia, defectos externos o precisión dimensional.\n\nForjado con dado abierto\n\nEste forjado es un proceso muy sencillo, la mayor parte de piezas forjadas con este método pesan de 15 a 500 Kg, se han forjado piezas hasta de 300 toneladas, como por ejemplo hélices de barco o hélices de helicópteros.\nEste proceso se puede describir como una pieza sólida colocada entre dos matrices planas o dados, cuya altura se reduce por compresión. Este proceso también recibe el nombre de recalcado o forjado con dado plano. Las superficies del dado pueden tener cavidades sencillas para producir forjados sencillos. En este proceso se mantiene el volumen constante, toda la reducción de la altura provoca el aumento del diámetro de la pieza forjada.\nEn las operación reales de forjado con dado plano la pieza no se deforma exactamente de forma uniforme sino que desarrolla una forma abarrilada llamada “pancaking” debida principalmente a las fuerzas de rozamiento en la interfases entre pieza y dado que se oponen al flujo de los materiales hacia fuera, éste fenómeno puede reducirse con el uso de un lubricante eficaz.\nTambién puede darse el caso de abarrilamiento al aplanar en dados fríos piezas caliente ya que el material se enfría con rapidez en las interfases y cerca de ellas mientras que el resto de la pieza se mantiene caliente, así el material en los extremos de la pieza es más resistente que el centro, lo que produce una dilatación más en dirección lateral en el centro que en los extremos. Este abarrilamiento producido por los efectos térmicos se puede reducir calentando los dados previamente o utilizando una tela de fibra de vidrio como barrera térmica colocándola entre la pieza y el dado.\nEl desbaste, "doping out", es una operación de forjado principalmente en dado abierto en la que a través de pasos sucesivos de forjado en intervalos específicos se puede disminuir el espesor de una barra larga (como el área de contacto entre pieza y herramienta es pequeña en el golpe se puede reducir el espesor sin la aportación de grandes fuerzas ni maquinaria), estas operaciones son realizadas por herreros en las que utilizan martillo y yunque, con piezas calientes de metal, así pueden fabricar:,contornos, rejas de hierro…\n\nFuerza de forjado con dado abierto\n\nLa fuerza de forjado γ en una operación de forjado con dado abierto sobre una pieza sólida cilíndrica, se puede calcular con la fórmula:\nDonde Yf es el esfuerzo de fluencia del material, μ es el coeficiente de fricción, r es el radio de la pieza y h la altura de la pieza.\n\nForjado con dado impresor o forjado con dado cerrado\n\nEl forjado con dado impresor o forjado con matriz de impresión la pieza a fabricar adquiere la forma de los huecos o cavidades al forjarse entre dos matrices con perfil.\nCuando se realiza esta operación algo de material fluye hacia fuera y forma una rebaba, ésta tiene un papel importante en el flujo del material en el estampado ya que es delgada, se enfría rápidamente y al ejercer una resistencia gracias a la fricción que existe entre la rebaba y la matriz, somete a grandes presiones al material en la cavidad de la matriz causando así el rellenado de la cavidad.\n\nLas piezas a forjar pueden ser preparadas previamente con otras operaciones como:\na) Corte o recorte de una barra estirada o extraída. \n\nb) Operaciones de preconformado, como por ejemplo la metalurgia en polvos.\n\nc) Fundido. Una pieza bruta preformada en un forjado anterior. La pieza en estado bruto se coloca en el dado inferior y al empezar a descender el dado superior la forma de la pieza cambia de forma progresiva.\n\nLos procesos de preformado, como el forjado con dados convexos y cóncavos, se utilizan para distribuir el material en las diferentes zonas de la pieza bruta, parecido a cómo se conforma la masa para hacer bizcochos.\nEn el forjado con dado cóncavo, el material de la pieza se aleja de una región. En el forjado con dado convexo se junta en una región localizada. Seguidamente a la pieza se le da la forma aproximada de la forma final con un proceso llamado bloqueo utilizando dados bloqueadores. Finalmente es el acabado del proceso de forja en matrices de estampado en el que la pieza obtiene su geometría final. La rebaba se elimina normalmente mediante troquelado.\nEn el proceso verdadero de forjado con dado cerrado o sin rebabas, éstas no se forman y el material de la pieza en bruto llena completamente las cavidades del dado. Es imprescindible el control del volumen del material y el del diseño correcto de la matriz para poder conseguir un forjado con matriz cerrada que tenga las dimensiones y tolerancias deseadas. Un mal control del volumen del material puede ocasionar que coloquemos piezas brutas pequeñas y no llenen completamente las cavidades del dado o por el contrario las piezas demasiado grandes pueden producir presiones excesivas y pueden hacer que los dados fallen prematuramente o se aplasten.\n\nDiseño del dado de forjado\n\nPara diseñar los dados es imprescindible conocer la ductilidad y resistencia del material de la pieza, su sensibilidad a la temperatura y a la velocidad de deformación, la forma y la complejidad de la pieza y sus características de fricción. Un efecto importante a tener en cuenta es la distorsión de los dados bajo las grandes cargas a las que se somete durante el proceso de la forja, especialmente si se requieren tolerancias dimensionales cerradas.\nEl aspecto más importante a tener en cuenta cuando se estudia el diseño de dados es que la pieza fluye en la dirección con menor resistencia, en consecuencia se debe conformar la pieza (forma intermedia)de tal modo que llene bien las cavidades del dado. El preformado de la pieza tiene gran importancia, ya que en una pieza bien preconformada o preformada, el material no debe fluir fácilmente hacia la rebaba, el patrón de flujo de grano debe ser favorable y se debe disminuir el deslizamiento excesivo en las caras que se encuentran en contacto entre dado y pieza para minimizar el desgaste.\nPara elegir las formas se requiere de gran experiencia y realizar bien los cálculos de la sección transversal de la superficie en cada lugar donde se realice la forja.\nSe han desarrollado técnicas para diseñar mediante computadoras para expeditar estos cálculos, así como para deducir la pauta del flujo del material en la cavidad del dado y la formación de defectos. Como consecuencia de que el material sufre diferentes grados de deformación a distintas velocidades y en distintas zonas de las cavidades del dado, las propiedades mecánicas de cada lugar son específicas de la forja.\nPara la mayor parte de las forjas o piezas forjadas, la línea de partición suele estar situada en la sección transversal máxima de la pieza. Para las formas simétricas sencillas, normalmente es una recta en el centro de la pieza forjada y para las piezas con forma más complejas esta línea puede no estar en un solo plano, por esto se suelen diseñar dados de la forma que se traben durante el acoplamiento para evitar empujes naturales y así equilibrar las fuerzas manteniendo el alineamiento durante el forjado.\nDespués de limitar de forma suficiente el flujo lateral para asegurar un llenado óptimo de las cavidades del dado, se deja que el material de rebaba fluya por un conducto llamado canal de rebaba para que si existe rebaba adicional no aumente de forma innecesaria la fuerza de forjado. Un lineamiento general para holguras de rebaba entre dados es el 3% del grosor máximo de la forja. La longitud de la cara suele ser de 2 a 5 veces el espesor de la rebaba. Con los años se han estudiado distintos diseños del canal de rebaba.\nLos ángulos de salida son imprescindibles en casi todos los dados de forjado, para ayudar a separar la pieza del dado una vez terminada la operación de forjado. Al enfriarse la pieza se contrae en dirección longitudinal y radial simultáneamente, por lo que lo que los ángulos de salida internos se hacen mayores que los ángulos externos. Los ángulos internos varían de 7 a 10º y los externos de 3 a 5º.\nEs importante escoger los radios de transición adecuados en las esquinas y los biseles, así se asegura el flujo uniforme del metal hacia la cavidad del dado y mejora la vida útil de éste. En general se deben despreciar los radios pequeños por su efecto adverso sobre el flujo del metal y por su propensión a desgastar con rapidez (como resultado de la los ciclos térmicos y concentración de esfuerzos). Además los radios pequeños de bisel pueden ser la causa de la ruptura de los dados por fatiga. Así pues, estos radios deben ser tan grandes como lo permita el diseño de la pieza forjada.\nLos dados se pueden ensamblar mediante insertos en lugar de hacerse de una sola pieza y más si las formas son complicadas, mediante este método de ensamblamiento se reduce el coste de fabricación de varios dados semejantes. Los insertos se pueden fabricar con materiales más duros y fuertes y se pueden cambiar fácilmente en caso de fallo o desgaste en una zona determinada.\nSe deben prever tolerancias en el diseño de los dados ya que se puede precisar del maquinado de la pieza forjada para obtener las dimensiones y el acabado superficial final. Estas tolerancias de maquinado deben preverse en orificios, bridas y superficies conjuntas.\n\nMateriales y lubricación de los dados\n\nLa mayoría de las operaciones de forjado especialmente para grandes piezas se realizan a elevadas temperaturas. Los requerimientos comunes para los materiales del dado son: \na) gran tenacidad y resistencia a altas temperaturas. \n\nb) capacidad de endurecimiento de forma uniforme.\n\nc) resistencia al choque mecánico y térmico.\n\nd) resistencia al desgaste, especialmente al desgaste abrasivo, por la existencia de cascarilla en la forja en caliente.\nLa elección de los materiales idóneos para la fabricación de los dados depende de factores tales como la composición y las propiedades de la pieza, la complejidad de la forma, su tamaño, la temperatura de forjado, el tipo de operación de forjado, el coste de los materiales del dado y la cantidad demandada de forjas. Otro factor importante es la transferencia de calor desde la pieza caliente a los dados con la consiguiente distorsión de estos.\nLos materiales más comunes utilizados para la fabricación de los dados son los aceros de herramienta y para los dados que trabajan a altas temperaturas materiales que contienen cromo, níquel, molibdeno y vanadio.\nLos dados se obtienen a partir de bloques, que a su vez se forjan a partir de fundición, más tarde se maquinan y se terminan con la forma y acabado superficial deseados.\nEn la fabricación de los dados se pueden presentar fallas debido a razones que se describirán en la sección de: falla de dados, donde también se describen métodos de fabricación de dados.\nLos lubricantes son esenciales e influyen en la fricción y desgaste como resultado sobre las fuerzas requeridas (ecuación 1) y sobre el flujo del metal en las cavidades del dado. Otro aspecto importante del lubricante es que puede actuar como barrera térmica entre la pieza caliente y los dados que se encuentran relativamente fríos, disminuyendo la velocidad de enfriamiento de la pieza y mejorando el flujo del metal. También sirve como agente de desprendimiento ya que impide que la pieza forjada se pegue en los dados.\nEn el forjado se puede emplear gran variedad de lubricante. Para una forja caliente se suelen emplear grafito, disulfuro de molibdeno, y, a veces, vidrio. Para la forja en frío los lubricantes que se usan generalmente son aceites minerales y jabones, aplicados después del recubrimiento de conversión de las piezas brutas. En la forja en caliente el lubricante se suele aplicar directamente sobre los dados, mientras que en la forja en frío se aplica sobre la pieza. El método de aplicación y la uniformidad del espesor del lubricante son muy importantes para la calidad del producto forjado.\n\nMétodos de fabricación de dados\n\nPara la fabricación de dados se pueden utilizar distintos métodos de manufactura, de forma única o en combinación. Entre ellos está: la forja, la fundición, el esmerilado, el maquinado, métodos electroquímicos y eléctricos de estampado de dados. El proceso de obtención de las cavidades de los dados suele ser el punzonado, sea en frío o en caliente. También se puede utilizar para fabricar dados pequeños con cavidades superficiales. Generalmente los dados se tratan térmicamente para que obtengan mayor resistencia al desgaste y dureza. Si lo requieren, su contorno y acabado superficial se mejoran con rectificado y pulido, con robots industriales programables o a mano.\nLa elección del método de fabricación depende de la operación en la que se va a usar el dado, así como de su forma y tamaño. Generalmente los costes determinan el proceso a seleccionar ya que éstos son importantes en las operaciones de manufactura. Aunque los dados sean pequeños y relativamente sencillos pueden llegar a costar cientos de euros. Sin embargo, debido a que se fabrica una gran cantidad de piezas utilizando el mismo dado, en general el coste por unidad suele ser sólo una pequeña parte del coste de fabricación de la pieza.\nLos dados se suelen clasificar como machos y hembras o por su tamaño. Generalmente, los dados pequeños son aquellos que tienen una superficie entre 2 cm a 1 m cuadrados, mientras que los grandes tienen superficies desede 1m cuadrado a mayores.\nLos dados pueden ser fundidos en aceros, fundiciones y aleaciones no ferrosas. Los procesos utilizados van desde el moldeo en cáscara (para los dados pequeños) a las fundiciones en arena (para dados grandes que pesan varias toneladas). \nEn general se prefieren los aceros fundidos para dados de grandes piezas debido a su resistencia y tenacidad y por la facilidad a la hora de controlar su composición, propiedades y tamaño de grano. Según cómo se solidifiquen, los dados fundidos, a diferencia de los de metal forjado o laminado, pueden no tener propiedades direccionales; pueden presentar las mismas propiedades en todas sus superficies de trabajo, no obstante, debido a la contracción, puede dificultarse el control de tolerancias dimensionales, en comparación con los dados maquinados.\nLo general es que los dados se maquinen a partir de bloque forjado, con procesos como rectificado, torneado, fresado, maquinado electroquímico y eléctrico. Puede resultar complicado el maquinado cuando los materiales son de alta resistencia, duros, con resistencia al desgaste o los que son tratados térmicamente.\nLas operaciones pueden consumir mucho tiempo, es por esto que se utilizan muchos procesos no tradicionales de maquinado especialmente en los dados pequeños o medianos ya que son más rápidos y económicos y los dados suelen no requerir acabado adicional. Los dados de diamante, para alambres finos, se fabrican produciendo orificios con una aguja giratoria delgada cubierta con polvo de diamante y con aceito como lubricante.\nLos aceros para dados se tratan térmicamente para mejorar la dureza, resistencia al desgaste y resistencia en general. Un mal tratamiento térmico es una de la causas más comunes de fallo de dados ya que los puede distorsionar por acción de cambios microestructurales y por ciclos térmicos no uniformes.\nLa selección adecuada de temperaturas y atmósferas del tratamiento térmico, los medios, el templado, la práctica del revenido y el manejo son importantes. Los dados se pueden someter a distintos tratamientos superficiales para mejorar sus características de desgaste y fricción. La condición y composición de las superficies del dado tienen especial importancia.\nDespués del tratamiento térmico, los dados son sometidos a operaciones de acabado, como rectificado, pulido…para obtener el acabado y precisión dimensional deseada. \nEl proceso de rectificado puede causar daños en la superficie si no se controla bien, debido al exceso de calor que se puede producir, y pueden incluir en la superficie esfuerzos residuales que reducen su vida a fatiga. Las ralladuras en las superficies pueden actuar como foco de concentración de tensiones. De igual manera los procesos de fabricación de dados pueden causar daños y grietas superficiales a menos que se controlen de forma exhaustiva los parámetros del proceso.\n\nFallos en los dados\n\nEstos fallos se deben generalmente en las operaciones de manufactura, a una o más causas que se citan a continuación: \na) diseño inadecuado.\n\nb) defecto del material.\n\nc) sobrecalentamiento y agrietamiento térmico.\n\nd) tratamiento térmico y operaciones de acabado inadecuados.\n\ne) sobrepeso.\n\nf) desgaste excesivo.\n\ng) mal uso y manejo inadecuado.\nEl diseño adecuado es muy importante. Para resistir las fuerzas en los procesos de manufactura, un dado debe tener secciones transversales, holguras adecuadas y las esquinas agudas. Los biseles y radios, así como los cambios abruptos en sección transversal actúan como concentradores de tensiones. Los dados se pueden segmentar, y preesforzarse durante el ensamblado para mejorar su resistencia.\nEl manejo, ensamble, instalación y alineamiento de los dados es de gran importancia. La sobrecarga en herramientas y dados puede causar fallos prematuros. Por ejemplo, una causa común en los dados para la extrusión en frío es que el operador de un robot no quite la pieza terminada antes de que la otra pieza en bruto se cargue.\nMateriales utilizados para los dados tales como los carburos y el diamante, a pesar de su dureza y resistencia a la abrasión, son susceptibles al rebabeo y al alargamiento debido a las fuerzas de impacto o por efectos térmicos causados por variaciones de temperatura en el interior. \nIncluso los fluidos de trabajo pueden afectar negativamente los materiales del dado y herramienta, por ejemplo, el cloro en los lubricantes, los aditivos con azufre y enfriadores pueden dañar el aglutinante de cobalto en el carburo de tungsteno disminuyendo su resistencia y tenacidad.\nIncluso si se fabrican de forma correcta, los dados se someten a altas temperaturas y a grandes esfuerzos durante el proceso, que pueden producir desgaste y (en consecuencia) cambios de forma. El desgaste de los dados se debe de tener en cuenta ya que cuando cambian su forma, las piezas producidas a su vez tendrán dimensiones incorrectas. \nDurante su empleo, los dados pueden sufrir agrietamiento térmico, debido a ciclos térmicos especialmente en la fundición en dados. Para evitar este defecto y la rotura eventual en operaciones en caliente, se suelen precalentar los dados a temperaturas entre 1500 y 2500\xa0°C. Los dados desgastados o con grietas pueden ser reparados con soldadura y de depósito de metal, que incluyen los láseres.\nSe pueden diseñar y fabricar dados con insertos reemplazables cuando se desgasten o se agriéten. El diseño y la colocación de los insertos debe ser estudiada minuciosamente ya que cualquier fallo en estos aspectos puede producir la rotura de estos. Los fallos y fractura de los dados pueden ser peligrosos para los empleados de plantas manufactureras.\nEs posible que los dados que esperan en un cajón se desintegren repentinamente, debido al estado de grandes esfuerzos internos de sus componentes (esfuerzos residuales). Las piezas que se rompen salen despedidas a gran velocidad y pudiendo causar graves lesiones. Las matrices deben rodearse de defensas metálicas que deben ser bien diseñadas y tener resistencia para contener las piezas fracturadas en caso de fallo.',
      'negative_13': 'El Bonillo\n\nClimatología\n\nSe caracteriza fundamentalmente por inviernos fríos, con medias invernales muy bajas, registrándose temperaturas por debajo de 0\xa0ºC. Son frecuentes las nevadas a lo largo del período invernal.\nSus veranos suelen ser calurosos y secos, en los que se superan ampliamente los 30\xa0°C.\nCon una pluviosidad no demasiado acusada se registran aproximadamente 400-600 mm. de media anual.\nOtra de las particularidades climatológicas es la gran presencia que el viento tiene en la localidad, no en vano han sido instalados varios parques eólicos dentro de su término.\n\nHistoria\n\nEn 1212 tiene lugar la batalla de Las Navas de Tolosa, y tras esta victoria cristiana, el rey castellano Alfonso VIII se dirige a la fortaleza de Alcaraz, y tras un azaroso asedio, conquista la plaza y entra en ella el 23 de mayo de 1213. Establece en todo el territorio conquistado un extenso alfoz, que coincide con todo el oeste y el sur de la actual provincia de Albacete, dotándolo de un fuero, basado en el de Cuenca y que incardina en él a El Bonillo, repoblando su territorio con colonos castellanos traídos por la Corona.\nLa tradición popular afirma que el término municipal, en época medieval, estaba compuesto por infinidad de núcleos poblacionales (como demuestran los restos de iglesias y ermitas) distando poco entre sí (ermita de Pinilla, ermita de -hoy Sotuélamos-, iglesia gótica en Cerro Bueno -la actual iglesia de Santa Catalina-, ermita de la Magdalena, Santa Ana, convento de los agustinos, ermita de San Roque, ermita de la Pura), aunque los más importantes eran la aldea de Sotuélamos (Soto de Álamos), San Miguel de Susaña y Santa Catalina (cerca de las Salinas de Pinilla). Éstas, a caballo entre los siglos XII y XIII, se unieron en Cerro Bueno formando lo que hoy es El Bonillo, en el sitio donde se encontraba una pequeña iglesia de estilo gótico.\nLa explicación del proceso parece confirmada arqueológica e históricamente. Sin embargo, los topónimos trasmitidos no tienen ninguna confirmación etimológica y apenas sentido. Lo más plausible es que Sotuélamos y El Bonillo, procedan de términos latinos trasmitidos y deformados a través del árabe y el mozárabe, y que los pretendidos Soto de Álamos y Cerro Bueno, no sean más que explicaciones populares a posteriori sin fundamento.\nSe dice que la unión tuvo lugar porque estos tres núcleos de población se hallaban situados en vaguadas que, en época de lluvias, eran de fácil inundación y porque en El Bonillo había mucha caza y buenas tierras. Poco después, en 1538 se le concede la segregación del  Alfoz de Alcaraz.\nDe estas tres aldeas originales se conserva:\n- Sotuélamos: la ermita y la propia aldea, que actualmente se sigue utilizando, y donde hasta hace pocos años había un núcleo permanente de población, siendo pedanía de El Bonillo. En esta pedanía construyó su casa palaciega, y donde descansan sus restos mortales, don Alberto Bosch y Fustegueras, Alcalde de Madrid, Ministro de Fomento y diputado por la provincia de Albacete en 1843.\n- Complejo Lagunar de Navalcudia-Susana: se compone de varias lagunas endorreicas que aparecen en épocas de importantes lluvias y a las que acuden aves migratorias.\n- San Miguel de Susaña: data de la época romana y se conservan las ruinas de una antigua posada actualmente conocida como Casa Redonda (el nombre hace referencia a su especial construcción) y vestigios de una calzada romana que iba desde la antigua Libisosa (hoy Lezuza) hasta Laminio (Alhambra). Todavía se conservan la espadaña de la iglesia y el cementerio, aunque este último en terrenos de propiedad privada. En los terrenos cercanos a la aldea los labradores habían encontrado recipientes de cerámica y monedas romanas. En las proximidades se ha instalado un mirador de aves esteparias ya que toda la zona está declarada como zona de especial protección de aves (ZEPA).\n- Santa Catalina: era una aldea sujeta al convento de los Templarios, de estilo románico, habitado por los caballeros de la Orden del Temple. Se conservan las pinturas en el artesonado, tapado por las bóvedas (entre el tejado y éstas). Santa Catalina estaba cerca de las Salinas de Pinilla, que son de remotísima antigüedad. Parece ser que los romanos las aprovechaban y prueba de ello son los restos de un campamento romano descubierto en las inmediaciones de las lagunas, llamadas de las Salinas. Pasaron a ser en 1620 propiedad real, llamándoselas El Real Saladero de Pinilla. Con la desamortización de Mendizábal pasaron a manos privadas.\nFormado el pueblo, absorbiendo a la población circundante, El Bonillo formaba parte de la jurisdicción de Alcaraz.\nEn marzo de 1475 Alcaraz se rebela contra el marqués de Villena, poniéndose de parte de los Reyes Católicos; los habitantes de El Bonillo también se alzaron en armas y solicitaron la ayuda del concejo alcaraceño. Estos enviaron sus tropas que, engrosadas con las reclutadas en El Bonillo, se pusieron en marcha para liberar al pueblo de Munera del dominio del marqués, dando así inicio a la Guerra de Sucesión Castellana.\nEl 27 de noviembre de 1532 la emperatriz Isabel le concede facultad para sentenciar sus propias causas civiles, siempre que no excediesen de los 400 maravedíes. La misma emperatriz Isabel, el 11 de enero de 1534 le cedía la propiedad de la Dehesa Nueva. Posteriormente el emperador Carlos I le otorga el título de Villa por una carta privilegio dada en Barcelona el 12 de febrero de 1538: «Haciéndole merced a la Villa de El Bonillo de eximirla de la ciudad de Alcaraz donde era sujeta, y hacerla villa de sí y sobre sí y darle jurisdicción civil y criminal (...) Y os damos poder y entera facultad para que podáis poner y tener, y pongáis y tengáis horca y picota (...)». Esta picota es el rollopicota, hoy conocido como Rollo de San Cristóbal, donde se ajusticiaba y exponía a los reos a la vergüenza pública.\nEl 20 de junio de 1566 Felipe II ratificó la concesión otorgada por Carlos I, y le amplió la jurisdicción «(...) Se le amplíe y acreciente de nuevo dos terceras partes de dos leguas vulgares que hay de término desde la Villa de El Bonillo hasta el mojón de Villarrobledo que es junto a la ermita de Sotuélamos (...) y que la misma ampliación se le de a la redonda y contorno de la dicha Villa de El Bonillo»..\n\nEconomía\n\nEn 2008 fue inaugurada una planta de energía termosolar capaz de suministrar electricidad a 800.000 habitantes, más del doble de la población en 2017 de toda la provincia, así como varias plantas de energía solar, entre las que destaca la situada en la finca El Guijoso, de 2,5 MW de capacidad.\nPosee en su término varios parques de energía eólica.\nTambién es conocida la zona por sus bodegas: en la mencionada finca El Guijoso se encuentra una de las más singulares de España, ya que tiene el reconocimiento de D.O. Pago Guijoso:  Bodegas y Viñedos Familia Conesa,\u200b que pertenece a la Asociación de Turismo Enológico de Castilla-La Mancha y es foco de atracción turística. \nOtra bodega conocida en la zona es Finca Élez, que posee igualmente denominación de origen propia, D.O. Finca Élez\u200b y que cuenta también con rutas enológicas.\nLa caza es otra fuente importante de ingresos, ya que el término cuenta con varias fincas de caza menor.\nSigue siendo un pueblo eminentemente agrícola con una destacable actividad ganadera (ovina, caprina, avícola y porcina) y de la construcción.\n\nExiste un incipiente «proyecto de dinamización turística» basado en: \n1.- La actividad cinegética.\n2.- La posición geográfica, (Ubicación intermedia entre el Parque Natural de las Lagunas de Ruidera y la Sierra de Alcaraz).\n3.- La producción artesanal de vino y queso, su difusión y puesta en valor.\n4.- La conservación del pequeño casco antiguo de la Villa.\n5.- La riqueza, calidad y amplitud del patrimonio gastronómico tradicional. (Alrededor de la actividad hostelera local).\n\nCampo de golf\n\nActualmente existe un campo de golf en las inmediaciones de El Bonillo donde se puede practicar este deporte.\nEl Campo de Golf La Lagunilla de El Bonillo es un campo de golf de 9 hoyos de reciente construcción, que fue inaugurado en junio de 2009. Es el primer campo de la provincia de Albacete y el único público de Castilla-La Mancha.SITUACIÓN: GPS. X 538810 Y 4310709 N 385639.4 W 23309.1\nEstá situado en el paraje La Lagunilla, en la carretera que va al Parque natural de las Lagunas de Ruidera. Cuenta con una cancha de prácticas, y mantiene un calendario anual de aproximadamente 20 torneos. Está homologado por la Real Federación Española de Golf.\n\nEntorno ambiental\n\nEl municipio de El Bonillo se sitúa entre cabeceras fluviales, justo en la divisoria hidrográfica de las cuencas de los ríos Guadiana (Guadiana Alto), y del río Lezuza (afluente "libre" hacia el Júcar). En él se sitúa la segunda cumbre más alta del Campo de Montiel, Los Barreros, de 1.102 msnm, que es el sector de la recarga principal del sistema acuífero 24, y donde se sitúan los nacimientos de algunos de los ríos esteparios montieleños y de la alta llanura, como el Córcoles, o el citado Lezuza; pero también como zona principal donde se originan las primeras fuentes de cabecera del Guadiana Alto, más arriba de las mismas Lagunas de Ruidera, como el arroyo Alarconcillo, el cual aporta las primeras aguas a éstas en los periodos lluviosos.\nHacia la zona oriental, próximos al límite con el término municipal de Lezuza, se ubican una veintena de pequeños navajos o esteros, algunos de más de 50 ha, que componen un único complejo torcal ligado a un mismo origen por hundimientos de disolución del zócalo calizo-dolomítico, tipo dolinas de Karst, que reciben ciertos nombres topográficos como: Laguna de Navalcudia (que da el nombre genérico al complejo), Navajoluengo, Nava Redonda, Los Melchores, Navajo Guijoso, etc. Estos enclaves, aunque secos en buena parte del año, debido en parte a que son centros de percolación de aguas, como magníficos higrohumedales para la conservación de la biodiversidad local, a pesar de lo erróneo que se declara en las fichas técnicas sobre los humedales del Complejo de El Bonillo, del costoso y exuberante Plan-ficción Especial del Alto Guadiana, 2008-2027 (de más de 5.000 millones de €); las cuales, contrariamente a lo que allí se dice, ni carecen, ni mucho menos, de valor ecológico, ni pueden ser destinadas de modo natural a retener agua, ya que su cometido ecológico fundamental es la de servir de centros de recarga hídrica al acuífero Campo de Montiel (cuya agua se transmite hidrodinámicamente posteriormente a otros hábitats).\nEn el triángulo comprendido entre El Bonillo, Viveros y El Ballestero se censa una población de 181 avutardas, en primavera y 130 individuos en verano. En las llanuras de El Bonillo, además, se puede ver sisón común, alcaraván común y una gran población de perdiz roja, además de otras aves esteparias.\nZEPA de Aves Esteparias de El Bonillo\nLa ZEPA (Zona de Especial Protección para Aves) de Esteparias de El Bonillo agrupa una amplia extensión de zonas cultivadas sobre todo con cereal de secano, leguminosas y girasol, intercaladas con zonas de eriales (denominadas en El Bonillo “liegos”) o pastizales mediterráneos xerófilos (de zonas secas), que han dado como resultado un hábitat privilegiado para una interesante comunidad de animales adaptados a la vida en las estepas, como es el caso de la Avutarda, o la Alondra ricotí, ambas especies amenazadas. Otras especies que se pueden encontrar en este espacio perteneciente a la Red Natura 2000 son el Alcaraván, el Cernícalo vulgar, el Sisón común, la Ganga ibérica, el Aguilucho cenizo, la Cogujada común o el Busardo ratonero.\nLas labores tradicionales de agricultura de secano y ganadería sobre todo de ovino han configurado a los largo del tiempo estos paisajes. No se entenderían por tanto sin esta labor de las gentes del campo. Sin embargo la reducción de la cabaña ganadera en los últimos años, y nuevas formas de entender la agricultura con parcelas de grandes extensiones de monocultivo, y la roturación de los eriales y pastizales (en estos momentos totalmente prohibidas) son las principales amenazas de este espacio protegido.\nEn la ZEPA de Esteparias de El Bonillo encontramos la mayor población de Avutardas de la provincia de Albacete, y una de las más grandes de Alondra ricotí.\nCerca se pueden visitar las Salinas de Pinilla (de origen romano), también como microrreserva creada por la JCCM (Junta de Comunidades de Castilla-La Mancha) por sus interesantes especies de flora, aunque no menos interesante es su avifauna acuática, destacando las avocetas comunes, cigüeñuelas comunes, ánades azulones, garzas reales e insectos que viven en el medio salino.\nMicroreserva Natural de las Salinas de Pinilla\nLas Salinas de Pinilla se encuentran situadas en los términos municipales de Alcaraz y El Bonillo, y a escasa distancia de Viveros, junto a la pedanía de Pinilla. La declaración como Microrreserva Natural tuvo lugar en el año 2005. Tienen una extensión de 50 Ha. y abarcan la propia zona de explotación de sal, el arroyo que pasa junto a ella y unas pequeñas lagunas que se forman más adelante.\nLa importancia de este lugar, y lo que hizo a la administración decantarse por protegerlo es la concentración de sal que hay en toda la zona y que ha hecho que allí se encuentren animales y plantas halófilos (que viven en zonas con concentraciones de sales superiores a lo normal). En efecto, la extracción de sal desde tiempos pasados hasta casi la actualidad han hecho que las sales se fuesen concentrando en los alrededores, llegando al río de Pinilla y a las lagunas que forma un poco más adelante. Igualmente con el paso del tiempo animales y plantas que sólo gustan de vivir en zonas con altas concentraciones salinas fueron colonizando la zona, hasta llegar a la actualidad, que encontramos diversidad de comunidades vegetales, desde praderas sumergidas de diversas plantas, briófitos, fanerógamas acuáticas, pastizales, albardinales y almarjales.\nEn el caso de los animales hablamos de pequeños insectos que prácticamente sólo se encuentran en contados enclaves acuáticos con altas concentraciones de sal. Además las lagunas son un importante lugar de concentración de aves acuáticas, y en los alrededores resulta sencillo observar aves tan emblemáticas como la avutarda.',
      'negative_14': 'Rejilla criptográfica\n\nUna rejilla, en criptografía, también llamada enrejado o celosía, no es más que un aparato que se emplea como ayuda en un cifrado, normalmente por transposición, de modo análogo al Disco de Alberti o las tablas de Vigenère para los métodos de sustitución. Está pensado para ser empleado con los métodos de papel y lápiz.\n\nEn la cultura popular\n\nEl método original de Cardano es empleado en la película Con Air, por el personaje Cyrus The Virus Grissom, interpretado por John Malkovich, para comunicarse desde la prisión, empleando una imagen de la Última Cena a la que se le habían quitado los ojos de los personajes para revelar el mensaje de una carta aparentemente inocente, de un abogado.\nEl segundo método, revelar un mensaje en unas letras aleatorias, fue empleado por el espía ruso, Valeri Petrofsky, interpretado por Pierce Brosnan, en la película de 1987 El cuarto protocolo.\n\nLas Rejillas como método de transposición\n\nLas rejillas pueden emplearse, igualmente, como métodos directos de transposición empleándolas como guía para realizar una transposición. Al parecer, esta transición se llevó a cabo en algún momento del siglo XVII. A este respecto las rejillas se dividen en dos grupos según su forma de creación, las ordinarias y las rotatorias. Las rejillas ordinarias se crean tal y como describió Cardano. Para las rejillas giratorias véase más abajo.\nUna posibilidad se ha sugerido para evitar a los comunicantes tener que mantener el secreto de sus rejillas (uno de los clásicos problemas de reparto de claves), emplear crucigramas, idealmente, los publicados en periódicos de uso común tanto para emisor como para receptor. De esa forma, la rejilla ya estaría disponible y sería totalmente inocente y justificable su posesión. Es importante destacar que los crucigramas de la tradición anglosajona (en lengua inglesa) presentan un mayor número de cuadros negros, y un menor número de palabras de dos letras que sus equivalentes de tradición continental (en francés, o español, por ejemplo).\nEn todo caso, tanto en uno como en otro caso, las rejillas se emplean para dotar de una cierta irregularidad a la transposición de un modo que sería difícil conseguir con una clave simplemente memorizada. A este respecto, la rejilla puede ser una herramienta muy útil transponiendo de muy diversas formas según se varíe el modo de introducir el texto en claro (de izquierda a derecha, en columnas, empezando por una casilla determinada, etcétera) y de leer el texto cifrado (donde se pueden hacer las mismas consideraciones). Otra posibilidad es la numeración previa, y desordenada, de las casillas de nuestra rejilla, escribiendo el mensaje en claro de acuerdo con este orden, se logra una transposición razonablemente compleja. No obstante, este sistema es propenso a los errores de transcripción.\nEl general italiano Luigi Sacco en su libro Manuel de cryptographie presenta lo que llama “rejilla indefinida”, una rejilla de forma rectangular con un número de filas fijo y un número de columnas arbitrario (o elegido en función de la longitud del mensaje). En cada una de las columnas, se reparten las celdas arbitrariamente entre llenas y vacías dentro del total de filas predeterminado. De esta forma se puede, igualmente, señalar una gran variedad de transposiciones distintas con la misma rejilla. Rejillas de este tipo fueron empleadas durante la Guerra Civil española entre 1936 y 1939.\nEsta flexibilidad de uso se señala, por ejemplo, en las cifras empleadas por algunos espías confederados durante la Guerra de Secesión, al emplear solamente fragmentos de una rejilla mayor (George T. Sinclair, relativo al asunto del buque Pampero),\u200b o por la rejilla de cifrado alemana Rasterschlüssel 44,\u200b empleada para el nivel táctico.\n\nLa Rejilla giratoria\n\nLas rejillas giratorias fueron descritas por el Barón Edouard Fleissner von Wostrowitz, antiguo coronel del ejército austrohúngaro, y por ese motivo también se las llama rejillas de Fleissner, aunque parece ser que ya estaban en uso anteriormente. Se trata de rejillas de forma cuadrada que tienen cuatro posiciones dependiendo de la parte que quede hacia arriba.\nPara construirlas, basta con dividir la rejilla en cuatro cuadrantes iguales y numerar cada uno de ellos con la especificidad de que cada cuarto estará girado 90º con respecto al precedente. Una vez hecho esto, bastará con perforar una vez (y solamente una) cada uno de los números.\u200b En caso de que la rejilla tenga un número impar de casillas por lado (como 5, 7, 9 ó superiores), cada uno de estos cuatro cuadrantes tendrá forma de paralelogramo y habrá que aclarar si la casilla central se deja sin perforar o, cuando tendría que ser rellenada.\nPara manejar las rejillas giratorias basta con escribir el mensaje en claro en los huecos perforados en las mismas e ir girando la rejilla conforme se iban terminando los espacios.\nDurante la I Guerra Mundial, en 1916, el ejército alemán empleó una serie de rejillas giratorias para sus comunicaciones. Estas rejillas recibían nombres distintos según el tamaño de las mismas, en las rejillas de orden impar, uno de los lados estaba marcado en color negro para indicar que era con ese con el que debía rellenarse la casilla central:\u200b \n 5x5 ANNA\n 6x6 BERTA\n 7x7 CLARA\n 8x8 DORA\n 9x9 EMIL\n 10x10 FRANZ\n\nEn la cultura popular\n\nEl uso más famoso de este método de cifrado aparece en la novela Matías Sandorf de Julio Verne, donde no sólo tiene una importancia crucial en la trama sino que se explica su funcionamiento.\u200b\n\nElaboración de las rejillas giratorias\n\nEn su libro, el coronel Fleissner da a conocer un método para la elaboración de rejillas cuadradas de orden impar, (con lados de 3, 5, 7 y sucesivos) dejando la casilla central sólida, sin agujero. Por su parte, en su Tratado de criptografía con especial aplicación al Ejército, J. G. Carmona\u200b, aparte de mencionar el anterior, indica un método para la elaboración de rejillas cuadradas de orden par (con lados de 2, 4, 6 y sucesivos). El método de Carmona, cómo él mismo indica, tiene la peculiaridad de que cada cuadrado de orden superior, se puede construir sobre el cuadrado de orden inferior. Indica también que, si se deja sin fijar al siguiente cada uno de los cuadrados de orden inferior, se puede, por rotación, aumentar el número de rejillas posibles a generar con la misma plantilla.\nOtro método alternativo, en las rejillas cuadradas de orden par, es la división del total de la plantilla en cuatro cuadrantes y numerar cada una de las casillas dentro de los mismos. La rotación de estos números y su sucesiva perforación, sin repetir nunca, permite elaborar la rejilla.\n\nSeguridad de los cifrados con rejilla\n\nLa seguridad de los cifrados con rejilla es la propia de los sistemas de cifrado por transposición aunque no es menos cierto que las rejillas, en cuanto tales, pueden violar los segundo y tercer principios de Kerckhoffs al ser recordatorios escritos tanto del algoritmo de cifrado como de la clave por cuanto que su descubrimiento revelaría completamente el contenido de los mensajes secretos. Siendo su naturaleza la propia de un sistema de transposición, pueden ser empleadas en conjunción con cifrados por sustitución, de hecho, el general Luigi Sacco recomendó emplear las rejillas junto con métodos de sustitución fraccionada, como las cifras bífida y trífida de Delastelle, para aumentar la seguridad tanto de unas como de otras.',
      'negative_15': 'Facundo Valverde García\n\nBiografía\n\nPasó su infancia entre Cartagena (Murcia) y la Sierra del Taibilla (Albacete) donde trabajaba su padre en la construcción de la canalización de aguas hasta Cartagena. Cursó los estudios de Bachillerato en el Colegio Hispania de Cartagena.\nEn 1953 se trasladó a Madrid para estudiar Medicina. Poco después de acabar la carrera en 1959, tomó la decisión de dedicarse a la investigación, en una época donde esta profesión era prácticamente desconocida, dedicándose al estudio de la estructura, desarrollo y función del cerebro.\nDefendió su tesis doctoral en 1962 y entre 1963 y 1965 estuvo becado por los National Institutes of Health (USA) en la Universidad de Harvard en Boston.\nA su regreso a España en 1965 continuó sus estudios en el Instituto Cajal del Consejo Superior de Investigaciones Científicas (CSIC) donde llegó a ser Profesor de Investigación. Con la financiación obtenida de varias Fundaciones  Juan March, Lepetit,  Eugenio Rodríguez Pascual,  Ramón Areces) y posteriormente gracias a la financiación de Proyectos de Investigación por la Comisión Asesora de Investigación Científica y Técnica, desarrolló su labor investigadora en Neurociencia durante más de cuarenta años junto a varios discípulos y colaboradores que se formaron o trabajaron junto a él, hasta su jubilación en 2003.\nDiscípulo del Profesor Fernando de Castro Rodríguez, sus trabajos de investigación se han basado fundamentalmente en el estudio del desarrollo y estructura del cerebro en varios mamíferos utilizando diversas técnicas histológicas.\nHa formado parte de varios comités científicos de evaluación así como de consejos editoriales en revistas especializadas. Autor de numerosas publicaciones en revistas internacionales, diversos libros y capítulos de libros colectivos, ha recibido varios premios por su labor investigadora entre los que cabe destacar el Premio Rey Jaime I de la Generalitat Valenciana en 1992.\n\nLabor investigadora\n\nDeprivación sensorial. Plasticidad neuronal.\nEntre 1966 y 1970, tomando como modelo experimental la corteza visual, sus estudios se centraron en la demostración de la variabilidad del número de espinas dendríticas (lugar donde se establecen contactos funcionales - sinapsis - sobre las dendritas en las células piramidales de la corteza visual) en ratones con deprivación de la visión por mantenimiento en oscuridad absoluta desde su nacimiento y por distintos periodos de tiempo. Aunque el ratón apenas depende de la visión para el desarrollo de sus funciones, la estructura de la corteza visual en este roedor mantiene el mismo patrón estructural que en el resto de los mamíferos.\nLa disminución del número de espinas dendríticas en ratones mantenidos en la oscuridad resultó ser altamente significativa en el primer mes de vida del animal, después de que estos abrieran los ojos (el ratón abre los ojos normalmente en torno al día 13-14). En comparación, los animales mantenidos en oscuridad desde su nacimiento por períodos prolongados de tiempo (hasta 6 meses), mostraban también una disminución del número de espinas, si bien este disminución no era tan acusada como en períodos juveniles. Según los datos obtenidos, se demostró que, pese a existir cierta tendencia a la recuperación del número de espinas después de vueltos a la normalidad, quedaba una población de neuronas en la que el número de espinas nunca llagaba a alcanzar cifras normales. La privación visual no afectaba a otras áreas corticales.\nEstos estudios demostraron por primera vez que la deprivación sensorial produce variaciones morfológicas en la estructura del cerebro (plasticidad neuronal), estando las espinas dendríticas probablemente implicadas en los procesos de memoria y aprendizaje. Con estas observaciones se obtuvo la conclusión de que la deprivación de la visión provoca una alteración o daño permanente en algunas neuronas de la corteza visual, daño que resultó ser más acusado en animales jóvenes al no recuperar el número normal de espinas dendríticas una vez vueltos a las condiciones normales. (Trabajos publicados 14-22).\nOrganización de la corteza cerebral.\nEn el decenio de 1970 a 1980 estudió la organización de la corteza visual primaria en primates (Área 17) describiendo numerosas variedades celulares y estableciendo las bases estructurales de la organización columnar de la corteza cerebral, cuya unidad es la columna cortical extendida en todo el espesor de la corteza cerebral. Esta unidad anatómica y funcional, de unas 400 micras de diámetro, cuyo esbozo estructural describió en 1971, contiene, además de las células piramidales, que representan el 80% de las neuronas de la corteza, un amplio espectro de variedades celulares que pueden caracterizarse, no solo por su morfología, sino también por la longitud y tipo de ramificación axonal y dendrítica que poseen (células piramidales de  axón recurrente, células estrelladas con espinas, células en ovillo, en cesto, de doble penacho, etc). Estos estudios probaron que existen variedades neuronales que, desde un punto de vista morfológico y probablemente funcional también, son distintas para cada especie, existiendo variedades celulares que no se encuentran en otras especies por lo que la descripción de un patrón estructural único no es aplicable a menos de recurrir a una simplificación y generalización extrema. (Trabajos publicados 23, 27-29, 35, 38, 40, 50, 51, 74 y 76).\nLas células en candelabro: una nueva variedad neuronal. \nLas células en candelabro corresponden a una variedad neuronal que, junto con su colaborador A. Fairén, describe por primera vez en la corteza visual del gato en 1980. Solo descritas anteriormente como células axo-axónicas en el cerebro de la rata, esta variedad neuronal tiene la particularidad de que sus terminaciones axonales hacen contacto sináptico exclusivamente sobre los segmentos iniciales del  axón de las células piramidales de la corteza cerebral donde probablemente ejerzan un poderoso efecto inhibidor (Trabajos publicados 30 y 31). En estudios posteriores realizados con algunos de sus colaboradores, demostró que esta variedad neuronal no era exclusiva de determinadas especies sino que pueden observarse en toda clase de mamíferos estudiados, desde insectívoros a primates, incluido el hombre (Trabajos publicados 32-35, 38, 40, 50 y 51).\nEl Sistema Olfativo.\nA partir de 1986 una serie de estudios centraron su interés en el Sistema olfativo como modelo experimental, dada la especial naturaleza de sus componentes entre los que cabe destacar la presencia de neuronas capaces de reproducirse durante toda la vida y la existencia de una variedad única de neuroglia que ha servido para estudios de regeneración nerviosa en pacientes con lesiones medulares (Trabajos publicados 62 y 70). Todos estos estudios dieron lugar a numerosas publicaciones sobre Anatomía comparada (Trabajos publicados 32, 33, 36-39, 44, 45, 48 y 51), migraciones celulares durante el desarrollo (Trabajos publicados 62-65 y 67) y otra serie de estudios referidos al bulbo, centros olfativos y factores de trascripción implicados en la regionalización del cerebro (Trabajos publicados 55, 68, 70 y 72).\n\nPremios Y Otras Distinciones\n\n- Premio Santiago Ramón y Cajal en Biología (CSIC), 1962\n- Research Fellow in Anatomy, Universidad de Harvard 1963-1965\n- Miembro, American Association of Anatomists (USA),desde 1964\n- Miembro, Cajal Club (USA), desde 1964\n- Jefe de la Sección de Neuroanatomía Comparada. Instituto Santiago Ramón y Cajal (CSIC), 1968-1984\n- Premio Santiago Ramón y Cajal en Biología (CSIC), 1970\n- Miembro, International Brain Research Organization (IBRO), desde 1970\n- Premio Francisco Franco de Ciencias (CSIC) 1971\n- Miembro, Society for Neuroscience (SFN), desde 1975\n- Miembro del Comité Editorial de la revista Synapse (Wiley, New York), 1975-1998\n- Miembro del Comité Editorial de la revista Brain, Behavior and Evolution (S.Karger, Basel), 1978-1990\n- Premio Rey Jaime I  \u200b  1992\n- Miembro del Alto Consejo Consultivo de la Generalitat Valenciana, 1992-2000\n- Neurona de Plata. Instituto Santiago Ramón y Cajal (CSIC), 2000\n- Profesor Vinculado ad honorem. Instituto Santiago Ramón y Cajal (CSIC), 2003-2005',
      'negative_16': 'Difusión simple\n\nSe denomina difusión simple al proceso por el cual se produce un flujo de moléculas a través de una membrana permeable sin que solo exista un aporte externo de energía molecular. Este proceso, que en última instancia es por una diferencia de concentración molecular entre los dos medios separados por la membrana, no requiere de un aporte de energía debido a que su principal fuerza impulsora es el aumento de la entropía total del sistema\nEn este proceso el desplazamiento de las moléculas se produce siguiendo el gradiente de concentración, las moléculas atraviesan la membrana desde el medio donde se encuentran en mayor concentración, hacia el medio donde se encuentran en menor concentración.\nEl proceso de difusión simple se encuentra descrito por las Leyes de Fick, las cuales relacionan la densidad del flujo de las moléculas con la diferencia de concentración entre los dos medios separados por la membrana, el coeficiente de difusión de las mismas y la permeabilidad de la membrana.\nEl proceso de difusión simple es de vital importancia para el transporte de moléculas pequeñas a través de las membranas celulares. Es el único mecanismo por el cual el oxígeno ingresa a las células que lo utilizan como aceptor final de electrones en la cadena respiratoria y uno de los principales mecanismos de regulación osmótica en las células.\n\nDifusión\n\nDifusión es el proceso irreversible por el cual un grupo de partículas se distribuye de manera uniforme en un medio ya sea vacío o formado por otro grupo de partículas. Este proceso es estadísticamente predecible en conjunto, aunque el movimiento de cada partícula aislada es totalmente aleatorio. Se encuentra impulsado por el movimiento térmico de las partículas que componen ese sistema y se produce siguiendo las líneas de mayor diferencia de concentración entre regiones, esto es, siguiendo los gradientes de concentración.\n\nEn las membranas celulares\n\nEn el caso de las células vivas, el proceso de difusión simple se establece a través de la membrana celular, por lo que de hecho existen tres procesos de difusión encadenados, una difusión que ocurre en el medio de mayor concentración, una difusión que ocurre en el medio de separación y una difusión que ocurre en el medio de menor concentración. Como el proceso limitante de la velocidad es la difusión a través del medio de separación, se puede simplificar un modelo donde el flujo de partículas depende de la diferencia de concentración entre ambos lados del medio de separación y del tipo de interacciones que presente la molécula que va a atravesar la membrana con ese medio. \nLas moléculas que pueden atravesar con facilidad las membranas celulares, debido a este fenómeno, son únicamente las de los gases (por ejemplo CO₂, O₂), las moléculas hidrofóbicas (por ejemplo benceno) y las moléculas polares pequeñas (por ejemplo H₂O y etanol), esto es así debido a que las moléculas hidrofóbicas y apolares son solubles en la región central apolar de la bicapa lipídica, y las moléculas polares pequeñas son lo suficientemente pequeñas como para que las interacciones desfavorables se vean compensadas por un aumento de la entropía del sistema. Por otra parte, las moléculas polares grandes tales como la glucosa, los aminoácidos y las moléculas cargadas o iones (Hx⁺, Na⁺, Cl⁺ y Ca²⁺) establecen interacciones demasiado fuertes con el medio acuoso fuera de la bicapa lipídica, por lo que les resulta muy desfavorable desde el punto de vista energético romper estas interacciones para atravesar la región central hidrofóbica. Como consecuencia las membranas biológicas son prácticamente impermeables a este tipo de moléculas, por lo que requieren de otros mecanismos de transporte.\n\nLeyes de Fick en la difusión simple\n\nPara el estudio del transporte a través de las membranas celulares por difusión simple, es necesario considerar las leyes que rigen los procesos de difusión: las Leyes de Fick. Cuando un sistema presenta una diferencia en el número de moléculas por unidad de volumen (concentración), por dentro y por fuera de un espacio delimitado por una membrana, se establece un gradiente de concentración que, expresado en forma diferencial sencilla, es proporcional a la diferencia en la concentración entre ambos medios (c) e inversamente proporcional al espesor de la membrana (x): \nEn caso de que la membrana sea permeable a las moléculas desigualmente distribuidas, se establece un flujo neto de partículas desde la zona de mayor concentración hacia la zona de menor concentración. La densidad de partículas en este flujo (J) depende del gradiente de concentración y de la facilidad con que las partículas atraviesan la membrana (D o coeficiente de difusión). El signo negativo indica la dirección del flujo (de mayor a menor concentración\nAl considerar una membrana de espesor no infinitesimal relativamente constante, en la cual se presenta una diferencia de concentración  también constante, la primera Ley de Fick se puede reescribir como: \nEn esta ecuación el coeficiente de permeabilidad de la membrana queda definido como: \nPor lo que la primera ley de Fick también puede escribirse cómo:  \nLa ecuación de continuidad que expresa la conservación del número de moléculas, obtenida a partir del análisis del flujo entrante y saliente de las moléculas a través de un área y de la rapidez de acumulación (aumento por unidad de tiempo del número de partículas unidad de volumen) es:\nReemplazando, se obtiene:',
      'negative_17': 'Guayabero\n\nForma de vida\n\nLos Guayaberos eran nómadas, pero el despojo de su territorio por la colonización, los obligó a sedentarizarse. Aún se movilizan en canoas por el río y en caminatas de caza y recolección por el bosque, pero la agricultura es fundamental para su subsistencia, al lado de la pesca y la artesanía.\nEn las huertas o chagras (lula, baká), el cultivo principal es la yuca amarga, o brava (baw, halw+ah, haltoet), de la que obtienen "casabe" (ben:tortilla) y "fariña" (maniku, béñel, beñilon: harina tostada). Cultivan también maíz (hes), batata (nat, d+ad), bore, ñame, aguacate, cacao, chontaduro, papaya, piña (duind), ají (nol), calabaza (yam), plátano, caña de azúcar, arroz, mango, algodón (papud), tabaco (jo) y achiote (hoes). El hombre es el encargado de tumbar y quemar para preparar el terreno y la mujer siembra, cuida y cosecha, (aunque hoy día esto último lo hacen juntos-hombre y mujer) \nCazan con arcos (fadoit y woijta) y flechas (buya) y jabalinas o lanzas (b+oin), dantas (mesa), venados (alái), chigüiros (humbóe), diferentes clases de monos, cachirres (makléh), armadillos (tuha), pecarís (chama), lapas (ap+), agutís, aves, iguanas (matiw), y tortugas (hachk). Pescan tradicionalmente con arco y flecha y arpones (b+oin) y barbasco y además, actualmente con anzuelos y redes. Recolectan gran número de frutos y semillas (bats) silvestres, "mojojoy" (larvas de coleópteros Rynchophorus spp. que proliferan en las palmas) y huevos de tortuga, iguana y aves. Crían gallinas y cerdos para la venta.\nLos hombres tejen instrumentos para procesar la yuca (wat: sebucán; hapaj: cernidor) y canastos para recibir la masa (japox), asarla (juit) y almacenar la harina (mapiri) o para otros usos. Las mujeres hilan fibra de tronco de palma y con ella fabrican hamacas (bu), mochilas y brazaletes; fabrican canastas de carga (joel); telas de corteza taja taja, del árbol f+tne; recipientes de totumo (haaft); y también ollas de barro (marma).\nPara poder subsistir, muchos guayabero trabajan temporalmente por un salario. El desplazamiento forzado, la reducción de su territorio y de la fauna y flora del bosque han causado un gran perjuicio a los Guayabero, por lo que hoy se ven afectados por la desnutrición, la tuberculosis y el incremento de las infecciones intestinales y respiratorias.\n\nMatrimonio\n\nEl matrimonio ocurre a temprana edad, desde los 12 años para las mujeres y los 14 para los hombres. Por solicitud del novio los padres conversan y arreglan la fiesta de bodas (aunque en sí no hay una ceremonia como lo hay entre los occidentales), que a veces ocurre cuando la pareja ya convive. El matrimonio preferencial es entre primos cruzados. La regla es la monogamia. Es posible el divorcio, especialmente cuando se arguye que el cónyuge es perezoso o mal trabajador o la infidelidad.\n\nCosmovisión\n\nConciben el universo constituido por diferentes niveles: en el superior o "cielo" están con los astros, seres que han desempeñado papeles especiales y espíritus de los antepasados buenos; en la tierra además de lo que vemos comúnmente, hay espíritus dép que influyen negativa o positivamente sobre la gente.\nPara los Guayabero, determinados héroes han desempeñado un papel fundamental. Kuwei fue el creador que formó la tierra, la primera mujer, Jumino, a diferentes gentes y a varias especies de animales. Huimit, el sol, era un jefe guayabero. Nejeim fue el héroe cultural que enseñó a los Guayaberos a conocer su medio y practicar diversas actividades de subsistencia. Con él y otros antepasados aun pueden comunicarse en las ceremonias en las que se consume la bebida del "yajé" (tuipaj). La corteza cruda del yajé se masca como estimulante; en tanto que el "yopo" (dop), es inhalado (tuw) por los hombres, para averiguar el futuro o qué están tramando otras personas.\nLos "payes" (pinhoin) pueden tratar con los dép y controlar las enfermedades, así como dirigir los rituales con el yajé y el uso del yopo. Son asistidos por cantores que desempeñan un papel imprescindible en su labor.',
      'negative_18': 'Choque hipovolémico\n\nCausas\n\nEl choque hipovolémico es consecuencia de pérdidas de líquidos internos o externos por la disminución de la masa de hematíes y de plasma sanguíneo por hemorragia o por la pérdida de volumen plasmático como consecuencia del secuestro de líquido en el espacio extravascular o de pérdidas digestivas, urinarias o pérdidas insensibles.\u200b\nLas pérdidas internas pueden deberse a una desviación al tercer espacio, escape de líquidos de los capilares del intestino hacia la luz intestinal, hemorragia interna y deterioro del retorno venoso por obstrucción de la vena cava. Dos causas comunes de la rápida pérdida de sangre interna son las lesiones de órganos sólidos y rotura de un aneurisma aórtico abdominal. Un choque hipovolémico significativo puede ser el resultado de pérdida de fluidos, diferentes a la sangre. Dos ejemplos son la gastroenteritis y las quemaduras extensas. \nLas pérdidas externas de líquidos se refieren al escape de líquidos, plasma o líquidos del cuerpo, por hemorragia debido a heridas externas. La cantidad de sangre circulante en el cuerpo puede disminuir cuando se pierde demasiada cantidad de otros líquidos corporales, como en las quemaduras, diarrea y vómitos.\u200b La pérdida aguda de sangre externa secundaria a trauma penetrante y trastornos de sangrado gastrointestinal graves son las dos causas más comunes de choque hemorrágico. El choque hemorrágico también puede resultar de gran pérdida interna súbita de sangre en las cavidades torácica y abdominal.\n\nChoque por traumatismos\n\nLos traumatismos también pueden ser causa de choque. Aunque muchas veces la pérdida de sangre es derivada de la hemorragia, también puede ocurrir sin pérdida de sangre. La contusión del cuerpo puede lesionar los capilares hasta el grado de permitir una pérdida excesiva de plasma hacia los tejidos promoviendo una disminución del volumen plasmático. este tipo de choque por traumatismo también puede incluir un cierto grado de choque neurogénico causado por el dolor, que es así mismo, un factor agravante de este tipo de choque al inhibir el centro vasomotor, con lo que se eleva la capacidad vascular y disminuye el retorno venoso.\n\nPatogenia\n\nEl cuerpo humano responde ante una hemorragia aguda con la activación de los principales sistemas fisiológicos: la hematológica, cardiovascular, renal, y los sistemas neuroendocrinos. Estos intrincados mecanismos son eficaces en el mantenimiento de la perfusión de órganos vitales ante una grave pérdida de sangre. Sin sangre y fluidos de reanimación y/o corrección de la patología subyacente que causa la hemorragia, disminuye la perfusión cardiaca y se instala sin demora una insuficiencia multi-orgánica.\n\nRespuesta hematológica\n\nLa respuesta del sistema hematológico ante una pérdida de sangre aguda y grave se basa en la activación de la cascada de coagulación y la vasoconstricción de vasos sanguíneos sangrantes, fundamentalmente por medio de la liberación local de tromboxano A2.\u200b Además, se activan las plaquetas, también bajo la dirección de la liberación local de tromboxano A2, y se forma un coágulo inmaduro en el sitio del sangrado. El vaso dañado expone el colágeno, que posteriormente causa la deposición de fibrina y la estabilización del coágulo. Son necesarias aproximadamente 24 horas para completar la fibrinización del coágulo.\n\nRespuesta cardiovascular\n\nInicialmente, el sistema cardiovascular responde ante un choque hipovolémico con el aumento de la frecuencia cardíaca, aumento de la contractilidad miocárdica, y la vasoconstricción de vasos sanguíneos periféricos. Esta respuesta se produce como consecuencia a un aumento en la liberación de noradrenalina y la disminución del tono vagal, regulada por los baroreceptores en el cayado aórtico, seno carotídeo, aurícula izquierda, y los vasos pulmonares. El sistema cardiovascular responde también con la redistribución de la sangre hacia el cerebro, corazón y los riñones y menos hacia la piel, músculo y tracto gastrointestinal.\n\nRespuesta renal\n\nEl sistema renal responde ante un choque hemorrágico con la estimulación de un aumento en la secreción de renina del aparato yuxtaglomerular. La renina convierte al angiotensinógeno en angiotensina I, que posteriormente es convertida a angiotensina II en los pulmones y el hígado.\u200b La angiotensina II tiene dos efectos principales que ayudarán a revertir el choque hemorrágico: vasoconstricción del músculo liso arteriolar, y la estimulación de la secreción de aldosterona por la corteza suprarrenal. La aldosterona es responsable de la reabsorción activa de sodio y consecuente conservación del agua.\u200b La activación del sistema renina-angiotensina es precoz y sensible a pérdidas hemáticas relativamente pequeñas.\u200b\n\nRespuesta neuro-endocrina\n\nEl sistema neuroendocrino responde ante el choque hemorrágico, provocando un aumento de circulante de hormona antidiurética (ADH).\u200b El ADH se libera de la glándula pituitaria posterior en respuesta a una disminución de la tensión arterial, detectados por barorreceptores, y una disminución en la concentración de sodio, detectados por osmorreceptores. La ADH conduce a un aumento de la reabsorción de agua y NaCl por el túbulo contorneado distal y los túbulos colectores.\n\nDiagnóstico\n\nDespués de la toma de la historia clínica y el examen físico del paciente, la conducta a seguir depende de la causa probable de la hipovolemia, así como la estabilidad de la condición del paciente.\n\nExámenes de laboratorio\n\nLos estudios iniciales de laboratorio suelen incluir el análisis del hemograma, los niveles de electrolitos, por ejemplo, sodio, potasio, cloro, bicarbonato, urea, creatinina y los niveles de glucosa, exámenes de coagulación como el tiempo de protrombina y el tiempo de tromboplastina parcial activado, gasometría, análisis de orina, especialmente en pacientes con traumatismos, y una prueba de embarazo en orina. Casi siempre se solicita un tipaje de la sangre y se prepara el banco de sangre para posibles transfusiones.\n\nEstudios de imagen\n\nLos pacientes con una marcada hipotensión arterial y/o en condiciones inestables son sometidos a medidas adecuadas de reanimación. Este tratamiento tiene prioridad sobre los estudios de imágenes y pueden incluir intervenciones quirúrgicas inmediatas.\nEn el paciente con trauma y signos y síntomas de hipovolemia se enfoca hacia la búsqueda de la fuente de la pérdida de sangre. El paciente atraumático con choque hipovolémico requiere un examen ecográfico en la sala de emergencia si se sospecha un aneurisma aórtico abdominal. Otros exámenes radiológicos útiles ante la sospecha de un aneurisma incluyen la ecocardiografía transesofágica, la aortografía, o la TAC de tórax. Si se sospecha una hemorragia gastrointestinal, los especialistas colocan una sonda nasogástrica debe ser colocado para realizar un lavado gástrico. Se solicita una radiografía de tórax en posición vertical si una úlcera perforada o el síndrome de Boerhaave resulta ser una posibilidad. La endoscopia se puede realizar, por lo general después de que el paciente ha sido hospitalizado, para definir con mayor precisión el origen del sangrado.\nSe indica una prueba de embarazo en todas las pacientes del sexo femenino en edad fértil. Si el paciente está embarazada y en estado de choque, se realiza una ecografía pélvica sin demora y puede ser llevada a una operación exploratoria. El choque hipovolémico secundario a un embarazo ectópico es común, incluso se han reportado embarazos ectópicos en pacientes con un test negativo de embarazo, aunque es un hallazgo muy infrecuente. Las radiografías simples se emplean cuando se sospechan fracturas óseas.\n\nTratamiento\n\nAunque el organismo puede compensar la pérdida de tensión por medio de reflejos autónomos, en ocasiones la pérdida de líquidos es tan extensa que es necesario aplicar un tratamiento para corregir la situación. El tratamiento médico inicial para el choque hipovolémico debe tener como finalidad el arreglo de tres áreas principales: maximizar el suministro de oxígeno—asegurando una adecuada ventilación, aumentando la saturación de oxígeno de la sangre, y restaurando el flujo sanguíneo; el control de la pérdida de sangre; y la restitución con líquidos.\n\nFármacos en el choque hipovolémico\n\nLa hipovolemia puede ser causa de varios equilibrios acidobásicos. La persona puede tener al principio una alcalosis respiratoria que podrá progresar en una acidosis metabólica. En estos casos se indica el uso de bicarbonato de sodio.\nPueden administrarse fármacos inotrópicos como la dopamina, dobutamina, epinefrina y norepinefrina a dosis bajas para mejorar el gasto cardíaco y la contractilidad del miocardio en pacientes con problemas de función cardiaca.\u200b Los vasodilatadores como la nitroglicerina dilatan las arterias coronarias para incrementar el aporte de oxígeno y reducir la poscarga. Aún existe controversia sobre el uso de los vasodilatadores y vasopresores.\u200b\nLa somatostatina es un polipéptido natural aislado del páncreas, el hipotálamo y las células epiteliales del estómago. La somatostatina disminuye el flujo sanguíneo a la red porta a causa de la vasoconstricción. Tiene efectos similares como la vasopresina, pero no causa vasoconstricción coronaria. Es rápidamente retirada de la circulación, con una vida media inicial de 1-3 minutos. En pacientes adultos se indica un bolo de 250\xa0μg intravenoso, seguido de 250-500\xa0μg/h en infusión continua por 2-5 días en caso de que sea efectiva.\u200b\n\nSupervisión hemodinámica\n\nLa hemodinámica es el análisis del flujo de sangre y de los factores que puede influenciarla. El estudio de la hemodinámica incluye el corazón y el sistema circulatorio, y los pulmones se incluyen a menudo también, pues la enfermedad que involucre en parte importante a los pulmones pueden inhibir la oxigenación de la sangre. Usar medidas tales como presión arterial ayudan a que el médico pueda recopilar la información sobre el sistema circulatorio de un paciente para determinar el grado de gravedad de una manera objetiva y esencial.\nPorque el sistema cardiovascular es tan crítico a la salud general, los perfiles hemodinámicos se hacen a menudo en situaciones donde la enfermedad del paciente ponga en tal riesgo su vida que al determinar dichos parámetros se haga una evaluación rápida y se ahorre tiempo en la atención primaria para mejorar su pronostico. Los elementos más utilizados para valorar a un paciente son los invasivos (colocación de una línea arterial, catéter de Swan-Ganz, catéter central, presión intra-abdominal, presión intracraneal) y los no invasivos (presión arterial, temperatura, frecuencia cardiaca, frecuencia respiratoria y más recientemente la escala análoga del dolor). Todos ellos aportan cifras que ayudan en el tratamiento así como el la toma de laboratoriales en sangre, o líquido específico.',
      'negative_19': 'Andrew Linzey\n\nAndrew Linzey (nacido el 2 de febrero de 1952, Reino Unido) es un teólogo, sacerdote anglicano y escritor. Es una importante figura en la reflexión teológica sobre el valor y el cuidado de los animales, así como dentro del movimiento de cristianos vegetarianos. Trabaja como docente e investigador en la Facultad de Teología de la Universidad de Oxford.\nEl profesor Linzey fundó y dirige el Oxford Centre for Animal Ethics, institución académica independiente abierta en noviembre de 2006 para promover la investigación sobre ética de los animales.\u200b\n\nObra\n\nEs autor de numerosos libros sobre los derechos de los animales y su relación con la teología cristiana: Animal Rights: A Christian Perspective (1976), Christianity and the Rights of Animals (1987), Animal Theology (1994), and Why Animal Suffering Matters: Philosophy, Theology, and Practical Ethics (2009). Asimismo, es editor de la revista académica, Journal of Animal Ethic, publicada conjuntamente por el Oxford Centre y por la Universidad de Illinois.\u200b Edita, con su compañera Priscilla Cohn, unas series editoriales sobre Ética animal en Palgrave Macmillan.\nHa escrito más de 180 artículos y 20 libros sobre teología y ética. Ha ejercido su docencia tanto en Europa como en Estados Unidos. Su obra Animal Theology ha sido traducida al italiano, español (Los animales en la Teología, Herder, 1995), japonés y francés.\n\nPensamiento\n\nLinzey ha dicho: “Los animales son criaturas de Dios; no son propiedad ni recursos de los seres humanos, ni están para la utilidad o comodidad de éstos, más bien son seres preciosos a los ojos de Dios... Los cristianos, cuyos ojos están fijados en el horror de la crucifixión, se sitúan en una posición especial para entender el horror del sufrimiento inocente. La cruz de Cristo es la absoluta identificación de Dios con el débil y el vulnerable, pero sobre todo con el sufrimiento desprotegido, indefenso e inocente”.\u200b\nTambién ha afirmado que “Los cristianos no están lejos de pensar que el gran mundo fue hecho para nosotros, con el resultado final de que los animales son vistos dentro de una perspectiva instrumental como objetos, máquinas, herramientas y productos, en vez de verlos como criaturas compañeras”.\u200b Su reivindicación es “ver a los abusadores de los animales puestos en un registro y que se prohíba retener a un animal o trabajar con ellos”.\u200b\n\nDel paradigma jerárquico en la creación a la fraternidad cósmica\n\nEl profesor Linzey propone pasar de un orden jerárquico entre las distintas criaturas ante Dios (que llevaría al antropocentrismo) a un "paradigma de la generosidad", donde la misión especial del ser humano es vivir ante los demás seres con las actitudes del Dios que crea, reconcilia y redime. Si el ser humano tiene un lugar especial es el de servir a las demás criaturas siguiendo a Cristo, el servidor de todos. Según Linzey, el ser humano no puede poseer a los animales, porque Dios es el único dueño de la creación. Al mismo tiempo que critica la praxis cristiana occidental en relación al trato humano con la Tierra, también considera peligrosas ciertas éticas contemporáneas animalistas, como la de Peter Singer por su planteamiento utilitarista, aunque a veces llega a las mismas conclusiones que el filósofo australiano.\u200b\n\nDefensa de un vegetarianismo cristiano\n\nPara Linzey también los cristianos están llamados a asumir una dieta vegetariana como paso previo a la realización de los "cielos nuevos y tierra nueva" (Is 66,22) donde, según el profeta Isaías, no habrá más violencia entre los seres humanos y los animales, o entre unos animales y otros (11,6-8), y así se dará un "retorno" al plan original querido por Dios antes del diluvio (Génesis 1,29-30). Los cristianos están llamados - argumenta Linzey - a practicar el vegetarianismo cuanto más les sea posible en estos tiempos escatológicos, ya que el rechazo al consumo de carne es un aspecto integral del reino de paz previsto por las Sagradas Escrituras.\u200b\n\nReconocimientos\n\nEn 1990 recibió la Peaceable Kingdom Medal por su excepcional trabajo en el campo de la teología y los animales.\u200b En 2001 fue galardonado como Doctor of Divinity (D.D.) por Georfe Carey, Arzobispo de Canterbury, en reconocimiento de su “único, masivo y pionero trabajo en el área de la teología de la creación con una particular referencia a los derechos y bienestar de las criaturas sentientes de Dios”. Este es el premio más alto que el Arzobispo de Canterbury puede otorgar a un teólogo y la primera vez que se premia un trabajo que tiene por tema a los animales. En 2006, reconociendo el papel de Andrew Linzey en la creación del Oxford Centre for Animal Ethics, recibió el título honorífico de ‘Profesor de Ética Animal Henry Bergh’ en la Graduate Theological Foundation de Estados Unidos, siendo la primera vez que se concedía este título.',
      'negative_20': 'Chrysler 300M\n\nAntecedentes\n\nEL 300M al igual que sus hermanos el Chrysler Concorde, Chrysler LHS y el Dodge Intrepid, es la evolución de la primera generación de los autos LH (llamados así por su plataforma) que se vendieron exitosamente de 1993 a 1997. Aunque portan la misma plataforma fueron mejorados en todos los aspectos. El diseño fue liderado por Tom Gale.\n\nDesarrollo\n\nEL 300M es el relevo del Eagle Vision, pero de último momento se cambió el nombre debido a dos temas: el cierre de la marca Eagle (una de las decisiones de DaimlerChrysler) y revivir la famosa y tradicional saga americana de los "300".\nExisten fotos donde se muestran los primeros modelos de pre producción del 300M todavía con emblemas de Eagle, sin embargo esta decisión de último momento fue buena, pues el nombre fue la cereza en el pastel que el público americano deseaba saborear, ya que el último 300 había sido el 300K en el 64 y el 300L (una edición limitada basándose en un Chrysler Cordoba).\nLa idea era crear en esta evolución de los LH, una versión larga y una corta. La larga sería el Chrysler Concorde y el Chrysler LHS que al final terminarían siendo el mismo auto, y la corta sería el 300M; La versión larga apostaba al confort, a un tremendo espacio en cajuela y un grandioso espacio en plazas traseras, mientras que la corta le apostaba al manejo deportivo y una imagen más amigable para el comprador europeo (en Europa, los cajones de estacionamiento son de 5 metros, mientras que en USA son más largos).\n\nRivales\n\nEl 300M fue posicionado para competir con autos mucho más costosos. Sus rivales Europeos fueron el Audi A6, BMW Serie 5, Mercedes Clase E, por parte de Asia sus rivales fueron el Lexus GS 300, el Nissan Maxima, los Infinity Q45, J30 e I30, y el Mazda Millenia, y por parte de Estados Unidos, sus rivales fueron el Buick Park Avenue, el Oldsmobile LSS, y de manera no tan directa, el Toyota Avalon, Lincoln Continental, Cadillac STS y Oldsmobile Aurora\n\nLanzamiento\n\nEl lanzamiento del 300M generó polémica debido a que no superaba la mítica cifra de 300 caballos de fuerza, ni tampoco tenía un motor de 8 cilindros, situaciones que eran prácticamente requisitos en toda la dinastía 300 desde la década de los 50\'s. Adicional a esto, la dinastía 300 siempre fue de edición limitada y nunca un auto de producción en masa. Con todo y eso, los tiempos de 0 a 100 km/h eran de 7.5 segundos, que son mejores tiempos que la mayoría de los originales 300 de antaño, a pesar de sus aterrorizantes motores Hemi.\n\nGeneralidades\n\nEL 300M no fue posicionado para competir contra Ford, Toyota o GM, sino para ponerse frente a frente con Audi, BMW y ahora su primo Mercedes. En Estados Unidos, se esperaba que el LHS se vendiera mejor que el 300M, pero fue todo lo contrario, pues el revivir el nombre “300” ayudó bastante en la publicidad del modelo. Además, el 300M con sus adecuaciones deportivas, impresionó a todos los “reviewers” que lo probaron, mientras que el LHS únicamente dejó satisfechos a los clientes, y hasta ahí.\nAún con su preparación para el mercado europeo, el 300M reprobó el “Eurotest” en algunos aspectos como por ejemplo: No tenía versión turbo, no tenía opción Diesel, no tenía caja de 5 velocidades, etc. sin embargo los críticos europeos lo recibieron relativamente bien.\nSólo hubo dos motores disponibles: El 2.7 y el 3.5 V6 con sus transmisiones Autostick de 4 velocidades.\n\nCambios año tras año\n\n1998: Versión de lanzamiento.\n1999: Sin cambios\n2000: Se añade un seguro trabapalanca para evitar cambiar de Parking sin pisar el freno. Se añade el cambiador de 4 CD’s en el equipo de Audio con equipos Infinity series II, botonería cromada en los paneles de puertas, posavasos al centro, suspensión trasera mejorada, tapón de combustible distinto, se añaden las luces automáticas por sensor de obscuridad.\n2001: Luces de freno de nuevo diseño, airbags laterales, EVIC de nueva generación, sin embargo por recorte de costos se retiran otras cosas como la botonería cromada, los tweeters se les quita la etiqueta “Infinity”, las cabeceras inclinables, las luces de cortesía de las puertas traseras y de peor calidad en las delanteras.\n2002: Se añade el sistema de Mercedes Benz EBD al ABS que ya traía de serie.\n2003: Cambiador de 6 CD’s que reemplaza al de 4, controles de audio al volante, estéreo opcional para leer DVD.\n2004: Versión de salida.\n\n300M Special\n\nA mediados de 2002 surge una versión llamada “Special” con 255 caballos y al normal le bajan la potencia a 250 (tema de marketing para separar más a las dos versiones), equipado con luces HID y unas molduras interiores imitación fibra de carbono que sustituyen a las tradicionales de madera, frenos mejorados y ruedas de 18”. Así mismo tiene doble escape con puntas cromadas y un kit aerodinámico exterior discreto de faldones y estribos.\n\nCese de producción\n\nEl último modelo del 300M fue el 2004; Todos los 300M se fabricaron en Brampton, la planta de Chrysler Ubicada en Ontario, Canadá. El relevo, un mucho más exitoso Chrysler 300C estaba listo para ocupar ahora el piso de ventas en las agencias, despidiendo al 300M quien ocupara los más preciados escaparates durante 7 años.'
    }
    ```
* Collection strategy: Reading the MLDR jsonl files in [Shitao/bge-m3-data](https://huggingface.co/datasets/Shitao/bge-m3-data), using all positives and the 20 negatives.
* Deduplified: No

### `...-triplet-all` subset

* Columns: "anchor", "positive", "negative"
* Column types: `str`, `str`, `str`
* Examples:
    ```python
    {
      'anchor': '¿Cuál es el efecto de la dilución crema simple en los pelajes básicos de los caballos?',
      'positive': 'Gen crema\n\nPelajes resultantes\n\nTodos los caballos tienen dos copias del gen MATP: una de parte de la yegua y la otra de parte del Estal.\nLos pelajes básicos no tienen ningún alelo crema. Los pelajes dluïts crema simples se producen cuando se añade un alelo crema a pelajes básicos.\nEl negro se transforma en negro-ahumado (poco diferente del negro), el moreno pasa a pardo-ahumado (muy parecido al pardo pero con zonas amarillentas en lugar de rojas), el castaño se convierte bayo-crema (generalmente sin raya dorsal) y el alazán se convierte en palomino.\n\u200b\nLa dilución crema simple implica que los pelos rojos pasan a amarillentos o dorados, las crines rojas convierten blancas. Los pelos negros no cambian (o cambian muy poco) de color, ni tampoco las crines negras. En los simples diluidos crema el color de los ojos suele ser relativamente claro, de tonalidad avellana. Los doblemente diluidos crema, formados por dos alelos crema sobre los pelajes básicos, tienen un pelaje blanco roto sobre una piel ligeramente pigmentada. Y suelen tener ojos azules.\u200b Los caballos con 2 copias del. Alelo crema también exhiben rasgos específicos: pelajes de color blanco roto, ojos azules pálidos, y piel muy poco pigmentada. Estos caballos se llaman normalmente crema, perla, negro-crema y pardo-crema.\n\nCrema diluido crema heterocigótico (crema diluido crema simple)\n\nLos pelajes crema diluido simple (con un alelo crema único) mantienen una piel pigmentada y los ojos castaños. A veces los pollinos nacen con una piel más clara que se oscurece con los años. También hay casos de ojos más claros con la tonalidad de la ámbar. El observador poco avezado puede confundir algún diluido crema simple (por ejemplo, el bayo) con un pelaje diluido champagne (gen champagne. Los pollinos champagne nacen con una piel rosada-calabaza que se oscurece y se vuelve pecosa, especialmente en el hocico, alrededor de los ojos y en la zona de los genitales.\nEl pelaje palomino de color ocre con crines blancas resulta de la acción de un alelo crema sobre un pelaje alazán (rojo). La variante clásica con pelos del cuerpo dorados y cola y crin blancas es una de las más vistosas.\u200b Menos frecuentes son las variedades oscuras, a veces producidas por la acción combinada del al. Alelo crema y del patrón modificador "Sooty". También hay variantes muy pálidas, casi blancas, que se confunden con los pelajes crema. Los ojos y la piel sin embargo mantienen una tonalidad oscura.\nEl pelaje bayo con crines negras o isabello. Es el diluido crema simple del castaño. El alelo crema hace que todos los pelos que en el castaño serían rojos sean dorados o amarillentos en el bayo-crema. Los pelos y las crines negras no varían de color.\nLos caballos negro-ahumados, dilución simple de los negros, son muy difíciles de detectar a simple vista. Su aspecto exterior es prácticamente igual que el de los negros (La dilución crema no afecta a los pelos y crines negras en forma simple). La única manera segura es el análisis genético.\nEl pelaje pardo-ahumado Es el diluido crema simple del pardo. Se parece mucho al pardo con zonas amarillentas en el hocico y brazada y, a veces, los flancos. La dilución crema simple hace que las zonas rojas del pardo pasen a amarillas en el moreno-ahumado.\n\nRazas de caballos con gen crema\n\nEl gen crema se encuentra en muchas razas: American Quarter Horse, Morgan, Morabit, Tennessee Walker, Misuri Fox Trotterinant de Tennessee, Miniature horse, Akhal-Teke, Connemara, Poni Gales, Pura Sangre Inglés, PRE, PSL,...\nEn cambio, no hay gen crema en los caballos árabes actuales. Hay referencias antiguas que hablan de caballos famosos diluidos crema.\n\nDiluciones combinadas\n\nDebido a que los genes de las diversas diluciones son diferentes, un mismo caballo puede ser portador de dos o más diluciones. En cada caso las diluciones combinadas pueden producir pelajes difíciles de distinguir a simple vista y que exigen pruebas genéticas para determinar con seguridad.\n\nAspectos genéticos\n\nEl locus crema se sitúa en el exón 2 del gen MATP, un polimorfismo nucleótido simple resulta en el canje del ácido aspàrgic y el aspargina. (N153D).\u200b La prueba genética que ofrecen algunos laboratorios detecta esta mutación.\nLos genes "overo" ("frame overo" según la American Paint Horse Association) y "sabino" provocan manchas blancas interrumpiendo o limitando la migración de melanocitos desde la cresta neural, mientras que la mutación crema afecta a la naturaleza de los pigmentos producidos por los melanocitos. La dilución crema es un caso de hipomelanisme. La piel, los pelos y los ojos de los caballos diluidos crema conservan un cierto grado de pigmentación.\nAntes del mapeo del gen de crema, este locus se titulaba C para indicar "color". Hay dos alelos en la serie: el recesivo C, y el dominante C Cr. (Nota: En exposiciones simplificadas la notación es Cr para una copia crema y Cr/Cr para dos copias crema. Para evitar el uso de super-índice).\nLa dilución crema fue investigada formalmente por Adalsteinsson en 1974, con la conclusión de que la herencia de los pelajes palomino y bayo-crema seguía en los caballos islandeses seguía un modelo semi-dominante o dominante incompleto. Adalsteinsson observó, también, que en los diluidos heterocigóticos sólo se diluía la feomelanina.\u200b',
      'negative': 'Tuneladora\n\nUna tuneladora, T.B.M. (del inglés Tunnel Boring Machine) o minador a sección completa es una máquina capaz de excavar túneles a sección completa, a la vez que colabora en la colocación de la entibación para la sustentación del túnel si ésta es necesaria, ya sea de forma provisional o definitiva. \nLa excavación se realiza normalmente mediante una cabeza giratoria equipada con elementos de corte y accionada por motores hidráulicos (alimentados a su vez por motores eléctricos, dado que la alimentación general de la máquina se realiza con energía eléctrica), aun cuando también existen tuneladoras menos mecanizadas sin cabeza giratoria. El empuje necesario para adelantar se consigue mediante un sistema de gatos perimetrales que se apoyan en el último anillo de sostenimiento colocado o en zapatas móviles (denominadas grippers), accionados también por gatos que las empujan contra la pared del túnel, de forma que se consigue un punto fijo desde donde empujan. \nDetrás de los equipos de excavación y avance se sitúa el denominado "equipo de rezaga" de la tuneladora (o en denominación inglesa back up), constituido por una serie de plataformas arrastradas por la propia máquina y que, a menudo, ruedan sobre rieles que la misma tuneladora coloca, donde se alojan todos los equipos transformadores, de ventilación, depósitos de mortero y el sistema de evacuación del material excavado. \nLos rendimientos conseguidos con tuneladoras de cabeza giratoria son elevadísimos si se comparan con otros métodos de excavación de túneles, pero su uso no es rentable hasta una longitud mínima de túnel a excavar: hace falta amortizar el precio de la máquina y calcular el tiempo que se tarda en diseñarla, fabricarla, transportarla y montarla (que puede llegar a los dos años). Además, los túneles a excavar con tuneladora tienen que tener radios de curvatura elevados porque las máquinas no pueden hacer curvas cerradas, y la sección tiene que ser circular en túneles excavados con cabeza giratoria.\n\nTipos de tuneladoras\n\nSe distinguen dos grandes grupos: los topos y los escudos, aun cuando también existen tuneladoras mixtas como las que excavan actualmente la línea 9 del metro de Barcelona.\n\nTopos\n\nLos topos son tuneladoras diseñadas para excavar rocas duras o medianas, sin demasiadas necesidades de sostenimiento. Su diferencia fundamental con los escudos es que no están dotados de un cilindro de acero tras la rueda de corte que realiza la función de entibación provisional.\nLa fuerza de empuje se transmite a la cabeza de corte mediante cilindros (cilindros de empuje). La reacción producida se transmite al hastial del túnel mediante los grippers (fuerza de anclaje). Los grippers también compensan el par producido por la cabeza de corte, que se transmite a éstos a través de la viga principal.\nCuando se ha terminado un ciclo de avance, se necesita reposicionar las zapatas de agarre (grippers), para la cual se apoya la viga principal en el apoyo trasero. Una vez anclados los grippers en su nuevo emplazamiento, se libera el apoyo trasero y se inicia un nuevo ciclo de avance.\n\nDoble Escudo\n\nOtra modalidad de tuneladora es la denominada Doble Escudo, capaz de trabajar como topo o como escudo, en función de la calidad del macizo rocoso, siendo la mejor solución para macizos con tramos de tipología variable suelo-roca. En este tipo de tuneladoras el escudo está dividido en dos partes, la delantera en la que se encuentra la cabeza de corte, y la zona trasera en la que se realiza el montaje del anillo de dovelas.\nEl movimiento de estas dos partes del escudo es independiente, situándose los "grippers" en un hueco abierto entre ambas, por lo que la cabeza puede excavar mientras que en la cola del escudo se van montando los anillos de dovelas. De esta manera los rendimientos alcanzados con este sistema son mucho mayores que con un escudo simple. Este sistema se aplica en aquellos terrenos capaces de resistir la presión que transmiten los “grippers”. Al mismo tiempo que los cilindros de empuje principal impulsan hacia delante el escudo de cabeza y la rueda de corte realiza la excavación, en el escudo trasero se procede al montaje de un nuevo anillo de dovelas de sostenimiento al abrigo del mismo. \nCuando el terreno es más débil y no es capaz de resistir la presión de los “grippers”, la tuneladora funciona como escudo simple, cerrándose el hueco de los "grippers", y apoyándose la tuneladora, mediante unos cilindros auxiliares, en el último anillo colocado, para así obtener la reacción necesaria para el empuje de la cabeza de corte (es decir, como trabaja un escudo normal). Por ello, trabajando en modo escudo, no es posible simultanear la excavación con el montaje del anillo de dovelas.'
    }
    ```
* Collection strategy: Reading the MLDR jsonl files in [Shitao/bge-m3-data](https://huggingface.co/datasets/Shitao/bge-m3-data) and taking each negative, but making a separate sample with each of the negatives.
* Deduplified: No