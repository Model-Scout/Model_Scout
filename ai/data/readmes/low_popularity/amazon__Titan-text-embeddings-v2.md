---
license: other
license_name: amazon-service-terms
license_link: https://aws.amazon.com/service-terms/
language:
- en
- fr
- de
- es
- ja
- zh
- hi
- ar
- it
- pt
- sv
- ko
- he
- cs
- tr
- tl
- ru
- nl
- pl
- ta
- mr
- ml
- te
- kn
- vi
- id
- fa
- hu
- el
- ro
- da
- th
- fi
- sk
- uk
- 'no'
- bg
- ca
- sr
- hr
- lt
- sl
- et
- la
- bn
- lv
- ms
- bs
- sq
- az
- gl
- is
- ka
- mk
- eu
- hy
- ne
- ur
- kk
- mn
- be
- uz
- km
- nn
- gu
- my
- cy
- eo
- si
- tt
- sw
- af
- ga
- pa
- ku
- ky
- tg
- or
- lo
- fo
- mt
- so
- lb
- am
- oc
- jv
- ha
- ps
- sa
- fy
- mg
- as
- ba
- br
- tk
- co
- dv
- rw
- ht
- yi
- sd
- zu
- gd
- bo
- ug
- mi
- rm
- xh
- su
- yo
tags:
- feature-extraction
- sentence-similarity
- mteb
inference: false
model-index:
- name: Titan-text-embeddings-v2
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 79.31343283582089
    - type: ap
      value: 43.9465851246623
    - type: f1
      value: 73.6131343594374
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (de)
      config: de
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 70.94218415417559
    - type: ap
      value: 82.30115528468109
    - type: f1
      value: 69.37963699148699
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en-ext)
      config: en-ext
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 82.29385307346327
    - type: ap
      value: 29.956638709449372
    - type: f1
      value: 68.88158061498754
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (ja)
      config: ja
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 80.06423982869379
    - type: ap
      value: 25.2439835379337
    - type: f1
      value: 65.53837311569734
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 76.66435
    - type: ap
      value: 70.76988138513991
    - type: f1
      value: 76.54117595647566
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 35.276
    - type: f1
      value: 34.90637768461089
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (de)
      config: de
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 38.826
    - type: f1
      value: 37.71339372044998
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (es)
      config: es
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 39.385999999999996
    - type: f1
      value: 38.24347249789392
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (fr)
      config: fr
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 39.472
    - type: f1
      value: 38.37157729490788
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (ja)
      config: ja
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 35.897999999999996
    - type: f1
      value: 35.187204289589346
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 36.068
    - type: f1
      value: 35.042441064207175
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.027
    - type: map_at_10
      value: 42.617
    - type: map_at_100
      value: 43.686
    - type: map_at_1000
      value: 43.695
    - type: map_at_3
      value: 37.684
    - type: map_at_5
      value: 40.532000000000004
    - type: mrr_at_1
      value: 27.667
    - type: mrr_at_10
      value: 42.88
    - type: mrr_at_100
      value: 43.929
    - type: mrr_at_1000
      value: 43.938
    - type: mrr_at_3
      value: 37.933
    - type: mrr_at_5
      value: 40.774
    - type: ndcg_at_1
      value: 27.027
    - type: ndcg_at_10
      value: 51.312000000000005
    - type: ndcg_at_100
      value: 55.696
    - type: ndcg_at_1000
      value: 55.896
    - type: ndcg_at_3
      value: 41.124
    - type: ndcg_at_5
      value: 46.283
    - type: precision_at_1
      value: 27.027
    - type: precision_at_10
      value: 7.9159999999999995
    - type: precision_at_100
      value: 0.979
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_3
      value: 17.022000000000002
    - type: precision_at_5
      value: 12.731
    - type: recall_at_1
      value: 27.027
    - type: recall_at_10
      value: 79.161
    - type: recall_at_100
      value: 97.937
    - type: recall_at_1000
      value: 99.431
    - type: recall_at_3
      value: 51.06699999999999
    - type: recall_at_5
      value: 63.656
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 41.775131599226874
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 34.134214263072494
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 63.2885651257187
    - type: mrr
      value: 76.37712702809655
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 89.53738990667027
    - type: cos_sim_spearman
      value: 87.13210584606783
    - type: euclidean_pearson
      value: 87.33265405736388
    - type: euclidean_spearman
      value: 87.18632394893399
    - type: manhattan_pearson
      value: 87.33673166528312
    - type: manhattan_spearman
      value: 86.9736685010257
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (de-en)
      config: de-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 98.32985386221294
    - type: f1
      value: 98.18371607515658
    - type: precision
      value: 98.1106471816284
    - type: recall
      value: 98.32985386221294
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (fr-en)
      config: fr-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 98.20603125687872
    - type: f1
      value: 98.04461075647515
    - type: precision
      value: 97.96390050627338
    - type: recall
      value: 98.20603125687872
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (ru-en)
      config: ru-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 94.8874263941808
    - type: f1
      value: 94.57568410114305
    - type: precision
      value: 94.42096755570951
    - type: recall
      value: 94.8874263941808
  - task:
      type: BitextMining
    dataset:
      type: mteb/bucc-bitext-mining
      name: MTEB BUCC (zh-en)
      config: zh-en
      split: test
      revision: d51519689f32196a32af33b075a01d0e7c51e252
    metrics:
    - type: accuracy
      value: 96.78778304370721
    - type: f1
      value: 96.75267684746358
    - type: precision
      value: 96.73512374934175
    - type: recall
      value: 96.78778304370721
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 84.3051948051948
    - type: f1
      value: 83.97876601554812
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 35.005716163806575
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 30.999141295578852
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 36.153
    - type: map_at_10
      value: 48.742000000000004
    - type: map_at_100
      value: 50.253
    - type: map_at_1000
      value: 50.373999999999995
    - type: map_at_3
      value: 45.089
    - type: map_at_5
      value: 47.08
    - type: mrr_at_1
      value: 44.635000000000005
    - type: mrr_at_10
      value: 54.715
    - type: mrr_at_100
      value: 55.300000000000004
    - type: mrr_at_1000
      value: 55.337
    - type: mrr_at_3
      value: 52.527
    - type: mrr_at_5
      value: 53.76499999999999
    - type: ndcg_at_1
      value: 44.635000000000005
    - type: ndcg_at_10
      value: 55.31
    - type: ndcg_at_100
      value: 60.084
    - type: ndcg_at_1000
      value: 61.645
    - type: ndcg_at_3
      value: 50.876999999999995
    - type: ndcg_at_5
      value: 52.764
    - type: precision_at_1
      value: 44.635000000000005
    - type: precision_at_10
      value: 10.687000000000001
    - type: precision_at_100
      value: 1.66
    - type: precision_at_1000
      value: 0.212
    - type: precision_at_3
      value: 24.94
    - type: precision_at_5
      value: 17.596999999999998
    - type: recall_at_1
      value: 36.153
    - type: recall_at_10
      value: 67.308
    - type: recall_at_100
      value: 87.199
    - type: recall_at_1000
      value: 96.904
    - type: recall_at_3
      value: 53.466
    - type: recall_at_5
      value: 59.512
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.0
    - type: map_at_10
      value: 43.646
    - type: map_at_100
      value: 44.933
    - type: map_at_1000
      value: 45.049
    - type: map_at_3
      value: 40.333999999999996
    - type: map_at_5
      value: 42.108000000000004
    - type: mrr_at_1
      value: 40.382
    - type: mrr_at_10
      value: 49.738
    - type: mrr_at_100
      value: 50.331
    - type: mrr_at_1000
      value: 50.364
    - type: mrr_at_3
      value: 47.442
    - type: mrr_at_5
      value: 48.719
    - type: ndcg_at_1
      value: 40.382
    - type: ndcg_at_10
      value: 49.808
    - type: ndcg_at_100
      value: 54.053
    - type: ndcg_at_1000
      value: 55.753
    - type: ndcg_at_3
      value: 45.355000000000004
    - type: ndcg_at_5
      value: 47.215
    - type: precision_at_1
      value: 40.382
    - type: precision_at_10
      value: 9.58
    - type: precision_at_100
      value: 1.488
    - type: precision_at_1000
      value: 0.192
    - type: precision_at_3
      value: 22.272
    - type: precision_at_5
      value: 15.604999999999999
    - type: recall_at_1
      value: 32.0
    - type: recall_at_10
      value: 60.839
    - type: recall_at_100
      value: 78.869
    - type: recall_at_1000
      value: 89.384
    - type: recall_at_3
      value: 47.226
    - type: recall_at_5
      value: 52.864
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 44.084
    - type: map_at_10
      value: 56.591
    - type: map_at_100
      value: 57.533
    - type: map_at_1000
      value: 57.583
    - type: map_at_3
      value: 53.356
    - type: map_at_5
      value: 55.236
    - type: mrr_at_1
      value: 50.532999999999994
    - type: mrr_at_10
      value: 59.974000000000004
    - type: mrr_at_100
      value: 60.557
    - type: mrr_at_1000
      value: 60.584
    - type: mrr_at_3
      value: 57.774
    - type: mrr_at_5
      value: 59.063
    - type: ndcg_at_1
      value: 50.532999999999994
    - type: ndcg_at_10
      value: 62.265
    - type: ndcg_at_100
      value: 65.78
    - type: ndcg_at_1000
      value: 66.76299999999999
    - type: ndcg_at_3
      value: 57.154
    - type: ndcg_at_5
      value: 59.708000000000006
    - type: precision_at_1
      value: 50.532999999999994
    - type: precision_at_10
      value: 9.85
    - type: precision_at_100
      value: 1.247
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 25.434
    - type: precision_at_5
      value: 17.279
    - type: recall_at_1
      value: 44.084
    - type: recall_at_10
      value: 75.576
    - type: recall_at_100
      value: 90.524
    - type: recall_at_1000
      value: 97.38799999999999
    - type: recall_at_3
      value: 61.792
    - type: recall_at_5
      value: 68.112
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.203000000000003
    - type: map_at_10
      value: 38.078
    - type: map_at_100
      value: 39.144
    - type: map_at_1000
      value: 39.222
    - type: map_at_3
      value: 35.278999999999996
    - type: map_at_5
      value: 36.812
    - type: mrr_at_1
      value: 31.299
    - type: mrr_at_10
      value: 39.879
    - type: mrr_at_100
      value: 40.832
    - type: mrr_at_1000
      value: 40.891
    - type: mrr_at_3
      value: 37.513999999999996
    - type: mrr_at_5
      value: 38.802
    - type: ndcg_at_1
      value: 31.299
    - type: ndcg_at_10
      value: 43.047999999999995
    - type: ndcg_at_100
      value: 48.101
    - type: ndcg_at_1000
      value: 49.958999999999996
    - type: ndcg_at_3
      value: 37.778
    - type: ndcg_at_5
      value: 40.257
    - type: precision_at_1
      value: 31.299
    - type: precision_at_10
      value: 6.508
    - type: precision_at_100
      value: 0.9530000000000001
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_3
      value: 15.744
    - type: precision_at_5
      value: 10.893
    - type: recall_at_1
      value: 29.203000000000003
    - type: recall_at_10
      value: 56.552
    - type: recall_at_100
      value: 79.21000000000001
    - type: recall_at_1000
      value: 92.884
    - type: recall_at_3
      value: 42.441
    - type: recall_at_5
      value: 48.399
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.029
    - type: map_at_10
      value: 28.410000000000004
    - type: map_at_100
      value: 29.773
    - type: map_at_1000
      value: 29.887000000000004
    - type: map_at_3
      value: 25.374000000000002
    - type: map_at_5
      value: 27.162
    - type: mrr_at_1
      value: 23.632
    - type: mrr_at_10
      value: 33.0
    - type: mrr_at_100
      value: 34.043
    - type: mrr_at_1000
      value: 34.105999999999995
    - type: mrr_at_3
      value: 30.245
    - type: mrr_at_5
      value: 31.830000000000002
    - type: ndcg_at_1
      value: 23.632
    - type: ndcg_at_10
      value: 34.192
    - type: ndcg_at_100
      value: 40.29
    - type: ndcg_at_1000
      value: 42.753
    - type: ndcg_at_3
      value: 28.811999999999998
    - type: ndcg_at_5
      value: 31.46
    - type: precision_at_1
      value: 23.632
    - type: precision_at_10
      value: 6.455
    - type: precision_at_100
      value: 1.095
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 14.096
    - type: precision_at_5
      value: 10.448
    - type: recall_at_1
      value: 19.029
    - type: recall_at_10
      value: 47.278999999999996
    - type: recall_at_100
      value: 72.977
    - type: recall_at_1000
      value: 90.17699999999999
    - type: recall_at_3
      value: 32.519
    - type: recall_at_5
      value: 39.156
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.983
    - type: map_at_10
      value: 42.595
    - type: map_at_100
      value: 43.906
    - type: map_at_1000
      value: 44.001000000000005
    - type: map_at_3
      value: 39.245000000000005
    - type: map_at_5
      value: 41.14
    - type: mrr_at_1
      value: 38.114
    - type: mrr_at_10
      value: 48.181000000000004
    - type: mrr_at_100
      value: 48.935
    - type: mrr_at_1000
      value: 48.972
    - type: mrr_at_3
      value: 45.877
    - type: mrr_at_5
      value: 47.249
    - type: ndcg_at_1
      value: 38.114
    - type: ndcg_at_10
      value: 48.793
    - type: ndcg_at_100
      value: 54.001999999999995
    - type: ndcg_at_1000
      value: 55.749
    - type: ndcg_at_3
      value: 43.875
    - type: ndcg_at_5
      value: 46.23
    - type: precision_at_1
      value: 38.114
    - type: precision_at_10
      value: 8.98
    - type: precision_at_100
      value: 1.3390000000000002
    - type: precision_at_1000
      value: 0.166
    - type: precision_at_3
      value: 21.303
    - type: precision_at_5
      value: 15.072
    - type: recall_at_1
      value: 30.983
    - type: recall_at_10
      value: 61.47
    - type: recall_at_100
      value: 83.14399999999999
    - type: recall_at_1000
      value: 94.589
    - type: recall_at_3
      value: 47.019
    - type: recall_at_5
      value: 53.445
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.707
    - type: map_at_10
      value: 40.900999999999996
    - type: map_at_100
      value: 42.369
    - type: map_at_1000
      value: 42.455
    - type: map_at_3
      value: 37.416
    - type: map_at_5
      value: 39.483000000000004
    - type: mrr_at_1
      value: 36.301
    - type: mrr_at_10
      value: 46.046
    - type: mrr_at_100
      value: 46.922999999999995
    - type: mrr_at_1000
      value: 46.964
    - type: mrr_at_3
      value: 43.436
    - type: mrr_at_5
      value: 45.04
    - type: ndcg_at_1
      value: 36.301
    - type: ndcg_at_10
      value: 46.955999999999996
    - type: ndcg_at_100
      value: 52.712
    - type: ndcg_at_1000
      value: 54.447
    - type: ndcg_at_3
      value: 41.643
    - type: ndcg_at_5
      value: 44.305
    - type: precision_at_1
      value: 36.301
    - type: precision_at_10
      value: 8.607
    - type: precision_at_100
      value: 1.34
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 19.901
    - type: precision_at_5
      value: 14.429
    - type: recall_at_1
      value: 29.707
    - type: recall_at_10
      value: 59.559
    - type: recall_at_100
      value: 83.60499999999999
    - type: recall_at_1000
      value: 95.291
    - type: recall_at_3
      value: 44.774
    - type: recall_at_5
      value: 51.67
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.455416666666668
    - type: map_at_10
      value: 39.61333333333334
    - type: map_at_100
      value: 40.85875
    - type: map_at_1000
      value: 40.96791666666667
    - type: map_at_3
      value: 36.48874999999999
    - type: map_at_5
      value: 38.24341666666667
    - type: mrr_at_1
      value: 34.80258333333334
    - type: mrr_at_10
      value: 43.783
    - type: mrr_at_100
      value: 44.591833333333334
    - type: mrr_at_1000
      value: 44.64208333333333
    - type: mrr_at_3
      value: 41.38974999999999
    - type: mrr_at_5
      value: 42.74566666666667
    - type: ndcg_at_1
      value: 34.80258333333334
    - type: ndcg_at_10
      value: 45.2705
    - type: ndcg_at_100
      value: 50.31224999999999
    - type: ndcg_at_1000
      value: 52.27916666666667
    - type: ndcg_at_3
      value: 40.2745
    - type: ndcg_at_5
      value: 42.61575
    - type: precision_at_1
      value: 34.80258333333334
    - type: precision_at_10
      value: 7.97075
    - type: precision_at_100
      value: 1.2400000000000002
    - type: precision_at_1000
      value: 0.1595
    - type: precision_at_3
      value: 18.627583333333337
    - type: precision_at_5
      value: 13.207000000000003
    - type: recall_at_1
      value: 29.455416666666668
    - type: recall_at_10
      value: 57.66091666666665
    - type: recall_at_100
      value: 79.51966666666665
    - type: recall_at_1000
      value: 93.01883333333333
    - type: recall_at_3
      value: 43.580416666666665
    - type: recall_at_5
      value: 49.7025
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.569
    - type: map_at_10
      value: 34.73
    - type: map_at_100
      value: 35.708
    - type: map_at_1000
      value: 35.808
    - type: map_at_3
      value: 32.62
    - type: map_at_5
      value: 33.556999999999995
    - type: mrr_at_1
      value: 31.135
    - type: mrr_at_10
      value: 37.833
    - type: mrr_at_100
      value: 38.68
    - type: mrr_at_1000
      value: 38.749
    - type: mrr_at_3
      value: 35.915
    - type: mrr_at_5
      value: 36.751
    - type: ndcg_at_1
      value: 31.135
    - type: ndcg_at_10
      value: 39.047
    - type: ndcg_at_100
      value: 43.822
    - type: ndcg_at_1000
      value: 46.249
    - type: ndcg_at_3
      value: 35.115
    - type: ndcg_at_5
      value: 36.49
    - type: precision_at_1
      value: 31.135
    - type: precision_at_10
      value: 6.058
    - type: precision_at_100
      value: 0.923
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 15.031
    - type: precision_at_5
      value: 10.030999999999999
    - type: recall_at_1
      value: 27.569
    - type: recall_at_10
      value: 49.332
    - type: recall_at_100
      value: 70.967
    - type: recall_at_1000
      value: 88.876
    - type: recall_at_3
      value: 37.858999999999995
    - type: recall_at_5
      value: 41.589
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 19.677
    - type: map_at_10
      value: 28.097
    - type: map_at_100
      value: 29.24
    - type: map_at_1000
      value: 29.365000000000002
    - type: map_at_3
      value: 25.566
    - type: map_at_5
      value: 26.852999999999998
    - type: mrr_at_1
      value: 23.882
    - type: mrr_at_10
      value: 31.851000000000003
    - type: mrr_at_100
      value: 32.757
    - type: mrr_at_1000
      value: 32.83
    - type: mrr_at_3
      value: 29.485
    - type: mrr_at_5
      value: 30.744
    - type: ndcg_at_1
      value: 23.882
    - type: ndcg_at_10
      value: 33.154
    - type: ndcg_at_100
      value: 38.491
    - type: ndcg_at_1000
      value: 41.274
    - type: ndcg_at_3
      value: 28.648
    - type: ndcg_at_5
      value: 30.519000000000002
    - type: precision_at_1
      value: 23.882
    - type: precision_at_10
      value: 6.117999999999999
    - type: precision_at_100
      value: 1.0330000000000001
    - type: precision_at_1000
      value: 0.145
    - type: precision_at_3
      value: 13.73
    - type: precision_at_5
      value: 9.794
    - type: recall_at_1
      value: 19.677
    - type: recall_at_10
      value: 44.444
    - type: recall_at_100
      value: 68.477
    - type: recall_at_1000
      value: 88.23
    - type: recall_at_3
      value: 31.708
    - type: recall_at_5
      value: 36.599
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.489
    - type: map_at_10
      value: 40.883
    - type: map_at_100
      value: 42.058
    - type: map_at_1000
      value: 42.152
    - type: map_at_3
      value: 37.525999999999996
    - type: map_at_5
      value: 39.753
    - type: mrr_at_1
      value: 35.541
    - type: mrr_at_10
      value: 44.842999999999996
    - type: mrr_at_100
      value: 45.673
    - type: mrr_at_1000
      value: 45.723
    - type: mrr_at_3
      value: 42.397
    - type: mrr_at_5
      value: 43.937
    - type: ndcg_at_1
      value: 35.541
    - type: ndcg_at_10
      value: 46.504
    - type: ndcg_at_100
      value: 51.637
    - type: ndcg_at_1000
      value: 53.535
    - type: ndcg_at_3
      value: 41.127
    - type: ndcg_at_5
      value: 44.17
    - type: precision_at_1
      value: 35.541
    - type: precision_at_10
      value: 7.864
    - type: precision_at_100
      value: 1.165
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 18.688
    - type: precision_at_5
      value: 13.507
    - type: recall_at_1
      value: 30.489
    - type: recall_at_10
      value: 59.378
    - type: recall_at_100
      value: 81.38300000000001
    - type: recall_at_1000
      value: 94.294
    - type: recall_at_3
      value: 44.946000000000005
    - type: recall_at_5
      value: 52.644999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 29.981
    - type: map_at_10
      value: 39.688
    - type: map_at_100
      value: 41.400999999999996
    - type: map_at_1000
      value: 41.634
    - type: map_at_3
      value: 36.047000000000004
    - type: map_at_5
      value: 38.064
    - type: mrr_at_1
      value: 35.375
    - type: mrr_at_10
      value: 44.169000000000004
    - type: mrr_at_100
      value: 45.07
    - type: mrr_at_1000
      value: 45.113
    - type: mrr_at_3
      value: 41.502
    - type: mrr_at_5
      value: 43.034
    - type: ndcg_at_1
      value: 35.375
    - type: ndcg_at_10
      value: 45.959
    - type: ndcg_at_100
      value: 51.688
    - type: ndcg_at_1000
      value: 53.714
    - type: ndcg_at_3
      value: 40.457
    - type: ndcg_at_5
      value: 43.08
    - type: precision_at_1
      value: 35.375
    - type: precision_at_10
      value: 8.953
    - type: precision_at_100
      value: 1.709
    - type: precision_at_1000
      value: 0.253
    - type: precision_at_3
      value: 18.775
    - type: precision_at_5
      value: 14.032
    - type: recall_at_1
      value: 29.981
    - type: recall_at_10
      value: 57.896
    - type: recall_at_100
      value: 83.438
    - type: recall_at_1000
      value: 95.608
    - type: recall_at_3
      value: 42.327
    - type: recall_at_5
      value: 49.069
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.59
    - type: map_at_10
      value: 32.999
    - type: map_at_100
      value: 33.987
    - type: map_at_1000
      value: 34.085
    - type: map_at_3
      value: 30.013
    - type: map_at_5
      value: 31.673000000000002
    - type: mrr_at_1
      value: 26.802
    - type: mrr_at_10
      value: 35.167
    - type: mrr_at_100
      value: 36.001
    - type: mrr_at_1000
      value: 36.071999999999996
    - type: mrr_at_3
      value: 32.562999999999995
    - type: mrr_at_5
      value: 34.014
    - type: ndcg_at_1
      value: 26.802
    - type: ndcg_at_10
      value: 38.21
    - type: ndcg_at_100
      value: 43.086999999999996
    - type: ndcg_at_1000
      value: 45.509
    - type: ndcg_at_3
      value: 32.452999999999996
    - type: ndcg_at_5
      value: 35.191
    - type: precision_at_1
      value: 26.802
    - type: precision_at_10
      value: 5.989
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.125
    - type: precision_at_3
      value: 13.617
    - type: precision_at_5
      value: 9.797
    - type: recall_at_1
      value: 24.59
    - type: recall_at_10
      value: 52.298
    - type: recall_at_100
      value: 74.443
    - type: recall_at_1000
      value: 92.601
    - type: recall_at_3
      value: 36.888
    - type: recall_at_5
      value: 43.37
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 9.798
    - type: map_at_10
      value: 15.983
    - type: map_at_100
      value: 17.18
    - type: map_at_1000
      value: 17.329
    - type: map_at_3
      value: 13.594000000000001
    - type: map_at_5
      value: 14.984
    - type: mrr_at_1
      value: 21.564
    - type: mrr_at_10
      value: 31.415
    - type: mrr_at_100
      value: 32.317
    - type: mrr_at_1000
      value: 32.376
    - type: mrr_at_3
      value: 28.360000000000003
    - type: mrr_at_5
      value: 30.194
    - type: ndcg_at_1
      value: 21.564
    - type: ndcg_at_10
      value: 22.762
    - type: ndcg_at_100
      value: 28.199
    - type: ndcg_at_1000
      value: 31.284
    - type: ndcg_at_3
      value: 18.746
    - type: ndcg_at_5
      value: 20.434
    - type: precision_at_1
      value: 21.564
    - type: precision_at_10
      value: 6.755999999999999
    - type: precision_at_100
      value: 1.258
    - type: precision_at_1000
      value: 0.182
    - type: precision_at_3
      value: 13.507
    - type: precision_at_5
      value: 10.541
    - type: recall_at_1
      value: 9.798
    - type: recall_at_10
      value: 27.407999999999998
    - type: recall_at_100
      value: 46.659
    - type: recall_at_1000
      value: 64.132
    - type: recall_at_3
      value: 17.541999999999998
    - type: recall_at_5
      value: 22.137999999999998
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 8.276
    - type: map_at_10
      value: 18.003
    - type: map_at_100
      value: 23.759
    - type: map_at_1000
      value: 25.105
    - type: map_at_3
      value: 13.812
    - type: map_at_5
      value: 15.659999999999998
    - type: mrr_at_1
      value: 63.0
    - type: mrr_at_10
      value: 71.812
    - type: mrr_at_100
      value: 72.205
    - type: mrr_at_1000
      value: 72.21300000000001
    - type: mrr_at_3
      value: 70.375
    - type: mrr_at_5
      value: 71.188
    - type: ndcg_at_1
      value: 50.5
    - type: ndcg_at_10
      value: 36.954
    - type: ndcg_at_100
      value: 40.083999999999996
    - type: ndcg_at_1000
      value: 47.661
    - type: ndcg_at_3
      value: 42.666
    - type: ndcg_at_5
      value: 39.581
    - type: precision_at_1
      value: 63.0
    - type: precision_at_10
      value: 28.249999999999996
    - type: precision_at_100
      value: 8.113
    - type: precision_at_1000
      value: 1.7149999999999999
    - type: precision_at_3
      value: 47.083000000000006
    - type: precision_at_5
      value: 38.65
    - type: recall_at_1
      value: 8.276
    - type: recall_at_10
      value: 23.177
    - type: recall_at_100
      value: 45.321
    - type: recall_at_1000
      value: 68.742
    - type: recall_at_3
      value: 15.473
    - type: recall_at_5
      value: 18.276
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 55.605000000000004
    - type: f1
      value: 49.86208997523934
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 80.079
    - type: map_at_10
      value: 85.143
    - type: map_at_100
      value: 85.287
    - type: map_at_1000
      value: 85.297
    - type: map_at_3
      value: 84.533
    - type: map_at_5
      value: 84.953
    - type: mrr_at_1
      value: 86.424
    - type: mrr_at_10
      value: 91.145
    - type: mrr_at_100
      value: 91.212
    - type: mrr_at_1000
      value: 91.213
    - type: mrr_at_3
      value: 90.682
    - type: mrr_at_5
      value: 91.013
    - type: ndcg_at_1
      value: 86.424
    - type: ndcg_at_10
      value: 88.175
    - type: ndcg_at_100
      value: 88.77199999999999
    - type: ndcg_at_1000
      value: 88.967
    - type: ndcg_at_3
      value: 87.265
    - type: ndcg_at_5
      value: 87.813
    - type: precision_at_1
      value: 86.424
    - type: precision_at_10
      value: 10.012
    - type: precision_at_100
      value: 1.042
    - type: precision_at_1000
      value: 0.107
    - type: precision_at_3
      value: 32.228
    - type: precision_at_5
      value: 19.724
    - type: recall_at_1
      value: 80.079
    - type: recall_at_10
      value: 91.96600000000001
    - type: recall_at_100
      value: 94.541
    - type: recall_at_1000
      value: 95.824
    - type: recall_at_3
      value: 89.213
    - type: recall_at_5
      value: 90.791
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.006999999999998
    - type: map_at_10
      value: 36.923
    - type: map_at_100
      value: 38.932
    - type: map_at_1000
      value: 39.096
    - type: map_at_3
      value: 32.322
    - type: map_at_5
      value: 35.119
    - type: mrr_at_1
      value: 45.37
    - type: mrr_at_10
      value: 53.418
    - type: mrr_at_100
      value: 54.174
    - type: mrr_at_1000
      value: 54.20700000000001
    - type: mrr_at_3
      value: 51.132
    - type: mrr_at_5
      value: 52.451
    - type: ndcg_at_1
      value: 45.37
    - type: ndcg_at_10
      value: 44.799
    - type: ndcg_at_100
      value: 51.605000000000004
    - type: ndcg_at_1000
      value: 54.30500000000001
    - type: ndcg_at_3
      value: 41.33
    - type: ndcg_at_5
      value: 42.608000000000004
    - type: precision_at_1
      value: 45.37
    - type: precision_at_10
      value: 12.33
    - type: precision_at_100
      value: 1.9349999999999998
    - type: precision_at_1000
      value: 0.241
    - type: precision_at_3
      value: 27.828999999999997
    - type: precision_at_5
      value: 20.432
    - type: recall_at_1
      value: 23.006999999999998
    - type: recall_at_10
      value: 51.06699999999999
    - type: recall_at_100
      value: 75.917
    - type: recall_at_1000
      value: 92.331
    - type: recall_at_3
      value: 36.544
    - type: recall_at_5
      value: 43.449
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 38.196999999999996
    - type: map_at_10
      value: 55.554
    - type: map_at_100
      value: 56.309
    - type: map_at_1000
      value: 56.37799999999999
    - type: map_at_3
      value: 53.123
    - type: map_at_5
      value: 54.626
    - type: mrr_at_1
      value: 76.39399999999999
    - type: mrr_at_10
      value: 81.75
    - type: mrr_at_100
      value: 81.973
    - type: mrr_at_1000
      value: 81.982
    - type: mrr_at_3
      value: 80.79499999999999
    - type: mrr_at_5
      value: 81.393
    - type: ndcg_at_1
      value: 76.39399999999999
    - type: ndcg_at_10
      value: 64.14800000000001
    - type: ndcg_at_100
      value: 66.90899999999999
    - type: ndcg_at_1000
      value: 68.277
    - type: ndcg_at_3
      value: 60.529999999999994
    - type: ndcg_at_5
      value: 62.513
    - type: precision_at_1
      value: 76.39399999999999
    - type: precision_at_10
      value: 12.967999999999998
    - type: precision_at_100
      value: 1.5150000000000001
    - type: precision_at_1000
      value: 0.16999999999999998
    - type: precision_at_3
      value: 37.884
    - type: precision_at_5
      value: 24.294
    - type: recall_at_1
      value: 38.196999999999996
    - type: recall_at_10
      value: 64.84100000000001
    - type: recall_at_100
      value: 75.726
    - type: recall_at_1000
      value: 84.794
    - type: recall_at_3
      value: 56.826
    - type: recall_at_5
      value: 60.736000000000004
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 82.3912
    - type: ap
      value: 76.3949298163793
    - type: f1
      value: 82.30848699417406
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 19.454
    - type: map_at_10
      value: 31.22
    - type: map_at_100
      value: 32.475
    - type: map_at_1000
      value: 32.532
    - type: map_at_3
      value: 27.419
    - type: map_at_5
      value: 29.608
    - type: mrr_at_1
      value: 20.072000000000003
    - type: mrr_at_10
      value: 31.813999999999997
    - type: mrr_at_100
      value: 33.01
    - type: mrr_at_1000
      value: 33.062000000000005
    - type: mrr_at_3
      value: 28.055999999999997
    - type: mrr_at_5
      value: 30.218
    - type: ndcg_at_1
      value: 20.072000000000003
    - type: ndcg_at_10
      value: 38.0
    - type: ndcg_at_100
      value: 44.038
    - type: ndcg_at_1000
      value: 45.43
    - type: ndcg_at_3
      value: 30.219
    - type: ndcg_at_5
      value: 34.127
    - type: precision_at_1
      value: 20.072000000000003
    - type: precision_at_10
      value: 6.159
    - type: precision_at_100
      value: 0.9169999999999999
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 13.071
    - type: precision_at_5
      value: 9.814
    - type: recall_at_1
      value: 19.454
    - type: recall_at_10
      value: 58.931
    - type: recall_at_100
      value: 86.886
    - type: recall_at_1000
      value: 97.425
    - type: recall_at_3
      value: 37.697
    - type: recall_at_5
      value: 47.101
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 90.46283629730961
    - type: f1
      value: 90.22448402668293
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (de)
      config: de
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 86.91462383770076
    - type: f1
      value: 85.77767304705436
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (es)
      config: es
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 87.73849232821881
    - type: f1
      value: 87.33680109229385
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (fr)
      config: fr
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 86.22298778578141
    - type: f1
      value: 85.88868176519013
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (hi)
      config: hi
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 82.91860882036572
    - type: f1
      value: 81.38044567838352
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (th)
      config: th
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 69.90235081374323
    - type: f1
      value: 68.12897827044782
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 66.0031919744642
    - type: f1
      value: 48.13490278120492
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (de)
      config: de
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 63.260073260073256
    - type: f1
      value: 42.627167415555505
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (es)
      config: es
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 65.06004002668445
    - type: f1
      value: 44.90527231209402
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (fr)
      config: fr
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 59.42687128092702
    - type: f1
      value: 41.79584710899656
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (hi)
      config: hi
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 59.078522768017216
    - type: f1
      value: 40.398016878580734
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (th)
      config: th
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 43.750452079565996
    - type: f1
      value: 28.985320742729865
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (af)
      config: af
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 47.59919300605245
    - type: f1
      value: 44.27505749600044
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (am)
      config: am
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 31.56691324815064
    - type: f1
      value: 30.34952276390722
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ar)
      config: ar
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 52.62945527908541
    - type: f1
      value: 49.689536347222386
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (az)
      config: az
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 50.0941492938803
    - type: f1
      value: 48.47831879848094
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (bn)
      config: bn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 46.540013449899135
    - type: f1
      value: 44.25663324630171
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (cy)
      config: cy
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 44.25689307330195
    - type: f1
      value: 42.06066077477426
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (da)
      config: da
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 55.05716207128446
    - type: f1
      value: 52.41516089202158
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (de)
      config: de
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 61.86953597848015
    - type: f1
      value: 58.45989820228606
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (el)
      config: el
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 47.02084734364493
    - type: f1
      value: 45.21525882986924
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 69.24008069939475
    - type: f1
      value: 68.27971089998472
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (es)
      config: es
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 62.53530598520511
    - type: f1
      value: 61.83588971206536
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fa)
      config: fa
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 55.19166106254204
    - type: f1
      value: 52.335787325774
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fi)
      config: fi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 48.43308675184936
    - type: f1
      value: 45.841102061239184
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (fr)
      config: fr
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 64.26698049764627
    - type: f1
      value: 62.25607481996241
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (he)
      config: he
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 57.619367854741085
    - type: f1
      value: 54.93671211092237
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hi)
      config: hi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 57.53530598520511
    - type: f1
      value: 55.36413211751344
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hu)
      config: hu
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 45.66913248150638
    - type: f1
      value: 42.52092657926257
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (hy)
      config: hy
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 39.19973100201749
    - type: f1
      value: 37.194613407773566
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (id)
      config: id
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 54.99663752521856
    - type: f1
      value: 53.875181150315356
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (is)
      config: is
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 43.143913920645595
    - type: f1
      value: 41.756257561394456
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (it)
      config: it
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 60.99529253530599
    - type: f1
      value: 59.103812128183705
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ja)
      config: ja
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 64.29051782111634
    - type: f1
      value: 62.5268914542489
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (jv)
      config: jv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 43.69199731002017
    - type: f1
      value: 41.71651113018154
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ka)
      config: ka
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 38.34566240753194
    - type: f1
      value: 36.935911015227894
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (km)
      config: km
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 34.21654337592467
    - type: f1
      value: 32.067289455027755
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (kn)
      config: kn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 51.785474108944186
    - type: f1
      value: 49.29285691779668
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ko)
      config: ko
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 59.58977807666444
    - type: f1
      value: 57.81630371862734
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (lv)
      config: lv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 46.53665097511768
    - type: f1
      value: 44.8386852929464
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ml)
      config: ml
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 54.468728984532625
    - type: f1
      value: 52.13613631138983
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (mn)
      config: mn
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 40.67921990585071
    - type: f1
      value: 39.87218130311539
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ms)
      config: ms
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 51.2441156691325
    - type: f1
      value: 48.93351041227674
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (my)
      config: my
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 31.76193678547411
    - type: f1
      value: 29.917012787908785
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nb)
      config: nb
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 54.40820443846671
    - type: f1
      value: 51.232049156874396
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (nl)
      config: nl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 60.8170813718897
    - type: f1
      value: 57.74887572270486
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pl)
      config: pl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 60.067249495628786
    - type: f1
      value: 57.60151669462318
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (pt)
      config: pt
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 62.73705447209146
    - type: f1
      value: 61.14377989075874
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ro)
      config: ro
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 49.68392737054472
    - type: f1
      value: 48.07062918679129
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ru)
      config: ru
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 60.85406859448555
    - type: f1
      value: 58.48852652838252
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sl)
      config: sl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 48.58776059179556
    - type: f1
      value: 46.92163099241966
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sq)
      config: sq
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 47.16879623402824
    - type: f1
      value: 45.8155066134247
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sv)
      config: sv
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 62.41425689307329
    - type: f1
      value: 60.097954878192574
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (sw)
      config: sw
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 45.97175521183591
    - type: f1
      value: 44.29275283000346
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ta)
      config: ta
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 53.597848016139885
    - type: f1
      value: 51.54318966923094
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (te)
      config: te
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 53.44653665097512
    - type: f1
      value: 51.60095623356469
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (th)
      config: th
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 46.173503698722264
    - type: f1
      value: 46.311285276929105
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tl)
      config: tl
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 49.47881640887693
    - type: f1
      value: 46.63989802589145
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (tr)
      config: tr
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 58.02958977807666
    - type: f1
      value: 55.34728796730868
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (ur)
      config: ur
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 39.26361802286483
    - type: f1
      value: 37.61201358829197
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (vi)
      config: vi
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 52.15534633490249
    - type: f1
      value: 50.438951980623145
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 63.39946200403498
    - type: f1
      value: 62.152249150179664
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 58.207800941492934
    - type: f1
      value: 58.318584465398104
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (af)
      config: af
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 58.069939475453936
    - type: f1
      value: 55.04073616892449
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (am)
      config: am
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 38.214525891055814
    - type: f1
      value: 36.42184260742777
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ar)
      config: ar
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.47141896435777
    - type: f1
      value: 57.22453431938479
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (az)
      config: az
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 54.37121721587089
    - type: f1
      value: 53.004976087120134
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (bn)
      config: bn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.71687962340283
    - type: f1
      value: 51.140151342341646
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (cy)
      config: cy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 49.502353732347004
    - type: f1
      value: 45.74604753969847
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (da)
      config: da
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.25689307330195
    - type: f1
      value: 62.25355539317913
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (de)
      config: de
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 71.27774041694688
    - type: f1
      value: 70.26880477280841
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (el)
      config: el
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.420981842636195
    - type: f1
      value: 50.824547366213565
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 74.11230665770006
    - type: f1
      value: 73.00723710263364
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (es)
      config: es
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 67.04102219233356
    - type: f1
      value: 66.7904194512351
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fa)
      config: fa
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 60.1714862138534
    - type: f1
      value: 58.781208933846095
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fi)
      config: fi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 54.04841963685272
    - type: f1
      value: 51.185007148328545
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (fr)
      config: fr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.76462676529927
    - type: f1
      value: 68.85227238388136
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (he)
      config: he
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 62.84801613987895
    - type: f1
      value: 61.18395865529196
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hi)
      config: hi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 62.17888365837256
    - type: f1
      value: 60.40570575783401
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hu)
      config: hu
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 53.52051109616678
    - type: f1
      value: 51.210696278552014
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (hy)
      config: hy
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 45.94821788836584
    - type: f1
      value: 43.65062337089374
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (id)
      config: id
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 60.33288500336248
    - type: f1
      value: 59.50436947982156
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (is)
      config: is
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 50.09751176866174
    - type: f1
      value: 47.293838685239
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (it)
      config: it
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 66.49293880295897
    - type: f1
      value: 65.96586462307134
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ja)
      config: ja
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 68.35911230665769
    - type: f1
      value: 67.77840431764355
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (jv)
      config: jv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 50.585070611970416
    - type: f1
      value: 47.957277125670295
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ka)
      config: ka
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 42.76059179556153
    - type: f1
      value: 40.446327361325565
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (km)
      config: km
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 40.648957632817755
    - type: f1
      value: 37.231284508608276
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (kn)
      config: kn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.24613315400134
    - type: f1
      value: 55.14523425690653
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ko)
      config: ko
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 63.839946200403496
    - type: f1
      value: 62.6239063060589
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (lv)
      config: lv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 53.14391392064559
    - type: f1
      value: 50.08744471966442
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ml)
      config: ml
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 58.8399462004035
    - type: f1
      value: 57.586991117740794
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (mn)
      config: mn
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 44.81842636180229
    - type: f1
      value: 42.82813975084655
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ms)
      config: ms
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 58.90047074646939
    - type: f1
      value: 56.640503134745714
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (my)
      config: my
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 38.52051109616678
    - type: f1
      value: 36.504553927569454
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nb)
      config: nb
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.63685272360458
    - type: f1
      value: 62.88129994502907
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (nl)
      config: nl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 67.54203093476798
    - type: f1
      value: 66.02745142287087
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pl)
      config: pl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.00470746469402
    - type: f1
      value: 62.91845058355313
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (pt)
      config: pt
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 65.69939475453934
    - type: f1
      value: 65.37413822081011
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ro)
      config: ro
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.19905850706121
    - type: f1
      value: 55.08271383695852
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ru)
      config: ru
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 65.42367182246134
    - type: f1
      value: 64.61962307022019
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sl)
      config: sl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 55.147948890383326
    - type: f1
      value: 53.2933851469903
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sq)
      config: sq
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 55.679219905850715
    - type: f1
      value: 52.80159603468007
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sv)
      config: sv
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.42165433759246
    - type: f1
      value: 67.99984081248608
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (sw)
      config: sw
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.30329522528581
    - type: f1
      value: 50.10810382364662
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ta)
      config: ta
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 56.186953597848024
    - type: f1
      value: 55.51656586643505
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (te)
      config: te
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 58.019502353732356
    - type: f1
      value: 56.260726586358736
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (th)
      config: th
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 52.55548083389374
    - type: f1
      value: 51.139712264362714
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tl)
      config: tl
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 57.43443174176194
    - type: f1
      value: 55.76244076715635
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (tr)
      config: tr
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 61.55346334902488
    - type: f1
      value: 61.25819823057803
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (ur)
      config: ur
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 47.114996637525216
    - type: f1
      value: 45.20428169546973
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (vi)
      config: vi
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 56.83254875588434
    - type: f1
      value: 56.00919757601416
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 69.57969065232012
    - type: f1
      value: 69.17378512156806
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-TW)
      config: zh-TW
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 64.02488231338263
    - type: f1
      value: 64.09790488949963
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 29.71446786877363
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 28.003624498407547
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 31.29671894458151
    - type: mrr
      value: 32.44455140124599
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 6.127
    - type: map_at_10
      value: 13.047
    - type: map_at_100
      value: 15.754000000000001
    - type: map_at_1000
      value: 16.930999999999997
    - type: map_at_3
      value: 9.876999999999999
    - type: map_at_5
      value: 11.265
    - type: mrr_at_1
      value: 45.511
    - type: mrr_at_10
      value: 54.75600000000001
    - type: mrr_at_100
      value: 55.33
    - type: mrr_at_1000
      value: 55.374
    - type: mrr_at_3
      value: 53.147999999999996
    - type: mrr_at_5
      value: 53.952999999999996
    - type: ndcg_at_1
      value: 43.653
    - type: ndcg_at_10
      value: 33.936
    - type: ndcg_at_100
      value: 29.952
    - type: ndcg_at_1000
      value: 38.356
    - type: ndcg_at_3
      value: 40.018
    - type: ndcg_at_5
      value: 37.102000000000004
    - type: precision_at_1
      value: 45.511
    - type: precision_at_10
      value: 24.768
    - type: precision_at_100
      value: 7.13
    - type: precision_at_1000
      value: 1.928
    - type: precision_at_3
      value: 37.461
    - type: precision_at_5
      value: 31.703
    - type: recall_at_1
      value: 6.127
    - type: recall_at_10
      value: 16.512999999999998
    - type: recall_at_100
      value: 29.057
    - type: recall_at_1000
      value: 59.25899999999999
    - type: recall_at_3
      value: 10.940999999999999
    - type: recall_at_5
      value: 12.925
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.228
    - type: map_at_10
      value: 47.56
    - type: map_at_100
      value: 48.539
    - type: map_at_1000
      value: 48.567
    - type: map_at_3
      value: 43.214999999999996
    - type: map_at_5
      value: 45.799
    - type: mrr_at_1
      value: 36.53
    - type: mrr_at_10
      value: 50.004000000000005
    - type: mrr_at_100
      value: 50.737
    - type: mrr_at_1000
      value: 50.758
    - type: mrr_at_3
      value: 46.543
    - type: mrr_at_5
      value: 48.672
    - type: ndcg_at_1
      value: 36.501
    - type: ndcg_at_10
      value: 55.103
    - type: ndcg_at_100
      value: 59.156
    - type: ndcg_at_1000
      value: 59.821999999999996
    - type: ndcg_at_3
      value: 47.089
    - type: ndcg_at_5
      value: 51.35999999999999
    - type: precision_at_1
      value: 36.501
    - type: precision_at_10
      value: 9.046999999999999
    - type: precision_at_100
      value: 1.13
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 21.398
    - type: precision_at_5
      value: 15.307
    - type: recall_at_1
      value: 32.228
    - type: recall_at_10
      value: 75.608
    - type: recall_at_100
      value: 93.062
    - type: recall_at_1000
      value: 98.059
    - type: recall_at_3
      value: 55.021
    - type: recall_at_5
      value: 64.873
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.623
    - type: map_at_10
      value: 84.705
    - type: map_at_100
      value: 85.333
    - type: map_at_1000
      value: 85.348
    - type: map_at_3
      value: 81.736
    - type: map_at_5
      value: 83.616
    - type: mrr_at_1
      value: 81.28
    - type: mrr_at_10
      value: 87.518
    - type: mrr_at_100
      value: 87.619
    - type: mrr_at_1000
      value: 87.62
    - type: mrr_at_3
      value: 86.545
    - type: mrr_at_5
      value: 87.238
    - type: ndcg_at_1
      value: 81.28999999999999
    - type: ndcg_at_10
      value: 88.412
    - type: ndcg_at_100
      value: 89.603
    - type: ndcg_at_1000
      value: 89.696
    - type: ndcg_at_3
      value: 85.563
    - type: ndcg_at_5
      value: 87.17
    - type: precision_at_1
      value: 81.28999999999999
    - type: precision_at_10
      value: 13.439
    - type: precision_at_100
      value: 1.5310000000000001
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.437
    - type: precision_at_5
      value: 24.662
    - type: recall_at_1
      value: 70.623
    - type: recall_at_10
      value: 95.531
    - type: recall_at_100
      value: 99.58
    - type: recall_at_1000
      value: 99.978
    - type: recall_at_3
      value: 87.368
    - type: recall_at_5
      value: 91.898
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 49.53241309124786
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 59.712004482915994
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 5.313
    - type: map_at_10
      value: 13.447000000000001
    - type: map_at_100
      value: 15.491
    - type: map_at_1000
      value: 15.784999999999998
    - type: map_at_3
      value: 9.58
    - type: map_at_5
      value: 11.562
    - type: mrr_at_1
      value: 26.200000000000003
    - type: mrr_at_10
      value: 37.212
    - type: mrr_at_100
      value: 38.190000000000005
    - type: mrr_at_1000
      value: 38.242
    - type: mrr_at_3
      value: 34.067
    - type: mrr_at_5
      value: 35.862
    - type: ndcg_at_1
      value: 26.200000000000003
    - type: ndcg_at_10
      value: 21.979000000000003
    - type: ndcg_at_100
      value: 29.726999999999997
    - type: ndcg_at_1000
      value: 34.766000000000005
    - type: ndcg_at_3
      value: 21.16
    - type: ndcg_at_5
      value: 18.478
    - type: precision_at_1
      value: 26.200000000000003
    - type: precision_at_10
      value: 11.25
    - type: precision_at_100
      value: 2.241
    - type: precision_at_1000
      value: 0.345
    - type: precision_at_3
      value: 19.633
    - type: precision_at_5
      value: 16.14
    - type: recall_at_1
      value: 5.313
    - type: recall_at_10
      value: 22.808
    - type: recall_at_100
      value: 45.540000000000006
    - type: recall_at_1000
      value: 70.043
    - type: recall_at_3
      value: 11.932
    - type: recall_at_5
      value: 16.347
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 75.95540796619258
    - type: cos_sim_spearman
      value: 76.49462277620303
    - type: euclidean_pearson
      value: 71.67643435507317
    - type: euclidean_spearman
      value: 76.4915921108082
    - type: manhattan_pearson
      value: 71.71412560074847
    - type: manhattan_spearman
      value: 76.46738312094736
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 81.48773267615617
    - type: cos_sim_spearman
      value: 74.99867664033701
    - type: euclidean_pearson
      value: 76.0885798115032
    - type: euclidean_spearman
      value: 74.99438208715942
    - type: manhattan_pearson
      value: 76.09382557464033
    - type: manhattan_spearman
      value: 74.96139353538533
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 88.19022560804167
    - type: cos_sim_spearman
      value: 87.9128142106699
    - type: euclidean_pearson
      value: 85.51390183763914
    - type: euclidean_spearman
      value: 87.89995488057309
    - type: manhattan_pearson
      value: 85.44945034816052
    - type: manhattan_spearman
      value: 87.791458898378
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 85.17877898640924
    - type: cos_sim_spearman
      value: 82.25544088807465
    - type: euclidean_pearson
      value: 82.36395988835416
    - type: euclidean_spearman
      value: 82.26359924974219
    - type: manhattan_pearson
      value: 82.39219808999891
    - type: manhattan_spearman
      value: 82.27757404868157
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 87.66865350602554
    - type: cos_sim_spearman
      value: 87.87150169810872
    - type: euclidean_pearson
      value: 85.41520650056647
    - type: euclidean_spearman
      value: 87.86636613654022
    - type: manhattan_pearson
      value: 85.38710485867502
    - type: manhattan_spearman
      value: 87.83513424575301
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 80.75527643407175
    - type: cos_sim_spearman
      value: 80.9239008594745
    - type: euclidean_pearson
      value: 79.37682746800515
    - type: euclidean_spearman
      value: 80.91978947194092
    - type: manhattan_pearson
      value: 79.38884189990698
    - type: manhattan_spearman
      value: 80.91771608341014
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ko-ko)
      config: ko-ko
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 80.24344311909609
    - type: cos_sim_spearman
      value: 80.78933956176022
    - type: euclidean_pearson
      value: 76.95229806538676
    - type: euclidean_spearman
      value: 80.79706724032172
    - type: manhattan_pearson
      value: 76.90212135774246
    - type: manhattan_spearman
      value: 80.68727415384441
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (ar-ar)
      config: ar-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 77.33891809228084
    - type: cos_sim_spearman
      value: 79.37912430317627
    - type: euclidean_pearson
      value: 72.56919843951036
    - type: euclidean_spearman
      value: 79.3091436905072
    - type: manhattan_pearson
      value: 72.4282811588754
    - type: manhattan_spearman
      value: 78.90144894538078
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-ar)
      config: en-ar
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 59.68908656739356
    - type: cos_sim_spearman
      value: 58.76110210983758
    - type: euclidean_pearson
      value: 59.14749159577439
    - type: euclidean_spearman
      value: 59.015997032145016
    - type: manhattan_pearson
      value: 57.907675340322676
    - type: manhattan_spearman
      value: 57.07751173022352
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-de)
      config: en-de
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 75.53325164873934
    - type: cos_sim_spearman
      value: 76.13104388846271
    - type: euclidean_pearson
      value: 74.61931031522006
    - type: euclidean_spearman
      value: 75.96875166459931
    - type: manhattan_pearson
      value: 74.82154350849251
    - type: manhattan_spearman
      value: 76.64455924104236
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 85.4228376590724
    - type: cos_sim_spearman
      value: 87.22764976624408
    - type: euclidean_pearson
      value: 81.94975688107507
    - type: euclidean_spearman
      value: 87.19193932664932
    - type: manhattan_pearson
      value: 82.0043964628936
    - type: manhattan_spearman
      value: 87.09130430957818
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-tr)
      config: en-tr
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 57.5627552601949
    - type: cos_sim_spearman
      value: 55.5263144563657
    - type: euclidean_pearson
      value: 57.00569241610482
    - type: euclidean_spearman
      value: 55.35291811479459
    - type: manhattan_pearson
      value: 56.99656284623506
    - type: manhattan_spearman
      value: 55.593673744709946
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-en)
      config: es-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 69.93801311909735
    - type: cos_sim_spearman
      value: 72.2581115470475
    - type: euclidean_pearson
      value: 68.24881290268563
    - type: euclidean_spearman
      value: 72.60813652864522
    - type: manhattan_pearson
      value: 67.86369874088834
    - type: manhattan_spearman
      value: 71.92346382988023
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (es-es)
      config: es-es
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 86.20555264114785
    - type: cos_sim_spearman
      value: 85.0588060013836
    - type: euclidean_pearson
      value: 81.78229090166155
    - type: euclidean_spearman
      value: 85.09687374900614
    - type: manhattan_pearson
      value: 81.77449099980244
    - type: manhattan_spearman
      value: 84.70331476222177
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (fr-en)
      config: fr-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 73.786793911605
    - type: cos_sim_spearman
      value: 75.63094397551554
    - type: euclidean_pearson
      value: 71.64292842519251
    - type: euclidean_spearman
      value: 75.60215267384011
    - type: manhattan_pearson
      value: 72.2124078037642
    - type: manhattan_spearman
      value: 76.34546028465175
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (it-en)
      config: it-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 69.62139987106455
    - type: cos_sim_spearman
      value: 71.35872226722493
    - type: euclidean_pearson
      value: 68.50103697766141
    - type: euclidean_spearman
      value: 71.24590187948473
    - type: manhattan_pearson
      value: 68.89236562525663
    - type: manhattan_spearman
      value: 71.77994400789173
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (nl-en)
      config: nl-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 71.62728174871292
    - type: cos_sim_spearman
      value: 71.98655715409397
    - type: euclidean_pearson
      value: 70.27026741609356
    - type: euclidean_spearman
      value: 72.14004669693777
    - type: manhattan_pearson
      value: 70.46335140108751
    - type: manhattan_spearman
      value: 72.6638254374311
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 71.10248717637424
    - type: cos_sim_spearman
      value: 68.5905931564714
    - type: euclidean_pearson
      value: 71.23290000423759
    - type: euclidean_spearman
      value: 68.6419513130457
    - type: manhattan_pearson
      value: 71.6886015250234
    - type: manhattan_spearman
      value: 69.47543660368697
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de)
      config: de
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 59.010555056244776
    - type: cos_sim_spearman
      value: 60.121771179899255
    - type: euclidean_pearson
      value: 53.04527785573465
    - type: euclidean_spearman
      value: 60.121771179899255
    - type: manhattan_pearson
      value: 52.931480071124234
    - type: manhattan_spearman
      value: 60.03868409331775
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es)
      config: es
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 70.6833028374664
    - type: cos_sim_spearman
      value: 68.57396263856863
    - type: euclidean_pearson
      value: 68.30905084522986
    - type: euclidean_spearman
      value: 68.57396263856863
    - type: manhattan_pearson
      value: 70.91400657516918
    - type: manhattan_spearman
      value: 72.72240857808112
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl)
      config: pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 36.948290734279645
    - type: cos_sim_spearman
      value: 42.07722031011005
    - type: euclidean_pearson
      value: 22.539446972018467
    - type: euclidean_spearman
      value: 42.07722031011005
    - type: manhattan_pearson
      value: 24.119402246951786
    - type: manhattan_spearman
      value: 45.80525501822569
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (tr)
      config: tr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 66.97840719036533
    - type: cos_sim_spearman
      value: 66.62430648804775
    - type: euclidean_pearson
      value: 66.89526587772023
    - type: euclidean_spearman
      value: 66.62430648804775
    - type: manhattan_pearson
      value: 68.6929895225091
    - type: manhattan_spearman
      value: 68.91772708432867
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ar)
      config: ar
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 56.65098289103698
    - type: cos_sim_spearman
      value: 57.436674670689214
    - type: euclidean_pearson
      value: 51.79149892785239
    - type: euclidean_spearman
      value: 57.436674670689214
    - type: manhattan_pearson
      value: 52.64807953938707
    - type: manhattan_spearman
      value: 58.94583987372767
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (ru)
      config: ru
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 60.669531297510225
    - type: cos_sim_spearman
      value: 61.71342510003327
    - type: euclidean_pearson
      value: 55.821871433553504
    - type: euclidean_spearman
      value: 61.71342510003327
    - type: manhattan_pearson
      value: 57.77073441351117
    - type: manhattan_spearman
      value: 65.20759033207
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 64.34728960310699
    - type: cos_sim_spearman
      value: 64.03565302589584
    - type: euclidean_pearson
      value: 61.958942333930544
    - type: euclidean_spearman
      value: 64.03565302589584
    - type: manhattan_pearson
      value: 64.65072672727923
    - type: manhattan_spearman
      value: 67.82569969943107
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr)
      config: fr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 82.47120815594353
    - type: cos_sim_spearman
      value: 81.46916544955101
    - type: euclidean_pearson
      value: 79.21753533489019
    - type: euclidean_spearman
      value: 81.46916544955101
    - type: manhattan_pearson
      value: 78.26605518839271
    - type: manhattan_spearman
      value: 81.29749169339514
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-en)
      config: de-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 63.31467231933632
    - type: cos_sim_spearman
      value: 53.36160506603274
    - type: euclidean_pearson
      value: 64.98434169416196
    - type: euclidean_spearman
      value: 53.36160506603274
    - type: manhattan_pearson
      value: 69.6837006629638
    - type: manhattan_spearman
      value: 60.85384324700893
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-en)
      config: es-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 79.99425127770438
    - type: cos_sim_spearman
      value: 77.41308957007035
    - type: euclidean_pearson
      value: 79.69441265626801
    - type: euclidean_spearman
      value: 77.41308957007035
    - type: manhattan_pearson
      value: 80.3726291667624
    - type: manhattan_spearman
      value: 79.0414050644631
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (it)
      config: it
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 79.13469287716659
    - type: cos_sim_spearman
      value: 79.27976881582065
    - type: euclidean_pearson
      value: 77.65964425780172
    - type: euclidean_spearman
      value: 79.27976881582065
    - type: manhattan_pearson
      value: 77.64158710257945
    - type: manhattan_spearman
      value: 79.22242281895944
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (pl-en)
      config: pl-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 76.303314995599
    - type: cos_sim_spearman
      value: 77.4991345414335
    - type: euclidean_pearson
      value: 74.88826621426401
    - type: euclidean_spearman
      value: 77.4991345414335
    - type: manhattan_pearson
      value: 77.70223488989319
    - type: manhattan_spearman
      value: 79.69746987627822
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh-en)
      config: zh-en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 70.87814957197239
    - type: cos_sim_spearman
      value: 69.86785751801642
    - type: euclidean_pearson
      value: 68.68630146548654
    - type: euclidean_spearman
      value: 69.8615799070054
    - type: manhattan_pearson
      value: 61.83743315022061
    - type: manhattan_spearman
      value: 64.35346450347738
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (es-it)
      config: es-it
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 74.1484689923211
    - type: cos_sim_spearman
      value: 74.69046355179742
    - type: euclidean_pearson
      value: 73.03951899271793
    - type: euclidean_spearman
      value: 74.69820632954205
    - type: manhattan_pearson
      value: 73.36810146930709
    - type: manhattan_spearman
      value: 75.33154135287258
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-fr)
      config: de-fr
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 51.43125921362742
    - type: cos_sim_spearman
      value: 58.25341239774093
    - type: euclidean_pearson
      value: 48.00689582162098
    - type: euclidean_spearman
      value: 58.533194841668426
    - type: manhattan_pearson
      value: 46.11721778230745
    - type: manhattan_spearman
      value: 55.026889052448134
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (de-pl)
      config: de-pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 40.066205533538046
    - type: cos_sim_spearman
      value: 48.46991890841381
    - type: euclidean_pearson
      value: 42.29606506858651
    - type: euclidean_spearman
      value: 48.34674249441531
    - type: manhattan_pearson
      value: 41.70680990555484
    - type: manhattan_spearman
      value: 47.54609580342499
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (fr-pl)
      config: fr-pl
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 82.26527545520592
    - type: cos_sim_spearman
      value: 73.24670207647144
    - type: euclidean_pearson
      value: 81.78699781584893
    - type: euclidean_spearman
      value: 73.24670207647144
    - type: manhattan_pearson
      value: 83.14172292187807
    - type: manhattan_spearman
      value: 73.24670207647144
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 81.51438108053523
    - type: cos_sim_spearman
      value: 81.9481311864648
    - type: euclidean_pearson
      value: 78.6683040592179
    - type: euclidean_spearman
      value: 81.9535649926177
    - type: manhattan_pearson
      value: 78.65396325536754
    - type: manhattan_spearman
      value: 81.96918240343872
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 80.6689275068653
    - type: mrr
      value: 95.021337594867
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 55.193999999999996
    - type: map_at_10
      value: 65.814
    - type: map_at_100
      value: 66.428
    - type: map_at_1000
      value: 66.447
    - type: map_at_3
      value: 63.304
    - type: map_at_5
      value: 64.64
    - type: mrr_at_1
      value: 57.99999999999999
    - type: mrr_at_10
      value: 66.957
    - type: mrr_at_100
      value: 67.405
    - type: mrr_at_1000
      value: 67.422
    - type: mrr_at_3
      value: 65.0
    - type: mrr_at_5
      value: 66.183
    - type: ndcg_at_1
      value: 57.99999999999999
    - type: ndcg_at_10
      value: 70.523
    - type: ndcg_at_100
      value: 72.987
    - type: ndcg_at_1000
      value: 73.605
    - type: ndcg_at_3
      value: 66.268
    - type: ndcg_at_5
      value: 68.27600000000001
    - type: precision_at_1
      value: 57.99999999999999
    - type: precision_at_10
      value: 9.467
    - type: precision_at_100
      value: 1.073
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 26.444000000000003
    - type: precision_at_5
      value: 17.2
    - type: recall_at_1
      value: 55.193999999999996
    - type: recall_at_10
      value: 83.52199999999999
    - type: recall_at_100
      value: 94.5
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_3
      value: 71.989
    - type: recall_at_5
      value: 77.31700000000001
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.73465346534654
    - type: cos_sim_ap
      value: 92.91719494015508
    - type: cos_sim_f1
      value: 86.46200301962756
    - type: cos_sim_precision
      value: 87.03140830800406
    - type: cos_sim_recall
      value: 85.9
    - type: dot_accuracy
      value: 99.73663366336633
    - type: dot_ap
      value: 92.90802848215259
    - type: dot_f1
      value: 86.46200301962756
    - type: dot_precision
      value: 87.03140830800406
    - type: dot_recall
      value: 85.9
    - type: euclidean_accuracy
      value: 99.73465346534654
    - type: euclidean_ap
      value: 92.91627363446204
    - type: euclidean_f1
      value: 86.43469490670702
    - type: euclidean_precision
      value: 87.18209562563581
    - type: euclidean_recall
      value: 85.7
    - type: manhattan_accuracy
      value: 99.73663366336633
    - type: manhattan_ap
      value: 92.90219877406929
    - type: manhattan_f1
      value: 86.31471040492056
    - type: manhattan_precision
      value: 88.53838065194533
    - type: manhattan_recall
      value: 84.2
    - type: max_accuracy
      value: 99.73663366336633
    - type: max_ap
      value: 92.91719494015508
    - type: max_f1
      value: 86.46200301962756
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 60.73098998430779
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 34.64256206757585
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 54.749150614295694
    - type: mrr
      value: 55.78880984211867
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 28.863577054305907
    - type: cos_sim_spearman
      value: 27.538596944829774
    - type: dot_pearson
      value: 28.93043755116643
    - type: dot_spearman
      value: 27.733110516733987
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.22899999999999998
    - type: map_at_10
      value: 2.078
    - type: map_at_100
      value: 12.024
    - type: map_at_1000
      value: 29.036
    - type: map_at_3
      value: 0.681
    - type: map_at_5
      value: 1.083
    - type: mrr_at_1
      value: 86.0
    - type: mrr_at_10
      value: 92.667
    - type: mrr_at_100
      value: 92.667
    - type: mrr_at_1000
      value: 92.667
    - type: mrr_at_3
      value: 92.667
    - type: mrr_at_5
      value: 92.667
    - type: ndcg_at_1
      value: 82.0
    - type: ndcg_at_10
      value: 80.746
    - type: ndcg_at_100
      value: 61.090999999999994
    - type: ndcg_at_1000
      value: 55.034000000000006
    - type: ndcg_at_3
      value: 82.419
    - type: ndcg_at_5
      value: 81.018
    - type: precision_at_1
      value: 86.0
    - type: precision_at_10
      value: 86.2
    - type: precision_at_100
      value: 62.68
    - type: precision_at_1000
      value: 24.032
    - type: precision_at_3
      value: 88.667
    - type: precision_at_5
      value: 86.0
    - type: recall_at_1
      value: 0.22899999999999998
    - type: recall_at_10
      value: 2.263
    - type: recall_at_100
      value: 15.238999999999999
    - type: recall_at_1000
      value: 51.937
    - type: recall_at_3
      value: 0.719
    - type: recall_at_5
      value: 1.15
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (sqi-eng)
      config: sqi-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 19.400000000000002
    - type: f1
      value: 15.386076064970075
    - type: precision
      value: 14.253878834615676
    - type: recall
      value: 19.400000000000002
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fry-eng)
      config: fry-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 42.19653179190752
    - type: f1
      value: 37.726396917148364
    - type: precision
      value: 36.14643545279384
    - type: recall
      value: 42.19653179190752
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kur-eng)
      config: kur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 18.536585365853657
    - type: f1
      value: 13.512010347376199
    - type: precision
      value: 12.034068912117693
    - type: recall
      value: 18.536585365853657
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tur-eng)
      config: tur-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 81.69999999999999
    - type: f1
      value: 77.37888888888888
    - type: precision
      value: 75.49583333333332
    - type: recall
      value: 81.69999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (deu-eng)
      config: deu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 97.39999999999999
    - type: f1
      value: 96.56666666666666
    - type: precision
      value: 96.16666666666667
    - type: recall
      value: 97.39999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nld-eng)
      config: nld-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 90.0
    - type: f1
      value: 87.22333333333333
    - type: precision
      value: 85.89166666666667
    - type: recall
      value: 90.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ron-eng)
      config: ron-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 64.7
    - type: f1
      value: 59.10904761904763
    - type: precision
      value: 56.91968253968254
    - type: recall
      value: 64.7
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ang-eng)
      config: ang-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 38.80597014925373
    - type: f1
      value: 30.890784174366264
    - type: precision
      value: 28.327114427860696
    - type: recall
      value: 38.80597014925373
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ido-eng)
      config: ido-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 53.900000000000006
    - type: f1
      value: 48.294138583638585
    - type: precision
      value: 46.333495670995674
    - type: recall
      value: 53.900000000000006
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jav-eng)
      config: jav-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.707317073170733
    - type: f1
      value: 8.999999999999998
    - type: precision
      value: 8.175377468060395
    - type: recall
      value: 11.707317073170733
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (isl-eng)
      config: isl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 15.9
    - type: f1
      value: 12.451226269430602
    - type: precision
      value: 11.404807799760325
    - type: recall
      value: 15.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slv-eng)
      config: slv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 41.919805589307416
    - type: f1
      value: 35.880619060297064
    - type: precision
      value: 33.77682308241239
    - type: recall
      value: 41.919805589307416
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cym-eng)
      config: cym-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 10.956521739130434
    - type: f1
      value: 9.098715976676996
    - type: precision
      value: 8.659935858401333
    - type: recall
      value: 10.956521739130434
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kaz-eng)
      config: kaz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.652173913043478
    - type: f1
      value: 9.154324883225136
    - type: precision
      value: 8.505898125360801
    - type: recall
      value: 11.652173913043478
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (est-eng)
      config: est-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.700000000000001
    - type: f1
      value: 7.431679431679432
    - type: precision
      value: 6.799925118740907
    - type: recall
      value: 9.700000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (heb-eng)
      config: heb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 77.5
    - type: f1
      value: 72.39999999999999
    - type: precision
      value: 70.13444444444444
    - type: recall
      value: 77.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gla-eng)
      config: gla-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.548854041013269
    - type: f1
      value: 4.233155465362944
    - type: precision
      value: 3.948150869646547
    - type: recall
      value: 5.548854041013269
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mar-eng)
      config: mar-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 73.5
    - type: f1
      value: 67.35333333333332
    - type: precision
      value: 64.63666666666666
    - type: recall
      value: 73.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lat-eng)
      config: lat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 27.700000000000003
    - type: f1
      value: 21.152765495941964
    - type: precision
      value: 19.27832403707404
    - type: recall
      value: 27.700000000000003
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bel-eng)
      config: bel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 48.1
    - type: f1
      value: 41.21001443001443
    - type: precision
      value: 38.628495670995676
    - type: recall
      value: 48.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pms-eng)
      config: pms-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 40.0
    - type: f1
      value: 34.32060003488575
    - type: precision
      value: 32.32134353741497
    - type: recall
      value: 40.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gle-eng)
      config: gle-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.800000000000001
    - type: f1
      value: 4.3954389450190465
    - type: precision
      value: 3.893838027469606
    - type: recall
      value: 6.800000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pes-eng)
      config: pes-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 51.800000000000004
    - type: f1
      value: 45.04222943722944
    - type: precision
      value: 42.541984126984126
    - type: recall
      value: 51.800000000000004
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nob-eng)
      config: nob-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 83.1
    - type: f1
      value: 79.20675324675324
    - type: precision
      value: 77.44944444444444
    - type: recall
      value: 83.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bul-eng)
      config: bul-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 66.8
    - type: f1
      value: 60.25746031746031
    - type: precision
      value: 57.55250000000001
    - type: recall
      value: 66.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cbk-eng)
      config: cbk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 63.6
    - type: f1
      value: 56.73421356421356
    - type: precision
      value: 54.02218253968254
    - type: recall
      value: 63.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hun-eng)
      config: hun-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 17.599999999999998
    - type: f1
      value: 13.17699134199134
    - type: precision
      value: 11.77444805194805
    - type: recall
      value: 17.599999999999998
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uig-eng)
      config: uig-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 2.0
    - type: f1
      value: 1.3126923076923078
    - type: precision
      value: 1.104952380952381
    - type: recall
      value: 2.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (rus-eng)
      config: rus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 88.3
    - type: f1
      value: 84.96333333333334
    - type: precision
      value: 83.38333333333333
    - type: recall
      value: 88.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (spa-eng)
      config: spa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 94.69999999999999
    - type: f1
      value: 93.12333333333333
    - type: precision
      value: 92.375
    - type: recall
      value: 94.69999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hye-eng)
      config: hye-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.6738544474393532
    - type: f1
      value: 0.3690849566291394
    - type: precision
      value: 0.3305452159899599
    - type: recall
      value: 0.6738544474393532
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tel-eng)
      config: tel-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 71.7948717948718
    - type: f1
      value: 65.37037037037037
    - type: precision
      value: 62.46438746438747
    - type: recall
      value: 71.7948717948718
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (afr-eng)
      config: afr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 56.699999999999996
    - type: f1
      value: 50.58054945054945
    - type: precision
      value: 48.313047619047616
    - type: recall
      value: 56.699999999999996
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mon-eng)
      config: mon-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.863636363636363
    - type: f1
      value: 10.948429096156369
    - type: precision
      value: 10.227287994137523
    - type: recall
      value: 13.863636363636363
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arz-eng)
      config: arz-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 62.473794549266245
    - type: f1
      value: 56.04172906059699
    - type: precision
      value: 53.26694619147448
    - type: recall
      value: 62.473794549266245
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hrv-eng)
      config: hrv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 40.0
    - type: f1
      value: 34.62948179271708
    - type: precision
      value: 32.699030910609864
    - type: recall
      value: 40.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nov-eng)
      config: nov-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 60.311284046692606
    - type: f1
      value: 54.06182447038479
    - type: precision
      value: 51.757921067259595
    - type: recall
      value: 60.311284046692606
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (gsw-eng)
      config: gsw-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 43.58974358974359
    - type: f1
      value: 37.042359350051655
    - type: precision
      value: 34.75783475783476
    - type: recall
      value: 43.58974358974359
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nds-eng)
      config: nds-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 56.49999999999999
    - type: f1
      value: 49.471269841269844
    - type: precision
      value: 46.742182539682545
    - type: recall
      value: 56.49999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ukr-eng)
      config: ukr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 71.5
    - type: f1
      value: 65.32880952380951
    - type: precision
      value: 62.71261904761904
    - type: recall
      value: 71.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (uzb-eng)
      config: uzb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.448598130841122
    - type: f1
      value: 7.861361294691689
    - type: precision
      value: 6.961045509526818
    - type: recall
      value: 11.448598130841122
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lit-eng)
      config: lit-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.5
    - type: f1
      value: 10.448586132968154
    - type: precision
      value: 9.624691955878397
    - type: recall
      value: 13.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ina-eng)
      config: ina-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 82.19999999999999
    - type: f1
      value: 78.25366946778712
    - type: precision
      value: 76.54291666666667
    - type: recall
      value: 82.19999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lfn-eng)
      config: lfn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 53.5
    - type: f1
      value: 47.48505411255411
    - type: precision
      value: 45.29801587301587
    - type: recall
      value: 53.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (zsm-eng)
      config: zsm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 61.1
    - type: f1
      value: 54.60758056758057
    - type: precision
      value: 52.16455433455434
    - type: recall
      value: 61.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ita-eng)
      config: ita-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 85.1
    - type: f1
      value: 81.98506715506716
    - type: precision
      value: 80.64754901960784
    - type: recall
      value: 85.1
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cmn-eng)
      config: cmn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 89.2
    - type: f1
      value: 86.13333333333333
    - type: precision
      value: 84.65
    - type: recall
      value: 89.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (lvs-eng)
      config: lvs-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.600000000000001
    - type: f1
      value: 10.721816580317723
    - type: precision
      value: 9.97922024538847
    - type: recall
      value: 13.600000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (glg-eng)
      config: glg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 79.0
    - type: f1
      value: 74.2652380952381
    - type: precision
      value: 72.18690476190476
    - type: recall
      value: 79.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ceb-eng)
      config: ceb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 12.833333333333332
    - type: f1
      value: 10.45993265993266
    - type: precision
      value: 9.849548907882243
    - type: recall
      value: 12.833333333333332
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bre-eng)
      config: bre-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 8.3
    - type: f1
      value: 5.457311371692176
    - type: precision
      value: 4.8466941508148595
    - type: recall
      value: 8.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ben-eng)
      config: ben-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 26.3
    - type: f1
      value: 20.851341154819416
    - type: precision
      value: 19.1173617945522
    - type: recall
      value: 26.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swg-eng)
      config: swg-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 41.964285714285715
    - type: f1
      value: 36.38605442176871
    - type: precision
      value: 34.523809523809526
    - type: recall
      value: 41.964285714285715
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (arq-eng)
      config: arq-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 26.454445664105382
    - type: f1
      value: 20.67692765826684
    - type: precision
      value: 18.684070229075715
    - type: recall
      value: 26.454445664105382
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kab-eng)
      config: kab-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 2.8000000000000003
    - type: f1
      value: 1.9487240537240536
    - type: precision
      value: 1.7766582325720255
    - type: recall
      value: 2.8000000000000003
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fra-eng)
      config: fra-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 91.5
    - type: f1
      value: 89.39
    - type: precision
      value: 88.425
    - type: recall
      value: 91.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (por-eng)
      config: por-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 91.5
    - type: f1
      value: 89.38333333333333
    - type: precision
      value: 88.36666666666667
    - type: recall
      value: 91.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tat-eng)
      config: tat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.2
    - type: f1
      value: 6.672282438325198
    - type: precision
      value: 6.046073589145276
    - type: recall
      value: 9.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (oci-eng)
      config: oci-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 45.2
    - type: f1
      value: 39.12095238095238
    - type: precision
      value: 36.820952380952384
    - type: recall
      value: 45.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pol-eng)
      config: pol-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 86.8
    - type: f1
      value: 83.35000000000001
    - type: precision
      value: 81.825
    - type: recall
      value: 86.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (war-eng)
      config: war-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 13.5
    - type: f1
      value: 10.66862856136998
    - type: precision
      value: 9.845928551928552
    - type: recall
      value: 13.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (aze-eng)
      config: aze-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 33.4
    - type: f1
      value: 27.78153389993659
    - type: precision
      value: 25.778055555555557
    - type: recall
      value: 33.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (vie-eng)
      config: vie-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 57.699999999999996
    - type: f1
      value: 50.440714285714286
    - type: precision
      value: 47.64396825396825
    - type: recall
      value: 57.699999999999996
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (nno-eng)
      config: nno-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 62.2
    - type: f1
      value: 56.0098625351257
    - type: precision
      value: 53.691914098972916
    - type: recall
      value: 62.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cha-eng)
      config: cha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 27.00729927007299
    - type: f1
      value: 22.798053527980535
    - type: precision
      value: 21.107055961070557
    - type: recall
      value: 27.00729927007299
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mhr-eng)
      config: mhr-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.2
    - type: f1
      value: 4.295544090473964
    - type: precision
      value: 3.913153952193392
    - type: recall
      value: 6.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dan-eng)
      config: dan-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 77.10000000000001
    - type: f1
      value: 72.49333333333334
    - type: precision
      value: 70.53368637110017
    - type: recall
      value: 77.10000000000001
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ell-eng)
      config: ell-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 15.2
    - type: f1
      value: 10.429591693330824
    - type: precision
      value: 9.145801926831338
    - type: recall
      value: 15.2
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (amh-eng)
      config: amh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 1.7857142857142856
    - type: f1
      value: 0.3635204081632653
    - type: precision
      value: 0.205026455026455
    - type: recall
      value: 1.7857142857142856
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (pam-eng)
      config: pam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 6.4
    - type: f1
      value: 4.8412763053939525
    - type: precision
      value: 4.444087810337809
    - type: recall
      value: 6.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hsb-eng)
      config: hsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 43.47826086956522
    - type: f1
      value: 37.13266949291794
    - type: precision
      value: 34.655332590115194
    - type: recall
      value: 43.47826086956522
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (srp-eng)
      config: srp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 42.0
    - type: f1
      value: 35.412229437229435
    - type: precision
      value: 32.907539682539685
    - type: recall
      value: 42.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (epo-eng)
      config: epo-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 36.0
    - type: f1
      value: 30.53874458874459
    - type: precision
      value: 28.711192408382807
    - type: recall
      value: 36.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kzj-eng)
      config: kzj-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.9
    - type: f1
      value: 5.80190114561213
    - type: precision
      value: 5.298527531836355
    - type: recall
      value: 7.9
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (awa-eng)
      config: awa-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 49.35064935064935
    - type: f1
      value: 41.57805638325119
    - type: precision
      value: 38.87445887445887
    - type: recall
      value: 49.35064935064935
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fao-eng)
      config: fao-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 25.572519083969464
    - type: f1
      value: 21.338006776938073
    - type: precision
      value: 20.194474736459465
    - type: recall
      value: 25.572519083969464
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mal-eng)
      config: mal-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 79.62154294032024
    - type: f1
      value: 74.47355652595827
    - type: precision
      value: 72.2076661814653
    - type: recall
      value: 79.62154294032024
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ile-eng)
      config: ile-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 68.0
    - type: f1
      value: 61.80859649122807
    - type: precision
      value: 59.30381381381381
    - type: recall
      value: 68.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (bos-eng)
      config: bos-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 42.93785310734463
    - type: f1
      value: 36.72617201306135
    - type: precision
      value: 34.72641059505466
    - type: recall
      value: 42.93785310734463
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cor-eng)
      config: cor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.5
    - type: f1
      value: 3.8651658986175113
    - type: precision
      value: 3.4432814407814405
    - type: recall
      value: 5.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (cat-eng)
      config: cat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 69.19999999999999
    - type: f1
      value: 63.41880952380953
    - type: precision
      value: 61.07913419913419
    - type: recall
      value: 69.19999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (eus-eng)
      config: eus-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 15.4
    - type: f1
      value: 11.672122577122575
    - type: precision
      value: 10.59919974661354
    - type: recall
      value: 15.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yue-eng)
      config: yue-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 58.5
    - type: f1
      value: 51.31880452880453
    - type: precision
      value: 48.60550125313283
    - type: recall
      value: 58.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swe-eng)
      config: swe-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 89.3
    - type: f1
      value: 86.32666666666667
    - type: precision
      value: 84.98333333333333
    - type: recall
      value: 89.3
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dtp-eng)
      config: dtp-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 5.7
    - type: f1
      value: 3.8739805216757546
    - type: precision
      value: 3.4734608954367014
    - type: recall
      value: 5.7
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kat-eng)
      config: kat-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.8042895442359249
    - type: f1
      value: 0.7596067917783735
    - type: precision
      value: 0.7372654155495978
    - type: recall
      value: 0.8042895442359249
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (jpn-eng)
      config: jpn-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 89.7
    - type: f1
      value: 86.92333333333333
    - type: precision
      value: 85.64166666666667
    - type: recall
      value: 89.7
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (csb-eng)
      config: csb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 26.08695652173913
    - type: f1
      value: 20.517863778733343
    - type: precision
      value: 18.901098901098898
    - type: recall
      value: 26.08695652173913
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (xho-eng)
      config: xho-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 12.676056338028168
    - type: f1
      value: 9.526324614352783
    - type: precision
      value: 9.006292657908235
    - type: recall
      value: 12.676056338028168
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (orv-eng)
      config: orv-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 24.910179640718564
    - type: f1
      value: 19.645099411566473
    - type: precision
      value: 17.676076418591386
    - type: recall
      value: 24.910179640718564
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ind-eng)
      config: ind-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 61.4
    - type: f1
      value: 54.64269841269841
    - type: precision
      value: 51.981071428571425
    - type: recall
      value: 61.4
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tuk-eng)
      config: tuk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.330049261083744
    - type: f1
      value: 9.610016420361248
    - type: precision
      value: 9.123781574258464
    - type: recall
      value: 11.330049261083744
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (max-eng)
      config: max-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 27.816901408450708
    - type: f1
      value: 22.51925345174495
    - type: precision
      value: 21.10468365750056
    - type: recall
      value: 27.816901408450708
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (swh-eng)
      config: swh-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 11.282051282051283
    - type: f1
      value: 7.777167097237831
    - type: precision
      value: 7.050109879436802
    - type: recall
      value: 11.282051282051283
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (hin-eng)
      config: hin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 86.0
    - type: f1
      value: 82.05857142857143
    - type: precision
      value: 80.25
    - type: recall
      value: 86.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (dsb-eng)
      config: dsb-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 34.44676409185804
    - type: f1
      value: 28.296517215097587
    - type: precision
      value: 26.16624956236465
    - type: recall
      value: 34.44676409185804
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ber-eng)
      config: ber-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 7.199999999999999
    - type: f1
      value: 5.500051631938041
    - type: precision
      value: 5.164411510424442
    - type: recall
      value: 7.199999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tam-eng)
      config: tam-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 71.9869706840391
    - type: f1
      value: 65.79339227547696
    - type: precision
      value: 63.16503800217155
    - type: recall
      value: 71.9869706840391
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (slk-eng)
      config: slk-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 70.89999999999999
    - type: f1
      value: 65.4152380952381
    - type: precision
      value: 63.106666666666655
    - type: recall
      value: 70.89999999999999
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tgl-eng)
      config: tgl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 21.0
    - type: f1
      value: 17.86438197644649
    - type: precision
      value: 16.84469948469949
    - type: recall
      value: 21.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ast-eng)
      config: ast-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 62.20472440944882
    - type: f1
      value: 55.81364829396325
    - type: precision
      value: 53.262092238470196
    - type: recall
      value: 62.20472440944882
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (mkd-eng)
      config: mkd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 41.8
    - type: f1
      value: 34.724603174603175
    - type: precision
      value: 32.040277777777774
    - type: recall
      value: 41.8
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (khm-eng)
      config: khm-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 0.41551246537396125
    - type: f1
      value: 0.3462603878116343
    - type: precision
      value: 0.32317636195752536
    - type: recall
      value: 0.41551246537396125
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ces-eng)
      config: ces-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 85.6
    - type: f1
      value: 81.81333333333333
    - type: precision
      value: 80.08333333333334
    - type: recall
      value: 85.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tzl-eng)
      config: tzl-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 31.73076923076923
    - type: f1
      value: 26.097374847374844
    - type: precision
      value: 24.31891025641026
    - type: recall
      value: 31.73076923076923
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (urd-eng)
      config: urd-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 9.6
    - type: f1
      value: 6.598392371412457
    - type: precision
      value: 5.855494356434758
    - type: recall
      value: 9.6
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (ara-eng)
      config: ara-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 83.5
    - type: f1
      value: 79.65190476190476
    - type: precision
      value: 77.875
    - type: recall
      value: 83.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (kor-eng)
      config: kor-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 80.5
    - type: f1
      value: 75.75999999999999
    - type: precision
      value: 73.60333333333332
    - type: recall
      value: 80.5
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (yid-eng)
      config: yid-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 2.1226415094339623
    - type: f1
      value: 1.4622641509433962
    - type: precision
      value: 1.2637578616352203
    - type: recall
      value: 2.1226415094339623
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (fin-eng)
      config: fin-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 23.0
    - type: f1
      value: 18.111780719280716
    - type: precision
      value: 16.497738095238095
    - type: recall
      value: 23.0
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (tha-eng)
      config: tha-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 4.562043795620438
    - type: f1
      value: 3.1632119907667358
    - type: precision
      value: 2.8806772100567724
    - type: recall
      value: 4.562043795620438
  - task:
      type: BitextMining
    dataset:
      type: mteb/tatoeba-bitext-mining
      name: MTEB Tatoeba (wuu-eng)
      config: wuu-eng
      split: test
      revision: 9080400076fbadbb4c4dcb136ff4eddc40b42553
    metrics:
    - type: accuracy
      value: 75.9
    - type: f1
      value: 70.57690476190476
    - type: precision
      value: 68.19761904761904
    - type: recall
      value: 75.9
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 2.804
    - type: map_at_10
      value: 11.267000000000001
    - type: map_at_100
      value: 17.034
    - type: map_at_1000
      value: 18.733
    - type: map_at_3
      value: 6.071
    - type: map_at_5
      value: 8.187
    - type: mrr_at_1
      value: 34.694
    - type: mrr_at_10
      value: 50.504000000000005
    - type: mrr_at_100
      value: 51.162
    - type: mrr_at_1000
      value: 51.162
    - type: mrr_at_3
      value: 45.918
    - type: mrr_at_5
      value: 49.082
    - type: ndcg_at_1
      value: 33.672999999999995
    - type: ndcg_at_10
      value: 27.478
    - type: ndcg_at_100
      value: 37.961
    - type: ndcg_at_1000
      value: 50.117
    - type: ndcg_at_3
      value: 30.156
    - type: ndcg_at_5
      value: 29.293999999999997
    - type: precision_at_1
      value: 34.694
    - type: precision_at_10
      value: 24.082
    - type: precision_at_100
      value: 7.632999999999999
    - type: precision_at_1000
      value: 1.569
    - type: precision_at_3
      value: 30.612000000000002
    - type: precision_at_5
      value: 29.387999999999998
    - type: recall_at_1
      value: 2.804
    - type: recall_at_10
      value: 17.785
    - type: recall_at_100
      value: 47.452
    - type: recall_at_1000
      value: 84.687
    - type: recall_at_3
      value: 6.9190000000000005
    - type: recall_at_5
      value: 10.807
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 74.5162
    - type: ap
      value: 15.022137849208509
    - type: f1
      value: 56.77914300422838
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 59.589700056593095
    - type: f1
      value: 59.93893560752363
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 40.11538634360855
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 83.97806520832091
    - type: cos_sim_ap
      value: 67.80381341664686
    - type: cos_sim_f1
      value: 63.01665268958908
    - type: cos_sim_precision
      value: 57.713407943822695
    - type: cos_sim_recall
      value: 69.39313984168865
    - type: dot_accuracy
      value: 83.9899862907552
    - type: dot_ap
      value: 67.80914960711299
    - type: dot_f1
      value: 63.0287144048612
    - type: dot_precision
      value: 57.46252444058223
    - type: dot_recall
      value: 69.78891820580475
    - type: euclidean_accuracy
      value: 83.9601835846695
    - type: euclidean_ap
      value: 67.79862461635126
    - type: euclidean_f1
      value: 63.02426882389545
    - type: euclidean_precision
      value: 59.64664310954063
    - type: euclidean_recall
      value: 66.80738786279683
    - type: manhattan_accuracy
      value: 83.94230196101806
    - type: manhattan_ap
      value: 67.78560087328111
    - type: manhattan_f1
      value: 63.10622881851117
    - type: manhattan_precision
      value: 56.63939584644431
    - type: manhattan_recall
      value: 71.2401055408971
    - type: max_accuracy
      value: 83.9899862907552
    - type: max_ap
      value: 67.80914960711299
    - type: max_f1
      value: 63.10622881851117
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 89.04994760740482
    - type: cos_sim_ap
      value: 85.71231674852108
    - type: cos_sim_f1
      value: 78.92350867093619
    - type: cos_sim_precision
      value: 74.07807645549101
    - type: cos_sim_recall
      value: 84.44718201416693
    - type: dot_accuracy
      value: 89.05188807389295
    - type: dot_ap
      value: 85.71776365526502
    - type: dot_f1
      value: 78.92055922835156
    - type: dot_precision
      value: 74.34152317430069
    - type: dot_recall
      value: 84.10070834616569
    - type: euclidean_accuracy
      value: 89.05188807389295
    - type: euclidean_ap
      value: 85.7114644968015
    - type: euclidean_f1
      value: 78.9458525345622
    - type: euclidean_precision
      value: 74.14119556397078
    - type: euclidean_recall
      value: 84.41638435478903
    - type: manhattan_accuracy
      value: 89.06547133930997
    - type: manhattan_ap
      value: 85.70658730333459
    - type: manhattan_f1
      value: 78.91009741543552
    - type: manhattan_precision
      value: 74.00714719169308
    - type: manhattan_recall
      value: 84.5087773329227
    - type: max_accuracy
      value: 89.06547133930997
    - type: max_ap
      value: 85.71776365526502
    - type: max_f1
      value: 78.9458525345622
---

## Bedrock Titan Text Embeddings v2
This repository contains the MTEB scores and usage examples of Bedrock Titan Text Embeddings v2. You can use the embedding model either via the Bedrock InvokeModel API or via Bedrock's batch jobs. For RAG use cases we recommend the former to embed queries during search (latency optimized) and the latter to index corpus (throughput optimized).

## Using Bedrock's InvokeModel API

```python
import json
import boto3
class TitanEmbeddings(object):
    accept = "application/json"
    content_type = "application/json"
    
    def __init__(self, model_id="amazon.titan-embed-text-v2:0"):
        self.bedrock = boto3.client(service_name='bedrock-runtime')
        self.model_id = model_id
    def __call__(self, text, dimensions, normalize=True):
        """
        Returns Titan Embeddings
        Args:
            text (str): text to embed
            dimensions (int): Number of output dimensions.
            normalize (bool): Whether to return the normalized embedding or not.
        Return:
            List[float]: Embedding
            
        """
        body = json.dumps({
            "inputText": text,
            "dimensions": dimensions,
            "normalize": normalize
        })
        response = self.bedrock.invoke_model(
            body=body, modelId=self.model_id, accept=self.accept, contentType=self.content_type
        )
        response_body = json.loads(response.get('body').read())
        return response_body['embedding']

if __name__ == '__main__':
    """
    Entrypoint for Amazon Titan Embeddings V2 - Text example.
    """
    dimensions = 1024
    normalize = True
    
    titan_embeddings_v2 = TitanEmbeddings(model_id="amazon.titan-embed-text-v2:0")

    input_text = "What are the different services that you offer?"
    embedding = titan_embeddings_v2(input_text, dimensions, normalize)
    
    print(f"{input_text=}")
    print(f"{embedding[:10]=}")

```


## Using Bedrock's batch jobs

```python
import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

region = "us-east-1"
base_uri = f"bedrock.{region}.amazonaws.com"
batch_job_uri = f"https://{base_uri}/model-invocation-job/"

# For details on how to set up an IAM role for batch inference, see
# https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-permissions.html
role_arn = "arn:aws:iam::111122223333:role/my-batch-inference-role"

payload = {
   "inputDataConfig": { 
        "s3InputDataConfig": { 
            "s3Uri": "s3://my-input-bucket/batch-input/",
            "s3InputFormat": "JSONL"
        }
   },
   "jobName": "embeddings-v2-batch-job",
   "modelId": "amazon.titan-embed-text-v2:0",
   "outputDataConfig": {
        "s3OutputDataConfig": {
            "s3Uri": "s3://my-output-bucket/batch-output/"
        }
   },
   "roleArn": role_arn
}

request_auth = BotoAWSRequestsAuth(
    aws_host=base_uri,
    aws_region=region,
    aws_service="bedrock"
)


response= requests.request("POST", batch_job_uri, json=payload, auth=request_auth)
print(response.json())
```