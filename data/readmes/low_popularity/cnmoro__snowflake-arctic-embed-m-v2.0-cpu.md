---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
- arctic
- snowflake-arctic-embed
- transformers.js
license: apache-2.0
language:
- af
- ar
- az
- be
- bg
- bn
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- ht
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ky
- lo
- lt
- lv
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- pa
- pl
- pt
- qu
- ro
- ru
- si
- sk
- sl
- so
- sq
- sr
- sv
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- vi
- yo
- zh
model-index:
- name: snowflake-arctic-embed-m-v2.0
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 66.6867
    - type: f1
      value: 55.0373
    - type: f1_weighted
      value: 73.07430000000001
    - type: ap
      value: 18.077399999999997
    - type: ap_weighted
      value: 18.077399999999997
    - type: main_score
      value: 66.6867
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 66.194
    - type: f1
      value: 60.854299999999995
    - type: f1_weighted
      value: 69.57339999999999
    - type: ap
      value: 30.279099999999996
    - type: ap_weighted
      value: 30.279099999999996
    - type: main_score
      value: 66.194
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 70.3589
    - type: f1
      value: 70.0409
    - type: f1_weighted
      value: 70.0409
    - type: ap
      value: 64.81949999999999
    - type: ap_weighted
      value: 64.81949999999999
    - type: main_score
      value: 70.3589
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 33.766
    - type: f1
      value: 33.3656
    - type: f1_weighted
      value: 33.3656
    - type: main_score
      value: 33.766
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: ndcg_at_1
      value: 33.144
    - type: ndcg_at_3
      value: 47.909
    - type: ndcg_at_5
      value: 52.932
    - type: ndcg_at_10
      value: 58.011
    - type: ndcg_at_20
      value: 60.168
    - type: ndcg_at_100
      value: 60.928000000000004
    - type: ndcg_at_1000
      value: 61.046
    - type: map_at_1
      value: 33.144
    - type: map_at_3
      value: 44.156
    - type: map_at_5
      value: 46.951
    - type: map_at_10
      value: 49.071999999999996
    - type: map_at_20
      value: 49.692
    - type: map_at_100
      value: 49.809
    - type: map_at_1000
      value: 49.815
    - type: recall_at_1
      value: 33.144
    - type: recall_at_3
      value: 58.819
    - type: recall_at_5
      value: 70.982
    - type: recall_at_10
      value: 86.558
    - type: recall_at_20
      value: 94.879
    - type: recall_at_100
      value: 98.791
    - type: recall_at_1000
      value: 99.644
    - type: precision_at_1
      value: 33.144
    - type: precision_at_3
      value: 19.606
    - type: precision_at_5
      value: 14.196
    - type: precision_at_10
      value: 8.656
    - type: precision_at_20
      value: 4.744000000000001
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 33.4993
    - type: mrr_at_3
      value: 44.393100000000004
    - type: mrr_at_5
      value: 47.131299999999996
    - type: mrr_at_10
      value: 49.264599999999994
    - type: mrr_at_20
      value: 49.8707
    - type: mrr_at_100
      value: 49.987700000000004
    - type: mrr_at_1000
      value: 49.993700000000004
    - type: nauc_ndcg_at_1_max
      value: -10.8287
    - type: nauc_ndcg_at_1_std
      value: -17.1177
    - type: nauc_ndcg_at_1_diff1
      value: 14.4508
    - type: nauc_ndcg_at_3_max
      value: -7.7004
    - type: nauc_ndcg_at_3_std
      value: -16.6705
    - type: nauc_ndcg_at_3_diff1
      value: 10.0448
    - type: nauc_ndcg_at_5_max
      value: -7.0436
    - type: nauc_ndcg_at_5_std
      value: -15.8744
    - type: nauc_ndcg_at_5_diff1
      value: 9.1132
    - type: nauc_ndcg_at_10_max
      value: -7.4729
    - type: nauc_ndcg_at_10_std
      value: -14.9349
    - type: nauc_ndcg_at_10_diff1
      value: 8.527700000000001
    - type: nauc_ndcg_at_20_max
      value: -6.997000000000001
    - type: nauc_ndcg_at_20_std
      value: -14.688399999999998
    - type: nauc_ndcg_at_20_diff1
      value: 9.7605
    - type: nauc_ndcg_at_100_max
      value: -7.5599
    - type: nauc_ndcg_at_100_std
      value: -15.0565
    - type: nauc_ndcg_at_100_diff1
      value: 10.2688
    - type: nauc_ndcg_at_1000_max
      value: -7.675800000000001
    - type: nauc_ndcg_at_1000_std
      value: -15.223500000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 10.32
    - type: nauc_map_at_1_max
      value: -10.8287
    - type: nauc_map_at_1_std
      value: -17.1177
    - type: nauc_map_at_1_diff1
      value: 14.4508
    - type: nauc_map_at_3_max
      value: -8.5473
    - type: nauc_map_at_3_std
      value: -16.6674
    - type: nauc_map_at_3_diff1
      value: 11.1004
    - type: nauc_map_at_5_max
      value: -8.1927
    - type: nauc_map_at_5_std
      value: -16.2275
    - type: nauc_map_at_5_diff1
      value: 10.678600000000001
    - type: nauc_map_at_10_max
      value: -8.3855
    - type: nauc_map_at_10_std
      value: -15.8309
    - type: nauc_map_at_10_diff1
      value: 10.5414
    - type: nauc_map_at_20_max
      value: -8.277700000000001
    - type: nauc_map_at_20_std
      value: -15.824
    - type: nauc_map_at_20_diff1
      value: 10.8494
    - type: nauc_map_at_100_max
      value: -8.3178
    - type: nauc_map_at_100_std
      value: -15.848300000000002
    - type: nauc_map_at_100_diff1
      value: 10.9384
    - type: nauc_map_at_1000_max
      value: -8.319799999999999
    - type: nauc_map_at_1000_std
      value: -15.8522
    - type: nauc_map_at_1000_diff1
      value: 10.9401
    - type: nauc_recall_at_1_max
      value: -10.8287
    - type: nauc_recall_at_1_std
      value: -17.1177
    - type: nauc_recall_at_1_diff1
      value: 14.4508
    - type: nauc_recall_at_3_max
      value: -5.0587
    - type: nauc_recall_at_3_std
      value: -16.730800000000002
    - type: nauc_recall_at_3_diff1
      value: 6.8079
    - type: nauc_recall_at_5_max
      value: -2.6783
    - type: nauc_recall_at_5_std
      value: -14.5046
    - type: nauc_recall_at_5_diff1
      value: 3.096
    - type: nauc_recall_at_10_max
      value: -1.5855000000000001
    - type: nauc_recall_at_10_std
      value: -8.2276
    - type: nauc_recall_at_10_diff1
      value: -6.1741
    - type: nauc_recall_at_20_max
      value: 15.754299999999999
    - type: nauc_recall_at_20_std
      value: 8.1974
    - type: nauc_recall_at_20_diff1
      value: -4.9207
    - type: nauc_recall_at_100_max
      value: 20.4574
    - type: nauc_recall_at_100_std
      value: 36.3741
    - type: nauc_recall_at_100_diff1
      value: -7.9483
    - type: nauc_recall_at_1000_max
      value: 21.6023
    - type: nauc_recall_at_1000_std
      value: 68.7296
    - type: nauc_recall_at_1000_diff1
      value: -24.9261
    - type: nauc_precision_at_1_max
      value: -10.8287
    - type: nauc_precision_at_1_std
      value: -17.1177
    - type: nauc_precision_at_1_diff1
      value: 14.4508
    - type: nauc_precision_at_3_max
      value: -5.0587
    - type: nauc_precision_at_3_std
      value: -16.730800000000002
    - type: nauc_precision_at_3_diff1
      value: 6.8079
    - type: nauc_precision_at_5_max
      value: -2.6783
    - type: nauc_precision_at_5_std
      value: -14.5046
    - type: nauc_precision_at_5_diff1
      value: 3.096
    - type: nauc_precision_at_10_max
      value: -1.5855000000000001
    - type: nauc_precision_at_10_std
      value: -8.2276
    - type: nauc_precision_at_10_diff1
      value: -6.1741
    - type: nauc_precision_at_20_max
      value: 15.754299999999999
    - type: nauc_precision_at_20_std
      value: 8.1974
    - type: nauc_precision_at_20_diff1
      value: -4.9207
    - type: nauc_precision_at_100_max
      value: 20.4574
    - type: nauc_precision_at_100_std
      value: 36.3741
    - type: nauc_precision_at_100_diff1
      value: -7.9483
    - type: nauc_precision_at_1000_max
      value: 21.6023
    - type: nauc_precision_at_1000_std
      value: 68.7296
    - type: nauc_precision_at_1000_diff1
      value: -24.9261
    - type: nauc_mrr_at_1_max
      value: -11.251999999999999
    - type: nauc_mrr_at_1_std
      value: -17.4386
    - type: nauc_mrr_at_1_diff1
      value: 13.414200000000001
    - type: nauc_mrr_at_3_max
      value: -9.7985
    - type: nauc_mrr_at_3_std
      value: -16.650000000000002
    - type: nauc_mrr_at_3_diff1
      value: 9.5099
    - type: nauc_mrr_at_5_max
      value: -9.064
    - type: nauc_mrr_at_5_std
      value: -16.4409
    - type: nauc_mrr_at_5_diff1
      value: 9.4773
    - type: nauc_mrr_at_10_max
      value: -9.310400000000001
    - type: nauc_mrr_at_10_std
      value: -16.0546
    - type: nauc_mrr_at_10_diff1
      value: 9.2528
    - type: nauc_mrr_at_20_max
      value: -9.223099999999999
    - type: nauc_mrr_at_20_std
      value: -16.0659
    - type: nauc_mrr_at_20_diff1
      value: 9.5259
    - type: nauc_mrr_at_100_max
      value: -9.2678
    - type: nauc_mrr_at_100_std
      value: -16.0911
    - type: nauc_mrr_at_100_diff1
      value: 9.608600000000001
    - type: nauc_mrr_at_1000_max
      value: -9.2699
    - type: nauc_mrr_at_1000_std
      value: -16.095100000000002
    - type: nauc_mrr_at_1000_diff1
      value: 9.6099
    - type: main_score
      value: 58.011
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 44.684400000000004
    - type: v_measure_std
      value: 13.5064
    - type: main_score
      value: 44.684400000000004
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 35.0503
    - type: v_measure_std
      value: 13.9543
    - type: main_score
      value: 35.0503
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: map
      value: 60.648500000000006
    - type: mrr
      value: 74.528
    - type: nAUC_map_max
      value: 19.4239
    - type: nAUC_map_std
      value: 20.0729
    - type: nAUC_map_diff1
      value: 10.0382
    - type: nAUC_mrr_max
      value: 30.693199999999997
    - type: nAUC_mrr_std
      value: 27.1279
    - type: nAUC_mrr_diff1
      value: 23.0291
    - type: main_score
      value: 60.648500000000006
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: pearson
      value: 89.5081
    - type: spearman
      value: 87.0568
    - type: cosine_pearson
      value: 89.5081
    - type: cosine_spearman
      value: 87.0568
    - type: manhattan_pearson
      value: 88.1247
    - type: manhattan_spearman
      value: 87.2556
    - type: euclidean_pearson
      value: 88.3266
    - type: euclidean_spearman
      value: 87.0568
    - type: main_score
      value: 87.0568
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 80.18180000000001
    - type: f1
      value: 79.5538
    - type: f1_weighted
      value: 79.5538
    - type: main_score
      value: 80.18180000000001
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 36.0126
    - type: v_measure_std
      value: 0.47019999999999995
    - type: main_score
      value: 36.0126
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 28.6331
    - type: v_measure_std
      value: 0.8607999999999999
    - type: main_score
      value: 28.6331
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: ndcg_at_1
      value: 45.207
    - type: ndcg_at_3
      value: 51.31400000000001
    - type: ndcg_at_5
      value: 54.093999999999994
    - type: ndcg_at_10
      value: 56.31
    - type: ndcg_at_20
      value: 58.378
    - type: ndcg_at_100
      value: 61.307
    - type: ndcg_at_1000
      value: 62.724999999999994
    - type: map_at_1
      value: 37.732
    - type: map_at_3
      value: 46.263
    - type: map_at_5
      value: 48.553000000000004
    - type: map_at_10
      value: 49.984
    - type: map_at_20
      value: 50.888999999999996
    - type: map_at_100
      value: 51.568999999999996
    - type: map_at_1000
      value: 51.666999999999994
    - type: recall_at_1
      value: 37.732
    - type: recall_at_3
      value: 53.736
    - type: recall_at_5
      value: 60.95399999999999
    - type: recall_at_10
      value: 68.062
    - type: recall_at_20
      value: 75.149
    - type: recall_at_100
      value: 88.075
    - type: recall_at_1000
      value: 96.878
    - type: precision_at_1
      value: 45.207
    - type: precision_at_3
      value: 24.368000000000002
    - type: precision_at_5
      value: 17.854
    - type: precision_at_10
      value: 10.558
    - type: precision_at_20
      value: 6.23
    - type: precision_at_100
      value: 1.614
    - type: precision_at_1000
      value: 0.202
    - type: mrr_at_1
      value: 45.2074
    - type: mrr_at_3
      value: 52.9804
    - type: mrr_at_5
      value: 54.718599999999995
    - type: mrr_at_10
      value: 55.5713
    - type: mrr_at_20
      value: 55.94
    - type: mrr_at_100
      value: 56.21699999999999
    - type: mrr_at_1000
      value: 56.2504
    - type: nauc_ndcg_at_1_max
      value: 43.7697
    - type: nauc_ndcg_at_1_std
      value: -3.9530000000000003
    - type: nauc_ndcg_at_1_diff1
      value: 57.75320000000001
    - type: nauc_ndcg_at_3_max
      value: 42.7238
    - type: nauc_ndcg_at_3_std
      value: -3.5654
    - type: nauc_ndcg_at_3_diff1
      value: 53.552299999999995
    - type: nauc_ndcg_at_5_max
      value: 43.115500000000004
    - type: nauc_ndcg_at_5_std
      value: -2.1444
    - type: nauc_ndcg_at_5_diff1
      value: 53.130500000000005
    - type: nauc_ndcg_at_10_max
      value: 43.0188
    - type: nauc_ndcg_at_10_std
      value: -3.1515
    - type: nauc_ndcg_at_10_diff1
      value: 53.593199999999996
    - type: nauc_ndcg_at_20_max
      value: 43.4617
    - type: nauc_ndcg_at_20_std
      value: -2.9284
    - type: nauc_ndcg_at_20_diff1
      value: 53.28000000000001
    - type: nauc_ndcg_at_100_max
      value: 44.0704
    - type: nauc_ndcg_at_100_std
      value: -0.5772
    - type: nauc_ndcg_at_100_diff1
      value: 53.439899999999994
    - type: nauc_ndcg_at_1000_max
      value: 44.256099999999996
    - type: nauc_ndcg_at_1000_std
      value: -1.1407
    - type: nauc_ndcg_at_1000_diff1
      value: 53.8728
    - type: nauc_map_at_1_max
      value: 36.613800000000005
    - type: nauc_map_at_1_std
      value: -5.8014
    - type: nauc_map_at_1_diff1
      value: 59.0186
    - type: nauc_map_at_3_max
      value: 40.8666
    - type: nauc_map_at_3_std
      value: -4.886299999999999
    - type: nauc_map_at_3_diff1
      value: 55.324600000000004
    - type: nauc_map_at_5_max
      value: 41.9942
    - type: nauc_map_at_5_std
      value: -3.9361
    - type: nauc_map_at_5_diff1
      value: 54.8805
    - type: nauc_map_at_10_max
      value: 42.1621
    - type: nauc_map_at_10_std
      value: -4.3264
    - type: nauc_map_at_10_diff1
      value: 55.0133
    - type: nauc_map_at_20_max
      value: 42.5837
    - type: nauc_map_at_20_std
      value: -3.8526
    - type: nauc_map_at_20_diff1
      value: 54.895700000000005
    - type: nauc_map_at_100_max
      value: 42.7645
    - type: nauc_map_at_100_std
      value: -3.4568000000000003
    - type: nauc_map_at_100_diff1
      value: 54.98030000000001
    - type: nauc_map_at_1000_max
      value: 42.7915
    - type: nauc_map_at_1000_std
      value: -3.4715999999999996
    - type: nauc_map_at_1000_diff1
      value: 55.0117
    - type: nauc_recall_at_1_max
      value: 36.613800000000005
    - type: nauc_recall_at_1_std
      value: -5.8014
    - type: nauc_recall_at_1_diff1
      value: 59.0186
    - type: nauc_recall_at_3_max
      value: 39.3588
    - type: nauc_recall_at_3_std
      value: -3.29
    - type: nauc_recall_at_3_diff1
      value: 50.1633
    - type: nauc_recall_at_5_max
      value: 39.7596
    - type: nauc_recall_at_5_std
      value: 0.4483
    - type: nauc_recall_at_5_diff1
      value: 47.598600000000005
    - type: nauc_recall_at_10_max
      value: 37.5367
    - type: nauc_recall_at_10_std
      value: -2.5935
    - type: nauc_recall_at_10_diff1
      value: 46.824799999999996
    - type: nauc_recall_at_20_max
      value: 38.521100000000004
    - type: nauc_recall_at_20_std
      value: -2.5774
    - type: nauc_recall_at_20_diff1
      value: 44.099
    - type: nauc_recall_at_100_max
      value: 44.043
    - type: nauc_recall_at_100_std
      value: 22.724
    - type: nauc_recall_at_100_diff1
      value: 40.4973
    - type: nauc_recall_at_1000_max
      value: 59.780100000000004
    - type: nauc_recall_at_1000_std
      value: 52.512
    - type: nauc_recall_at_1000_diff1
      value: 45.2841
    - type: nauc_precision_at_1_max
      value: 43.7697
    - type: nauc_precision_at_1_std
      value: -3.9530000000000003
    - type: nauc_precision_at_1_diff1
      value: 57.75320000000001
    - type: nauc_precision_at_3_max
      value: 37.486000000000004
    - type: nauc_precision_at_3_std
      value: -1.0619
    - type: nauc_precision_at_3_diff1
      value: 28.264699999999998
    - type: nauc_precision_at_5_max
      value: 31.613599999999998
    - type: nauc_precision_at_5_std
      value: 3.6863
    - type: nauc_precision_at_5_diff1
      value: 16.0838
    - type: nauc_precision_at_10_max
      value: 23.4082
    - type: nauc_precision_at_10_std
      value: 3.3977
    - type: nauc_precision_at_10_diff1
      value: 7.3632
    - type: nauc_precision_at_20_max
      value: 16.7236
    - type: nauc_precision_at_20_std
      value: 5.7516
    - type: nauc_precision_at_20_diff1
      value: -0.8460000000000001
    - type: nauc_precision_at_100_max
      value: 3.9043
    - type: nauc_precision_at_100_std
      value: 7.7799
    - type: nauc_precision_at_100_diff1
      value: -11.0756
    - type: nauc_precision_at_1000_max
      value: -7.728
    - type: nauc_precision_at_1000_std
      value: -1.9303000000000001
    - type: nauc_precision_at_1000_diff1
      value: -17.025000000000002
    - type: nauc_mrr_at_1_max
      value: 43.7697
    - type: nauc_mrr_at_1_std
      value: -3.9530000000000003
    - type: nauc_mrr_at_1_diff1
      value: 57.75320000000001
    - type: nauc_mrr_at_3_max
      value: 44.8007
    - type: nauc_mrr_at_3_std
      value: -2.9754
    - type: nauc_mrr_at_3_diff1
      value: 53.7928
    - type: nauc_mrr_at_5_max
      value: 44.860499999999995
    - type: nauc_mrr_at_5_std
      value: -1.7683
    - type: nauc_mrr_at_5_diff1
      value: 53.5852
    - type: nauc_mrr_at_10_max
      value: 44.8025
    - type: nauc_mrr_at_10_std
      value: -2.1691
    - type: nauc_mrr_at_10_diff1
      value: 53.880300000000005
    - type: nauc_mrr_at_20_max
      value: 44.7838
    - type: nauc_mrr_at_20_std
      value: -2.3529
    - type: nauc_mrr_at_20_diff1
      value: 53.890499999999996
    - type: nauc_mrr_at_100_max
      value: 44.7905
    - type: nauc_mrr_at_100_std
      value: -2.1931
    - type: nauc_mrr_at_100_diff1
      value: 53.9458
    - type: nauc_mrr_at_1000_max
      value: 44.7943
    - type: nauc_mrr_at_1000_std
      value: -2.2006
    - type: nauc_mrr_at_1000_diff1
      value: 53.954800000000006
    - type: main_score
      value: 56.31
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: ndcg_at_1
      value: 44.840999999999994
    - type: ndcg_at_3
      value: 49.217
    - type: ndcg_at_5
      value: 50.934000000000005
    - type: ndcg_at_10
      value: 53.142999999999994
    - type: ndcg_at_20
      value: 54.778000000000006
    - type: ndcg_at_100
      value: 57.241
    - type: ndcg_at_1000
      value: 58.967999999999996
    - type: map_at_1
      value: 35.675000000000004
    - type: map_at_3
      value: 44.017
    - type: map_at_5
      value: 45.786
    - type: map_at_10
      value: 47.204
    - type: map_at_20
      value: 47.946
    - type: map_at_100
      value: 48.564
    - type: map_at_1000
      value: 48.684
    - type: recall_at_1
      value: 35.675000000000004
    - type: recall_at_3
      value: 50.641000000000005
    - type: recall_at_5
      value: 55.897
    - type: recall_at_10
      value: 62.873999999999995
    - type: recall_at_20
      value: 68.766
    - type: recall_at_100
      value: 79.90899999999999
    - type: recall_at_1000
      value: 90.78399999999999
    - type: precision_at_1
      value: 44.840999999999994
    - type: precision_at_3
      value: 23.843
    - type: precision_at_5
      value: 16.637
    - type: precision_at_10
      value: 9.968
    - type: precision_at_20
      value: 5.863
    - type: precision_at_100
      value: 1.562
    - type: precision_at_1000
      value: 0.197
    - type: mrr_at_1
      value: 44.840799999999994
    - type: mrr_at_3
      value: 51.634800000000006
    - type: mrr_at_5
      value: 52.746300000000005
    - type: mrr_at_10
      value: 53.6323
    - type: mrr_at_20
      value: 53.9565
    - type: mrr_at_100
      value: 54.198
    - type: mrr_at_1000
      value: 54.234899999999996
    - type: nauc_ndcg_at_1_max
      value: 50.3827
    - type: nauc_ndcg_at_1_std
      value: -0.8129000000000001
    - type: nauc_ndcg_at_1_diff1
      value: 59.7518
    - type: nauc_ndcg_at_3_max
      value: 49.6676
    - type: nauc_ndcg_at_3_std
      value: -2.1006
    - type: nauc_ndcg_at_3_diff1
      value: 52.7373
    - type: nauc_ndcg_at_5_max
      value: 50.5186
    - type: nauc_ndcg_at_5_std
      value: -1.5242
    - type: nauc_ndcg_at_5_diff1
      value: 53.234300000000005
    - type: nauc_ndcg_at_10_max
      value: 50.5247
    - type: nauc_ndcg_at_10_std
      value: -1.2392
    - type: nauc_ndcg_at_10_diff1
      value: 53.1045
    - type: nauc_ndcg_at_20_max
      value: 51.3292
    - type: nauc_ndcg_at_20_std
      value: -0.06570000000000001
    - type: nauc_ndcg_at_20_diff1
      value: 53.48349999999999
    - type: nauc_ndcg_at_100_max
      value: 51.588100000000004
    - type: nauc_ndcg_at_100_std
      value: 1.9398
    - type: nauc_ndcg_at_100_diff1
      value: 52.755399999999995
    - type: nauc_ndcg_at_1000_max
      value: 51.5558
    - type: nauc_ndcg_at_1000_std
      value: 2.3446000000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 52.9377
    - type: nauc_map_at_1_max
      value: 40.0957
    - type: nauc_map_at_1_std
      value: -11.972
    - type: nauc_map_at_1_diff1
      value: 61.88249999999999
    - type: nauc_map_at_3_max
      value: 45.6088
    - type: nauc_map_at_3_std
      value: -9.249699999999999
    - type: nauc_map_at_3_diff1
      value: 56.260299999999994
    - type: nauc_map_at_5_max
      value: 47.2279
    - type: nauc_map_at_5_std
      value: -7.407500000000001
    - type: nauc_map_at_5_diff1
      value: 55.7894
    - type: nauc_map_at_10_max
      value: 48.0167
    - type: nauc_map_at_10_std
      value: -6.1371
    - type: nauc_map_at_10_diff1
      value: 55.4646
    - type: nauc_map_at_20_max
      value: 48.6024
    - type: nauc_map_at_20_std
      value: -5.1559
    - type: nauc_map_at_20_diff1
      value: 55.338100000000004
    - type: nauc_map_at_100_max
      value: 48.993700000000004
    - type: nauc_map_at_100_std
      value: -4.1873000000000005
    - type: nauc_map_at_100_diff1
      value: 55.1214
    - type: nauc_map_at_1000_max
      value: 49.054500000000004
    - type: nauc_map_at_1000_std
      value: -4.0072
    - type: nauc_map_at_1000_diff1
      value: 55.109300000000005
    - type: nauc_recall_at_1_max
      value: 40.0957
    - type: nauc_recall_at_1_std
      value: -11.972
    - type: nauc_recall_at_1_diff1
      value: 61.88249999999999
    - type: nauc_recall_at_3_max
      value: 44.188
    - type: nauc_recall_at_3_std
      value: -8.3756
    - type: nauc_recall_at_3_diff1
      value: 48.6817
    - type: nauc_recall_at_5_max
      value: 46.6706
    - type: nauc_recall_at_5_std
      value: -4.1561
    - type: nauc_recall_at_5_diff1
      value: 47.6738
    - type: nauc_recall_at_10_max
      value: 47.614200000000004
    - type: nauc_recall_at_10_std
      value: -1.1676
    - type: nauc_recall_at_10_diff1
      value: 45.628099999999996
    - type: nauc_recall_at_20_max
      value: 51.490100000000005
    - type: nauc_recall_at_20_std
      value: 5.111000000000001
    - type: nauc_recall_at_20_diff1
      value: 45.730199999999996
    - type: nauc_recall_at_100_max
      value: 54.0635
    - type: nauc_recall_at_100_std
      value: 19.8381
    - type: nauc_recall_at_100_diff1
      value: 39.1924
    - type: nauc_recall_at_1000_max
      value: 56.3672
    - type: nauc_recall_at_1000_std
      value: 33.9274
    - type: nauc_recall_at_1000_diff1
      value: 38.1103
    - type: nauc_precision_at_1_max
      value: 50.3827
    - type: nauc_precision_at_1_std
      value: -0.8129000000000001
    - type: nauc_precision_at_1_diff1
      value: 59.7518
    - type: nauc_precision_at_3_max
      value: 46.281299999999995
    - type: nauc_precision_at_3_std
      value: 14.7166
    - type: nauc_precision_at_3_diff1
      value: 24.211
    - type: nauc_precision_at_5_max
      value: 44.466899999999995
    - type: nauc_precision_at_5_std
      value: 22.5103
    - type: nauc_precision_at_5_diff1
      value: 15.746099999999998
    - type: nauc_precision_at_10_max
      value: 38.0804
    - type: nauc_precision_at_10_std
      value: 29.677999999999997
    - type: nauc_precision_at_10_diff1
      value: 4.886299999999999
    - type: nauc_precision_at_20_max
      value: 32.302
    - type: nauc_precision_at_20_std
      value: 34.8443
    - type: nauc_precision_at_20_diff1
      value: -2.9212
    - type: nauc_precision_at_100_max
      value: 21.4725
    - type: nauc_precision_at_100_std
      value: 41.8747
    - type: nauc_precision_at_100_diff1
      value: -14.976600000000001
    - type: nauc_precision_at_1000_max
      value: 10.3891
    - type: nauc_precision_at_1000_std
      value: 39.4181
    - type: nauc_precision_at_1000_diff1
      value: -21.9914
    - type: nauc_mrr_at_1_max
      value: 50.3827
    - type: nauc_mrr_at_1_std
      value: -0.8129000000000001
    - type: nauc_mrr_at_1_diff1
      value: 59.7518
    - type: nauc_mrr_at_3_max
      value: 51.9937
    - type: nauc_mrr_at_3_std
      value: 2.1604
    - type: nauc_mrr_at_3_diff1
      value: 54.58539999999999
    - type: nauc_mrr_at_5_max
      value: 52.39319999999999
    - type: nauc_mrr_at_5_std
      value: 2.8171
    - type: nauc_mrr_at_5_diff1
      value: 54.825100000000006
    - type: nauc_mrr_at_10_max
      value: 52.2047
    - type: nauc_mrr_at_10_std
      value: 2.6525
    - type: nauc_mrr_at_10_diff1
      value: 54.703500000000005
    - type: nauc_mrr_at_20_max
      value: 52.251999999999995
    - type: nauc_mrr_at_20_std
      value: 2.7842
    - type: nauc_mrr_at_20_diff1
      value: 54.76689999999999
    - type: nauc_mrr_at_100_max
      value: 52.2776
    - type: nauc_mrr_at_100_std
      value: 2.9701999999999997
    - type: nauc_mrr_at_100_diff1
      value: 54.712799999999994
    - type: nauc_mrr_at_1000_max
      value: 52.274699999999996
    - type: nauc_mrr_at_1000_std
      value: 2.9652000000000003
    - type: nauc_mrr_at_1000_diff1
      value: 54.7296
    - type: main_score
      value: 53.142999999999994
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: ndcg_at_1
      value: 53.542
    - type: ndcg_at_3
      value: 60.098
    - type: ndcg_at_5
      value: 62.515
    - type: ndcg_at_10
      value: 65.315
    - type: ndcg_at_20
      value: 66.683
    - type: ndcg_at_100
      value: 68.47800000000001
    - type: ndcg_at_1000
      value: 69.329
    - type: map_at_1
      value: 47.135
    - type: map_at_3
      value: 56.548
    - type: map_at_5
      value: 58.306000000000004
    - type: map_at_10
      value: 59.819
    - type: map_at_20
      value: 60.328
    - type: map_at_100
      value: 60.653999999999996
    - type: map_at_1000
      value: 60.699000000000005
    - type: recall_at_1
      value: 47.135
    - type: recall_at_3
      value: 64.371
    - type: recall_at_5
      value: 70.293
    - type: recall_at_10
      value: 78.346
    - type: recall_at_20
      value: 83.369
    - type: recall_at_100
      value: 92.04599999999999
    - type: recall_at_1000
      value: 97.933
    - type: precision_at_1
      value: 53.542
    - type: precision_at_3
      value: 26.395000000000003
    - type: precision_at_5
      value: 17.806
    - type: precision_at_10
      value: 10.238
    - type: precision_at_20
      value: 5.586
    - type: precision_at_100
      value: 1.266
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 53.5423
    - type: mrr_at_3
      value: 60.595600000000005
    - type: mrr_at_5
      value: 61.931000000000004
    - type: mrr_at_10
      value: 62.8406
    - type: mrr_at_20
      value: 63.1667
    - type: mrr_at_100
      value: 63.347699999999996
    - type: mrr_at_1000
      value: 63.368100000000005
    - type: nauc_ndcg_at_1_max
      value: 50.004599999999996
    - type: nauc_ndcg_at_1_std
      value: -4.3123000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 61.1973
    - type: nauc_ndcg_at_3_max
      value: 48.65
    - type: nauc_ndcg_at_3_std
      value: -6.0419
    - type: nauc_ndcg_at_3_diff1
      value: 56.712700000000005
    - type: nauc_ndcg_at_5_max
      value: 50.0908
    - type: nauc_ndcg_at_5_std
      value: -4.4674
    - type: nauc_ndcg_at_5_diff1
      value: 56.216
    - type: nauc_ndcg_at_10_max
      value: 50.578
    - type: nauc_ndcg_at_10_std
      value: -2.661
    - type: nauc_ndcg_at_10_diff1
      value: 55.9162
    - type: nauc_ndcg_at_20_max
      value: 51.3801
    - type: nauc_ndcg_at_20_std
      value: -0.8059999999999999
    - type: nauc_ndcg_at_20_diff1
      value: 55.8654
    - type: nauc_ndcg_at_100_max
      value: 51.4594
    - type: nauc_ndcg_at_100_std
      value: -0.3524
    - type: nauc_ndcg_at_100_diff1
      value: 56.131699999999995
    - type: nauc_ndcg_at_1000_max
      value: 51.6105
    - type: nauc_ndcg_at_1000_std
      value: -0.8832
    - type: nauc_ndcg_at_1000_diff1
      value: 56.6507
    - type: nauc_map_at_1_max
      value: 42.7316
    - type: nauc_map_at_1_std
      value: -6.979100000000001
    - type: nauc_map_at_1_diff1
      value: 61.6382
    - type: nauc_map_at_3_max
      value: 47.6139
    - type: nauc_map_at_3_std
      value: -7.0931
    - type: nauc_map_at_3_diff1
      value: 58.2923
    - type: nauc_map_at_5_max
      value: 48.6039
    - type: nauc_map_at_5_std
      value: -5.9601
    - type: nauc_map_at_5_diff1
      value: 57.7052
    - type: nauc_map_at_10_max
      value: 49.2631
    - type: nauc_map_at_10_std
      value: -4.808
    - type: nauc_map_at_10_diff1
      value: 57.5979
    - type: nauc_map_at_20_max
      value: 49.6783
    - type: nauc_map_at_20_std
      value: -4.0106
    - type: nauc_map_at_20_diff1
      value: 57.5781
    - type: nauc_map_at_100_max
      value: 49.775000000000006
    - type: nauc_map_at_100_std
      value: -3.8082
    - type: nauc_map_at_100_diff1
      value: 57.6013
    - type: nauc_map_at_1000_max
      value: 49.8135
    - type: nauc_map_at_1000_std
      value: -3.7974
    - type: nauc_map_at_1000_diff1
      value: 57.6323
    - type: nauc_recall_at_1_max
      value: 42.7316
    - type: nauc_recall_at_1_std
      value: -6.979100000000001
    - type: nauc_recall_at_1_diff1
      value: 61.6382
    - type: nauc_recall_at_3_max
      value: 46.1138
    - type: nauc_recall_at_3_std
      value: -8.6906
    - type: nauc_recall_at_3_diff1
      value: 52.6263
    - type: nauc_recall_at_5_max
      value: 49.074200000000005
    - type: nauc_recall_at_5_std
      value: -4.5975
    - type: nauc_recall_at_5_diff1
      value: 49.994
    - type: nauc_recall_at_10_max
      value: 49.696
    - type: nauc_recall_at_10_std
      value: 2.049
    - type: nauc_recall_at_10_diff1
      value: 46.7897
    - type: nauc_recall_at_20_max
      value: 54.03980000000001
    - type: nauc_recall_at_20_std
      value: 14.4898
    - type: nauc_recall_at_20_diff1
      value: 43.8642
    - type: nauc_recall_at_100_max
      value: 57.23629999999999
    - type: nauc_recall_at_100_std
      value: 32.6507
    - type: nauc_recall_at_100_diff1
      value: 38.4662
    - type: nauc_recall_at_1000_max
      value: 81.5918
    - type: nauc_recall_at_1000_std
      value: 67.0848
    - type: nauc_recall_at_1000_diff1
      value: 40.5123
    - type: nauc_precision_at_1_max
      value: 50.004599999999996
    - type: nauc_precision_at_1_std
      value: -4.3123000000000005
    - type: nauc_precision_at_1_diff1
      value: 61.1973
    - type: nauc_precision_at_3_max
      value: 41.0359
    - type: nauc_precision_at_3_std
      value: 2.2363
    - type: nauc_precision_at_3_diff1
      value: 26.9914
    - type: nauc_precision_at_5_max
      value: 38.3114
    - type: nauc_precision_at_5_std
      value: 8.7643
    - type: nauc_precision_at_5_diff1
      value: 17.0673
    - type: nauc_precision_at_10_max
      value: 31.1391
    - type: nauc_precision_at_10_std
      value: 17.1411
    - type: nauc_precision_at_10_diff1
      value: 4.9287
    - type: nauc_precision_at_20_max
      value: 27.7595
    - type: nauc_precision_at_20_std
      value: 25.470399999999998
    - type: nauc_precision_at_20_diff1
      value: -2.6803
    - type: nauc_precision_at_100_max
      value: 18.2146
    - type: nauc_precision_at_100_std
      value: 29.244300000000003
    - type: nauc_precision_at_100_diff1
      value: -13.083
    - type: nauc_precision_at_1000_max
      value: 13.5621
    - type: nauc_precision_at_1000_std
      value: 26.3405
    - type: nauc_precision_at_1000_diff1
      value: -15.398200000000001
    - type: nauc_mrr_at_1_max
      value: 50.004599999999996
    - type: nauc_mrr_at_1_std
      value: -4.3123000000000005
    - type: nauc_mrr_at_1_diff1
      value: 61.1973
    - type: nauc_mrr_at_3_max
      value: 50.114599999999996
    - type: nauc_mrr_at_3_std
      value: -4.7759
    - type: nauc_mrr_at_3_diff1
      value: 57.9624
    - type: nauc_mrr_at_5_max
      value: 50.956900000000005
    - type: nauc_mrr_at_5_std
      value: -3.7144999999999997
    - type: nauc_mrr_at_5_diff1
      value: 57.784400000000005
    - type: nauc_mrr_at_10_max
      value: 50.8112
    - type: nauc_mrr_at_10_std
      value: -3.3526
    - type: nauc_mrr_at_10_diff1
      value: 57.674499999999995
    - type: nauc_mrr_at_20_max
      value: 50.9425
    - type: nauc_mrr_at_20_std
      value: -2.9598
    - type: nauc_mrr_at_20_diff1
      value: 57.6704
    - type: nauc_mrr_at_100_max
      value: 50.901799999999994
    - type: nauc_mrr_at_100_std
      value: -3.0112
    - type: nauc_mrr_at_100_diff1
      value: 57.736200000000004
    - type: nauc_mrr_at_1000_max
      value: 50.901399999999995
    - type: nauc_mrr_at_1000_std
      value: -3.0314
    - type: nauc_mrr_at_1000_diff1
      value: 57.747400000000006
    - type: main_score
      value: 65.315
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: ndcg_at_1
      value: 33.898
    - type: ndcg_at_3
      value: 39.875
    - type: ndcg_at_5
      value: 42.455999999999996
    - type: ndcg_at_10
      value: 45.4
    - type: ndcg_at_20
      value: 47.831
    - type: ndcg_at_100
      value: 50.428
    - type: ndcg_at_1000
      value: 52.037
    - type: map_at_1
      value: 31.357000000000003
    - type: map_at_3
      value: 37.358999999999995
    - type: map_at_5
      value: 38.948
    - type: map_at_10
      value: 40.243
    - type: map_at_20
      value: 40.98
    - type: map_at_100
      value: 41.349999999999994
    - type: map_at_1000
      value: 41.418
    - type: recall_at_1
      value: 31.357000000000003
    - type: recall_at_3
      value: 44.324000000000005
    - type: recall_at_5
      value: 50.449
    - type: recall_at_10
      value: 59.17400000000001
    - type: recall_at_20
      value: 68.272
    - type: recall_at_100
      value: 81.672
    - type: recall_at_1000
      value: 93.572
    - type: precision_at_1
      value: 33.898
    - type: precision_at_3
      value: 16.648
    - type: precision_at_5
      value: 11.503
    - type: precision_at_10
      value: 6.847
    - type: precision_at_20
      value: 3.9890000000000003
    - type: precision_at_100
      value: 0.9809999999999999
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: mrr_at_1
      value: 33.8983
    - type: mrr_at_3
      value: 39.8117
    - type: mrr_at_5
      value: 41.2354
    - type: mrr_at_10
      value: 42.4212
    - type: mrr_at_20
      value: 43.0404
    - type: mrr_at_100
      value: 43.3429
    - type: mrr_at_1000
      value: 43.3894
    - type: nauc_ndcg_at_1_max
      value: 36.1482
    - type: nauc_ndcg_at_1_std
      value: -4.471
    - type: nauc_ndcg_at_1_diff1
      value: 44.1333
    - type: nauc_ndcg_at_3_max
      value: 35.404
    - type: nauc_ndcg_at_3_std
      value: -4.487
    - type: nauc_ndcg_at_3_diff1
      value: 40.3399
    - type: nauc_ndcg_at_5_max
      value: 35.0036
    - type: nauc_ndcg_at_5_std
      value: -4.0964
    - type: nauc_ndcg_at_5_diff1
      value: 38.2164
    - type: nauc_ndcg_at_10_max
      value: 34.7255
    - type: nauc_ndcg_at_10_std
      value: -2.9356
    - type: nauc_ndcg_at_10_diff1
      value: 37.3216
    - type: nauc_ndcg_at_20_max
      value: 35.5433
    - type: nauc_ndcg_at_20_std
      value: -1.8858
    - type: nauc_ndcg_at_20_diff1
      value: 36.6106
    - type: nauc_ndcg_at_100_max
      value: 35.9643
    - type: nauc_ndcg_at_100_std
      value: -1.6303
    - type: nauc_ndcg_at_100_diff1
      value: 37.515100000000004
    - type: nauc_ndcg_at_1000_max
      value: 35.9222
    - type: nauc_ndcg_at_1000_std
      value: -2.1452999999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 37.472100000000005
    - type: nauc_map_at_1_max
      value: 32.413599999999995
    - type: nauc_map_at_1_std
      value: -7.391300000000001
    - type: nauc_map_at_1_diff1
      value: 45.5299
    - type: nauc_map_at_3_max
      value: 34.1688
    - type: nauc_map_at_3_std
      value: -5.6375
    - type: nauc_map_at_3_diff1
      value: 41.5371
    - type: nauc_map_at_5_max
      value: 34.2057
    - type: nauc_map_at_5_std
      value: -5.4512
    - type: nauc_map_at_5_diff1
      value: 40.3839
    - type: nauc_map_at_10_max
      value: 34.3355
    - type: nauc_map_at_10_std
      value: -4.7743
    - type: nauc_map_at_10_diff1
      value: 40.1027
    - type: nauc_map_at_20_max
      value: 34.638400000000004
    - type: nauc_map_at_20_std
      value: -4.4951
    - type: nauc_map_at_20_diff1
      value: 39.8905
    - type: nauc_map_at_100_max
      value: 34.6621
    - type: nauc_map_at_100_std
      value: -4.4568
    - type: nauc_map_at_100_diff1
      value: 39.9854
    - type: nauc_map_at_1000_max
      value: 34.6674
    - type: nauc_map_at_1000_std
      value: -4.4651000000000005
    - type: nauc_map_at_1000_diff1
      value: 39.9739
    - type: nauc_recall_at_1_max
      value: 32.413599999999995
    - type: nauc_recall_at_1_std
      value: -7.391300000000001
    - type: nauc_recall_at_1_diff1
      value: 45.5299
    - type: nauc_recall_at_3_max
      value: 34.374500000000005
    - type: nauc_recall_at_3_std
      value: -3.8977999999999997
    - type: nauc_recall_at_3_diff1
      value: 36.9855
    - type: nauc_recall_at_5_max
      value: 33.5608
    - type: nauc_recall_at_5_std
      value: -2.9009
    - type: nauc_recall_at_5_diff1
      value: 31.9638
    - type: nauc_recall_at_10_max
      value: 32.1813
    - type: nauc_recall_at_10_std
      value: 0.8024999999999999
    - type: nauc_recall_at_10_diff1
      value: 28.3153
    - type: nauc_recall_at_20_max
      value: 35.0617
    - type: nauc_recall_at_20_std
      value: 6.531199999999999
    - type: nauc_recall_at_20_diff1
      value: 23.6762
    - type: nauc_recall_at_100_max
      value: 38.9147
    - type: nauc_recall_at_100_std
      value: 12.4753
    - type: nauc_recall_at_100_diff1
      value: 26.1627
    - type: nauc_recall_at_1000_max
      value: 45.8191
    - type: nauc_recall_at_1000_std
      value: 17.1419
    - type: nauc_recall_at_1000_diff1
      value: 13.2284
    - type: nauc_precision_at_1_max
      value: 36.1482
    - type: nauc_precision_at_1_std
      value: -4.471
    - type: nauc_precision_at_1_diff1
      value: 44.1333
    - type: nauc_precision_at_3_max
      value: 38.315
    - type: nauc_precision_at_3_std
      value: -0.16019999999999998
    - type: nauc_precision_at_3_diff1
      value: 32.4158
    - type: nauc_precision_at_5_max
      value: 36.3912
    - type: nauc_precision_at_5_std
      value: 0.9605
    - type: nauc_precision_at_5_diff1
      value: 25.7513
    - type: nauc_precision_at_10_max
      value: 34.043
    - type: nauc_precision_at_10_std
      value: 5.6308
    - type: nauc_precision_at_10_diff1
      value: 20.5638
    - type: nauc_precision_at_20_max
      value: 34.5796
    - type: nauc_precision_at_20_std
      value: 10.0006
    - type: nauc_precision_at_20_diff1
      value: 13.069500000000001
    - type: nauc_precision_at_100_max
      value: 27.5607
    - type: nauc_precision_at_100_std
      value: 13.173399999999999
    - type: nauc_precision_at_100_diff1
      value: 6.1834
    - type: nauc_precision_at_1000_max
      value: 15.5825
    - type: nauc_precision_at_1000_std
      value: 9.9148
    - type: nauc_precision_at_1000_diff1
      value: -8.7873
    - type: nauc_mrr_at_1_max
      value: 36.1482
    - type: nauc_mrr_at_1_std
      value: -4.471
    - type: nauc_mrr_at_1_diff1
      value: 44.1333
    - type: nauc_mrr_at_3_max
      value: 37.059799999999996
    - type: nauc_mrr_at_3_std
      value: -2.7984999999999998
    - type: nauc_mrr_at_3_diff1
      value: 40.3801
    - type: nauc_mrr_at_5_max
      value: 36.921
    - type: nauc_mrr_at_5_std
      value: -2.5107
    - type: nauc_mrr_at_5_diff1
      value: 39.3331
    - type: nauc_mrr_at_10_max
      value: 36.5977
    - type: nauc_mrr_at_10_std
      value: -2.3744
    - type: nauc_mrr_at_10_diff1
      value: 38.851200000000006
    - type: nauc_mrr_at_20_max
      value: 36.7083
    - type: nauc_mrr_at_20_std
      value: -2.164
    - type: nauc_mrr_at_20_diff1
      value: 38.729200000000006
    - type: nauc_mrr_at_100_max
      value: 36.7448
    - type: nauc_mrr_at_100_std
      value: -2.1399999999999997
    - type: nauc_mrr_at_100_diff1
      value: 38.8403
    - type: nauc_mrr_at_1000_max
      value: 36.742200000000004
    - type: nauc_mrr_at_1000_std
      value: -2.1506999999999996
    - type: nauc_mrr_at_1000_diff1
      value: 38.8393
    - type: main_score
      value: 45.4
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: ndcg_at_1
      value: 25.124000000000002
    - type: ndcg_at_3
      value: 29.798000000000002
    - type: ndcg_at_5
      value: 32.112
    - type: ndcg_at_10
      value: 34.926
    - type: ndcg_at_20
      value: 37.317
    - type: ndcg_at_100
      value: 40.903
    - type: ndcg_at_1000
      value: 43.18
    - type: map_at_1
      value: 20.279
    - type: map_at_3
      value: 26.551000000000002
    - type: map_at_5
      value: 28.051
    - type: map_at_10
      value: 29.37
    - type: map_at_20
      value: 30.085
    - type: map_at_100
      value: 30.668
    - type: map_at_1000
      value: 30.774
    - type: recall_at_1
      value: 20.279
    - type: recall_at_3
      value: 33.043
    - type: recall_at_5
      value: 38.991
    - type: recall_at_10
      value: 47.355999999999995
    - type: recall_at_20
      value: 55.873
    - type: recall_at_100
      value: 72.90100000000001
    - type: recall_at_1000
      value: 88.678
    - type: precision_at_1
      value: 25.124000000000002
    - type: precision_at_3
      value: 14.221
    - type: precision_at_5
      value: 10.323
    - type: precision_at_10
      value: 6.381
    - type: precision_at_20
      value: 3.8739999999999997
    - type: precision_at_100
      value: 1.082
    - type: precision_at_1000
      value: 0.13999999999999999
    - type: mrr_at_1
      value: 25.1244
    - type: mrr_at_3
      value: 31.3847
    - type: mrr_at_5
      value: 32.9768
    - type: mrr_at_10
      value: 34.1348
    - type: mrr_at_20
      value: 34.7501
    - type: mrr_at_100
      value: 35.1367
    - type: mrr_at_1000
      value: 35.191
    - type: nauc_ndcg_at_1_max
      value: 27.160600000000002
    - type: nauc_ndcg_at_1_std
      value: 1.7711999999999999
    - type: nauc_ndcg_at_1_diff1
      value: 39.8547
    - type: nauc_ndcg_at_3_max
      value: 23.7332
    - type: nauc_ndcg_at_3_std
      value: 0.4508
    - type: nauc_ndcg_at_3_diff1
      value: 34.3668
    - type: nauc_ndcg_at_5_max
      value: 24.6552
    - type: nauc_ndcg_at_5_std
      value: 1.7423000000000002
    - type: nauc_ndcg_at_5_diff1
      value: 34.8806
    - type: nauc_ndcg_at_10_max
      value: 24.3869
    - type: nauc_ndcg_at_10_std
      value: 1.3054
    - type: nauc_ndcg_at_10_diff1
      value: 33.7015
    - type: nauc_ndcg_at_20_max
      value: 24.449
    - type: nauc_ndcg_at_20_std
      value: 2.4919000000000002
    - type: nauc_ndcg_at_20_diff1
      value: 32.9483
    - type: nauc_ndcg_at_100_max
      value: 25.3655
    - type: nauc_ndcg_at_100_std
      value: 2.7169
    - type: nauc_ndcg_at_100_diff1
      value: 32.8817
    - type: nauc_ndcg_at_1000_max
      value: 25.524599999999996
    - type: nauc_ndcg_at_1000_std
      value: 3.1405000000000003
    - type: nauc_ndcg_at_1000_diff1
      value: 32.7208
    - type: nauc_map_at_1_max
      value: 24.9051
    - type: nauc_map_at_1_std
      value: 2.788
    - type: nauc_map_at_1_diff1
      value: 38.9946
    - type: nauc_map_at_3_max
      value: 23.061
    - type: nauc_map_at_3_std
      value: 1.0529
    - type: nauc_map_at_3_diff1
      value: 35.0109
    - type: nauc_map_at_5_max
      value: 23.704800000000002
    - type: nauc_map_at_5_std
      value: 1.7375999999999998
    - type: nauc_map_at_5_diff1
      value: 35.2714
    - type: nauc_map_at_10_max
      value: 23.7351
    - type: nauc_map_at_10_std
      value: 1.5004
    - type: nauc_map_at_10_diff1
      value: 34.8483
    - type: nauc_map_at_20_max
      value: 23.7699
    - type: nauc_map_at_20_std
      value: 1.8925999999999998
    - type: nauc_map_at_20_diff1
      value: 34.6198
    - type: nauc_map_at_100_max
      value: 23.962600000000002
    - type: nauc_map_at_100_std
      value: 1.9238000000000002
    - type: nauc_map_at_100_diff1
      value: 34.7253
    - type: nauc_map_at_1000_max
      value: 23.965
    - type: nauc_map_at_1000_std
      value: 1.9339
    - type: nauc_map_at_1000_diff1
      value: 34.719899999999996
    - type: nauc_recall_at_1_max
      value: 24.9051
    - type: nauc_recall_at_1_std
      value: 2.788
    - type: nauc_recall_at_1_diff1
      value: 38.9946
    - type: nauc_recall_at_3_max
      value: 21.8415
    - type: nauc_recall_at_3_std
      value: 0.5292
    - type: nauc_recall_at_3_diff1
      value: 30.811
    - type: nauc_recall_at_5_max
      value: 23.8237
    - type: nauc_recall_at_5_std
      value: 2.5335
    - type: nauc_recall_at_5_diff1
      value: 31.928800000000003
    - type: nauc_recall_at_10_max
      value: 22.5541
    - type: nauc_recall_at_10_std
      value: 0.9076000000000001
    - type: nauc_recall_at_10_diff1
      value: 27.8364
    - type: nauc_recall_at_20_max
      value: 22.0853
    - type: nauc_recall_at_20_std
      value: 4.9954
    - type: nauc_recall_at_20_diff1
      value: 24.2376
    - type: nauc_recall_at_100_max
      value: 26.4301
    - type: nauc_recall_at_100_std
      value: 8.5471
    - type: nauc_recall_at_100_diff1
      value: 19.2131
    - type: nauc_recall_at_1000_max
      value: 36.3726
    - type: nauc_recall_at_1000_std
      value: 26.9247
    - type: nauc_recall_at_1000_diff1
      value: 3.8798
    - type: nauc_precision_at_1_max
      value: 27.160600000000002
    - type: nauc_precision_at_1_std
      value: 1.7711999999999999
    - type: nauc_precision_at_1_diff1
      value: 39.8547
    - type: nauc_precision_at_3_max
      value: 23.8679
    - type: nauc_precision_at_3_std
      value: -1.052
    - type: nauc_precision_at_3_diff1
      value: 29.999100000000002
    - type: nauc_precision_at_5_max
      value: 24.7345
    - type: nauc_precision_at_5_std
      value: 1.3604
    - type: nauc_precision_at_5_diff1
      value: 29.8611
    - type: nauc_precision_at_10_max
      value: 21.5396
    - type: nauc_precision_at_10_std
      value: -1.0137
    - type: nauc_precision_at_10_diff1
      value: 23.519000000000002
    - type: nauc_precision_at_20_max
      value: 18.4431
    - type: nauc_precision_at_20_std
      value: 1.5350000000000001
    - type: nauc_precision_at_20_diff1
      value: 16.5031
    - type: nauc_precision_at_100_max
      value: 13.9255
    - type: nauc_precision_at_100_std
      value: -0.48650000000000004
    - type: nauc_precision_at_100_diff1
      value: 7.700799999999999
    - type: nauc_precision_at_1000_max
      value: 3.6421
    - type: nauc_precision_at_1000_std
      value: -4.7682
    - type: nauc_precision_at_1000_diff1
      value: -1.4256
    - type: nauc_mrr_at_1_max
      value: 27.160600000000002
    - type: nauc_mrr_at_1_std
      value: 1.7711999999999999
    - type: nauc_mrr_at_1_diff1
      value: 39.8547
    - type: nauc_mrr_at_3_max
      value: 25.44
    - type: nauc_mrr_at_3_std
      value: 0.08639999999999999
    - type: nauc_mrr_at_3_diff1
      value: 35.381800000000005
    - type: nauc_mrr_at_5_max
      value: 26.011899999999997
    - type: nauc_mrr_at_5_std
      value: 0.6948
    - type: nauc_mrr_at_5_diff1
      value: 36.246
    - type: nauc_mrr_at_10_max
      value: 25.8141
    - type: nauc_mrr_at_10_std
      value: 0.5511
    - type: nauc_mrr_at_10_diff1
      value: 35.7313
    - type: nauc_mrr_at_20_max
      value: 25.805899999999998
    - type: nauc_mrr_at_20_std
      value: 0.8933
    - type: nauc_mrr_at_20_diff1
      value: 35.4972
    - type: nauc_mrr_at_100_max
      value: 25.909
    - type: nauc_mrr_at_100_std
      value: 0.8796999999999999
    - type: nauc_mrr_at_100_diff1
      value: 35.5299
    - type: nauc_mrr_at_1000_max
      value: 25.910800000000002
    - type: nauc_mrr_at_1000_std
      value: 0.9046000000000001
    - type: nauc_mrr_at_1000_diff1
      value: 35.522999999999996
    - type: main_score
      value: 34.926
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: ndcg_at_1
      value: 42.059999999999995
    - type: ndcg_at_3
      value: 46.461999999999996
    - type: ndcg_at_5
      value: 48.662
    - type: ndcg_at_10
      value: 50.925
    - type: ndcg_at_20
      value: 53.120999999999995
    - type: ndcg_at_100
      value: 56.189
    - type: ndcg_at_1000
      value: 57.972
    - type: map_at_1
      value: 33.919
    - type: map_at_3
      value: 41.858000000000004
    - type: map_at_5
      value: 43.629
    - type: map_at_10
      value: 45.01
    - type: map_at_20
      value: 45.781
    - type: map_at_100
      value: 46.372
    - type: map_at_1000
      value: 46.477000000000004
    - type: recall_at_1
      value: 33.919
    - type: recall_at_3
      value: 49.153999999999996
    - type: recall_at_5
      value: 55.422000000000004
    - type: recall_at_10
      value: 62.204
    - type: recall_at_20
      value: 69.819
    - type: recall_at_100
      value: 83.67599999999999
    - type: recall_at_1000
      value: 95.093
    - type: precision_at_1
      value: 42.059999999999995
    - type: precision_at_3
      value: 22.201
    - type: precision_at_5
      value: 15.342
    - type: precision_at_10
      value: 9.038
    - type: precision_at_20
      value: 5.244999999999999
    - type: precision_at_100
      value: 1.348
    - type: precision_at_1000
      value: 0.168
    - type: mrr_at_1
      value: 42.0597
    - type: mrr_at_3
      value: 49.005500000000005
    - type: mrr_at_5
      value: 50.3673
    - type: mrr_at_10
      value: 51.14959999999999
    - type: mrr_at_20
      value: 51.656
    - type: mrr_at_100
      value: 51.969
    - type: mrr_at_1000
      value: 52.0088
    - type: nauc_ndcg_at_1_max
      value: 39.321400000000004
    - type: nauc_ndcg_at_1_std
      value: -3.3204
    - type: nauc_ndcg_at_1_diff1
      value: 50.999300000000005
    - type: nauc_ndcg_at_3_max
      value: 37.6896
    - type: nauc_ndcg_at_3_std
      value: -4.7356
    - type: nauc_ndcg_at_3_diff1
      value: 48.0551
    - type: nauc_ndcg_at_5_max
      value: 36.9149
    - type: nauc_ndcg_at_5_std
      value: -5.8358
    - type: nauc_ndcg_at_5_diff1
      value: 48.4085
    - type: nauc_ndcg_at_10_max
      value: 36.9047
    - type: nauc_ndcg_at_10_std
      value: -5.1284
    - type: nauc_ndcg_at_10_diff1
      value: 48.3356
    - type: nauc_ndcg_at_20_max
      value: 36.9876
    - type: nauc_ndcg_at_20_std
      value: -4.0274
    - type: nauc_ndcg_at_20_diff1
      value: 48.0203
    - type: nauc_ndcg_at_100_max
      value: 38.472899999999996
    - type: nauc_ndcg_at_100_std
      value: -1.1645
    - type: nauc_ndcg_at_100_diff1
      value: 47.734
    - type: nauc_ndcg_at_1000_max
      value: 38.828
    - type: nauc_ndcg_at_1000_std
      value: -1.5388000000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 47.8951
    - type: nauc_map_at_1_max
      value: 32.8495
    - type: nauc_map_at_1_std
      value: -11.1224
    - type: nauc_map_at_1_diff1
      value: 52.8561
    - type: nauc_map_at_3_max
      value: 35.2472
    - type: nauc_map_at_3_std
      value: -7.8861
    - type: nauc_map_at_3_diff1
      value: 49.2087
    - type: nauc_map_at_5_max
      value: 35.5165
    - type: nauc_map_at_5_std
      value: -7.8567
    - type: nauc_map_at_5_diff1
      value: 49.3185
    - type: nauc_map_at_10_max
      value: 36.2371
    - type: nauc_map_at_10_std
      value: -6.7322999999999995
    - type: nauc_map_at_10_diff1
      value: 49.3669
    - type: nauc_map_at_20_max
      value: 36.3245
    - type: nauc_map_at_20_std
      value: -6.2256
    - type: nauc_map_at_20_diff1
      value: 49.242999999999995
    - type: nauc_map_at_100_max
      value: 36.6375
    - type: nauc_map_at_100_std
      value: -5.694599999999999
    - type: nauc_map_at_100_diff1
      value: 49.1942
    - type: nauc_map_at_1000_max
      value: 36.6734
    - type: nauc_map_at_1000_std
      value: -5.6653
    - type: nauc_map_at_1000_diff1
      value: 49.1813
    - type: nauc_recall_at_1_max
      value: 32.8495
    - type: nauc_recall_at_1_std
      value: -11.1224
    - type: nauc_recall_at_1_diff1
      value: 52.8561
    - type: nauc_recall_at_3_max
      value: 33.2098
    - type: nauc_recall_at_3_std
      value: -7.4756
    - type: nauc_recall_at_3_diff1
      value: 44.6512
    - type: nauc_recall_at_5_max
      value: 32.0734
    - type: nauc_recall_at_5_std
      value: -8.552
    - type: nauc_recall_at_5_diff1
      value: 43.2098
    - type: nauc_recall_at_10_max
      value: 32.452999999999996
    - type: nauc_recall_at_10_std
      value: -5.631
    - type: nauc_recall_at_10_diff1
      value: 42.4641
    - type: nauc_recall_at_20_max
      value: 31.660300000000003
    - type: nauc_recall_at_20_std
      value: -1.5259
    - type: nauc_recall_at_20_diff1
      value: 40.5356
    - type: nauc_recall_at_100_max
      value: 40.3906
    - type: nauc_recall_at_100_std
      value: 22.5792
    - type: nauc_recall_at_100_diff1
      value: 36.2667
    - type: nauc_recall_at_1000_max
      value: 61.422399999999996
    - type: nauc_recall_at_1000_std
      value: 46.7038
    - type: nauc_recall_at_1000_diff1
      value: 36.4218
    - type: nauc_precision_at_1_max
      value: 39.321400000000004
    - type: nauc_precision_at_1_std
      value: -3.3204
    - type: nauc_precision_at_1_diff1
      value: 50.999300000000005
    - type: nauc_precision_at_3_max
      value: 35.7839
    - type: nauc_precision_at_3_std
      value: 7.773199999999999
    - type: nauc_precision_at_3_diff1
      value: 29.8081
    - type: nauc_precision_at_5_max
      value: 32.7723
    - type: nauc_precision_at_5_std
      value: 9.8457
    - type: nauc_precision_at_5_diff1
      value: 24.9104
    - type: nauc_precision_at_10_max
      value: 30.6076
    - type: nauc_precision_at_10_std
      value: 16.5018
    - type: nauc_precision_at_10_diff1
      value: 17.5733
    - type: nauc_precision_at_20_max
      value: 25.8982
    - type: nauc_precision_at_20_std
      value: 20.4936
    - type: nauc_precision_at_20_diff1
      value: 9.4253
    - type: nauc_precision_at_100_max
      value: 20.5147
    - type: nauc_precision_at_100_std
      value: 28.0537
    - type: nauc_precision_at_100_diff1
      value: -3.5682
    - type: nauc_precision_at_1000_max
      value: 8.9834
    - type: nauc_precision_at_1000_std
      value: 21.330099999999998
    - type: nauc_precision_at_1000_diff1
      value: -13.9467
    - type: nauc_mrr_at_1_max
      value: 39.321400000000004
    - type: nauc_mrr_at_1_std
      value: -3.3204
    - type: nauc_mrr_at_1_diff1
      value: 50.999300000000005
    - type: nauc_mrr_at_3_max
      value: 39.537099999999995
    - type: nauc_mrr_at_3_std
      value: -1.8964999999999999
    - type: nauc_mrr_at_3_diff1
      value: 48.790499999999994
    - type: nauc_mrr_at_5_max
      value: 39.5914
    - type: nauc_mrr_at_5_std
      value: -2.1046
    - type: nauc_mrr_at_5_diff1
      value: 48.674099999999996
    - type: nauc_mrr_at_10_max
      value: 39.4877
    - type: nauc_mrr_at_10_std
      value: -2.1155
    - type: nauc_mrr_at_10_diff1
      value: 48.5082
    - type: nauc_mrr_at_20_max
      value: 39.5837
    - type: nauc_mrr_at_20_std
      value: -1.8568999999999998
    - type: nauc_mrr_at_20_diff1
      value: 48.4835
    - type: nauc_mrr_at_100_max
      value: 39.6439
    - type: nauc_mrr_at_100_std
      value: -1.6681000000000001
    - type: nauc_mrr_at_100_diff1
      value: 48.4452
    - type: nauc_mrr_at_1000_max
      value: 39.6426
    - type: nauc_mrr_at_1000_std
      value: -1.6824
    - type: nauc_mrr_at_1000_diff1
      value: 48.4594
    - type: main_score
      value: 50.925
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: ndcg_at_1
      value: 38.812999999999995
    - type: ndcg_at_3
      value: 43.126999999999995
    - type: ndcg_at_5
      value: 45.269999999999996
    - type: ndcg_at_10
      value: 48.181000000000004
    - type: ndcg_at_20
      value: 50.475
    - type: ndcg_at_100
      value: 53.378
    - type: ndcg_at_1000
      value: 55.372
    - type: map_at_1
      value: 31.228
    - type: map_at_3
      value: 38.727000000000004
    - type: map_at_5
      value: 40.544000000000004
    - type: map_at_10
      value: 42.022999999999996
    - type: map_at_20
      value: 42.815
    - type: map_at_100
      value: 43.336000000000006
    - type: map_at_1000
      value: 43.434
    - type: recall_at_1
      value: 31.228
    - type: recall_at_3
      value: 46.075
    - type: recall_at_5
      value: 52.065
    - type: recall_at_10
      value: 60.86
    - type: recall_at_20
      value: 68.916
    - type: recall_at_100
      value: 82.49600000000001
    - type: recall_at_1000
      value: 95.914
    - type: precision_at_1
      value: 38.812999999999995
    - type: precision_at_3
      value: 20.51
    - type: precision_at_5
      value: 14.405999999999999
    - type: precision_at_10
      value: 8.676
    - type: precision_at_20
      value: 5.08
    - type: precision_at_100
      value: 1.3
    - type: precision_at_1000
      value: 0.165
    - type: mrr_at_1
      value: 38.812799999999996
    - type: mrr_at_3
      value: 45.3957
    - type: mrr_at_5
      value: 46.8113
    - type: mrr_at_10
      value: 47.9132
    - type: mrr_at_20
      value: 48.4148
    - type: mrr_at_100
      value: 48.694900000000004
    - type: mrr_at_1000
      value: 48.74
    - type: nauc_ndcg_at_1_max
      value: 46.951100000000004
    - type: nauc_ndcg_at_1_std
      value: 4.750299999999999
    - type: nauc_ndcg_at_1_diff1
      value: 50.353300000000004
    - type: nauc_ndcg_at_3_max
      value: 44.852
    - type: nauc_ndcg_at_3_std
      value: 5.976
    - type: nauc_ndcg_at_3_diff1
      value: 44.8003
    - type: nauc_ndcg_at_5_max
      value: 44.7999
    - type: nauc_ndcg_at_5_std
      value: 7.138799999999999
    - type: nauc_ndcg_at_5_diff1
      value: 43.786
    - type: nauc_ndcg_at_10_max
      value: 45.272800000000004
    - type: nauc_ndcg_at_10_std
      value: 8.318200000000001
    - type: nauc_ndcg_at_10_diff1
      value: 43.5412
    - type: nauc_ndcg_at_20_max
      value: 45.9439
    - type: nauc_ndcg_at_20_std
      value: 9.5894
    - type: nauc_ndcg_at_20_diff1
      value: 43.635400000000004
    - type: nauc_ndcg_at_100_max
      value: 46.555800000000005
    - type: nauc_ndcg_at_100_std
      value: 11.4897
    - type: nauc_ndcg_at_100_diff1
      value: 43.2953
    - type: nauc_ndcg_at_1000_max
      value: 46.4671
    - type: nauc_ndcg_at_1000_std
      value: 10.198500000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 43.9655
    - type: nauc_map_at_1_max
      value: 41.2881
    - type: nauc_map_at_1_std
      value: -1.7105
    - type: nauc_map_at_1_diff1
      value: 52.340900000000005
    - type: nauc_map_at_3_max
      value: 43.2779
    - type: nauc_map_at_3_std
      value: 3.1361
    - type: nauc_map_at_3_diff1
      value: 46.899499999999996
    - type: nauc_map_at_5_max
      value: 44.034600000000005
    - type: nauc_map_at_5_std
      value: 4.376
    - type: nauc_map_at_5_diff1
      value: 46.1768
    - type: nauc_map_at_10_max
      value: 44.495200000000004
    - type: nauc_map_at_10_std
      value: 5.1069
    - type: nauc_map_at_10_diff1
      value: 45.8036
    - type: nauc_map_at_20_max
      value: 44.9796
    - type: nauc_map_at_20_std
      value: 5.6501
    - type: nauc_map_at_20_diff1
      value: 45.8538
    - type: nauc_map_at_100_max
      value: 45.178000000000004
    - type: nauc_map_at_100_std
      value: 6.1053999999999995
    - type: nauc_map_at_100_diff1
      value: 45.7785
    - type: nauc_map_at_1000_max
      value: 45.169599999999996
    - type: nauc_map_at_1000_std
      value: 6.0758
    - type: nauc_map_at_1000_diff1
      value: 45.794200000000004
    - type: nauc_recall_at_1_max
      value: 41.2881
    - type: nauc_recall_at_1_std
      value: -1.7105
    - type: nauc_recall_at_1_diff1
      value: 52.340900000000005
    - type: nauc_recall_at_3_max
      value: 40.213100000000004
    - type: nauc_recall_at_3_std
      value: 5.0584
    - type: nauc_recall_at_3_diff1
      value: 39.8885
    - type: nauc_recall_at_5_max
      value: 40.629799999999996
    - type: nauc_recall_at_5_std
      value: 9.2891
    - type: nauc_recall_at_5_diff1
      value: 36.7529
    - type: nauc_recall_at_10_max
      value: 41.1258
    - type: nauc_recall_at_10_std
      value: 14.056
    - type: nauc_recall_at_10_diff1
      value: 34.416000000000004
    - type: nauc_recall_at_20_max
      value: 42.2647
    - type: nauc_recall_at_20_std
      value: 19.0659
    - type: nauc_recall_at_20_diff1
      value: 33.9025
    - type: nauc_recall_at_100_max
      value: 45.4518
    - type: nauc_recall_at_100_std
      value: 38.2567
    - type: nauc_recall_at_100_diff1
      value: 27.418300000000002
    - type: nauc_recall_at_1000_max
      value: 52.1153
    - type: nauc_recall_at_1000_std
      value: 54.8108
    - type: nauc_recall_at_1000_diff1
      value: 28.122200000000003
    - type: nauc_precision_at_1_max
      value: 46.951100000000004
    - type: nauc_precision_at_1_std
      value: 4.750299999999999
    - type: nauc_precision_at_1_diff1
      value: 50.353300000000004
    - type: nauc_precision_at_3_max
      value: 43.3769
    - type: nauc_precision_at_3_std
      value: 15.2362
    - type: nauc_precision_at_3_diff1
      value: 29.4925
    - type: nauc_precision_at_5_max
      value: 40.0531
    - type: nauc_precision_at_5_std
      value: 18.0719
    - type: nauc_precision_at_5_diff1
      value: 21.4607
    - type: nauc_precision_at_10_max
      value: 34.558
    - type: nauc_precision_at_10_std
      value: 20.2349
    - type: nauc_precision_at_10_diff1
      value: 13.0483
    - type: nauc_precision_at_20_max
      value: 30.3112
    - type: nauc_precision_at_20_std
      value: 23.7865
    - type: nauc_precision_at_20_diff1
      value: 6.678000000000001
    - type: nauc_precision_at_100_max
      value: 15.782599999999999
    - type: nauc_precision_at_100_std
      value: 23.3508
    - type: nauc_precision_at_100_diff1
      value: -5.356199999999999
    - type: nauc_precision_at_1000_max
      value: -1.203
    - type: nauc_precision_at_1000_std
      value: 9.2771
    - type: nauc_precision_at_1000_diff1
      value: -12.0167
    - type: nauc_mrr_at_1_max
      value: 46.951100000000004
    - type: nauc_mrr_at_1_std
      value: 4.750299999999999
    - type: nauc_mrr_at_1_diff1
      value: 50.353300000000004
    - type: nauc_mrr_at_3_max
      value: 47.1661
    - type: nauc_mrr_at_3_std
      value: 7.985
    - type: nauc_mrr_at_3_diff1
      value: 45.5407
    - type: nauc_mrr_at_5_max
      value: 46.7954
    - type: nauc_mrr_at_5_std
      value: 8.615200000000002
    - type: nauc_mrr_at_5_diff1
      value: 44.767
    - type: nauc_mrr_at_10_max
      value: 46.874500000000005
    - type: nauc_mrr_at_10_std
      value: 8.9973
    - type: nauc_mrr_at_10_diff1
      value: 44.7807
    - type: nauc_mrr_at_20_max
      value: 46.8582
    - type: nauc_mrr_at_20_std
      value: 9.1312
    - type: nauc_mrr_at_20_diff1
      value: 44.7926
    - type: nauc_mrr_at_100_max
      value: 46.9119
    - type: nauc_mrr_at_100_std
      value: 9.2225
    - type: nauc_mrr_at_100_diff1
      value: 44.7972
    - type: nauc_mrr_at_1000_max
      value: 46.9139
    - type: nauc_mrr_at_1000_std
      value: 9.1867
    - type: nauc_mrr_at_1000_diff1
      value: 44.8208
    - type: main_score
      value: 48.181000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 47.198
    - type: ndcg_at_10
      value: 47.198
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: ndcg_at_1
      value: 32.515
    - type: ndcg_at_3
      value: 36.754999999999995
    - type: ndcg_at_5
      value: 38.461
    - type: ndcg_at_10
      value: 41.113
    - type: ndcg_at_20
      value: 42.744
    - type: ndcg_at_100
      value: 45.607
    - type: ndcg_at_1000
      value: 47.769
    - type: map_at_1
      value: 28.877999999999997
    - type: map_at_3
      value: 34.111000000000004
    - type: map_at_5
      value: 35.296
    - type: map_at_10
      value: 36.516
    - type: map_at_20
      value: 37.031
    - type: map_at_100
      value: 37.455
    - type: map_at_1000
      value: 37.54
    - type: recall_at_1
      value: 28.877999999999997
    - type: recall_at_3
      value: 39.823
    - type: recall_at_5
      value: 44.074000000000005
    - type: recall_at_10
      value: 52.138
    - type: recall_at_20
      value: 58.268
    - type: recall_at_100
      value: 72.675
    - type: recall_at_1000
      value: 88.49900000000001
    - type: precision_at_1
      value: 32.515
    - type: precision_at_3
      value: 15.491
    - type: precision_at_5
      value: 10.613
    - type: precision_at_10
      value: 6.411
    - type: precision_at_20
      value: 3.604
    - type: precision_at_100
      value: 0.9390000000000001
    - type: precision_at_1000
      value: 0.121
    - type: mrr_at_1
      value: 32.5153
    - type: mrr_at_3
      value: 37.5256
    - type: mrr_at_5
      value: 38.507200000000005
    - type: mrr_at_10
      value: 39.6489
    - type: mrr_at_20
      value: 40.0734
    - type: mrr_at_100
      value: 40.408899999999996
    - type: mrr_at_1000
      value: 40.470600000000005
    - type: nauc_ndcg_at_1_max
      value: 46.9541
    - type: nauc_ndcg_at_1_std
      value: -0.6345
    - type: nauc_ndcg_at_1_diff1
      value: 56.4747
    - type: nauc_ndcg_at_3_max
      value: 44.595600000000005
    - type: nauc_ndcg_at_3_std
      value: -0.6883
    - type: nauc_ndcg_at_3_diff1
      value: 51.176100000000005
    - type: nauc_ndcg_at_5_max
      value: 45.0672
    - type: nauc_ndcg_at_5_std
      value: 0.7248
    - type: nauc_ndcg_at_5_diff1
      value: 50.6661
    - type: nauc_ndcg_at_10_max
      value: 45.3702
    - type: nauc_ndcg_at_10_std
      value: 3.7225
    - type: nauc_ndcg_at_10_diff1
      value: 48.5914
    - type: nauc_ndcg_at_20_max
      value: 45.134800000000006
    - type: nauc_ndcg_at_20_std
      value: 3.4250999999999996
    - type: nauc_ndcg_at_20_diff1
      value: 48.0876
    - type: nauc_ndcg_at_100_max
      value: 45.848
    - type: nauc_ndcg_at_100_std
      value: 5.0007
    - type: nauc_ndcg_at_100_diff1
      value: 48.4221
    - type: nauc_ndcg_at_1000_max
      value: 46.0472
    - type: nauc_ndcg_at_1000_std
      value: 4.8727
    - type: nauc_ndcg_at_1000_diff1
      value: 48.7787
    - type: nauc_map_at_1_max
      value: 44.2723
    - type: nauc_map_at_1_std
      value: -4.1624
    - type: nauc_map_at_1_diff1
      value: 56.3666
    - type: nauc_map_at_3_max
      value: 44.368
    - type: nauc_map_at_3_std
      value: -2.2338
    - type: nauc_map_at_3_diff1
      value: 52.662299999999995
    - type: nauc_map_at_5_max
      value: 44.9376
    - type: nauc_map_at_5_std
      value: -0.9258000000000001
    - type: nauc_map_at_5_diff1
      value: 52.2675
    - type: nauc_map_at_10_max
      value: 45.162600000000005
    - type: nauc_map_at_10_std
      value: 0.5709
    - type: nauc_map_at_10_diff1
      value: 51.2702
    - type: nauc_map_at_20_max
      value: 45.088899999999995
    - type: nauc_map_at_20_std
      value: 0.5163
    - type: nauc_map_at_20_diff1
      value: 51.1058
    - type: nauc_map_at_100_max
      value: 45.203700000000005
    - type: nauc_map_at_100_std
      value: 0.7443
    - type: nauc_map_at_100_diff1
      value: 51.1744
    - type: nauc_map_at_1000_max
      value: 45.2121
    - type: nauc_map_at_1000_std
      value: 0.7443
    - type: nauc_map_at_1000_diff1
      value: 51.186699999999995
    - type: nauc_recall_at_1_max
      value: 44.2723
    - type: nauc_recall_at_1_std
      value: -4.1624
    - type: nauc_recall_at_1_diff1
      value: 56.3666
    - type: nauc_recall_at_3_max
      value: 41.484700000000004
    - type: nauc_recall_at_3_std
      value: -1.5438
    - type: nauc_recall_at_3_diff1
      value: 47.3155
    - type: nauc_recall_at_5_max
      value: 42.7926
    - type: nauc_recall_at_5_std
      value: 2.2485999999999997
    - type: nauc_recall_at_5_diff1
      value: 45.7287
    - type: nauc_recall_at_10_max
      value: 43.3757
    - type: nauc_recall_at_10_std
      value: 11.1774
    - type: nauc_recall_at_10_diff1
      value: 38.699
    - type: nauc_recall_at_20_max
      value: 41.9806
    - type: nauc_recall_at_20_std
      value: 9.8464
    - type: nauc_recall_at_20_diff1
      value: 36.209599999999995
    - type: nauc_recall_at_100_max
      value: 44.935399999999994
    - type: nauc_recall_at_100_std
      value: 22.2528
    - type: nauc_recall_at_100_diff1
      value: 33.9811
    - type: nauc_recall_at_1000_max
      value: 48.0178
    - type: nauc_recall_at_1000_std
      value: 35.6656
    - type: nauc_recall_at_1000_diff1
      value: 27.0609
    - type: nauc_precision_at_1_max
      value: 46.9541
    - type: nauc_precision_at_1_std
      value: -0.6345
    - type: nauc_precision_at_1_diff1
      value: 56.4747
    - type: nauc_precision_at_3_max
      value: 44.8235
    - type: nauc_precision_at_3_std
      value: 6.392399999999999
    - type: nauc_precision_at_3_diff1
      value: 43.4139
    - type: nauc_precision_at_5_max
      value: 44.1627
    - type: nauc_precision_at_5_std
      value: 12.5801
    - type: nauc_precision_at_5_diff1
      value: 38.3975
    - type: nauc_precision_at_10_max
      value: 42.2932
    - type: nauc_precision_at_10_std
      value: 21.9445
    - type: nauc_precision_at_10_diff1
      value: 28.898200000000003
    - type: nauc_precision_at_20_max
      value: 38.3815
    - type: nauc_precision_at_20_std
      value: 21.2644
    - type: nauc_precision_at_20_diff1
      value: 22.902900000000002
    - type: nauc_precision_at_100_max
      value: 30.0629
    - type: nauc_precision_at_100_std
      value: 25.7938
    - type: nauc_precision_at_100_diff1
      value: 13.500599999999999
    - type: nauc_precision_at_1000_max
      value: 16.1509
    - type: nauc_precision_at_1000_std
      value: 22.168599999999998
    - type: nauc_precision_at_1000_diff1
      value: -0.5865
    - type: nauc_mrr_at_1_max
      value: 46.9541
    - type: nauc_mrr_at_1_std
      value: -0.6345
    - type: nauc_mrr_at_1_diff1
      value: 56.4747
    - type: nauc_mrr_at_3_max
      value: 45.571
    - type: nauc_mrr_at_3_std
      value: 0.5652
    - type: nauc_mrr_at_3_diff1
      value: 52.2878
    - type: nauc_mrr_at_5_max
      value: 45.9243
    - type: nauc_mrr_at_5_std
      value: 1.4102
    - type: nauc_mrr_at_5_diff1
      value: 52.0197
    - type: nauc_mrr_at_10_max
      value: 46.090599999999995
    - type: nauc_mrr_at_10_std
      value: 2.5422000000000002
    - type: nauc_mrr_at_10_diff1
      value: 51.1523
    - type: nauc_mrr_at_20_max
      value: 46.0581
    - type: nauc_mrr_at_20_std
      value: 2.4245
    - type: nauc_mrr_at_20_diff1
      value: 51.1149
    - type: nauc_mrr_at_100_max
      value: 46.138200000000005
    - type: nauc_mrr_at_100_std
      value: 2.5852
    - type: nauc_mrr_at_100_diff1
      value: 51.19200000000001
    - type: nauc_mrr_at_1000_max
      value: 46.134
    - type: nauc_mrr_at_1000_std
      value: 2.5724
    - type: nauc_mrr_at_1000_diff1
      value: 51.20099999999999
    - type: main_score
      value: 41.113
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: ndcg_at_1
      value: 26.358999999999998
    - type: ndcg_at_3
      value: 30.921
    - type: ndcg_at_5
      value: 33.083
    - type: ndcg_at_10
      value: 35.669000000000004
    - type: ndcg_at_20
      value: 37.486999999999995
    - type: ndcg_at_100
      value: 40.897
    - type: ndcg_at_1000
      value: 43.492999999999995
    - type: map_at_1
      value: 21.644
    - type: map_at_3
      value: 27.638
    - type: map_at_5
      value: 29.181
    - type: map_at_10
      value: 30.429000000000002
    - type: map_at_20
      value: 31.018
    - type: map_at_100
      value: 31.557000000000002
    - type: map_at_1000
      value: 31.676
    - type: recall_at_1
      value: 21.644
    - type: recall_at_3
      value: 33.727000000000004
    - type: recall_at_5
      value: 39.402
    - type: recall_at_10
      value: 47.166000000000004
    - type: recall_at_20
      value: 53.818
    - type: recall_at_100
      value: 70.625
    - type: recall_at_1000
      value: 88.848
    - type: precision_at_1
      value: 26.358999999999998
    - type: precision_at_3
      value: 14.602
    - type: precision_at_5
      value: 10.509
    - type: precision_at_10
      value: 6.468999999999999
    - type: precision_at_20
      value: 3.7969999999999997
    - type: precision_at_100
      value: 1.0619999999999998
    - type: precision_at_1000
      value: 0.147
    - type: mrr_at_1
      value: 26.3593
    - type: mrr_at_3
      value: 32.2379
    - type: mrr_at_5
      value: 33.5559
    - type: mrr_at_10
      value: 34.6105
    - type: mrr_at_20
      value: 35.0733
    - type: mrr_at_100
      value: 35.4832
    - type: mrr_at_1000
      value: 35.5508
    - type: nauc_ndcg_at_1_max
      value: 38.821
    - type: nauc_ndcg_at_1_std
      value: -0.9577
    - type: nauc_ndcg_at_1_diff1
      value: 49.477900000000005
    - type: nauc_ndcg_at_3_max
      value: 36.9651
    - type: nauc_ndcg_at_3_std
      value: 0.5652
    - type: nauc_ndcg_at_3_diff1
      value: 42.9649
    - type: nauc_ndcg_at_5_max
      value: 36.9433
    - type: nauc_ndcg_at_5_std
      value: 1.4069
    - type: nauc_ndcg_at_5_diff1
      value: 41.3321
    - type: nauc_ndcg_at_10_max
      value: 37.0556
    - type: nauc_ndcg_at_10_std
      value: 1.983
    - type: nauc_ndcg_at_10_diff1
      value: 40.6062
    - type: nauc_ndcg_at_20_max
      value: 37.621
    - type: nauc_ndcg_at_20_std
      value: 3.1833
    - type: nauc_ndcg_at_20_diff1
      value: 40.0768
    - type: nauc_ndcg_at_100_max
      value: 37.5859
    - type: nauc_ndcg_at_100_std
      value: 4.4883
    - type: nauc_ndcg_at_100_diff1
      value: 39.6131
    - type: nauc_ndcg_at_1000_max
      value: 37.9037
    - type: nauc_ndcg_at_1000_std
      value: 4.3155
    - type: nauc_ndcg_at_1000_diff1
      value: 40.393
    - type: nauc_map_at_1_max
      value: 34.2335
    - type: nauc_map_at_1_std
      value: -2.5663
    - type: nauc_map_at_1_diff1
      value: 49.3827
    - type: nauc_map_at_3_max
      value: 35.1539
    - type: nauc_map_at_3_std
      value: -0.4655
    - type: nauc_map_at_3_diff1
      value: 44.0299
    - type: nauc_map_at_5_max
      value: 35.546499999999995
    - type: nauc_map_at_5_std
      value: -0.0021
    - type: nauc_map_at_5_diff1
      value: 43.0138
    - type: nauc_map_at_10_max
      value: 35.904799999999994
    - type: nauc_map_at_10_std
      value: 0.367
    - type: nauc_map_at_10_diff1
      value: 42.762699999999995
    - type: nauc_map_at_20_max
      value: 36.1855
    - type: nauc_map_at_20_std
      value: 0.7818
    - type: nauc_map_at_20_diff1
      value: 42.6084
    - type: nauc_map_at_100_max
      value: 36.2406
    - type: nauc_map_at_100_std
      value: 0.9825999999999999
    - type: nauc_map_at_100_diff1
      value: 42.5375
    - type: nauc_map_at_1000_max
      value: 36.2732
    - type: nauc_map_at_1000_std
      value: 0.9912000000000001
    - type: nauc_map_at_1000_diff1
      value: 42.5821
    - type: nauc_recall_at_1_max
      value: 34.2335
    - type: nauc_recall_at_1_std
      value: -2.5663
    - type: nauc_recall_at_1_diff1
      value: 49.3827
    - type: nauc_recall_at_3_max
      value: 34.2402
    - type: nauc_recall_at_3_std
      value: 1.3011
    - type: nauc_recall_at_3_diff1
      value: 38.5403
    - type: nauc_recall_at_5_max
      value: 34.2169
    - type: nauc_recall_at_5_std
      value: 3.0383
    - type: nauc_recall_at_5_diff1
      value: 34.3078
    - type: nauc_recall_at_10_max
      value: 34.2267
    - type: nauc_recall_at_10_std
      value: 4.7303
    - type: nauc_recall_at_10_diff1
      value: 31.2869
    - type: nauc_recall_at_20_max
      value: 35.6281
    - type: nauc_recall_at_20_std
      value: 8.940199999999999
    - type: nauc_recall_at_20_diff1
      value: 28.655599999999996
    - type: nauc_recall_at_100_max
      value: 34.0961
    - type: nauc_recall_at_100_std
      value: 18.096799999999998
    - type: nauc_recall_at_100_diff1
      value: 22.490199999999998
    - type: nauc_recall_at_1000_max
      value: 37.3724
    - type: nauc_recall_at_1000_std
      value: 29.723699999999997
    - type: nauc_recall_at_1000_diff1
      value: 18.9603
    - type: nauc_precision_at_1_max
      value: 38.821
    - type: nauc_precision_at_1_std
      value: -0.9577
    - type: nauc_precision_at_1_diff1
      value: 49.477900000000005
    - type: nauc_precision_at_3_max
      value: 38.9589
    - type: nauc_precision_at_3_std
      value: 3.6894000000000005
    - type: nauc_precision_at_3_diff1
      value: 34.869499999999995
    - type: nauc_precision_at_5_max
      value: 37.9132
    - type: nauc_precision_at_5_std
      value: 6.1095
    - type: nauc_precision_at_5_diff1
      value: 28.7686
    - type: nauc_precision_at_10_max
      value: 35.5564
    - type: nauc_precision_at_10_std
      value: 7.4825
    - type: nauc_precision_at_10_diff1
      value: 24.0663
    - type: nauc_precision_at_20_max
      value: 34.3717
    - type: nauc_precision_at_20_std
      value: 10.989
    - type: nauc_precision_at_20_diff1
      value: 19.0117
    - type: nauc_precision_at_100_max
      value: 25.595000000000002
    - type: nauc_precision_at_100_std
      value: 13.692499999999999
    - type: nauc_precision_at_100_diff1
      value: 9.7287
    - type: nauc_precision_at_1000_max
      value: 15.6194
    - type: nauc_precision_at_1000_std
      value: 7.9235
    - type: nauc_precision_at_1000_diff1
      value: 3.5067
    - type: nauc_mrr_at_1_max
      value: 38.821
    - type: nauc_mrr_at_1_std
      value: -0.9577
    - type: nauc_mrr_at_1_diff1
      value: 49.477900000000005
    - type: nauc_mrr_at_3_max
      value: 39.365899999999996
    - type: nauc_mrr_at_3_std
      value: 0.8999999999999999
    - type: nauc_mrr_at_3_diff1
      value: 44.8801
    - type: nauc_mrr_at_5_max
      value: 39.339400000000005
    - type: nauc_mrr_at_5_std
      value: 1.6056000000000001
    - type: nauc_mrr_at_5_diff1
      value: 43.9725
    - type: nauc_mrr_at_10_max
      value: 39.245200000000004
    - type: nauc_mrr_at_10_std
      value: 1.6921
    - type: nauc_mrr_at_10_diff1
      value: 43.6805
    - type: nauc_mrr_at_20_max
      value: 39.283699999999996
    - type: nauc_mrr_at_20_std
      value: 1.9199000000000002
    - type: nauc_mrr_at_20_diff1
      value: 43.5636
    - type: nauc_mrr_at_100_max
      value: 39.293299999999995
    - type: nauc_mrr_at_100_std
      value: 2.0535
    - type: nauc_mrr_at_100_diff1
      value: 43.5431
    - type: nauc_mrr_at_1000_max
      value: 39.299299999999995
    - type: nauc_mrr_at_1000_std
      value: 2.0467
    - type: nauc_mrr_at_1000_diff1
      value: 43.5649
    - type: main_score
      value: 35.669000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: ndcg_at_1
      value: 37.407000000000004
    - type: ndcg_at_3
      value: 43.179
    - type: ndcg_at_5
      value: 45.540000000000006
    - type: ndcg_at_10
      value: 48.189
    - type: ndcg_at_20
      value: 50.308
    - type: ndcg_at_100
      value: 53.15800000000001
    - type: ndcg_at_1000
      value: 55.108999999999995
    - type: map_at_1
      value: 32.314
    - type: map_at_3
      value: 39.757
    - type: map_at_5
      value: 41.448
    - type: map_at_10
      value: 42.742999999999995
    - type: map_at_20
      value: 43.438
    - type: map_at_100
      value: 43.909
    - type: map_at_1000
      value: 44.005
    - type: recall_at_1
      value: 32.314
    - type: recall_at_3
      value: 46.852
    - type: recall_at_5
      value: 53.15
    - type: recall_at_10
      value: 60.748000000000005
    - type: recall_at_20
      value: 68.30199999999999
    - type: recall_at_100
      value: 81.846
    - type: recall_at_1000
      value: 94.92399999999999
    - type: precision_at_1
      value: 37.407000000000004
    - type: precision_at_3
      value: 19.59
    - type: precision_at_5
      value: 13.544999999999998
    - type: precision_at_10
      value: 8.013
    - type: precision_at_20
      value: 4.627
    - type: precision_at_100
      value: 1.172
    - type: precision_at_1000
      value: 0.14400000000000002
    - type: mrr_at_1
      value: 37.4067
    - type: mrr_at_3
      value: 43.9832
    - type: mrr_at_5
      value: 45.4291
    - type: mrr_at_10
      value: 46.4308
    - type: mrr_at_20
      value: 46.9435
    - type: mrr_at_100
      value: 47.2549
    - type: mrr_at_1000
      value: 47.3064
    - type: nauc_ndcg_at_1_max
      value: 49.5683
    - type: nauc_ndcg_at_1_std
      value: -4.5333
    - type: nauc_ndcg_at_1_diff1
      value: 59.0792
    - type: nauc_ndcg_at_3_max
      value: 46.881
    - type: nauc_ndcg_at_3_std
      value: -1.9335000000000002
    - type: nauc_ndcg_at_3_diff1
      value: 50.6091
    - type: nauc_ndcg_at_5_max
      value: 46.596399999999996
    - type: nauc_ndcg_at_5_std
      value: -1.6747
    - type: nauc_ndcg_at_5_diff1
      value: 50.731
    - type: nauc_ndcg_at_10_max
      value: 47.119699999999995
    - type: nauc_ndcg_at_10_std
      value: -1.8790999999999998
    - type: nauc_ndcg_at_10_diff1
      value: 50.4398
    - type: nauc_ndcg_at_20_max
      value: 46.931400000000004
    - type: nauc_ndcg_at_20_std
      value: -1.2184
    - type: nauc_ndcg_at_20_diff1
      value: 50.2302
    - type: nauc_ndcg_at_100_max
      value: 47.4715
    - type: nauc_ndcg_at_100_std
      value: 0.512
    - type: nauc_ndcg_at_100_diff1
      value: 49.831399999999995
    - type: nauc_ndcg_at_1000_max
      value: 47.4049
    - type: nauc_ndcg_at_1000_std
      value: -0.07730000000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 50.045399999999994
    - type: nauc_map_at_1_max
      value: 46.3138
    - type: nauc_map_at_1_std
      value: -6.1365
    - type: nauc_map_at_1_diff1
      value: 59.1901
    - type: nauc_map_at_3_max
      value: 46.4225
    - type: nauc_map_at_3_std
      value: -3.3928
    - type: nauc_map_at_3_diff1
      value: 53.0394
    - type: nauc_map_at_5_max
      value: 46.634
    - type: nauc_map_at_5_std
      value: -2.8697
    - type: nauc_map_at_5_diff1
      value: 52.837500000000006
    - type: nauc_map_at_10_max
      value: 46.9634
    - type: nauc_map_at_10_std
      value: -2.8736
    - type: nauc_map_at_10_diff1
      value: 52.62670000000001
    - type: nauc_map_at_20_max
      value: 46.943
    - type: nauc_map_at_20_std
      value: -2.7709
    - type: nauc_map_at_20_diff1
      value: 52.525299999999994
    - type: nauc_map_at_100_max
      value: 47.072
    - type: nauc_map_at_100_std
      value: -2.4186
    - type: nauc_map_at_100_diff1
      value: 52.4223
    - type: nauc_map_at_1000_max
      value: 47.058299999999996
    - type: nauc_map_at_1000_std
      value: -2.4274
    - type: nauc_map_at_1000_diff1
      value: 52.410000000000004
    - type: nauc_recall_at_1_max
      value: 46.3138
    - type: nauc_recall_at_1_std
      value: -6.1365
    - type: nauc_recall_at_1_diff1
      value: 59.1901
    - type: nauc_recall_at_3_max
      value: 43.556
    - type: nauc_recall_at_3_std
      value: -1.0473
    - type: nauc_recall_at_3_diff1
      value: 45.3836
    - type: nauc_recall_at_5_max
      value: 42.8197
    - type: nauc_recall_at_5_std
      value: 0.364
    - type: nauc_recall_at_5_diff1
      value: 44.0828
    - type: nauc_recall_at_10_max
      value: 43.5287
    - type: nauc_recall_at_10_std
      value: -0.16999999999999998
    - type: nauc_recall_at_10_diff1
      value: 42.2532
    - type: nauc_recall_at_20_max
      value: 41.9415
    - type: nauc_recall_at_20_std
      value: 3.0739
    - type: nauc_recall_at_20_diff1
      value: 40.6138
    - type: nauc_recall_at_100_max
      value: 43.648199999999996
    - type: nauc_recall_at_100_std
      value: 17.8151
    - type: nauc_recall_at_100_diff1
      value: 34.7435
    - type: nauc_recall_at_1000_max
      value: 42.9288
    - type: nauc_recall_at_1000_std
      value: 34.9874
    - type: nauc_recall_at_1000_diff1
      value: 21.8361
    - type: nauc_precision_at_1_max
      value: 49.5683
    - type: nauc_precision_at_1_std
      value: -4.5333
    - type: nauc_precision_at_1_diff1
      value: 59.0792
    - type: nauc_precision_at_3_max
      value: 40.726
    - type: nauc_precision_at_3_std
      value: 3.6327
    - type: nauc_precision_at_3_diff1
      value: 32.726
    - type: nauc_precision_at_5_max
      value: 37.575599999999994
    - type: nauc_precision_at_5_std
      value: 5.4281999999999995
    - type: nauc_precision_at_5_diff1
      value: 26.8851
    - type: nauc_precision_at_10_max
      value: 31.7382
    - type: nauc_precision_at_10_std
      value: 4.0767999999999995
    - type: nauc_precision_at_10_diff1
      value: 18.174799999999998
    - type: nauc_precision_at_20_max
      value: 25.4159
    - type: nauc_precision_at_20_std
      value: 6.0251
    - type: nauc_precision_at_20_diff1
      value: 10.059800000000001
    - type: nauc_precision_at_100_max
      value: 13.5296
    - type: nauc_precision_at_100_std
      value: 14.0608
    - type: nauc_precision_at_100_diff1
      value: -7.792000000000001
    - type: nauc_precision_at_1000_max
      value: -3.7522
    - type: nauc_precision_at_1000_std
      value: 7.536099999999999
    - type: nauc_precision_at_1000_diff1
      value: -21.2683
    - type: nauc_mrr_at_1_max
      value: 49.5683
    - type: nauc_mrr_at_1_std
      value: -4.5333
    - type: nauc_mrr_at_1_diff1
      value: 59.0792
    - type: nauc_mrr_at_3_max
      value: 48.3581
    - type: nauc_mrr_at_3_std
      value: -1.8857
    - type: nauc_mrr_at_3_diff1
      value: 52.5945
    - type: nauc_mrr_at_5_max
      value: 48.2651
    - type: nauc_mrr_at_5_std
      value: -1.5519
    - type: nauc_mrr_at_5_diff1
      value: 52.323699999999995
    - type: nauc_mrr_at_10_max
      value: 48.346000000000004
    - type: nauc_mrr_at_10_std
      value: -1.7543
    - type: nauc_mrr_at_10_diff1
      value: 52.278999999999996
    - type: nauc_mrr_at_20_max
      value: 48.2692
    - type: nauc_mrr_at_20_std
      value: -1.5904000000000003
    - type: nauc_mrr_at_20_diff1
      value: 52.27460000000001
    - type: nauc_mrr_at_100_max
      value: 48.273700000000005
    - type: nauc_mrr_at_100_std
      value: -1.4659
    - type: nauc_mrr_at_100_diff1
      value: 52.278400000000005
    - type: nauc_mrr_at_1000_max
      value: 48.2811
    - type: nauc_mrr_at_1000_std
      value: -1.4881
    - type: nauc_mrr_at_1000_diff1
      value: 52.298500000000004
    - type: main_score
      value: 48.189
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: ndcg_at_1
      value: 38.141999999999996
    - type: ndcg_at_3
      value: 42.689
    - type: ndcg_at_5
      value: 44.318999999999996
    - type: ndcg_at_10
      value: 47.303
    - type: ndcg_at_20
      value: 49.236000000000004
    - type: ndcg_at_100
      value: 53.09700000000001
    - type: ndcg_at_1000
      value: 55.117000000000004
    - type: map_at_1
      value: 32.468
    - type: map_at_3
      value: 38.573
    - type: map_at_5
      value: 39.926
    - type: map_at_10
      value: 41.482
    - type: map_at_20
      value: 42.370000000000005
    - type: map_at_100
      value: 43.204
    - type: map_at_1000
      value: 43.425999999999995
    - type: recall_at_1
      value: 32.468
    - type: recall_at_3
      value: 44.241
    - type: recall_at_5
      value: 49.177
    - type: recall_at_10
      value: 57.63399999999999
    - type: recall_at_20
      value: 64.724
    - type: recall_at_100
      value: 83.817
    - type: recall_at_1000
      value: 95.91
    - type: precision_at_1
      value: 38.141999999999996
    - type: precision_at_3
      value: 19.499
    - type: precision_at_5
      value: 13.478000000000002
    - type: precision_at_10
      value: 8.774999999999999
    - type: precision_at_20
      value: 5.455
    - type: precision_at_100
      value: 1.6760000000000002
    - type: precision_at_1000
      value: 0.251
    - type: mrr_at_1
      value: 38.1423
    - type: mrr_at_3
      value: 44.005300000000005
    - type: mrr_at_5
      value: 45.1515
    - type: mrr_at_10
      value: 46.3542
    - type: mrr_at_20
      value: 46.7589
    - type: mrr_at_100
      value: 47.185100000000006
    - type: mrr_at_1000
      value: 47.2249
    - type: nauc_ndcg_at_1_max
      value: 47.905300000000004
    - type: nauc_ndcg_at_1_std
      value: 7.8307
    - type: nauc_ndcg_at_1_diff1
      value: 51.3311
    - type: nauc_ndcg_at_3_max
      value: 46.8119
    - type: nauc_ndcg_at_3_std
      value: 6.993099999999999
    - type: nauc_ndcg_at_3_diff1
      value: 48.3281
    - type: nauc_ndcg_at_5_max
      value: 47.5687
    - type: nauc_ndcg_at_5_std
      value: 8.7295
    - type: nauc_ndcg_at_5_diff1
      value: 49.106300000000005
    - type: nauc_ndcg_at_10_max
      value: 47.3786
    - type: nauc_ndcg_at_10_std
      value: 8.9795
    - type: nauc_ndcg_at_10_diff1
      value: 47.5348
    - type: nauc_ndcg_at_20_max
      value: 47.9792
    - type: nauc_ndcg_at_20_std
      value: 10.2734
    - type: nauc_ndcg_at_20_diff1
      value: 48.3578
    - type: nauc_ndcg_at_100_max
      value: 48.5313
    - type: nauc_ndcg_at_100_std
      value: 11.2393
    - type: nauc_ndcg_at_100_diff1
      value: 47.497299999999996
    - type: nauc_ndcg_at_1000_max
      value: 48.4189
    - type: nauc_ndcg_at_1000_std
      value: 10.857700000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 47.9808
    - type: nauc_map_at_1_max
      value: 45.0797
    - type: nauc_map_at_1_std
      value: 1.9601
    - type: nauc_map_at_1_diff1
      value: 55.33050000000001
    - type: nauc_map_at_3_max
      value: 46.6641
    - type: nauc_map_at_3_std
      value: 3.9848000000000003
    - type: nauc_map_at_3_diff1
      value: 51.4752
    - type: nauc_map_at_5_max
      value: 47.2652
    - type: nauc_map_at_5_std
      value: 5.0378
    - type: nauc_map_at_5_diff1
      value: 51.3051
    - type: nauc_map_at_10_max
      value: 47.3629
    - type: nauc_map_at_10_std
      value: 5.4796
    - type: nauc_map_at_10_diff1
      value: 50.43450000000001
    - type: nauc_map_at_20_max
      value: 47.5858
    - type: nauc_map_at_20_std
      value: 6.4494
    - type: nauc_map_at_20_diff1
      value: 50.3333
    - type: nauc_map_at_100_max
      value: 47.6506
    - type: nauc_map_at_100_std
      value: 7.1591000000000005
    - type: nauc_map_at_100_diff1
      value: 50.138000000000005
    - type: nauc_map_at_1000_max
      value: 47.516999999999996
    - type: nauc_map_at_1000_std
      value: 7.2322
    - type: nauc_map_at_1000_diff1
      value: 50.132299999999994
    - type: nauc_recall_at_1_max
      value: 45.0797
    - type: nauc_recall_at_1_std
      value: 1.9601
    - type: nauc_recall_at_1_diff1
      value: 55.33050000000001
    - type: nauc_recall_at_3_max
      value: 44.9897
    - type: nauc_recall_at_3_std
      value: 5.6308
    - type: nauc_recall_at_3_diff1
      value: 46.6793
    - type: nauc_recall_at_5_max
      value: 46.6283
    - type: nauc_recall_at_5_std
      value: 9.998999999999999
    - type: nauc_recall_at_5_diff1
      value: 45.9247
    - type: nauc_recall_at_10_max
      value: 44.714
    - type: nauc_recall_at_10_std
      value: 10.8319
    - type: nauc_recall_at_10_diff1
      value: 40.291900000000005
    - type: nauc_recall_at_20_max
      value: 46.361200000000004
    - type: nauc_recall_at_20_std
      value: 17.9809
    - type: nauc_recall_at_20_diff1
      value: 42.4004
    - type: nauc_recall_at_100_max
      value: 48.9864
    - type: nauc_recall_at_100_std
      value: 31.7118
    - type: nauc_recall_at_100_diff1
      value: 30.9676
    - type: nauc_recall_at_1000_max
      value: 59.9606
    - type: nauc_recall_at_1000_std
      value: 64.66229999999999
    - type: nauc_recall_at_1000_diff1
      value: 27.669
    - type: nauc_precision_at_1_max
      value: 47.905300000000004
    - type: nauc_precision_at_1_std
      value: 7.8307
    - type: nauc_precision_at_1_diff1
      value: 51.3311
    - type: nauc_precision_at_3_max
      value: 38.4644
    - type: nauc_precision_at_3_std
      value: 11.7975
    - type: nauc_precision_at_3_diff1
      value: 27.7451
    - type: nauc_precision_at_5_max
      value: 36.8955
    - type: nauc_precision_at_5_std
      value: 17.702399999999997
    - type: nauc_precision_at_5_diff1
      value: 24.6268
    - type: nauc_precision_at_10_max
      value: 26.5975
    - type: nauc_precision_at_10_std
      value: 22.3993
    - type: nauc_precision_at_10_diff1
      value: 8.6213
    - type: nauc_precision_at_20_max
      value: 17.3127
    - type: nauc_precision_at_20_std
      value: 24.7139
    - type: nauc_precision_at_20_diff1
      value: 1.3941000000000001
    - type: nauc_precision_at_100_max
      value: -0.882
    - type: nauc_precision_at_100_std
      value: 24.5949
    - type: nauc_precision_at_100_diff1
      value: -10.3409
    - type: nauc_precision_at_1000_max
      value: -15.3829
    - type: nauc_precision_at_1000_std
      value: 15.4108
    - type: nauc_precision_at_1000_diff1
      value: -19.8547
    - type: nauc_mrr_at_1_max
      value: 47.905300000000004
    - type: nauc_mrr_at_1_std
      value: 7.8307
    - type: nauc_mrr_at_1_diff1
      value: 51.3311
    - type: nauc_mrr_at_3_max
      value: 46.6702
    - type: nauc_mrr_at_3_std
      value: 8.4343
    - type: nauc_mrr_at_3_diff1
      value: 47.7232
    - type: nauc_mrr_at_5_max
      value: 47.439
    - type: nauc_mrr_at_5_std
      value: 9.8287
    - type: nauc_mrr_at_5_diff1
      value: 48.2284
    - type: nauc_mrr_at_10_max
      value: 47.477000000000004
    - type: nauc_mrr_at_10_std
      value: 9.9349
    - type: nauc_mrr_at_10_diff1
      value: 47.7388
    - type: nauc_mrr_at_20_max
      value: 47.5871
    - type: nauc_mrr_at_20_std
      value: 10.137400000000001
    - type: nauc_mrr_at_20_diff1
      value: 47.949000000000005
    - type: nauc_mrr_at_100_max
      value: 47.5206
    - type: nauc_mrr_at_100_std
      value: 10.0871
    - type: nauc_mrr_at_100_diff1
      value: 47.875299999999996
    - type: nauc_mrr_at_1000_max
      value: 47.5212
    - type: nauc_mrr_at_1000_std
      value: 10.0739
    - type: nauc_mrr_at_1000_diff1
      value: 47.8953
    - type: main_score
      value: 47.303
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: ndcg_at_1
      value: 29.759999999999998
    - type: ndcg_at_3
      value: 33.824
    - type: ndcg_at_5
      value: 36.766
    - type: ndcg_at_10
      value: 39.902
    - type: ndcg_at_20
      value: 41.618
    - type: ndcg_at_100
      value: 44.983000000000004
    - type: ndcg_at_1000
      value: 46.938
    - type: map_at_1
      value: 27.181
    - type: map_at_3
      value: 31.526
    - type: map_at_5
      value: 33.397
    - type: map_at_10
      value: 34.766999999999996
    - type: map_at_20
      value: 35.244
    - type: map_at_100
      value: 35.757
    - type: map_at_1000
      value: 35.836
    - type: recall_at_1
      value: 27.181
    - type: recall_at_3
      value: 37.19
    - type: recall_at_5
      value: 44.153999999999996
    - type: recall_at_10
      value: 53.705000000000005
    - type: recall_at_20
      value: 60.22
    - type: recall_at_100
      value: 77.39200000000001
    - type: recall_at_1000
      value: 91.77
    - type: precision_at_1
      value: 29.759999999999998
    - type: precision_at_3
      value: 13.925
    - type: precision_at_5
      value: 10.24
    - type: precision_at_10
      value: 6.265999999999999
    - type: precision_at_20
      value: 3.549
    - type: precision_at_100
      value: 0.9520000000000001
    - type: precision_at_1000
      value: 0.122
    - type: mrr_at_1
      value: 29.7597
    - type: mrr_at_3
      value: 34.4732
    - type: mrr_at_5
      value: 35.915
    - type: mrr_at_10
      value: 37.1488
    - type: mrr_at_20
      value: 37.637100000000004
    - type: mrr_at_100
      value: 38.0403
    - type: mrr_at_1000
      value: 38.096999999999994
    - type: nauc_ndcg_at_1_max
      value: 35.7865
    - type: nauc_ndcg_at_1_std
      value: 1.9512
    - type: nauc_ndcg_at_1_diff1
      value: 54.9311
    - type: nauc_ndcg_at_3_max
      value: 32.6952
    - type: nauc_ndcg_at_3_std
      value: 6.2215
    - type: nauc_ndcg_at_3_diff1
      value: 48.2731
    - type: nauc_ndcg_at_5_max
      value: 33.893
    - type: nauc_ndcg_at_5_std
      value: 5.418
    - type: nauc_ndcg_at_5_diff1
      value: 47.5903
    - type: nauc_ndcg_at_10_max
      value: 31.5442
    - type: nauc_ndcg_at_10_std
      value: 6.4778
    - type: nauc_ndcg_at_10_diff1
      value: 46.1388
    - type: nauc_ndcg_at_20_max
      value: 31.613200000000003
    - type: nauc_ndcg_at_20_std
      value: 7.0572
    - type: nauc_ndcg_at_20_diff1
      value: 46.5949
    - type: nauc_ndcg_at_100_max
      value: 32.8054
    - type: nauc_ndcg_at_100_std
      value: 9.4452
    - type: nauc_ndcg_at_100_diff1
      value: 46.8179
    - type: nauc_ndcg_at_1000_max
      value: 33.0064
    - type: nauc_ndcg_at_1000_std
      value: 8.8104
    - type: nauc_ndcg_at_1000_diff1
      value: 47.4082
    - type: nauc_map_at_1_max
      value: 32.9731
    - type: nauc_map_at_1_std
      value: 0.6048
    - type: nauc_map_at_1_diff1
      value: 53.8662
    - type: nauc_map_at_3_max
      value: 32.1607
    - type: nauc_map_at_3_std
      value: 4.4275
    - type: nauc_map_at_3_diff1
      value: 49.648900000000005
    - type: nauc_map_at_5_max
      value: 33.0496
    - type: nauc_map_at_5_std
      value: 4.3251
    - type: nauc_map_at_5_diff1
      value: 49.1433
    - type: nauc_map_at_10_max
      value: 32.2061
    - type: nauc_map_at_10_std
      value: 4.7649
    - type: nauc_map_at_10_diff1
      value: 48.5962
    - type: nauc_map_at_20_max
      value: 32.2822
    - type: nauc_map_at_20_std
      value: 4.8831
    - type: nauc_map_at_20_diff1
      value: 48.766799999999996
    - type: nauc_map_at_100_max
      value: 32.521699999999996
    - type: nauc_map_at_100_std
      value: 5.2962
    - type: nauc_map_at_100_diff1
      value: 48.7986
    - type: nauc_map_at_1000_max
      value: 32.5074
    - type: nauc_map_at_1000_std
      value: 5.2721
    - type: nauc_map_at_1000_diff1
      value: 48.803000000000004
    - type: nauc_recall_at_1_max
      value: 32.9731
    - type: nauc_recall_at_1_std
      value: 0.6048
    - type: nauc_recall_at_1_diff1
      value: 53.8662
    - type: nauc_recall_at_3_max
      value: 29.308699999999998
    - type: nauc_recall_at_3_std
      value: 7.6516
    - type: nauc_recall_at_3_diff1
      value: 42.4534
    - type: nauc_recall_at_5_max
      value: 32.1131
    - type: nauc_recall_at_5_std
      value: 6.260599999999999
    - type: nauc_recall_at_5_diff1
      value: 40.5131
    - type: nauc_recall_at_10_max
      value: 24.2332
    - type: nauc_recall_at_10_std
      value: 9.7985
    - type: nauc_recall_at_10_diff1
      value: 34.911500000000004
    - type: nauc_recall_at_20_max
      value: 23.692
    - type: nauc_recall_at_20_std
      value: 12.088799999999999
    - type: nauc_recall_at_20_diff1
      value: 35.8843
    - type: nauc_recall_at_100_max
      value: 27.729300000000002
    - type: nauc_recall_at_100_std
      value: 31.9796
    - type: nauc_recall_at_100_diff1
      value: 32.5991
    - type: nauc_recall_at_1000_max
      value: 32.483200000000004
    - type: nauc_recall_at_1000_std
      value: 48.2299
    - type: nauc_recall_at_1000_diff1
      value: 35.8086
    - type: nauc_precision_at_1_max
      value: 35.7865
    - type: nauc_precision_at_1_std
      value: 1.9512
    - type: nauc_precision_at_1_diff1
      value: 54.9311
    - type: nauc_precision_at_3_max
      value: 35.729
    - type: nauc_precision_at_3_std
      value: 12.873499999999998
    - type: nauc_precision_at_3_diff1
      value: 43.6572
    - type: nauc_precision_at_5_max
      value: 35.9285
    - type: nauc_precision_at_5_std
      value: 11.120099999999999
    - type: nauc_precision_at_5_diff1
      value: 37.458999999999996
    - type: nauc_precision_at_10_max
      value: 29.4037
    - type: nauc_precision_at_10_std
      value: 16.1533
    - type: nauc_precision_at_10_diff1
      value: 30.7829
    - type: nauc_precision_at_20_max
      value: 28.733700000000002
    - type: nauc_precision_at_20_std
      value: 19.4687
    - type: nauc_precision_at_20_diff1
      value: 29.154999999999998
    - type: nauc_precision_at_100_max
      value: 28.109099999999998
    - type: nauc_precision_at_100_std
      value: 31.4104
    - type: nauc_precision_at_100_diff1
      value: 17.7183
    - type: nauc_precision_at_1000_max
      value: 5.8763000000000005
    - type: nauc_precision_at_1000_std
      value: 18.5651
    - type: nauc_precision_at_1000_diff1
      value: -0.5546
    - type: nauc_mrr_at_1_max
      value: 35.7865
    - type: nauc_mrr_at_1_std
      value: 1.9512
    - type: nauc_mrr_at_1_diff1
      value: 54.9311
    - type: nauc_mrr_at_3_max
      value: 35.371
    - type: nauc_mrr_at_3_std
      value: 6.447700000000001
    - type: nauc_mrr_at_3_diff1
      value: 50.998900000000006
    - type: nauc_mrr_at_5_max
      value: 36.2682
    - type: nauc_mrr_at_5_std
      value: 5.8895
    - type: nauc_mrr_at_5_diff1
      value: 50.72879999999999
    - type: nauc_mrr_at_10_max
      value: 35.1719
    - type: nauc_mrr_at_10_std
      value: 6.074199999999999
    - type: nauc_mrr_at_10_diff1
      value: 50.087
    - type: nauc_mrr_at_20_max
      value: 35.0608
    - type: nauc_mrr_at_20_std
      value: 6.2545
    - type: nauc_mrr_at_20_diff1
      value: 50.1754
    - type: nauc_mrr_at_100_max
      value: 35.1314
    - type: nauc_mrr_at_100_std
      value: 6.417299999999999
    - type: nauc_mrr_at_100_diff1
      value: 50.1819
    - type: nauc_mrr_at_1000_max
      value: 35.124
    - type: nauc_mrr_at_1000_std
      value: 6.3942
    - type: nauc_mrr_at_1000_diff1
      value: 50.1926
    - type: main_score
      value: 39.902
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: ndcg_at_1
      value: 40.129999999999995
    - type: ndcg_at_3
      value: 33.11
    - type: ndcg_at_5
      value: 34.721999999999994
    - type: ndcg_at_10
      value: 38.314
    - type: ndcg_at_20
      value: 41.006
    - type: ndcg_at_100
      value: 44.651
    - type: ndcg_at_1000
      value: 47.262
    - type: map_at_1
      value: 17.72
    - type: map_at_3
      value: 24.807000000000002
    - type: map_at_5
      value: 26.931
    - type: map_at_10
      value: 28.923
    - type: map_at_20
      value: 29.970999999999997
    - type: map_at_100
      value: 30.720999999999997
    - type: map_at_1000
      value: 30.866
    - type: recall_at_1
      value: 17.72
    - type: recall_at_3
      value: 29.421000000000003
    - type: recall_at_5
      value: 35.089
    - type: recall_at_10
      value: 42.962
    - type: recall_at_20
      value: 50.46000000000001
    - type: recall_at_100
      value: 64.39399999999999
    - type: recall_at_1000
      value: 78.93599999999999
    - type: precision_at_1
      value: 40.129999999999995
    - type: precision_at_3
      value: 24.407999999999998
    - type: precision_at_5
      value: 17.954
    - type: precision_at_10
      value: 11.375
    - type: precision_at_20
      value: 6.857
    - type: precision_at_100
      value: 1.812
    - type: precision_at_1000
      value: 0.231
    - type: mrr_at_1
      value: 40.130300000000005
    - type: mrr_at_3
      value: 48.7296
    - type: mrr_at_5
      value: 50.3583
    - type: mrr_at_10
      value: 51.415299999999995
    - type: mrr_at_20
      value: 51.831700000000005
    - type: mrr_at_100
      value: 52.0518
    - type: mrr_at_1000
      value: 52.0826
    - type: nauc_ndcg_at_1_max
      value: 40.104299999999995
    - type: nauc_ndcg_at_1_std
      value: 18.0912
    - type: nauc_ndcg_at_1_diff1
      value: 37.8955
    - type: nauc_ndcg_at_3_max
      value: 42.9593
    - type: nauc_ndcg_at_3_std
      value: 19.1131
    - type: nauc_ndcg_at_3_diff1
      value: 30.6546
    - type: nauc_ndcg_at_5_max
      value: 44.351
    - type: nauc_ndcg_at_5_std
      value: 21.026500000000002
    - type: nauc_ndcg_at_5_diff1
      value: 29.723100000000002
    - type: nauc_ndcg_at_10_max
      value: 45.1246
    - type: nauc_ndcg_at_10_std
      value: 23.4349
    - type: nauc_ndcg_at_10_diff1
      value: 29.488599999999998
    - type: nauc_ndcg_at_20_max
      value: 45.2818
    - type: nauc_ndcg_at_20_std
      value: 24.904899999999998
    - type: nauc_ndcg_at_20_diff1
      value: 28.9215
    - type: nauc_ndcg_at_100_max
      value: 46.7221
    - type: nauc_ndcg_at_100_std
      value: 28.011799999999997
    - type: nauc_ndcg_at_100_diff1
      value: 29.6544
    - type: nauc_ndcg_at_1000_max
      value: 46.7951
    - type: nauc_ndcg_at_1000_std
      value: 28.5671
    - type: nauc_ndcg_at_1000_diff1
      value: 29.7716
    - type: nauc_map_at_1_max
      value: 41.754400000000004
    - type: nauc_map_at_1_std
      value: 11.7817
    - type: nauc_map_at_1_diff1
      value: 39.7588
    - type: nauc_map_at_3_max
      value: 43.086
    - type: nauc_map_at_3_std
      value: 16.2776
    - type: nauc_map_at_3_diff1
      value: 31.2632
    - type: nauc_map_at_5_max
      value: 43.8303
    - type: nauc_map_at_5_std
      value: 18.2317
    - type: nauc_map_at_5_diff1
      value: 30.451099999999997
    - type: nauc_map_at_10_max
      value: 44.1511
    - type: nauc_map_at_10_std
      value: 19.9622
    - type: nauc_map_at_10_diff1
      value: 30.1447
    - type: nauc_map_at_20_max
      value: 44.2367
    - type: nauc_map_at_20_std
      value: 20.6727
    - type: nauc_map_at_20_diff1
      value: 29.7979
    - type: nauc_map_at_100_max
      value: 44.6514
    - type: nauc_map_at_100_std
      value: 21.451999999999998
    - type: nauc_map_at_100_diff1
      value: 29.9572
    - type: nauc_map_at_1000_max
      value: 44.6665
    - type: nauc_map_at_1000_std
      value: 21.507
    - type: nauc_map_at_1000_diff1
      value: 29.9788
    - type: nauc_recall_at_1_max
      value: 41.754400000000004
    - type: nauc_recall_at_1_std
      value: 11.7817
    - type: nauc_recall_at_1_diff1
      value: 39.7588
    - type: nauc_recall_at_3_max
      value: 42.1306
    - type: nauc_recall_at_3_std
      value: 17.397299999999998
    - type: nauc_recall_at_3_diff1
      value: 26.3229
    - type: nauc_recall_at_5_max
      value: 41.9516
    - type: nauc_recall_at_5_std
      value: 20.566699999999997
    - type: nauc_recall_at_5_diff1
      value: 23.4934
    - type: nauc_recall_at_10_max
      value: 41.260400000000004
    - type: nauc_recall_at_10_std
      value: 24.0061
    - type: nauc_recall_at_10_diff1
      value: 21.6158
    - type: nauc_recall_at_20_max
      value: 39.8437
    - type: nauc_recall_at_20_std
      value: 26.892100000000003
    - type: nauc_recall_at_20_diff1
      value: 19.1214
    - type: nauc_recall_at_100_max
      value: 42.9589
    - type: nauc_recall_at_100_std
      value: 37.7833
    - type: nauc_recall_at_100_diff1
      value: 19.575899999999997
    - type: nauc_recall_at_1000_max
      value: 43.292500000000004
    - type: nauc_recall_at_1000_std
      value: 46.5189
    - type: nauc_recall_at_1000_diff1
      value: 16.3096
    - type: nauc_precision_at_1_max
      value: 40.104299999999995
    - type: nauc_precision_at_1_std
      value: 18.0912
    - type: nauc_precision_at_1_diff1
      value: 37.8955
    - type: nauc_precision_at_3_max
      value: 37.2383
    - type: nauc_precision_at_3_std
      value: 24.0517
    - type: nauc_precision_at_3_diff1
      value: 19.169800000000002
    - type: nauc_precision_at_5_max
      value: 34.6764
    - type: nauc_precision_at_5_std
      value: 26.4407
    - type: nauc_precision_at_5_diff1
      value: 14.188
    - type: nauc_precision_at_10_max
      value: 31.1544
    - type: nauc_precision_at_10_std
      value: 28.997099999999996
    - type: nauc_precision_at_10_diff1
      value: 11.4475
    - type: nauc_precision_at_20_max
      value: 27.065499999999997
    - type: nauc_precision_at_20_std
      value: 29.658099999999997
    - type: nauc_precision_at_20_diff1
      value: 7.388999999999999
    - type: nauc_precision_at_100_max
      value: 22.5635
    - type: nauc_precision_at_100_std
      value: 35.1885
    - type: nauc_precision_at_100_diff1
      value: 4.612900000000001
    - type: nauc_precision_at_1000_max
      value: 9.4366
    - type: nauc_precision_at_1000_std
      value: 29.399399999999996
    - type: nauc_precision_at_1000_diff1
      value: -2.8055
    - type: nauc_mrr_at_1_max
      value: 40.104299999999995
    - type: nauc_mrr_at_1_std
      value: 18.0912
    - type: nauc_mrr_at_1_diff1
      value: 37.8955
    - type: nauc_mrr_at_3_max
      value: 43.088300000000004
    - type: nauc_mrr_at_3_std
      value: 21.658
    - type: nauc_mrr_at_3_diff1
      value: 34.4445
    - type: nauc_mrr_at_5_max
      value: 43.2876
    - type: nauc_mrr_at_5_std
      value: 22.6188
    - type: nauc_mrr_at_5_diff1
      value: 34.143699999999995
    - type: nauc_mrr_at_10_max
      value: 43.4627
    - type: nauc_mrr_at_10_std
      value: 22.7775
    - type: nauc_mrr_at_10_diff1
      value: 34.3108
    - type: nauc_mrr_at_20_max
      value: 43.5013
    - type: nauc_mrr_at_20_std
      value: 22.825599999999998
    - type: nauc_mrr_at_20_diff1
      value: 34.4236
    - type: nauc_mrr_at_100_max
      value: 43.543
    - type: nauc_mrr_at_100_std
      value: 22.8566
    - type: nauc_mrr_at_100_diff1
      value: 34.5171
    - type: nauc_mrr_at_1000_max
      value: 43.5287
    - type: nauc_mrr_at_1000_std
      value: 22.8398
    - type: nauc_mrr_at_1000_diff1
      value: 34.5149
    - type: main_score
      value: 38.314
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: ndcg_at_1
      value: 57.875
    - type: ndcg_at_3
      value: 48.424
    - type: ndcg_at_5
      value: 45.907
    - type: ndcg_at_10
      value: 43.881
    - type: ndcg_at_20
      value: 43.047000000000004
    - type: ndcg_at_100
      value: 47.892
    - type: ndcg_at_1000
      value: 55.175
    - type: map_at_1
      value: 9.705
    - type: map_at_3
      value: 14.984
    - type: map_at_5
      value: 17.579
    - type: map_at_10
      value: 20.901
    - type: map_at_20
      value: 24.244
    - type: map_at_100
      value: 29.263
    - type: map_at_1000
      value: 30.953000000000003
    - type: recall_at_1
      value: 9.705
    - type: recall_at_3
      value: 16.136
    - type: recall_at_5
      value: 20.4
    - type: recall_at_10
      value: 26.3
    - type: recall_at_20
      value: 33.719
    - type: recall_at_100
      value: 53.080000000000005
    - type: recall_at_1000
      value: 75.732
    - type: precision_at_1
      value: 70.75
    - type: precision_at_3
      value: 51.833
    - type: precision_at_5
      value: 44.2
    - type: precision_at_10
      value: 34.8
    - type: precision_at_20
      value: 26.174999999999997
    - type: precision_at_100
      value: 10.879999999999999
    - type: precision_at_1000
      value: 2.073
    - type: mrr_at_1
      value: 70.75
    - type: mrr_at_3
      value: 76.66669999999999
    - type: mrr_at_5
      value: 77.7667
    - type: mrr_at_10
      value: 78.2846
    - type: mrr_at_20
      value: 78.4431
    - type: mrr_at_100
      value: 78.5246
    - type: mrr_at_1000
      value: 78.5325
    - type: nauc_ndcg_at_1_max
      value: 47.8626
    - type: nauc_ndcg_at_1_std
      value: 29.184500000000003
    - type: nauc_ndcg_at_1_diff1
      value: 51.1817
    - type: nauc_ndcg_at_3_max
      value: 40.4824
    - type: nauc_ndcg_at_3_std
      value: 27.226899999999997
    - type: nauc_ndcg_at_3_diff1
      value: 29.3703
    - type: nauc_ndcg_at_5_max
      value: 38.145
    - type: nauc_ndcg_at_5_std
      value: 27.050600000000003
    - type: nauc_ndcg_at_5_diff1
      value: 27.043
    - type: nauc_ndcg_at_10_max
      value: 36.7997
    - type: nauc_ndcg_at_10_std
      value: 25.5961
    - type: nauc_ndcg_at_10_diff1
      value: 26.062800000000003
    - type: nauc_ndcg_at_20_max
      value: 33.0901
    - type: nauc_ndcg_at_20_std
      value: 21.3937
    - type: nauc_ndcg_at_20_diff1
      value: 24.8751
    - type: nauc_ndcg_at_100_max
      value: 36.032199999999996
    - type: nauc_ndcg_at_100_std
      value: 26.6399
    - type: nauc_ndcg_at_100_diff1
      value: 25.341399999999997
    - type: nauc_ndcg_at_1000_max
      value: 42.1806
    - type: nauc_ndcg_at_1000_std
      value: 36.6225
    - type: nauc_ndcg_at_1000_diff1
      value: 26.957700000000003
    - type: nauc_map_at_1_max
      value: -1.8065000000000002
    - type: nauc_map_at_1_std
      value: -23.1418
    - type: nauc_map_at_1_diff1
      value: 26.009700000000002
    - type: nauc_map_at_3_max
      value: 4.5538
    - type: nauc_map_at_3_std
      value: -19.7685
    - type: nauc_map_at_3_diff1
      value: 18.431900000000002
    - type: nauc_map_at_5_max
      value: 7.6586
    - type: nauc_map_at_5_std
      value: -15.1836
    - type: nauc_map_at_5_diff1
      value: 17.1768
    - type: nauc_map_at_10_max
      value: 12.3345
    - type: nauc_map_at_10_std
      value: -7.3311
    - type: nauc_map_at_10_diff1
      value: 16.467399999999998
    - type: nauc_map_at_20_max
      value: 16.9535
    - type: nauc_map_at_20_std
      value: 2.3999
    - type: nauc_map_at_20_diff1
      value: 16.1074
    - type: nauc_map_at_100_max
      value: 24.238699999999998
    - type: nauc_map_at_100_std
      value: 17.0193
    - type: nauc_map_at_100_diff1
      value: 17.179
    - type: nauc_map_at_1000_max
      value: 26.147199999999998
    - type: nauc_map_at_1000_std
      value: 20.597199999999997
    - type: nauc_map_at_1000_diff1
      value: 17.3145
    - type: nauc_recall_at_1_max
      value: -1.8065000000000002
    - type: nauc_recall_at_1_std
      value: -23.1418
    - type: nauc_recall_at_1_diff1
      value: 26.009700000000002
    - type: nauc_recall_at_3_max
      value: 1.7474
    - type: nauc_recall_at_3_std
      value: -21.331
    - type: nauc_recall_at_3_diff1
      value: 14.844899999999999
    - type: nauc_recall_at_5_max
      value: 3.9203
    - type: nauc_recall_at_5_std
      value: -17.225299999999997
    - type: nauc_recall_at_5_diff1
      value: 13.3026
    - type: nauc_recall_at_10_max
      value: 7.484399999999999
    - type: nauc_recall_at_10_std
      value: -10.879800000000001
    - type: nauc_recall_at_10_diff1
      value: 11.187
    - type: nauc_recall_at_20_max
      value: 12.327499999999999
    - type: nauc_recall_at_20_std
      value: -1.7592
    - type: nauc_recall_at_20_diff1
      value: 12.3485
    - type: nauc_recall_at_100_max
      value: 26.868799999999997
    - type: nauc_recall_at_100_std
      value: 23.4846
    - type: nauc_recall_at_100_diff1
      value: 16.4859
    - type: nauc_recall_at_1000_max
      value: 35.4478
    - type: nauc_recall_at_1000_std
      value: 42.7445
    - type: nauc_recall_at_1000_diff1
      value: 17.108
    - type: nauc_precision_at_1_max
      value: 59.8572
    - type: nauc_precision_at_1_std
      value: 39.1
    - type: nauc_precision_at_1_diff1
      value: 57.475
    - type: nauc_precision_at_3_max
      value: 42.9945
    - type: nauc_precision_at_3_std
      value: 41.5933
    - type: nauc_precision_at_3_diff1
      value: 12.3299
    - type: nauc_precision_at_5_max
      value: 39.8975
    - type: nauc_precision_at_5_std
      value: 46.3626
    - type: nauc_precision_at_5_diff1
      value: 7.990600000000001
    - type: nauc_precision_at_10_max
      value: 37.501200000000004
    - type: nauc_precision_at_10_std
      value: 51.9395
    - type: nauc_precision_at_10_diff1
      value: 4.8036
    - type: nauc_precision_at_20_max
      value: 34.9806
    - type: nauc_precision_at_20_std
      value: 53.513999999999996
    - type: nauc_precision_at_20_diff1
      value: 3.8808000000000002
    - type: nauc_precision_at_100_max
      value: 29.6714
    - type: nauc_precision_at_100_std
      value: 50.9404
    - type: nauc_precision_at_100_diff1
      value: 1.7782
    - type: nauc_precision_at_1000_max
      value: 4.9528
    - type: nauc_precision_at_1000_std
      value: 23.0701
    - type: nauc_precision_at_1000_diff1
      value: -11.6606
    - type: nauc_mrr_at_1_max
      value: 59.8572
    - type: nauc_mrr_at_1_std
      value: 39.1
    - type: nauc_mrr_at_1_diff1
      value: 57.475
    - type: nauc_mrr_at_3_max
      value: 61.6508
    - type: nauc_mrr_at_3_std
      value: 43.013400000000004
    - type: nauc_mrr_at_3_diff1
      value: 55.14170000000001
    - type: nauc_mrr_at_5_max
      value: 61.8982
    - type: nauc_mrr_at_5_std
      value: 42.4903
    - type: nauc_mrr_at_5_diff1
      value: 55.880300000000005
    - type: nauc_mrr_at_10_max
      value: 61.6843
    - type: nauc_mrr_at_10_std
      value: 42.8332
    - type: nauc_mrr_at_10_diff1
      value: 55.7773
    - type: nauc_mrr_at_20_max
      value: 61.7877
    - type: nauc_mrr_at_20_std
      value: 42.6655
    - type: nauc_mrr_at_20_diff1
      value: 55.9627
    - type: nauc_mrr_at_100_max
      value: 61.755300000000005
    - type: nauc_mrr_at_100_std
      value: 42.681799999999996
    - type: nauc_mrr_at_100_diff1
      value: 55.97410000000001
    - type: nauc_mrr_at_1000_max
      value: 61.7454
    - type: nauc_mrr_at_1000_std
      value: 42.6813
    - type: nauc_mrr_at_1000_diff1
      value: 55.9732
    - type: main_score
      value: 43.881
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 42.385
    - type: f1
      value: 38.2581
    - type: f1_weighted
      value: 44.6657
    - type: main_score
      value: 42.385
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: ndcg_at_1
      value: 89.81400000000001
    - type: ndcg_at_3
      value: 90.789
    - type: ndcg_at_5
      value: 91.266
    - type: ndcg_at_10
      value: 91.552
    - type: ndcg_at_20
      value: 91.759
    - type: ndcg_at_100
      value: 92.04
    - type: ndcg_at_1000
      value: 92.264
    - type: map_at_1
      value: 83.343
    - type: map_at_3
      value: 88.293
    - type: map_at_5
      value: 88.709
    - type: map_at_10
      value: 88.895
    - type: map_at_20
      value: 88.985
    - type: map_at_100
      value: 89.046
    - type: map_at_1000
      value: 89.059
    - type: recall_at_1
      value: 83.343
    - type: recall_at_3
      value: 92.545
    - type: recall_at_5
      value: 93.944
    - type: recall_at_10
      value: 94.82300000000001
    - type: recall_at_20
      value: 95.48100000000001
    - type: recall_at_100
      value: 96.64
    - type: recall_at_1000
      value: 97.989
    - type: precision_at_1
      value: 89.81400000000001
    - type: precision_at_3
      value: 33.698
    - type: precision_at_5
      value: 20.602999999999998
    - type: precision_at_10
      value: 10.453
    - type: precision_at_20
      value: 5.299
    - type: precision_at_100
      value: 1.091
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 89.81400000000001
    - type: mrr_at_3
      value: 93.7594
    - type: mrr_at_5
      value: 94.0144
    - type: mrr_at_10
      value: 94.073
    - type: mrr_at_20
      value: 94.0835
    - type: mrr_at_100
      value: 94.0871
    - type: mrr_at_1000
      value: 94.0873
    - type: nauc_ndcg_at_1_max
      value: 23.8983
    - type: nauc_ndcg_at_1_std
      value: -16.226
    - type: nauc_ndcg_at_1_diff1
      value: 78.4902
    - type: nauc_ndcg_at_3_max
      value: 15.106
    - type: nauc_ndcg_at_3_std
      value: -11.4
    - type: nauc_ndcg_at_3_diff1
      value: 41.9768
    - type: nauc_ndcg_at_5_max
      value: 14.6485
    - type: nauc_ndcg_at_5_std
      value: -9.5441
    - type: nauc_ndcg_at_5_diff1
      value: 39.7958
    - type: nauc_ndcg_at_10_max
      value: 14.241100000000001
    - type: nauc_ndcg_at_10_std
      value: -8.4259
    - type: nauc_ndcg_at_10_diff1
      value: 38.8701
    - type: nauc_ndcg_at_20_max
      value: 14.211199999999998
    - type: nauc_ndcg_at_20_std
      value: -7.916399999999999
    - type: nauc_ndcg_at_20_diff1
      value: 39.3907
    - type: nauc_ndcg_at_100_max
      value: 14.871400000000001
    - type: nauc_ndcg_at_100_std
      value: -7.4491000000000005
    - type: nauc_ndcg_at_100_diff1
      value: 40.7175
    - type: nauc_ndcg_at_1000_max
      value: 15.386800000000001
    - type: nauc_ndcg_at_1000_std
      value: -7.939100000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 42.1499
    - type: nauc_map_at_1_max
      value: 13.431199999999999
    - type: nauc_map_at_1_std
      value: -10.2714
    - type: nauc_map_at_1_diff1
      value: 50.8151
    - type: nauc_map_at_3_max
      value: 13.2276
    - type: nauc_map_at_3_std
      value: -9.8315
    - type: nauc_map_at_3_diff1
      value: 39.6441
    - type: nauc_map_at_5_max
      value: 13.4859
    - type: nauc_map_at_5_std
      value: -9.284
    - type: nauc_map_at_5_diff1
      value: 39.4358
    - type: nauc_map_at_10_max
      value: 13.578399999999998
    - type: nauc_map_at_10_std
      value: -8.828800000000001
    - type: nauc_map_at_10_diff1
      value: 39.338499999999996
    - type: nauc_map_at_20_max
      value: 13.600200000000001
    - type: nauc_map_at_20_std
      value: -8.6524
    - type: nauc_map_at_20_diff1
      value: 39.5327
    - type: nauc_map_at_100_max
      value: 13.7266
    - type: nauc_map_at_100_std
      value: -8.583
    - type: nauc_map_at_100_diff1
      value: 39.749
    - type: nauc_map_at_1000_max
      value: 13.7522
    - type: nauc_map_at_1000_std
      value: -8.5978
    - type: nauc_map_at_1000_diff1
      value: 39.8105
    - type: nauc_recall_at_1_max
      value: 13.431199999999999
    - type: nauc_recall_at_1_std
      value: -10.2714
    - type: nauc_recall_at_1_diff1
      value: 50.8151
    - type: nauc_recall_at_3_max
      value: 7.7703999999999995
    - type: nauc_recall_at_3_std
      value: -7.5428999999999995
    - type: nauc_recall_at_3_diff1
      value: 14.6511
    - type: nauc_recall_at_5_max
      value: 7.7514
    - type: nauc_recall_at_5_std
      value: -0.9165
    - type: nauc_recall_at_5_diff1
      value: 5.1985
    - type: nauc_recall_at_10_max
      value: 5.4695
    - type: nauc_recall_at_10_std
      value: 4.8362
    - type: nauc_recall_at_10_diff1
      value: -2.3994
    - type: nauc_recall_at_20_max
      value: 3.7693
    - type: nauc_recall_at_20_std
      value: 9.4046
    - type: nauc_recall_at_20_diff1
      value: -5.3729
    - type: nauc_recall_at_100_max
      value: 4.6496
    - type: nauc_recall_at_100_std
      value: 19.605700000000002
    - type: nauc_recall_at_100_diff1
      value: -9.1885
    - type: nauc_recall_at_1000_max
      value: 7.266
    - type: nauc_recall_at_1000_std
      value: 25.461699999999997
    - type: nauc_recall_at_1000_diff1
      value: -11.698699999999999
    - type: nauc_precision_at_1_max
      value: 23.8983
    - type: nauc_precision_at_1_std
      value: -16.226
    - type: nauc_precision_at_1_diff1
      value: 78.4902
    - type: nauc_precision_at_3_max
      value: 14.686399999999999
    - type: nauc_precision_at_3_std
      value: -5.6663
    - type: nauc_precision_at_3_diff1
      value: 0.5428999999999999
    - type: nauc_precision_at_5_max
      value: 12.9569
    - type: nauc_precision_at_5_std
      value: 1.145
    - type: nauc_precision_at_5_diff1
      value: -10.0661
    - type: nauc_precision_at_10_max
      value: 9.8558
    - type: nauc_precision_at_10_std
      value: 6.1638
    - type: nauc_precision_at_10_diff1
      value: -14.3308
    - type: nauc_precision_at_20_max
      value: 7.1591000000000005
    - type: nauc_precision_at_20_std
      value: 8.4559
    - type: nauc_precision_at_20_diff1
      value: -12.226099999999999
    - type: nauc_precision_at_100_max
      value: 7.6160000000000005
    - type: nauc_precision_at_100_std
      value: 8.6876
    - type: nauc_precision_at_100_diff1
      value: -5.8182
    - type: nauc_precision_at_1000_max
      value: 7.3231
    - type: nauc_precision_at_1000_std
      value: 4.929399999999999
    - type: nauc_precision_at_1000_diff1
      value: -1.187
    - type: nauc_mrr_at_1_max
      value: 23.8983
    - type: nauc_mrr_at_1_std
      value: -16.226
    - type: nauc_mrr_at_1_diff1
      value: 78.4902
    - type: nauc_mrr_at_3_max
      value: 25.2759
    - type: nauc_mrr_at_3_std
      value: -20.4713
    - type: nauc_mrr_at_3_diff1
      value: 77.55030000000001
    - type: nauc_mrr_at_5_max
      value: 25.709799999999998
    - type: nauc_mrr_at_5_std
      value: -19.3177
    - type: nauc_mrr_at_5_diff1
      value: 77.7659
    - type: nauc_mrr_at_10_max
      value: 25.4059
    - type: nauc_mrr_at_10_std
      value: -19.128600000000002
    - type: nauc_mrr_at_10_diff1
      value: 77.78580000000001
    - type: nauc_mrr_at_20_max
      value: 25.303399999999996
    - type: nauc_mrr_at_20_std
      value: -19.137999999999998
    - type: nauc_mrr_at_20_diff1
      value: 77.7914
    - type: nauc_mrr_at_100_max
      value: 25.2918
    - type: nauc_mrr_at_100_std
      value: -19.1132
    - type: nauc_mrr_at_100_diff1
      value: 77.7997
    - type: nauc_mrr_at_1000_max
      value: 25.2892
    - type: nauc_mrr_at_1000_std
      value: -19.1172
    - type: nauc_mrr_at_1000_diff1
      value: 77.7992
    - type: main_score
      value: 91.552
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: ndcg_at_1
      value: 44.907000000000004
    - type: ndcg_at_3
      value: 40.095
    - type: ndcg_at_5
      value: 41.464
    - type: ndcg_at_10
      value: 43.958999999999996
    - type: ndcg_at_20
      value: 46.931
    - type: ndcg_at_100
      value: 50.656
    - type: ndcg_at_1000
      value: 53.474999999999994
    - type: map_at_1
      value: 22.846
    - type: map_at_3
      value: 31.533
    - type: map_at_5
      value: 34.175
    - type: map_at_10
      value: 36.105
    - type: map_at_20
      value: 37.232
    - type: map_at_100
      value: 37.993
    - type: map_at_1000
      value: 38.171
    - type: recall_at_1
      value: 22.846
    - type: recall_at_3
      value: 36.065000000000005
    - type: recall_at_5
      value: 42.754999999999995
    - type: recall_at_10
      value: 50.595
    - type: recall_at_20
      value: 59.85
    - type: recall_at_100
      value: 75.08
    - type: recall_at_1000
      value: 91.685
    - type: precision_at_1
      value: 44.907000000000004
    - type: precision_at_3
      value: 26.183
    - type: precision_at_5
      value: 19.29
    - type: precision_at_10
      value: 11.883000000000001
    - type: precision_at_20
      value: 7.191
    - type: precision_at_100
      value: 1.8870000000000002
    - type: precision_at_1000
      value: 0.23900000000000002
    - type: mrr_at_1
      value: 44.907399999999996
    - type: mrr_at_3
      value: 50.10289999999999
    - type: mrr_at_5
      value: 51.5303
    - type: mrr_at_10
      value: 52.61169999999999
    - type: mrr_at_20
      value: 53.13290000000001
    - type: mrr_at_100
      value: 53.3809
    - type: mrr_at_1000
      value: 53.4181
    - type: nauc_ndcg_at_1_max
      value: 50.2672
    - type: nauc_ndcg_at_1_std
      value: -5.858
    - type: nauc_ndcg_at_1_diff1
      value: 55.1067
    - type: nauc_ndcg_at_3_max
      value: 40.9279
    - type: nauc_ndcg_at_3_std
      value: -6.954000000000001
    - type: nauc_ndcg_at_3_diff1
      value: 43.9096
    - type: nauc_ndcg_at_5_max
      value: 38.406400000000005
    - type: nauc_ndcg_at_5_std
      value: -5.951
    - type: nauc_ndcg_at_5_diff1
      value: 42.9537
    - type: nauc_ndcg_at_10_max
      value: 40.1602
    - type: nauc_ndcg_at_10_std
      value: -3.486
    - type: nauc_ndcg_at_10_diff1
      value: 43.693
    - type: nauc_ndcg_at_20_max
      value: 40.3159
    - type: nauc_ndcg_at_20_std
      value: -1.6125
    - type: nauc_ndcg_at_20_diff1
      value: 43.0649
    - type: nauc_ndcg_at_100_max
      value: 42.5543
    - type: nauc_ndcg_at_100_std
      value: 0.133
    - type: nauc_ndcg_at_100_diff1
      value: 44.263799999999996
    - type: nauc_ndcg_at_1000_max
      value: 43.520399999999995
    - type: nauc_ndcg_at_1000_std
      value: -0.49300000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 44.550200000000004
    - type: nauc_map_at_1_max
      value: 26.930300000000003
    - type: nauc_map_at_1_std
      value: -6.8881
    - type: nauc_map_at_1_diff1
      value: 45.905499999999996
    - type: nauc_map_at_3_max
      value: 32.3991
    - type: nauc_map_at_3_std
      value: -8.1954
    - type: nauc_map_at_3_diff1
      value: 42.9392
    - type: nauc_map_at_5_max
      value: 34.0031
    - type: nauc_map_at_5_std
      value: -6.9963999999999995
    - type: nauc_map_at_5_diff1
      value: 42.7737
    - type: nauc_map_at_10_max
      value: 36.38
    - type: nauc_map_at_10_std
      value: -5.663
    - type: nauc_map_at_10_diff1
      value: 43.1583
    - type: nauc_map_at_20_max
      value: 36.6981
    - type: nauc_map_at_20_std
      value: -4.9736
    - type: nauc_map_at_20_diff1
      value: 42.924800000000005
    - type: nauc_map_at_100_max
      value: 37.268699999999995
    - type: nauc_map_at_100_std
      value: -4.6967
    - type: nauc_map_at_100_diff1
      value: 43.024
    - type: nauc_map_at_1000_max
      value: 37.3818
    - type: nauc_map_at_1000_std
      value: -4.7077
    - type: nauc_map_at_1000_diff1
      value: 43.0575
    - type: nauc_recall_at_1_max
      value: 26.930300000000003
    - type: nauc_recall_at_1_std
      value: -6.8881
    - type: nauc_recall_at_1_diff1
      value: 45.905499999999996
    - type: nauc_recall_at_3_max
      value: 27.860200000000003
    - type: nauc_recall_at_3_std
      value: -7.8473
    - type: nauc_recall_at_3_diff1
      value: 36.569
    - type: nauc_recall_at_5_max
      value: 27.1751
    - type: nauc_recall_at_5_std
      value: -5.0796
    - type: nauc_recall_at_5_diff1
      value: 33.9236
    - type: nauc_recall_at_10_max
      value: 32.0004
    - type: nauc_recall_at_10_std
      value: 1.0071
    - type: nauc_recall_at_10_diff1
      value: 33.1849
    - type: nauc_recall_at_20_max
      value: 30.6595
    - type: nauc_recall_at_20_std
      value: 7.3179
    - type: nauc_recall_at_20_diff1
      value: 29.751300000000004
    - type: nauc_recall_at_100_max
      value: 35.9924
    - type: nauc_recall_at_100_std
      value: 21.691399999999998
    - type: nauc_recall_at_100_diff1
      value: 31.397100000000002
    - type: nauc_recall_at_1000_max
      value: 47.176899999999996
    - type: nauc_recall_at_1000_std
      value: 37.8536
    - type: nauc_recall_at_1000_diff1
      value: 30.2447
    - type: nauc_precision_at_1_max
      value: 50.2672
    - type: nauc_precision_at_1_std
      value: -5.858
    - type: nauc_precision_at_1_diff1
      value: 55.1067
    - type: nauc_precision_at_3_max
      value: 44.4071
    - type: nauc_precision_at_3_std
      value: -4.4772
    - type: nauc_precision_at_3_diff1
      value: 32.6195
    - type: nauc_precision_at_5_max
      value: 42.6336
    - type: nauc_precision_at_5_std
      value: -0.9528
    - type: nauc_precision_at_5_diff1
      value: 27.821299999999997
    - type: nauc_precision_at_10_max
      value: 45.5267
    - type: nauc_precision_at_10_std
      value: 4.0484
    - type: nauc_precision_at_10_diff1
      value: 23.8886
    - type: nauc_precision_at_20_max
      value: 41.7389
    - type: nauc_precision_at_20_std
      value: 9.3544
    - type: nauc_precision_at_20_diff1
      value: 16.236700000000003
    - type: nauc_precision_at_100_max
      value: 38.4564
    - type: nauc_precision_at_100_std
      value: 12.544
    - type: nauc_precision_at_100_diff1
      value: 10.5924
    - type: nauc_precision_at_1000_max
      value: 31.2525
    - type: nauc_precision_at_1000_std
      value: 10.641399999999999
    - type: nauc_precision_at_1000_diff1
      value: 1.5966
    - type: nauc_mrr_at_1_max
      value: 50.2672
    - type: nauc_mrr_at_1_std
      value: -5.858
    - type: nauc_mrr_at_1_diff1
      value: 55.1067
    - type: nauc_mrr_at_3_max
      value: 49.1124
    - type: nauc_mrr_at_3_std
      value: -5.0685
    - type: nauc_mrr_at_3_diff1
      value: 51.1787
    - type: nauc_mrr_at_5_max
      value: 48.5671
    - type: nauc_mrr_at_5_std
      value: -4.6053999999999995
    - type: nauc_mrr_at_5_diff1
      value: 50.688599999999994
    - type: nauc_mrr_at_10_max
      value: 49.2018
    - type: nauc_mrr_at_10_std
      value: -3.8524000000000003
    - type: nauc_mrr_at_10_diff1
      value: 50.4746
    - type: nauc_mrr_at_20_max
      value: 49.2589
    - type: nauc_mrr_at_20_std
      value: -3.5479
    - type: nauc_mrr_at_20_diff1
      value: 50.4304
    - type: nauc_mrr_at_100_max
      value: 49.3016
    - type: nauc_mrr_at_100_std
      value: -3.5770999999999997
    - type: nauc_mrr_at_100_diff1
      value: 50.6172
    - type: nauc_mrr_at_1000_max
      value: 49.2911
    - type: nauc_mrr_at_1000_std
      value: -3.6117999999999997
    - type: nauc_mrr_at_1000_diff1
      value: 50.6268
    - type: main_score
      value: 43.958999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: ndcg_at_1
      value: 85.955
    - type: ndcg_at_3
      value: 68.83
    - type: ndcg_at_5
      value: 70.894
    - type: ndcg_at_10
      value: 72.399
    - type: ndcg_at_20
      value: 73.328
    - type: ndcg_at_100
      value: 74.765
    - type: ndcg_at_1000
      value: 75.87899999999999
    - type: map_at_1
      value: 42.978
    - type: map_at_3
      value: 61.568
    - type: map_at_5
      value: 63.241
    - type: map_at_10
      value: 64.18199999999999
    - type: map_at_20
      value: 64.562
    - type: map_at_100
      value: 64.865
    - type: map_at_1000
      value: 64.922
    - type: recall_at_1
      value: 42.978
    - type: recall_at_3
      value: 64.801
    - type: recall_at_5
      value: 68.866
    - type: recall_at_10
      value: 72.627
    - type: recall_at_20
      value: 75.625
    - type: recall_at_100
      value: 81.951
    - type: recall_at_1000
      value: 89.37899999999999
    - type: precision_at_1
      value: 85.955
    - type: precision_at_3
      value: 43.201
    - type: precision_at_5
      value: 27.546
    - type: precision_at_10
      value: 14.524999999999999
    - type: precision_at_20
      value: 7.562
    - type: precision_at_100
      value: 1.6389999999999998
    - type: precision_at_1000
      value: 0.179
    - type: mrr_at_1
      value: 85.9554
    - type: mrr_at_3
      value: 89.2753
    - type: mrr_at_5
      value: 89.6838
    - type: mrr_at_10
      value: 89.8559
    - type: mrr_at_20
      value: 89.92569999999999
    - type: mrr_at_100
      value: 89.96600000000001
    - type: mrr_at_1000
      value: 89.97070000000001
    - type: nauc_ndcg_at_1_max
      value: 57.1837
    - type: nauc_ndcg_at_1_std
      value: -4.2725
    - type: nauc_ndcg_at_1_diff1
      value: 74.8832
    - type: nauc_ndcg_at_3_max
      value: 13.953399999999998
    - type: nauc_ndcg_at_3_std
      value: 0.9547
    - type: nauc_ndcg_at_3_diff1
      value: 4.6952
    - type: nauc_ndcg_at_5_max
      value: 12.1892
    - type: nauc_ndcg_at_5_std
      value: 1.7878
    - type: nauc_ndcg_at_5_diff1
      value: 2.1255
    - type: nauc_ndcg_at_10_max
      value: 11.4909
    - type: nauc_ndcg_at_10_std
      value: 2.9917
    - type: nauc_ndcg_at_10_diff1
      value: 1.111
    - type: nauc_ndcg_at_20_max
      value: 11.183800000000002
    - type: nauc_ndcg_at_20_std
      value: 3.8205999999999998
    - type: nauc_ndcg_at_20_diff1
      value: 0.5191
    - type: nauc_ndcg_at_100_max
      value: 11.4582
    - type: nauc_ndcg_at_100_std
      value: 5.2234
    - type: nauc_ndcg_at_100_diff1
      value: 0.7051
    - type: nauc_ndcg_at_1000_max
      value: 11.8891
    - type: nauc_ndcg_at_1000_std
      value: 5.0018
    - type: nauc_ndcg_at_1000_diff1
      value: 1.3516
    - type: nauc_map_at_1_max
      value: 57.1837
    - type: nauc_map_at_1_std
      value: -4.2725
    - type: nauc_map_at_1_diff1
      value: 74.8832
    - type: nauc_map_at_3_max
      value: 8.7588
    - type: nauc_map_at_3_std
      value: 0.8586
    - type: nauc_map_at_3_diff1
      value: -2.1179
    - type: nauc_map_at_5_max
      value: 7.8513
    - type: nauc_map_at_5_std
      value: 1.4206999999999999
    - type: nauc_map_at_5_diff1
      value: -3.5381000000000005
    - type: nauc_map_at_10_max
      value: 7.603999999999999
    - type: nauc_map_at_10_std
      value: 2.0785
    - type: nauc_map_at_10_diff1
      value: -3.9354
    - type: nauc_map_at_20_max
      value: 7.5393
    - type: nauc_map_at_20_std
      value: 2.3233
    - type: nauc_map_at_20_diff1
      value: -4.0794999999999995
    - type: nauc_map_at_100_max
      value: 7.593500000000001
    - type: nauc_map_at_100_std
      value: 2.5528
    - type: nauc_map_at_100_diff1
      value: -4.0459000000000005
    - type: nauc_map_at_1000_max
      value: 7.6116
    - type: nauc_map_at_1000_std
      value: 2.5475000000000003
    - type: nauc_map_at_1000_diff1
      value: -4.0208
    - type: nauc_recall_at_1_max
      value: 57.1837
    - type: nauc_recall_at_1_std
      value: -4.2725
    - type: nauc_recall_at_1_diff1
      value: 74.8832
    - type: nauc_recall_at_3_max
      value: 5.1265
    - type: nauc_recall_at_3_std
      value: 2.3453999999999997
    - type: nauc_recall_at_3_diff1
      value: -9.5534
    - type: nauc_recall_at_5_max
      value: 1.3988
    - type: nauc_recall_at_5_std
      value: 3.8738
    - type: nauc_recall_at_5_diff1
      value: -14.770900000000001
    - type: nauc_recall_at_10_max
      value: -1.1159999999999999
    - type: nauc_recall_at_10_std
      value: 6.7406999999999995
    - type: nauc_recall_at_10_diff1
      value: -18.08
    - type: nauc_recall_at_20_max
      value: -2.9072
    - type: nauc_recall_at_20_std
      value: 9.6567
    - type: nauc_recall_at_20_diff1
      value: -21.197
    - type: nauc_recall_at_100_max
      value: -4.4864
    - type: nauc_recall_at_100_std
      value: 17.8761
    - type: nauc_recall_at_100_diff1
      value: -24.5792
    - type: nauc_recall_at_1000_max
      value: -7.9052
    - type: nauc_recall_at_1000_std
      value: 21.7637
    - type: nauc_recall_at_1000_diff1
      value: -30.4447
    - type: nauc_precision_at_1_max
      value: 57.1837
    - type: nauc_precision_at_1_std
      value: -4.2725
    - type: nauc_precision_at_1_diff1
      value: 74.8832
    - type: nauc_precision_at_3_max
      value: 5.1265
    - type: nauc_precision_at_3_std
      value: 2.3453999999999997
    - type: nauc_precision_at_3_diff1
      value: -9.5534
    - type: nauc_precision_at_5_max
      value: 1.3988
    - type: nauc_precision_at_5_std
      value: 3.8738
    - type: nauc_precision_at_5_diff1
      value: -14.770900000000001
    - type: nauc_precision_at_10_max
      value: -1.1159999999999999
    - type: nauc_precision_at_10_std
      value: 6.7406999999999995
    - type: nauc_precision_at_10_diff1
      value: -18.08
    - type: nauc_precision_at_20_max
      value: -2.9072
    - type: nauc_precision_at_20_std
      value: 9.6567
    - type: nauc_precision_at_20_diff1
      value: -21.197
    - type: nauc_precision_at_100_max
      value: -4.4864
    - type: nauc_precision_at_100_std
      value: 17.8761
    - type: nauc_precision_at_100_diff1
      value: -24.5792
    - type: nauc_precision_at_1000_max
      value: -7.9052
    - type: nauc_precision_at_1000_std
      value: 21.7637
    - type: nauc_precision_at_1000_diff1
      value: -30.4447
    - type: nauc_mrr_at_1_max
      value: 57.1837
    - type: nauc_mrr_at_1_std
      value: -4.2725
    - type: nauc_mrr_at_1_diff1
      value: 74.8832
    - type: nauc_mrr_at_3_max
      value: 60.68019999999999
    - type: nauc_mrr_at_3_std
      value: -2.5041
    - type: nauc_mrr_at_3_diff1
      value: 74.2505
    - type: nauc_mrr_at_5_max
      value: 60.3928
    - type: nauc_mrr_at_5_std
      value: -2.2979
    - type: nauc_mrr_at_5_diff1
      value: 74.27470000000001
    - type: nauc_mrr_at_10_max
      value: 60.336800000000004
    - type: nauc_mrr_at_10_std
      value: -2.308
    - type: nauc_mrr_at_10_diff1
      value: 74.4135
    - type: nauc_mrr_at_20_max
      value: 60.317299999999996
    - type: nauc_mrr_at_20_std
      value: -2.1652
    - type: nauc_mrr_at_20_diff1
      value: 74.3945
    - type: nauc_mrr_at_100_max
      value: 60.283
    - type: nauc_mrr_at_100_std
      value: -2.154
    - type: nauc_mrr_at_100_diff1
      value: 74.38040000000001
    - type: nauc_mrr_at_1000_max
      value: 60.272099999999995
    - type: nauc_mrr_at_1000_std
      value: -2.1783
    - type: nauc_mrr_at_1000_diff1
      value: 74.378
    - type: main_score
      value: 72.399
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 69.0916
    - type: f1
      value: 68.9866
    - type: f1_weighted
      value: 68.9866
    - type: ap
      value: 63.3215
    - type: ap_weighted
      value: 63.3215
    - type: main_score
      value: 69.0916
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: dev
      type: mteb/msmarco
    metrics:
    - type: ndcg_at_1
      value: 24.914
    - type: ndcg_at_3
      value: 36.479
    - type: ndcg_at_5
      value: 40.288000000000004
    - type: ndcg_at_10
      value: 44.043
    - type: ndcg_at_20
      value: 46.838
    - type: ndcg_at_100
      value: 49.626999999999995
    - type: ndcg_at_1000
      value: 50.665000000000006
    - type: map_at_1
      value: 24.223
    - type: map_at_3
      value: 33.348
    - type: map_at_5
      value: 35.494
    - type: map_at_10
      value: 37.077
    - type: map_at_20
      value: 37.867
    - type: map_at_100
      value: 38.279999999999994
    - type: map_at_1000
      value: 38.323
    - type: recall_at_1
      value: 24.223
    - type: recall_at_3
      value: 44.9
    - type: recall_at_5
      value: 54.010999999999996
    - type: recall_at_10
      value: 65.399
    - type: recall_at_20
      value: 76.248
    - type: recall_at_100
      value: 90.78
    - type: recall_at_1000
      value: 98.619
    - type: precision_at_1
      value: 24.914
    - type: precision_at_3
      value: 15.501000000000001
    - type: precision_at_5
      value: 11.238
    - type: precision_at_10
      value: 6.837
    - type: precision_at_20
      value: 3.9960000000000004
    - type: precision_at_100
      value: 0.959
    - type: precision_at_1000
      value: 0.105
    - type: mrr_at_1
      value: 24.914
    - type: mrr_at_3
      value: 34.0043
    - type: mrr_at_5
      value: 36.1089
    - type: mrr_at_10
      value: 37.6521
    - type: mrr_at_20
      value: 38.4106
    - type: mrr_at_100
      value: 38.7938
    - type: mrr_at_1000
      value: 38.8316
    - type: nauc_ndcg_at_1_max
      value: 3.9297
    - type: nauc_ndcg_at_1_std
      value: -22.016
    - type: nauc_ndcg_at_1_diff1
      value: 39.7204
    - type: nauc_ndcg_at_3_max
      value: 4.7672
    - type: nauc_ndcg_at_3_std
      value: -27.0359
    - type: nauc_ndcg_at_3_diff1
      value: 34.139
    - type: nauc_ndcg_at_5_max
      value: 5.1921
    - type: nauc_ndcg_at_5_std
      value: -28.6425
    - type: nauc_ndcg_at_5_diff1
      value: 33.671800000000005
    - type: nauc_ndcg_at_10_max
      value: 5.3812999999999995
    - type: nauc_ndcg_at_10_std
      value: -28.7602
    - type: nauc_ndcg_at_10_diff1
      value: 33.5856
    - type: nauc_ndcg_at_20_max
      value: 5.7039
    - type: nauc_ndcg_at_20_std
      value: -27.578000000000003
    - type: nauc_ndcg_at_20_diff1
      value: 33.9639
    - type: nauc_ndcg_at_100_max
      value: 5.9491000000000005
    - type: nauc_ndcg_at_100_std
      value: -25.562800000000003
    - type: nauc_ndcg_at_100_diff1
      value: 34.5177
    - type: nauc_ndcg_at_1000_max
      value: 5.7685
    - type: nauc_ndcg_at_1000_std
      value: -25.796400000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 34.617
    - type: nauc_map_at_1_max
      value: 3.8164
    - type: nauc_map_at_1_std
      value: -22.1345
    - type: nauc_map_at_1_diff1
      value: 39.7682
    - type: nauc_map_at_3_max
      value: 4.5438
    - type: nauc_map_at_3_std
      value: -25.990299999999998
    - type: nauc_map_at_3_diff1
      value: 35.4211
    - type: nauc_map_at_5_max
      value: 4.7521
    - type: nauc_map_at_5_std
      value: -26.9187
    - type: nauc_map_at_5_diff1
      value: 35.1711
    - type: nauc_map_at_10_max
      value: 4.8275
    - type: nauc_map_at_10_std
      value: -26.962799999999998
    - type: nauc_map_at_10_diff1
      value: 35.1875
    - type: nauc_map_at_20_max
      value: 4.9247
    - type: nauc_map_at_20_std
      value: -26.622899999999998
    - type: nauc_map_at_20_diff1
      value: 35.308499999999995
    - type: nauc_map_at_100_max
      value: 4.9704
    - type: nauc_map_at_100_std
      value: -26.3156
    - type: nauc_map_at_100_diff1
      value: 35.3955
    - type: nauc_map_at_1000_max
      value: 4.9692
    - type: nauc_map_at_1000_std
      value: -26.3098
    - type: nauc_map_at_1000_diff1
      value: 35.3987
    - type: nauc_recall_at_1_max
      value: 3.8164
    - type: nauc_recall_at_1_std
      value: -22.1345
    - type: nauc_recall_at_1_diff1
      value: 39.7682
    - type: nauc_recall_at_3_max
      value: 5.2443
    - type: nauc_recall_at_3_std
      value: -29.965000000000003
    - type: nauc_recall_at_3_diff1
      value: 30.303
    - type: nauc_recall_at_5_max
      value: 6.164499999999999
    - type: nauc_recall_at_5_std
      value: -33.9534
    - type: nauc_recall_at_5_diff1
      value: 28.9101
    - type: nauc_recall_at_10_max
      value: 6.8656999999999995
    - type: nauc_recall_at_10_std
      value: -35.2711
    - type: nauc_recall_at_10_diff1
      value: 27.785500000000003
    - type: nauc_recall_at_20_max
      value: 8.7891
    - type: nauc_recall_at_20_std
      value: -31.276
    - type: nauc_recall_at_20_diff1
      value: 28.048099999999998
    - type: nauc_recall_at_100_max
      value: 15.3546
    - type: nauc_recall_at_100_std
      value: -7.2786
    - type: nauc_recall_at_100_diff1
      value: 29.0868
    - type: nauc_recall_at_1000_max
      value: 33.858
    - type: nauc_recall_at_1000_std
      value: 42.2189
    - type: nauc_recall_at_1000_diff1
      value: 18.9862
    - type: nauc_precision_at_1_max
      value: 3.9297
    - type: nauc_precision_at_1_std
      value: -22.016
    - type: nauc_precision_at_1_diff1
      value: 39.7204
    - type: nauc_precision_at_3_max
      value: 5.1912
    - type: nauc_precision_at_3_std
      value: -29.697000000000003
    - type: nauc_precision_at_3_diff1
      value: 30.089199999999998
    - type: nauc_precision_at_5_max
      value: 6.311400000000001
    - type: nauc_precision_at_5_std
      value: -32.9724
    - type: nauc_precision_at_5_diff1
      value: 28.0676
    - type: nauc_precision_at_10_max
      value: 6.869400000000001
    - type: nauc_precision_at_10_std
      value: -32.4788
    - type: nauc_precision_at_10_diff1
      value: 25.6897
    - type: nauc_precision_at_20_max
      value: 9.206
    - type: nauc_precision_at_20_std
      value: -25.3222
    - type: nauc_precision_at_20_diff1
      value: 23.799500000000002
    - type: nauc_precision_at_100_max
      value: 13.8625
    - type: nauc_precision_at_100_std
      value: 3.3068
    - type: nauc_precision_at_100_diff1
      value: 14.3806
    - type: nauc_precision_at_1000_max
      value: 11.8588
    - type: nauc_precision_at_1000_std
      value: 17.6676
    - type: nauc_precision_at_1000_diff1
      value: -3.8201
    - type: nauc_mrr_at_1_max
      value: 3.9297
    - type: nauc_mrr_at_1_std
      value: -22.016
    - type: nauc_mrr_at_1_diff1
      value: 39.7204
    - type: nauc_mrr_at_3_max
      value: 4.6479
    - type: nauc_mrr_at_3_std
      value: -25.644699999999997
    - type: nauc_mrr_at_3_diff1
      value: 35.478
    - type: nauc_mrr_at_5_max
      value: 4.986
    - type: nauc_mrr_at_5_std
      value: -26.4206
    - type: nauc_mrr_at_5_diff1
      value: 35.285
    - type: nauc_mrr_at_10_max
      value: 5.0845
    - type: nauc_mrr_at_10_std
      value: -26.411800000000003
    - type: nauc_mrr_at_10_diff1
      value: 35.2365
    - type: nauc_mrr_at_20_max
      value: 5.1531
    - type: nauc_mrr_at_20_std
      value: -26.0735
    - type: nauc_mrr_at_20_diff1
      value: 35.3495
    - type: nauc_mrr_at_100_max
      value: 5.1672
    - type: nauc_mrr_at_100_std
      value: -25.8254
    - type: nauc_mrr_at_100_diff1
      value: 35.4396
    - type: nauc_mrr_at_1000_max
      value: 5.1629000000000005
    - type: nauc_mrr_at_1000_std
      value: -25.8233
    - type: nauc_mrr_at_1000_diff1
      value: 35.4444
    - type: main_score
      value: 44.043
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 92.08619999999999
    - type: f1
      value: 91.8074
    - type: f1_weighted
      value: 92.0765
    - type: main_score
      value: 92.08619999999999
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 65.2668
    - type: f1
      value: 44.499
    - type: f1_weighted
      value: 67.9193
    - type: main_score
      value: 65.2668
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 68.0128
    - type: f1
      value: 64.4011
    - type: f1_weighted
      value: 67.4705
    - type: main_score
      value: 68.0128
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 72.67320000000001
    - type: f1
      value: 71.7881
    - type: f1_weighted
      value: 72.9092
    - type: main_score
      value: 72.67320000000001
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 31.5764
    - type: v_measure_std
      value: 1.3743999999999998
    - type: main_score
      value: 31.5764
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 28.006999999999998
    - type: v_measure_std
      value: 1.4235
    - type: main_score
      value: 28.006999999999998
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: map
      value: 30.3039
    - type: mrr
      value: 31.168699999999998
    - type: nAUC_map_max
      value: -25.113200000000003
    - type: nAUC_map_std
      value: -8.5652
    - type: nAUC_map_diff1
      value: 12.437199999999999
    - type: nAUC_mrr_max
      value: -19.5255
    - type: nAUC_mrr_std
      value: -6.1112
    - type: nAUC_mrr_diff1
      value: 12.1585
    - type: main_score
      value: 30.3039
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: ndcg_at_1
      value: 45.046
    - type: ndcg_at_3
      value: 41.975
    - type: ndcg_at_5
      value: 39.421
    - type: ndcg_at_10
      value: 35.879
    - type: ndcg_at_20
      value: 32.987
    - type: ndcg_at_100
      value: 32.107
    - type: ndcg_at_1000
      value: 40.67
    - type: map_at_1
      value: 5.854
    - type: map_at_3
      value: 9.991999999999999
    - type: map_at_5
      value: 11.405999999999999
    - type: map_at_10
      value: 13.272
    - type: map_at_20
      value: 14.604000000000001
    - type: map_at_100
      value: 16.521
    - type: map_at_1000
      value: 17.925
    - type: recall_at_1
      value: 5.854
    - type: recall_at_3
      value: 11.036999999999999
    - type: recall_at_5
      value: 13.391
    - type: recall_at_10
      value: 16.841
    - type: recall_at_20
      value: 20.522000000000002
    - type: recall_at_100
      value: 31.733
    - type: recall_at_1000
      value: 63.525
    - type: precision_at_1
      value: 46.749
    - type: precision_at_3
      value: 39.525
    - type: precision_at_5
      value: 34.056
    - type: precision_at_10
      value: 26.656000000000002
    - type: precision_at_20
      value: 19.211
    - type: precision_at_100
      value: 8.099
    - type: precision_at_1000
      value: 2.061
    - type: mrr_at_1
      value: 47.0588
    - type: mrr_at_3
      value: 53.9732
    - type: mrr_at_5
      value: 55.443799999999996
    - type: mrr_at_10
      value: 56.04599999999999
    - type: mrr_at_20
      value: 56.37799999999999
    - type: mrr_at_100
      value: 56.6504
    - type: mrr_at_1000
      value: 56.6866
    - type: nauc_ndcg_at_1_max
      value: 43.5884
    - type: nauc_ndcg_at_1_std
      value: 22.4376
    - type: nauc_ndcg_at_1_diff1
      value: 34.7846
    - type: nauc_ndcg_at_3_max
      value: 44.7961
    - type: nauc_ndcg_at_3_std
      value: 24.4811
    - type: nauc_ndcg_at_3_diff1
      value: 25.5747
    - type: nauc_ndcg_at_5_max
      value: 43.5994
    - type: nauc_ndcg_at_5_std
      value: 24.827199999999998
    - type: nauc_ndcg_at_5_diff1
      value: 23.8874
    - type: nauc_ndcg_at_10_max
      value: 43.126999999999995
    - type: nauc_ndcg_at_10_std
      value: 27.5053
    - type: nauc_ndcg_at_10_diff1
      value: 23.4832
    - type: nauc_ndcg_at_20_max
      value: 43.1243
    - type: nauc_ndcg_at_20_std
      value: 27.3455
    - type: nauc_ndcg_at_20_diff1
      value: 23.8534
    - type: nauc_ndcg_at_100_max
      value: 46.5936
    - type: nauc_ndcg_at_100_std
      value: 28.0084
    - type: nauc_ndcg_at_100_diff1
      value: 29.630200000000002
    - type: nauc_ndcg_at_1000_max
      value: 51.7379
    - type: nauc_ndcg_at_1000_std
      value: 33.2077
    - type: nauc_ndcg_at_1000_diff1
      value: 30.1522
    - type: nauc_map_at_1_max
      value: 17.2703
    - type: nauc_map_at_1_std
      value: -14.6241
    - type: nauc_map_at_1_diff1
      value: 46.9767
    - type: nauc_map_at_3_max
      value: 25.562600000000003
    - type: nauc_map_at_3_std
      value: -10.1565
    - type: nauc_map_at_3_diff1
      value: 39.347500000000004
    - type: nauc_map_at_5_max
      value: 28.397299999999998
    - type: nauc_map_at_5_std
      value: -7.0083
    - type: nauc_map_at_5_diff1
      value: 37.4216
    - type: nauc_map_at_10_max
      value: 31.639400000000002
    - type: nauc_map_at_10_std
      value: -1.9
    - type: nauc_map_at_10_diff1
      value: 35.9293
    - type: nauc_map_at_20_max
      value: 34.342800000000004
    - type: nauc_map_at_20_std
      value: 2.6614
    - type: nauc_map_at_20_diff1
      value: 34.7985
    - type: nauc_map_at_100_max
      value: 37.046600000000005
    - type: nauc_map_at_100_std
      value: 9.2072
    - type: nauc_map_at_100_diff1
      value: 33.2764
    - type: nauc_map_at_1000_max
      value: 37.6597
    - type: nauc_map_at_1000_std
      value: 12.6768
    - type: nauc_map_at_1000_diff1
      value: 31.773699999999998
    - type: nauc_recall_at_1_max
      value: 17.2703
    - type: nauc_recall_at_1_std
      value: -14.6241
    - type: nauc_recall_at_1_diff1
      value: 46.9767
    - type: nauc_recall_at_3_max
      value: 24.5473
    - type: nauc_recall_at_3_std
      value: -9.7412
    - type: nauc_recall_at_3_diff1
      value: 37.8539
    - type: nauc_recall_at_5_max
      value: 27.249200000000002
    - type: nauc_recall_at_5_std
      value: -5.823799999999999
    - type: nauc_recall_at_5_diff1
      value: 34.06
    - type: nauc_recall_at_10_max
      value: 29.1217
    - type: nauc_recall_at_10_std
      value: -0.21159999999999998
    - type: nauc_recall_at_10_diff1
      value: 32.3914
    - type: nauc_recall_at_20_max
      value: 31.142999999999997
    - type: nauc_recall_at_20_std
      value: 4.3805
    - type: nauc_recall_at_20_diff1
      value: 28.852899999999998
    - type: nauc_recall_at_100_max
      value: 32.8751
    - type: nauc_recall_at_100_std
      value: 16.0658
    - type: nauc_recall_at_100_diff1
      value: 24.8181
    - type: nauc_recall_at_1000_max
      value: 24.5638
    - type: nauc_recall_at_1000_std
      value: 20.822
    - type: nauc_recall_at_1000_diff1
      value: 13.123099999999999
    - type: nauc_precision_at_1_max
      value: 44.714999999999996
    - type: nauc_precision_at_1_std
      value: 23.2541
    - type: nauc_precision_at_1_diff1
      value: 33.9092
    - type: nauc_precision_at_3_max
      value: 44.935199999999995
    - type: nauc_precision_at_3_std
      value: 29.0989
    - type: nauc_precision_at_3_diff1
      value: 14.9816
    - type: nauc_precision_at_5_max
      value: 40.7582
    - type: nauc_precision_at_5_std
      value: 31.049
    - type: nauc_precision_at_5_diff1
      value: 9.7826
    - type: nauc_precision_at_10_max
      value: 37.8974
    - type: nauc_precision_at_10_std
      value: 38.9576
    - type: nauc_precision_at_10_diff1
      value: 4.3217
    - type: nauc_precision_at_20_max
      value: 33.254099999999994
    - type: nauc_precision_at_20_std
      value: 42.3527
    - type: nauc_precision_at_20_diff1
      value: -1.8002
    - type: nauc_precision_at_100_max
      value: 20.6042
    - type: nauc_precision_at_100_std
      value: 46.0314
    - type: nauc_precision_at_100_diff1
      value: -10.098
    - type: nauc_precision_at_1000_max
      value: 6.8368
    - type: nauc_precision_at_1000_std
      value: 36.4345
    - type: nauc_precision_at_1000_diff1
      value: -16.1738
    - type: nauc_mrr_at_1_max
      value: 44.1317
    - type: nauc_mrr_at_1_std
      value: 22.794900000000002
    - type: nauc_mrr_at_1_diff1
      value: 33.071600000000004
    - type: nauc_mrr_at_3_max
      value: 49.8647
    - type: nauc_mrr_at_3_std
      value: 28.821600000000004
    - type: nauc_mrr_at_3_diff1
      value: 31.1845
    - type: nauc_mrr_at_5_max
      value: 50.3448
    - type: nauc_mrr_at_5_std
      value: 28.721799999999998
    - type: nauc_mrr_at_5_diff1
      value: 31.6681
    - type: nauc_mrr_at_10_max
      value: 50.601
    - type: nauc_mrr_at_10_std
      value: 29.461199999999998
    - type: nauc_mrr_at_10_diff1
      value: 31.5519
    - type: nauc_mrr_at_20_max
      value: 50.7861
    - type: nauc_mrr_at_20_std
      value: 29.615000000000002
    - type: nauc_mrr_at_20_diff1
      value: 31.535200000000003
    - type: nauc_mrr_at_100_max
      value: 50.7764
    - type: nauc_mrr_at_100_std
      value: 29.772199999999998
    - type: nauc_mrr_at_100_diff1
      value: 31.5569
    - type: nauc_mrr_at_1000_max
      value: 50.75150000000001
    - type: nauc_mrr_at_1000_std
      value: 29.747600000000002
    - type: nauc_mrr_at_1000_diff1
      value: 31.5457
    - type: main_score
      value: 35.879
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: ndcg_at_1
      value: 45.394
    - type: ndcg_at_3
      value: 57.17
    - type: ndcg_at_5
      value: 61.402
    - type: ndcg_at_10
      value: 64.59899999999999
    - type: ndcg_at_20
      value: 66.24600000000001
    - type: ndcg_at_100
      value: 67.522
    - type: ndcg_at_1000
      value: 67.849
    - type: map_at_1
      value: 40.6
    - type: map_at_3
      value: 53.055
    - type: map_at_5
      value: 55.67100000000001
    - type: map_at_10
      value: 57.160999999999994
    - type: map_at_20
      value: 57.701
    - type: map_at_100
      value: 57.926
    - type: map_at_1000
      value: 57.940999999999995
    - type: recall_at_1
      value: 40.6
    - type: recall_at_3
      value: 65.766
    - type: recall_at_5
      value: 75.466
    - type: recall_at_10
      value: 84.654
    - type: recall_at_20
      value: 90.60000000000001
    - type: recall_at_100
      value: 96.854
    - type: recall_at_1000
      value: 99.232
    - type: precision_at_1
      value: 45.394
    - type: precision_at_3
      value: 25.521
    - type: precision_at_5
      value: 17.781
    - type: precision_at_10
      value: 10.098
    - type: precision_at_20
      value: 5.4559999999999995
    - type: precision_at_100
      value: 1.176
    - type: precision_at_1000
      value: 0.121
    - type: mrr_at_1
      value: 45.394
    - type: mrr_at_3
      value: 56.3104
    - type: mrr_at_5
      value: 58.36130000000001
    - type: mrr_at_10
      value: 59.5005
    - type: mrr_at_20
      value: 59.866299999999995
    - type: mrr_at_100
      value: 59.9998
    - type: mrr_at_1000
      value: 60.0097
    - type: nauc_ndcg_at_1_max
      value: 26.4568
    - type: nauc_ndcg_at_1_std
      value: -5.4489
    - type: nauc_ndcg_at_1_diff1
      value: 39.8496
    - type: nauc_ndcg_at_3_max
      value: 31.1415
    - type: nauc_ndcg_at_3_std
      value: -7.0855
    - type: nauc_ndcg_at_3_diff1
      value: 36.4212
    - type: nauc_ndcg_at_5_max
      value: 32.819199999999995
    - type: nauc_ndcg_at_5_std
      value: -5.775
    - type: nauc_ndcg_at_5_diff1
      value: 35.7043
    - type: nauc_ndcg_at_10_max
      value: 33.0741
    - type: nauc_ndcg_at_10_std
      value: -4.5213
    - type: nauc_ndcg_at_10_diff1
      value: 36.19
    - type: nauc_ndcg_at_20_max
      value: 33.266400000000004
    - type: nauc_ndcg_at_20_std
      value: -3.5874
    - type: nauc_ndcg_at_20_diff1
      value: 36.2496
    - type: nauc_ndcg_at_100_max
      value: 32.7922
    - type: nauc_ndcg_at_100_std
      value: -3.2738000000000005
    - type: nauc_ndcg_at_100_diff1
      value: 36.5649
    - type: nauc_ndcg_at_1000_max
      value: 32.237500000000004
    - type: nauc_ndcg_at_1000_std
      value: -3.9578
    - type: nauc_ndcg_at_1000_diff1
      value: 36.717499999999994
    - type: nauc_map_at_1_max
      value: 24.3328
    - type: nauc_map_at_1_std
      value: -7.889799999999999
    - type: nauc_map_at_1_diff1
      value: 40.0251
    - type: nauc_map_at_3_max
      value: 29.6774
    - type: nauc_map_at_3_std
      value: -7.5739
    - type: nauc_map_at_3_diff1
      value: 37.459900000000005
    - type: nauc_map_at_5_max
      value: 30.6947
    - type: nauc_map_at_5_std
      value: -6.7940000000000005
    - type: nauc_map_at_5_diff1
      value: 37.0909
    - type: nauc_map_at_10_max
      value: 30.723899999999997
    - type: nauc_map_at_10_std
      value: -6.2581999999999995
    - type: nauc_map_at_10_diff1
      value: 37.1775
    - type: nauc_map_at_20_max
      value: 30.7861
    - type: nauc_map_at_20_std
      value: -5.9957
    - type: nauc_map_at_20_diff1
      value: 37.209900000000005
    - type: nauc_map_at_100_max
      value: 30.7336
    - type: nauc_map_at_100_std
      value: -5.909
    - type: nauc_map_at_100_diff1
      value: 37.2446
    - type: nauc_map_at_1000_max
      value: 30.7142
    - type: nauc_map_at_1000_std
      value: -5.9306
    - type: nauc_map_at_1000_diff1
      value: 37.25
    - type: nauc_recall_at_1_max
      value: 24.3328
    - type: nauc_recall_at_1_std
      value: -7.889799999999999
    - type: nauc_recall_at_1_diff1
      value: 40.0251
    - type: nauc_recall_at_3_max
      value: 34.2412
    - type: nauc_recall_at_3_std
      value: -7.5245999999999995
    - type: nauc_recall_at_3_diff1
      value: 32.7498
    - type: nauc_recall_at_5_max
      value: 39.6798
    - type: nauc_recall_at_5_std
      value: -4.1992
    - type: nauc_recall_at_5_diff1
      value: 29.5385
    - type: nauc_recall_at_10_max
      value: 44.5052
    - type: nauc_recall_at_10_std
      value: 2.4045
    - type: nauc_recall_at_10_diff1
      value: 30.051499999999997
    - type: nauc_recall_at_20_max
      value: 52.8161
    - type: nauc_recall_at_20_std
      value: 14.1647
    - type: nauc_recall_at_20_diff1
      value: 27.7847
    - type: nauc_recall_at_100_max
      value: 74.644
    - type: nauc_recall_at_100_std
      value: 54.927099999999996
    - type: nauc_recall_at_100_diff1
      value: 27.507900000000003
    - type: nauc_recall_at_1000_max
      value: 85.1144
    - type: nauc_recall_at_1000_std
      value: 80.0515
    - type: nauc_recall_at_1000_diff1
      value: 37.028299999999994
    - type: nauc_precision_at_1_max
      value: 26.4568
    - type: nauc_precision_at_1_std
      value: -5.4489
    - type: nauc_precision_at_1_diff1
      value: 39.8496
    - type: nauc_precision_at_3_max
      value: 30.0271
    - type: nauc_precision_at_3_std
      value: -0.8751
    - type: nauc_precision_at_3_diff1
      value: 21.8662
    - type: nauc_precision_at_5_max
      value: 28.4063
    - type: nauc_precision_at_5_std
      value: 4.1253
    - type: nauc_precision_at_5_diff1
      value: 13.1855
    - type: nauc_precision_at_10_max
      value: 22.6524
    - type: nauc_precision_at_10_std
      value: 10.340399999999999
    - type: nauc_precision_at_10_diff1
      value: 5.4243
    - type: nauc_precision_at_20_max
      value: 18.4481
    - type: nauc_precision_at_20_std
      value: 16.0409
    - type: nauc_precision_at_20_diff1
      value: -0.9561
    - type: nauc_precision_at_100_max
      value: 9.361600000000001
    - type: nauc_precision_at_100_std
      value: 19.1145
    - type: nauc_precision_at_100_diff1
      value: -8.0049
    - type: nauc_precision_at_1000_max
      value: 3.0707
    - type: nauc_precision_at_1000_std
      value: 15.259900000000002
    - type: nauc_precision_at_1000_diff1
      value: -10.190000000000001
    - type: nauc_mrr_at_1_max
      value: 26.4568
    - type: nauc_mrr_at_1_std
      value: -5.4489
    - type: nauc_mrr_at_1_diff1
      value: 39.8496
    - type: nauc_mrr_at_3_max
      value: 30.262299999999996
    - type: nauc_mrr_at_3_std
      value: -5.428100000000001
    - type: nauc_mrr_at_3_diff1
      value: 36.878899999999994
    - type: nauc_mrr_at_5_max
      value: 30.813000000000002
    - type: nauc_mrr_at_5_std
      value: -4.7534
    - type: nauc_mrr_at_5_diff1
      value: 36.5968
    - type: nauc_mrr_at_10_max
      value: 30.857499999999998
    - type: nauc_mrr_at_10_std
      value: -4.4249
    - type: nauc_mrr_at_10_diff1
      value: 36.973
    - type: nauc_mrr_at_20_max
      value: 30.8228
    - type: nauc_mrr_at_20_std
      value: -4.3275
    - type: nauc_mrr_at_20_diff1
      value: 37.0266
    - type: nauc_mrr_at_100_max
      value: 30.7442
    - type: nauc_mrr_at_100_std
      value: -4.3408
    - type: nauc_mrr_at_100_diff1
      value: 37.060500000000005
    - type: nauc_mrr_at_1000_max
      value: 30.7286
    - type: nauc_mrr_at_1000_std
      value: -4.36
    - type: nauc_mrr_at_1000_diff1
      value: 37.0647
    - type: main_score
      value: 64.59899999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: ndcg_at_1
      value: 82.01
    - type: ndcg_at_3
      value: 86.035
    - type: ndcg_at_5
      value: 87.628
    - type: ndcg_at_10
      value: 88.735
    - type: ndcg_at_20
      value: 89.375
    - type: ndcg_at_100
      value: 89.89
    - type: ndcg_at_1000
      value: 90.001
    - type: map_at_1
      value: 71.126
    - type: map_at_3
      value: 82.14399999999999
    - type: map_at_5
      value: 84.03500000000001
    - type: map_at_10
      value: 85.064
    - type: map_at_20
      value: 85.469
    - type: map_at_100
      value: 85.673
    - type: map_at_1000
      value: 85.69099999999999
    - type: recall_at_1
      value: 71.126
    - type: recall_at_3
      value: 87.76
    - type: recall_at_5
      value: 92.286
    - type: recall_at_10
      value: 95.56
    - type: recall_at_20
      value: 97.655
    - type: recall_at_100
      value: 99.497
    - type: recall_at_1000
      value: 99.979
    - type: precision_at_1
      value: 82.01
    - type: precision_at_3
      value: 37.653
    - type: precision_at_5
      value: 24.779999999999998
    - type: precision_at_10
      value: 13.441
    - type: precision_at_20
      value: 7.114
    - type: precision_at_100
      value: 1.524
    - type: precision_at_1000
      value: 0.157
    - type: mrr_at_1
      value: 81.96
    - type: mrr_at_3
      value: 87.105
    - type: mrr_at_5
      value: 87.779
    - type: mrr_at_10
      value: 88.02680000000001
    - type: mrr_at_20
      value: 88.10470000000001
    - type: mrr_at_100
      value: 88.126
    - type: mrr_at_1000
      value: 88.127
    - type: nauc_ndcg_at_1_max
      value: 37.866499999999995
    - type: nauc_ndcg_at_1_std
      value: -40.9317
    - type: nauc_ndcg_at_1_diff1
      value: 78.09089999999999
    - type: nauc_ndcg_at_3_max
      value: 35.4917
    - type: nauc_ndcg_at_3_std
      value: -48.968
    - type: nauc_ndcg_at_3_diff1
      value: 75.90050000000001
    - type: nauc_ndcg_at_5_max
      value: 35.898799999999994
    - type: nauc_ndcg_at_5_std
      value: -50.5572
    - type: nauc_ndcg_at_5_diff1
      value: 76.6471
    - type: nauc_ndcg_at_10_max
      value: 36.7786
    - type: nauc_ndcg_at_10_std
      value: -49.6733
    - type: nauc_ndcg_at_10_diff1
      value: 76.8147
    - type: nauc_ndcg_at_20_max
      value: 37.1374
    - type: nauc_ndcg_at_20_std
      value: -47.9144
    - type: nauc_ndcg_at_20_diff1
      value: 76.6412
    - type: nauc_ndcg_at_100_max
      value: 37.3452
    - type: nauc_ndcg_at_100_std
      value: -46.0007
    - type: nauc_ndcg_at_100_diff1
      value: 76.6194
    - type: nauc_ndcg_at_1000_max
      value: 37.4848
    - type: nauc_ndcg_at_1000_std
      value: -45.6578
    - type: nauc_ndcg_at_1000_diff1
      value: 76.6001
    - type: nauc_map_at_1_max
      value: 26.7109
    - type: nauc_map_at_1_std
      value: -42.9943
    - type: nauc_map_at_1_diff1
      value: 80.5567
    - type: nauc_map_at_3_max
      value: 32.8491
    - type: nauc_map_at_3_std
      value: -51.64
    - type: nauc_map_at_3_diff1
      value: 77.29700000000001
    - type: nauc_map_at_5_max
      value: 34.4071
    - type: nauc_map_at_5_std
      value: -51.6503
    - type: nauc_map_at_5_diff1
      value: 77.28920000000001
    - type: nauc_map_at_10_max
      value: 35.4934
    - type: nauc_map_at_10_std
      value: -50.0995
    - type: nauc_map_at_10_diff1
      value: 76.9983
    - type: nauc_map_at_20_max
      value: 35.8087
    - type: nauc_map_at_20_std
      value: -48.8069
    - type: nauc_map_at_20_diff1
      value: 76.8026
    - type: nauc_map_at_100_max
      value: 35.8928
    - type: nauc_map_at_100_std
      value: -48.0561
    - type: nauc_map_at_100_diff1
      value: 76.7244
    - type: nauc_map_at_1000_max
      value: 35.924499999999995
    - type: nauc_map_at_1000_std
      value: -47.981899999999996
    - type: nauc_map_at_1000_diff1
      value: 76.7183
    - type: nauc_recall_at_1_max
      value: 26.7109
    - type: nauc_recall_at_1_std
      value: -42.9943
    - type: nauc_recall_at_1_diff1
      value: 80.5567
    - type: nauc_recall_at_3_max
      value: 29.066300000000002
    - type: nauc_recall_at_3_std
      value: -60.1536
    - type: nauc_recall_at_3_diff1
      value: 73.32469999999999
    - type: nauc_recall_at_5_max
      value: 30.1025
    - type: nauc_recall_at_5_std
      value: -67.8779
    - type: nauc_recall_at_5_diff1
      value: 73.13340000000001
    - type: nauc_recall_at_10_max
      value: 33.771699999999996
    - type: nauc_recall_at_10_std
      value: -72.4753
    - type: nauc_recall_at_10_diff1
      value: 74.168
    - type: nauc_recall_at_20_max
      value: 34.8005
    - type: nauc_recall_at_20_std
      value: -68.60579999999999
    - type: nauc_recall_at_20_diff1
      value: 72.6083
    - type: nauc_recall_at_100_max
      value: 33.394800000000004
    - type: nauc_recall_at_100_std
      value: -49.7417
    - type: nauc_recall_at_100_diff1
      value: 73.5857
    - type: nauc_recall_at_1000_max
      value: 48.8898
    - type: nauc_recall_at_1000_std
      value: 54.583800000000004
    - type: nauc_recall_at_1000_diff1
      value: 64.0609
    - type: nauc_precision_at_1_max
      value: 37.866499999999995
    - type: nauc_precision_at_1_std
      value: -40.9317
    - type: nauc_precision_at_1_diff1
      value: 78.09089999999999
    - type: nauc_precision_at_3_max
      value: 8.2308
    - type: nauc_precision_at_3_std
      value: 5.0732
    - type: nauc_precision_at_3_diff1
      value: -19.919
    - type: nauc_precision_at_5_max
      value: 3.0249
    - type: nauc_precision_at_5_std
      value: 16.7897
    - type: nauc_precision_at_5_diff1
      value: -32.0086
    - type: nauc_precision_at_10_max
      value: -0.5459999999999999
    - type: nauc_precision_at_10_std
      value: 27.1262
    - type: nauc_precision_at_10_diff1
      value: -38.8076
    - type: nauc_precision_at_20_max
      value: -2.7663
    - type: nauc_precision_at_20_std
      value: 34.1696
    - type: nauc_precision_at_20_diff1
      value: -42.1088
    - type: nauc_precision_at_100_max
      value: -5.0689
    - type: nauc_precision_at_100_std
      value: 40.023599999999995
    - type: nauc_precision_at_100_diff1
      value: -43.8996
    - type: nauc_precision_at_1000_max
      value: -5.1495
    - type: nauc_precision_at_1000_std
      value: 41.4194
    - type: nauc_precision_at_1000_diff1
      value: -44.219
    - type: nauc_mrr_at_1_max
      value: 37.7695
    - type: nauc_mrr_at_1_std
      value: -41.0563
    - type: nauc_mrr_at_1_diff1
      value: 78.1854
    - type: nauc_mrr_at_3_max
      value: 38.3824
    - type: nauc_mrr_at_3_std
      value: -43.7797
    - type: nauc_mrr_at_3_diff1
      value: 77.0796
    - type: nauc_mrr_at_5_max
      value: 38.5156
    - type: nauc_mrr_at_5_std
      value: -43.8092
    - type: nauc_mrr_at_5_diff1
      value: 77.31710000000001
    - type: nauc_mrr_at_10_max
      value: 38.523
    - type: nauc_mrr_at_10_std
      value: -43.5039
    - type: nauc_mrr_at_10_diff1
      value: 77.375
    - type: nauc_mrr_at_20_max
      value: 38.4635
    - type: nauc_mrr_at_20_std
      value: -43.3619
    - type: nauc_mrr_at_20_diff1
      value: 77.3565
    - type: nauc_mrr_at_100_max
      value: 38.4502
    - type: nauc_mrr_at_100_std
      value: -43.3315
    - type: nauc_mrr_at_100_diff1
      value: 77.3584
    - type: nauc_mrr_at_1000_max
      value: 38.449
    - type: nauc_mrr_at_1000_std
      value: -43.3339
    - type: nauc_mrr_at_1000_diff1
      value: 77.3584
    - type: main_score
      value: 88.735
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: v_measure
      value: 49.1271
    - type: v_measure_std
      value: 4.5517
    - type: main_score
      value: 49.1271
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: v_measure
      value: 61.0626
    - type: v_measure_std
      value: 12.6364
    - type: main_score
      value: 61.0626
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: ndcg_at_1
      value: 23.7
    - type: ndcg_at_3
      value: 19.346
    - type: ndcg_at_5
      value: 17.044999999999998
    - type: ndcg_at_10
      value: 20.347
    - type: ndcg_at_20
      value: 23.237
    - type: ndcg_at_100
      value: 27.923
    - type: ndcg_at_1000
      value: 32.891999999999996
    - type: map_at_1
      value: 4.813
    - type: map_at_3
      value: 8.688
    - type: map_at_5
      value: 10.41
    - type: map_at_10
      value: 12.107999999999999
    - type: map_at_20
      value: 13.187
    - type: map_at_100
      value: 14.113000000000001
    - type: map_at_1000
      value: 14.383000000000001
    - type: recall_at_1
      value: 4.813
    - type: recall_at_3
      value: 11.022
    - type: recall_at_5
      value: 15.242
    - type: recall_at_10
      value: 21.308
    - type: recall_at_20
      value: 28.1
    - type: recall_at_100
      value: 43.335
    - type: recall_at_1000
      value: 67.672
    - type: precision_at_1
      value: 23.7
    - type: precision_at_3
      value: 18.099999999999998
    - type: precision_at_5
      value: 15.0
    - type: precision_at_10
      value: 10.48
    - type: precision_at_20
      value: 6.909999999999999
    - type: precision_at_100
      value: 2.133
    - type: precision_at_1000
      value: 0.333
    - type: mrr_at_1
      value: 23.7
    - type: mrr_at_3
      value: 31.35
    - type: mrr_at_5
      value: 33.650000000000006
    - type: mrr_at_10
      value: 34.9399
    - type: mrr_at_20
      value: 35.5429
    - type: mrr_at_100
      value: 35.9342
    - type: mrr_at_1000
      value: 35.9943
    - type: nauc_ndcg_at_1_max
      value: 20.214499999999997
    - type: nauc_ndcg_at_1_std
      value: 7.2459999999999996
    - type: nauc_ndcg_at_1_diff1
      value: 26.8353
    - type: nauc_ndcg_at_3_max
      value: 23.3459
    - type: nauc_ndcg_at_3_std
      value: 10.9732
    - type: nauc_ndcg_at_3_diff1
      value: 21.0618
    - type: nauc_ndcg_at_5_max
      value: 24.5147
    - type: nauc_ndcg_at_5_std
      value: 13.309000000000001
    - type: nauc_ndcg_at_5_diff1
      value: 20.0975
    - type: nauc_ndcg_at_10_max
      value: 27.0937
    - type: nauc_ndcg_at_10_std
      value: 16.4516
    - type: nauc_ndcg_at_10_diff1
      value: 19.9585
    - type: nauc_ndcg_at_20_max
      value: 28.503600000000002
    - type: nauc_ndcg_at_20_std
      value: 19.1956
    - type: nauc_ndcg_at_20_diff1
      value: 19.508200000000002
    - type: nauc_ndcg_at_100_max
      value: 30.7317
    - type: nauc_ndcg_at_100_std
      value: 23.2169
    - type: nauc_ndcg_at_100_diff1
      value: 19.7085
    - type: nauc_ndcg_at_1000_max
      value: 30.3307
    - type: nauc_ndcg_at_1000_std
      value: 24.7664
    - type: nauc_ndcg_at_1000_diff1
      value: 19.0469
    - type: nauc_map_at_1_max
      value: 20.3702
    - type: nauc_map_at_1_std
      value: 7.219200000000001
    - type: nauc_map_at_1_diff1
      value: 27.0193
    - type: nauc_map_at_3_max
      value: 23.0558
    - type: nauc_map_at_3_std
      value: 9.411999999999999
    - type: nauc_map_at_3_diff1
      value: 21.3691
    - type: nauc_map_at_5_max
      value: 23.763
    - type: nauc_map_at_5_std
      value: 11.228
    - type: nauc_map_at_5_diff1
      value: 20.4299
    - type: nauc_map_at_10_max
      value: 25.6655
    - type: nauc_map_at_10_std
      value: 14.0481
    - type: nauc_map_at_10_diff1
      value: 19.7937
    - type: nauc_map_at_20_max
      value: 26.5994
    - type: nauc_map_at_20_std
      value: 15.820400000000001
    - type: nauc_map_at_20_diff1
      value: 19.476499999999998
    - type: nauc_map_at_100_max
      value: 27.4895
    - type: nauc_map_at_100_std
      value: 17.262
    - type: nauc_map_at_100_diff1
      value: 19.4661
    - type: nauc_map_at_1000_max
      value: 27.5301
    - type: nauc_map_at_1000_std
      value: 17.4927
    - type: nauc_map_at_1000_diff1
      value: 19.4691
    - type: nauc_recall_at_1_max
      value: 20.3702
    - type: nauc_recall_at_1_std
      value: 7.219200000000001
    - type: nauc_recall_at_1_diff1
      value: 27.0193
    - type: nauc_recall_at_3_max
      value: 23.6476
    - type: nauc_recall_at_3_std
      value: 11.9176
    - type: nauc_recall_at_3_diff1
      value: 18.1657
    - type: nauc_recall_at_5_max
      value: 24.8053
    - type: nauc_recall_at_5_std
      value: 15.5205
    - type: nauc_recall_at_5_diff1
      value: 16.4924
    - type: nauc_recall_at_10_max
      value: 27.9864
    - type: nauc_recall_at_10_std
      value: 20.1496
    - type: nauc_recall_at_10_diff1
      value: 16.0154
    - type: nauc_recall_at_20_max
      value: 29.0157
    - type: nauc_recall_at_20_std
      value: 24.374100000000002
    - type: nauc_recall_at_20_diff1
      value: 14.174800000000001
    - type: nauc_recall_at_100_max
      value: 31.245299999999997
    - type: nauc_recall_at_100_std
      value: 32.161699999999996
    - type: nauc_recall_at_100_diff1
      value: 12.9714
    - type: nauc_recall_at_1000_max
      value: 25.6486
    - type: nauc_recall_at_1000_std
      value: 37.1526
    - type: nauc_recall_at_1000_diff1
      value: 6.0907
    - type: nauc_precision_at_1_max
      value: 20.214499999999997
    - type: nauc_precision_at_1_std
      value: 7.2459999999999996
    - type: nauc_precision_at_1_diff1
      value: 26.8353
    - type: nauc_precision_at_3_max
      value: 23.8245
    - type: nauc_precision_at_3_std
      value: 12.2589
    - type: nauc_precision_at_3_diff1
      value: 18.192800000000002
    - type: nauc_precision_at_5_max
      value: 25.3681
    - type: nauc_precision_at_5_std
      value: 15.947700000000001
    - type: nauc_precision_at_5_diff1
      value: 16.6931
    - type: nauc_precision_at_10_max
      value: 28.2682
    - type: nauc_precision_at_10_std
      value: 20.2673
    - type: nauc_precision_at_10_diff1
      value: 15.8977
    - type: nauc_precision_at_20_max
      value: 29.3989
    - type: nauc_precision_at_20_std
      value: 24.5769
    - type: nauc_precision_at_20_diff1
      value: 14.1994
    - type: nauc_precision_at_100_max
      value: 31.418000000000003
    - type: nauc_precision_at_100_std
      value: 32.0978
    - type: nauc_precision_at_100_diff1
      value: 12.768199999999998
    - type: nauc_precision_at_1000_max
      value: 25.501099999999997
    - type: nauc_precision_at_1000_std
      value: 36.477399999999996
    - type: nauc_precision_at_1000_diff1
      value: 5.5335
    - type: nauc_mrr_at_1_max
      value: 20.214499999999997
    - type: nauc_mrr_at_1_std
      value: 7.2459999999999996
    - type: nauc_mrr_at_1_diff1
      value: 26.8353
    - type: nauc_mrr_at_3_max
      value: 22.7925
    - type: nauc_mrr_at_3_std
      value: 10.6945
    - type: nauc_mrr_at_3_diff1
      value: 23.6308
    - type: nauc_mrr_at_5_max
      value: 23.427799999999998
    - type: nauc_mrr_at_5_std
      value: 11.8634
    - type: nauc_mrr_at_5_diff1
      value: 23.0875
    - type: nauc_mrr_at_10_max
      value: 24.0918
    - type: nauc_mrr_at_10_std
      value: 12.4753
    - type: nauc_mrr_at_10_diff1
      value: 23.352999999999998
    - type: nauc_mrr_at_20_max
      value: 24.078
    - type: nauc_mrr_at_20_std
      value: 12.5849
    - type: nauc_mrr_at_20_diff1
      value: 23.3351
    - type: nauc_mrr_at_100_max
      value: 24.0858
    - type: nauc_mrr_at_100_std
      value: 12.5772
    - type: nauc_mrr_at_100_diff1
      value: 23.4778
    - type: nauc_mrr_at_1000_max
      value: 24.058799999999998
    - type: nauc_mrr_at_1000_std
      value: 12.549
    - type: nauc_mrr_at_1000_diff1
      value: 23.4713
    - type: main_score
      value: 20.347
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: pearson
      value: 75.7747
    - type: spearman
      value: 71.3142
    - type: cosine_pearson
      value: 75.7747
    - type: cosine_spearman
      value: 71.3142
    - type: manhattan_pearson
      value: 73.8759
    - type: manhattan_spearman
      value: 71.1003
    - type: euclidean_pearson
      value: 74.088
    - type: euclidean_spearman
      value: 71.3142
    - type: main_score
      value: 71.3142
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: pearson
      value: 72.5903
    - type: spearman
      value: 70.6581
    - type: cosine_pearson
      value: 72.5903
    - type: cosine_spearman
      value: 70.6581
    - type: manhattan_pearson
      value: 69.2077
    - type: manhattan_spearman
      value: 70.4521
    - type: euclidean_pearson
      value: 69.41720000000001
    - type: euclidean_spearman
      value: 70.6581
    - type: main_score
      value: 70.6581
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: pearson
      value: 73.1686
    - type: spearman
      value: 77.4225
    - type: cosine_pearson
      value: 73.1686
    - type: cosine_spearman
      value: 77.4225
    - type: manhattan_pearson
      value: 76.2481
    - type: manhattan_spearman
      value: 77.325
    - type: euclidean_pearson
      value: 76.3568
    - type: euclidean_spearman
      value: 77.4225
    - type: main_score
      value: 77.4225
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: pearson
      value: 74.46340000000001
    - type: spearman
      value: 72.9162
    - type: cosine_pearson
      value: 74.46340000000001
    - type: cosine_spearman
      value: 72.9162
    - type: manhattan_pearson
      value: 73.8079
    - type: manhattan_spearman
      value: 72.8704
    - type: euclidean_pearson
      value: 73.8244
    - type: euclidean_spearman
      value: 72.9162
    - type: main_score
      value: 72.9162
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: pearson
      value: 80.1161
    - type: spearman
      value: 81.83200000000001
    - type: cosine_pearson
      value: 80.1161
    - type: cosine_spearman
      value: 81.83200000000001
    - type: manhattan_pearson
      value: 81.573
    - type: manhattan_spearman
      value: 81.807
    - type: euclidean_pearson
      value: 81.59490000000001
    - type: euclidean_spearman
      value: 81.83200000000001
    - type: main_score
      value: 81.83200000000001
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: pearson
      value: 78.8244
    - type: spearman
      value: 81.2262
    - type: cosine_pearson
      value: 78.8244
    - type: cosine_spearman
      value: 81.2262
    - type: manhattan_pearson
      value: 80.6177
    - type: manhattan_spearman
      value: 81.1361
    - type: euclidean_pearson
      value: 80.7347
    - type: euclidean_spearman
      value: 81.2262
    - type: main_score
      value: 81.2262
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS17 (es-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 67.9751
    - type: spearman
      value: 68.92099999999999
    - type: cosine_pearson
      value: 67.9751
    - type: cosine_spearman
      value: 68.92099999999999
    - type: manhattan_pearson
      value: 68.9355
    - type: manhattan_spearman
      value: 68.777
    - type: euclidean_pearson
      value: 69.11410000000001
    - type: euclidean_spearman
      value: 68.92099999999999
    - type: main_score
      value: 68.92099999999999
    task:
      type: STS
  - dataset:
      config: fr-en
      name: MTEB STS17 (fr-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 72.08449999999999
    - type: spearman
      value: 74.6931
    - type: cosine_pearson
      value: 72.08449999999999
    - type: cosine_spearman
      value: 74.6931
    - type: manhattan_pearson
      value: 73.52
    - type: manhattan_spearman
      value: 74.7097
    - type: euclidean_pearson
      value: 73.62180000000001
    - type: euclidean_spearman
      value: 74.6931
    - type: main_score
      value: 74.6931
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 80.528
    - type: spearman
      value: 84.10459999999999
    - type: cosine_pearson
      value: 80.528
    - type: cosine_spearman
      value: 84.10459999999999
    - type: manhattan_pearson
      value: 83.1537
    - type: manhattan_spearman
      value: 84.0952
    - type: euclidean_pearson
      value: 83.337
    - type: euclidean_spearman
      value: 84.10459999999999
    - type: main_score
      value: 84.10459999999999
    task:
      type: STS
  - dataset:
      config: en-tr
      name: MTEB STS17 (en-tr)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 49.641400000000004
    - type: spearman
      value: 48.9413
    - type: cosine_pearson
      value: 49.641400000000004
    - type: cosine_spearman
      value: 48.9413
    - type: manhattan_pearson
      value: 51.434000000000005
    - type: manhattan_spearman
      value: 49.1595
    - type: euclidean_pearson
      value: 50.867799999999995
    - type: euclidean_spearman
      value: 48.9413
    - type: main_score
      value: 48.9413
    task:
      type: STS
  - dataset:
      config: it-en
      name: MTEB STS17 (it-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 71.2577
    - type: spearman
      value: 73.82419999999999
    - type: cosine_pearson
      value: 71.2577
    - type: cosine_spearman
      value: 73.82419999999999
    - type: manhattan_pearson
      value: 71.9329
    - type: manhattan_spearman
      value: 73.4651
    - type: euclidean_pearson
      value: 72.2771
    - type: euclidean_spearman
      value: 73.82419999999999
    - type: main_score
      value: 73.82419999999999
    task:
      type: STS
  - dataset:
      config: nl-en
      name: MTEB STS17 (nl-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 64.1562
    - type: spearman
      value: 64.8766
    - type: cosine_pearson
      value: 64.1562
    - type: cosine_spearman
      value: 64.8766
    - type: manhattan_pearson
      value: 64.16579999999999
    - type: manhattan_spearman
      value: 64.1931
    - type: euclidean_pearson
      value: 64.6169
    - type: euclidean_spearman
      value: 64.8766
    - type: main_score
      value: 64.8766
    task:
      type: STS
  - dataset:
      config: en-ar
      name: MTEB STS17 (en-ar)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 42.257400000000004
    - type: spearman
      value: 43.2176
    - type: cosine_pearson
      value: 42.257400000000004
    - type: cosine_spearman
      value: 43.2176
    - type: manhattan_pearson
      value: 43.5359
    - type: manhattan_spearman
      value: 42.4143
    - type: euclidean_pearson
      value: 43.6717
    - type: euclidean_spearman
      value: 43.2176
    - type: main_score
      value: 43.2176
    task:
      type: STS
  - dataset:
      config: en-de
      name: MTEB STS17 (en-de)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: pearson
      value: 74.0088
    - type: spearman
      value: 75.8687
    - type: cosine_pearson
      value: 74.0088
    - type: cosine_spearman
      value: 75.8687
    - type: manhattan_pearson
      value: 74.8505
    - type: manhattan_spearman
      value: 75.6101
    - type: euclidean_pearson
      value: 75.1303
    - type: euclidean_spearman
      value: 75.8687
    - type: main_score
      value: 75.8687
    task:
      type: STS
  - dataset:
      config: zh-en
      name: MTEB STS22 (zh-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 68.0842
    - type: spearman
      value: 69.4346
    - type: cosine_pearson
      value: 68.0842
    - type: cosine_spearman
      value: 69.4346
    - type: manhattan_pearson
      value: 69.9982
    - type: manhattan_spearman
      value: 69.8952
    - type: euclidean_pearson
      value: 69.6375
    - type: euclidean_spearman
      value: 69.4346
    - type: main_score
      value: 69.4346
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS22 (es-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 76.3695
    - type: spearman
      value: 78.88730000000001
    - type: cosine_pearson
      value: 76.3695
    - type: cosine_spearman
      value: 78.88730000000001
    - type: manhattan_pearson
      value: 79.0721
    - type: manhattan_spearman
      value: 79.1151
    - type: euclidean_pearson
      value: 78.783
    - type: euclidean_spearman
      value: 78.88730000000001
    - type: main_score
      value: 78.88730000000001
    task:
      type: STS
  - dataset:
      config: de-en
      name: MTEB STS22 (de-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 60.59139999999999
    - type: spearman
      value: 52.692099999999996
    - type: cosine_pearson
      value: 60.59139999999999
    - type: cosine_spearman
      value: 52.692099999999996
    - type: manhattan_pearson
      value: 64.66499999999999
    - type: manhattan_spearman
      value: 53.09009999999999
    - type: euclidean_pearson
      value: 64.5541
    - type: euclidean_spearman
      value: 52.692099999999996
    - type: main_score
      value: 52.692099999999996
    task:
      type: STS
  - dataset:
      config: pl-en
      name: MTEB STS22 (pl-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 77.8405
    - type: spearman
      value: 76.6188
    - type: cosine_pearson
      value: 77.8405
    - type: cosine_spearman
      value: 76.6188
    - type: manhattan_pearson
      value: 76.6598
    - type: manhattan_spearman
      value: 76.3583
    - type: euclidean_pearson
      value: 77.1442
    - type: euclidean_spearman
      value: 76.6188
    - type: main_score
      value: 76.6188
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: pearson
      value: 69.8017
    - type: spearman
      value: 68.7734
    - type: cosine_pearson
      value: 69.8017
    - type: cosine_spearman
      value: 68.7734
    - type: manhattan_pearson
      value: 70.6884
    - type: manhattan_spearman
      value: 68.2974
    - type: euclidean_pearson
      value: 70.7968
    - type: euclidean_spearman
      value: 68.7734
    - type: main_score
      value: 68.7734
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: pearson
      value: 73.3293
    - type: spearman
      value: 76.00919999999999
    - type: cosine_pearson
      value: 73.3293
    - type: cosine_spearman
      value: 76.00919999999999
    - type: manhattan_pearson
      value: 75.0184
    - type: manhattan_spearman
      value: 75.8014
    - type: euclidean_pearson
      value: 75.2638
    - type: euclidean_spearman
      value: 76.00919999999999
    - type: main_score
      value: 76.00919999999999
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: map
      value: 77.3669
    - type: mrr
      value: 93.5985
    - type: nAUC_map_max
      value: 50.2355
    - type: nAUC_map_std
      value: 65.5401
    - type: nAUC_map_diff1
      value: 9.6333
    - type: nAUC_mrr_max
      value: 76.5201
    - type: nAUC_mrr_std
      value: 74.7401
    - type: nAUC_mrr_diff1
      value: 53.170899999999996
    - type: main_score
      value: 77.3669
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: ndcg_at_1
      value: 61.0
    - type: ndcg_at_3
      value: 67.589
    - type: ndcg_at_5
      value: 68.948
    - type: ndcg_at_10
      value: 71.8
    - type: ndcg_at_20
      value: 72.595
    - type: ndcg_at_100
      value: 74.138
    - type: ndcg_at_1000
      value: 74.83800000000001
    - type: map_at_1
      value: 57.74399999999999
    - type: map_at_3
      value: 64.866
    - type: map_at_5
      value: 66.018
    - type: map_at_10
      value: 67.535
    - type: map_at_20
      value: 67.77
    - type: map_at_100
      value: 68.011
    - type: map_at_1000
      value: 68.042
    - type: recall_at_1
      value: 57.74399999999999
    - type: recall_at_3
      value: 71.906
    - type: recall_at_5
      value: 75.344
    - type: recall_at_10
      value: 83.2
    - type: recall_at_20
      value: 86.26700000000001
    - type: recall_at_100
      value: 94.333
    - type: recall_at_1000
      value: 99.667
    - type: precision_at_1
      value: 61.0
    - type: precision_at_3
      value: 26.111
    - type: precision_at_5
      value: 16.8
    - type: precision_at_10
      value: 9.5
    - type: precision_at_20
      value: 4.933
    - type: precision_at_100
      value: 1.073
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 61.0
    - type: mrr_at_3
      value: 67.4444
    - type: mrr_at_5
      value: 68.0778
    - type: mrr_at_10
      value: 69.0483
    - type: mrr_at_20
      value: 69.2333
    - type: mrr_at_100
      value: 69.4403
    - type: mrr_at_1000
      value: 69.4708
    - type: nauc_ndcg_at_1_max
      value: 53.481500000000004
    - type: nauc_ndcg_at_1_std
      value: 8.227
    - type: nauc_ndcg_at_1_diff1
      value: 72.0771
    - type: nauc_ndcg_at_3_max
      value: 57.0147
    - type: nauc_ndcg_at_3_std
      value: 5.2435
    - type: nauc_ndcg_at_3_diff1
      value: 68.8841
    - type: nauc_ndcg_at_5_max
      value: 57.4675
    - type: nauc_ndcg_at_5_std
      value: 8.4709
    - type: nauc_ndcg_at_5_diff1
      value: 67.2977
    - type: nauc_ndcg_at_10_max
      value: 60.3957
    - type: nauc_ndcg_at_10_std
      value: 11.3174
    - type: nauc_ndcg_at_10_diff1
      value: 67.8332
    - type: nauc_ndcg_at_20_max
      value: 60.3607
    - type: nauc_ndcg_at_20_std
      value: 11.9948
    - type: nauc_ndcg_at_20_diff1
      value: 68.1122
    - type: nauc_ndcg_at_100_max
      value: 59.5293
    - type: nauc_ndcg_at_100_std
      value: 11.697799999999999
    - type: nauc_ndcg_at_100_diff1
      value: 68.453
    - type: nauc_ndcg_at_1000_max
      value: 58.8931
    - type: nauc_ndcg_at_1000_std
      value: 10.876199999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 68.5746
    - type: nauc_map_at_1_max
      value: 49.762299999999996
    - type: nauc_map_at_1_std
      value: -0.2785
    - type: nauc_map_at_1_diff1
      value: 71.9072
    - type: nauc_map_at_3_max
      value: 54.108599999999996
    - type: nauc_map_at_3_std
      value: 2.0995
    - type: nauc_map_at_3_diff1
      value: 69.3459
    - type: nauc_map_at_5_max
      value: 55.257
    - type: nauc_map_at_5_std
      value: 5.5776
    - type: nauc_map_at_5_diff1
      value: 68.3314
    - type: nauc_map_at_10_max
      value: 57.1506
    - type: nauc_map_at_10_std
      value: 7.4561
    - type: nauc_map_at_10_diff1
      value: 68.8482
    - type: nauc_map_at_20_max
      value: 57.126200000000004
    - type: nauc_map_at_20_std
      value: 7.6833
    - type: nauc_map_at_20_diff1
      value: 68.9132
    - type: nauc_map_at_100_max
      value: 56.9874
    - type: nauc_map_at_100_std
      value: 7.7405
    - type: nauc_map_at_100_diff1
      value: 68.9371
    - type: nauc_map_at_1000_max
      value: 56.959199999999996
    - type: nauc_map_at_1000_std
      value: 7.709499999999999
    - type: nauc_map_at_1000_diff1
      value: 68.9444
    - type: nauc_recall_at_1_max
      value: 49.762299999999996
    - type: nauc_recall_at_1_std
      value: -0.2785
    - type: nauc_recall_at_1_diff1
      value: 71.9072
    - type: nauc_recall_at_3_max
      value: 58.22580000000001
    - type: nauc_recall_at_3_std
      value: 2.3135
    - type: nauc_recall_at_3_diff1
      value: 65.5868
    - type: nauc_recall_at_5_max
      value: 60.4096
    - type: nauc_recall_at_5_std
      value: 11.7662
    - type: nauc_recall_at_5_diff1
      value: 61.5815
    - type: nauc_recall_at_10_max
      value: 72.74629999999999
    - type: nauc_recall_at_10_std
      value: 22.148
    - type: nauc_recall_at_10_diff1
      value: 62.2401
    - type: nauc_recall_at_20_max
      value: 74.9625
    - type: nauc_recall_at_20_std
      value: 28.1358
    - type: nauc_recall_at_20_diff1
      value: 63.240700000000004
    - type: nauc_recall_at_100_max
      value: 79.15910000000001
    - type: nauc_recall_at_100_std
      value: 39.4162
    - type: nauc_recall_at_100_diff1
      value: 65.733
    - type: nauc_recall_at_1000_max
      value: 100.0
    - type: nauc_recall_at_1000_std
      value: 72.2222
    - type: nauc_recall_at_1000_diff1
      value: 72.2222
    - type: nauc_precision_at_1_max
      value: 53.481500000000004
    - type: nauc_precision_at_1_std
      value: 8.227
    - type: nauc_precision_at_1_diff1
      value: 72.0771
    - type: nauc_precision_at_3_max
      value: 55.675799999999995
    - type: nauc_precision_at_3_std
      value: 23.9615
    - type: nauc_precision_at_3_diff1
      value: 48.1199
    - type: nauc_precision_at_5_max
      value: 50.503299999999996
    - type: nauc_precision_at_5_std
      value: 36.9259
    - type: nauc_precision_at_5_diff1
      value: 31.769399999999997
    - type: nauc_precision_at_10_max
      value: 45.4878
    - type: nauc_precision_at_10_std
      value: 44.0469
    - type: nauc_precision_at_10_diff1
      value: 16.666900000000002
    - type: nauc_precision_at_20_max
      value: 40.2908
    - type: nauc_precision_at_20_std
      value: 47.330600000000004
    - type: nauc_precision_at_20_diff1
      value: 11.0043
    - type: nauc_precision_at_100_max
      value: 27.4643
    - type: nauc_precision_at_100_std
      value: 53.0014
    - type: nauc_precision_at_100_diff1
      value: -4.8238
    - type: nauc_precision_at_1000_max
      value: 15.755099999999999
    - type: nauc_precision_at_1000_std
      value: 56.634499999999996
    - type: nauc_precision_at_1000_diff1
      value: -21.124100000000002
    - type: nauc_mrr_at_1_max
      value: 53.481500000000004
    - type: nauc_mrr_at_1_std
      value: 8.227
    - type: nauc_mrr_at_1_diff1
      value: 72.0771
    - type: nauc_mrr_at_3_max
      value: 57.6662
    - type: nauc_mrr_at_3_std
      value: 9.2816
    - type: nauc_mrr_at_3_diff1
      value: 69.8276
    - type: nauc_mrr_at_5_max
      value: 57.6565
    - type: nauc_mrr_at_5_std
      value: 10.422099999999999
    - type: nauc_mrr_at_5_diff1
      value: 69.0964
    - type: nauc_mrr_at_10_max
      value: 58.000099999999996
    - type: nauc_mrr_at_10_std
      value: 10.957600000000001
    - type: nauc_mrr_at_10_diff1
      value: 69.0098
    - type: nauc_mrr_at_20_max
      value: 58.0066
    - type: nauc_mrr_at_20_std
      value: 11.0139
    - type: nauc_mrr_at_20_diff1
      value: 69.1278
    - type: nauc_mrr_at_100_max
      value: 57.9072
    - type: nauc_mrr_at_100_std
      value: 10.9621
    - type: nauc_mrr_at_100_diff1
      value: 69.1925
    - type: nauc_mrr_at_1000_max
      value: 57.87949999999999
    - type: nauc_mrr_at_1000_std
      value: 10.934199999999999
    - type: nauc_mrr_at_1000_diff1
      value: 69.2004
    - type: main_score
      value: 71.8
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 99.8248
    - type: similarity_accuracy_threshold
      value: 74.6155
    - type: similarity_f1
      value: 91.12780000000001
    - type: similarity_f1_threshold
      value: 74.2422
    - type: similarity_precision
      value: 91.3568
    - type: similarity_recall
      value: 90.9
    - type: similarity_ap
      value: 96.00319999999999
    - type: cosine_accuracy
      value: 99.8248
    - type: cosine_accuracy_threshold
      value: 74.6155
    - type: cosine_f1
      value: 91.12780000000001
    - type: cosine_f1_threshold
      value: 74.2422
    - type: cosine_precision
      value: 91.3568
    - type: cosine_recall
      value: 90.9
    - type: cosine_ap
      value: 96.00319999999999
    - type: manhattan_accuracy
      value: 99.8257
    - type: manhattan_accuracy_threshold
      value: 1574.1653
    - type: manhattan_f1
      value: 91.1531
    - type: manhattan_f1_threshold
      value: 1595.7924
    - type: manhattan_precision
      value: 90.6126
    - type: manhattan_recall
      value: 91.7
    - type: manhattan_ap
      value: 95.9848
    - type: euclidean_accuracy
      value: 99.8248
    - type: euclidean_accuracy_threshold
      value: 71.2523
    - type: euclidean_f1
      value: 91.12780000000001
    - type: euclidean_f1_threshold
      value: 71.7744
    - type: euclidean_precision
      value: 91.3568
    - type: euclidean_recall
      value: 90.9
    - type: euclidean_ap
      value: 96.00319999999999
    - type: dot_accuracy
      value: 99.8248
    - type: dot_accuracy_threshold
      value: 74.6155
    - type: dot_f1
      value: 91.12780000000001
    - type: dot_f1_threshold
      value: 74.2422
    - type: dot_precision
      value: 91.3568
    - type: dot_recall
      value: 90.9
    - type: dot_ap
      value: 96.00319999999999
    - type: max_accuracy
      value: 99.8257
    - type: max_f1
      value: 91.1531
    - type: max_precision
      value: 91.3568
    - type: max_recall
      value: 91.7
    - type: max_ap
      value: 96.00319999999999
    - type: main_score
      value: 96.00319999999999
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: v_measure
      value: 61.3985
    - type: v_measure_std
      value: 5.2151000000000005
    - type: main_score
      value: 61.3985
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: v_measure
      value: 36.1433
    - type: v_measure_std
      value: 1.5853
    - type: main_score
      value: 36.1433
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: map
      value: 50.47580000000001
    - type: mrr
      value: 51.221399999999996
    - type: nAUC_map_max
      value: 10.1311
    - type: nAUC_map_std
      value: 6.239999999999999
    - type: nAUC_map_diff1
      value: 36.3486
    - type: nAUC_mrr_max
      value: 10.9306
    - type: nAUC_mrr_std
      value: 6.7909
    - type: nAUC_mrr_diff1
      value: 36.5536
    - type: main_score
      value: 50.47580000000001
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: pearson
      value: 29.8474
    - type: spearman
      value: 29.391099999999998
    - type: cosine_spearman
      value: 29.391099999999998
    - type: cosine_pearson
      value: 29.8474
    - type: dot_spearman
      value: 29.391099999999998
    - type: dot_pearson
      value: 29.8474
    - type: main_score
      value: 29.391099999999998
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: ndcg_at_1
      value: 85.0
    - type: ndcg_at_3
      value: 84.58099999999999
    - type: ndcg_at_5
      value: 83.573
    - type: ndcg_at_10
      value: 80.285
    - type: ndcg_at_20
      value: 77.469
    - type: ndcg_at_100
      value: 63.524
    - type: ndcg_at_1000
      value: 56.839
    - type: map_at_1
      value: 0.22799999999999998
    - type: map_at_3
      value: 0.656
    - type: map_at_5
      value: 1.078
    - type: map_at_10
      value: 2.0389999999999997
    - type: map_at_20
      value: 3.7670000000000003
    - type: map_at_100
      value: 12.8
    - type: map_at_1000
      value: 31.575999999999997
    - type: recall_at_1
      value: 0.22799999999999998
    - type: recall_at_3
      value: 0.695
    - type: recall_at_5
      value: 1.151
    - type: recall_at_10
      value: 2.215
    - type: recall_at_20
      value: 4.232
    - type: recall_at_100
      value: 15.828000000000001
    - type: recall_at_1000
      value: 53.516
    - type: precision_at_1
      value: 90.0
    - type: precision_at_3
      value: 89.333
    - type: precision_at_5
      value: 88.8
    - type: precision_at_10
      value: 84.6
    - type: precision_at_20
      value: 81.6
    - type: precision_at_100
      value: 65.64
    - type: precision_at_1000
      value: 25.380000000000003
    - type: mrr_at_1
      value: 90.0
    - type: mrr_at_3
      value: 94.6667
    - type: mrr_at_5
      value: 94.6667
    - type: mrr_at_10
      value: 94.6667
    - type: mrr_at_20
      value: 94.6667
    - type: mrr_at_100
      value: 94.6667
    - type: mrr_at_1000
      value: 94.6667
    - type: nauc_ndcg_at_1_max
      value: -5.4637
    - type: nauc_ndcg_at_1_std
      value: 14.5981
    - type: nauc_ndcg_at_1_diff1
      value: 13.6414
    - type: nauc_ndcg_at_3_max
      value: 10.9521
    - type: nauc_ndcg_at_3_std
      value: 39.8204
    - type: nauc_ndcg_at_3_diff1
      value: -13.839799999999999
    - type: nauc_ndcg_at_5_max
      value: 20.9664
    - type: nauc_ndcg_at_5_std
      value: 50.876999999999995
    - type: nauc_ndcg_at_5_diff1
      value: -15.3559
    - type: nauc_ndcg_at_10_max
      value: 34.053
    - type: nauc_ndcg_at_10_std
      value: 59.1102
    - type: nauc_ndcg_at_10_diff1
      value: -23.3868
    - type: nauc_ndcg_at_20_max
      value: 39.5081
    - type: nauc_ndcg_at_20_std
      value: 70.287
    - type: nauc_ndcg_at_20_diff1
      value: -36.7999
    - type: nauc_ndcg_at_100_max
      value: 38.8671
    - type: nauc_ndcg_at_100_std
      value: 80.5875
    - type: nauc_ndcg_at_100_diff1
      value: -28.766599999999997
    - type: nauc_ndcg_at_1000_max
      value: 45.4017
    - type: nauc_ndcg_at_1000_std
      value: 73.1799
    - type: nauc_ndcg_at_1000_diff1
      value: -13.5374
    - type: nauc_map_at_1_max
      value: -15.7901
    - type: nauc_map_at_1_std
      value: -14.5481
    - type: nauc_map_at_1_diff1
      value: 35.3307
    - type: nauc_map_at_3_max
      value: -4.8114
    - type: nauc_map_at_3_std
      value: -8.3704
    - type: nauc_map_at_3_diff1
      value: 26.2918
    - type: nauc_map_at_5_max
      value: -0.9780000000000001
    - type: nauc_map_at_5_std
      value: -3.4821
    - type: nauc_map_at_5_diff1
      value: 25.469
    - type: nauc_map_at_10_max
      value: 4.2075000000000005
    - type: nauc_map_at_10_std
      value: 1.5897999999999999
    - type: nauc_map_at_10_diff1
      value: 20.0578
    - type: nauc_map_at_20_max
      value: 11.1623
    - type: nauc_map_at_20_std
      value: 13.4387
    - type: nauc_map_at_20_diff1
      value: 12.9992
    - type: nauc_map_at_100_max
      value: 21.7341
    - type: nauc_map_at_100_std
      value: 51.2629
    - type: nauc_map_at_100_diff1
      value: 6.3333
    - type: nauc_map_at_1000_max
      value: 45.7524
    - type: nauc_map_at_1000_std
      value: 79.5106
    - type: nauc_map_at_1000_diff1
      value: -16.2395
    - type: nauc_recall_at_1_max
      value: -15.7901
    - type: nauc_recall_at_1_std
      value: -14.5481
    - type: nauc_recall_at_1_diff1
      value: 35.3307
    - type: nauc_recall_at_3_max
      value: -3.9641
    - type: nauc_recall_at_3_std
      value: -11.6408
    - type: nauc_recall_at_3_diff1
      value: 26.243
    - type: nauc_recall_at_5_max
      value: -1.3654
    - type: nauc_recall_at_5_std
      value: -7.7433000000000005
    - type: nauc_recall_at_5_diff1
      value: 25.5058
    - type: nauc_recall_at_10_max
      value: 0.6649999999999999
    - type: nauc_recall_at_10_std
      value: -5.8116
    - type: nauc_recall_at_10_diff1
      value: 23.0906
    - type: nauc_recall_at_20_max
      value: 4.398
    - type: nauc_recall_at_20_std
      value: 2.5343999999999998
    - type: nauc_recall_at_20_diff1
      value: 17.0552
    - type: nauc_recall_at_100_max
      value: 12.8082
    - type: nauc_recall_at_100_std
      value: 32.912400000000005
    - type: nauc_recall_at_100_diff1
      value: 14.6836
    - type: nauc_recall_at_1000_max
      value: 42.261500000000005
    - type: nauc_recall_at_1000_std
      value: 60.5793
    - type: nauc_recall_at_1000_diff1
      value: -6.1521
    - type: nauc_precision_at_1_max
      value: -7.077500000000001
    - type: nauc_precision_at_1_std
      value: 19.7572
    - type: nauc_precision_at_1_diff1
      value: 21.9141
    - type: nauc_precision_at_3_max
      value: 30.758799999999997
    - type: nauc_precision_at_3_std
      value: 53.897099999999995
    - type: nauc_precision_at_3_diff1
      value: -25.885399999999997
    - type: nauc_precision_at_5_max
      value: 43.5162
    - type: nauc_precision_at_5_std
      value: 66.8874
    - type: nauc_precision_at_5_diff1
      value: -20.7483
    - type: nauc_precision_at_10_max
      value: 46.7798
    - type: nauc_precision_at_10_std
      value: 63.677499999999995
    - type: nauc_precision_at_10_diff1
      value: -21.1182
    - type: nauc_precision_at_20_max
      value: 49.8621
    - type: nauc_precision_at_20_std
      value: 79.1937
    - type: nauc_precision_at_20_diff1
      value: -38.9691
    - type: nauc_precision_at_100_max
      value: 42.8699
    - type: nauc_precision_at_100_std
      value: 83.7695
    - type: nauc_precision_at_100_diff1
      value: -26.794
    - type: nauc_precision_at_1000_max
      value: 42.7819
    - type: nauc_precision_at_1000_std
      value: 53.815900000000006
    - type: nauc_precision_at_1000_diff1
      value: -34.4047
    - type: nauc_mrr_at_1_max
      value: -7.077500000000001
    - type: nauc_mrr_at_1_std
      value: 19.7572
    - type: nauc_mrr_at_1_diff1
      value: 21.9141
    - type: nauc_mrr_at_3_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_3_std
      value: 21.9859
    - type: nauc_mrr_at_3_diff1
      value: 25.0584
    - type: nauc_mrr_at_5_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_5_std
      value: 21.9859
    - type: nauc_mrr_at_5_diff1
      value: 25.0584
    - type: nauc_mrr_at_10_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_10_std
      value: 21.9859
    - type: nauc_mrr_at_10_diff1
      value: 25.0584
    - type: nauc_mrr_at_20_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_20_std
      value: 21.9859
    - type: nauc_mrr_at_20_diff1
      value: 25.0584
    - type: nauc_mrr_at_100_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_100_std
      value: 21.9859
    - type: nauc_mrr_at_100_diff1
      value: 25.0584
    - type: nauc_mrr_at_1000_max
      value: -2.1212999999999997
    - type: nauc_mrr_at_1000_std
      value: 21.9859
    - type: nauc_mrr_at_1000_diff1
      value: 25.0584
    - type: main_score
      value: 80.285
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: ndcg_at_1
      value: 33.672999999999995
    - type: ndcg_at_3
      value: 34.392
    - type: ndcg_at_5
      value: 32.606
    - type: ndcg_at_10
      value: 29.767
    - type: ndcg_at_20
      value: 30.353
    - type: ndcg_at_100
      value: 41.094
    - type: ndcg_at_1000
      value: 51.937
    - type: map_at_1
      value: 2.64
    - type: map_at_3
      value: 6.428000000000001
    - type: map_at_5
      value: 8.792
    - type: map_at_10
      value: 11.882
    - type: map_at_20
      value: 14.818000000000001
    - type: map_at_100
      value: 18.613
    - type: map_at_1000
      value: 20.233
    - type: recall_at_1
      value: 2.64
    - type: recall_at_3
      value: 7.951999999999999
    - type: recall_at_5
      value: 11.898
    - type: recall_at_10
      value: 18.782
    - type: recall_at_20
      value: 27.488
    - type: recall_at_100
      value: 51.337999999999994
    - type: recall_at_1000
      value: 84.399
    - type: precision_at_1
      value: 36.735
    - type: precision_at_3
      value: 36.735
    - type: precision_at_5
      value: 33.061
    - type: precision_at_10
      value: 26.122
    - type: precision_at_20
      value: 19.898
    - type: precision_at_100
      value: 8.429
    - type: precision_at_1000
      value: 1.5650000000000002
    - type: mrr_at_1
      value: 36.7347
    - type: mrr_at_3
      value: 51.7007
    - type: mrr_at_5
      value: 54.65989999999999
    - type: mrr_at_10
      value: 55.8868
    - type: mrr_at_20
      value: 56.2944
    - type: mrr_at_100
      value: 56.360200000000006
    - type: mrr_at_1000
      value: 56.360200000000006
    - type: nauc_ndcg_at_1_max
      value: -23.0012
    - type: nauc_ndcg_at_1_std
      value: -9.474
    - type: nauc_ndcg_at_1_diff1
      value: 15.5991
    - type: nauc_ndcg_at_3_max
      value: -16.1454
    - type: nauc_ndcg_at_3_std
      value: -26.226100000000002
    - type: nauc_ndcg_at_3_diff1
      value: 22.9111
    - type: nauc_ndcg_at_5_max
      value: -20.3259
    - type: nauc_ndcg_at_5_std
      value: -23.3106
    - type: nauc_ndcg_at_5_diff1
      value: 20.112199999999998
    - type: nauc_ndcg_at_10_max
      value: -17.4616
    - type: nauc_ndcg_at_10_std
      value: -15.5791
    - type: nauc_ndcg_at_10_diff1
      value: 13.2876
    - type: nauc_ndcg_at_20_max
      value: -20.0683
    - type: nauc_ndcg_at_20_std
      value: -10.979899999999999
    - type: nauc_ndcg_at_20_diff1
      value: 5.929
    - type: nauc_ndcg_at_100_max
      value: -21.096899999999998
    - type: nauc_ndcg_at_100_std
      value: 13.212399999999999
    - type: nauc_ndcg_at_100_diff1
      value: 3.9886
    - type: nauc_ndcg_at_1000_max
      value: -14.1544
    - type: nauc_ndcg_at_1000_std
      value: 19.5979
    - type: nauc_ndcg_at_1000_diff1
      value: 1.2742
    - type: nauc_map_at_1_max
      value: -18.123900000000003
    - type: nauc_map_at_1_std
      value: -17.8031
    - type: nauc_map_at_1_diff1
      value: 21.032899999999998
    - type: nauc_map_at_3_max
      value: -6.7797
    - type: nauc_map_at_3_std
      value: -28.810299999999998
    - type: nauc_map_at_3_diff1
      value: 16.2912
    - type: nauc_map_at_5_max
      value: -7.620699999999999
    - type: nauc_map_at_5_std
      value: -27.6982
    - type: nauc_map_at_5_diff1
      value: 14.813100000000002
    - type: nauc_map_at_10_max
      value: -5.1492
    - type: nauc_map_at_10_std
      value: -23.885
    - type: nauc_map_at_10_diff1
      value: 6.9926
    - type: nauc_map_at_20_max
      value: -9.6331
    - type: nauc_map_at_20_std
      value: -19.215
    - type: nauc_map_at_20_diff1
      value: 0.6491
    - type: nauc_map_at_100_max
      value: -9.7297
    - type: nauc_map_at_100_std
      value: -6.9502999999999995
    - type: nauc_map_at_100_diff1
      value: -1.5897999999999999
    - type: nauc_map_at_1000_max
      value: -8.9517
    - type: nauc_map_at_1000_std
      value: -3.9941999999999998
    - type: nauc_map_at_1000_diff1
      value: -2.8158
    - type: nauc_recall_at_1_max
      value: -18.123900000000003
    - type: nauc_recall_at_1_std
      value: -17.8031
    - type: nauc_recall_at_1_diff1
      value: 21.032899999999998
    - type: nauc_recall_at_3_max
      value: -12.1006
    - type: nauc_recall_at_3_std
      value: -35.3199
    - type: nauc_recall_at_3_diff1
      value: 12.044
    - type: nauc_recall_at_5_max
      value: -15.7192
    - type: nauc_recall_at_5_std
      value: -30.7299
    - type: nauc_recall_at_5_diff1
      value: 8.3249
    - type: nauc_recall_at_10_max
      value: -13.3968
    - type: nauc_recall_at_10_std
      value: -19.2107
    - type: nauc_recall_at_10_diff1
      value: 0.1315
    - type: nauc_recall_at_20_max
      value: -19.5043
    - type: nauc_recall_at_20_std
      value: -10.005500000000001
    - type: nauc_recall_at_20_diff1
      value: -7.197299999999999
    - type: nauc_recall_at_100_max
      value: -21.4032
    - type: nauc_recall_at_100_std
      value: 33.5358
    - type: nauc_recall_at_100_diff1
      value: -10.4876
    - type: nauc_recall_at_1000_max
      value: 1.8395000000000001
    - type: nauc_recall_at_1000_std
      value: 70.462
    - type: nauc_recall_at_1000_diff1
      value: -23.4072
    - type: nauc_precision_at_1_max
      value: -23.0917
    - type: nauc_precision_at_1_std
      value: -8.036999999999999
    - type: nauc_precision_at_1_diff1
      value: 19.354599999999998
    - type: nauc_precision_at_3_max
      value: -11.3547
    - type: nauc_precision_at_3_std
      value: -30.2495
    - type: nauc_precision_at_3_diff1
      value: 20.3126
    - type: nauc_precision_at_5_max
      value: -17.2545
    - type: nauc_precision_at_5_std
      value: -24.8896
    - type: nauc_precision_at_5_diff1
      value: 15.6276
    - type: nauc_precision_at_10_max
      value: -11.5796
    - type: nauc_precision_at_10_std
      value: -2.3662
    - type: nauc_precision_at_10_diff1
      value: 3.8091
    - type: nauc_precision_at_20_max
      value: -11.9042
    - type: nauc_precision_at_20_std
      value: 15.6577
    - type: nauc_precision_at_20_diff1
      value: -8.8878
    - type: nauc_precision_at_100_max
      value: -0.5217
    - type: nauc_precision_at_100_std
      value: 71.8387
    - type: nauc_precision_at_100_diff1
      value: -16.8714
    - type: nauc_precision_at_1000_max
      value: 36.234300000000005
    - type: nauc_precision_at_1000_std
      value: 37.5447
    - type: nauc_precision_at_1000_diff1
      value: -20.7229
    - type: nauc_mrr_at_1_max
      value: -23.0917
    - type: nauc_mrr_at_1_std
      value: -8.036999999999999
    - type: nauc_mrr_at_1_diff1
      value: 19.354599999999998
    - type: nauc_mrr_at_3_max
      value: -27.9937
    - type: nauc_mrr_at_3_std
      value: -26.519900000000003
    - type: nauc_mrr_at_3_diff1
      value: 20.288
    - type: nauc_mrr_at_5_max
      value: -33.218599999999995
    - type: nauc_mrr_at_5_std
      value: -23.857400000000002
    - type: nauc_mrr_at_5_diff1
      value: 15.978200000000001
    - type: nauc_mrr_at_10_max
      value: -31.7904
    - type: nauc_mrr_at_10_std
      value: -19.169900000000002
    - type: nauc_mrr_at_10_diff1
      value: 17.762700000000002
    - type: nauc_mrr_at_20_max
      value: -30.44
    - type: nauc_mrr_at_20_std
      value: -20.2867
    - type: nauc_mrr_at_20_diff1
      value: 18.895500000000002
    - type: nauc_mrr_at_100_max
      value: -30.5404
    - type: nauc_mrr_at_100_std
      value: -20.5699
    - type: nauc_mrr_at_100_diff1
      value: 18.7046
    - type: nauc_mrr_at_1000_max
      value: -30.5404
    - type: nauc_mrr_at_1000_std
      value: -20.5699
    - type: nauc_mrr_at_1000_diff1
      value: 18.7046
    - type: main_score
      value: 29.767
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 64.8096
    - type: f1
      value: 49.844300000000004
    - type: f1_weighted
      value: 72.5251
    - type: ap
      value: 11.7519
    - type: ap_weighted
      value: 11.7519
    - type: main_score
      value: 64.8096
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 58.1692
    - type: f1
      value: 58.4408
    - type: f1_weighted
      value: 57.565599999999996
    - type: main_score
      value: 58.1692
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: v_measure
      value: 39.293
    - type: v_measure_std
      value: 1.5684
    - type: main_score
      value: 39.293
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 83.29260000000001
    - type: similarity_accuracy_threshold
      value: 78.2732
    - type: similarity_f1
      value: 60.656600000000005
    - type: similarity_f1_threshold
      value: 73.4961
    - type: similarity_precision
      value: 59.007
    - type: similarity_recall
      value: 62.4011
    - type: similarity_ap
      value: 64.7501
    - type: cosine_accuracy
      value: 83.29260000000001
    - type: cosine_accuracy_threshold
      value: 78.2732
    - type: cosine_f1
      value: 60.656600000000005
    - type: cosine_f1_threshold
      value: 73.4961
    - type: cosine_precision
      value: 59.007
    - type: cosine_recall
      value: 62.4011
    - type: cosine_ap
      value: 64.7501
    - type: manhattan_accuracy
      value: 83.2986
    - type: manhattan_accuracy_threshold
      value: 1476.7148
    - type: manhattan_f1
      value: 60.7459
    - type: manhattan_f1_threshold
      value: 1607.9180000000001
    - type: manhattan_precision
      value: 59.0581
    - type: manhattan_recall
      value: 62.53300000000001
    - type: manhattan_ap
      value: 64.76859999999999
    - type: euclidean_accuracy
      value: 83.29260000000001
    - type: euclidean_accuracy_threshold
      value: 65.9194
    - type: euclidean_f1
      value: 60.656600000000005
    - type: euclidean_f1_threshold
      value: 72.8065
    - type: euclidean_precision
      value: 59.007
    - type: euclidean_recall
      value: 62.4011
    - type: euclidean_ap
      value: 64.7501
    - type: dot_accuracy
      value: 83.29260000000001
    - type: dot_accuracy_threshold
      value: 78.2731
    - type: dot_f1
      value: 60.656600000000005
    - type: dot_f1_threshold
      value: 73.4961
    - type: dot_precision
      value: 59.007
    - type: dot_recall
      value: 62.4011
    - type: dot_ap
      value: 64.7501
    - type: max_accuracy
      value: 83.2986
    - type: max_f1
      value: 60.7459
    - type: max_precision
      value: 59.0581
    - type: max_recall
      value: 62.53300000000001
    - type: max_ap
      value: 64.76859999999999
    - type: main_score
      value: 64.76859999999999
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: similarity_accuracy
      value: 89.0247
    - type: similarity_accuracy_threshold
      value: 69.271
    - type: similarity_f1
      value: 78.24419999999999
    - type: similarity_f1_threshold
      value: 66.2183
    - type: similarity_precision
      value: 76.616
    - type: similarity_recall
      value: 79.943
    - type: similarity_ap
      value: 85.9494
    - type: cosine_accuracy
      value: 89.0247
    - type: cosine_accuracy_threshold
      value: 69.271
    - type: cosine_f1
      value: 78.24419999999999
    - type: cosine_f1_threshold
      value: 66.2183
    - type: cosine_precision
      value: 76.616
    - type: cosine_recall
      value: 79.943
    - type: cosine_ap
      value: 85.9494
    - type: manhattan_accuracy
      value: 89.0267
    - type: manhattan_accuracy_threshold
      value: 1750.3544000000002
    - type: manhattan_f1
      value: 78.2188
    - type: manhattan_f1_threshold
      value: 1837.7304
    - type: manhattan_precision
      value: 75.1472
    - type: manhattan_recall
      value: 81.5522
    - type: manhattan_ap
      value: 85.9496
    - type: euclidean_accuracy
      value: 89.0247
    - type: euclidean_accuracy_threshold
      value: 78.3951
    - type: euclidean_f1
      value: 78.24419999999999
    - type: euclidean_f1_threshold
      value: 82.197
    - type: euclidean_precision
      value: 76.616
    - type: euclidean_recall
      value: 79.943
    - type: euclidean_ap
      value: 85.9494
    - type: dot_accuracy
      value: 89.0247
    - type: dot_accuracy_threshold
      value: 69.271
    - type: dot_f1
      value: 78.24419999999999
    - type: dot_f1_threshold
      value: 66.2183
    - type: dot_precision
      value: 76.616
    - type: dot_recall
      value: 79.943
    - type: dot_ap
      value: 85.9494
    - type: max_accuracy
      value: 89.0267
    - type: max_f1
      value: 78.24419999999999
    - type: max_precision
      value: 76.616
    - type: max_recall
      value: 81.5522
    - type: max_ap
      value: 85.9496
    - type: main_score
      value: 85.9496
    task:
      type: PairClassification
---
A modified version of [Snowflake/snowflake-arctic-embed-m-v2.0](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0), without xformers, so it works on CPU.

```python
from sentence_transformers import SentenceTransformer
import torch

device = torch.device("cpu")
model = SentenceTransformer("cnmoro/snowflake-arctic-embed-m-v2.0-cpu", device=device, trust_remote_code=True)
```