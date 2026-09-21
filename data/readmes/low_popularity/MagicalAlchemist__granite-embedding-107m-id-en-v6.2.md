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
model-index:
- name: ibm-granite/granite-embedding-107m-multilingual
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 72.7136
    - type: f1
      value: 60.44540000000001
    - type: f1_weighted
      value: 77.8541
    - type: ap
      value: 22.4958
    - type: ap_weighted
      value: 22.4958
    - type: main_score
      value: 72.7136
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
      value: 71.6716
    - type: f1
      value: 65.4221
    - type: f1_weighted
      value: 74.3533
    - type: ap
      value: 33.7567
    - type: ap_weighted
      value: 33.7567
    - type: main_score
      value: 71.6716
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
      value: 66.5804
    - type: f1
      value: 66.2191
    - type: f1_weighted
      value: 66.2191
    - type: ap
      value: 61.340799999999994
    - type: ap_weighted
      value: 61.340799999999994
    - type: main_score
      value: 66.5804
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
      value: 36.412
    - type: f1
      value: 35.633199999999995
    - type: f1_weighted
      value: 35.633199999999995
    - type: main_score
      value: 36.412
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
      value: 2.39
    - type: ndcg_at_3
      value: 3.527
    - type: ndcg_at_5
      value: 3.9759999999999995
    - type: ndcg_at_10
      value: 4.537
    - type: ndcg_at_20
      value: 5.140000000000001
    - type: ndcg_at_100
      value: 6.526
    - type: ndcg_at_1000
      value: 9.797
    - type: map_at_1
      value: 2.39
    - type: map_at_3
      value: 3.2489999999999997
    - type: map_at_5
      value: 3.499
    - type: map_at_10
      value: 3.7220000000000004
    - type: map_at_20
      value: 3.887
    - type: map_at_100
      value: 4.058
    - type: map_at_1000
      value: 4.146
    - type: recall_at_1
      value: 2.39
    - type: recall_at_3
      value: 4.329000000000001
    - type: recall_at_5
      value: 5.418
    - type: recall_at_10
      value: 7.198
    - type: recall_at_20
      value: 9.588000000000001
    - type: recall_at_100
      value: 17.371
    - type: recall_at_1000
      value: 45.206
    - type: precision_at_1
      value: 2.39
    - type: precision_at_3
      value: 1.443
    - type: precision_at_5
      value: 1.084
    - type: precision_at_10
      value: 0.72
    - type: precision_at_20
      value: 0.479
    - type: precision_at_100
      value: 0.174
    - type: precision_at_1000
      value: 0.045
    - type: mrr_at_1
      value: 2.3904
    - type: mrr_at_3
      value: 3.2492
    - type: mrr_at_5
      value: 3.4989
    - type: mrr_at_10
      value: 3.7220000000000004
    - type: mrr_at_20
      value: 3.8869000000000002
    - type: mrr_at_100
      value: 4.0578
    - type: mrr_at_1000
      value: 4.1463
    - type: nauc_ndcg_at_1_max
      value: 37.599700000000006
    - type: nauc_ndcg_at_1_std
      value: 20.302899999999998
    - type: nauc_ndcg_at_1_diff1
      value: 40.4987
    - type: nauc_ndcg_at_3_max
      value: 31.119400000000002
    - type: nauc_ndcg_at_3_std
      value: 11.7335
    - type: nauc_ndcg_at_3_diff1
      value: 28.788000000000004
    - type: nauc_ndcg_at_5_max
      value: 28.505399999999998
    - type: nauc_ndcg_at_5_std
      value: 12.1402
    - type: nauc_ndcg_at_5_diff1
      value: 25.730900000000002
    - type: nauc_ndcg_at_10_max
      value: 27.0656
    - type: nauc_ndcg_at_10_std
      value: 12.648699999999998
    - type: nauc_ndcg_at_10_diff1
      value: 22.0832
    - type: nauc_ndcg_at_20_max
      value: 25.953599999999998
    - type: nauc_ndcg_at_20_std
      value: 12.550500000000001
    - type: nauc_ndcg_at_20_diff1
      value: 19.3722
    - type: nauc_ndcg_at_100_max
      value: 23.268
    - type: nauc_ndcg_at_100_std
      value: 12.8176
    - type: nauc_ndcg_at_100_diff1
      value: 15.9275
    - type: nauc_ndcg_at_1000_max
      value: 21.921499999999998
    - type: nauc_ndcg_at_1000_std
      value: 12.656300000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 13.9004
    - type: nauc_map_at_1_max
      value: 37.599700000000006
    - type: nauc_map_at_1_std
      value: 20.302899999999998
    - type: nauc_map_at_1_diff1
      value: 40.4987
    - type: nauc_map_at_3_max
      value: 32.2818
    - type: nauc_map_at_3_std
      value: 13.276399999999999
    - type: nauc_map_at_3_diff1
      value: 30.9064
    - type: nauc_map_at_5_max
      value: 30.5166
    - type: nauc_map_at_5_std
      value: 13.406
    - type: nauc_map_at_5_diff1
      value: 28.8213
    - type: nauc_map_at_10_max
      value: 29.731999999999996
    - type: nauc_map_at_10_std
      value: 13.5688
    - type: nauc_map_at_10_diff1
      value: 26.888499999999997
    - type: nauc_map_at_20_max
      value: 29.211399999999998
    - type: nauc_map_at_20_std
      value: 13.4739
    - type: nauc_map_at_20_diff1
      value: 25.6814
    - type: nauc_map_at_100_max
      value: 28.578300000000002
    - type: nauc_map_at_100_std
      value: 13.5385
    - type: nauc_map_at_100_diff1
      value: 24.793100000000003
    - type: nauc_map_at_1000_max
      value: 28.3912
    - type: nauc_map_at_1000_std
      value: 13.5039
    - type: nauc_map_at_1000_diff1
      value: 24.570600000000002
    - type: nauc_recall_at_1_max
      value: 37.599700000000006
    - type: nauc_recall_at_1_std
      value: 20.302899999999998
    - type: nauc_recall_at_1_diff1
      value: 40.4987
    - type: nauc_recall_at_3_max
      value: 28.598000000000003
    - type: nauc_recall_at_3_std
      value: 8.3847
    - type: nauc_recall_at_3_diff1
      value: 24.1871
    - type: nauc_recall_at_5_max
      value: 24.5381
    - type: nauc_recall_at_5_std
      value: 9.8274
    - type: nauc_recall_at_5_diff1
      value: 19.6821
    - type: nauc_recall_at_10_max
      value: 22.5445
    - type: nauc_recall_at_10_std
      value: 11.4415
    - type: nauc_recall_at_10_diff1
      value: 13.8268
    - type: nauc_recall_at_20_max
      value: 21.3196
    - type: nauc_recall_at_20_std
      value: 11.5932
    - type: nauc_recall_at_20_diff1
      value: 10.1991
    - type: nauc_recall_at_100_max
      value: 16.9415
    - type: nauc_recall_at_100_std
      value: 12.353200000000001
    - type: nauc_recall_at_100_diff1
      value: 5.7534
    - type: nauc_recall_at_1000_max
      value: 15.9223
    - type: nauc_recall_at_1000_std
      value: 12.2848
    - type: nauc_recall_at_1000_diff1
      value: 3.5477000000000003
    - type: nauc_precision_at_1_max
      value: 37.599700000000006
    - type: nauc_precision_at_1_std
      value: 20.302899999999998
    - type: nauc_precision_at_1_diff1
      value: 40.4987
    - type: nauc_precision_at_3_max
      value: 28.598000000000003
    - type: nauc_precision_at_3_std
      value: 8.3847
    - type: nauc_precision_at_3_diff1
      value: 24.1871
    - type: nauc_precision_at_5_max
      value: 24.5381
    - type: nauc_precision_at_5_std
      value: 9.8274
    - type: nauc_precision_at_5_diff1
      value: 19.6821
    - type: nauc_precision_at_10_max
      value: 22.5445
    - type: nauc_precision_at_10_std
      value: 11.4415
    - type: nauc_precision_at_10_diff1
      value: 13.8268
    - type: nauc_precision_at_20_max
      value: 21.3196
    - type: nauc_precision_at_20_std
      value: 11.5932
    - type: nauc_precision_at_20_diff1
      value: 10.1991
    - type: nauc_precision_at_100_max
      value: 16.9415
    - type: nauc_precision_at_100_std
      value: 12.353200000000001
    - type: nauc_precision_at_100_diff1
      value: 5.7534
    - type: nauc_precision_at_1000_max
      value: 15.9223
    - type: nauc_precision_at_1000_std
      value: 12.2848
    - type: nauc_precision_at_1000_diff1
      value: 3.5477000000000003
    - type: nauc_mrr_at_1_max
      value: 37.599700000000006
    - type: nauc_mrr_at_1_std
      value: 20.302899999999998
    - type: nauc_mrr_at_1_diff1
      value: 40.4987
    - type: nauc_mrr_at_3_max
      value: 32.2818
    - type: nauc_mrr_at_3_std
      value: 13.276399999999999
    - type: nauc_mrr_at_3_diff1
      value: 30.9064
    - type: nauc_mrr_at_5_max
      value: 30.5166
    - type: nauc_mrr_at_5_std
      value: 13.406
    - type: nauc_mrr_at_5_diff1
      value: 28.8213
    - type: nauc_mrr_at_10_max
      value: 29.731999999999996
    - type: nauc_mrr_at_10_std
      value: 13.5688
    - type: nauc_mrr_at_10_diff1
      value: 26.888499999999997
    - type: nauc_mrr_at_20_max
      value: 29.211399999999998
    - type: nauc_mrr_at_20_std
      value: 13.4739
    - type: nauc_mrr_at_20_diff1
      value: 25.6814
    - type: nauc_mrr_at_100_max
      value: 28.578300000000002
    - type: nauc_mrr_at_100_std
      value: 13.5385
    - type: nauc_mrr_at_100_diff1
      value: 24.793100000000003
    - type: nauc_mrr_at_1000_max
      value: 28.3912
    - type: nauc_mrr_at_1000_std
      value: 13.5039
    - type: nauc_mrr_at_1000_diff1
      value: 24.570600000000002
    - type: main_score
      value: 4.537
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
      value: 27.168999999999997
    - type: ndcg_at_3
      value: 41.08
    - type: ndcg_at_5
      value: 46.375
    - type: ndcg_at_10
      value: 51.663000000000004
    - type: ndcg_at_20
      value: 54.339999999999996
    - type: ndcg_at_100
      value: 55.656000000000006
    - type: ndcg_at_1000
      value: 55.875
    - type: map_at_1
      value: 27.168999999999997
    - type: map_at_3
      value: 37.482
    - type: map_at_5
      value: 40.416000000000004
    - type: map_at_10
      value: 42.624
    - type: map_at_20
      value: 43.376999999999995
    - type: map_at_100
      value: 43.578
    - type: map_at_1000
      value: 43.588
    - type: recall_at_1
      value: 27.168999999999997
    - type: recall_at_3
      value: 51.565000000000005
    - type: recall_at_5
      value: 64.43799999999999
    - type: recall_at_10
      value: 80.654
    - type: recall_at_20
      value: 91.11
    - type: recall_at_100
      value: 97.937
    - type: recall_at_1000
      value: 99.57300000000001
    - type: precision_at_1
      value: 27.168999999999997
    - type: precision_at_3
      value: 17.188
    - type: precision_at_5
      value: 12.888
    - type: precision_at_10
      value: 8.065
    - type: precision_at_20
      value: 4.555
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 27.6671
    - type: mrr_at_3
      value: 37.6245
    - type: mrr_at_5
      value: 40.6188
    - type: mrr_at_10
      value: 42.8016
    - type: mrr_at_20
      value: 43.5582
    - type: mrr_at_100
      value: 43.7551
    - type: mrr_at_1000
      value: 43.765
    - type: nauc_ndcg_at_1_max
      value: -4.3233
    - type: nauc_ndcg_at_1_std
      value: -3.5458000000000003
    - type: nauc_ndcg_at_1_diff1
      value: 10.8118
    - type: nauc_ndcg_at_3_max
      value: -1.1566
    - type: nauc_ndcg_at_3_std
      value: -2.5897
    - type: nauc_ndcg_at_3_diff1
      value: 8.3298
    - type: nauc_ndcg_at_5_max
      value: -1.399
    - type: nauc_ndcg_at_5_std
      value: -1.9604
    - type: nauc_ndcg_at_5_diff1
      value: 7.6803
    - type: nauc_ndcg_at_10_max
      value: 0.7746000000000001
    - type: nauc_ndcg_at_10_std
      value: -0.9521
    - type: nauc_ndcg_at_10_diff1
      value: 9.1107
    - type: nauc_ndcg_at_20_max
      value: 1.0111999999999999
    - type: nauc_ndcg_at_20_std
      value: 0.1519
    - type: nauc_ndcg_at_20_diff1
      value: 9.5802
    - type: nauc_ndcg_at_100_max
      value: -0.3616
    - type: nauc_ndcg_at_100_std
      value: -0.6704
    - type: nauc_ndcg_at_100_diff1
      value: 9.2401
    - type: nauc_ndcg_at_1000_max
      value: -0.6766
    - type: nauc_ndcg_at_1000_std
      value: -1.0513
    - type: nauc_ndcg_at_1000_diff1
      value: 9.0561
    - type: nauc_map_at_1_max
      value: -4.3233
    - type: nauc_map_at_1_std
      value: -3.5458000000000003
    - type: nauc_map_at_1_diff1
      value: 10.8118
    - type: nauc_map_at_3_max
      value: -1.9845000000000002
    - type: nauc_map_at_3_std
      value: -2.6683
    - type: nauc_map_at_3_diff1
      value: 8.7329
    - type: nauc_map_at_5_max
      value: -2.1342
    - type: nauc_map_at_5_std
      value: -2.3612
    - type: nauc_map_at_5_diff1
      value: 8.4139
    - type: nauc_map_at_10_max
      value: -1.331
    - type: nauc_map_at_10_std
      value: -1.982
    - type: nauc_map_at_10_diff1
      value: 9.004199999999999
    - type: nauc_map_at_20_max
      value: -1.3376000000000001
    - type: nauc_map_at_20_std
      value: -1.7424
    - type: nauc_map_at_20_diff1
      value: 9.1012
    - type: nauc_map_at_100_max
      value: -1.5152
    - type: nauc_map_at_100_std
      value: -1.8418
    - type: nauc_map_at_100_diff1
      value: 9.0513
    - type: nauc_map_at_1000_max
      value: -1.5264
    - type: nauc_map_at_1000_std
      value: -1.8530000000000002
    - type: nauc_map_at_1000_diff1
      value: 9.043800000000001
    - type: nauc_recall_at_1_max
      value: -4.3233
    - type: nauc_recall_at_1_std
      value: -3.5458000000000003
    - type: nauc_recall_at_1_diff1
      value: 10.8118
    - type: nauc_recall_at_3_max
      value: 1.2361
    - type: nauc_recall_at_3_std
      value: -2.4248
    - type: nauc_recall_at_3_diff1
      value: 7.2543
    - type: nauc_recall_at_5_max
      value: 0.9835999999999999
    - type: nauc_recall_at_5_std
      value: -0.5726
    - type: nauc_recall_at_5_diff1
      value: 5.2376
    - type: nauc_recall_at_10_max
      value: 12.7099
    - type: nauc_recall_at_10_std
      value: 4.9688
    - type: nauc_recall_at_10_diff1
      value: 10.5016
    - type: nauc_recall_at_20_max
      value: 28.2615
    - type: nauc_recall_at_20_std
      value: 23.7662
    - type: nauc_recall_at_20_diff1
      value: 17.6392
    - type: nauc_recall_at_100_max
      value: 31.295099999999998
    - type: nauc_recall_at_100_std
      value: 47.1556
    - type: nauc_recall_at_100_diff1
      value: 24.055699999999998
    - type: nauc_recall_at_1000_max
      value: 14.418000000000001
    - type: nauc_recall_at_1000_std
      value: 56.899699999999996
    - type: nauc_recall_at_1000_diff1
      value: 3.7199999999999998
    - type: nauc_precision_at_1_max
      value: -4.3233
    - type: nauc_precision_at_1_std
      value: -3.5458000000000003
    - type: nauc_precision_at_1_diff1
      value: 10.8118
    - type: nauc_precision_at_3_max
      value: 1.2361
    - type: nauc_precision_at_3_std
      value: -2.4248
    - type: nauc_precision_at_3_diff1
      value: 7.2543
    - type: nauc_precision_at_5_max
      value: 0.9835999999999999
    - type: nauc_precision_at_5_std
      value: -0.5726
    - type: nauc_precision_at_5_diff1
      value: 5.2376
    - type: nauc_precision_at_10_max
      value: 12.7099
    - type: nauc_precision_at_10_std
      value: 4.9688
    - type: nauc_precision_at_10_diff1
      value: 10.5016
    - type: nauc_precision_at_20_max
      value: 28.2615
    - type: nauc_precision_at_20_std
      value: 23.7662
    - type: nauc_precision_at_20_diff1
      value: 17.6392
    - type: nauc_precision_at_100_max
      value: 31.295099999999998
    - type: nauc_precision_at_100_std
      value: 47.1556
    - type: nauc_precision_at_100_diff1
      value: 24.055699999999998
    - type: nauc_precision_at_1000_max
      value: 14.418000000000001
    - type: nauc_precision_at_1000_std
      value: 56.899699999999996
    - type: nauc_precision_at_1000_diff1
      value: 3.7199999999999998
    - type: nauc_mrr_at_1_max
      value: -4.2285
    - type: nauc_mrr_at_1_std
      value: -2.9951
    - type: nauc_mrr_at_1_diff1
      value: 9.2226
    - type: nauc_mrr_at_3_max
      value: -2.8361
    - type: nauc_mrr_at_3_std
      value: -2.5372
    - type: nauc_mrr_at_3_diff1
      value: 7.205
    - type: nauc_mrr_at_5_max
      value: -2.827
    - type: nauc_mrr_at_5_std
      value: -2.1469
    - type: nauc_mrr_at_5_diff1
      value: 6.9564
    - type: nauc_mrr_at_10_max
      value: -2.0531
    - type: nauc_mrr_at_10_std
      value: -1.8227
    - type: nauc_mrr_at_10_diff1
      value: 7.500500000000001
    - type: nauc_mrr_at_20_max
      value: -2.0823
    - type: nauc_mrr_at_20_std
      value: -1.585
    - type: nauc_mrr_at_20_diff1
      value: 7.5577000000000005
    - type: nauc_mrr_at_100_max
      value: -2.2609
    - type: nauc_mrr_at_100_std
      value: -1.6787
    - type: nauc_mrr_at_100_diff1
      value: 7.500500000000001
    - type: nauc_mrr_at_1000_max
      value: -2.2721999999999998
    - type: nauc_mrr_at_1000_std
      value: -1.6898
    - type: nauc_mrr_at_1000_diff1
      value: 7.492400000000001
    - type: main_score
      value: 51.663000000000004
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
      value: 41.4944
    - type: v_measure_std
      value: 13.6458
    - type: main_score
      value: 41.4944
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
      value: 30.6155
    - type: v_measure_std
      value: 14.377999999999998
    - type: main_score
      value: 30.6155
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
      value: 61.9001
    - type: mrr
      value: 77.0427
    - type: nAUC_map_max
      value: 27.7273
    - type: nAUC_map_std
      value: 14.369299999999999
    - type: nAUC_map_diff1
      value: 10.7899
    - type: nAUC_mrr_max
      value: 35.606100000000005
    - type: nAUC_mrr_std
      value: 20.2621
    - type: nAUC_mrr_diff1
      value: 17.814
    - type: main_score
      value: 61.9001
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
      value: 81.5558
    - type: spearman
      value: 79.2952
    - type: cosine_pearson
      value: 81.5558
    - type: cosine_spearman
      value: 79.2952
    - type: manhattan_pearson
      value: 79.4434
    - type: manhattan_spearman
      value: 78.803
    - type: euclidean_pearson
      value: 80.0336
    - type: euclidean_spearman
      value: 79.2952
    - type: main_score
      value: 79.2952
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
      value: 75.9481
    - type: f1
      value: 74.9851
    - type: f1_weighted
      value: 74.9851
    - type: main_score
      value: 75.9481
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
      value: 35.6038
    - type: v_measure_std
      value: 0.5428999999999999
    - type: main_score
      value: 35.6038
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
      value: 28.3652
    - type: v_measure_std
      value: 1.0767
    - type: main_score
      value: 28.3652
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
      value: 78.69699999999999
    - type: ndcg_at_3
      value: 82.666
    - type: ndcg_at_5
      value: 83.607
    - type: ndcg_at_10
      value: 84.407
    - type: ndcg_at_20
      value: 84.92699999999999
    - type: ndcg_at_100
      value: 85.641
    - type: ndcg_at_1000
      value: 85.978
    - type: map_at_1
      value: 78.69699999999999
    - type: map_at_3
      value: 81.723
    - type: map_at_5
      value: 82.245
    - type: map_at_10
      value: 82.577
    - type: map_at_20
      value: 82.722
    - type: map_at_100
      value: 82.821
    - type: map_at_1000
      value: 82.834
    - type: recall_at_1
      value: 78.69699999999999
    - type: recall_at_3
      value: 85.38
    - type: recall_at_5
      value: 87.666
    - type: recall_at_10
      value: 90.133
    - type: recall_at_20
      value: 92.171
    - type: recall_at_100
      value: 96.012
    - type: recall_at_1000
      value: 98.68599999999999
    - type: precision_at_1
      value: 78.69699999999999
    - type: precision_at_3
      value: 28.46
    - type: precision_at_5
      value: 17.533
    - type: precision_at_10
      value: 9.013
    - type: precision_at_20
      value: 4.609
    - type: precision_at_100
      value: 0.96
    - type: precision_at_1000
      value: 0.099
    - type: mrr_at_1
      value: 78.7036
    - type: mrr_at_3
      value: 81.7223
    - type: mrr_at_5
      value: 82.24719999999999
    - type: mrr_at_10
      value: 82.5792
    - type: mrr_at_20
      value: 82.72460000000001
    - type: mrr_at_100
      value: 82.82350000000001
    - type: mrr_at_1000
      value: 82.8357
    - type: nauc_ndcg_at_1_max
      value: 84.22319999999999
    - type: nauc_ndcg_at_1_std
      value: 23.538999999999998
    - type: nauc_ndcg_at_1_diff1
      value: 90.73750000000001
    - type: nauc_ndcg_at_3_max
      value: 85.0914
    - type: nauc_ndcg_at_3_std
      value: 25.0172
    - type: nauc_ndcg_at_3_diff1
      value: 89.3858
    - type: nauc_ndcg_at_5_max
      value: 84.9112
    - type: nauc_ndcg_at_5_std
      value: 25.732899999999997
    - type: nauc_ndcg_at_5_diff1
      value: 89.1327
    - type: nauc_ndcg_at_10_max
      value: 84.6806
    - type: nauc_ndcg_at_10_std
      value: 26.488
    - type: nauc_ndcg_at_10_diff1
      value: 88.83879999999999
    - type: nauc_ndcg_at_20_max
      value: 84.8315
    - type: nauc_ndcg_at_20_std
      value: 26.9453
    - type: nauc_ndcg_at_20_diff1
      value: 88.9755
    - type: nauc_ndcg_at_100_max
      value: 84.924
    - type: nauc_ndcg_at_100_std
      value: 26.9297
    - type: nauc_ndcg_at_100_diff1
      value: 89.1861
    - type: nauc_ndcg_at_1000_max
      value: 84.9058
    - type: nauc_ndcg_at_1000_std
      value: 26.5904
    - type: nauc_ndcg_at_1000_diff1
      value: 89.2659
    - type: nauc_map_at_1_max
      value: 84.22319999999999
    - type: nauc_map_at_1_std
      value: 23.538999999999998
    - type: nauc_map_at_1_diff1
      value: 90.73750000000001
    - type: nauc_map_at_3_max
      value: 84.9005
    - type: nauc_map_at_3_std
      value: 24.622
    - type: nauc_map_at_3_diff1
      value: 89.74069999999999
    - type: nauc_map_at_5_max
      value: 84.8017
    - type: nauc_map_at_5_std
      value: 24.9739
    - type: nauc_map_at_5_diff1
      value: 89.61970000000001
    - type: nauc_map_at_10_max
      value: 84.7091
    - type: nauc_map_at_10_std
      value: 25.223699999999997
    - type: nauc_map_at_10_diff1
      value: 89.51639999999999
    - type: nauc_map_at_20_max
      value: 84.7458
    - type: nauc_map_at_20_std
      value: 25.3151
    - type: nauc_map_at_20_diff1
      value: 89.5589
    - type: nauc_map_at_100_max
      value: 84.75930000000001
    - type: nauc_map_at_100_std
      value: 25.318099999999998
    - type: nauc_map_at_100_diff1
      value: 89.58850000000001
    - type: nauc_map_at_1000_max
      value: 84.75880000000001
    - type: nauc_map_at_1000_std
      value: 25.3086
    - type: nauc_map_at_1000_diff1
      value: 89.591
    - type: nauc_recall_at_1_max
      value: 84.22319999999999
    - type: nauc_recall_at_1_std
      value: 23.538999999999998
    - type: nauc_recall_at_1_diff1
      value: 90.73750000000001
    - type: nauc_recall_at_3_max
      value: 85.7389
    - type: nauc_recall_at_3_std
      value: 26.4015
    - type: nauc_recall_at_3_diff1
      value: 88.1462
    - type: nauc_recall_at_5_max
      value: 85.2854
    - type: nauc_recall_at_5_std
      value: 28.9065
    - type: nauc_recall_at_5_diff1
      value: 87.15039999999999
    - type: nauc_recall_at_10_max
      value: 84.3391
    - type: nauc_recall_at_10_std
      value: 33.2602
    - type: nauc_recall_at_10_diff1
      value: 85.3733
    - type: nauc_recall_at_20_max
      value: 85.3385
    - type: nauc_recall_at_20_std
      value: 38.4429
    - type: nauc_recall_at_20_diff1
      value: 85.40299999999999
    - type: nauc_recall_at_100_max
      value: 87.3325
    - type: nauc_recall_at_100_std
      value: 48.357
    - type: nauc_recall_at_100_diff1
      value: 85.7283
    - type: nauc_recall_at_1000_max
      value: 90.63419999999999
    - type: nauc_recall_at_1000_std
      value: 63.489399999999996
    - type: nauc_recall_at_1000_diff1
      value: 85.1443
    - type: nauc_precision_at_1_max
      value: 84.22319999999999
    - type: nauc_precision_at_1_std
      value: 23.538999999999998
    - type: nauc_precision_at_1_diff1
      value: 90.73750000000001
    - type: nauc_precision_at_3_max
      value: 85.7389
    - type: nauc_precision_at_3_std
      value: 26.4015
    - type: nauc_precision_at_3_diff1
      value: 88.1462
    - type: nauc_precision_at_5_max
      value: 85.2854
    - type: nauc_precision_at_5_std
      value: 28.9065
    - type: nauc_precision_at_5_diff1
      value: 87.15039999999999
    - type: nauc_precision_at_10_max
      value: 84.3391
    - type: nauc_precision_at_10_std
      value: 33.2602
    - type: nauc_precision_at_10_diff1
      value: 85.3733
    - type: nauc_precision_at_20_max
      value: 85.3385
    - type: nauc_precision_at_20_std
      value: 38.4429
    - type: nauc_precision_at_20_diff1
      value: 85.40299999999999
    - type: nauc_precision_at_100_max
      value: 87.3325
    - type: nauc_precision_at_100_std
      value: 48.357
    - type: nauc_precision_at_100_diff1
      value: 85.7283
    - type: nauc_precision_at_1000_max
      value: 90.63419999999999
    - type: nauc_precision_at_1000_std
      value: 63.489399999999996
    - type: nauc_precision_at_1000_diff1
      value: 85.1443
    - type: nauc_mrr_at_1_max
      value: 84.1909
    - type: nauc_mrr_at_1_std
      value: 23.5506
    - type: nauc_mrr_at_1_diff1
      value: 90.7257
    - type: nauc_mrr_at_3_max
      value: 84.883
    - type: nauc_mrr_at_3_std
      value: 24.630499999999998
    - type: nauc_mrr_at_3_diff1
      value: 89.7361
    - type: nauc_mrr_at_5_max
      value: 84.783
    - type: nauc_mrr_at_5_std
      value: 24.9813
    - type: nauc_mrr_at_5_diff1
      value: 89.6132
    - type: nauc_mrr_at_10_max
      value: 84.6899
    - type: nauc_mrr_at_10_std
      value: 25.230200000000004
    - type: nauc_mrr_at_10_diff1
      value: 89.5099
    - type: nauc_mrr_at_20_max
      value: 84.7264
    - type: nauc_mrr_at_20_std
      value: 25.3216
    - type: nauc_mrr_at_20_diff1
      value: 89.5523
    - type: nauc_mrr_at_100_max
      value: 84.7398
    - type: nauc_mrr_at_100_std
      value: 25.324799999999996
    - type: nauc_mrr_at_100_diff1
      value: 89.5818
    - type: nauc_mrr_at_1000_max
      value: 84.7393
    - type: nauc_mrr_at_1000_std
      value: 25.315199999999997
    - type: nauc_mrr_at_1000_diff1
      value: 89.5843
    - type: main_score
      value: 84.407
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
      value: 22.03
    - type: ndcg_at_3
      value: 27.577
    - type: ndcg_at_5
      value: 29.465000000000003
    - type: ndcg_at_10
      value: 31.297000000000004
    - type: ndcg_at_20
      value: 32.666000000000004
    - type: ndcg_at_100
      value: 34.905
    - type: ndcg_at_1000
      value: 37.126
    - type: map_at_1
      value: 22.03
    - type: map_at_3
      value: 26.208
    - type: map_at_5
      value: 27.255000000000003
    - type: map_at_10
      value: 28.014
    - type: map_at_20
      value: 28.394000000000002
    - type: map_at_100
      value: 28.676000000000002
    - type: map_at_1000
      value: 28.747
    - type: recall_at_1
      value: 22.03
    - type: recall_at_3
      value: 31.541000000000004
    - type: recall_at_5
      value: 36.129
    - type: recall_at_10
      value: 41.781
    - type: recall_at_20
      value: 47.159
    - type: recall_at_100
      value: 59.648
    - type: recall_at_1000
      value: 77.818
    - type: precision_at_1
      value: 22.03
    - type: precision_at_3
      value: 10.514
    - type: precision_at_5
      value: 7.226000000000001
    - type: precision_at_10
      value: 4.178
    - type: precision_at_20
      value: 2.358
    - type: precision_at_100
      value: 0.596
    - type: precision_at_1000
      value: 0.078
    - type: mrr_at_1
      value: 22.029799999999998
    - type: mrr_at_3
      value: 26.2078
    - type: mrr_at_5
      value: 27.2546
    - type: mrr_at_10
      value: 28.0138
    - type: mrr_at_20
      value: 28.393800000000002
    - type: mrr_at_100
      value: 28.6755
    - type: mrr_at_1000
      value: 28.7473
    - type: nauc_ndcg_at_1_max
      value: 43.7913
    - type: nauc_ndcg_at_1_std
      value: 5.8822
    - type: nauc_ndcg_at_1_diff1
      value: 57.5892
    - type: nauc_ndcg_at_3_max
      value: 43.6608
    - type: nauc_ndcg_at_3_std
      value: 7.308199999999999
    - type: nauc_ndcg_at_3_diff1
      value: 50.727199999999996
    - type: nauc_ndcg_at_5_max
      value: 43.540099999999995
    - type: nauc_ndcg_at_5_std
      value: 8.2882
    - type: nauc_ndcg_at_5_diff1
      value: 49.7273
    - type: nauc_ndcg_at_10_max
      value: 43.290800000000004
    - type: nauc_ndcg_at_10_std
      value: 9.177
    - type: nauc_ndcg_at_10_diff1
      value: 48.6902
    - type: nauc_ndcg_at_20_max
      value: 43.1726
    - type: nauc_ndcg_at_20_std
      value: 9.9537
    - type: nauc_ndcg_at_20_diff1
      value: 48.2511
    - type: nauc_ndcg_at_100_max
      value: 43.0801
    - type: nauc_ndcg_at_100_std
      value: 11.2629
    - type: nauc_ndcg_at_100_diff1
      value: 47.7496
    - type: nauc_ndcg_at_1000_max
      value: 43.0087
    - type: nauc_ndcg_at_1000_std
      value: 11.3454
    - type: nauc_ndcg_at_1000_diff1
      value: 47.7628
    - type: nauc_map_at_1_max
      value: 43.7913
    - type: nauc_map_at_1_std
      value: 5.8822
    - type: nauc_map_at_1_diff1
      value: 57.5892
    - type: nauc_map_at_3_max
      value: 43.623200000000004
    - type: nauc_map_at_3_std
      value: 6.9021
    - type: nauc_map_at_3_diff1
      value: 52.296600000000005
    - type: nauc_map_at_5_max
      value: 43.567099999999996
    - type: nauc_map_at_5_std
      value: 7.4779
    - type: nauc_map_at_5_diff1
      value: 51.7259
    - type: nauc_map_at_10_max
      value: 43.4204
    - type: nauc_map_at_10_std
      value: 7.82
    - type: nauc_map_at_10_diff1
      value: 51.266
    - type: nauc_map_at_20_max
      value: 43.3827
    - type: nauc_map_at_20_std
      value: 8.0332
    - type: nauc_map_at_20_diff1
      value: 51.139599999999994
    - type: nauc_map_at_100_max
      value: 43.3681
    - type: nauc_map_at_100_std
      value: 8.205400000000001
    - type: nauc_map_at_100_diff1
      value: 51.054
    - type: nauc_map_at_1000_max
      value: 43.3619
    - type: nauc_map_at_1000_std
      value: 8.2009
    - type: nauc_map_at_1000_diff1
      value: 51.0517
    - type: nauc_recall_at_1_max
      value: 43.7913
    - type: nauc_recall_at_1_std
      value: 5.8822
    - type: nauc_recall_at_1_diff1
      value: 57.5892
    - type: nauc_recall_at_3_max
      value: 43.7869
    - type: nauc_recall_at_3_std
      value: 8.4252
    - type: nauc_recall_at_3_diff1
      value: 46.5268
    - type: nauc_recall_at_5_max
      value: 43.4642
    - type: nauc_recall_at_5_std
      value: 10.5594
    - type: nauc_recall_at_5_diff1
      value: 44.329800000000006
    - type: nauc_recall_at_10_max
      value: 42.9497
    - type: nauc_recall_at_10_std
      value: 13.252
    - type: nauc_recall_at_10_diff1
      value: 41.5027
    - type: nauc_recall_at_20_max
      value: 42.5357
    - type: nauc_recall_at_20_std
      value: 16.2323
    - type: nauc_recall_at_20_diff1
      value: 39.7814
    - type: nauc_recall_at_100_max
      value: 41.963899999999995
    - type: nauc_recall_at_100_std
      value: 24.3312
    - type: nauc_recall_at_100_diff1
      value: 36.321
    - type: nauc_recall_at_1000_max
      value: 40.839999999999996
    - type: nauc_recall_at_1000_std
      value: 32.861000000000004
    - type: nauc_recall_at_1000_diff1
      value: 30.7145
    - type: nauc_precision_at_1_max
      value: 43.7913
    - type: nauc_precision_at_1_std
      value: 5.8822
    - type: nauc_precision_at_1_diff1
      value: 57.5892
    - type: nauc_precision_at_3_max
      value: 43.7869
    - type: nauc_precision_at_3_std
      value: 8.4252
    - type: nauc_precision_at_3_diff1
      value: 46.5268
    - type: nauc_precision_at_5_max
      value: 43.4642
    - type: nauc_precision_at_5_std
      value: 10.5594
    - type: nauc_precision_at_5_diff1
      value: 44.329800000000006
    - type: nauc_precision_at_10_max
      value: 42.9497
    - type: nauc_precision_at_10_std
      value: 13.252
    - type: nauc_precision_at_10_diff1
      value: 41.5027
    - type: nauc_precision_at_20_max
      value: 42.5357
    - type: nauc_precision_at_20_std
      value: 16.2323
    - type: nauc_precision_at_20_diff1
      value: 39.7814
    - type: nauc_precision_at_100_max
      value: 41.963899999999995
    - type: nauc_precision_at_100_std
      value: 24.3312
    - type: nauc_precision_at_100_diff1
      value: 36.321
    - type: nauc_precision_at_1000_max
      value: 40.839999999999996
    - type: nauc_precision_at_1000_std
      value: 32.861000000000004
    - type: nauc_precision_at_1000_diff1
      value: 30.7145
    - type: nauc_mrr_at_1_max
      value: 43.7913
    - type: nauc_mrr_at_1_std
      value: 5.8822
    - type: nauc_mrr_at_1_diff1
      value: 57.5892
    - type: nauc_mrr_at_3_max
      value: 43.623200000000004
    - type: nauc_mrr_at_3_std
      value: 6.9021
    - type: nauc_mrr_at_3_diff1
      value: 52.296600000000005
    - type: nauc_mrr_at_5_max
      value: 43.567099999999996
    - type: nauc_mrr_at_5_std
      value: 7.4779
    - type: nauc_mrr_at_5_diff1
      value: 51.7259
    - type: nauc_mrr_at_10_max
      value: 43.4204
    - type: nauc_mrr_at_10_std
      value: 7.82
    - type: nauc_mrr_at_10_diff1
      value: 51.266
    - type: nauc_mrr_at_20_max
      value: 43.3827
    - type: nauc_mrr_at_20_std
      value: 8.0332
    - type: nauc_mrr_at_20_diff1
      value: 51.139599999999994
    - type: nauc_mrr_at_100_max
      value: 43.3681
    - type: nauc_mrr_at_100_std
      value: 8.2055
    - type: nauc_mrr_at_100_diff1
      value: 51.054100000000005
    - type: nauc_mrr_at_1000_max
      value: 43.3619
    - type: nauc_mrr_at_1000_std
      value: 8.2009
    - type: nauc_mrr_at_1000_diff1
      value: 51.0518
    - type: main_score
      value: 31.297000000000004
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
      value: 36.58
    - type: ndcg_at_3
      value: 44.633
    - type: ndcg_at_5
      value: 46.766000000000005
    - type: ndcg_at_10
      value: 48.921
    - type: ndcg_at_20
      value: 50.52100000000001
    - type: ndcg_at_100
      value: 52.795
    - type: ndcg_at_1000
      value: 54.291
    - type: map_at_1
      value: 36.58
    - type: map_at_3
      value: 42.666
    - type: map_at_5
      value: 43.852000000000004
    - type: map_at_10
      value: 44.744
    - type: map_at_20
      value: 45.188
    - type: map_at_100
      value: 45.493
    - type: map_at_1000
      value: 45.544000000000004
    - type: recall_at_1
      value: 36.58
    - type: recall_at_3
      value: 50.32
    - type: recall_at_5
      value: 55.491
    - type: recall_at_10
      value: 62.13999999999999
    - type: recall_at_20
      value: 68.431
    - type: recall_at_100
      value: 80.83
    - type: recall_at_1000
      value: 92.896
    - type: precision_at_1
      value: 36.58
    - type: precision_at_3
      value: 16.773
    - type: precision_at_5
      value: 11.097999999999999
    - type: precision_at_10
      value: 6.214
    - type: precision_at_20
      value: 3.422
    - type: precision_at_100
      value: 0.808
    - type: precision_at_1000
      value: 0.093
    - type: mrr_at_1
      value: 36.579699999999995
    - type: mrr_at_3
      value: 42.666
    - type: mrr_at_5
      value: 43.8517
    - type: mrr_at_10
      value: 44.7436
    - type: mrr_at_20
      value: 45.1875
    - type: mrr_at_100
      value: 45.493
    - type: mrr_at_1000
      value: 45.544200000000004
    - type: nauc_ndcg_at_1_max
      value: 41.7601
    - type: nauc_ndcg_at_1_std
      value: 4.5455000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 58.6454
    - type: nauc_ndcg_at_3_max
      value: 42.3992
    - type: nauc_ndcg_at_3_std
      value: 6.3083
    - type: nauc_ndcg_at_3_diff1
      value: 52.4271
    - type: nauc_ndcg_at_5_max
      value: 42.2462
    - type: nauc_ndcg_at_5_std
      value: 6.8773
    - type: nauc_ndcg_at_5_diff1
      value: 51.75880000000001
    - type: nauc_ndcg_at_10_max
      value: 41.7943
    - type: nauc_ndcg_at_10_std
      value: 7.2982000000000005
    - type: nauc_ndcg_at_10_diff1
      value: 51.0016
    - type: nauc_ndcg_at_20_max
      value: 41.5875
    - type: nauc_ndcg_at_20_std
      value: 7.8825
    - type: nauc_ndcg_at_20_diff1
      value: 50.7648
    - type: nauc_ndcg_at_100_max
      value: 41.6971
    - type: nauc_ndcg_at_100_std
      value: 8.4077
    - type: nauc_ndcg_at_100_diff1
      value: 50.9386
    - type: nauc_ndcg_at_1000_max
      value: 41.7837
    - type: nauc_ndcg_at_1000_std
      value: 8.250300000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 51.4691
    - type: nauc_map_at_1_max
      value: 41.7601
    - type: nauc_map_at_1_std
      value: 4.5455000000000005
    - type: nauc_map_at_1_diff1
      value: 58.6454
    - type: nauc_map_at_3_max
      value: 42.2864
    - type: nauc_map_at_3_std
      value: 5.8461
    - type: nauc_map_at_3_diff1
      value: 53.9381
    - type: nauc_map_at_5_max
      value: 42.1957
    - type: nauc_map_at_5_std
      value: 6.142
    - type: nauc_map_at_5_diff1
      value: 53.600300000000004
    - type: nauc_map_at_10_max
      value: 42.005900000000004
    - type: nauc_map_at_10_std
      value: 6.2986
    - type: nauc_map_at_10_diff1
      value: 53.296200000000006
    - type: nauc_map_at_20_max
      value: 41.946099999999994
    - type: nauc_map_at_20_std
      value: 6.452299999999999
    - type: nauc_map_at_20_diff1
      value: 53.2485
    - type: nauc_map_at_100_max
      value: 41.9563
    - type: nauc_map_at_100_std
      value: 6.511
    - type: nauc_map_at_100_diff1
      value: 53.2816
    - type: nauc_map_at_1000_max
      value: 41.9598
    - type: nauc_map_at_1000_std
      value: 6.5069
    - type: nauc_map_at_1000_diff1
      value: 53.3008
    - type: nauc_recall_at_1_max
      value: 41.7601
    - type: nauc_recall_at_1_std
      value: 4.5455000000000005
    - type: nauc_recall_at_1_diff1
      value: 58.6454
    - type: nauc_recall_at_3_max
      value: 42.7117
    - type: nauc_recall_at_3_std
      value: 7.674799999999999
    - type: nauc_recall_at_3_diff1
      value: 48.0061
    - type: nauc_recall_at_5_max
      value: 42.365399999999994
    - type: nauc_recall_at_5_std
      value: 9.2378
    - type: nauc_recall_at_5_diff1
      value: 46.0218
    - type: nauc_recall_at_10_max
      value: 40.8705
    - type: nauc_recall_at_10_std
      value: 10.9253
    - type: nauc_recall_at_10_diff1
      value: 43.0092
    - type: nauc_recall_at_20_max
      value: 39.818599999999996
    - type: nauc_recall_at_20_std
      value: 14.1425
    - type: nauc_recall_at_20_diff1
      value: 40.8455
    - type: nauc_recall_at_100_max
      value: 40.1229
    - type: nauc_recall_at_100_std
      value: 22.0804
    - type: nauc_recall_at_100_diff1
      value: 37.6538
    - type: nauc_recall_at_1000_max
      value: 40.4194
    - type: nauc_recall_at_1000_std
      value: 36.7051
    - type: nauc_recall_at_1000_diff1
      value: 35.3088
    - type: nauc_precision_at_1_max
      value: 41.7601
    - type: nauc_precision_at_1_std
      value: 4.5455000000000005
    - type: nauc_precision_at_1_diff1
      value: 58.6454
    - type: nauc_precision_at_3_max
      value: 42.7117
    - type: nauc_precision_at_3_std
      value: 7.674799999999999
    - type: nauc_precision_at_3_diff1
      value: 48.0061
    - type: nauc_precision_at_5_max
      value: 42.365399999999994
    - type: nauc_precision_at_5_std
      value: 9.2378
    - type: nauc_precision_at_5_diff1
      value: 46.0218
    - type: nauc_precision_at_10_max
      value: 40.8705
    - type: nauc_precision_at_10_std
      value: 10.9253
    - type: nauc_precision_at_10_diff1
      value: 43.0092
    - type: nauc_precision_at_20_max
      value: 39.818599999999996
    - type: nauc_precision_at_20_std
      value: 14.1425
    - type: nauc_precision_at_20_diff1
      value: 40.8455
    - type: nauc_precision_at_100_max
      value: 40.1229
    - type: nauc_precision_at_100_std
      value: 22.0804
    - type: nauc_precision_at_100_diff1
      value: 37.6538
    - type: nauc_precision_at_1000_max
      value: 40.4194
    - type: nauc_precision_at_1000_std
      value: 36.7051
    - type: nauc_precision_at_1000_diff1
      value: 35.3088
    - type: nauc_mrr_at_1_max
      value: 41.7601
    - type: nauc_mrr_at_1_std
      value: 4.5455000000000005
    - type: nauc_mrr_at_1_diff1
      value: 58.6454
    - type: nauc_mrr_at_3_max
      value: 42.2864
    - type: nauc_mrr_at_3_std
      value: 5.8461
    - type: nauc_mrr_at_3_diff1
      value: 53.9381
    - type: nauc_mrr_at_5_max
      value: 42.1957
    - type: nauc_mrr_at_5_std
      value: 6.142
    - type: nauc_mrr_at_5_diff1
      value: 53.600300000000004
    - type: nauc_mrr_at_10_max
      value: 42.005900000000004
    - type: nauc_mrr_at_10_std
      value: 6.2986
    - type: nauc_mrr_at_10_diff1
      value: 53.296200000000006
    - type: nauc_mrr_at_20_max
      value: 41.946099999999994
    - type: nauc_mrr_at_20_std
      value: 6.452299999999999
    - type: nauc_mrr_at_20_diff1
      value: 53.2485
    - type: nauc_mrr_at_100_max
      value: 41.9563
    - type: nauc_mrr_at_100_std
      value: 6.511
    - type: nauc_mrr_at_100_diff1
      value: 53.2816
    - type: nauc_mrr_at_1000_max
      value: 41.9598
    - type: nauc_mrr_at_1000_std
      value: 6.5069
    - type: nauc_mrr_at_1000_diff1
      value: 53.3008
    - type: main_score
      value: 48.921
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
      value: 27.359
    - type: ndcg_at_3
      value: 33.405
    - type: ndcg_at_5
      value: 35.111
    - type: ndcg_at_10
      value: 37.124
    - type: ndcg_at_20
      value: 38.637
    - type: ndcg_at_100
      value: 40.809
    - type: ndcg_at_1000
      value: 43.206
    - type: map_at_1
      value: 27.359
    - type: map_at_3
      value: 31.906000000000002
    - type: map_at_5
      value: 32.838
    - type: map_at_10
      value: 33.677
    - type: map_at_20
      value: 34.086
    - type: map_at_100
      value: 34.379
    - type: map_at_1000
      value: 34.458
    - type: recall_at_1
      value: 27.359
    - type: recall_at_3
      value: 37.748
    - type: recall_at_5
      value: 41.951
    - type: recall_at_10
      value: 48.136
    - type: recall_at_20
      value: 54.163
    - type: recall_at_100
      value: 65.979
    - type: recall_at_1000
      value: 85.488
    - type: precision_at_1
      value: 27.359
    - type: precision_at_3
      value: 12.583
    - type: precision_at_5
      value: 8.39
    - type: precision_at_10
      value: 4.814
    - type: precision_at_20
      value: 2.708
    - type: precision_at_100
      value: 0.66
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: mrr_at_1
      value: 27.3592
    - type: mrr_at_3
      value: 31.9059
    - type: mrr_at_5
      value: 32.8377
    - type: mrr_at_10
      value: 33.677099999999996
    - type: mrr_at_20
      value: 34.086
    - type: mrr_at_100
      value: 34.3787
    - type: mrr_at_1000
      value: 34.4575
    - type: nauc_ndcg_at_1_max
      value: 41.336
    - type: nauc_ndcg_at_1_std
      value: 4.9167000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 59.489599999999996
    - type: nauc_ndcg_at_3_max
      value: 42.3939
    - type: nauc_ndcg_at_3_std
      value: 9.324200000000001
    - type: nauc_ndcg_at_3_diff1
      value: 53.886
    - type: nauc_ndcg_at_5_max
      value: 41.523700000000005
    - type: nauc_ndcg_at_5_std
      value: 8.7661
    - type: nauc_ndcg_at_5_diff1
      value: 52.6116
    - type: nauc_ndcg_at_10_max
      value: 40.7362
    - type: nauc_ndcg_at_10_std
      value: 9.3454
    - type: nauc_ndcg_at_10_diff1
      value: 51.226000000000006
    - type: nauc_ndcg_at_20_max
      value: 40.1284
    - type: nauc_ndcg_at_20_std
      value: 10.1067
    - type: nauc_ndcg_at_20_diff1
      value: 50.6354
    - type: nauc_ndcg_at_100_max
      value: 40.109899999999996
    - type: nauc_ndcg_at_100_std
      value: 11.125599999999999
    - type: nauc_ndcg_at_100_diff1
      value: 50.021499999999996
    - type: nauc_ndcg_at_1000_max
      value: 39.9325
    - type: nauc_ndcg_at_1000_std
      value: 10.9899
    - type: nauc_ndcg_at_1000_diff1
      value: 50.3713
    - type: nauc_map_at_1_max
      value: 41.336
    - type: nauc_map_at_1_std
      value: 4.9167000000000005
    - type: nauc_map_at_1_diff1
      value: 59.489599999999996
    - type: nauc_map_at_3_max
      value: 42.1793
    - type: nauc_map_at_3_std
      value: 8.149099999999999
    - type: nauc_map_at_3_diff1
      value: 55.1967
    - type: nauc_map_at_5_max
      value: 41.6768
    - type: nauc_map_at_5_std
      value: 7.8223
    - type: nauc_map_at_5_diff1
      value: 54.4705
    - type: nauc_map_at_10_max
      value: 41.3395
    - type: nauc_map_at_10_std
      value: 8.076
    - type: nauc_map_at_10_diff1
      value: 53.87929999999999
    - type: nauc_map_at_20_max
      value: 41.1762
    - type: nauc_map_at_20_std
      value: 8.2845
    - type: nauc_map_at_20_diff1
      value: 53.7144
    - type: nauc_map_at_100_max
      value: 41.1731
    - type: nauc_map_at_100_std
      value: 8.394
    - type: nauc_map_at_100_diff1
      value: 53.64919999999999
    - type: nauc_map_at_1000_max
      value: 41.165600000000005
    - type: nauc_map_at_1000_std
      value: 8.3923
    - type: nauc_map_at_1000_diff1
      value: 53.654199999999996
    - type: nauc_recall_at_1_max
      value: 41.336
    - type: nauc_recall_at_1_std
      value: 4.9167000000000005
    - type: nauc_recall_at_1_diff1
      value: 59.489599999999996
    - type: nauc_recall_at_3_max
      value: 42.9746
    - type: nauc_recall_at_3_std
      value: 12.632399999999999
    - type: nauc_recall_at_3_diff1
      value: 50.259100000000004
    - type: nauc_recall_at_5_max
      value: 40.9855
    - type: nauc_recall_at_5_std
      value: 11.368300000000001
    - type: nauc_recall_at_5_diff1
      value: 47.3165
    - type: nauc_recall_at_10_max
      value: 38.6473
    - type: nauc_recall_at_10_std
      value: 13.1083
    - type: nauc_recall_at_10_diff1
      value: 43.1086
    - type: nauc_recall_at_20_max
      value: 36.0858
    - type: nauc_recall_at_20_std
      value: 16.345100000000002
    - type: nauc_recall_at_20_diff1
      value: 40.3971
    - type: nauc_recall_at_100_max
      value: 35.3344
    - type: nauc_recall_at_100_std
      value: 24.4293
    - type: nauc_recall_at_100_diff1
      value: 34.4263
    - type: nauc_recall_at_1000_max
      value: 27.814
    - type: nauc_recall_at_1000_std
      value: 34.5865
    - type: nauc_recall_at_1000_diff1
      value: 26.621
    - type: nauc_precision_at_1_max
      value: 41.336
    - type: nauc_precision_at_1_std
      value: 4.9167000000000005
    - type: nauc_precision_at_1_diff1
      value: 59.489599999999996
    - type: nauc_precision_at_3_max
      value: 42.9746
    - type: nauc_precision_at_3_std
      value: 12.632399999999999
    - type: nauc_precision_at_3_diff1
      value: 50.259100000000004
    - type: nauc_precision_at_5_max
      value: 40.9855
    - type: nauc_precision_at_5_std
      value: 11.368300000000001
    - type: nauc_precision_at_5_diff1
      value: 47.3165
    - type: nauc_precision_at_10_max
      value: 38.6473
    - type: nauc_precision_at_10_std
      value: 13.1083
    - type: nauc_precision_at_10_diff1
      value: 43.1086
    - type: nauc_precision_at_20_max
      value: 36.0858
    - type: nauc_precision_at_20_std
      value: 16.345100000000002
    - type: nauc_precision_at_20_diff1
      value: 40.3971
    - type: nauc_precision_at_100_max
      value: 35.3344
    - type: nauc_precision_at_100_std
      value: 24.4293
    - type: nauc_precision_at_100_diff1
      value: 34.4263
    - type: nauc_precision_at_1000_max
      value: 27.814
    - type: nauc_precision_at_1000_std
      value: 34.5865
    - type: nauc_precision_at_1000_diff1
      value: 26.621
    - type: nauc_mrr_at_1_max
      value: 41.336
    - type: nauc_mrr_at_1_std
      value: 4.9167000000000005
    - type: nauc_mrr_at_1_diff1
      value: 59.489599999999996
    - type: nauc_mrr_at_3_max
      value: 42.1793
    - type: nauc_mrr_at_3_std
      value: 8.149099999999999
    - type: nauc_mrr_at_3_diff1
      value: 55.1967
    - type: nauc_mrr_at_5_max
      value: 41.6768
    - type: nauc_mrr_at_5_std
      value: 7.8223
    - type: nauc_mrr_at_5_diff1
      value: 54.4705
    - type: nauc_mrr_at_10_max
      value: 41.3395
    - type: nauc_mrr_at_10_std
      value: 8.076
    - type: nauc_mrr_at_10_diff1
      value: 53.87929999999999
    - type: nauc_mrr_at_20_max
      value: 41.1762
    - type: nauc_mrr_at_20_std
      value: 8.2845
    - type: nauc_mrr_at_20_diff1
      value: 53.7144
    - type: nauc_mrr_at_100_max
      value: 41.1731
    - type: nauc_mrr_at_100_std
      value: 8.394
    - type: nauc_mrr_at_100_diff1
      value: 53.64919999999999
    - type: nauc_mrr_at_1000_max
      value: 41.165600000000005
    - type: nauc_mrr_at_1000_std
      value: 8.3923
    - type: nauc_mrr_at_1000_diff1
      value: 53.654199999999996
    - type: main_score
      value: 37.124
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
      value: 29.621
    - type: ndcg_at_3
      value: 36.388999999999996
    - type: ndcg_at_5
      value: 38.071
    - type: ndcg_at_10
      value: 39.856
    - type: ndcg_at_20
      value: 41.189
    - type: ndcg_at_100
      value: 43.391999999999996
    - type: ndcg_at_1000
      value: 45.080999999999996
    - type: map_at_1
      value: 29.621
    - type: map_at_3
      value: 34.733000000000004
    - type: map_at_5
      value: 35.668
    - type: map_at_10
      value: 36.411
    - type: map_at_20
      value: 36.778
    - type: map_at_100
      value: 37.077
    - type: map_at_1000
      value: 37.133
    - type: recall_at_1
      value: 29.621
    - type: recall_at_3
      value: 41.178
    - type: recall_at_5
      value: 45.257999999999996
    - type: recall_at_10
      value: 50.744
    - type: recall_at_20
      value: 56.001999999999995
    - type: recall_at_100
      value: 67.96
    - type: recall_at_1000
      value: 81.707
    - type: precision_at_1
      value: 29.621
    - type: precision_at_3
      value: 13.725999999999999
    - type: precision_at_5
      value: 9.052
    - type: precision_at_10
      value: 5.074
    - type: precision_at_20
      value: 2.8000000000000003
    - type: precision_at_100
      value: 0.6799999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 29.593799999999998
    - type: mrr_at_3
      value: 34.7254
    - type: mrr_at_5
      value: 35.6583
    - type: mrr_at_10
      value: 36.4022
    - type: mrr_at_20
      value: 36.7689
    - type: mrr_at_100
      value: 37.0681
    - type: mrr_at_1000
      value: 37.124
    - type: nauc_ndcg_at_1_max
      value: 39.7113
    - type: nauc_ndcg_at_1_std
      value: -1.3535
    - type: nauc_ndcg_at_1_diff1
      value: 57.7222
    - type: nauc_ndcg_at_3_max
      value: 40.4493
    - type: nauc_ndcg_at_3_std
      value: 1.4639
    - type: nauc_ndcg_at_3_diff1
      value: 52.145799999999994
    - type: nauc_ndcg_at_5_max
      value: 40.1219
    - type: nauc_ndcg_at_5_std
      value: 2.1448
    - type: nauc_ndcg_at_5_diff1
      value: 51.2694
    - type: nauc_ndcg_at_10_max
      value: 39.4187
    - type: nauc_ndcg_at_10_std
      value: 2.5085
    - type: nauc_ndcg_at_10_diff1
      value: 50.171699999999994
    - type: nauc_ndcg_at_20_max
      value: 39.2822
    - type: nauc_ndcg_at_20_std
      value: 3.1015
    - type: nauc_ndcg_at_20_diff1
      value: 49.8837
    - type: nauc_ndcg_at_100_max
      value: 39.1352
    - type: nauc_ndcg_at_100_std
      value: 3.8505
    - type: nauc_ndcg_at_100_diff1
      value: 49.7104
    - type: nauc_ndcg_at_1000_max
      value: 39.1441
    - type: nauc_ndcg_at_1000_std
      value: 4.1791
    - type: nauc_ndcg_at_1000_diff1
      value: 49.806200000000004
    - type: nauc_map_at_1_max
      value: 39.7113
    - type: nauc_map_at_1_std
      value: -1.3535
    - type: nauc_map_at_1_diff1
      value: 57.7222
    - type: nauc_map_at_3_max
      value: 40.3518
    - type: nauc_map_at_3_std
      value: 0.7879
    - type: nauc_map_at_3_diff1
      value: 53.4756
    - type: nauc_map_at_5_max
      value: 40.1793
    - type: nauc_map_at_5_std
      value: 1.1596
    - type: nauc_map_at_5_diff1
      value: 52.993900000000004
    - type: nauc_map_at_10_max
      value: 39.8893
    - type: nauc_map_at_10_std
      value: 1.3074000000000001
    - type: nauc_map_at_10_diff1
      value: 52.53679999999999
    - type: nauc_map_at_20_max
      value: 39.8583
    - type: nauc_map_at_20_std
      value: 1.4666000000000001
    - type: nauc_map_at_20_diff1
      value: 52.4664
    - type: nauc_map_at_100_max
      value: 39.8303
    - type: nauc_map_at_100_std
      value: 1.5578
    - type: nauc_map_at_100_diff1
      value: 52.44950000000001
    - type: nauc_map_at_1000_max
      value: 39.827400000000004
    - type: nauc_map_at_1000_std
      value: 1.568
    - type: nauc_map_at_1000_diff1
      value: 52.452600000000004
    - type: nauc_recall_at_1_max
      value: 39.7113
    - type: nauc_recall_at_1_std
      value: -1.3535
    - type: nauc_recall_at_1_diff1
      value: 57.7222
    - type: nauc_recall_at_3_max
      value: 40.6926
    - type: nauc_recall_at_3_std
      value: 3.3686000000000003
    - type: nauc_recall_at_3_diff1
      value: 48.4023
    - type: nauc_recall_at_5_max
      value: 39.8681
    - type: nauc_recall_at_5_std
      value: 5.0524
    - type: nauc_recall_at_5_diff1
      value: 46.2361
    - type: nauc_recall_at_10_max
      value: 37.6778
    - type: nauc_recall_at_10_std
      value: 6.2486
    - type: nauc_recall_at_10_diff1
      value: 42.7533
    - type: nauc_recall_at_20_max
      value: 36.9831
    - type: nauc_recall_at_20_std
      value: 8.9021
    - type: nauc_recall_at_20_diff1
      value: 41.1453
    - type: nauc_recall_at_100_max
      value: 35.6903
    - type: nauc_recall_at_100_std
      value: 15.161
    - type: nauc_recall_at_100_diff1
      value: 38.1673
    - type: nauc_recall_at_1000_max
      value: 34.2718
    - type: nauc_recall_at_1000_std
      value: 26.3982
    - type: nauc_recall_at_1000_diff1
      value: 33.3322
    - type: nauc_precision_at_1_max
      value: 39.7113
    - type: nauc_precision_at_1_std
      value: -1.3535
    - type: nauc_precision_at_1_diff1
      value: 57.7222
    - type: nauc_precision_at_3_max
      value: 40.6926
    - type: nauc_precision_at_3_std
      value: 3.3686000000000003
    - type: nauc_precision_at_3_diff1
      value: 48.4023
    - type: nauc_precision_at_5_max
      value: 39.8681
    - type: nauc_precision_at_5_std
      value: 5.0524
    - type: nauc_precision_at_5_diff1
      value: 46.2361
    - type: nauc_precision_at_10_max
      value: 37.6778
    - type: nauc_precision_at_10_std
      value: 6.2486
    - type: nauc_precision_at_10_diff1
      value: 42.7533
    - type: nauc_precision_at_20_max
      value: 36.9831
    - type: nauc_precision_at_20_std
      value: 8.9021
    - type: nauc_precision_at_20_diff1
      value: 41.1453
    - type: nauc_precision_at_100_max
      value: 35.6903
    - type: nauc_precision_at_100_std
      value: 15.161
    - type: nauc_precision_at_100_diff1
      value: 38.1673
    - type: nauc_precision_at_1000_max
      value: 34.2718
    - type: nauc_precision_at_1000_std
      value: 26.3982
    - type: nauc_precision_at_1000_diff1
      value: 33.3322
    - type: nauc_mrr_at_1_max
      value: 39.6284
    - type: nauc_mrr_at_1_std
      value: -1.345
    - type: nauc_mrr_at_1_diff1
      value: 57.828
    - type: nauc_mrr_at_3_max
      value: 40.3036
    - type: nauc_mrr_at_3_std
      value: 0.7952000000000001
    - type: nauc_mrr_at_3_diff1
      value: 53.524499999999996
    - type: nauc_mrr_at_5_max
      value: 40.1366
    - type: nauc_mrr_at_5_std
      value: 1.1708
    - type: nauc_mrr_at_5_diff1
      value: 53.0405
    - type: nauc_mrr_at_10_max
      value: 39.848
    - type: nauc_mrr_at_10_std
      value: 1.3195000000000001
    - type: nauc_mrr_at_10_diff1
      value: 52.5868
    - type: nauc_mrr_at_20_max
      value: 39.815400000000004
    - type: nauc_mrr_at_20_std
      value: 1.4787
    - type: nauc_mrr_at_20_diff1
      value: 52.513299999999994
    - type: nauc_mrr_at_100_max
      value: 39.787299999999995
    - type: nauc_mrr_at_100_std
      value: 1.5699999999999998
    - type: nauc_mrr_at_100_diff1
      value: 52.496500000000005
    - type: nauc_mrr_at_1000_max
      value: 39.7844
    - type: nauc_mrr_at_1000_std
      value: 1.5803
    - type: nauc_mrr_at_1000_diff1
      value: 52.4996
    - type: main_score
      value: 39.856
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
      value: 25.211
    - type: ndcg_at_3
      value: 31.994
    - type: ndcg_at_5
      value: 33.986
    - type: ndcg_at_10
      value: 36.086
    - type: ndcg_at_20
      value: 37.638
    - type: ndcg_at_100
      value: 40.268
    - type: ndcg_at_1000
      value: 42.309999999999995
    - type: map_at_1
      value: 25.211
    - type: map_at_3
      value: 30.346
    - type: map_at_5
      value: 31.452
    - type: map_at_10
      value: 32.323
    - type: map_at_20
      value: 32.751000000000005
    - type: map_at_100
      value: 33.097
    - type: map_at_1000
      value: 33.165
    - type: recall_at_1
      value: 25.211
    - type: recall_at_3
      value: 36.756
    - type: recall_at_5
      value: 41.587
    - type: recall_at_10
      value: 48.059000000000005
    - type: recall_at_20
      value: 54.189
    - type: recall_at_100
      value: 68.61
    - type: recall_at_1000
      value: 85.172
    - type: precision_at_1
      value: 25.211
    - type: precision_at_3
      value: 12.252
    - type: precision_at_5
      value: 8.317
    - type: precision_at_10
      value: 4.806
    - type: precision_at_20
      value: 2.709
    - type: precision_at_100
      value: 0.6859999999999999
    - type: precision_at_1000
      value: 0.08499999999999999
    - type: mrr_at_1
      value: 25.1962
    - type: mrr_at_3
      value: 30.335099999999997
    - type: mrr_at_5
      value: 31.4426
    - type: mrr_at_10
      value: 32.3121
    - type: mrr_at_20
      value: 32.741
    - type: mrr_at_100
      value: 33.0877
    - type: mrr_at_1000
      value: 33.1558
    - type: nauc_ndcg_at_1_max
      value: 38.358799999999995
    - type: nauc_ndcg_at_1_std
      value: 4.3283000000000005
    - type: nauc_ndcg_at_1_diff1
      value: 53.33520000000001
    - type: nauc_ndcg_at_3_max
      value: 38.0766
    - type: nauc_ndcg_at_3_std
      value: 6.0852
    - type: nauc_ndcg_at_3_diff1
      value: 45.5009
    - type: nauc_ndcg_at_5_max
      value: 37.788199999999996
    - type: nauc_ndcg_at_5_std
      value: 7.0073
    - type: nauc_ndcg_at_5_diff1
      value: 44.3577
    - type: nauc_ndcg_at_10_max
      value: 37.674
    - type: nauc_ndcg_at_10_std
      value: 7.954700000000001
    - type: nauc_ndcg_at_10_diff1
      value: 43.6869
    - type: nauc_ndcg_at_20_max
      value: 37.4368
    - type: nauc_ndcg_at_20_std
      value: 8.4592
    - type: nauc_ndcg_at_20_diff1
      value: 43.3112
    - type: nauc_ndcg_at_100_max
      value: 37.5955
    - type: nauc_ndcg_at_100_std
      value: 9.5313
    - type: nauc_ndcg_at_100_diff1
      value: 42.9187
    - type: nauc_ndcg_at_1000_max
      value: 37.8056
    - type: nauc_ndcg_at_1000_std
      value: 9.7477
    - type: nauc_ndcg_at_1000_diff1
      value: 43.3862
    - type: nauc_map_at_1_max
      value: 38.358799999999995
    - type: nauc_map_at_1_std
      value: 4.3283000000000005
    - type: nauc_map_at_1_diff1
      value: 53.33520000000001
    - type: nauc_map_at_3_max
      value: 38.1738
    - type: nauc_map_at_3_std
      value: 5.6814
    - type: nauc_map_at_3_diff1
      value: 47.229
    - type: nauc_map_at_5_max
      value: 38.005100000000006
    - type: nauc_map_at_5_std
      value: 6.1966
    - type: nauc_map_at_5_diff1
      value: 46.559200000000004
    - type: nauc_map_at_10_max
      value: 37.9741
    - type: nauc_map_at_10_std
      value: 6.5971
    - type: nauc_map_at_10_diff1
      value: 46.285
    - type: nauc_map_at_20_max
      value: 37.9009
    - type: nauc_map_at_20_std
      value: 6.7273
    - type: nauc_map_at_20_diff1
      value: 46.1825
    - type: nauc_map_at_100_max
      value: 37.9135
    - type: nauc_map_at_100_std
      value: 6.8602
    - type: nauc_map_at_100_diff1
      value: 46.1376
    - type: nauc_map_at_1000_max
      value: 37.918
    - type: nauc_map_at_1000_std
      value: 6.8636
    - type: nauc_map_at_1000_diff1
      value: 46.1515
    - type: nauc_recall_at_1_max
      value: 38.358799999999995
    - type: nauc_recall_at_1_std
      value: 4.3283000000000005
    - type: nauc_recall_at_1_diff1
      value: 53.33520000000001
    - type: nauc_recall_at_3_max
      value: 37.7993
    - type: nauc_recall_at_3_std
      value: 7.1854000000000005
    - type: nauc_recall_at_3_diff1
      value: 40.8217
    - type: nauc_recall_at_5_max
      value: 37.1564
    - type: nauc_recall_at_5_std
      value: 9.3324
    - type: nauc_recall_at_5_diff1
      value: 38.2991
    - type: nauc_recall_at_10_max
      value: 36.721399999999996
    - type: nauc_recall_at_10_std
      value: 12.1836
    - type: nauc_recall_at_10_diff1
      value: 36.1617
    - type: nauc_recall_at_20_max
      value: 35.7969
    - type: nauc_recall_at_20_std
      value: 14.4368
    - type: nauc_recall_at_20_diff1
      value: 34.3383
    - type: nauc_recall_at_100_max
      value: 36.6044
    - type: nauc_recall_at_100_std
      value: 23.055500000000002
    - type: nauc_recall_at_100_diff1
      value: 29.555500000000002
    - type: nauc_recall_at_1000_max
      value: 39.7315
    - type: nauc_recall_at_1000_std
      value: 38.601600000000005
    - type: nauc_recall_at_1000_diff1
      value: 26.7047
    - type: nauc_precision_at_1_max
      value: 38.358799999999995
    - type: nauc_precision_at_1_std
      value: 4.3283000000000005
    - type: nauc_precision_at_1_diff1
      value: 53.33520000000001
    - type: nauc_precision_at_3_max
      value: 37.7993
    - type: nauc_precision_at_3_std
      value: 7.1854000000000005
    - type: nauc_precision_at_3_diff1
      value: 40.8217
    - type: nauc_precision_at_5_max
      value: 37.1564
    - type: nauc_precision_at_5_std
      value: 9.3324
    - type: nauc_precision_at_5_diff1
      value: 38.2991
    - type: nauc_precision_at_10_max
      value: 36.721399999999996
    - type: nauc_precision_at_10_std
      value: 12.1836
    - type: nauc_precision_at_10_diff1
      value: 36.1617
    - type: nauc_precision_at_20_max
      value: 35.7969
    - type: nauc_precision_at_20_std
      value: 14.4368
    - type: nauc_precision_at_20_diff1
      value: 34.3383
    - type: nauc_precision_at_100_max
      value: 36.6044
    - type: nauc_precision_at_100_std
      value: 23.055500000000002
    - type: nauc_precision_at_100_diff1
      value: 29.555500000000002
    - type: nauc_precision_at_1000_max
      value: 39.7315
    - type: nauc_precision_at_1000_std
      value: 38.601600000000005
    - type: nauc_precision_at_1000_diff1
      value: 26.7047
    - type: nauc_mrr_at_1_max
      value: 38.3753
    - type: nauc_mrr_at_1_std
      value: 4.3651
    - type: nauc_mrr_at_1_diff1
      value: 53.3935
    - type: nauc_mrr_at_3_max
      value: 38.183299999999996
    - type: nauc_mrr_at_3_std
      value: 5.7071
    - type: nauc_mrr_at_3_diff1
      value: 47.2578
    - type: nauc_mrr_at_5_max
      value: 38.0161
    - type: nauc_mrr_at_5_std
      value: 6.2222
    - type: nauc_mrr_at_5_diff1
      value: 46.5907
    - type: nauc_mrr_at_10_max
      value: 37.9882
    - type: nauc_mrr_at_10_std
      value: 6.6221000000000005
    - type: nauc_mrr_at_10_diff1
      value: 46.3178
    - type: nauc_mrr_at_20_max
      value: 37.912
    - type: nauc_mrr_at_20_std
      value: 6.752700000000001
    - type: nauc_mrr_at_20_diff1
      value: 46.2141
    - type: nauc_mrr_at_100_max
      value: 37.9247
    - type: nauc_mrr_at_100_std
      value: 6.8857
    - type: nauc_mrr_at_100_diff1
      value: 46.169399999999996
    - type: nauc_mrr_at_1000_max
      value: 37.9292
    - type: nauc_mrr_at_1000_std
      value: 6.889099999999999
    - type: nauc_mrr_at_1000_diff1
      value: 46.1833
    - type: main_score
      value: 36.086
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
      value: 41.059
    - type: ndcg_at_3
      value: 45.091
    - type: ndcg_at_5
      value: 47.754000000000005
    - type: ndcg_at_10
      value: 50.403
    - type: ndcg_at_20
      value: 52.629999999999995
    - type: ndcg_at_100
      value: 55.669999999999995
    - type: ndcg_at_1000
      value: 57.645
    - type: map_at_1
      value: 33.304
    - type: map_at_3
      value: 40.428999999999995
    - type: map_at_5
      value: 42.638999999999996
    - type: map_at_10
      value: 44.239
    - type: map_at_20
      value: 45.144
    - type: map_at_100
      value: 45.783
    - type: map_at_1000
      value: 45.911
    - type: recall_at_1
      value: 33.304
    - type: recall_at_3
      value: 46.509
    - type: recall_at_5
      value: 53.849999999999994
    - type: recall_at_10
      value: 61.694
    - type: recall_at_20
      value: 69.708
    - type: recall_at_100
      value: 83.314
    - type: recall_at_1000
      value: 95.955
    - type: precision_at_1
      value: 41.059
    - type: precision_at_3
      value: 21.316
    - type: precision_at_5
      value: 15.651000000000002
    - type: precision_at_10
      value: 9.642000000000001
    - type: precision_at_20
      value: 5.744
    - type: precision_at_100
      value: 1.538
    - type: precision_at_1000
      value: 0.20500000000000002
    - type: mrr_at_1
      value: 41.058699999999995
    - type: mrr_at_3
      value: 47.258
    - type: mrr_at_5
      value: 49.082
    - type: mrr_at_10
      value: 50.0836
    - type: mrr_at_20
      value: 50.5221
    - type: mrr_at_100
      value: 50.8217
    - type: mrr_at_1000
      value: 50.8713
    - type: nauc_ndcg_at_1_max
      value: 40.6525
    - type: nauc_ndcg_at_1_std
      value: -9.376
    - type: nauc_ndcg_at_1_diff1
      value: 50.0125
    - type: nauc_ndcg_at_3_max
      value: 40.9809
    - type: nauc_ndcg_at_3_std
      value: -7.1297
    - type: nauc_ndcg_at_3_diff1
      value: 47.0051
    - type: nauc_ndcg_at_5_max
      value: 40.037800000000004
    - type: nauc_ndcg_at_5_std
      value: -4.3972999999999995
    - type: nauc_ndcg_at_5_diff1
      value: 45.8909
    - type: nauc_ndcg_at_10_max
      value: 39.939400000000006
    - type: nauc_ndcg_at_10_std
      value: -4.5747
    - type: nauc_ndcg_at_10_diff1
      value: 45.0088
    - type: nauc_ndcg_at_20_max
      value: 40.144999999999996
    - type: nauc_ndcg_at_20_std
      value: -4.2649
    - type: nauc_ndcg_at_20_diff1
      value: 45.6565
    - type: nauc_ndcg_at_100_max
      value: 41.2015
    - type: nauc_ndcg_at_100_std
      value: -3.0772
    - type: nauc_ndcg_at_100_diff1
      value: 45.8564
    - type: nauc_ndcg_at_1000_max
      value: 41.2273
    - type: nauc_ndcg_at_1000_std
      value: -3.8580000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 46.0075
    - type: nauc_map_at_1_max
      value: 33.681400000000004
    - type: nauc_map_at_1_std
      value: -10.792499999999999
    - type: nauc_map_at_1_diff1
      value: 51.6292
    - type: nauc_map_at_3_max
      value: 38.5132
    - type: nauc_map_at_3_std
      value: -9.085899999999999
    - type: nauc_map_at_3_diff1
      value: 48.516
    - type: nauc_map_at_5_max
      value: 38.7849
    - type: nauc_map_at_5_std
      value: -7.2336
    - type: nauc_map_at_5_diff1
      value: 47.9868
    - type: nauc_map_at_10_max
      value: 39.3231
    - type: nauc_map_at_10_std
      value: -7.1676
    - type: nauc_map_at_10_diff1
      value: 47.446
    - type: nauc_map_at_20_max
      value: 39.589
    - type: nauc_map_at_20_std
      value: -6.8943
    - type: nauc_map_at_20_diff1
      value: 47.4397
    - type: nauc_map_at_100_max
      value: 39.875
    - type: nauc_map_at_100_std
      value: -6.549199999999999
    - type: nauc_map_at_100_diff1
      value: 47.4459
    - type: nauc_map_at_1000_max
      value: 39.8847
    - type: nauc_map_at_1000_std
      value: -6.5965
    - type: nauc_map_at_1000_diff1
      value: 47.4298
    - type: nauc_recall_at_1_max
      value: 33.681400000000004
    - type: nauc_recall_at_1_std
      value: -10.792499999999999
    - type: nauc_recall_at_1_diff1
      value: 51.6292
    - type: nauc_recall_at_3_max
      value: 37.3654
    - type: nauc_recall_at_3_std
      value: -6.1476999999999995
    - type: nauc_recall_at_3_diff1
      value: 43.147400000000005
    - type: nauc_recall_at_5_max
      value: 35.3328
    - type: nauc_recall_at_5_std
      value: 1.0517
    - type: nauc_recall_at_5_diff1
      value: 39.7709
    - type: nauc_recall_at_10_max
      value: 34.6109
    - type: nauc_recall_at_10_std
      value: 1.5653000000000001
    - type: nauc_recall_at_10_diff1
      value: 35.5858
    - type: nauc_recall_at_20_max
      value: 34.2941
    - type: nauc_recall_at_20_std
      value: 3.9570000000000003
    - type: nauc_recall_at_20_diff1
      value: 36.910199999999996
    - type: nauc_recall_at_100_max
      value: 41.6344
    - type: nauc_recall_at_100_std
      value: 18.614
    - type: nauc_recall_at_100_diff1
      value: 35.9742
    - type: nauc_recall_at_1000_max
      value: 53.67960000000001
    - type: nauc_recall_at_1000_std
      value: 46.8911
    - type: nauc_recall_at_1000_diff1
      value: 35.167500000000004
    - type: nauc_precision_at_1_max
      value: 40.6525
    - type: nauc_precision_at_1_std
      value: -9.376
    - type: nauc_precision_at_1_diff1
      value: 50.0125
    - type: nauc_precision_at_3_max
      value: 40.7269
    - type: nauc_precision_at_3_std
      value: -1.2473
    - type: nauc_precision_at_3_diff1
      value: 31.521500000000003
    - type: nauc_precision_at_5_max
      value: 34.9193
    - type: nauc_precision_at_5_std
      value: 6.758699999999999
    - type: nauc_precision_at_5_diff1
      value: 20.958399999999997
    - type: nauc_precision_at_10_max
      value: 29.1675
    - type: nauc_precision_at_10_std
      value: 8.4146
    - type: nauc_precision_at_10_diff1
      value: 9.517000000000001
    - type: nauc_precision_at_20_max
      value: 23.0603
    - type: nauc_precision_at_20_std
      value: 9.5615
    - type: nauc_precision_at_20_diff1
      value: 3.3520000000000003
    - type: nauc_precision_at_100_max
      value: 10.3906
    - type: nauc_precision_at_100_std
      value: 8.8378
    - type: nauc_precision_at_100_diff1
      value: -8.2594
    - type: nauc_precision_at_1000_max
      value: -4.7287
    - type: nauc_precision_at_1000_std
      value: -2.5721000000000003
    - type: nauc_precision_at_1000_diff1
      value: -19.5341
    - type: nauc_mrr_at_1_max
      value: 40.6525
    - type: nauc_mrr_at_1_std
      value: -9.376
    - type: nauc_mrr_at_1_diff1
      value: 50.0125
    - type: nauc_mrr_at_3_max
      value: 42.4409
    - type: nauc_mrr_at_3_std
      value: -7.4642
    - type: nauc_mrr_at_3_diff1
      value: 47.773199999999996
    - type: nauc_mrr_at_5_max
      value: 41.8687
    - type: nauc_mrr_at_5_std
      value: -6.0165999999999995
    - type: nauc_mrr_at_5_diff1
      value: 46.929500000000004
    - type: nauc_mrr_at_10_max
      value: 41.6607
    - type: nauc_mrr_at_10_std
      value: -5.8776
    - type: nauc_mrr_at_10_diff1
      value: 46.5117
    - type: nauc_mrr_at_20_max
      value: 41.6088
    - type: nauc_mrr_at_20_std
      value: -6.0403
    - type: nauc_mrr_at_20_diff1
      value: 46.7355
    - type: nauc_mrr_at_100_max
      value: 41.6881
    - type: nauc_mrr_at_100_std
      value: -6.0445
    - type: nauc_mrr_at_100_diff1
      value: 46.7504
    - type: nauc_mrr_at_1000_max
      value: 41.6981
    - type: nauc_mrr_at_1000_std
      value: -6.0584
    - type: nauc_mrr_at_1000_diff1
      value: 46.7686
    - type: main_score
      value: 50.403
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
      value: 32.293
    - type: ndcg_at_3
      value: 35.357
    - type: ndcg_at_5
      value: 37.135
    - type: ndcg_at_10
      value: 39.682
    - type: ndcg_at_20
      value: 41.477000000000004
    - type: ndcg_at_100
      value: 44.594
    - type: ndcg_at_1000
      value: 46.938
    - type: map_at_1
      value: 25.084
    - type: map_at_3
      value: 31.134
    - type: map_at_5
      value: 32.693
    - type: map_at_10
      value: 34.072
    - type: map_at_20
      value: 34.719
    - type: map_at_100
      value: 35.327999999999996
    - type: map_at_1000
      value: 35.461
    - type: recall_at_1
      value: 25.084
    - type: recall_at_3
      value: 36.678
    - type: recall_at_5
      value: 41.839999999999996
    - type: recall_at_10
      value: 49.782
    - type: recall_at_20
      value: 56.442
    - type: recall_at_100
      value: 71.114
    - type: recall_at_1000
      value: 86.372
    - type: precision_at_1
      value: 32.293
    - type: precision_at_3
      value: 17.452
    - type: precision_at_5
      value: 12.446
    - type: precision_at_10
      value: 7.758
    - type: precision_at_20
      value: 4.634
    - type: precision_at_100
      value: 1.324
    - type: precision_at_1000
      value: 0.184
    - type: mrr_at_1
      value: 32.293
    - type: mrr_at_3
      value: 37.8344
    - type: mrr_at_5
      value: 39.0223
    - type: mrr_at_10
      value: 40.1805
    - type: mrr_at_20
      value: 40.6083
    - type: mrr_at_100
      value: 40.928799999999995
    - type: mrr_at_1000
      value: 40.9754
    - type: nauc_ndcg_at_1_max
      value: 45.3161
    - type: nauc_ndcg_at_1_std
      value: 4.444
    - type: nauc_ndcg_at_1_diff1
      value: 46.0858
    - type: nauc_ndcg_at_3_max
      value: 46.1152
    - type: nauc_ndcg_at_3_std
      value: 3.2603
    - type: nauc_ndcg_at_3_diff1
      value: 42.6324
    - type: nauc_ndcg_at_5_max
      value: 46.3649
    - type: nauc_ndcg_at_5_std
      value: 2.5442
    - type: nauc_ndcg_at_5_diff1
      value: 42.9534
    - type: nauc_ndcg_at_10_max
      value: 45.9638
    - type: nauc_ndcg_at_10_std
      value: 3.849
    - type: nauc_ndcg_at_10_diff1
      value: 42.3058
    - type: nauc_ndcg_at_20_max
      value: 45.6402
    - type: nauc_ndcg_at_20_std
      value: 4.6758
    - type: nauc_ndcg_at_20_diff1
      value: 41.8551
    - type: nauc_ndcg_at_100_max
      value: 45.7963
    - type: nauc_ndcg_at_100_std
      value: 6.154599999999999
    - type: nauc_ndcg_at_100_diff1
      value: 41.1414
    - type: nauc_ndcg_at_1000_max
      value: 45.9794
    - type: nauc_ndcg_at_1000_std
      value: 6.9567000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 40.8964
    - type: nauc_map_at_1_max
      value: 40.1856
    - type: nauc_map_at_1_std
      value: -4.0307
    - type: nauc_map_at_1_diff1
      value: 49.675999999999995
    - type: nauc_map_at_3_max
      value: 43.8311
    - type: nauc_map_at_3_std
      value: -1.2912
    - type: nauc_map_at_3_diff1
      value: 45.9441
    - type: nauc_map_at_5_max
      value: 44.818400000000004
    - type: nauc_map_at_5_std
      value: -0.7452000000000001
    - type: nauc_map_at_5_diff1
      value: 45.6591
    - type: nauc_map_at_10_max
      value: 44.9988
    - type: nauc_map_at_10_std
      value: 0.41960000000000003
    - type: nauc_map_at_10_diff1
      value: 45.1582
    - type: nauc_map_at_20_max
      value: 45.0395
    - type: nauc_map_at_20_std
      value: 0.9468000000000001
    - type: nauc_map_at_20_diff1
      value: 44.890600000000006
    - type: nauc_map_at_100_max
      value: 45.311
    - type: nauc_map_at_100_std
      value: 1.5421
    - type: nauc_map_at_100_diff1
      value: 44.7203
    - type: nauc_map_at_1000_max
      value: 45.364399999999996
    - type: nauc_map_at_1000_std
      value: 1.6643000000000001
    - type: nauc_map_at_1000_diff1
      value: 44.6926
    - type: nauc_recall_at_1_max
      value: 40.1856
    - type: nauc_recall_at_1_std
      value: -4.0307
    - type: nauc_recall_at_1_diff1
      value: 49.675999999999995
    - type: nauc_recall_at_3_max
      value: 43.0698
    - type: nauc_recall_at_3_std
      value: 0.4071
    - type: nauc_recall_at_3_diff1
      value: 39.6364
    - type: nauc_recall_at_5_max
      value: 44.056200000000004
    - type: nauc_recall_at_5_std
      value: 0.6597000000000001
    - type: nauc_recall_at_5_diff1
      value: 38.5431
    - type: nauc_recall_at_10_max
      value: 42.5643
    - type: nauc_recall_at_10_std
      value: 5.446899999999999
    - type: nauc_recall_at_10_diff1
      value: 35.3363
    - type: nauc_recall_at_20_max
      value: 40.9176
    - type: nauc_recall_at_20_std
      value: 8.6434
    - type: nauc_recall_at_20_diff1
      value: 33.0525
    - type: nauc_recall_at_100_max
      value: 41.2899
    - type: nauc_recall_at_100_std
      value: 17.3979
    - type: nauc_recall_at_100_diff1
      value: 28.0707
    - type: nauc_recall_at_1000_max
      value: 43.2786
    - type: nauc_recall_at_1000_std
      value: 33.6676
    - type: nauc_recall_at_1000_diff1
      value: 19.6489
    - type: nauc_precision_at_1_max
      value: 45.3161
    - type: nauc_precision_at_1_std
      value: 4.444
    - type: nauc_precision_at_1_diff1
      value: 46.0858
    - type: nauc_precision_at_3_max
      value: 45.937400000000004
    - type: nauc_precision_at_3_std
      value: 13.606599999999998
    - type: nauc_precision_at_3_diff1
      value: 28.8887
    - type: nauc_precision_at_5_max
      value: 43.6409
    - type: nauc_precision_at_5_std
      value: 15.3222
    - type: nauc_precision_at_5_diff1
      value: 23.5428
    - type: nauc_precision_at_10_max
      value: 38.8973
    - type: nauc_precision_at_10_std
      value: 21.049300000000002
    - type: nauc_precision_at_10_diff1
      value: 15.912200000000002
    - type: nauc_precision_at_20_max
      value: 33.1485
    - type: nauc_precision_at_20_std
      value: 26.1451
    - type: nauc_precision_at_20_diff1
      value: 7.7276
    - type: nauc_precision_at_100_max
      value: 24.1577
    - type: nauc_precision_at_100_std
      value: 31.4656
    - type: nauc_precision_at_100_diff1
      value: -4.0066999999999995
    - type: nauc_precision_at_1000_max
      value: 12.3639
    - type: nauc_precision_at_1000_std
      value: 28.9285
    - type: nauc_precision_at_1000_diff1
      value: -11.7577
    - type: nauc_mrr_at_1_max
      value: 45.3161
    - type: nauc_mrr_at_1_std
      value: 4.444
    - type: nauc_mrr_at_1_diff1
      value: 46.0858
    - type: nauc_mrr_at_3_max
      value: 45.9129
    - type: nauc_mrr_at_3_std
      value: 5.743
    - type: nauc_mrr_at_3_diff1
      value: 41.6507
    - type: nauc_mrr_at_5_max
      value: 45.8273
    - type: nauc_mrr_at_5_std
      value: 5.57
    - type: nauc_mrr_at_5_diff1
      value: 41.531400000000005
    - type: nauc_mrr_at_10_max
      value: 45.8144
    - type: nauc_mrr_at_10_std
      value: 6.263000000000001
    - type: nauc_mrr_at_10_diff1
      value: 41.2348
    - type: nauc_mrr_at_20_max
      value: 45.7975
    - type: nauc_mrr_at_20_std
      value: 6.392200000000001
    - type: nauc_mrr_at_20_diff1
      value: 41.259499999999996
    - type: nauc_mrr_at_100_max
      value: 45.7286
    - type: nauc_mrr_at_100_std
      value: 6.456099999999999
    - type: nauc_mrr_at_100_diff1
      value: 41.185100000000006
    - type: nauc_mrr_at_1000_max
      value: 45.7325
    - type: nauc_mrr_at_1000_std
      value: 6.4614
    - type: nauc_mrr_at_1000_diff1
      value: 41.188
    - type: main_score
      value: 39.682
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
      value: 41.379
    - type: ndcg_at_3
      value: 48.789
    - type: ndcg_at_5
      value: 51.535
    - type: ndcg_at_10
      value: 53.654999999999994
    - type: ndcg_at_20
      value: 55.559999999999995
    - type: ndcg_at_100
      value: 57.911
    - type: ndcg_at_1000
      value: 59.275
    - type: map_at_1
      value: 36.224000000000004
    - type: map_at_3
      value: 45.190999999999995
    - type: map_at_5
      value: 47.012
    - type: map_at_10
      value: 48.141
    - type: map_at_20
      value: 48.802
    - type: map_at_100
      value: 49.214
    - type: map_at_1000
      value: 49.278
    - type: recall_at_1
      value: 36.224000000000004
    - type: recall_at_3
      value: 53.513
    - type: recall_at_5
      value: 60.221000000000004
    - type: recall_at_10
      value: 66.346
    - type: recall_at_20
      value: 73.359
    - type: recall_at_100
      value: 84.77
    - type: recall_at_1000
      value: 94.547
    - type: precision_at_1
      value: 41.379
    - type: precision_at_3
      value: 21.902
    - type: precision_at_5
      value: 15.197
    - type: precision_at_10
      value: 8.639
    - type: precision_at_20
      value: 4.887
    - type: precision_at_100
      value: 1.164
    - type: precision_at_1000
      value: 0.133
    - type: mrr_at_1
      value: 41.3793
    - type: mrr_at_3
      value: 49.0282
    - type: mrr_at_5
      value: 50.7022
    - type: mrr_at_10
      value: 51.462399999999995
    - type: mrr_at_20
      value: 51.9372
    - type: mrr_at_100
      value: 52.1984
    - type: mrr_at_1000
      value: 52.2374
    - type: nauc_ndcg_at_1_max
      value: 45.521499999999996
    - type: nauc_ndcg_at_1_std
      value: -3.2632000000000003
    - type: nauc_ndcg_at_1_diff1
      value: 55.017799999999994
    - type: nauc_ndcg_at_3_max
      value: 43.343399999999995
    - type: nauc_ndcg_at_3_std
      value: -4.4684
    - type: nauc_ndcg_at_3_diff1
      value: 49.7562
    - type: nauc_ndcg_at_5_max
      value: 44.034600000000005
    - type: nauc_ndcg_at_5_std
      value: -2.8813
    - type: nauc_ndcg_at_5_diff1
      value: 48.7767
    - type: nauc_ndcg_at_10_max
      value: 45.0674
    - type: nauc_ndcg_at_10_std
      value: -1.332
    - type: nauc_ndcg_at_10_diff1
      value: 48.448600000000006
    - type: nauc_ndcg_at_20_max
      value: 45.6717
    - type: nauc_ndcg_at_20_std
      value: 0.0107
    - type: nauc_ndcg_at_20_diff1
      value: 48.6492
    - type: nauc_ndcg_at_100_max
      value: 45.974
    - type: nauc_ndcg_at_100_std
      value: 1.1665999999999999
    - type: nauc_ndcg_at_100_diff1
      value: 48.9852
    - type: nauc_ndcg_at_1000_max
      value: 46.0653
    - type: nauc_ndcg_at_1000_std
      value: 0.7539
    - type: nauc_ndcg_at_1000_diff1
      value: 49.453399999999995
    - type: nauc_map_at_1_max
      value: 39.5162
    - type: nauc_map_at_1_std
      value: -4.4784
    - type: nauc_map_at_1_diff1
      value: 54.076
    - type: nauc_map_at_3_max
      value: 42.022999999999996
    - type: nauc_map_at_3_std
      value: -5.5131
    - type: nauc_map_at_3_diff1
      value: 50.727199999999996
    - type: nauc_map_at_5_max
      value: 42.700700000000005
    - type: nauc_map_at_5_std
      value: -4.3487
    - type: nauc_map_at_5_diff1
      value: 50.058499999999995
    - type: nauc_map_at_10_max
      value: 43.4533
    - type: nauc_map_at_10_std
      value: -3.3632000000000004
    - type: nauc_map_at_10_diff1
      value: 49.8247
    - type: nauc_map_at_20_max
      value: 43.7821
    - type: nauc_map_at_20_std
      value: -2.8057
    - type: nauc_map_at_20_diff1
      value: 49.8795
    - type: nauc_map_at_100_max
      value: 43.9125
    - type: nauc_map_at_100_std
      value: -2.5162
    - type: nauc_map_at_100_diff1
      value: 49.9437
    - type: nauc_map_at_1000_max
      value: 43.9371
    - type: nauc_map_at_1000_std
      value: -2.5118
    - type: nauc_map_at_1000_diff1
      value: 49.973600000000005
    - type: nauc_recall_at_1_max
      value: 39.5162
    - type: nauc_recall_at_1_std
      value: -4.4784
    - type: nauc_recall_at_1_diff1
      value: 54.076
    - type: nauc_recall_at_3_max
      value: 40.1719
    - type: nauc_recall_at_3_std
      value: -5.8908000000000005
    - type: nauc_recall_at_3_diff1
      value: 46.1075
    - type: nauc_recall_at_5_max
      value: 41.3221
    - type: nauc_recall_at_5_std
      value: -1.7418
    - type: nauc_recall_at_5_diff1
      value: 42.4571
    - type: nauc_recall_at_10_max
      value: 44.1382
    - type: nauc_recall_at_10_std
      value: 3.0869
    - type: nauc_recall_at_10_diff1
      value: 40.6674
    - type: nauc_recall_at_20_max
      value: 47.0264
    - type: nauc_recall_at_20_std
      value: 10.7409
    - type: nauc_recall_at_20_diff1
      value: 39.8838
    - type: nauc_recall_at_100_max
      value: 49.660700000000006
    - type: nauc_recall_at_100_std
      value: 26.1413
    - type: nauc_recall_at_100_diff1
      value: 38.1192
    - type: nauc_recall_at_1000_max
      value: 58.9341
    - type: nauc_recall_at_1000_std
      value: 47.4146
    - type: nauc_recall_at_1000_diff1
      value: 39.7378
    - type: nauc_precision_at_1_max
      value: 45.521499999999996
    - type: nauc_precision_at_1_std
      value: -3.2632000000000003
    - type: nauc_precision_at_1_diff1
      value: 55.017799999999994
    - type: nauc_precision_at_3_max
      value: 41.9576
    - type: nauc_precision_at_3_std
      value: 0.3431
    - type: nauc_precision_at_3_diff1
      value: 33.5013
    - type: nauc_precision_at_5_max
      value: 41.024
    - type: nauc_precision_at_5_std
      value: 6.962400000000001
    - type: nauc_precision_at_5_diff1
      value: 26.0905
    - type: nauc_precision_at_10_max
      value: 38.4505
    - type: nauc_precision_at_10_std
      value: 13.459
    - type: nauc_precision_at_10_diff1
      value: 18.2984
    - type: nauc_precision_at_20_max
      value: 35.6898
    - type: nauc_precision_at_20_std
      value: 19.7287
    - type: nauc_precision_at_20_diff1
      value: 12.3455
    - type: nauc_precision_at_100_max
      value: 29.284
    - type: nauc_precision_at_100_std
      value: 26.509100000000004
    - type: nauc_precision_at_100_diff1
      value: 4.118200000000001
    - type: nauc_precision_at_1000_max
      value: 22.5188
    - type: nauc_precision_at_1000_std
      value: 26.6978
    - type: nauc_precision_at_1000_diff1
      value: -2.4383
    - type: nauc_mrr_at_1_max
      value: 45.521499999999996
    - type: nauc_mrr_at_1_std
      value: -3.2632000000000003
    - type: nauc_mrr_at_1_diff1
      value: 55.017799999999994
    - type: nauc_mrr_at_3_max
      value: 45.2583
    - type: nauc_mrr_at_3_std
      value: -4.0796
    - type: nauc_mrr_at_3_diff1
      value: 51.3842
    - type: nauc_mrr_at_5_max
      value: 45.683099999999996
    - type: nauc_mrr_at_5_std
      value: -3.0403
    - type: nauc_mrr_at_5_diff1
      value: 50.928
    - type: nauc_mrr_at_10_max
      value: 46.0254
    - type: nauc_mrr_at_10_std
      value: -2.5618
    - type: nauc_mrr_at_10_diff1
      value: 50.9016
    - type: nauc_mrr_at_20_max
      value: 46.1397
    - type: nauc_mrr_at_20_std
      value: -2.2378
    - type: nauc_mrr_at_20_diff1
      value: 50.983900000000006
    - type: nauc_mrr_at_100_max
      value: 46.0813
    - type: nauc_mrr_at_100_std
      value: -2.1819
    - type: nauc_mrr_at_100_diff1
      value: 50.9924
    - type: nauc_mrr_at_1000_max
      value: 46.075700000000005
    - type: nauc_mrr_at_1000_std
      value: -2.2086
    - type: nauc_mrr_at_1000_diff1
      value: 51.004400000000004
    - type: main_score
      value: 53.654999999999994
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
      value: 28.701
    - type: ndcg_at_3
      value: 35.095
    - type: ndcg_at_5
      value: 37.533
    - type: ndcg_at_10
      value: 40.224
    - type: ndcg_at_20
      value: 41.818
    - type: ndcg_at_100
      value: 44.651999999999994
    - type: ndcg_at_1000
      value: 47.05
    - type: map_at_1
      value: 26.251
    - type: map_at_3
      value: 32.49
    - type: map_at_5
      value: 33.931
    - type: map_at_10
      value: 35.154
    - type: map_at_20
      value: 35.641
    - type: map_at_100
      value: 36.032
    - type: map_at_1000
      value: 36.132
    - type: recall_at_1
      value: 26.251
    - type: recall_at_3
      value: 39.76
    - type: recall_at_5
      value: 45.739999999999995
    - type: recall_at_10
      value: 53.698
    - type: recall_at_20
      value: 59.48
    - type: recall_at_100
      value: 74.298
    - type: recall_at_1000
      value: 92.06299999999999
    - type: precision_at_1
      value: 28.701
    - type: precision_at_3
      value: 14.953
    - type: precision_at_5
      value: 10.328
    - type: precision_at_10
      value: 6.158
    - type: precision_at_20
      value: 3.469
    - type: precision_at_100
      value: 0.886
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: mrr_at_1
      value: 28.700599999999998
    - type: mrr_at_3
      value: 34.9906
    - type: mrr_at_5
      value: 36.3917
    - type: mrr_at_10
      value: 37.4735
    - type: mrr_at_20
      value: 37.896
    - type: mrr_at_100
      value: 38.229600000000005
    - type: mrr_at_1000
      value: 38.3107
    - type: nauc_ndcg_at_1_max
      value: 35.5663
    - type: nauc_ndcg_at_1_std
      value: -11.130700000000001
    - type: nauc_ndcg_at_1_diff1
      value: 47.2971
    - type: nauc_ndcg_at_3_max
      value: 33.591300000000004
    - type: nauc_ndcg_at_3_std
      value: -8.8712
    - type: nauc_ndcg_at_3_diff1
      value: 43.9366
    - type: nauc_ndcg_at_5_max
      value: 32.8546
    - type: nauc_ndcg_at_5_std
      value: -7.764799999999999
    - type: nauc_ndcg_at_5_diff1
      value: 42.896699999999996
    - type: nauc_ndcg_at_10_max
      value: 33.8862
    - type: nauc_ndcg_at_10_std
      value: -5.8975
    - type: nauc_ndcg_at_10_diff1
      value: 42.0493
    - type: nauc_ndcg_at_20_max
      value: 34.4891
    - type: nauc_ndcg_at_20_std
      value: -4.7832
    - type: nauc_ndcg_at_20_diff1
      value: 41.857499999999995
    - type: nauc_ndcg_at_100_max
      value: 34.2737
    - type: nauc_ndcg_at_100_std
      value: -4.8904000000000005
    - type: nauc_ndcg_at_100_diff1
      value: 41.3476
    - type: nauc_ndcg_at_1000_max
      value: 34.031800000000004
    - type: nauc_ndcg_at_1000_std
      value: -5.5376
    - type: nauc_ndcg_at_1000_diff1
      value: 41.8603
    - type: nauc_map_at_1_max
      value: 33.128299999999996
    - type: nauc_map_at_1_std
      value: -12.1157
    - type: nauc_map_at_1_diff1
      value: 49.8448
    - type: nauc_map_at_3_max
      value: 33.283699999999996
    - type: nauc_map_at_3_std
      value: -9.7518
    - type: nauc_map_at_3_diff1
      value: 45.4875
    - type: nauc_map_at_5_max
      value: 32.9355
    - type: nauc_map_at_5_std
      value: -9.1755
    - type: nauc_map_at_5_diff1
      value: 44.8675
    - type: nauc_map_at_10_max
      value: 33.5532
    - type: nauc_map_at_10_std
      value: -8.3763
    - type: nauc_map_at_10_diff1
      value: 44.670700000000004
    - type: nauc_map_at_20_max
      value: 33.8065
    - type: nauc_map_at_20_std
      value: -8.0253
    - type: nauc_map_at_20_diff1
      value: 44.5987
    - type: nauc_map_at_100_max
      value: 33.7647
    - type: nauc_map_at_100_std
      value: -8.0399
    - type: nauc_map_at_100_diff1
      value: 44.5212
    - type: nauc_map_at_1000_max
      value: 33.752700000000004
    - type: nauc_map_at_1000_std
      value: -8.0557
    - type: nauc_map_at_1000_diff1
      value: 44.5285
    - type: nauc_recall_at_1_max
      value: 33.128299999999996
    - type: nauc_recall_at_1_std
      value: -12.1157
    - type: nauc_recall_at_1_diff1
      value: 49.8448
    - type: nauc_recall_at_3_max
      value: 31.5403
    - type: nauc_recall_at_3_std
      value: -6.862699999999999
    - type: nauc_recall_at_3_diff1
      value: 40.4438
    - type: nauc_recall_at_5_max
      value: 29.549300000000002
    - type: nauc_recall_at_5_std
      value: -4.8186
    - type: nauc_recall_at_5_diff1
      value: 37.7652
    - type: nauc_recall_at_10_max
      value: 32.0106
    - type: nauc_recall_at_10_std
      value: 1.1384999999999998
    - type: nauc_recall_at_10_diff1
      value: 34.4037
    - type: nauc_recall_at_20_max
      value: 34.1547
    - type: nauc_recall_at_20_std
      value: 6.0514
    - type: nauc_recall_at_20_diff1
      value: 33.4793
    - type: nauc_recall_at_100_max
      value: 32.610099999999996
    - type: nauc_recall_at_100_std
      value: 9.046899999999999
    - type: nauc_recall_at_100_diff1
      value: 27.256999999999998
    - type: nauc_recall_at_1000_max
      value: 26.3079
    - type: nauc_recall_at_1000_std
      value: 16.963900000000002
    - type: nauc_recall_at_1000_diff1
      value: 22.1857
    - type: nauc_precision_at_1_max
      value: 35.5663
    - type: nauc_precision_at_1_std
      value: -11.130700000000001
    - type: nauc_precision_at_1_diff1
      value: 47.2971
    - type: nauc_precision_at_3_max
      value: 34.8919
    - type: nauc_precision_at_3_std
      value: -4.6598
    - type: nauc_precision_at_3_diff1
      value: 36.1773
    - type: nauc_precision_at_5_max
      value: 32.9054
    - type: nauc_precision_at_5_std
      value: -2.0126999999999997
    - type: nauc_precision_at_5_diff1
      value: 32.6994
    - type: nauc_precision_at_10_max
      value: 33.683600000000006
    - type: nauc_precision_at_10_std
      value: 3.2531999999999996
    - type: nauc_precision_at_10_diff1
      value: 28.099800000000002
    - type: nauc_precision_at_20_max
      value: 33.7297
    - type: nauc_precision_at_20_std
      value: 7.0116
    - type: nauc_precision_at_20_diff1
      value: 23.663999999999998
    - type: nauc_precision_at_100_max
      value: 26.119300000000003
    - type: nauc_precision_at_100_std
      value: 7.8559
    - type: nauc_precision_at_100_diff1
      value: 9.9931
    - type: nauc_precision_at_1000_max
      value: 11.0973
    - type: nauc_precision_at_1000_std
      value: 4.6916
    - type: nauc_precision_at_1000_diff1
      value: -6.2033
    - type: nauc_mrr_at_1_max
      value: 35.5663
    - type: nauc_mrr_at_1_std
      value: -11.130700000000001
    - type: nauc_mrr_at_1_diff1
      value: 47.2971
    - type: nauc_mrr_at_3_max
      value: 35.0322
    - type: nauc_mrr_at_3_std
      value: -8.6242
    - type: nauc_mrr_at_3_diff1
      value: 43.435
    - type: nauc_mrr_at_5_max
      value: 34.796899999999994
    - type: nauc_mrr_at_5_std
      value: -8.1215
    - type: nauc_mrr_at_5_diff1
      value: 42.9234
    - type: nauc_mrr_at_10_max
      value: 35.0315
    - type: nauc_mrr_at_10_std
      value: -7.4498
    - type: nauc_mrr_at_10_diff1
      value: 42.348
    - type: nauc_mrr_at_20_max
      value: 35.0761
    - type: nauc_mrr_at_20_std
      value: -7.246700000000001
    - type: nauc_mrr_at_20_diff1
      value: 42.3282
    - type: nauc_mrr_at_100_max
      value: 35.0173
    - type: nauc_mrr_at_100_std
      value: -7.269699999999999
    - type: nauc_mrr_at_100_diff1
      value: 42.306
    - type: nauc_mrr_at_1000_max
      value: 35.015
    - type: nauc_mrr_at_1000_std
      value: -7.2973
    - type: nauc_mrr_at_1000_diff1
      value: 42.3292
    - type: main_score
      value: 40.224
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
      value: 20.398
    - type: ndcg_at_3
      value: 25.701
    - type: ndcg_at_5
      value: 27.503
    - type: ndcg_at_10
      value: 30.016
    - type: ndcg_at_20
      value: 31.941000000000003
    - type: ndcg_at_100
      value: 35.995
    - type: ndcg_at_1000
      value: 38.732
    - type: map_at_1
      value: 15.827
    - type: map_at_3
      value: 22.185
    - type: map_at_5
      value: 23.398
    - type: map_at_10
      value: 24.576
    - type: map_at_20
      value: 25.158
    - type: map_at_100
      value: 25.790000000000003
    - type: map_at_1000
      value: 25.906000000000002
    - type: recall_at_1
      value: 15.827
    - type: recall_at_3
      value: 29.404000000000003
    - type: recall_at_5
      value: 34.408
    - type: recall_at_10
      value: 41.802
    - type: recall_at_20
      value: 48.775
    - type: recall_at_100
      value: 68.643
    - type: recall_at_1000
      value: 88.022
    - type: precision_at_1
      value: 20.398
    - type: precision_at_3
      value: 12.769
    - type: precision_at_5
      value: 9.030000000000001
    - type: precision_at_10
      value: 5.684
    - type: precision_at_20
      value: 3.408
    - type: precision_at_100
      value: 1.004
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: mrr_at_1
      value: 20.398
    - type: mrr_at_3
      value: 27.1144
    - type: mrr_at_5
      value: 28.4453
    - type: mrr_at_10
      value: 29.5935
    - type: mrr_at_20
      value: 30.0591
    - type: mrr_at_100
      value: 30.516399999999997
    - type: mrr_at_1000
      value: 30.5831
    - type: nauc_ndcg_at_1_max
      value: 26.8727
    - type: nauc_ndcg_at_1_std
      value: -2.0329
    - type: nauc_ndcg_at_1_diff1
      value: 28.792099999999998
    - type: nauc_ndcg_at_3_max
      value: 29.210900000000002
    - type: nauc_ndcg_at_3_std
      value: 1.357
    - type: nauc_ndcg_at_3_diff1
      value: 25.153399999999998
    - type: nauc_ndcg_at_5_max
      value: 28.031499999999998
    - type: nauc_ndcg_at_5_std
      value: 1.546
    - type: nauc_ndcg_at_5_diff1
      value: 23.6489
    - type: nauc_ndcg_at_10_max
      value: 27.2909
    - type: nauc_ndcg_at_10_std
      value: 1.8301
    - type: nauc_ndcg_at_10_diff1
      value: 21.7899
    - type: nauc_ndcg_at_20_max
      value: 27.934900000000003
    - type: nauc_ndcg_at_20_std
      value: 2.3472
    - type: nauc_ndcg_at_20_diff1
      value: 22.322
    - type: nauc_ndcg_at_100_max
      value: 28.1958
    - type: nauc_ndcg_at_100_std
      value: 3.5208000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 23.156499999999998
    - type: nauc_ndcg_at_1000_max
      value: 28.766000000000002
    - type: nauc_ndcg_at_1000_std
      value: 3.4803
    - type: nauc_ndcg_at_1000_diff1
      value: 23.096600000000002
    - type: nauc_map_at_1_max
      value: 26.271099999999997
    - type: nauc_map_at_1_std
      value: -0.8499
    - type: nauc_map_at_1_diff1
      value: 32.0953
    - type: nauc_map_at_3_max
      value: 28.1188
    - type: nauc_map_at_3_std
      value: 0.42040000000000005
    - type: nauc_map_at_3_diff1
      value: 26.6573
    - type: nauc_map_at_5_max
      value: 27.5138
    - type: nauc_map_at_5_std
      value: 0.43010000000000004
    - type: nauc_map_at_5_diff1
      value: 25.6081
    - type: nauc_map_at_10_max
      value: 27.313900000000004
    - type: nauc_map_at_10_std
      value: 0.644
    - type: nauc_map_at_10_diff1
      value: 24.6459
    - type: nauc_map_at_20_max
      value: 27.5519
    - type: nauc_map_at_20_std
      value: 0.7802
    - type: nauc_map_at_20_diff1
      value: 24.7392
    - type: nauc_map_at_100_max
      value: 27.717999999999996
    - type: nauc_map_at_100_std
      value: 1.078
    - type: nauc_map_at_100_diff1
      value: 24.884500000000003
    - type: nauc_map_at_1000_max
      value: 27.7366
    - type: nauc_map_at_1000_std
      value: 1.0739
    - type: nauc_map_at_1000_diff1
      value: 24.9131
    - type: nauc_recall_at_1_max
      value: 26.271099999999997
    - type: nauc_recall_at_1_std
      value: -0.8499
    - type: nauc_recall_at_1_diff1
      value: 32.0953
    - type: nauc_recall_at_3_max
      value: 28.034399999999998
    - type: nauc_recall_at_3_std
      value: 2.7848
    - type: nauc_recall_at_3_diff1
      value: 21.845
    - type: nauc_recall_at_5_max
      value: 25.510899999999996
    - type: nauc_recall_at_5_std
      value: 3.2032
    - type: nauc_recall_at_5_diff1
      value: 18.1497
    - type: nauc_recall_at_10_max
      value: 23.6985
    - type: nauc_recall_at_10_std
      value: 4.2382
    - type: nauc_recall_at_10_diff1
      value: 13.4018
    - type: nauc_recall_at_20_max
      value: 25.0105
    - type: nauc_recall_at_20_std
      value: 6.2892
    - type: nauc_recall_at_20_diff1
      value: 14.6347
    - type: nauc_recall_at_100_max
      value: 23.6484
    - type: nauc_recall_at_100_std
      value: 12.826299999999998
    - type: nauc_recall_at_100_diff1
      value: 16.372999999999998
    - type: nauc_recall_at_1000_max
      value: 34.1999
    - type: nauc_recall_at_1000_std
      value: 26.1497
    - type: nauc_recall_at_1000_diff1
      value: 7.666199999999999
    - type: nauc_precision_at_1_max
      value: 26.8727
    - type: nauc_precision_at_1_std
      value: -2.0329
    - type: nauc_precision_at_1_diff1
      value: 28.792099999999998
    - type: nauc_precision_at_3_max
      value: 31.689
    - type: nauc_precision_at_3_std
      value: 4.5703000000000005
    - type: nauc_precision_at_3_diff1
      value: 20.0233
    - type: nauc_precision_at_5_max
      value: 27.807
    - type: nauc_precision_at_5_std
      value: 4.209899999999999
    - type: nauc_precision_at_5_diff1
      value: 15.3505
    - type: nauc_precision_at_10_max
      value: 22.672800000000002
    - type: nauc_precision_at_10_std
      value: 3.624
    - type: nauc_precision_at_10_diff1
      value: 8.4378
    - type: nauc_precision_at_20_max
      value: 23.3401
    - type: nauc_precision_at_20_std
      value: 3.6032
    - type: nauc_precision_at_20_diff1
      value: 9.2764
    - type: nauc_precision_at_100_max
      value: 16.516000000000002
    - type: nauc_precision_at_100_std
      value: 5.7479000000000005
    - type: nauc_precision_at_100_diff1
      value: 5.733499999999999
    - type: nauc_precision_at_1000_max
      value: 6.1677
    - type: nauc_precision_at_1000_std
      value: 0.4491
    - type: nauc_precision_at_1000_diff1
      value: 0.2477
    - type: nauc_mrr_at_1_max
      value: 26.8727
    - type: nauc_mrr_at_1_std
      value: -2.0329
    - type: nauc_mrr_at_1_diff1
      value: 28.792099999999998
    - type: nauc_mrr_at_3_max
      value: 29.6131
    - type: nauc_mrr_at_3_std
      value: 0.6053000000000001
    - type: nauc_mrr_at_3_diff1
      value: 25.8043
    - type: nauc_mrr_at_5_max
      value: 29.0205
    - type: nauc_mrr_at_5_std
      value: 0.8692
    - type: nauc_mrr_at_5_diff1
      value: 24.8413
    - type: nauc_mrr_at_10_max
      value: 28.459400000000002
    - type: nauc_mrr_at_10_std
      value: 0.5887
    - type: nauc_mrr_at_10_diff1
      value: 24.364
    - type: nauc_mrr_at_20_max
      value: 28.5242
    - type: nauc_mrr_at_20_std
      value: 0.6396
    - type: nauc_mrr_at_20_diff1
      value: 24.4579
    - type: nauc_mrr_at_100_max
      value: 28.540599999999998
    - type: nauc_mrr_at_100_std
      value: 0.7425
    - type: nauc_mrr_at_100_diff1
      value: 24.5761
    - type: nauc_mrr_at_1000_max
      value: 28.5429
    - type: nauc_mrr_at_1000_std
      value: 0.7348
    - type: nauc_mrr_at_1000_diff1
      value: 24.562800000000003
    - type: main_score
      value: 30.016
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
      value: 34.937000000000005
    - type: ndcg_at_3
      value: 39.366
    - type: ndcg_at_5
      value: 41.980000000000004
    - type: ndcg_at_10
      value: 44.674
    - type: ndcg_at_20
      value: 46.671
    - type: ndcg_at_100
      value: 50.041999999999994
    - type: ndcg_at_1000
      value: 52.120999999999995
    - type: map_at_1
      value: 27.750000000000004
    - type: map_at_3
      value: 35.027
    - type: map_at_5
      value: 36.952
    - type: map_at_10
      value: 38.382
    - type: map_at_20
      value: 39.072
    - type: map_at_100
      value: 39.694
    - type: map_at_1000
      value: 39.81
    - type: recall_at_1
      value: 27.750000000000004
    - type: recall_at_3
      value: 42.321999999999996
    - type: recall_at_5
      value: 49.209
    - type: recall_at_10
      value: 57.282
    - type: recall_at_20
      value: 64.30399999999999
    - type: recall_at_100
      value: 80.143
    - type: recall_at_1000
      value: 93.664
    - type: precision_at_1
      value: 34.937000000000005
    - type: precision_at_3
      value: 18.993
    - type: precision_at_5
      value: 13.648
    - type: precision_at_10
      value: 8.412
    - type: precision_at_20
      value: 4.885
    - type: precision_at_100
      value: 1.302
    - type: precision_at_1000
      value: 0.167
    - type: mrr_at_1
      value: 34.937400000000004
    - type: mrr_at_3
      value: 41.7389
    - type: mrr_at_5
      value: 43.4184
    - type: mrr_at_10
      value: 44.4776
    - type: mrr_at_20
      value: 44.8859
    - type: mrr_at_100
      value: 45.2197
    - type: mrr_at_1000
      value: 45.2704
    - type: nauc_ndcg_at_1_max
      value: 41.1314
    - type: nauc_ndcg_at_1_std
      value: 0.6393
    - type: nauc_ndcg_at_1_diff1
      value: 52.494
    - type: nauc_ndcg_at_3_max
      value: 38.8915
    - type: nauc_ndcg_at_3_std
      value: -1.1358
    - type: nauc_ndcg_at_3_diff1
      value: 48.8256
    - type: nauc_ndcg_at_5_max
      value: 38.6924
    - type: nauc_ndcg_at_5_std
      value: -2.2843999999999998
    - type: nauc_ndcg_at_5_diff1
      value: 47.9194
    - type: nauc_ndcg_at_10_max
      value: 37.8751
    - type: nauc_ndcg_at_10_std
      value: -1.5187000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 46.455400000000004
    - type: nauc_ndcg_at_20_max
      value: 38.1022
    - type: nauc_ndcg_at_20_std
      value: -0.7692
    - type: nauc_ndcg_at_20_diff1
      value: 46.5041
    - type: nauc_ndcg_at_100_max
      value: 40.396100000000004
    - type: nauc_ndcg_at_100_std
      value: 1.8087
    - type: nauc_ndcg_at_100_diff1
      value: 47.2332
    - type: nauc_ndcg_at_1000_max
      value: 40.2539
    - type: nauc_ndcg_at_1000_std
      value: 2.1609
    - type: nauc_ndcg_at_1000_diff1
      value: 47.185700000000004
    - type: nauc_map_at_1_max
      value: 34.3255
    - type: nauc_map_at_1_std
      value: -6.783599999999999
    - type: nauc_map_at_1_diff1
      value: 54.6668
    - type: nauc_map_at_3_max
      value: 36.5777
    - type: nauc_map_at_3_std
      value: -3.8482000000000003
    - type: nauc_map_at_3_diff1
      value: 50.1703
    - type: nauc_map_at_5_max
      value: 37.229
    - type: nauc_map_at_5_std
      value: -3.9170000000000003
    - type: nauc_map_at_5_diff1
      value: 49.5882
    - type: nauc_map_at_10_max
      value: 37.318400000000004
    - type: nauc_map_at_10_std
      value: -3.2477
    - type: nauc_map_at_10_diff1
      value: 48.8387
    - type: nauc_map_at_20_max
      value: 37.5075
    - type: nauc_map_at_20_std
      value: -2.8737
    - type: nauc_map_at_20_diff1
      value: 48.896699999999996
    - type: nauc_map_at_100_max
      value: 37.965199999999996
    - type: nauc_map_at_100_std
      value: -2.3644
    - type: nauc_map_at_100_diff1
      value: 48.9583
    - type: nauc_map_at_1000_max
      value: 37.9824
    - type: nauc_map_at_1000_std
      value: -2.2945
    - type: nauc_map_at_1000_diff1
      value: 48.9472
    - type: nauc_recall_at_1_max
      value: 34.3255
    - type: nauc_recall_at_1_std
      value: -6.783599999999999
    - type: nauc_recall_at_1_diff1
      value: 54.6668
    - type: nauc_recall_at_3_max
      value: 33.823100000000004
    - type: nauc_recall_at_3_std
      value: -3.7593
    - type: nauc_recall_at_3_diff1
      value: 44.3225
    - type: nauc_recall_at_5_max
      value: 34.271499999999996
    - type: nauc_recall_at_5_std
      value: -4.8704
    - type: nauc_recall_at_5_diff1
      value: 41.3594
    - type: nauc_recall_at_10_max
      value: 32.2652
    - type: nauc_recall_at_10_std
      value: -1.5755000000000001
    - type: nauc_recall_at_10_diff1
      value: 35.9057
    - type: nauc_recall_at_20_max
      value: 32.1614
    - type: nauc_recall_at_20_std
      value: 0.8789
    - type: nauc_recall_at_20_diff1
      value: 34.6074
    - type: nauc_recall_at_100_max
      value: 44.527499999999996
    - type: nauc_recall_at_100_std
      value: 17.735500000000002
    - type: nauc_recall_at_100_diff1
      value: 36.446
    - type: nauc_recall_at_1000_max
      value: 47.751
    - type: nauc_recall_at_1000_std
      value: 41.8399
    - type: nauc_recall_at_1000_diff1
      value: 26.7075
    - type: nauc_precision_at_1_max
      value: 41.1314
    - type: nauc_precision_at_1_std
      value: 0.6393
    - type: nauc_precision_at_1_diff1
      value: 52.494
    - type: nauc_precision_at_3_max
      value: 40.7504
    - type: nauc_precision_at_3_std
      value: 8.6914
    - type: nauc_precision_at_3_diff1
      value: 34.590900000000005
    - type: nauc_precision_at_5_max
      value: 38.5891
    - type: nauc_precision_at_5_std
      value: 8.7898
    - type: nauc_precision_at_5_diff1
      value: 27.122200000000003
    - type: nauc_precision_at_10_max
      value: 32.5422
    - type: nauc_precision_at_10_std
      value: 13.9757
    - type: nauc_precision_at_10_diff1
      value: 15.504000000000001
    - type: nauc_precision_at_20_max
      value: 28.212799999999998
    - type: nauc_precision_at_20_std
      value: 17.0921
    - type: nauc_precision_at_20_diff1
      value: 10.264800000000001
    - type: nauc_precision_at_100_max
      value: 23.9818
    - type: nauc_precision_at_100_std
      value: 24.7802
    - type: nauc_precision_at_100_diff1
      value: -0.1275
    - type: nauc_precision_at_1000_max
      value: 11.8968
    - type: nauc_precision_at_1000_std
      value: 24.0201
    - type: nauc_precision_at_1000_diff1
      value: -12.1507
    - type: nauc_mrr_at_1_max
      value: 41.1314
    - type: nauc_mrr_at_1_std
      value: 0.6393
    - type: nauc_mrr_at_1_diff1
      value: 52.494
    - type: nauc_mrr_at_3_max
      value: 41.0145
    - type: nauc_mrr_at_3_std
      value: 1.7641
    - type: nauc_mrr_at_3_diff1
      value: 49.3663
    - type: nauc_mrr_at_5_max
      value: 41.4664
    - type: nauc_mrr_at_5_std
      value: 1.6695000000000002
    - type: nauc_mrr_at_5_diff1
      value: 49.0033
    - type: nauc_mrr_at_10_max
      value: 41.2351
    - type: nauc_mrr_at_10_std
      value: 2.0388
    - type: nauc_mrr_at_10_diff1
      value: 48.7703
    - type: nauc_mrr_at_20_max
      value: 41.2064
    - type: nauc_mrr_at_20_std
      value: 2.081
    - type: nauc_mrr_at_20_diff1
      value: 48.6787
    - type: nauc_mrr_at_100_max
      value: 41.3966
    - type: nauc_mrr_at_100_std
      value: 2.2723
    - type: nauc_mrr_at_100_diff1
      value: 48.746
    - type: nauc_mrr_at_1000_max
      value: 41.3803
    - type: nauc_mrr_at_1000_std
      value: 2.2632
    - type: nauc_mrr_at_1000_diff1
      value: 48.7541
    - type: main_score
      value: 44.674
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
      value: 29.909000000000002
    - type: ndcg_at_3
      value: 35.056
    - type: ndcg_at_5
      value: 37.076
    - type: ndcg_at_10
      value: 40.093
    - type: ndcg_at_20
      value: 42.254999999999995
    - type: ndcg_at_100
      value: 45.692
    - type: ndcg_at_1000
      value: 48.204
    - type: map_at_1
      value: 24.68
    - type: map_at_3
      value: 31.379
    - type: map_at_5
      value: 32.92
    - type: map_at_10
      value: 34.391
    - type: map_at_20
      value: 35.109
    - type: map_at_100
      value: 35.686
    - type: map_at_1000
      value: 35.804
    - type: recall_at_1
      value: 24.68
    - type: recall_at_3
      value: 38.190000000000005
    - type: recall_at_5
      value: 43.519999999999996
    - type: recall_at_10
      value: 52.364999999999995
    - type: recall_at_20
      value: 60.02499999999999
    - type: recall_at_100
      value: 76.229
    - type: recall_at_1000
      value: 93.31099999999999
    - type: precision_at_1
      value: 29.909000000000002
    - type: precision_at_3
      value: 16.667
    - type: precision_at_5
      value: 11.781
    - type: precision_at_10
      value: 7.340000000000001
    - type: precision_at_20
      value: 4.315
    - type: precision_at_100
      value: 1.18
    - type: precision_at_1000
      value: 0.158
    - type: mrr_at_1
      value: 29.9087
    - type: mrr_at_3
      value: 36.6438
    - type: mrr_at_5
      value: 37.939499999999995
    - type: mrr_at_10
      value: 39.1699
    - type: mrr_at_20
      value: 39.6872
    - type: mrr_at_100
      value: 40.0648
    - type: mrr_at_1000
      value: 40.1254
    - type: nauc_ndcg_at_1_max
      value: 37.3397
    - type: nauc_ndcg_at_1_std
      value: 5.9699
    - type: nauc_ndcg_at_1_diff1
      value: 46.6563
    - type: nauc_ndcg_at_3_max
      value: 39.0153
    - type: nauc_ndcg_at_3_std
      value: 8.5756
    - type: nauc_ndcg_at_3_diff1
      value: 41.2988
    - type: nauc_ndcg_at_5_max
      value: 39.4932
    - type: nauc_ndcg_at_5_std
      value: 9.4963
    - type: nauc_ndcg_at_5_diff1
      value: 40.0798
    - type: nauc_ndcg_at_10_max
      value: 40.0787
    - type: nauc_ndcg_at_10_std
      value: 10.312100000000001
    - type: nauc_ndcg_at_10_diff1
      value: 39.6584
    - type: nauc_ndcg_at_20_max
      value: 40.9003
    - type: nauc_ndcg_at_20_std
      value: 11.991100000000001
    - type: nauc_ndcg_at_20_diff1
      value: 39.4373
    - type: nauc_ndcg_at_100_max
      value: 41.4069
    - type: nauc_ndcg_at_100_std
      value: 13.6103
    - type: nauc_ndcg_at_100_diff1
      value: 40.0088
    - type: nauc_ndcg_at_1000_max
      value: 41.505900000000004
    - type: nauc_ndcg_at_1000_std
      value: 12.742400000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 40.1457
    - type: nauc_map_at_1_max
      value: 34.739
    - type: nauc_map_at_1_std
      value: 0.9294
    - type: nauc_map_at_1_diff1
      value: 48.1138
    - type: nauc_map_at_3_max
      value: 37.0441
    - type: nauc_map_at_3_std
      value: 5.5666
    - type: nauc_map_at_3_diff1
      value: 42.7429
    - type: nauc_map_at_5_max
      value: 37.891799999999996
    - type: nauc_map_at_5_std
      value: 6.7185999999999995
    - type: nauc_map_at_5_diff1
      value: 41.9849
    - type: nauc_map_at_10_max
      value: 38.556000000000004
    - type: nauc_map_at_10_std
      value: 7.4627
    - type: nauc_map_at_10_diff1
      value: 41.8061
    - type: nauc_map_at_20_max
      value: 38.8822
    - type: nauc_map_at_20_std
      value: 8.0747
    - type: nauc_map_at_20_diff1
      value: 41.7518
    - type: nauc_map_at_100_max
      value: 39.0912
    - type: nauc_map_at_100_std
      value: 8.4627
    - type: nauc_map_at_100_diff1
      value: 41.8958
    - type: nauc_map_at_1000_max
      value: 39.112700000000004
    - type: nauc_map_at_1000_std
      value: 8.4459
    - type: nauc_map_at_1000_diff1
      value: 41.903400000000005
    - type: nauc_recall_at_1_max
      value: 34.739
    - type: nauc_recall_at_1_std
      value: 0.9294
    - type: nauc_recall_at_1_diff1
      value: 48.1138
    - type: nauc_recall_at_3_max
      value: 37.3971
    - type: nauc_recall_at_3_std
      value: 9.2075
    - type: nauc_recall_at_3_diff1
      value: 36.4624
    - type: nauc_recall_at_5_max
      value: 38.1516
    - type: nauc_recall_at_5_std
      value: 11.5318
    - type: nauc_recall_at_5_diff1
      value: 33.3421
    - type: nauc_recall_at_10_max
      value: 38.8221
    - type: nauc_recall_at_10_std
      value: 14.0268
    - type: nauc_recall_at_10_diff1
      value: 31.4088
    - type: nauc_recall_at_20_max
      value: 40.9493
    - type: nauc_recall_at_20_std
      value: 20.2136
    - type: nauc_recall_at_20_diff1
      value: 29.9447
    - type: nauc_recall_at_100_max
      value: 43.149300000000004
    - type: nauc_recall_at_100_std
      value: 33.7709
    - type: nauc_recall_at_100_diff1
      value: 29.3082
    - type: nauc_recall_at_1000_max
      value: 55.435500000000005
    - type: nauc_recall_at_1000_std
      value: 51.8958
    - type: nauc_recall_at_1000_diff1
      value: 19.3816
    - type: nauc_precision_at_1_max
      value: 37.3397
    - type: nauc_precision_at_1_std
      value: 5.9699
    - type: nauc_precision_at_1_diff1
      value: 46.6563
    - type: nauc_precision_at_3_max
      value: 40.3693
    - type: nauc_precision_at_3_std
      value: 17.0552
    - type: nauc_precision_at_3_diff1
      value: 29.498400000000004
    - type: nauc_precision_at_5_max
      value: 39.7607
    - type: nauc_precision_at_5_std
      value: 20.274
    - type: nauc_precision_at_5_diff1
      value: 23.061300000000003
    - type: nauc_precision_at_10_max
      value: 38.0299
    - type: nauc_precision_at_10_std
      value: 22.256899999999998
    - type: nauc_precision_at_10_diff1
      value: 17.0507
    - type: nauc_precision_at_20_max
      value: 36.0867
    - type: nauc_precision_at_20_std
      value: 25.936700000000002
    - type: nauc_precision_at_20_diff1
      value: 12.1754
    - type: nauc_precision_at_100_max
      value: 24.1493
    - type: nauc_precision_at_100_std
      value: 23.8361
    - type: nauc_precision_at_100_diff1
      value: 5.2714
    - type: nauc_precision_at_1000_max
      value: 7.033499999999999
    - type: nauc_precision_at_1000_std
      value: 9.0198
    - type: nauc_precision_at_1000_diff1
      value: -4.8427999999999995
    - type: nauc_mrr_at_1_max
      value: 37.3397
    - type: nauc_mrr_at_1_std
      value: 5.9699
    - type: nauc_mrr_at_1_diff1
      value: 46.6563
    - type: nauc_mrr_at_3_max
      value: 40.2205
    - type: nauc_mrr_at_3_std
      value: 9.8833
    - type: nauc_mrr_at_3_diff1
      value: 42.3963
    - type: nauc_mrr_at_5_max
      value: 40.1911
    - type: nauc_mrr_at_5_std
      value: 10.3282
    - type: nauc_mrr_at_5_diff1
      value: 41.796499999999995
    - type: nauc_mrr_at_10_max
      value: 40.3748
    - type: nauc_mrr_at_10_std
      value: 10.567699999999999
    - type: nauc_mrr_at_10_diff1
      value: 41.643299999999996
    - type: nauc_mrr_at_20_max
      value: 40.4527
    - type: nauc_mrr_at_20_std
      value: 10.8016
    - type: nauc_mrr_at_20_diff1
      value: 41.594300000000004
    - type: nauc_mrr_at_100_max
      value: 40.395199999999996
    - type: nauc_mrr_at_100_std
      value: 10.8396
    - type: nauc_mrr_at_100_diff1
      value: 41.706700000000005
    - type: nauc_mrr_at_1000_max
      value: 40.3932
    - type: nauc_mrr_at_1000_std
      value: 10.8097
    - type: nauc_mrr_at_1000_diff1
      value: 41.7124
    - type: main_score
      value: 40.093
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
      value: 30.19958333333333
    - type: ndcg_at_3
      value: 35.01541666666667
    - type: ndcg_at_5
      value: 37.22058333333334
    - type: ndcg_at_10
      value: 39.84525000000001
    - type: ndcg_at_20
      value: 41.81666666666667
    - type: ndcg_at_100
      value: 44.973
    - type: ndcg_at_1000
      value: 47.338583333333325
    - type: map_at_1
      value: 25.296916666666668
    - type: map_at_3
      value: 31.593166666666665
    - type: map_at_5
      value: 33.145916666666665
    - type: map_at_10
      value: 34.45275
    - type: map_at_20
      value: 35.10883333333334
    - type: map_at_100
      value: 35.647499999999994
    - type: map_at_1000
      value: 35.768166666666666
    - type: recall_at_1
      value: 25.296916666666668
    - type: recall_at_3
      value: 38.05166666666666
    - type: recall_at_5
      value: 43.82625
    - type: recall_at_10
      value: 51.58916666666668
    - type: recall_at_20
      value: 58.77308333333334
    - type: recall_at_100
      value: 74.15658333333333
    - type: recall_at_1000
      value: 90.51333333333335
    - type: precision_at_1
      value: 30.19958333333333
    - type: precision_at_3
      value: 16.167999999999996
    - type: precision_at_5
      value: 11.49225
    - type: precision_at_10
      value: 7.057666666666666
    - type: precision_at_20
      value: 4.174083333333333
    - type: precision_at_100
      value: 1.1363333333333332
    - type: precision_at_1000
      value: 0.15383333333333332
    - type: mrr_at_1
      value: 30.199658333333335
    - type: mrr_at_3
      value: 36.21564166666667
    - type: mrr_at_5
      value: 37.627291666666665
    - type: mrr_at_10
      value: 38.70535
    - type: mrr_at_20
      value: 39.193799999999996
    - type: mrr_at_100
      value: 39.55041666666666
    - type: mrr_at_1000
      value: 39.61140833333333
    - type: nauc_ndcg_at_1_max
      value: 39.3715
    - type: nauc_ndcg_at_1_std
      value: -1.2167000000000008
    - type: nauc_ndcg_at_1_diff1
      value: 47.05770833333333
    - type: nauc_ndcg_at_3_max
      value: 38.67278333333333
    - type: nauc_ndcg_at_3_std
      value: -0.10360000000000005
    - type: nauc_ndcg_at_3_diff1
      value: 42.23506666666667
    - type: nauc_ndcg_at_5_max
      value: 38.421591666666664
    - type: nauc_ndcg_at_5_std
      value: 0.9004833333333335
    - type: nauc_ndcg_at_5_diff1
      value: 41.46895
    - type: nauc_ndcg_at_10_max
      value: 38.31713333333333
    - type: nauc_ndcg_at_10_std
      value: 1.6739333333333335
    - type: nauc_ndcg_at_10_diff1
      value: 40.52259166666667
    - type: nauc_ndcg_at_20_max
      value: 38.61266666666667
    - type: nauc_ndcg_at_20_std
      value: 2.7783666666666673
    - type: nauc_ndcg_at_20_diff1
      value: 40.28085833333333
    - type: nauc_ndcg_at_100_max
      value: 39.27558333333333
    - type: nauc_ndcg_at_100_std
      value: 3.9398000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 40.39787499999999
    - type: nauc_ndcg_at_1000_max
      value: 39.44075
    - type: nauc_ndcg_at_1000_std
      value: 3.9607833333333327
    - type: nauc_ndcg_at_1000_diff1
      value: 40.683225
    - type: nauc_map_at_1_max
      value: 35.66645
    - type: nauc_map_at_1_std
      value: -4.276391666666667
    - type: nauc_map_at_1_diff1
      value: 48.810141666666674
    - type: nauc_map_at_3_max
      value: 37.424108333333336
    - type: nauc_map_at_3_std
      value: -2.064866666666667
    - type: nauc_map_at_3_diff1
      value: 44.115075
    - type: nauc_map_at_5_max
      value: 37.693016666666665
    - type: nauc_map_at_5_std
      value: -1.1872749999999994
    - type: nauc_map_at_5_diff1
      value: 43.554458333333336
    - type: nauc_map_at_10_max
      value: 37.9333
    - type: nauc_map_at_10_std
      value: -0.6246583333333332
    - type: nauc_map_at_10_diff1
      value: 43.05175
    - type: nauc_map_at_20_max
      value: 38.11316666666667
    - type: nauc_map_at_20_std
      value: -0.17139166666666622
    - type: nauc_map_at_20_diff1
      value: 42.929925000000004
    - type: nauc_map_at_100_max
      value: 38.296825
    - type: nauc_map_at_100_std
      value: 0.1448500000000002
    - type: nauc_map_at_100_diff1
      value: 42.91681666666667
    - type: nauc_map_at_1000_max
      value: 38.308891666666675
    - type: nauc_map_at_1000_std
      value: 0.17599166666666682
    - type: nauc_map_at_1000_diff1
      value: 42.91478333333333
    - type: nauc_recall_at_1_max
      value: 35.66645
    - type: nauc_recall_at_1_std
      value: -4.276391666666667
    - type: nauc_recall_at_1_diff1
      value: 48.810141666666674
    - type: nauc_recall_at_3_max
      value: 36.144949999999994
    - type: nauc_recall_at_3_std
      value: -0.07622500000000007
    - type: nauc_recall_at_3_diff1
      value: 38.39805833333333
    - type: nauc_recall_at_5_max
      value: 35.599016666666664
    - type: nauc_recall_at_5_std
      value: 2.6147583333333335
    - type: nauc_recall_at_5_diff1
      value: 35.84809166666666
    - type: nauc_recall_at_10_max
      value: 34.73115833333333
    - type: nauc_recall_at_10_std
      value: 5.2187166666666664
    - type: nauc_recall_at_10_diff1
      value: 32.22850833333333
    - type: nauc_recall_at_20_max
      value: 35.11221666666667
    - type: nauc_recall_at_20_std
      value: 9.564958333333331
    - type: nauc_recall_at_20_diff1
      value: 30.415991666666663
    - type: nauc_recall_at_100_max
      value: 37.735958333333336
    - type: nauc_recall_at_100_std
      value: 19.1386
    - type: nauc_recall_at_100_diff1
      value: 28.129675
    - type: nauc_recall_at_1000_max
      value: 43.71879166666667
    - type: nauc_recall_at_1000_std
      value: 39.80074166666667
    - type: nauc_recall_at_1000_diff1
      value: 23.800666666666668
    - type: nauc_precision_at_1_max
      value: 39.3715
    - type: nauc_precision_at_1_std
      value: -1.2167000000000008
    - type: nauc_precision_at_1_diff1
      value: 47.05770833333333
    - type: nauc_precision_at_3_max
      value: 39.00785833333333
    - type: nauc_precision_at_3_std
      value: 5.753050000000001
    - type: nauc_precision_at_3_diff1
      value: 31.4196
    - type: nauc_precision_at_5_max
      value: 36.98677500000001
    - type: nauc_precision_at_5_std
      value: 9.464608333333333
    - type: nauc_precision_at_5_diff1
      value: 25.906116666666662
    - type: nauc_precision_at_10_max
      value: 33.26575833333333
    - type: nauc_precision_at_10_std
      value: 12.540025
    - type: nauc_precision_at_10_diff1
      value: 18.274116666666668
    - type: nauc_precision_at_20_max
      value: 30.13705833333334
    - type: nauc_precision_at_20_std
      value: 16.549291666666665
    - type: nauc_precision_at_20_diff1
      value: 12.541983333333334
    - type: nauc_precision_at_100_max
      value: 22.078525000000003
    - type: nauc_precision_at_100_std
      value: 19.263416666666664
    - type: nauc_precision_at_100_diff1
      value: 2.293625
    - type: nauc_precision_at_1000_max
      value: 8.336641666666667
    - type: nauc_precision_at_1000_std
      value: 14.828683333333334
    - type: nauc_precision_at_1000_diff1
      value: -8.852525
    - type: nauc_mrr_at_1_max
      value: 39.3715
    - type: nauc_mrr_at_1_std
      value: -1.2167000000000008
    - type: nauc_mrr_at_1_diff1
      value: 47.05770833333333
    - type: nauc_mrr_at_3_max
      value: 39.90615
    - type: nauc_mrr_at_3_std
      value: 0.7366500000000004
    - type: nauc_mrr_at_3_diff1
      value: 42.96046666666666
    - type: nauc_mrr_at_5_max
      value: 39.78708333333334
    - type: nauc_mrr_at_5_std
      value: 1.3970916666666666
    - type: nauc_mrr_at_5_diff1
      value: 42.44258333333333
    - type: nauc_mrr_at_10_max
      value: 39.65595
    - type: nauc_mrr_at_10_std
      value: 1.6633916666666666
    - type: nauc_mrr_at_10_diff1
      value: 42.084358333333334
    - type: nauc_mrr_at_20_max
      value: 39.67735
    - type: nauc_mrr_at_20_std
      value: 1.8360749999999995
    - type: nauc_mrr_at_20_diff1
      value: 42.04530833333333
    - type: nauc_mrr_at_100_max
      value: 39.71681666666667
    - type: nauc_mrr_at_100_std
      value: 1.8971666666666671
    - type: nauc_mrr_at_100_diff1
      value: 42.075141666666674
    - type: nauc_mrr_at_1000_max
      value: 39.72038333333334
    - type: nauc_mrr_at_1000_std
      value: 1.8916749999999996
    - type: nauc_mrr_at_1000_diff1
      value: 42.091208333333334
    - type: main_score
      value: 39.84525000000001
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
      value: 39.84525000000001
    - type: ndcg_at_10
      value: 39.84525000000001
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
      value: 27.454
    - type: ndcg_at_3
      value: 31.464
    - type: ndcg_at_5
      value: 33.533
    - type: ndcg_at_10
      value: 35.477
    - type: ndcg_at_20
      value: 37.092999999999996
    - type: ndcg_at_100
      value: 39.808
    - type: ndcg_at_1000
      value: 42.309000000000005
    - type: map_at_1
      value: 24.489
    - type: map_at_3
      value: 29.204
    - type: map_at_5
      value: 30.496000000000002
    - type: map_at_10
      value: 31.415
    - type: map_at_20
      value: 31.897
    - type: map_at_100
      value: 32.259
    - type: map_at_1000
      value: 32.361000000000004
    - type: recall_at_1
      value: 24.489
    - type: recall_at_3
      value: 34.333999999999996
    - type: recall_at_5
      value: 39.550999999999995
    - type: recall_at_10
      value: 45.275999999999996
    - type: recall_at_20
      value: 51.241
    - type: recall_at_100
      value: 65.398
    - type: recall_at_1000
      value: 83.685
    - type: precision_at_1
      value: 27.454
    - type: precision_at_3
      value: 13.344000000000001
    - type: precision_at_5
      value: 9.417
    - type: precision_at_10
      value: 5.567
    - type: precision_at_20
      value: 3.221
    - type: precision_at_100
      value: 0.845
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: mrr_at_1
      value: 27.454
    - type: mrr_at_3
      value: 32.1063
    - type: mrr_at_5
      value: 33.2797
    - type: mrr_at_10
      value: 34.0563
    - type: mrr_at_20
      value: 34.4952
    - type: mrr_at_100
      value: 34.8327
    - type: mrr_at_1000
      value: 34.9002
    - type: nauc_ndcg_at_1_max
      value: 45.7913
    - type: nauc_ndcg_at_1_std
      value: 10.6304
    - type: nauc_ndcg_at_1_diff1
      value: 51.58160000000001
    - type: nauc_ndcg_at_3_max
      value: 42.992599999999996
    - type: nauc_ndcg_at_3_std
      value: 10.1454
    - type: nauc_ndcg_at_3_diff1
      value: 45.330799999999996
    - type: nauc_ndcg_at_5_max
      value: 43.081399999999995
    - type: nauc_ndcg_at_5_std
      value: 11.7829
    - type: nauc_ndcg_at_5_diff1
      value: 45.8734
    - type: nauc_ndcg_at_10_max
      value: 45.2554
    - type: nauc_ndcg_at_10_std
      value: 14.2953
    - type: nauc_ndcg_at_10_diff1
      value: 45.908
    - type: nauc_ndcg_at_20_max
      value: 45.7565
    - type: nauc_ndcg_at_20_std
      value: 15.1327
    - type: nauc_ndcg_at_20_diff1
      value: 45.512
    - type: nauc_ndcg_at_100_max
      value: 45.602599999999995
    - type: nauc_ndcg_at_100_std
      value: 15.6507
    - type: nauc_ndcg_at_100_diff1
      value: 44.3626
    - type: nauc_ndcg_at_1000_max
      value: 45.6835
    - type: nauc_ndcg_at_1000_std
      value: 16.3352
    - type: nauc_ndcg_at_1000_diff1
      value: 44.9838
    - type: nauc_map_at_1_max
      value: 41.989900000000006
    - type: nauc_map_at_1_std
      value: 5.3356
    - type: nauc_map_at_1_diff1
      value: 52.711200000000005
    - type: nauc_map_at_3_max
      value: 42.363
    - type: nauc_map_at_3_std
      value: 8.1615
    - type: nauc_map_at_3_diff1
      value: 47.1827
    - type: nauc_map_at_5_max
      value: 42.6039
    - type: nauc_map_at_5_std
      value: 9.500300000000001
    - type: nauc_map_at_5_diff1
      value: 47.4177
    - type: nauc_map_at_10_max
      value: 43.703399999999995
    - type: nauc_map_at_10_std
      value: 10.729
    - type: nauc_map_at_10_diff1
      value: 47.4334
    - type: nauc_map_at_20_max
      value: 43.9336
    - type: nauc_map_at_20_std
      value: 11.0612
    - type: nauc_map_at_20_diff1
      value: 47.321600000000004
    - type: nauc_map_at_100_max
      value: 43.978899999999996
    - type: nauc_map_at_100_std
      value: 11.148299999999999
    - type: nauc_map_at_100_diff1
      value: 47.1738
    - type: nauc_map_at_1000_max
      value: 43.985400000000006
    - type: nauc_map_at_1000_std
      value: 11.1754
    - type: nauc_map_at_1000_diff1
      value: 47.197
    - type: nauc_recall_at_1_max
      value: 41.989900000000006
    - type: nauc_recall_at_1_std
      value: 5.3356
    - type: nauc_recall_at_1_diff1
      value: 52.711200000000005
    - type: nauc_recall_at_3_max
      value: 40.8671
    - type: nauc_recall_at_3_std
      value: 9.4511
    - type: nauc_recall_at_3_diff1
      value: 41.2041
    - type: nauc_recall_at_5_max
      value: 40.9279
    - type: nauc_recall_at_5_std
      value: 13.688600000000001
    - type: nauc_recall_at_5_diff1
      value: 41.9126
    - type: nauc_recall_at_10_max
      value: 46.1436
    - type: nauc_recall_at_10_std
      value: 20.8837
    - type: nauc_recall_at_10_diff1
      value: 41.0814
    - type: nauc_recall_at_20_max
      value: 47.245599999999996
    - type: nauc_recall_at_20_std
      value: 23.405
    - type: nauc_recall_at_20_diff1
      value: 38.864599999999996
    - type: nauc_recall_at_100_max
      value: 45.457
    - type: nauc_recall_at_100_std
      value: 28.075
    - type: nauc_recall_at_100_diff1
      value: 30.213600000000003
    - type: nauc_recall_at_1000_max
      value: 48.8291
    - type: nauc_recall_at_1000_std
      value: 47.8416
    - type: nauc_recall_at_1000_diff1
      value: 30.387199999999996
    - type: nauc_precision_at_1_max
      value: 45.7913
    - type: nauc_precision_at_1_std
      value: 10.6304
    - type: nauc_precision_at_1_diff1
      value: 51.58160000000001
    - type: nauc_precision_at_3_max
      value: 44.710899999999995
    - type: nauc_precision_at_3_std
      value: 17.7458
    - type: nauc_precision_at_3_diff1
      value: 36.7588
    - type: nauc_precision_at_5_max
      value: 44.0582
    - type: nauc_precision_at_5_std
      value: 22.7864
    - type: nauc_precision_at_5_diff1
      value: 35.3597
    - type: nauc_precision_at_10_max
      value: 45.5849
    - type: nauc_precision_at_10_std
      value: 28.758899999999997
    - type: nauc_precision_at_10_diff1
      value: 30.3452
    - type: nauc_precision_at_20_max
      value: 43.6996
    - type: nauc_precision_at_20_std
      value: 30.314799999999998
    - type: nauc_precision_at_20_diff1
      value: 25.916299999999996
    - type: nauc_precision_at_100_max
      value: 33.6976
    - type: nauc_precision_at_100_std
      value: 28.7876
    - type: nauc_precision_at_100_diff1
      value: 11.670300000000001
    - type: nauc_precision_at_1000_max
      value: 14.089599999999999
    - type: nauc_precision_at_1000_std
      value: 23.8288
    - type: nauc_precision_at_1000_diff1
      value: -1.8387
    - type: nauc_mrr_at_1_max
      value: 45.7913
    - type: nauc_mrr_at_1_std
      value: 10.6304
    - type: nauc_mrr_at_1_diff1
      value: 51.58160000000001
    - type: nauc_mrr_at_3_max
      value: 45.5677
    - type: nauc_mrr_at_3_std
      value: 12.692800000000002
    - type: nauc_mrr_at_3_diff1
      value: 46.578599999999994
    - type: nauc_mrr_at_5_max
      value: 45.4634
    - type: nauc_mrr_at_5_std
      value: 13.386999999999999
    - type: nauc_mrr_at_5_diff1
      value: 46.7306
    - type: nauc_mrr_at_10_max
      value: 46.1532
    - type: nauc_mrr_at_10_std
      value: 14.3297
    - type: nauc_mrr_at_10_diff1
      value: 46.6835
    - type: nauc_mrr_at_20_max
      value: 46.1552
    - type: nauc_mrr_at_20_std
      value: 14.492099999999999
    - type: nauc_mrr_at_20_diff1
      value: 46.611000000000004
    - type: nauc_mrr_at_100_max
      value: 46.1171
    - type: nauc_mrr_at_100_std
      value: 14.4984
    - type: nauc_mrr_at_100_diff1
      value: 46.4837
    - type: nauc_mrr_at_1000_max
      value: 46.1231
    - type: nauc_mrr_at_1000_std
      value: 14.516000000000002
    - type: nauc_mrr_at_1000_diff1
      value: 46.5135
    - type: main_score
      value: 35.477
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
      value: 21.266
    - type: ndcg_at_3
      value: 25.337
    - type: ndcg_at_5
      value: 27.18
    - type: ndcg_at_10
      value: 29.452
    - type: ndcg_at_20
      value: 31.226
    - type: ndcg_at_100
      value: 34.409
    - type: ndcg_at_1000
      value: 37.577
    - type: map_at_1
      value: 17.363
    - type: map_at_3
      value: 22.448999999999998
    - type: map_at_5
      value: 23.686
    - type: map_at_10
      value: 24.769
    - type: map_at_20
      value: 25.295
    - type: map_at_100
      value: 25.790999999999997
    - type: map_at_1000
      value: 25.929000000000002
    - type: recall_at_1
      value: 17.363
    - type: recall_at_3
      value: 28.022000000000002
    - type: recall_at_5
      value: 32.817
    - type: recall_at_10
      value: 39.639
    - type: recall_at_20
      value: 46.245999999999995
    - type: recall_at_100
      value: 61.934
    - type: recall_at_1000
      value: 84.507
    - type: precision_at_1
      value: 21.266
    - type: precision_at_3
      value: 12.056000000000001
    - type: precision_at_5
      value: 8.727
    - type: precision_at_10
      value: 5.382
    - type: precision_at_20
      value: 3.2300000000000004
    - type: precision_at_100
      value: 0.922
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 21.266299999999998
    - type: mrr_at_3
      value: 26.5887
    - type: mrr_at_5
      value: 27.7931
    - type: mrr_at_10
      value: 28.7136
    - type: mrr_at_20
      value: 29.1995
    - type: mrr_at_100
      value: 29.5953
    - type: mrr_at_1000
      value: 29.677999999999997
    - type: nauc_ndcg_at_1_max
      value: 32.1973
    - type: nauc_ndcg_at_1_std
      value: -3.8459
    - type: nauc_ndcg_at_1_diff1
      value: 40.2485
    - type: nauc_ndcg_at_3_max
      value: 31.338300000000004
    - type: nauc_ndcg_at_3_std
      value: -3.2641000000000004
    - type: nauc_ndcg_at_3_diff1
      value: 34.212199999999996
    - type: nauc_ndcg_at_5_max
      value: 30.9515
    - type: nauc_ndcg_at_5_std
      value: -2.5583
    - type: nauc_ndcg_at_5_diff1
      value: 33.3896
    - type: nauc_ndcg_at_10_max
      value: 31.1472
    - type: nauc_ndcg_at_10_std
      value: -1.4321000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 33.057700000000004
    - type: nauc_ndcg_at_20_max
      value: 31.513099999999998
    - type: nauc_ndcg_at_20_std
      value: 0.4013
    - type: nauc_ndcg_at_20_diff1
      value: 32.2353
    - type: nauc_ndcg_at_100_max
      value: 31.8931
    - type: nauc_ndcg_at_100_std
      value: 2.0259
    - type: nauc_ndcg_at_100_diff1
      value: 31.966499999999996
    - type: nauc_ndcg_at_1000_max
      value: 32.1421
    - type: nauc_ndcg_at_1000_std
      value: 1.9602000000000002
    - type: nauc_ndcg_at_1000_diff1
      value: 32.6747
    - type: nauc_map_at_1_max
      value: 28.973
    - type: nauc_map_at_1_std
      value: -4.6768
    - type: nauc_map_at_1_diff1
      value: 40.726600000000005
    - type: nauc_map_at_3_max
      value: 29.9942
    - type: nauc_map_at_3_std
      value: -3.7635
    - type: nauc_map_at_3_diff1
      value: 35.5655
    - type: nauc_map_at_5_max
      value: 30.157099999999996
    - type: nauc_map_at_5_std
      value: -3.3414
    - type: nauc_map_at_5_diff1
      value: 35.085699999999996
    - type: nauc_map_at_10_max
      value: 30.4178
    - type: nauc_map_at_10_std
      value: -2.7081999999999997
    - type: nauc_map_at_10_diff1
      value: 34.834700000000005
    - type: nauc_map_at_20_max
      value: 30.5785
    - type: nauc_map_at_20_std
      value: -2.1469
    - type: nauc_map_at_20_diff1
      value: 34.6132
    - type: nauc_map_at_100_max
      value: 30.755100000000002
    - type: nauc_map_at_100_std
      value: -1.846
    - type: nauc_map_at_100_diff1
      value: 34.5596
    - type: nauc_map_at_1000_max
      value: 30.818800000000003
    - type: nauc_map_at_1000_std
      value: -1.8256000000000001
    - type: nauc_map_at_1000_diff1
      value: 34.602199999999996
    - type: nauc_recall_at_1_max
      value: 28.973
    - type: nauc_recall_at_1_std
      value: -4.6768
    - type: nauc_recall_at_1_diff1
      value: 40.726600000000005
    - type: nauc_recall_at_3_max
      value: 28.962300000000003
    - type: nauc_recall_at_3_std
      value: -2.8797
    - type: nauc_recall_at_3_diff1
      value: 29.9765
    - type: nauc_recall_at_5_max
      value: 28.193
    - type: nauc_recall_at_5_std
      value: -1.6741
    - type: nauc_recall_at_5_diff1
      value: 27.825100000000003
    - type: nauc_recall_at_10_max
      value: 28.266099999999998
    - type: nauc_recall_at_10_std
      value: 0.9544
    - type: nauc_recall_at_10_diff1
      value: 26.365499999999997
    - type: nauc_recall_at_20_max
      value: 28.839
    - type: nauc_recall_at_20_std
      value: 6.809
    - type: nauc_recall_at_20_diff1
      value: 22.761400000000002
    - type: nauc_recall_at_100_max
      value: 29.2235
    - type: nauc_recall_at_100_std
      value: 15.3679
    - type: nauc_recall_at_100_diff1
      value: 19.3302
    - type: nauc_recall_at_1000_max
      value: 27.954800000000002
    - type: nauc_recall_at_1000_std
      value: 25.5618
    - type: nauc_recall_at_1000_diff1
      value: 17.749100000000002
    - type: nauc_precision_at_1_max
      value: 32.1973
    - type: nauc_precision_at_1_std
      value: -3.8459
    - type: nauc_precision_at_1_diff1
      value: 40.2485
    - type: nauc_precision_at_3_max
      value: 33.3915
    - type: nauc_precision_at_3_std
      value: -1.7868
    - type: nauc_precision_at_3_diff1
      value: 29.0619
    - type: nauc_precision_at_5_max
      value: 33.0357
    - type: nauc_precision_at_5_std
      value: 0.7308
    - type: nauc_precision_at_5_diff1
      value: 25.966299999999997
    - type: nauc_precision_at_10_max
      value: 33.1657
    - type: nauc_precision_at_10_std
      value: 4.3635
    - type: nauc_precision_at_10_diff1
      value: 23.5546
    - type: nauc_precision_at_20_max
      value: 32.9354
    - type: nauc_precision_at_20_std
      value: 10.2754
    - type: nauc_precision_at_20_diff1
      value: 18.9755
    - type: nauc_precision_at_100_max
      value: 30.0047
    - type: nauc_precision_at_100_std
      value: 14.9007
    - type: nauc_precision_at_100_diff1
      value: 10.6748
    - type: nauc_precision_at_1000_max
      value: 24.2685
    - type: nauc_precision_at_1000_std
      value: 10.8307
    - type: nauc_precision_at_1000_diff1
      value: 1.3375
    - type: nauc_mrr_at_1_max
      value: 32.1973
    - type: nauc_mrr_at_1_std
      value: -3.8459
    - type: nauc_mrr_at_1_diff1
      value: 40.2485
    - type: nauc_mrr_at_3_max
      value: 32.670100000000005
    - type: nauc_mrr_at_3_std
      value: -2.7189
    - type: nauc_mrr_at_3_diff1
      value: 35.8073
    - type: nauc_mrr_at_5_max
      value: 32.4756
    - type: nauc_mrr_at_5_std
      value: -2.2318000000000002
    - type: nauc_mrr_at_5_diff1
      value: 35.2567
    - type: nauc_mrr_at_10_max
      value: 32.594699999999996
    - type: nauc_mrr_at_10_std
      value: -1.8573
    - type: nauc_mrr_at_10_diff1
      value: 35.268100000000004
    - type: nauc_mrr_at_20_max
      value: 32.7337
    - type: nauc_mrr_at_20_std
      value: -1.3544
    - type: nauc_mrr_at_20_diff1
      value: 35.0493
    - type: nauc_mrr_at_100_max
      value: 32.775999999999996
    - type: nauc_mrr_at_100_std
      value: -1.2326
    - type: nauc_mrr_at_100_diff1
      value: 35.0304
    - type: nauc_mrr_at_1000_max
      value: 32.7772
    - type: nauc_mrr_at_1000_std
      value: -1.2438
    - type: nauc_mrr_at_1000_diff1
      value: 35.0535
    - type: main_score
      value: 29.452
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
      value: 32.556000000000004
    - type: ndcg_at_3
      value: 36.928
    - type: ndcg_at_5
      value: 39.116
    - type: ndcg_at_10
      value: 41.801
    - type: ndcg_at_20
      value: 44.080999999999996
    - type: ndcg_at_100
      value: 47.138999999999996
    - type: ndcg_at_1000
      value: 49.372
    - type: map_at_1
      value: 27.062
    - type: map_at_3
      value: 33.616
    - type: map_at_5
      value: 35.181000000000004
    - type: map_at_10
      value: 36.431000000000004
    - type: map_at_20
      value: 37.15
    - type: map_at_100
      value: 37.662
    - type: map_at_1000
      value: 37.763999999999996
    - type: recall_at_1
      value: 27.062
    - type: recall_at_3
      value: 40.199
    - type: recall_at_5
      value: 46.025
    - type: recall_at_10
      value: 53.973000000000006
    - type: recall_at_20
      value: 61.989000000000004
    - type: recall_at_100
      value: 76.537
    - type: recall_at_1000
      value: 92.087
    - type: precision_at_1
      value: 32.556000000000004
    - type: precision_at_3
      value: 16.915
    - type: precision_at_5
      value: 11.791
    - type: precision_at_10
      value: 7.034
    - type: precision_at_20
      value: 4.1739999999999995
    - type: precision_at_100
      value: 1.089
    - type: precision_at_1000
      value: 0.13799999999999998
    - type: mrr_at_1
      value: 32.556000000000004
    - type: mrr_at_3
      value: 38.339600000000004
    - type: mrr_at_5
      value: 39.696799999999996
    - type: mrr_at_10
      value: 40.7987
    - type: mrr_at_20
      value: 41.3962
    - type: mrr_at_100
      value: 41.7337
    - type: mrr_at_1000
      value: 41.794399999999996
    - type: nauc_ndcg_at_1_max
      value: 43.5112
    - type: nauc_ndcg_at_1_std
      value: -9.9968
    - type: nauc_ndcg_at_1_diff1
      value: 54.4148
    - type: nauc_ndcg_at_3_max
      value: 44.4173
    - type: nauc_ndcg_at_3_std
      value: -4.9704999999999995
    - type: nauc_ndcg_at_3_diff1
      value: 49.746
    - type: nauc_ndcg_at_5_max
      value: 43.944100000000006
    - type: nauc_ndcg_at_5_std
      value: -3.8952
    - type: nauc_ndcg_at_5_diff1
      value: 48.2127
    - type: nauc_ndcg_at_10_max
      value: 43.0905
    - type: nauc_ndcg_at_10_std
      value: -3.6698
    - type: nauc_ndcg_at_10_diff1
      value: 46.8763
    - type: nauc_ndcg_at_20_max
      value: 42.6245
    - type: nauc_ndcg_at_20_std
      value: -4.1508
    - type: nauc_ndcg_at_20_diff1
      value: 46.0823
    - type: nauc_ndcg_at_100_max
      value: 42.9829
    - type: nauc_ndcg_at_100_std
      value: -3.2881
    - type: nauc_ndcg_at_100_diff1
      value: 46.9669
    - type: nauc_ndcg_at_1000_max
      value: 43.3769
    - type: nauc_ndcg_at_1000_std
      value: -2.6679
    - type: nauc_ndcg_at_1000_diff1
      value: 47.3983
    - type: nauc_map_at_1_max
      value: 41.5528
    - type: nauc_map_at_1_std
      value: -11.307599999999999
    - type: nauc_map_at_1_diff1
      value: 54.931700000000006
    - type: nauc_map_at_3_max
      value: 43.2776
    - type: nauc_map_at_3_std
      value: -7.421800000000001
    - type: nauc_map_at_3_diff1
      value: 51.1883
    - type: nauc_map_at_5_max
      value: 43.4821
    - type: nauc_map_at_5_std
      value: -6.2339
    - type: nauc_map_at_5_diff1
      value: 50.1494
    - type: nauc_map_at_10_max
      value: 43.3333
    - type: nauc_map_at_10_std
      value: -6.065
    - type: nauc_map_at_10_diff1
      value: 49.661100000000005
    - type: nauc_map_at_20_max
      value: 43.231
    - type: nauc_map_at_20_std
      value: -6.2244
    - type: nauc_map_at_20_diff1
      value: 49.407000000000004
    - type: nauc_map_at_100_max
      value: 43.3803
    - type: nauc_map_at_100_std
      value: -5.9752
    - type: nauc_map_at_100_diff1
      value: 49.5411
    - type: nauc_map_at_1000_max
      value: 43.4007
    - type: nauc_map_at_1000_std
      value: -5.9336
    - type: nauc_map_at_1000_diff1
      value: 49.5578
    - type: nauc_recall_at_1_max
      value: 41.5528
    - type: nauc_recall_at_1_std
      value: -11.307599999999999
    - type: nauc_recall_at_1_diff1
      value: 54.931700000000006
    - type: nauc_recall_at_3_max
      value: 42.6893
    - type: nauc_recall_at_3_std
      value: -2.3828
    - type: nauc_recall_at_3_diff1
      value: 46.050999999999995
    - type: nauc_recall_at_5_max
      value: 41.6989
    - type: nauc_recall_at_5_std
      value: 1.0116
    - type: nauc_recall_at_5_diff1
      value: 41.5014
    - type: nauc_recall_at_10_max
      value: 37.9823
    - type: nauc_recall_at_10_std
      value: 1.9809
    - type: nauc_recall_at_10_diff1
      value: 36.3968
    - type: nauc_recall_at_20_max
      value: 35.5843
    - type: nauc_recall_at_20_std
      value: 0.1044
    - type: nauc_recall_at_20_diff1
      value: 32.377
    - type: nauc_recall_at_100_max
      value: 35.316900000000004
    - type: nauc_recall_at_100_std
      value: 5.6158
    - type: nauc_recall_at_100_diff1
      value: 34.8474
    - type: nauc_recall_at_1000_max
      value: 40.3589
    - type: nauc_recall_at_1000_std
      value: 36.2315
    - type: nauc_recall_at_1000_diff1
      value: 32.7652
    - type: nauc_precision_at_1_max
      value: 43.5112
    - type: nauc_precision_at_1_std
      value: -9.9968
    - type: nauc_precision_at_1_diff1
      value: 54.4148
    - type: nauc_precision_at_3_max
      value: 43.5357
    - type: nauc_precision_at_3_std
      value: 1.8129
    - type: nauc_precision_at_3_diff1
      value: 39.4033
    - type: nauc_precision_at_5_max
      value: 41.2383
    - type: nauc_precision_at_5_std
      value: 5.952500000000001
    - type: nauc_precision_at_5_diff1
      value: 32.6387
    - type: nauc_precision_at_10_max
      value: 35.8673
    - type: nauc_precision_at_10_std
      value: 6.9601
    - type: nauc_precision_at_10_diff1
      value: 25.1842
    - type: nauc_precision_at_20_max
      value: 28.9362
    - type: nauc_precision_at_20_std
      value: 7.607800000000001
    - type: nauc_precision_at_20_diff1
      value: 16.7232
    - type: nauc_precision_at_100_max
      value: 18.434800000000003
    - type: nauc_precision_at_100_std
      value: 12.987000000000002
    - type: nauc_precision_at_100_diff1
      value: 6.9893
    - type: nauc_precision_at_1000_max
      value: 1.0569
    - type: nauc_precision_at_1000_std
      value: 12.5503
    - type: nauc_precision_at_1000_diff1
      value: -7.3416
    - type: nauc_mrr_at_1_max
      value: 43.5112
    - type: nauc_mrr_at_1_std
      value: -9.9968
    - type: nauc_mrr_at_1_diff1
      value: 54.4148
    - type: nauc_mrr_at_3_max
      value: 44.642900000000004
    - type: nauc_mrr_at_3_std
      value: -5.3517
    - type: nauc_mrr_at_3_diff1
      value: 50.2935
    - type: nauc_mrr_at_5_max
      value: 44.4732
    - type: nauc_mrr_at_5_std
      value: -4.608099999999999
    - type: nauc_mrr_at_5_diff1
      value: 49.346000000000004
    - type: nauc_mrr_at_10_max
      value: 43.9489
    - type: nauc_mrr_at_10_std
      value: -4.5868
    - type: nauc_mrr_at_10_diff1
      value: 48.7018
    - type: nauc_mrr_at_20_max
      value: 43.7826
    - type: nauc_mrr_at_20_std
      value: -4.8502
    - type: nauc_mrr_at_20_diff1
      value: 48.5755
    - type: nauc_mrr_at_100_max
      value: 43.7991
    - type: nauc_mrr_at_100_std
      value: -4.8094
    - type: nauc_mrr_at_100_diff1
      value: 48.7361
    - type: nauc_mrr_at_1000_max
      value: 43.8348
    - type: nauc_mrr_at_1000_std
      value: -4.7897
    - type: nauc_mrr_at_1000_diff1
      value: 48.7638
    - type: main_score
      value: 41.801
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
      value: 30.631999999999998
    - type: ndcg_at_3
      value: 34.528999999999996
    - type: ndcg_at_5
      value: 36.547000000000004
    - type: ndcg_at_10
      value: 40.105000000000004
    - type: ndcg_at_20
      value: 42.34
    - type: ndcg_at_100
      value: 45.712
    - type: ndcg_at_1000
      value: 48.314
    - type: map_at_1
      value: 25.19
    - type: map_at_3
      value: 30.656
    - type: map_at_5
      value: 32.161
    - type: map_at_10
      value: 33.928000000000004
    - type: map_at_20
      value: 34.782999999999994
    - type: map_at_100
      value: 35.493
    - type: map_at_1000
      value: 35.713
    - type: recall_at_1
      value: 25.19
    - type: recall_at_3
      value: 36.007
    - type: recall_at_5
      value: 41.772
    - type: recall_at_10
      value: 52.117999999999995
    - type: recall_at_20
      value: 60.458
    - type: recall_at_100
      value: 77.34400000000001
    - type: recall_at_1000
      value: 93.77
    - type: precision_at_1
      value: 30.631999999999998
    - type: precision_at_3
      value: 15.942
    - type: precision_at_5
      value: 11.462
    - type: precision_at_10
      value: 7.826
    - type: precision_at_20
      value: 4.9799999999999995
    - type: precision_at_100
      value: 1.528
    - type: precision_at_1000
      value: 0.242
    - type: mrr_at_1
      value: 30.632399999999997
    - type: mrr_at_3
      value: 35.8037
    - type: mrr_at_5
      value: 37.2661
    - type: mrr_at_10
      value: 38.8381
    - type: mrr_at_20
      value: 39.4229
    - type: mrr_at_100
      value: 39.7673
    - type: mrr_at_1000
      value: 39.8227
    - type: nauc_ndcg_at_1_max
      value: 45.7418
    - type: nauc_ndcg_at_1_std
      value: 7.7497
    - type: nauc_ndcg_at_1_diff1
      value: 47.656
    - type: nauc_ndcg_at_3_max
      value: 45.6597
    - type: nauc_ndcg_at_3_std
      value: 9.6418
    - type: nauc_ndcg_at_3_diff1
      value: 43.1631
    - type: nauc_ndcg_at_5_max
      value: 44.893100000000004
    - type: nauc_ndcg_at_5_std
      value: 12.2393
    - type: nauc_ndcg_at_5_diff1
      value: 42.7159
    - type: nauc_ndcg_at_10_max
      value: 43.6388
    - type: nauc_ndcg_at_10_std
      value: 12.0574
    - type: nauc_ndcg_at_10_diff1
      value: 41.4018
    - type: nauc_ndcg_at_20_max
      value: 43.8549
    - type: nauc_ndcg_at_20_std
      value: 14.065900000000001
    - type: nauc_ndcg_at_20_diff1
      value: 41.056
    - type: nauc_ndcg_at_100_max
      value: 44.770700000000005
    - type: nauc_ndcg_at_100_std
      value: 14.8343
    - type: nauc_ndcg_at_100_diff1
      value: 42.2405
    - type: nauc_ndcg_at_1000_max
      value: 45.524100000000004
    - type: nauc_ndcg_at_1000_std
      value: 14.578199999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 42.3126
    - type: nauc_map_at_1_max
      value: 44.1517
    - type: nauc_map_at_1_std
      value: 3.4579
    - type: nauc_map_at_1_diff1
      value: 53.915
    - type: nauc_map_at_3_max
      value: 45.8324
    - type: nauc_map_at_3_std
      value: 6.8385
    - type: nauc_map_at_3_diff1
      value: 47.8444
    - type: nauc_map_at_5_max
      value: 45.4063
    - type: nauc_map_at_5_std
      value: 8.3539
    - type: nauc_map_at_5_diff1
      value: 47.0671
    - type: nauc_map_at_10_max
      value: 45.0727
    - type: nauc_map_at_10_std
      value: 8.6699
    - type: nauc_map_at_10_diff1
      value: 46.050200000000004
    - type: nauc_map_at_20_max
      value: 45.2504
    - type: nauc_map_at_20_std
      value: 9.7359
    - type: nauc_map_at_20_diff1
      value: 45.711200000000005
    - type: nauc_map_at_100_max
      value: 45.2055
    - type: nauc_map_at_100_std
      value: 10.2755
    - type: nauc_map_at_100_diff1
      value: 45.5556
    - type: nauc_map_at_1000_max
      value: 45.1304
    - type: nauc_map_at_1000_std
      value: 10.3956
    - type: nauc_map_at_1000_diff1
      value: 45.4084
    - type: nauc_recall_at_1_max
      value: 44.1517
    - type: nauc_recall_at_1_std
      value: 3.4579
    - type: nauc_recall_at_1_diff1
      value: 53.915
    - type: nauc_recall_at_3_max
      value: 44.349199999999996
    - type: nauc_recall_at_3_std
      value: 9.464599999999999
    - type: nauc_recall_at_3_diff1
      value: 41.302499999999995
    - type: nauc_recall_at_5_max
      value: 42.2726
    - type: nauc_recall_at_5_std
      value: 14.7778
    - type: nauc_recall_at_5_diff1
      value: 38.1663
    - type: nauc_recall_at_10_max
      value: 37.0689
    - type: nauc_recall_at_10_std
      value: 14.760699999999998
    - type: nauc_recall_at_10_diff1
      value: 32.1674
    - type: nauc_recall_at_20_max
      value: 36.1879
    - type: nauc_recall_at_20_std
      value: 22.6902
    - type: nauc_recall_at_20_diff1
      value: 28.933999999999997
    - type: nauc_recall_at_100_max
      value: 38.5222
    - type: nauc_recall_at_100_std
      value: 31.595299999999998
    - type: nauc_recall_at_100_diff1
      value: 30.495499999999996
    - type: nauc_recall_at_1000_max
      value: 59.5012
    - type: nauc_recall_at_1000_std
      value: 61.421499999999995
    - type: nauc_recall_at_1000_diff1
      value: 30.153000000000002
    - type: nauc_precision_at_1_max
      value: 45.7418
    - type: nauc_precision_at_1_std
      value: 7.7497
    - type: nauc_precision_at_1_diff1
      value: 47.656
    - type: nauc_precision_at_3_max
      value: 41.5197
    - type: nauc_precision_at_3_std
      value: 14.416200000000002
    - type: nauc_precision_at_3_diff1
      value: 27.4448
    - type: nauc_precision_at_5_max
      value: 37.372699999999995
    - type: nauc_precision_at_5_std
      value: 20.4825
    - type: nauc_precision_at_5_diff1
      value: 20.4335
    - type: nauc_precision_at_10_max
      value: 26.792899999999996
    - type: nauc_precision_at_10_std
      value: 20.895
    - type: nauc_precision_at_10_diff1
      value: 6.9729
    - type: nauc_precision_at_20_max
      value: 19.3562
    - type: nauc_precision_at_20_std
      value: 26.9338
    - type: nauc_precision_at_20_diff1
      value: -2.5024
    - type: nauc_precision_at_100_max
      value: 2.6254
    - type: nauc_precision_at_100_std
      value: 24.4194
    - type: nauc_precision_at_100_diff1
      value: -14.6956
    - type: nauc_precision_at_1000_max
      value: -7.0939000000000005
    - type: nauc_precision_at_1000_std
      value: 17.2116
    - type: nauc_precision_at_1000_diff1
      value: -23.3519
    - type: nauc_mrr_at_1_max
      value: 45.7418
    - type: nauc_mrr_at_1_std
      value: 7.7497
    - type: nauc_mrr_at_1_diff1
      value: 47.656
    - type: nauc_mrr_at_3_max
      value: 44.974799999999995
    - type: nauc_mrr_at_3_std
      value: 10.0484
    - type: nauc_mrr_at_3_diff1
      value: 42.5053
    - type: nauc_mrr_at_5_max
      value: 45.0004
    - type: nauc_mrr_at_5_std
      value: 11.505700000000001
    - type: nauc_mrr_at_5_diff1
      value: 42.0568
    - type: nauc_mrr_at_10_max
      value: 44.5236
    - type: nauc_mrr_at_10_std
      value: 11.6009
    - type: nauc_mrr_at_10_diff1
      value: 41.5394
    - type: nauc_mrr_at_20_max
      value: 44.568400000000004
    - type: nauc_mrr_at_20_std
      value: 11.9612
    - type: nauc_mrr_at_20_diff1
      value: 41.4954
    - type: nauc_mrr_at_100_max
      value: 44.6377
    - type: nauc_mrr_at_100_std
      value: 12.0293
    - type: nauc_mrr_at_100_diff1
      value: 41.6504
    - type: nauc_mrr_at_1000_max
      value: 44.650099999999995
    - type: nauc_mrr_at_1000_std
      value: 12.0106
    - type: nauc_mrr_at_1000_diff1
      value: 41.6595
    - type: main_score
      value: 40.105000000000004
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
      value: 21.811
    - type: ndcg_at_3
      value: 27.472
    - type: ndcg_at_5
      value: 29.755
    - type: ndcg_at_10
      value: 32.561
    - type: ndcg_at_20
      value: 34.708
    - type: ndcg_at_100
      value: 38.052
    - type: ndcg_at_1000
      value: 40.526
    - type: map_at_1
      value: 20.339
    - type: map_at_3
      value: 25.358000000000004
    - type: map_at_5
      value: 26.682
    - type: map_at_10
      value: 27.935
    - type: map_at_20
      value: 28.536
    - type: map_at_100
      value: 29.038000000000004
    - type: map_at_1000
      value: 29.149
    - type: recall_at_1
      value: 20.339
    - type: recall_at_3
      value: 31.682
    - type: recall_at_5
      value: 36.962
    - type: recall_at_10
      value: 45.095
    - type: recall_at_20
      value: 53.25
    - type: recall_at_100
      value: 70.155
    - type: recall_at_1000
      value: 88.177
    - type: precision_at_1
      value: 21.811
    - type: precision_at_3
      value: 11.706999999999999
    - type: precision_at_5
      value: 8.429
    - type: precision_at_10
      value: 5.25
    - type: precision_at_20
      value: 3.1419999999999995
    - type: precision_at_100
      value: 0.8540000000000001
    - type: precision_at_1000
      value: 0.117
    - type: mrr_at_1
      value: 21.8115
    - type: mrr_at_3
      value: 27.1411
    - type: mrr_at_5
      value: 28.490399999999998
    - type: mrr_at_10
      value: 29.616500000000002
    - type: mrr_at_20
      value: 30.215999999999998
    - type: mrr_at_100
      value: 30.6966
    - type: mrr_at_1000
      value: 30.767899999999997
    - type: nauc_ndcg_at_1_max
      value: 32.8162
    - type: nauc_ndcg_at_1_std
      value: -4.388199999999999
    - type: nauc_ndcg_at_1_diff1
      value: 44.436
    - type: nauc_ndcg_at_3_max
      value: 28.517
    - type: nauc_ndcg_at_3_std
      value: -4.3836
    - type: nauc_ndcg_at_3_diff1
      value: 35.7606
    - type: nauc_ndcg_at_5_max
      value: 28.68
    - type: nauc_ndcg_at_5_std
      value: -3.0216
    - type: nauc_ndcg_at_5_diff1
      value: 35.27
    - type: nauc_ndcg_at_10_max
      value: 26.572200000000002
    - type: nauc_ndcg_at_10_std
      value: -3.8319
    - type: nauc_ndcg_at_10_diff1
      value: 33.311099999999996
    - type: nauc_ndcg_at_20_max
      value: 26.7196
    - type: nauc_ndcg_at_20_std
      value: -1.3162
    - type: nauc_ndcg_at_20_diff1
      value: 32.202999999999996
    - type: nauc_ndcg_at_100_max
      value: 28.8134
    - type: nauc_ndcg_at_100_std
      value: -0.2386
    - type: nauc_ndcg_at_100_diff1
      value: 31.5089
    - type: nauc_ndcg_at_1000_max
      value: 28.732799999999997
    - type: nauc_ndcg_at_1000_std
      value: 0.6251
    - type: nauc_ndcg_at_1000_diff1
      value: 32.1837
    - type: nauc_map_at_1_max
      value: 29.4829
    - type: nauc_map_at_1_std
      value: -6.0044
    - type: nauc_map_at_1_diff1
      value: 43.3353
    - type: nauc_map_at_3_max
      value: 28.230499999999996
    - type: nauc_map_at_3_std
      value: -5.0899
    - type: nauc_map_at_3_diff1
      value: 37.3547
    - type: nauc_map_at_5_max
      value: 28.7927
    - type: nauc_map_at_5_std
      value: -4.254899999999999
    - type: nauc_map_at_5_diff1
      value: 37.1805
    - type: nauc_map_at_10_max
      value: 28.1557
    - type: nauc_map_at_10_std
      value: -4.4931
    - type: nauc_map_at_10_diff1
      value: 36.2513
    - type: nauc_map_at_20_max
      value: 28.205799999999996
    - type: nauc_map_at_20_std
      value: -3.6852000000000005
    - type: nauc_map_at_20_diff1
      value: 35.9099
    - type: nauc_map_at_100_max
      value: 28.604499999999998
    - type: nauc_map_at_100_std
      value: -3.4775
    - type: nauc_map_at_100_diff1
      value: 35.802
    - type: nauc_map_at_1000_max
      value: 28.6008
    - type: nauc_map_at_1000_std
      value: -3.4255
    - type: nauc_map_at_1000_diff1
      value: 35.8238
    - type: nauc_recall_at_1_max
      value: 29.4829
    - type: nauc_recall_at_1_std
      value: -6.0044
    - type: nauc_recall_at_1_diff1
      value: 43.3353
    - type: nauc_recall_at_3_max
      value: 25.4695
    - type: nauc_recall_at_3_std
      value: -4.3068
    - type: nauc_recall_at_3_diff1
      value: 30.2776
    - type: nauc_recall_at_5_max
      value: 25.901400000000002
    - type: nauc_recall_at_5_std
      value: -1.4424
    - type: nauc_recall_at_5_diff1
      value: 29.3842
    - type: nauc_recall_at_10_max
      value: 19.203200000000002
    - type: nauc_recall_at_10_std
      value: -3.8822
    - type: nauc_recall_at_10_diff1
      value: 24.0215
    - type: nauc_recall_at_20_max
      value: 18.9758
    - type: nauc_recall_at_20_std
      value: 4.9965
    - type: nauc_recall_at_20_diff1
      value: 19.5423
    - type: nauc_recall_at_100_max
      value: 27.7916
    - type: nauc_recall_at_100_std
      value: 13.4764
    - type: nauc_recall_at_100_diff1
      value: 11.1211
    - type: nauc_recall_at_1000_max
      value: 28.3949
    - type: nauc_recall_at_1000_std
      value: 41.7299
    - type: nauc_recall_at_1000_diff1
      value: 4.0583
    - type: nauc_precision_at_1_max
      value: 32.8162
    - type: nauc_precision_at_1_std
      value: -4.388199999999999
    - type: nauc_precision_at_1_diff1
      value: 44.436
    - type: nauc_precision_at_3_max
      value: 28.614
    - type: nauc_precision_at_3_std
      value: -1.5110000000000001
    - type: nauc_precision_at_3_diff1
      value: 30.165
    - type: nauc_precision_at_5_max
      value: 29.49
    - type: nauc_precision_at_5_std
      value: 3.3188000000000004
    - type: nauc_precision_at_5_diff1
      value: 27.6501
    - type: nauc_precision_at_10_max
      value: 24.334500000000002
    - type: nauc_precision_at_10_std
      value: 3.4701000000000004
    - type: nauc_precision_at_10_diff1
      value: 20.4126
    - type: nauc_precision_at_20_max
      value: 23.4494
    - type: nauc_precision_at_20_std
      value: 14.380799999999999
    - type: nauc_precision_at_20_diff1
      value: 12.5855
    - type: nauc_precision_at_100_max
      value: 25.5811
    - type: nauc_precision_at_100_std
      value: 21.0337
    - type: nauc_precision_at_100_diff1
      value: 0.1621
    - type: nauc_precision_at_1000_max
      value: 1.3693
    - type: nauc_precision_at_1000_std
      value: 22.288
    - type: nauc_precision_at_1000_diff1
      value: -18.3564
    - type: nauc_mrr_at_1_max
      value: 32.8162
    - type: nauc_mrr_at_1_std
      value: -4.388199999999999
    - type: nauc_mrr_at_1_diff1
      value: 44.436
    - type: nauc_mrr_at_3_max
      value: 31.5259
    - type: nauc_mrr_at_3_std
      value: -3.6585
    - type: nauc_mrr_at_3_diff1
      value: 38.5309
    - type: nauc_mrr_at_5_max
      value: 31.1784
    - type: nauc_mrr_at_5_std
      value: -2.5462
    - type: nauc_mrr_at_5_diff1
      value: 37.9675
    - type: nauc_mrr_at_10_max
      value: 30.0497
    - type: nauc_mrr_at_10_std
      value: -3.0947999999999998
    - type: nauc_mrr_at_10_diff1
      value: 37.0458
    - type: nauc_mrr_at_20_max
      value: 30.082900000000002
    - type: nauc_mrr_at_20_std
      value: -2.6054
    - type: nauc_mrr_at_20_diff1
      value: 36.774499999999996
    - type: nauc_mrr_at_100_max
      value: 30.424200000000003
    - type: nauc_mrr_at_100_std
      value: -2.5341
    - type: nauc_mrr_at_100_diff1
      value: 36.7384
    - type: nauc_mrr_at_1000_max
      value: 30.4217
    - type: nauc_mrr_at_1000_std
      value: -2.4978
    - type: nauc_mrr_at_1000_diff1
      value: 36.7847
    - type: main_score
      value: 32.561
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
      value: 23.388
    - type: ndcg_at_3
      value: 20.198
    - type: ndcg_at_5
      value: 21.959
    - type: ndcg_at_10
      value: 24.97
    - type: ndcg_at_20
      value: 27.26
    - type: ndcg_at_100
      value: 31.244
    - type: ndcg_at_1000
      value: 34.694
    - type: map_at_1
      value: 10.738
    - type: map_at_3
      value: 14.707
    - type: map_at_5
      value: 16.123
    - type: map_at_10
      value: 17.45
    - type: map_at_20
      value: 18.251
    - type: map_at_100
      value: 18.979
    - type: map_at_1000
      value: 19.154
    - type: recall_at_1
      value: 10.738
    - type: recall_at_3
      value: 18.590999999999998
    - type: recall_at_5
      value: 23.427
    - type: recall_at_10
      value: 30.144
    - type: recall_at_20
      value: 36.586999999999996
    - type: recall_at_100
      value: 51.757
    - type: recall_at_1000
      value: 71.353
    - type: precision_at_1
      value: 23.388
    - type: precision_at_3
      value: 14.527999999999999
    - type: precision_at_5
      value: 11.375
    - type: precision_at_10
      value: 7.674
    - type: precision_at_20
      value: 4.824
    - type: precision_at_100
      value: 1.4460000000000002
    - type: precision_at_1000
      value: 0.208
    - type: mrr_at_1
      value: 23.3876
    - type: mrr_at_3
      value: 30.640600000000003
    - type: mrr_at_5
      value: 32.7416
    - type: mrr_at_10
      value: 34.2082
    - type: mrr_at_20
      value: 34.696
    - type: mrr_at_100
      value: 35.0613
    - type: mrr_at_1000
      value: 35.1158
    - type: nauc_ndcg_at_1_max
      value: 34.0809
    - type: nauc_ndcg_at_1_std
      value: 11.4587
    - type: nauc_ndcg_at_1_diff1
      value: 24.7702
    - type: nauc_ndcg_at_3_max
      value: 36.7061
    - type: nauc_ndcg_at_3_std
      value: 15.8194
    - type: nauc_ndcg_at_3_diff1
      value: 22.0991
    - type: nauc_ndcg_at_5_max
      value: 40.0278
    - type: nauc_ndcg_at_5_std
      value: 19.442
    - type: nauc_ndcg_at_5_diff1
      value: 22.0353
    - type: nauc_ndcg_at_10_max
      value: 41.8522
    - type: nauc_ndcg_at_10_std
      value: 22.2665
    - type: nauc_ndcg_at_10_diff1
      value: 21.9219
    - type: nauc_ndcg_at_20_max
      value: 42.111599999999996
    - type: nauc_ndcg_at_20_std
      value: 24.7003
    - type: nauc_ndcg_at_20_diff1
      value: 21.1493
    - type: nauc_ndcg_at_100_max
      value: 41.4285
    - type: nauc_ndcg_at_100_std
      value: 26.8766
    - type: nauc_ndcg_at_100_diff1
      value: 20.658
    - type: nauc_ndcg_at_1000_max
      value: 41.7107
    - type: nauc_ndcg_at_1000_std
      value: 27.8879
    - type: nauc_ndcg_at_1000_diff1
      value: 20.249
    - type: nauc_map_at_1_max
      value: 39.0907
    - type: nauc_map_at_1_std
      value: 10.9155
    - type: nauc_map_at_1_diff1
      value: 27.478799999999996
    - type: nauc_map_at_3_max
      value: 39.1964
    - type: nauc_map_at_3_std
      value: 14.1844
    - type: nauc_map_at_3_diff1
      value: 24.5869
    - type: nauc_map_at_5_max
      value: 40.8907
    - type: nauc_map_at_5_std
      value: 16.6955
    - type: nauc_map_at_5_diff1
      value: 24.1453
    - type: nauc_map_at_10_max
      value: 41.8968
    - type: nauc_map_at_10_std
      value: 18.4835
    - type: nauc_map_at_10_diff1
      value: 24.0071
    - type: nauc_map_at_20_max
      value: 42.1779
    - type: nauc_map_at_20_std
      value: 19.831599999999998
    - type: nauc_map_at_20_diff1
      value: 23.6712
    - type: nauc_map_at_100_max
      value: 42.0617
    - type: nauc_map_at_100_std
      value: 20.524700000000003
    - type: nauc_map_at_100_diff1
      value: 23.5193
    - type: nauc_map_at_1000_max
      value: 42.080400000000004
    - type: nauc_map_at_1000_std
      value: 20.6099
    - type: nauc_map_at_1000_diff1
      value: 23.48
    - type: nauc_recall_at_1_max
      value: 39.0907
    - type: nauc_recall_at_1_std
      value: 10.9155
    - type: nauc_recall_at_1_diff1
      value: 27.478799999999996
    - type: nauc_recall_at_3_max
      value: 36.479099999999995
    - type: nauc_recall_at_3_std
      value: 16.370199999999997
    - type: nauc_recall_at_3_diff1
      value: 21.0061
    - type: nauc_recall_at_5_max
      value: 39.3227
    - type: nauc_recall_at_5_std
      value: 21.753800000000002
    - type: nauc_recall_at_5_diff1
      value: 18.6069
    - type: nauc_recall_at_10_max
      value: 40.7894
    - type: nauc_recall_at_10_std
      value: 25.6917
    - type: nauc_recall_at_10_diff1
      value: 17.7339
    - type: nauc_recall_at_20_max
      value: 39.6829
    - type: nauc_recall_at_20_std
      value: 30.0384
    - type: nauc_recall_at_20_diff1
      value: 15.3931
    - type: nauc_recall_at_100_max
      value: 34.9178
    - type: nauc_recall_at_100_std
      value: 34.6884
    - type: nauc_recall_at_100_diff1
      value: 13.1482
    - type: nauc_recall_at_1000_max
      value: 34.3804
    - type: nauc_recall_at_1000_std
      value: 41.778
    - type: nauc_recall_at_1000_diff1
      value: 9.3052
    - type: nauc_precision_at_1_max
      value: 34.0809
    - type: nauc_precision_at_1_std
      value: 11.4587
    - type: nauc_precision_at_1_diff1
      value: 24.7702
    - type: nauc_precision_at_3_max
      value: 31.784000000000002
    - type: nauc_precision_at_3_std
      value: 18.567700000000002
    - type: nauc_precision_at_3_diff1
      value: 16.1653
    - type: nauc_precision_at_5_max
      value: 34.9086
    - type: nauc_precision_at_5_std
      value: 25.0212
    - type: nauc_precision_at_5_diff1
      value: 14.2787
    - type: nauc_precision_at_10_max
      value: 35.1734
    - type: nauc_precision_at_10_std
      value: 30.2243
    - type: nauc_precision_at_10_diff1
      value: 11.4396
    - type: nauc_precision_at_20_max
      value: 31.347599999999996
    - type: nauc_precision_at_20_std
      value: 33.2444
    - type: nauc_precision_at_20_diff1
      value: 8.0151
    - type: nauc_precision_at_100_max
      value: 21.0705
    - type: nauc_precision_at_100_std
      value: 33.561800000000005
    - type: nauc_precision_at_100_diff1
      value: 3.1647000000000003
    - type: nauc_precision_at_1000_max
      value: 10.1267
    - type: nauc_precision_at_1000_std
      value: 28.746199999999998
    - type: nauc_precision_at_1000_diff1
      value: -4.6774000000000004
    - type: nauc_mrr_at_1_max
      value: 34.0809
    - type: nauc_mrr_at_1_std
      value: 11.4587
    - type: nauc_mrr_at_1_diff1
      value: 24.7702
    - type: nauc_mrr_at_3_max
      value: 33.799
    - type: nauc_mrr_at_3_std
      value: 16.0923
    - type: nauc_mrr_at_3_diff1
      value: 20.8456
    - type: nauc_mrr_at_5_max
      value: 35.1249
    - type: nauc_mrr_at_5_std
      value: 17.8145
    - type: nauc_mrr_at_5_diff1
      value: 20.467299999999998
    - type: nauc_mrr_at_10_max
      value: 35.856500000000004
    - type: nauc_mrr_at_10_std
      value: 18.4864
    - type: nauc_mrr_at_10_diff1
      value: 20.6532
    - type: nauc_mrr_at_20_max
      value: 35.787200000000006
    - type: nauc_mrr_at_20_std
      value: 18.607599999999998
    - type: nauc_mrr_at_20_diff1
      value: 20.6192
    - type: nauc_mrr_at_100_max
      value: 35.7134
    - type: nauc_mrr_at_100_std
      value: 18.5964
    - type: nauc_mrr_at_100_diff1
      value: 20.5979
    - type: nauc_mrr_at_1000_max
      value: 35.713499999999996
    - type: nauc_mrr_at_1000_std
      value: 18.5792
    - type: nauc_mrr_at_1000_diff1
      value: 20.610300000000002
    - type: main_score
      value: 24.97
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
      value: 15.403
    - type: ndcg_at_3
      value: 20.087
    - type: ndcg_at_5
      value: 21.72
    - type: ndcg_at_10
      value: 23.458000000000002
    - type: ndcg_at_20
      value: 24.990000000000002
    - type: ndcg_at_100
      value: 27.933000000000003
    - type: ndcg_at_1000
      value: 30.642999999999997
    - type: map_at_1
      value: 15.403
    - type: map_at_3
      value: 18.925
    - type: map_at_5
      value: 19.832
    - type: map_at_10
      value: 20.549999999999997
    - type: map_at_20
      value: 20.97
    - type: map_at_100
      value: 21.358
    - type: map_at_1000
      value: 21.447
    - type: recall_at_1
      value: 15.403
    - type: recall_at_3
      value: 23.454
    - type: recall_at_5
      value: 27.416
    - type: recall_at_10
      value: 32.786
    - type: recall_at_20
      value: 38.849000000000004
    - type: recall_at_100
      value: 54.99699999999999
    - type: recall_at_1000
      value: 77.096
    - type: precision_at_1
      value: 15.403
    - type: precision_at_3
      value: 7.818
    - type: precision_at_5
      value: 5.483
    - type: precision_at_10
      value: 3.279
    - type: precision_at_20
      value: 1.942
    - type: precision_at_100
      value: 0.5499999999999999
    - type: precision_at_1000
      value: 0.077
    - type: mrr_at_1
      value: 15.4026
    - type: mrr_at_3
      value: 18.925
    - type: mrr_at_5
      value: 19.8322
    - type: mrr_at_10
      value: 20.5497
    - type: mrr_at_20
      value: 20.9696
    - type: mrr_at_100
      value: 21.3582
    - type: mrr_at_1000
      value: 21.4471
    - type: nauc_ndcg_at_1_max
      value: 14.524799999999999
    - type: nauc_ndcg_at_1_std
      value: -14.704500000000001
    - type: nauc_ndcg_at_1_diff1
      value: 45.3337
    - type: nauc_ndcg_at_3_max
      value: 12.3014
    - type: nauc_ndcg_at_3_std
      value: -14.977199999999998
    - type: nauc_ndcg_at_3_diff1
      value: 37.6118
    - type: nauc_ndcg_at_5_max
      value: 12.015099999999999
    - type: nauc_ndcg_at_5_std
      value: -14.844399999999998
    - type: nauc_ndcg_at_5_diff1
      value: 36.439
    - type: nauc_ndcg_at_10_max
      value: 11.886800000000001
    - type: nauc_ndcg_at_10_std
      value: -14.274600000000001
    - type: nauc_ndcg_at_10_diff1
      value: 35.0552
    - type: nauc_ndcg_at_20_max
      value: 11.843
    - type: nauc_ndcg_at_20_std
      value: -13.729099999999999
    - type: nauc_ndcg_at_20_diff1
      value: 34.172999999999995
    - type: nauc_ndcg_at_100_max
      value: 12.570700000000002
    - type: nauc_ndcg_at_100_std
      value: -11.956999999999999
    - type: nauc_ndcg_at_100_diff1
      value: 33.5916
    - type: nauc_ndcg_at_1000_max
      value: 13.3025
    - type: nauc_ndcg_at_1000_std
      value: -10.6411
    - type: nauc_ndcg_at_1000_diff1
      value: 33.535900000000005
    - type: nauc_map_at_1_max
      value: 14.524799999999999
    - type: nauc_map_at_1_std
      value: -14.704500000000001
    - type: nauc_map_at_1_diff1
      value: 45.3337
    - type: nauc_map_at_3_max
      value: 12.7833
    - type: nauc_map_at_3_std
      value: -14.9312
    - type: nauc_map_at_3_diff1
      value: 39.2273
    - type: nauc_map_at_5_max
      value: 12.606200000000001
    - type: nauc_map_at_5_std
      value: -14.846200000000001
    - type: nauc_map_at_5_diff1
      value: 38.5015
    - type: nauc_map_at_10_max
      value: 12.5202
    - type: nauc_map_at_10_std
      value: -14.5979
    - type: nauc_map_at_10_diff1
      value: 37.8521
    - type: nauc_map_at_20_max
      value: 12.5101
    - type: nauc_map_at_20_std
      value: -14.444899999999999
    - type: nauc_map_at_20_diff1
      value: 37.5942
    - type: nauc_map_at_100_max
      value: 12.601399999999998
    - type: nauc_map_at_100_std
      value: -14.2092
    - type: nauc_map_at_100_diff1
      value: 37.4992
    - type: nauc_map_at_1000_max
      value: 12.6334
    - type: nauc_map_at_1000_std
      value: -14.1545
    - type: nauc_map_at_1000_diff1
      value: 37.4959
    - type: nauc_recall_at_1_max
      value: 14.524799999999999
    - type: nauc_recall_at_1_std
      value: -14.704500000000001
    - type: nauc_recall_at_1_diff1
      value: 45.3337
    - type: nauc_recall_at_3_max
      value: 11.0823
    - type: nauc_recall_at_3_std
      value: -15.088899999999999
    - type: nauc_recall_at_3_diff1
      value: 33.5456
    - type: nauc_recall_at_5_max
      value: 10.5617
    - type: nauc_recall_at_5_std
      value: -14.8289
    - type: nauc_recall_at_5_diff1
      value: 31.3732
    - type: nauc_recall_at_10_max
      value: 10.4061
    - type: nauc_recall_at_10_std
      value: -13.3346
    - type: nauc_recall_at_10_diff1
      value: 28.131099999999996
    - type: nauc_recall_at_20_max
      value: 10.2817
    - type: nauc_recall_at_20_std
      value: -11.5314
    - type: nauc_recall_at_20_diff1
      value: 25.3998
    - type: nauc_recall_at_100_max
      value: 13.818
    - type: nauc_recall_at_100_std
      value: -2.6188
    - type: nauc_recall_at_100_diff1
      value: 22.0747
    - type: nauc_recall_at_1000_max
      value: 21.893099999999997
    - type: nauc_recall_at_1000_std
      value: 16.1546
    - type: nauc_recall_at_1000_diff1
      value: 15.1476
    - type: nauc_precision_at_1_max
      value: 14.524799999999999
    - type: nauc_precision_at_1_std
      value: -14.704500000000001
    - type: nauc_precision_at_1_diff1
      value: 45.3337
    - type: nauc_precision_at_3_max
      value: 11.0823
    - type: nauc_precision_at_3_std
      value: -15.088899999999999
    - type: nauc_precision_at_3_diff1
      value: 33.5456
    - type: nauc_precision_at_5_max
      value: 10.5617
    - type: nauc_precision_at_5_std
      value: -14.8289
    - type: nauc_precision_at_5_diff1
      value: 31.3732
    - type: nauc_precision_at_10_max
      value: 10.4061
    - type: nauc_precision_at_10_std
      value: -13.3346
    - type: nauc_precision_at_10_diff1
      value: 28.131099999999996
    - type: nauc_precision_at_20_max
      value: 10.2817
    - type: nauc_precision_at_20_std
      value: -11.5314
    - type: nauc_precision_at_20_diff1
      value: 25.3998
    - type: nauc_precision_at_100_max
      value: 13.818
    - type: nauc_precision_at_100_std
      value: -2.6188
    - type: nauc_precision_at_100_diff1
      value: 22.0747
    - type: nauc_precision_at_1000_max
      value: 21.893099999999997
    - type: nauc_precision_at_1000_std
      value: 16.1546
    - type: nauc_precision_at_1000_diff1
      value: 15.1476
    - type: nauc_mrr_at_1_max
      value: 14.524799999999999
    - type: nauc_mrr_at_1_std
      value: -14.704500000000001
    - type: nauc_mrr_at_1_diff1
      value: 45.3337
    - type: nauc_mrr_at_3_max
      value: 12.7833
    - type: nauc_mrr_at_3_std
      value: -14.9312
    - type: nauc_mrr_at_3_diff1
      value: 39.2273
    - type: nauc_mrr_at_5_max
      value: 12.606200000000001
    - type: nauc_mrr_at_5_std
      value: -14.846200000000001
    - type: nauc_mrr_at_5_diff1
      value: 38.5015
    - type: nauc_mrr_at_10_max
      value: 12.5202
    - type: nauc_mrr_at_10_std
      value: -14.5979
    - type: nauc_mrr_at_10_diff1
      value: 37.8521
    - type: nauc_mrr_at_20_max
      value: 12.5101
    - type: nauc_mrr_at_20_std
      value: -14.444899999999999
    - type: nauc_mrr_at_20_diff1
      value: 37.5942
    - type: nauc_mrr_at_100_max
      value: 12.601399999999998
    - type: nauc_mrr_at_100_std
      value: -14.2092
    - type: nauc_mrr_at_100_diff1
      value: 37.4992
    - type: nauc_mrr_at_1000_max
      value: 12.6334
    - type: nauc_mrr_at_1000_std
      value: -14.1545
    - type: nauc_mrr_at_1000_diff1
      value: 37.4959
    - type: main_score
      value: 23.458000000000002
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
      value: 42.781000000000006
    - type: ndcg_at_3
      value: 53.547999999999995
    - type: ndcg_at_5
      value: 56.184999999999995
    - type: ndcg_at_10
      value: 58.455
    - type: ndcg_at_20
      value: 59.897
    - type: ndcg_at_100
      value: 61.806000000000004
    - type: ndcg_at_1000
      value: 62.769
    - type: map_at_1
      value: 42.781000000000006
    - type: map_at_3
      value: 50.92100000000001
    - type: map_at_5
      value: 52.38699999999999
    - type: map_at_10
      value: 53.335
    - type: map_at_20
      value: 53.733
    - type: map_at_100
      value: 53.998999999999995
    - type: map_at_1000
      value: 54.035
    - type: recall_at_1
      value: 42.781000000000006
    - type: recall_at_3
      value: 61.141999999999996
    - type: recall_at_5
      value: 67.533
    - type: recall_at_10
      value: 74.491
    - type: recall_at_20
      value: 80.17999999999999
    - type: recall_at_100
      value: 90.443
    - type: recall_at_1000
      value: 98.051
    - type: precision_at_1
      value: 42.781000000000006
    - type: precision_at_3
      value: 20.381
    - type: precision_at_5
      value: 13.507
    - type: precision_at_10
      value: 7.449
    - type: precision_at_20
      value: 4.009
    - type: precision_at_100
      value: 0.9039999999999999
    - type: precision_at_1000
      value: 0.098
    - type: mrr_at_1
      value: 42.8193
    - type: mrr_at_3
      value: 50.9333
    - type: mrr_at_5
      value: 52.4157
    - type: mrr_at_10
      value: 53.3551
    - type: mrr_at_20
      value: 53.7532
    - type: mrr_at_100
      value: 54.0192
    - type: mrr_at_1000
      value: 54.0547
    - type: nauc_ndcg_at_1_max
      value: 8.1476
    - type: nauc_ndcg_at_1_std
      value: -18.415599999999998
    - type: nauc_ndcg_at_1_diff1
      value: 61.467499999999994
    - type: nauc_ndcg_at_3_max
      value: 14.5702
    - type: nauc_ndcg_at_3_std
      value: -18.4765
    - type: nauc_ndcg_at_3_diff1
      value: 54.7928
    - type: nauc_ndcg_at_5_max
      value: 15.2642
    - type: nauc_ndcg_at_5_std
      value: -18.2014
    - type: nauc_ndcg_at_5_diff1
      value: 53.9847
    - type: nauc_ndcg_at_10_max
      value: 15.0742
    - type: nauc_ndcg_at_10_std
      value: -17.8811
    - type: nauc_ndcg_at_10_diff1
      value: 53.9565
    - type: nauc_ndcg_at_20_max
      value: 14.7067
    - type: nauc_ndcg_at_20_std
      value: -17.618000000000002
    - type: nauc_ndcg_at_20_diff1
      value: 54.041399999999996
    - type: nauc_ndcg_at_100_max
      value: 14.4373
    - type: nauc_ndcg_at_100_std
      value: -17.1309
    - type: nauc_ndcg_at_100_diff1
      value: 54.5959
    - type: nauc_ndcg_at_1000_max
      value: 14.1768
    - type: nauc_ndcg_at_1000_std
      value: -17.2829
    - type: nauc_ndcg_at_1000_diff1
      value: 55.053799999999995
    - type: nauc_map_at_1_max
      value: 8.1476
    - type: nauc_map_at_1_std
      value: -18.415599999999998
    - type: nauc_map_at_1_diff1
      value: 61.467499999999994
    - type: nauc_map_at_3_max
      value: 12.961400000000001
    - type: nauc_map_at_3_std
      value: -18.4454
    - type: nauc_map_at_3_diff1
      value: 56.42
    - type: nauc_map_at_5_max
      value: 13.295599999999999
    - type: nauc_map_at_5_std
      value: -18.293599999999998
    - type: nauc_map_at_5_diff1
      value: 56.033
    - type: nauc_map_at_10_max
      value: 13.189600000000002
    - type: nauc_map_at_10_std
      value: -18.169
    - type: nauc_map_at_10_diff1
      value: 56.0467
    - type: nauc_map_at_20_max
      value: 13.0847
    - type: nauc_map_at_20_std
      value: -18.1099
    - type: nauc_map_at_20_diff1
      value: 56.0909
    - type: nauc_map_at_100_max
      value: 13.0384
    - type: nauc_map_at_100_std
      value: -18.0582
    - type: nauc_map_at_100_diff1
      value: 56.1735
    - type: nauc_map_at_1000_max
      value: 13.03
    - type: nauc_map_at_1000_std
      value: -18.0598
    - type: nauc_map_at_1000_diff1
      value: 56.1901
    - type: nauc_recall_at_1_max
      value: 8.1476
    - type: nauc_recall_at_1_std
      value: -18.415599999999998
    - type: nauc_recall_at_1_diff1
      value: 61.467499999999994
    - type: nauc_recall_at_3_max
      value: 19.6416
    - type: nauc_recall_at_3_std
      value: -18.582099999999997
    - type: nauc_recall_at_3_diff1
      value: 49.6845
    - type: nauc_recall_at_5_max
      value: 22.2239
    - type: nauc_recall_at_5_std
      value: -17.847099999999998
    - type: nauc_recall_at_5_diff1
      value: 46.739999999999995
    - type: nauc_recall_at_10_max
      value: 22.8276
    - type: nauc_recall_at_10_std
      value: -16.486600000000003
    - type: nauc_recall_at_10_diff1
      value: 45.2586
    - type: nauc_recall_at_20_max
      value: 22.2364
    - type: nauc_recall_at_20_std
      value: -14.5036
    - type: nauc_recall_at_20_diff1
      value: 43.7903
    - type: nauc_recall_at_100_max
      value: 25.254700000000003
    - type: nauc_recall_at_100_std
      value: -3.9357
    - type: nauc_recall_at_100_diff1
      value: 42.6367
    - type: nauc_recall_at_1000_max
      value: 38.3787
    - type: nauc_recall_at_1000_std
      value: 27.075100000000003
    - type: nauc_recall_at_1000_diff1
      value: 44.277
    - type: nauc_precision_at_1_max
      value: 8.1476
    - type: nauc_precision_at_1_std
      value: -18.415599999999998
    - type: nauc_precision_at_1_diff1
      value: 61.467499999999994
    - type: nauc_precision_at_3_max
      value: 19.6416
    - type: nauc_precision_at_3_std
      value: -18.582099999999997
    - type: nauc_precision_at_3_diff1
      value: 49.6845
    - type: nauc_precision_at_5_max
      value: 22.2239
    - type: nauc_precision_at_5_std
      value: -17.847099999999998
    - type: nauc_precision_at_5_diff1
      value: 46.739999999999995
    - type: nauc_precision_at_10_max
      value: 22.8276
    - type: nauc_precision_at_10_std
      value: -16.486600000000003
    - type: nauc_precision_at_10_diff1
      value: 45.2586
    - type: nauc_precision_at_20_max
      value: 22.2364
    - type: nauc_precision_at_20_std
      value: -14.5036
    - type: nauc_precision_at_20_diff1
      value: 43.7903
    - type: nauc_precision_at_100_max
      value: 25.254700000000003
    - type: nauc_precision_at_100_std
      value: -3.9357
    - type: nauc_precision_at_100_diff1
      value: 42.6367
    - type: nauc_precision_at_1000_max
      value: 38.3787
    - type: nauc_precision_at_1000_std
      value: 27.075100000000003
    - type: nauc_precision_at_1000_diff1
      value: 44.277
    - type: nauc_mrr_at_1_max
      value: 7.7336
    - type: nauc_mrr_at_1_std
      value: -18.2617
    - type: nauc_mrr_at_1_diff1
      value: 61.3653
    - type: nauc_mrr_at_3_max
      value: 12.6751
    - type: nauc_mrr_at_3_std
      value: -18.3779
    - type: nauc_mrr_at_3_diff1
      value: 56.383
    - type: nauc_mrr_at_5_max
      value: 13.031200000000002
    - type: nauc_mrr_at_5_std
      value: -18.252499999999998
    - type: nauc_mrr_at_5_diff1
      value: 55.9734
    - type: nauc_mrr_at_10_max
      value: 12.934399999999998
    - type: nauc_mrr_at_10_std
      value: -18.0918
    - type: nauc_mrr_at_10_diff1
      value: 55.9883
    - type: nauc_mrr_at_20_max
      value: 12.8271
    - type: nauc_mrr_at_20_std
      value: -18.0345
    - type: nauc_mrr_at_20_diff1
      value: 56.033100000000005
    - type: nauc_mrr_at_100_max
      value: 12.7798
    - type: nauc_mrr_at_100_std
      value: -17.983
    - type: nauc_mrr_at_100_diff1
      value: 56.115700000000004
    - type: nauc_mrr_at_1000_max
      value: 12.771099999999999
    - type: nauc_mrr_at_1000_std
      value: -17.9844
    - type: nauc_mrr_at_1000_diff1
      value: 56.1323
    - type: main_score
      value: 58.455
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
      value: 29.32
    - type: ndcg_at_3
      value: 37.202
    - type: ndcg_at_5
      value: 39.399
    - type: ndcg_at_10
      value: 41.583
    - type: ndcg_at_20
      value: 43.156
    - type: ndcg_at_100
      value: 45.506
    - type: ndcg_at_1000
      value: 47.28
    - type: map_at_1
      value: 29.32
    - type: map_at_3
      value: 35.266999999999996
    - type: map_at_5
      value: 36.489
    - type: map_at_10
      value: 37.399
    - type: map_at_20
      value: 37.829
    - type: map_at_100
      value: 38.149
    - type: map_at_1000
      value: 38.208
    - type: recall_at_1
      value: 29.32
    - type: recall_at_3
      value: 42.801
    - type: recall_at_5
      value: 48.123
    - type: recall_at_10
      value: 54.82599999999999
    - type: recall_at_20
      value: 61.06700000000001
    - type: recall_at_100
      value: 73.817
    - type: recall_at_1000
      value: 88.189
    - type: precision_at_1
      value: 29.32
    - type: precision_at_3
      value: 14.267
    - type: precision_at_5
      value: 9.625
    - type: precision_at_10
      value: 5.483
    - type: precision_at_20
      value: 3.053
    - type: precision_at_100
      value: 0.738
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 29.3203
    - type: mrr_at_3
      value: 35.2661
    - type: mrr_at_5
      value: 36.4878
    - type: mrr_at_10
      value: 37.398399999999995
    - type: mrr_at_20
      value: 37.8278
    - type: mrr_at_100
      value: 38.1474
    - type: mrr_at_1000
      value: 38.2072
    - type: nauc_ndcg_at_1_max
      value: 27.608
    - type: nauc_ndcg_at_1_std
      value: -0.1578
    - type: nauc_ndcg_at_1_diff1
      value: 50.7213
    - type: nauc_ndcg_at_3_max
      value: 28.488799999999998
    - type: nauc_ndcg_at_3_std
      value: 0.8798
    - type: nauc_ndcg_at_3_diff1
      value: 46.4513
    - type: nauc_ndcg_at_5_max
      value: 28.2088
    - type: nauc_ndcg_at_5_std
      value: 1.536
    - type: nauc_ndcg_at_5_diff1
      value: 45.5291
    - type: nauc_ndcg_at_10_max
      value: 28.076600000000003
    - type: nauc_ndcg_at_10_std
      value: 2.4101999999999997
    - type: nauc_ndcg_at_10_diff1
      value: 45.0789
    - type: nauc_ndcg_at_20_max
      value: 28.1814
    - type: nauc_ndcg_at_20_std
      value: 3.1981999999999995
    - type: nauc_ndcg_at_20_diff1
      value: 44.8012
    - type: nauc_ndcg_at_100_max
      value: 27.9818
    - type: nauc_ndcg_at_100_std
      value: 3.8790999999999998
    - type: nauc_ndcg_at_100_diff1
      value: 44.7506
    - type: nauc_ndcg_at_1000_max
      value: 28.1483
    - type: nauc_ndcg_at_1000_std
      value: 3.8562
    - type: nauc_ndcg_at_1000_diff1
      value: 45.1726
    - type: nauc_map_at_1_max
      value: 27.608
    - type: nauc_map_at_1_std
      value: -0.1578
    - type: nauc_map_at_1_diff1
      value: 50.7213
    - type: nauc_map_at_3_max
      value: 28.3097
    - type: nauc_map_at_3_std
      value: 0.6224000000000001
    - type: nauc_map_at_3_diff1
      value: 47.4366
    - type: nauc_map_at_5_max
      value: 28.157500000000002
    - type: nauc_map_at_5_std
      value: 0.9838
    - type: nauc_map_at_5_diff1
      value: 46.9294
    - type: nauc_map_at_10_max
      value: 28.097
    - type: nauc_map_at_10_std
      value: 1.3426
    - type: nauc_map_at_10_diff1
      value: 46.7574
    - type: nauc_map_at_20_max
      value: 28.124100000000002
    - type: nauc_map_at_20_std
      value: 1.5459
    - type: nauc_map_at_20_diff1
      value: 46.6828
    - type: nauc_map_at_100_max
      value: 28.0887
    - type: nauc_map_at_100_std
      value: 1.6311
    - type: nauc_map_at_100_diff1
      value: 46.684599999999996
    - type: nauc_map_at_1000_max
      value: 28.0938
    - type: nauc_map_at_1000_std
      value: 1.6345999999999998
    - type: nauc_map_at_1000_diff1
      value: 46.6979
    - type: nauc_recall_at_1_max
      value: 27.608
    - type: nauc_recall_at_1_std
      value: -0.1578
    - type: nauc_recall_at_1_diff1
      value: 50.7213
    - type: nauc_recall_at_3_max
      value: 28.982000000000003
    - type: nauc_recall_at_3_std
      value: 1.6101
    - type: nauc_recall_at_3_diff1
      value: 43.6847
    - type: nauc_recall_at_5_max
      value: 28.297800000000002
    - type: nauc_recall_at_5_std
      value: 3.2162
    - type: nauc_recall_at_5_diff1
      value: 41.402899999999995
    - type: nauc_recall_at_10_max
      value: 27.915499999999998
    - type: nauc_recall_at_10_std
      value: 6.0788
    - type: nauc_recall_at_10_diff1
      value: 39.7106
    - type: nauc_recall_at_20_max
      value: 28.3661
    - type: nauc_recall_at_20_std
      value: 9.8068
    - type: nauc_recall_at_20_diff1
      value: 38.153
    - type: nauc_recall_at_100_max
      value: 27.114300000000004
    - type: nauc_recall_at_100_std
      value: 17.0125
    - type: nauc_recall_at_100_diff1
      value: 35.6053
    - type: nauc_recall_at_1000_max
      value: 29.8655
    - type: nauc_recall_at_1000_std
      value: 28.480800000000002
    - type: nauc_recall_at_1000_diff1
      value: 35.9375
    - type: nauc_precision_at_1_max
      value: 27.608
    - type: nauc_precision_at_1_std
      value: -0.1578
    - type: nauc_precision_at_1_diff1
      value: 50.7213
    - type: nauc_precision_at_3_max
      value: 28.982000000000003
    - type: nauc_precision_at_3_std
      value: 1.6101
    - type: nauc_precision_at_3_diff1
      value: 43.6847
    - type: nauc_precision_at_5_max
      value: 28.297800000000002
    - type: nauc_precision_at_5_std
      value: 3.2162
    - type: nauc_precision_at_5_diff1
      value: 41.402899999999995
    - type: nauc_precision_at_10_max
      value: 27.915499999999998
    - type: nauc_precision_at_10_std
      value: 6.0788
    - type: nauc_precision_at_10_diff1
      value: 39.7106
    - type: nauc_precision_at_20_max
      value: 28.3661
    - type: nauc_precision_at_20_std
      value: 9.8068
    - type: nauc_precision_at_20_diff1
      value: 38.153
    - type: nauc_precision_at_100_max
      value: 27.114300000000004
    - type: nauc_precision_at_100_std
      value: 17.0125
    - type: nauc_precision_at_100_diff1
      value: 35.6053
    - type: nauc_precision_at_1000_max
      value: 29.8655
    - type: nauc_precision_at_1000_std
      value: 28.480800000000002
    - type: nauc_precision_at_1000_diff1
      value: 35.9375
    - type: nauc_mrr_at_1_max
      value: 27.608
    - type: nauc_mrr_at_1_std
      value: -0.1578
    - type: nauc_mrr_at_1_diff1
      value: 50.7213
    - type: nauc_mrr_at_3_max
      value: 28.310200000000002
    - type: nauc_mrr_at_3_std
      value: 0.6187
    - type: nauc_mrr_at_3_diff1
      value: 47.4396
    - type: nauc_mrr_at_5_max
      value: 28.1581
    - type: nauc_mrr_at_5_std
      value: 0.9801000000000001
    - type: nauc_mrr_at_5_diff1
      value: 46.9325
    - type: nauc_mrr_at_10_max
      value: 28.097499999999997
    - type: nauc_mrr_at_10_std
      value: 1.3393
    - type: nauc_mrr_at_10_diff1
      value: 46.760600000000004
    - type: nauc_mrr_at_20_max
      value: 28.124700000000004
    - type: nauc_mrr_at_20_std
      value: 1.5427
    - type: nauc_mrr_at_20_diff1
      value: 46.686
    - type: nauc_mrr_at_100_max
      value: 28.0893
    - type: nauc_mrr_at_100_std
      value: 1.6274
    - type: nauc_mrr_at_100_diff1
      value: 46.6879
    - type: nauc_mrr_at_1000_max
      value: 28.0943
    - type: nauc_mrr_at_1000_std
      value: 1.6312
    - type: nauc_mrr_at_1000_diff1
      value: 46.7012
    - type: main_score
      value: 41.583
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
      value: 30.294999999999998
    - type: ndcg_at_3
      value: 38.102000000000004
    - type: ndcg_at_5
      value: 40.164
    - type: ndcg_at_10
      value: 42.041000000000004
    - type: ndcg_at_20
      value: 43.464000000000006
    - type: ndcg_at_100
      value: 45.791
    - type: ndcg_at_1000
      value: 47.689
    - type: map_at_1
      value: 30.294999999999998
    - type: map_at_3
      value: 36.19
    - type: map_at_5
      value: 37.332
    - type: map_at_10
      value: 38.112
    - type: map_at_20
      value: 38.507999999999996
    - type: map_at_100
      value: 38.812999999999995
    - type: map_at_1000
      value: 38.875
    - type: recall_at_1
      value: 30.294999999999998
    - type: recall_at_3
      value: 43.634
    - type: recall_at_5
      value: 48.648
    - type: recall_at_10
      value: 54.421
    - type: recall_at_20
      value: 60.012
    - type: recall_at_100
      value: 72.80499999999999
    - type: recall_at_1000
      value: 88.271
    - type: precision_at_1
      value: 30.294999999999998
    - type: precision_at_3
      value: 14.545
    - type: precision_at_5
      value: 9.73
    - type: precision_at_10
      value: 5.442
    - type: precision_at_20
      value: 3.001
    - type: precision_at_100
      value: 0.728
    - type: precision_at_1000
      value: 0.08800000000000001
    - type: mrr_at_1
      value: 30.294700000000002
    - type: mrr_at_3
      value: 36.1845
    - type: mrr_at_5
      value: 37.3271
    - type: mrr_at_10
      value: 38.1071
    - type: mrr_at_20
      value: 38.502700000000004
    - type: mrr_at_100
      value: 38.8081
    - type: mrr_at_1000
      value: 38.8701
    - type: nauc_ndcg_at_1_max
      value: 26.3264
    - type: nauc_ndcg_at_1_std
      value: -4.8982
    - type: nauc_ndcg_at_1_diff1
      value: 50.14189999999999
    - type: nauc_ndcg_at_3_max
      value: 27.4968
    - type: nauc_ndcg_at_3_std
      value: -4.1065
    - type: nauc_ndcg_at_3_diff1
      value: 46.0956
    - type: nauc_ndcg_at_5_max
      value: 28.409299999999998
    - type: nauc_ndcg_at_5_std
      value: -3.7853
    - type: nauc_ndcg_at_5_diff1
      value: 45.6748
    - type: nauc_ndcg_at_10_max
      value: 27.942
    - type: nauc_ndcg_at_10_std
      value: -3.3216
    - type: nauc_ndcg_at_10_diff1
      value: 44.6236
    - type: nauc_ndcg_at_20_max
      value: 27.47
    - type: nauc_ndcg_at_20_std
      value: -3.1514
    - type: nauc_ndcg_at_20_diff1
      value: 44.74
    - type: nauc_ndcg_at_100_max
      value: 27.4711
    - type: nauc_ndcg_at_100_std
      value: -3.0054999999999996
    - type: nauc_ndcg_at_100_diff1
      value: 44.5073
    - type: nauc_ndcg_at_1000_max
      value: 27.7016
    - type: nauc_ndcg_at_1000_std
      value: -3.0528
    - type: nauc_ndcg_at_1000_diff1
      value: 44.8851
    - type: nauc_map_at_1_max
      value: 26.3264
    - type: nauc_map_at_1_std
      value: -4.8982
    - type: nauc_map_at_1_diff1
      value: 50.14189999999999
    - type: nauc_map_at_3_max
      value: 27.279500000000002
    - type: nauc_map_at_3_std
      value: -4.2798
    - type: nauc_map_at_3_diff1
      value: 47.0454
    - type: nauc_map_at_5_max
      value: 27.776600000000002
    - type: nauc_map_at_5_std
      value: -4.1068
    - type: nauc_map_at_5_diff1
      value: 46.8171
    - type: nauc_map_at_10_max
      value: 27.589399999999998
    - type: nauc_map_at_10_std
      value: -3.8844
    - type: nauc_map_at_10_diff1
      value: 46.4013
    - type: nauc_map_at_20_max
      value: 27.455099999999998
    - type: nauc_map_at_20_std
      value: -3.8475
    - type: nauc_map_at_20_diff1
      value: 46.4395
    - type: nauc_map_at_100_max
      value: 27.470299999999998
    - type: nauc_map_at_100_std
      value: -3.8240000000000003
    - type: nauc_map_at_100_diff1
      value: 46.4176
    - type: nauc_map_at_1000_max
      value: 27.473
    - type: nauc_map_at_1000_std
      value: -3.8289999999999997
    - type: nauc_map_at_1000_diff1
      value: 46.427
    - type: nauc_recall_at_1_max
      value: 26.3264
    - type: nauc_recall_at_1_std
      value: -4.8982
    - type: nauc_recall_at_1_diff1
      value: 50.14189999999999
    - type: nauc_recall_at_3_max
      value: 28.089599999999997
    - type: nauc_recall_at_3_std
      value: -3.6197
    - type: nauc_recall_at_3_diff1
      value: 43.4007
    - type: nauc_recall_at_5_max
      value: 30.3494
    - type: nauc_recall_at_5_std
      value: -2.8134
    - type: nauc_recall_at_5_diff1
      value: 42.3267
    - type: nauc_recall_at_10_max
      value: 28.9106
    - type: nauc_recall_at_10_std
      value: -1.4690999999999999
    - type: nauc_recall_at_10_diff1
      value: 38.7477
    - type: nauc_recall_at_20_max
      value: 27.0023
    - type: nauc_recall_at_20_std
      value: -0.5613
    - type: nauc_recall_at_20_diff1
      value: 38.874700000000004
    - type: nauc_recall_at_100_max
      value: 26.4945
    - type: nauc_recall_at_100_std
      value: 1.1353
    - type: nauc_recall_at_100_diff1
      value: 35.297200000000004
    - type: nauc_recall_at_1000_max
      value: 31.464100000000002
    - type: nauc_recall_at_1000_std
      value: 5.16
    - type: nauc_recall_at_1000_diff1
      value: 34.5536
    - type: nauc_precision_at_1_max
      value: 26.3264
    - type: nauc_precision_at_1_std
      value: -4.8982
    - type: nauc_precision_at_1_diff1
      value: 50.14189999999999
    - type: nauc_precision_at_3_max
      value: 28.089599999999997
    - type: nauc_precision_at_3_std
      value: -3.6197
    - type: nauc_precision_at_3_diff1
      value: 43.4007
    - type: nauc_precision_at_5_max
      value: 30.3494
    - type: nauc_precision_at_5_std
      value: -2.8134
    - type: nauc_precision_at_5_diff1
      value: 42.3267
    - type: nauc_precision_at_10_max
      value: 28.9106
    - type: nauc_precision_at_10_std
      value: -1.4690999999999999
    - type: nauc_precision_at_10_diff1
      value: 38.7477
    - type: nauc_precision_at_20_max
      value: 27.0023
    - type: nauc_precision_at_20_std
      value: -0.5613
    - type: nauc_precision_at_20_diff1
      value: 38.874700000000004
    - type: nauc_precision_at_100_max
      value: 26.4945
    - type: nauc_precision_at_100_std
      value: 1.1353
    - type: nauc_precision_at_100_diff1
      value: 35.297200000000004
    - type: nauc_precision_at_1000_max
      value: 31.464100000000002
    - type: nauc_precision_at_1000_std
      value: 5.16
    - type: nauc_precision_at_1000_diff1
      value: 34.5536
    - type: nauc_mrr_at_1_max
      value: 26.464199999999998
    - type: nauc_mrr_at_1_std
      value: -4.6967
    - type: nauc_mrr_at_1_diff1
      value: 50.14189999999999
    - type: nauc_mrr_at_3_max
      value: 27.3495
    - type: nauc_mrr_at_3_std
      value: -4.1872
    - type: nauc_mrr_at_3_diff1
      value: 47.0534
    - type: nauc_mrr_at_5_max
      value: 27.8469
    - type: nauc_mrr_at_5_std
      value: -4.0137
    - type: nauc_mrr_at_5_diff1
      value: 46.8252
    - type: nauc_mrr_at_10_max
      value: 27.660200000000003
    - type: nauc_mrr_at_10_std
      value: -3.7907
    - type: nauc_mrr_at_10_diff1
      value: 46.4094
    - type: nauc_mrr_at_20_max
      value: 27.526699999999998
    - type: nauc_mrr_at_20_std
      value: -3.7532
    - type: nauc_mrr_at_20_diff1
      value: 46.448
    - type: nauc_mrr_at_100_max
      value: 27.5422
    - type: nauc_mrr_at_100_std
      value: -3.7292
    - type: nauc_mrr_at_100_diff1
      value: 46.4261
    - type: nauc_mrr_at_1000_max
      value: 27.544999999999998
    - type: nauc_mrr_at_1000_std
      value: -3.734
    - type: nauc_mrr_at_1000_diff1
      value: 46.435500000000005
    - type: main_score
      value: 42.041000000000004
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
      value: 23.615
    - type: ndcg_at_3
      value: 29.892999999999997
    - type: ndcg_at_5
      value: 31.953
    - type: ndcg_at_10
      value: 33.861000000000004
    - type: ndcg_at_20
      value: 35.402
    - type: ndcg_at_100
      value: 37.891000000000005
    - type: ndcg_at_1000
      value: 40.036
    - type: map_at_1
      value: 23.615
    - type: map_at_3
      value: 28.366999999999997
    - type: map_at_5
      value: 29.511
    - type: map_at_10
      value: 30.304
    - type: map_at_20
      value: 30.732
    - type: map_at_100
      value: 31.062
    - type: map_at_1000
      value: 31.133
    - type: recall_at_1
      value: 23.615
    - type: recall_at_3
      value: 34.302
    - type: recall_at_5
      value: 39.301
    - type: recall_at_10
      value: 45.174
    - type: recall_at_20
      value: 51.231
    - type: recall_at_100
      value: 64.849
    - type: recall_at_1000
      value: 82.307
    - type: precision_at_1
      value: 23.615
    - type: precision_at_3
      value: 11.434
    - type: precision_at_5
      value: 7.86
    - type: precision_at_10
      value: 4.517
    - type: precision_at_20
      value: 2.562
    - type: precision_at_100
      value: 0.6479999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 23.5902
    - type: mrr_at_3
      value: 28.353
    - type: mrr_at_5
      value: 29.4987
    - type: mrr_at_10
      value: 30.292099999999998
    - type: mrr_at_20
      value: 30.72
    - type: mrr_at_100
      value: 31.049599999999998
    - type: mrr_at_1000
      value: 31.120399999999997
    - type: nauc_ndcg_at_1_max
      value: 29.1258
    - type: nauc_ndcg_at_1_std
      value: 1.0401
    - type: nauc_ndcg_at_1_diff1
      value: 47.328199999999995
    - type: nauc_ndcg_at_3_max
      value: 27.8848
    - type: nauc_ndcg_at_3_std
      value: 0.2671
    - type: nauc_ndcg_at_3_diff1
      value: 41.4436
    - type: nauc_ndcg_at_5_max
      value: 27.475300000000004
    - type: nauc_ndcg_at_5_std
      value: -0.1773
    - type: nauc_ndcg_at_5_diff1
      value: 40.184999999999995
    - type: nauc_ndcg_at_10_max
      value: 27.1682
    - type: nauc_ndcg_at_10_std
      value: -0.0666
    - type: nauc_ndcg_at_10_diff1
      value: 39.698
    - type: nauc_ndcg_at_20_max
      value: 26.822699999999998
    - type: nauc_ndcg_at_20_std
      value: 0.3046
    - type: nauc_ndcg_at_20_diff1
      value: 39.0465
    - type: nauc_ndcg_at_100_max
      value: 26.55
    - type: nauc_ndcg_at_100_std
      value: 0.9386
    - type: nauc_ndcg_at_100_diff1
      value: 38.4816
    - type: nauc_ndcg_at_1000_max
      value: 26.8464
    - type: nauc_ndcg_at_1000_std
      value: 1.601
    - type: nauc_ndcg_at_1000_diff1
      value: 38.75
    - type: nauc_map_at_1_max
      value: 29.1258
    - type: nauc_map_at_1_std
      value: 1.0401
    - type: nauc_map_at_1_diff1
      value: 47.328199999999995
    - type: nauc_map_at_3_max
      value: 28.1313
    - type: nauc_map_at_3_std
      value: 0.4596
    - type: nauc_map_at_3_diff1
      value: 42.743199999999995
    - type: nauc_map_at_5_max
      value: 27.91
    - type: nauc_map_at_5_std
      value: 0.1926
    - type: nauc_map_at_5_diff1
      value: 42.0283
    - type: nauc_map_at_10_max
      value: 27.7964
    - type: nauc_map_at_10_std
      value: 0.2326
    - type: nauc_map_at_10_diff1
      value: 41.8324
    - type: nauc_map_at_20_max
      value: 27.6958
    - type: nauc_map_at_20_std
      value: 0.3369
    - type: nauc_map_at_20_diff1
      value: 41.6458
    - type: nauc_map_at_100_max
      value: 27.6475
    - type: nauc_map_at_100_std
      value: 0.4118
    - type: nauc_map_at_100_diff1
      value: 41.5667
    - type: nauc_map_at_1000_max
      value: 27.654899999999998
    - type: nauc_map_at_1000_std
      value: 0.43439999999999995
    - type: nauc_map_at_1000_diff1
      value: 41.578199999999995
    - type: nauc_recall_at_1_max
      value: 29.1258
    - type: nauc_recall_at_1_std
      value: 1.0401
    - type: nauc_recall_at_1_diff1
      value: 47.328199999999995
    - type: nauc_recall_at_3_max
      value: 27.232200000000002
    - type: nauc_recall_at_3_std
      value: -0.25980000000000003
    - type: nauc_recall_at_3_diff1
      value: 37.946200000000005
    - type: nauc_recall_at_5_max
      value: 26.266000000000002
    - type: nauc_recall_at_5_std
      value: -1.2084
    - type: nauc_recall_at_5_diff1
      value: 35.1318
    - type: nauc_recall_at_10_max
      value: 25.2762
    - type: nauc_recall_at_10_std
      value: -0.8635
    - type: nauc_recall_at_10_diff1
      value: 33.6001
    - type: nauc_recall_at_20_max
      value: 23.9389
    - type: nauc_recall_at_20_std
      value: 0.5331
    - type: nauc_recall_at_20_diff1
      value: 30.9907
    - type: nauc_recall_at_100_max
      value: 21.9631
    - type: nauc_recall_at_100_std
      value: 4.6604
    - type: nauc_recall_at_100_diff1
      value: 26.1225
    - type: nauc_recall_at_1000_max
      value: 23.450699999999998
    - type: nauc_recall_at_1000_std
      value: 17.0092
    - type: nauc_recall_at_1000_diff1
      value: 21.3813
    - type: nauc_precision_at_1_max
      value: 29.1258
    - type: nauc_precision_at_1_std
      value: 1.0401
    - type: nauc_precision_at_1_diff1
      value: 47.328199999999995
    - type: nauc_precision_at_3_max
      value: 27.232200000000002
    - type: nauc_precision_at_3_std
      value: -0.25980000000000003
    - type: nauc_precision_at_3_diff1
      value: 37.946200000000005
    - type: nauc_precision_at_5_max
      value: 26.266000000000002
    - type: nauc_precision_at_5_std
      value: -1.2084
    - type: nauc_precision_at_5_diff1
      value: 35.1318
    - type: nauc_precision_at_10_max
      value: 25.2762
    - type: nauc_precision_at_10_std
      value: -0.8635
    - type: nauc_precision_at_10_diff1
      value: 33.6001
    - type: nauc_precision_at_20_max
      value: 23.9389
    - type: nauc_precision_at_20_std
      value: 0.5331
    - type: nauc_precision_at_20_diff1
      value: 30.9907
    - type: nauc_precision_at_100_max
      value: 21.9631
    - type: nauc_precision_at_100_std
      value: 4.6604
    - type: nauc_precision_at_100_diff1
      value: 26.1225
    - type: nauc_precision_at_1000_max
      value: 23.450699999999998
    - type: nauc_precision_at_1000_std
      value: 17.0092
    - type: nauc_precision_at_1000_diff1
      value: 21.3813
    - type: nauc_mrr_at_1_max
      value: 29.1731
    - type: nauc_mrr_at_1_std
      value: 1.0801
    - type: nauc_mrr_at_1_diff1
      value: 47.429
    - type: nauc_mrr_at_3_max
      value: 28.1768
    - type: nauc_mrr_at_3_std
      value: 0.4919
    - type: nauc_mrr_at_3_diff1
      value: 42.830200000000005
    - type: nauc_mrr_at_5_max
      value: 27.9396
    - type: nauc_mrr_at_5_std
      value: 0.2168
    - type: nauc_mrr_at_5_diff1
      value: 42.0956
    - type: nauc_mrr_at_10_max
      value: 27.8301
    - type: nauc_mrr_at_10_std
      value: 0.2567
    - type: nauc_mrr_at_10_diff1
      value: 41.8926
    - type: nauc_mrr_at_20_max
      value: 27.7297
    - type: nauc_mrr_at_20_std
      value: 0.3648
    - type: nauc_mrr_at_20_diff1
      value: 41.7068
    - type: nauc_mrr_at_100_max
      value: 27.6788
    - type: nauc_mrr_at_100_std
      value: 0.43550000000000005
    - type: nauc_mrr_at_100_diff1
      value: 41.626000000000005
    - type: nauc_mrr_at_1000_max
      value: 27.6876
    - type: nauc_mrr_at_1000_std
      value: 0.4594
    - type: nauc_mrr_at_1000_diff1
      value: 41.6377
    - type: main_score
      value: 33.861000000000004
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
      value: 32.99
    - type: ndcg_at_3
      value: 40.416999999999994
    - type: ndcg_at_5
      value: 42.492000000000004
    - type: ndcg_at_10
      value: 44.528
    - type: ndcg_at_20
      value: 46.135999999999996
    - type: ndcg_at_100
      value: 48.33
    - type: ndcg_at_1000
      value: 50.047
    - type: map_at_1
      value: 32.99
    - type: map_at_3
      value: 38.647
    - type: map_at_5
      value: 39.789
    - type: map_at_10
      value: 40.62
    - type: map_at_20
      value: 41.062
    - type: map_at_100
      value: 41.366
    - type: map_at_1000
      value: 41.422
    - type: recall_at_1
      value: 32.99
    - type: recall_at_3
      value: 45.519
    - type: recall_at_5
      value: 50.595
    - type: recall_at_10
      value: 56.93899999999999
    - type: recall_at_20
      value: 63.283
    - type: recall_at_100
      value: 75.099
    - type: recall_at_1000
      value: 89.13600000000001
    - type: precision_at_1
      value: 32.99
    - type: precision_at_3
      value: 15.173
    - type: precision_at_5
      value: 10.119
    - type: precision_at_10
      value: 5.694
    - type: precision_at_20
      value: 3.164
    - type: precision_at_100
      value: 0.751
    - type: precision_at_1000
      value: 0.089
    - type: mrr_at_1
      value: 33.068999999999996
    - type: mrr_at_3
      value: 38.6862
    - type: mrr_at_5
      value: 39.8282
    - type: mrr_at_10
      value: 40.6593
    - type: mrr_at_20
      value: 41.1016
    - type: mrr_at_100
      value: 41.4058
    - type: mrr_at_1000
      value: 41.4614
    - type: nauc_ndcg_at_1_max
      value: 34.985699999999994
    - type: nauc_ndcg_at_1_std
      value: -7.5317
    - type: nauc_ndcg_at_1_diff1
      value: 55.82899999999999
    - type: nauc_ndcg_at_3_max
      value: 34.3163
    - type: nauc_ndcg_at_3_std
      value: -7.0863
    - type: nauc_ndcg_at_3_diff1
      value: 50.0509
    - type: nauc_ndcg_at_5_max
      value: 33.7316
    - type: nauc_ndcg_at_5_std
      value: -7.3946
    - type: nauc_ndcg_at_5_diff1
      value: 48.7525
    - type: nauc_ndcg_at_10_max
      value: 34.6192
    - type: nauc_ndcg_at_10_std
      value: -6.7839
    - type: nauc_ndcg_at_10_diff1
      value: 48.6166
    - type: nauc_ndcg_at_20_max
      value: 34.334399999999995
    - type: nauc_ndcg_at_20_std
      value: -7.0675
    - type: nauc_ndcg_at_20_diff1
      value: 48.0635
    - type: nauc_ndcg_at_100_max
      value: 34.6406
    - type: nauc_ndcg_at_100_std
      value: -6.8653
    - type: nauc_ndcg_at_100_diff1
      value: 48.617
    - type: nauc_ndcg_at_1000_max
      value: 34.2365
    - type: nauc_ndcg_at_1000_std
      value: -7.0976
    - type: nauc_ndcg_at_1000_diff1
      value: 48.464200000000005
    - type: nauc_map_at_1_max
      value: 34.985699999999994
    - type: nauc_map_at_1_std
      value: -7.5317
    - type: nauc_map_at_1_diff1
      value: 55.82899999999999
    - type: nauc_map_at_3_max
      value: 34.577000000000005
    - type: nauc_map_at_3_std
      value: -7.1427000000000005
    - type: nauc_map_at_3_diff1
      value: 51.4256
    - type: nauc_map_at_5_max
      value: 34.2296
    - type: nauc_map_at_5_std
      value: -7.322299999999999
    - type: nauc_map_at_5_diff1
      value: 50.709700000000005
    - type: nauc_map_at_10_max
      value: 34.633900000000004
    - type: nauc_map_at_10_std
      value: -7.056900000000001
    - type: nauc_map_at_10_diff1
      value: 50.714099999999995
    - type: nauc_map_at_20_max
      value: 34.5386
    - type: nauc_map_at_20_std
      value: -7.142900000000001
    - type: nauc_map_at_20_diff1
      value: 50.568900000000006
    - type: nauc_map_at_100_max
      value: 34.5697
    - type: nauc_map_at_100_std
      value: -7.1189
    - type: nauc_map_at_100_diff1
      value: 50.6351
    - type: nauc_map_at_1000_max
      value: 34.558499999999995
    - type: nauc_map_at_1000_std
      value: -7.1173
    - type: nauc_map_at_1000_diff1
      value: 50.6277
    - type: nauc_recall_at_1_max
      value: 34.985699999999994
    - type: nauc_recall_at_1_std
      value: -7.5317
    - type: nauc_recall_at_1_diff1
      value: 55.82899999999999
    - type: nauc_recall_at_3_max
      value: 33.5265
    - type: nauc_recall_at_3_std
      value: -6.9448
    - type: nauc_recall_at_3_diff1
      value: 46.1063
    - type: nauc_recall_at_5_max
      value: 32.1817
    - type: nauc_recall_at_5_std
      value: -7.6609
    - type: nauc_recall_at_5_diff1
      value: 42.8551
    - type: nauc_recall_at_10_max
      value: 34.7502
    - type: nauc_recall_at_10_std
      value: -5.7719
    - type: nauc_recall_at_10_diff1
      value: 41.7549
    - type: nauc_recall_at_20_max
      value: 33.6546
    - type: nauc_recall_at_20_std
      value: -6.862500000000001
    - type: nauc_recall_at_20_diff1
      value: 38.6947
    - type: nauc_recall_at_100_max
      value: 36.095699999999994
    - type: nauc_recall_at_100_std
      value: -5.2094000000000005
    - type: nauc_recall_at_100_diff1
      value: 40.336800000000004
    - type: nauc_recall_at_1000_max
      value: 27.8549
    - type: nauc_recall_at_1000_std
      value: -10.570699999999999
    - type: nauc_recall_at_1000_diff1
      value: 28.6812
    - type: nauc_precision_at_1_max
      value: 34.985699999999994
    - type: nauc_precision_at_1_std
      value: -7.5317
    - type: nauc_precision_at_1_diff1
      value: 55.82899999999999
    - type: nauc_precision_at_3_max
      value: 33.5265
    - type: nauc_precision_at_3_std
      value: -6.9448
    - type: nauc_precision_at_3_diff1
      value: 46.1063
    - type: nauc_precision_at_5_max
      value: 32.1817
    - type: nauc_precision_at_5_std
      value: -7.6609
    - type: nauc_precision_at_5_diff1
      value: 42.8551
    - type: nauc_precision_at_10_max
      value: 34.7502
    - type: nauc_precision_at_10_std
      value: -5.7719
    - type: nauc_precision_at_10_diff1
      value: 41.7549
    - type: nauc_precision_at_20_max
      value: 33.6546
    - type: nauc_precision_at_20_std
      value: -6.862500000000001
    - type: nauc_precision_at_20_diff1
      value: 38.6947
    - type: nauc_precision_at_100_max
      value: 36.095699999999994
    - type: nauc_precision_at_100_std
      value: -5.2094000000000005
    - type: nauc_precision_at_100_diff1
      value: 40.336800000000004
    - type: nauc_precision_at_1000_max
      value: 27.8549
    - type: nauc_precision_at_1000_std
      value: -10.570699999999999
    - type: nauc_precision_at_1000_diff1
      value: 28.6812
    - type: nauc_mrr_at_1_max
      value: 35.099599999999995
    - type: nauc_mrr_at_1_std
      value: -7.268199999999999
    - type: nauc_mrr_at_1_diff1
      value: 55.5813
    - type: nauc_mrr_at_3_max
      value: 34.6335
    - type: nauc_mrr_at_3_std
      value: -7.012300000000001
    - type: nauc_mrr_at_3_diff1
      value: 51.3038
    - type: nauc_mrr_at_5_max
      value: 34.2864
    - type: nauc_mrr_at_5_std
      value: -7.1912
    - type: nauc_mrr_at_5_diff1
      value: 50.5873
    - type: nauc_mrr_at_10_max
      value: 34.6912
    - type: nauc_mrr_at_10_std
      value: -6.9247000000000005
    - type: nauc_mrr_at_10_diff1
      value: 50.5908
    - type: nauc_mrr_at_20_max
      value: 34.596199999999996
    - type: nauc_mrr_at_20_std
      value: -7.01
    - type: nauc_mrr_at_20_diff1
      value: 50.4448
    - type: nauc_mrr_at_100_max
      value: 34.6274
    - type: nauc_mrr_at_100_std
      value: -6.984999999999999
    - type: nauc_mrr_at_100_diff1
      value: 50.510200000000005
    - type: nauc_mrr_at_1000_max
      value: 34.6163
    - type: nauc_mrr_at_1000_std
      value: -6.9832
    - type: nauc_mrr_at_1000_diff1
      value: 50.5026
    - type: main_score
      value: 44.528
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
      value: 26.407999999999998
    - type: ndcg_at_3
      value: 33.356
    - type: ndcg_at_5
      value: 35.143
    - type: ndcg_at_10
      value: 37.008
    - type: ndcg_at_20
      value: 38.394
    - type: ndcg_at_100
      value: 40.726
    - type: ndcg_at_1000
      value: 42.648
    - type: map_at_1
      value: 26.407999999999998
    - type: map_at_3
      value: 31.663000000000004
    - type: map_at_5
      value: 32.651
    - type: map_at_10
      value: 33.424
    - type: map_at_20
      value: 33.808
    - type: map_at_100
      value: 34.121
    - type: map_at_1000
      value: 34.184
    - type: recall_at_1
      value: 26.407999999999998
    - type: recall_at_3
      value: 38.247
    - type: recall_at_5
      value: 42.602000000000004
    - type: recall_at_10
      value: 48.352000000000004
    - type: recall_at_20
      value: 53.811
    - type: recall_at_100
      value: 66.508
    - type: recall_at_1000
      value: 82.173
    - type: precision_at_1
      value: 26.407999999999998
    - type: precision_at_3
      value: 12.748999999999999
    - type: precision_at_5
      value: 8.52
    - type: precision_at_10
      value: 4.835
    - type: precision_at_20
      value: 2.691
    - type: precision_at_100
      value: 0.6649999999999999
    - type: precision_at_1000
      value: 0.082
    - type: mrr_at_1
      value: 26.4263
    - type: mrr_at_3
      value: 31.673499999999997
    - type: mrr_at_5
      value: 32.6607
    - type: mrr_at_10
      value: 33.4314
    - type: mrr_at_20
      value: 33.8153
    - type: mrr_at_100
      value: 34.1293
    - type: mrr_at_1000
      value: 34.192499999999995
    - type: nauc_ndcg_at_1_max
      value: 29.026600000000002
    - type: nauc_ndcg_at_1_std
      value: -5.3401
    - type: nauc_ndcg_at_1_diff1
      value: 51.7505
    - type: nauc_ndcg_at_3_max
      value: 30.0657
    - type: nauc_ndcg_at_3_std
      value: -4.2413
    - type: nauc_ndcg_at_3_diff1
      value: 46.476600000000005
    - type: nauc_ndcg_at_5_max
      value: 29.7155
    - type: nauc_ndcg_at_5_std
      value: -3.8619
    - type: nauc_ndcg_at_5_diff1
      value: 45.5131
    - type: nauc_ndcg_at_10_max
      value: 29.4459
    - type: nauc_ndcg_at_10_std
      value: -3.3680000000000003
    - type: nauc_ndcg_at_10_diff1
      value: 44.6258
    - type: nauc_ndcg_at_20_max
      value: 29.135499999999997
    - type: nauc_ndcg_at_20_std
      value: -3.0517
    - type: nauc_ndcg_at_20_diff1
      value: 44.1
    - type: nauc_ndcg_at_100_max
      value: 29.131400000000003
    - type: nauc_ndcg_at_100_std
      value: -2.03
    - type: nauc_ndcg_at_100_diff1
      value: 43.7972
    - type: nauc_ndcg_at_1000_max
      value: 29.285099999999996
    - type: nauc_ndcg_at_1000_std
      value: -1.9141
    - type: nauc_ndcg_at_1000_diff1
      value: 44.1738
    - type: nauc_map_at_1_max
      value: 29.026600000000002
    - type: nauc_map_at_1_std
      value: -5.3401
    - type: nauc_map_at_1_diff1
      value: 51.7505
    - type: nauc_map_at_3_max
      value: 29.8237
    - type: nauc_map_at_3_std
      value: -4.5517
    - type: nauc_map_at_3_diff1
      value: 47.6757
    - type: nauc_map_at_5_max
      value: 29.624200000000002
    - type: nauc_map_at_5_std
      value: -4.338100000000001
    - type: nauc_map_at_5_diff1
      value: 47.1309
    - type: nauc_map_at_10_max
      value: 29.5078
    - type: nauc_map_at_10_std
      value: -4.1374
    - type: nauc_map_at_10_diff1
      value: 46.7589
    - type: nauc_map_at_20_max
      value: 29.421000000000003
    - type: nauc_map_at_20_std
      value: -4.0543000000000005
    - type: nauc_map_at_20_diff1
      value: 46.6131
    - type: nauc_map_at_100_max
      value: 29.411199999999997
    - type: nauc_map_at_100_std
      value: -3.9336
    - type: nauc_map_at_100_diff1
      value: 46.578199999999995
    - type: nauc_map_at_1000_max
      value: 29.4134
    - type: nauc_map_at_1000_std
      value: -3.9301000000000004
    - type: nauc_map_at_1000_diff1
      value: 46.5892
    - type: nauc_recall_at_1_max
      value: 29.026600000000002
    - type: nauc_recall_at_1_std
      value: -5.3401
    - type: nauc_recall_at_1_diff1
      value: 51.7505
    - type: nauc_recall_at_3_max
      value: 30.7299
    - type: nauc_recall_at_3_std
      value: -3.3682999999999996
    - type: nauc_recall_at_3_diff1
      value: 43.1978
    - type: nauc_recall_at_5_max
      value: 29.9215
    - type: nauc_recall_at_5_std
      value: -2.4814
    - type: nauc_recall_at_5_diff1
      value: 40.9532
    - type: nauc_recall_at_10_max
      value: 29.1323
    - type: nauc_recall_at_10_std
      value: -0.9436999999999999
    - type: nauc_recall_at_10_diff1
      value: 38.221199999999996
    - type: nauc_recall_at_20_max
      value: 27.889999999999997
    - type: nauc_recall_at_20_std
      value: 0.4464
    - type: nauc_recall_at_20_diff1
      value: 35.8795
    - type: nauc_recall_at_100_max
      value: 27.8094
    - type: nauc_recall_at_100_std
      value: 7.914499999999999
    - type: nauc_recall_at_100_diff1
      value: 32.3117
    - type: nauc_recall_at_1000_max
      value: 29.6608
    - type: nauc_recall_at_1000_std
      value: 15.9532
    - type: nauc_recall_at_1000_diff1
      value: 31.069799999999997
    - type: nauc_precision_at_1_max
      value: 29.026600000000002
    - type: nauc_precision_at_1_std
      value: -5.3401
    - type: nauc_precision_at_1_diff1
      value: 51.7505
    - type: nauc_precision_at_3_max
      value: 30.7299
    - type: nauc_precision_at_3_std
      value: -3.3682999999999996
    - type: nauc_precision_at_3_diff1
      value: 43.1978
    - type: nauc_precision_at_5_max
      value: 29.9215
    - type: nauc_precision_at_5_std
      value: -2.4814
    - type: nauc_precision_at_5_diff1
      value: 40.9532
    - type: nauc_precision_at_10_max
      value: 29.1323
    - type: nauc_precision_at_10_std
      value: -0.9436999999999999
    - type: nauc_precision_at_10_diff1
      value: 38.221199999999996
    - type: nauc_precision_at_20_max
      value: 27.889999999999997
    - type: nauc_precision_at_20_std
      value: 0.4464
    - type: nauc_precision_at_20_diff1
      value: 35.8795
    - type: nauc_precision_at_100_max
      value: 27.8094
    - type: nauc_precision_at_100_std
      value: 7.914499999999999
    - type: nauc_precision_at_100_diff1
      value: 32.3117
    - type: nauc_precision_at_1000_max
      value: 29.6608
    - type: nauc_precision_at_1000_std
      value: 15.9532
    - type: nauc_precision_at_1000_diff1
      value: 31.069799999999997
    - type: nauc_mrr_at_1_max
      value: 29.0947
    - type: nauc_mrr_at_1_std
      value: -5.2643
    - type: nauc_mrr_at_1_diff1
      value: 51.678000000000004
    - type: nauc_mrr_at_3_max
      value: 29.8523
    - type: nauc_mrr_at_3_std
      value: -4.5234000000000005
    - type: nauc_mrr_at_3_diff1
      value: 47.653099999999995
    - type: nauc_mrr_at_5_max
      value: 29.648799999999998
    - type: nauc_mrr_at_5_std
      value: -4.3013
    - type: nauc_mrr_at_5_diff1
      value: 47.105799999999995
    - type: nauc_mrr_at_10_max
      value: 29.5336
    - type: nauc_mrr_at_10_std
      value: -4.1075
    - type: nauc_mrr_at_10_diff1
      value: 46.733799999999995
    - type: nauc_mrr_at_20_max
      value: 29.451500000000003
    - type: nauc_mrr_at_20_std
      value: -4.0183
    - type: nauc_mrr_at_20_diff1
      value: 46.5858
    - type: nauc_mrr_at_100_max
      value: 29.440699999999996
    - type: nauc_mrr_at_100_std
      value: -3.8987000000000003
    - type: nauc_mrr_at_100_diff1
      value: 46.5526
    - type: nauc_mrr_at_1000_max
      value: 29.442899999999998
    - type: nauc_mrr_at_1000_std
      value: -3.8952
    - type: nauc_mrr_at_1000_diff1
      value: 46.563500000000005
    - type: main_score
      value: 37.008
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
      value: 21.022
    - type: ndcg_at_3
      value: 27.082
    - type: ndcg_at_5
      value: 28.956
    - type: ndcg_at_10
      value: 30.791
    - type: ndcg_at_20
      value: 32.301
    - type: ndcg_at_100
      value: 34.794000000000004
    - type: ndcg_at_1000
      value: 37.082
    - type: map_at_1
      value: 21.022
    - type: map_at_3
      value: 25.593
    - type: map_at_5
      value: 26.634999999999998
    - type: map_at_10
      value: 27.395000000000003
    - type: map_at_20
      value: 27.811000000000003
    - type: map_at_100
      value: 28.143
    - type: map_at_1000
      value: 28.218
    - type: recall_at_1
      value: 21.022
    - type: recall_at_3
      value: 31.39
    - type: recall_at_5
      value: 35.935
    - type: recall_at_10
      value: 41.593999999999994
    - type: recall_at_20
      value: 47.552
    - type: recall_at_100
      value: 61.18900000000001
    - type: recall_at_1000
      value: 79.827
    - type: precision_at_1
      value: 21.022
    - type: precision_at_3
      value: 10.463000000000001
    - type: precision_at_5
      value: 7.187
    - type: precision_at_10
      value: 4.159
    - type: precision_at_20
      value: 2.378
    - type: precision_at_100
      value: 0.612
    - type: precision_at_1000
      value: 0.08
    - type: mrr_at_1
      value: 21.0218
    - type: mrr_at_3
      value: 25.588699999999996
    - type: mrr_at_5
      value: 26.631899999999998
    - type: mrr_at_10
      value: 27.3915
    - type: mrr_at_20
      value: 27.807900000000004
    - type: mrr_at_100
      value: 28.138800000000003
    - type: mrr_at_1000
      value: 28.2141
    - type: nauc_ndcg_at_1_max
      value: 22.1861
    - type: nauc_ndcg_at_1_std
      value: -3.218
    - type: nauc_ndcg_at_1_diff1
      value: 46.4989
    - type: nauc_ndcg_at_3_max
      value: 21.7282
    - type: nauc_ndcg_at_3_std
      value: -2.1185
    - type: nauc_ndcg_at_3_diff1
      value: 40.8096
    - type: nauc_ndcg_at_5_max
      value: 21.339199999999998
    - type: nauc_ndcg_at_5_std
      value: -1.6541000000000001
    - type: nauc_ndcg_at_5_diff1
      value: 39.6483
    - type: nauc_ndcg_at_10_max
      value: 20.9441
    - type: nauc_ndcg_at_10_std
      value: -0.8141
    - type: nauc_ndcg_at_10_diff1
      value: 38.5517
    - type: nauc_ndcg_at_20_max
      value: 20.7702
    - type: nauc_ndcg_at_20_std
      value: -0.293
    - type: nauc_ndcg_at_20_diff1
      value: 38.2386
    - type: nauc_ndcg_at_100_max
      value: 20.569100000000002
    - type: nauc_ndcg_at_100_std
      value: 0.8404
    - type: nauc_ndcg_at_100_diff1
      value: 37.6899
    - type: nauc_ndcg_at_1000_max
      value: 20.72
    - type: nauc_ndcg_at_1000_std
      value: 0.9279000000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 37.9486
    - type: nauc_map_at_1_max
      value: 22.1861
    - type: nauc_map_at_1_std
      value: -3.218
    - type: nauc_map_at_1_diff1
      value: 46.4989
    - type: nauc_map_at_3_max
      value: 21.86
    - type: nauc_map_at_3_std
      value: -2.4015999999999997
    - type: nauc_map_at_3_diff1
      value: 42.0695
    - type: nauc_map_at_5_max
      value: 21.6404
    - type: nauc_map_at_5_std
      value: -2.1305
    - type: nauc_map_at_5_diff1
      value: 41.3954
    - type: nauc_map_at_10_max
      value: 21.4897
    - type: nauc_map_at_10_std
      value: -1.76
    - type: nauc_map_at_10_diff1
      value: 40.9264
    - type: nauc_map_at_20_max
      value: 21.4368
    - type: nauc_map_at_20_std
      value: -1.6178000000000001
    - type: nauc_map_at_20_diff1
      value: 40.847
    - type: nauc_map_at_100_max
      value: 21.3978
    - type: nauc_map_at_100_std
      value: -1.4705
    - type: nauc_map_at_100_diff1
      value: 40.775
    - type: nauc_map_at_1000_max
      value: 21.4068
    - type: nauc_map_at_1000_std
      value: -1.4657
    - type: nauc_map_at_1000_diff1
      value: 40.7824
    - type: nauc_recall_at_1_max
      value: 22.1861
    - type: nauc_recall_at_1_std
      value: -3.218
    - type: nauc_recall_at_1_diff1
      value: 46.4989
    - type: nauc_recall_at_3_max
      value: 21.3684
    - type: nauc_recall_at_3_std
      value: -1.3554
    - type: nauc_recall_at_3_diff1
      value: 37.4804
    - type: nauc_recall_at_5_max
      value: 20.4902
    - type: nauc_recall_at_5_std
      value: -0.3449
    - type: nauc_recall_at_5_diff1
      value: 34.9587
    - type: nauc_recall_at_10_max
      value: 19.2959
    - type: nauc_recall_at_10_std
      value: 1.9666
    - type: nauc_recall_at_10_diff1
      value: 31.903
    - type: nauc_recall_at_20_max
      value: 18.6516
    - type: nauc_recall_at_20_std
      value: 3.9671
    - type: nauc_recall_at_20_diff1
      value: 30.576999999999998
    - type: nauc_recall_at_100_max
      value: 17.383699999999997
    - type: nauc_recall_at_100_std
      value: 11.050699999999999
    - type: nauc_recall_at_100_diff1
      value: 26.4222
    - type: nauc_recall_at_1000_max
      value: 17.1265
    - type: nauc_recall_at_1000_std
      value: 18.235699999999998
    - type: nauc_recall_at_1000_diff1
      value: 23.186300000000003
    - type: nauc_precision_at_1_max
      value: 22.1861
    - type: nauc_precision_at_1_std
      value: -3.218
    - type: nauc_precision_at_1_diff1
      value: 46.4989
    - type: nauc_precision_at_3_max
      value: 21.3684
    - type: nauc_precision_at_3_std
      value: -1.3554
    - type: nauc_precision_at_3_diff1
      value: 37.4804
    - type: nauc_precision_at_5_max
      value: 20.4902
    - type: nauc_precision_at_5_std
      value: -0.3449
    - type: nauc_precision_at_5_diff1
      value: 34.9587
    - type: nauc_precision_at_10_max
      value: 19.2959
    - type: nauc_precision_at_10_std
      value: 1.9666
    - type: nauc_precision_at_10_diff1
      value: 31.903
    - type: nauc_precision_at_20_max
      value: 18.6516
    - type: nauc_precision_at_20_std
      value: 3.9671
    - type: nauc_precision_at_20_diff1
      value: 30.576999999999998
    - type: nauc_precision_at_100_max
      value: 17.383699999999997
    - type: nauc_precision_at_100_std
      value: 11.050699999999999
    - type: nauc_precision_at_100_diff1
      value: 26.4222
    - type: nauc_precision_at_1000_max
      value: 17.1265
    - type: nauc_precision_at_1000_std
      value: 18.235699999999998
    - type: nauc_precision_at_1000_diff1
      value: 23.186300000000003
    - type: nauc_mrr_at_1_max
      value: 22.159000000000002
    - type: nauc_mrr_at_1_std
      value: -3.2346
    - type: nauc_mrr_at_1_diff1
      value: 46.4989
    - type: nauc_mrr_at_3_max
      value: 21.8304
    - type: nauc_mrr_at_3_std
      value: -2.4013
    - type: nauc_mrr_at_3_diff1
      value: 42.0356
    - type: nauc_mrr_at_5_max
      value: 21.617900000000002
    - type: nauc_mrr_at_5_std
      value: -2.1397
    - type: nauc_mrr_at_5_diff1
      value: 41.3793
    - type: nauc_mrr_at_10_max
      value: 21.467200000000002
    - type: nauc_mrr_at_10_std
      value: -1.7682
    - type: nauc_mrr_at_10_diff1
      value: 40.912
    - type: nauc_mrr_at_20_max
      value: 21.415200000000002
    - type: nauc_mrr_at_20_std
      value: -1.6295
    - type: nauc_mrr_at_20_diff1
      value: 40.8319
    - type: nauc_mrr_at_100_max
      value: 21.376800000000003
    - type: nauc_mrr_at_100_std
      value: -1.4815
    - type: nauc_mrr_at_100_diff1
      value: 40.760400000000004
    - type: nauc_mrr_at_1000_max
      value: 21.3858
    - type: nauc_mrr_at_1000_std
      value: -1.4767000000000001
    - type: nauc_mrr_at_1000_diff1
      value: 40.7677
    - type: main_score
      value: 30.791
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
      value: 65.2
    - type: ndcg_at_3
      value: 76.41
    - type: ndcg_at_5
      value: 77.981
    - type: ndcg_at_10
      value: 79.044
    - type: ndcg_at_20
      value: 79.855
    - type: ndcg_at_100
      value: 80.622
    - type: ndcg_at_1000
      value: 80.806
    - type: map_at_1
      value: 65.2
    - type: map_at_3
      value: 73.65
    - type: map_at_5
      value: 74.52499999999999
    - type: map_at_10
      value: 74.98
    - type: map_at_20
      value: 75.203
    - type: map_at_100
      value: 75.319
    - type: map_at_1000
      value: 75.327
    - type: recall_at_1
      value: 65.2
    - type: recall_at_3
      value: 84.39999999999999
    - type: recall_at_5
      value: 88.2
    - type: recall_at_10
      value: 91.4
    - type: recall_at_20
      value: 94.6
    - type: recall_at_100
      value: 98.6
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 65.2
    - type: precision_at_3
      value: 28.133000000000003
    - type: precision_at_5
      value: 17.64
    - type: precision_at_10
      value: 9.139999999999999
    - type: precision_at_20
      value: 4.73
    - type: precision_at_100
      value: 0.9860000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 65.2
    - type: mrr_at_3
      value: 73.65
    - type: mrr_at_5
      value: 74.52499999999999
    - type: mrr_at_10
      value: 74.9802
    - type: mrr_at_20
      value: 75.20320000000001
    - type: mrr_at_100
      value: 75.319
    - type: mrr_at_1000
      value: 75.3269
    - type: nauc_ndcg_at_1_max
      value: 36.4698
    - type: nauc_ndcg_at_1_std
      value: -10.8058
    - type: nauc_ndcg_at_1_diff1
      value: 70.5679
    - type: nauc_ndcg_at_3_max
      value: 40.582499999999996
    - type: nauc_ndcg_at_3_std
      value: -9.3767
    - type: nauc_ndcg_at_3_diff1
      value: 64.8235
    - type: nauc_ndcg_at_5_max
      value: 41.191100000000006
    - type: nauc_ndcg_at_5_std
      value: -8.6758
    - type: nauc_ndcg_at_5_diff1
      value: 64.70179999999999
    - type: nauc_ndcg_at_10_max
      value: 41.5913
    - type: nauc_ndcg_at_10_std
      value: -8.8502
    - type: nauc_ndcg_at_10_diff1
      value: 65.7197
    - type: nauc_ndcg_at_20_max
      value: 41.4419
    - type: nauc_ndcg_at_20_std
      value: -9.0406
    - type: nauc_ndcg_at_20_diff1
      value: 66.1819
    - type: nauc_ndcg_at_100_max
      value: 40.6791
    - type: nauc_ndcg_at_100_std
      value: -8.343499999999999
    - type: nauc_ndcg_at_100_diff1
      value: 66.468
    - type: nauc_ndcg_at_1000_max
      value: 40.3153
    - type: nauc_ndcg_at_1000_std
      value: -8.7689
    - type: nauc_ndcg_at_1000_diff1
      value: 66.49249999999999
    - type: nauc_map_at_1_max
      value: 36.4698
    - type: nauc_map_at_1_std
      value: -10.8058
    - type: nauc_map_at_1_diff1
      value: 70.5679
    - type: nauc_map_at_3_max
      value: 39.3299
    - type: nauc_map_at_3_std
      value: -9.4675
    - type: nauc_map_at_3_diff1
      value: 66.3583
    - type: nauc_map_at_5_max
      value: 39.5636
    - type: nauc_map_at_5_std
      value: -9.1881
    - type: nauc_map_at_5_diff1
      value: 66.37910000000001
    - type: nauc_map_at_10_max
      value: 39.6806
    - type: nauc_map_at_10_std
      value: -9.3088
    - type: nauc_map_at_10_diff1
      value: 66.8131
    - type: nauc_map_at_20_max
      value: 39.635999999999996
    - type: nauc_map_at_20_std
      value: -9.3305
    - type: nauc_map_at_20_diff1
      value: 66.93430000000001
    - type: nauc_map_at_100_max
      value: 39.536500000000004
    - type: nauc_map_at_100_std
      value: -9.1873
    - type: nauc_map_at_100_diff1
      value: 66.96419999999999
    - type: nauc_map_at_1000_max
      value: 39.5233
    - type: nauc_map_at_1000_std
      value: -9.200999999999999
    - type: nauc_map_at_1000_diff1
      value: 66.9634
    - type: nauc_recall_at_1_max
      value: 36.4698
    - type: nauc_recall_at_1_std
      value: -10.8058
    - type: nauc_recall_at_1_diff1
      value: 70.5679
    - type: nauc_recall_at_3_max
      value: 46.0932
    - type: nauc_recall_at_3_std
      value: -9.193900000000001
    - type: nauc_recall_at_3_diff1
      value: 58.2067
    - type: nauc_recall_at_5_max
      value: 50.2927
    - type: nauc_recall_at_5_std
      value: -5.8297
    - type: nauc_recall_at_5_diff1
      value: 55.6113
    - type: nauc_recall_at_10_max
      value: 55.961099999999995
    - type: nauc_recall_at_10_std
      value: -5.3568999999999996
    - type: nauc_recall_at_10_diff1
      value: 58.6075
    - type: nauc_recall_at_20_max
      value: 62.2869
    - type: nauc_recall_at_20_std
      value: -6.4927
    - type: nauc_recall_at_20_diff1
      value: 60.207699999999996
    - type: nauc_recall_at_100_max
      value: 73.4427
    - type: nauc_recall_at_100_std
      value: 31.606
    - type: nauc_recall_at_100_diff1
      value: 63.0919
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 36.4698
    - type: nauc_precision_at_1_std
      value: -10.8058
    - type: nauc_precision_at_1_diff1
      value: 70.5679
    - type: nauc_precision_at_3_max
      value: 46.0932
    - type: nauc_precision_at_3_std
      value: -9.193900000000001
    - type: nauc_precision_at_3_diff1
      value: 58.2067
    - type: nauc_precision_at_5_max
      value: 50.2927
    - type: nauc_precision_at_5_std
      value: -5.8297
    - type: nauc_precision_at_5_diff1
      value: 55.6113
    - type: nauc_precision_at_10_max
      value: 55.961099999999995
    - type: nauc_precision_at_10_std
      value: -5.3568999999999996
    - type: nauc_precision_at_10_diff1
      value: 58.6075
    - type: nauc_precision_at_20_max
      value: 62.2869
    - type: nauc_precision_at_20_std
      value: -6.4927
    - type: nauc_precision_at_20_diff1
      value: 60.207699999999996
    - type: nauc_precision_at_100_max
      value: 73.4427
    - type: nauc_precision_at_100_std
      value: 31.606
    - type: nauc_precision_at_100_diff1
      value: 63.0919
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 36.4698
    - type: nauc_mrr_at_1_std
      value: -10.8058
    - type: nauc_mrr_at_1_diff1
      value: 70.5679
    - type: nauc_mrr_at_3_max
      value: 39.3299
    - type: nauc_mrr_at_3_std
      value: -9.4675
    - type: nauc_mrr_at_3_diff1
      value: 66.3583
    - type: nauc_mrr_at_5_max
      value: 39.5636
    - type: nauc_mrr_at_5_std
      value: -9.1881
    - type: nauc_mrr_at_5_diff1
      value: 66.37910000000001
    - type: nauc_mrr_at_10_max
      value: 39.6806
    - type: nauc_mrr_at_10_std
      value: -9.3088
    - type: nauc_mrr_at_10_diff1
      value: 66.8131
    - type: nauc_mrr_at_20_max
      value: 39.635999999999996
    - type: nauc_mrr_at_20_std
      value: -9.3305
    - type: nauc_mrr_at_20_diff1
      value: 66.93430000000001
    - type: nauc_mrr_at_100_max
      value: 39.536500000000004
    - type: nauc_mrr_at_100_std
      value: -9.1873
    - type: nauc_mrr_at_100_diff1
      value: 66.96419999999999
    - type: nauc_mrr_at_1000_max
      value: 39.5233
    - type: nauc_mrr_at_1000_std
      value: -9.200999999999999
    - type: nauc_mrr_at_1000_diff1
      value: 66.9634
    - type: main_score
      value: 79.044
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
      value: 55.2
    - type: ndcg_at_3
      value: 63.709
    - type: ndcg_at_5
      value: 65.267
    - type: ndcg_at_10
      value: 67.239
    - type: ndcg_at_20
      value: 68.372
    - type: ndcg_at_100
      value: 69.854
    - type: ndcg_at_1000
      value: 70.831
    - type: map_at_1
      value: 55.2
    - type: map_at_3
      value: 61.667
    - type: map_at_5
      value: 62.527
    - type: map_at_10
      value: 63.339999999999996
    - type: map_at_20
      value: 63.648
    - type: map_at_100
      value: 63.854
    - type: map_at_1000
      value: 63.885999999999996
    - type: recall_at_1
      value: 55.2
    - type: recall_at_3
      value: 69.6
    - type: recall_at_5
      value: 73.4
    - type: recall_at_10
      value: 79.5
    - type: recall_at_20
      value: 84.0
    - type: recall_at_100
      value: 92.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 55.2
    - type: precision_at_3
      value: 23.200000000000003
    - type: precision_at_5
      value: 14.680000000000001
    - type: precision_at_10
      value: 7.95
    - type: precision_at_20
      value: 4.2
    - type: precision_at_100
      value: 0.9199999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 55.2
    - type: mrr_at_3
      value: 61.6667
    - type: mrr_at_5
      value: 62.526700000000005
    - type: mrr_at_10
      value: 63.339999999999996
    - type: mrr_at_20
      value: 63.6484
    - type: mrr_at_100
      value: 63.854200000000006
    - type: mrr_at_1000
      value: 63.88549999999999
    - type: nauc_ndcg_at_1_max
      value: 48.821
    - type: nauc_ndcg_at_1_std
      value: 19.6886
    - type: nauc_ndcg_at_1_diff1
      value: 65.515
    - type: nauc_ndcg_at_3_max
      value: 56.316
    - type: nauc_ndcg_at_3_std
      value: 26.6555
    - type: nauc_ndcg_at_3_diff1
      value: 61.755300000000005
    - type: nauc_ndcg_at_5_max
      value: 57.566300000000005
    - type: nauc_ndcg_at_5_std
      value: 29.5288
    - type: nauc_ndcg_at_5_diff1
      value: 61.655300000000004
    - type: nauc_ndcg_at_10_max
      value: 58.89339999999999
    - type: nauc_ndcg_at_10_std
      value: 32.1136
    - type: nauc_ndcg_at_10_diff1
      value: 61.7916
    - type: nauc_ndcg_at_20_max
      value: 58.675999999999995
    - type: nauc_ndcg_at_20_std
      value: 32.2575
    - type: nauc_ndcg_at_20_diff1
      value: 62.5682
    - type: nauc_ndcg_at_100_max
      value: 57.6832
    - type: nauc_ndcg_at_100_std
      value: 31.2476
    - type: nauc_ndcg_at_100_diff1
      value: 62.356100000000005
    - type: nauc_ndcg_at_1000_max
      value: 56.9118
    - type: nauc_ndcg_at_1000_std
      value: 29.624499999999998
    - type: nauc_ndcg_at_1000_diff1
      value: 62.4914
    - type: nauc_map_at_1_max
      value: 48.821
    - type: nauc_map_at_1_std
      value: 19.6886
    - type: nauc_map_at_1_diff1
      value: 65.515
    - type: nauc_map_at_3_max
      value: 54.47260000000001
    - type: nauc_map_at_3_std
      value: 24.864800000000002
    - type: nauc_map_at_3_diff1
      value: 62.6644
    - type: nauc_map_at_5_max
      value: 55.1021
    - type: nauc_map_at_5_std
      value: 26.2921
    - type: nauc_map_at_5_diff1
      value: 62.624100000000006
    - type: nauc_map_at_10_max
      value: 55.552
    - type: nauc_map_at_10_std
      value: 27.199
    - type: nauc_map_at_10_diff1
      value: 62.7054
    - type: nauc_map_at_20_max
      value: 55.4708
    - type: nauc_map_at_20_std
      value: 27.2067
    - type: nauc_map_at_20_diff1
      value: 62.8945
    - type: nauc_map_at_100_max
      value: 55.3465
    - type: nauc_map_at_100_std
      value: 27.0926
    - type: nauc_map_at_100_diff1
      value: 62.8575
    - type: nauc_map_at_1000_max
      value: 55.3249
    - type: nauc_map_at_1000_std
      value: 27.0527
    - type: nauc_map_at_1000_diff1
      value: 62.8617
    - type: nauc_recall_at_1_max
      value: 48.821
    - type: nauc_recall_at_1_std
      value: 19.6886
    - type: nauc_recall_at_1_diff1
      value: 65.515
    - type: nauc_recall_at_3_max
      value: 62.36279999999999
    - type: nauc_recall_at_3_std
      value: 32.569199999999995
    - type: nauc_recall_at_3_diff1
      value: 58.781499999999994
    - type: nauc_recall_at_5_max
      value: 66.6246
    - type: nauc_recall_at_5_std
      value: 41.813
    - type: nauc_recall_at_5_diff1
      value: 58.1854
    - type: nauc_recall_at_10_max
      value: 74.4567
    - type: nauc_recall_at_10_std
      value: 55.835
    - type: nauc_recall_at_10_diff1
      value: 57.89189999999999
    - type: nauc_recall_at_20_max
      value: 76.9008
    - type: nauc_recall_at_20_std
      value: 62.54110000000001
    - type: nauc_recall_at_20_diff1
      value: 62.200500000000005
    - type: nauc_recall_at_100_max
      value: 76.46300000000001
    - type: nauc_recall_at_100_std
      value: 71.4723
    - type: nauc_recall_at_100_diff1
      value: 59.0844
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 48.821
    - type: nauc_precision_at_1_std
      value: 19.6886
    - type: nauc_precision_at_1_diff1
      value: 65.515
    - type: nauc_precision_at_3_max
      value: 62.36279999999999
    - type: nauc_precision_at_3_std
      value: 32.569199999999995
    - type: nauc_precision_at_3_diff1
      value: 58.781499999999994
    - type: nauc_precision_at_5_max
      value: 66.6246
    - type: nauc_precision_at_5_std
      value: 41.813
    - type: nauc_precision_at_5_diff1
      value: 58.1854
    - type: nauc_precision_at_10_max
      value: 74.4567
    - type: nauc_precision_at_10_std
      value: 55.835
    - type: nauc_precision_at_10_diff1
      value: 57.89189999999999
    - type: nauc_precision_at_20_max
      value: 76.9008
    - type: nauc_precision_at_20_std
      value: 62.54110000000001
    - type: nauc_precision_at_20_diff1
      value: 62.200500000000005
    - type: nauc_precision_at_100_max
      value: 76.46300000000001
    - type: nauc_precision_at_100_std
      value: 71.4723
    - type: nauc_precision_at_100_diff1
      value: 59.0844
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 48.821
    - type: nauc_mrr_at_1_std
      value: 19.6886
    - type: nauc_mrr_at_1_diff1
      value: 65.515
    - type: nauc_mrr_at_3_max
      value: 54.47260000000001
    - type: nauc_mrr_at_3_std
      value: 24.864800000000002
    - type: nauc_mrr_at_3_diff1
      value: 62.6644
    - type: nauc_mrr_at_5_max
      value: 55.1021
    - type: nauc_mrr_at_5_std
      value: 26.2921
    - type: nauc_mrr_at_5_diff1
      value: 62.624100000000006
    - type: nauc_mrr_at_10_max
      value: 55.552
    - type: nauc_mrr_at_10_std
      value: 27.199
    - type: nauc_mrr_at_10_diff1
      value: 62.7054
    - type: nauc_mrr_at_20_max
      value: 55.4708
    - type: nauc_mrr_at_20_std
      value: 27.2067
    - type: nauc_mrr_at_20_diff1
      value: 62.8945
    - type: nauc_mrr_at_100_max
      value: 55.3465
    - type: nauc_mrr_at_100_std
      value: 27.0926
    - type: nauc_mrr_at_100_diff1
      value: 62.8575
    - type: nauc_mrr_at_1000_max
      value: 55.3249
    - type: nauc_mrr_at_1000_std
      value: 27.0527
    - type: nauc_mrr_at_1000_diff1
      value: 62.8617
    - type: main_score
      value: 67.239
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
      value: 70.19999999999999
    - type: ndcg_at_3
      value: 79.566
    - type: ndcg_at_5
      value: 81.012
    - type: ndcg_at_10
      value: 82.217
    - type: ndcg_at_20
      value: 82.97
    - type: ndcg_at_100
      value: 83.43199999999999
    - type: ndcg_at_1000
      value: 83.597
    - type: map_at_1
      value: 70.19999999999999
    - type: map_at_3
      value: 77.333
    - type: map_at_5
      value: 78.13799999999999
    - type: map_at_10
      value: 78.641
    - type: map_at_20
      value: 78.84400000000001
    - type: map_at_100
      value: 78.908
    - type: map_at_1000
      value: 78.914
    - type: recall_at_1
      value: 70.19999999999999
    - type: recall_at_3
      value: 86.0
    - type: recall_at_5
      value: 89.5
    - type: recall_at_10
      value: 93.2
    - type: recall_at_20
      value: 96.2
    - type: recall_at_100
      value: 98.7
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 70.19999999999999
    - type: precision_at_3
      value: 28.666999999999998
    - type: precision_at_5
      value: 17.9
    - type: precision_at_10
      value: 9.32
    - type: precision_at_20
      value: 4.81
    - type: precision_at_100
      value: 0.987
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 70.19999999999999
    - type: mrr_at_3
      value: 77.33330000000001
    - type: mrr_at_5
      value: 78.1383
    - type: mrr_at_10
      value: 78.6408
    - type: mrr_at_20
      value: 78.8441
    - type: mrr_at_100
      value: 78.9075
    - type: mrr_at_1000
      value: 78.91369999999999
    - type: nauc_ndcg_at_1_max
      value: 54.447199999999995
    - type: nauc_ndcg_at_1_std
      value: 5.7226
    - type: nauc_ndcg_at_1_diff1
      value: 71.1626
    - type: nauc_ndcg_at_3_max
      value: 60.4446
    - type: nauc_ndcg_at_3_std
      value: 6.2227
    - type: nauc_ndcg_at_3_diff1
      value: 69.419
    - type: nauc_ndcg_at_5_max
      value: 59.7692
    - type: nauc_ndcg_at_5_std
      value: 7.4161
    - type: nauc_ndcg_at_5_diff1
      value: 68.9958
    - type: nauc_ndcg_at_10_max
      value: 59.559
    - type: nauc_ndcg_at_10_std
      value: 6.792199999999999
    - type: nauc_ndcg_at_10_diff1
      value: 68.42099999999999
    - type: nauc_ndcg_at_20_max
      value: 59.1576
    - type: nauc_ndcg_at_20_std
      value: 6.762600000000001
    - type: nauc_ndcg_at_20_diff1
      value: 69.1402
    - type: nauc_ndcg_at_100_max
      value: 58.729699999999994
    - type: nauc_ndcg_at_100_std
      value: 6.6151
    - type: nauc_ndcg_at_100_diff1
      value: 69.3485
    - type: nauc_ndcg_at_1000_max
      value: 58.68879999999999
    - type: nauc_ndcg_at_1000_std
      value: 6.5546999999999995
    - type: nauc_ndcg_at_1000_diff1
      value: 69.3974
    - type: nauc_map_at_1_max
      value: 54.447199999999995
    - type: nauc_map_at_1_std
      value: 5.7226
    - type: nauc_map_at_1_diff1
      value: 71.1626
    - type: nauc_map_at_3_max
      value: 58.82150000000001
    - type: nauc_map_at_3_std
      value: 6.111
    - type: nauc_map_at_3_diff1
      value: 69.8853
    - type: nauc_map_at_5_max
      value: 58.4332
    - type: nauc_map_at_5_std
      value: 6.6455
    - type: nauc_map_at_5_diff1
      value: 69.6593
    - type: nauc_map_at_10_max
      value: 58.3284
    - type: nauc_map_at_10_std
      value: 6.3941
    - type: nauc_map_at_10_diff1
      value: 69.4544
    - type: nauc_map_at_20_max
      value: 58.2269
    - type: nauc_map_at_20_std
      value: 6.3983
    - type: nauc_map_at_20_diff1
      value: 69.634
    - type: nauc_map_at_100_max
      value: 58.180299999999995
    - type: nauc_map_at_100_std
      value: 6.372
    - type: nauc_map_at_100_diff1
      value: 69.6674
    - type: nauc_map_at_1000_max
      value: 58.1796
    - type: nauc_map_at_1000_std
      value: 6.3696
    - type: nauc_map_at_1000_diff1
      value: 69.6689
    - type: nauc_recall_at_1_max
      value: 54.447199999999995
    - type: nauc_recall_at_1_std
      value: 5.7226
    - type: nauc_recall_at_1_diff1
      value: 71.1626
    - type: nauc_recall_at_3_max
      value: 67.3635
    - type: nauc_recall_at_3_std
      value: 6.682499999999999
    - type: nauc_recall_at_3_diff1
      value: 67.4356
    - type: nauc_recall_at_5_max
      value: 66.6632
    - type: nauc_recall_at_5_std
      value: 11.969899999999999
    - type: nauc_recall_at_5_diff1
      value: 65.4311
    - type: nauc_recall_at_10_max
      value: 68.76339999999999
    - type: nauc_recall_at_10_std
      value: 10.0319
    - type: nauc_recall_at_10_diff1
      value: 59.6357
    - type: nauc_recall_at_20_max
      value: 69.58569999999999
    - type: nauc_recall_at_20_std
      value: 11.5374
    - type: nauc_recall_at_20_diff1
      value: 63.8926
    - type: nauc_recall_at_100_max
      value: 62.5009
    - type: nauc_recall_at_100_std
      value: 12.447
    - type: nauc_recall_at_100_diff1
      value: 65.065
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 54.447199999999995
    - type: nauc_precision_at_1_std
      value: 5.7226
    - type: nauc_precision_at_1_diff1
      value: 71.1626
    - type: nauc_precision_at_3_max
      value: 67.3635
    - type: nauc_precision_at_3_std
      value: 6.682499999999999
    - type: nauc_precision_at_3_diff1
      value: 67.4356
    - type: nauc_precision_at_5_max
      value: 66.6632
    - type: nauc_precision_at_5_std
      value: 11.969899999999999
    - type: nauc_precision_at_5_diff1
      value: 65.4311
    - type: nauc_precision_at_10_max
      value: 68.76339999999999
    - type: nauc_precision_at_10_std
      value: 10.0319
    - type: nauc_precision_at_10_diff1
      value: 59.6357
    - type: nauc_precision_at_20_max
      value: 69.58569999999999
    - type: nauc_precision_at_20_std
      value: 11.5374
    - type: nauc_precision_at_20_diff1
      value: 63.8926
    - type: nauc_precision_at_100_max
      value: 62.5009
    - type: nauc_precision_at_100_std
      value: 12.447
    - type: nauc_precision_at_100_diff1
      value: 65.065
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 54.447199999999995
    - type: nauc_mrr_at_1_std
      value: 5.7226
    - type: nauc_mrr_at_1_diff1
      value: 71.1626
    - type: nauc_mrr_at_3_max
      value: 58.82150000000001
    - type: nauc_mrr_at_3_std
      value: 6.111
    - type: nauc_mrr_at_3_diff1
      value: 69.8853
    - type: nauc_mrr_at_5_max
      value: 58.4332
    - type: nauc_mrr_at_5_std
      value: 6.6455
    - type: nauc_mrr_at_5_diff1
      value: 69.6593
    - type: nauc_mrr_at_10_max
      value: 58.3284
    - type: nauc_mrr_at_10_std
      value: 6.3941
    - type: nauc_mrr_at_10_diff1
      value: 69.4544
    - type: nauc_mrr_at_20_max
      value: 58.2269
    - type: nauc_mrr_at_20_std
      value: 6.3983
    - type: nauc_mrr_at_20_diff1
      value: 69.634
    - type: nauc_mrr_at_100_max
      value: 58.180299999999995
    - type: nauc_mrr_at_100_std
      value: 6.372
    - type: nauc_mrr_at_100_diff1
      value: 69.6674
    - type: nauc_mrr_at_1000_max
      value: 58.1796
    - type: nauc_mrr_at_1000_std
      value: 6.3696
    - type: nauc_mrr_at_1000_diff1
      value: 69.6689
    - type: main_score
      value: 82.217
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
      value: 56.49999999999999
    - type: ndcg_at_3
      value: 66.597
    - type: ndcg_at_5
      value: 68.98100000000001
    - type: ndcg_at_10
      value: 70.829
    - type: ndcg_at_20
      value: 71.77799999999999
    - type: ndcg_at_100
      value: 72.85199999999999
    - type: ndcg_at_1000
      value: 73.563
    - type: map_at_1
      value: 56.49999999999999
    - type: map_at_3
      value: 64.2
    - type: map_at_5
      value: 65.52
    - type: map_at_10
      value: 66.305
    - type: map_at_20
      value: 66.572
    - type: map_at_100
      value: 66.733
    - type: map_at_1000
      value: 66.756
    - type: recall_at_1
      value: 56.49999999999999
    - type: recall_at_3
      value: 73.5
    - type: recall_at_5
      value: 79.3
    - type: recall_at_10
      value: 84.89999999999999
    - type: recall_at_20
      value: 88.6
    - type: recall_at_100
      value: 94.19999999999999
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 56.49999999999999
    - type: precision_at_3
      value: 24.5
    - type: precision_at_5
      value: 15.86
    - type: precision_at_10
      value: 8.49
    - type: precision_at_20
      value: 4.43
    - type: precision_at_100
      value: 0.942
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 56.49999999999999
    - type: mrr_at_3
      value: 64.2
    - type: mrr_at_5
      value: 65.52
    - type: mrr_at_10
      value: 66.30460000000001
    - type: mrr_at_20
      value: 66.5724
    - type: mrr_at_100
      value: 66.7334
    - type: mrr_at_1000
      value: 66.7564
    - type: nauc_ndcg_at_1_max
      value: 55.3207
    - type: nauc_ndcg_at_1_std
      value: 7.2139
    - type: nauc_ndcg_at_1_diff1
      value: 72.6385
    - type: nauc_ndcg_at_3_max
      value: 58.4997
    - type: nauc_ndcg_at_3_std
      value: 8.3729
    - type: nauc_ndcg_at_3_diff1
      value: 69.0137
    - type: nauc_ndcg_at_5_max
      value: 58.213899999999995
    - type: nauc_ndcg_at_5_std
      value: 11.8464
    - type: nauc_ndcg_at_5_diff1
      value: 67.8369
    - type: nauc_ndcg_at_10_max
      value: 58.2068
    - type: nauc_ndcg_at_10_std
      value: 13.320000000000002
    - type: nauc_ndcg_at_10_diff1
      value: 67.8139
    - type: nauc_ndcg_at_20_max
      value: 58.0545
    - type: nauc_ndcg_at_20_std
      value: 13.601199999999999
    - type: nauc_ndcg_at_20_diff1
      value: 67.814
    - type: nauc_ndcg_at_100_max
      value: 58.1651
    - type: nauc_ndcg_at_100_std
      value: 13.946900000000001
    - type: nauc_ndcg_at_100_diff1
      value: 68.07180000000001
    - type: nauc_ndcg_at_1000_max
      value: 57.9397
    - type: nauc_ndcg_at_1000_std
      value: 12.188400000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 68.6001
    - type: nauc_map_at_1_max
      value: 55.3207
    - type: nauc_map_at_1_std
      value: 7.2139
    - type: nauc_map_at_1_diff1
      value: 72.6385
    - type: nauc_map_at_3_max
      value: 57.678399999999996
    - type: nauc_map_at_3_std
      value: 7.900500000000001
    - type: nauc_map_at_3_diff1
      value: 69.8646
    - type: nauc_map_at_5_max
      value: 57.5229
    - type: nauc_map_at_5_std
      value: 9.7157
    - type: nauc_map_at_5_diff1
      value: 69.2704
    - type: nauc_map_at_10_max
      value: 57.5133
    - type: nauc_map_at_10_std
      value: 10.2078
    - type: nauc_map_at_10_diff1
      value: 69.2876
    - type: nauc_map_at_20_max
      value: 57.4843
    - type: nauc_map_at_20_std
      value: 10.2501
    - type: nauc_map_at_20_diff1
      value: 69.303
    - type: nauc_map_at_100_max
      value: 57.4927
    - type: nauc_map_at_100_std
      value: 10.3077
    - type: nauc_map_at_100_diff1
      value: 69.3295
    - type: nauc_map_at_1000_max
      value: 57.4921
    - type: nauc_map_at_1000_std
      value: 10.2661
    - type: nauc_map_at_1000_diff1
      value: 69.3497
    - type: nauc_recall_at_1_max
      value: 55.3207
    - type: nauc_recall_at_1_std
      value: 7.2139
    - type: nauc_recall_at_1_diff1
      value: 72.6385
    - type: nauc_recall_at_3_max
      value: 61.36899999999999
    - type: nauc_recall_at_3_std
      value: 10.1165
    - type: nauc_recall_at_3_diff1
      value: 66.0874
    - type: nauc_recall_at_5_max
      value: 60.956999999999994
    - type: nauc_recall_at_5_std
      value: 21.409
    - type: nauc_recall_at_5_diff1
      value: 61.770199999999996
    - type: nauc_recall_at_10_max
      value: 61.73689999999999
    - type: nauc_recall_at_10_std
      value: 32.1058
    - type: nauc_recall_at_10_diff1
      value: 59.7434
    - type: nauc_recall_at_20_max
      value: 61.2737
    - type: nauc_recall_at_20_std
      value: 39.7564
    - type: nauc_recall_at_20_diff1
      value: 57.3813
    - type: nauc_recall_at_100_max
      value: 66.6667
    - type: nauc_recall_at_100_std
      value: 69.0613
    - type: nauc_recall_at_100_diff1
      value: 53.7574
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 55.3207
    - type: nauc_precision_at_1_std
      value: 7.2139
    - type: nauc_precision_at_1_diff1
      value: 72.6385
    - type: nauc_precision_at_3_max
      value: 61.36899999999999
    - type: nauc_precision_at_3_std
      value: 10.1165
    - type: nauc_precision_at_3_diff1
      value: 66.0874
    - type: nauc_precision_at_5_max
      value: 60.956999999999994
    - type: nauc_precision_at_5_std
      value: 21.409
    - type: nauc_precision_at_5_diff1
      value: 61.770199999999996
    - type: nauc_precision_at_10_max
      value: 61.73689999999999
    - type: nauc_precision_at_10_std
      value: 32.1058
    - type: nauc_precision_at_10_diff1
      value: 59.7434
    - type: nauc_precision_at_20_max
      value: 61.2737
    - type: nauc_precision_at_20_std
      value: 39.7564
    - type: nauc_precision_at_20_diff1
      value: 57.3813
    - type: nauc_precision_at_100_max
      value: 66.6667
    - type: nauc_precision_at_100_std
      value: 69.0613
    - type: nauc_precision_at_100_diff1
      value: 53.7574
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 55.3207
    - type: nauc_mrr_at_1_std
      value: 7.2139
    - type: nauc_mrr_at_1_diff1
      value: 72.6385
    - type: nauc_mrr_at_3_max
      value: 57.678399999999996
    - type: nauc_mrr_at_3_std
      value: 7.900500000000001
    - type: nauc_mrr_at_3_diff1
      value: 69.8646
    - type: nauc_mrr_at_5_max
      value: 57.5229
    - type: nauc_mrr_at_5_std
      value: 9.7157
    - type: nauc_mrr_at_5_diff1
      value: 69.2704
    - type: nauc_mrr_at_10_max
      value: 57.5133
    - type: nauc_mrr_at_10_std
      value: 10.2078
    - type: nauc_mrr_at_10_diff1
      value: 69.2876
    - type: nauc_mrr_at_20_max
      value: 57.4843
    - type: nauc_mrr_at_20_std
      value: 10.2501
    - type: nauc_mrr_at_20_diff1
      value: 69.303
    - type: nauc_mrr_at_100_max
      value: 57.4927
    - type: nauc_mrr_at_100_std
      value: 10.3077
    - type: nauc_mrr_at_100_diff1
      value: 69.3295
    - type: nauc_mrr_at_1000_max
      value: 57.4921
    - type: nauc_mrr_at_1000_std
      value: 10.2661
    - type: nauc_mrr_at_1000_diff1
      value: 69.3497
    - type: main_score
      value: 70.829
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
      value: 50.3
    - type: ndcg_at_3
      value: 62.883
    - type: ndcg_at_5
      value: 65.11200000000001
    - type: ndcg_at_10
      value: 67.044
    - type: ndcg_at_20
      value: 68.326
    - type: ndcg_at_100
      value: 69.592
    - type: ndcg_at_1000
      value: 70.209
    - type: map_at_1
      value: 50.3
    - type: map_at_3
      value: 59.8
    - type: map_at_5
      value: 61.040000000000006
    - type: map_at_10
      value: 61.852
    - type: map_at_20
      value: 62.212999999999994
    - type: map_at_100
      value: 62.397000000000006
    - type: map_at_1000
      value: 62.416000000000004
    - type: recall_at_1
      value: 50.3
    - type: recall_at_3
      value: 71.8
    - type: recall_at_5
      value: 77.2
    - type: recall_at_10
      value: 83.1
    - type: recall_at_20
      value: 88.1
    - type: recall_at_100
      value: 94.8
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 50.3
    - type: precision_at_3
      value: 23.933
    - type: precision_at_5
      value: 15.440000000000001
    - type: precision_at_10
      value: 8.309999999999999
    - type: precision_at_20
      value: 4.405
    - type: precision_at_100
      value: 0.9480000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 50.3
    - type: mrr_at_3
      value: 59.8
    - type: mrr_at_5
      value: 61.040000000000006
    - type: mrr_at_10
      value: 61.8522
    - type: mrr_at_20
      value: 62.21339999999999
    - type: mrr_at_100
      value: 62.397499999999994
    - type: mrr_at_1000
      value: 62.415600000000005
    - type: nauc_ndcg_at_1_max
      value: 27.9845
    - type: nauc_ndcg_at_1_std
      value: -16.28
    - type: nauc_ndcg_at_1_diff1
      value: 61.9927
    - type: nauc_ndcg_at_3_max
      value: 33.0521
    - type: nauc_ndcg_at_3_std
      value: -10.3558
    - type: nauc_ndcg_at_3_diff1
      value: 56.8436
    - type: nauc_ndcg_at_5_max
      value: 34.6635
    - type: nauc_ndcg_at_5_std
      value: -7.1861
    - type: nauc_ndcg_at_5_diff1
      value: 56.39999999999999
    - type: nauc_ndcg_at_10_max
      value: 36.0742
    - type: nauc_ndcg_at_10_std
      value: -6.1496
    - type: nauc_ndcg_at_10_diff1
      value: 57.239
    - type: nauc_ndcg_at_20_max
      value: 36.5836
    - type: nauc_ndcg_at_20_std
      value: -5.3723
    - type: nauc_ndcg_at_20_diff1
      value: 57.7333
    - type: nauc_ndcg_at_100_max
      value: 36.0909
    - type: nauc_ndcg_at_100_std
      value: -5.655799999999999
    - type: nauc_ndcg_at_100_diff1
      value: 58.411699999999996
    - type: nauc_ndcg_at_1000_max
      value: 34.8377
    - type: nauc_ndcg_at_1000_std
      value: -7.542999999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 58.198899999999995
    - type: nauc_map_at_1_max
      value: 27.9845
    - type: nauc_map_at_1_std
      value: -16.28
    - type: nauc_map_at_1_diff1
      value: 61.9927
    - type: nauc_map_at_3_max
      value: 31.7824
    - type: nauc_map_at_3_std
      value: -11.9282
    - type: nauc_map_at_3_diff1
      value: 58.2543
    - type: nauc_map_at_5_max
      value: 32.5811
    - type: nauc_map_at_5_std
      value: -10.3315
    - type: nauc_map_at_5_diff1
      value: 58.046
    - type: nauc_map_at_10_max
      value: 33.0525
    - type: nauc_map_at_10_std
      value: -10.0071
    - type: nauc_map_at_10_diff1
      value: 58.3778
    - type: nauc_map_at_20_max
      value: 33.164
    - type: nauc_map_at_20_std
      value: -9.8753
    - type: nauc_map_at_20_diff1
      value: 58.5075
    - type: nauc_map_at_100_max
      value: 33.0857
    - type: nauc_map_at_100_std
      value: -9.9373
    - type: nauc_map_at_100_diff1
      value: 58.581399999999995
    - type: nauc_map_at_1000_max
      value: 33.0589
    - type: nauc_map_at_1000_std
      value: -9.9773
    - type: nauc_map_at_1000_diff1
      value: 58.5777
    - type: nauc_recall_at_1_max
      value: 27.9845
    - type: nauc_recall_at_1_std
      value: -16.28
    - type: nauc_recall_at_1_diff1
      value: 61.9927
    - type: nauc_recall_at_3_max
      value: 37.5284
    - type: nauc_recall_at_3_std
      value: -4.7627999999999995
    - type: nauc_recall_at_3_diff1
      value: 51.8022
    - type: nauc_recall_at_5_max
      value: 43.4852
    - type: nauc_recall_at_5_std
      value: 6.3649
    - type: nauc_recall_at_5_diff1
      value: 49.5664
    - type: nauc_recall_at_10_max
      value: 53.156000000000006
    - type: nauc_recall_at_10_std
      value: 15.4361
    - type: nauc_recall_at_10_diff1
      value: 51.865300000000005
    - type: nauc_recall_at_20_max
      value: 63.3834
    - type: nauc_recall_at_20_std
      value: 30.2094
    - type: nauc_recall_at_20_diff1
      value: 54.013999999999996
    - type: nauc_recall_at_100_max
      value: 84.36399999999999
    - type: nauc_recall_at_100_std
      value: 67.20089999999999
    - type: nauc_recall_at_100_diff1
      value: 66.6146
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 27.9845
    - type: nauc_precision_at_1_std
      value: -16.28
    - type: nauc_precision_at_1_diff1
      value: 61.9927
    - type: nauc_precision_at_3_max
      value: 37.5284
    - type: nauc_precision_at_3_std
      value: -4.7627999999999995
    - type: nauc_precision_at_3_diff1
      value: 51.8022
    - type: nauc_precision_at_5_max
      value: 43.4852
    - type: nauc_precision_at_5_std
      value: 6.3649
    - type: nauc_precision_at_5_diff1
      value: 49.5664
    - type: nauc_precision_at_10_max
      value: 53.156000000000006
    - type: nauc_precision_at_10_std
      value: 15.4361
    - type: nauc_precision_at_10_diff1
      value: 51.865300000000005
    - type: nauc_precision_at_20_max
      value: 63.3834
    - type: nauc_precision_at_20_std
      value: 30.2094
    - type: nauc_precision_at_20_diff1
      value: 54.013999999999996
    - type: nauc_precision_at_100_max
      value: 84.36399999999999
    - type: nauc_precision_at_100_std
      value: 67.20089999999999
    - type: nauc_precision_at_100_diff1
      value: 66.6146
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 27.9845
    - type: nauc_mrr_at_1_std
      value: -16.28
    - type: nauc_mrr_at_1_diff1
      value: 61.9927
    - type: nauc_mrr_at_3_max
      value: 31.7824
    - type: nauc_mrr_at_3_std
      value: -11.9282
    - type: nauc_mrr_at_3_diff1
      value: 58.2543
    - type: nauc_mrr_at_5_max
      value: 32.5811
    - type: nauc_mrr_at_5_std
      value: -10.3315
    - type: nauc_mrr_at_5_diff1
      value: 58.046
    - type: nauc_mrr_at_10_max
      value: 33.0525
    - type: nauc_mrr_at_10_std
      value: -10.0071
    - type: nauc_mrr_at_10_diff1
      value: 58.3778
    - type: nauc_mrr_at_20_max
      value: 33.164
    - type: nauc_mrr_at_20_std
      value: -9.8753
    - type: nauc_mrr_at_20_diff1
      value: 58.5075
    - type: nauc_mrr_at_100_max
      value: 33.0857
    - type: nauc_mrr_at_100_std
      value: -9.9373
    - type: nauc_mrr_at_100_diff1
      value: 58.581399999999995
    - type: nauc_mrr_at_1000_max
      value: 33.0589
    - type: nauc_mrr_at_1000_std
      value: -9.9773
    - type: nauc_mrr_at_1000_diff1
      value: 58.5777
    - type: main_score
      value: 67.044
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
      value: 52.5
    - type: ndcg_at_3
      value: 65.362
    - type: ndcg_at_5
      value: 67.797
    - type: ndcg_at_10
      value: 69.791
    - type: ndcg_at_20
      value: 70.787
    - type: ndcg_at_100
      value: 71.607
    - type: ndcg_at_1000
      value: 72.24000000000001
    - type: map_at_1
      value: 52.5
    - type: map_at_3
      value: 62.233000000000004
    - type: map_at_5
      value: 63.588
    - type: map_at_10
      value: 64.424
    - type: map_at_20
      value: 64.703
    - type: map_at_100
      value: 64.825
    - type: map_at_1000
      value: 64.84100000000001
    - type: recall_at_1
      value: 52.5
    - type: recall_at_3
      value: 74.4
    - type: recall_at_5
      value: 80.30000000000001
    - type: recall_at_10
      value: 86.4
    - type: recall_at_20
      value: 90.3
    - type: recall_at_100
      value: 94.6
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 52.5
    - type: precision_at_3
      value: 24.8
    - type: precision_at_5
      value: 16.06
    - type: precision_at_10
      value: 8.64
    - type: precision_at_20
      value: 4.515000000000001
    - type: precision_at_100
      value: 0.946
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 52.5
    - type: mrr_at_3
      value: 62.2333
    - type: mrr_at_5
      value: 63.5883
    - type: mrr_at_10
      value: 64.4237
    - type: mrr_at_20
      value: 64.7029
    - type: mrr_at_100
      value: 64.8249
    - type: mrr_at_1000
      value: 64.84140000000001
    - type: nauc_ndcg_at_1_max
      value: 28.977700000000002
    - type: nauc_ndcg_at_1_std
      value: 5.5688
    - type: nauc_ndcg_at_1_diff1
      value: 62.8127
    - type: nauc_ndcg_at_3_max
      value: 42.5053
    - type: nauc_ndcg_at_3_std
      value: 13.8126
    - type: nauc_ndcg_at_3_diff1
      value: 60.791700000000006
    - type: nauc_ndcg_at_5_max
      value: 43.521100000000004
    - type: nauc_ndcg_at_5_std
      value: 14.5838
    - type: nauc_ndcg_at_5_diff1
      value: 61.267700000000005
    - type: nauc_ndcg_at_10_max
      value: 43.2523
    - type: nauc_ndcg_at_10_std
      value: 16.2237
    - type: nauc_ndcg_at_10_diff1
      value: 61.642300000000006
    - type: nauc_ndcg_at_20_max
      value: 42.7707
    - type: nauc_ndcg_at_20_std
      value: 17.0607
    - type: nauc_ndcg_at_20_diff1
      value: 61.5855
    - type: nauc_ndcg_at_100_max
      value: 42.127900000000004
    - type: nauc_ndcg_at_100_std
      value: 16.582900000000002
    - type: nauc_ndcg_at_100_diff1
      value: 61.916700000000006
    - type: nauc_ndcg_at_1000_max
      value: 40.7945
    - type: nauc_ndcg_at_1000_std
      value: 14.6562
    - type: nauc_ndcg_at_1000_diff1
      value: 61.7069
    - type: nauc_map_at_1_max
      value: 28.977700000000002
    - type: nauc_map_at_1_std
      value: 5.5688
    - type: nauc_map_at_1_diff1
      value: 62.8127
    - type: nauc_map_at_3_max
      value: 38.5313
    - type: nauc_map_at_3_std
      value: 11.2395
    - type: nauc_map_at_3_diff1
      value: 61.1888
    - type: nauc_map_at_5_max
      value: 38.8835
    - type: nauc_map_at_5_std
      value: 11.5395
    - type: nauc_map_at_5_diff1
      value: 61.449
    - type: nauc_map_at_10_max
      value: 38.6822
    - type: nauc_map_at_10_std
      value: 12.0181
    - type: nauc_map_at_10_diff1
      value: 61.5846
    - type: nauc_map_at_20_max
      value: 38.5328
    - type: nauc_map_at_20_std
      value: 12.182500000000001
    - type: nauc_map_at_20_diff1
      value: 61.578599999999994
    - type: nauc_map_at_100_max
      value: 38.4484
    - type: nauc_map_at_100_std
      value: 12.1157
    - type: nauc_map_at_100_diff1
      value: 61.6247
    - type: nauc_map_at_1000_max
      value: 38.418600000000005
    - type: nauc_map_at_1000_std
      value: 12.0795
    - type: nauc_map_at_1000_diff1
      value: 61.6214
    - type: nauc_recall_at_1_max
      value: 28.977700000000002
    - type: nauc_recall_at_1_std
      value: 5.5688
    - type: nauc_recall_at_1_diff1
      value: 62.8127
    - type: nauc_recall_at_3_max
      value: 57.338699999999996
    - type: nauc_recall_at_3_std
      value: 23.4946
    - type: nauc_recall_at_3_diff1
      value: 59.4094
    - type: nauc_recall_at_5_max
      value: 64.4058
    - type: nauc_recall_at_5_std
      value: 28.382
    - type: nauc_recall_at_5_diff1
      value: 60.671600000000005
    - type: nauc_recall_at_10_max
      value: 71.11070000000001
    - type: nauc_recall_at_10_std
      value: 43.6152
    - type: nauc_recall_at_10_diff1
      value: 62.6013
    - type: nauc_recall_at_20_max
      value: 76.3142
    - type: nauc_recall_at_20_std
      value: 61.0644
    - type: nauc_recall_at_20_diff1
      value: 62.244600000000005
    - type: nauc_recall_at_100_max
      value: 87.9526
    - type: nauc_recall_at_100_std
      value: 84.63619999999999
    - type: nauc_recall_at_100_diff1
      value: 69.6848
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 28.977700000000002
    - type: nauc_precision_at_1_std
      value: 5.5688
    - type: nauc_precision_at_1_diff1
      value: 62.8127
    - type: nauc_precision_at_3_max
      value: 57.338699999999996
    - type: nauc_precision_at_3_std
      value: 23.4946
    - type: nauc_precision_at_3_diff1
      value: 59.4094
    - type: nauc_precision_at_5_max
      value: 64.4058
    - type: nauc_precision_at_5_std
      value: 28.382
    - type: nauc_precision_at_5_diff1
      value: 60.671600000000005
    - type: nauc_precision_at_10_max
      value: 71.11070000000001
    - type: nauc_precision_at_10_std
      value: 43.6152
    - type: nauc_precision_at_10_diff1
      value: 62.6013
    - type: nauc_precision_at_20_max
      value: 76.3142
    - type: nauc_precision_at_20_std
      value: 61.0644
    - type: nauc_precision_at_20_diff1
      value: 62.244600000000005
    - type: nauc_precision_at_100_max
      value: 87.9526
    - type: nauc_precision_at_100_std
      value: 84.63619999999999
    - type: nauc_precision_at_100_diff1
      value: 69.6848
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 28.977700000000002
    - type: nauc_mrr_at_1_std
      value: 5.5688
    - type: nauc_mrr_at_1_diff1
      value: 62.8127
    - type: nauc_mrr_at_3_max
      value: 38.5313
    - type: nauc_mrr_at_3_std
      value: 11.2395
    - type: nauc_mrr_at_3_diff1
      value: 61.1888
    - type: nauc_mrr_at_5_max
      value: 38.8835
    - type: nauc_mrr_at_5_std
      value: 11.5395
    - type: nauc_mrr_at_5_diff1
      value: 61.449
    - type: nauc_mrr_at_10_max
      value: 38.6822
    - type: nauc_mrr_at_10_std
      value: 12.0181
    - type: nauc_mrr_at_10_diff1
      value: 61.5846
    - type: nauc_mrr_at_20_max
      value: 38.5328
    - type: nauc_mrr_at_20_std
      value: 12.182500000000001
    - type: nauc_mrr_at_20_diff1
      value: 61.578599999999994
    - type: nauc_mrr_at_100_max
      value: 38.4484
    - type: nauc_mrr_at_100_std
      value: 12.1157
    - type: nauc_mrr_at_100_diff1
      value: 61.6247
    - type: nauc_mrr_at_1000_max
      value: 38.418600000000005
    - type: nauc_mrr_at_1000_std
      value: 12.0795
    - type: nauc_mrr_at_1000_diff1
      value: 61.6214
    - type: main_score
      value: 69.791
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
      value: 33.032000000000004
    - type: ndcg_at_3
      value: 38.041000000000004
    - type: ndcg_at_5
      value: 40.67
    - type: ndcg_at_10
      value: 43.651
    - type: ndcg_at_20
      value: 45.255
    - type: ndcg_at_100
      value: 48.41
    - type: ndcg_at_1000
      value: 50.775000000000006
    - type: map_at_1
      value: 33.032000000000004
    - type: map_at_3
      value: 36.802
    - type: map_at_5
      value: 38.273
    - type: map_at_10
      value: 39.45
    - type: map_at_20
      value: 39.891
    - type: map_at_100
      value: 40.312
    - type: map_at_1000
      value: 40.396
    - type: recall_at_1
      value: 33.032000000000004
    - type: recall_at_3
      value: 41.629
    - type: recall_at_5
      value: 47.964
    - type: recall_at_10
      value: 57.465999999999994
    - type: recall_at_20
      value: 63.800999999999995
    - type: recall_at_100
      value: 80.99499999999999
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 33.032000000000004
    - type: precision_at_3
      value: 13.876
    - type: precision_at_5
      value: 9.593
    - type: precision_at_10
      value: 5.747
    - type: precision_at_20
      value: 3.19
    - type: precision_at_100
      value: 0.8099999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 33.0317
    - type: mrr_at_3
      value: 36.8024
    - type: mrr_at_5
      value: 38.273
    - type: mrr_at_10
      value: 39.4504
    - type: mrr_at_20
      value: 39.8911
    - type: mrr_at_100
      value: 40.3122
    - type: mrr_at_1000
      value: 40.3955
    - type: nauc_ndcg_at_1_max
      value: 53.0197
    - type: nauc_ndcg_at_1_std
      value: 0.8863
    - type: nauc_ndcg_at_1_diff1
      value: 67.8151
    - type: nauc_ndcg_at_3_max
      value: 50.37350000000001
    - type: nauc_ndcg_at_3_std
      value: 1.3549
    - type: nauc_ndcg_at_3_diff1
      value: 61.698699999999995
    - type: nauc_ndcg_at_5_max
      value: 49.1498
    - type: nauc_ndcg_at_5_std
      value: 2.5727
    - type: nauc_ndcg_at_5_diff1
      value: 58.0748
    - type: nauc_ndcg_at_10_max
      value: 47.5197
    - type: nauc_ndcg_at_10_std
      value: 2.7498
    - type: nauc_ndcg_at_10_diff1
      value: 56.9398
    - type: nauc_ndcg_at_20_max
      value: 47.5836
    - type: nauc_ndcg_at_20_std
      value: 3.4302
    - type: nauc_ndcg_at_20_diff1
      value: 55.8913
    - type: nauc_ndcg_at_100_max
      value: 48.079499999999996
    - type: nauc_ndcg_at_100_std
      value: 3.7983999999999996
    - type: nauc_ndcg_at_100_diff1
      value: 56.7706
    - type: nauc_ndcg_at_1000_max
      value: 48.7136
    - type: nauc_ndcg_at_1000_std
      value: 2.949
    - type: nauc_ndcg_at_1000_diff1
      value: 58.0488
    - type: nauc_map_at_1_max
      value: 53.0197
    - type: nauc_map_at_1_std
      value: 0.8863
    - type: nauc_map_at_1_diff1
      value: 67.8151
    - type: nauc_map_at_3_max
      value: 51.1105
    - type: nauc_map_at_3_std
      value: 1.5191
    - type: nauc_map_at_3_diff1
      value: 63.005900000000004
    - type: nauc_map_at_5_max
      value: 50.4462
    - type: nauc_map_at_5_std
      value: 2.0751
    - type: nauc_map_at_5_diff1
      value: 61.0287
    - type: nauc_map_at_10_max
      value: 49.772499999999994
    - type: nauc_map_at_10_std
      value: 2.1092
    - type: nauc_map_at_10_diff1
      value: 60.528000000000006
    - type: nauc_map_at_20_max
      value: 49.7904
    - type: nauc_map_at_20_std
      value: 2.3456
    - type: nauc_map_at_20_diff1
      value: 60.2416
    - type: nauc_map_at_100_max
      value: 49.8742
    - type: nauc_map_at_100_std
      value: 2.3747000000000003
    - type: nauc_map_at_100_diff1
      value: 60.390600000000006
    - type: nauc_map_at_1000_max
      value: 49.8875
    - type: nauc_map_at_1000_std
      value: 2.3390999999999997
    - type: nauc_map_at_1000_diff1
      value: 60.41180000000001
    - type: nauc_recall_at_1_max
      value: 53.0197
    - type: nauc_recall_at_1_std
      value: 0.8863
    - type: nauc_recall_at_1_diff1
      value: 67.8151
    - type: nauc_recall_at_3_max
      value: 48.2306
    - type: nauc_recall_at_3_std
      value: 0.7745
    - type: nauc_recall_at_3_diff1
      value: 58.0358
    - type: nauc_recall_at_5_max
      value: 45.1577
    - type: nauc_recall_at_5_std
      value: 4.228400000000001
    - type: nauc_recall_at_5_diff1
      value: 49.0182
    - type: nauc_recall_at_10_max
      value: 39.584
    - type: nauc_recall_at_10_std
      value: 5.1647
    - type: nauc_recall_at_10_diff1
      value: 44.864399999999996
    - type: nauc_recall_at_20_max
      value: 39.1616
    - type: nauc_recall_at_20_std
      value: 7.9384
    - type: nauc_recall_at_20_diff1
      value: 39.124700000000004
    - type: nauc_recall_at_100_max
      value: 38.4356
    - type: nauc_recall_at_100_std
      value: 14.498
    - type: nauc_recall_at_100_diff1
      value: 36.8934
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 53.0197
    - type: nauc_precision_at_1_std
      value: 0.8863
    - type: nauc_precision_at_1_diff1
      value: 67.8151
    - type: nauc_precision_at_3_max
      value: 48.2306
    - type: nauc_precision_at_3_std
      value: 0.7745
    - type: nauc_precision_at_3_diff1
      value: 58.0358
    - type: nauc_precision_at_5_max
      value: 45.1577
    - type: nauc_precision_at_5_std
      value: 4.228400000000001
    - type: nauc_precision_at_5_diff1
      value: 49.0182
    - type: nauc_precision_at_10_max
      value: 39.584
    - type: nauc_precision_at_10_std
      value: 5.1647
    - type: nauc_precision_at_10_diff1
      value: 44.864399999999996
    - type: nauc_precision_at_20_max
      value: 39.1616
    - type: nauc_precision_at_20_std
      value: 7.9384
    - type: nauc_precision_at_20_diff1
      value: 39.124700000000004
    - type: nauc_precision_at_100_max
      value: 38.4356
    - type: nauc_precision_at_100_std
      value: 14.498
    - type: nauc_precision_at_100_diff1
      value: 36.8934
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 53.0197
    - type: nauc_mrr_at_1_std
      value: 0.8863
    - type: nauc_mrr_at_1_diff1
      value: 67.8151
    - type: nauc_mrr_at_3_max
      value: 51.1105
    - type: nauc_mrr_at_3_std
      value: 1.5191
    - type: nauc_mrr_at_3_diff1
      value: 63.005900000000004
    - type: nauc_mrr_at_5_max
      value: 50.4462