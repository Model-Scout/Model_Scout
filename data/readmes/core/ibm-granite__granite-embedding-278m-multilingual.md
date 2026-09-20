---
language:
- en
- ar
- cs
- de
- es
- fr
- it
- ja
- ko
- nl
- pt
- zh
license: apache-2.0
library_name: transformers
tags:
- language
- granite
- embeddings
- multilingual
- mteb
- sentence-transformers
model-index:
- name: ibm-granite/granite-embedding-278m-multilingual
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 73.4333
    - type: f1
      value: 61.2301
    - type: f1_weighted
      value: 78.40899999999999
    - type: ap
      value: 23.347
    - type: ap_weighted
      value: 23.347
    - type: main_score
      value: 73.4333
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
      value: 71.806
    - type: f1
      value: 65.6467
    - type: f1_weighted
      value: 74.4815
    - type: ap
      value: 34.045700000000004
    - type: ap_weighted
      value: 34.045700000000004
    - type: main_score
      value: 71.806
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
      value: 67.5907
    - type: f1
      value: 67.36370000000001
    - type: f1_weighted
      value: 67.36370000000001
    - type: ap
      value: 62.0368
    - type: ap_weighted
      value: 62.0368
    - type: main_score
      value: 67.5907
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
      value: 37.278
    - type: f1
      value: 36.4099
    - type: f1_weighted
      value: 36.4099
    - type: main_score
      value: 37.278
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AppsRetrieval (default)
      revision: f22508f96b7a36c2415181ed8bb76f76e04ae2d5
      split: test
      type: CoIR-Retrieval/apps
    metrics:
    - type: ndcg_at_1
      value: 3.453
    - type: ndcg_at_3
      value: 4.882000000000001
    - type: ndcg_at_5
      value: 5.564
    - type: ndcg_at_10
      value: 6.214
    - type: ndcg_at_20
      value: 6.814000000000001
    - type: ndcg_at_100
      value: 8.581
    - type: ndcg_at_1000
      value: 12.215
    - type: map_at_1
      value: 3.453
    - type: map_at_3
      value: 4.515000000000001
    - type: map_at_5
      value: 4.89
    - type: map_at_10
      value: 5.151
    - type: map_at_20
      value: 5.313
    - type: map_at_100
      value: 5.539000000000001
    - type: map_at_1000
      value: 5.638
    - type: recall_at_1
      value: 3.453
    - type: recall_at_3
      value: 5.949999999999999
    - type: recall_at_5
      value: 7.623
    - type: recall_at_10
      value: 9.668000000000001
    - type: recall_at_20
      value: 12.058
    - type: recall_at_100
      value: 21.859
    - type: recall_at_1000
      value: 52.722
    - type: precision_at_1
      value: 3.453
    - type: precision_at_3
      value: 1.983
    - type: precision_at_5
      value: 1.525
    - type: precision_at_10
      value: 0.967
    - type: precision_at_20
      value: 0.603
    - type: precision_at_100
      value: 0.219
    - type: precision_at_1000
      value: 0.053
    - type: mrr_at_1
      value: 3.4528999999999996
    - type: mrr_at_3
      value: 4.5153
    - type: mrr_at_5
      value: 4.889799999999999
    - type: mrr_at_10
      value: 5.1507
    - type: mrr_at_20
      value: 5.3135
    - type: mrr_at_100
      value: 5.5391
    - type: mrr_at_1000
      value: 5.6382
    - type: nauc_ndcg_at_1_max
      value: 37.1714
    - type: nauc_ndcg_at_1_std
      value: 15.306700000000001
    - type: nauc_ndcg_at_1_diff1
      value: 46.2252
    - type: nauc_ndcg_at_3_max
      value: 32.0309
    - type: nauc_ndcg_at_3_std
      value: 14.2983
    - type: nauc_ndcg_at_3_diff1
      value: 34.7174
    - type: nauc_ndcg_at_5_max
      value: 29.3613
    - type: nauc_ndcg_at_5_std
      value: 13.0358
    - type: nauc_ndcg_at_5_diff1
      value: 30.8369
    - type: nauc_ndcg_at_10_max
      value: 26.820100000000004
    - type: nauc_ndcg_at_10_std
      value: 12.3422
    - type: nauc_ndcg_at_10_diff1
      value: 27.3719
    - type: nauc_ndcg_at_20_max
      value: 25.5643
    - type: nauc_ndcg_at_20_std
      value: 11.383000000000001
    - type: nauc_ndcg_at_20_diff1
      value: 25.7058
    - type: nauc_ndcg_at_100_max
      value: 23.2131
    - type: nauc_ndcg_at_100_std
      value: 12.4787
    - type: nauc_ndcg_at_100_diff1
      value: 21.6874
    - type: nauc_ndcg_at_1000_max
      value: 22.900499999999997
    - type: nauc_ndcg_at_1000_std
      value: 13.2218
    - type: nauc_ndcg_at_1000_diff1
      value: 19.668
    - type: nauc_map_at_1_max
      value: 37.1714
    - type: nauc_map_at_1_std
      value: 15.306700000000001
    - type: nauc_map_at_1_diff1
      value: 46.2252
    - type: nauc_map_at_3_max
      value: 33.1012
    - type: nauc_map_at_3_std
      value: 14.4117
    - type: nauc_map_at_3_diff1
      value: 36.8859
    - type: nauc_map_at_5_max
      value: 31.404700000000002
    - type: nauc_map_at_5_std
      value: 13.5956
    - type: nauc_map_at_5_diff1
      value: 34.3454
    - type: nauc_map_at_10_max
      value: 30.1013
    - type: nauc_map_at_10_std
      value: 13.2253
    - type: nauc_map_at_10_diff1
      value: 32.487
    - type: nauc_map_at_20_max
      value: 29.5747
    - type: nauc_map_at_20_std
      value: 12.843499999999999
    - type: nauc_map_at_20_diff1
      value: 31.8252
    - type: nauc_map_at_100_max
      value: 28.968899999999998
    - type: nauc_map_at_100_std
      value: 12.967699999999999
    - type: nauc_map_at_100_diff1
      value: 30.924000000000003
    - type: nauc_map_at_1000_max
      value: 28.894599999999997
    - type: nauc_map_at_1000_std
      value: 12.997800000000002
    - type: nauc_map_at_1000_diff1
      value: 30.7653
    - type: nauc_recall_at_1_max
      value: 37.1714
    - type: nauc_recall_at_1_std
      value: 15.306700000000001
    - type: nauc_recall_at_1_diff1
      value: 46.2252
    - type: nauc_recall_at_3_max
      value: 29.6485
    - type: nauc_recall_at_3_std
      value: 14.072799999999999
    - type: nauc_recall_at_3_diff1
      value: 29.9536
    - type: nauc_recall_at_5_max
      value: 25.251099999999997
    - type: nauc_recall_at_5_std
      value: 11.9121
    - type: nauc_recall_at_5_diff1
      value: 23.9203
    - type: nauc_recall_at_10_max
      value: 20.8856
    - type: nauc_recall_at_10_std
      value: 10.7653
    - type: nauc_recall_at_10_diff1
      value: 18.3716
    - type: nauc_recall_at_20_max
      value: 18.9378
    - type: nauc_recall_at_20_std
      value: 8.8933
    - type: nauc_recall_at_20_diff1
      value: 15.7693
    - type: nauc_recall_at_100_max
      value: 15.7027
    - type: nauc_recall_at_100_std
      value: 12.6519
    - type: nauc_recall_at_100_diff1
      value: 9.2726
    - type: nauc_recall_at_1000_max
      value: 16.2321
    - type: nauc_recall_at_1000_std
      value: 15.2717
    - type: nauc_recall_at_1000_diff1
      value: 4.4337
    - type: nauc_precision_at_1_max
      value: 37.1714
    - type: nauc_precision_at_1_std
      value: 15.306700000000001
    - type: nauc_precision_at_1_diff1
      value: 46.2252
    - type: nauc_precision_at_3_max
      value: 29.6485
    - type: nauc_precision_at_3_std
      value: 14.072799999999999
    - type: nauc_precision_at_3_diff1
      value: 29.9536
    - type: nauc_precision_at_5_max
      value: 25.251099999999997
    - type: nauc_precision_at_5_std
      value: 11.9121
    - type: nauc_precision_at_5_diff1
      value: 23.9203
    - type: nauc_precision_at_10_max
      value: 20.8856
    - type: nauc_precision_at_10_std
      value: 10.7653
    - type: nauc_precision_at_10_diff1
      value: 18.3716
    - type: nauc_precision_at_20_max
      value: 18.9378
    - type: nauc_precision_at_20_std
      value: 8.8933
    - type: nauc_precision_at_20_diff1
      value: 15.7693
    - type: nauc_precision_at_100_max
      value: 15.7027
    - type: nauc_precision_at_100_std
      value: 12.6519
    - type: nauc_precision_at_100_diff1
      value: 9.2726
    - type: nauc_precision_at_1000_max
      value: 16.2321
    - type: nauc_precision_at_1000_std
      value: 15.2717
    - type: nauc_precision_at_1000_diff1
      value: 4.4337
    - type: nauc_mrr_at_1_max
      value: 37.1714
    - type: nauc_mrr_at_1_std
      value: 15.306700000000001
    - type: nauc_mrr_at_1_diff1
      value: 46.2252
    - type: nauc_mrr_at_3_max
      value: 33.1012
    - type: nauc_mrr_at_3_std
      value: 14.4117
    - type: nauc_mrr_at_3_diff1
      value: 36.8859
    - type: nauc_mrr_at_5_max
      value: 31.404700000000002
    - type: nauc_mrr_at_5_std
      value: 13.5956
    - type: nauc_mrr_at_5_diff1
      value: 34.3454
    - type: nauc_mrr_at_10_max
      value: 30.1013
    - type: nauc_mrr_at_10_std
      value: 13.2253
    - type: nauc_mrr_at_10_diff1
      value: 32.487
    - type: nauc_mrr_at_20_max
      value: 29.5747
    - type: nauc_mrr_at_20_std
      value: 12.843499999999999
    - type: nauc_mrr_at_20_diff1
      value: 31.8252
    - type: nauc_mrr_at_100_max
      value: 28.968899999999998
    - type: nauc_mrr_at_100_std
      value: 12.967699999999999
    - type: nauc_mrr_at_100_diff1
      value: 30.9239
    - type: nauc_mrr_at_1000_max
      value: 28.894599999999997
    - type: nauc_mrr_at_1000_std
      value: 12.997800000000002
    - type: nauc_mrr_at_1000_diff1
      value: 30.7653
    - type: main_score
      value: 6.214
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: ndcg_at_1
      value: 31.152
    - type: ndcg_at_3
      value: 45.050000000000004
    - type: ndcg_at_5
      value: 50.458999999999996
    - type: ndcg_at_10
      value: 55.24400000000001
    - type: ndcg_at_20
      value: 57.918000000000006
    - type: ndcg_at_100
      value: 58.97
    - type: ndcg_at_1000
      value: 59.080999999999996
    - type: map_at_1
      value: 31.152
    - type: map_at_3
      value: 41.513
    - type: map_at_5
      value: 44.542
    - type: map_at_10
      value: 46.544000000000004
    - type: map_at_20
      value: 47.304
    - type: map_at_100
      value: 47.467999999999996
    - type: map_at_1000
      value: 47.473
    - type: recall_at_1
      value: 31.152
    - type: recall_at_3
      value: 55.334
    - type: recall_at_5
      value: 68.35
    - type: recall_at_10
      value: 83.001
    - type: recall_at_20
      value: 93.38499999999999
    - type: recall_at_100
      value: 98.791
    - type: recall_at_1000
      value: 99.644
    - type: precision_at_1
      value: 31.152
    - type: precision_at_3
      value: 18.445
    - type: precision_at_5
      value: 13.669999999999998
    - type: precision_at_10
      value: 8.3
    - type: precision_at_20
      value: 4.6690000000000005
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 31.7212
    - type: mrr_at_3
      value: 41.7141
    - type: mrr_at_5
      value: 44.754599999999996
    - type: mrr_at_10
      value: 46.7491
    - type: mrr_at_20
      value: 47.515299999999996
    - type: mrr_at_100
      value: 47.679300000000005
    - type: mrr_at_1000
      value: 47.6841
    - type: nauc_ndcg_at_1_max
      value: -7.8191
    - type: nauc_ndcg_at_1_std
      value: -4.0581
    - type: nauc_ndcg_at_1_diff1
      value: 14.383199999999999
    - type: nauc_ndcg_at_3_max
      value: -4.6856
    - type: nauc_ndcg_at_3_std
      value: -3.4165
    - type: nauc_ndcg_at_3_diff1
      value: 10.7764
    - type: nauc_ndcg_at_5_max
      value: -3.2999
    - type: nauc_ndcg_at_5_std
      value: -3.6675
    - type: nauc_ndcg_at_5_diff1
      value: 11.6249
    - type: nauc_ndcg_at_10_max
      value: -3.2984
    - type: nauc_ndcg_at_10_std
      value: -3.0373
    - type: nauc_ndcg_at_10_diff1
      value: 11.9938
    - type: nauc_ndcg_at_20_max
      value: -3.147
    - type: nauc_ndcg_at_20_std
      value: -2.9219
    - type: nauc_ndcg_at_20_diff1
      value: 12.4893
    - type: nauc_ndcg_at_100_max
      value: -4.2572
    - type: nauc_ndcg_at_100_std
      value: -2.8537
    - type: nauc_ndcg_at_100_diff1
      value: 12.1039
    - type: nauc_ndcg_at_1000_max
      value: -4.3526
    - type: nauc_ndcg_at_1000_std
      value: -3.0145
    - type: nauc_ndcg_at_1000_diff1
      value: 12.1685
    - type: nauc_map_at_1_max
      value: -7.8191
    - type: nauc_map_at_1_std
      value: -4.0581
    - type: nauc_map_at_1_diff1
      value: 14.383199999999999
    - type: nauc_map_at_3_max
      value: -5.5556
    - type: nauc_map_at_3_std
      value: -3.515
    - type: nauc_map_at_3_diff1
      value: 11.5486
    - type: nauc_map_at_5_max
      value: -4.840599999999999
    - type: nauc_map_at_5_std
      value: -3.6663
    - type: nauc_map_at_5_diff1
      value: 12.053899999999999
    - type: nauc_map_at_10_max
      value: -4.9401
    - type: nauc_map_at_10_std
      value: -3.3724
    - type: nauc_map_at_10_diff1
      value: 12.1558
    - type: nauc_map_at_20_max
      value: -4.9365
    - type: nauc_map_at_20_std
      value: -3.3676999999999997
    - type: nauc_map_at_20_diff1
      value: 12.2729
    - type: nauc_map_at_100_max
      value: -5.0695
    - type: nauc_map_at_100_std
      value: -3.3561
    - type: nauc_map_at_100_diff1
      value: 12.237
    - type: nauc_map_at_1000_max
      value: -5.0709
    - type: nauc_map_at_1000_std
      value: -3.3594
    - type: nauc_map_at_1000_diff1
      value: 12.2408
    - type: nauc_recall_at_1_max
      value: -7.8191
    - type: nauc_recall_at_1_std
      value: -4.0581
    - type: nauc_recall_at_1_diff1
      value: 14.383199999999999
    - type: nauc_recall_at_3_max
      value: -2.0358
    - type: nauc_recall_at_3_std
      value: -3.1464
    - type: nauc_recall_at_3_diff1
      value: 8.510900000000001
    - type: nauc_recall_at_5_max
      value: 2.4358999999999997
    - type: nauc_recall_at_5_std
      value: -3.727
    - type: nauc_recall_at_5_diff1
      value: 10.2867
    - type: nauc_recall_at_10_max
      value: 6.5777
    - type: nauc_recall_at_10_std
      value: -1.0198
    - type: nauc_recall_at_10_diff1
      value: 11.9244
    - type: nauc_recall_at_20_max
      value: 22.8541
    - type: nauc_recall_at_20_std
      value: 4.1539
    - type: nauc_recall_at_20_diff1
      value: 19.3648
    - type: nauc_recall_at_100_max
      value: 18.5148
    - type: nauc_recall_at_100_std
      value: 41.1822
    - type: nauc_recall_at_100_diff1
      value: 5.1883
    - type: nauc_recall_at_1000_max
      value: 13.995099999999999
    - type: nauc_recall_at_1000_std
      value: 53.7961
    - type: nauc_recall_at_1000_diff1
      value: 14.8451
    - type: nauc_precision_at_1_max
      value: -7.8191
    - type: nauc_precision_at_1_std
      value: -4.0581
    - type: nauc_precision_at_1_diff1
      value: 14.383199999999999
    - type: nauc_precision_at_3_max
      value: -2.0358
    - type: nauc_precision_at_3_std
      value: -3.1464
    - type: nauc_precision_at_3_diff1
      value: 8.510900000000001
    - type: nauc_precision_at_5_max
      value: 2.4358999999999997
    - type: nauc_precision_at_5_std
      value: -3.727
    - type: nauc_precision_at_5_diff1
      value: 10.2867
    - type: nauc_precision_at_10_max
      value: 6.5777
    - type: nauc_precision_at_10_std
      value: -1.0198
    - type: nauc_precision_at_10_diff1
      value: 11.9244
    - type: nauc_precision_at_20_max
      value: 22.8541
    - type: nauc_precision_at_20_std
      value: 4.1539
    - type: nauc_precision_at_20_diff1
      value: 19.3648
    - type: nauc_precision_at_100_max
      value: 18.5148
    - type: nauc_precision_at_100_std
      value: 41.1822
    - type: nauc_precision_at_100_diff1
      value: 5.1883
    - type: nauc_precision_at_1000_max
      value: 13.995099999999999
    - type: nauc_precision_at_1000_std
      value: 53.7961
    - type: nauc_precision_at_1000_diff1
      value: 14.8451
    - type: nauc_mrr_at_1_max
      value: -8.1904
    - type: nauc_mrr_at_1_std
      value: -4.0896
    - type: nauc_mrr_at_1_diff1
      value: 12.7103
    - type: nauc_mrr_at_3_max
      value: -6.6608
    - type: nauc_mrr_at_3_std
      value: -3.6741
    - type: nauc_mrr_at_3_diff1
      value: 9.851
    - type: nauc_mrr_at_5_max
      value: -5.7596
    - type: nauc_mrr_at_5_std
      value: -3.7391
    - type: nauc_mrr_at_5_diff1
      value: 10.4908
    - type: nauc_mrr_at_10_max
      value: -5.8613
    - type: nauc_mrr_at_10_std
      value: -3.4377999999999997
    - type: nauc_mrr_at_10_diff1
      value: 10.5641
    - type: nauc_mrr_at_20_max
      value: -5.8497
    - type: nauc_mrr_at_20_std
      value: -3.4543
    - type: nauc_mrr_at_20_diff1
      value: 10.6822
    - type: nauc_mrr_at_100_max
      value: -5.9873
    - type: nauc_mrr_at_100_std
      value: -3.4431000000000003
    - type: nauc_mrr_at_100_diff1
      value: 10.6379
    - type: nauc_mrr_at_1000_max
      value: -5.9887999999999995
    - type: nauc_mrr_at_1000_std
      value: -3.4465000000000003
    - type: nauc_mrr_at_1000_diff1
      value: 10.641399999999999
    - type: main_score
      value: 55.24400000000001
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
      value: 43.1321
    - type: v_measure_std
      value: 13.594000000000001
    - type: main_score
      value: 43.1321
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
      value: 32.9343
    - type: v_measure_std
      value: 14.2478
    - type: main_score
      value: 32.9343
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
      value: 62.3443
    - type: mrr
      value: 76.3882
    - type: nAUC_map_max
      value: 28.3073
    - type: nAUC_map_std
      value: 15.5307
    - type: nAUC_map_diff1
      value: 12.6855
    - type: nAUC_mrr_max
      value: 36.409200000000006
    - type: nAUC_mrr_std
      value: 22.6271
    - type: nAUC_mrr_diff1
      value: 19.1211
    - type: main_score
      value: 62.3443
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
      value: 84.3253
    - type: spearman
      value: 81.6362
    - type: cosine_pearson
      value: 84.3253
    - type: cosine_spearman
      value: 81.6362
    - type: manhattan_pearson
      value: 82.70960000000001
    - type: manhattan_spearman
      value: 81.3037
    - type: euclidean_pearson
      value: 82.6906
    - type: euclidean_spearman
      value: 81.6362
    - type: main_score
      value: 81.6362
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
      value: 78.0617
    - type: f1
      value: 77.2085
    - type: f1_weighted
      value: 77.2085
    - type: main_score
      value: 78.0617
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
      value: 35.8271
    - type: v_measure_std
      value: 0.7191000000000001
    - type: main_score
      value: 35.8271
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
      value: 30.3905
    - type: v_measure_std
      value: 0.7136
    - type: main_score
      value: 30.3905
    task:
      type: Clustering
  - dataset:
      config: python
      name: MTEB COIRCodeSearchNetRetrieval (python)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 83.22800000000001
    - type: ndcg_at_3
      value: 87.41799999999999
    - type: ndcg_at_5
      value: 88.089
    - type: ndcg_at_10
      value: 88.789
    - type: ndcg_at_20
      value: 89.156
    - type: ndcg_at_100
      value: 89.60900000000001
    - type: ndcg_at_1000
      value: 89.79
    - type: map_at_1
      value: 83.22800000000001
    - type: map_at_3
      value: 86.431
    - type: map_at_5
      value: 86.80499999999999
    - type: map_at_10
      value: 87.09599999999999
    - type: map_at_20
      value: 87.198
    - type: map_at_100
      value: 87.263
    - type: map_at_1000
      value: 87.27000000000001
    - type: recall_at_1
      value: 83.22800000000001
    - type: recall_at_3
      value: 90.253
    - type: recall_at_5
      value: 91.876
    - type: recall_at_10
      value: 94.03399999999999
    - type: recall_at_20
      value: 95.475
    - type: recall_at_100
      value: 97.882
    - type: recall_at_1000
      value: 99.316
    - type: precision_at_1
      value: 83.22800000000001
    - type: precision_at_3
      value: 30.084
    - type: precision_at_5
      value: 18.375
    - type: precision_at_10
      value: 9.403
    - type: precision_at_20
      value: 4.774
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 83.235
    - type: mrr_at_3
      value: 86.4336
    - type: mrr_at_5
      value: 86.8077
    - type: mrr_at_10
      value: 87.0979
    - type: mrr_at_20
      value: 87.2001
    - type: mrr_at_100
      value: 87.26509999999999
    - type: mrr_at_1000
      value: 87.2718
    - type: nauc_ndcg_at_1_max
      value: 82.2462
    - type: nauc_ndcg_at_1_std
      value: 11.4635
    - type: nauc_ndcg_at_1_diff1
      value: 90.5106
    - type: nauc_ndcg_at_3_max
      value: 83.9742
    - type: nauc_ndcg_at_3_std
      value: 12.7085
    - type: nauc_ndcg_at_3_diff1
      value: 88.2182
    - type: nauc_ndcg_at_5_max
      value: 84.18870000000001
    - type: nauc_ndcg_at_5_std
      value: 13.167499999999999
    - type: nauc_ndcg_at_5_diff1
      value: 88.44999999999999
    - type: nauc_ndcg_at_10_max
      value: 84.2219
    - type: nauc_ndcg_at_10_std
      value: 13.5219
    - type: nauc_ndcg_at_10_diff1
      value: 88.6386
    - type: nauc_ndcg_at_20_max
      value: 84.2289
    - type: nauc_ndcg_at_20_std
      value: 14.0686
    - type: nauc_ndcg_at_20_diff1
      value: 88.7516
    - type: nauc_ndcg_at_100_max
      value: 84.12049999999999
    - type: nauc_ndcg_at_100_std
      value: 14.1778
    - type: nauc_ndcg_at_100_diff1
      value: 88.8592
    - type: nauc_ndcg_at_1000_max
      value: 84.0367
    - type: nauc_ndcg_at_1000_std
      value: 13.9125
    - type: nauc_ndcg_at_1000_diff1
      value: 88.9054
    - type: nauc_map_at_1_max
      value: 82.2462
    - type: nauc_map_at_1_std
      value: 11.4635
    - type: nauc_map_at_1_diff1
      value: 90.5106
    - type: nauc_map_at_3_max
      value: 83.5638
    - type: nauc_map_at_3_std
      value: 12.3576
    - type: nauc_map_at_3_diff1
      value: 88.8502
    - type: nauc_map_at_5_max
      value: 83.6625
    - type: nauc_map_at_5_std
      value: 12.582099999999999
    - type: nauc_map_at_5_diff1
      value: 88.9876
    - type: nauc_map_at_10_max
      value: 83.6605
    - type: nauc_map_at_10_std
      value: 12.6859
    - type: nauc_map_at_10_diff1
      value: 89.07119999999999
    - type: nauc_map_at_20_max
      value: 83.65629999999999
    - type: nauc_map_at_20_std
      value: 12.8105
    - type: nauc_map_at_20_diff1
      value: 89.1036
    - type: nauc_map_at_100_max
      value: 83.6413
    - type: nauc_map_at_100_std
      value: 12.823699999999999
    - type: nauc_map_at_100_diff1
      value: 89.1193
    - type: nauc_map_at_1000_max
      value: 83.6386
    - type: nauc_map_at_1000_std
      value: 12.815999999999999
    - type: nauc_map_at_1000_diff1
      value: 89.1209
    - type: nauc_recall_at_1_max
      value: 82.2462
    - type: nauc_recall_at_1_std
      value: 11.4635
    - type: nauc_recall_at_1_diff1
      value: 90.5106
    - type: nauc_recall_at_3_max
      value: 85.512
    - type: nauc_recall_at_3_std
      value: 14.061399999999999
    - type: nauc_recall_at_3_diff1
      value: 85.7898
    - type: nauc_recall_at_5_max
      value: 86.5434
    - type: nauc_recall_at_5_std
      value: 15.894400000000001
    - type: nauc_recall_at_5_diff1
      value: 86.0934
    - type: nauc_recall_at_10_max
      value: 87.59909999999999
    - type: nauc_recall_at_10_std
      value: 18.9872
    - type: nauc_recall_at_10_diff1
      value: 86.26740000000001
    - type: nauc_recall_at_20_max
      value: 88.76190000000001
    - type: nauc_recall_at_20_std
      value: 25.6618
    - type: nauc_recall_at_20_diff1
      value: 86.5002
    - type: nauc_recall_at_100_max
      value: 91.0976
    - type: nauc_recall_at_100_std
      value: 40.9161
    - type: nauc_recall_at_100_diff1
      value: 86.5441
    - type: nauc_recall_at_1000_max
      value: 96.018
    - type: nauc_recall_at_1000_std
      value: 65.6217
    - type: nauc_recall_at_1000_diff1
      value: 86.8456
    - type: nauc_precision_at_1_max
      value: 82.2462
    - type: nauc_precision_at_1_std
      value: 11.4635
    - type: nauc_precision_at_1_diff1
      value: 90.5106
    - type: nauc_precision_at_3_max
      value: 85.512
    - type: nauc_precision_at_3_std
      value: 14.061399999999999
    - type: nauc_precision_at_3_diff1
      value: 85.7898
    - type: nauc_precision_at_5_max
      value: 86.5434
    - type: nauc_precision_at_5_std
      value: 15.894400000000001
    - type: nauc_precision_at_5_diff1
      value: 86.0934
    - type: nauc_precision_at_10_max
      value: 87.59909999999999
    - type: nauc_precision_at_10_std
      value: 18.9872
    - type: nauc_precision_at_10_diff1
      value: 86.26740000000001
    - type: nauc_precision_at_20_max
      value: 88.76190000000001
    - type: nauc_precision_at_20_std
      value: 25.6618
    - type: nauc_precision_at_20_diff1
      value: 86.5002
    - type: nauc_precision_at_100_max
      value: 91.0976
    - type: nauc_precision_at_100_std
      value: 40.9161
    - type: nauc_precision_at_100_diff1
      value: 86.5441
    - type: nauc_precision_at_1000_max
      value: 96.018
    - type: nauc_precision_at_1000_std
      value: 65.6217
    - type: nauc_precision_at_1000_diff1
      value: 86.8456
    - type: nauc_mrr_at_1_max
      value: 82.2393
    - type: nauc_mrr_at_1_std
      value: 11.5163
    - type: nauc_mrr_at_1_diff1
      value: 90.50160000000001
    - type: nauc_mrr_at_3_max
      value: 83.5623
    - type: nauc_mrr_at_3_std
      value: 12.395
    - type: nauc_mrr_at_3_diff1
      value: 88.8463
    - type: nauc_mrr_at_5_max
      value: 83.6609
    - type: nauc_mrr_at_5_std
      value: 12.620700000000001
    - type: nauc_mrr_at_5_diff1
      value: 88.9836
    - type: nauc_mrr_at_10_max
      value: 83.6589
    - type: nauc_mrr_at_10_std
      value: 12.7255
    - type: nauc_mrr_at_10_diff1
      value: 89.0672
    - type: nauc_mrr_at_20_max
      value: 83.6546
    - type: nauc_mrr_at_20_std
      value: 12.8504
    - type: nauc_mrr_at_20_diff1
      value: 89.09949999999999
    - type: nauc_mrr_at_100_max
      value: 83.6396
    - type: nauc_mrr_at_100_std
      value: 12.8638
    - type: nauc_mrr_at_100_diff1
      value: 89.1152
    - type: nauc_mrr_at_1000_max
      value: 83.6369
    - type: nauc_mrr_at_1000_std
      value: 12.856100000000001
    - type: nauc_mrr_at_1000_diff1
      value: 89.1168
    - type: main_score
      value: 88.789
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB COIRCodeSearchNetRetrieval (javascript)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 29.14
    - type: ndcg_at_3
      value: 35.185
    - type: ndcg_at_5
      value: 37.013
    - type: ndcg_at_10
      value: 38.778
    - type: ndcg_at_20
      value: 40.184999999999995
    - type: ndcg_at_100
      value: 42.394999999999996
    - type: ndcg_at_1000
      value: 44.243
    - type: map_at_1
      value: 29.14
    - type: map_at_3
      value: 33.703
    - type: map_at_5
      value: 34.717999999999996
    - type: map_at_10
      value: 35.443999999999996
    - type: map_at_20
      value: 35.831
    - type: map_at_100
      value: 36.132999999999996
    - type: map_at_1000
      value: 36.193999999999996
    - type: recall_at_1
      value: 29.14
    - type: recall_at_3
      value: 39.471000000000004
    - type: recall_at_5
      value: 43.908
    - type: recall_at_10
      value: 49.376999999999995
    - type: recall_at_20
      value: 54.937999999999995
    - type: recall_at_100
      value: 66.91
    - type: recall_at_1000
      value: 81.98100000000001
    - type: precision_at_1
      value: 29.14
    - type: precision_at_3
      value: 13.157
    - type: precision_at_5
      value: 8.782
    - type: precision_at_10
      value: 4.938
    - type: precision_at_20
      value: 2.7470000000000003
    - type: precision_at_100
      value: 0.6689999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 29.140100000000004
    - type: mrr_at_3
      value: 33.703
    - type: mrr_at_5
      value: 34.7179
    - type: mrr_at_10
      value: 35.4443
    - type: mrr_at_20
      value: 35.830600000000004
    - type: mrr_at_100
      value: 36.1332
    - type: mrr_at_1000
      value: 36.1935
    - type: nauc_ndcg_at_1_max
      value: 46.9222
    - type: nauc_ndcg_at_1_std
      value: 3.3564999999999996
    - type: nauc_ndcg_at_1_diff1
      value: 60.583
    - type: nauc_ndcg_at_3_max
      value: 49.205799999999996
    - type: nauc_ndcg_at_3_std
      value: 5.976299999999999
    - type: nauc_ndcg_at_3_diff1
      value: 55.09610000000001
    - type: nauc_ndcg_at_5_max
      value: 49.0533
    - type: nauc_ndcg_at_5_std
      value: 6.5834
    - type: nauc_ndcg_at_5_diff1
      value: 54.430800000000005
    - type: nauc_ndcg_at_10_max
      value: 48.626799999999996
    - type: nauc_ndcg_at_10_std
      value: 7.4441
    - type: nauc_ndcg_at_10_diff1
      value: 53.1986
    - type: nauc_ndcg_at_20_max
      value: 48.7498
    - type: nauc_ndcg_at_20_std
      value: 8.3344
    - type: nauc_ndcg_at_20_diff1
      value: 52.844
    - type: nauc_ndcg_at_100_max
      value: 48.7164
    - type: nauc_ndcg_at_100_std
      value: 9.1646
    - type: nauc_ndcg_at_100_diff1
      value: 52.6307
    - type: nauc_ndcg_at_1000_max
      value: 48.634699999999995
    - type: nauc_ndcg_at_1000_std
      value: 9.3865
    - type: nauc_ndcg_at_1000_diff1
      value: 53.100899999999996
    - type: nauc_map_at_1_max
      value: 46.9222
    - type: nauc_map_at_1_std
      value: 3.3564999999999996
    - type: nauc_map_at_1_diff1
      value: 60.583
    - type: nauc_map_at_3_max
      value: 48.7099
    - type: nauc_map_at_3_std
      value: 5.2638
    - type: nauc_map_at_3_diff1
      value: 56.370200000000004
    - type: nauc_map_at_5_max
      value: 48.6303
    - type: nauc_map_at_5_std
      value: 5.5931
    - type: nauc_map_at_5_diff1
      value: 55.9968
    - type: nauc_map_at_10_max
      value: 48.4549
    - type: nauc_map_at_10_std
      value: 5.949800000000001
    - type: nauc_map_at_10_diff1
      value: 55.4941
    - type: nauc_map_at_20_max
      value: 48.4854
    - type: nauc_map_at_20_std
      value: 6.1861
    - type: nauc_map_at_20_diff1
      value: 55.4072
    - type: nauc_map_at_100_max
      value: 48.4835
    - type: nauc_map_at_100_std
      value: 6.2885
    - type: nauc_map_at_100_diff1
      value: 55.3743
    - type: nauc_map_at_1000_max
      value: 48.4769
    - type: nauc_map_at_1000_std
      value: 6.2978000000000005
    - type: nauc_map_at_1000_diff1
      value: 55.3852
    - type: nauc_recall_at_1_max
      value: 46.9222
    - type: nauc_recall_at_1_std
      value: 3.3564999999999996
    - type: nauc_recall_at_1_diff1
      value: 60.583
    - type: nauc_recall_at_3_max
      value: 50.5754
    - type: nauc_recall_at_3_std
      value: 8.005700000000001
    - type: nauc_recall_at_3_diff1
      value: 51.542100000000005
    - type: nauc_recall_at_5_max
      value: 50.199000000000005
    - type: nauc_recall_at_5_std
      value: 9.5088
    - type: nauc_recall_at_5_diff1
      value: 49.9358
    - type: nauc_recall_at_10_max
      value: 48.899100000000004
    - type: nauc_recall_at_10_std
      value: 12.2017
    - type: nauc_recall_at_10_diff1
      value: 46.042
    - type: nauc_recall_at_20_max
      value: 49.433899999999994
    - type: nauc_recall_at_20_std
      value: 16.1228
    - type: nauc_recall_at_20_diff1
      value: 44.1762
    - type: nauc_recall_at_100_max
      value: 49.2626
    - type: nauc_recall_at_100_std
      value: 23.1356
    - type: nauc_recall_at_100_diff1
      value: 41.2386
    - type: nauc_recall_at_1000_max
      value: 48.7068
    - type: nauc_recall_at_1000_std
      value: 34.4874
    - type: nauc_recall_at_1000_diff1
      value: 42.088
    - type: nauc_precision_at_1_max
      value: 46.9222
    - type: nauc_precision_at_1_std
      value: 3.3564999999999996
    - type: nauc_precision_at_1_diff1
      value: 60.583
    - type: nauc_precision_at_3_max
      value: 50.5754
    - type: nauc_precision_at_3_std
      value: 8.005700000000001
    - type: nauc_precision_at_3_diff1
      value: 51.542100000000005
    - type: nauc_precision_at_5_max
      value: 50.199000000000005
    - type: nauc_precision_at_5_std
      value: 9.5088
    - type: nauc_precision_at_5_diff1
      value: 49.9358
    - type: nauc_precision_at_10_max
      value: 48.899100000000004
    - type: nauc_precision_at_10_std
      value: 12.2017
    - type: nauc_precision_at_10_diff1
      value: 46.042
    - type: nauc_precision_at_20_max
      value: 49.433899999999994
    - type: nauc_precision_at_20_std
      value: 16.1228
    - type: nauc_precision_at_20_diff1
      value: 44.1762
    - type: nauc_precision_at_100_max
      value: 49.2626
    - type: nauc_precision_at_100_std
      value: 23.1356
    - type: nauc_precision_at_100_diff1
      value: 41.2386
    - type: nauc_precision_at_1000_max
      value: 48.7068
    - type: nauc_precision_at_1000_std
      value: 34.4874
    - type: nauc_precision_at_1000_diff1
      value: 42.088
    - type: nauc_mrr_at_1_max
      value: 46.9222
    - type: nauc_mrr_at_1_std
      value: 3.3564999999999996
    - type: nauc_mrr_at_1_diff1
      value: 60.583
    - type: nauc_mrr_at_3_max
      value: 48.7099
    - type: nauc_mrr_at_3_std
      value: 5.2638
    - type: nauc_mrr_at_3_diff1
      value: 56.370200000000004
    - type: nauc_mrr_at_5_max
      value: 48.6303
    - type: nauc_mrr_at_5_std
      value: 5.5931
    - type: nauc_mrr_at_5_diff1
      value: 55.9968
    - type: nauc_mrr_at_10_max
      value: 48.4549
    - type: nauc_mrr_at_10_std
      value: 5.949800000000001
    - type: nauc_mrr_at_10_diff1
      value: 55.4941
    - type: nauc_mrr_at_20_max
      value: 48.4854
    - type: nauc_mrr_at_20_std
      value: 6.1861
    - type: nauc_mrr_at_20_diff1
      value: 55.4072
    - type: nauc_mrr_at_100_max
      value: 48.4835
    - type: nauc_mrr_at_100_std
      value: 6.2885
    - type: nauc_mrr_at_100_diff1
      value: 55.3743
    - type: nauc_mrr_at_1000_max
      value: 48.4769
    - type: nauc_mrr_at_1000_std
      value: 6.2978000000000005
    - type: nauc_mrr_at_1000_diff1
      value: 55.3852
    - type: main_score
      value: 38.778
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB COIRCodeSearchNetRetrieval (go)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 42.809999999999995
    - type: ndcg_at_3
      value: 51.949999999999996
    - type: ndcg_at_5
      value: 54.217000000000006
    - type: ndcg_at_10
      value: 56.296
    - type: ndcg_at_20
      value: 57.735
    - type: ndcg_at_100
      value: 59.68599999999999
    - type: ndcg_at_1000
      value: 60.812
    - type: map_at_1
      value: 42.809999999999995
    - type: map_at_3
      value: 49.727
    - type: map_at_5
      value: 50.988
    - type: map_at_10
      value: 51.847
    - type: map_at_20
      value: 52.248000000000005
    - type: map_at_100
      value: 52.52
    - type: map_at_1000
      value: 52.561
    - type: recall_at_1
      value: 42.809999999999995
    - type: recall_at_3
      value: 58.372
    - type: recall_at_5
      value: 63.864
    - type: recall_at_10
      value: 70.291
    - type: recall_at_20
      value: 75.92999999999999
    - type: recall_at_100
      value: 86.432
    - type: recall_at_1000
      value: 95.371
    - type: precision_at_1
      value: 42.809999999999995
    - type: precision_at_3
      value: 19.457
    - type: precision_at_5
      value: 12.773000000000001
    - type: precision_at_10
      value: 7.029000000000001
    - type: precision_at_20
      value: 3.7960000000000003
    - type: precision_at_100
      value: 0.864
    - type: precision_at_1000
      value: 0.095
    - type: mrr_at_1
      value: 42.8097
    - type: mrr_at_3
      value: 49.7271
    - type: mrr_at_5
      value: 50.987899999999996
    - type: mrr_at_10
      value: 51.847100000000005
    - type: mrr_at_20
      value: 52.2483
    - type: mrr_at_100
      value: 52.519499999999994
    - type: mrr_at_1000
      value: 52.560700000000004
    - type: nauc_ndcg_at_1_max
      value: 42.5169
    - type: nauc_ndcg_at_1_std
      value: -2.56
    - type: nauc_ndcg_at_1_diff1
      value: 61.5235
    - type: nauc_ndcg_at_3_max
      value: 43.897999999999996
    - type: nauc_ndcg_at_3_std
      value: -0.927
    - type: nauc_ndcg_at_3_diff1
      value: 55.5453
    - type: nauc_ndcg_at_5_max
      value: 44.069199999999995
    - type: nauc_ndcg_at_5_std
      value: -0.5125000000000001
    - type: nauc_ndcg_at_5_diff1
      value: 55.095000000000006
    - type: nauc_ndcg_at_10_max
      value: 43.9261
    - type: nauc_ndcg_at_10_std
      value: 0.218
    - type: nauc_ndcg_at_10_diff1
      value: 54.7159
    - type: nauc_ndcg_at_20_max
      value: 44.0206
    - type: nauc_ndcg_at_20_std
      value: 0.8718999999999999
    - type: nauc_ndcg_at_20_diff1
      value: 54.830400000000004
    - type: nauc_ndcg_at_100_max
      value: 43.7526
    - type: nauc_ndcg_at_100_std
      value: 0.9793
    - type: nauc_ndcg_at_100_diff1
      value: 54.9701
    - type: nauc_ndcg_at_1000_max
      value: 43.8809
    - type: nauc_ndcg_at_1000_std
      value: 0.7155
    - type: nauc_ndcg_at_1000_diff1
      value: 55.3053
    - type: nauc_map_at_1_max
      value: 42.5169
    - type: nauc_map_at_1_std
      value: -2.56
    - type: nauc_map_at_1_diff1
      value: 61.5235
    - type: nauc_map_at_3_max
      value: 43.5908
    - type: nauc_map_at_3_std
      value: -1.3469
    - type: nauc_map_at_3_diff1
      value: 56.9825
    - type: nauc_map_at_5_max
      value: 43.674099999999996
    - type: nauc_map_at_5_std
      value: -1.1391
    - type: nauc_map_at_5_diff1
      value: 56.7628
    - type: nauc_map_at_10_max
      value: 43.6154
    - type: nauc_map_at_10_std
      value: -0.861
    - type: nauc_map_at_10_diff1
      value: 56.6439
    - type: nauc_map_at_20_max
      value: 43.650099999999995
    - type: nauc_map_at_20_std
      value: -0.6788
    - type: nauc_map_at_20_diff1
      value: 56.6917
    - type: nauc_map_at_100_max
      value: 43.6075
    - type: nauc_map_at_100_std
      value: -0.6773
    - type: nauc_map_at_100_diff1
      value: 56.7132
    - type: nauc_map_at_1000_max
      value: 43.6113
    - type: nauc_map_at_1000_std
      value: -0.6847
    - type: nauc_map_at_1000_diff1
      value: 56.725300000000004
    - type: nauc_recall_at_1_max
      value: 42.5169
    - type: nauc_recall_at_1_std
      value: -2.56
    - type: nauc_recall_at_1_diff1
      value: 61.5235
    - type: nauc_recall_at_3_max
      value: 44.8282
    - type: nauc_recall_at_3_std
      value: 0.3731
    - type: nauc_recall_at_3_diff1
      value: 51.139199999999995
    - type: nauc_recall_at_5_max
      value: 45.3912
    - type: nauc_recall_at_5_std
      value: 1.6466999999999998
    - type: nauc_recall_at_5_diff1
      value: 49.5336
    - type: nauc_recall_at_10_max
      value: 45.0172
    - type: nauc_recall_at_10_std
      value: 4.702
    - type: nauc_recall_at_10_diff1
      value: 47.287600000000005
    - type: nauc_recall_at_20_max
      value: 45.5956
    - type: nauc_recall_at_20_std
      value: 8.8859
    - type: nauc_recall_at_20_diff1
      value: 46.5039
    - type: nauc_recall_at_100_max
      value: 43.7193
    - type: nauc_recall_at_100_std
      value: 15.4564
    - type: nauc_recall_at_100_diff1
      value: 42.9843
    - type: nauc_recall_at_1000_max
      value: 49.6578
    - type: nauc_recall_at_1000_std
      value: 28.1802
    - type: nauc_recall_at_1000_diff1
      value: 37.0098
    - type: nauc_precision_at_1_max
      value: 42.5169
    - type: nauc_precision_at_1_std
      value: -2.56
    - type: nauc_precision_at_1_diff1
      value: 61.5235
    - type: nauc_precision_at_3_max
      value: 44.8282
    - type: nauc_precision_at_3_std
      value: 0.3731
    - type: nauc_precision_at_3_diff1
      value: 51.139199999999995
    - type: nauc_precision_at_5_max
      value: 45.3912
    - type: nauc_precision_at_5_std
      value: 1.6466999999999998
    - type: nauc_precision_at_5_diff1
      value: 49.5336
    - type: nauc_precision_at_10_max
      value: 45.0172
    - type: nauc_precision_at_10_std
      value: 4.702
    - type: nauc_precision_at_10_diff1
      value: 47.287600000000005
    - type: nauc_precision_at_20_max
      value: 45.5956
    - type: nauc_precision_at_20_std
      value: 8.8859
    - type: nauc_precision_at_20_diff1
      value: 46.5039
    - type: nauc_precision_at_100_max
      value: 43.7193
    - type: nauc_precision_at_100_std
      value: 15.4564
    - type: nauc_precision_at_100_diff1
      value: 42.9843
    - type: nauc_precision_at_1000_max
      value: 49.6578
    - type: nauc_precision_at_1000_std
      value: 28.1802
    - type: nauc_precision_at_1000_diff1
      value: 37.0098
    - type: nauc_mrr_at_1_max
      value: 42.5169
    - type: nauc_mrr_at_1_std
      value: -2.56
    - type: nauc_mrr_at_1_diff1
      value: 61.5235
    - type: nauc_mrr_at_3_max
      value: 43.5908
    - type: nauc_mrr_at_3_std
      value: -1.3469
    - type: nauc_mrr_at_3_diff1
      value: 56.9825
    - type: nauc_mrr_at_5_max
      value: 43.674099999999996
    - type: nauc_mrr_at_5_std
      value: -1.1391
    - type: nauc_mrr_at_5_diff1
      value: 56.7628
    - type: nauc_mrr_at_10_max
      value: 43.6154
    - type: nauc_mrr_at_10_std
      value: -0.861
    - type: nauc_mrr_at_10_diff1
      value: 56.6439
    - type: nauc_mrr_at_20_max
      value: 43.650099999999995
    - type: nauc_mrr_at_20_std
      value: -0.6788
    - type: nauc_mrr_at_20_diff1
      value: 56.6917
    - type: nauc_mrr_at_100_max
      value: 43.6075
    - type: nauc_mrr_at_100_std
      value: -0.6773
    - type: nauc_mrr_at_100_diff1
      value: 56.7132
    - type: nauc_mrr_at_1000_max
      value: 43.6113
    - type: nauc_mrr_at_1000_std
      value: -0.6847
    - type: nauc_mrr_at_1000_diff1
      value: 56.725300000000004
    - type: main_score
      value: 56.296
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB COIRCodeSearchNetRetrieval (ruby)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 31.721
    - type: ndcg_at_3
      value: 38.559
    - type: ndcg_at_5
      value: 40.303
    - type: ndcg_at_10
      value: 42.536
    - type: ndcg_at_20
      value: 44.05
    - type: ndcg_at_100
      value: 46.565
    - type: ndcg_at_1000
      value: 48.447
    - type: map_at_1
      value: 31.721
    - type: map_at_3
      value: 36.915
    - type: map_at_5
      value: 37.891000000000005
    - type: map_at_10
      value: 38.814
    - type: map_at_20
      value: 39.236
    - type: map_at_100
      value: 39.574
    - type: map_at_1000
      value: 39.641999999999996
    - type: recall_at_1
      value: 31.721
    - type: recall_at_3
      value: 43.299
    - type: recall_at_5
      value: 47.502
    - type: recall_at_10
      value: 54.400999999999996
    - type: recall_at_20
      value: 60.349
    - type: recall_at_100
      value: 74.068
    - type: recall_at_1000
      value: 89.056
    - type: precision_at_1
      value: 31.721
    - type: precision_at_3
      value: 14.433000000000002
    - type: precision_at_5
      value: 9.5
    - type: precision_at_10
      value: 5.4399999999999995
    - type: precision_at_20
      value: 3.017
    - type: precision_at_100
      value: 0.741
    - type: precision_at_1000
      value: 0.089
    - type: mrr_at_1
      value: 31.7209
    - type: mrr_at_3
      value: 36.9151
    - type: mrr_at_5
      value: 37.8906
    - type: mrr_at_10
      value: 38.8144
    - type: mrr_at_20
      value: 39.2355
    - type: mrr_at_100
      value: 39.5737
    - type: mrr_at_1000
      value: 39.641999999999996
    - type: nauc_ndcg_at_1_max
      value: 46.428999999999995
    - type: nauc_ndcg_at_1_std
      value: 0.0014
    - type: nauc_ndcg_at_1_diff1
      value: 59.6017
    - type: nauc_ndcg_at_3_max
      value: 45.9805
    - type: nauc_ndcg_at_3_std
      value: 0.5511
    - type: nauc_ndcg_at_3_diff1
      value: 53.4978
    - type: nauc_ndcg_at_5_max
      value: 45.5339
    - type: nauc_ndcg_at_5_std
      value: 1.2229
    - type: nauc_ndcg_at_5_diff1
      value: 51.798500000000004
    - type: nauc_ndcg_at_10_max
      value: 44.018
    - type: nauc_ndcg_at_10_std
      value: 1.6709
    - type: nauc_ndcg_at_10_diff1
      value: 50.428799999999995
    - type: nauc_ndcg_at_20_max
      value: 43.5252
    - type: nauc_ndcg_at_20_std
      value: 2.4627
    - type: nauc_ndcg_at_20_diff1
      value: 50.6172
    - type: nauc_ndcg_at_100_max
      value: 43.723099999999995
    - type: nauc_ndcg_at_100_std
      value: 4.0416
    - type: nauc_ndcg_at_100_diff1
      value: 50.135600000000004
    - type: nauc_ndcg_at_1000_max
      value: 43.7739
    - type: nauc_ndcg_at_1000_std
      value: 3.4729
    - type: nauc_ndcg_at_1000_diff1
      value: 50.6595
    - type: nauc_map_at_1_max
      value: 46.428999999999995
    - type: nauc_map_at_1_std
      value: 0.0014
    - type: nauc_map_at_1_diff1
      value: 59.6017
    - type: nauc_map_at_3_max
      value: 46.217999999999996
    - type: nauc_map_at_3_std
      value: 0.43889999999999996
    - type: nauc_map_at_3_diff1
      value: 54.882299999999994
    - type: nauc_map_at_5_max
      value: 45.9757
    - type: nauc_map_at_5_std
      value: 0.8049999999999999
    - type: nauc_map_at_5_diff1
      value: 53.950900000000004
    - type: nauc_map_at_10_max
      value: 45.3363
    - type: nauc_map_at_10_std
      value: 0.9662999999999999
    - type: nauc_map_at_10_diff1
      value: 53.369
    - type: nauc_map_at_20_max
      value: 45.2008
    - type: nauc_map_at_20_std
      value: 1.1801000000000001
    - type: nauc_map_at_20_diff1
      value: 53.4425
    - type: nauc_map_at_100_max
      value: 45.226699999999994
    - type: nauc_map_at_100_std
      value: 1.3667
    - type: nauc_map_at_100_diff1
      value: 53.4089
    - type: nauc_map_at_1000_max
      value: 45.2252
    - type: nauc_map_at_1000_std
      value: 1.3433000000000002
    - type: nauc_map_at_1000_diff1
      value: 53.4268
    - type: nauc_recall_at_1_max
      value: 46.428999999999995
    - type: nauc_recall_at_1_std
      value: 0.0014
    - type: nauc_recall_at_1_diff1
      value: 59.6017
    - type: nauc_recall_at_3_max
      value: 45.2499
    - type: nauc_recall_at_3_std
      value: 0.8637
    - type: nauc_recall_at_3_diff1
      value: 49.5773
    - type: nauc_recall_at_5_max
      value: 44.1355
    - type: nauc_recall_at_5_std
      value: 2.5255
    - type: nauc_recall_at_5_diff1
      value: 45.3656
    - type: nauc_recall_at_10_max
      value: 39.313700000000004
    - type: nauc_recall_at_10_std
      value: 4.1421
    - type: nauc_recall_at_10_diff1
      value: 40.8109
    - type: nauc_recall_at_20_max
      value: 36.923
    - type: nauc_recall_at_20_std
      value: 7.691199999999999
    - type: nauc_recall_at_20_diff1
      value: 40.8715
    - type: nauc_recall_at_100_max
      value: 36.296
    - type: nauc_recall_at_100_std
      value: 22.020999999999997
    - type: nauc_recall_at_100_diff1
      value: 33.400800000000004
    - type: nauc_recall_at_1000_max
      value: 30.508999999999997
    - type: nauc_recall_at_1000_std
      value: 29.497600000000002
    - type: nauc_recall_at_1000_diff1
      value: 27.5001
    - type: nauc_precision_at_1_max
      value: 46.428999999999995
    - type: nauc_precision_at_1_std
      value: 0.0014
    - type: nauc_precision_at_1_diff1
      value: 59.6017
    - type: nauc_precision_at_3_max
      value: 45.2499
    - type: nauc_precision_at_3_std
      value: 0.8637
    - type: nauc_precision_at_3_diff1
      value: 49.5773
    - type: nauc_precision_at_5_max
      value: 44.1355
    - type: nauc_precision_at_5_std
      value: 2.5255
    - type: nauc_precision_at_5_diff1
      value: 45.3656
    - type: nauc_precision_at_10_max
      value: 39.313700000000004
    - type: nauc_precision_at_10_std
      value: 4.1421
    - type: nauc_precision_at_10_diff1
      value: 40.8109
    - type: nauc_precision_at_20_max
      value: 36.923
    - type: nauc_precision_at_20_std
      value: 7.691199999999999
    - type: nauc_precision_at_20_diff1
      value: 40.8715
    - type: nauc_precision_at_100_max
      value: 36.296
    - type: nauc_precision_at_100_std
      value: 22.020999999999997
    - type: nauc_precision_at_100_diff1
      value: 33.400800000000004
    - type: nauc_precision_at_1000_max
      value: 30.508999999999997
    - type: nauc_precision_at_1000_std
      value: 29.497600000000002
    - type: nauc_precision_at_1000_diff1
      value: 27.5001
    - type: nauc_mrr_at_1_max
      value: 46.428999999999995
    - type: nauc_mrr_at_1_std
      value: 0.0014
    - type: nauc_mrr_at_1_diff1
      value: 59.6017
    - type: nauc_mrr_at_3_max
      value: 46.217999999999996
    - type: nauc_mrr_at_3_std
      value: 0.43889999999999996
    - type: nauc_mrr_at_3_diff1
      value: 54.882299999999994
    - type: nauc_mrr_at_5_max
      value: 45.9757
    - type: nauc_mrr_at_5_std
      value: 0.8049999999999999
    - type: nauc_mrr_at_5_diff1
      value: 53.950900000000004
    - type: nauc_mrr_at_10_max
      value: 45.3363
    - type: nauc_mrr_at_10_std
      value: 0.9662999999999999
    - type: nauc_mrr_at_10_diff1
      value: 53.369
    - type: nauc_mrr_at_20_max
      value: 45.2008
    - type: nauc_mrr_at_20_std
      value: 1.1801000000000001
    - type: nauc_mrr_at_20_diff1
      value: 53.4425
    - type: nauc_mrr_at_100_max
      value: 45.226699999999994
    - type: nauc_mrr_at_100_std
      value: 1.3667
    - type: nauc_mrr_at_100_diff1
      value: 53.4089
    - type: nauc_mrr_at_1000_max
      value: 45.2252
    - type: nauc_mrr_at_1000_std
      value: 1.3433000000000002
    - type: nauc_mrr_at_1000_diff1
      value: 53.4268
    - type: main_score
      value: 42.536
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB COIRCodeSearchNetRetrieval (java)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 36.887
    - type: ndcg_at_3
      value: 44.671
    - type: ndcg_at_5
      value: 46.619
    - type: ndcg_at_10
      value: 48.54
    - type: ndcg_at_20
      value: 49.881
    - type: ndcg_at_100
      value: 51.847
    - type: ndcg_at_1000
      value: 53.286
    - type: map_at_1
      value: 36.887
    - type: map_at_3
      value: 42.805
    - type: map_at_5
      value: 43.884
    - type: map_at_10
      value: 44.68
    - type: map_at_20
      value: 45.051
    - type: map_at_100
      value: 45.316
    - type: map_at_1000
      value: 45.364
    - type: recall_at_1
      value: 36.887
    - type: recall_at_3
      value: 50.05
    - type: recall_at_5
      value: 54.788000000000004
    - type: recall_at_10
      value: 60.711999999999996
    - type: recall_at_20
      value: 65.997
    - type: recall_at_100
      value: 76.696
    - type: recall_at_1000
      value: 88.371
    - type: precision_at_1
      value: 36.887
    - type: precision_at_3
      value: 16.683
    - type: precision_at_5
      value: 10.958
    - type: precision_at_10
      value: 6.071
    - type: precision_at_20
      value: 3.3000000000000003
    - type: precision_at_100
      value: 0.767
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 36.9147
    - type: mrr_at_3
      value: 42.823699999999995
    - type: mrr_at_5
      value: 43.8985
    - type: mrr_at_10
      value: 44.6961
    - type: mrr_at_20
      value: 45.067
    - type: mrr_at_100
      value: 45.3318
    - type: mrr_at_1000
      value: 45.3801
    - type: nauc_ndcg_at_1_max
      value: 42.8063
    - type: nauc_ndcg_at_1_std
      value: -5.3001
    - type: nauc_ndcg_at_1_diff1
      value: 63.370099999999994
    - type: nauc_ndcg_at_3_max
      value: 44.0649
    - type: nauc_ndcg_at_3_std
      value: -4.0304
    - type: nauc_ndcg_at_3_diff1
      value: 57.7429
    - type: nauc_ndcg_at_5_max
      value: 43.864799999999995
    - type: nauc_ndcg_at_5_std
      value: -3.2800000000000002
    - type: nauc_ndcg_at_5_diff1
      value: 57.0472
    - type: nauc_ndcg_at_10_max
      value: 43.614799999999995
    - type: nauc_ndcg_at_10_std
      value: -2.424
    - type: nauc_ndcg_at_10_diff1
      value: 56.3498
    - type: nauc_ndcg_at_20_max
      value: 43.6108
    - type: nauc_ndcg_at_20_std
      value: -1.699
    - type: nauc_ndcg_at_20_diff1
      value: 56.2153
    - type: nauc_ndcg_at_100_max
      value: 43.4705
    - type: nauc_ndcg_at_100_std
      value: -0.7144
    - type: nauc_ndcg_at_100_diff1
      value: 56.0679
    - type: nauc_ndcg_at_1000_max
      value: 43.6856
    - type: nauc_ndcg_at_1000_std
      value: -0.7129
    - type: nauc_ndcg_at_1000_diff1
      value: 56.40540000000001
    - type: nauc_map_at_1_max
      value: 42.8063
    - type: nauc_map_at_1_std
      value: -5.3001
    - type: nauc_map_at_1_diff1
      value: 63.370099999999994
    - type: nauc_map_at_3_max
      value: 43.797999999999995
    - type: nauc_map_at_3_std
      value: -4.3491
    - type: nauc_map_at_3_diff1
      value: 59.0673
    - type: nauc_map_at_5_max
      value: 43.6812
    - type: nauc_map_at_5_std
      value: -3.9397
    - type: nauc_map_at_5_diff1
      value: 58.6982
    - type: nauc_map_at_10_max
      value: 43.5745
    - type: nauc_map_at_10_std
      value: -3.6122
    - type: nauc_map_at_10_diff1
      value: 58.431999999999995
    - type: nauc_map_at_20_max
      value: 43.573
    - type: nauc_map_at_20_std
      value: -3.4323
    - type: nauc_map_at_20_diff1
      value: 58.4168
    - type: nauc_map_at_100_max
      value: 43.5448
    - type: nauc_map_at_100_std
      value: -3.3167
    - type: nauc_map_at_100_diff1
      value: 58.394999999999996
    - type: nauc_map_at_1000_max
      value: 43.5506
    - type: nauc_map_at_1000_std
      value: -3.3144
    - type: nauc_map_at_1000_diff1
      value: 58.4057
    - type: nauc_recall_at_1_max
      value: 42.8063
    - type: nauc_recall_at_1_std
      value: -5.3001
    - type: nauc_recall_at_1_diff1
      value: 63.370099999999994
    - type: nauc_recall_at_3_max
      value: 44.8286
    - type: nauc_recall_at_3_std
      value: -3.0949999999999998
    - type: nauc_recall_at_3_diff1
      value: 53.8907
    - type: nauc_recall_at_5_max
      value: 44.3801
    - type: nauc_recall_at_5_std
      value: -1.1593
    - type: nauc_recall_at_5_diff1
      value: 51.948899999999995
    - type: nauc_recall_at_10_max
      value: 43.6005
    - type: nauc_recall_at_10_std
      value: 1.9532999999999998
    - type: nauc_recall_at_10_diff1
      value: 49.2211
    - type: nauc_recall_at_20_max
      value: 43.5839
    - type: nauc_recall_at_20_std
      value: 5.8288
    - type: nauc_recall_at_20_diff1
      value: 47.7761
    - type: nauc_recall_at_100_max
      value: 42.6633
    - type: nauc_recall_at_100_std
      value: 16.4317
    - type: nauc_recall_at_100_diff1
      value: 44.0676
    - type: nauc_recall_at_1000_max
      value: 46.698
    - type: nauc_recall_at_1000_std
      value: 30.054799999999997
    - type: nauc_recall_at_1000_diff1
      value: 41.5816
    - type: nauc_precision_at_1_max
      value: 42.8063
    - type: nauc_precision_at_1_std
      value: -5.3001
    - type: nauc_precision_at_1_diff1
      value: 63.370099999999994
    - type: nauc_precision_at_3_max
      value: 44.8286
    - type: nauc_precision_at_3_std
      value: -3.0949999999999998
    - type: nauc_precision_at_3_diff1
      value: 53.8907
    - type: nauc_precision_at_5_max
      value: 44.3801
    - type: nauc_precision_at_5_std
      value: -1.1593
    - type: nauc_precision_at_5_diff1
      value: 51.948899999999995
    - type: nauc_precision_at_10_max
      value: 43.6005
    - type: nauc_precision_at_10_std
      value: 1.9532999999999998
    - type: nauc_precision_at_10_diff1
      value: 49.2211
    - type: nauc_precision_at_20_max
      value: 43.5839
    - type: nauc_precision_at_20_std
      value: 5.8288
    - type: nauc_precision_at_20_diff1
      value: 47.7761
    - type: nauc_precision_at_100_max
      value: 42.6633
    - type: nauc_precision_at_100_std
      value: 16.4317
    - type: nauc_precision_at_100_diff1
      value: 44.0676
    - type: nauc_precision_at_1000_max
      value: 46.698
    - type: nauc_precision_at_1000_std
      value: 30.054799999999997
    - type: nauc_precision_at_1000_diff1
      value: 41.5816
    - type: nauc_mrr_at_1_max
      value: 42.7425
    - type: nauc_mrr_at_1_std
      value: -5.2358
    - type: nauc_mrr_at_1_diff1
      value: 63.285199999999996
    - type: nauc_mrr_at_3_max
      value: 43.763200000000005
    - type: nauc_mrr_at_3_std
      value: -4.2973
    - type: nauc_mrr_at_3_diff1
      value: 59.031
    - type: nauc_mrr_at_5_max
      value: 43.650800000000004
    - type: nauc_mrr_at_5_std
      value: -3.8918
    - type: nauc_mrr_at_5_diff1
      value: 58.6636
    - type: nauc_mrr_at_10_max
      value: 43.5429
    - type: nauc_mrr_at_10_std
      value: -3.5659000000000005
    - type: nauc_mrr_at_10_diff1
      value: 58.3946
    - type: nauc_mrr_at_20_max
      value: 43.5411
    - type: nauc_mrr_at_20_std
      value: -3.3855000000000004
    - type: nauc_mrr_at_20_diff1
      value: 58.379099999999994
    - type: nauc_mrr_at_100_max
      value: 43.5128
    - type: nauc_mrr_at_100_std
      value: -3.2696000000000005
    - type: nauc_mrr_at_100_diff1
      value: 58.3572
    - type: nauc_mrr_at_1000_max
      value: 43.5186
    - type: nauc_mrr_at_1000_std
      value: -3.2672
    - type: nauc_mrr_at_1000_diff1
      value: 58.3678
    - type: main_score
      value: 48.54
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB COIRCodeSearchNetRetrieval (php)
      revision: 4adc7bc41202b5c13543c9c886a25f340634dab3
      split: test
      type: CoIR-Retrieval/CodeSearchNet
    metrics:
    - type: ndcg_at_1
      value: 30.734
    - type: ndcg_at_3
      value: 38.155
    - type: ndcg_at_5
      value: 40.306999999999995
    - type: ndcg_at_10
      value: 42.510999999999996
    - type: ndcg_at_20
      value: 44.156
    - type: ndcg_at_100
      value: 46.641
    - type: ndcg_at_1000
      value: 48.359
    - type: map_at_1
      value: 30.734
    - type: map_at_3
      value: 36.347
    - type: map_at_5
      value: 37.539
    - type: map_at_10
      value: 38.455
    - type: map_at_20
      value: 38.906
    - type: map_at_100
      value: 39.24
    - type: map_at_1000
      value: 39.300000000000004
    - type: recall_at_1
      value: 30.734
    - type: recall_at_3
      value: 43.378
    - type: recall_at_5
      value: 48.616
    - type: recall_at_10
      value: 55.395
    - type: recall_at_20
      value: 61.91
    - type: recall_at_100
      value: 75.432
    - type: recall_at_1000
      value: 89.254
    - type: precision_at_1
      value: 30.734
    - type: precision_at_3
      value: 14.459
    - type: precision_at_5
      value: 9.722999999999999
    - type: precision_at_10
      value: 5.539000000000001
    - type: precision_at_20
      value: 3.0949999999999998
    - type: precision_at_100
      value: 0.754
    - type: precision_at_1000
      value: 0.089
    - type: mrr_at_1
      value: 30.6907
    - type: mrr_at_3
      value: 36.3137
    - type: mrr_at_5
      value: 37.5121
    - type: mrr_at_10
      value: 38.4289
    - type: mrr_at_20
      value: 38.8786
    - type: mrr_at_100
      value: 39.2136
    - type: mrr_at_1000
      value: 39.2729
    - type: nauc_ndcg_at_1_max
      value: 36.8055
    - type: nauc_ndcg_at_1_std
      value: -1.5909
    - type: nauc_ndcg_at_1_diff1
      value: 55.9244
    - type: nauc_ndcg_at_3_max
      value: 38.4262
    - type: nauc_ndcg_at_3_std
      value: 0.5292
    - type: nauc_ndcg_at_3_diff1
      value: 49.7477
    - type: nauc_ndcg_at_5_max
      value: 38.0552
    - type: nauc_ndcg_at_5_std
      value: 1.102
    - type: nauc_ndcg_at_5_diff1
      value: 48.5308
    - type: nauc_ndcg_at_10_max
      value: 38.0054
    - type: nauc_ndcg_at_10_std
      value: 1.9313
    - type: nauc_ndcg_at_10_diff1
      value: 48.016999999999996
    - type: nauc_ndcg_at_20_max
      value: 37.8808
    - type: nauc_ndcg_at_20_std
      value: 2.56
    - type: nauc_ndcg_at_20_diff1
      value: 47.5649
    - type: nauc_ndcg_at_100_max
      value: 38.3754
    - type: nauc_ndcg_at_100_std
      value: 3.6703
    - type: nauc_ndcg_at_100_diff1
      value: 47.6154
    - type: nauc_ndcg_at_1000_max
      value: 38.534600000000005
    - type: nauc_ndcg_at_1000_std
      value: 3.7317000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 48.0299
    - type: nauc_map_at_1_max
      value: 36.8055
    - type: nauc_map_at_1_std
      value: -1.5909
    - type: nauc_map_at_1_diff1
      value: 55.9244
    - type: nauc_map_at_3_max
      value: 38.0383
    - type: nauc_map_at_3_std
      value: 0.0207
    - type: nauc_map_at_3_diff1
      value: 51.137299999999996
    - type: nauc_map_at_5_max
      value: 37.8223
    - type: nauc_map_at_5_std
      value: 0.3179
    - type: nauc_map_at_5_diff1
      value: 50.4641
    - type: nauc_map_at_10_max
      value: 37.8022
    - type: nauc_map_at_10_std
      value: 0.6617999999999999
    - type: nauc_map_at_10_diff1
      value: 50.269
    - type: nauc_map_at_20_max
      value: 37.7686
    - type: nauc_map_at_20_std
      value: 0.8326999999999999
    - type: nauc_map_at_20_diff1
      value: 50.153499999999994
    - type: nauc_map_at_100_max
      value: 37.832300000000004
    - type: nauc_map_at_100_std
      value: 0.9767
    - type: nauc_map_at_100_diff1
      value: 50.174099999999996
    - type: nauc_map_at_1000_max
      value: 37.838300000000004
    - type: nauc_map_at_1000_std
      value: 0.9815
    - type: nauc_map_at_1000_diff1
      value: 50.1882
    - type: nauc_recall_at_1_max
      value: 36.8055
    - type: nauc_recall_at_1_std
      value: -1.5909
    - type: nauc_recall_at_1_diff1
      value: 55.9244
    - type: nauc_recall_at_3_max
      value: 39.5304
    - type: nauc_recall_at_3_std
      value: 1.9767
    - type: nauc_recall_at_3_diff1
      value: 45.8281
    - type: nauc_recall_at_5_max
      value: 38.6851
    - type: nauc_recall_at_5_std
      value: 3.4711
    - type: nauc_recall_at_5_diff1
      value: 42.8172
    - type: nauc_recall_at_10_max
      value: 38.5524
    - type: nauc_recall_at_10_std
      value: 6.2315000000000005
    - type: nauc_recall_at_10_diff1
      value: 40.801
    - type: nauc_recall_at_20_max
      value: 38.048300000000005
    - type: nauc_recall_at_20_std
      value: 9.3045
    - type: nauc_recall_at_20_diff1
      value: 38.222
    - type: nauc_recall_at_100_max
      value: 42.054399999999994
    - type: nauc_recall_at_100_std
      value: 20.4425
    - type: nauc_recall_at_100_diff1
      value: 35.0773
    - type: nauc_recall_at_1000_max
      value: 49.2856
    - type: nauc_recall_at_1000_std
      value: 38.4529
    - type: nauc_recall_at_1000_diff1
      value: 31.7647
    - type: nauc_precision_at_1_max
      value: 36.8055
    - type: nauc_precision_at_1_std
      value: -1.5909
    - type: nauc_precision_at_1_diff1
      value: 55.9244
    - type: nauc_precision_at_3_max
      value: 39.5304
    - type: nauc_precision_at_3_std
      value: 1.9767
    - type: nauc_precision_at_3_diff1
      value: 45.8281
    - type: nauc_precision_at_5_max
      value: 38.6851
    - type: nauc_precision_at_5_std
      value: 3.4711
    - type: nauc_precision_at_5_diff1
      value: 42.8172
    - type: nauc_precision_at_10_max
      value: 38.5524
    - type: nauc_precision_at_10_std
      value: 6.2315000000000005
    - type: nauc_precision_at_10_diff1
      value: 40.801
    - type: nauc_precision_at_20_max
      value: 38.048300000000005
    - type: nauc_precision_at_20_std
      value: 9.3045
    - type: nauc_precision_at_20_diff1
      value: 38.222
    - type: nauc_precision_at_100_max
      value: 42.054399999999994
    - type: nauc_precision_at_100_std
      value: 20.4425
    - type: nauc_precision_at_100_diff1
      value: 35.0773
    - type: nauc_precision_at_1000_max
      value: 49.2856
    - type: nauc_precision_at_1000_std
      value: 38.4529
    - type: nauc_precision_at_1000_diff1
      value: 31.7647
    - type: nauc_mrr_at_1_max
      value: 36.8365
    - type: nauc_mrr_at_1_std
      value: -1.4754
    - type: nauc_mrr_at_1_diff1
      value: 56.0597
    - type: nauc_mrr_at_3_max
      value: 38.054
    - type: nauc_mrr_at_3_std
      value: 0.09430000000000001
    - type: nauc_mrr_at_3_diff1
      value: 51.2016
    - type: nauc_mrr_at_5_max
      value: 37.8431
    - type: nauc_mrr_at_5_std
      value: 0.3829
    - type: nauc_mrr_at_5_diff1
      value: 50.5285
    - type: nauc_mrr_at_10_max
      value: 37.8231
    - type: nauc_mrr_at_10_std
      value: 0.7271
    - type: nauc_mrr_at_10_diff1
      value: 50.333099999999995
    - type: nauc_mrr_at_20_max
      value: 37.7905
    - type: nauc_mrr_at_20_std
      value: 0.8992999999999999
    - type: nauc_mrr_at_20_diff1
      value: 50.2181
    - type: nauc_mrr_at_100_max
      value: 37.853500000000004
    - type: nauc_mrr_at_100_std
      value: 1.0428
    - type: nauc_mrr_at_100_diff1
      value: 50.239
    - type: nauc_mrr_at_1000_max
      value: 37.859500000000004
    - type: nauc_mrr_at_1000_std
      value: 1.0477
    - type: nauc_mrr_at_1000_diff1
      value: 50.2532
    - type: main_score
      value: 42.510999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: ndcg_at_1
      value: 42.918
    - type: ndcg_at_3
      value: 47.992000000000004
    - type: ndcg_at_5
      value: 50.298
    - type: ndcg_at_10
      value: 53.047999999999995
    - type: ndcg_at_20
      value: 55.36600000000001
    - type: ndcg_at_100
      value: 58.18
    - type: ndcg_at_1000
      value: 59.992999999999995
    - type: map_at_1
      value: 35.147
    - type: map_at_3
      value: 42.985
    - type: map_at_5
      value: 44.895
    - type: map_at_10
      value: 46.568
    - type: map_at_20
      value: 47.527
    - type: map_at_100
      value: 48.178
    - type: map_at_1000
      value: 48.303000000000004
    - type: recall_at_1
      value: 35.147
    - type: recall_at_3
      value: 50.229
    - type: recall_at_5
      value: 56.586999999999996
    - type: recall_at_10
      value: 64.656
    - type: recall_at_20
      value: 72.875
    - type: recall_at_100
      value: 85.397
    - type: recall_at_1000
      value: 96.799
    - type: precision_at_1
      value: 42.918
    - type: precision_at_3
      value: 22.698999999999998
    - type: precision_at_5
      value: 16.309
    - type: precision_at_10
      value: 10.100000000000001
    - type: precision_at_20
      value: 6.0440000000000005
    - type: precision_at_100
      value: 1.5890000000000002
    - type: precision_at_1000
      value: 0.209
    - type: mrr_at_1
      value: 42.9185
    - type: mrr_at_3
      value: 50.1907
    - type: mrr_at_5
      value: 51.9003
    - type: mrr_at_10
      value: 52.824400000000004
    - type: mrr_at_20
      value: 53.3002
    - type: mrr_at_100
      value: 53.5134
    - type: mrr_at_1000
      value: 53.5569
    - type: nauc_ndcg_at_1_max
      value: 45.115300000000005
    - type: nauc_ndcg_at_1_std
      value: -5.3469999999999995
    - type: nauc_ndcg_at_1_diff1
      value: 50.792899999999996
    - type: nauc_ndcg_at_3_max
      value: 44.379000000000005
    - type: nauc_ndcg_at_3_std
      value: -2.628
    - type: nauc_ndcg_at_3_diff1
      value: 45.6678
    - type: nauc_ndcg_at_5_max
      value: 44.8852
    - type: nauc_ndcg_at_5_std
      value: -1.7051
    - type: nauc_ndcg_at_5_diff1
      value: 46.0814
    - type: nauc_ndcg_at_10_max
      value: 43.969500000000004
    - type: nauc_ndcg_at_10_std
      value: -0.4902
    - type: nauc_ndcg_at_10_diff1
      value: 46.2439
    - type: nauc_ndcg_at_20_max
      value: 44.588499999999996
    - type: nauc_ndcg_at_20_std
      value: 0.5193
    - type: nauc_ndcg_at_20_diff1
      value: 45.9229
    - type: nauc_ndcg_at_100_max
      value: 45.0779
    - type: nauc_ndcg_at_100_std
      value: 1.1967999999999999
    - type: nauc_ndcg_at_100_diff1
      value: 46.090199999999996
    - type: nauc_ndcg_at_1000_max
      value: 45.082
    - type: nauc_ndcg_at_1000_std
      value: 0.3457
    - type: nauc_ndcg_at_1000_diff1
      value: 46.366
    - type: nauc_map_at_1_max
      value: 38.731
    - type: nauc_map_at_1_std
      value: -7.1701
    - type: nauc_map_at_1_diff1
      value: 52.0087
    - type: nauc_map_at_3_max
      value: 42.126799999999996
    - type: nauc_map_at_3_std
      value: -4.8249
    - type: nauc_map_at_3_diff1
      value: 47.7841
    - type: nauc_map_at_5_max
      value: 43.2155
    - type: nauc_map_at_5_std
      value: -3.9702
    - type: nauc_map_at_5_diff1
      value: 47.9376
    - type: nauc_map_at_10_max
      value: 43.4398
    - type: nauc_map_at_10_std
      value: -2.8201
    - type: nauc_map_at_10_diff1
      value: 47.9726
    - type: nauc_map_at_20_max
      value: 43.9625
    - type: nauc_map_at_20_std
      value: -2.4088
    - type: nauc_map_at_20_diff1
      value: 47.7323
    - type: nauc_map_at_100_max
      value: 44.0439
    - type: nauc_map_at_100_std
      value: -2.1932
    - type: nauc_map_at_100_diff1
      value: 47.672399999999996
    - type: nauc_map_at_1000_max
      value: 44.059599999999996
    - type: nauc_map_at_1000_std
      value: -2.2453999999999996
    - type: nauc_map_at_1000_diff1
      value: 47.6659
    - type: nauc_recall_at_1_max
      value: 38.731
    - type: nauc_recall_at_1_std
      value: -7.1701
    - type: nauc_recall_at_1_diff1
      value: 52.0087
    - type: nauc_recall_at_3_max
      value: 40.5229
    - type: nauc_recall_at_3_std
      value: -1.3240999999999998
    - type: nauc_recall_at_3_diff1
      value: 41.1764
    - type: nauc_recall_at_5_max
      value: 41.248000000000005
    - type: nauc_recall_at_5_std
      value: 1.4647999999999999
    - type: nauc_recall_at_5_diff1
      value: 41.044799999999995
    - type: nauc_recall_at_10_max
      value: 38.6375
    - type: nauc_recall_at_10_std
      value: 5.3439
    - type: nauc_recall_at_10_diff1
      value: 39.8162
    - type: nauc_recall_at_20_max
      value: 39.6813
    - type: nauc_recall_at_20_std
      value: 11.1138
    - type: nauc_recall_at_20_diff1
      value: 36.8881
    - type: nauc_recall_at_100_max
      value: 44.9346
    - type: nauc_recall_at_100_std
      value: 22.5203
    - type: nauc_recall_at_100_diff1
      value: 34.8792
    - type: nauc_recall_at_1000_max
      value: 52.49979999999999
    - type: nauc_recall_at_1000_std
      value: 50.954299999999996
    - type: nauc_recall_at_1000_diff1
      value: 36.1016
    - type: nauc_precision_at_1_max
      value: 45.115300000000005
    - type: nauc_precision_at_1_std
      value: -5.3469999999999995
    - type: nauc_precision_at_1_diff1
      value: 50.792899999999996
    - type: nauc_precision_at_3_max
      value: 41.841
    - type: nauc_precision_at_3_std
      value: 3.3930000000000002
    - type: nauc_precision_at_3_diff1
      value: 27.495399999999997
    - type: nauc_precision_at_5_max
      value: 38.527
    - type: nauc_precision_at_5_std
      value: 8.2496
    - type: nauc_precision_at_5_diff1
      value: 19.3628
    - type: nauc_precision_at_10_max
      value: 27.5499
    - type: nauc_precision_at_10_std
      value: 13.264100000000001
    - type: nauc_precision_at_10_diff1
      value: 9.9718
    - type: nauc_precision_at_20_max
      value: 21.431
    - type: nauc_precision_at_20_std
      value: 14.426400000000001
    - type: nauc_precision_at_20_diff1
      value: -0.11030000000000001
    - type: nauc_precision_at_100_max
      value: 6.8088
    - type: nauc_precision_at_100_std
      value: 9.8979
    - type: nauc_precision_at_100_diff1
      value: -10.1603
    - type: nauc_precision_at_1000_max
      value: -6.4949
    - type: nauc_precision_at_1000_std
      value: -3.9967999999999995
    - type: nauc_precision_at_1000_diff1
      value: -17.765800000000002
    - type: nauc_mrr_at_1_max
      value: 45.115300000000005
    - type: nauc_mrr_at_1_std
      value: -5.3469999999999995
    - type: nauc_mrr_at_1_diff1
      value: 50.792899999999996
    - type: nauc_mrr_at_3_max
      value: 45.8581
    - type: nauc_mrr_at_3_std
      value: -2.9239
    - type: nauc_mrr_at_3_diff1
      value: 47.079
    - type: nauc_mrr_at_5_max
      value: 45.5453
    - type: nauc_mrr_at_5_std
      value: -2.2778
    - type: nauc_mrr_at_5_diff1
      value: 47.0394
    - type: nauc_mrr_at_10_max
      value: 45.2727
    - type: nauc_mrr_at_10_std
      value: -2.1793
    - type: nauc_mrr_at_10_diff1
      value: 46.7719
    - type: nauc_mrr_at_20_max
      value: 45.232
    - type: nauc_mrr_at_20_std
      value: -2.0842
    - type: nauc_mrr_at_20_diff1
      value: 46.75
    - type: nauc_mrr_at_100_max
      value: 45.3233
    - type: nauc_mrr_at_100_std
      value: -2.0778000000000003
    - type: nauc_mrr_at_100_diff1
      value: 46.7919
    - type: nauc_mrr_at_1000_max
      value: 45.325700000000005
    - type: nauc_mrr_at_1000_std
      value: -2.0868
    - type: nauc_mrr_at_1000_diff1
      value: 46.812799999999996
    - type: main_score
      value: 53.047999999999995
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
      value: 35.796
    - type: ndcg_at_3
      value: 40.036
    - type: ndcg_at_5
      value: 41.778
    - type: ndcg_at_10
      value: 43.868
    - type: ndcg_at_20
      value: 45.777
    - type: ndcg_at_100
      value: 48.771
    - type: ndcg_at_1000
      value: 51.001
    - type: map_at_1
      value: 28.177000000000003
    - type: map_at_3
      value: 35.445
    - type: map_at_5
      value: 36.976
    - type: map_at_10
      value: 38.25
    - type: map_at_20
      value: 38.981
    - type: map_at_100
      value: 39.585
    - type: map_at_1000
      value: 39.728
    - type: recall_at_1
      value: 28.177000000000003
    - type: recall_at_3
      value: 41.782000000000004
    - type: recall_at_5
      value: 46.861000000000004
    - type: recall_at_10
      value: 53.464
    - type: recall_at_20
      value: 60.621
    - type: recall_at_100
      value: 74.628
    - type: recall_at_1000
      value: 88.839
    - type: precision_at_1
      value: 35.796
    - type: precision_at_3
      value: 19.639
    - type: precision_at_5
      value: 13.924
    - type: precision_at_10
      value: 8.439
    - type: precision_at_20
      value: 5.016
    - type: precision_at_100
      value: 1.394
    - type: precision_at_1000
      value: 0.189
    - type: mrr_at_1
      value: 35.7962
    - type: mrr_at_3
      value: 42.1019
    - type: mrr_at_5
      value: 43.4172
    - type: mrr_at_10
      value: 44.2407
    - type: mrr_at_20
      value: 44.6907
    - type: mrr_at_100
      value: 45.0075
    - type: mrr_at_1000
      value: 45.059
    - type: nauc_ndcg_at_1_max
      value: 47.856
    - type: nauc_ndcg_at_1_std
      value: 3.0363
    - type: nauc_ndcg_at_1_diff1
      value: 48.7364
    - type: nauc_ndcg_at_3_max
      value: 49.2728
    - type: nauc_ndcg_at_3_std
      value: 4.1776
    - type: nauc_ndcg_at_3_diff1
      value: 45.1449
    - type: nauc_ndcg_at_5_max
      value: 49.5649
    - type: nauc_ndcg_at_5_std
      value: 3.7340999999999998
    - type: nauc_ndcg_at_5_diff1
      value: 44.6651
    - type: nauc_ndcg_at_10_max
      value: 50.1977
    - type: nauc_ndcg_at_10_std
      value: 4.5302
    - type: nauc_ndcg_at_10_diff1
      value: 45.0403
    - type: nauc_ndcg_at_20_max
      value: 49.9326
    - type: nauc_ndcg_at_20_std
      value: 5.5147
    - type: nauc_ndcg_at_20_diff1
      value: 44.5055
    - type: nauc_ndcg_at_100_max
      value: 50.3035
    - type: nauc_ndcg_at_100_std
      value: 7.1086
    - type: nauc_ndcg_at_100_diff1
      value: 44.451
    - type: nauc_ndcg_at_1000_max
      value: 50.1836
    - type: nauc_ndcg_at_1000_std
      value: 7.4503
    - type: nauc_ndcg_at_1000_diff1
      value: 44.301899999999996
    - type: nauc_map_at_1_max
      value: 41.2555
    - type: nauc_map_at_1_std
      value: -5.2668
    - type: nauc_map_at_1_diff1
      value: 52.0284
    - type: nauc_map_at_3_max
      value: 46.6939
    - type: nauc_map_at_3_std
      value: -0.8533000000000001
    - type: nauc_map_at_3_diff1
      value: 47.9095
    - type: nauc_map_at_5_max
      value: 47.5024
    - type: nauc_map_at_5_std
      value: -0.05109999999999999
    - type: nauc_map_at_5_diff1
      value: 47.1421
    - type: nauc_map_at_10_max
      value: 48.1632
    - type: nauc_map_at_10_std
      value: 0.8672
    - type: nauc_map_at_10_diff1
      value: 46.9929
    - type: nauc_map_at_20_max
      value: 48.2708
    - type: nauc_map_at_20_std
      value: 1.5195
    - type: nauc_map_at_20_diff1
      value: 46.7349
    - type: nauc_map_at_100_max
      value: 48.5516
    - type: nauc_map_at_100_std
      value: 2.1593
    - type: nauc_map_at_100_diff1
      value: 46.6641
    - type: nauc_map_at_1000_max
      value: 48.6017
    - type: nauc_map_at_1000_std
      value: 2.2745
    - type: nauc_map_at_1000_diff1
      value: 46.649
    - type: nauc_recall_at_1_max
      value: 41.2555
    - type: nauc_recall_at_1_std
      value: -5.2668
    - type: nauc_recall_at_1_diff1
      value: 52.0284
    - type: nauc_recall_at_3_max
      value: 47.0403
    - type: nauc_recall_at_3_std
      value: 1.5399
    - type: nauc_recall_at_3_diff1
      value: 42.998599999999996
    - type: nauc_recall_at_5_max
      value: 47.7652
    - type: nauc_recall_at_5_std
      value: 2.5079000000000002
    - type: nauc_recall_at_5_diff1
      value: 40.131099999999996
    - type: nauc_recall_at_10_max
      value: 49.215199999999996
    - type: nauc_recall_at_10_std
      value: 5.6207
    - type: nauc_recall_at_10_diff1
      value: 40.0067
    - type: nauc_recall_at_20_max
      value: 47.6907
    - type: nauc_recall_at_20_std
      value: 10.0091
    - type: nauc_recall_at_20_diff1
      value: 36.548
    - type: nauc_recall_at_100_max
      value: 49.8978
    - type: nauc_recall_at_100_std
      value: 20.7533
    - type: nauc_recall_at_100_diff1
      value: 34.463100000000004
    - type: nauc_recall_at_1000_max
      value: 49.2751
    - type: nauc_recall_at_1000_std
      value: 33.7021
    - type: nauc_recall_at_1000_diff1
      value: 27.995199999999997
    - type: nauc_precision_at_1_max
      value: 47.856
    - type: nauc_precision_at_1_std
      value: 3.0363
    - type: nauc_precision_at_1_diff1
      value: 48.7364
    - type: nauc_precision_at_3_max
      value: 48.0591
    - type: nauc_precision_at_3_std
      value: 16.0079
    - type: nauc_precision_at_3_diff1
      value: 28.286099999999998
    - type: nauc_precision_at_5_max
      value: 45.3901
    - type: nauc_precision_at_5_std
      value: 18.939500000000002
    - type: nauc_precision_at_5_diff1
      value: 20.7183
    - type: nauc_precision_at_10_max
      value: 40.2901
    - type: nauc_precision_at_10_std
      value: 24.1368
    - type: nauc_precision_at_10_diff1
      value: 13.1708
    - type: nauc_precision_at_20_max
      value: 34.5736
    - type: nauc_precision_at_20_std
      value: 28.524
    - type: nauc_precision_at_20_diff1
      value: 6.0857
    - type: nauc_precision_at_100_max
      value: 24.0575
    - type: nauc_precision_at_100_std
      value: 32.7048
    - type: nauc_precision_at_100_diff1
      value: -4.175800000000001
    - type: nauc_precision_at_1000_max
      value: 11.3804
    - type: nauc_precision_at_1000_std
      value: 28.917700000000004
    - type: nauc_precision_at_1000_diff1
      value: -11.994100000000001
    - type: nauc_mrr_at_1_max
      value: 47.856
    - type: nauc_mrr_at_1_std
      value: 3.0363
    - type: nauc_mrr_at_1_diff1
      value: 48.7364
    - type: nauc_mrr_at_3_max
      value: 50.048
    - type: nauc_mrr_at_3_std
      value: 6.464300000000001
    - type: nauc_mrr_at_3_diff1
      value: 45.5115
    - type: nauc_mrr_at_5_max
      value: 50.0947
    - type: nauc_mrr_at_5_std
      value: 6.3483
    - type: nauc_mrr_at_5_diff1
      value: 44.8476
    - type: nauc_mrr_at_10_max
      value: 50.244699999999995
    - type: nauc_mrr_at_10_std
      value: 6.666900000000001
    - type: nauc_mrr_at_10_diff1
      value: 45.0222
    - type: nauc_mrr_at_20_max
      value: 50.1332
    - type: nauc_mrr_at_20_std
      value: 6.868200000000001
    - type: nauc_mrr_at_20_diff1
      value: 44.8895
    - type: nauc_mrr_at_100_max
      value: 50.1173
    - type: nauc_mrr_at_100_std
      value: 6.930600000000001
    - type: nauc_mrr_at_100_diff1
      value: 44.8887
    - type: nauc_mrr_at_1000_max
      value: 50.11259999999999
    - type: nauc_mrr_at_1000_std
      value: 6.923799999999999
    - type: nauc_mrr_at_1000_diff1
      value: 44.8928
    - type: main_score
      value: 43.868
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
      value: 43.448
    - type: ndcg_at_3
      value: 51.032999999999994
    - type: ndcg_at_5
      value: 53.73
    - type: ndcg_at_10
      value: 56.369
    - type: ndcg_at_20
      value: 58.167
    - type: ndcg_at_100
      value: 60.28
    - type: ndcg_at_1000
      value: 61.511
    - type: map_at_1
      value: 38.115
    - type: map_at_3
      value: 47.355999999999995
    - type: map_at_5
      value: 49.221
    - type: map_at_10
      value: 50.57000000000001
    - type: map_at_20
      value: 51.2
    - type: map_at_100
      value: 51.568999999999996
    - type: map_at_1000
      value: 51.627
    - type: recall_at_1
      value: 38.115
    - type: recall_at_3
      value: 55.733
    - type: recall_at_5
      value: 62.41100000000001
    - type: recall_at_10
      value: 70.11800000000001
    - type: recall_at_20
      value: 76.714
    - type: recall_at_100
      value: 87.071
    - type: recall_at_1000
      value: 95.921
    - type: precision_at_1
      value: 43.448
    - type: precision_at_3
      value: 22.947
    - type: precision_at_5
      value: 15.799
    - type: precision_at_10
      value: 9.154
    - type: precision_at_20
      value: 5.141
    - type: precision_at_100
      value: 1.196
    - type: precision_at_1000
      value: 0.135
    - type: mrr_at_1
      value: 43.4483
    - type: mrr_at_3
      value: 51.3689
    - type: mrr_at_5
      value: 52.8955
    - type: mrr_at_10
      value: 53.809200000000004
    - type: mrr_at_20
      value: 54.224700000000006
    - type: mrr_at_100
      value: 54.4617
    - type: mrr_at_1000
      value: 54.49079999999999
    - type: nauc_ndcg_at_1_max
      value: 41.9268
    - type: nauc_ndcg_at_1_std
      value: -6.0252
    - type: nauc_ndcg_at_1_diff1
      value: 55.4978
    - type: nauc_ndcg_at_3_max
      value: 43.5492
    - type: nauc_ndcg_at_3_std
      value: -4.7010000000000005
    - type: nauc_ndcg_at_3_diff1
      value: 51.0898
    - type: nauc_ndcg_at_5_max
      value: 44.7544
    - type: nauc_ndcg_at_5_std
      value: -2.9584
    - type: nauc_ndcg_at_5_diff1
      value: 50.6481
    - type: nauc_ndcg_at_10_max
      value: 45.2203
    - type: nauc_ndcg_at_10_std
      value: -1.6934
    - type: nauc_ndcg_at_10_diff1
      value: 49.9874
    - type: nauc_ndcg_at_20_max
      value: 45.002199999999995
    - type: nauc_ndcg_at_20_std
      value: -0.9383
    - type: nauc_ndcg_at_20_diff1
      value: 49.666700000000006
    - type: nauc_ndcg_at_100_max
      value: 45.448699999999995
    - type: nauc_ndcg_at_100_std
      value: -0.1934
    - type: nauc_ndcg_at_100_diff1
      value: 50.0483
    - type: nauc_ndcg_at_1000_max
      value: 45.3335
    - type: nauc_ndcg_at_1000_std
      value: -0.42389999999999994
    - type: nauc_ndcg_at_1000_diff1
      value: 50.5614
    - type: nauc_map_at_1_max
      value: 35.7022
    - type: nauc_map_at_1_std
      value: -6.6763
    - type: nauc_map_at_1_diff1
      value: 54.848699999999994
    - type: nauc_map_at_3_max
      value: 41.5987
    - type: nauc_map_at_3_std
      value: -6.3043000000000005
    - type: nauc_map_at_3_diff1
      value: 52.058400000000006
    - type: nauc_map_at_5_max
      value: 42.5887
    - type: nauc_map_at_5_std
      value: -5.0012
    - type: nauc_map_at_5_diff1
      value: 51.804300000000005
    - type: nauc_map_at_10_max
      value: 43.085
    - type: nauc_map_at_10_std
      value: -4.1721
    - type: nauc_map_at_10_diff1
      value: 51.524499999999996
    - type: nauc_map_at_20_max
      value: 43.185
    - type: nauc_map_at_20_std
      value: -3.6862
    - type: nauc_map_at_20_diff1
      value: 51.4297
    - type: nauc_map_at_100_max
      value: 43.3473
    - type: nauc_map_at_100_std
      value: -3.4286999999999996
    - type: nauc_map_at_100_diff1
      value: 51.497099999999996
    - type: nauc_map_at_1000_max
      value: 43.358799999999995
    - type: nauc_map_at_1000_std
      value: -3.3894
    - type: nauc_map_at_1000_diff1
      value: 51.5155
    - type: nauc_recall_at_1_max
      value: 35.7022
    - type: nauc_recall_at_1_std
      value: -6.6763
    - type: nauc_recall_at_1_diff1
      value: 54.848699999999994
    - type: nauc_recall_at_3_max
      value: 42.9096
    - type: nauc_recall_at_3_std
      value: -5.9907
    - type: nauc_recall_at_3_diff1
      value: 47.407
    - type: nauc_recall_at_5_max
      value: 45.9891
    - type: nauc_recall_at_5_std
      value: -0.5341
    - type: nauc_recall_at_5_diff1
      value: 45.336
    - type: nauc_recall_at_10_max
      value: 47.457899999999995
    - type: nauc_recall_at_10_std
      value: 4.2982
    - type: nauc_recall_at_10_diff1
      value: 41.6
    - type: nauc_recall_at_20_max
      value: 47.3364
    - type: nauc_recall_at_20_std
      value: 9.667100000000001
    - type: nauc_recall_at_20_diff1
      value: 38.4822
    - type: nauc_recall_at_100_max
      value: 52.0554
    - type: nauc_recall_at_100_std
      value: 21.6585
    - type: nauc_recall_at_100_diff1
      value: 35.2361
    - type: nauc_recall_at_1000_max
      value: 62.38590000000001
    - type: nauc_recall_at_1000_std
      value: 42.5442
    - type: nauc_recall_at_1000_diff1
      value: 37.1857
    - type: nauc_precision_at_1_max
      value: 41.9268
    - type: nauc_precision_at_1_std
      value: -6.0252
    - type: nauc_precision_at_1_diff1
      value: 55.4978
    - type: nauc_precision_at_3_max
      value: 44.0934
    - type: nauc_precision_at_3_std
      value: 2.4657
    - type: nauc_precision_at_3_diff1
      value: 33.468399999999995
    - type: nauc_precision_at_5_max
      value: 41.8649
    - type: nauc_precision_at_5_std
      value: 8.4992
    - type: nauc_precision_at_5_diff1
      value: 25.8132
    - type: nauc_precision_at_10_max
      value: 36.8909
    - type: nauc_precision_at_10_std
      value: 15.173200000000001
    - type: nauc_precision_at_10_diff1
      value: 16.0022
    - type: nauc_precision_at_20_max
      value: 31.3774
    - type: nauc_precision_at_20_std
      value: 21.304100000000002
    - type: nauc_precision_at_20_diff1
      value: 7.8406
    - type: nauc_precision_at_100_max
      value: 23.828
    - type: nauc_precision_at_100_std
      value: 27.3387
    - type: nauc_precision_at_100_diff1
      value: -0.5574
    - type: nauc_precision_at_1000_max
      value: 14.3787
    - type: nauc_precision_at_1000_std
      value: 27.8714
    - type: nauc_precision_at_1000_diff1
      value: -6.372400000000001
    - type: nauc_mrr_at_1_max
      value: 41.9268
    - type: nauc_mrr_at_1_std
      value: -6.0252
    - type: nauc_mrr_at_1_diff1
      value: 55.4978
    - type: nauc_mrr_at_3_max
      value: 44.3228
    - type: nauc_mrr_at_3_std
      value: -4.8039
    - type: nauc_mrr_at_3_diff1
      value: 52.6895
    - type: nauc_mrr_at_5_max
      value: 45.0053
    - type: nauc_mrr_at_5_std
      value: -3.5381000000000005
    - type: nauc_mrr_at_5_diff1
      value: 52.321
    - type: nauc_mrr_at_10_max
      value: 44.9242
    - type: nauc_mrr_at_10_std
      value: -3.2841
    - type: nauc_mrr_at_10_diff1
      value: 52.0518
    - type: nauc_mrr_at_20_max
      value: 44.8189
    - type: nauc_mrr_at_20_std
      value: -3.1717000000000004
    - type: nauc_mrr_at_20_diff1
      value: 52.0415
    - type: nauc_mrr_at_100_max
      value: 44.8679
    - type: nauc_mrr_at_100_std
      value: -3.1606
    - type: nauc_mrr_at_100_diff1
      value: 52.1083
    - type: nauc_mrr_at_1000_max
      value: 44.864599999999996
    - type: nauc_mrr_at_1000_std
      value: -3.167
    - type: nauc_mrr_at_1000_diff1
      value: 52.121399999999994
    - type: main_score
      value: 56.369
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
      value: 31.863999999999997
    - type: ndcg_at_3
      value: 38.537
    - type: ndcg_at_5
      value: 41.104
    - type: ndcg_at_10
      value: 43.503
    - type: ndcg_at_20
      value: 45.413
    - type: ndcg_at_100
      value: 48.291000000000004
    - type: ndcg_at_1000
      value: 50.26199999999999
    - type: map_at_1
      value: 29.37
    - type: map_at_3
      value: 35.824
    - type: map_at_5
      value: 37.408
    - type: map_at_10
      value: 38.452999999999996
    - type: map_at_20
      value: 39.004
    - type: map_at_100
      value: 39.421
    - type: map_at_1000
      value: 39.501
    - type: recall_at_1
      value: 29.37
    - type: recall_at_3
      value: 43.442
    - type: recall_at_5
      value: 49.551
    - type: recall_at_10
      value: 56.791000000000004
    - type: recall_at_20
      value: 63.93
    - type: recall_at_100
      value: 78.666
    - type: recall_at_1000
      value: 93.354
    - type: precision_at_1
      value: 31.863999999999997
    - type: precision_at_3
      value: 16.083
    - type: precision_at_5
      value: 11.254
    - type: precision_at_10
      value: 6.508
    - type: precision_at_20
      value: 3.712
    - type: precision_at_100
      value: 0.9390000000000001
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: mrr_at_1
      value: 31.8644
    - type: mrr_at_3
      value: 38.5122
    - type: mrr_at_5
      value: 39.873799999999996
    - type: mrr_at_10
      value: 40.8308
    - type: mrr_at_20
      value: 41.3284
    - type: mrr_at_100
      value: 41.6819
    - type: mrr_at_1000
      value: 41.7416
    - type: nauc_ndcg_at_1_max
      value: 33.7601
    - type: nauc_ndcg_at_1_std
      value: -9.8717
    - type: nauc_ndcg_at_1_diff1
      value: 42.2537
    - type: nauc_ndcg_at_3_max
      value: 34.409600000000005
    - type: nauc_ndcg_at_3_std
      value: -10.6027
    - type: nauc_ndcg_at_3_diff1
      value: 40.0317
    - type: nauc_ndcg_at_5_max
      value: 34.0482
    - type: nauc_ndcg_at_5_std
      value: -9.0778
    - type: nauc_ndcg_at_5_diff1
      value: 39.421499999999995
    - type: nauc_ndcg_at_10_max
      value: 34.5365
    - type: nauc_ndcg_at_10_std
      value: -7.3511999999999995
    - type: nauc_ndcg_at_10_diff1
      value: 38.6886
    - type: nauc_ndcg_at_20_max
      value: 35.335699999999996
    - type: nauc_ndcg_at_20_std
      value: -5.9596
    - type: nauc_ndcg_at_20_diff1
      value: 38.6051
    - type: nauc_ndcg_at_100_max
      value: 34.6961
    - type: nauc_ndcg_at_100_std
      value: -6.5812
    - type: nauc_ndcg_at_100_diff1
      value: 37.8079
    - type: nauc_ndcg_at_1000_max
      value: 34.3938
    - type: nauc_ndcg_at_1000_std
      value: -6.9155
    - type: nauc_ndcg_at_1000_diff1
      value: 38.2247
    - type: nauc_map_at_1_max
      value: 32.231500000000004
    - type: nauc_map_at_1_std
      value: -11.4991
    - type: nauc_map_at_1_diff1
      value: 44.7044
    - type: nauc_map_at_3_max
      value: 34.0411
    - type: nauc_map_at_3_std
      value: -10.8111
    - type: nauc_map_at_3_diff1
      value: 41.6004
    - type: nauc_map_at_5_max
      value: 33.9275
    - type: nauc_map_at_5_std
      value: -9.9881
    - type: nauc_map_at_5_diff1
      value: 41.1704
    - type: nauc_map_at_10_max
      value: 34.1806
    - type: nauc_map_at_10_std
      value: -9.2606
    - type: nauc_map_at_10_diff1
      value: 40.9213
    - type: nauc_map_at_20_max
      value: 34.474
    - type: nauc_map_at_20_std
      value: -8.798599999999999
    - type: nauc_map_at_20_diff1
      value: 40.9088
    - type: nauc_map_at_100_max
      value: 34.381699999999995
    - type: nauc_map_at_100_std
      value: -8.869
    - type: nauc_map_at_100_diff1
      value: 40.7894
    - type: nauc_map_at_1000_max
      value: 34.3718
    - type: nauc_map_at_1000_std
      value: -8.8674
    - type: nauc_map_at_1000_diff1
      value: 40.801700000000004
    - type: nauc_recall_at_1_max
      value: 32.231500000000004
    - type: nauc_recall_at_1_std
      value: -11.4991
    - type: nauc_recall_at_1_diff1
      value: 44.7044
    - type: nauc_recall_at_3_max
      value: 33.4997
    - type: nauc_recall_at_3_std
      value: -10.793999999999999
    - type: nauc_recall_at_3_diff1
      value: 36.8971
    - type: nauc_recall_at_5_max
      value: 33.217600000000004
    - type: nauc_recall_at_5_std
      value: -7.4771
    - type: nauc_recall_at_5_diff1
      value: 35.7378
    - type: nauc_recall_at_10_max
      value: 34.3881
    - type: nauc_recall_at_10_std
      value: -1.9206
    - type: nauc_recall_at_10_diff1
      value: 33.024300000000004
    - type: nauc_recall_at_20_max
      value: 37.1734
    - type: nauc_recall_at_20_std
      value: 4.5757
    - type: nauc_recall_at_20_diff1
      value: 31.7119
    - type: nauc_recall_at_100_max
      value: 33.3328
    - type: nauc_recall_at_100_std
      value: 4.0235
    - type: nauc_recall_at_100_diff1
      value: 23.5836
    - type: nauc_recall_at_1000_max
      value: 23.6203
    - type: nauc_recall_at_1000_std
      value: 10.4212
    - type: nauc_recall_at_1000_diff1
      value: 16.5204
    - type: nauc_precision_at_1_max
      value: 33.7601
    - type: nauc_precision_at_1_std
      value: -9.8717
    - type: nauc_precision_at_1_diff1
      value: 42.2537
    - type: nauc_precision_at_3_max
      value: 37.046099999999996
    - type: nauc_precision_at_3_std
      value: -8.1696
    - type: nauc_precision_at_3_diff1
      value: 32.893699999999995
    - type: nauc_precision_at_5_max
      value: 33.5411
    - type: nauc_precision_at_5_std
      value: -3.8621000000000003
    - type: nauc_precision_at_5_diff1
      value: 28.4192
    - type: nauc_precision_at_10_max
      value: 33.8177
    - type: nauc_precision_at_10_std
      value: 1.4605
    - type: nauc_precision_at_10_diff1
      value: 23.8779
    - type: nauc_precision_at_20_max
      value: 33.2362
    - type: nauc_precision_at_20_std
      value: 6.8675
    - type: nauc_precision_at_20_diff1
      value: 19.12
    - type: nauc_precision_at_100_max
      value: 22.0581
    - type: nauc_precision_at_100_std
      value: 5.6537999999999995
    - type: nauc_precision_at_100_diff1
      value: 2.677
    - type: nauc_precision_at_1000_max
      value: 6.4192
    - type: nauc_precision_at_1000_std
      value: 5.2604999999999995
    - type: nauc_precision_at_1000_diff1
      value: -12.5191
    - type: nauc_mrr_at_1_max
      value: 33.7601
    - type: nauc_mrr_at_1_std
      value: -9.8717
    - type: nauc_mrr_at_1_diff1
      value: 42.2537
    - type: nauc_mrr_at_3_max
      value: 34.590700000000005
    - type: nauc_mrr_at_3_std
      value: -9.3063
    - type: nauc_mrr_at_3_diff1
      value: 39.157599999999995
    - type: nauc_mrr_at_5_max
      value: 34.262
    - type: nauc_mrr_at_5_std
      value: -8.6629
    - type: nauc_mrr_at_5_diff1
      value: 38.7425
    - type: nauc_mrr_at_10_max
      value: 34.3456
    - type: nauc_mrr_at_10_std
      value: -8.0433
    - type: nauc_mrr_at_10_diff1
      value: 38.474199999999996
    - type: nauc_mrr_at_20_max
      value: 34.504400000000004
    - type: nauc_mrr_at_20_std
      value: -7.7764
    - type: nauc_mrr_at_20_diff1
      value: 38.4646
    - type: nauc_mrr_at_100_max
      value: 34.407700000000006
    - type: nauc_mrr_at_100_std
      value: -7.8669
    - type: nauc_mrr_at_100_diff1
      value: 38.4062
    - type: nauc_mrr_at_1000_max
      value: 34.400999999999996
    - type: nauc_mrr_at_1000_std
      value: -7.8653
    - type: nauc_mrr_at_1000_diff1
      value: 38.4264
    - type: main_score
      value: 43.503
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
      value: 22.637
    - type: ndcg_at_3
      value: 26.865
    - type: ndcg_at_5
      value: 29.506
    - type: ndcg_at_10
      value: 32.024
    - type: ndcg_at_20
      value: 34.123999999999995
    - type: ndcg_at_100
      value: 38.013999999999996
    - type: ndcg_at_1000
      value: 40.681
    - type: map_at_1
      value: 18.354
    - type: map_at_3
      value: 23.777
    - type: map_at_5
      value: 25.380000000000003
    - type: map_at_10
      value: 26.588
    - type: map_at_20
      value: 27.227
    - type: map_at_100
      value: 27.851
    - type: map_at_1000
      value: 27.971
    - type: recall_at_1
      value: 18.354
    - type: recall_at_3
      value: 30.029
    - type: recall_at_5
      value: 36.716
    - type: recall_at_10
      value: 44.083
    - type: recall_at_20
      value: 51.653000000000006
    - type: recall_at_100
      value: 70.24000000000001
    - type: recall_at_1000
      value: 88.941
    - type: precision_at_1
      value: 22.637
    - type: precision_at_3
      value: 12.852
    - type: precision_at_5
      value: 9.652
    - type: precision_at_10
      value: 5.970000000000001
    - type: precision_at_20
      value: 3.557
    - type: precision_at_100
      value: 1.035
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: mrr_at_1
      value: 22.6368
    - type: mrr_at_3
      value: 28.296
    - type: mrr_at_5
      value: 30.198999999999998
    - type: mrr_at_10
      value: 31.2411
    - type: mrr_at_20
      value: 31.773600000000002
    - type: mrr_at_100
      value: 32.230199999999996
    - type: mrr_at_1000
      value: 32.2949
    - type: nauc_ndcg_at_1_max
      value: 31.0579
    - type: nauc_ndcg_at_1_std
      value: -1.1154000000000002
    - type: nauc_ndcg_at_1_diff1
      value: 37.0188
    - type: nauc_ndcg_at_3_max
      value: 30.6319
    - type: nauc_ndcg_at_3_std
      value: 1.2079
    - type: nauc_ndcg_at_3_diff1
      value: 29.7055
    - type: nauc_ndcg_at_5_max
      value: 29.2059
    - type: nauc_ndcg_at_5_std
      value: 3.0105
    - type: nauc_ndcg_at_5_diff1
      value: 28.0947
    - type: nauc_ndcg_at_10_max
      value: 29.2307
    - type: nauc_ndcg_at_10_std
      value: 3.1515
    - type: nauc_ndcg_at_10_diff1
      value: 27.2115
    - type: nauc_ndcg_at_20_max
      value: 29.1914
    - type: nauc_ndcg_at_20_std
      value: 3.9833
    - type: nauc_ndcg_at_20_diff1
      value: 27.287899999999997
    - type: nauc_ndcg_at_100_max
      value: 30.759999999999998
    - type: nauc_ndcg_at_100_std
      value: 5.6163
    - type: nauc_ndcg_at_100_diff1
      value: 28.1445
    - type: nauc_ndcg_at_1000_max
      value: 30.4012
    - type: nauc_ndcg_at_1000_std
      value: 4.8586
    - type: nauc_ndcg_at_1000_diff1
      value: 27.7366
    - type: nauc_map_at_1_max
      value: 26.9538
    - type: nauc_map_at_1_std
      value: -0.9815
    - type: nauc_map_at_1_diff1
      value: 35.1964
    - type: nauc_map_at_3_max
      value: 28.9516
    - type: nauc_map_at_3_std
      value: 0.6373
    - type: nauc_map_at_3_diff1
      value: 30.476599999999998
    - type: nauc_map_at_5_max
      value: 28.3735
    - type: nauc_map_at_5_std
      value: 1.5893000000000002
    - type: nauc_map_at_5_diff1
      value: 29.4822
    - type: nauc_map_at_10_max
      value: 28.4489
    - type: nauc_map_at_10_std
      value: 1.7179
    - type: nauc_map_at_10_diff1
      value: 29.0721
    - type: nauc_map_at_20_max
      value: 28.6443
    - type: nauc_map_at_20_std
      value: 1.9567999999999999
    - type: nauc_map_at_20_diff1
      value: 29.2744
    - type: nauc_map_at_100_max
      value: 28.9144
    - type: nauc_map_at_100_std
      value: 2.2790999999999997
    - type: nauc_map_at_100_diff1
      value: 29.3889
    - type: nauc_map_at_1000_max
      value: 28.8827
    - type: nauc_map_at_1000_std
      value: 2.2127999999999997
    - type: nauc_map_at_1000_diff1
      value: 29.367700000000003
    - type: nauc_recall_at_1_max
      value: 26.9538
    - type: nauc_recall_at_1_std
      value: -0.9815
    - type: nauc_recall_at_1_diff1
      value: 35.1964
    - type: nauc_recall_at_3_max
      value: 29.2823
    - type: nauc_recall_at_3_std
      value: 2.2192
    - type: nauc_recall_at_3_diff1
      value: 25.174400000000002
    - type: nauc_recall_at_5_max
      value: 26.098300000000002
    - type: nauc_recall_at_5_std
      value: 5.870100000000001
    - type: nauc_recall_at_5_diff1
      value: 21.5717
    - type: nauc_recall_at_10_max
      value: 26.3965
    - type: nauc_recall_at_10_std
      value: 5.9524
    - type: nauc_recall_at_10_diff1
      value: 19.2576
    - type: nauc_recall_at_20_max
      value: 25.014799999999997
    - type: nauc_recall_at_20_std
      value: 8.889800000000001
    - type: nauc_recall_at_20_diff1
      value: 18.2048
    - type: nauc_recall_at_100_max
      value: 32.664100000000005
    - type: nauc_recall_at_100_std
      value: 20.66
    - type: nauc_recall_at_100_diff1
      value: 20.7167
    - type: nauc_recall_at_1000_max
      value: 32.7425
    - type: nauc_recall_at_1000_std
      value: 31.798
    - type: nauc_recall_at_1000_diff1
      value: 6.1744
    - type: nauc_precision_at_1_max
      value: 31.0579
    - type: nauc_precision_at_1_std
      value: -1.1154000000000002
    - type: nauc_precision_at_1_diff1
      value: 37.0188
    - type: nauc_precision_at_3_max
      value: 34.0041
    - type: nauc_precision_at_3_std
      value: 2.759
    - type: nauc_precision_at_3_diff1
      value: 26.0113
    - type: nauc_precision_at_5_max
      value: 31.591599999999996
    - type: nauc_precision_at_5_std
      value: 7.019499999999999
    - type: nauc_precision_at_5_diff1
      value: 22.5517
    - type: nauc_precision_at_10_max
      value: 28.9779
    - type: nauc_precision_at_10_std
      value: 6.0112
    - type: nauc_precision_at_10_diff1
      value: 18.4627
    - type: nauc_precision_at_20_max
      value: 27.2677
    - type: nauc_precision_at_20_std
      value: 7.9853
    - type: nauc_precision_at_20_diff1
      value: 17.6528
    - type: nauc_precision_at_100_max
      value: 23.8248
    - type: nauc_precision_at_100_std
      value: 9.9215
    - type: nauc_precision_at_100_diff1
      value: 13.5355
    - type: nauc_precision_at_1000_max
      value: 9.9312
    - type: nauc_precision_at_1000_std
      value: 1.8778
    - type: nauc_precision_at_1000_diff1
      value: 3.6692
    - type: nauc_mrr_at_1_max
      value: 31.0579
    - type: nauc_mrr_at_1_std
      value: -1.1154000000000002
    - type: nauc_mrr_at_1_diff1
      value: 37.0188
    - type: nauc_mrr_at_3_max
      value: 32.265100000000004
    - type: nauc_mrr_at_3_std
      value: 0.4738
    - type: nauc_mrr_at_3_diff1
      value: 31.6965
    - type: nauc_mrr_at_5_max
      value: 31.610100000000003
    - type: nauc_mrr_at_5_std
      value: 1.693
    - type: nauc_mrr_at_5_diff1
      value: 31.2068
    - type: nauc_mrr_at_10_max
      value: 31.593500000000002
    - type: nauc_mrr_at_10_std
      value: 1.6910999999999998
    - type: nauc_mrr_at_10_diff1
      value: 30.988300000000002
    - type: nauc_mrr_at_20_max
      value: 31.4229
    - type: nauc_mrr_at_20_std
      value: 1.9178000000000002
    - type: nauc_mrr_at_20_diff1
      value: 30.911
    - type: nauc_mrr_at_100_max
      value: 31.510500000000004
    - type: nauc_mrr_at_100_std
      value: 1.9404000000000001
    - type: nauc_mrr_at_100_diff1
      value: 30.928499999999996
    - type: nauc_mrr_at_1000_max
      value: 31.499899999999997
    - type: nauc_mrr_at_1000_std
      value: 1.9026999999999998
    - type: nauc_mrr_at_1000_diff1
      value: 30.9234
    - type: main_score
      value: 32.024
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
      value: 36.477
    - type: ndcg_at_3
      value: 41.9
    - type: ndcg_at_5
      value: 44.352000000000004
    - type: ndcg_at_10
      value: 47.316
    - type: ndcg_at_20
      value: 49.262
    - type: ndcg_at_100
      value: 52.5
    - type: ndcg_at_1000
      value: 54.433
    - type: map_at_1
      value: 29.633
    - type: map_at_3
      value: 37.374
    - type: map_at_5
      value: 39.327
    - type: map_at_10
      value: 40.897
    - type: map_at_20
      value: 41.629
    - type: map_at_100
      value: 42.221
    - type: map_at_1000
      value: 42.337
    - type: recall_at_1
      value: 29.633
    - type: recall_at_3
      value: 45.141999999999996
    - type: recall_at_5
      value: 51.578
    - type: recall_at_10
      value: 60.465999999999994
    - type: recall_at_20
      value: 67.012
    - type: recall_at_100
      value: 82.174
    - type: recall_at_1000
      value: 94.65
    - type: precision_at_1
      value: 36.477
    - type: precision_at_3
      value: 20.308
    - type: precision_at_5
      value: 14.379
    - type: precision_at_10
      value: 8.816
    - type: precision_at_20
      value: 5.106
    - type: precision_at_100
      value: 1.3419999999999999
    - type: precision_at_1000
      value: 0.169
    - type: mrr_at_1
      value: 36.477399999999996
    - type: mrr_at_3
      value: 44.0648
    - type: mrr_at_5
      value: 45.4604
    - type: mrr_at_10
      value: 46.6132
    - type: mrr_at_20
      value: 47.0122
    - type: mrr_at_100
      value: 47.3432
    - type: mrr_at_1000
      value: 47.383900000000004
    - type: nauc_ndcg_at_1_max
      value: 44.2532
    - type: nauc_ndcg_at_1_std
      value: 0.27399999999999997
    - type: nauc_ndcg_at_1_diff1
      value: 56.0608
    - type: nauc_ndcg_at_3_max
      value: 40.7243
    - type: nauc_ndcg_at_3_std
      value: -3.0545
    - type: nauc_ndcg_at_3_diff1
      value: 48.4101
    - type: nauc_ndcg_at_5_max
      value: 39.556999999999995
    - type: nauc_ndcg_at_5_std
      value: -3.9035
    - type: nauc_ndcg_at_5_diff1
      value: 47.2832
    - type: nauc_ndcg_at_10_max
      value: 39.6116
    - type: nauc_ndcg_at_10_std
      value: -4.2111
    - type: nauc_ndcg_at_10_diff1
      value: 47.0266
    - type: nauc_ndcg_at_20_max
      value: 40.1775
    - type: nauc_ndcg_at_20_std
      value: -2.9367
    - type: nauc_ndcg_at_20_diff1
      value: 47.4448
    - type: nauc_ndcg_at_100_max
      value: 41.9972
    - type: nauc_ndcg_at_100_std
      value: 0.46740000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 48.4355
    - type: nauc_ndcg_at_1000_max
      value: 42.1182
    - type: nauc_ndcg_at_1000_std
      value: 0.8456
    - type: nauc_ndcg_at_1000_diff1
      value: 48.1614
    - type: nauc_map_at_1_max
      value: 37.5422
    - type: nauc_map_at_1_std
      value: -4.2909999999999995
    - type: nauc_map_at_1_diff1
      value: 55.083800000000004
    - type: nauc_map_at_3_max
      value: 39.0107
    - type: nauc_map_at_3_std
      value: -4.3038
    - type: nauc_map_at_3_diff1
      value: 49.5355
    - type: nauc_map_at_5_max
      value: 38.9933
    - type: nauc_map_at_5_std
      value: -4.3489
    - type: nauc_map_at_5_diff1
      value: 48.9543
    - type: nauc_map_at_10_max
      value: 39.2673
    - type: nauc_map_at_10_std
      value: -4.1611
    - type: nauc_map_at_10_diff1
      value: 48.891400000000004
    - type: nauc_map_at_20_max
      value: 39.533699999999996
    - type: nauc_map_at_20_std
      value: -3.7303
    - type: nauc_map_at_20_diff1
      value: 49.001099999999994
    - type: nauc_map_at_100_max
      value: 39.9274
    - type: nauc_map_at_100_std
      value: -3.0797000000000003
    - type: nauc_map_at_100_diff1
      value: 49.1862
    - type: nauc_map_at_1000_max
      value: 39.957100000000004
    - type: nauc_map_at_1000_std
      value: -3.0084
    - type: nauc_map_at_1000_diff1
      value: 49.1595
    - type: nauc_recall_at_1_max
      value: 37.5422
    - type: nauc_recall_at_1_std
      value: -4.2909999999999995
    - type: nauc_recall_at_1_diff1
      value: 55.083800000000004
    - type: nauc_recall_at_3_max
      value: 35.5355
    - type: nauc_recall_at_3_std
      value: -7.140000000000001
    - type: nauc_recall_at_3_diff1
      value: 42.4278
    - type: nauc_recall_at_5_max
      value: 33.9238
    - type: nauc_recall_at_5_std
      value: -7.9919
    - type: nauc_recall_at_5_diff1
      value: 39.1808
    - type: nauc_recall_at_10_max
      value: 33.4493
    - type: nauc_recall_at_10_std
      value: -9.1861
    - type: nauc_recall_at_10_diff1
      value: 36.8475
    - type: nauc_recall_at_20_max
      value: 34.9121
    - type: nauc_recall_at_20_std
      value: -4.8026
    - type: nauc_recall_at_20_diff1
      value: 37.9247
    - type: nauc_recall_at_100_max
      value: 44.1541
    - type: nauc_recall_at_100_std
      value: 18.1134
    - type: nauc_recall_at_100_diff1
      value: 41.6633
    - type: nauc_recall_at_1000_max
      value: 56.3385
    - type: nauc_recall_at_1000_std
      value: 53.257299999999994
    - type: nauc_recall_at_1000_diff1
      value: 36.1232
    - type: nauc_precision_at_1_max
      value: 44.2532
    - type: nauc_precision_at_1_std
      value: 0.27399999999999997
    - type: nauc_precision_at_1_diff1
      value: 56.0608
    - type: nauc_precision_at_3_max
      value: 41.179
    - type: nauc_precision_at_3_std
      value: 5.588
    - type: nauc_precision_at_3_diff1
      value: 32.8574
    - type: nauc_precision_at_5_max
      value: 34.808699999999995
    - type: nauc_precision_at_5_std
      value: 6.261
    - type: nauc_precision_at_5_diff1
      value: 23.993100000000002
    - type: nauc_precision_at_10_max
      value: 30.966500000000003
    - type: nauc_precision_at_10_std
      value: 9.9887
    - type: nauc_precision_at_10_diff1
      value: 16.8352
    - type: nauc_precision_at_20_max
      value: 26.977600000000002
    - type: nauc_precision_at_20_std
      value: 14.0043
    - type: nauc_precision_at_20_diff1
      value: 10.9725
    - type: nauc_precision_at_100_max
      value: 20.0541
    - type: nauc_precision_at_100_std
      value: 24.0399
    - type: nauc_precision_at_100_diff1
      value: -0.46509999999999996
    - type: nauc_precision_at_1000_max
      value: 8.1382
    - type: nauc_precision_at_1000_std
      value: 21.7963
    - type: nauc_precision_at_1000_diff1
      value: -13.7289
    - type: nauc_mrr_at_1_max
      value: 44.2532
    - type: nauc_mrr_at_1_std
      value: 0.27399999999999997
    - type: nauc_mrr_at_1_diff1
      value: 56.0608
    - type: nauc_mrr_at_3_max
      value: 43.0277
    - type: nauc_mrr_at_3_std
      value: -0.8843
    - type: nauc_mrr_at_3_diff1
      value: 51.112899999999996
    - type: nauc_mrr_at_5_max
      value: 42.852000000000004
    - type: nauc_mrr_at_5_std
      value: -0.8572
    - type: nauc_mrr_at_5_diff1
      value: 50.4937
    - type: nauc_mrr_at_10_max
      value: 43.0093
    - type: nauc_mrr_at_10_std
      value: -0.8631
    - type: nauc_mrr_at_10_diff1
      value: 50.41909999999999
    - type: nauc_mrr_at_20_max
      value: 43.0484
    - type: nauc_mrr_at_20_std
      value: -0.6054999999999999
    - type: nauc_mrr_at_20_diff1
      value: 50.527100000000004
    - type: nauc_mrr_at_100_max
      value: 43.175200000000004
    - type: nauc_mrr_at_100_std
      value: -0.3019
    - type: nauc_mrr_at_100_diff1
      value: 50.5962
    - type: nauc_mrr_at_1000_max
      value: 43.173899999999996
    - type: nauc_mrr_at_1000_std
      value: -0.3115
    - type: nauc_mrr_at_1000_diff1
      value: 50.6012
    - type: main_score
      value: 47.316
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
      value: 33.676
    - type: ndcg_at_3
      value: 38.7
    - type: ndcg_at_5
      value: 41.032999999999994
    - type: ndcg_at_10
      value: 43.580999999999996
    - type: ndcg_at_20
      value: 45.992
    - type: ndcg_at_100
      value: 49.192
    - type: ndcg_at_1000
      value: 51.473
    - type: map_at_1
      value: 27.389999999999997
    - type: map_at_3
      value: 34.660999999999994
    - type: map_at_5
      value: 36.38
    - type: map_at_10
      value: 37.768
    - type: map_at_20
      value: 38.534
    - type: map_at_100
      value: 39.091
    - type: map_at_1000
      value: 39.2
    - type: recall_at_1
      value: 27.389999999999997
    - type: recall_at_3
      value: 41.876000000000005
    - type: recall_at_5
      value: 47.961999999999996
    - type: recall_at_10
      value: 55.445
    - type: recall_at_20
      value: 64.143
    - type: recall_at_100
      value: 79.327
    - type: recall_at_1000
      value: 94.64200000000001
    - type: precision_at_1
      value: 33.676
    - type: precision_at_3
      value: 18.455
    - type: precision_at_5
      value: 13.128
    - type: precision_at_10
      value: 7.888000000000001
    - type: precision_at_20
      value: 4.697
    - type: precision_at_100
      value: 1.234
    - type: precision_at_1000
      value: 0.161
    - type: mrr_at_1
      value: 33.6758
    - type: mrr_at_3
      value: 40.7725
    - type: mrr_at_5
      value: 42.267900000000004
    - type: mrr_at_10
      value: 43.1813
    - type: mrr_at_20
      value: 43.769200000000005
    - type: mrr_at_100
      value: 44.0965
    - type: mrr_at_1000
      value: 44.149899999999995
    - type: nauc_ndcg_at_1_max
      value: 47.957699999999996
    - type: nauc_ndcg_at_1_std
      value: 11.211
    - type: nauc_ndcg_at_1_diff1
      value: 50.975899999999996
    - type: nauc_ndcg_at_3_max
      value: 46.7077
    - type: nauc_ndcg_at_3_std
      value: 11.8166
    - type: nauc_ndcg_at_3_diff1
      value: 44.183699999999995
    - type: nauc_ndcg_at_5_max
      value: 46.5691
    - type: nauc_ndcg_at_5_std
      value: 12.3224
    - type: nauc_ndcg_at_5_diff1
      value: 43.2912
    - type: nauc_ndcg_at_10_max
      value: 45.989200000000004
    - type: nauc_ndcg_at_10_std
      value: 13.4501
    - type: nauc_ndcg_at_10_diff1
      value: 41.3206
    - type: nauc_ndcg_at_20_max
      value: 46.400400000000005
    - type: nauc_ndcg_at_20_std
      value: 15.004000000000001
    - type: nauc_ndcg_at_20_diff1
      value: 40.8932
    - type: nauc_ndcg_at_100_max
      value: 47.3346
    - type: nauc_ndcg_at_100_std
      value: 16.5132
    - type: nauc_ndcg_at_100_diff1
      value: 42.126599999999996
    - type: nauc_ndcg_at_1000_max
      value: 47.5217
    - type: nauc_ndcg_at_1000_std
      value: 15.4551
    - type: nauc_ndcg_at_1000_diff1
      value: 42.5563
    - type: nauc_map_at_1_max
      value: 42.549
    - type: nauc_map_at_1_std
      value: 4.9833
    - type: nauc_map_at_1_diff1
      value: 52.14339999999999
    - type: nauc_map_at_3_max
      value: 44.8114
    - type: nauc_map_at_3_std
      value: 9.440800000000001
    - type: nauc_map_at_3_diff1
      value: 46.1197
    - type: nauc_map_at_5_max
      value: 45.3059
    - type: nauc_map_at_5_std
      value: 10.286900000000001
    - type: nauc_map_at_5_diff1
      value: 45.6263
    - type: nauc_map_at_10_max
      value: 45.3517
    - type: nauc_map_at_10_std
      value: 11.1304
    - type: nauc_map_at_10_diff1
      value: 44.6502
    - type: nauc_map_at_20_max
      value: 45.5319
    - type: nauc_map_at_20_std
      value: 11.5773
    - type: nauc_map_at_20_diff1
      value: 44.5681
    - type: nauc_map_at_100_max
      value: 45.8019
    - type: nauc_map_at_100_std
      value: 11.9772
    - type: nauc_map_at_100_diff1
      value: 44.7825
    - type: nauc_map_at_1000_max
      value: 45.8134
    - type: nauc_map_at_1000_std
      value: 11.9461
    - type: nauc_map_at_1000_diff1
      value: 44.7905
    - type: nauc_recall_at_1_max
      value: 42.549
    - type: nauc_recall_at_1_std
      value: 4.9833
    - type: nauc_recall_at_1_diff1
      value: 52.14339999999999
    - type: nauc_recall_at_3_max
      value: 44.0409
    - type: nauc_recall_at_3_std
      value: 11.9146
    - type: nauc_recall_at_3_diff1
      value: 38.6436
    - type: nauc_recall_at_5_max
      value: 43.3961
    - type: nauc_recall_at_5_std
      value: 12.6675
    - type: nauc_recall_at_5_diff1
      value: 35.5553
    - type: nauc_recall_at_10_max
      value: 41.4966
    - type: nauc_recall_at_10_std
      value: 16.1644
    - type: nauc_recall_at_10_diff1
      value: 29.2835
    - type: nauc_recall_at_20_max
      value: 41.474
    - type: nauc_recall_at_20_std
      value: 22.5684
    - type: nauc_recall_at_20_diff1
      value: 25.7308
    - type: nauc_recall_at_100_max
      value: 45.1253
    - type: nauc_recall_at_100_std
      value: 36.248799999999996
    - type: nauc_recall_at_100_diff1
      value: 28.799500000000002
    - type: nauc_recall_at_1000_max
      value: 54.1747
    - type: nauc_recall_at_1000_std
      value: 47.1501
    - type: nauc_recall_at_1000_diff1
      value: 23.198900000000002
    - type: nauc_precision_at_1_max
      value: 47.957699999999996
    - type: nauc_precision_at_1_std
      value: 11.211
    - type: nauc_precision_at_1_diff1
      value: 50.975899999999996
    - type: nauc_precision_at_3_max
      value: 46.6181
    - type: nauc_precision_at_3_std
      value: 19.475
    - type: nauc_precision_at_3_diff1
      value: 30.6784
    - type: nauc_precision_at_5_max
      value: 43.5114
    - type: nauc_precision_at_5_std
      value: 22.1293
    - type: nauc_precision_at_5_diff1
      value: 24.6525
    - type: nauc_precision_at_10_max
      value: 37.47
    - type: nauc_precision_at_10_std
      value: 23.8068
    - type: nauc_precision_at_10_diff1
      value: 14.9368
    - type: nauc_precision_at_20_max
      value: 33.4529
    - type: nauc_precision_at_20_std
      value: 25.4979
    - type: nauc_precision_at_20_diff1
      value: 9.4501
    - type: nauc_precision_at_100_max
      value: 23.7406
    - type: nauc_precision_at_100_std
      value: 22.8583
    - type: nauc_precision_at_100_diff1
      value: 3.6348
    - type: nauc_precision_at_1000_max
      value: 4.5396
    - type: nauc_precision_at_1000_std
      value: 6.0796
    - type: nauc_precision_at_1000_diff1
      value: -7.2498000000000005
    - type: nauc_mrr_at_1_max
      value: 47.957699999999996
    - type: nauc_mrr_at_1_std
      value: 11.211
    - type: nauc_mrr_at_1_diff1
      value: 50.975899999999996
    - type: nauc_mrr_at_3_max
      value: 48.6226
    - type: nauc_mrr_at_3_std
      value: 13.600000000000001
    - type: nauc_mrr_at_3_diff1
      value: 45.2881
    - type: nauc_mrr_at_5_max
      value: 48.402499999999996
    - type: nauc_mrr_at_5_std
      value: 13.616
    - type: nauc_mrr_at_5_diff1
      value: 44.7074
    - type: nauc_mrr_at_10_max
      value: 48.0556
    - type: nauc_mrr_at_10_std
      value: 13.7803
    - type: nauc_mrr_at_10_diff1
      value: 44.0852
    - type: nauc_mrr_at_20_max
      value: 48.173500000000004
    - type: nauc_mrr_at_20_std
      value: 14.1617
    - type: nauc_mrr_at_20_diff1
      value: 44.0396
    - type: nauc_mrr_at_100_max
      value: 48.1841
    - type: nauc_mrr_at_100_std
      value: 14.1827
    - type: nauc_mrr_at_100_diff1
      value: 44.210100000000004
    - type: nauc_mrr_at_1000_max
      value: 48.1875
    - type: nauc_mrr_at_1000_std
      value: 14.161000000000001
    - type: nauc_mrr_at_1000_diff1
      value: 44.222
    - type: main_score
      value: 43.580999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: ndcg_at_1
      value: 32.588499999999996
    - type: ndcg_at_3
      value: 37.949083333333334
    - type: ndcg_at_5
      value: 40.258833333333335
    - type: ndcg_at_10
      value: 42.74341666666667
    - type: ndcg_at_20
      value: 44.784
    - type: ndcg_at_100
      value: 47.903416666666665
    - type: ndcg_at_1000
      value: 50.067416666666674
    - type: map_at_1
      value: 27.52808333333333
    - type: map_at_3
      value: 34.321999999999996
    - type: map_at_5
      value: 35.96091666666666
    - type: map_at_10
      value: 37.22708333333333
    - type: map_at_20
      value: 37.914833333333334
    - type: map_at_100
      value: 38.462166666666675
    - type: map_at_1000
      value: 38.57725
    - type: recall_at_1
      value: 27.52808333333333
    - type: recall_at_3
      value: 41.30075
    - type: recall_at_5
      value: 47.26408333333334
    - type: recall_at_10
      value: 54.663833333333336
    - type: recall_at_20
      value: 62.11658333333333
    - type: recall_at_100
      value: 77.176
    - type: recall_at_1000
      value: 92.03791666666666
    - type: precision_at_1
      value: 32.588499999999996
    - type: precision_at_3
      value: 17.485
    - type: precision_at_5
      value: 12.427666666666669
    - type: precision_at_10
      value: 7.493333333333334
    - type: precision_at_20
      value: 4.413499999999999
    - type: precision_at_100
      value: 1.18675
    - type: precision_at_1000
      value: 0.15691666666666665
    - type: mrr_at_1
      value: 32.58871666666667
    - type: mrr_at_3
      value: 39.09032499999999
    - type: mrr_at_5
      value: 40.533125
    - type: mrr_at_10
      value: 41.51483333333333
    - type: mrr_at_20
      value: 42.01036666666667
    - type: mrr_at_100
      value: 42.35724166666667
    - type: mrr_at_1000
      value: 42.41010833333333
    - type: nauc_ndcg_at_1_max
      value: 41.86760833333334
    - type: nauc_ndcg_at_1_std
      value: -0.022441666666666443
    - type: nauc_ndcg_at_1_diff1
      value: 48.604266666666675
    - type: nauc_ndcg_at_3_max
      value: 40.649825
    - type: nauc_ndcg_at_3_std
      value: 0.9594416666666666
    - type: nauc_ndcg_at_3_diff1
      value: 42.754375
    - type: nauc_ndcg_at_5_max
      value: 40.71646666666666
    - type: nauc_ndcg_at_5_std
      value: 1.8118249999999998
    - type: nauc_ndcg_at_5_diff1
      value: 42.09031666666666
    - type: nauc_ndcg_at_10_max
      value: 40.616033333333334
    - type: nauc_ndcg_at_10_std
      value: 2.621475
    - type: nauc_ndcg_at_10_diff1
      value: 41.56405833333333
    - type: nauc_ndcg_at_20_max
      value: 41.00335
    - type: nauc_ndcg_at_20_std
      value: 3.5835
    - type: nauc_ndcg_at_20_diff1
      value: 41.526025
    - type: nauc_ndcg_at_100_max
      value: 41.626575
    - type: nauc_ndcg_at_100_std
      value: 4.921058333333334
    - type: nauc_ndcg_at_100_diff1
      value: 41.785700000000006
    - type: nauc_ndcg_at_1000_max
      value: 41.623041666666666
    - type: nauc_ndcg_at_1000_std
      value: 4.743416666666667
    - type: nauc_ndcg_at_1000_diff1
      value: 41.930049999999994
    - type: nauc_map_at_1_max
      value: 37.757374999999996
    - type: nauc_map_at_1_std
      value: -2.7256583333333335
    - type: nauc_map_at_1_diff1
      value: 49.68454166666667
    - type: nauc_map_at_3_max
      value: 39.41603333333333
    - type: nauc_map_at_3_std
      value: -0.7485333333333334
    - type: nauc_map_at_3_diff1
      value: 44.64258333333333
    - type: nauc_map_at_5_max
      value: 39.84875833333333
    - type: nauc_map_at_5_std
      value: 0.010733333333333428
    - type: nauc_map_at_5_diff1
      value: 44.133975
    - type: nauc_map_at_10_max
      value: 40.05009166666666
    - type: nauc_map_at_10_std
      value: 0.6503083333333333
    - type: nauc_map_at_10_diff1
      value: 43.826724999999996
    - type: nauc_map_at_20_max
      value: 40.287733333333335
    - type: nauc_map_at_20_std
      value: 1.0432333333333332
    - type: nauc_map_at_20_diff1
      value: 43.784241666666674
    - type: nauc_map_at_100_max
      value: 40.44630833333334
    - type: nauc_map_at_100_std
      value: 1.3809583333333333
    - type: nauc_map_at_100_diff1
      value: 43.81610833333333
    - type: nauc_map_at_1000_max
      value: 40.45624166666667
    - type: nauc_map_at_1000_std
      value: 1.4088416666666665
    - type: nauc_map_at_1000_diff1
      value: 43.81260833333333
    - type: nauc_recall_at_1_max
      value: 37.757374999999996
    - type: nauc_recall_at_1_std
      value: -2.7256583333333335
    - type: nauc_recall_at_1_diff1
      value: 49.68454166666667
    - type: nauc_recall_at_3_max
      value: 37.99286666666667
    - type: nauc_recall_at_3_std
      value: 0.5074666666666666
    - type: nauc_recall_at_3_diff1
      value: 38.458816666666664
    - type: nauc_recall_at_5_max
      value: 38.23744166666667
    - type: nauc_recall_at_5_std
      value: 2.8538000000000006
    - type: nauc_recall_at_5_diff1
      value: 36.16175833333334
    - type: nauc_recall_at_10_max
      value: 37.54170833333333
    - type: nauc_recall_at_10_std
      value: 5.354441666666667
    - type: nauc_recall_at_10_diff1
      value: 33.80731666666667
    - type: nauc_recall_at_20_max
      value: 38.071758333333335
    - type: nauc_recall_at_20_std
      value: 9.4403
    - type: nauc_recall_at_20_diff1
      value: 32.409758333333336
    - type: nauc_recall_at_100_max
      value: 41.127158333333334
    - type: nauc_recall_at_100_std
      value: 20.718875000000004
    - type: nauc_recall_at_100_diff1
      value: 30.971016666666664
    - type: nauc_recall_at_1000_max
      value: 44.978608333333334
    - type: nauc_recall_at_1000_std
      value: 39.36581666666667
    - type: nauc_recall_at_1000_diff1
      value: 27.076241666666668
    - type: nauc_precision_at_1_max
      value: 41.86760833333334
    - type: nauc_precision_at_1_std
      value: -0.022441666666666443
    - type: nauc_precision_at_1_diff1
      value: 48.604266666666675
    - type: nauc_precision_at_3_max
      value: 40.53820000000001
    - type: nauc_precision_at_3_std
      value: 6.682866666666667
    - type: nauc_precision_at_3_diff1
      value: 30.627458333333337
    - type: nauc_precision_at_5_max
      value: 38.085708333333336
    - type: nauc_precision_at_5_std
      value: 10.236816666666666
    - type: nauc_precision_at_5_diff1
      value: 24.589866666666666
    - type: nauc_precision_at_10_max
      value: 33.795766666666665
    - type: nauc_precision_at_10_std
      value: 13.644358333333335
    - type: nauc_precision_at_10_diff1
      value: 17.663875
    - type: nauc_precision_at_20_max
      value: 30.67170833333333
    - type: nauc_precision_at_20_std
      value: 16.899591666666666
    - type: nauc_precision_at_20_diff1
      value: 12.398666666666665
    - type: nauc_precision_at_100_max
      value: 21.46699166666666
    - type: nauc_precision_at_100_std
      value: 19.683266666666665
    - type: nauc_precision_at_100_diff1
      value: 2.3721666666666668
    - type: nauc_precision_at_1000_max
      value: 6.773875
    - type: nauc_precision_at_1000_std
      value: 13.712933333333336
    - type: nauc_precision_at_1000_diff1
      value: -9.302758333333333
    - type: nauc_mrr_at_1_max
      value: 41.86760833333334
    - type: nauc_mrr_at_1_std
      value: -0.022441666666666443
    - type: nauc_mrr_at_1_diff1
      value: 48.604266666666675
    - type: nauc_mrr_at_3_max
      value: 42.065525
    - type: nauc_mrr_at_3_std
      value: 1.6751166666666664
    - type: nauc_mrr_at_3_diff1
      value: 43.90220833333333
    - type: nauc_mrr_at_5_max
      value: 42.07275833333333
    - type: nauc_mrr_at_5_std
      value: 2.3014749999999995
    - type: nauc_mrr_at_5_diff1
      value: 43.440275
    - type: nauc_mrr_at_10_max
      value: 41.955425000000005
    - type: nauc_mrr_at_10_std
      value: 2.499491666666667
    - type: nauc_mrr_at_10_diff1
      value: 43.23685833333333
    - type: nauc_mrr_at_20_max
      value: 41.98479166666666
    - type: nauc_mrr_at_20_std
      value: 2.6983083333333333
    - type: nauc_mrr_at_20_diff1
      value: 43.24806666666667
    - type: nauc_mrr_at_100_max
      value: 42.01090833333334
    - type: nauc_mrr_at_100_std
      value: 2.7583083333333334
    - type: nauc_mrr_at_100_diff1
      value: 43.28899166666667
    - type: nauc_mrr_at_1000_max
      value: 42.010841666666664
    - type: nauc_mrr_at_1000_std
      value: 2.750433333333333
    - type: nauc_mrr_at_1000_diff1
      value: 43.299625
    - type: main_score
      value: 42.74341666666667
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
      value: 42.743416666666675
    - type: ndcg_at_10
      value: 42.743416666666675
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
      value: 27.607
    - type: ndcg_at_3
      value: 32.665
    - type: ndcg_at_5
      value: 34.876000000000005
    - type: ndcg_at_10
      value: 36.796
    - type: ndcg_at_20
      value: 38.405
    - type: ndcg_at_100
      value: 41.612
    - type: ndcg_at_1000
      value: 43.869
    - type: map_at_1
      value: 24.748
    - type: map_at_3
      value: 30.192999999999998
    - type: map_at_5
      value: 31.563999999999997
    - type: map_at_10
      value: 32.424
    - type: map_at_20
      value: 32.905
    - type: map_at_100
      value: 33.385
    - type: map_at_1000
      value: 33.476
    - type: recall_at_1
      value: 24.748
    - type: recall_at_3
      value: 36.14
    - type: recall_at_5
      value: 41.617
    - type: recall_at_10
      value: 47.49
    - type: recall_at_20
      value: 53.413
    - type: recall_at_100
      value: 69.461
    - type: recall_at_1000
      value: 86.014
    - type: precision_at_1
      value: 27.607
    - type: precision_at_3
      value: 13.957
    - type: precision_at_5
      value: 9.847
    - type: precision_at_10
      value: 5.782
    - type: precision_at_20
      value: 3.3360000000000003
    - type: precision_at_100
      value: 0.906
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: mrr_at_1
      value: 27.6074
    - type: mrr_at_3
      value: 32.9499
    - type: mrr_at_5
      value: 34.2229
    - type: mrr_at_10
      value: 35.0668
    - type: mrr_at_20
      value: 35.4859
    - type: mrr_at_100
      value: 35.8948
    - type: mrr_at_1000
      value: 35.9562
    - type: nauc_ndcg_at_1_max
      value: 49.1944
    - type: nauc_ndcg_at_1_std
      value: 11.7093
    - type: nauc_ndcg_at_1_diff1
      value: 56.8806
    - type: nauc_ndcg_at_3_max
      value: 46.7361
    - type: nauc_ndcg_at_3_std
      value: 13.4354
    - type: nauc_ndcg_at_3_diff1
      value: 49.7927
    - type: nauc_ndcg_at_5_max
      value: 47.280899999999995
    - type: nauc_ndcg_at_5_std
      value: 14.5061
    - type: nauc_ndcg_at_5_diff1
      value: 48.9168
    - type: nauc_ndcg_at_10_max
      value: 47.5137
    - type: nauc_ndcg_at_10_std
      value: 15.4698
    - type: nauc_ndcg_at_10_diff1
      value: 48.4279
    - type: nauc_ndcg_at_20_max
      value: 47.9904
    - type: nauc_ndcg_at_20_std
      value: 15.7135
    - type: nauc_ndcg_at_20_diff1
      value: 48.4332
    - type: nauc_ndcg_at_100_max
      value: 48.2942
    - type: nauc_ndcg_at_100_std
      value: 17.502100000000002
    - type: nauc_ndcg_at_100_diff1
      value: 48.6035
    - type: nauc_ndcg_at_1000_max
      value: 48.0957
    - type: nauc_ndcg_at_1000_std
      value: 17.6368
    - type: nauc_ndcg_at_1000_diff1
      value: 48.7597
    - type: nauc_map_at_1_max
      value: 45.6445
    - type: nauc_map_at_1_std
      value: 6.9397
    - type: nauc_map_at_1_diff1
      value: 58.6992
    - type: nauc_map_at_3_max
      value: 45.8449
    - type: nauc_map_at_3_std
      value: 11.036200000000001
    - type: nauc_map_at_3_diff1
      value: 51.906
    - type: nauc_map_at_5_max
      value: 46.3198
    - type: nauc_map_at_5_std
      value: 11.921
    - type: nauc_map_at_5_diff1
      value: 51.2763
    - type: nauc_map_at_10_max
      value: 46.5425
    - type: nauc_map_at_10_std
      value: 12.5743
    - type: nauc_map_at_10_diff1
      value: 50.9536
    - type: nauc_map_at_20_max
      value: 46.726
    - type: nauc_map_at_20_std
      value: 12.6497
    - type: nauc_map_at_20_diff1
      value: 50.99510000000001
    - type: nauc_map_at_100_max
      value: 46.7746
    - type: nauc_map_at_100_std
      value: 12.881200000000002
    - type: nauc_map_at_100_diff1
      value: 51.011399999999995
    - type: nauc_map_at_1000_max
      value: 46.785900000000005
    - type: nauc_map_at_1000_std
      value: 12.898000000000001
    - type: nauc_map_at_1000_diff1
      value: 51.01480000000001
    - type: nauc_recall_at_1_max
      value: 45.6445
    - type: nauc_recall_at_1_std
      value: 6.9397
    - type: nauc_recall_at_1_diff1
      value: 58.6992
    - type: nauc_recall_at_3_max
      value: 45.0182
    - type: nauc_recall_at_3_std
      value: 14.2648
    - type: nauc_recall_at_3_diff1
      value: 45.3428
    - type: nauc_recall_at_5_max
      value: 46.2258
    - type: nauc_recall_at_5_std
      value: 17.2103
    - type: nauc_recall_at_5_diff1
      value: 42.5614
    - type: nauc_recall_at_10_max
      value: 46.251799999999996
    - type: nauc_recall_at_10_std
      value: 19.8669
    - type: nauc_recall_at_10_diff1
      value: 40.415
    - type: nauc_recall_at_20_max
      value: 46.7318
    - type: nauc_recall_at_20_std
      value: 20.3996
    - type: nauc_recall_at_20_diff1
      value: 39.0112
    - type: nauc_recall_at_100_max
      value: 48.3756
    - type: nauc_recall_at_100_std
      value: 33.558
    - type: nauc_recall_at_100_diff1
      value: 37.584
    - type: nauc_recall_at_1000_max
      value: 46.1278
    - type: nauc_recall_at_1000_std
      value: 50.2506
    - type: nauc_recall_at_1000_diff1
      value: 33.7694
    - type: nauc_precision_at_1_max
      value: 49.1944
    - type: nauc_precision_at_1_std
      value: 11.7093
    - type: nauc_precision_at_1_diff1
      value: 56.8806
    - type: nauc_precision_at_3_max
      value: 49.9406
    - type: nauc_precision_at_3_std
      value: 22.883200000000002
    - type: nauc_precision_at_3_diff1
      value: 40.5974
    - type: nauc_precision_at_5_max
      value: 48.4187
    - type: nauc_precision_at_5_std
      value: 25.9129
    - type: nauc_precision_at_5_diff1
      value: 34.863
    - type: nauc_precision_at_10_max
      value: 46.734700000000004
    - type: nauc_precision_at_10_std
      value: 28.5765
    - type: nauc_precision_at_10_diff1
      value: 30.071599999999997
    - type: nauc_precision_at_20_max
      value: 45.2343
    - type: nauc_precision_at_20_std
      value: 27.4324
    - type: nauc_precision_at_20_diff1
      value: 26.888299999999997
    - type: nauc_precision_at_100_max
      value: 33.7511
    - type: nauc_precision_at_100_std
      value: 30.084300000000002
    - type: nauc_precision_at_100_diff1
      value: 14.877099999999999
    - type: nauc_precision_at_1000_max
      value: 15.059000000000001
    - type: nauc_precision_at_1000_std
      value: 21.4471
    - type: nauc_precision_at_1000_diff1
      value: -1.2862
    - type: nauc_mrr_at_1_max
      value: 49.1944
    - type: nauc_mrr_at_1_std
      value: 11.7093
    - type: nauc_mrr_at_1_diff1
      value: 56.8806
    - type: nauc_mrr_at_3_max
      value: 48.8173
    - type: nauc_mrr_at_3_std
      value: 14.7023
    - type: nauc_mrr_at_3_diff1
      value: 50.9845
    - type: nauc_mrr_at_5_max
      value: 49.0933
    - type: nauc_mrr_at_5_std
      value: 15.5443
    - type: nauc_mrr_at_5_diff1
      value: 50.403299999999994
    - type: nauc_mrr_at_10_max
      value: 49.058
    - type: nauc_mrr_at_10_std
      value: 15.6592
    - type: nauc_mrr_at_10_diff1
      value: 50.3304
    - type: nauc_mrr_at_20_max
      value: 49.104
    - type: nauc_mrr_at_20_std
      value: 15.7446
    - type: nauc_mrr_at_20_diff1
      value: 50.2689
    - type: nauc_mrr_at_100_max
      value: 49.071999999999996
    - type: nauc_mrr_at_100_std
      value: 15.8584
    - type: nauc_mrr_at_100_diff1
      value: 50.3045
    - type: nauc_mrr_at_1000_max
      value: 49.061
    - type: nauc_mrr_at_1000_std
      value: 15.856700000000002
    - type: nauc_mrr_at_1000_diff1
      value: 50.3081
    - type: main_score
      value: 36.796
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
      value: 23.159
    - type: ndcg_at_3
      value: 27.401999999999997
    - type: ndcg_at_5
      value: 29.354000000000003
    - type: ndcg_at_10
      value: 31.775
    - type: ndcg_at_20
      value: 33.743
    - type: ndcg_at_100
      value: 37.125
    - type: ndcg_at_1000
      value: 39.956
    - type: map_at_1
      value: 18.997
    - type: map_at_3
      value: 24.351
    - type: map_at_5
      value: 25.724999999999998
    - type: map_at_10
      value: 26.873
    - type: map_at_20
      value: 27.479
    - type: map_at_100
      value: 28.008
    - type: map_at_1000
      value: 28.133999999999997
    - type: recall_at_1
      value: 18.997
    - type: recall_at_3
      value: 30.14
    - type: recall_at_5
      value: 35.225
    - type: recall_at_10
      value: 42.447
    - type: recall_at_20
      value: 49.769000000000005
    - type: recall_at_100
      value: 66.39500000000001
    - type: recall_at_1000
      value: 86.434
    - type: precision_at_1
      value: 23.159
    - type: precision_at_3
      value: 12.995999999999999
    - type: precision_at_5
      value: 9.381
    - type: precision_at_10
      value: 5.778
    - type: precision_at_20
      value: 3.467
    - type: precision_at_100
      value: 0.9900000000000001
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: mrr_at_1
      value: 23.159
    - type: mrr_at_3
      value: 28.676299999999998
    - type: mrr_at_5
      value: 29.9082
    - type: mrr_at_10
      value: 30.9286
    - type: mrr_at_20
      value: 31.4303
    - type: mrr_at_100
      value: 31.845000000000002
    - type: mrr_at_1000
      value: 31.9176
    - type: nauc_ndcg_at_1_max
      value: 32.959500000000006
    - type: nauc_ndcg_at_1_std
      value: -2.0082
    - type: nauc_ndcg_at_1_diff1
      value: 41.801500000000004
    - type: nauc_ndcg_at_3_max
      value: 32.8362
    - type: nauc_ndcg_at_3_std
      value: -0.9611
    - type: nauc_ndcg_at_3_diff1
      value: 36.248200000000004
    - type: nauc_ndcg_at_5_max
      value: 32.650800000000004
    - type: nauc_ndcg_at_5_std
      value: 0.13879999999999998
    - type: nauc_ndcg_at_5_diff1
      value: 35.2211
    - type: nauc_ndcg_at_10_max
      value: 32.6256
    - type: nauc_ndcg_at_10_std
      value: 1.0654000000000001
    - type: nauc_ndcg_at_10_diff1
      value: 34.6558
    - type: nauc_ndcg_at_20_max
      value: 33.0706
    - type: nauc_ndcg_at_20_std
      value: 2.2485
    - type: nauc_ndcg_at_20_diff1
      value: 34.5314
    - type: nauc_ndcg_at_100_max
      value: 33.3131
    - type: nauc_ndcg_at_100_std
      value: 3.4467
    - type: nauc_ndcg_at_100_diff1
      value: 34.4791
    - type: nauc_ndcg_at_1000_max
      value: 33.644400000000005
    - type: nauc_ndcg_at_1000_std
      value: 3.6159999999999997
    - type: nauc_ndcg_at_1000_diff1
      value: 34.9717
    - type: nauc_map_at_1_max
      value: 30.2696
    - type: nauc_map_at_1_std
      value: -3.3264
    - type: nauc_map_at_1_diff1
      value: 42.0066
    - type: nauc_map_at_3_max
      value: 31.455899999999996
    - type: nauc_map_at_3_std
      value: -1.8429999999999997
    - type: nauc_map_at_3_diff1
      value: 37.4893
    - type: nauc_map_at_5_max
      value: 31.7755
    - type: nauc_map_at_5_std
      value: -1.1461999999999999
    - type: nauc_map_at_5_diff1
      value: 36.8624
    - type: nauc_map_at_10_max
      value: 31.9842
    - type: nauc_map_at_10_std
      value: -0.6542
    - type: nauc_map_at_10_diff1
      value: 36.5911
    - type: nauc_map_at_20_max
      value: 32.1745
    - type: nauc_map_at_20_std
      value: -0.2191
    - type: nauc_map_at_20_diff1
      value: 36.552800000000005
    - type: nauc_map_at_100_max
      value: 32.3001
    - type: nauc_map_at_100_std
      value: 0.012199999999999999
    - type: nauc_map_at_100_diff1
      value: 36.5376
    - type: nauc_map_at_1000_max
      value: 32.3571
    - type: nauc_map_at_1000_std
      value: 0.0557
    - type: nauc_map_at_1000_diff1
      value: 36.5535
    - type: nauc_recall_at_1_max
      value: 30.2696
    - type: nauc_recall_at_1_std
      value: -3.3264
    - type: nauc_recall_at_1_diff1
      value: 42.0066
    - type: nauc_recall_at_3_max
      value: 30.413600000000002
    - type: nauc_recall_at_3_std
      value: -0.44530000000000003
    - type: nauc_recall_at_3_diff1
      value: 32.3805
    - type: nauc_recall_at_5_max
      value: 30.075499999999998
    - type: nauc_recall_at_5_std
      value: 1.8853000000000002
    - type: nauc_recall_at_5_diff1
      value: 29.8885
    - type: nauc_recall_at_10_max
      value: 29.7039
    - type: nauc_recall_at_10_std
      value: 4.1936
    - type: nauc_recall_at_10_diff1
      value: 27.9912
    - type: nauc_recall_at_20_max
      value: 30.538700000000002
    - type: nauc_recall_at_20_std
      value: 7.8352
    - type: nauc_recall_at_20_diff1
      value: 26.842
    - type: nauc_recall_at_100_max
      value: 30.8116
    - type: nauc_recall_at_100_std
      value: 15.1426
    - type: nauc_recall_at_100_diff1
      value: 23.9166
    - type: nauc_recall_at_1000_max
      value: 31.9647
    - type: nauc_recall_at_1000_std
      value: 26.5754
    - type: nauc_recall_at_1000_diff1
      value: 22.608
    - type: nauc_precision_at_1_max
      value: 32.959500000000006
    - type: nauc_precision_at_1_std
      value: -2.0082
    - type: nauc_precision_at_1_diff1
      value: 41.801500000000004
    - type: nauc_precision_at_3_max
      value: 34.8709
    - type: nauc_precision_at_3_std
      value: 1.5288
    - type: nauc_precision_at_3_diff1
      value: 30.6782
    - type: nauc_precision_at_5_max
      value: 34.163700000000006
    - type: nauc_precision_at_5_std
      value: 4.3446
    - type: nauc_precision_at_5_diff1
      value: 26.2964
    - type: nauc_precision_at_10_max
      value: 33.1747
    - type: nauc_precision_at_10_std
      value: 7.2109000000000005
    - type: nauc_precision_at_10_diff1
      value: 22.6126
    - type: nauc_precision_at_20_max
      value: 32.8185
    - type: nauc_precision_at_20_std
      value: 11.296100000000001
    - type: nauc_precision_at_20_diff1
      value: 19.4086
    - type: nauc_precision_at_100_max
      value: 30.4363
    - type: nauc_precision_at_100_std
      value: 14.23
    - type: nauc_precision_at_100_diff1
      value: 13.1689
    - type: nauc_precision_at_1000_max
      value: 24.6263
    - type: nauc_precision_at_1000_std
      value: 11.190999999999999
    - type: nauc_precision_at_1000_diff1
      value: 4.5375
    - type: nauc_mrr_at_1_max
      value: 32.959500000000006
    - type: nauc_mrr_at_1_std
      value: -2.0082
    - type: nauc_mrr_at_1_diff1
      value: 41.801500000000004
    - type: nauc_mrr_at_3_max
      value: 33.949400000000004
    - type: nauc_mrr_at_3_std
      value: -0.5342
    - type: nauc_mrr_at_3_diff1
      value: 37.3148
    - type: nauc_mrr_at_5_max
      value: 33.7685
    - type: nauc_mrr_at_5_std
      value: 0.2542
    - type: nauc_mrr_at_5_diff1
      value: 36.5632
    - type: nauc_mrr_at_10_max
      value: 33.849000000000004
    - type: nauc_mrr_at_10_std
      value: 0.6677
    - type: nauc_mrr_at_10_diff1
      value: 36.4741
    - type: nauc_mrr_at_20_max
      value: 33.9586
    - type: nauc_mrr_at_20_std
      value: 0.897
    - type: nauc_mrr_at_20_diff1
      value: 36.478899999999996
    - type: nauc_mrr_at_100_max
      value: 33.9441
    - type: nauc_mrr_at_100_std
      value: 0.9808000000000001
    - type: nauc_mrr_at_100_diff1
      value: 36.5049
    - type: nauc_mrr_at_1000_max
      value: 33.9546
    - type: nauc_mrr_at_1000_std
      value: 0.9831
    - type: nauc_mrr_at_1000_diff1
      value: 36.5259
    - type: main_score
      value: 31.775
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
      value: 34.981
    - type: ndcg_at_3
      value: 40.107
    - type: ndcg_at_5
      value: 42.842999999999996
    - type: ndcg_at_10
      value: 45.275
    - type: ndcg_at_20
      value: 47.455999999999996
    - type: ndcg_at_100
      value: 50.321000000000005
    - type: ndcg_at_1000
      value: 52.406
    - type: map_at_1
      value: 29.504
    - type: map_at_3
      value: 36.622
    - type: map_at_5
      value: 38.541
    - type: map_at_10
      value: 39.675
    - type: map_at_20
      value: 40.409
    - type: map_at_100
      value: 40.914
    - type: map_at_1000
      value: 41.012
    - type: recall_at_1
      value: 29.504
    - type: recall_at_3
      value: 43.807
    - type: recall_at_5
      value: 50.77700000000001
    - type: recall_at_10
      value: 57.898
    - type: recall_at_20
      value: 65.59899999999999
    - type: recall_at_100
      value: 78.974
    - type: recall_at_1000
      value: 93.33399999999999
    - type: precision_at_1
      value: 34.981
    - type: precision_at_3
      value: 18.315
    - type: precision_at_5
      value: 13.097
    - type: precision_at_10
      value: 7.631
    - type: precision_at_20
      value: 4.431
    - type: precision_at_100
      value: 1.13
    - type: precision_at_1000
      value: 0.14100000000000001
    - type: mrr_at_1
      value: 34.9813
    - type: mrr_at_3
      value: 41.3557
    - type: mrr_at_5
      value: 42.9602
    - type: mrr_at_10
      value: 43.9816
    - type: mrr_at_20
      value: 44.5
    - type: mrr_at_100
      value: 44.8076
    - type: mrr_at_1000
      value: 44.865
    - type: nauc_ndcg_at_1_max
      value: 48.6102
    - type: nauc_ndcg_at_1_std
      value: -5.6691
    - type: nauc_ndcg_at_1_diff1
      value: 56.008599999999994
    - type: nauc_ndcg_at_3_max
      value: 46.388400000000004
    - type: nauc_ndcg_at_3_std
      value: -4.877800000000001
    - type: nauc_ndcg_at_3_diff1
      value: 49.1768
    - type: nauc_ndcg_at_5_max
      value: 46.3438
    - type: nauc_ndcg_at_5_std
      value: -4.1069
    - type: nauc_ndcg_at_5_diff1
      value: 48.209999999999994
    - type: nauc_ndcg_at_10_max
      value: 46.147
    - type: nauc_ndcg_at_10_std
      value: -3.7115
    - type: nauc_ndcg_at_10_diff1
      value: 47.9846
    - type: nauc_ndcg_at_20_max
      value: 46.2731
    - type: nauc_ndcg_at_20_std
      value: -3.5068
    - type: nauc_ndcg_at_20_diff1
      value: 48.1901
    - type: nauc_ndcg_at_100_max
      value: 46.886
    - type: nauc_ndcg_at_100_std
      value: -1.8507
    - type: nauc_ndcg_at_100_diff1
      value: 49.058
    - type: nauc_ndcg_at_1000_max
      value: 46.5984
    - type: nauc_ndcg_at_1000_std
      value: -2.1614999999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 49.1318
    - type: nauc_map_at_1_max
      value: 45.5569
    - type: nauc_map_at_1_std
      value: -7.604900000000001
    - type: nauc_map_at_1_diff1
      value: 56.3936
    - type: nauc_map_at_3_max
      value: 46.0028
    - type: nauc_map_at_3_std
      value: -6.334
    - type: nauc_map_at_3_diff1
      value: 51.3472
    - type: nauc_map_at_5_max
      value: 46.2903
    - type: nauc_map_at_5_std
      value: -5.475300000000001
    - type: nauc_map_at_5_diff1
      value: 50.5945
    - type: nauc_map_at_10_max
      value: 46.3277
    - type: nauc_map_at_10_std
      value: -5.1829
    - type: nauc_map_at_10_diff1
      value: 50.4714
    - type: nauc_map_at_20_max
      value: 46.5326
    - type: nauc_map_at_20_std
      value: -5.0456
    - type: nauc_map_at_20_diff1
      value: 50.5729
    - type: nauc_map_at_100_max
      value: 46.6537
    - type: nauc_map_at_100_std
      value: -4.7367
    - type: nauc_map_at_100_diff1
      value: 50.711
    - type: nauc_map_at_1000_max
      value: 46.6406
    - type: nauc_map_at_1000_std
      value: -4.7269
    - type: nauc_map_at_1000_diff1
      value: 50.6985
    - type: nauc_recall_at_1_max
      value: 45.5569
    - type: nauc_recall_at_1_std
      value: -7.604900000000001
    - type: nauc_recall_at_1_diff1
      value: 56.3936
    - type: nauc_recall_at_3_max
      value: 43.1624
    - type: nauc_recall_at_3_std
      value: -5.0664
    - type: nauc_recall_at_3_diff1
      value: 44.016
    - type: nauc_recall_at_5_max
      value: 42.893
    - type: nauc_recall_at_5_std
      value: -2.0581
    - type: nauc_recall_at_5_diff1
      value: 40.6813
    - type: nauc_recall_at_10_max
      value: 41.3464
    - type: nauc_recall_at_10_std
      value: -0.9026
    - type: nauc_recall_at_10_diff1
      value: 38.8716
    - type: nauc_recall_at_20_max
      value: 40.7766
    - type: nauc_recall_at_20_std
      value: -0.4664
    - type: nauc_recall_at_20_diff1
      value: 38.6801
    - type: nauc_recall_at_100_max
      value: 43.856
    - type: nauc_recall_at_100_std
      value: 12.148200000000001
    - type: nauc_recall_at_100_diff1
      value: 43.189899999999994
    - type: nauc_recall_at_1000_max
      value: 36.6555
    - type: nauc_recall_at_1000_std
      value: 25.7409
    - type: nauc_recall_at_1000_diff1
      value: 44.9133
    - type: nauc_precision_at_1_max
      value: 48.6102
    - type: nauc_precision_at_1_std
      value: -5.6691
    - type: nauc_precision_at_1_diff1
      value: 56.008599999999994
    - type: nauc_precision_at_3_max
      value: 43.2148
    - type: nauc_precision_at_3_std
      value: 0.0292
    - type: nauc_precision_at_3_diff1
      value: 35.75
    - type: nauc_precision_at_5_max
      value: 39.8562
    - type: nauc_precision_at_5_std
      value: 4.105
    - type: nauc_precision_at_5_diff1
      value: 28.4213
    - type: nauc_precision_at_10_max
      value: 34.901199999999996
    - type: nauc_precision_at_10_std
      value: 6.4718
    - type: nauc_precision_at_10_diff1
      value: 22.785
    - type: nauc_precision_at_20_max
      value: 29.151
    - type: nauc_precision_at_20_std
      value: 8.213
    - type: nauc_precision_at_20_diff1
      value: 16.6992
    - type: nauc_precision_at_100_max
      value: 17.1377
    - type: nauc_precision_at_100_std
      value: 16.1652
    - type: nauc_precision_at_100_diff1
      value: 4.4657
    - type: nauc_precision_at_1000_max
      value: -2.6889
    - type: nauc_precision_at_1000_std
      value: 11.010499999999999
    - type: nauc_precision_at_1000_diff1
      value: -11.0026
    - type: nauc_mrr_at_1_max
      value: 48.6102
    - type: nauc_mrr_at_1_std
      value: -5.6691
    - type: nauc_mrr_at_1_diff1
      value: 56.008599999999994
    - type: nauc_mrr_at_3_max
      value: 47.6571
    - type: nauc_mrr_at_3_std
      value: -4.1072999999999995
    - type: nauc_mrr_at_3_diff1
      value: 50.18470000000001
    - type: nauc_mrr_at_5_max
      value: 47.6268
    - type: nauc_mrr_at_5_std
      value: -3.6222
    - type: nauc_mrr_at_5_diff1
      value: 49.5854
    - type: nauc_mrr_at_10_max
      value: 47.454499999999996
    - type: nauc_mrr_at_10_std
      value: -3.4977
    - type: nauc_mrr_at_10_diff1
      value: 49.5833
    - type: nauc_mrr_at_20_max
      value: 47.3316
    - type: nauc_mrr_at_20_std
      value: -3.5721000000000003
    - type: nauc_mrr_at_20_diff1
      value: 49.6713
    - type: nauc_mrr_at_100_max
      value: 47.387299999999996
    - type: nauc_mrr_at_100_std
      value: -3.4835
    - type: nauc_mrr_at_100_diff1
      value: 49.8135
    - type: nauc_mrr_at_1000_max
      value: 47.4002
    - type: nauc_mrr_at_1000_std
      value: -3.4842999999999997
    - type: nauc_mrr_at_1000_diff1
      value: 49.8286
    - type: main_score
      value: 45.275
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
      value: 32.806000000000004
    - type: ndcg_at_3
      value: 38.775999999999996
    - type: ndcg_at_5
      value: 40.614
    - type: ndcg_at_10
      value: 42.957
    - type: ndcg_at_20
      value: 45.202999999999996
    - type: ndcg_at_100
      value: 48.941
    - type: ndcg_at_1000
      value: 51.105000000000004
    - type: map_at_1
      value: 27.236
    - type: map_at_3
      value: 34.204
    - type: map_at_5
      value: 35.66
    - type: map_at_10
      value: 36.986000000000004
    - type: map_at_20
      value: 37.827
    - type: map_at_100
      value: 38.602
    - type: map_at_1000
      value: 38.818000000000005
    - type: recall_at_1
      value: 27.236
    - type: recall_at_3
      value: 41.596
    - type: recall_at_5
      value: 46.947
    - type: recall_at_10
      value: 54.129000000000005
    - type: recall_at_20
      value: 62.641000000000005
    - type: recall_at_100
      value: 80.971
    - type: recall_at_1000
      value: 93.98100000000001
    - type: precision_at_1
      value: 32.806000000000004
    - type: precision_at_3
      value: 18.445
    - type: precision_at_5
      value: 13.083
    - type: precision_at_10
      value: 8.142000000000001
    - type: precision_at_20
      value: 5.119
    - type: precision_at_100
      value: 1.599
    - type: precision_at_1000
      value: 0.244
    - type: mrr_at_1
      value: 32.8063
    - type: mrr_at_3
      value: 39.5257
    - type: mrr_at_5
      value: 40.8399
    - type: mrr_at_10
      value: 41.8107
    - type: mrr_at_20
      value: 42.4012
    - type: mrr_at_100
      value: 42.7919
    - type: mrr_at_1000
      value: 42.8261
    - type: nauc_ndcg_at_1_max
      value: 49.2838
    - type: nauc_ndcg_at_1_std
      value: 8.713799999999999
    - type: nauc_ndcg_at_1_diff1
      value: 48.2777
    - type: nauc_ndcg_at_3_max
      value: 44.4031
    - type: nauc_ndcg_at_3_std
      value: 11.4725
    - type: nauc_ndcg_at_3_diff1
      value: 41.5639
    - type: nauc_ndcg_at_5_max
      value: 44.452999999999996
    - type: nauc_ndcg_at_5_std
      value: 11.9373
    - type: nauc_ndcg_at_5_diff1
      value: 41.977199999999996
    - type: nauc_ndcg_at_10_max
      value: 44.8695
    - type: nauc_ndcg_at_10_std
      value: 13.6193
    - type: nauc_ndcg_at_10_diff1
      value: 41.665
    - type: nauc_ndcg_at_20_max
      value: 45.691900000000004
    - type: nauc_ndcg_at_20_std
      value: 14.0959
    - type: nauc_ndcg_at_20_diff1
      value: 42.2414
    - type: nauc_ndcg_at_100_max
      value: 45.7442
    - type: nauc_ndcg_at_100_std
      value: 15.218699999999998
    - type: nauc_ndcg_at_100_diff1
      value: 41.7288
    - type: nauc_ndcg_at_1000_max
      value: 46.788000000000004
    - type: nauc_ndcg_at_1000_std
      value: 15.409900000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 41.9824
    - type: nauc_map_at_1_max
      value: 48.0334
    - type: nauc_map_at_1_std
      value: 8.0125
    - type: nauc_map_at_1_diff1
      value: 53.4579
    - type: nauc_map_at_3_max
      value: 45.1289
    - type: nauc_map_at_3_std
      value: 10.013
    - type: nauc_map_at_3_diff1
      value: 45.51
    - type: nauc_map_at_5_max
      value: 45.3494
    - type: nauc_map_at_5_std
      value: 10.0348
    - type: nauc_map_at_5_diff1
      value: 45.3972
    - type: nauc_map_at_10_max
      value: 45.8378
    - type: nauc_map_at_10_std
      value: 11.3299
    - type: nauc_map_at_10_diff1
      value: 44.8933
    - type: nauc_map_at_20_max
      value: 46.156000000000006
    - type: nauc_map_at_20_std
      value: 11.8154
    - type: nauc_map_at_20_diff1
      value: 44.6615
    - type: nauc_map_at_100_max
      value: 46.1188
    - type: nauc_map_at_100_std
      value: 12.3635
    - type: nauc_map_at_100_diff1
      value: 44.5946
    - type: nauc_map_at_1000_max
      value: 46.1113
    - type: nauc_map_at_1000_std
      value: 12.526599999999998
    - type: nauc_map_at_1000_diff1
      value: 44.595400000000005
    - type: nauc_recall_at_1_max
      value: 48.0334
    - type: nauc_recall_at_1_std
      value: 8.0125
    - type: nauc_recall_at_1_diff1
      value: 53.4579
    - type: nauc_recall_at_3_max
      value: 39.3688
    - type: nauc_recall_at_3_std
      value: 10.3834
    - type: nauc_recall_at_3_diff1
      value: 37.8084
    - type: nauc_recall_at_5_max
      value: 39.3184
    - type: nauc_recall_at_5_std
      value: 10.509400000000001
    - type: nauc_recall_at_5_diff1
      value: 36.7191
    - type: nauc_recall_at_10_max
      value: 38.785599999999995
    - type: nauc_recall_at_10_std
      value: 15.781300000000002
    - type: nauc_recall_at_10_diff1
      value: 34.7564
    - type: nauc_recall_at_20_max
      value: 39.6075
    - type: nauc_recall_at_20_std
      value: 18.0278
    - type: nauc_recall_at_20_diff1
      value: 35.483399999999996
    - type: nauc_recall_at_100_max
      value: 36.1361
    - type: nauc_recall_at_100_std
      value: 29.1037
    - type: nauc_recall_at_100_diff1
      value: 26.9486
    - type: nauc_recall_at_1000_max
      value: 62.4461
    - type: nauc_recall_at_1000_std
      value: 57.465599999999995
    - type: nauc_recall_at_1000_diff1
      value: 29.5554
    - type: nauc_precision_at_1_max
      value: 49.2838
    - type: nauc_precision_at_1_std
      value: 8.713799999999999
    - type: nauc_precision_at_1_diff1
      value: 48.2777
    - type: nauc_precision_at_3_max
      value: 36.4572
    - type: nauc_precision_at_3_std
      value: 14.3924
    - type: nauc_precision_at_3_diff1
      value: 22.9406
    - type: nauc_precision_at_5_max
      value: 32.5803
    - type: nauc_precision_at_5_std
      value: 16.4452
    - type: nauc_precision_at_5_diff1
      value: 18.2745
    - type: nauc_precision_at_10_max
      value: 27.3789
    - type: nauc_precision_at_10_std
      value: 21.0131
    - type: nauc_precision_at_10_diff1
      value: 6.947399999999999
    - type: nauc_precision_at_20_max
      value: 22.8404
    - type: nauc_precision_at_20_std
      value: 24.6328
    - type: nauc_precision_at_20_diff1
      value: 0.1601
    - type: nauc_precision_at_100_max
      value: 2.6098
    - type: nauc_precision_at_100_std
      value: 22.3326
    - type: nauc_precision_at_100_diff1
      value: -10.1755
    - type: nauc_precision_at_1000_max
      value: -6.730899999999999
    - type: nauc_precision_at_1000_std
      value: 18.262900000000002
    - type: nauc_precision_at_1000_diff1
      value: -16.3364
    - type: nauc_mrr_at_1_max
      value: 49.2838
    - type: nauc_mrr_at_1_std
      value: 8.713799999999999
    - type: nauc_mrr_at_1_diff1
      value: 48.2777
    - type: nauc_mrr_at_3_max
      value: 45.8613
    - type: nauc_mrr_at_3_std
      value: 10.4584
    - type: nauc_mrr_at_3_diff1
      value: 42.2388
    - type: nauc_mrr_at_5_max
      value: 46.1544
    - type: nauc_mrr_at_5_std
      value: 11.1434
    - type: nauc_mrr_at_5_diff1
      value: 42.2252
    - type: nauc_mrr_at_10_max
      value: 46.2703
    - type: nauc_mrr_at_10_std
      value: 11.7714
    - type: nauc_mrr_at_10_diff1
      value: 42.0821
    - type: nauc_mrr_at_20_max
      value: 46.4586
    - type: nauc_mrr_at_20_std
      value: 11.9329
    - type: nauc_mrr_at_20_diff1
      value: 42.3199
    - type: nauc_mrr_at_100_max
      value: 46.4309
    - type: nauc_mrr_at_100_std
      value: 11.9458
    - type: nauc_mrr_at_100_diff1
      value: 42.2902
    - type: nauc_mrr_at_1000_max
      value: 46.4392
    - type: nauc_mrr_at_1000_std
      value: 11.9269
    - type: nauc_mrr_at_1000_diff1
      value: 42.3078
    - type: main_score
      value: 42.957
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
      value: 25.692999999999998
    - type: ndcg_at_3
      value: 31.375999999999998
    - type: ndcg_at_5
      value: 33.617999999999995
    - type: ndcg_at_10
      value: 36.409000000000006
    - type: ndcg_at_20
      value: 38.5
    - type: ndcg_at_100
      value: 41.614000000000004
    - type: ndcg_at_1000
      value: 44.119
    - type: map_at_1
      value: 23.666
    - type: map_at_3
      value: 29.072
    - type: map_at_5
      value: 30.453999999999997
    - type: map_at_10
      value: 31.673000000000002
    - type: map_at_20
      value: 32.256
    - type: map_at_100
      value: 32.721000000000004
    - type: map_at_1000
      value: 32.82
    - type: recall_at_1
      value: 23.666
    - type: recall_at_3
      value: 35.693000000000005
    - type: recall_at_5
      value: 40.937
    - type: recall_at_10
      value: 48.979
    - type: recall_at_20
      value: 57.028999999999996
    - type: recall_at_100
      value: 72.80799999999999
    - type: recall_at_1000
      value: 91.546
    - type: precision_at_1
      value: 25.692999999999998
    - type: precision_at_3
      value: 13.123999999999999
    - type: precision_at_5
      value: 9.279
    - type: precision_at_10
      value: 5.712
    - type: precision_at_20
      value: 3.3360000000000003
    - type: precision_at_100
      value: 0.8869999999999999
    - type: precision_at_1000
      value: 0.122
    - type: mrr_at_1
      value: 25.6932
    - type: mrr_at_3
      value: 31.2693
    - type: mrr_at_5
      value: 32.4522
    - type: mrr_at_10
      value: 33.6496
    - type: mrr_at_20
      value: 34.208
    - type: mrr_at_100
      value: 34.6132
    - type: mrr_at_1000
      value: 34.6794
    - type: nauc_ndcg_at_1_max
      value: 30.436400000000003
    - type: nauc_ndcg_at_1_std
      value: -5.177099999999999
    - type: nauc_ndcg_at_1_diff1
      value: 38.9465
    - type: nauc_ndcg_at_3_max
      value: 27.759600000000002
    - type: nauc_ndcg_at_3_std
      value: -3.7716
    - type: nauc_ndcg_at_3_diff1
      value: 32.0374
    - type: nauc_ndcg_at_5_max
      value: 29.284399999999998
    - type: nauc_ndcg_at_5_std
      value: -2.1555999999999997
    - type: nauc_ndcg_at_5_diff1
      value: 31.2735
    - type: nauc_ndcg_at_10_max
      value: 27.4811
    - type: nauc_ndcg_at_10_std
      value: -2.3712
    - type: nauc_ndcg_at_10_diff1
      value: 30.5165
    - type: nauc_ndcg_at_20_max
      value: 28.385899999999996
    - type: nauc_ndcg_at_20_std
      value: -0.7358
    - type: nauc_ndcg_at_20_diff1
      value: 30.5901
    - type: nauc_ndcg_at_100_max
      value: 29.6634
    - type: nauc_ndcg_at_100_std
      value: 0.6082
    - type: nauc_ndcg_at_100_diff1
      value: 30.455
    - type: nauc_ndcg_at_1000_max
      value: 29.316
    - type: nauc_ndcg_at_1000_std
      value: 0.8039
    - type: nauc_ndcg_at_1000_diff1
      value: 30.406699999999997
    - type: nauc_map_at_1_max
      value: 28.618900000000004
    - type: nauc_map_at_1_std
      value: -5.8273
    - type: nauc_map_at_1_diff1
      value: 39.6434
    - type: nauc_map_at_3_max
      value: 27.3257
    - type: nauc_map_at_3_std
      value: -4.8353
    - type: nauc_map_at_3_diff1
      value: 33.9743
    - type: nauc_map_at_5_max
      value: 28.5433
    - type: nauc_map_at_5_std
      value: -3.7222
    - type: nauc_map_at_5_diff1
      value: 33.360099999999996
    - type: nauc_map_at_10_max
      value: 27.972399999999997
    - type: nauc_map_at_10_std
      value: -3.565
    - type: nauc_map_at_10_diff1
      value: 32.9863
    - type: nauc_map_at_20_max
      value: 28.2615
    - type: nauc_map_at_20_std
      value: -3.1113
    - type: nauc_map_at_20_diff1
      value: 32.9793
    - type: nauc_map_at_100_max
      value: 28.540300000000002
    - type: nauc_map_at_100_std
      value: -2.7937
    - type: nauc_map_at_100_diff1
      value: 32.9581
    - type: nauc_map_at_1000_max
      value: 28.5349
    - type: nauc_map_at_1000_std
      value: -2.7701
    - type: nauc_map_at_1000_diff1
      value: 32.939299999999996
    - type: nauc_recall_at_1_max
      value: 28.618900000000004
    - type: nauc_recall_at_1_std
      value: -5.8273
    - type: nauc_recall_at_1_diff1
      value: 39.6434
    - type: nauc_recall_at_3_max
      value: 25.120199999999997
    - type: nauc_recall_at_3_std
      value: -3.4718
    - type: nauc_recall_at_3_diff1
      value: 27.233200000000004
    - type: nauc_recall_at_5_max
      value: 28.6985
    - type: nauc_recall_at_5_std
      value: 0.1915
    - type: nauc_recall_at_5_diff1
      value: 25.533299999999997
    - type: nauc_recall_at_10_max
      value: 23.3717
    - type: nauc_recall_at_10_std
      value: -0.9587999999999999
    - type: nauc_recall_at_10_diff1
      value: 23.8178
    - type: nauc_recall_at_20_max
      value: 25.923800000000004
    - type: nauc_recall_at_20_std
      value: 5.4661
    - type: nauc_recall_at_20_diff1
      value: 23.4099
    - type: nauc_recall_at_100_max
      value: 32.182500000000005
    - type: nauc_recall_at_100_std
      value: 14.696200000000001
    - type: nauc_recall_at_100_diff1
      value: 20.6716
    - type: nauc_recall_at_1000_max
      value: 31.512400000000003
    - type: nauc_recall_at_1000_std
      value: 42.5301
    - type: nauc_recall_at_1000_diff1
      value: 10.7694
    - type: nauc_precision_at_1_max
      value: 30.436400000000003
    - type: nauc_precision_at_1_std
      value: -5.177099999999999
    - type: nauc_precision_at_1_diff1
      value: 38.9465
    - type: nauc_precision_at_3_max
      value: 29.1341
    - type: nauc_precision_at_3_std
      value: -0.1582
    - type: nauc_precision_at_3_diff1
      value: 25.872600000000002
    - type: nauc_precision_at_5_max
      value: 32.7748
    - type: nauc_precision_at_5_std
      value: 4.798100000000001
    - type: nauc_precision_at_5_diff1
      value: 21.712400000000002
    - type: nauc_precision_at_10_max
      value: 27.396700000000003
    - type: nauc_precision_at_10_std
      value: 6.6187
    - type: nauc_precision_at_10_diff1
      value: 16.292499999999997
    - type: nauc_precision_at_20_max
      value: 29.6999
    - type: nauc_precision_at_20_std
      value: 12.6113
    - type: nauc_precision_at_20_diff1
      value: 14.616399999999999
    - type: nauc_precision_at_100_max
      value: 29.297099999999997
    - type: nauc_precision_at_100_std
      value: 20.9722
    - type: nauc_precision_at_100_diff1
      value: 1.6410999999999998
    - type: nauc_precision_at_1000_max
      value: 2.7286
    - type: nauc_precision_at_1000_std
      value: 14.837200000000001
    - type: nauc_precision_at_1000_diff1
      value: -21.584500000000002
    - type: nauc_mrr_at_1_max
      value: 30.436400000000003
    - type: nauc_mrr_at_1_std
      value: -5.177099999999999
    - type: nauc_mrr_at_1_diff1
      value: 38.9465
    - type: nauc_mrr_at_3_max
      value: 29.766199999999998
    - type: nauc_mrr_at_3_std
      value: -3.0375
    - type: nauc_mrr_at_3_diff1
      value: 33.568599999999996
    - type: nauc_mrr_at_5_max
      value: 30.4582
    - type: nauc_mrr_at_5_std
      value: -2.0233
    - type: nauc_mrr_at_5_diff1
      value: 33.1478
    - type: nauc_mrr_at_10_max
      value: 29.3877
    - type: nauc_mrr_at_10_std
      value: -2.3752
    - type: nauc_mrr_at_10_diff1
      value: 32.5597
    - type: nauc_mrr_at_20_max
      value: 29.631400000000003
    - type: nauc_mrr_at_20_std
      value: -1.9325999999999999
    - type: nauc_mrr_at_20_diff1
      value: 32.6145
    - type: nauc_mrr_at_100_max
      value: 29.7106
    - type: nauc_mrr_at_100_std
      value: -1.8483
    - type: nauc_mrr_at_100_diff1
      value: 32.624900000000004
    - type: nauc_mrr_at_1000_max
      value: 29.7099
    - type: nauc_mrr_at_1000_std
      value: -1.8341
    - type: nauc_mrr_at_1000_diff1
      value: 32.6251
    - type: main_score
      value: 36.409000000000006
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
      value: 26.971
    - type: ndcg_at_3
      value: 24.196
    - type: ndcg_at_5
      value: 25.811
    - type: ndcg_at_10
      value: 29.494
    - type: ndcg_at_20
      value: 32.013999999999996
    - type: ndcg_at_100
      value: 35.989
    - type: ndcg_at_1000
      value: 39.326
    - type: map_at_1
      value: 12.107
    - type: map_at_3
      value: 17.538
    - type: map_at_5
      value: 19.124
    - type: map_at_10
      value: 20.896
    - type: map_at_20
      value: 21.798000000000002
    - type: map_at_100
      value: 22.567
    - type: map_at_1000
      value: 22.746
    - type: recall_at_1
      value: 12.107
    - type: recall_at_3
      value: 22.425
    - type: recall_at_5
      value: 27.394000000000002
    - type: recall_at_10
      value: 35.57
    - type: recall_at_20
      value: 42.565
    - type: recall_at_100
      value: 57.708000000000006
    - type: recall_at_1000
      value: 76.673
    - type: precision_at_1
      value: 26.971
    - type: precision_at_3
      value: 18.111
    - type: precision_at_5
      value: 13.694
    - type: precision_at_10
      value: 9.303
    - type: precision_at_20
      value: 5.769
    - type: precision_at_100
      value: 1.6320000000000001
    - type: precision_at_1000
      value: 0.22499999999999998
    - type: mrr_at_1
      value: 26.970699999999997
    - type: mrr_at_3
      value: 36.0478
    - type: mrr_at_5
      value: 37.9598
    - type: mrr_at_10
      value: 39.4286
    - type: mrr_at_20
      value: 39.9242
    - type: mrr_at_100
      value: 40.232600000000005
    - type: mrr_at_1000
      value: 40.2711
    - type: nauc_ndcg_at_1_max
      value: 30.1498
    - type: nauc_ndcg_at_1_std
      value: 9.795
    - type: nauc_ndcg_at_1_diff1
      value: 28.3202
    - type: nauc_ndcg_at_3_max
      value: 36.1507
    - type: nauc_ndcg_at_3_std
      value: 16.6918
    - type: nauc_ndcg_at_3_diff1
      value: 25.9179
    - type: nauc_ndcg_at_5_max
      value: 38.4314
    - type: nauc_ndcg_at_5_std
      value: 19.1236
    - type: nauc_ndcg_at_5_diff1
      value: 25.7315
    - type: nauc_ndcg_at_10_max
      value: 39.734
    - type: nauc_ndcg_at_10_std
      value: 22.795199999999998
    - type: nauc_ndcg_at_10_diff1
      value: 24.5446
    - type: nauc_ndcg_at_20_max
      value: 40.0306
    - type: nauc_ndcg_at_20_std
      value: 25.0242
    - type: nauc_ndcg_at_20_diff1
      value: 23.7608
    - type: nauc_ndcg_at_100_max
      value: 39.881
    - type: nauc_ndcg_at_100_std
      value: 26.8935
    - type: nauc_ndcg_at_100_diff1
      value: 23.366600000000002
    - type: nauc_ndcg_at_1000_max
      value: 39.6299
    - type: nauc_ndcg_at_1000_std
      value: 27.556000000000004
    - type: nauc_ndcg_at_1000_diff1
      value: 23.4406
    - type: nauc_map_at_1_max
      value: 36.033500000000004
    - type: nauc_map_at_1_std
      value: 9.3902
    - type: nauc_map_at_1_diff1
      value: 33.3389
    - type: nauc_map_at_3_max
      value: 38.2772
    - type: nauc_map_at_3_std
      value: 14.862
    - type: nauc_map_at_3_diff1
      value: 29.121799999999997
    - type: nauc_map_at_5_max
      value: 38.8901
    - type: nauc_map_at_5_std
      value: 16.4551
    - type: nauc_map_at_5_diff1
      value: 28.258499999999998
    - type: nauc_map_at_10_max
      value: 39.689099999999996
    - type: nauc_map_at_10_std
      value: 19.0082
    - type: nauc_map_at_10_diff1
      value: 27.5292
    - type: nauc_map_at_20_max
      value: 39.8114
    - type: nauc_map_at_20_std
      value: 20.099700000000002
    - type: nauc_map_at_20_diff1
      value: 27.1249
    - type: nauc_map_at_100_max
      value: 39.7759
    - type: nauc_map_at_100_std
      value: 20.671400000000002
    - type: nauc_map_at_100_diff1
      value: 26.9515
    - type: nauc_map_at_1000_max
      value: 39.7635
    - type: nauc_map_at_1000_std
      value: 20.7381
    - type: nauc_map_at_1000_diff1
      value: 26.9318
    - type: nauc_recall_at_1_max
      value: 36.033500000000004
    - type: nauc_recall_at_1_std
      value: 9.3902
    - type: nauc_recall_at_1_diff1
      value: 33.3389
    - type: nauc_recall_at_3_max
      value: 37.040099999999995
    - type: nauc_recall_at_3_std
      value: 18.421000000000003
    - type: nauc_recall_at_3_diff1
      value: 23.591
    - type: nauc_recall_at_5_max
      value: 38.2483
    - type: nauc_recall_at_5_std
      value: 21.9791
    - type: nauc_recall_at_5_diff1
      value: 20.9432
    - type: nauc_recall_at_10_max
      value: 38.684400000000004
    - type: nauc_recall_at_10_std
      value: 27.528000000000002
    - type: nauc_recall_at_10_diff1
      value: 17.874599999999997
    - type: nauc_recall_at_20_max
      value: 37.7408
    - type: nauc_recall_at_20_std
      value: 31.178800000000003
    - type: nauc_recall_at_20_diff1
      value: 15.3021
    - type: nauc_recall_at_100_max
      value: 35.0668
    - type: nauc_recall_at_100_std
      value: 35.8934
    - type: nauc_recall_at_100_diff1
      value: 12.0978
    - type: nauc_recall_at_1000_max
      value: 33.2113
    - type: nauc_recall_at_1000_std
      value: 44.3165
    - type: nauc_recall_at_1000_diff1
      value: 9.6011
    - type: nauc_precision_at_1_max
      value: 30.1498
    - type: nauc_precision_at_1_std
      value: 9.795
    - type: nauc_precision_at_1_diff1
      value: 28.3202
    - type: nauc_precision_at_3_max
      value: 32.1047
    - type: nauc_precision_at_3_std
      value: 20.7027
    - type: nauc_precision_at_3_diff1
      value: 18.3366
    - type: nauc_precision_at_5_max
      value: 32.9484
    - type: nauc_precision_at_5_std
      value: 24.439700000000002
    - type: nauc_precision_at_5_diff1
      value: 16.3709
    - type: nauc_precision_at_10_max
      value: 30.626900000000003
    - type: nauc_precision_at_10_std
      value: 30.3335
    - type: nauc_precision_at_10_diff1
      value: 10.4378
    - type: nauc_precision_at_20_max
      value: 26.875100000000003
    - type: nauc_precision_at_20_std
      value: 33.1578
    - type: nauc_precision_at_20_diff1
      value: 6.3161
    - type: nauc_precision_at_100_max
      value: 18.5691
    - type: nauc_precision_at_100_std
      value: 32.4294
    - type: nauc_precision_at_100_diff1
      value: 1.9001000000000001
    - type: nauc_precision_at_1000_max
      value: 5.2522
    - type: nauc_precision_at_1000_std
      value: 26.337899999999998
    - type: nauc_precision_at_1000_diff1
      value: -4.2309
    - type: nauc_mrr_at_1_max
      value: 30.1498
    - type: nauc_mrr_at_1_std
      value: 9.795
    - type: nauc_mrr_at_1_diff1
      value: 28.3202
    - type: nauc_mrr_at_3_max
      value: 32.2466
    - type: nauc_mrr_at_3_std
      value: 15.6475
    - type: nauc_mrr_at_3_diff1
      value: 24.160899999999998
    - type: nauc_mrr_at_5_max
      value: 33.1837
    - type: nauc_mrr_at_5_std
      value: 16.8917
    - type: nauc_mrr_at_5_diff1
      value: 24.072499999999998
    - type: nauc_mrr_at_10_max
      value: 33.576
    - type: nauc_mrr_at_10_std
      value: 17.4501
    - type: nauc_mrr_at_10_diff1
      value: 23.9826
    - type: nauc_mrr_at_20_max
      value: 33.5003
    - type: nauc_mrr_at_20_std
      value: 17.5104
    - type: nauc_mrr_at_20_diff1
      value: 23.9237
    - type: nauc_mrr_at_100_max
      value: 33.455200000000005
    - type: nauc_mrr_at_100_std
      value: 17.5181
    - type: nauc_mrr_at_100_diff1
      value: 23.9598
    - type: nauc_mrr_at_1000_max
      value: 33.4473
    - type: nauc_mrr_at_1000_std
      value: 17.4969
    - type: nauc_mrr_at_1000_diff1
      value: 23.974899999999998
    - type: main_score
      value: 29.494
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeFeedbackMT (default)
      revision: b0f12fa0c0dd67f59c95a5c33d02aeeb4c398c5f
      split: test
      type: CoIR-Retrieval/codefeedback-mt
    metrics:
    - type: ndcg_at_1
      value: 21.044
    - type: ndcg_at_3
      value: 27.134999999999998
    - type: ndcg_at_5
      value: 29.205
    - type: ndcg_at_10
      value: 31.391999999999996
    - type: ndcg_at_20
      value: 33.031
    - type: ndcg_at_100
      value: 35.852000000000004
    - type: ndcg_at_1000
      value: 38.076
    - type: map_at_1
      value: 21.044
    - type: map_at_3
      value: 25.637
    - type: map_at_5
      value: 26.779999999999998
    - type: map_at_10
      value: 27.683000000000003
    - type: map_at_20
      value: 28.133999999999997
    - type: map_at_100
      value: 28.510999999999996
    - type: map_at_1000
      value: 28.588
    - type: recall_at_1
      value: 21.044
    - type: recall_at_3
      value: 31.468
    - type: recall_at_5
      value: 36.522
    - type: recall_at_10
      value: 43.278
    - type: recall_at_20
      value: 49.748
    - type: recall_at_100
      value: 65.16499999999999
    - type: recall_at_1000
      value: 83.031
    - type: precision_at_1
      value: 21.044
    - type: precision_at_3
      value: 10.488999999999999
    - type: precision_at_5
      value: 7.303999999999999
    - type: precision_at_10
      value: 4.328
    - type: precision_at_20
      value: 2.487
    - type: precision_at_100
      value: 0.652
    - type: precision_at_1000
      value: 0.083
    - type: mrr_at_1
      value: 21.043899999999997
    - type: mrr_at_3
      value: 25.6371
    - type: mrr_at_5
      value: 26.7796
    - type: mrr_at_10
      value: 27.6831
    - type: mrr_at_20
      value: 28.1344
    - type: mrr_at_100
      value: 28.510999999999996
    - type: mrr_at_1000
      value: 28.588400000000004
    - type: nauc_ndcg_at_1_max
      value: 11.8658
    - type: nauc_ndcg_at_1_std
      value: -18.4852
    - type: nauc_ndcg_at_1_diff1
      value: 47.3429
    - type: nauc_ndcg_at_3_max
      value: 11.608400000000001
    - type: nauc_ndcg_at_3_std
      value: -19.0804
    - type: nauc_ndcg_at_3_diff1
      value: 41.7031
    - type: nauc_ndcg_at_5_max
      value: 11.289299999999999
    - type: nauc_ndcg_at_5_std
      value: -19.3124
    - type: nauc_ndcg_at_5_diff1
      value: 40.5381
    - type: nauc_ndcg_at_10_max
      value: 11.6701
    - type: nauc_ndcg_at_10_std
      value: -18.7838
    - type: nauc_ndcg_at_10_diff1
      value: 39.8088
    - type: nauc_ndcg_at_20_max
      value: 11.942400000000001
    - type: nauc_ndcg_at_20_std
      value: -18.123900000000003
    - type: nauc_ndcg_at_20_diff1
      value: 38.967800000000004
    - type: nauc_ndcg_at_100_max
      value: 13.114999999999998
    - type: nauc_ndcg_at_100_std
      value: -16.1964
    - type: nauc_ndcg_at_100_diff1
      value: 39.0077
    - type: nauc_ndcg_at_1000_max
      value: 13.5244
    - type: nauc_ndcg_at_1000_std
      value: -15.2702
    - type: nauc_ndcg_at_1000_diff1
      value: 39.1235
    - type: nauc_map_at_1_max
      value: 11.8658
    - type: nauc_map_at_1_std
      value: -18.4852
    - type: nauc_map_at_1_diff1
      value: 47.3429
    - type: nauc_map_at_3_max
      value: 11.6937
    - type: nauc_map_at_3_std
      value: -18.9625
    - type: nauc_map_at_3_diff1
      value: 42.993900000000004
    - type: nauc_map_at_5_max
      value: 11.5064
    - type: nauc_map_at_5_std
      value: -19.0958
    - type: nauc_map_at_5_diff1
      value: 42.3108
    - type: nauc_map_at_10_max
      value: 11.6615
    - type: nauc_map_at_10_std
      value: -18.885199999999998
    - type: nauc_map_at_10_diff1
      value: 41.993399999999994
    - type: nauc_map_at_20_max
      value: 11.7419
    - type: nauc_map_at_20_std
      value: -18.7005
    - type: nauc_map_at_20_diff1
      value: 41.7643
    - type: nauc_map_at_100_max
      value: 11.902600000000001
    - type: nauc_map_at_100_std
      value: -18.4376
    - type: nauc_map_at_100_diff1
      value: 41.7771
    - type: nauc_map_at_1000_max
      value: 11.9208
    - type: nauc_map_at_1000_std
      value: -18.395500000000002
    - type: nauc_map_at_1000_diff1
      value: 41.7802
    - type: nauc_recall_at_1_max
      value: 11.8658
    - type: nauc_recall_at_1_std
      value: -18.4852
    - type: nauc_recall_at_1_diff1
      value: 47.3429
    - type: nauc_recall_at_3_max
      value: 11.3724
    - type: nauc_recall_at_3_std
      value: -19.3869
    - type: nauc_recall_at_3_diff1
      value: 38.2763
    - type: nauc_recall_at_5_max
      value: 10.678600000000001
    - type: nauc_recall_at_5_std
      value: -19.8995
    - type: nauc_recall_at_5_diff1
      value: 35.781400000000005
    - type: nauc_recall_at_10_max
      value: 11.7997
    - type: nauc_recall_at_10_std
      value: -18.3219
    - type: nauc_recall_at_10_diff1
      value: 33.7507
    - type: nauc_recall_at_20_max
      value: 12.7832
    - type: nauc_recall_at_20_std
      value: -15.8611
    - type: nauc_recall_at_20_diff1
      value: 30.4676
    - type: nauc_recall_at_100_max
      value: 20.0012
    - type: nauc_recall_at_100_std
      value: -3.8268000000000004
    - type: nauc_recall_at_100_diff1
      value: 28.8928
    - type: nauc_recall_at_1000_max
      value: 30.812099999999997
    - type: nauc_recall_at_1000_std
      value: 18.1771
    - type: nauc_recall_at_1000_diff1
      value: 23.3851
    - type: nauc_precision_at_1_max
      value: 11.8658
    - type: nauc_precision_at_1_std
      value: -18.4852
    - type: nauc_precision_at_1_diff1
      value: 47.3429
    - type: nauc_precision_at_3_max
      value: 11.3724
    - type: nauc_precision_at_3_std
      value: -19.3869
    - type: nauc_precision_at_3_diff1
      value: 38.2763
    - type: nauc_precision_at_5_max
      value: 10.678600000000001
    - type: nauc_precision_at_5_std
      value: -19.8995
    - type: nauc_precision_at_5_diff1
      value: 35.781400000000005
    - type: nauc_precision_at_10_max
      value: 11.7997
    - type: nauc_precision_at_10_std
      value: -18.3219
    - type: nauc_precision_at_10_diff1
      value: 33.7507
    - type: nauc_precision_at_20_max
      value: 12.7832
    - type: nauc_precision_at_20_std
      value: -15.8611
    - type: nauc_precision_at_20_diff1
      value: 30.4676
    - type: nauc_precision_at_100_max
      value: 20.0012
    - type: nauc_precision_at_100_std
      value: -3.8268000000000004
    - type: nauc_precision_at_100_diff1
      value: 28.8928
    - type: nauc_precision_at_1000_max
      value: 30.812099999999997
    - type: nauc_precision_at_1000_std
      value: 18.1771
    - type: nauc_precision_at_1000_diff1
      value: 23.3851
    - type: nauc_mrr_at_1_max
      value: 11.8658
    - type: nauc_mrr_at_1_std
      value: -18.4852
    - type: nauc_mrr_at_1_diff1
      value: 47.3429
    - type: nauc_mrr_at_3_max
      value: 11.6937
    - type: nauc_mrr_at_3_std
      value: -18.9625
    - type: nauc_mrr_at_3_diff1
      value: 42.993900000000004
    - type: nauc_mrr_at_5_max
      value: 11.5064
    - type: nauc_mrr_at_5_std
      value: -19.0958
    - type: nauc_mrr_at_5_diff1
      value: 42.3108
    - type: nauc_mrr_at_10_max
      value: 11.6615
    - type: nauc_mrr_at_10_std
      value: -18.885199999999998
    - type: nauc_mrr_at_10_diff1
      value: 41.993399999999994
    - type: nauc_mrr_at_20_max
      value: 11.7419
    - type: nauc_mrr_at_20_std
      value: -18.7005
    - type: nauc_mrr_at_20_diff1
      value: 41.7643
    - type: nauc_mrr_at_100_max
      value: 11.902600000000001
    - type: nauc_mrr_at_100_std
      value: -18.4376
    - type: nauc_mrr_at_100_diff1
      value: 41.7771
    - type: nauc_mrr_at_1000_max
      value: 11.9208
    - type: nauc_mrr_at_1000_std
      value: -18.395500000000002
    - type: nauc_mrr_at_1000_diff1
      value: 41.7802
    - type: main_score
      value: 31.391999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeFeedbackST (default)
      revision: d213819e87aab9010628da8b73ab4eb337c89340
      split: test
      type: CoIR-Retrieval/codefeedback-st
    metrics:
    - type: ndcg_at_1
      value: 51.227000000000004
    - type: ndcg_at_3
      value: 62.971999999999994
    - type: ndcg_at_5
      value: 65.649
    - type: ndcg_at_10
      value: 67.72200000000001
    - type: ndcg_at_20
      value: 68.919
    - type: ndcg_at_100
      value: 70.15299999999999
    - type: ndcg_at_1000
      value: 70.658
    - type: map_at_1
      value: 51.227000000000004
    - type: map_at_3
      value: 60.114000000000004
    - type: map_at_5
      value: 61.607
    - type: map_at_10
      value: 62.475
    - type: map_at_20
      value: 62.806
    - type: map_at_100
      value: 62.979
    - type: map_at_1000
      value: 62.999
    - type: recall_at_1
      value: 51.227000000000004
    - type: recall_at_3
      value: 71.232
    - type: recall_at_5
      value: 77.69800000000001
    - type: recall_at_10
      value: 84.041
    - type: recall_at_20
      value: 88.756
    - type: recall_at_100
      value: 95.371
    - type: recall_at_1000
      value: 99.278
    - type: precision_at_1
      value: 51.227000000000004
    - type: precision_at_3
      value: 23.744
    - type: precision_at_5
      value: 15.540000000000001
    - type: precision_at_10
      value: 8.404
    - type: precision_at_20
      value: 4.438000000000001
    - type: precision_at_100
      value: 0.954
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 51.0062
    - type: mrr_at_3
      value: 60.0023
    - type: mrr_at_5
      value: 61.492999999999995
    - type: mrr_at_10
      value: 62.362899999999996
    - type: mrr_at_20
      value: 62.693200000000004
    - type: mrr_at_100
      value: 62.8664
    - type: mrr_at_1000
      value: 62.8866
    - type: nauc_ndcg_at_1_max
      value: 5.5119
    - type: nauc_ndcg_at_1_std
      value: -27.434599999999996
    - type: nauc_ndcg_at_1_diff1
      value: 67.3476
    - type: nauc_ndcg_at_3_max
      value: 11.8474
    - type: nauc_ndcg_at_3_std
      value: -30.5305
    - type: nauc_ndcg_at_3_diff1
      value: 61.4515
    - type: nauc_ndcg_at_5_max
      value: 12.692700000000002
    - type: nauc_ndcg_at_5_std
      value: -30.938
    - type: nauc_ndcg_at_5_diff1
      value: 61.0505
    - type: nauc_ndcg_at_10_max
      value: 12.354800000000001
    - type: nauc_ndcg_at_10_std
      value: -30.6409
    - type: nauc_ndcg_at_10_diff1
      value: 61.205600000000004
    - type: nauc_ndcg_at_20_max
      value: 11.9146
    - type: nauc_ndcg_at_20_std
      value: -30.247
    - type: nauc_ndcg_at_20_diff1
      value: 61.5428
    - type: nauc_ndcg_at_100_max
      value: 11.5407
    - type: nauc_ndcg_at_100_std
      value: -29.561700000000002
    - type: nauc_ndcg_at_100_diff1
      value: 62.06270000000001
    - type: nauc_ndcg_at_1000_max
      value: 11.2459
    - type: nauc_ndcg_at_1000_std
      value: -29.5751
    - type: nauc_ndcg_at_1000_diff1
      value: 62.28
    - type: nauc_map_at_1_max
      value: 5.5119
    - type: nauc_map_at_1_std
      value: -27.434599999999996
    - type: nauc_map_at_1_diff1
      value: 67.3476
    - type: nauc_map_at_3_max
      value: 10.1298
    - type: nauc_map_at_3_std
      value: -29.674899999999997
    - type: nauc_map_at_3_diff1
      value: 62.982000000000006
    - type: nauc_map_at_5_max
      value: 10.5075
    - type: nauc_map_at_5_std
      value: -29.858600000000003
    - type: nauc_map_at_5_diff1
      value: 62.829299999999996
    - type: nauc_map_at_10_max
      value: 10.3459
    - type: nauc_map_at_10_std
      value: -29.7338
    - type: nauc_map_at_10_diff1
      value: 62.917699999999996
    - type: nauc_map_at_20_max
      value: 10.2198
    - type: nauc_map_at_20_std
      value: -29.6284
    - type: nauc_map_at_20_diff1
      value: 63.01409999999999
    - type: nauc_map_at_100_max
      value: 10.1683
    - type: nauc_map_at_100_std
      value: -29.5448
    - type: nauc_map_at_100_diff1
      value: 63.0794
    - type: nauc_map_at_1000_max
      value: 10.1602
    - type: nauc_map_at_1000_std
      value: -29.5412
    - type: nauc_map_at_1000_diff1
      value: 63.0874
    - type: nauc_recall_at_1_max
      value: 5.5119
    - type: nauc_recall_at_1_std
      value: -27.434599999999996
    - type: nauc_recall_at_1_diff1
      value: 67.3476
    - type: nauc_recall_at_3_max
      value: 17.8724
    - type: nauc_recall_at_3_std
      value: -33.5404
    - type: nauc_recall_at_3_diff1
      value: 56.1172
    - type: nauc_recall_at_5_max
      value: 21.945700000000002
    - type: nauc_recall_at_5_std
      value: -35.5124
    - type: nauc_recall_at_5_diff1
      value: 53.6154
    - type: nauc_recall_at_10_max
      value: 23.1968
    - type: nauc_recall_at_10_std
      value: -35.4292
    - type: nauc_recall_at_10_diff1
      value: 51.998900000000006
    - type: nauc_recall_at_20_max
      value: 23.4056
    - type: nauc_recall_at_20_std
      value: -33.825300000000006
    - type: nauc_recall_at_20_diff1
      value: 51.544900000000005
    - type: nauc_recall_at_100_max
      value: 29.2331
    - type: nauc_recall_at_100_std
      value: -20.444499999999998
    - type: nauc_recall_at_100_diff1
      value: 51.8606
    - type: nauc_recall_at_1000_max
      value: 47.943000000000005
    - type: nauc_recall_at_1000_std
      value: 16.1139
    - type: nauc_recall_at_1000_diff1
      value: 49.2407
    - type: nauc_precision_at_1_max
      value: 5.5119
    - type: nauc_precision_at_1_std
      value: -27.434599999999996
    - type: nauc_precision_at_1_diff1
      value: 67.3476
    - type: nauc_precision_at_3_max
      value: 17.8724
    - type: nauc_precision_at_3_std
      value: -33.5404
    - type: nauc_precision_at_3_diff1
      value: 56.1172
    - type: nauc_precision_at_5_max
      value: 21.945700000000002
    - type: nauc_precision_at_5_std
      value: -35.5124
    - type: nauc_precision_at_5_diff1
      value: 53.6154
    - type: nauc_precision_at_10_max
      value: 23.1968
    - type: nauc_precision_at_10_std
      value: -35.4292
    - type: nauc_precision_at_10_diff1
      value: 51.998900000000006
    - type: nauc_precision_at_20_max
      value: 23.4056
    - type: nauc_precision_at_20_std
      value: -33.825300000000006
    - type: nauc_precision_at_20_diff1
      value: 51.544900000000005
    - type: nauc_precision_at_100_max
      value: 29.2331
    - type: nauc_precision_at_100_std
      value: -20.444499999999998
    - type: nauc_precision_at_100_diff1
      value: 51.8606
    - type: nauc_precision_at_1000_max
      value: 47.943000000000005
    - type: nauc_precision_at_1000_std
      value: 16.1139
    - type: nauc_precision_at_1000_diff1
      value: 49.2407
    - type: nauc_mrr_at_1_max
      value: 4.9502
    - type: nauc_mrr_at_1_std
      value: -27.426099999999998
    - type: nauc_mrr_at_1_diff1
      value: 67.8214
    - type: nauc_mrr_at_3_max
      value: 9.7423
    - type: nauc_mrr_at_3_std
      value: -29.674699999999998
    - type: nauc_mrr_at_3_diff1
      value: 63.24340000000001
    - type: nauc_mrr_at_5_max
      value: 10.1129
    - type: nauc_mrr_at_5_std
      value: -29.871100000000002
    - type: nauc_mrr_at_5_diff1
      value: 63.1148
    - type: nauc_mrr_at_10_max
      value: 9.9493
    - type: nauc_mrr_at_10_std
      value: -29.7413
    - type: nauc_mrr_at_10_diff1
      value: 63.2057
    - type: nauc_mrr_at_20_max
      value: 9.8157
    - type: nauc_mrr_at_20_std
      value: -29.644
    - type: nauc_mrr_at_20_diff1
      value: 63.307100000000005
    - type: nauc_mrr_at_100_max
      value: 9.7639
    - type: nauc_mrr_at_100_std
      value: -29.5582
    - type: nauc_mrr_at_100_diff1
      value: 63.3738
    - type: nauc_mrr_at_1000_max
      value: 9.7555
    - type: nauc_mrr_at_1000_std
      value: -29.554599999999997
    - type: nauc_mrr_at_1000_diff1
      value: 63.382000000000005
    - type: main_score
      value: 67.72200000000001
    task:
      type: Retrieval
  - dataset:
      config: python
      name: MTEB CodeSearchNetCCRetrieval (python)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 32.417
    - type: ndcg_at_3
      value: 40.904
    - type: ndcg_at_5
      value: 43.321
    - type: ndcg_at_10
      value: 45.532000000000004
    - type: ndcg_at_20
      value: 47.071000000000005
    - type: ndcg_at_100
      value: 49.297999999999995
    - type: ndcg_at_1000
      value: 50.859
    - type: map_at_1
      value: 32.417
    - type: map_at_3
      value: 38.829
    - type: map_at_5
      value: 40.166000000000004
    - type: map_at_10
      value: 41.087
    - type: map_at_20
      value: 41.510999999999996
    - type: map_at_100
      value: 41.815000000000005
    - type: map_at_1000
      value: 41.869
    - type: recall_at_1
      value: 32.417
    - type: recall_at_3
      value: 46.903
    - type: recall_at_5
      value: 52.788999999999994
    - type: recall_at_10
      value: 59.57900000000001
    - type: recall_at_20
      value: 65.652
    - type: recall_at_100
      value: 77.718
    - type: recall_at_1000
      value: 90.294
    - type: precision_at_1
      value: 32.417
    - type: precision_at_3
      value: 15.634
    - type: precision_at_5
      value: 10.558
    - type: precision_at_10
      value: 5.958
    - type: precision_at_20
      value: 3.283
    - type: precision_at_100
      value: 0.777
    - type: precision_at_1000
      value: 0.09
    - type: mrr_at_1
      value: 32.4239
    - type: mrr_at_3
      value: 38.8323
    - type: mrr_at_5
      value: 40.1696
    - type: mrr_at_10
      value: 41.0908
    - type: mrr_at_20
      value: 41.5149
    - type: mrr_at_100
      value: 41.8188
    - type: mrr_at_1000
      value: 41.8726
    - type: nauc_ndcg_at_1_max
      value: 32.4803
    - type: nauc_ndcg_at_1_std
      value: -1.1774
    - type: nauc_ndcg_at_1_diff1
      value: 54.68730000000001
    - type: nauc_ndcg_at_3_max
      value: 33.5662
    - type: nauc_ndcg_at_3_std
      value: 0.361
    - type: nauc_ndcg_at_3_diff1
      value: 49.522
    - type: nauc_ndcg_at_5_max
      value: 33.0861
    - type: nauc_ndcg_at_5_std
      value: 0.5551999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 48.9052
    - type: nauc_ndcg_at_10_max
      value: 33.0427
    - type: nauc_ndcg_at_10_std
      value: 1.466
    - type: nauc_ndcg_at_10_diff1
      value: 48.3256
    - type: nauc_ndcg_at_20_max
      value: 33.059
    - type: nauc_ndcg_at_20_std
      value: 2.2277
    - type: nauc_ndcg_at_20_diff1
      value: 48.2916
    - type: nauc_ndcg_at_100_max
      value: 33.0797
    - type: nauc_ndcg_at_100_std
      value: 2.9991
    - type: nauc_ndcg_at_100_diff1
      value: 48.266999999999996
    - type: nauc_ndcg_at_1000_max
      value: 33.1052
    - type: nauc_ndcg_at_1000_std
      value: 2.8583000000000003
    - type: nauc_ndcg_at_1000_diff1
      value: 48.5209
    - type: nauc_map_at_1_max
      value: 32.4803
    - type: nauc_map_at_1_std
      value: -1.1774
    - type: nauc_map_at_1_diff1
      value: 54.68730000000001
    - type: nauc_map_at_3_max
      value: 33.3014
    - type: nauc_map_at_3_std
      value: -0.06409999999999999
    - type: nauc_map_at_3_diff1
      value: 50.6726
    - type: nauc_map_at_5_max
      value: 33.0327
    - type: nauc_map_at_5_std
      value: 0.0325
    - type: nauc_map_at_5_diff1
      value: 50.3363
    - type: nauc_map_at_10_max
      value: 33.0181
    - type: nauc_map_at_10_std
      value: 0.3939
    - type: nauc_map_at_10_diff1
      value: 50.1109
    - type: nauc_map_at_20_max
      value: 33.0183
    - type: nauc_map_at_20_std
      value: 0.5951
    - type: nauc_map_at_20_diff1
      value: 50.108
    - type: nauc_map_at_100_max
      value: 33.022
    - type: nauc_map_at_100_std
      value: 0.6973
    - type: nauc_map_at_100_diff1
      value: 50.10790000000001
    - type: nauc_map_at_1000_max
      value: 33.022
    - type: nauc_map_at_1000_std
      value: 0.6931999999999999
    - type: nauc_map_at_1000_diff1
      value: 50.1174
    - type: nauc_recall_at_1_max
      value: 32.4803
    - type: nauc_recall_at_1_std
      value: -1.1774
    - type: nauc_recall_at_1_diff1
      value: 54.68730000000001
    - type: nauc_recall_at_3_max
      value: 34.3301
    - type: nauc_recall_at_3_std
      value: 1.6075
    - type: nauc_recall_at_3_diff1
      value: 46.2477
    - type: nauc_recall_at_5_max
      value: 33.177299999999995
    - type: nauc_recall_at_5_std
      value: 2.1687000000000003
    - type: nauc_recall_at_5_diff1
      value: 44.61
    - type: nauc_recall_at_10_max
      value: 33.020500000000006
    - type: nauc_recall_at_10_std
      value: 5.3331
    - type: nauc_recall_at_10_diff1
      value: 42.3796
    - type: nauc_recall_at_20_max
      value: 33.1279
    - type: nauc_recall_at_20_std
      value: 9.2437
    - type: nauc_recall_at_20_diff1
      value: 41.584199999999996
    - type: nauc_recall_at_100_max
      value: 33.2882
    - type: nauc_recall_at_100_std
      value: 18.1866
    - type: nauc_recall_at_100_diff1
      value: 38.9221
    - type: nauc_recall_at_1000_max
      value: 34.2607
    - type: nauc_recall_at_1000_std
      value: 30.5699
    - type: nauc_recall_at_1000_diff1
      value: 35.204800000000006
    - type: nauc_precision_at_1_max
      value: 32.4803
    - type: nauc_precision_at_1_std
      value: -1.1774
    - type: nauc_precision_at_1_diff1
      value: 54.68730000000001
    - type: nauc_precision_at_3_max
      value: 34.3301
    - type: nauc_precision_at_3_std
      value: 1.6075
    - type: nauc_precision_at_3_diff1
      value: 46.2477
    - type: nauc_precision_at_5_max
      value: 33.177299999999995
    - type: nauc_precision_at_5_std
      value: 2.1687000000000003
    - type: nauc_precision_at_5_diff1
      value: 44.61
    - type: nauc_precision_at_10_max
      value: 33.020500000000006
    - type: nauc_precision_at_10_std
      value: 5.3331
    - type: nauc_precision_at_10_diff1
      value: 42.3796
    - type: nauc_precision_at_20_max
      value: 33.1279
    - type: nauc_precision_at_20_std
      value: 9.2437
    - type: nauc_precision_at_20_diff1
      value: 41.584199999999996
    - type: nauc_precision_at_100_max
      value: 33.2882
    - type: nauc_precision_at_100_std
      value: 18.1866
    - type: nauc_precision_at_100_diff1
      value: 38.9221
    - type: nauc_precision_at_1000_max
      value: 34.2607
    - type: nauc_precision_at_1000_std
      value: 30.5699
    - type: nauc_precision_at_1000_diff1
      value: 35.204800000000006
    - type: nauc_mrr_at_1_max
      value: 32.5013
    - type: nauc_mrr_at_1_std
      value: -1.1843
    - type: nauc_mrr_at_1_diff1
      value: 54.6663
    - type: nauc_mrr_at_3_max
      value: 33.315
    - type: nauc_mrr_at_3_std
      value: -0.06849999999999999
    - type: nauc_mrr_at_3_diff1
      value: 50.66460000000001
    - type: nauc_mrr_at_5_max
      value: 33.0452
    - type: nauc_mrr_at_5_std
      value: 0.0305
    - type: nauc_mrr_at_5_diff1
      value: 50.326499999999996
    - type: nauc_mrr_at_10_max
      value: 33.0308
    - type: nauc_mrr_at_10_std
      value: 0.39189999999999997
    - type: nauc_mrr_at_10_diff1
      value: 50.101
    - type: nauc_mrr_at_20_max
      value: 33.031
    - type: nauc_mrr_at_20_std
      value: 0.5930000000000001
    - type: nauc_mrr_at_20_diff1
      value: 50.0981
    - type: nauc_mrr_at_100_max
      value: 33.0348
    - type: nauc_mrr_at_100_std
      value: 0.6952
    - type: nauc_mrr_at_100_diff1
      value: 50.097899999999996
    - type: nauc_mrr_at_1000_max
      value: 33.0348
    - type: nauc_mrr_at_1000_std
      value: 0.6910999999999999
    - type: nauc_mrr_at_1000_diff1
      value: 50.1074
    - type: main_score
      value: 45.532000000000004
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB CodeSearchNetCCRetrieval (javascript)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 33.364
    - type: ndcg_at_3
      value: 41.943999999999996
    - type: ndcg_at_5
      value: 44.167
    - type: ndcg_at_10
      value: 46.024
    - type: ndcg_at_20
      value: 47.508
    - type: ndcg_at_100
      value: 49.668
    - type: ndcg_at_1000
      value: 51.336999999999996
    - type: map_at_1
      value: 33.364
    - type: map_at_3
      value: 39.846
    - type: map_at_5
      value: 41.083999999999996
    - type: map_at_10
      value: 41.85
    - type: map_at_20
      value: 42.254000000000005
    - type: map_at_100
      value: 42.547000000000004
    - type: map_at_1000
      value: 42.601
    - type: recall_at_1
      value: 33.364
    - type: recall_at_3
      value: 48.010000000000005
    - type: recall_at_5
      value: 53.388000000000005
    - type: recall_at_10
      value: 59.131
    - type: recall_at_20
      value: 65.026
    - type: recall_at_100
      value: 76.755
    - type: recall_at_1000
      value: 90.398
    - type: precision_at_1
      value: 33.364
    - type: precision_at_3
      value: 16.003
    - type: precision_at_5
      value: 10.678
    - type: precision_at_10
      value: 5.913
    - type: precision_at_20
      value: 3.251
    - type: precision_at_100
      value: 0.768
    - type: precision_at_1000
      value: 0.09
    - type: mrr_at_1
      value: 33.272600000000004
    - type: mrr_at_3
      value: 39.7954
    - type: mrr_at_5
      value: 41.0412
    - type: mrr_at_10
      value: 41.8073
    - type: mrr_at_20
      value: 42.2109
    - type: mrr_at_100
      value: 42.5037
    - type: mrr_at_1000
      value: 42.5577
    - type: nauc_ndcg_at_1_max
      value: 26.6036
    - type: nauc_ndcg_at_1_std
      value: -8.3972
    - type: nauc_ndcg_at_1_diff1
      value: 52.43560000000001
    - type: nauc_ndcg_at_3_max
      value: 28.5119
    - type: nauc_ndcg_at_3_std
      value: -5.6812000000000005
    - type: nauc_ndcg_at_3_diff1
      value: 47.1671
    - type: nauc_ndcg_at_5_max
      value: 28.1875
    - type: nauc_ndcg_at_5_std
      value: -5.6434999999999995
    - type: nauc_ndcg_at_5_diff1
      value: 46.1849
    - type: nauc_ndcg_at_10_max
      value: 27.5534
    - type: nauc_ndcg_at_10_std
      value: -5.6785000000000005
    - type: nauc_ndcg_at_10_diff1
      value: 45.6927
    - type: nauc_ndcg_at_20_max
      value: 27.4338
    - type: nauc_ndcg_at_20_std
      value: -5.5037
    - type: nauc_ndcg_at_20_diff1
      value: 45.872800000000005
    - type: nauc_ndcg_at_100_max
      value: 27.386100000000003
    - type: nauc_ndcg_at_100_std
      value: -5.2795000000000005
    - type: nauc_ndcg_at_100_diff1
      value: 46.1008
    - type: nauc_ndcg_at_1000_max
      value: 27.5195
    - type: nauc_ndcg_at_1000_std
      value: -5.0668999999999995
    - type: nauc_ndcg_at_1000_diff1
      value: 46.381499999999996
    - type: nauc_map_at_1_max
      value: 26.6036
    - type: nauc_map_at_1_std
      value: -8.3972
    - type: nauc_map_at_1_diff1
      value: 52.43560000000001
    - type: nauc_map_at_3_max
      value: 28.098699999999997
    - type: nauc_map_at_3_std
      value: -6.357500000000001
    - type: nauc_map_at_3_diff1
      value: 48.4799
    - type: nauc_map_at_5_max
      value: 27.938000000000002
    - type: nauc_map_at_5_std
      value: -6.3283000000000005
    - type: nauc_map_at_5_diff1
      value: 47.955799999999996
    - type: nauc_map_at_10_max
      value: 27.6989
    - type: nauc_map_at_10_std
      value: -6.3546000000000005
    - type: nauc_map_at_10_diff1
      value: 47.7813
    - type: nauc_map_at_20_max
      value: 27.637099999999997
    - type: nauc_map_at_20_std
      value: -6.3278
    - type: nauc_map_at_20_diff1
      value: 47.8258
    - type: nauc_map_at_100_max
      value: 27.6654
    - type: nauc_map_at_100_std
      value: -6.284199999999999
    - type: nauc_map_at_100_diff1
      value: 47.8675
    - type: nauc_map_at_1000_max
      value: 27.668599999999998
    - type: nauc_map_at_1000_std
      value: -6.2727
    - type: nauc_map_at_1000_diff1
      value: 47.8793
    - type: nauc_recall_at_1_max
      value: 26.6036
    - type: nauc_recall_at_1_std
      value: -8.3972
    - type: nauc_recall_at_1_diff1
      value: 52.43560000000001
    - type: nauc_recall_at_3_max
      value: 29.686600000000002
    - type: nauc_recall_at_3_std
      value: -3.7178999999999998
    - type: nauc_recall_at_3_diff1
      value: 43.3556
    - type: nauc_recall_at_5_max
      value: 28.835499999999996
    - type: nauc_recall_at_5_std
      value: -3.6023
    - type: nauc_recall_at_5_diff1
      value: 40.7246
    - type: nauc_recall_at_10_max
      value: 26.6593
    - type: nauc_recall_at_10_std
      value: -3.5498000000000003
    - type: nauc_recall_at_10_diff1
      value: 38.6728
    - type: nauc_recall_at_20_max
      value: 26.293499999999998
    - type: nauc_recall_at_20_std
      value: -2.3813
    - type: nauc_recall_at_20_diff1
      value: 38.8857
    - type: nauc_recall_at_100_max
      value: 24.7411
    - type: nauc_recall_at_100_std
      value: 0.1296
    - type: nauc_recall_at_100_diff1
      value: 38.1683
    - type: nauc_recall_at_1000_max
      value: 25.1934
    - type: nauc_recall_at_1000_std
      value: 10.7766
    - type: nauc_recall_at_1000_diff1
      value: 35.856300000000005
    - type: nauc_precision_at_1_max
      value: 26.6036
    - type: nauc_precision_at_1_std
      value: -8.3972
    - type: nauc_precision_at_1_diff1
      value: 52.43560000000001
    - type: nauc_precision_at_3_max
      value: 29.686600000000002
    - type: nauc_precision_at_3_std
      value: -3.7178999999999998
    - type: nauc_precision_at_3_diff1
      value: 43.3556
    - type: nauc_precision_at_5_max
      value: 28.835499999999996
    - type: nauc_precision_at_5_std
      value: -3.6023
    - type: nauc_precision_at_5_diff1
      value: 40.7246
    - type: nauc_precision_at_10_max
      value: 26.6593
    - type: nauc_precision_at_10_std
      value: -3.5498000000000003
    - type: nauc_precision_at_10_diff1
      value: 38.6728
    - type: nauc_precision_at_20_max
      value: 26.293499999999998
    - type: nauc_precision_at_20_std
      value: -2.3813
    - type: nauc_precision_at_20_diff1
      value: 38.8857
    - type: nauc_precision_at_100_max
      value: 24.7411
    - type: nauc_precision_at_100_std
      value: 0.1296
    - type: nauc_precision_at_100_diff1
      value: 38.1683
    - type: nauc_precision_at_1000_max
      value: 25.1934
    - type: nauc_precision_at_1000_std
      value: 10.7766
    - type: nauc_precision_at_1000_diff1
      value: 35.856300000000005
    - type: nauc_mrr_at_1_max
      value: 26.7351
    - type: nauc_mrr_at_1_std
      value: -8.2798
    - type: nauc_mrr_at_1_diff1
      value: 52.7186
    - type: nauc_mrr_at_3_max
      value: 28.1671
    - type: nauc_mrr_at_3_std
      value: -6.3235
    - type: nauc_mrr_at_3_diff1
      value: 48.6387
    - type: nauc_mrr_at_5_max
      value: 28.0115
    - type: nauc_mrr_at_5_std
      value: -6.256399999999999
    - type: nauc_mrr_at_5_diff1
      value: 48.098400000000005
    - type: nauc_mrr_at_10_max
      value: 27.7729
    - type: nauc_mrr_at_10_std
      value: -6.2821
    - type: nauc_mrr_at_10_diff1
      value: 47.925000000000004
    - type: nauc_mrr_at_20_max
      value: 27.7115
    - type: nauc_mrr_at_20_std
      value: -6.254899999999999
    - type: nauc_mrr_at_20_diff1
      value: 47.9703
    - type: nauc_mrr_at_100_max
      value: 27.740199999999998
    - type: nauc_mrr_at_100_std
      value: -6.2109
    - type: nauc_mrr_at_100_diff1
      value: 48.0128
    - type: nauc_mrr_at_1000_max
      value: 27.743499999999997
    - type: nauc_mrr_at_1000_std
      value: -6.1993
    - type: nauc_mrr_at_1000_diff1
      value: 48.0248
    - type: main_score
      value: 46.024
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB CodeSearchNetCCRetrieval (go)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 26.471
    - type: ndcg_at_3
      value: 33.489999999999995
    - type: ndcg_at_5
      value: 35.55
    - type: ndcg_at_10
      value: 37.555
    - type: ndcg_at_20
      value: 39.029
    - type: ndcg_at_100
      value: 41.478
    - type: ndcg_at_1000
      value: 43.457
    - type: map_at_1
      value: 26.471
    - type: map_at_3
      value: 31.774
    - type: map_at_5
      value: 32.915
    - type: map_at_10
      value: 33.745999999999995
    - type: map_at_20
      value: 34.150000000000006
    - type: map_at_100
      value: 34.477999999999994
    - type: map_at_1000
      value: 34.544000000000004
    - type: recall_at_1
      value: 26.471
    - type: recall_at_3
      value: 38.451
    - type: recall_at_5
      value: 43.462
    - type: recall_at_10
      value: 49.643
    - type: recall_at_20
      value: 55.479
    - type: recall_at_100
      value: 68.825
    - type: recall_at_1000
      value: 84.93
    - type: precision_at_1
      value: 26.471
    - type: precision_at_3
      value: 12.817
    - type: precision_at_5
      value: 8.692
    - type: precision_at_10
      value: 4.9639999999999995
    - type: precision_at_20
      value: 2.774
    - type: precision_at_100
      value: 0.688
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: mrr_at_1
      value: 26.459
    - type: mrr_at_3
      value: 31.757400000000004
    - type: mrr_at_5
      value: 32.9092
    - type: mrr_at_10
      value: 33.7387
    - type: mrr_at_20
      value: 34.1428
    - type: mrr_at_100
      value: 34.471000000000004
    - type: mrr_at_1000
      value: 34.5364
    - type: nauc_ndcg_at_1_max
      value: 29.408299999999997
    - type: nauc_ndcg_at_1_std
      value: 1.5685
    - type: nauc_ndcg_at_1_diff1
      value: 45.834599999999995
    - type: nauc_ndcg_at_3_max
      value: 27.7526
    - type: nauc_ndcg_at_3_std
      value: -0.43810000000000004
    - type: nauc_ndcg_at_3_diff1
      value: 41.272999999999996
    - type: nauc_ndcg_at_5_max
      value: 27.2864
    - type: nauc_ndcg_at_5_std
      value: -0.37820000000000004
    - type: nauc_ndcg_at_5_diff1
      value: 40.4934
    - type: nauc_ndcg_at_10_max
      value: 26.845599999999997
    - type: nauc_ndcg_at_10_std
      value: -0.3317
    - type: nauc_ndcg_at_10_diff1
      value: 39.9305
    - type: nauc_ndcg_at_20_max
      value: 26.4669
    - type: nauc_ndcg_at_20_std
      value: 0.1423
    - type: nauc_ndcg_at_20_diff1
      value: 39.432
    - type: nauc_ndcg_at_100_max
      value: 26.3318
    - type: nauc_ndcg_at_100_std
      value: 0.8049000000000001
    - type: nauc_ndcg_at_100_diff1
      value: 39.0276
    - type: nauc_ndcg_at_1000_max
      value: 26.5895
    - type: nauc_ndcg_at_1000_std
      value: 1.0204
    - type: nauc_ndcg_at_1000_diff1
      value: 39.2747
    - type: nauc_map_at_1_max
      value: 29.408299999999997
    - type: nauc_map_at_1_std
      value: 1.5685
    - type: nauc_map_at_1_diff1
      value: 45.834599999999995
    - type: nauc_map_at_3_max
      value: 28.1245
    - type: nauc_map_at_3_std
      value: -0.006999999999999999
    - type: nauc_map_at_3_diff1
      value: 42.2701
    - type: nauc_map_at_5_max
      value: 27.8563
    - type: nauc_map_at_5_std
      value: 0.0204
    - type: nauc_map_at_5_diff1
      value: 41.8294
    - type: nauc_map_at_10_max
      value: 27.6709
    - type: nauc_map_at_10_std
      value: 0.0262
    - type: nauc_map_at_10_diff1
      value: 41.5973
    - type: nauc_map_at_20_max
      value: 27.572000000000003
    - type: nauc_map_at_20_std
      value: 0.1652
    - type: nauc_map_at_20_diff1
      value: 41.4683
    - type: nauc_map_at_100_max
      value: 27.5573
    - type: nauc_map_at_100_std
      value: 0.243
    - type: nauc_map_at_100_diff1
      value: 41.4201
    - type: nauc_map_at_1000_max
      value: 27.5663
    - type: nauc_map_at_1000_std
      value: 0.254
    - type: nauc_map_at_1000_diff1
      value: 41.4275
    - type: nauc_recall_at_1_max
      value: 29.408299999999997
    - type: nauc_recall_at_1_std
      value: 1.5685
    - type: nauc_recall_at_1_diff1
      value: 45.834599999999995
    - type: nauc_recall_at_3_max
      value: 26.737499999999997
    - type: nauc_recall_at_3_std
      value: -1.6067999999999998
    - type: nauc_recall_at_3_diff1
      value: 38.5628
    - type: nauc_recall_at_5_max
      value: 25.6664
    - type: nauc_recall_at_5_std
      value: -1.4459
    - type: nauc_recall_at_5_diff1
      value: 36.7369
    - type: nauc_recall_at_10_max
      value: 24.3156
    - type: nauc_recall_at_10_std
      value: -1.25
    - type: nauc_recall_at_10_diff1
      value: 34.959
    - type: nauc_recall_at_20_max
      value: 22.6187
    - type: nauc_recall_at_20_std
      value: 0.5539
    - type: nauc_recall_at_20_diff1
      value: 32.634299999999996
    - type: nauc_recall_at_100_max
      value: 20.8069
    - type: nauc_recall_at_100_std
      value: 5.2502
    - type: nauc_recall_at_100_diff1
      value: 28.3304
    - type: nauc_recall_at_1000_max
      value: 20.8473
    - type: nauc_recall_at_1000_std
      value: 12.2405
    - type: nauc_recall_at_1000_diff1
      value: 24.2366
    - type: nauc_precision_at_1_max
      value: 29.408299999999997
    - type: nauc_precision_at_1_std
      value: 1.5685
    - type: nauc_precision_at_1_diff1
      value: 45.834599999999995
    - type: nauc_precision_at_3_max
      value: 26.737499999999997
    - type: nauc_precision_at_3_std
      value: -1.6067999999999998
    - type: nauc_precision_at_3_diff1
      value: 38.5628
    - type: nauc_precision_at_5_max
      value: 25.6664
    - type: nauc_precision_at_5_std
      value: -1.4459
    - type: nauc_precision_at_5_diff1
      value: 36.7369
    - type: nauc_precision_at_10_max
      value: 24.3156
    - type: nauc_precision_at_10_std
      value: -1.25
    - type: nauc_precision_at_10_diff1
      value: 34.959
    - type: nauc_precision_at_20_max
      value: 22.6187
    - type: nauc_precision_at_20_std
      value: 0.5539
    - type: nauc_precision_at_20_diff1
      value: 32.634299999999996
    - type: nauc_precision_at_100_max
      value: 20.8069
    - type: nauc_precision_at_100_std
      value: 5.2502
    - type: nauc_precision_at_100_diff1
      value: 28.3304
    - type: nauc_precision_at_1000_max
      value: 20.8473
    - type: nauc_precision_at_1000_std
      value: 12.2405
    - type: nauc_precision_at_1000_diff1
      value: 24.2366
    - type: nauc_mrr_at_1_max
      value: 29.435499999999998
    - type: nauc_mrr_at_1_std
      value: 1.5623
    - type: nauc_mrr_at_1_diff1
      value: 45.8822
    - type: nauc_mrr_at_3_max
      value: 28.183000000000003
    - type: nauc_mrr_at_3_std
      value: -0.00039999999999999996
    - type: nauc_mrr_at_3_diff1
      value: 42.2776
    - type: nauc_mrr_at_5_max
      value: 27.8735
    - type: nauc_mrr_at_5_std
      value: 0.0288
    - type: nauc_mrr_at_5_diff1
      value: 41.827999999999996
    - type: nauc_mrr_at_10_max
      value: 27.6989
    - type: nauc_mrr_at_10_std
      value: 0.0349
    - type: nauc_mrr_at_10_diff1
      value: 41.6043
    - type: nauc_mrr_at_20_max
      value: 27.599
    - type: nauc_mrr_at_20_std
      value: 0.1719
    - type: nauc_mrr_at_20_diff1
      value: 41.4786
    - type: nauc_mrr_at_100_max
      value: 27.5846
    - type: nauc_mrr_at_100_std
      value: 0.25
    - type: nauc_mrr_at_100_diff1
      value: 41.4307
    - type: nauc_mrr_at_1000_max
      value: 27.5937
    - type: nauc_mrr_at_1000_std
      value: 0.261
    - type: nauc_mrr_at_1000_diff1
      value: 41.4381
    - type: main_score
      value: 37.555
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB CodeSearchNetCCRetrieval (ruby)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 36.003
    - type: ndcg_at_3
      value: 43.306
    - type: ndcg_at_5
      value: 45.443
    - type: ndcg_at_10
      value: 47.549
    - type: ndcg_at_20
      value: 48.872
    - type: ndcg_at_100
      value: 50.651
    - type: ndcg_at_1000
      value: 52.406
    - type: map_at_1
      value: 36.003
    - type: map_at_3
      value: 41.501
    - type: map_at_5
      value: 42.695
    - type: map_at_10
      value: 43.580999999999996
    - type: map_at_20
      value: 43.954
    - type: map_at_100
      value: 44.195
    - type: map_at_1000
      value: 44.255
    - type: recall_at_1
      value: 36.003
    - type: recall_at_3
      value: 48.533
    - type: recall_at_5
      value: 53.688
    - type: recall_at_10
      value: 60.111000000000004
    - type: recall_at_20
      value: 65.266
    - type: recall_at_100
      value: 74.941
    - type: recall_at_1000
      value: 89.056
    - type: precision_at_1
      value: 36.003
    - type: precision_at_3
      value: 16.178
    - type: precision_at_5
      value: 10.738
    - type: precision_at_10
      value: 6.010999999999999
    - type: precision_at_20
      value: 3.263
    - type: precision_at_100
      value: 0.749
    - type: precision_at_1000
      value: 0.089
    - type: mrr_at_1
      value: 36.0032
    - type: mrr_at_3
      value: 41.5015
    - type: mrr_at_5
      value: 42.695
    - type: mrr_at_10
      value: 43.580600000000004
    - type: mrr_at_20
      value: 43.9543
    - type: mrr_at_100
      value: 44.195299999999996
    - type: mrr_at_1000
      value: 44.255
    - type: nauc_ndcg_at_1_max
      value: 32.9994
    - type: nauc_ndcg_at_1_std
      value: -12.2575
    - type: nauc_ndcg_at_1_diff1
      value: 55.63360000000001
    - type: nauc_ndcg_at_3_max
      value: 33.314899999999994
    - type: nauc_ndcg_at_3_std
      value: -11.4208
    - type: nauc_ndcg_at_3_diff1
      value: 50.995599999999996
    - type: nauc_ndcg_at_5_max
      value: 33.1612
    - type: nauc_ndcg_at_5_std
      value: -11.4067
    - type: nauc_ndcg_at_5_diff1
      value: 50.766999999999996
    - type: nauc_ndcg_at_10_max
      value: 32.903999999999996
    - type: nauc_ndcg_at_10_std
      value: -11.447000000000001
    - type: nauc_ndcg_at_10_diff1
      value: 50.1061
    - type: nauc_ndcg_at_20_max
      value: 32.8849
    - type: nauc_ndcg_at_20_std
      value: -11.4567
    - type: nauc_ndcg_at_20_diff1
      value: 50.0131
    - type: nauc_ndcg_at_100_max
      value: 32.5449
    - type: nauc_ndcg_at_100_std
      value: -11.0686
    - type: nauc_ndcg_at_100_diff1
      value: 49.7046
    - type: nauc_ndcg_at_1000_max
      value: 32.7575
    - type: nauc_ndcg_at_1000_std
      value: -10.9682
    - type: nauc_ndcg_at_1000_diff1
      value: 50.17359999999999
    - type: nauc_map_at_1_max
      value: 32.9994
    - type: nauc_map_at_1_std
      value: -12.2575
    - type: nauc_map_at_1_diff1
      value: 55.63360000000001
    - type: nauc_map_at_3_max
      value: 33.2746
    - type: nauc_map_at_3_std
      value: -11.5215
    - type: nauc_map_at_3_diff1
      value: 52.1439
    - type: nauc_map_at_5_max
      value: 33.206799999999994
    - type: nauc_map_at_5_std
      value: -11.533
    - type: nauc_map_at_5_diff1
      value: 52.0477
    - type: nauc_map_at_10_max
      value: 33.1113
    - type: nauc_map_at_10_std
      value: -11.5406
    - type: nauc_map_at_10_diff1
      value: 51.8103
    - type: nauc_map_at_20_max
      value: 33.070899999999995
    - type: nauc_map_at_20_std
      value: -11.5655
    - type: nauc_map_at_20_diff1
      value: 51.7759
    - type: nauc_map_at_100_max
      value: 32.9989
    - type: nauc_map_at_100_std
      value: -11.546
    - type: nauc_map_at_100_diff1
      value: 51.739000000000004
    - type: nauc_map_at_1000_max
      value: 33.0074
    - type: nauc_map_at_1000_std
      value: -11.541
    - type: nauc_map_at_1000_diff1
      value: 51.7548
    - type: nauc_recall_at_1_max
      value: 32.9994
    - type: nauc_recall_at_1_std
      value: -12.2575
    - type: nauc_recall_at_1_diff1
      value: 55.63360000000001
    - type: nauc_recall_at_3_max
      value: 33.4172
    - type: nauc_recall_at_3_std
      value: -11.1701
    - type: nauc_recall_at_3_diff1
      value: 47.6442
    - type: nauc_recall_at_5_max
      value: 32.962799999999994
    - type: nauc_recall_at_5_std
      value: -11.0448
    - type: nauc_recall_at_5_diff1
      value: 46.8433
    - type: nauc_recall_at_10_max
      value: 32.042500000000004
    - type: nauc_recall_at_10_std
      value: -11.2125
    - type: nauc_recall_at_10_diff1
      value: 44.2396
    - type: nauc_recall_at_20_max
      value: 32.1997
    - type: nauc_recall_at_20_std
      value: -11.0222
    - type: nauc_recall_at_20_diff1
      value: 43.4014
    - type: nauc_recall_at_100_max
      value: 29.972500000000004
    - type: nauc_recall_at_100_std
      value: -7.2572
    - type: nauc_recall_at_100_diff1
      value: 39.285199999999996
    - type: nauc_recall_at_1000_max
      value: 31.759300000000003
    - type: nauc_recall_at_1000_std
      value: -1.555
    - type: nauc_recall_at_1000_diff1
      value: 38.7819
    - type: nauc_precision_at_1_max
      value: 32.9994
    - type: nauc_precision_at_1_std
      value: -12.2575
    - type: nauc_precision_at_1_diff1
      value: 55.63360000000001
    - type: nauc_precision_at_3_max
      value: 33.4172
    - type: nauc_precision_at_3_std
      value: -11.1701
    - type: nauc_precision_at_3_diff1
      value: 47.6442
    - type: nauc_precision_at_5_max
      value: 32.962799999999994
    - type: nauc_precision_at_5_std
      value: -11.0448
    - type: nauc_precision_at_5_diff1
      value: 46.8433
    - type: nauc_precision_at_10_max
      value: 32.042500000000004
    - type: nauc_precision_at_10_std
      value: -11.2125
    - type: nauc_precision_at_10_diff1
      value: 44.2396
    - type: nauc_precision_at_20_max
      value: 32.1997
    - type: nauc_precision_at_20_std
      value: -11.0222
    - type: nauc_precision_at_20_diff1
      value: 43.4014
    - type: nauc_precision_at_100_max
      value: 29.972500000000004
    - type: nauc_precision_at_100_std
      value: -7.2572
    - type: nauc_precision_at_100_diff1
      value: 39.285199999999996
    - type: nauc_precision_at_1000_max
      value: 31.759300000000003
    - type: nauc_precision_at_1000_std
      value: -1.555
    - type: nauc_precision_at_1000_diff1
      value: 38.7819
    - type: nauc_mrr_at_1_max
      value: 33.1174
    - type: nauc_mrr_at_1_std
      value: -12.0388
    - type: nauc_mrr_at_1_diff1
      value: 55.63360000000001
    - type: nauc_mrr_at_3_max
      value: 33.333800000000004
    - type: nauc_mrr_at_3_std
      value: -11.4119
    - type: nauc_mrr_at_3_diff1
      value: 52.1439
    - type: nauc_mrr_at_5_max
      value: 33.2665
    - type: nauc_mrr_at_5_std
      value: -11.4223
    - type: nauc_mrr_at_5_diff1
      value: 52.0477
    - type: nauc_mrr_at_10_max
      value: 33.1716
    - type: nauc_mrr_at_10_std
      value: -11.4289
    - type: nauc_mrr_at_10_diff1
      value: 51.8103
    - type: nauc_mrr_at_20_max
      value: 33.1315
    - type: nauc_mrr_at_20_std
      value: -11.4531
    - type: nauc_mrr_at_20_diff1
      value: 51.7759
    - type: nauc_mrr_at_100_max
      value: 33.0598
    - type: nauc_mrr_at_100_std
      value: -11.4331
    - type: nauc_mrr_at_100_diff1
      value: 51.739000000000004
    - type: nauc_mrr_at_1000_max
      value: 33.0684
    - type: nauc_mrr_at_1000_std
      value: -11.428
    - type: nauc_mrr_at_1000_diff1
      value: 51.7548
    - type: main_score
      value: 47.549
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB CodeSearchNetCCRetrieval (java)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 33.355000000000004
    - type: ndcg_at_3
      value: 41.551
    - type: ndcg_at_5
      value: 43.592
    - type: ndcg_at_10
      value: 45.539
    - type: ndcg_at_20
      value: 46.922999999999995
    - type: ndcg_at_100
      value: 49.01
    - type: ndcg_at_1000
      value: 50.592000000000006
    - type: map_at_1
      value: 33.355000000000004
    - type: map_at_3
      value: 39.582
    - type: map_at_5
      value: 40.716
    - type: map_at_10
      value: 41.524
    - type: map_at_20
      value: 41.905
    - type: map_at_100
      value: 42.185
    - type: map_at_1000
      value: 42.239
    - type: recall_at_1
      value: 33.355000000000004
    - type: recall_at_3
      value: 47.23
    - type: recall_at_5
      value: 52.17699999999999
    - type: recall_at_10
      value: 58.17400000000001
    - type: recall_at_20
      value: 63.641999999999996
    - type: recall_at_100
      value: 75.034
    - type: recall_at_1000
      value: 87.85
    - type: precision_at_1
      value: 33.355000000000004
    - type: precision_at_3
      value: 15.742999999999999
    - type: precision_at_5
      value: 10.435
    - type: precision_at_10
      value: 5.817
    - type: precision_at_20
      value: 3.182
    - type: precision_at_100
      value: 0.75
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 33.3455
    - type: mrr_at_3
      value: 39.569500000000005
    - type: mrr_at_5
      value: 40.7055
    - type: mrr_at_10
      value: 41.5123
    - type: mrr_at_20
      value: 41.8948
    - type: mrr_at_100
      value: 42.175200000000004
    - type: mrr_at_1000
      value: 42.228500000000004
    - type: nauc_ndcg_at_1_max
      value: 29.177500000000002
    - type: nauc_ndcg_at_1_std
      value: -5.8229999999999995
    - type: nauc_ndcg_at_1_diff1
      value: 53.2548
    - type: nauc_ndcg_at_3_max
      value: 31.0728
    - type: nauc_ndcg_at_3_std
      value: -4.3403
    - type: nauc_ndcg_at_3_diff1
      value: 48.6597
    - type: nauc_ndcg_at_5_max
      value: 30.9135
    - type: nauc_ndcg_at_5_std
      value: -3.5812999999999997
    - type: nauc_ndcg_at_5_diff1
      value: 47.6076
    - type: nauc_ndcg_at_10_max
      value: 30.662899999999997
    - type: nauc_ndcg_at_10_std
      value: -3.3078999999999996
    - type: nauc_ndcg_at_10_diff1
      value: 46.9647
    - type: nauc_ndcg_at_20_max
      value: 30.7534
    - type: nauc_ndcg_at_20_std
      value: -2.6957
    - type: nauc_ndcg_at_20_diff1
      value: 46.6956
    - type: nauc_ndcg_at_100_max
      value: 30.8268
    - type: nauc_ndcg_at_100_std
      value: -1.9675000000000002
    - type: nauc_ndcg_at_100_diff1
      value: 46.4854
    - type: nauc_ndcg_at_1000_max
      value: 30.7713
    - type: nauc_ndcg_at_1000_std
      value: -1.9892
    - type: nauc_ndcg_at_1000_diff1
      value: 46.7157
    - type: nauc_map_at_1_max
      value: 29.177500000000002
    - type: nauc_map_at_1_std
      value: -5.8229999999999995
    - type: nauc_map_at_1_diff1
      value: 53.2548
    - type: nauc_map_at_3_max
      value: 30.6136
    - type: nauc_map_at_3_std
      value: -4.7136
    - type: nauc_map_at_3_diff1
      value: 49.709399999999995
    - type: nauc_map_at_5_max
      value: 30.523699999999998
    - type: nauc_map_at_5_std
      value: -4.288200000000001
    - type: nauc_map_at_5_diff1
      value: 49.127700000000004
    - type: nauc_map_at_10_max
      value: 30.4224
    - type: nauc_map_at_10_std
      value: -4.1822
    - type: nauc_map_at_10_diff1
      value: 48.8812
    - type: nauc_map_at_20_max
      value: 30.4446
    - type: nauc_map_at_20_std
      value: -4.0194
    - type: nauc_map_at_20_diff1
      value: 48.8177
    - type: nauc_map_at_100_max
      value: 30.4531
    - type: nauc_map_at_100_std
      value: -3.9356
    - type: nauc_map_at_100_diff1
      value: 48.7971
    - type: nauc_map_at_1000_max
      value: 30.4507
    - type: nauc_map_at_1000_std
      value: -3.9337999999999997
    - type: nauc_map_at_1000_diff1
      value: 48.8055
    - type: nauc_recall_at_1_max
      value: 29.177500000000002
    - type: nauc_recall_at_1_std
      value: -5.8229999999999995
    - type: nauc_recall_at_1_diff1
      value: 53.2548
    - type: nauc_recall_at_3_max
      value: 32.3983
    - type: nauc_recall_at_3_std
      value: -3.2567
    - type: nauc_recall_at_3_diff1
      value: 45.6552
    - type: nauc_recall_at_5_max
      value: 32.043
    - type: nauc_recall_at_5_std
      value: -1.3823
    - type: nauc_recall_at_5_diff1
      value: 42.9898
    - type: nauc_recall_at_10_max
      value: 31.272
    - type: nauc_recall_at_10_std
      value: -0.3417
    - type: nauc_recall_at_10_diff1
      value: 40.5539
    - type: nauc_recall_at_20_max
      value: 31.7395
    - type: nauc_recall_at_20_std
      value: 2.645
    - type: nauc_recall_at_20_diff1
      value: 38.777499999999996
    - type: nauc_recall_at_100_max
      value: 32.6198
    - type: nauc_recall_at_100_std
      value: 10.1172
    - type: nauc_recall_at_100_diff1
      value: 34.6806
    - type: nauc_recall_at_1000_max
      value: 33.0633
    - type: nauc_recall_at_1000_std
      value: 19.5697
    - type: nauc_recall_at_1000_diff1
      value: 29.418699999999998
    - type: nauc_precision_at_1_max
      value: 29.177500000000002
    - type: nauc_precision_at_1_std
      value: -5.8229999999999995
    - type: nauc_precision_at_1_diff1
      value: 53.2548
    - type: nauc_precision_at_3_max
      value: 32.3983
    - type: nauc_precision_at_3_std
      value: -3.2567
    - type: nauc_precision_at_3_diff1
      value: 45.6552
    - type: nauc_precision_at_5_max
      value: 32.043
    - type: nauc_precision_at_5_std
      value: -1.3823
    - type: nauc_precision_at_5_diff1
      value: 42.9898
    - type: nauc_precision_at_10_max
      value: 31.272
    - type: nauc_precision_at_10_std
      value: -0.3417
    - type: nauc_precision_at_10_diff1
      value: 40.5539
    - type: nauc_precision_at_20_max
      value: 31.7395
    - type: nauc_precision_at_20_std
      value: 2.645
    - type: nauc_precision_at_20_diff1
      value: 38.777499999999996
    - type: nauc_precision_at_100_max
      value: 32.6198
    - type: nauc_precision_at_100_std
      value: 10.1172
    - type: nauc_precision_at_100_diff1
      value: 34.6806
    - type: nauc_precision_at_1000_max
      value: 33.0633
    - type: nauc_precision_at_1000_std
      value: 19.5697
    - type: nauc_precision_at_1000_diff1
      value: 29.418699999999998
    - type: nauc_mrr_at_1_max
      value: 29.217900000000004
    - type: nauc_mrr_at_1_std
      value: -5.8532
    - type: nauc_mrr_at_1_diff1
      value: 53.283100000000005
    - type: nauc_mrr_at_3_max
      value: 30.6327
    - type: nauc_mrr_at_3_std
      value: -4.7439
    - type: nauc_mrr_at_3_diff1
      value: 49.7477
    - type: nauc_mrr_at_5_max
      value: 30.5427
    - type: nauc_mrr_at_5_std
      value: -4.3167
    - type: nauc_mrr_at_5_diff1
      value: 49.152
    - type: nauc_mrr_at_10_max
      value: 30.444100000000002
    - type: nauc_mrr_at_10_std
      value: -4.2066
    - type: nauc_mrr_at_10_diff1
      value: 48.9038
    - type: nauc_mrr_at_20_max
      value: 30.462899999999998
    - type: nauc_mrr_at_20_std
      value: -4.0467
    - type: nauc_mrr_at_20_diff1
      value: 48.8397
    - type: nauc_mrr_at_100_max
      value: 30.4714
    - type: nauc_mrr_at_100_std
      value: -3.963
    - type: nauc_mrr_at_100_diff1
      value: 48.8192
    - type: nauc_mrr_at_1000_max
      value: 30.469
    - type: nauc_mrr_at_1000_std
      value: -3.9613
    - type: nauc_mrr_at_1000_diff1
      value: 48.8277
    - type: main_score
      value: 45.539
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB CodeSearchNetCCRetrieval (php)
      revision: 6e1effa2c03723c5fde48ee912b5ee08d4f211e8
      split: test
      type: CoIR-Retrieval/CodeSearchNet-ccr
    metrics:
    - type: ndcg_at_1
      value: 25.139
    - type: ndcg_at_3
      value: 31.922
    - type: ndcg_at_5
      value: 33.989999999999995
    - type: ndcg_at_10
      value: 35.942
    - type: ndcg_at_20
      value: 37.506
    - type: ndcg_at_100
      value: 39.971000000000004
    - type: ndcg_at_1000
      value: 42.074
    - type: map_at_1
      value: 25.139
    - type: map_at_3
      value: 30.263
    - type: map_at_5
      value: 31.411
    - type: map_at_10
      value: 32.218
    - type: map_at_20
      value: 32.65
    - type: map_at_100
      value: 32.979
    - type: map_at_1000
      value: 33.050000000000004
    - type: recall_at_1
      value: 25.139
    - type: recall_at_3
      value: 36.720000000000006
    - type: recall_at_5
      value: 41.737
    - type: recall_at_10
      value: 47.766999999999996
    - type: recall_at_20
      value: 53.932
    - type: recall_at_100
      value: 67.38300000000001
    - type: recall_at_1000
      value: 84.416
    - type: precision_at_1
      value: 25.139
    - type: precision_at_3
      value: 12.24
    - type: precision_at_5
      value: 8.347
    - type: precision_at_10
      value: 4.777
    - type: precision_at_20
      value: 2.697
    - type: precision_at_100
      value: 0.674
    - type: precision_at_1000
      value: 0.084
    - type: mrr_at_1
      value: 25.1463
    - type: mrr_at_3
      value: 30.2709
    - type: mrr_at_5
      value: 31.4126
    - type: mrr_at_10
      value: 32.2202
    - type: mrr_at_20
      value: 32.6527
    - type: mrr_at_100
      value: 32.9822
    - type: mrr_at_1000
      value: 33.0527
    - type: nauc_ndcg_at_1_max
      value: 24.082600000000003
    - type: nauc_ndcg_at_1_std
      value: -3.9068
    - type: nauc_ndcg_at_1_diff1
      value: 50.1815
    - type: nauc_ndcg_at_3_max
      value: 23.160700000000002
    - type: nauc_ndcg_at_3_std
      value: -3.3746
    - type: nauc_ndcg_at_3_diff1
      value: 45.009
    - type: nauc_ndcg_at_5_max
      value: 22.644000000000002
    - type: nauc_ndcg_at_5_std
      value: -3.0027999999999997
    - type: nauc_ndcg_at_5_diff1
      value: 44.0016
    - type: nauc_ndcg_at_10_max
      value: 22.3578
    - type: nauc_ndcg_at_10_std
      value: -2.5096
    - type: nauc_ndcg_at_10_diff1
      value: 43.4367
    - type: nauc_ndcg_at_20_max
      value: 22.0477
    - type: nauc_ndcg_at_20_std
      value: -1.7484
    - type: nauc_ndcg_at_20_diff1
      value: 42.9771
    - type: nauc_ndcg_at_100_max
      value: 21.7016
    - type: nauc_ndcg_at_100_std
      value: -1.0854000000000001
    - type: nauc_ndcg_at_100_diff1
      value: 42.707
    - type: nauc_ndcg_at_1000_max
      value: 21.988
    - type: nauc_ndcg_at_1000_std
      value: -0.8564999999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 43.0368
    - type: nauc_map_at_1_max
      value: 24.082600000000003
    - type: nauc_map_at_1_std
      value: -3.9068
    - type: nauc_map_at_1_diff1
      value: 50.1815
    - type: nauc_map_at_3_max
      value: 23.418
    - type: nauc_map_at_3_std
      value: -3.4922
    - type: nauc_map_at_3_diff1
      value: 46.19
    - type: nauc_map_at_5_max
      value: 23.1203
    - type: nauc_map_at_5_std
      value: -3.2856000000000005
    - type: nauc_map_at_5_diff1
      value: 45.6063
    - type: nauc_map_at_10_max
      value: 23.0132
    - type: nauc_map_at_10_std
      value: -3.0803000000000003
    - type: nauc_map_at_10_diff1
      value: 45.3708
    - type: nauc_map_at_20_max
      value: 22.926199999999998
    - type: nauc_map_at_20_std
      value: -2.8717
    - type: nauc_map_at_20_diff1
      value: 45.2482
    - type: nauc_map_at_100_max
      value: 22.8776
    - type: nauc_map_at_100_std
      value: -2.7819
    - type: nauc_map_at_100_diff1
      value: 45.2205
    - type: nauc_map_at_1000_max
      value: 22.886
    - type: nauc_map_at_1000_std
      value: -2.7714
    - type: nauc_map_at_1000_diff1
      value: 45.231300000000005
    - type: nauc_recall_at_1_max
      value: 24.082600000000003
    - type: nauc_recall_at_1_std
      value: -3.9068
    - type: nauc_recall_at_1_diff1
      value: 50.1815
    - type: nauc_recall_at_3_max
      value: 22.442500000000003
    - type: nauc_recall_at_3_std
      value: -3.0562
    - type: nauc_recall_at_3_diff1
      value: 41.797000000000004
    - type: nauc_recall_at_5_max
      value: 21.2749
    - type: nauc_recall_at_5_std
      value: -2.1853000000000002
    - type: nauc_recall_at_5_diff1
      value: 39.543
    - type: nauc_recall_at_10_max
      value: 20.336399999999998
    - type: nauc_recall_at_10_std
      value: -0.6941
    - type: nauc_recall_at_10_diff1
      value: 37.7835
    - type: nauc_recall_at_20_max
      value: 19.031799999999997
    - type: nauc_recall_at_20_std
      value: 2.4044
    - type: nauc_recall_at_20_diff1
      value: 35.6973
    - type: nauc_recall_at_100_max
      value: 16.1657
    - type: nauc_recall_at_100_std
      value: 7.480199999999999
    - type: nauc_recall_at_100_diff1
      value: 32.2845
    - type: nauc_recall_at_1000_max
      value: 16.6175
    - type: nauc_recall_at_1000_std
      value: 17.7626
    - type: nauc_recall_at_1000_diff1
      value: 29.4846
    - type: nauc_precision_at_1_max
      value: 24.082600000000003
    - type: nauc_precision_at_1_std
      value: -3.9068
    - type: nauc_precision_at_1_diff1
      value: 50.1815
    - type: nauc_precision_at_3_max
      value: 22.442500000000003
    - type: nauc_precision_at_3_std
      value: -3.0562
    - type: nauc_precision_at_3_diff1
      value: 41.797000000000004
    - type: nauc_precision_at_5_max
      value: 21.2749
    - type: nauc_precision_at_5_std
      value: -2.1853000000000002
    - type: nauc_precision_at_5_diff1
      value: 39.543
    - type: nauc_precision_at_10_max
      value: 20.336399999999998
    - type: nauc_precision_at_10_std
      value: -0.6941
    - type: nauc_precision_at_10_diff1
      value: 37.7835
    - type: nauc_precision_at_20_max
      value: 19.031799999999997
    - type: nauc_precision_at_20_std
      value: 2.4044
    - type: nauc_precision_at_20_diff1
      value: 35.6973
    - type: nauc_precision_at_100_max
      value: 16.1657
    - type: nauc_precision_at_100_std
      value: 7.480199999999999
    - type: nauc_precision_at_100_diff1
      value: 32.2845
    - type: nauc_precision_at_1000_max
      value: 16.6175
    - type: nauc_precision_at_1000_std
      value: 17.7626
    - type: nauc_precision_at_1000_diff1
      value: 29.4846
    - type: nauc_mrr_at_1_max
      value: 23.9848
    - type: nauc_mrr_at_1_std
      value: -3.9669000000000003
    - type: nauc_mrr_at_1_diff1
      value: 50.152699999999996
    - type: nauc_mrr_at_3_max
      value: 23.3397
    - type: nauc_mrr_at_3_std
      value: -3.5128
    - type: nauc_mrr_at_3_diff1
      value: 46.1227
    - type: nauc_mrr_at_5_max
      value: 23.0454
    - type: nauc_mrr_at_5_std
      value: -3.3141
    - type: nauc_mrr_at_5_diff1
      value: 45.561
    - type: nauc_mrr_at_10_max
      value: 22.9526
    - type: nauc_mrr_at_10_std
      value: -3.1052
    - type: nauc_mrr_at_10_diff1
      value: 45.3316
    - type: nauc_mrr_at_20_max
      value: 22.8654
    - type: nauc_mrr_at_20_std
      value: -2.8967
    - type: nauc_mrr_at_20_diff1
      value: 45.2089
    - type: nauc_mrr_at_100_max
      value: 22.8164
    - type: nauc_mrr_at_100_std
      value: -2.8074000000000003
    - type: nauc_mrr_at_100_diff1
      value: 45.1812
    - type: nauc_mrr_at_1000_max
      value: 22.8248
    - type: nauc_mrr_at_1000_std
      value: -2.7968
    - type: nauc_mrr_at_1000_diff1
      value: 45.191900000000004
    - type: main_score
      value: 35.942
    task:
      type: Retrieval
  - dataset:
      config: python
      name: MTEB CodeSearchNetRetrieval (python)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 70.89999999999999
    - type: ndcg_at_3
      value: 80.06400000000001
    - type: ndcg_at_5
      value: 81.703
    - type: ndcg_at_10
      value: 83.12
    - type: ndcg_at_20
      value: 83.67999999999999
    - type: ndcg_at_100
      value: 84.11
    - type: ndcg_at_1000
      value: 84.195
    - type: map_at_1
      value: 70.89999999999999
    - type: map_at_3
      value: 77.86699999999999
    - type: map_at_5
      value: 78.77199999999999
    - type: map_at_10
      value: 79.353
    - type: map_at_20
      value: 79.508
    - type: map_at_100
      value: 79.569
    - type: map_at_1000
      value: 79.571
    - type: recall_at_1
      value: 70.89999999999999
    - type: recall_at_3
      value: 86.4
    - type: recall_at_5
      value: 90.4
    - type: recall_at_10
      value: 94.8
    - type: recall_at_20
      value: 97.0
    - type: recall_at_100
      value: 99.3
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 70.89999999999999
    - type: precision_at_3
      value: 28.799999999999997
    - type: precision_at_5
      value: 18.08
    - type: precision_at_10
      value: 9.48
    - type: precision_at_20
      value: 4.8500000000000005
    - type: precision_at_100
      value: 0.993
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 70.89999999999999
    - type: mrr_at_3
      value: 77.8667
    - type: mrr_at_5
      value: 78.7717
    - type: mrr_at_10
      value: 79.3526
    - type: mrr_at_20
      value: 79.5084
    - type: mrr_at_100
      value: 79.5687
    - type: mrr_at_1000
      value: 79.5713
    - type: nauc_ndcg_at_1_max
      value: 42.7162
    - type: nauc_ndcg_at_1_std
      value: -4.6818
    - type: nauc_ndcg_at_1_diff1
      value: 70.6364
    - type: nauc_ndcg_at_3_max
      value: 48.1282
    - type: nauc_ndcg_at_3_std
      value: -2.8091
    - type: nauc_ndcg_at_3_diff1
      value: 67.9426
    - type: nauc_ndcg_at_5_max
      value: 45.713
    - type: nauc_ndcg_at_5_std
      value: -4.0022
    - type: nauc_ndcg_at_5_diff1
      value: 67.0684
    - type: nauc_ndcg_at_10_max
      value: 45.8762
    - type: nauc_ndcg_at_10_std
      value: -2.8594999999999997
    - type: nauc_ndcg_at_10_diff1
      value: 67.318
    - type: nauc_ndcg_at_20_max
      value: 45.8448
    - type: nauc_ndcg_at_20_std
      value: -2.9843
    - type: nauc_ndcg_at_20_diff1
      value: 67.5016
    - type: nauc_ndcg_at_100_max
      value: 45.9045
    - type: nauc_ndcg_at_100_std
      value: -3.1647000000000003
    - type: nauc_ndcg_at_100_diff1
      value: 67.8211
    - type: nauc_ndcg_at_1000_max
      value: 45.7011
    - type: nauc_ndcg_at_1000_std
      value: -3.4981
    - type: nauc_ndcg_at_1000_diff1
      value: 67.9137
    - type: nauc_map_at_1_max
      value: 42.7162
    - type: nauc_map_at_1_std
      value: -4.6818
    - type: nauc_map_at_1_diff1
      value: 70.6364
    - type: nauc_map_at_3_max
      value: 46.5287
    - type: nauc_map_at_3_std
      value: -3.6239
    - type: nauc_map_at_3_diff1
      value: 68.5879
    - type: nauc_map_at_5_max
      value: 45.291599999999995
    - type: nauc_map_at_5_std
      value: -4.2172
    - type: nauc_map_at_5_diff1
      value: 68.1788
    - type: nauc_map_at_10_max
      value: 45.31
    - type: nauc_map_at_10_std
      value: -3.8557
    - type: nauc_map_at_10_diff1
      value: 68.2538
    - type: nauc_map_at_20_max
      value: 45.2841
    - type: nauc_map_at_20_std
      value: -3.92
    - type: nauc_map_at_20_diff1
      value: 68.2978
    - type: nauc_map_at_100_max
      value: 45.3154
    - type: nauc_map_at_100_std
      value: -3.929
    - type: nauc_map_at_100_diff1
      value: 68.3362
    - type: nauc_map_at_1000_max
      value: 45.3097
    - type: nauc_map_at_1000_std
      value: -3.9364999999999997
    - type: nauc_map_at_1000_diff1
      value: 68.3376
    - type: nauc_recall_at_1_max
      value: 42.7162
    - type: nauc_recall_at_1_std
      value: -4.6818
    - type: nauc_recall_at_1_diff1
      value: 70.6364
    - type: nauc_recall_at_3_max
      value: 55.0798
    - type: nauc_recall_at_3_std
      value: 0.9014
    - type: nauc_recall_at_3_diff1
      value: 65.2358
    - type: nauc_recall_at_5_max
      value: 47.4148
    - type: nauc_recall_at_5_std
      value: -2.9387
    - type: nauc_recall_at_5_diff1
      value: 60.644299999999994
    - type: nauc_recall_at_10_max
      value: 50.820600000000006
    - type: nauc_recall_at_10_std
      value: 8.7499
    - type: nauc_recall_at_10_diff1
      value: 58.34049999999999
    - type: nauc_recall_at_20_max
      value: 54.4382
    - type: nauc_recall_at_20_std
      value: 16.0862
    - type: nauc_recall_at_20_diff1
      value: 55.5229
    - type: nauc_recall_at_100_max
      value: 79.2317
    - type: nauc_recall_at_100_std
      value: 54.095000000000006
    - type: nauc_recall_at_100_diff1
      value: 50.6869
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 42.7162
    - type: nauc_precision_at_1_std
      value: -4.6818
    - type: nauc_precision_at_1_diff1
      value: 70.6364
    - type: nauc_precision_at_3_max
      value: 55.0798
    - type: nauc_precision_at_3_std
      value: 0.9014
    - type: nauc_precision_at_3_diff1
      value: 65.2358
    - type: nauc_precision_at_5_max
      value: 47.4148
    - type: nauc_precision_at_5_std
      value: -2.9387
    - type: nauc_precision_at_5_diff1
      value: 60.644299999999994
    - type: nauc_precision_at_10_max
      value: 50.820600000000006
    - type: nauc_precision_at_10_std
      value: 8.7499
    - type: nauc_precision_at_10_diff1
      value: 58.34049999999999
    - type: nauc_precision_at_20_max
      value: 54.4382
    - type: nauc_precision_at_20_std
      value: 16.0862
    - type: nauc_precision_at_20_diff1
      value: 55.5229
    - type: nauc_precision_at_100_max
      value: 79.2317
    - type: nauc_precision_at_100_std
      value: 54.095000000000006
    - type: nauc_precision_at_100_diff1
      value: 50.6869
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 42.7162
    - type: nauc_mrr_at_1_std
      value: -4.6818
    - type: nauc_mrr_at_1_diff1
      value: 70.6364
    - type: nauc_mrr_at_3_max
      value: 46.5287
    - type: nauc_mrr_at_3_std
      value: -3.6239
    - type: nauc_mrr_at_3_diff1
      value: 68.5879
    - type: nauc_mrr_at_5_max
      value: 45.291599999999995
    - type: nauc_mrr_at_5_std
      value: -4.2172
    - type: nauc_mrr_at_5_diff1
      value: 68.1788
    - type: nauc_mrr_at_10_max
      value: 45.31
    - type: nauc_mrr_at_10_std
      value: -3.8557
    - type: nauc_mrr_at_10_diff1
      value: 68.2538
    - type: nauc_mrr_at_20_max
      value: 45.2841
    - type: nauc_mrr_at_20_std
      value: -3.92
    - type: nauc_mrr_at_20_diff1
      value: 68.2978
    - type: nauc_mrr_at_100_max
      value: 45.3154
    - type: nauc_mrr_at_100_std
      value: -3.929
    - type: nauc_mrr_at_100_diff1
      value: 68.3362
    - type: nauc_mrr_at_1000_max
      value: 45.3097
    - type: nauc_mrr_at_1000_std
      value: -3.9364999999999997
    - type: nauc_mrr_at_1000_diff1
      value: 68.3376
    - type: main_score
      value: 83.12
    task:
      type: Retrieval
  - dataset:
      config: javascript
      name: MTEB CodeSearchNetRetrieval (javascript)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_3
      value: 67.24900000000001
    - type: ndcg_at_5
      value: 68.781
    - type: ndcg_at_10
      value: 70.34
    - type: ndcg_at_20
      value: 71.24000000000001
    - type: ndcg_at_100
      value: 72.617
    - type: ndcg_at_1000
      value: 73.436
    - type: map_at_1
      value: 57.99999999999999
    - type: map_at_3
      value: 64.983
    - type: map_at_5
      value: 65.838
    - type: map_at_10
      value: 66.50500000000001
    - type: map_at_20
      value: 66.74600000000001
    - type: map_at_100
      value: 66.93299999999999
    - type: map_at_1000
      value: 66.959
    - type: recall_at_1
      value: 57.99999999999999
    - type: recall_at_3
      value: 73.8
    - type: recall_at_5
      value: 77.5
    - type: recall_at_10
      value: 82.19999999999999
    - type: recall_at_20
      value: 85.8
    - type: recall_at_100
      value: 93.30000000000001
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 57.99999999999999
    - type: precision_at_3
      value: 24.6
    - type: precision_at_5
      value: 15.5
    - type: precision_at_10
      value: 8.219999999999999
    - type: precision_at_20
      value: 4.29
    - type: precision_at_100
      value: 0.9329999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 57.99999999999999
    - type: mrr_at_3
      value: 64.9833
    - type: mrr_at_5
      value: 65.8383
    - type: mrr_at_10
      value: 66.50500000000001
    - type: mrr_at_20
      value: 66.7464
    - type: mrr_at_100
      value: 66.9326
    - type: mrr_at_1000
      value: 66.9593
    - type: nauc_ndcg_at_1_max
      value: 51.0918
    - type: nauc_ndcg_at_1_std
      value: 12.0501
    - type: nauc_ndcg_at_1_diff1
      value: 69.1716
    - type: nauc_ndcg_at_3_max
      value: 59.404199999999996
    - type: nauc_ndcg_at_3_std
      value: 22.4787
    - type: nauc_ndcg_at_3_diff1
      value: 66.2602
    - type: nauc_ndcg_at_5_max
      value: 60.711000000000006
    - type: nauc_ndcg_at_5_std
      value: 24.1272
    - type: nauc_ndcg_at_5_diff1
      value: 65.9406
    - type: nauc_ndcg_at_10_max
      value: 61.492599999999996
    - type: nauc_ndcg_at_10_std
      value: 26.6758
    - type: nauc_ndcg_at_10_diff1
      value: 66.1164
    - type: nauc_ndcg_at_20_max
      value: 61.34610000000001
    - type: nauc_ndcg_at_20_std
      value: 27.331
    - type: nauc_ndcg_at_20_diff1
      value: 66.981
    - type: nauc_ndcg_at_100_max
      value: 60.50020000000001
    - type: nauc_ndcg_at_100_std
      value: 26.623
    - type: nauc_ndcg_at_100_diff1
      value: 66.4658
    - type: nauc_ndcg_at_1000_max
      value: 59.600500000000004
    - type: nauc_ndcg_at_1000_std
      value: 24.3596
    - type: nauc_ndcg_at_1000_diff1
      value: 66.7619
    - type: nauc_map_at_1_max
      value: 51.0918
    - type: nauc_map_at_1_std
      value: 12.0501
    - type: nauc_map_at_1_diff1
      value: 69.1716
    - type: nauc_map_at_3_max
      value: 57.2093
    - type: nauc_map_at_3_std
      value: 19.4523
    - type: nauc_map_at_3_diff1
      value: 67.0065
    - type: nauc_map_at_5_max
      value: 57.81699999999999
    - type: nauc_map_at_5_std
      value: 20.2597
    - type: nauc_map_at_5_diff1
      value: 66.8577
    - type: nauc_map_at_10_max
      value: 58.052099999999996
    - type: nauc_map_at_10_std
      value: 21.195
    - type: nauc_map_at_10_diff1
      value: 66.9095
    - type: nauc_map_at_20_max
      value: 57.9955
    - type: nauc_map_at_20_std
      value: 21.3121
    - type: nauc_map_at_20_diff1
      value: 67.1257
    - type: nauc_map_at_100_max
      value: 57.8974
    - type: nauc_map_at_100_std
      value: 21.2576
    - type: nauc_map_at_100_diff1
      value: 67.0765
    - type: nauc_map_at_1000_max
      value: 57.873799999999996
    - type: nauc_map_at_1000_std
      value: 21.195
    - type: nauc_map_at_1000_diff1
      value: 67.08579999999999
    - type: nauc_recall_at_1_max
      value: 51.0918
    - type: nauc_recall_at_1_std
      value: 12.0501
    - type: nauc_recall_at_1_diff1
      value: 69.1716
    - type: nauc_recall_at_3_max
      value: 67.0934
    - type: nauc_recall_at_3_std
      value: 33.2241
    - type: nauc_recall_at_3_diff1
      value: 63.65769999999999
    - type: nauc_recall_at_5_max
      value: 72.2191
    - type: nauc_recall_at_5_std
      value: 39.5657
    - type: nauc_recall_at_5_diff1
      value: 62.3367
    - type: nauc_recall_at_10_max
      value: 78.3358
    - type: nauc_recall_at_10_std
      value: 54.093599999999995
    - type: nauc_recall_at_10_diff1
      value: 62.605900000000005
    - type: nauc_recall_at_20_max
      value: 81.0991
    - type: nauc_recall_at_20_std
      value: 64.9068
    - type: nauc_recall_at_20_diff1
      value: 67.7761
    - type: nauc_recall_at_100_max
      value: 85.0279
    - type: nauc_recall_at_100_std
      value: 87.47930000000001
    - type: nauc_recall_at_100_diff1
      value: 58.818000000000005
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 51.0918
    - type: nauc_precision_at_1_std
      value: 12.0501
    - type: nauc_precision_at_1_diff1
      value: 69.1716
    - type: nauc_precision_at_3_max
      value: 67.0934
    - type: nauc_precision_at_3_std
      value: 33.2241
    - type: nauc_precision_at_3_diff1
      value: 63.65769999999999
    - type: nauc_precision_at_5_max
      value: 72.2191
    - type: nauc_precision_at_5_std
      value: 39.5657
    - type: nauc_precision_at_5_diff1
      value: 62.3367
    - type: nauc_precision_at_10_max
      value: 78.3358
    - type: nauc_precision_at_10_std
      value: 54.093599999999995
    - type: nauc_precision_at_10_diff1
      value: 62.605900000000005
    - type: nauc_precision_at_20_max
      value: 81.0991
    - type: nauc_precision_at_20_std
      value: 64.9068
    - type: nauc_precision_at_20_diff1
      value: 67.7761
    - type: nauc_precision_at_100_max
      value: 85.0279
    - type: nauc_precision_at_100_std
      value: 87.47930000000001
    - type: nauc_precision_at_100_diff1
      value: 58.818000000000005
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 51.0918
    - type: nauc_mrr_at_1_std
      value: 12.0501
    - type: nauc_mrr_at_1_diff1
      value: 69.1716
    - type: nauc_mrr_at_3_max
      value: 57.2093
    - type: nauc_mrr_at_3_std
      value: 19.4523
    - type: nauc_mrr_at_3_diff1
      value: 67.0065
    - type: nauc_mrr_at_5_max
      value: 57.81699999999999
    - type: nauc_mrr_at_5_std
      value: 20.2597
    - type: nauc_mrr_at_5_diff1
      value: 66.8577
    - type: nauc_mrr_at_10_max
      value: 58.052099999999996
    - type: nauc_mrr_at_10_std
      value: 21.195
    - type: nauc_mrr_at_10_diff1
      value: 66.9095
    - type: nauc_mrr_at_20_max
      value: 57.9955
    - type: nauc_mrr_at_20_std
      value: 21.3121
    - type: nauc_mrr_at_20_diff1
      value: 67.1257
    - type: nauc_mrr_at_100_max
      value: 57.8974
    - type: nauc_mrr_at_100_std
      value: 21.2576
    - type: nauc_mrr_at_100_diff1
      value: 67.0765
    - type: nauc_mrr_at_1000_max
      value: 57.873799999999996
    - type: nauc_mrr_at_1000_std
      value: 21.195
    - type: nauc_mrr_at_1000_diff1
      value: 67.08579999999999
    - type: main_score
      value: 70.34
    task:
      type: Retrieval
  - dataset:
      config: go
      name: MTEB CodeSearchNetRetrieval (go)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 75.6
    - type: ndcg_at_3
      value: 84.112
    - type: ndcg_at_5
      value: 85.351
    - type: ndcg_at_10
      value: 86.139
    - type: ndcg_at_20
      value: 86.599
    - type: ndcg_at_100
      value: 86.971
    - type: ndcg_at_1000
      value: 87.086
    - type: map_at_1
      value: 75.6
    - type: map_at_3
      value: 82.1
    - type: map_at_5
      value: 82.78999999999999
    - type: map_at_10
      value: 83.122
    - type: map_at_20
      value: 83.25099999999999
    - type: map_at_100
      value: 83.30300000000001
    - type: map_at_1000
      value: 83.307
    - type: recall_at_1
      value: 75.6
    - type: recall_at_3
      value: 89.9
    - type: recall_at_5
      value: 92.9
    - type: recall_at_10
      value: 95.3
    - type: recall_at_20
      value: 97.1
    - type: recall_at_100
      value: 99.1
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 75.6
    - type: precision_at_3
      value: 29.967
    - type: precision_at_5
      value: 18.58
    - type: precision_at_10
      value: 9.53
    - type: precision_at_20
      value: 4.855
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 75.6
    - type: mrr_at_3
      value: 82.1
    - type: mrr_at_5
      value: 82.78999999999999
    - type: mrr_at_10
      value: 83.12230000000001
    - type: mrr_at_20
      value: 83.2511
    - type: mrr_at_100
      value: 83.3027
    - type: mrr_at_1000
      value: 83.307
    - type: nauc_ndcg_at_1_max
      value: 50.9856
    - type: nauc_ndcg_at_1_std
      value: 6.729
    - type: nauc_ndcg_at_1_diff1
      value: 75.68589999999999
    - type: nauc_ndcg_at_3_max
      value: 59.266
    - type: nauc_ndcg_at_3_std
      value: 10.0957
    - type: nauc_ndcg_at_3_diff1
      value: 73.3044
    - type: nauc_ndcg_at_5_max
      value: 58.7545
    - type: nauc_ndcg_at_5_std
      value: 9.295399999999999
    - type: nauc_ndcg_at_5_diff1
      value: 73.9355
    - type: nauc_ndcg_at_10_max
      value: 58.7538
    - type: nauc_ndcg_at_10_std
      value: 10.335999999999999
    - type: nauc_ndcg_at_10_diff1
      value: 74.01870000000001
    - type: nauc_ndcg_at_20_max
      value: 57.9057
    - type: nauc_ndcg_at_20_std
      value: 10.115300000000001
    - type: nauc_ndcg_at_20_diff1
      value: 74.456
    - type: nauc_ndcg_at_100_max
      value: 57.198800000000006
    - type: nauc_ndcg_at_100_std
      value: 9.2269
    - type: nauc_ndcg_at_100_diff1
      value: 74.2418
    - type: nauc_ndcg_at_1000_max
      value: 57.1141
    - type: nauc_ndcg_at_1000_std
      value: 9.366900000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 74.3329
    - type: nauc_map_at_1_max
      value: 50.9856
    - type: nauc_map_at_1_std
      value: 6.729
    - type: nauc_map_at_1_diff1
      value: 75.68589999999999
    - type: nauc_map_at_3_max
      value: 57.0017
    - type: nauc_map_at_3_std
      value: 9.2059
    - type: nauc_map_at_3_diff1
      value: 73.9956
    - type: nauc_map_at_5_max
      value: 56.6856
    - type: nauc_map_at_5_std
      value: 8.8058
    - type: nauc_map_at_5_diff1
      value: 74.3367
    - type: nauc_map_at_10_max
      value: 56.652100000000004
    - type: nauc_map_at_10_std
      value: 9.1465
    - type: nauc_map_at_10_diff1
      value: 74.37519999999999
    - type: nauc_map_at_20_max
      value: 56.4431
    - type: nauc_map_at_20_std
      value: 9.0962
    - type: nauc_map_at_20_diff1
      value: 74.4763
    - type: nauc_map_at_100_max
      value: 56.3572
    - type: nauc_map_at_100_std
      value: 8.9981
    - type: nauc_map_at_100_diff1
      value: 74.4551
    - type: nauc_map_at_1000_max
      value: 56.3527
    - type: nauc_map_at_1000_std
      value: 9.0022
    - type: nauc_map_at_1000_diff1
      value: 74.4583
    - type: nauc_recall_at_1_max
      value: 50.9856
    - type: nauc_recall_at_1_std
      value: 6.729
    - type: nauc_recall_at_1_diff1
      value: 75.68589999999999
    - type: nauc_recall_at_3_max
      value: 69.7291
    - type: nauc_recall_at_3_std
      value: 14.183000000000002
    - type: nauc_recall_at_3_diff1
      value: 70.07900000000001
    - type: nauc_recall_at_5_max
      value: 71.5009
    - type: nauc_recall_at_5_std
      value: 11.9764
    - type: nauc_recall_at_5_diff1
      value: 71.5765
    - type: nauc_recall_at_10_max
      value: 77.7927
    - type: nauc_recall_at_10_std
      value: 22.2123
    - type: nauc_recall_at_10_diff1
      value: 71.0601
    - type: nauc_recall_at_20_max
      value: 75.421
    - type: nauc_recall_at_20_std
      value: 25.5385
    - type: nauc_recall_at_20_diff1
      value: 76.5318
    - type: nauc_recall_at_100_max
      value: 64.4206
    - type: nauc_recall_at_100_std
      value: -4.8864
    - type: nauc_recall_at_100_diff1
      value: 65.2765
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 50.9856
    - type: nauc_precision_at_1_std
      value: 6.729
    - type: nauc_precision_at_1_diff1
      value: 75.68589999999999
    - type: nauc_precision_at_3_max
      value: 69.7291
    - type: nauc_precision_at_3_std
      value: 14.183000000000002
    - type: nauc_precision_at_3_diff1
      value: 70.07900000000001
    - type: nauc_precision_at_5_max
      value: 71.5009
    - type: nauc_precision_at_5_std
      value: 11.9764
    - type: nauc_precision_at_5_diff1
      value: 71.5765
    - type: nauc_precision_at_10_max
      value: 77.7927
    - type: nauc_precision_at_10_std
      value: 22.2123
    - type: nauc_precision_at_10_diff1
      value: 71.0601
    - type: nauc_precision_at_20_max
      value: 75.421
    - type: nauc_precision_at_20_std
      value: 25.5385
    - type: nauc_precision_at_20_diff1
      value: 76.5318
    - type: nauc_precision_at_100_max
      value: 64.4206
    - type: nauc_precision_at_100_std
      value: -4.8864
    - type: nauc_precision_at_100_diff1
      value: 65.2765
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 50.9856
    - type: nauc_mrr_at_1_std
      value: 6.729
    - type: nauc_mrr_at_1_diff1
      value: 75.68589999999999
    - type: nauc_mrr_at_3_max
      value: 57.0017
    - type: nauc_mrr_at_3_std
      value: 9.2059
    - type: nauc_mrr_at_3_diff1
      value: 73.9956
    - type: nauc_mrr_at_5_max
      value: 56.6856
    - type: nauc_mrr_at_5_std
      value: 8.8058
    - type: nauc_mrr_at_5_diff1
      value: 74.3367
    - type: nauc_mrr_at_10_max
      value: 56.652100000000004
    - type: nauc_mrr_at_10_std
      value: 9.1465
    - type: nauc_mrr_at_10_diff1
      value: 74.37519999999999
    - type: nauc_mrr_at_20_max
      value: 56.4431
    - type: nauc_mrr_at_20_std
      value: 9.0962
    - type: nauc_mrr_at_20_diff1
      value: 74.4763
    - type: nauc_mrr_at_100_max
      value: 56.3572
    - type: nauc_mrr_at_100_std
      value: 8.9981
    - type: nauc_mrr_at_100_diff1
      value: 74.4551
    - type: nauc_mrr_at_1000_max
      value: 56.3527
    - type: nauc_mrr_at_1000_std
      value: 9.0022
    - type: nauc_mrr_at_1000_diff1
      value: 74.4583
    - type: main_score
      value: 86.139
    task:
      type: Retrieval
  - dataset:
      config: ruby
      name: MTEB CodeSearchNetRetrieval (ruby)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 61.3
    - type: ndcg_at_3
      value: 71.232
    - type: ndcg_at_5
      value: 73.1
    - type: ndcg_at_10
      value: 74.736
    - type: ndcg_at_20
      value: 75.511
    - type: ndcg_at_100
      value: 76.416
    - type: ndcg_at_1000
      value: 76.996
    - type: map_at_1
      value: 61.3
    - type: map_at_3
      value: 68.85
    - type: map_at_5
      value: 69.895
    - type: map_at_10
      value: 70.581
    - type: map_at_20
      value: 70.80199999999999
    - type: map_at_100
      value: 70.94200000000001
    - type: map_at_1000
      value: 70.961
    - type: recall_at_1
      value: 61.3
    - type: recall_at_3
      value: 78.10000000000001
    - type: recall_at_5
      value: 82.6
    - type: recall_at_10
      value: 87.6
    - type: recall_at_20
      value: 90.60000000000001
    - type: recall_at_100
      value: 95.3
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 61.3
    - type: precision_at_3
      value: 26.033
    - type: precision_at_5
      value: 16.520000000000003
    - type: precision_at_10
      value: 8.76
    - type: precision_at_20
      value: 4.53
    - type: precision_at_100
      value: 0.9530000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 61.3
    - type: mrr_at_3
      value: 68.85
    - type: mrr_at_5
      value: 69.895
    - type: mrr_at_10
      value: 70.58109999999999
    - type: mrr_at_20
      value: 70.8024
    - type: mrr_at_100
      value: 70.94160000000001
    - type: mrr_at_1000
      value: 70.96090000000001
    - type: nauc_ndcg_at_1_max
      value: 54.2597
    - type: nauc_ndcg_at_1_std
      value: 9.9915
    - type: nauc_ndcg_at_1_diff1
      value: 72.0029
    - type: nauc_ndcg_at_3_max
      value: 58.517799999999994
    - type: nauc_ndcg_at_3_std
      value: 13.256599999999999
    - type: nauc_ndcg_at_3_diff1
      value: 67.861
    - type: nauc_ndcg_at_5_max
      value: 59.1541
    - type: nauc_ndcg_at_5_std
      value: 16.237099999999998
    - type: nauc_ndcg_at_5_diff1
      value: 67.8155
    - type: nauc_ndcg_at_10_max
      value: 59.1703
    - type: nauc_ndcg_at_10_std
      value: 17.8202
    - type: nauc_ndcg_at_10_diff1
      value: 67.6082
    - type: nauc_ndcg_at_20_max
      value: 58.829299999999996
    - type: nauc_ndcg_at_20_std
      value: 18.001900000000003
    - type: nauc_ndcg_at_20_diff1
      value: 67.6747
    - type: nauc_ndcg_at_100_max
      value: 58.675399999999996
    - type: nauc_ndcg_at_100_std
      value: 17.7394
    - type: nauc_ndcg_at_100_diff1
      value: 68.02810000000001
    - type: nauc_ndcg_at_1000_max
      value: 58.333400000000005
    - type: nauc_ndcg_at_1000_std
      value: 16.169900000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 68.3788
    - type: nauc_map_at_1_max
      value: 54.2597
    - type: nauc_map_at_1_std
      value: 9.9915
    - type: nauc_map_at_1_diff1
      value: 72.0029
    - type: nauc_map_at_3_max
      value: 57.4277
    - type: nauc_map_at_3_std
      value: 12.1778
    - type: nauc_map_at_3_diff1
      value: 69.0312
    - type: nauc_map_at_5_max
      value: 57.7291
    - type: nauc_map_at_5_std
      value: 13.655800000000001
    - type: nauc_map_at_5_diff1
      value: 69.0376
    - type: nauc_map_at_10_max
      value: 57.7091
    - type: nauc_map_at_10_std
      value: 14.2236
    - type: nauc_map_at_10_diff1
      value: 68.99849999999999
    - type: nauc_map_at_20_max
      value: 57.605700000000006
    - type: nauc_map_at_20_std
      value: 14.2305
    - type: nauc_map_at_20_diff1
      value: 69.0304
    - type: nauc_map_at_100_max
      value: 57.6007
    - type: nauc_map_at_100_std
      value: 14.219499999999998
    - type: nauc_map_at_100_diff1
      value: 69.0682
    - type: nauc_map_at_1000_max
      value: 57.5939
    - type: nauc_map_at_1000_std
      value: 14.1793
    - type: nauc_map_at_1000_diff1
      value: 69.0767
    - type: nauc_recall_at_1_max
      value: 54.2597
    - type: nauc_recall_at_1_std
      value: 9.9915
    - type: nauc_recall_at_1_diff1
      value: 72.0029
    - type: nauc_recall_at_3_max
      value: 62.5301
    - type: nauc_recall_at_3_std
      value: 17.372799999999998
    - type: nauc_recall_at_3_diff1
      value: 63.488
    - type: nauc_recall_at_5_max
      value: 65.4804
    - type: nauc_recall_at_5_std
      value: 28.376
    - type: nauc_recall_at_5_diff1
      value: 62.4274
    - type: nauc_recall_at_10_max
      value: 67.7459
    - type: nauc_recall_at_10_std
      value: 40.8339
    - type: nauc_recall_at_10_diff1
      value: 59.2704
    - type: nauc_recall_at_20_max
      value: 67.4241
    - type: nauc_recall_at_20_std
      value: 49.1244
    - type: nauc_recall_at_20_diff1
      value: 57.3728
    - type: nauc_recall_at_100_max
      value: 71.1514
    - type: nauc_recall_at_100_std
      value: 71.35510000000001
    - type: nauc_recall_at_100_diff1
      value: 55.964800000000004
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 54.2597
    - type: nauc_precision_at_1_std
      value: 9.9915
    - type: nauc_precision_at_1_diff1
      value: 72.0029
    - type: nauc_precision_at_3_max
      value: 62.5301
    - type: nauc_precision_at_3_std
      value: 17.372799999999998
    - type: nauc_precision_at_3_diff1
      value: 63.488
    - type: nauc_precision_at_5_max
      value: 65.4804
    - type: nauc_precision_at_5_std
      value: 28.376
    - type: nauc_precision_at_5_diff1
      value: 62.4274
    - type: nauc_precision_at_10_max
      value: 67.7459
    - type: nauc_precision_at_10_std
      value: 40.8339
    - type: nauc_precision_at_10_diff1
      value: 59.2704
    - type: nauc_precision_at_20_max
      value: 67.4241
    - type: nauc_precision_at_20_std
      value: 49.1244
    - type: nauc_precision_at_20_diff1
      value: 57.3728
    - type: nauc_precision_at_100_max
      value: 71.1514
    - type: nauc_precision_at_100_std
      value: 71.35510000000001
    - type: nauc_precision_at_100_diff1
      value: 55.964800000000004
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 54.2597
    - type: nauc_mrr_at_1_std
      value: 9.9915
    - type: nauc_mrr_at_1_diff1
      value: 72.0029
    - type: nauc_mrr_at_3_max
      value: 57.4277
    - type: nauc_mrr_at_3_std
      value: 12.1778
    - type: nauc_mrr_at_3_diff1
      value: 69.0312
    - type: nauc_mrr_at_5_max
      value: 57.7291
    - type: nauc_mrr_at_5_std
      value: 13.655800000000001
    - type: nauc_mrr_at_5_diff1
      value: 69.0376
    - type: nauc_mrr_at_10_max
      value: 57.7091
    - type: nauc_mrr_at_10_std
      value: 14.2236
    - type: nauc_mrr_at_10_diff1
      value: 68.99849999999999
    - type: nauc_mrr_at_20_max
      value: 57.605700000000006
    - type: nauc_mrr_at_20_std
      value: 14.2305
    - type: nauc_mrr_at_20_diff1
      value: 69.0304
    - type: nauc_mrr_at_100_max
      value: 57.6007
    - type: nauc_mrr_at_100_std
      value: 14.219499999999998
    - type: nauc_mrr_at_100_diff1
      value: 69.0682
    - type: nauc_mrr_at_1000_max
      value: 57.5939
    - type: nauc_mrr_at_1000_std
      value: 14.1793
    - type: nauc_mrr_at_1000_diff1
      value: 69.0767
    - type: main_score
      value: 74.736
    task:
      type: Retrieval
  - dataset:
      config: java
      name: MTEB CodeSearchNetRetrieval (java)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 55.1
    - type: ndcg_at_3
      value: 66.89399999999999
    - type: ndcg_at_5
      value: 68.89999999999999
    - type: ndcg_at_10
      value: 70.89
    - type: ndcg_at_20
      value: 72.016
    - type: ndcg_at_100
      value: 73.047
    - type: ndcg_at_1000
      value: 73.553
    - type: map_at_1
      value: 55.1
    - type: map_at_3
      value: 64.05
    - type: map_at_5
      value: 65.18
    - type: map_at_10
      value: 66.012
    - type: map_at_20
      value: 66.328
    - type: map_at_100
      value: 66.483
    - type: map_at_1000
      value: 66.498
    - type: recall_at_1
      value: 55.1
    - type: recall_at_3
      value: 75.1
    - type: recall_at_5
      value: 79.9
    - type: recall_at_10
      value: 86.0
    - type: recall_at_20
      value: 90.4
    - type: recall_at_100
      value: 95.8
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 55.1
    - type: precision_at_3
      value: 25.033
    - type: precision_at_5
      value: 15.98
    - type: precision_at_10
      value: 8.6
    - type: precision_at_20
      value: 4.52
    - type: precision_at_100
      value: 0.958
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 55.1
    - type: mrr_at_3
      value: 64.05
    - type: mrr_at_5
      value: 65.18
    - type: mrr_at_10
      value: 66.0123
    - type: mrr_at_20
      value: 66.32820000000001
    - type: mrr_at_100
      value: 66.4827
    - type: mrr_at_1000
      value: 66.49810000000001
    - type: nauc_ndcg_at_1_max
      value: 30.206100000000003
    - type: nauc_ndcg_at_1_std
      value: -14.6389
    - type: nauc_ndcg_at_1_diff1
      value: 61.8849
    - type: nauc_ndcg_at_3_max
      value: 32.7259
    - type: nauc_ndcg_at_3_std
      value: -11.568399999999999
    - type: nauc_ndcg_at_3_diff1
      value: 59.918800000000005
    - type: nauc_ndcg_at_5_max
      value: 34.1822
    - type: nauc_ndcg_at_5_std
      value: -8.104
    - type: nauc_ndcg_at_5_diff1
      value: 59.434799999999996
    - type: nauc_ndcg_at_10_max
      value: 36.1247
    - type: nauc_ndcg_at_10_std
      value: -6.585100000000001
    - type: nauc_ndcg_at_10_diff1
      value: 59.2885
    - type: nauc_ndcg_at_20_max
      value: 35.9396
    - type: nauc_ndcg_at_20_std
      value: -6.0885
    - type: nauc_ndcg_at_20_diff1
      value: 59.4417
    - type: nauc_ndcg_at_100_max
      value: 35.951499999999996
    - type: nauc_ndcg_at_100_std
      value: -6.1491
    - type: nauc_ndcg_at_100_diff1
      value: 60.3437
    - type: nauc_ndcg_at_1000_max
      value: 34.7092
    - type: nauc_ndcg_at_1000_std
      value: -8.0607
    - type: nauc_ndcg_at_1000_diff1
      value: 60.0215
    - type: nauc_map_at_1_max
      value: 30.206100000000003
    - type: nauc_map_at_1_std
      value: -14.6389
    - type: nauc_map_at_1_diff1
      value: 61.8849
    - type: nauc_map_at_3_max
      value: 31.9303
    - type: nauc_map_at_3_std
      value: -12.651200000000001
    - type: nauc_map_at_3_diff1
      value: 60.33
    - type: nauc_map_at_5_max
      value: 32.6537
    - type: nauc_map_at_5_std
      value: -10.8746
    - type: nauc_map_at_5_diff1
      value: 60.0754
    - type: nauc_map_at_10_max
      value: 33.269
    - type: nauc_map_at_10_std
      value: -10.4054
    - type: nauc_map_at_10_diff1
      value: 60.0235
    - type: nauc_map_at_20_max
      value: 33.1875
    - type: nauc_map_at_20_std
      value: -10.3417
    - type: nauc_map_at_20_diff1
      value: 60.067899999999995
    - type: nauc_map_at_100_max
      value: 33.213
    - type: nauc_map_at_100_std
      value: -10.3299
    - type: nauc_map_at_100_diff1
      value: 60.166399999999996
    - type: nauc_map_at_1000_max
      value: 33.186
    - type: nauc_map_at_1000_std
      value: -10.3713
    - type: nauc_map_at_1000_diff1
      value: 60.16010000000001
    - type: nauc_recall_at_1_max
      value: 30.206100000000003
    - type: nauc_recall_at_1_std
      value: -14.6389
    - type: nauc_recall_at_1_diff1
      value: 61.8849
    - type: nauc_recall_at_3_max
      value: 35.7096
    - type: nauc_recall_at_3_std
      value: -7.4548000000000005
    - type: nauc_recall_at_3_diff1
      value: 58.475699999999996
    - type: nauc_recall_at_5_max
      value: 41.0231
    - type: nauc_recall_at_5_std
      value: 4.4421
    - type: nauc_recall_at_5_diff1
      value: 56.7391
    - type: nauc_recall_at_10_max
      value: 54.789
    - type: nauc_recall_at_10_std
      value: 17.7044
    - type: nauc_recall_at_10_diff1
      value: 55.0592
    - type: nauc_recall_at_20_max
      value: 60.7809
    - type: nauc_recall_at_20_std
      value: 32.4021
    - type: nauc_recall_at_20_diff1
      value: 54.7663
    - type: nauc_recall_at_100_max
      value: 89.4591
    - type: nauc_recall_at_100_std
      value: 76.2783
    - type: nauc_recall_at_100_diff1
      value: 74.4576
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 30.206100000000003
    - type: nauc_precision_at_1_std
      value: -14.6389
    - type: nauc_precision_at_1_diff1
      value: 61.8849
    - type: nauc_precision_at_3_max
      value: 35.7096
    - type: nauc_precision_at_3_std
      value: -7.4548000000000005
    - type: nauc_precision_at_3_diff1
      value: 58.475699999999996
    - type: nauc_precision_at_5_max
      value: 41.0231
    - type: nauc_precision_at_5_std
      value: 4.4421
    - type: nauc_precision_at_5_diff1
      value: 56.7391
    - type: nauc_precision_at_10_max
      value: 54.789
    - type: nauc_precision_at_10_std
      value: 17.7044
    - type: nauc_precision_at_10_diff1
      value: 55.0592
    - type: nauc_precision_at_20_max
      value: 60.7809
    - type: nauc_precision_at_20_std
      value: 32.4021
    - type: nauc_precision_at_20_diff1
      value: 54.7663
    - type: nauc_precision_at_100_max
      value: 89.4591
    - type: nauc_precision_at_100_std
      value: 76.2783
    - type: nauc_precision_at_100_diff1
      value: 74.4576
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 30.206100000000003
    - type: nauc_mrr_at_1_std
      value: -14.6389
    - type: nauc_mrr_at_1_diff1
      value: 61.8849
    - type: nauc_mrr_at_3_max
      value: 31.9303
    - type: nauc_mrr_at_3_std
      value: -12.651200000000001
    - type: nauc_mrr_at_3_diff1
      value: 60.33
    - type: nauc_mrr_at_5_max
      value: 32.6537
    - type: nauc_mrr_at_5_std
      value: -10.8746
    - type: nauc_mrr_at_5_diff1
      value: 60.0754
    - type: nauc_mrr_at_10_max
      value: 33.269
    - type: nauc_mrr_at_10_std
      value: -10.4054
    - type: nauc_mrr_at_10_diff1
      value: 60.0235
    - type: nauc_mrr_at_20_max
      value: 33.1875
    - type: nauc_mrr_at_20_std
      value: -10.3417
    - type: nauc_mrr_at_20_diff1
      value: 60.067899999999995
    - type: nauc_mrr_at_100_max
      value: 33.213
    - type: nauc_mrr_at_100_std
      value: -10.3299
    - type: nauc_mrr_at_100_diff1
      value: 60.166399999999996
    - type: nauc_mrr_at_1000_max
      value: 33.186
    - type: nauc_mrr_at_1000_std
      value: -10.3713
    - type: nauc_mrr_at_1000_diff1
      value: 60.16010000000001
    - type: main_score
      value: 70.89
    task:
      type: Retrieval
  - dataset:
      config: php
      name: MTEB CodeSearchNetRetrieval (php)
      revision: fdc6a9e39575768c27eb8a2a5f702bf846eb4759
      split: test
      type: code-search-net/code_search_net
    metrics:
    - type: ndcg_at_1
      value: 56.89999999999999
    - type: ndcg_at_3
      value: 69.128
    - type: ndcg_at_5
      value: 71.495
    - type: ndcg_at_10
      value: 72.92999999999999
    - type: ndcg_at_20
      value: 73.775
    - type: ndcg_at_100
      value: 74.476
    - type: ndcg_at_1000
      value: 75.075
    - type: map_at_1
      value: 56.89999999999999
    - type: map_at_3
      value: 66.10000000000001
    - type: map_at_5
      value: 67.425
    - type: map_at_10
      value: 68.024
    - type: map_at_20
      value: 68.26100000000001
    - type: map_at_100
      value: 68.357
    - type: map_at_1000
      value: 68.376
    - type: recall_at_1
      value: 56.89999999999999
    - type: recall_at_3
      value: 77.9
    - type: recall_at_5
      value: 83.6
    - type: recall_at_10
      value: 88.0
    - type: recall_at_20
      value: 91.3
    - type: recall_at_100
      value: 95.1
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 56.89999999999999
    - type: precision_at_3
      value: 25.967000000000002
    - type: precision_at_5
      value: 16.72
    - type: precision_at_10
      value: 8.799999999999999
    - type: precision_at_20
      value: 4.565
    - type: precision_at_100
      value: 0.951
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 56.89999999999999
    - type: mrr_at_3
      value: 66.10000000000001
    - type: mrr_at_5
      value: 67.425
    - type: mrr_at_10
      value: 68.0238
    - type: mrr_at_20
      value: 68.2613
    - type: mrr_at_100
      value: 68.35719999999999
    - type: mrr_at_1000
      value: 68.3763
    - type: nauc_ndcg_at_1_max
      value: 43.5297
    - type: nauc_ndcg_at_1_std
      value: 7.986600000000001
    - type: nauc_ndcg_at_1_diff1
      value: 65.95689999999999
    - type: nauc_ndcg_at_3_max
      value: 52.166500000000006
    - type: nauc_ndcg_at_3_std
      value: 17.0778
    - type: nauc_ndcg_at_3_diff1
      value: 60.8598
    - type: nauc_ndcg_at_5_max
      value: 53.1733
    - type: nauc_ndcg_at_5_std
      value: 18.7316
    - type: nauc_ndcg_at_5_diff1
      value: 61.4908
    - type: nauc_ndcg_at_10_max
      value: 53.6245
    - type: nauc_ndcg_at_10_std
      value: 19.5627
    - type: nauc_ndcg_at_10_diff1
      value: 61.9788
    - type: nauc_ndcg_at_20_max
      value: 53.725199999999994
    - type: nauc_ndcg_at_20_std
      value: 20.5901
    - type: nauc_ndcg_at_20_diff1
      value: 62.480199999999996
    - type: nauc_ndcg_at_100_max
      value: 53.083499999999994
    - type: nauc_ndcg_at_100_std
      value: 19.8779
    - type: nauc_ndcg_at_100_diff1
      value: 62.849
    - type: nauc_ndcg_at_1000_max
      value: 51.9568
    - type: nauc_ndcg_at_1000_std
      value: 17.8629
    - type: nauc_ndcg_at_1000_diff1
      value: 62.7251
    - type: nauc_map_at_1_max
      value: 43.5297
    - type: nauc_map_at_1_std
      value: 7.986600000000001
    - type: nauc_map_at_1_diff1
      value: 65.95689999999999
    - type: nauc_map_at_3_max
      value: 49.7136
    - type: nauc_map_at_3_std
      value: 14.054400000000001
    - type: nauc_map_at_3_diff1
      value: 62.3127
    - type: nauc_map_at_5_max
      value: 50.138400000000004
    - type: nauc_map_at_5_std
      value: 14.7824
    - type: nauc_map_at_5_diff1
      value: 62.6784
    - type: nauc_map_at_10_max
      value: 50.2613
    - type: nauc_map_at_10_std
      value: 15.024899999999999
    - type: nauc_map_at_10_diff1
      value: 62.864200000000004
    - type: nauc_map_at_20_max
      value: 50.267300000000006
    - type: nauc_map_at_20_std
      value: 15.234300000000001
    - type: nauc_map_at_20_diff1
      value: 63.00130000000001
    - type: nauc_map_at_100_max
      value: 50.1927
    - type: nauc_map_at_100_std
      value: 15.1701
    - type: nauc_map_at_100_diff1
      value: 63.0549
    - type: nauc_map_at_1000_max
      value: 50.1623
    - type: nauc_map_at_1000_std
      value: 15.118500000000001
    - type: nauc_map_at_1000_diff1
      value: 63.048300000000005
    - type: nauc_recall_at_1_max
      value: 43.5297
    - type: nauc_recall_at_1_std
      value: 7.986600000000001
    - type: nauc_recall_at_1_diff1
      value: 65.95689999999999
    - type: nauc_recall_at_3_max
      value: 61.7214
    - type: nauc_recall_at_3_std
      value: 29.1046
    - type: nauc_recall_at_3_diff1
      value: 55.1971
    - type: nauc_recall_at_5_max
      value: 68.1151
    - type: nauc_recall_at_5_std
      value: 38.587700000000005
    - type: nauc_recall_at_5_diff1
      value: 55.886
    - type: nauc_recall_at_10_max
      value: 75.3834
    - type: nauc_recall_at_10_std
      value: 49.6516
    - type: nauc_recall_at_10_diff1
      value: 57.0852
    - type: nauc_recall_at_20_max
      value: 83.7342
    - type: nauc_recall_at_20_std
      value: 69.9947
    - type: nauc_recall_at_20_diff1
      value: 60.002500000000005
    - type: nauc_recall_at_100_max
      value: 91.4204
    - type: nauc_recall_at_100_std
      value: 89.0309
    - type: nauc_recall_at_100_diff1
      value: 65.7358
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 43.5297
    - type: nauc_precision_at_1_std
      value: 7.986600000000001
    - type: nauc_precision_at_1_diff1
      value: 65.95689999999999
    - type: nauc_precision_at_3_max
      value: 61.7214
    - type: nauc_precision_at_3_std
      value: 29.1046
    - type: nauc_precision_at_3_diff1
      value: 55.1971
    - type: nauc_precision_at_5_max
      value: 68.1151
    - type: nauc_precision_at_5_std
      value: 38.587700000000005
    - type: nauc_precision_at_5_diff1
      value: 55.886
    - type: nauc_precision_at_10_max
      value: 75.3834
    - type: nauc_precision_at_10_std
      value: 49.6516
    - type: nauc_precision_at_10_diff1
      value: 57.0852
    - type: nauc_precision_at_20_max
      value: 83.7342
    - type: nauc_precision_at_20_std
      value: 69.9947
    - type: nauc_precision_at_20_diff1
      value: 60.002500000000005
    - type: nauc_precision_at_100_max
      value: 91.4204
    - type: nauc_precision_at_100_std
      value: 89.0309
    - type: nauc_precision_at_100_diff1
      value: 65.7358
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 43.5297
    - type: nauc_mrr_at_1_std
      value: 7.986600000000001
    - type: nauc_mrr_at_1_diff1
      value: 65.95689999999999
    - type: nauc_mrr_at_3_max
      value: 49.7136
    - type: nauc_mrr_at_3_std
      value: 14.054400000000001
    - type: nauc_mrr_at_3_diff1
      value: 62.3127
    - type: nauc_mrr_at_5_max
      value: 50.138400000000004
    - type: nauc_mrr_at_5_std
      value: 14.7824
    - type: nauc_mrr_at_5_diff1
      value: 62.6784
    - type: nauc_mrr_at_10_max
      value: 50.2613
    - type: nauc_mrr_at_10_std
      value: 15.024899999999999
    - type: nauc_mrr_at_10_diff1
      value: 62.864200000000004
    - type: nauc_mrr_at_20_max
      value: 50.267300000000006
    - type: nauc_mrr_at_20_std
      value: 15.234300000000001
    - type: nauc_mrr_at_20_diff1
      value: 63.00130000000001
    - type: nauc_mrr_at_100_max
      value: 50.1927
    - type: nauc_mrr_at_100_std
      value: 15.1701
    - type: nauc_mrr_at_100_diff1
      value: 63.0549
    - type: nauc_mrr_at_1000_max
      value: 50.1623
    - type: nauc_mrr_at_1000_std
      value: 15.118500000000001
    - type: nauc_mrr_at_1000_diff1
      value: 63.048300000000005
    - type: main_score
      value: 72.92999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CodeTransOceanContest (default)
      revision: 20da4eb20a4b17300c0986ee148c90867a7f2a4d
      split: test
      type: CoIR-Retrieval/codetrans-contest
    metrics:
    - type: ndcg_at_1
      value: 50.226000000000006
    - type: ndcg_at_3
      value: 55.748
    - type: ndcg_at_5
      value: 58.007
    - type: ndcg_at_10
      value: 60.831
    - type: ndcg_at_20
      value: 62.793
    - type: ndcg_at_100
      value: 64.43299999999999
    - type: ndcg_at_1000
      value: 65.60000000000001
    - type: map_at_1
      value: 50.226000000000006
    - type: map_at_3
      value: 54.374
    - type: map_at_5
      value: 55.641
    - type: map_at_10
      value: 56.83200000000001
    - type: map_at_20
      value: 57.379999999999995
    - type: map_at_100
      value: 57.594
    - type: map_at_1000
      value: 57.633
    - type: recall_at_1
      value: 50.226000000000006
    - type: recall_at_3
      value: 59.729
    - type: recall_at_5
      value: 65.158
    - type: recall_at_10
      value: 73.756
    - type: recall_at_20
      value: 81.448
    - type: recall_at_100
      value: 90.498
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 50.226000000000006
    - type: precision_at_3
      value: 19.91
    - type: precision_at_5
      value: 13.032
    - type: precision_at_10
      value: 7.376
    - type: precision_at_20
      value: 4.072
    - type: precision_at_100
      value: 0.905
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 50.2262
    - type: mrr_at_3
      value: 54.374100000000006
    - type: mrr_at_5
      value: 55.641
    - type: mrr_at_10
      value: 56.8322
    - type: mrr_at_20
      value: 57.3798
    - type: mrr_at_100
      value: 57.594500000000004
    - type: mrr_at_1000
      value: 57.6333
    - type: nauc_ndcg_at_1_max
      value: 57.24249999999999
    - type: nauc_ndcg_at_1_std
      value: 3.4893
    - type: nauc_ndcg_at_1_diff1
      value: 74.5093
    - type: nauc_ndcg_at_3_max
      value: 57.099
    - type: nauc_ndcg_at_3_std
      value: 3.3562000000000003
    - type: nauc_ndcg_at_3_diff1
      value: 71.5239
    - type: nauc_ndcg_at_5_max
      value: 57.5998
    - type: nauc_ndcg_at_5_std
      value: 4.7879
    - type: nauc_ndcg_at_5_diff1
      value: 69.9839
    - type: nauc_ndcg_at_10_max
      value: 56.1631
    - type: nauc_ndcg_at_10_std
      value: 6.0869
    - type: nauc_ndcg_at_10_diff1
      value: 68.32939999999999
    - type: nauc_ndcg_at_20_max
      value: 56.098800000000004
    - type: nauc_ndcg_at_20_std
      value: 5.1246
    - type: nauc_ndcg_at_20_diff1
      value: 68.9858
    - type: nauc_ndcg_at_100_max
      value: 56.788799999999995
    - type: nauc_ndcg_at_100_std
      value: 5.6714
    - type: nauc_ndcg_at_100_diff1
      value: 69.3668
    - type: nauc_ndcg_at_1000_max
      value: 56.7396
    - type: nauc_ndcg_at_1000_std
      value: 5.0106
    - type: nauc_ndcg_at_1000_diff1
      value: 70.1024
    - type: nauc_map_at_1_max
      value: 57.24249999999999
    - type: nauc_map_at_1_std
      value: 3.4893
    - type: nauc_map_at_1_diff1
      value: 74.5093
    - type: nauc_map_at_3_max
      value: 57.2832
    - type: nauc_map_at_3_std
      value: 3.4703999999999997
    - type: nauc_map_at_3_diff1
      value: 72.40490000000001
    - type: nauc_map_at_5_max
      value: 57.5445
    - type: nauc_map_at_5_std
      value: 4.1418
    - type: nauc_map_at_5_diff1
      value: 71.5756
    - type: nauc_map_at_10_max
      value: 57.0669
    - type: nauc_map_at_10_std
      value: 4.7488
    - type: nauc_map_at_10_diff1
      value: 70.97869999999999
    - type: nauc_map_at_20_max
      value: 57.08800000000001
    - type: nauc_map_at_20_std
      value: 4.4653
    - type: nauc_map_at_20_diff1
      value: 71.2187
    - type: nauc_map_at_100_max
      value: 57.1484
    - type: nauc_map_at_100_std
      value: 4.5175
    - type: nauc_map_at_100_diff1
      value: 71.2734
    - type: nauc_map_at_1000_max
      value: 57.1356
    - type: nauc_map_at_1000_std
      value: 4.4929
    - type: nauc_map_at_1000_diff1
      value: 71.28710000000001
    - type: nauc_recall_at_1_max
      value: 57.24249999999999
    - type: nauc_recall_at_1_std
      value: 3.4893
    - type: nauc_recall_at_1_diff1
      value: 74.5093
    - type: nauc_recall_at_3_max
      value: 56.469800000000006
    - type: nauc_recall_at_3_std
      value: 2.9709
    - type: nauc_recall_at_3_diff1
      value: 68.7698
    - type: nauc_recall_at_5_max
      value: 57.811
    - type: nauc_recall_at_5_std
      value: 7.2669999999999995
    - type: nauc_recall_at_5_diff1
      value: 64.4325
    - type: nauc_recall_at_10_max
      value: 51.5712
    - type: nauc_recall_at_10_std
      value: 12.1867
    - type: nauc_recall_at_10_diff1
      value: 56.4929
    - type: nauc_recall_at_20_max
      value: 49.3
    - type: nauc_recall_at_20_std
      value: 8.371599999999999
    - type: nauc_recall_at_20_diff1
      value: 56.2505
    - type: nauc_recall_at_100_max
      value: 55.7663
    - type: nauc_recall_at_100_std
      value: 19.9214
    - type: nauc_recall_at_100_diff1
      value: 51.6979
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 57.24249999999999
    - type: nauc_precision_at_1_std
      value: 3.4893
    - type: nauc_precision_at_1_diff1
      value: 74.5093
    - type: nauc_precision_at_3_max
      value: 56.469800000000006
    - type: nauc_precision_at_3_std
      value: 2.9709
    - type: nauc_precision_at_3_diff1
      value: 68.7698
    - type: nauc_precision_at_5_max
      value: 57.811
    - type: nauc_precision_at_5_std
      value: 7.2669999999999995
    - type: nauc_precision_at_5_diff1
      value: 64.4325
    - type: nauc_precision_at_10_max
      value: 51.5712
    - type: nauc_precision_at_10_std
      value: 12.1867
    - type: nauc_precision_at_10_diff1
      value: 56.4929
    - type: nauc_precision_at_20_max
      value: 49.3
    - type: nauc_precision_at_20_std
      value: 8.371599999999999
    - type: nauc_precision_at_20_diff1
      value: 56.2505
    - type: nauc_precision_at_100_max
      value: 55.7663
    - type: nauc_precision_at_100_std
      value: 19.9214
    - type: nauc_precision_at_100_diff1
      value: 51.6979
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 57.24249999999999
    - type: nauc_mrr_at_1_std
      value: 3.4893
    - type: nauc_mrr_at_1_diff1
      value: 74.5093
    - type: nauc_mrr_at_3_max
      value: 57.2832
    - type: nauc_mrr_at_3_std
      value: 3.4703999999999997
    - type: nauc_mrr_at_3_diff1
      value: 72.40490000000001
    - type: nauc_mrr_at_5_max
      value: 57.5445
    - type: nauc_mrr_at_5_std
      value: 4.1418
    -