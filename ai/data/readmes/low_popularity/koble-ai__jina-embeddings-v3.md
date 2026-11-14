---
license: cc-by-nc-4.0
tags:
- feature-extraction
- sentence-similarity
- mteb
- sentence-transformers
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
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
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
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
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
inference: false
library_name: transformers
model-index:
- name: jina-embeddings-v3
  results:
  - dataset:
      config: default
      name: MTEB AFQMC (default)
      revision: b44c3b011063adb25877c13823db83bb193913c4
      split: validation
      type: C-MTEB/AFQMC
    metrics:
    - type: cosine_pearson
      value: 41.74237700998808
    - type: cosine_spearman
      value: 43.4726782647566
    - type: euclidean_pearson
      value: 42.244585459479964
    - type: euclidean_spearman
      value: 43.525070045169606
    - type: main_score
      value: 43.4726782647566
    - type: manhattan_pearson
      value: 42.04616728224863
    - type: manhattan_spearman
      value: 43.308828270754645
    - type: pearson
      value: 41.74237700998808
    - type: spearman
      value: 43.4726782647566
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB ArguAna-PL (default)
      revision: 63fc86750af76253e8c760fc9e534bbf24d260a2
      split: test
      type: clarin-knext/arguana-pl
    metrics:
    - type: main_score
      value: 50.117999999999995
    - type: map_at_1
      value: 24.253
    - type: map_at_10
      value: 40.725
    - type: map_at_100
      value: 41.699999999999996
    - type: map_at_1000
      value: 41.707
    - type: map_at_20
      value: 41.467999999999996
    - type: map_at_3
      value: 35.467
    - type: map_at_5
      value: 38.291
    - type: mrr_at_1
      value: 24.751066856330013
    - type: mrr_at_10
      value: 40.91063808169072
    - type: mrr_at_100
      value: 41.885497923928675
    - type: mrr_at_1000
      value: 41.89301098419842
    - type: mrr_at_20
      value: 41.653552355442514
    - type: mrr_at_3
      value: 35.656709340919775
    - type: mrr_at_5
      value: 38.466097676623946
    - type: nauc_map_at_1000_diff1
      value: 7.503000359807567
    - type: nauc_map_at_1000_max
      value: -11.030405164830546
    - type: nauc_map_at_1000_std
      value: -8.902792782585117
    - type: nauc_map_at_100_diff1
      value: 7.509899249593199
    - type: nauc_map_at_100_max
      value: -11.023581259404406
    - type: nauc_map_at_100_std
      value: -8.892241185067272
    - type: nauc_map_at_10_diff1
      value: 7.24369711881512
    - type: nauc_map_at_10_max
      value: -10.810000200433278
    - type: nauc_map_at_10_std
      value: -8.987230542165776
    - type: nauc_map_at_1_diff1
      value: 11.37175831832417
    - type: nauc_map_at_1_max
      value: -13.315221903223055
    - type: nauc_map_at_1_std
      value: -9.398199605510275
    - type: nauc_map_at_20_diff1
      value: 7.477364530860648
    - type: nauc_map_at_20_max
      value: -10.901251218105566
    - type: nauc_map_at_20_std
      value: -8.868148116405925
    - type: nauc_map_at_3_diff1
      value: 6.555548802174882
    - type: nauc_map_at_3_max
      value: -12.247274800542934
    - type: nauc_map_at_3_std
      value: -9.879475250984811
    - type: nauc_map_at_5_diff1
      value: 7.426588563355882
    - type: nauc_map_at_5_max
      value: -11.347695686001805
    - type: nauc_map_at_5_std
      value: -9.34441892203972
    - type: nauc_mrr_at_1000_diff1
      value: 5.99737552143614
    - type: nauc_mrr_at_1000_max
      value: -11.327205136505727
    - type: nauc_mrr_at_1000_std
      value: -8.791079115519503
    - type: nauc_mrr_at_100_diff1
      value: 6.004622525255784
    - type: nauc_mrr_at_100_max
      value: -11.320336759899723
    - type: nauc_mrr_at_100_std
      value: -8.780602249831777
    - type: nauc_mrr_at_10_diff1
      value: 5.783623516930227
    - type: nauc_mrr_at_10_max
      value: -11.095971693467078
    - type: nauc_mrr_at_10_std
      value: -8.877242032013582
    - type: nauc_mrr_at_1_diff1
      value: 9.694937537703797
    - type: nauc_mrr_at_1_max
      value: -12.531905083727912
    - type: nauc_mrr_at_1_std
      value: -8.903992940100146
    - type: nauc_mrr_at_20_diff1
      value: 5.984841206233873
    - type: nauc_mrr_at_20_max
      value: -11.195236951048969
    - type: nauc_mrr_at_20_std
      value: -8.757266039186018
    - type: nauc_mrr_at_3_diff1
      value: 5.114333824261379
    - type: nauc_mrr_at_3_max
      value: -12.64809799843464
    - type: nauc_mrr_at_3_std
      value: -9.791146138025184
    - type: nauc_mrr_at_5_diff1
      value: 5.88941606224512
    - type: nauc_mrr_at_5_max
      value: -11.763903418071918
    - type: nauc_mrr_at_5_std
      value: -9.279175712709446
    - type: nauc_ndcg_at_1000_diff1
      value: 7.076950652226086
    - type: nauc_ndcg_at_1000_max
      value: -10.386482092087371
    - type: nauc_ndcg_at_1000_std
      value: -8.309190917074046
    - type: nauc_ndcg_at_100_diff1
      value: 7.2329220284865245
    - type: nauc_ndcg_at_100_max
      value: -10.208048403220337
    - type: nauc_ndcg_at_100_std
      value: -7.997975874274613
    - type: nauc_ndcg_at_10_diff1
      value: 6.065391100006953
    - type: nauc_ndcg_at_10_max
      value: -9.046164377601153
    - type: nauc_ndcg_at_10_std
      value: -8.34724889697153
    - type: nauc_ndcg_at_1_diff1
      value: 11.37175831832417
    - type: nauc_ndcg_at_1_max
      value: -13.315221903223055
    - type: nauc_ndcg_at_1_std
      value: -9.398199605510275
    - type: nauc_ndcg_at_20_diff1
      value: 6.949389989202601
    - type: nauc_ndcg_at_20_max
      value: -9.35740451760307
    - type: nauc_ndcg_at_20_std
      value: -7.761295171828212
    - type: nauc_ndcg_at_3_diff1
      value: 5.051471796151364
    - type: nauc_ndcg_at_3_max
      value: -12.158763333711653
    - type: nauc_ndcg_at_3_std
      value: -10.078902544421926
    - type: nauc_ndcg_at_5_diff1
      value: 6.527454512611454
    - type: nauc_ndcg_at_5_max
      value: -10.525118233848586
    - type: nauc_ndcg_at_5_std
      value: -9.120055125584031
    - type: nauc_precision_at_1000_diff1
      value: -10.6495668199151
    - type: nauc_precision_at_1000_max
      value: 12.070656425217841
    - type: nauc_precision_at_1000_std
      value: 55.844551709649004
    - type: nauc_precision_at_100_diff1
      value: 19.206967129266285
    - type: nauc_precision_at_100_max
      value: 16.296851020813456
    - type: nauc_precision_at_100_std
      value: 45.60378984257811
    - type: nauc_precision_at_10_diff1
      value: 0.6490335354304879
    - type: nauc_precision_at_10_max
      value: 0.5757198255366447
    - type: nauc_precision_at_10_std
      value: -4.875847131691451
    - type: nauc_precision_at_1_diff1
      value: 11.37175831832417
    - type: nauc_precision_at_1_max
      value: -13.315221903223055
    - type: nauc_precision_at_1_std
      value: -9.398199605510275
    - type: nauc_precision_at_20_diff1
      value: 4.899369866929203
    - type: nauc_precision_at_20_max
      value: 5.988537297189552
    - type: nauc_precision_at_20_std
      value: 4.830900387582837
    - type: nauc_precision_at_3_diff1
      value: 0.8791156910997744
    - type: nauc_precision_at_3_max
      value: -11.983373635905993
    - type: nauc_precision_at_3_std
      value: -10.646185111581257
    - type: nauc_precision_at_5_diff1
      value: 3.9314486166548432
    - type: nauc_precision_at_5_max
      value: -7.798591396895839
    - type: nauc_precision_at_5_std
      value: -8.293043407234125
    - type: nauc_recall_at_1000_diff1
      value: -10.649566819918673
    - type: nauc_recall_at_1000_max
      value: 12.070656425214647
    - type: nauc_recall_at_1000_std
      value: 55.84455170965023
    - type: nauc_recall_at_100_diff1
      value: 19.206967129265127
    - type: nauc_recall_at_100_max
      value: 16.296851020813722
    - type: nauc_recall_at_100_std
      value: 45.60378984257728
    - type: nauc_recall_at_10_diff1
      value: 0.6490335354304176
    - type: nauc_recall_at_10_max
      value: 0.5757198255366095
    - type: nauc_recall_at_10_std
      value: -4.875847131691468
    - type: nauc_recall_at_1_diff1
      value: 11.37175831832417
    - type: nauc_recall_at_1_max
      value: -13.315221903223055
    - type: nauc_recall_at_1_std
      value: -9.398199605510275
    - type: nauc_recall_at_20_diff1
      value: 4.899369866929402
    - type: nauc_recall_at_20_max
      value: 5.98853729718968
    - type: nauc_recall_at_20_std
      value: 4.830900387582967
    - type: nauc_recall_at_3_diff1
      value: 0.8791156910997652
    - type: nauc_recall_at_3_max
      value: -11.983373635905997
    - type: nauc_recall_at_3_std
      value: -10.64618511158124
    - type: nauc_recall_at_5_diff1
      value: 3.9314486166548472
    - type: nauc_recall_at_5_max
      value: -7.7985913968958585
    - type: nauc_recall_at_5_std
      value: -8.293043407234132
    - type: ndcg_at_1
      value: 24.253
    - type: ndcg_at_10
      value: 50.117999999999995
    - type: ndcg_at_100
      value: 54.291999999999994
    - type: ndcg_at_1000
      value: 54.44799999999999
    - type: ndcg_at_20
      value: 52.771
    - type: ndcg_at_3
      value: 39.296
    - type: ndcg_at_5
      value: 44.373000000000005
    - type: precision_at_1
      value: 24.253
    - type: precision_at_10
      value: 8.016
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.527
    - type: precision_at_3
      value: 16.808999999999997
    - type: precision_at_5
      value: 12.546
    - type: recall_at_1
      value: 24.253
    - type: recall_at_10
      value: 80.156
    - type: recall_at_100
      value: 98.43499999999999
    - type: recall_at_1000
      value: 99.57300000000001
    - type: recall_at_20
      value: 90.54100000000001
    - type: recall_at_3
      value: 50.427
    - type: recall_at_5
      value: 62.731
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia-PL (default)
      revision: 76afe41d9af165cc40999fcaa92312b8b012064a
      split: test
      type: clarin-knext/dbpedia-pl
    metrics:
    - type: main_score
      value: 34.827000000000005
    - type: map_at_1
      value: 7.049999999999999
    - type: map_at_10
      value: 14.982999999999999
    - type: map_at_100
      value: 20.816000000000003
    - type: map_at_1000
      value: 22.33
    - type: map_at_20
      value: 17.272000000000002
    - type: map_at_3
      value: 10.661
    - type: map_at_5
      value: 12.498
    - type: mrr_at_1
      value: 57.25
    - type: mrr_at_10
      value: 65.81934523809524
    - type: mrr_at_100
      value: 66.2564203928212
    - type: mrr_at_1000
      value: 66.27993662923856
    - type: mrr_at_20
      value: 66.0732139130649
    - type: mrr_at_3
      value: 64.08333333333333
    - type: mrr_at_5
      value: 65.27083333333333
    - type: nauc_map_at_1000_diff1
      value: 16.41780871174038
    - type: nauc_map_at_1000_max
      value: 30.193946325654654
    - type: nauc_map_at_1000_std
      value: 31.46095497039037
    - type: nauc_map_at_100_diff1
      value: 18.57903165498531
    - type: nauc_map_at_100_max
      value: 29.541476938623262
    - type: nauc_map_at_100_std
      value: 28.228604103301052
    - type: nauc_map_at_10_diff1
      value: 24.109434489748946
    - type: nauc_map_at_10_max
      value: 21.475954208048968
    - type: nauc_map_at_10_std
      value: 9.964464537806988
    - type: nauc_map_at_1_diff1
      value: 38.67437644802124
    - type: nauc_map_at_1_max
      value: 14.52136658726491
    - type: nauc_map_at_1_std
      value: -2.8981666782088755
    - type: nauc_map_at_20_diff1
      value: 21.42547228801935
    - type: nauc_map_at_20_max
      value: 25.04510402960458
    - type: nauc_map_at_20_std
      value: 16.533079346431155
    - type: nauc_map_at_3_diff1
      value: 26.63648858245477
    - type: nauc_map_at_3_max
      value: 13.632235789780415
    - type: nauc_map_at_3_std
      value: -0.40129174577700716
    - type: nauc_map_at_5_diff1
      value: 24.513861031197933
    - type: nauc_map_at_5_max
      value: 16.599888813946688
    - type: nauc_map_at_5_std
      value: 3.4448514739556346
    - type: nauc_mrr_at_1000_diff1
      value: 36.57353464537154
    - type: nauc_mrr_at_1000_max
      value: 55.34763483979515
    - type: nauc_mrr_at_1000_std
      value: 40.3722796438533
    - type: nauc_mrr_at_100_diff1
      value: 36.555989566513134
    - type: nauc_mrr_at_100_max
      value: 55.347805216808396
    - type: nauc_mrr_at_100_std
      value: 40.38465945075711
    - type: nauc_mrr_at_10_diff1
      value: 36.771572999261984
    - type: nauc_mrr_at_10_max
      value: 55.41239897909165
    - type: nauc_mrr_at_10_std
      value: 40.52058934624793
    - type: nauc_mrr_at_1_diff1
      value: 38.2472828531032
    - type: nauc_mrr_at_1_max
      value: 51.528473828685705
    - type: nauc_mrr_at_1_std
      value: 33.03676467942882
    - type: nauc_mrr_at_20_diff1
      value: 36.642602571889036
    - type: nauc_mrr_at_20_max
      value: 55.3763342076553
    - type: nauc_mrr_at_20_std
      value: 40.41520090500838
    - type: nauc_mrr_at_3_diff1
      value: 36.79451847426628
    - type: nauc_mrr_at_3_max
      value: 54.59778581826193
    - type: nauc_mrr_at_3_std
      value: 39.48392075873095
    - type: nauc_mrr_at_5_diff1
      value: 36.92150807529304
    - type: nauc_mrr_at_5_max
      value: 55.03553978718272
    - type: nauc_mrr_at_5_std
      value: 40.20147745489917
    - type: nauc_ndcg_at_1000_diff1
      value: 21.843092744321268
    - type: nauc_ndcg_at_1000_max
      value: 44.93275990394279
    - type: nauc_ndcg_at_1000_std
      value: 47.09186225236347
    - type: nauc_ndcg_at_100_diff1
      value: 25.180282568979095
    - type: nauc_ndcg_at_100_max
      value: 41.737709709508394
    - type: nauc_ndcg_at_100_std
      value: 38.80950644139446
    - type: nauc_ndcg_at_10_diff1
      value: 24.108368037214046
    - type: nauc_ndcg_at_10_max
      value: 41.29298370689967
    - type: nauc_ndcg_at_10_std
      value: 35.06450769738732
    - type: nauc_ndcg_at_1_diff1
      value: 35.51010679525079
    - type: nauc_ndcg_at_1_max
      value: 42.40790024212412
    - type: nauc_ndcg_at_1_std
      value: 26.696412036243157
    - type: nauc_ndcg_at_20_diff1
      value: 23.909989673256195
    - type: nauc_ndcg_at_20_max
      value: 39.78444647091927
    - type: nauc_ndcg_at_20_std
      value: 33.39544470364529
    - type: nauc_ndcg_at_3_diff1
      value: 22.50484297956035
    - type: nauc_ndcg_at_3_max
      value: 39.14551926034168
    - type: nauc_ndcg_at_3_std
      value: 30.330135925392014
    - type: nauc_ndcg_at_5_diff1
      value: 21.7798872028265
    - type: nauc_ndcg_at_5_max
      value: 40.23856975248015
    - type: nauc_ndcg_at_5_std
      value: 32.438381067440396
    - type: nauc_precision_at_1000_diff1
      value: -21.62692442272279
    - type: nauc_precision_at_1000_max
      value: 0.9689046974430882
    - type: nauc_precision_at_1000_std
      value: 18.54001058230465
    - type: nauc_precision_at_100_diff1
      value: -10.132258779856192
    - type: nauc_precision_at_100_max
      value: 23.74516110444681
    - type: nauc_precision_at_100_std
      value: 47.03416663319965
    - type: nauc_precision_at_10_diff1
      value: 1.543656509571949
    - type: nauc_precision_at_10_max
      value: 36.98864812757555
    - type: nauc_precision_at_10_std
      value: 46.56427199077426
    - type: nauc_precision_at_1_diff1
      value: 38.2472828531032
    - type: nauc_precision_at_1_max
      value: 51.528473828685705
    - type: nauc_precision_at_1_std
      value: 33.03676467942882
    - type: nauc_precision_at_20_diff1
      value: -4.612864872734335
    - type: nauc_precision_at_20_max
      value: 34.03565449182125
    - type: nauc_precision_at_20_std
      value: 48.880727648349534
    - type: nauc_precision_at_3_diff1
      value: 6.360850444467829
    - type: nauc_precision_at_3_max
      value: 36.25816942368427
    - type: nauc_precision_at_3_std
      value: 34.48882647419187
    - type: nauc_precision_at_5_diff1
      value: 2.6445596936740037
    - type: nauc_precision_at_5_max
      value: 37.174463388899056
    - type: nauc_precision_at_5_std
      value: 40.25254370626113
    - type: nauc_recall_at_1000_diff1
      value: 13.041227176748077
    - type: nauc_recall_at_1000_max
      value: 39.722336427072094
    - type: nauc_recall_at_1000_std
      value: 52.04032890059214
    - type: nauc_recall_at_100_diff1
      value: 18.286096899139153
    - type: nauc_recall_at_100_max
      value: 34.072389201930314
    - type: nauc_recall_at_100_std
      value: 37.73637623416653
    - type: nauc_recall_at_10_diff1
      value: 22.35560419280504
    - type: nauc_recall_at_10_max
      value: 19.727247199595197
    - type: nauc_recall_at_10_std
      value: 8.58498575109203
    - type: nauc_recall_at_1_diff1
      value: 38.67437644802124
    - type: nauc_recall_at_1_max
      value: 14.52136658726491
    - type: nauc_recall_at_1_std
      value: -2.8981666782088755
    - type: nauc_recall_at_20_diff1
      value: 19.026320886902916
    - type: nauc_recall_at_20_max
      value: 22.753562309469867
    - type: nauc_recall_at_20_std
      value: 14.89994263882445
    - type: nauc_recall_at_3_diff1
      value: 23.428129702129684
    - type: nauc_recall_at_3_max
      value: 10.549153954790542
    - type: nauc_recall_at_3_std
      value: -1.7590608997055206
    - type: nauc_recall_at_5_diff1
      value: 21.27448645803921
    - type: nauc_recall_at_5_max
      value: 13.620279707461677
    - type: nauc_recall_at_5_std
      value: 2.0577962208292675
    - type: ndcg_at_1
      value: 46.75
    - type: ndcg_at_10
      value: 34.827000000000005
    - type: ndcg_at_100
      value: 38.157999999999994
    - type: ndcg_at_1000
      value: 44.816
    - type: ndcg_at_20
      value: 34.152
    - type: ndcg_at_3
      value: 39.009
    - type: ndcg_at_5
      value: 36.826
    - type: precision_at_1
      value: 57.25
    - type: precision_at_10
      value: 27.575
    - type: precision_at_100
      value: 8.84
    - type: precision_at_1000
      value: 1.949
    - type: precision_at_20
      value: 20.724999999999998
    - type: precision_at_3
      value: 41.167
    - type: precision_at_5
      value: 35.199999999999996
    - type: recall_at_1
      value: 7.049999999999999
    - type: recall_at_10
      value: 19.817999999999998
    - type: recall_at_100
      value: 42.559999999999995
    - type: recall_at_1000
      value: 63.744
    - type: recall_at_20
      value: 25.968000000000004
    - type: recall_at_3
      value: 11.959
    - type: recall_at_5
      value: 14.939
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA-PL (default)
      revision: 2e535829717f8bf9dc829b7f911cc5bbd4e6608e
      split: test
      type: clarin-knext/fiqa-pl
    metrics:
    - type: main_score
      value: 38.828
    - type: map_at_1
      value: 19.126
    - type: map_at_10
      value: 31.002000000000002
    - type: map_at_100
      value: 32.736
    - type: map_at_1000
      value: 32.933
    - type: map_at_20
      value: 31.894
    - type: map_at_3
      value: 26.583000000000002
    - type: map_at_5
      value: 28.904000000000003
    - type: mrr_at_1
      value: 37.808641975308646
    - type: mrr_at_10
      value: 46.36745541838134
    - type: mrr_at_100
      value: 47.14140915794908
    - type: mrr_at_1000
      value: 47.190701435388846
    - type: mrr_at_20
      value: 46.81387776440309
    - type: mrr_at_3
      value: 43.750000000000014
    - type: mrr_at_5
      value: 45.23919753086418
    - type: nauc_map_at_1000_diff1
      value: 38.5532285881503
    - type: nauc_map_at_1000_max
      value: 34.44383884813453
    - type: nauc_map_at_1000_std
      value: -1.3963497949476722
    - type: nauc_map_at_100_diff1
      value: 38.49292464176943
    - type: nauc_map_at_100_max
      value: 34.33752755618645
    - type: nauc_map_at_100_std
      value: -1.4794032905848582
    - type: nauc_map_at_10_diff1
      value: 38.26061536370962
    - type: nauc_map_at_10_max
      value: 33.16977912721411
    - type: nauc_map_at_10_std
      value: -2.3853370604730393
    - type: nauc_map_at_1_diff1
      value: 46.288767289528344
    - type: nauc_map_at_1_max
      value: 25.67706785013364
    - type: nauc_map_at_1_std
      value: -6.989769609924645
    - type: nauc_map_at_20_diff1
      value: 38.507270129330685
    - type: nauc_map_at_20_max
      value: 33.70963328055982
    - type: nauc_map_at_20_std
      value: -1.9835510011554272
    - type: nauc_map_at_3_diff1
      value: 39.81061518646884
    - type: nauc_map_at_3_max
      value: 30.101186374147748
    - type: nauc_map_at_3_std
      value: -4.027120247237715
    - type: nauc_map_at_5_diff1
      value: 38.55602589746512
    - type: nauc_map_at_5_max
      value: 31.515174267015983
    - type: nauc_map_at_5_std
      value: -3.4064239358570303
    - type: nauc_mrr_at_1000_diff1
      value: 45.030514454725726
    - type: nauc_mrr_at_1000_max
      value: 43.878919881666164
    - type: nauc_mrr_at_1000_std
      value: 2.517594250297626
    - type: nauc_mrr_at_100_diff1
      value: 45.00868212878687
    - type: nauc_mrr_at_100_max
      value: 43.87437011120001
    - type: nauc_mrr_at_100_std
      value: 2.5257874265014966
    - type: nauc_mrr_at_10_diff1
      value: 44.855044606754056
    - type: nauc_mrr_at_10_max
      value: 43.946617058785186
    - type: nauc_mrr_at_10_std
      value: 2.5173751662794044
    - type: nauc_mrr_at_1_diff1
      value: 49.441510997817346
    - type: nauc_mrr_at_1_max
      value: 43.08547383044357
    - type: nauc_mrr_at_1_std
      value: -1.8747770703324347
    - type: nauc_mrr_at_20_diff1
      value: 45.019880416584215
    - type: nauc_mrr_at_20_max
      value: 43.85691473662242
    - type: nauc_mrr_at_20_std
      value: 2.4625487605091303
    - type: nauc_mrr_at_3_diff1
      value: 45.322041658604036
    - type: nauc_mrr_at_3_max
      value: 43.95079293074395
    - type: nauc_mrr_at_3_std
      value: 2.4644274393435737
    - type: nauc_mrr_at_5_diff1
      value: 44.99461837803437
    - type: nauc_mrr_at_5_max
      value: 43.97934275090601
    - type: nauc_mrr_at_5_std
      value: 2.5353091695125096
    - type: nauc_ndcg_at_1000_diff1
      value: 39.38449023275524
    - type: nauc_ndcg_at_1000_max
      value: 39.48382767312788
    - type: nauc_ndcg_at_1000_std
      value: 3.414789408343409
    - type: nauc_ndcg_at_100_diff1
      value: 38.29675861135578
    - type: nauc_ndcg_at_100_max
      value: 38.2674786507297
    - type: nauc_ndcg_at_100_std
      value: 2.7094055381218207
    - type: nauc_ndcg_at_10_diff1
      value: 38.09514955708717
    - type: nauc_ndcg_at_10_max
      value: 36.664923238906525
    - type: nauc_ndcg_at_10_std
      value: 0.6901410544967921
    - type: nauc_ndcg_at_1_diff1
      value: 49.441510997817346
    - type: nauc_ndcg_at_1_max
      value: 43.08547383044357
    - type: nauc_ndcg_at_1_std
      value: -1.8747770703324347
    - type: nauc_ndcg_at_20_diff1
      value: 38.44967736231759
    - type: nauc_ndcg_at_20_max
      value: 36.871179313622584
    - type: nauc_ndcg_at_20_std
      value: 1.157560360065234
    - type: nauc_ndcg_at_3_diff1
      value: 39.02419271805571
    - type: nauc_ndcg_at_3_max
      value: 37.447669442586324
    - type: nauc_ndcg_at_3_std
      value: 0.41502589779297794
    - type: nauc_ndcg_at_5_diff1
      value: 38.10233452742001
    - type: nauc_ndcg_at_5_max
      value: 35.816381905465676
    - type: nauc_ndcg_at_5_std
      value: -0.3704499913387088
    - type: nauc_precision_at_1000_diff1
      value: 2.451267097838658
    - type: nauc_precision_at_1000_max
      value: 29.116394969085306
    - type: nauc_precision_at_1000_std
      value: 14.85900786538363
    - type: nauc_precision_at_100_diff1
      value: 8.10919082251277
    - type: nauc_precision_at_100_max
      value: 36.28388256191417
    - type: nauc_precision_at_100_std
      value: 14.830039904317657
    - type: nauc_precision_at_10_diff1
      value: 15.02446609920477
    - type: nauc_precision_at_10_max
      value: 41.008463775454054
    - type: nauc_precision_at_10_std
      value: 10.431403152334486
    - type: nauc_precision_at_1_diff1
      value: 49.441510997817346
    - type: nauc_precision_at_1_max
      value: 43.08547383044357
    - type: nauc_precision_at_1_std
      value: -1.8747770703324347
    - type: nauc_precision_at_20_diff1
      value: 14.222022201169926
    - type: nauc_precision_at_20_max
      value: 40.10189643835305
    - type: nauc_precision_at_20_std
      value: 12.204443815975527
    - type: nauc_precision_at_3_diff1
      value: 25.41905395341234
    - type: nauc_precision_at_3_max
      value: 41.56133905339819
    - type: nauc_precision_at_3_std
      value: 5.575516915590082
    - type: nauc_precision_at_5_diff1
      value: 20.20081221089351
    - type: nauc_precision_at_5_max
      value: 40.95218555916681
    - type: nauc_precision_at_5_std
      value: 7.2040745500708745
    - type: nauc_recall_at_1000_diff1
      value: 28.021198234033395
    - type: nauc_recall_at_1000_max
      value: 36.165148684597504
    - type: nauc_recall_at_1000_std
      value: 28.28852356008973
    - type: nauc_recall_at_100_diff1
      value: 21.882447802741897
    - type: nauc_recall_at_100_max
      value: 26.979684607567222
    - type: nauc_recall_at_100_std
      value: 9.783658817010082
    - type: nauc_recall_at_10_diff1
      value: 28.493097951178818
    - type: nauc_recall_at_10_max
      value: 29.40937476550134
    - type: nauc_recall_at_10_std
      value: 2.7593763576979353
    - type: nauc_recall_at_1_diff1
      value: 46.288767289528344
    - type: nauc_recall_at_1_max
      value: 25.67706785013364
    - type: nauc_recall_at_1_std
      value: -6.989769609924645
    - type: nauc_recall_at_20_diff1
      value: 27.638381299425234
    - type: nauc_recall_at_20_max
      value: 27.942035836106328
    - type: nauc_recall_at_20_std
      value: 3.489835161380808
    - type: nauc_recall_at_3_diff1
      value: 33.90054781392646
    - type: nauc_recall_at_3_max
      value: 27.778812533030322
    - type: nauc_recall_at_3_std
      value: -0.03054068020022706
    - type: nauc_recall_at_5_diff1
      value: 30.279060732221346
    - type: nauc_recall_at_5_max
      value: 27.49854749597931
    - type: nauc_recall_at_5_std
      value: 0.5434664581939099
    - type: ndcg_at_1
      value: 37.809
    - type: ndcg_at_10
      value: 38.828
    - type: ndcg_at_100
      value: 45.218
    - type: ndcg_at_1000
      value: 48.510999999999996
    - type: ndcg_at_20
      value: 41.11
    - type: ndcg_at_3
      value: 34.466
    - type: ndcg_at_5
      value: 35.843
    - type: precision_at_1
      value: 37.809
    - type: precision_at_10
      value: 11.157
    - type: precision_at_100
      value: 1.762
    - type: precision_at_1000
      value: 0.233
    - type: precision_at_20
      value: 6.497
    - type: precision_at_3
      value: 23.044999999999998
    - type: precision_at_5
      value: 17.284
    - type: recall_at_1
      value: 19.126
    - type: recall_at_10
      value: 46.062
    - type: recall_at_100
      value: 70.22800000000001
    - type: recall_at_1000
      value: 89.803
    - type: recall_at_20
      value: 53.217999999999996
    - type: recall_at_3
      value: 30.847
    - type: recall_at_5
      value: 37.11
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA-PL (default)
      revision: a0bd479ac97b4ccb5bd6ce320c415d0bb4beb907
      split: test
      type: clarin-knext/hotpotqa-pl
    metrics:
    - type: main_score
      value: 60.27
    - type: map_at_1
      value: 35.199000000000005
    - type: map_at_10
      value: 51.369
    - type: map_at_100
      value: 52.212
    - type: map_at_1000
      value: 52.28
    - type: map_at_20
      value: 51.864
    - type: map_at_3
      value: 48.446
    - type: map_at_5
      value: 50.302
    - type: mrr_at_1
      value: 70.39837947332883
    - type: mrr_at_10
      value: 76.8346141067273
    - type: mrr_at_100
      value: 77.10724392048137
    - type: mrr_at_1000
      value: 77.12037412892865
    - type: mrr_at_20
      value: 77.01061532947222
    - type: mrr_at_3
      value: 75.5908170155299
    - type: mrr_at_5
      value: 76.39095205941899
    - type: nauc_map_at_1000_diff1
      value: 24.701387884989117
    - type: nauc_map_at_1000_max
      value: 23.25553235642178
    - type: nauc_map_at_1000_std
      value: 7.1803506915661774
    - type: nauc_map_at_100_diff1
      value: 24.674498622483103
    - type: nauc_map_at_100_max
      value: 23.234948525052175
    - type: nauc_map_at_100_std
      value: 7.168677997105447
    - type: nauc_map_at_10_diff1
      value: 24.676025039755626
    - type: nauc_map_at_10_max
      value: 23.171971872726964
    - type: nauc_map_at_10_std
      value: 6.485610909852058
    - type: nauc_map_at_1_diff1
      value: 68.90178464319715
    - type: nauc_map_at_1_max
      value: 46.05537868917558
    - type: nauc_map_at_1_std
      value: 1.7658552480698708
    - type: nauc_map_at_20_diff1
      value: 24.69297151842494
    - type: nauc_map_at_20_max
      value: 23.213064691673637
    - type: nauc_map_at_20_std
      value: 6.9357946556849
    - type: nauc_map_at_3_diff1
      value: 26.279128947950507
    - type: nauc_map_at_3_max
      value: 23.929537354117922
    - type: nauc_map_at_3_std
      value: 4.625061565714759
    - type: nauc_map_at_5_diff1
      value: 25.04448959482816
    - type: nauc_map_at_5_max
      value: 23.432012857899338
    - type: nauc_map_at_5_std
      value: 5.845744681998008
    - type: nauc_mrr_at_1000_diff1
      value: 66.7503918108276
    - type: nauc_mrr_at_1000_max
      value: 48.42897342336844
    - type: nauc_mrr_at_1000_std
      value: 5.3097517971144415
    - type: nauc_mrr_at_100_diff1
      value: 66.74645215862695
    - type: nauc_mrr_at_100_max
      value: 48.4368663009989
    - type: nauc_mrr_at_100_std
      value: 5.322297898555188
    - type: nauc_mrr_at_10_diff1
      value: 66.69310166180729
    - type: nauc_mrr_at_10_max
      value: 48.475437698330225
    - type: nauc_mrr_at_10_std
      value: 5.258183461631702
    - type: nauc_mrr_at_1_diff1
      value: 68.90178464319715
    - type: nauc_mrr_at_1_max
      value: 46.05537868917558
    - type: nauc_mrr_at_1_std
      value: 1.7658552480698708
    - type: nauc_mrr_at_20_diff1
      value: 66.72000262431975
    - type: nauc_mrr_at_20_max
      value: 48.45593642981319
    - type: nauc_mrr_at_20_std
      value: 5.353665929072101
    - type: nauc_mrr_at_3_diff1
      value: 66.84936676396276
    - type: nauc_mrr_at_3_max
      value: 48.466611276778295
    - type: nauc_mrr_at_3_std
      value: 4.485810398557475
    - type: nauc_mrr_at_5_diff1
      value: 66.62362565394174
    - type: nauc_mrr_at_5_max
      value: 48.456431835482014
    - type: nauc_mrr_at_5_std
      value: 5.08482458391903
    - type: nauc_ndcg_at_1000_diff1
      value: 29.984825173719443
    - type: nauc_ndcg_at_1000_max
      value: 27.289179238639893
    - type: nauc_ndcg_at_1000_std
      value: 10.661480455527526
    - type: nauc_ndcg_at_100_diff1
      value: 29.322074257047877
    - type: nauc_ndcg_at_100_max
      value: 26.850650276220605
    - type: nauc_ndcg_at_100_std
      value: 10.599247982501902
    - type: nauc_ndcg_at_10_diff1
      value: 29.659909113886094
    - type: nauc_ndcg_at_10_max
      value: 26.836139599331005
    - type: nauc_ndcg_at_10_std
      value: 8.12844399452719
    - type: nauc_ndcg_at_1_diff1
      value: 68.90178464319715
    - type: nauc_ndcg_at_1_max
      value: 46.05537868917558
    - type: nauc_ndcg_at_1_std
      value: 1.7658552480698708
    - type: nauc_ndcg_at_20_diff1
      value: 29.510802214854294
    - type: nauc_ndcg_at_20_max
      value: 26.775562637730722
    - type: nauc_ndcg_at_20_std
      value: 9.341342661702363
    - type: nauc_ndcg_at_3_diff1
      value: 32.741885846292966
    - type: nauc_ndcg_at_3_max
      value: 28.44225108761343
    - type: nauc_ndcg_at_3_std
      value: 5.204440768465042
    - type: nauc_ndcg_at_5_diff1
      value: 30.57856348635919
    - type: nauc_ndcg_at_5_max
      value: 27.475007474301698
    - type: nauc_ndcg_at_5_std
      value: 6.961546044312487
    - type: nauc_precision_at_1000_diff1
      value: 0.002113156309413332
    - type: nauc_precision_at_1000_max
      value: 11.198242419541286
    - type: nauc_precision_at_1000_std
      value: 28.69676419166541
    - type: nauc_precision_at_100_diff1
      value: 3.6049575557782627
    - type: nauc_precision_at_100_max
      value: 12.499173524574791
    - type: nauc_precision_at_100_std
      value: 23.3755281004721
    - type: nauc_precision_at_10_diff1
      value: 10.922574784853193
    - type: nauc_precision_at_10_max
      value: 16.23221529562036
    - type: nauc_precision_at_10_std
      value: 12.45014808813857
    - type: nauc_precision_at_1_diff1
      value: 68.90178464319715
    - type: nauc_precision_at_1_max
      value: 46.05537868917558
    - type: nauc_precision_at_1_std
      value: 1.7658552480698708
    - type: nauc_precision_at_20_diff1
      value: 8.840710781302827
    - type: nauc_precision_at_20_max
      value: 14.804644554205524
    - type: nauc_precision_at_20_std
      value: 16.245009770815237
    - type: nauc_precision_at_3_diff1
      value: 19.447291487137573
    - type: nauc_precision_at_3_max
      value: 21.47123471597057
    - type: nauc_precision_at_3_std
      value: 6.441862800128802
    - type: nauc_precision_at_5_diff1
      value: 14.078545719721108
    - type: nauc_precision_at_5_max
      value: 18.468288046016387
    - type: nauc_precision_at_5_std
      value: 9.58650641691393
    - type: nauc_recall_at_1000_diff1
      value: 0.0021131563095336584
    - type: nauc_recall_at_1000_max
      value: 11.198242419541558
    - type: nauc_recall_at_1000_std
      value: 28.6967641916655
    - type: nauc_recall_at_100_diff1
      value: 3.6049575557781393
    - type: nauc_recall_at_100_max
      value: 12.499173524574765
    - type: nauc_recall_at_100_std
      value: 23.375528100472074
    - type: nauc_recall_at_10_diff1
      value: 10.922574784853168
    - type: nauc_recall_at_10_max
      value: 16.2322152956203
    - type: nauc_recall_at_10_std
      value: 12.450148088138535
    - type: nauc_recall_at_1_diff1
      value: 68.90178464319715
    - type: nauc_recall_at_1_max
      value: 46.05537868917558
    - type: nauc_recall_at_1_std
      value: 1.7658552480698708
    - type: nauc_recall_at_20_diff1
      value: 8.840710781302905
    - type: nauc_recall_at_20_max
      value: 14.804644554205515
    - type: nauc_recall_at_20_std
      value: 16.245009770815273
    - type: nauc_recall_at_3_diff1
      value: 19.447291487137498
    - type: nauc_recall_at_3_max
      value: 21.47123471597054
    - type: nauc_recall_at_3_std
      value: 6.441862800128763
    - type: nauc_recall_at_5_diff1
      value: 14.07854571972115
    - type: nauc_recall_at_5_max
      value: 18.468288046016337
    - type: nauc_recall_at_5_std
      value: 9.586506416913904
    - type: ndcg_at_1
      value: 70.39800000000001
    - type: ndcg_at_10
      value: 60.27
    - type: ndcg_at_100
      value: 63.400999999999996
    - type: ndcg_at_1000
      value: 64.847
    - type: ndcg_at_20
      value: 61.571
    - type: ndcg_at_3
      value: 55.875
    - type: ndcg_at_5
      value: 58.36599999999999
    - type: precision_at_1
      value: 70.39800000000001
    - type: precision_at_10
      value: 12.46
    - type: precision_at_100
      value: 1.493
    - type: precision_at_1000
      value: 0.169
    - type: precision_at_20
      value: 6.65
    - type: precision_at_3
      value: 35.062
    - type: precision_at_5
      value: 23.009
    - type: recall_at_1
      value: 35.199000000000005
    - type: recall_at_10
      value: 62.302
    - type: recall_at_100
      value: 74.666
    - type: recall_at_1000
      value: 84.355
    - type: recall_at_20
      value: 66.496
    - type: recall_at_3
      value: 52.593
    - type: recall_at_5
      value: 57.522
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MSMARCO-PL (default)
      revision: 8634c07806d5cce3a6138e260e59b81760a0a640
      split: test
      type: clarin-knext/msmarco-pl
    metrics:
    - type: main_score
      value: 64.886
    - type: map_at_1
      value: 1.644
    - type: map_at_10
      value: 12.24
    - type: map_at_100
      value: 28.248
    - type: map_at_1000
      value: 33.506
    - type: map_at_20
      value: 17.497
    - type: map_at_3
      value: 4.9399999999999995
    - type: map_at_5
      value: 8.272
    - type: mrr_at_1
      value: 83.72093023255815
    - type: mrr_at_10
      value: 91.08527131782945
    - type: mrr_at_100
      value: 91.08527131782945
    - type: mrr_at_1000
      value: 91.08527131782945
    - type: mrr_at_20
      value: 91.08527131782945
    - type: mrr_at_3
      value: 91.08527131782945
    - type: mrr_at_5
      value: 91.08527131782945
    - type: nauc_map_at_1000_diff1
      value: -36.428271627303424
    - type: nauc_map_at_1000_max
      value: 44.87615127218638
    - type: nauc_map_at_1000_std
      value: 67.92696808824724
    - type: nauc_map_at_100_diff1
      value: -28.11674206786188
    - type: nauc_map_at_100_max
      value: 36.422779766334955
    - type: nauc_map_at_100_std
      value: 49.99876313755116
    - type: nauc_map_at_10_diff1
      value: -5.838593619806058
    - type: nauc_map_at_10_max
      value: 11.026519190509742
    - type: nauc_map_at_10_std
      value: 2.5268752263522045
    - type: nauc_map_at_1_diff1
      value: 17.897907271073016
    - type: nauc_map_at_1_max
      value: 12.229062762540844
    - type: nauc_map_at_1_std
      value: -4.088830895573149
    - type: nauc_map_at_20_diff1
      value: -13.871097716255626
    - type: nauc_map_at_20_max
      value: 19.291271635609533
    - type: nauc_map_at_20_std
      value: 16.745335606507826
    - type: nauc_map_at_3_diff1
      value: 4.425238457033843
    - type: nauc_map_at_3_max
      value: 4.611864744680824
    - type: nauc_map_at_3_std
      value: -8.986916608582863
    - type: nauc_map_at_5_diff1
      value: -6.254849256920095
    - type: nauc_map_at_5_max
      value: 2.729437079919823
    - type: nauc_map_at_5_std
      value: -7.235906279913092
    - type: nauc_mrr_at_1000_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_1000_max
      value: 68.26259125411818
    - type: nauc_mrr_at_1000_std
      value: 56.345086428353575
    - type: nauc_mrr_at_100_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_100_max
      value: 68.26259125411818
    - type: nauc_mrr_at_100_std
      value: 56.345086428353575
    - type: nauc_mrr_at_10_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_10_max
      value: 68.26259125411818
    - type: nauc_mrr_at_10_std
      value: 56.345086428353575
    - type: nauc_mrr_at_1_diff1
      value: 56.55126663944154
    - type: nauc_mrr_at_1_max
      value: 66.37014285522565
    - type: nauc_mrr_at_1_std
      value: 53.2508271389779
    - type: nauc_mrr_at_20_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_20_max
      value: 68.26259125411818
    - type: nauc_mrr_at_20_std
      value: 56.345086428353575
    - type: nauc_mrr_at_3_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_3_max
      value: 68.26259125411818
    - type: nauc_mrr_at_3_std
      value: 56.345086428353575
    - type: nauc_mrr_at_5_diff1
      value: 52.18669104947672
    - type: nauc_mrr_at_5_max
      value: 68.26259125411818
    - type: nauc_mrr_at_5_std
      value: 56.345086428353575
    - type: nauc_ndcg_at_1000_diff1
      value: -19.06422926483731
    - type: nauc_ndcg_at_1000_max
      value: 56.30853514590265
    - type: nauc_ndcg_at_1000_std
      value: 70.30810947505557
    - type: nauc_ndcg_at_100_diff1
      value: -25.72587586459692
    - type: nauc_ndcg_at_100_max
      value: 51.433781241604194
    - type: nauc_ndcg_at_100_std
      value: 68.37678512652792
    - type: nauc_ndcg_at_10_diff1
      value: -23.21198108212602
    - type: nauc_ndcg_at_10_max
      value: 43.5450720846516
    - type: nauc_ndcg_at_10_std
      value: 48.78307907005605
    - type: nauc_ndcg_at_1_diff1
      value: 44.00179301267447
    - type: nauc_ndcg_at_1_max
      value: 48.202370455680395
    - type: nauc_ndcg_at_1_std
      value: 25.69655992704088
    - type: nauc_ndcg_at_20_diff1
      value: -33.88168753446507
    - type: nauc_ndcg_at_20_max
      value: 45.16199742613164
    - type: nauc_ndcg_at_20_std
      value: 61.87098383164902
    - type: nauc_ndcg_at_3_diff1
      value: 11.19174449544048
    - type: nauc_ndcg_at_3_max
      value: 44.34069860560555
    - type: nauc_ndcg_at_3_std
      value: 27.451258369798115
    - type: nauc_ndcg_at_5_diff1
      value: -7.186520929432436
    - type: nauc_ndcg_at_5_max
      value: 43.41869981139378
    - type: nauc_ndcg_at_5_std
      value: 34.89898115995178
    - type: nauc_precision_at_1000_diff1
      value: -34.43998154563451
    - type: nauc_precision_at_1000_max
      value: 29.172655907480372
    - type: nauc_precision_at_1000_std
      value: 65.15824469614837
    - type: nauc_precision_at_100_diff1
      value: -37.82409643259692
    - type: nauc_precision_at_100_max
      value: 38.24986991317909
    - type: nauc_precision_at_100_std
      value: 72.74768183105327
    - type: nauc_precision_at_10_diff1
      value: -32.21556182780535
    - type: nauc_precision_at_10_max
      value: 34.27170432382651
    - type: nauc_precision_at_10_std
      value: 58.358255004394664
    - type: nauc_precision_at_1_diff1
      value: 56.55126663944154
    - type: nauc_precision_at_1_max
      value: 66.37014285522565
    - type: nauc_precision_at_1_std
      value: 53.2508271389779
    - type: nauc_precision_at_20_diff1
      value: -40.18751579026395
    - type: nauc_precision_at_20_max
      value: 33.960783153758896
    - type: nauc_precision_at_20_std
      value: 65.42918390184195
    - type: nauc_precision_at_3_diff1
      value: -7.073870209006578
    - type: nauc_precision_at_3_max
      value: 50.81535269862325
    - type: nauc_precision_at_3_std
      value: 59.248681565955685
    - type: nauc_precision_at_5_diff1
      value: -31.136580596983876
    - type: nauc_precision_at_5_max
      value: 45.88147792380426
    - type: nauc_precision_at_5_std
      value: 67.46814230928243
    - type: nauc_recall_at_1000_diff1
      value: -23.15699999594577
    - type: nauc_recall_at_1000_max
      value: 39.77277799761876
    - type: nauc_recall_at_1000_std
      value: 60.326168012901114
    - type: nauc_recall_at_100_diff1
      value: -21.636664823598498
    - type: nauc_recall_at_100_max
      value: 31.104969346131583
    - type: nauc_recall_at_100_std
      value: 38.811686891592096
    - type: nauc_recall_at_10_diff1
      value: -10.542765625053569
    - type: nauc_recall_at_10_max
      value: 2.043876058107446
    - type: nauc_recall_at_10_std
      value: -5.578449908984766
    - type: nauc_recall_at_1_diff1
      value: 17.897907271073016
    - type: nauc_recall_at_1_max
      value: 12.229062762540844
    - type: nauc_recall_at_1_std
      value: -4.088830895573149
    - type: nauc_recall_at_20_diff1
      value: -15.132909355710103
    - type: nauc_recall_at_20_max
      value: 12.659765287241065
    - type: nauc_recall_at_20_std
      value: 8.277887800815819
    - type: nauc_recall_at_3_diff1
      value: -3.1975017812715016
    - type: nauc_recall_at_3_max
      value: -3.5539857085038538
    - type: nauc_recall_at_3_std
      value: -14.712102851318118
    - type: nauc_recall_at_5_diff1
      value: -14.040507717380743
    - type: nauc_recall_at_5_max
      value: -6.126912150131701
    - type: nauc_recall_at_5_std
      value: -13.821624015640355
    - type: ndcg_at_1
      value: 71.318
    - type: ndcg_at_10
      value: 64.886
    - type: ndcg_at_100
      value: 53.187
    - type: ndcg_at_1000
      value: 59.897999999999996
    - type: ndcg_at_20
      value: 58.96
    - type: ndcg_at_3
      value: 69.736
    - type: ndcg_at_5
      value: 70.14099999999999
    - type: precision_at_1
      value: 83.721
    - type: precision_at_10
      value: 71.163
    - type: precision_at_100
      value: 29.465000000000003
    - type: precision_at_1000
      value: 5.665
    - type: precision_at_20
      value: 57.791000000000004
    - type: precision_at_3
      value: 82.171
    - type: precision_at_5
      value: 81.86
    - type: recall_at_1
      value: 1.644
    - type: recall_at_10
      value: 14.238000000000001
    - type: recall_at_100
      value: 39.831
    - type: recall_at_1000
      value: 64.057
    - type: recall_at_20
      value: 21.021
    - type: recall_at_3
      value: 5.53
    - type: recall_at_5
      value: 9.623
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NFCorpus-PL (default)
      revision: 9a6f9567fda928260afed2de480d79c98bf0bec0
      split: test
      type: clarin-knext/nfcorpus-pl
    metrics:
    - type: main_score
      value: 31.391000000000002
    - type: map_at_1
      value: 4.163
    - type: map_at_10
      value: 10.744
    - type: map_at_100
      value: 14.038999999999998
    - type: map_at_1000
      value: 15.434999999999999
    - type: map_at_20
      value: 12.16
    - type: map_at_3
      value: 7.614999999999999
    - type: map_at_5
      value: 9.027000000000001
    - type: mrr_at_1
      value: 39.0092879256966
    - type: mrr_at_10
      value: 48.69809327239668
    - type: mrr_at_100
      value: 49.20788148442068
    - type: mrr_at_1000
      value: 49.25509336494706
    - type: mrr_at_20
      value: 48.99606551850896
    - type: mrr_at_3
      value: 46.284829721362236
    - type: mrr_at_5
      value: 47.77089783281735
    - type: nauc_map_at_1000_diff1
      value: 22.75421477116417
    - type: nauc_map_at_1000_max
      value: 49.242283787799046
    - type: nauc_map_at_1000_std
      value: 29.056888272331832
    - type: nauc_map_at_100_diff1
      value: 23.585977398585594
    - type: nauc_map_at_100_max
      value: 48.25845199409498
    - type: nauc_map_at_100_std
      value: 24.944264511223693
    - type: nauc_map_at_10_diff1
      value: 27.386613094780255
    - type: nauc_map_at_10_max
      value: 41.52415346691586
    - type: nauc_map_at_10_std
      value: 12.93872448563755
    - type: nauc_map_at_1_diff1
      value: 46.78688143865053
    - type: nauc_map_at_1_max
      value: 37.20408843995871
    - type: nauc_map_at_1_std
      value: 4.383444959401098
    - type: nauc_map_at_20_diff1
      value: 25.590969047740288
    - type: nauc_map_at_20_max
      value: 44.57109307999418
    - type: nauc_map_at_20_std
      value: 16.45855141821407
    - type: nauc_map_at_3_diff1
      value: 36.30017108362863
    - type: nauc_map_at_3_max
      value: 34.66149613991648
    - type: nauc_map_at_3_std
      value: 5.67985905078467
    - type: nauc_map_at_5_diff1
      value: 31.157644795417223
    - type: nauc_map_at_5_max
      value: 37.274738661636825
    - type: nauc_map_at_5_std
      value: 8.70088872394168
    - type: nauc_mrr_at_1000_diff1
      value: 25.638564218157384
    - type: nauc_mrr_at_1000_max
      value: 57.77788270285353
    - type: nauc_mrr_at_1000_std
      value: 43.507586592911274
    - type: nauc_mrr_at_100_diff1
      value: 25.662002580561584
    - type: nauc_mrr_at_100_max
      value: 57.80578394278584
    - type: nauc_mrr_at_100_std
      value: 43.543905743986635
    - type: nauc_mrr_at_10_diff1
      value: 25.426034796339835
    - type: nauc_mrr_at_10_max
      value: 57.68443186258669
    - type: nauc_mrr_at_10_std
      value: 43.438009108331215
    - type: nauc_mrr_at_1_diff1
      value: 26.073028156311075
    - type: nauc_mrr_at_1_max
      value: 52.11817916720053
    - type: nauc_mrr_at_1_std
      value: 37.41073893153695
    - type: nauc_mrr_at_20_diff1
      value: 25.548645553336147
    - type: nauc_mrr_at_20_max
      value: 57.78552760401915
    - type: nauc_mrr_at_20_std
      value: 43.521687428822325
    - type: nauc_mrr_at_3_diff1
      value: 25.72662577397805
    - type: nauc_mrr_at_3_max
      value: 56.891263536265605
    - type: nauc_mrr_at_3_std
      value: 41.384872305390104
    - type: nauc_mrr_at_5_diff1
      value: 25.552211551655386
    - type: nauc_mrr_at_5_max
      value: 57.976813828353926
    - type: nauc_mrr_at_5_std
      value: 43.504564461855544
    - type: nauc_ndcg_at_1000_diff1
      value: 23.456158044182757
    - type: nauc_ndcg_at_1000_max
      value: 60.05411773552709
    - type: nauc_ndcg_at_1000_std
      value: 47.857510017262584
    - type: nauc_ndcg_at_100_diff1
      value: 19.711635700390772
    - type: nauc_ndcg_at_100_max
      value: 56.178746740470665
    - type: nauc_ndcg_at_100_std
      value: 42.36829180286942
    - type: nauc_ndcg_at_10_diff1
      value: 18.364428967788413
    - type: nauc_ndcg_at_10_max
      value: 54.38372506578223
    - type: nauc_ndcg_at_10_std
      value: 41.75765411340369
    - type: nauc_ndcg_at_1_diff1
      value: 26.571093272640773
    - type: nauc_ndcg_at_1_max
      value: 51.061788341958284
    - type: nauc_ndcg_at_1_std
      value: 36.514987974075986
    - type: nauc_ndcg_at_20_diff1
      value: 18.345487193027697
    - type: nauc_ndcg_at_20_max
      value: 54.62621882656994
    - type: nauc_ndcg_at_20_std
      value: 41.42835554714241
    - type: nauc_ndcg_at_3_diff1
      value: 23.260105658139025
    - type: nauc_ndcg_at_3_max
      value: 52.07747385334546
    - type: nauc_ndcg_at_3_std
      value: 36.91985577837284
    - type: nauc_ndcg_at_5_diff1
      value: 20.40428109665566
    - type: nauc_ndcg_at_5_max
      value: 53.52015347884604
    - type: nauc_ndcg_at_5_std
      value: 39.46008849580017
    - type: nauc_precision_at_1000_diff1
      value: -7.3487344916380035
    - type: nauc_precision_at_1000_max
      value: 16.58045221394852
    - type: nauc_precision_at_1000_std
      value: 38.94030932397075
    - type: nauc_precision_at_100_diff1
      value: -5.257743986683922
    - type: nauc_precision_at_100_max
      value: 34.43071687475306
    - type: nauc_precision_at_100_std
      value: 53.499519170670474
    - type: nauc_precision_at_10_diff1
      value: 2.385136433119139
    - type: nauc_precision_at_10_max
      value: 47.210743878631064
    - type: nauc_precision_at_10_std
      value: 47.22767704186548
    - type: nauc_precision_at_1_diff1
      value: 26.073028156311075
    - type: nauc_precision_at_1_max
      value: 52.11817916720053
    - type: nauc_precision_at_1_std
      value: 37.41073893153695
    - type: nauc_precision_at_20_diff1
      value: -0.3531531127238474
    - type: nauc_precision_at_20_max
      value: 44.78044604856974
    - type: nauc_precision_at_20_std
      value: 49.532804150743615
    - type: nauc_precision_at_3_diff1
      value: 15.350050569991447
    - type: nauc_precision_at_3_max
      value: 51.01572315596549
    - type: nauc_precision_at_3_std
      value: 38.801125728413155
    - type: nauc_precision_at_5_diff1
      value: 9.109003666144694
    - type: nauc_precision_at_5_max
      value: 50.935269774898494
    - type: nauc_precision_at_5_std
      value: 43.323548180559676
    - type: nauc_recall_at_1000_diff1
      value: 16.64743647648886
    - type: nauc_recall_at_1000_max
      value: 38.46012283772285
    - type: nauc_recall_at_1000_std
      value: 36.02016164796441
    - type: nauc_recall_at_100_diff1
      value: 14.005834785186744
    - type: nauc_recall_at_100_max
      value: 37.70026105513647
    - type: nauc_recall_at_100_std
      value: 27.085222642129697
    - type: nauc_recall_at_10_diff1
      value: 21.204106627422632
    - type: nauc_recall_at_10_max
      value: 36.737624881893424
    - type: nauc_recall_at_10_std
      value: 13.755054514272702
    - type: nauc_recall_at_1_diff1
      value: 46.78688143865053
    - type: nauc_recall_at_1_max
      value: 37.20408843995871
    - type: nauc_recall_at_1_std
      value: 4.383444959401098
    - type: nauc_recall_at_20_diff1
      value: 19.740977611421933
    - type: nauc_recall_at_20_max
      value: 39.21908969539783
    - type: nauc_recall_at_20_std
      value: 16.560269670318494
    - type: nauc_recall_at_3_diff1
      value: 32.189359545367815
    - type: nauc_recall_at_3_max
      value: 31.693634445562758
    - type: nauc_recall_at_3_std
      value: 6.246326281543587
    - type: nauc_recall_at_5_diff1
      value: 25.51586860499901
    - type: nauc_recall_at_5_max
      value: 33.15934725342885
    - type: nauc_recall_at_5_std
      value: 9.677778511696705
    - type: ndcg_at_1
      value: 37.307
    - type: ndcg_at_10
      value: 31.391000000000002
    - type: ndcg_at_100
      value: 28.877999999999997
    - type: ndcg_at_1000
      value: 37.16
    - type: ndcg_at_20
      value: 29.314
    - type: ndcg_at_3
      value: 35.405
    - type: ndcg_at_5
      value: 33.922999999999995
    - type: precision_at_1
      value: 39.009
    - type: precision_at_10
      value: 24.52
    - type: precision_at_100
      value: 7.703
    - type: precision_at_1000
      value: 2.04
    - type: precision_at_20
      value: 18.08
    - type: precision_at_3
      value: 34.469
    - type: precision_at_5
      value: 30.712
    - type: recall_at_1
      value: 4.163
    - type: recall_at_10
      value: 15.015999999999998
    - type: recall_at_100
      value: 30.606
    - type: recall_at_1000
      value: 59.606
    - type: recall_at_20
      value: 19.09
    - type: recall_at_3
      value: 9.139
    - type: recall_at_5
      value: 11.477
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ-PL (default)
      revision: f171245712cf85dd4700b06bef18001578d0ca8d
      split: test
      type: clarin-knext/nq-pl
    metrics:
    - type: main_score
      value: 54.017
    - type: map_at_1
      value: 34.193
    - type: map_at_10
      value: 47.497
    - type: map_at_100
      value: 48.441
    - type: map_at_1000
      value: 48.481
    - type: map_at_20
      value: 48.093
    - type: map_at_3
      value: 44.017
    - type: map_at_5
      value: 46.111000000000004
    - type: mrr_at_1
      value: 37.949015063731174
    - type: mrr_at_10
      value: 49.915772315105954
    - type: mrr_at_100
      value: 50.62841255829997
    - type: mrr_at_1000
      value: 50.656773027666745
    - type: mrr_at_20
      value: 50.37785276657083
    - type: mrr_at_3
      value: 46.98725376593267
    - type: mrr_at_5
      value: 48.763035921205066
    - type: nauc_map_at_1000_diff1
      value: 39.5632191792873
    - type: nauc_map_at_1000_max
      value: 37.4728247053629
    - type: nauc_map_at_1000_std
      value: 5.742498414663762
    - type: nauc_map_at_100_diff1
      value: 39.555570352061906
    - type: nauc_map_at_100_max
      value: 37.497880976847334
    - type: nauc_map_at_100_std
      value: 5.7798021019465375
    - type: nauc_map_at_10_diff1
      value: 39.5423723444454
    - type: nauc_map_at_10_max
      value: 37.41661971723365
    - type: nauc_map_at_10_std
      value: 5.2378002164144695
    - type: nauc_map_at_1_diff1
      value: 41.52697034146981
    - type: nauc_map_at_1_max
      value: 28.558995576942863
    - type: nauc_map_at_1_std
      value: 0.13094542859192052
    - type: nauc_map_at_20_diff1
      value: 39.55484628943701
    - type: nauc_map_at_20_max
      value: 37.5247794933719
    - type: nauc_map_at_20_std
      value: 5.702881342279231
    - type: nauc_map_at_3_diff1
      value: 39.949323925425325
    - type: nauc_map_at_3_max
      value: 35.770298168901924
    - type: nauc_map_at_3_std
      value: 2.9127112432479874
    - type: nauc_map_at_5_diff1
      value: 39.768310617004545
    - type: nauc_map_at_5_max
      value: 37.1549191664796
    - type: nauc_map_at_5_std
      value: 4.4681285748269515
    - type: nauc_mrr_at_1000_diff1
      value: 39.14001746706457
    - type: nauc_mrr_at_1000_max
      value: 37.477376518267775
    - type: nauc_mrr_at_1000_std
      value: 6.8088891531621565
    - type: nauc_mrr_at_100_diff1
      value: 39.13054707413684
    - type: nauc_mrr_at_100_max
      value: 37.498126443766274
    - type: nauc_mrr_at_100_std
      value: 6.839411380129971
    - type: nauc_mrr_at_10_diff1
      value: 39.09764730048156
    - type: nauc_mrr_at_10_max
      value: 37.58593798217306
    - type: nauc_mrr_at_10_std
      value: 6.713795164982413
    - type: nauc_mrr_at_1_diff1
      value: 41.581599918664075
    - type: nauc_mrr_at_1_max
      value: 31.500589231378722
    - type: nauc_mrr_at_1_std
      value: 2.059116370339438
    - type: nauc_mrr_at_20_diff1
      value: 39.09011023988447
    - type: nauc_mrr_at_20_max
      value: 37.55856008791344
    - type: nauc_mrr_at_20_std
      value: 6.847165397615844
    - type: nauc_mrr_at_3_diff1
      value: 39.382542043738
    - type: nauc_mrr_at_3_max
      value: 36.49265363659468
    - type: nauc_mrr_at_3_std
      value: 4.759157976438336
    - type: nauc_mrr_at_5_diff1
      value: 39.304826333759976
    - type: nauc_mrr_at_5_max
      value: 37.46326016736024
    - type: nauc_mrr_at_5_std
      value: 6.122608305766621
    - type: nauc_ndcg_at_1000_diff1
      value: 38.568500038453266
    - type: nauc_ndcg_at_1000_max
      value: 39.799710882413166
    - type: nauc_ndcg_at_1000_std
      value: 9.357010223096639
    - type: nauc_ndcg_at_100_diff1
      value: 38.38026091343228
    - type: nauc_ndcg_at_100_max
      value: 40.48398173542486
    - type: nauc_ndcg_at_100_std
      value: 10.373054013302214
    - type: nauc_ndcg_at_10_diff1
      value: 38.27340980909964
    - type: nauc_ndcg_at_10_max
      value: 40.35241649744093
    - type: nauc_ndcg_at_10_std
      value: 8.579139930345168
    - type: nauc_ndcg_at_1_diff1
      value: 41.581599918664075
    - type: nauc_ndcg_at_1_max
      value: 31.500589231378722
    - type: nauc_ndcg_at_1_std
      value: 2.059116370339438
    - type: nauc_ndcg_at_20_diff1
      value: 38.26453028884807
    - type: nauc_ndcg_at_20_max
      value: 40.70517858426641
    - type: nauc_ndcg_at_20_std
      value: 9.987693876137905
    - type: nauc_ndcg_at_3_diff1
      value: 39.2078971733273
    - type: nauc_ndcg_at_3_max
      value: 37.48672195565316
    - type: nauc_ndcg_at_3_std
      value: 4.051464994659221
    - type: nauc_ndcg_at_5_diff1
      value: 38.883693595665285
    - type: nauc_ndcg_at_5_max
      value: 39.763115634437135
    - type: nauc_ndcg_at_5_std
      value: 6.738980451582073
    - type: nauc_precision_at_1000_diff1
      value: -7.223215910619012
    - type: nauc_precision_at_1000_max
      value: 13.075844604892161
    - type: nauc_precision_at_1000_std
      value: 19.864336920890107
    - type: nauc_precision_at_100_diff1
      value: 1.3305994810812418
    - type: nauc_precision_at_100_max
      value: 25.9219108557104
    - type: nauc_precision_at_100_std
      value: 27.5076605928207
    - type: nauc_precision_at_10_diff1
      value: 18.441551484970326
    - type: nauc_precision_at_10_max
      value: 39.85995330437054
    - type: nauc_precision_at_10_std
      value: 20.561269077428914
    - type: nauc_precision_at_1_diff1
      value: 41.581599918664075
    - type: nauc_precision_at_1_max
      value: 31.500589231378722
    - type: nauc_precision_at_1_std
      value: 2.059116370339438
    - type: nauc_precision_at_20_diff1
      value: 12.579593891480531
    - type: nauc_precision_at_20_max
      value: 36.620221830588775
    - type: nauc_precision_at_20_std
      value: 26.40364876775059
    - type: nauc_precision_at_3_diff1
      value: 30.158859294487073
    - type: nauc_precision_at_3_max
      value: 41.168215766389174
    - type: nauc_precision_at_3_std
      value: 9.44345004450809
    - type: nauc_precision_at_5_diff1
      value: 25.438624678672785
    - type: nauc_precision_at_5_max
      value: 42.72802023518524
    - type: nauc_precision_at_5_std
      value: 15.357657388511099
    - type: nauc_recall_at_1000_diff1
      value: 24.987564782718003
    - type: nauc_recall_at_1000_max
      value: 70.508416373353
    - type: nauc_recall_at_1000_std
      value: 69.75092280398808
    - type: nauc_recall_at_100_diff1
      value: 29.504202856421397
    - type: nauc_recall_at_100_max
      value: 63.41356585545318
    - type: nauc_recall_at_100_std
      value: 50.09250954437847
    - type: nauc_recall_at_10_diff1
      value: 32.355776022971774
    - type: nauc_recall_at_10_max
      value: 49.47121901667283
    - type: nauc_recall_at_10_std
      value: 19.418439406631244
    - type: nauc_recall_at_1_diff1
      value: 41.52697034146981
    - type: nauc_recall_at_1_max
      value: 28.558995576942863
    - type: nauc_recall_at_1_std
      value: 0.13094542859192052
    - type: nauc_recall_at_20_diff1
      value: 31.57334731023589
    - type: nauc_recall_at_20_max
      value: 54.06567225197383
    - type: nauc_recall_at_20_std
      value: 29.222029720570468
    - type: nauc_recall_at_3_diff1
      value: 36.45033533275773
    - type: nauc_recall_at_3_max
      value: 40.39529713780803
    - type: nauc_recall_at_3_std
      value: 5.21893897772794
    - type: nauc_recall_at_5_diff1
      value: 35.18471678478859
    - type: nauc_recall_at_5_max
      value: 46.20100816867823
    - type: nauc_recall_at_5_std
      value: 11.94481894633221
    - type: ndcg_at_1
      value: 37.949
    - type: ndcg_at_10
      value: 54.017
    - type: ndcg_at_100
      value: 58.126
    - type: ndcg_at_1000
      value: 59.073
    - type: ndcg_at_20
      value: 55.928
    - type: ndcg_at_3
      value: 47.494
    - type: ndcg_at_5
      value: 50.975
    - type: precision_at_1
      value: 37.949
    - type: precision_at_10
      value: 8.450000000000001
    - type: precision_at_100
      value: 1.083
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_20
      value: 4.689
    - type: precision_at_3
      value: 21.051000000000002
    - type: precision_at_5
      value: 14.664
    - type: recall_at_1
      value: 34.193
    - type: recall_at_10
      value: 71.357
    - type: recall_at_100
      value: 89.434
    - type: recall_at_1000
      value: 96.536
    - type: recall_at_20
      value: 78.363
    - type: recall_at_3
      value: 54.551
    - type: recall_at_5
      value: 62.543000000000006
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Quora-PL (default)
      revision: 0be27e93455051e531182b85e85e425aba12e9d4
      split: test
      type: clarin-knext/quora-pl
    metrics:
    - type: main_score
      value: 84.114
    - type: map_at_1
      value: 65.848
    - type: map_at_10
      value: 79.85900000000001
    - type: map_at_100
      value: 80.582
    - type: map_at_1000
      value: 80.60300000000001
    - type: map_at_20
      value: 80.321
    - type: map_at_3
      value: 76.741
    - type: map_at_5
      value: 78.72200000000001
    - type: mrr_at_1
      value: 75.97
    - type: mrr_at_10
      value: 83.04630158730119
    - type: mrr_at_100
      value: 83.22785731032968
    - type: mrr_at_1000
      value: 83.23123717623899
    - type: mrr_at_20
      value: 83.17412021320565
    - type: mrr_at_3
      value: 81.83333333333287
    - type: mrr_at_5
      value: 82.61933333333275
    - type: nauc_map_at_1000_diff1
      value: 73.26316553371083
    - type: nauc_map_at_1000_max
      value: 27.92567859085245
    - type: nauc_map_at_1000_std
      value: -47.477909533360446
    - type: nauc_map_at_100_diff1
      value: 73.2690602807223
    - type: nauc_map_at_100_max
      value: 27.915868327849996
    - type: nauc_map_at_100_std
      value: -47.525777766107595
    - type: nauc_map_at_10_diff1
      value: 73.45464428464894
    - type: nauc_map_at_10_max
      value: 27.451611487246296
    - type: nauc_map_at_10_std
      value: -49.35818715843809
    - type: nauc_map_at_1_diff1
      value: 77.29690208952982
    - type: nauc_map_at_1_max
      value: 19.839875762282293
    - type: nauc_map_at_1_std
      value: -45.355684654708284
    - type: nauc_map_at_20_diff1
      value: 73.35102731979796
    - type: nauc_map_at_20_max
      value: 27.741506490134583
    - type: nauc_map_at_20_std
      value: -48.22006207310331
    - type: nauc_map_at_3_diff1
      value: 73.94878241064137
    - type: nauc_map_at_3_max
      value: 24.761321386766728
    - type: nauc_map_at_3_std
      value: -51.20638883618126
    - type: nauc_map_at_5_diff1
      value: 73.66143558047698
    - type: nauc_map_at_5_max
      value: 26.53483405013543
    - type: nauc_map_at_5_std
      value: -50.697541279640056
    - type: nauc_mrr_at_1000_diff1
      value: 73.84632320009759
    - type: nauc_mrr_at_1000_max
      value: 30.50182733610048
    - type: nauc_mrr_at_1000_std
      value: -44.3021647995251
    - type: nauc_mrr_at_100_diff1
      value: 73.84480792662302
    - type: nauc_mrr_at_100_max
      value: 30.50749424571614
    - type: nauc_mrr_at_100_std
      value: -44.29615086388113
    - type: nauc_mrr_at_10_diff1
      value: 73.79442772949346
    - type: nauc_mrr_at_10_max
      value: 30.55724252219984
    - type: nauc_mrr_at_10_std
      value: -44.50997069462057
    - type: nauc_mrr_at_1_diff1
      value: 75.23369827945945
    - type: nauc_mrr_at_1_max
      value: 29.20073967447664
    - type: nauc_mrr_at_1_std
      value: -43.1920147658285
    - type: nauc_mrr_at_20_diff1
      value: 73.82731678072307
    - type: nauc_mrr_at_20_max
      value: 30.566328605497667
    - type: nauc_mrr_at_20_std
      value: -44.24683607643705
    - type: nauc_mrr_at_3_diff1
      value: 73.61997576749954
    - type: nauc_mrr_at_3_max
      value: 30.150393853381917
    - type: nauc_mrr_at_3_std
      value: -44.96847297506626
    - type: nauc_mrr_at_5_diff1
      value: 73.69084310616132
    - type: nauc_mrr_at_5_max
      value: 30.578033703441125
    - type: nauc_mrr_at_5_std
      value: -44.74920746066566
    - type: nauc_ndcg_at_1000_diff1
      value: 72.89349862557452
    - type: nauc_ndcg_at_1000_max
      value: 29.824725190462086
    - type: nauc_ndcg_at_1000_std
      value: -44.96284395063211
    - type: nauc_ndcg_at_100_diff1
      value: 72.85212753715273
    - type: nauc_ndcg_at_100_max
      value: 29.933114207845605
    - type: nauc_ndcg_at_100_std
      value: -44.944225570663754
    - type: nauc_ndcg_at_10_diff1
      value: 72.80576740454528
    - type: nauc_ndcg_at_10_max
      value: 29.16829118320828
    - type: nauc_ndcg_at_10_std
      value: -48.149473740079614
    - type: nauc_ndcg_at_1_diff1
      value: 75.00032534968587
    - type: nauc_ndcg_at_1_max
      value: 29.61849062038547
    - type: nauc_ndcg_at_1_std
      value: -42.560207043864054
    - type: nauc_ndcg_at_20_diff1
      value: 72.88440406302502
    - type: nauc_ndcg_at_20_max
      value: 29.65496676092656
    - type: nauc_ndcg_at_20_std
      value: -46.21238462167732
    - type: nauc_ndcg_at_3_diff1
      value: 72.37916962766987
    - type: nauc_ndcg_at_3_max
      value: 27.125094834547586
    - type: nauc_ndcg_at_3_std
      value: -48.62942991399391
    - type: nauc_ndcg_at_5_diff1
      value: 72.57017330527658
    - type: nauc_ndcg_at_5_max
      value: 28.470485561757254
    - type: nauc_ndcg_at_5_std
      value: -49.07593345591059
    - type: nauc_precision_at_1000_diff1
      value: -41.67915575853946
    - type: nauc_precision_at_1000_max
      value: 1.2012264478568844
    - type: nauc_precision_at_1000_std
      value: 44.723834559400466
    - type: nauc_precision_at_100_diff1
      value: -40.45196679236971
    - type: nauc_precision_at_100_max
      value: 2.3525450401714894
    - type: nauc_precision_at_100_std
      value: 43.7092529413952
    - type: nauc_precision_at_10_diff1
      value: -30.256026923068767
    - type: nauc_precision_at_10_max
      value: 8.313422052132559
    - type: nauc_precision_at_10_std
      value: 25.929372356449694
    - type: nauc_precision_at_1_diff1
      value: 75.00032534968587
    - type: nauc_precision_at_1_max
      value: 29.61849062038547
    - type: nauc_precision_at_1_std
      value: -42.560207043864054
    - type: nauc_precision_at_20_diff1
      value: -35.61971069986584
    - type: nauc_precision_at_20_max
      value: 5.4664303079116765
    - type: nauc_precision_at_20_std
      value: 34.992352471692826
    - type: nauc_precision_at_3_diff1
      value: -5.691231842471157
    - type: nauc_precision_at_3_max
      value: 14.797949087742444
    - type: nauc_precision_at_3_std
      value: -0.1930317395644928
    - type: nauc_precision_at_5_diff1
      value: -20.03913781462645
    - type: nauc_precision_at_5_max
      value: 11.956771408712749
    - type: nauc_precision_at_5_std
      value: 13.179251389859731
    - type: nauc_recall_at_1000_diff1
      value: 64.03509042729674
    - type: nauc_recall_at_1000_max
      value: 40.91691485428493
    - type: nauc_recall_at_1000_std
      value: 16.12968625875372
    - type: nauc_recall_at_100_diff1
      value: 63.83116179628575
    - type: nauc_recall_at_100_max
      value: 43.72908117676382
    - type: nauc_recall_at_100_std
      value: -20.50966716852155
    - type: nauc_recall_at_10_diff1
      value: 66.42071960186394
    - type: nauc_recall_at_10_max
      value: 28.983207818687205
    - type: nauc_recall_at_10_std
      value: -56.61417798753744
    - type: nauc_recall_at_1_diff1
      value: 77.29690208952982
    - type: nauc_recall_at_1_max
      value: 19.839875762282293
    - type: nauc_recall_at_1_std
      value: -45.355684654708284
    - type: nauc_recall_at_20_diff1
      value: 66.32360705219874
    - type: nauc_recall_at_20_max
      value: 33.30698111822631
    - type: nauc_recall_at_20_std
      value: -43.89233781737452
    - type: nauc_recall_at_3_diff1
      value: 69.67029394927077
    - type: nauc_recall_at_3_max
      value: 22.67803039327696
    - type: nauc_recall_at_3_std
      value: -56.43327209861502
    - type: nauc_recall_at_5_diff1
      value: 68.05622143936131
    - type: nauc_recall_at_5_max
      value: 26.67795559040675
    - type: nauc_recall_at_5_std
      value: -58.158231198510954
    - type: ndcg_at_1
      value: 76.08
    - type: ndcg_at_10
      value: 84.114
    - type: ndcg_at_100
      value: 85.784
    - type: ndcg_at_1000
      value: 85.992
    - type: ndcg_at_20
      value: 84.976
    - type: ndcg_at_3
      value: 80.74799999999999
    - type: ndcg_at_5
      value: 82.626
    - type: precision_at_1
      value: 76.08
    - type: precision_at_10
      value: 12.926000000000002
    - type: precision_at_100
      value: 1.509
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_20
      value: 6.912999999999999
    - type: precision_at_3
      value: 35.5
    - type: precision_at_5
      value: 23.541999999999998
    - type: recall_at_1
      value: 65.848
    - type: recall_at_10
      value: 92.611
    - type: recall_at_100
      value: 98.69
    - type: recall_at_1000
      value: 99.83999999999999
    - type: recall_at_20
      value: 95.47200000000001
    - type: recall_at_3
      value: 83.122
    - type: recall_at_5
      value: 88.23
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SCIDOCS-PL (default)
      revision: 45452b03f05560207ef19149545f168e596c9337
      split: test
      type: clarin-knext/scidocs-pl
    metrics:
    - type: main_score
      value: 15.379999999999999
    - type: map_at_1
      value: 3.6029999999999998
    - type: map_at_10
      value: 8.843
    - type: map_at_100
      value: 10.433
    - type: map_at_1000
      value: 10.689
    - type: map_at_20
      value: 9.597
    - type: map_at_3
      value: 6.363
    - type: map_at_5
      value: 7.603
    - type: mrr_at_1
      value: 17.7
    - type: mrr_at_10
      value: 26.58900793650793
    - type: mrr_at_100
      value: 27.699652322890987
    - type: mrr_at_1000
      value: 27.78065313118353
    - type: mrr_at_20
      value: 27.215020950411816
    - type: mrr_at_3
      value: 23.36666666666668
    - type: mrr_at_5
      value: 25.211666666666666
    - type: nauc_map_at_1000_diff1
      value: 21.92235143827129
    - type: nauc_map_at_1000_max
      value: 37.50300940750989
    - type: nauc_map_at_1000_std
      value: 20.872586122198552
    - type: nauc_map_at_100_diff1
      value: 21.917408170465833
    - type: nauc_map_at_100_max
      value: 37.4654466815513
    - type: nauc_map_at_100_std
      value: 20.621643878648534
    - type: nauc_map_at_10_diff1
      value: 22.914388723621183
    - type: nauc_map_at_10_max
      value: 36.468131213468794
    - type: nauc_map_at_10_std
      value: 16.760980140791492
    - type: nauc_map_at_1_diff1
      value: 29.00799502838457
    - type: nauc_map_at_1_max
      value: 26.64926291797503
    - type: nauc_map_at_1_std
      value: 8.167291261637361
    - type: nauc_map_at_20_diff1
      value: 22.46580947804047
    - type: nauc_map_at_20_max
      value: 36.656294842562275
    - type: nauc_map_at_20_std
      value: 18.099232417722078
    - type: nauc_map_at_3_diff1
      value: 23.436009032045934
    - type: nauc_map_at_3_max
      value: 31.325807212280914
    - type: nauc_map_at_3_std
      value: 9.780905232048852
    - type: nauc_map_at_5_diff1
      value: 22.891704394665528
    - type: nauc_map_at_5_max
      value: 35.40584466642894
    - type: nauc_map_at_5_std
      value: 13.476986099394656
    - type: nauc_mrr_at_1000_diff1
      value: 25.052937655397866
    - type: nauc_mrr_at_1000_max
      value: 29.64431912670108
    - type: nauc_mrr_at_1000_std
      value: 14.549744963988044
    - type: nauc_mrr_at_100_diff1
      value: 25.070871266969224
    - type: nauc_mrr_at_100_max
      value: 29.68743604652336
    - type: nauc_mrr_at_100_std
      value: 14.582010154574432
    - type: nauc_mrr_at_10_diff1
      value: 24.88881466938897
    - type: nauc_mrr_at_10_max
      value: 29.488430770768144
    - type: nauc_mrr_at_10_std
      value: 14.269241073852266
    - type: nauc_mrr_at_1_diff1
      value: 29.220540327267503
    - type: nauc_mrr_at_1_max
      value: 26.81908580507911
    - type: nauc_mrr_at_1_std
      value: 8.00840295809718
    - type: nauc_mrr_at_20_diff1
      value: 25.067912695721944
    - type: nauc_mrr_at_20_max
      value: 29.759227563849628
    - type: nauc_mrr_at_20_std
      value: 14.685076859257357
    - type: nauc_mrr_at_3_diff1
      value: 24.645848739182696
    - type: nauc_mrr_at_3_max
      value: 27.73368549660351
    - type: nauc_mrr_at_3_std
      value: 11.475742805586943
    - type: nauc_mrr_at_5_diff1
      value: 24.895295760909946
    - type: nauc_mrr_at_5_max
      value: 29.130755033240423
    - type: nauc_mrr_at_5_std
      value: 12.955802929145404
    - type: nauc_ndcg_at_1000_diff1
      value: 20.68434434777729
    - type: nauc_ndcg_at_1000_max
      value: 37.67055146424174
    - type: nauc_ndcg_at_1000_std
      value: 29.57493715069776
    - type: nauc_ndcg_at_100_diff1
      value: 20.396834816492383
    - type: nauc_ndcg_at_100_max
      value: 37.460575228670514
    - type: nauc_ndcg_at_100_std
      value: 27.826534756761944
    - type: nauc_ndcg_at_10_diff1
      value: 22.640844106236027
    - type: nauc_ndcg_at_10_max
      value: 35.21291764462327
    - type: nauc_ndcg_at_10_std
      value: 19.53289455984506
    - type: nauc_ndcg_at_1_diff1
      value: 29.220540327267503
    - type: nauc_ndcg_at_1_max
      value: 26.81908580507911
    - type: nauc_ndcg_at_1_std
      value: 8.00840295809718
    - type: nauc_ndcg_at_20_diff1
      value: 22.117126657768623
    - type: nauc_ndcg_at_20_max
      value: 35.79395781940806
    - type: nauc_ndcg_at_20_std
      value: 22.242748346260786
    - type: nauc_ndcg_at_3_diff1
      value: 23.00596063212187
    - type: nauc_ndcg_at_3_max
      value: 30.149013627580523
    - type: nauc_ndcg_at_3_std
      value: 11.07904064662722
    - type: nauc_ndcg_at_5_diff1
      value: 22.81875419630523
    - type: nauc_ndcg_at_5_max
      value: 34.24267468356626
    - type: nauc_ndcg_at_5_std
      value: 15.307780280752088
    - type: nauc_precision_at_1000_diff1
      value: 9.606677689029972
    - type: nauc_precision_at_1000_max
      value: 32.74855550489271
    - type: nauc_precision_at_1000_std
      value: 42.65372585937895
    - type: nauc_precision_at_100_diff1
      value: 11.528981313529545
    - type: nauc_precision_at_100_max
      value: 35.642529490132404
    - type: nauc_precision_at_100_std
      value: 38.146151426052306
    - type: nauc_precision_at_10_diff1
      value: 18.783957183811836
    - type: nauc_precision_at_10_max
      value: 36.1982008334257
    - type: nauc_precision_at_10_std
      value: 25.09349473195891
    - type: nauc_precision_at_1_diff1
      value: 29.220540327267503
    - type: nauc_precision_at_1_max
      value: 26.81908580507911
    - type: nauc_precision_at_1_std
      value: 8.00840295809718
    - type: nauc_precision_at_20_diff1
      value: 17.458766320828214
    - type: nauc_precision_at_20_max
      value: 36.000404903025235
    - type: nauc_precision_at_20_std
      value: 29.1608044138323
    - type: nauc_precision_at_3_diff1
      value: 20.213669462067166
    - type: nauc_precision_at_3_max
      value: 31.120650847205912
    - type: nauc_precision_at_3_std
      value: 12.390972418818118
    - type: nauc_precision_at_5_diff1
      value: 20.114245715785678
    - type: nauc_precision_at_5_max
      value: 37.30360111495823
    - type: nauc_precision_at_5_std
      value: 19.053109037822853
    - type: nauc_recall_at_1000_diff1
      value: 9.85800049032612
    - type: nauc_recall_at_1000_max
      value: 32.48319160802687
    - type: nauc_recall_at_1000_std
      value: 43.79941601741161
    - type: nauc_recall_at_100_diff1
      value: 11.375255270968337
    - type: nauc_recall_at_100_max
      value: 35.1868784124497
    - type: nauc_recall_at_100_std
      value: 38.422680583482666
    - type: nauc_recall_at_10_diff1
      value: 18.445783123521938
    - type: nauc_recall_at_10_max
      value: 35.633267936276766
    - type: nauc_recall_at_10_std
      value: 24.94469506254716
    - type: nauc_recall_at_1_diff1
      value: 29.00799502838457
    - type: nauc_recall_at_1_max
      value: 26.64926291797503
    - type: nauc_recall_at_1_std
      value: 8.167291261637361
    - type: nauc_recall_at_20_diff1
      value: 17.314906604151936
    - type: nauc_recall_at_20_max
      value: 35.66067699203996
    - type: nauc_recall_at_20_std
      value: 29.400137012506082
    - type: nauc_recall_at_3_diff1
      value: 19.873710875648698
    - type: nauc_recall_at_3_max
      value: 30.92404718742849
    - type: nauc_recall_at_3_std
      value: 12.400871018075199
    - type: nauc_recall_at_5_diff1
      value: 19.869948324233192
    - type: nauc_recall_at_5_max
      value: 37.06832511687574
    - type: nauc_recall_at_5_std
      value: 19.0798814966156
    - type: ndcg_at_1
      value: 17.7
    - type: ndcg_at_10
      value: 15.379999999999999
    - type: ndcg_at_100
      value: 22.09
    - type: ndcg_at_1000
      value: 27.151999999999997
    - type: ndcg_at_20
      value: 17.576
    - type: ndcg_at_3
      value: 14.219999999999999
    - type: ndcg_at_5
      value: 12.579
    - type: precision_at_1
      value: 17.7
    - type: precision_at_10
      value: 8.08
    - type: precision_at_100
      value: 1.7840000000000003
    - type: precision_at_1000
      value: 0.3
    - type: precision_at_20
      value: 5.305
    - type: precision_at_3
      value: 13.167000000000002
    - type: precision_at_5
      value: 11.06
    - type: recall_at_1
      value: 3.6029999999999998
    - type: recall_at_10
      value: 16.413
    - type: recall_at_100
      value: 36.263
    - type: recall_at_1000
      value: 61.016999999999996
    - type: recall_at_20
      value: 21.587999999999997
    - type: recall_at_3
      value: 8.013
    - type: recall_at_5
      value: 11.198
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SciFact-PL (default)
      revision: 47932a35f045ef8ed01ba82bf9ff67f6e109207e
      split: test
      type: clarin-knext/scifact-pl
    metrics:
    - type: main_score
      value: 64.764
    - type: map_at_1
      value: 49.778
    - type: map_at_10
      value: 59.88
    - type: map_at_100
      value: 60.707
    - type: map_at_1000
      value: 60.729
    - type: map_at_20
      value: 60.419999999999995
    - type: map_at_3
      value: 57.45400000000001
    - type: map_at_5
      value: 58.729
    - type: mrr_at_1
      value: 52.33333333333333
    - type: mrr_at_10
      value: 61.29193121693122
    - type: mrr_at_100
      value: 61.95817765126313
    - type: mrr_at_1000
      value: 61.97583284368782
    - type: mrr_at_20
      value: 61.72469949641003
    - type: mrr_at_3
      value: 59.44444444444444
    - type: mrr_at_5
      value: 60.494444444444454
    - type: nauc_map_at_1000_diff1
      value: 62.21235294015774
    - type: nauc_map_at_1000_max
      value: 48.83996609100249
    - type: nauc_map_at_1000_std
      value: 5.23892781043174
    - type: nauc_map_at_100_diff1
      value: 62.20170226789429
    - type: nauc_map_at_100_max
      value: 48.8391766453537
    - type: nauc_map_at_100_std
      value: 5.2664077457917715
    - type: nauc_map_at_10_diff1
      value: 61.961975488329024
    - type: nauc_map_at_10_max
      value: 48.397109987625186
    - type: nauc_map_at_10_std
      value: 4.314859710827481
    - type: nauc_map_at_1_diff1
      value: 65.0865197011516
    - type: nauc_map_at_1_max
      value: 41.38862781954889
    - type: nauc_map_at_1_std
      value: -0.9182122632530586
    - type: nauc_map_at_20_diff1
      value: 61.99173935851292
    - type: nauc_map_at_20_max
      value: 48.79961814179307
    - type: nauc_map_at_20_std
      value: 5.262181845825118
    - type: nauc_map_at_3_diff1
      value: 62.37910539880477
    - type: nauc_map_at_3_max
      value: 47.13627890977091
    - type: nauc_map_at_3_std
      value: 2.327897198087264
    - type: nauc_map_at_5_diff1
      value: 61.60080757149592
    - type: nauc_map_at_5_max
      value: 47.60052458345962
    - type: nauc_map_at_5_std
      value: 3.1770196981231047
    - type: nauc_mrr_at_1000_diff1
      value: 62.86810952814966
    - type: nauc_mrr_at_1000_max
      value: 52.13248094447774
    - type: nauc_mrr_at_1000_std
      value: 10.100485746570733
    - type: nauc_mrr_at_100_diff1
      value: 62.85364829491874
    - type: nauc_mrr_at_100_max
      value: 52.134528010631854
    - type: nauc_mrr_at_100_std
      value: 10.120945685447369
    - type: nauc_mrr_at_10_diff1
      value: 62.65679301829915
    - type: nauc_mrr_at_10_max
      value: 52.09270719182349
    - type: nauc_mrr_at_10_std
      value: 9.913834434725441
    - type: nauc_mrr_at_1_diff1
      value: 66.84108271415636
    - type: nauc_mrr_at_1_max
      value: 46.67646429855176
    - type: nauc_mrr_at_1_std
      value: 5.5505252956352304
    - type: nauc_mrr_at_20_diff1
      value: 62.72473227039611
    - type: nauc_mrr_at_20_max
      value: 52.13479097802757
    - type: nauc_mrr_at_20_std
      value: 10.188278833464084
    - type: nauc_mrr_at_3_diff1
      value: 63.797429185518496
    - type: nauc_mrr_at_3_max
      value: 52.16486999573481
    - type: nauc_mrr_at_3_std
      value: 9.094360767062762
    - type: nauc_mrr_at_5_diff1
      value: 62.592917975475494
    - type: nauc_mrr_at_5_max
      value: 52.330741486107414
    - type: nauc_mrr_at_5_std
      value: 9.742175534421389
    - type: nauc_ndcg_at_1000_diff1
      value: 61.38859337672476
    - type: nauc_ndcg_at_1000_max
      value: 51.48380058339184
    - type: nauc_ndcg_at_1000_std
      value: 9.670547660897673
    - type: nauc_ndcg_at_100_diff1
      value: 61.02438489641434
    - type: nauc_ndcg_at_100_max
      value: 51.781246646780865
    - type: nauc_ndcg_at_100_std
      value: 10.592961553245187
    - type: nauc_ndcg_at_10_diff1
      value: 60.03678353308358
    - type: nauc_ndcg_at_10_max
      value: 50.70725688848762
    - type: nauc_ndcg_at_10_std
      value: 7.9472446491016315
    - type: nauc_ndcg_at_1_diff1
      value: 66.84108271415636
    - type: nauc_ndcg_at_1_max
      value: 46.67646429855176
    - type: nauc_ndcg_at_1_std
      value: 5.5505252956352304
    - type: nauc_ndcg_at_20_diff1
      value: 59.828482718480224
    - type: nauc_ndcg_at_20_max
      value: 51.45831789601284
    - type: nauc_ndcg_at_20_std
      value: 10.722673683272049
    - type: nauc_ndcg_at_3_diff1
      value: 61.68982937524109
    - type: nauc_ndcg_at_3_max
      value: 49.745326748604775
    - type: nauc_ndcg_at_3_std
      value: 4.948298621202247
    - type: nauc_ndcg_at_5_diff1
      value: 59.67396171973207
    - type: nauc_ndcg_at_5_max
      value: 49.87855139298281
    - type: nauc_ndcg_at_5_std
      value: 6.08990428055584
    - type: nauc_precision_at_1000_diff1
      value: -1.594227972036865
    - type: nauc_precision_at_1000_max
      value: 32.48431723086185
    - type: nauc_precision_at_1000_std
      value: 53.84748466965268
    - type: nauc_precision_at_100_diff1
      value: 8.06411455192293
    - type: nauc_precision_at_100_max
      value: 39.91003601878948
    - type: nauc_precision_at_100_std
      value: 55.52979711075091
    - type: nauc_precision_at_10_diff1
      value: 26.610514456014066
    - type: nauc_precision_at_10_max
      value: 47.09062494321172
    - type: nauc_precision_at_10_std
      value: 33.91984226498748
    - type: nauc_precision_at_1_diff1
      value: 66.84108271415636
    - type: nauc_precision_at_1_max
      value: 46.67646429855176
    - type: nauc_precision_at_1_std
      value: 5.5505252956352304
    - type: nauc_precision_at_20_diff1
      value: 16.947688843085583
    - type: nauc_precision_at_20_max
      value: 45.40488186572008
    - type: nauc_precision_at_20_std
      value: 48.354421924500905
    - type: nauc_precision_at_3_diff1
      value: 49.11263981720622
    - type: nauc_precision_at_3_max
      value: 52.7084625111683
    - type: nauc_precision_at_3_std
      value: 16.734612173556453
    - type: nauc_precision_at_5_diff1
      value: 39.06503705015792
    - type: nauc_precision_at_5_max
      value: 52.21710506893391
    - type: nauc_precision_at_5_std
      value: 23.350948149460233
    - type: nauc_recall_at_1000_diff1
      value: 43.1559290382817
    - type: nauc_recall_at_1000_max
      value: 83.66013071895456
    - type: nauc_recall_at_1000_std
      value: 86.27450980392177
    - type: nauc_recall_at_100_diff1
      value: 46.016860850620375
    - type: nauc_recall_at_100_max
      value: 69.3944888744547
    - type: nauc_recall_at_100_std
      value: 55.286945696152735
    - type: nauc_recall_at_10_diff1
      value: 49.65877895350921
    - type: nauc_recall_at_10_max
      value: 53.02636695700889
    - type: nauc_recall_at_10_std
      value: 13.967608945823828
    - type: nauc_recall_at_1_diff1
      value: 65.0865197011516
    - type: nauc_recall_at_1_max
      value: 41.38862781954889
    - type: nauc_recall_at_1_std
      value: -0.9182122632530586
    - type: nauc_recall_at_20_diff1
      value: 43.355308229973524
    - type: nauc_recall_at_20_max
      value: 57.04187909533764
    - type: nauc_recall_at_20_std
      value: 33.578720846660524
    - type: nauc_recall_at_3_diff1
      value: 56.922996057428165
    - type: nauc_recall_at_3_max
      value: 50.74417041895424
    - type: nauc_recall_at_3_std
      value: 5.623890124328387
    - type: nauc_recall_at_5_diff1
      value: 50.55620076865238
    - type: nauc_recall_at_5_max
      value: 51.3316854622085
    - type: nauc_recall_at_5_std
      value: 8.995457887269255
    - type: ndcg_at_1
      value: 52.333
    - type: ndcg_at_10
      value: 64.764
    - type: ndcg_at_100
      value: 68.167
    - type: ndcg_at_1000
      value: 68.816
    - type: ndcg_at_20
      value: 66.457
    - type: ndcg_at_3
      value: 60.346
    - type: ndcg_at_5
      value: 62.365
    - type: precision_at_1
      value: 52.333
    - type: precision_at_10
      value: 8.799999999999999
    - type: precision_at_100
      value: 1.057
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_20
      value: 4.8
    - type: precision_at_3
      value: 23.889
    - type: precision_at_5
      value: 15.6
    - type: recall_at_1
      value: 49.778
    - type: recall_at_10
      value: 78.206
    - type: recall_at_100
      value: 93.10000000000001
    - type: recall_at_1000
      value: 98.333
    - type: recall_at_20
      value: 84.467
    - type: recall_at_3
      value: 66.367
    - type: recall_at_5
      value: 71.35000000000001
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID-PL (default)
      revision: 81bcb408f33366c2a20ac54adafad1ae7e877fdd
      split: test
      type: clarin-knext/trec-covid-pl
    metrics:
    - type: main_score
      value: 72.18900000000001
    - type: map_at_1
      value: 0.214
    - type: map_at_10
      value: 1.755
    - type: map_at_100
      value: 9.944
    - type: map_at_1000
      value: 24.205
    - type: map_at_20
      value: 3.1510000000000002
    - type: map_at_3
      value: 0.6
    - type: map_at_5
      value: 0.9560000000000001
    - type: mrr_at_1
      value: 82.0
    - type: mrr_at_10
      value: 89.06666666666666
    - type: mrr_at_100
      value: 89.06666666666666
    - type: mrr_at_1000
      value: 89.06666666666666
    - type: mrr_at_20
      value: 89.06666666666666
    - type: mrr_at_3
      value: 87.66666666666666
    - type: mrr_at_5
      value: 89.06666666666666
    - type: nauc_map_at_1000_diff1
      value: -9.342037623635543
    - type: nauc_map_at_1000_max
      value: 45.71499810252398
    - type: nauc_map_at_1000_std
      value: 76.86482845196852
    - type: nauc_map_at_100_diff1
      value: -6.932395299866198
    - type: nauc_map_at_100_max
      value: 36.097801891181604
    - type: nauc_map_at_100_std
      value: 65.6085215411685
    - type: nauc_map_at_10_diff1
      value: -6.3654843824342775
    - type: nauc_map_at_10_max
      value: 9.564437521432714
    - type: nauc_map_at_10_std
      value: 21.8377319336476
    - type: nauc_map_at_1_diff1
      value: 8.269590874255034
    - type: nauc_map_at_1_max
      value: 3.482498491294516
    - type: nauc_map_at_1_std
      value: 8.985226819412189
    - type: nauc_map_at_20_diff1
      value: -4.971435767877232
    - type: nauc_map_at_20_max
      value: 22.88801858567121
    - type: nauc_map_at_20_std
      value: 32.38492618534027
    - type: nauc_map_at_3_diff1
      value: 1.1615973694623123
    - type: nauc_map_at_3_max
      value: 1.935417800315643
    - type: nauc_map_at_3_std
      value: 10.289328305818698
    - type: nauc_map_at_5_diff1
      value: -2.4675967231444105
    - type: nauc_map_at_5_max
      value: 2.4611483736622373
    - type: nauc_map_at_5_std
      value: 15.082324305750811
    - type: nauc_mrr_at_1000_diff1
      value: 13.098526703499063
    - type: nauc_mrr_at_1000_max
      value: 56.37362177417431
    - type: nauc_mrr_at_1000_std
      value: 73.2456769749587
    - type: nauc_mrr_at_100_diff1
      value: 13.098526703499063
    - type: nauc_mrr_at_100_max
      value: 56.37362177417431
    - type: nauc_mrr_at_100_std
      value: 73.2456769749587
    - type: nauc_mrr_at_10_diff1
      value: 13.098526703499063
    - type: nauc_mrr_at_10_max
      value: 56.37362177417431
    - type: nauc_mrr_at_10_std
      value: 73.2456769749587
    - type: nauc_mrr_at_1_diff1
      value: 12.099350148694809
    - type: nauc_mrr_at_1_max
      value: 53.75041304108387
    - type: nauc_mrr_at_1_std
      value: 68.84018063663402
    - type: nauc_mrr_at_20_diff1
      value: 13.098526703499063
    - type: nauc_mrr_at_20_max
      value: 56.37362177417431
    - type: nauc_mrr_at_20_std
      value: 73.2456769749587
    - type: nauc_mrr_at_3_diff1
      value: 12.173557857011161
    - type: nauc_mrr_at_3_max
      value: 57.540780562363395
    - type: nauc_mrr_at_3_std
      value: 75.42098189580211
    - type: nauc_mrr_at_5_diff1
      value: 13.098526703499063
    - type: nauc_mrr_at_5_max
      value: 56.37362177417431
    - type: nauc_mrr_at_5_std
      value: 73.2456769749587
    - type: nauc_ndcg_at_1000_diff1
      value: -8.951471847310401
    - type: nauc_ndcg_at_1000_max
      value: 43.86942237288822
    - type: nauc_ndcg_at_1000_std
      value: 74.61077735148591
    - type: nauc_ndcg_at_100_diff1
      value: -17.754559361083817
    - type: nauc_ndcg_at_100_max
      value: 53.97187119773482
    - type: nauc_ndcg_at_100_std
      value: 80.7944136146514
    - type: nauc_ndcg_at_10_diff1
      value: -26.637734697836414
    - type: nauc_ndcg_at_10_max
      value: 47.70102699133149
    - type: nauc_ndcg_at_10_std
      value: 70.26909560828646
    - type: nauc_ndcg_at_1_diff1
      value: -1.2250530785563207
    - type: nauc_ndcg_at_1_max
      value: 46.60509554140131
    - type: nauc_ndcg_at_1_std
      value: 62.63906581740976
    - type: nauc_ndcg_at_20_diff1
      value: -22.44286466550908
    - type: nauc_ndcg_at_20_max
      value: 55.40492058090103
    - type: nauc_ndcg_at_20_std
      value: 72.11813912145738
    - type: nauc_ndcg_at_3_diff1
      value: -14.8152721896563
    - type: nauc_ndcg_at_3_max
      value: 38.952259383027595
    - type: nauc_ndcg_at_3_std
      value: 59.819750166537766
    - type: nauc_ndcg_at_5_diff1
      value: -19.150105688904375
    - type: nauc_ndcg_at_5_max
      value: 42.311180547775315
    - type: nauc_ndcg_at_5_std
      value: 66.6632229321094
    - type: nauc_precision_at_1000_diff1
      value: -11.555591477978941
    - type: nauc_precision_at_1000_max
      value: 43.7311644834851
    - type: nauc_precision_at_1000_std
      value: 52.10644767999648
    - type: nauc_precision_at_100_diff1
      value: -16.94803099801117
    - type: nauc_precision_at_100_max
      value: 54.08281631067633
    - type: nauc_precision_at_100_std
      value: 82.77237347891331
    - type: nauc_precision_at_10_diff1
      value: -27.351332814863355
    - type: nauc_precision_at_10_max
      value: 48.08237549065846
    - type: nauc_precision_at_10_std
      value: 69.37250843534329
    - type: nauc_precision_at_1_diff1
      value: 12.099350148694809
    - type: nauc_precision_at_1_max
      value: 53.75041304108387
    - type: nauc_precision_at_1_std
      value: 68.84018063663402
    - type: nauc_precision_at_20_diff1
      value: -18.2422222283388
    - type: nauc_precision_at_20_max
      value: 59.517328129343696
    - type: nauc_precision_at_20_std
      value: 72.05149307342747
    - type: nauc_precision_at_3_diff1
      value: -10.226547543075897
    - type: nauc_precision_at_3_max
      value: 43.14684818832875
    - type: nauc_precision_at_3_std
      value: 57.31936467418288
    - type: nauc_precision_at_5_diff1
      value: -14.28521589468673
    - type: nauc_precision_at_5_max
      value: 41.633426753962596
    - type: nauc_precision_at_5_std
      value: 64.94400576804541
    - type: nauc_recall_at_1000_diff1
      value: -0.9648831207497152
    - type: nauc_recall_at_1000_max
      value: 31.70832946085005
    - type: nauc_recall_at_1000_std
      value: 63.21471613968869
    - type: nauc_recall_at_100_diff1
      value: -1.360254380933586
    - type: nauc_recall_at_100_max
      value: 25.960597782099605
    - type: nauc_recall_at_100_std
      value: 51.52757589609674
    - type: nauc_recall_at_10_diff1
      value: -0.3899439424189566
    - type: nauc_recall_at_10_max
      value: 5.094341897886072
    - type: nauc_recall_at_10_std
      value: 11.266045616925698
    - type: nauc_recall_at_1_diff1
      value: 8.269590874255034
    - type: nauc_recall_at_1_max
      value: 3.482498491294516
    - type: nauc_recall_at_1_std
      value: 8.985226819412189
    - type: nauc_recall_at_20_diff1
      value: 6.4797098359254175
    - type: nauc_recall_at_20_max
      value: 15.663700985336124
    - type: nauc_recall_at_20_std
      value: 17.154099587904913
    - type: nauc_recall_at_3_diff1
      value: 3.7245972450393507
    - type: nauc_recall_at_3_max
      value: 0.4063857187240345
    - type: nauc_recall_at_3_std
      value: 6.641948062821941
    - type: nauc_recall_at_5_diff1
      value: 4.013879477591466
    - type: nauc_recall_at_5_max
      value: -1.4266586618013566
    - type: nauc_recall_at_5_std
      value: 7.311601874411205
    - type: ndcg_at_1
      value: 75.0
    - type: ndcg_at_10
      value: 72.18900000000001
    - type: ndcg_at_100
      value: 54.022999999999996
    - type: ndcg_at_1000
      value: 49.492000000000004
    - type: ndcg_at_20
      value: 68.51
    - type: ndcg_at_3
      value: 73.184
    - type: ndcg_at_5
      value: 72.811
    - type: precision_at_1
      value: 82.0
    - type: precision_at_10
      value: 77.4
    - type: precision_at_100
      value: 55.24
    - type: precision_at_1000
      value: 21.822
    - type: precision_at_20
      value: 73.0
    - type: precision_at_3
      value: 79.333
    - type: precision_at_5
      value: 79.2
    - type: recall_at_1
      value: 0.214
    - type: recall_at_10
      value: 1.9980000000000002
    - type: recall_at_100
      value: 13.328999999999999
    - type: recall_at_1000
      value: 47.204
    - type: recall_at_20
      value: 3.7310000000000003
    - type: recall_at_3
      value: 0.628
    - type: recall_at_5
      value: 1.049
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CEDRClassification (default)
      revision: c0ba03d058e3e1b2f3fd20518875a4563dd12db4
      split: test
      type: ai-forever/cedr-classification
    metrics:
    - type: accuracy
      value: 47.30605738575983
    - type: f1
      value: 41.26091043925065
    - type: lrap
      value: 72.89452709883206
    - type: main_score
      value: 47.30605738575983
    task:
      type: MultilabelClassification
  - dataset:
      config: ru
      name: MTEB MIRACLReranking (ru)
      revision: 6d1962c527217f8927fca80f890f14f36b2802af
      split: dev
      type: miracl/mmteb-miracl-reranking
    metrics:
    - type: MAP@1(MIRACL)
      value: 20.721999999999998
    - type: MAP@10(MIRACL)
      value: 33.900999999999996
    - type: MAP@100(MIRACL)
      value: 36.813
    - type: MAP@1000(MIRACL)
      value: 36.813
    - type: MAP@20(MIRACL)
      value: 35.684
    - type: MAP@3(MIRACL)
      value: 28.141
    - type: MAP@5(MIRACL)
      value: 31.075000000000003
    - type: NDCG@1(MIRACL)
      value: 32.799
    - type: NDCG@10(MIRACL)
      value: 42.065000000000005
    - type: NDCG@100(MIRACL)
      value: 49.730999999999995
    - type: NDCG@1000(MIRACL)
      value: 49.730999999999995
    - type: NDCG@20(MIRACL)
      value: 46.0
    - type: NDCG@3(MIRACL)
      value: 34.481
    - type: NDCG@5(MIRACL)
      value: 37.452999999999996
    - type: P@1(MIRACL)
      value: 32.799
    - type: P@10(MIRACL)
      value: 11.668000000000001
    - type: P@100(MIRACL)
      value: 1.9529999999999998
    - type: P@1000(MIRACL)
      value: 0.19499999999999998
    - type: P@20(MIRACL)
      value: 7.51
    - type: P@3(MIRACL)
      value: 20.823
    - type: P@5(MIRACL)
      value: 16.728
    - type: Recall@1(MIRACL)
      value: 20.721999999999998
    - type: Recall@10(MIRACL)
      value: 54.762
    - type: Recall@100(MIRACL)
      value: 79.952
    - type: Recall@1000(MIRACL)
      value: 79.952
    - type: Recall@20(MIRACL)
      value: 66.26100000000001
    - type: Recall@3(MIRACL)
      value: 34.410000000000004
    - type: Recall@5(MIRACL)
      value: 42.659000000000006
    - type: main_score
      value: 42.065000000000005
    - type: nAUC_MAP@1000_diff1(MIRACL)
      value: 14.33534992502818
    - type: nAUC_MAP@1000_max(MIRACL)
      value: 12.367998764646115
    - type: nAUC_MAP@1000_std(MIRACL)
      value: 4.569686002935006
    - type: nAUC_MAP@100_diff1(MIRACL)
      value: 14.33534992502818
    - type: nAUC_MAP@100_max(MIRACL)
      value: 12.367998764646115
    - type: nAUC_MAP@100_std(MIRACL)
      value: 4.569686002935006
    - type: nAUC_MAP@10_diff1(MIRACL)
      value: 16.920323975680027
    - type: nAUC_MAP@10_max(MIRACL)
      value: 9.327171297204082
    - type: nAUC_MAP@10_std(MIRACL)
      value: 3.2039133783079015
    - type: nAUC_MAP@1_diff1(MIRACL)
      value: 28.698973487482206
    - type: nAUC_MAP@1_max(MIRACL)
      value: 2.9217687660885034
    - type: nAUC_MAP@1_std(MIRACL)
      value: -1.1247408800976524
    - type: nAUC_MAP@20_diff1(MIRACL)
      value: 15.359083081640476
    - type: nAUC_MAP@20_max(MIRACL)
      value: 11.310494233946345
    - type: nAUC_MAP@20_std(MIRACL)
      value: 4.4171898386022885
    - type: nAUC_MAP@3_diff1(MIRACL)
      value: 22.27430591851617
    - type: nAUC_MAP@3_max(MIRACL)
      value: 6.407438291284658
    - type: nAUC_MAP@3_std(MIRACL)
      value: 0.9799184530397409
    - type: nAUC_MAP@5_diff1(MIRACL)
      value: 19.20571689941054
    - type: nAUC_MAP@5_max(MIRACL)
      value: 7.987468654026893
    - type: nAUC_MAP@5_std(MIRACL)
      value: 1.8324246565938962
    - type: nAUC_NDCG@1000_diff1(MIRACL)
      value: 3.7537669018914768
    - type: nAUC_NDCG@1000_max(MIRACL)
      value: 20.7944707840533
    - type: nAUC_NDCG@1000_std(MIRACL)
      value: 8.444837055303063
    - type: nAUC_NDCG@100_diff1(MIRACL)
      value: 3.7537669018914768
    - type: nAUC_NDCG@100_max(MIRACL)
      value: 20.7944707840533
    - type: nAUC_NDCG@100_std(MIRACL)
      value: 8.444837055303063
    - type: nAUC_NDCG@10_diff1(MIRACL)
      value: 10.829575656103888
    - type: nAUC_NDCG@10_max(MIRACL)
      value: 13.0445496498929
    - type: nAUC_NDCG@10_std(MIRACL)
      value: 6.050412212625362
    - type: nAUC_NDCG@1_diff1(MIRACL)
      value: 19.1388712233292
    - type: nAUC_NDCG@1_max(MIRACL)
      value: 10.871900994781642
    - type: nAUC_NDCG@1_std(MIRACL)
      value: 3.218568248751811
    - type: nAUC_NDCG@20_diff1(MIRACL)
      value: 7.093172181746442
    - type: nAUC_NDCG@20_max(MIRACL)
      value: 16.955238078958836
    - type: nAUC_NDCG@20_std(MIRACL)
      value: 8.325656379573035
    - type: nAUC_NDCG@3_diff1(MIRACL)
      value: 17.134437303330802
    - type: nAUC_NDCG@3_max(MIRACL)
      value: 10.235328822955793
    - type: nAUC_NDCG@3_std(MIRACL)
      value: 3.2341358691084814
    - type: nAUC_NDCG@5_diff1(MIRACL)
      value: 14.733664618337636
    - type: nAUC_NDCG@5_max(MIRACL)
      value: 11.181897412035282
    - type: nAUC_NDCG@5_std(MIRACL)
      value: 3.642277088791985
    - type: nAUC_P@1000_diff1(MIRACL)
      value: -26.330038284867573
    - type: nAUC_P@1000_max(MIRACL)
      value: 28.450694137240458
    - type: nAUC_P@1000_std(MIRACL)
      value: 9.892993775474912
    - type: nAUC_P@100_diff1(MIRACL)
      value: -26.330038284867552
    - type: nAUC_P@100_max(MIRACL)
      value: 28.45069413724051
    - type: nAUC_P@100_std(MIRACL)
      value: 9.892993775474928
    - type: nAUC_P@10_diff1(MIRACL)
      value: -17.436937353231112
    - type: nAUC_P@10_max(MIRACL)
      value: 24.327018012947857
    - type: nAUC_P@10_std(MIRACL)
      value: 11.78803527706634
    - type: nAUC_P@1_diff1(MIRACL)
      value: 19.1388712233292
    - type: nAUC_P@1_max(MIRACL)
      value: 10.871900994781642
    - type: nAUC_P@1_std(MIRACL)
      value: 3.218568248751811
    - type: nAUC_P@20_diff1(MIRACL)
      value: -22.947528755272426
    - type: nAUC_P@20_max(MIRACL)
      value: 27.773093471902538
    - type: nAUC_P@20_std(MIRACL)
      value: 14.898619107087221
    - type: nAUC_P@3_diff1(MIRACL)
      value: 1.4100426412400944
    - type: nAUC_P@3_max(MIRACL)
      value: 17.397472872058845
    - type: nAUC_P@3_std(MIRACL)
      value: 8.240008229861875
    - type: nAUC_P@5_diff1(MIRACL)
      value: -7.971349332207021
    - type: nAUC_P@5_max(MIRACL)
      value: 22.198441167940963
    - type: nAUC_P@5_std(MIRACL)
      value: 9.00265164460082
    - type: nAUC_Recall@1000_diff1(MIRACL)
      value: -38.69835271863148
    - type: nAUC_Recall@1000_max(MIRACL)
      value: 50.9545152809108
    - type: nAUC_Recall@1000_std(MIRACL)
      value: 20.44270887092116
    - type: nAUC_Recall@100_diff1(MIRACL)
      value: -38.69835271863148
    - type: nAUC_Recall@100_max(MIRACL)
      value: 50.9545152809108
    - type: nAUC_Recall@100_std(MIRACL)
      value: 20.44270887092116
    - type: nAUC_Recall@10_diff1(MIRACL)
      value: -0.08109036309433801
    - type: nAUC_Recall@10_max(MIRACL)
      value: 12.696619907773568
    - type: nAUC_Recall@10_std(MIRACL)
      value: 8.791982704261589
    - type: nAUC_Recall@1_diff1(MIRACL)
      value: 28.698973487482206
    - type: nAUC_Recall@1_max(MIRACL)
      value: 2.9217687660885034
    - type: nAUC_Recall@1_std(MIRACL)
      value: -1.1247408800976524
    - type: nAUC_Recall@20_diff1(MIRACL)
      value: -13.312171017942623
    - type: nAUC_Recall@20_max(MIRACL)
      value: 24.19847346821666
    - type: nAUC_Recall@20_std(MIRACL)
      value: 15.8157702609797
    - type: nAUC_Recall@3_diff1(MIRACL)
      value: 16.909128321353343
    - type: nAUC_Recall@3_max(MIRACL)
      value: 6.552122731902991
    - type: nAUC_Recall@3_std(MIRACL)
      value: 1.9963898223457228
    - type: nAUC_Recall@5_diff1(MIRACL)
      value: 9.990292655247721
    - type: nAUC_Recall@5_max(MIRACL)
      value: 9.361722273507574
    - type: nAUC_Recall@5_std(MIRACL)
      value: 3.270918827854495
    task:
      type: Reranking
  
  - dataset:
      config: default
      name: MTEB SensitiveTopicsClassification (default)
      revision: 416b34a802308eac30e4192afc0ff99bb8dcc7f2
      split: test
      type: ai-forever/sensitive-topics-classification
    metrics:
    - type: accuracy
      value: 30.634765625
    - type: f1
      value: 32.647559808678665
    - type: lrap
      value: 45.94319661458259
    - type: main_score
      value: 30.634765625
    task:
      type: MultilabelClassification
  - dataset:
      config: default
      name: MTEB ATEC (default)
      revision: 0f319b1142f28d00e055a6770f3f726ae9b7d865
      split: test
      type: C-MTEB/ATEC
    metrics:
    - type: cosine_pearson
      value: 47.541497334563296
    - type: cosine_spearman
      value: 49.06268944206629
    - type: euclidean_pearson
      value: 51.838926748581635
    - type: euclidean_spearman
      value: 48.930697157135356
    - type: main_score
      value: 49.06268944206629
    - type: manhattan_pearson
      value: 51.835306769406365
    - type: manhattan_spearman
      value: 48.86135493444834
    - type: pearson
      value: 47.541497334563296
    - type: spearman
      value: 49.06268944206629
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB AllegroReviews (default)
      revision: b89853e6de927b0e3bfa8ecc0e56fe4e02ceafc6
      split: test
      type: PL-MTEB/allegro-reviews
    metrics:
    - type: accuracy
      value: 49.51292246520874
    - type: f1
      value: 44.14350234332397
    - type: f1_weighted
      value: 51.65508998354552
    - type: main_score
      value: 49.51292246520874
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AlloProfClusteringP2P (default)
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: main_score
      value: 63.883383458621665
    - type: v_measure
      value: 63.883383458621665
    - type: v_measure_std
      value: 2.693666879958465
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB 8TagsClustering
      revision: None
      split: test
      type: PL-MTEB/8tags-clustering
    metrics:
    - type: v_measure
      value: 43.657212124525546
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AlloProfClusteringS2S (default)
      revision: 392ba3f5bcc8c51f578786c1fc3dae648662cb9b
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: main_score
      value: 46.85924588755251
    - type: v_measure
      value: 46.85924588755251
    - type: v_measure_std
      value: 2.1918258880872377
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AlloprofReranking (default)
      revision: e40c8a63ce02da43200eccb5b0846fcaa888f562
      split: test
      type: lyon-nlp/mteb-fr-reranking-alloprof-s2p
    metrics:
    - type: map
      value: 66.39013753839347
    - type: mrr
      value: 67.68045617786551
    - type: main_score
      value: 66.39013753839347
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB AlloprofRetrieval (default)
      revision: fcf295ea64c750f41fadbaa37b9b861558e1bfbd
      split: test
      type: lyon-nlp/alloprof
    metrics:
    - type: main_score
      value: 54.284
    - type: map_at_1
      value: 37.047000000000004
    - type: map_at_10
      value: 48.53
    - type: map_at_100
      value: 49.357
    - type: map_at_1000
      value: 49.39
    - type: map_at_20
      value: 49.064
    - type: map_at_3
      value: 45.675
    - type: map_at_5
      value: 47.441
    - type: mrr_at_1
      value: 37.04663212435233
    - type: mrr_at_10
      value: 48.5300326232969
    - type: mrr_at_100
      value: 49.35708199037581
    - type: mrr_at_1000
      value: 49.39005824603193
    - type: mrr_at_20
      value: 49.06417416464799
    - type: mrr_at_3
      value: 45.67501439263105
    - type: mrr_at_5
      value: 47.44099021301103
    - type: nauc_map_at_1000_diff1
      value: 43.32474221868009
    - type: nauc_map_at_1000_max
      value: 39.407334029058575
    - type: nauc_map_at_1000_std
      value: -2.3728154448932606
    - type: nauc_map_at_100_diff1
      value: 43.32336300929909
    - type: nauc_map_at_100_max
      value: 39.432174777554835
    - type: nauc_map_at_100_std
      value: -2.356396922384349
    - type: nauc_map_at_10_diff1
      value: 43.1606520154482
    - type: nauc_map_at_10_max
      value: 39.33734650558226
    - type: nauc_map_at_10_std
      value: -2.5156222475075256
    - type: nauc_map_at_1_diff1
      value: 46.2178975214499
    - type: nauc_map_at_1_max
      value: 36.26173199049361
    - type: nauc_map_at_1_std
      value: -3.0897555582816443
    - type: nauc_map_at_20_diff1
      value: 43.272980702916456
    - type: nauc_map_at_20_max
      value: 39.4896977052276
    - type: nauc_map_at_20_std
      value: -2.3305501742917043
    - type: nauc_map_at_3_diff1
      value: 43.49525042967079
    - type: nauc_map_at_3_max
      value: 38.66352501824728
    - type: nauc_map_at_3_std
      value: -3.202794391620473
    - type: nauc_map_at_5_diff1
      value: 43.2266692546611
    - type: nauc_map_at_5_max
      value: 38.77368661115743
    - type: nauc_map_at_5_std
      value: -3.0897532130127954
    - type: nauc_mrr_at_1000_diff1
      value: 43.32474221868009
    - type: nauc_mrr_at_1000_max
      value: 39.407334029058575
    - type: nauc_mrr_at_1000_std
      value: -2.3728154448932606
    - type: nauc_mrr_at_100_diff1
      value: 43.32336300929909
    - type: nauc_mrr_at_100_max
      value: 39.432174777554835
    - type: nauc_mrr_at_100_std
      value: -2.356396922384349
    - type: nauc_mrr_at_10_diff1
      value: 43.1606520154482
    - type: nauc_mrr_at_10_max
      value: 39.33734650558226
    - type: nauc_mrr_at_10_std
      value: -2.5156222475075256
    - type: nauc_mrr_at_1_diff1
      value: 46.2178975214499
    - type: nauc_mrr_at_1_max
      value: 36.26173199049361
    - type: nauc_mrr_at_1_std
      value: -3.0897555582816443
    - type: nauc_mrr_at_20_diff1
      value: 43.272980702916456
    - type: nauc_mrr_at_20_max
      value: 39.4896977052276
    - type: nauc_mrr_at_20_std
      value: -2.3305501742917043
    - type: nauc_mrr_at_3_diff1
      value: 43.49525042967079
    - type: nauc_mrr_at_3_max
      value: 38.66352501824728
    - type: nauc_mrr_at_3_std
      value: -3.202794391620473
    - type: nauc_mrr_at_5_diff1
      value: 43.2266692546611
    - type: nauc_mrr_at_5_max
      value: 38.77368661115743
    - type: nauc_mrr_at_5_std
      value: -3.0897532130127954
    - type: nauc_ndcg_at_1000_diff1
      value: 43.01903168202974
    - type: nauc_ndcg_at_1000_max
      value: 40.75496622942232
    - type: nauc_ndcg_at_1000_std
      value: -1.3150412981845496
    - type: nauc_ndcg_at_100_diff1
      value: 42.98016493758145
    - type: nauc_ndcg_at_100_max
      value: 41.55869635162325
    - type: nauc_ndcg_at_100_std
      value: -0.5355252976886055
    - type: nauc_ndcg_at_10_diff1
      value: 42.218755211347506
    - type: nauc_ndcg_at_10_max
      value: 41.305042275175765
    - type: nauc_ndcg_at_10_std
      value: -1.4034484444573714
    - type: nauc_ndcg_at_1_diff1
      value: 46.2178975214499
    - type: nauc_ndcg_at_1_max
      value: 36.26173199049361
    - type: nauc_ndcg_at_1_std
      value: -3.0897555582816443
    - type: nauc_ndcg_at_20_diff1
      value: 42.66574440095576
    - type: nauc_ndcg_at_20_max
      value: 42.014620115124515
    - type: nauc_ndcg_at_20_std
      value: -0.5176162553751498
    - type: nauc_ndcg_at_3_diff1
      value: 42.837450505106055
    - type: nauc_ndcg_at_3_max
      value: 39.525369733082414
    - type: nauc_ndcg_at_3_std
      value: -3.1605948245795155
    - type: nauc_ndcg_at_5_diff1
      value: 42.37951815451173
    - type: nauc_ndcg_at_5_max
      value: 39.78840132935179
    - type: nauc_ndcg_at_5_std
      value: -2.936898430768135
    - type: nauc_precision_at_1000_diff1
      value: 49.69224988612385
    - type: nauc_precision_at_1000_max
      value: 79.57897547128005
    - type: nauc_precision_at_1000_std
      value: 45.040371354764645
    - type: nauc_precision_at_100_diff1
      value: 42.70597486048422
    - type: nauc_precision_at_100_max
      value: 65.74628759606188
    - type: nauc_precision_at_100_std
      value: 25.49157745244855
    - type: nauc_precision_at_10_diff1
      value: 38.565609931689345
    - type: nauc_precision_at_10_max
      value: 50.0239696180852
    - type: nauc_precision_at_10_std
      value: 3.976354829503967
    - type: nauc_precision_at_1_diff1
      value: 46.2178975214499
    - type: nauc_precision_at_1_max
      value: 36.26173199049361
    - type: nauc_precision_at_1_std
      value: -3.0897555582816443
    - type: nauc_precision_at_20_diff1
      value: 40.4134718566864
    - type: nauc_precision_at_20_max
      value: 57.121778108665374
    - type: nauc_precision_at_20_std
      value: 11.46021975428544
    - type: nauc_precision_at_3_diff1
      value: 40.90538379461529
    - type: nauc_precision_at_3_max
      value: 42.18393248057992
    - type: nauc_precision_at_3_std
      value: -3.005249943837297
    - type: nauc_precision_at_5_diff1
      value: 39.60162965860782
    - type: nauc_precision_at_5_max
      value: 43.28317158174058
    - type: nauc_precision_at_5_std
      value: -2.3469094487738054
    - type: nauc_recall_at_1000_diff1
      value: 49.69224988612252
    - type: nauc_recall_at_1000_max
      value: 79.57897547127862
    - type: nauc_recall_at_1000_std
      value: 45.04037135476256
    - type: nauc_recall_at_100_diff1
      value: 42.70597486048432
    - type: nauc_recall_at_100_max
      value: 65.74628759606213
    - type: nauc_recall_at_100_std
      value: 25.491577452448727
    - type: nauc_recall_at_10_diff1
      value: 38.56560993168935
    - type: nauc_recall_at_10_max
      value: 50.02396961808522
    - type: nauc_recall_at_10_std
      value: 3.9763548295040314
    - type: nauc_recall_at_1_diff1
      value: 46.2178975214499
    - type: nauc_recall_at_1_max
      value: 36.26173199049361
    - type: nauc_recall_at_1_std
      value: -3.0897555582816443
    - type: nauc_recall_at_20_diff1
      value: 40.41347185668637
    - type: nauc_recall_at_20_max
      value: 57.12177810866533
    - type: nauc_recall_at_20_std
      value: 11.460219754285431
    - type: nauc_recall_at_3_diff1
      value: 40.90538379461527
    - type: nauc_recall_at_3_max
      value: 42.18393248057989
    - type: nauc_recall_at_3_std
      value: -3.005249943837297
    - type: nauc_recall_at_5_diff1
      value: 39.601629658607784
    - type: nauc_recall_at_5_max
      value: 43.28317158174053
    - type: nauc_recall_at_5_std
      value: -2.3469094487738054
    - type: ndcg_at_1
      value: 37.047000000000004
    - type: ndcg_at_10
      value: 54.284
    - type: ndcg_at_100
      value: 58.34
    - type: ndcg_at_1000
      value: 59.303
    - type: ndcg_at_20
      value: 56.235
    - type: ndcg_at_3
      value: 48.503
    - type: ndcg_at_5
      value: 51.686
    - type: precision_at_1
      value: 37.047000000000004
    - type: precision_at_10
      value: 7.237
    - type: precision_at_100
      value: 0.914
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_20
      value: 4.005
    - type: precision_at_3
      value: 18.898
    - type: precision_at_5
      value: 12.884
    - type: recall_at_1
      value: 37.047000000000004
    - type: recall_at_10
      value: 72.366
    - type: recall_at_100
      value: 91.408
    - type: recall_at_1000
      value: 99.136
    - type: recall_at_20
      value: 80.095
    - type: recall_at_3
      value: 56.693000000000005
    - type: recall_at_5
      value: 64.42099999999999
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 89.49253731343283
    - type: ap
      value: 61.88098616359918
    - type: ap_weighted
      value: 61.88098616359918
    - type: f1
      value: 84.76516623679144
    - type: f1_weighted
      value: 89.92745276292968
    - type: main_score
      value: 89.49253731343283
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB AmazonCounterfactualClassification (de)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 89.61456102783727
    - type: ap
      value: 93.11816566733742
    - type: ap_weighted
      value: 93.11816566733742
    - type: f1
      value: 88.27635757733722
    - type: f1_weighted
      value: 89.82581568285453
    - type: main_score
      value: 89.61456102783727
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
      value: 95.3825
    - type: ap
      value: 93.393033869502
    - type: ap_weighted
      value: 93.393033869502
    - type: f1
      value: 95.38109007966307
    - type: f1_weighted
      value: 95.38109007966305
    - type: main_score
      value: 95.3825
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
      value: 49.768
    - type: f1
      value: 48.95084821944411
    - type: f1_weighted
      value: 48.9508482194441
    - type: main_score
      value: 49.768
    task:
      type: Classification
  - dataset:
      config: de
      name: MTEB AmazonReviewsClassification (de)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 48.071999999999996
    - type: f1
      value: 47.24171107487612
    - type: f1_weighted
      value: 47.24171107487612
    - type: main_score
      value: 48.071999999999996
    task:
      type: Classification
  - dataset:
      config: es
      name: MTEB AmazonReviewsClassification (es)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 48.102000000000004
    - type: f1
      value: 47.27193805278696
    - type: f1_weighted
      value: 47.27193805278696
    - type: main_score
      value: 48.102000000000004
    task:
      type: Classification
  - dataset:
      config: fr
      name: MTEB AmazonReviewsClassification (fr)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 47.30800000000001
    - type: f1
      value: 46.41683358017851
    - type: f1_weighted
      value: 46.41683358017851
    - type: main_score
      value: 47.30800000000001
    task:
      type: Classification
  - dataset:
      config: zh
      name: MTEB AmazonReviewsClassification (zh)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 44.944
    - type: f1
      value: 44.223824487744395
    - type: f1_weighted
      value: 44.22382448774439
    - type: main_score
      value: 44.944
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: map_at_1
      value: 29.232000000000003
    - type: map_at_10
      value: 45.117000000000004
    - type: map_at_100
      value: 45.977000000000004
    - type: map_at_1000
      value: 45.98
    - type: map_at_20
      value: 45.815
    - type: map_at_3
      value: 39.912
    - type: map_at_5
      value: 42.693
    - type: mrr_at_1
      value: 29.659000000000002
    - type: mrr_at_10
      value: 45.253
    - type: mrr_at_100
      value: 46.125
    - type: mrr_at_1000
      value: 46.129
    - type: mrr_at_20
      value: 45.964
    - type: mrr_at_3
      value: 40.043
    - type: mrr_at_5
      value: 42.870000000000005
    - type: ndcg_at_1
      value: 29.232000000000003
    - type: ndcg_at_10
      value: 54.327999999999996
    - type: ndcg_at_100
      value: 57.86
    - type: ndcg_at_1000
      value: 57.935
    - type: ndcg_at_20
      value: 56.794
    - type: ndcg_at_3
      value: 43.516
    - type: ndcg_at_5
      value: 48.512
    - type: precision_at_1
      value: 29.232000000000003
    - type: precision_at_10
      value: 8.393
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.676
    - type: precision_at_3
      value: 17.994
    - type: precision_at_5
      value: 13.215
    - type: recall_at_1
      value: 29.232000000000003
    - type: recall_at_10
      value: 83.926
    - type: recall_at_100
      value: 99.075
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 93.528
    - type: recall_at_3
      value: 53.983000000000004
    - type: recall_at_5
      value: 66.074
    - type: main_score
      value: 54.327999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 46.6636824632419
    - type: v_measure
      value: 46.6636824632419
    - type: v_measure_std
      value: 13.817129140714963
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 39.271141892800024
    - type: v_measure
      value: 39.271141892800024
    - type: v_measure_std
      value: 14.276782483454827
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
      value: 65.04363277324629
    - type: mrr
      value: 78.2372598162072
    - type: main_score
      value: 65.04363277324629
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
      split: test
      type: mteb/mind_small
    metrics:
    - type: map
      value: 30.83
    - type: main_score
      value: 30.83
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 88.80382082011027
    - type: cosine_spearman
      value: 88.68876782169106
    - type: euclidean_pearson
      value: 87.00802890147176
    - type: euclidean_spearman
      value: 87.43211268192712
    - type: main_score
      value: 88.68876782169106
    - type: manhattan_pearson
      value: 87.14062537179474
    - type: manhattan_spearman
      value: 87.59115245033443
    - type: pearson
      value: 88.80382082011027
    - type: spearman
      value: 88.68876782169106
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB BQ (default)
      revision: e3dda5e115e487b39ec7e618c0c6a29137052a55
      split: test
      type: C-MTEB/BQ
    metrics:
    - type: cosine_pearson
      value: 61.588006604878196
    - type: cosine_spearman
      value: 63.20615427154465
    - type: euclidean_pearson
      value: 61.818547092516496
    - type: euclidean_spearman
      value: 63.21558009151778
    - type: main_score
      value: 63.20615427154465
    - type: manhattan_pearson
      value: 61.665588158487616
    - type: manhattan_spearman
      value: 63.051544488238584
    - type: pearson
      value: 61.588006604878196
    - type: spearman
      value: 63.20615427154465
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB BSARDRetrieval (default)
      revision: 5effa1b9b5fa3b0f9e12523e6e43e5f86a6e6d59
      split: test
      type: maastrichtlawtech/bsard
    metrics:
    - type: main_score
      value: 64.414
    - type: map_at_1
      value: 14.865
    - type: map_at_10
      value: 21.605
    - type: map_at_100
      value: 22.762
    - type: map_at_1000
      value: 22.854
    - type: map_at_20
      value: 22.259999999999998
    - type: map_at_3
      value: 20.119999999999997
    - type: map_at_5
      value: 20.931
    - type: mrr_at_1
      value: 14.864864864864865
    - type: mrr_at_10
      value: 21.605176605176606
    - type: mrr_at_100
      value: 22.7622306460065
    - type: mrr_at_1000
      value: 22.85383406410312
    - type: mrr_at_20
      value: 22.259528463088845
    - type: mrr_at_3
      value: 20.12012012012012
    - type: mrr_at_5
      value: 20.930930930930934
    - type: nauc_map_at_1000_diff1
      value: 17.486265968689338
    - type: nauc_map_at_1000_max
      value: 22.736799291688836
    - type: nauc_map_at_1000_std
      value: 9.831687441977147
    - type: nauc_map_at_100_diff1
      value: 17.50754492049086
    - type: nauc_map_at_100_max
      value: 22.77693662806787
    - type: nauc_map_at_100_std
      value: 9.853899509675395
    - type: nauc_map_at_10_diff1
      value: 17.42133968580952
    - type: nauc_map_at_10_max
      value: 22.45861793882279
    - type: nauc_map_at_10_std
      value: 8.964888472915938
    - type: nauc_map_at_1_diff1
      value: 19.433947086968093
    - type: nauc_map_at_1_max
      value: 24.75657047550517
    - type: nauc_map_at_1_std
      value: 15.122329157218505
    - type: nauc_map_at_20_diff1
      value: 17.429856756008785
    - type: nauc_map_at_20_max
      value: 22.438850987431017
    - type: nauc_map_at_20_std
      value: 9.172746012213558
    - type: nauc_map_at_3_diff1
      value: 18.218182689678475
    - type: nauc_map_at_3_max
      value: 23.57169444088667
    - type: nauc_map_at_3_std
      value: 10.464473559366356
    - type: nauc_map_at_5_diff1
      value: 18.6075342519133
    - type: nauc_map_at_5_max
      value: 23.308845973576673
    - type: nauc_map_at_5_std
      value: 9.364009996445652
    - type: nauc_mrr_at_1000_diff1
      value: 17.486265968689338
    - type: nauc_mrr_at_1000_max
      value: 22.736799291688836
    - type: nauc_mrr_at_1000_std
      value: 9.831687441977147
    - type: nauc_mrr_at_100_diff1
      value: 17.50754492049086
    - type: nauc_mrr_at_100_max
      value: 22.77693662806787
    - type: nauc_mrr_at_100_std
      value: 9.853899509675395
    - type: nauc_mrr_at_10_diff1
      value: 17.42133968580952
    - type: nauc_mrr_at_10_max
      value: 22.45861793882279
    - type: nauc_mrr_at_10_std
      value: 8.964888472915938
    - type: nauc_mrr_at_1_diff1
      value: 19.433947086968093
    - type: nauc_mrr_at_1_max
      value: 24.75657047550517
    - type: nauc_mrr_at_1_std
      value: 15.122329157218505
    - type: nauc_mrr_at_20_diff1
      value: 17.429856756008785
    - type: nauc_mrr_at_20_max
      value: 22.438850987431017
    - type: nauc_mrr_at_20_std
      value: 9.172746012213558
    - type: nauc_mrr_at_3_diff1
      value: 18.218182689678475
    - type: nauc_mrr_at_3_max
      value: 23.57169444088667
    - type: nauc_mrr_at_3_std
      value: 10.464473559366356
    - type: nauc_mrr_at_5_diff1
      value: 18.6075342519133
    - type: nauc_mrr_at_5_max
      value: 23.308845973576673
    - type: nauc_mrr_at_5_std
      value: 9.364009996445652
    - type: nauc_ndcg_at_1000_diff1
      value: 16.327871824135745
    - type: nauc_ndcg_at_1000_max
      value: 23.308241052911495
    - type: nauc_ndcg_at_1000_std
      value: 11.50905911184097
    - type: nauc_ndcg_at_100_diff1
      value: 16.676226744692773
    - type: nauc_ndcg_at_100_max
      value: 24.323253721240974
    - type: nauc_ndcg_at_100_std
      value: 11.952612443651557
    - type: nauc_ndcg_at_10_diff1
      value: 16.030325121764594
    - type: nauc_ndcg_at_10_max
      value: 21.306799242079542
    - type: nauc_ndcg_at_10_std
      value: 6.63359364302513
    - type: nauc_ndcg_at_1_diff1
      value: 19.433947086968093
    - type: nauc_ndcg_at_1_max
      value: 24.75657047550517
    - type: nauc_ndcg_at_1_std
      value: 15.122329157218505
    - type: nauc_ndcg_at_20_diff1
      value: 16.013173605999857
    - type: nauc_ndcg_at_20_max
      value: 21.607217260736576
    - type: nauc_ndcg_at_20_std
      value: 7.319482417138996
    - type: nauc_ndcg_at_3_diff1
      value: 17.97958548328493
    - type: nauc_ndcg_at_3_max
      value: 23.58346522810145
    - type: nauc_ndcg_at_3_std
      value: 9.392582854708314
    - type: nauc_ndcg_at_5_diff1
      value: 18.734733324685287
    - type: nauc_ndcg_at_5_max
      value: 23.273244317623742
    - type: nauc_ndcg_at_5_std
      value: 7.638611545253834
    - type: nauc_precision_at_1000_diff1
      value: 7.919843339380295
    - type: nauc_precision_at_1000_max
      value: 31.575386234270486
    - type: nauc_precision_at_1000_std
      value: 39.332224386769404
    - type: nauc_precision_at_100_diff1
      value: 15.018050960000052
    - type: nauc_precision_at_100_max
      value: 34.98209513759861
    - type: nauc_precision_at_100_std
      value: 26.970034484359022
    - type: nauc_precision_at_10_diff1
      value: 12.102191084210922
    - type: nauc_precision_at_10_max
      value: 18.112541150340675
    - type: nauc_precision_at_10_std
      value: 0.7358784689406018
    - type: nauc_precision_at_1_diff1
      value: 19.433947086968093
    - type: nauc_precision_at_1_max
      value: 24.75657047550517
    - type: nauc_precision_at_1_std
      value: 15.122329157218505
    - type: nauc_precision_at_20_diff1
      value: 12.018814361204328
    - type: nauc_precision_at_20_max
      value: 19.75123746049928
    - type: nauc_precision_at_20_std
      value: 3.012204650582264
    - type: nauc_precision_at_3_diff1
      value: 17.41375604940955
    - type: nauc_precision_at_3_max
      value: 23.699834627021037
    - type: nauc_precision_at_3_std
      value: 6.793486779050103
    - type: nauc_precision_at_5_diff1
      value: 19.194631963780257
    - type: nauc_precision_at_5_max
      value: 23.31708702442155
    - type: nauc_precision_at_5_std
      value: 3.4591358279667332
    - type: nauc_recall_at_1000_diff1
      value: 7.919843339380378
    - type: nauc_recall_at_1000_max
      value: 31.57538623427063
    - type: nauc_recall_at_1000_std
      value: 39.332224386769546
    - type: nauc_recall_at_100_diff1
      value: 15.018050960000085
    - type: nauc_recall_at_100_max
      value: 34.9820951375986
    - type: nauc_recall_at_100_std
      value: 26.97003448435901
    - type: nauc_recall_at_10_diff1
      value: 12.102191084210837
    - type: nauc_recall_at_10_max
      value: 18.112541150340594
    - type: nauc_recall_at_10_std
      value: 0.7358784689405188
    - type: nauc_recall_at_1_diff1
      value: 19.433947086968093
    - type: nauc_recall_at_1_max
      value: 24.75657047550517
    - type: nauc_recall_at_1_std
      value: 15.122329157218505
    - type: nauc_recall_at_20_diff1
      value: 12.01881436120429
    - type: nauc_recall_at_20_max
      value: 19.751237460499222
    - type: nauc_recall_at_20_std
      value: 3.0122046505822135
    - type: nauc_recall_at_3_diff1
      value: 17.413756049409503
    - type: nauc_recall_at_3_max
      value: 23.699834627020998
    - type: nauc_recall_at_3_std
      value: 6.793486779050083
    - type: nauc_recall_at_5_diff1
      value: 19.194631963780203
    - type: nauc_recall_at_5_max
      value: 23.3170870244215
    - type: nauc_recall_at_5_std
      value: 3.459135827966664
    - type: ndcg_at_1
      value: 14.865
    - type: ndcg_at_10
      value: 24.764
    - type: ndcg_at_100
      value: 30.861
    - type: ndcg_at_1000
      value: 33.628
    - type: ndcg_at_20
      value: 27.078000000000003
    - type: ndcg_at_3
      value: 21.675
    - type: ndcg_at_5
      value: 23.148
    - type: precision_at_1
      value: 14.865
    - type: precision_at_10
      value: 3.4680000000000004
    - type: precision_at_100
      value: 0.644
    - type: precision_at_1000
      value: 0.087
    - type: precision_at_20
      value: 2.185
    - type: precision_at_3
      value: 8.709
    - type: precision_at_5
      value: 5.946
    - type: recall_at_1
      value: 14.865
    - type: recall_at_10
      value: 34.685
    - type: recall_at_100
      value: 64.414
    - type: recall_at_1000
      value: 86.937
    - type: recall_at_20
      value: 43.694
    - type: recall_at_3
      value: 26.125999999999998
    - type: recall_at_5
      value: 29.73
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 84.08116883116882
    - type: f1
      value: 84.05587055990273
    - type: f1_weighted
      value: 84.05587055990274
    - type: main_score
      value: 84.08116883116882
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 38.1941007822277
    - type: v_measure
      value: 38.1941007822277
    - type: v_measure_std
      value: 0.7502113547288178
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 34.42075599178318
    - type: v_measure
      value: 34.42075599178318
    - type: v_measure_std
      value: 0.600256720497283
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BlurbsClusteringP2P (default)
      revision: a2dd5b02a77de3466a3eaa98ae586b5610314496
      split: test
      type: slvnwhrl/blurbs-clustering-p2p
    metrics:
    - type: main_score
      value: 41.634627363047265
    - type: v_measure
      value: 41.634627363047265
    - type: v_measure_std
      value: 9.726923191225307
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BlurbsClusteringS2S (default)
      revision: 22793b6a6465bf00120ad525e38c51210858132c
      split: test
      type: slvnwhrl/blurbs-clustering-s2s
    metrics:
    - type: main_score
      value: 20.996468295584197
    - type: v_measure
      value: 20.996468295584197
    - type: v_measure_std
      value: 9.225766688272197
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CBD (default)
      revision: 36ddb419bcffe6a5374c3891957912892916f28d
      split: test
      type: PL-MTEB/cbd
    metrics:
    - type: accuracy
      value: 69.99
    - type: ap
      value: 22.57826353116948
    - type: ap_weighted
      value: 22.57826353116948
    - type: f1
      value: 59.04574955548393
    - type: f1_weighted
      value: 74.36235022309789
    - type: main_score
      value: 69.99
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB CDSC-E (default)
      revision: 0a3d4aa409b22f80eb22cbf59b492637637b536d
      split: test
      type: PL-MTEB/cdsce-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.7
    - type: cosine_accuracy_threshold
      value: 97.37848043441772
    - type: cosine_ap
      value: 73.0405088928302
    - type: cosine_f1
      value: 63.52201257861635
    - type: cosine_f1_threshold
      value: 96.98888063430786
    - type: cosine_precision
      value: 78.90625
    - type: cosine_recall
      value: 53.1578947368421
    - type: dot_accuracy
      value: 84.89999999999999
    - type: dot_accuracy_threshold
      value: 43603.09753417969
    - type: dot_ap
      value: 56.98157569085279
    - type: dot_f1
      value: 57.606490872210955
    - type: dot_f1_threshold
      value: 40406.23779296875
    - type: dot_precision
      value: 46.864686468646866
    - type: dot_recall
      value: 74.73684210526315
    - type: euclidean_accuracy
      value: 88.5
    - type: euclidean_accuracy_threshold
      value: 498.0483055114746
    - type: euclidean_ap
      value: 72.97328234816734
    - type: euclidean_f1
      value: 63.722397476340696
    - type: euclidean_f1_threshold
      value: 508.6186408996582
    - type: euclidean_precision
      value: 79.52755905511812
    - type: euclidean_recall
      value: 53.1578947368421
    - type: main_score
      value: 73.0405088928302
    - type: manhattan_accuracy
      value: 88.6
    - type: manhattan_accuracy_threshold
      value: 12233.079528808594
    - type: manhattan_ap
      value: 72.92148503992615
    - type: manhattan_f1
      value: 63.69426751592356
    - type: manhattan_f1_threshold
      value: 12392.754364013672
    - type: manhattan_precision
      value: 80.64516129032258
    - type: manhattan_recall
      value: 52.63157894736842
    - type: max_accuracy
      value: 88.7
    - type: max_ap
      value: 73.0405088928302
    - type: max_f1
      value: 63.722397476340696
    - type: max_precision
      value: 80.64516129032258
    - type: max_recall
      value: 74.73684210526315
    - type: similarity_accuracy
      value: 88.7
    - type: similarity_accuracy_threshold
      value: 97.37848043441772
    - type: similarity_ap
      value: 73.0405088928302
    - type: similarity_f1
      value: 63.52201257861635
    - type: similarity_f1_threshold
      value: 96.98888063430786
    - type: similarity_precision
      value: 78.90625
    - type: similarity_recall
      value: 53.1578947368421
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB CDSC-R (default)
      revision: 1cd6abbb00df7d14be3dbd76a7dcc64b3a79a7cd
      split: test
      type: PL-MTEB/cdscr-sts
    metrics:
    - type: cosine_pearson
      value: 92.97492495289738
    - type: cosine_spearman
      value: 92.63248098608472
    - type: euclidean_pearson
      value: 92.04712487782031
    - type: euclidean_spearman
      value: 92.19679486755008
    - type: main_score
      value: 92.63248098608472
    - type: manhattan_pearson
      value: 92.0101187740438
    - type: manhattan_spearman
      value: 92.20926859332754
    - type: pearson
      value: 92.97492495289738
    - type: spearman
      value: 92.63248098608472
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB CLSClusteringP2P (default)
      revision: 4b6227591c6c1a73bc76b1055f3b7f3588e72476
      split: test
      type: C-MTEB/CLSClusteringP2P
    metrics:
    - type: main_score
      value: 39.96377851800628
    - type: v_measure
      value: 39.96377851800628
    - type: v_measure_std
      value: 0.9793033243093288
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CLSClusteringS2S (default)
      revision: e458b3f5414b62b7f9f83499ac1f5497ae2e869f
      split: test
      type: C-MTEB/CLSClusteringS2S
    metrics:
    - type: main_score
      value: 38.788850224595784
    - type: v_measure
      value: 38.788850224595784
    - type: v_measure_std
      value: 1.0712604145916924
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CMedQAv1
      revision: 8d7f1e942507dac42dc58017c1a001c3717da7df
      split: test
      type: C-MTEB/CMedQAv1-reranking
    metrics:
    - type: map
      value: 77.95952507806115
    - type: mrr
      value: 80.8643253968254
    - type: main_score
      value: 77.95952507806115
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB CMedQAv2
      revision: 23d186750531a14a0357ca22cd92d712fd512ea0
      split: test
      type: C-MTEB/CMedQAv2-reranking
    metrics:
    - type: map
      value: 78.21522500165045
    - type: mrr
      value: 81.28194444444443
    - type: main_score
      value: 78.21522500165045
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: map_at_1
      value: 33.377
    - type: map_at_10
      value: 46.371
    - type: map_at_100
      value: 47.829
    - type: map_at_1000
      value: 47.94
    - type: map_at_20
      value: 47.205000000000005
    - type: map_at_3
      value: 42.782
    - type: map_at_5
      value: 44.86
    - type: mrr_at_1
      value: 41.345
    - type: mrr_at_10
      value: 52.187
    - type: mrr_at_100
      value: 52.893
    - type: mrr_at_1000
      value: 52.929
    - type: mrr_at_20
      value: 52.637
    - type: mrr_at_3
      value: 49.714000000000006
    - type: mrr_at_5
      value: 51.373000000000005
    - type: ndcg_at_1
      value: 41.345
    - type: ndcg_at_10
      value: 52.946000000000005
    - type: ndcg_at_100
      value: 57.92699999999999
    - type: ndcg_at_1000
      value: 59.609
    - type: ndcg_at_20
      value: 54.900999999999996
    - type: ndcg_at_3
      value: 48.357
    - type: ndcg_at_5
      value: 50.739000000000004
    - type: precision_at_1
      value: 41.345
    - type: precision_at_10
      value: 10.186
    - type: precision_at_100
      value: 1.554
    - type: precision_at_1000
      value: 0.2
    - type: precision_at_20
      value: 5.959
    - type: precision_at_3
      value: 23.796
    - type: precision_at_5
      value: 17.024
    - type: recall_at_1
      value: 33.377
    - type: recall_at_10
      value: 65.067
    - type: recall_at_100
      value: 86.04899999999999
    - type: recall_at_1000
      value: 96.54899999999999
    - type: recall_at_20
      value: 72.071
    - type: recall_at_3
      value: 51.349999999999994
    - type: recall_at_5
      value: 58.41
    - type: main_score
      value: 52.946000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: map_at_1
      value: 31.097
    - type: map_at_10
      value: 42.183
    - type: map_at_100
      value: 43.580999999999996
    - type: map_at_1000
      value: 43.718
    - type: map_at_20
      value: 42.921
    - type: map_at_3
      value: 38.963
    - type: map_at_5
      value: 40.815
    - type: mrr_at_1
      value: 39.745000000000005
    - type: mrr_at_10
      value: 48.736000000000004
    - type: mrr_at_100
      value: 49.405
    - type: mrr_at_1000
      value: 49.452
    - type: mrr_at_20
      value: 49.118
    - type: mrr_at_3
      value: 46.497
    - type: mrr_at_5
      value: 47.827999999999996
    - type: ndcg_at_1
      value: 39.745000000000005
    - type: ndcg_at_10
      value: 48.248000000000005
    - type: ndcg_at_100
      value: 52.956
    - type: ndcg_at_1000
      value: 54.99699999999999
    - type: ndcg_at_20
      value: 50.01
    - type: ndcg_at_3
      value: 43.946000000000005
    - type: ndcg_at_5
      value: 46.038000000000004
    - type: precision_at_1
      value: 39.745000000000005
    - type: precision_at_10
      value: 9.229
    - type: precision_at_100
      value: 1.5070000000000001
    - type: precision_at_1000
      value: 0.199
    - type: precision_at_20
      value: 5.489999999999999
    - type: precision_at_3
      value: 21.38
    - type: precision_at_5
      value: 15.274
    - type: recall_at_1
      value: 31.097
    - type: recall_at_10
      value: 58.617
    - type: recall_at_100
      value: 78.55199999999999
    - type: recall_at_1000
      value: 91.13900000000001
    - type: recall_at_20
      value: 64.92
    - type: recall_at_3
      value: 45.672000000000004
    - type: recall_at_5
      value: 51.669
    - type: main_score
      value: 48.248000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: map_at_1
      value: 39.745000000000005
    - type: map_at_10
      value: 52.063
    - type: map_at_100
      value: 53.077
    - type: map_at_1000
      value: 53.13
    - type: map_at_20
      value: 52.66
    - type: map_at_3
      value: 48.662
    - type: map_at_5
      value: 50.507000000000005
    - type: mrr_at_1
      value: 45.391999999999996
    - type: mrr_at_10
      value: 55.528
    - type: mrr_at_100
      value: 56.16100000000001
    - type: mrr_at_1000
      value: 56.192
    - type: mrr_at_20
      value: 55.923
    - type: mrr_at_3
      value: 52.93600000000001
    - type: mrr_at_5
      value: 54.435
    - type: ndcg_at_1
      value: 45.391999999999996
    - type: ndcg_at_10
      value: 58.019
    - type: ndcg_at_100
      value: 61.936
    - type: ndcg_at_1000
      value: 63.015
    - type: ndcg_at_20
      value: 59.691
    - type: ndcg_at_3
      value: 52.294
    - type: ndcg_at_5
      value: 55.017
    - type: precision_at_1
      value: 45.391999999999996
    - type: precision_at_10
      value: 9.386
    - type: precision_at_100
      value: 1.232
    - type: precision_at_1000
      value: 0.136
    - type: precision_at_20
      value: 5.223
    - type: precision_at_3
      value: 23.177
    - type: precision_at_5
      value: 15.9
    - type: recall_at_1
      value: 39.745000000000005
    - type: recall_at_10
      value: 72.08099999999999
    - type: recall_at_100
      value: 88.85300000000001
    - type: recall_at_1000
      value: 96.569
    - type: recall_at_20
      value: 78.203
    - type: recall_at_3
      value: 56.957
    - type: recall_at_5
      value: 63.63100000000001
    - type: main_score
      value: 58.019
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: map_at_1
      value: 26.651999999999997
    - type: map_at_10
      value: 35.799
    - type: map_at_100
      value: 36.846000000000004
    - type: map_at_1000
      value: 36.931000000000004
    - type: map_at_20
      value: 36.341
    - type: map_at_3
      value: 32.999
    - type: map_at_5
      value: 34.597
    - type: mrr_at_1
      value: 28.814
    - type: mrr_at_10
      value: 37.869
    - type: mrr_at_100
      value: 38.728
    - type: mrr_at_1000
      value: 38.795
    - type: mrr_at_20
      value: 38.317
    - type: mrr_at_3
      value: 35.235
    - type: mrr_at_5
      value: 36.738
    - type: ndcg_at_1
      value: 28.814
    - type: ndcg_at_10
      value: 41.028
    - type: ndcg_at_100
      value: 46.162
    - type: ndcg_at_1000
      value: 48.15
    - type: ndcg_at_20
      value: 42.824
    - type: ndcg_at_3
      value: 35.621
    - type: ndcg_at_5
      value: 38.277
    - type: precision_at_1
      value: 28.814
    - type: precision_at_10
      value: 6.361999999999999
    - type: precision_at_100
      value: 0.9450000000000001
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_20
      value: 3.6159999999999997
    - type: precision_at_3
      value: 15.140999999999998
    - type: precision_at_5
      value: 10.712000000000002
    - type: recall_at_1
      value: 26.651999999999997
    - type: recall_at_10
      value: 55.038
    - type: recall_at_100
      value: 78.806
    - type: recall_at_1000
      value: 93.485
    - type: recall_at_20
      value: 61.742
    - type: recall_at_3
      value: 40.682
    - type: recall_at_5
      value: 46.855000000000004
    - type: main_score
      value: 41.028
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: map_at_1
      value: 17.627000000000002
    - type: map_at_10
      value: 26.436999999999998
    - type: map_at_100
      value: 27.85
    - type: map_at_1000
      value: 27.955999999999996
    - type: map_at_20
      value: 27.233
    - type: map_at_3
      value: 23.777
    - type: map_at_5
      value: 25.122
    - type: mrr_at_1
      value: 22.387999999999998
    - type: mrr_at_10
      value: 31.589
    - type: mrr_at_100
      value: 32.641999999999996
    - type: mrr_at_1000
      value: 32.696999999999996
    - type: mrr_at_20
      value: 32.201
    - type: mrr_at_3
      value: 28.98
    - type: mrr_at_5
      value: 30.342000000000002
    - type: ndcg_at_1
      value: 22.387999999999998
    - type: ndcg_at_10
      value: 32.129999999999995
    - type: ndcg_at_100
      value: 38.562999999999995
    - type: ndcg_at_1000
      value: 40.903
    - type: ndcg_at_20
      value: 34.652
    - type: ndcg_at_3
      value: 27.26
    - type: ndcg_at_5
      value: 29.235
    - type: precision_at_1
      value: 22.387999999999998
    - type: precision_at_10
      value: 5.970000000000001
    - type: precision_at_100
      value: 1.068
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_20
      value: 3.6999999999999997
    - type: precision_at_3
      value: 13.267000000000001
    - type: precision_at_5
      value: 9.403
    - type: recall_at_1
      value: 17.627000000000002
    - type: recall_at_10
      value: 44.71
    - type: recall_at_100
      value: 72.426
    - type: recall_at_1000
      value: 88.64699999999999
    - type: recall_at_20
      value: 53.65
    - type: recall_at_3
      value: 30.989
    - type: recall_at_5
      value: 36.237
    - type: main_score
      value: 32.129999999999995
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: map_at_1
      value: 30.891000000000002
    - type: map_at_10
      value: 41.519
    - type: map_at_100
      value: 42.896
    - type: map_at_1000
      value: 42.992999999999995
    - type: map_at_20
      value: 42.287
    - type: map_at_3
      value: 37.822
    - type: map_at_5
      value: 39.976
    - type: mrr_at_1
      value: 37.921
    - type: mrr_at_10
      value: 47.260999999999996
    - type: mrr_at_100
      value: 48.044
    - type: mrr_at_1000
      value: 48.08
    - type: mrr_at_20
      value: 47.699999999999996
    - type: mrr_at_3
      value: 44.513999999999996
    - type: mrr_at_5
      value: 46.064
    - type: ndcg_at_1
      value: 37.921
    - type: ndcg_at_10
      value: 47.806
    - type: ndcg_at_100
      value: 53.274
    - type: ndcg_at_1000
      value: 55.021
    - type: ndcg_at_20
      value: 49.973
    - type: ndcg_at_3
      value: 42.046
    - type: ndcg_at_5
      value: 44.835
    - type: precision_at_1
      value: 37.921
    - type: precision_at_10
      value: 8.767999999999999
    - type: precision_at_100
      value: 1.353
    - type: precision_at_1000
      value: 0.168
    - type: precision_at_20
      value: 5.135
    - type: precision_at_3
      value: 20.051
    - type: precision_at_5
      value: 14.398
    - type: recall_at_1
      value: 30.891000000000002
    - type: recall_at_10
      value: 60.897999999999996
    - type: recall_at_100
      value: 83.541
    - type: recall_at_1000
      value: 94.825
    - type: recall_at_20
      value: 68.356
    - type: recall_at_3
      value: 44.65
    - type: recall_at_5
      value: 51.919000000000004
    - type: main_score
      value: 47.806
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: map_at_1
      value: 27.654
    - type: map_at_10
      value: 38.025999999999996
    - type: map_at_100
      value: 39.425
    - type: map_at_1000
      value: 39.528
    - type: map_at_20
      value: 38.838
    - type: map_at_3
      value: 34.745
    - type: map_at_5
      value: 36.537
    - type: mrr_at_1
      value: 34.018
    - type: mrr_at_10
      value: 43.314
    - type: mrr_at_100
      value: 44.283
    - type: mrr_at_1000
      value: 44.327
    - type: mrr_at_20
      value: 43.929
    - type: mrr_at_3
      value: 40.868
    - type: mrr_at_5
      value: 42.317
    - type: ndcg_at_1
      value: 34.018
    - type: ndcg_at_10
      value: 43.887
    - type: ndcg_at_100
      value: 49.791000000000004
    - type: ndcg_at_1000
      value: 51.834
    - type: ndcg_at_20
      value: 46.376
    - type: ndcg_at_3
      value: 38.769999999999996
    - type: ndcg_at_5
      value: 41.144
    - type: precision_at_1
      value: 34.018
    - type: precision_at_10
      value: 8.001999999999999
    - type: precision_at_100
      value: 1.2630000000000001
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_20
      value: 4.737
    - type: precision_at_3
      value: 18.417
    - type: precision_at_5
      value: 13.150999999999998
    - type: recall_at_1
      value: 27.654
    - type: recall_at_10
      value: 56.111
    - type: recall_at_100
      value: 81.136
    - type: recall_at_1000
      value: 94.788
    - type: recall_at_20
      value: 65.068
    - type: recall_at_3
      value: 41.713
    - type: recall_at_5
      value: 48.106
    - type: main_score
      value: 43.887
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
      value: 42.58858333333333
    - type: ndcg_at_10
      value: 42.58858333333333
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: map_at_1
      value: 24.501
    - type: map_at_10
      value: 32.814
    - type: map_at_100
      value: 33.754
    - type: map_at_1000
      value: 33.859
    - type: map_at_20
      value: 33.324
    - type: map_at_3
      value: 30.758000000000003
    - type: map_at_5
      value: 31.936999999999998
    - type: mrr_at_1
      value: 27.761000000000003
    - type: mrr_at_10
      value: 35.662
    - type: mrr_at_100
      value: 36.443999999999996
    - type: mrr_at_1000
      value: 36.516999999999996
    - type: mrr_at_20
      value: 36.085
    - type: mrr_at_3
      value: 33.742
    - type: mrr_at_5
      value: 34.931
    - type: ndcg_at_1
      value: 27.761000000000003
    - type: ndcg_at_10
      value: 37.208000000000006
    - type: ndcg_at_100
      value: 41.839
    - type: ndcg_at_1000
      value: 44.421
    - type: ndcg_at_20
      value: 38.917
    - type: ndcg_at_3
      value: 33.544000000000004
    - type: ndcg_at_5
      value: 35.374
    - type: precision_at_1
      value: 27.761000000000003
    - type: precision_at_10
      value: 5.92
    - type: precision_at_100
      value: 0.899
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_20
      value: 3.4130000000000003
    - type: precision_at_3
      value: 15.031
    - type: precision_at_5
      value: 10.306999999999999
    - type: recall_at_1
      value: 24.501
    - type: recall_at_10
      value: 47.579
    - type: recall_at_100
      value: 69.045
    - type: recall_at_1000
      value: 88.032
    - type: recall_at_20
      value: 54.125
    - type: recall_at_3
      value: 37.202
    - type: recall_at_5
      value: 41.927
    - type: main_score
      value: 37.208000000000006
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: map_at_1
      value: 18.29
    - type: map_at_10
      value: 26.183
    - type: map_at_100
      value: 27.351999999999997
    - type: map_at_1000
      value: 27.483999999999998
    - type: map_at_20
      value: 26.798
    - type: map_at_3
      value: 23.629
    - type: map_at_5
      value: 24.937
    - type: mrr_at_1
      value: 22.299
    - type: mrr_at_10
      value: 30.189
    - type: mrr_at_100
      value: 31.098
    - type: mrr_at_1000
      value: 31.177
    - type: mrr_at_20
      value: 30.697000000000003
    - type: mrr_at_3
      value: 27.862
    - type: mrr_at_5
      value: 29.066
    - type: ndcg_at_1
      value: 22.299
    - type: ndcg_at_10
      value: 31.202
    - type: ndcg_at_100
      value: 36.617
    - type: ndcg_at_1000
      value: 39.544000000000004
    - type: ndcg_at_20
      value: 33.177
    - type: ndcg_at_3
      value: 26.639000000000003
    - type: ndcg_at_5
      value: 28.526
    - type: precision_at_1
      value: 22.299
    - type: precision_at_10
      value: 5.8020000000000005
    - type: precision_at_100
      value: 1.0070000000000001
    - type: precision_at_1000
      value: 0.14400000000000002
    - type: precision_at_20
      value: 3.505
    - type: precision_at_3
      value: 12.698
    - type: precision_at_5
      value: 9.174
    - type: recall_at_1
      value: 18.29
    - type: recall_at_10
      value: 42.254999999999995
    - type: recall_at_100
      value: 66.60000000000001
    - type: recall_at_1000
      value: 87.31400000000001
    - type: recall_at_20
      value: 49.572
    - type: recall_at_3
      value: 29.342000000000002
    - type: recall_at_5
      value: 34.221000000000004
    - type: main_score
      value: 31.202
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: map_at_1
      value: 27.722
    - type: map_at_10
      value: 37.698
    - type: map_at_100
      value: 38.899
    - type: map_at_1000
      value: 38.998
    - type: map_at_20
      value: 38.381
    - type: map_at_3
      value: 34.244
    - type: map_at_5
      value: 36.295
    - type: mrr_at_1
      value: 32.183
    - type: mrr_at_10
      value: 41.429
    - type: mrr_at_100
      value: 42.308
    - type: mrr_at_1000
      value: 42.358000000000004
    - type: mrr_at_20
      value: 41.957
    - type: mrr_at_3
      value: 38.401999999999994
    - type: mrr_at_5
      value: 40.294999999999995
    - type: ndcg_at_1
      value: 32.183
    - type: ndcg_at_10
      value: 43.519000000000005
    - type: ndcg_at_100
      value: 48.786
    - type: ndcg_at_1000
      value: 50.861999999999995
    - type: ndcg_at_20
      value: 45.654
    - type: ndcg_at_3
      value: 37.521
    - type: ndcg_at_5
      value: 40.615
    - type: precision_at_1
      value: 32.183
    - type: precision_at_10
      value: 7.603
    - type: precision_at_100
      value: 1.135
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_20
      value: 4.408
    - type: precision_at_3
      value: 17.071
    - type: precision_at_5
      value: 12.668
    - type: recall_at_1
      value: 27.722
    - type: recall_at_10
      value: 57.230000000000004
    - type: recall_at_100
      value: 79.97999999999999
    - type: recall_at_1000
      value: 94.217
    - type: recall_at_20
      value: 64.864
    - type: recall_at_3
      value: 41.215
    - type: recall_at_5
      value: 48.774
    - type: main_score
      value: 43.519000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: map_at_1
      value: 25.852999999999998
    - type: map_at_10
      value: 35.394999999999996
    - type: map_at_100
      value: 37.291999999999994
    - type: map_at_1000
      value: 37.495
    - type: map_at_20
      value: 36.372
    - type: map_at_3
      value: 32.336
    - type: map_at_5
      value: 34.159
    - type: mrr_at_1
      value: 31.818
    - type: mrr_at_10
      value: 40.677
    - type: mrr_at_100
      value: 41.728
    - type: mrr_at_1000
      value: 41.778
    - type: mrr_at_20
      value: 41.301
    - type: mrr_at_3
      value: 38.208
    - type: mrr_at_5
      value: 39.592
    - type: ndcg_at_1
      value: 31.818
    - type: ndcg_at_10
      value: 41.559000000000005
    - type: ndcg_at_100
      value: 48.012
    - type: ndcg_at_1000
      value: 50.234
    - type: ndcg_at_20
      value: 44.15
    - type: ndcg_at_3
      value: 36.918
    - type: ndcg_at_5
      value: 39.227000000000004
    - type: precision_at_1
      value: 31.818
    - type: precision_at_10
      value: 8.043
    - type: precision_at_100
      value: 1.625
    - type: precision_at_1000
      value: 0.245
    - type: precision_at_20
      value: 5.2170000000000005
    - type: precision_at_3
      value: 17.655
    - type: precision_at_5
      value: 12.845999999999998
    - type: recall_at_1
      value: 25.852999999999998
    - type: recall_at_10
      value: 53.093
    - type: recall_at_100
      value: 81.05799999999999
    - type: recall_at_1000
      value: 94.657
    - type: recall_at_20
      value: 62.748000000000005
    - type: recall_at_3
      value: 39.300000000000004
    - type: recall_at_5
      value: 45.754
    - type: main_score
      value: 41.559000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: map_at_1
      value: 19.23
    - type: map_at_10
      value: 28.128999999999998
    - type: map_at_100
      value: 29.195
    - type: map_at_1000
      value: 29.310000000000002
    - type: map_at_20
      value: 28.713
    - type: map_at_3
      value: 25.191000000000003
    - type: map_at_5
      value: 26.69
    - type: mrr_at_1
      value: 21.257
    - type: mrr_at_10
      value: 30.253999999999998
    - type: mrr_at_100
      value: 31.195
    - type: mrr_at_1000
      value: 31.270999999999997
    - type: mrr_at_20
      value: 30.747999999999998
    - type: mrr_at_3
      value: 27.633999999999997
    - type: mrr_at_5
      value: 28.937
    - type: ndcg_at_1
      value: 21.257
    - type: ndcg_at_10
      value: 33.511
    - type: ndcg_at_100
      value: 38.733000000000004
    - type: ndcg_at_1000
      value: 41.489
    - type: ndcg_at_20
      value: 35.476
    - type: ndcg_at_3
      value: 27.845
    - type: ndcg_at_5
      value: 30.264999999999997
    - type: precision_at_1
      value: 21.257
    - type: precision_at_10
      value: 5.619
    - type: precision_at_100
      value: 0.893
    - type: precision_at_1000
      value: 0.124
    - type: precision_at_20
      value: 3.29
    - type: precision_at_3
      value: 12.508
    - type: precision_at_5
      value: 8.946
    - type: recall_at_1
      value: 19.23
    - type: recall_at_10
      value: 48.185
    - type: recall_at_100
      value: 71.932
    - type: recall_at_1000
      value: 92.587
    - type: recall_at_20
      value: 55.533
    - type: recall_at_3
      value: 32.865
    - type: recall_at_5
      value: 38.577
    - type: main_score
      value: 33.511
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: map_at_1
      value: 19.594
    - type: map_at_10
      value: 32.519
    - type: map_at_100
      value: 34.1
    - type: map_at_1000
      value: 34.263
    - type: map_at_20
      value: 33.353
    - type: map_at_3
      value: 27.898
    - type: map_at_5
      value: 30.524
    - type: mrr_at_1
      value: 46.515
    - type: mrr_at_10
      value: 56.958
    - type: mrr_at_100
      value: 57.54899999999999
    - type: mrr_at_1000
      value: 57.574999999999996
    - type: mrr_at_20
      value: 57.315000000000005
    - type: mrr_at_3
      value: 54.852999999999994
    - type: mrr_at_5
      value: 56.153
    - type: ndcg_at_1
      value: 46.515
    - type: ndcg_at_10
      value: 42.363
    - type: ndcg_at_100
      value: 48.233
    - type: ndcg_at_1000
      value: 50.993
    - type: ndcg_at_20
      value: 44.533
    - type: ndcg_at_3
      value: 37.297000000000004
    - type: ndcg_at_5
      value: 38.911
    - type: precision_at_1
      value: 46.515
    - type: precision_at_10
      value: 12.520999999999999
    - type: precision_at_100
      value: 1.8980000000000001
    - type: precision_at_1000
      value: 0.242
    - type: precision_at_20
      value: 7.212000000000001
    - type: precision_at_3
      value: 27.752
    - type: precision_at_5
      value: 20.391000000000002
    - type: recall_at_1
      value: 19.594
    - type: recall_at_10
      value: 46.539
    - type: recall_at_100
      value: 66.782
    - type: recall_at_1000
      value: 82.049
    - type: recall_at_20
      value: 52.611
    - type: recall_at_3
      value: 32.528
    - type: recall_at_5
      value: 38.933
    - type: main_score
      value: 42.363
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CmedqaRetrieval (default)
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
      split: dev
      type: C-MTEB/CmedqaRetrieval
    metrics:
    - type: main_score
      value: 35.927
    - type: map_at_1
      value: 20.144000000000002
    - type: map_at_10
      value: 29.94
    - type: map_at_100
      value: 31.630000000000003
    - type: map_at_1000
      value: 31.778000000000002
    - type: map_at_20
      value: 30.798
    - type: map_at_3
      value: 26.534999999999997
    - type: map_at_5
      value: 28.33
    - type: mrr_at_1
      value: 31.23280820205051
    - type: mrr_at_10
      value: 38.66781179421835
    - type: mrr_at_100
      value: 39.656936166081785
    - type: mrr_at_1000
      value: 39.724602893117414
    - type: mrr_at_20
      value: 39.21272461558451
    - type: mrr_at_3
      value: 36.30907726931729
    - type: mrr_at_5
      value: 37.59814953738436
    - type: nauc_map_at_1000_diff1
      value: 44.5755334437146
    - type: nauc_map_at_1000_max
      value: 40.726916781400746
    - type: nauc_map_at_1000_std
      value: -19.591835061497367
    - type: nauc_map_at_100_diff1
      value: 44.54542899921038
    - type: nauc_map_at_100_max
      value: 40.68305902532837
    - type: nauc_map_at_100_std
      value: -19.658902089283487
    - type: nauc_map_at_10_diff1
      value: 44.56110529630953
    - type: nauc_map_at_10_max
      value: 39.89826167846008
    - type: nauc_map_at_10_std
      value: -20.62910633667902
    - type: nauc_map_at_1_diff1
      value: 50.82120107004449
    - type: nauc_map_at_1_max
      value: 33.208851367861584
    - type: nauc_map_at_1_std
      value: -20.29409730258174
    - type: nauc_map_at_20_diff1
      value: 44.51171242433788
    - type: nauc_map_at_20_max
      value: 40.30431132782945
    - type: nauc_map_at_20_std
      value: -20.290524142792417
    - type: nauc_map_at_3_diff1
      value: 45.80394138665133
    - type: nauc_map_at_3_max
      value: 37.766191281426956
    - type: nauc_map_at_3_std
      value: -21.223601997333876
    - type: nauc_map_at_5_diff1
      value: 45.00457218474283
    - type: nauc_map_at_5_max
      value: 38.901044576388365
    - type: nauc_map_at_5_std
      value: -20.893069613941634
    - type: nauc_mrr_at_1000_diff1
      value: 50.09855359231429
    - type: nauc_mrr_at_1000_max
      value: 46.481000170008826
    - type: nauc_mrr_at_1000_std
      value: -16.053461377096102
    - type: nauc_mrr_at_100_diff1
      value: 50.08205026347746
    - type: nauc_mrr_at_100_max
      value: 46.47262126963331
    - type: nauc_mrr_at_100_std
      value: -16.049112778748693
    - type: nauc_mrr_at_10_diff1
      value: 50.02363239081706
    - type: nauc_mrr_at_10_max
      value: 46.39287859062042
    - type: nauc_mrr_at_10_std
      value: -16.280866744769657
    - type: nauc_mrr_at_1_diff1
      value: 55.692503735317445
    - type: nauc_mrr_at_1_max
      value: 47.334834529801014
    - type: nauc_mrr_at_1_std
      value: -16.985483585693512
    - type: nauc_mrr_at_20_diff1
      value: 50.07725225722074
    - type: nauc_mrr_at_20_max
      value: 46.47279295070193
    - type: nauc_mrr_at_20_std
      value: -16.15168364678318
    - type: nauc_mrr_at_3_diff1
      value: 51.18685337274134
    - type: nauc_mrr_at_3_max
      value: 46.7286365021621
    - type: nauc_mrr_at_3_std
      value: -16.708451287313718
    - type: nauc_mrr_at_5_diff1
      value: 50.46777237893576
    - type: nauc_mrr_at_5_max
      value: 46.5352076502249
    - type: nauc_mrr_at_5_std
      value: -16.557413659905034
    - type: nauc_ndcg_at_1000_diff1
      value: 43.974299434438066
    - type: nauc_ndcg_at_1000_max
      value: 43.44628675071857
    - type: nauc_ndcg_at_1000_std
      value: -15.3495102005021
    - type: nauc_ndcg_at_100_diff1
      value: 43.336365081508504
    - type: nauc_ndcg_at_100_max
      value: 43.11345604460776
    - type: nauc_ndcg_at_100_std
      value: -15.571128070860615
    - type: nauc_ndcg_at_10_diff1
      value: 43.41266214720136
    - type: nauc_ndcg_at_10_max
      value: 41.519676787851914
    - type: nauc_ndcg_at_10_std
      value: -19.217175017223568
    - type: nauc_ndcg_at_1_diff1
      value: 55.692503735317445
    - type: nauc_ndcg_at_1_max
      value: 47.334834529801014
    - type: nauc_ndcg_at_1_std
      value: -16.985483585693512
    - type: nauc_ndcg_at_20_diff1
      value: 43.351653862834496
    - type: nauc_ndcg_at_20_max
      value: 42.11608469750499
    - type: nauc_ndcg_at_20_std
      value: -18.485363540641664
    - type: nauc_ndcg_at_3_diff1
      value: 45.64193888236677
    - type: nauc_ndcg_at_3_max
      value: 42.497135099009995
    - type: nauc_ndcg_at_3_std
      value: -18.764012041130094
    - type: nauc_ndcg_at_5_diff1
      value: 44.523392133895186
    - type: nauc_ndcg_at_5_max
      value: 41.564242030096345
    - type: nauc_ndcg_at_5_std
      value: -19.31080790984941
    - type: nauc_precision_at_1000_diff1
      value: 6.383464615714393
    - type: nauc_precision_at_1000_max
      value: 27.439930931284657
    - type: nauc_precision_at_1000_std
      value: 19.070716188143034
    - type: nauc_precision_at_100_diff1
      value: 12.599136754501284
    - type: nauc_precision_at_100_max
      value: 35.886310962337795
    - type: nauc_precision_at_100_std
      value: 14.06587592659196
    - type: nauc_precision_at_10_diff1
      value: 25.388891173150206
    - type: nauc_precision_at_10_max
      value: 46.10269270777384
    - type: nauc_precision_at_10_std
      value: -5.993803607158499
    - type: nauc_precision_at_1_diff1
      value: 55.692503735317445
    - type: nauc_precision_at_1_max
      value: 47.334834529801014
    - type: nauc_precision_at_1_std
      value: -16.985483585693512
    - type: nauc_precision_at_20_diff1
      value: 20.984013463099707
    - type: nauc_precision_at_20_max
      value: 42.9471854616888
    - type: nauc_precision_at_20_std
      value: -0.8045549929346024
    - type: nauc_precision_at_3_diff1
      value: 36.191850547148356
    - type: nauc_precision_at_3_max
      value: 48.09923832376049
    - type: nauc_precision_at_3_std
      value: -13.159407051271321
    - type: nauc_precision_at_5_diff1
      value: 31.04967966700407
    - type: nauc_precision_at_5_max
      value: 47.62867673349624
    - type: nauc_precision_at_5_std
      value: -10.345790325137353
    - type: nauc_recall_at_1000_diff1
      value: 11.03436839065707
    - type: nauc_recall_at_1000_max
      value: 42.32265076651575
    - type: nauc_recall_at_1000_std
      value: 30.478521053399206
    - type: nauc_recall_at_100_diff1
      value: 24.788349084510806
    - type: nauc_recall_at_100_max
      value: 36.72097184821956
    - type: nauc_recall_at_100_std
      value: -0.2241144179522076
    - type: nauc_recall_at_10_diff1
      value: 31.613053567704885
    - type: nauc_recall_at_10_max
      value: 34.4597322828833
    - type: nauc_recall_at_10_std
      value: -18.00022912690819
    - type: nauc_recall_at_1_diff1
      value: 50.82120107004449
    - type: nauc_recall_at_1_max
      value: 33.208851367861584
    - type: nauc_recall_at_1_std
      value: -20.29409730258174
    - type: nauc_recall_at_20_diff1
      value: 30.277002670708384
    - type: nauc_recall_at_20_max
      value: 35.212475675060375
    - type: nauc_recall_at_20_std
      value: -15.822788854733687
    - type: nauc_recall_at_3_diff1
      value: 38.87844958322257
    - type: nauc_recall_at_3_max
      value: 34.66914910044104
    - type: nauc_recall_at_3_std
      value: -20.234707300209127
    - type: nauc_recall_at_5_diff1
      value: 35.551139991687776
    - type: nauc_recall_at_5_max
      value: 34.61009958820695
    - type: nauc_recall_at_5_std
      value: -19.519180149293444
    - type: ndcg_at_1
      value: 31.233
    - type: ndcg_at_10
      value: 35.927
    - type: ndcg_at_100
      value: 43.037
    - type: ndcg_at_1000
      value: 45.900999999999996
    - type: ndcg_at_20
      value: 38.39
    - type: ndcg_at_3
      value: 31.366
    - type: ndcg_at_5
      value: 33.108
    - type: precision_at_1
      value: 31.233
    - type: precision_at_10
      value: 8.15
    - type: precision_at_100
      value: 1.402
    - type: precision_at_1000
      value: 0.17700000000000002
    - type: precision_at_20
      value: 4.91
    - type: precision_at_3
      value: 17.871000000000002
    - type: precision_at_5
      value: 12.948
    - type: recall_at_1
      value: 20.144000000000002
    - type: recall_at_10
      value: 44.985
    - type: recall_at_100
      value: 74.866
    - type: recall_at_1000
      value: 94.477
    - type: recall_at_20
      value: 53.37
    - type: recall_at_3
      value: 31.141000000000002
    - type: recall_at_5
      value: 36.721
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Cmnli (default)
      revision: None
      split: validation
      type: C-MTEB/CMNLI
    metrics:
    - type: cos_sim_accuracy
      value: 71.25676488274203
    - type: cos_sim_accuracy_threshold
      value: 78.11152935028076
    - type: cos_sim_ap
      value: 79.10444825556077
    - type: cos_sim_f1
      value: 74.10750923266312
    - type: cos_sim_f1_threshold
      value: 75.2312421798706
    - type: cos_sim_precision
      value: 66.02083714129044
    - type: cos_sim_recall
      value: 84.45171849427169
    - type: dot_accuracy
      value: 68.11785929043896
    - type: dot_accuracy_threshold
      value: 34783.23974609375
    - type: dot_ap
      value: 75.80201827987712
    - type: dot_f1
      value: 72.31670990679349
    - type: dot_f1_threshold
      value: 31978.036499023438
    - type: dot_precision
      value: 61.386623164763456
    - type: dot_recall
      value: 87.98223053542202
    - type: euclidean_accuracy
      value: 71.41310883944678
    - type: euclidean_accuracy_threshold
      value: 1374.9353408813477
    - type: euclidean_ap
      value: 79.23359768836457
    - type: euclidean_f1
      value: 74.38512297540491
    - type: euclidean_f1_threshold
      value: 1512.6035690307617
    - type: euclidean_precision
      value: 64.97816593886463
    - type: euclidean_recall
      value: 86.97685293429974
    - type: manhattan_accuracy
      value: 71.32892363199038
    - type: manhattan_accuracy_threshold
      value: 33340.49072265625
    - type: manhattan_ap
      value: 79.11973684118587
    - type: manhattan_f1
      value: 74.29401993355481
    - type: manhattan_f1_threshold
      value: 36012.52746582031
    - type: manhattan_precision
      value: 66.81605975723622
    - type: manhattan_recall
      value: 83.65676876315175
    - type: max_accuracy
      value: 71.41310883944678
    - type: max_ap
      value: 79.23359768836457
    - type: max_f1
      value: 74.38512297540491
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB CovidRetrieval (default)
      revision: 1271c7809071a13532e05f25fb53511ffce77117
      split: dev
      type: C-MTEB/CovidRetrieval
    metrics:
    - type: main_score
      value: 78.917
    - type: map_at_1
      value: 67.281
    - type: map_at_10
      value: 75.262
    - type: map_at_100
      value: 75.60900000000001
    - type: map_at_1000
      value: 75.618
    - type: map_at_20
      value: 75.50200000000001
    - type: map_at_3
      value: 73.455
    - type: map_at_5
      value: 74.657
    - type: mrr_at_1
      value: 67.43940990516333
    - type: mrr_at_10
      value: 75.27367989696756
    - type: mrr_at_100
      value: 75.62029353306437
    - type: mrr_at_1000
      value: 75.62934741874726
    - type: mrr_at_20
      value: 75.51356607409173
    - type: mrr_at_3
      value: 73.5159817351598
    - type: mrr_at_5
      value: 74.73832103969093
    - type: nauc_map_at_1000_diff1
      value: 77.26666391867634
    - type: nauc_map_at_1000_max
      value: 49.928541012203496
    - type: nauc_map_at_1000_std
      value: -40.494469470474456
    - type: nauc_map_at_100_diff1
      value: 77.26087423162396
    - type: nauc_map_at_100_max
      value: 49.944275615664424
    - type: nauc_map_at_100_std
      value: -40.48299992715398
    - type: nauc_map_at_10_diff1
      value: 76.97400113500906
    - type: nauc_map_at_10_max
      value: 49.84177029115674
    - type: nauc_map_at_10_std
      value: -40.829250876511445
    - type: nauc_map_at_1_diff1
      value: 81.44050620630395
    - type: nauc_map_at_1_max
      value: 48.97711944070578
    - type: nauc_map_at_1_std
      value: -38.963689457570254
    - type: nauc_map_at_20_diff1
      value: 77.21791353089375
    - type: nauc_map_at_20_max
      value: 49.958206759079424
    - type: nauc_map_at_20_std
      value: -40.53067571658996
    - type: nauc_map_at_3_diff1
      value: 77.3555925208868
    - type: nauc_map_at_3_max
      value: 49.32158146451256
    - type: nauc_map_at_3_std
      value: -41.93552426981978
    - type: nauc_map_at_5_diff1
      value: 77.07099950431504
    - type: nauc_map_at_5_max
      value: 49.54190504495002
    - type: nauc_map_at_5_std
      value: -41.814968130918096
    - type: nauc_mrr_at_1000_diff1
      value: 77.31388774540477
    - type: nauc_mrr_at_1000_max
      value: 49.96779699175759
    - type: nauc_mrr_at_1000_std
      value: -40.43739645160277
    - type: nauc_mrr_at_100_diff1
      value: 77.30817786449413
    - type: nauc_mrr_at_100_max
      value: 49.982514428937655
    - type: nauc_mrr_at_100_std
      value: -40.42876582797744
    - type: nauc_mrr_at_10_diff1
      value: 77.02048060465756
    - type: nauc_mrr_at_10_max
      value: 49.87937207270602
    - type: nauc_mrr_at_10_std
      value: -40.77596560333177
    - type: nauc_mrr_at_1_diff1
      value: 81.27219599516599
    - type: nauc_mrr_at_1_max
      value: 49.3083394026327
    - type: nauc_mrr_at_1_std
      value: -38.31023037552026
    - type: nauc_mrr_at_20_diff1
      value: 77.26497089316055
    - type: nauc_mrr_at_20_max
      value: 49.996257597621415
    - type: nauc_mrr_at_20_std
      value: -40.476723608868014
    - type: nauc_mrr_at_3_diff1
      value: 77.38971294099257
    - type: nauc_mrr_at_3_max
      value: 49.38110328987404
    - type: nauc_mrr_at_3_std
      value: -41.7118646715979
    - type: nauc_mrr_at_5_diff1
      value: 77.08286142519952
    - type: nauc_mrr_at_5_max
      value: 49.655249374588685
    - type: nauc_mrr_at_5_std
      value: -41.48173039989406
    - type: nauc_ndcg_at_1000_diff1
      value: 76.47399204021758
    - type: nauc_ndcg_at_1000_max
      value: 50.55770139961048
    - type: nauc_ndcg_at_1000_std
      value: -39.55650430279072
    - type: nauc_ndcg_at_100_diff1
      value: 76.29355616618253
    - type: nauc_ndcg_at_100_max
      value: 51.003608112592936
    - type: nauc_ndcg_at_100_std
      value: -39.24769744605206
    - type: nauc_ndcg_at_10_diff1
      value: 74.88697528447634
    - type: nauc_ndcg_at_10_max
      value: 50.398416372815234
    - type: nauc_ndcg_at_10_std
      value: -40.76526585772833
    - type: nauc_ndcg_at_1_diff1
      value: 81.27219599516599
    - type: nauc_ndcg_at_1_max
      value: 49.3083394026327
    - type: nauc_ndcg_at_1_std
      value: -38.31023037552026
    - type: nauc_ndcg_at_20_diff1
      value: 75.85463512091866
    - type: nauc_ndcg_at_20_max
      value: 50.97338683654334
    - type: nauc_ndcg_at_20_std
      value: -39.353128774903404
    - type: nauc_ndcg_at_3_diff1
      value: 75.94015726123543
    - type: nauc_ndcg_at_3_max
      value: 49.22194251063148
    - type: nauc_ndcg_at_3_std
      value: -43.040457030630435
    - type: nauc_ndcg_at_5_diff1
      value: 75.19166189770303
    - type: nauc_ndcg_at_5_max
      value: 49.65696229797189
    - type: nauc_ndcg_at_5_std
      value: -42.81534909184424
    - type: nauc_precision_at_1000_diff1
      value: -14.830901395815788
    - type: nauc_precision_at_1000_max
      value: 19.686297136854623
    - type: nauc_precision_at_1000_std
      value: 61.19310360166978
    - type: nauc_precision_at_100_diff1
      value: 20.55469986751769
    - type: nauc_precision_at_100_max
      value: 50.78431835075583
    - type: nauc_precision_at_100_std
      value: 31.54986568374813
    - type: nauc_precision_at_10_diff1
      value: 45.991938532558656
    - type: nauc_precision_at_10_max
      value: 46.386318595630385
    - type: nauc_precision_at_10_std
      value: -23.463011435224608
    - type: nauc_precision_at_1_diff1
      value: 81.27219599516599
    - type: nauc_precision_at_1_max
      value: 49.3083394026327
    - type: nauc_precision_at_1_std
      value: -38.31023037552026
    - type: nauc_precision_at_20_diff1
      value: 41.53180472410822
    - type: nauc_precision_at_20_max
      value: 49.89800247204318
    - type: nauc_precision_at_20_std
      value: -2.4192847331537095
    - type: nauc_precision_at_3_diff1
      value: 67.37504651209993
    - type: nauc_precision_at_3_max
      value: 47.893537208629496
    - type: nauc_precision_at_3_std
      value: -43.2362212382819
    - type: nauc_precision_at_5_diff1
      value: 60.03438883791718
    - type: nauc_precision_at_5_max
      value: 48.29770502354206
    - type: nauc_precision_at_5_std
      value: -40.39588448271546
    - type: nauc_recall_at_1000_diff1
      value: 71.04741174480844
    - type: nauc_recall_at_1000_max
      value: 93.19056506596002
    - type: nauc_recall_at_1000_std
      value: 62.96994797650912
    - type: nauc_recall_at_100_diff1
      value: 65.00418176852641
    - type: nauc_recall_at_100_max
      value: 85.27352708427193
    - type: nauc_recall_at_100_std
      value: 2.8812005546518886
    - type: nauc_recall_at_10_diff1
      value: 61.263254794998865
    - type: nauc_recall_at_10_max
      value: 54.17618329507141
    - type: nauc_recall_at_10_std
      value: -39.80603966142593
    - type: nauc_recall_at_1_diff1
      value: 81.44050620630395
    - type: nauc_recall_at_1_max
      value: 48.97711944070578
    - type: nauc_recall_at_1_std
      value: -38.963689457570254
    - type: nauc_recall_at_20_diff1
      value: 64.42106091745396
    - type: nauc_recall_at_20_max
      value: 63.10796640821887
    - type: nauc_recall_at_20_std
      value: -22.60117424572222
    - type: nauc_recall_at_3_diff1
      value: 70.66311436592945
    - type: nauc_recall_at_3_max
      value: 48.69498944323469
    - type: nauc_recall_at_3_std
      value: -47.37847524874532
    - type: nauc_recall_at_5_diff1
      value: 66.12701111728848
    - type: nauc_recall_at_5_max
      value: 49.91763957934711
    - type: nauc_recall_at_5_std
      value: -48.173252920584126
    - type: ndcg_at_1
      value: 67.43900000000001
    - type: ndcg_at_10
      value: 78.917
    - type: ndcg_at_100
      value: 80.53399999999999
    - type: ndcg_at_1000
      value: 80.768
    - type: ndcg_at_20
      value: 79.813
    - type: ndcg_at_3
      value: 75.37
    - type: ndcg_at_5
      value: 77.551
    - type: precision_at_1
      value: 67.43900000000001
    - type: precision_at_10
      value: 9.115
    - type: precision_at_100
      value: 0.985
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.737
    - type: precision_at_3
      value: 27.081
    - type: precision_at_5
      value: 17.345
    - type: recall_at_1
      value: 67.281
    - type: recall_at_10
      value: 90.2
    - type: recall_at_100
      value: 97.576
    - type: recall_at_1000
      value: 99.368
    - type: recall_at_20
      value: 93.783
    - type: recall_at_3
      value: 80.822
    - type: recall_at_5
      value: 86.091
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: map_at_1
      value: 9.041
    - type: map_at_10
      value: 18.662
    - type: map_at_100
      value: 26.054
    - type: map_at_1000
      value: 27.769
    - type: map_at_20
      value: 21.499
    - type: map_at_3
      value: 13.628000000000002
    - type: map_at_5
      value: 15.617
    - type: mrr_at_1
      value: 67.25
    - type: mrr_at_10
      value: 74.673
    - type: mrr_at_100
      value: 75.022
    - type: mrr_at_1000
      value: 75.031
    - type: mrr_at_20
      value: 74.895
    - type: mrr_at_3
      value: 73.042
    - type: mrr_at_5
      value: 74.179
    - type: ndcg_at_1
      value: 55.75
    - type: ndcg_at_10
      value: 41.004000000000005
    - type: ndcg_at_100
      value: 44.912
    - type: ndcg_at_1000
      value: 51.946000000000005
    - type: ndcg_at_20
      value: 40.195
    - type: ndcg_at_3
      value: 45.803
    - type: ndcg_at_5
      value: 42.976
    - type: precision_at_1
      value: 67.25
    - type: precision_at_10
      value: 31.874999999999996
    - type: precision_at_100
      value: 10.37
    - type: precision_at_1000
      value: 2.1430000000000002
    - type: precision_at_20
      value: 24.275
    - type: precision_at_3
      value: 48.417
    - type: precision_at_5
      value: 40.2
    - type: recall_at_1
      value: 9.041
    - type: recall_at_10
      value: 23.592
    - type: recall_at_100
      value: 49.476
    - type: recall_at_1000
      value: 71.677
    - type: recall_at_20
      value: 30.153000000000002
    - type: recall_at_3
      value: 14.777000000000001
    - type: recall_at_5
      value: 17.829
    - type: main_score
      value: 41.004000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DuRetrieval (default)
      revision: a1a333e290fe30b10f3f56498e3a0d911a693ced
      split: dev
      type: C-MTEB/DuRetrieval
    metrics:
    - type: main_score
      value: 83.134
    - type: map_at_1
      value: 23.907999999999998
    - type: map_at_10
      value: 74.566
    - type: map_at_100
      value: 77.706
    - type: map_at_1000
      value: 77.762
    - type: map_at_20
      value: 76.943
    - type: map_at_3
      value: 50.971999999999994
    - type: map_at_5
      value: 64.429
    - type: mrr_at_1
      value: 84.8
    - type: mrr_at_10
      value: 89.73218253968246
    - type: mrr_at_100
      value: 89.82853630655774
    - type: mrr_at_1000
      value: 89.83170411703153
    - type: mrr_at_20
      value: 89.79582030091501
    - type: mrr_at_3
      value: 89.32499999999992
    - type: mrr_at_5
      value: 89.58749999999992
    - type: nauc_map_at_1000_diff1
      value: -2.2736020650163717
    - type: nauc_map_at_1000_max
      value: 45.3937519555142
    - type: nauc_map_at_1000_std
      value: 10.824778228268581
    - type: nauc_map_at_100_diff1
      value: -2.2662939752750066
    - type: nauc_map_at_100_max
      value: 45.423960626031366
    - type: nauc_map_at_100_std
      value: 10.804239351738717
    - type: nauc_map_at_10_diff1
      value: 0.9395752585654343
    - type: nauc_map_at_10_max
      value: 42.53814836940551
    - type: nauc_map_at_10_std
      value: 0.7199313235265218
    - type: nauc_map_at_1_diff1
      value: 45.19415865267676
    - type: nauc_map_at_1_max
      value: -1.7261947382471912
    - type: nauc_map_at_1_std
      value: -32.16144291613605
    - type: nauc_map_at_20_diff1
      value: -1.884514152147472
    - type: nauc_map_at_20_max
      value: 44.830401115927174
    - type: nauc_map_at_20_std
      value: 8.118530414377219
    - type: nauc_map_at_3_diff1
      value: 25.678881127059967
    - type: nauc_map_at_3_max
      value: 12.191400431839758
    - type: nauc_map_at_3_std
      value: -27.201740587642327
    - type: nauc_map_at_5_diff1
      value: 13.227128780829572
    - type: nauc_map_at_5_max
      value: 26.978282739708977
    - type: nauc_map_at_5_std
      value: -17.555610348070584
    - type: nauc_mrr_at_1000_diff1
      value: 21.073512437502178
    - type: nauc_mrr_at_1000_max
      value: 64.9680257861005
    - type: nauc_mrr_at_1000_std
      value: 19.626288754404293
    - type: nauc_mrr_at_100_diff1
      value: 21.074637426957732
    - type: nauc_mrr_at_100_max
      value: 64.97612675661915
    - type: nauc_mrr_at_100_std
      value: 19.649504127800878
    - type: nauc_mrr_at_10_diff1
      value: 21.12003267626651
    - type: nauc_mrr_at_10_max
      value: 65.24362289059766
    - type: nauc_mrr_at_10_std
      value: 19.92351276180984
    - type: nauc_mrr_at_1_diff1
      value: 22.711430629147635
    - type: nauc_mrr_at_1_max
      value: 58.4059429497403
    - type: nauc_mrr_at_1_std
      value: 11.967886722567973
    - type: nauc_mrr_at_20_diff1
      value: 20.98220830510272
    - type: nauc_mrr_at_20_max
      value: 65.05737535197835
    - type: nauc_mrr_at_20_std
      value: 19.66672900782771
    - type: nauc_mrr_at_3_diff1
      value: 20.924796220048528
    - type: nauc_mrr_at_3_max
      value: 65.71388669932584
    - type: nauc_mrr_at_3_std
      value: 20.05912197134477
    - type: nauc_mrr_at_5_diff1
      value: 20.61978649468208
    - type: nauc_mrr_at_5_max
      value: 65.50709154526211
    - type: nauc_mrr_at_5_std
      value: 20.241434276181838
    - type: nauc_ndcg_at_1000_diff1
      value: 0.25363171946133656
    - type: nauc_ndcg_at_1000_max
      value: 54.12840465309885
    - type: nauc_ndcg_at_1000_std
      value: 20.749184325412546
    - type: nauc_ndcg_at_100_diff1
      value: 0.15649430250272792
    - type: nauc_ndcg_at_100_max
      value: 54.47995322413234
    - type: nauc_ndcg_at_100_std
      value: 21.266786634233267
    - type: nauc_ndcg_at_10_diff1
      value: 0.14579250840386346
    - type: nauc_ndcg_at_10_max
      value: 49.8643037948353
    - type: nauc_ndcg_at_10_std
      value: 12.960701643914216
    - type: nauc_ndcg_at_1_diff1
      value: 22.711430629147635
    - type: nauc_ndcg_at_1_max
      value: 58.4059429497403
    - type: nauc_ndcg_at_1_std
      value: 11.967886722567973
    - type: nauc_ndcg_at_20_diff1
      value: -0.6701559981776763
    - type: nauc_ndcg_at_20_max
      value: 52.95443437012488
    - type: nauc_ndcg_at_20_std
      value: 16.708883972005758
    - type: nauc_ndcg_at_3_diff1
      value: -0.19084922341962388
    - type: nauc_ndcg_at_3_max
      value: 46.2110230886874
    - type: nauc_ndcg_at_3_std
      value: 13.363250229683038
    - type: nauc_ndcg_at_5_diff1
      value: 0.9840019268192548
    - type: nauc_ndcg_at_5_max
      value: 43.56594891798146
    - type: nauc_ndcg_at_5_std
      value: 8.577017104088146
    - type: nauc_precision_at_1000_diff1
      value: -30.779179091501145
    - type: nauc_precision_at_1000_max
      value: 16.056094258615673
    - type: nauc_precision_at_1000_std
      value: 49.96303902363283
    - type: nauc_precision_at_100_diff1
      value: -31.583236638899585
    - type: nauc_precision_at_100_max
      value: 19.16571713603373
    - type: nauc_precision_at_100_std
      value: 51.870647903980036
    - type: nauc_precision_at_10_diff1
      value: -35.62134572732597
    - type: nauc_precision_at_10_max
      value: 31.6935186494612
    - type: nauc_precision_at_10_std
      value: 46.68659723766723
    - type: nauc_precision_at_1_diff1
      value: 22.711430629147635
    - type: nauc_precision_at_1_max
      value: 58.4059429497403
    - type: nauc_precision_at_1_std
      value: 11.967886722567973
    - type: nauc_precision_at_20_diff1
      value: -33.875460046920495
    - type: nauc_precision_at_20_max
      value: 24.188420133566442
    - type: nauc_precision_at_20_std
      value: 50.02387762958483
    - type: nauc_precision_at_3_diff1
      value: -28.875998450906827
    - type: nauc_precision_at_3_max
      value: 44.77058831167941
    - type: nauc_precision_at_3_std
      value: 31.77993710437207
    - type: nauc_precision_at_5_diff1
      value: -34.92525440306491
    - type: nauc_precision_at_5_max
      value: 39.855219917077086
    - type: nauc_precision_at_5_std
      value: 37.95432046169299
    - type: nauc_recall_at_1000_diff1
      value: -14.293309371874733
    - type: nauc_recall_at_1000_max
      value: 59.06948692482579
    - type: nauc_recall_at_1000_std
      value: 62.586254868312686
    - type: nauc_recall_at_100_diff1
      value: -4.344100947212704
    - type: nauc_recall_at_100_max
      value: 58.42120421043602
    - type: nauc_recall_at_100_std
      value: 46.48562009316997
    - type: nauc_recall_at_10_diff1
      value: 0.04948662912161709
    - type: nauc_recall_at_10_max
      value: 42.42809687119093
    - type: nauc_recall_at_10_std
      value: 0.6892504250411409
    - type: nauc_recall_at_1_diff1
      value: 45.19415865267676
    - type: nauc_recall_at_1_max
      value: -1.7261947382471912
    - type: nauc_recall_at_1_std
      value: -32.16144291613605
    - type: nauc_recall_at_20_diff1
      value: -7.634587864605111
    - type: nauc_recall_at_20_max
      value: 49.21327187174134
    - type: nauc_recall_at_20_std
      value: 16.408481068336346
    - type: nauc_recall_at_3_diff1
      value: 24.72546591038644
    - type: nauc_recall_at_3_max
      value: 6.620763400972902
    - type: nauc_recall_at_3_std
      value: -29.994703323331684
    - type: nauc_recall_at_5_diff1
      value: 12.65527364845842
    - type: nauc_recall_at_5_max
      value: 20.400121385794694
    - type: nauc_recall_at_5_std
      value: -22.34284568447213
    - type: ndcg_at_1
      value: 84.8
    - type: ndcg_at_10
      value: 83.134
    - type: ndcg_at_100
      value: 86.628
    - type: ndcg_at_1000
      value: 87.151
    - type: ndcg_at_20
      value: 85.092
    - type: ndcg_at_3
      value: 81.228
    - type: ndcg_at_5
      value: 80.2
    - type: precision_at_1
      value: 84.8
    - type: precision_at_10
      value: 40.394999999999996
    - type: precision_at_100
      value: 4.745
    - type: precision_at_1000
      value: 0.488
    - type: precision_at_20
      value: 22.245
    - type: precision_at_3
      value: 73.25
    - type: precision_at_5
      value: 61.86000000000001
    - type: recall_at_1
      value: 23.907999999999998
    - type: recall_at_10
      value: 85.346
    - type: recall_at_100
      value: 96.515
    - type: recall_at_1000
      value: 99.156
    - type: recall_at_20
      value: 91.377
    - type: recall_at_3
      value: 54.135
    - type: recall_at_5
      value: 70.488
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EcomRetrieval (default)
      revision: 687de13dc7294d6fd9be10c6945f9e8fec8166b9
      split: dev
      type: C-MTEB/EcomRetrieval
    metrics:
    - type: main_score
      value: 60.887
    - type: map_at_1
      value: 46.6
    - type: map_at_10
      value: 56.035000000000004
    - type: map_at_100
      value: 56.741
    - type: map_at_1000
      value: 56.764
    - type: map_at_20
      value: 56.513999999999996
    - type: map_at_3
      value: 53.733
    - type: map_at_5
      value: 54.913000000000004
    - type: mrr_at_1
      value: 46.6
    - type: mrr_at_10
      value: 56.034523809523776
    - type: mrr_at_100
      value: 56.74056360434383
    - type: mrr_at_1000
      value: 56.76373487222486
    - type: mrr_at_20
      value: 56.51374873879128
    - type: mrr_at_3
      value: 53.73333333333328
    - type: mrr_at_5
      value: 54.91333333333327
    - type: nauc_map_at_1000_diff1
      value: 65.13546939953387
    - type: nauc_map_at_1000_max
      value: 43.358890946774494
    - type: nauc_map_at_1000_std
      value: -9.973282105235036
    - type: nauc_map_at_100_diff1
      value: 65.12449309472493
    - type: nauc_map_at_100_max
      value: 43.377100882923145
    - type: nauc_map_at_100_std
      value: -9.971781228240555
    - type: nauc_map_at_10_diff1
      value: 64.83020018537475
    - type: nauc_map_at_10_max
      value: 43.25969482323034
    - type: nauc_map_at_10_std
      value: -10.120272176001547
    - type: nauc_map_at_1_diff1
      value: 69.58727592100516
    - type: nauc_map_at_1_max
      value: 38.236494689522026
    - type: nauc_map_at_1_std
      value: -14.833390831689597
    - type: nauc_map_at_20_diff1
      value: 65.01159809914586
    - type: nauc_map_at_20_max
      value: 43.33440319829618
    - type: nauc_map_at_20_std
      value: -10.039958228659726
    - type: nauc_map_at_3_diff1
      value: 65.2396323885909
    - type: nauc_map_at_3_max
      value: 42.26904017378952
    - type: nauc_map_at_3_std
      value: -11.793017036934044
    - type: nauc_map_at_5_diff1
      value: 64.96397227898036
    - type: nauc_map_at_5_max
      value: 43.231333789145424
    - type: nauc_map_at_5_std
      value: -10.349933732151372
    - type: nauc_mrr_at_1000_diff1
      value: 65.13546939953387
    - type: nauc_mrr_at_1000_max
      value: 43.358890946774494
    - type: nauc_mrr_at_1000_std
      value: -9.973282105235036
    - type: nauc_mrr_at_100_diff1
      value: 65.12449309472493
    - type: nauc_mrr_at_100_max
      value: 43.377100882923145
    - type: nauc_mrr_at_100_std
      value: -9.971781228240555
    - type: nauc_mrr_at_10_diff1
      value: 64.83020018537475
    - type: nauc_mrr_at_10_max
      value: 43.25969482323034
    - type: nauc_mrr_at_10_std
      value: -10.120272176001547
    - type: nauc_mrr_at_1_diff1
      value: 69.58727592100516
    - type: nauc_mrr_at_1_max
      value: 38.236494689522026
    - type: nauc_mrr_at_1_std
      value: -14.833390831689597
    - type: nauc_mrr_at_20_diff1
      value: 65.01159809914586
    - type: nauc_mrr_at_20_max
      value: 43.33440319829618
    - type: nauc_mrr_at_20_std
      value: -10.039958228659726
    - type: nauc_mrr_at_3_diff1
      value: 65.2396323885909
    - type: nauc_mrr_at_3_max
      value: 42.26904017378952
    - type: nauc_mrr_at_3_std
      value: -11.793017036934044
    - type: nauc_mrr_at_5_diff1
      value: 64.96397227898036
    - type: nauc_mrr_at_5_max
      value: 43.231333789145424
    - type: nauc_mrr_at_5_std
      value: -10.349933732151372
    - type: nauc_ndcg_at_1000_diff1
      value: 64.26802655199876
    - type: nauc_ndcg_at_1000_max
      value: 45.854310744745185
    - type: nauc_ndcg_at_1000_std
      value: -6.184417305204082
    - type: nauc_ndcg_at_100_diff1
      value: 63.99268329609827
    - type: nauc_ndcg_at_100_max
      value: 46.31270128748375
    - type: nauc_ndcg_at_100_std
      value: -6.1393433180558965
    - type: nauc_ndcg_at_10_diff1
      value: 62.6735104141137
    - type: nauc_ndcg_at_10_max
      value: 45.54954799462398
    - type: nauc_ndcg_at_10_std
      value: -7.348851199024871
    - type: nauc_ndcg_at_1_diff1
      value: 69.58727592100516
    - type: nauc_ndcg_at_1_max
      value: 38.236494689522026
    - type: nauc_ndcg_at_1_std
      value: -14.833390831689597
    - type: nauc_ndcg_at_20_diff1
      value: 63.25899651677274
    - type: nauc_ndcg_at_20_max
      value: 45.952196968886014
    - type: nauc_ndcg_at_20_std
      value: -6.807607465125713
    - type: nauc_ndcg_at_3_diff1
      value: 63.65618337476822
    - type: nauc_ndcg_at_3_max
      value: 43.507890965228945
    - type: nauc_ndcg_at_3_std
      value: -10.73845622217601
    - type: nauc_ndcg_at_5_diff1
      value: 63.079162432921855
    - type: nauc_ndcg_at_5_max
      value: 45.38303443868148
    - type: nauc_ndcg_at_5_std
      value: -8.063657824835534
    - type: nauc_precision_at_1000_diff1
      value: 63.01459977930557
    - type: nauc_precision_at_1000_max
      value: 92.4253034547151
    - type: nauc_precision_at_1000_std
      value: 84.4845513963158
    - type: nauc_precision_at_100_diff1
      value: 57.17217119405878
    - type: nauc_precision_at_100_max
      value: 80.70049725316484
    - type: nauc_precision_at_100_std
      value: 41.78392287147403
    - type: nauc_precision_at_10_diff1
      value: 53.115665404390725
    - type: nauc_precision_at_10_max
      value: 55.73825657341263
    - type: nauc_precision_at_10_std
      value: 5.406226305013257
    - type: nauc_precision_at_1_diff1
      value: 69.58727592100516
    - type: nauc_precision_at_1_max
      value: 38.236494689522026
    - type: nauc_precision_at_1_std
      value: -14.833390831689597
    - type: nauc_precision_at_20_diff1
      value: 53.77730697622828
    - type: nauc_precision_at_20_max
      value: 61.88170819253054
    - type: nauc_precision_at_20_std
      value: 13.678730470003856
    - type: nauc_precision_at_3_diff1
      value: 58.580196992291455
    - type: nauc_precision_at_3_max
      value: 47.404834585376626
    - type: nauc_precision_at_3_std
      value: -7.374978769024051
    - type: nauc_precision_at_5_diff1
      value: 56.44564652606437
    - type: nauc_precision_at_5_max
      value: 53.08973975162324
    - type: nauc_precision_at_5_std
      value: 0.22762700141423803
    - type: nauc_recall_at_1000_diff1
      value: 63.01459977930565
    - type: nauc_recall_at_1000_max
      value: 92.42530345471532
    - type: nauc_recall_at_1000_std
      value: 84.48455139631602
    - type: nauc_recall_at_100_diff1
      value: 57.17217119405904
    - type: nauc_recall_at_100_max
      value: 80.70049725316468
    - type: nauc_recall_at_100_std
      value: 41.783922871474275
    - type: nauc_recall_at_10_diff1
      value: 53.11566540439087
    - type: nauc_recall_at_10_max
      value: 55.738256573412656
    - type: nauc_recall_at_10_std
      value: 5.406226305013377
    - type: nauc_recall_at_1_diff1
      value: 69.58727592100516
    - type: nauc_recall_at_1_max
      value: 38.236494689522026
    - type: nauc_recall_at_1_std
      value: -14.833390831689597
    - type: nauc_recall_at_20_diff1
      value: 53.77730697622846
    - type: nauc_recall_at_20_max
      value: 61.881708192530525
    - type: nauc_recall_at_20_std
      value: 13.678730470003947
    - type: nauc_recall_at_3_diff1
      value: 58.5801969922914
    - type: nauc_recall_at_3_max
      value: 47.40483458537654
    - type: nauc_recall_at_3_std
      value: -7.37497876902413
    - type: nauc_recall_at_5_diff1
      value: 56.445646526064394
    - type: nauc_recall_at_5_max
      value: 53.08973975162332
    - type: nauc_recall_at_5_std
      value: 0.22762700141428024
    - type: ndcg_at_1
      value: 46.6
    - type: ndcg_at_10
      value: 60.887
    - type: ndcg_at_100
      value: 64.18199999999999
    - type: ndcg_at_1000
      value: 64.726
    - type: ndcg_at_20
      value: 62.614999999999995
    - type: ndcg_at_3
      value: 56.038
    - type: ndcg_at_5
      value: 58.150999999999996
    - type: precision_at_1
      value: 46.6
    - type: precision_at_10
      value: 7.630000000000001
    - type: precision_at_100
      value: 0.914
    - type: precision_at_1000
      value: 0.096
    - type: precision_at_20
      value: 4.154999999999999
    - type: precision_at_3
      value: 20.9
    - type: precision_at_5
      value: 13.56
    - type: recall_at_1
      value: 46.6
    - type: recall_at_10
      value: 76.3
    - type: recall_at_100
      value: 91.4
    - type: recall_at_1000
      value: 95.6
    - type: recall_at_20
      value: 83.1
    - type: recall_at_3
      value: 62.7
    - type: recall_at_5
      value: 67.80000000000001
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
      value: 73.29999999999998
    - type: f1
      value: 67.71473706580302
    - type: f1_weighted
      value: 74.83537255312045
    - type: main_score
      value: 73.29999999999998
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: map_at_1
      value: 78.371
    - type: map_at_10
      value: 85.762
    - type: map_at_100
      value: 85.954
    - type: map_at_1000
      value: 85.966
    - type: map_at_20
      value: 85.887
    - type: map_at_3
      value: 84.854
    - type: map_at_5
      value: 85.408
    - type: mrr_at_1
      value: 84.443
    - type: mrr_at_10
      value: 90.432
    - type: mrr_at_100
      value: 90.483
    - type: mrr_at_1000
      value: 90.484
    - type: mrr_at_20
      value: 90.473
    - type: mrr_at_3
      value: 89.89399999999999
    - type: mrr_at_5
      value: 90.244
    - type: ndcg_at_1
      value: 84.443
    - type: ndcg_at_10
      value: 89.05499999999999
    - type: ndcg_at_100
      value: 89.68
    - type: ndcg_at_1000
      value: 89.87899999999999
    - type: ndcg_at_20
      value: 89.381
    - type: ndcg_at_3
      value: 87.73100000000001
    - type: ndcg_at_5
      value: 88.425
    - type: precision_at_1
      value: 84.443
    - type: precision_at_10
      value: 10.520999999999999
    - type: precision_at_100
      value: 1.103
    - type: precision_at_1000
      value: 0.11399999999999999
    - type: precision_at_20
      value: 5.362
    - type: precision_at_3
      value: 33.198
    - type: precision_at_5
      value: 20.441000000000003
    - type: recall_at_1
      value: 78.371
    - type: recall_at_10
      value: 94.594
    - type: recall_at_100
      value: 96.97099999999999
    - type: recall_at_1000
      value: 98.18
    - type: recall_at_20
      value: 95.707
    - type: recall_at_3
      value: 90.853
    - type: recall_at_5
      value: 92.74799999999999
    - type: main_score
      value: 89.05499999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: map_at_1
      value: 23.810000000000002
    - type: map_at_10
      value: 39.051
    - type: map_at_100
      value: 41.231
    - type: map_at_1000
      value: 41.376000000000005
    - type: map_at_20
      value: 40.227000000000004
    - type: map_at_3
      value: 33.915
    - type: map_at_5
      value: 36.459
    - type: mrr_at_1
      value: 48.148
    - type: mrr_at_10
      value: 55.765
    - type: mrr_at_100
      value: 56.495
    - type: mrr_at_1000
      value: 56.525999999999996
    - type: mrr_at_20
      value: 56.213
    - type: mrr_at_3
      value: 53.086
    - type: mrr_at_5
      value: 54.513999999999996
    - type: ndcg_at_1
      value: 48.148
    - type: ndcg_at_10
      value: 47.349999999999994
    - type: ndcg_at_100
      value: 54.61899999999999
    - type: ndcg_at_1000
      value: 56.830000000000005
    - type: ndcg_at_20
      value: 50.143
    - type: ndcg_at_3
      value: 43.108000000000004
    - type: ndcg_at_5
      value: 44.023
    - type: precision_at_1
      value: 48.148
    - type: precision_at_10
      value: 13.441
    - type: precision_at_100
      value: 2.085
    - type: precision_at_1000
      value: 0.248
    - type: precision_at_20
      value: 7.870000000000001
    - type: precision_at_3
      value: 28.909000000000002
    - type: precision_at_5
      value: 20.957
    - type: recall_at_1
      value: 23.810000000000002
    - type: recall_at_10
      value: 54.303000000000004
    - type: recall_at_100
      value: 81.363
    - type: recall_at_1000
      value: 94.391
    - type: recall_at_20
      value: 63.056999999999995
    - type: recall_at_3
      value: 38.098
    - type: recall_at_5
      value: 44.414
    - type: main_score
      value: 47.349999999999994
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GeoreviewClassification (default)
      revision: 3765c0d1de6b7d264bc459433c45e5a75513839c
      split: test
      type: ai-forever/georeview-classification
    metrics:
    - type: accuracy
      value: 48.0126953125
    - type: f1
      value: 47.65764016160488
    - type: f1_weighted
      value: 47.65701659482088
    - type: main_score
      value: 48.0126953125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB GeoreviewClusteringP2P (default)
      revision: 97a313c8fc85b47f13f33e7e9a95c1ad888c7fec
      split: test
      type: ai-forever/georeview-clustering-p2p
    metrics:
    - type: main_score
      value: 73.62357853672266
    - type: v_measure
      value: 73.62357853672266
    - type: v_measure_std
      value: 0.5942247545535766
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB GerDaLIR (default)
      revision: 0bb47f1d73827e96964edb84dfe552f62f4fd5eb
      split: test
      type: jinaai/ger_da_lir
    metrics:
    - type: main_score
      value: 16.227
    - type: map_at_1
      value: 8.082
    - type: map_at_10
      value: 12.959999999999999
    - type: map_at_100
      value: 13.923
    - type: map_at_1000
      value: 14.030999999999999
    - type: map_at_20
      value: 13.453000000000001
    - type: map_at_3
      value: 11.018
    - type: map_at_5
      value: 12.056000000000001
    - type: mrr_at_1
      value: 8.993332249146203
    - type: mrr_at_10
      value: 13.994013092850247
    - type: mrr_at_100
      value: 14.913737673149308
    - type: mrr_at_1000
      value: 15.00843809934407
    - type: mrr_at_20
      value: 14.470268462334007
    - type: mrr_at_3
      value: 12.000596302921846
    - type: mrr_at_5
      value: 13.070689000921561
    - type: nauc_map_at_1000_diff1
      value: 28.559639584013286
    - type: nauc_map_at_1000_max
      value: 25.533800126086714
    - type: nauc_map_at_1000_std
      value: 9.826551026628666
    - type: nauc_map_at_100_diff1
      value: 28.544724499331696
    - type: nauc_map_at_100_max
      value: 25.46734324526386
    - type: nauc_map_at_100_std
      value: 9.739314481785591
    - type: nauc_map_at_10_diff1
      value: 28.77447517718118
    - type: nauc_map_at_10_max
      value: 24.7431615237795
    - type: nauc_map_at_10_std
      value: 8.349878188033646
    - type: nauc_map_at_1_diff1
      value: 37.405452629895514
    - type: nauc_map_at_1_max
      value: 24.444208978394023
    - type: nauc_map_at_1_std
      value: 4.043820373810528
    - type: nauc_map_at_20_diff1
      value: 28.69764217789062
    - type: nauc_map_at_20_max
      value: 25.111848355996496
    - type: nauc_map_at_20_std
      value: 9.034829905305918
    - type: nauc_map_at_3_diff1
      value: 30.89053285076882
    - type: nauc_map_at_3_max
      value: 24.862886115911152
    - type: nauc_map_at_3_std
      value: 6.654260832396586
    - type: nauc_map_at_5_diff1
      value: 29.230629676604263
    - type: nauc_map_at_5_max
      value: 24.374302288018583
    - type: nauc_map_at_5_std
      value: 7.341846952319046
    - type: nauc_mrr_at_1000_diff1
      value: 28.086147932781426
    - type: nauc_mrr_at_1000_max
      value: 25.98698528264653
    - type: nauc_mrr_at_1000_std
      value: 9.917554348624545
    - type: nauc_mrr_at_100_diff1
      value: 28.069163279791336
    - type: nauc_mrr_at_100_max
      value: 25.949440010886804
    - type: nauc_mrr_at_100_std
      value: 9.874340979732578
    - type: nauc_mrr_at_10_diff1
      value: 28.239920869530046
    - type: nauc_mrr_at_10_max
      value: 25.351271409498576
    - type: nauc_mrr_at_10_std
      value: 8.669862759875162
    - type: nauc_mrr_at_1_diff1
      value: 35.96543040207856
    - type: nauc_mrr_at_1_max
      value: 25.488936487231967
    - type: nauc_mrr_at_1_std
      value: 4.76439131038345
    - type: nauc_mrr_at_20_diff1
      value: 28.18865871284607
    - type: nauc_mrr_at_20_max
      value: 25.67121763344746
    - type: nauc_mrr_at_20_std
      value: 9.297910707519472
    - type: nauc_mrr_at_3_diff1
      value: 30.166714199740717
    - type: nauc_mrr_at_3_max
      value: 25.541792491964877
    - type: nauc_mrr_at_3_std
      value: 7.083090296398472
    - type: nauc_mrr_at_5_diff1
      value: 28.68475284656478
    - type: nauc_mrr_at_5_max
      value: 24.994071363482835
    - type: nauc_mrr_at_5_std
      value: 7.687507254902365
    - type: nauc_ndcg_at_1000_diff1
      value: 25.292792613586467
    - type: nauc_ndcg_at_1000_max
      value: 29.211905289377178
    - type: nauc_ndcg_at_1000_std
      value: 18.088867467320355
    - type: nauc_ndcg_at_100_diff1
      value: 25.026905011089152
    - type: nauc_ndcg_at_100_max
      value: 27.98822281254431
    - type: nauc_ndcg_at_100_std
      value: 16.69456904301902
    - type: nauc_ndcg_at_10_diff1
      value: 25.972279051109503
    - type: nauc_ndcg_at_10_max
      value: 24.86486482734957
    - type: nauc_ndcg_at_10_std
      value: 10.398605822106353
    - type: nauc_ndcg_at_1_diff1
      value: 36.134710485184826
    - type: nauc_ndcg_at_1_max
      value: 25.384572790326025
    - type: nauc_ndcg_at_1_std
      value: 4.591863033771824
    - type: nauc_ndcg_at_20_diff1
      value: 25.850033660205536
    - type: nauc_ndcg_at_20_max
      value: 25.944243193140515
    - type: nauc_ndcg_at_20_std
      value: 12.392409721204892
    - type: nauc_ndcg_at_3_diff1
      value: 29.1966056380018
    - type: nauc_ndcg_at_3_max
      value: 24.978843156259913
    - type: nauc_ndcg_at_3_std
      value: 7.353914459205087
    - type: nauc_ndcg_at_5_diff1
      value: 26.795315295756282
    - type: nauc_ndcg_at_5_max
      value: 24.1196789150412
    - type: nauc_ndcg_at_5_std
      value: 8.311970988265172
    - type: nauc_precision_at_1000_diff1
      value: 9.128270550217984
    - type: nauc_precision_at_1000_max
      value: 35.79286915973607
    - type: nauc_precision_at_1000_std
      value: 39.15669472887154
    - type: nauc_precision_at_100_diff1
      value: 14.770289799034384
    - type: nauc_precision_at_100_max
      value: 34.58262232264337
    - type: nauc_precision_at_100_std
      value: 34.101148102981384
    - type: nauc_precision_at_10_diff1
      value: 19.899104673118178
    - type: nauc_precision_at_10_max
      value: 26.636940338985625
    - type: nauc_precision_at_10_std
      value: 15.73871357255849
    - type: nauc_precision_at_1_diff1
      value: 36.134710485184826
    - type: nauc_precision_at_1_max
      value: 25.384572790326025
    - type: nauc_precision_at_1_std
      value: 4.591863033771824
    - type: nauc_precision_at_20_diff1
      value: 19.423457975148942
    - type: nauc_precision_at_20_max
      value: 29.58123490878582
    - type: nauc_precision_at_20_std
      value: 20.847850110821618
    - type: nauc_precision_at_3_diff1
      value: 24.986416623492918
    - type: nauc_precision_at_3_max
      value: 25.973548400472975
    - type: nauc_precision_at_3_std
      value: 9.486410455972823
    - type: nauc_precision_at_5_diff1
      value: 21.237741424923332
    - type: nauc_precision_at_5_max
      value: 24.647141028200164
    - type: nauc_precision_at_5_std
      value: 11.102785032334147
    - type: nauc_recall_at_1000_diff1
      value: 15.999714888817829
    - type: nauc_recall_at_1000_max
      value: 44.34701908906545
    - type: nauc_recall_at_1000_std
      value: 51.13471291594717
    - type: nauc_recall_at_100_diff1
      value: 17.401714890483706
    - type: nauc_recall_at_100_max
      value: 33.39042631654808
    - type: nauc_recall_at_100_std
      value: 33.944446168451584
    - type: nauc_recall_at_10_diff1
      value: 20.30036232399894
    - type: nauc_recall_at_10_max
      value: 24.006718284396786
    - type: nauc_recall_at_10_std
      value: 14.049375108518669
    - type: nauc_recall_at_1_diff1
      value: 37.405452629895514
    - type: nauc_recall_at_1_max
      value: 24.444208978394023
    - type: nauc_recall_at_1_std
      value: 4.043820373810528
    - type: nauc_recall_at_20_diff1
      value: 20.23582802609045
    - type: nauc_recall_at_20_max
      value: 26.408063410785243
    - type: nauc_recall_at_20_std
      value: 18.617479515468112
    - type: nauc_recall_at_3_diff1
      value: 25.53221830103098
    - type: nauc_recall_at_3_max
      value: 24.283712329152678
    - type: nauc_recall_at_3_std
      value: 8.428947805841867
    - type: nauc_recall_at_5_diff1
      value: 21.741499601020823
    - type: nauc_recall_at_5_max
      value: 22.754924586295296
    - type: nauc_recall_at_5_std
      value: 9.966736688169814
    - type: ndcg_at_1
      value: 8.977
    - type: ndcg_at_10
      value: 16.227
    - type: ndcg_at_100
      value: 21.417
    - type: ndcg_at_1000
      value: 24.451
    - type: ndcg_at_20
      value: 17.982
    - type: ndcg_at_3
      value: 12.206999999999999
    - type: ndcg_at_5
      value: 14.059
    - type: precision_at_1
      value: 8.977
    - type: precision_at_10
      value: 2.933
    - type: precision_at_100
      value: 0.59
    - type: precision_at_1000
      value: 0.087
    - type: precision_at_20
      value: 1.8599999999999999
    - type: precision_at_3
      value: 5.550999999999999
    - type: precision_at_5
      value: 4.340999999999999
    - type: recall_at_1
      value: 8.082
    - type: recall_at_10
      value: 25.52
    - type: recall_at_100
      value: 50.32
    - type: recall_at_1000
      value: 74.021
    - type: recall_at_20
      value: 32.229
    - type: recall_at_3
      value: 14.66
    - type: recall_at_5
      value: 19.062
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GermanDPR (default)
      revision: 5129d02422a66be600ac89cd3e8531b4f97d347d
      split: test
      type: deepset/germandpr
    metrics:
    - type: main_score
      value: 82.422
    - type: map_at_1
      value: 64.39
    - type: map_at_10
      value: 77.273
    - type: map_at_100
      value: 77.375
    - type: map_at_1000
      value: 77.376
    - type: map_at_20
      value: 77.351
    - type: map_at_3
      value: 75.46300000000001
    - type: map_at_5
      value: 76.878
    - type: mrr_at_1
      value: 64.19512195121952
    - type: mrr_at_10
      value: 77.15842044134736
    - type: mrr_at_100
      value: 77.2604854308704
    - type: mrr_at_1000
      value: 77.26087882190109
    - type: mrr_at_20
      value: 77.23572154560611
    - type: mrr_at_3
      value: 75.34959349593504
    - type: mrr_at_5
      value: 76.76422764227652
    - type: nauc_map_at_1000_diff1
      value: 49.73135253389972
    - type: nauc_map_at_1000_max
      value: 8.665570717396145
    - type: nauc_map_at_1000_std
      value: -25.920927572114522
    - type: nauc_map_at_100_diff1
      value: 49.729170775336605
    - type: nauc_map_at_100_max
      value: 8.66717979705074
    - type: nauc_map_at_100_std
      value: -25.918338868918596
    - type: nauc_map_at_10_diff1
      value: 49.708681691445925
    - type: nauc_map_at_10_max
      value: 8.830640635692113
    - type: nauc_map_at_10_std
      value: -25.843238986304858
    - type: nauc_map_at_1_diff1
      value: 51.750022350988914
    - type: nauc_map_at_1_max
      value: 3.599863010364626
    - type: nauc_map_at_1_std
      value: -27.670122127567314
    - type: nauc_map_at_20_diff1
      value: 49.72609185887161
    - type: nauc_map_at_20_max
      value: 8.766556053409218
    - type: nauc_map_at_20_std
      value: -25.85975887517904
    - type: nauc_map_at_3_diff1
      value: 49.328512536255595
    - type: nauc_map_at_3_max
      value: 9.475682028996795
    - type: nauc_map_at_3_std
      value: -26.277349632171017
    - type: nauc_map_at_5_diff1
      value: 49.42801822186142
    - type: nauc_map_at_5_max
      value: 8.788822474357252
    - type: nauc_map_at_5_std
      value: -25.959260882028573
    - type: nauc_mrr_at_1000_diff1
      value: 50.13038598302397
    - type: nauc_mrr_at_1000_max
      value: 8.734338637484832
    - type: nauc_mrr_at_1000_std
      value: -26.653343549855908
    - type: nauc_mrr_at_100_diff1
      value: 50.12820392111392
    - type: nauc_mrr_at_100_max
      value: 8.735940503917966
    - type: nauc_mrr_at_100_std
      value: -26.65074918231251
    - type: nauc_mrr_at_10_diff1
      value: 50.10567888458267
    - type: nauc_mrr_at_10_max
      value: 8.898451291748575
    - type: nauc_mrr_at_10_std
      value: -26.572046921975655
    - type: nauc_mrr_at_1_diff1
      value: 52.22769994409465
    - type: nauc_mrr_at_1_max
      value: 3.6490820146062015
    - type: nauc_mrr_at_1_std
      value: -28.535100562320498
    - type: nauc_mrr_at_20_diff1
      value: 50.12462222100699
    - type: nauc_mrr_at_20_max
      value: 8.83487018268756
    - type: nauc_mrr_at_20_std
      value: -26.591437036958332
    - type: nauc_mrr_at_3_diff1
      value: 49.6987353700016
    - type: nauc_mrr_at_3_max
      value: 9.531003760756258
    - type: nauc_mrr_at_3_std
      value: -26.949799063124818
    - type: nauc_mrr_at_5_diff1
      value: 49.823881656376585
    - type: nauc_mrr_at_5_max
      value: 8.850404667985085
    - type: nauc_mrr_at_5_std
      value: -26.680008966088582
    - type: nauc_ndcg_at_1000_diff1
      value: 49.41721203361181
    - type: nauc_ndcg_at_1000_max
      value: 9.41093067609825
    - type: nauc_ndcg_at_1000_std
      value: -25.499543637737567
    - type: nauc_ndcg_at_100_diff1
      value: 49.32810419509252
    - type: nauc_ndcg_at_100_max
      value: 9.476216458766897
    - type: nauc_ndcg_at_100_std
      value: -25.393856250990414
    - type: nauc_ndcg_at_10_diff1
      value: 49.181984436623694
    - type: nauc_ndcg_at_10_max
      value: 10.65234732763274
    - type: nauc_ndcg_at_10_std
      value: -24.737669349012297
    - type: nauc_ndcg_at_1_diff1
      value: 51.750022350988914
    - type: nauc_ndcg_at_1_max
      value: 3.599863010364626
    - type: nauc_ndcg_at_1_std
      value: -27.670122127567314
    - type: nauc_ndcg_at_20_diff1
      value: 49.275394594995056
    - type: nauc_ndcg_at_20_max
      value: 10.402059796651923
    - type: nauc_ndcg_at_20_std
      value: -24.82329915806705
    - type: nauc_ndcg_at_3_diff1
      value: 48.22614352152889
    - type: nauc_ndcg_at_3_max
      value: 11.67464280791404
    - type: nauc_ndcg_at_3_std
      value: -25.867824868234095
    - type: nauc_ndcg_at_5_diff1
      value: 48.35583502987241
    - type: nauc_ndcg_at_5_max
      value: 10.494278750448451
    - type: nauc_ndcg_at_5_std
      value: -25.11599634172764
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_100_diff1
      value: -56.39478136433852
    - type: nauc_precision_at_100_max
      value: 86.93518577529493
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_10_diff1
      value: 38.662829729133094
    - type: nauc_precision_at_10_max
      value: 56.38018435740605
    - type: nauc_precision_at_10_std
      value: 6.288091897081105
    - type: nauc_precision_at_1_diff1
      value: 51.750022350988914
    - type: nauc_precision_at_1_max
      value: 3.599863010364626
    - type: nauc_precision_at_1_std
      value: -27.670122127567314
    - type: nauc_precision_at_20_diff1
      value: 34.739153182429085
    - type: nauc_precision_at_20_max
      value: 84.86908403000989
    - type: nauc_precision_at_20_std
      value: 29.156199421219455
    - type: nauc_precision_at_3_diff1
      value: 42.09287362529135
    - type: nauc_precision_at_3_max
      value: 23.629152759287074
    - type: nauc_precision_at_3_std
      value: -23.721376911302492
    - type: nauc_precision_at_5_diff1
      value: 36.03866171924644
    - type: nauc_precision_at_5_max
      value: 29.166173558775327
    - type: nauc_precision_at_5_std
      value: -15.096374563068448
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: -56.39478136433541
    - type: nauc_recall_at_100_max
      value: 86.93518577528111
    - type: nauc_recall_at_100_std
      value: 100.0
    - type: nauc_recall_at_10_diff1
      value: 38.66282972913384
    - type: nauc_recall_at_10_max
      value: 56.3801843574071
    - type: nauc_recall_at_10_std
      value: 6.288091897082639
    - type: nauc_recall_at_1_diff1
      value: 51.750022350988914
    - type: nauc_recall_at_1_max
      value: 3.599863010364626
    - type: nauc_recall_at_1_std
      value: -27.670122127567314
    - type: nauc_recall_at_20_diff1
      value: 34.7391531824321
    - type: nauc_recall_at_20_max
      value: 84.86908403001016
    - type: nauc_recall_at_20_std
      value: 29.156199421220748
    - type: nauc_recall_at_3_diff1
      value: 42.09287362529107
    - type: nauc_recall_at_3_max
      value: 23.629152759286946
    - type: nauc_recall_at_3_std
      value: -23.72137691130291
    - type: nauc_recall_at_5_diff1
      value: 36.0386617192469
    - type: nauc_recall_at_5_max
      value: 29.1661735587759
    - type: nauc_recall_at_5_std
      value: -15.09637456306774
    - type: ndcg_at_1
      value: 64.39
    - type: ndcg_at_10
      value: 82.422
    - type: ndcg_at_100
      value: 82.86099999999999
    - type: ndcg_at_1000
      value: 82.87299999999999
    - type: ndcg_at_20
      value: 82.67999999999999
    - type: ndcg_at_3
      value: 78.967
    - type: ndcg_at_5
      value: 81.50699999999999
    - type: precision_at_1
      value: 64.39
    - type: precision_at_10
      value: 9.795
    - type: precision_at_100
      value: 0.9990000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.946
    - type: precision_at_3
      value: 29.691000000000003
    - type: precision_at_5
      value: 19.044
    - type: recall_at_1
      value: 64.39
    - type: recall_at_10
      value: 97.951
    - type: recall_at_100
      value: 99.902
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 98.92699999999999
    - type: recall_at_3
      value: 89.07300000000001
    - type: recall_at_5
      value: 95.22
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GermanQuAD-Retrieval (default)
      revision: f5c87ae5a2e7a5106606314eef45255f03151bb3
      split: test
      type: mteb/germanquad-retrieval
    metrics:
    - type: main_score
      value: 94.15532365396247
    - type: map_at_1
      value: 90.789
    - type: map_at_10
      value: 94.24
    - type: map_at_100
      value: 94.283
    - type: map_at_1000
      value: 94.284
    - type: map_at_20
      value: 94.272
    - type: map_at_3
      value: 93.913
    - type: map_at_5
      value: 94.155
    - type: mrr_at_1
      value: 90.78947368421053
    - type: mrr_at_10
      value: 94.23987411056376
    - type: mrr_at_100
      value: 94.28320936825
    - type: mrr_at_1000
      value: 94.28350209115848
    - type: mrr_at_20
      value: 94.271919092559
    - type: mrr_at_3
      value: 93.91258318209313
    - type: mrr_at_5
      value: 94.15532365396247
    - type: nauc_map_at_1000_diff1
      value: 89.29089310650436
    - type: nauc_map_at_1000_max
      value: 73.83868784032414
    - type: nauc_map_at_1000_std
      value: -11.635778561889989
    - type: nauc_map_at_100_diff1
      value: 89.29077225707755
    - type: nauc_map_at_100_max
      value: 73.84002740580378
    - type: nauc_map_at_100_std
      value: -11.644096256165092
    - type: nauc_map_at_10_diff1
      value: 89.29117612292366
    - type: nauc_map_at_10_max
      value: 73.97487984981221
    - type: nauc_map_at_10_std
      value: -11.35191794373827
    - type: nauc_map_at_1_diff1
      value: 89.35436544117584
    - type: nauc_map_at_1_max
      value: 70.35936815057701
    - type: nauc_map_at_1_std
      value: -13.598996360976903
    - type: nauc_map_at_20_diff1
      value: 89.2530394052653
    - type: nauc_map_at_20_max
      value: 73.83537529419839
    - type: nauc_map_at_20_std
      value: -11.628272822028478
    - type: nauc_map_at_3_diff1
      value: 89.375111893546
    - type: nauc_map_at_3_max
      value: 74.78900366026112
    - type: nauc_map_at_3_std
      value: -12.720905253503274
    - type: nauc_map_at_5_diff1
      value: 89.35358300820893
    - type: nauc_map_at_5_max
      value: 74.31996219723239
    - type: nauc_map_at_5_std
      value: -10.768642638210867
    - type: nauc_mrr_at_1000_diff1
      value: 89.29089310650436
    - type: nauc_mrr_at_1000_max
      value: 73.83868784032414
    - type: nauc_mrr_at_1000_std
      value: -11.635778561889989
    - type: nauc_mrr_at_100_diff1
      value: 89.29077225707755
    - type: nauc_mrr_at_100_max
      value: 73.84002740580378
    - type: nauc_mrr_at_100_std
      value: -11.644096256165092
    - type: nauc_mrr_at_10_diff1
      value: 89.29117612292366
    - type: nauc_mrr_at_10_max
      value: 73.97487984981221
    - type: nauc_mrr_at_10_std
      value: -11.35191794373827
    - type: nauc_mrr_at_1_diff1
      value: 89.35436544117584
    - type: nauc_mrr_at_1_max
      value: 70.35936815057701
    - type: nauc_mrr_at_1_std
      value: -13.598996360976903
    - type: nauc_mrr_at_20_diff1
      value: 89.2530394052653
    - type: nauc_mrr_at_20_max
      value: 73.83537529419839
    - type: nauc_mrr_at_20_std
      value: -11.628272822028478
    - type: nauc_mrr_at_3_diff1
      value: 89.375111893546
    - type: nauc_mrr_at_3_max
      value: 74.78900366026112
    - type: nauc_mrr_at_3_std
      value: -12.720905253503274
    - type: nauc_mrr_at_5_diff1
      value: 89.35358300820893
    - type: nauc_mrr_at_5_max
      value: 74.31996219723239
    - type: nauc_mrr_at_5_std
      value: -10.768642638210867
    - type: nauc_ndcg_at_1000_diff1
      value: 89.27620775856863
    - type: nauc_ndcg_at_1000_max
      value: 74.2985757362615
    - type: nauc_ndcg_at_1000_std
      value: -11.236142819703023
    - type: nauc_ndcg_at_100_diff1
      value: 89.27284787540731
    - type: nauc_ndcg_at_100_max
      value: 74.33539303365968
    - type: nauc_ndcg_at_100_std
      value: -11.469413615851936
    - type: nauc_ndcg_at_10_diff1
      value: 89.21496710661724
    - type: nauc_ndcg_at_10_max
      value: 75.02035398490516
    - type: nauc_ndcg_at_10_std
      value: -9.903255803665814
    - type: nauc_ndcg_at_1_diff1
      value: 89.35436544117584
    - type: nauc_ndcg_at_1_max
      value: 70.35936815057701
    - type: nauc_ndcg_at_1_std
      value: -13.598996360976903
    - type: nauc_ndcg_at_20_diff1
      value: 89.03561289544179
    - type: nauc_ndcg_at_20_max
      value: 74.4006766600049
    - type: nauc_ndcg_at_20_std
      value: -11.129237862587743
    - type: nauc_ndcg_at_3_diff1
      value: 89.46540193201693
    - type: nauc_ndcg_at_3_max
      value: 76.87093548368378
    - type: nauc_ndcg_at_3_std
      value: -12.484902872086767
    - type: nauc_ndcg_at_5_diff1
      value: 89.39924941584766
    - type: nauc_ndcg_at_5_max
      value: 75.96975269092722
    - type: nauc_ndcg_at_5_std
      value: -8.180295581144833
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 86.93074003795302
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: -174.07785375176616
    - type: nauc_precision_at_10_diff1
      value: 87.43064119412082
    - type: nauc_precision_at_10_max
      value: 90.60785783417448
    - type: nauc_precision_at_10_std
      value: 15.378710059645906
    - type: nauc_precision_at_1_diff1
      value: 89.35436544117584
    - type: nauc_precision_at_1_max
      value: 70.35936815057701
    - type: nauc_precision_at_1_std
      value: -13.598996360976903
    - type: nauc_precision_at_20_diff1
      value: 78.78206037685919
    - type: nauc_precision_at_20_max
      value: 82.52264166455923
    - type: nauc_precision_at_20_std
      value: -5.95806599216658
    - type: nauc_precision_at_3_diff1
      value: 90.12709256456401
    - type: nauc_precision_at_3_max
      value: 90.72678805838154
    - type: nauc_precision_at_3_std
      value: -11.047599315631993
    - type: nauc_precision_at_5_diff1
      value: 89.9066873566561
    - type: nauc_precision_at_5_max
      value: 93.51571626543664
    - type: nauc_precision_at_5_std
      value: 22.632403279126162
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: 86.93074003793416
    - type: nauc_recall_at_100_max
      value: 100.0
    - type: nauc_recall_at_100_std
      value: -174.07785375175723
    - type: nauc_recall_at_10_diff1
      value: 87.43064119411991
    - type: nauc_recall_at_10_max
      value: 90.60785783417579
    - type: nauc_recall_at_10_std
      value: 15.378710059643607
    - type: nauc_recall_at_1_diff1
      value: 89.35436544117584
    - type: nauc_recall_at_1_max
      value: 70.35936815057701
    - type: nauc_recall_at_1_std
      value: -13.598996360976903
    - type: nauc_recall_at_20_diff1
      value: 78.78206037685645
    - type: nauc_recall_at_20_max
      value: 82.52264166455791
    - type: nauc_recall_at_20_std
      value: -5.958065992168697
    - type: nauc_recall_at_3_diff1
      value: 90.12709256456463
    - type: nauc_recall_at_3_max
      value: 90.7267880583832
    - type: nauc_recall_at_3_std
      value: -11.047599315631881
    - type: nauc_recall_at_5_diff1
      value: 89.90668735665676
    - type: nauc_recall_at_5_max
      value: 93.51571626543753
    - type: nauc_recall_at_5_std
      value: 22.632403279126112
    - type: ndcg_at_1
      value: 90.789
    - type: ndcg_at_10
      value: 95.46
    - type: ndcg_at_100
      value: 95.652
    - type: ndcg_at_1000
      value: 95.659
    - type: ndcg_at_20
      value: 95.575
    - type: ndcg_at_3
      value: 94.82000000000001
    - type: ndcg_at_5
      value: 95.26400000000001
    - type: precision_at_1
      value: 90.789
    - type: precision_at_10
      value: 9.908999999999999
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.977
    - type: precision_at_3
      value: 32.471
    - type: precision_at_5
      value: 19.701
    - type: recall_at_1
      value: 90.789
    - type: recall_at_10
      value: 99.093
    - type: recall_at_100
      value: 99.955
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 99.546
    - type: recall_at_3
      value: 97.414
    - type: recall_at_5
      value: 98.503
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB GermanSTSBenchmark (default)
      revision: e36907544d44c3a247898ed81540310442329e20
      split: test
      type: jinaai/german-STSbenchmark
    metrics:
    - type: cosine_pearson
      value: 86.55319003300265
    - type: cosine_spearman
      value: 87.50267373081324
    - type: euclidean_pearson
      value: 87.41630636501863
    - type: euclidean_spearman
      value: 88.02170803409365
    - type: main_score
      value: 87.50267373081324
    - type: manhattan_pearson
      value: 87.33703179056744
    - type: manhattan_spearman
      value: 87.99192826922514
    - type: pearson
      value: 86.55319003300265
    - type: spearman
      value: 87.50267373081324
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB HALClusteringS2S (default)
      revision: e06ebbbb123f8144bef1a5d18796f3dec9ae2915
      split: test
      type: lyon-nlp/clustering-hal-s2s
    metrics:
    - type: main_score
      value: 27.477557517301303
    - type: v_measure
      value: 27.477557517301303
    - type: v_measure_std
      value: 3.3525736581861336
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB HeadlineClassification (default)
      revision: 2fe05ee6b5832cda29f2ef7aaad7b7fe6a3609eb
      split: test
      type: ai-forever/headline-classification
    metrics:
    - type: accuracy
      value: 75.0830078125
    - type: f1
      value: 75.08863209267814
    - type: f1_weighted
      value: 75.08895979060917
    - type: main_score
      value: 75.0830078125
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: map_at_1
      value: 38.143
    - type: map_at_10
      value: 55.916999999999994
    - type: map_at_100
      value: 56.706
    - type: map_at_1000
      value: 56.77100000000001
    - type: map_at_20
      value: 56.367
    - type: map_at_3
      value: 53.111
    - type: map_at_5
      value: 54.839000000000006
    - type: mrr_at_1
      value: 76.286
    - type: mrr_at_10
      value: 81.879
    - type: mrr_at_100
      value: 82.09100000000001
    - type: mrr_at_1000
      value: 82.101
    - type: mrr_at_20
      value: 82.01
    - type: mrr_at_3
      value: 80.972
    - type: mrr_at_5
      value: 81.537
    - type: ndcg_at_1
      value: 76.286
    - type: ndcg_at_10
      value: 64.673
    - type: ndcg_at_100
      value: 67.527
    - type: ndcg_at_1000
      value: 68.857
    - type: ndcg_at_20
      value: 65.822
    - type: ndcg_at_3
      value: 60.616
    - type: ndcg_at_5
      value: 62.827999999999996
    - type: precision_at_1
      value: 76.286
    - type: precision_at_10
      value: 13.196
    - type: precision_at_100
      value: 1.544
    - type: precision_at_1000
      value: 0.172
    - type: precision_at_20
      value: 6.968000000000001
    - type: precision_at_3
      value: 37.992
    - type: precision_at_5
      value: 24.54
    - type: recall_at_1
      value: 38.143
    - type: recall_at_10
      value: 65.982
    - type: recall_at_100
      value: 77.225
    - type: recall_at_1000
      value: 86.077
    - type: recall_at_20
      value: 69.68299999999999
    - type: recall_at_3
      value: 56.989000000000004
    - type: recall_at_5
      value: 61.35
    - type: main_score
      value: 64.673
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB IFlyTek (default)
      revision: 421605374b29664c5fc098418fe20ada9bd55f8a
      split: validation
      type: C-MTEB/IFlyTek-classification
    metrics:
    - type: accuracy
      value: 41.67756829549827
    - type: f1
      value: 33.929325579581636
    - type: f1_weighted
      value: 43.03952025643197
    - type: main_score
      value: 41.67756829549827
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 91.90440000000001
    - type: ap
      value: 88.78663714603425
    - type: ap_weighted
      value: 88.78663714603425
    - type: f1
      value: 91.89564361975891
    - type: f1_weighted
      value: 91.89564361975891
    - type: main_score
      value: 91.90440000000001
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB InappropriatenessClassification (default)
      revision: 601651fdc45ef243751676e62dd7a19f491c0285
      split: test
      type: ai-forever/inappropriateness-classification
    metrics:
    - type: accuracy
      value: 61.0498046875
    - type: ap
      value: 57.04240566648215
    - type: ap_weighted
      value: 57.04240566648215
    - type: f1
      value: 60.867630038606954
    - type: f1_weighted
      value: 60.867630038606954
    - type: main_score
      value: 61.0498046875
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB JDReview (default)
      revision: b7c64bd89eb87f8ded463478346f76731f07bf8b
      split: test
      type: C-MTEB/JDReview-classification
    metrics:
    - type: accuracy
      value: 83.50844277673546
    - type: ap
      value: 48.46732380712268
    - type: ap_weighted
      value: 48.46732380712268
    - type: f1
      value: 77.43967451387445
    - type: f1_weighted
      value: 84.78462929014114
    - type: main_score
      value: 83.50844277673546
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB KinopoiskClassification (default)
      revision: 5911f26666ac11af46cb9c6849d0dc80a378af24
      split: test
      type: ai-forever/kinopoisk-sentiment-classification
    metrics:
    - type: accuracy
      value: 62.393333333333324
    - type: f1
      value: 61.35940129568015
    - type: f1_weighted
      value: 61.35940129568015
    - type: main_score
      value: 62.393333333333324
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB LCQMC (default)
      revision: 17f9b096f80380fce5ed12a9be8be7784b337daf
      split: test
      type: C-MTEB/LCQMC
    metrics:
    - type: cosine_pearson
      value: 67.74375505907872
    - type: cosine_spearman
      value: 75.94582231399434
    - type: euclidean_pearson
      value: 74.52501692443582
    - type: euclidean_spearman
      value: 75.88428434746646
    - type: main_score
      value: 75.94582231399434
    - type: manhattan_pearson
      value: 74.55015441749529
    - type: manhattan_spearman
      value: 75.83288262176175
    - type: pearson
      value: 67.74375505907872
    - type: spearman
      value: 75.94582231399434
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB LEMBNarrativeQARetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: test
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 23.093
    - type: map_at_10
      value: 30.227999999999998
    - type: map_at_100
      value: 31.423000000000002
    - type: map_at_1000
      value: 31.533
    - type: map_at_20
      value: 30.835
    - type: map_at_3
      value: 27.983999999999998
    - type: map_at_5
      value: 29.253
    - type: mrr_at_1
      value: 23.093
    - type: mrr_at_10
      value: 30.227999999999998
    - type: mrr_at_100
      value: 31.423000000000002
    - type: mrr_at_1000
      value: 31.533
    - type: mrr_at_20
      value: 30.835
    - type: mrr_at_3
      value: 27.983999999999998
    - type: mrr_at_5
      value: 29.253
    - type: ndcg_at_1
      value: 23.093
    - type: ndcg_at_10
      value: 34.297
    - type: ndcg_at_100
      value: 41.049
    - type: ndcg_at_1000
      value: 43.566
    - type: ndcg_at_20
      value: 36.52
    - type: ndcg_at_3
      value: 29.629
    - type: ndcg_at_5
      value: 31.926
    - type: precision_at_1
      value: 23.093
    - type: precision_at_10
      value: 4.735
    - type: precision_at_100
      value: 0.8109999999999999
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 2.8080000000000003
    - type: precision_at_3
      value: 11.468
    - type: precision_at_5
      value: 8.001
    - type: recall_at_1
      value: 23.093
    - type: recall_at_10
      value: 47.354
    - type: recall_at_100
      value: 81.147
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 56.16799999999999
    - type: recall_at_3
      value: 34.405
    - type: recall_at_5
      value: 40.004
    - type: main_score
      value: 34.297
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB LEMBNeedleRetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: test_256
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 64.0
    - type: map_at_10
      value: 77.083
    - type: map_at_100
      value: 77.265
    - type: map_at_1000
      value: 77.265
    - type: map_at_20
      value: 77.265
    - type: map_at_3
      value: 76.333
    - type: map_at_5
      value: 76.833
    - type: mrr_at_1
      value: 64.0
    - type: mrr_at_10
      value: 77.083
    - type: mrr_at_100
      value: 77.265
    - type: mrr_at_1000
      value: 77.265
    - type: mrr_at_20
      value: 77.265
    - type: mrr_at_3
      value: 76.333
    - type: mrr_at_5
      value: 76.833
    - type: ndcg_at_1
      value: 64.0
    - type: ndcg_at_10
      value: 82.325
    - type: ndcg_at_100
      value: 82.883
    - type: ndcg_at_1000
      value: 82.883
    - type: ndcg_at_20
      value: 82.883
    - type: ndcg_at_3
      value: 80.833
    - type: ndcg_at_5
      value: 81.694
    - type: precision_at_1
      value: 64.0
    - type: precision_at_10
      value: 9.8
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 5.0
    - type: precision_at_3
      value: 31.333
    - type: precision_at_5
      value: 19.2
    - type: recall_at_1
      value: 64.0
    - type: recall_at_10
      value: 98.0
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 100.0
    - type: recall_at_3
      value: 94.0
    - type: recall_at_5
      value: 96.0
    - type: main_score
      value: 64.0
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB LEMBPasskeyRetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: test_256
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 100.0
    - type: map_at_10
      value: 100.0
    - type: map_at_100
      value: 100.0
    - type: map_at_1000
      value: 100.0
    - type: map_at_20
      value: 100.0
    - type: map_at_3
      value: 100.0
    - type: map_at_5
      value: 100.0
    - type: mrr_at_1
      value: 100.0
    - type: mrr_at_10
      value: 100.0
    - type: mrr_at_100
      value: 100.0
    - type: mrr_at_1000
      value: 100.0
    - type: mrr_at_20
      value: 100.0
    - type: mrr_at_3
      value: 100.0
    - type: mrr_at_5
      value: 100.0
    - type: ndcg_at_1
      value: 100.0
    - type: ndcg_at_10
      value: 100.0
    - type: ndcg_at_100
      value: 100.0
    - type: ndcg_at_1000
      value: 100.0
    - type: ndcg_at_20
      value: 100.0
    - type: ndcg_at_3
      value: 100.0
    - type: ndcg_at_5
      value: 100.0
    - type: precision_at_1
      value: 100.0
    - type: precision_at_10
      value: 10.0
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 5.0
    - type: precision_at_3
      value: 33.333
    - type: precision_at_5
      value: 20.0
    - type: recall_at_1
      value: 100.0
    - type: recall_at_10
      value: 100.0
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 100.0
    - type: recall_at_3
      value: 100.0
    - type: recall_at_5
      value: 100.0
    - type: main_score
      value: 100.0
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB LEMBQMSumRetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: test
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 24.361
    - type: map_at_10
      value: 33.641
    - type: map_at_100
      value: 35.104
    - type: map_at_1000
      value: 35.127
    - type: map_at_20
      value: 34.388999999999996
    - type: map_at_3
      value: 30.255
    - type: map_at_5
      value: 32.079
    - type: mrr_at_1
      value: 24.361
    - type: mrr_at_10
      value: 33.641
    - type: mrr_at_100
      value: 35.104
    - type: mrr_at_1000
      value: 35.127
    - type: mrr_at_20
      value: 34.388999999999996
    - type: mrr_at_3
      value: 30.255
    - type: mrr_at_5
      value: 32.079
    - type: ndcg_at_1
      value: 24.361
    - type: ndcg_at_10
      value: 39.337
    - type: ndcg_at_100
      value: 47.384
    - type: ndcg_at_1000
      value: 47.75
    - type: ndcg_at_20
      value: 42.077999999999996
    - type: ndcg_at_3
      value: 32.235
    - type: ndcg_at_5
      value: 35.524
    - type: precision_at_1
      value: 24.361
    - type: precision_at_10
      value: 5.783
    - type: precision_at_100
      value: 0.975
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 3.435
    - type: precision_at_3
      value: 12.661
    - type: precision_at_5
      value: 9.193999999999999
    - type: recall_at_1
      value: 24.361
    - type: recall_at_10
      value: 57.826
    - type: recall_at_100
      value: 97.51100000000001
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 68.697
    - type: recall_at_3
      value: 37.983
    - type: recall_at_5
      value: 45.972
    - type: main_score
      value: 39.337
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB LEMBSummScreenFDRetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: validation
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 84.821
    - type: map_at_10
      value: 90.11200000000001
    - type: map_at_100
      value: 90.158
    - type: map_at_1000
      value: 90.158
    - type: map_at_20
      value: 90.137
    - type: map_at_3
      value: 89.385
    - type: map_at_5
      value: 89.876
    - type: mrr_at_1
      value: 84.821
    - type: mrr_at_10
      value: 90.11200000000001
    - type: mrr_at_100
      value: 90.158
    - type: mrr_at_1000
      value: 90.158
    - type: mrr_at_20
      value: 90.137
    - type: mrr_at_3
      value: 89.385
    - type: mrr_at_5
      value: 89.876
    - type: ndcg_at_1
      value: 84.821
    - type: ndcg_at_10
      value: 92.334
    - type: ndcg_at_100
      value: 92.535
    - type: ndcg_at_1000
      value: 92.535
    - type: ndcg_at_20
      value: 92.414
    - type: ndcg_at_3
      value: 90.887
    - type: ndcg_at_5
      value: 91.758
    - type: precision_at_1
      value: 84.821
    - type: precision_at_10
      value: 9.911
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.97
    - type: precision_at_3
      value: 31.746000000000002
    - type: precision_at_5
      value: 19.464000000000002
    - type: recall_at_1
      value: 84.821
    - type: recall_at_10
      value: 99.107
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 99.405
    - type: recall_at_3
      value: 95.238
    - type: recall_at_5
      value: 97.321
    - type: main_score
      value: 92.334
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB LEMBWikimQARetrieval (default)
      revision: 6e346642246bfb4928c560ee08640dc84d074e8c
      split: test
      type: dwzhu/LongEmbed
    metrics:
    - type: map_at_1
      value: 53.667
    - type: map_at_10
      value: 61.719
    - type: map_at_100
      value: 62.471
    - type: map_at_1000
      value: 62.492000000000004
    - type: map_at_20
      value: 62.153000000000006
    - type: map_at_3
      value: 59.167
    - type: map_at_5
      value: 60.95
    - type: mrr_at_1
      value: 53.667
    - type: mrr_at_10
      value: 61.719
    - type: mrr_at_100
      value: 62.471
    - type: mrr_at_1000
      value: 62.492000000000004
    - type: mrr_at_20
      value: 62.153000000000006
    - type: mrr_at_3
      value: 59.167
    - type: mrr_at_5
      value: 60.95
    - type: ndcg_at_1
      value: 53.667
    - type: ndcg_at_10
      value: 66.018
    - type: ndcg_at_100
      value: 69.726
    - type: ndcg_at_1000
      value: 70.143
    - type: ndcg_at_20
      value: 67.61399999999999
    - type: ndcg_at_3
      value: 60.924
    - type: ndcg_at_5
      value: 64.10900000000001
    - type: precision_at_1
      value: 53.667
    - type: precision_at_10
      value: 7.9670000000000005
    - type: precision_at_100
      value: 0.97
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.3
    - type: precision_at_3
      value: 22.0
    - type: precision_at_5
      value: 14.732999999999999
    - type: recall_at_1
      value: 53.667
    - type: recall_at_10
      value: 79.667
    - type: recall_at_100
      value: 97.0
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 86.0
    - type: recall_at_3
      value: 66.0
    - type: recall_at_5
      value: 73.667
    - type: main_score
      value: 66.018
    task:
      type: Retrieval
  - dataset:
      config: deu-deu
      name: MTEB MLQARetrieval (deu-deu)
      revision: 397ed406c1a7902140303e7faf60fff35b58d285
      split: test
      type: facebook/mlqa
    metrics:
    - type: main_score
      value: 67.548
    - type: map_at_1
      value: 56.559000000000005
    - type: map_at_10
      value: 63.867
    - type: map_at_100
      value: 64.429
    - type: map_at_1000
      value: 64.457
    - type: map_at_20
      value: 64.215
    - type: map_at_3
      value: 62.109
    - type: map_at_5
      value: 63.101
    - type: mrr_at_1
      value: 56.56990915134057
    - type: mrr_at_10
      value: 63.86820789324668
    - type: mrr_at_100
      value: 64.42973602152581
    - type: mrr_at_1000
      value: 64.45818598090155
    - type: mrr_at_20
      value: 64.2163052263868
    - type: mrr_at_3
      value: 62.10946155550634
    - type: mrr_at_5
      value: 63.10104143585199
    - type: nauc_map_at_1000_diff1
      value: 73.78440163370111
    - type: nauc_map_at_1000_max
      value: 66.37875518052162
    - type: nauc_map_at_1000_std
      value: -17.063915098135396
    - type: nauc_map_at_100_diff1
      value: 73.77180802985815
    - type: nauc_map_at_100_max
      value: 66.38365998362033
    - type: nauc_map_at_100_std
      value: -17.053345109661972
    - type: nauc_map_at_10_diff1
      value: 73.70041876696037
    - type: nauc_map_at_10_max
      value: 66.33213342705997
    - type: nauc_map_at_10_std
      value: -17.40657791273925
    - type: nauc_map_at_1_diff1
      value: 76.8784374396948
    - type: nauc_map_at_1_max
      value: 64.07170606935357
    - type: nauc_map_at_1_std
      value: -18.464213686790654
    - type: nauc_map_at_20_diff1
      value: 73.72371377231813
    - type: nauc_map_at_20_max
      value: 66.42108121059451
    - type: nauc_map_at_20_std
      value: -17.05384923889036
    - type: nauc_map_at_3_diff1
      value: 74.08287018839246
    - type: nauc_map_at_3_max
      value: 66.42422337760333
    - type: nauc_map_at_3_std
      value: -17.79503404131652
    - type: nauc_map_at_5_diff1
      value: 73.9294779027339
    - type: nauc_map_at_5_max
      value: 66.51752041065726
    - type: nauc_map_at_5_std
      value: -17.67309805113804
    - type: nauc_mrr_at_1000_diff1
      value: 73.78389736923545
    - type: nauc_mrr_at_1000_max
      value: 66.37929720858341
    - type: nauc_mrr_at_1000_std
      value: -17.058591711291278
    - type: nauc_mrr_at_100_diff1
      value: 73.77126451253136
    - type: nauc_mrr_at_100_max
      value: 66.38405917246607
    - type: nauc_mrr_at_100_std
      value: -17.047251035212863
    - type: nauc_mrr_at_10_diff1
      value: 73.69960470665124
    - type: nauc_mrr_at_10_max
      value: 66.33265194210313
    - type: nauc_mrr_at_10_std
      value: -17.399659076827998
    - type: nauc_mrr_at_1_diff1
      value: 76.8689850260726
    - type: nauc_mrr_at_1_max
      value: 64.09858188287487
    - type: nauc_mrr_at_1_std
      value: -18.46064784201847
    - type: nauc_mrr_at_20_diff1
      value: 73.72312682063128
    - type: nauc_mrr_at_20_max
      value: 66.42181932858745
    - type: nauc_mrr_at_20_std
      value: -17.04690257511092
    - type: nauc_mrr_at_3_diff1
      value: 74.08287018839246
    - type: nauc_mrr_at_3_max
      value: 66.42422337760333
    - type: nauc_mrr_at_3_std
      value: -17.79503404131652
    - type: nauc_mrr_at_5_diff1
      value: 73.9294779027339
    - type: nauc_mrr_at_5_max
      value: 66.51752041065726
    - type: nauc_mrr_at_5_std
      value: -17.67309805113804
    - type: nauc_ndcg_at_1000_diff1
      value: 72.97825548342801
    - type: nauc_ndcg_at_1000_max
      value: 66.96275437178257
    - type: nauc_ndcg_at_1000_std
      value: -15.611902299641587
    - type: nauc_ndcg_at_100_diff1
      value: 72.58724738936613
    - type: nauc_ndcg_at_100_max
      value: 67.16774012704182
    - type: nauc_ndcg_at_100_std
      value: -14.945088654796812
    - type: nauc_ndcg_at_10_diff1
      value: 72.16253640477947
    - type: nauc_ndcg_at_10_max
      value: 67.01746849484621
    - type: nauc_ndcg_at_10_std
      value: -16.46102507270809
    - type: nauc_ndcg_at_1_diff1
      value: 76.8689850260726
    - type: nauc_ndcg_at_1_max
      value: 64.09858188287487
    - type: nauc_ndcg_at_1_std
      value: -18.46064784201847
    - type: nauc_ndcg_at_20_diff1
      value: 72.19995325129975
    - type: nauc_ndcg_at_20_max
      value: 67.39639713797962
    - type: nauc_ndcg_at_20_std
      value: -15.091689370748531
    - type: nauc_ndcg_at_3_diff1
      value: 73.13123604206514
    - type: nauc_ndcg_at_3_max
      value: 67.23123167871547
    - type: nauc_ndcg_at_3_std
      value: -17.492755234009156
    - type: nauc_ndcg_at_5_diff1
      value: 72.8154718929895
    - type: nauc_ndcg_at_5_max
      value: 67.44578008373777
    - type: nauc_ndcg_at_5_std
      value: -17.251840358751362
    - type: nauc_precision_at_1000_diff1
      value: 47.89748325983604
    - type: nauc_precision_at_1000_max
      value: 70.47466197804906
    - type: nauc_precision_at_1000_std
      value: 72.66193512114775
    - type: nauc_precision_at_100_diff1
      value: 59.493743734005356
    - type: nauc_precision_at_100_max
      value: 74.02140147220713
    - type: nauc_precision_at_100_std
      value: 17.26664098026236
    - type: nauc_precision_at_10_diff1
      value: 64.94415011040277
    - type: nauc_precision_at_10_max
      value: 69.6963814950747
    - type: nauc_precision_at_10_std
      value: -11.663043657012954
    - type: nauc_precision_at_1_diff1
      value: 76.8689850260726
    - type: nauc_precision_at_1_max
      value: 64.09858188287487
    - type: nauc_precision_at_1_std
      value: -18.46064784201847
    - type: nauc_precision_at_20_diff1
      value: 63.145886909986416
    - type: nauc_precision_at_20_max
      value: 72.95708033630744
    - type: nauc_precision_at_20_std
      value: -1.5039593629280323
    - type: nauc_precision_at_3_diff1
      value: 69.88902201644449
    - type: nauc_precision_at_3_max
      value: 69.80499971089935
    - type: nauc_precision_at_3_std
      value: -16.444680766676647
    - type: nauc_precision_at_5_diff1
      value: 68.60869967062919
    - type: nauc_precision_at_5_max
      value: 70.75998207564281
    - type: nauc_precision_at_5_std
      value: -15.62613396998262
    - type: nauc_recall_at_1000_diff1
      value: 62.6646436338833
    - type: nauc_recall_at_1000_max
      value: 86.17801636476078
    - type: nauc_recall_at_1000_std
      value: 71.84718775540334
    - type: nauc_recall_at_100_diff1
      value: 61.110492191439505
    - type: nauc_recall_at_100_max
      value: 75.45730686603042
    - type: nauc_recall_at_100_std
      value: 16.202465011589428
    - type: nauc_recall_at_10_diff1
      value: 65.1522196516815
    - type: nauc_recall_at_10_max
      value: 69.7626435962161
    - type: nauc_recall_at_10_std
      value: -11.801178474770449
    - type: nauc_recall_at_1_diff1
      value: 76.8784374396948
    - type: nauc_recall_at_1_max
      value: 64.07170606935357
    - type: nauc_recall_at_1_std
      value: -18.464213686790654
    - type: nauc_recall_at_20_diff1
      value: 63.40332739504143
    - type: nauc_recall_at_20_max
      value: 73.04113661090965
    - type: nauc_recall_at_20_std
      value: -1.6609741140266947
    - type: nauc_recall_at_3_diff1
      value: 70.03728086098866
    - type: nauc_recall_at_3_max
      value: 69.85953774320521
    - type: nauc_recall_at_3_std
      value: -16.482993123411706
    - type: nauc_recall_at_5_diff1
      value: 68.77396121765933
    - type: nauc_recall_at_5_max
      value: 70.8231205493519
    - type: nauc_recall_at_5_std
      value: -15.668037770700863
    - type: ndcg_at_1
      value: 56.57
    - type: ndcg_at_10
      value: 67.548
    - type: ndcg_at_100
      value: 70.421
    - type: ndcg_at_1000
      value: 71.198
    - type: ndcg_at_20
      value: 68.829
    - type: ndcg_at_3
      value: 63.88700000000001
    - type: ndcg_at_5
      value: 65.689
    - type: precision_at_1
      value: 56.57
    - type: precision_at_10
      value: 7.922
    - type: precision_at_100
      value: 0.9299999999999999
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_20
      value: 4.216
    - type: precision_at_3
      value: 23.015
    - type: precision_at_5
      value: 14.691
    - type: recall_at_1
      value: 56.559000000000005
    - type: recall_at_10
      value: 79.182
    - type: recall_at_100
      value: 92.946
    - type: recall_at_1000
      value: 99.092
    - type: recall_at_20
      value: 84.27900000000001
    - type: recall_at_3
      value: 69.023
    - type: recall_at_5
      value: 73.432
    task:
      type: Retrieval
  - dataset:
      config: deu-spa
      name: MTEB MLQARetrieval (deu-spa)
      revision: 397ed406c1a7902140303e7faf60fff35b58d285
      split: test
      type: facebook/mlqa
    metrics:
    - type: main_score
      value: 70.645
    - type: map_at_1
      value: 58.423
    - type: map_at_10
      value: 66.613
    - type: map_at_100
      value: 67.14099999999999
    - type: map_at_1000
      value: 67.161
    - type: map_at_20
      value: 66.965
    - type: map_at_3
      value: 64.714
    - type: map_at_5
      value: 65.835
    - type: mrr_at_1
      value: 58.4225352112676
    - type: mrr_at_10
      value: 66.61321260898735
    - type: mrr_at_100
      value: 67.13991570812132
    - type: mrr_at_1000
      value: 67.1598532168174
    - type: mrr_at_20
      value: 66.96384710024888
    - type: mrr_at_3
      value: 64.71361502347425
    - type: mrr_at_5
      value: 65.83474178403769
    - type: nauc_map_at_1000_diff1
      value: 73.9485117118935
    - type: nauc_map_at_1000_max
      value: 65.74479869396299
    - type: nauc_map_at_1000_std
      value: -20.300269749495563
    - type: nauc_map_at_100_diff1
      value: 73.93900406302829
    - type: nauc_map_at_100_max
      value: 65.75508449194885
    - type: nauc_map_at_100_std
      value: -20.265330791570175
    - type: nauc_map_at_10_diff1
      value: 73.84863233472605
    - type: nauc_map_at_10_max
      value: 65.89377317378211
    - type: nauc_map_at_10_std
      value: -20.404123131964695
    - type: nauc_map_at_1_diff1
      value: 76.73627284218519
    - type: nauc_map_at_1_max
      value: 62.94957512510876
    - type: nauc_map_at_1_std
      value: -20.99649749330682
    - type: nauc_map_at_20_diff1
      value: 73.88712006109598
    - type: nauc_map_at_20_max
      value: 65.82057018162664
    - type: nauc_map_at_20_std
      value: -20.269476512431915
    - type: nauc_map_at_3_diff1
      value: 74.21419190161502
    - type: nauc_map_at_3_max
      value: 65.64993368062119
    - type: nauc_map_at_3_std
      value: -21.34641749007071
    - type: nauc_map_at_5_diff1
      value: 74.0119419385777
    - type: nauc_map_at_5_max
      value: 65.69809416369732
    - type: nauc_map_at_5_std
      value: -21.16901556082261
    - type: nauc_mrr_at_1000_diff1
      value: 73.94915184134923
    - type: nauc_mrr_at_1000_max
      value: 65.74522469633418
    - type: nauc_mrr_at_1000_std
      value: -20.303028367132246
    - type: nauc_mrr_at_100_diff1
      value: 73.93964394728808
    - type: nauc_mrr_at_100_max
      value: 65.75550992323707
    - type: nauc_mrr_at_100_std
      value: -20.26808820438918
    - type: nauc_mrr_at_10_diff1
      value: 73.84863233472605
    - type: nauc_mrr_at_10_max
      value: 65.89377317378211
    - type: nauc_mrr_at_10_std
      value: -20.404123131964695
    - type: nauc_mrr_at_1_diff1
      value: 76.73627284218519
    - type: nauc_mrr_at_1_max
      value: 62.94957512510876
    - type: nauc_mrr_at_1_std
      value: -20.99649749330682
    - type: nauc_mrr_at_20_diff1
      value: 73.88775721128745
    - type: nauc_mrr_at_20_max
      value: 65.820991355628
    - type: nauc_mrr_at_20_std
      value: -20.272216587019734
    - type: nauc_mrr_at_3_diff1
      value: 74.21419190161502
    - type: nauc_mrr_at_3_max
      value: 65.64993368062119
    - type: nauc_mrr_at_3_std
      value: -21.34641749007071
    - type: nauc_mrr_at_5_diff1
      value: 74.0119419385777
    - type: nauc_mrr_at_5_max
      value: 65.69809416369732
    - type: nauc_mrr_at_5_std
      value: -21.16901556082261
    - type: nauc_ndcg_at_1000_diff1
      value: 73.29396365944277
    - type: nauc_ndcg_at_1000_max
      value: 66.44879592109541
    - type: nauc_ndcg_at_1000_std
      value: -19.285991058788195
    - type: nauc_ndcg_at_100_diff1
      value: 73.0159172721162
    - type: nauc_ndcg_at_100_max
      value: 66.76216389231388
    - type: nauc_ndcg_at_100_std
      value: -18.27931368094887
    - type: nauc_ndcg_at_10_diff1
      value: 72.42096650774693
    - type: nauc_ndcg_at_10_max
      value: 67.48592688463306
    - type: nauc_ndcg_at_10_std
      value: -18.91453756077581
    - type: nauc_ndcg_at_1_diff1
      value: 76.73627284218519
    - type: nauc_ndcg_at_1_max
      value: 62.94957512510876
    - type: nauc_ndcg_at_1_std
      value: -20.99649749330682
    - type: nauc_ndcg_at_20_diff1
      value: 72.53699362385684
    - type: nauc_ndcg_at_20_max
      value: 67.22763976357872
    - type: nauc_ndcg_at_20_std
      value: -18.299910635008338
    - type: nauc_ndcg_at_3_diff1
      value: 73.3698453761989
    - type: nauc_ndcg_at_3_max
      value: 66.71056987289383
    - type: nauc_ndcg_at_3_std
      value: -21.405154376652803
    - type: nauc_ndcg_at_5_diff1
      value: 72.9491030712935
    - type: nauc_ndcg_at_5_max
      value: 66.85786103137077
    - type: nauc_ndcg_at_5_std
      value: -21.04005053344073
    - type: nauc_precision_at_1000_diff1
      value: 17.02462370967451
    - type: nauc_precision_at_1000_max
      value: 48.03260752496052
    - type: nauc_precision_at_1000_std
      value: 87.56077915079334
    - type: nauc_precision_at_100_diff1
      value: 58.590352501194985
    - type: nauc_precision_at_100_max
      value: 78.2649015433222
    - type: nauc_precision_at_100_std
      value: 28.05030453158992
    - type: nauc_precision_at_10_diff1
      value: 64.89497928764766
    - type: nauc_precision_at_10_max
      value: 75.93257124951242
    - type: nauc_precision_at_10_std
      value: -9.825306994117462
    - type: nauc_precision_at_1_diff1
      value: 76.73627284218519
    - type: nauc_precision_at_1_max
      value: 62.94957512510876
    - type: nauc_precision_at_1_std
      value: -20.99649749330682
    - type: nauc_precision_at_20_diff1
      value: 62.11366204321558
    - type: nauc_precision_at_20_max
      value: 75.9571427846493
    - type: nauc_precision_at_20_std
      value: -0.94585212808191
    - type: nauc_precision_at_3_diff1
      value: 70.52940972112398
    - type: nauc_precision_at_3_max
      value: 70.3402053170779
    - type: nauc_precision_at_3_std
      value: -21.579778424241304
    - type: nauc_precision_at_5_diff1
      value: 68.78962580223575
    - type: nauc_precision_at_5_max
      value: 71.41410894398376
    - type: nauc_precision_at_5_std
      value: -20.415603405161956
    - type: nauc_recall_at_1000_diff1
      value: 55.88625447348128
    - type: nauc_recall_at_1000_max
      value: 100.0
    - type: nauc_recall_at_1000_std
      value: 100.0
    - type: nauc_recall_at_100_diff1
      value: 61.17942268389525
    - type: nauc_recall_at_100_max
      value: 81.12207841563487
    - type: nauc_recall_at_100_std
      value: 27.141215257528113
    - type: nauc_recall_at_10_diff1
      value: 64.8949792876478
    - type: nauc_recall_at_10_max
      value: 75.93257124951249
    - type: nauc_recall_at_10_std
      value: -9.825306994117323
    - type: nauc_recall_at_1_diff1
      value: 76.73627284218519
    - type: nauc_recall_at_1_max
      value: 62.94957512510876
    - type: nauc_recall_at_1_std
      value: -20.99649749330682
    - type: nauc_recall_at_20_diff1
      value: 63.07808719241162
    - type: nauc_recall_at_20_max
      value: 76.96808746317542
    - type: nauc_recall_at_20_std
      value: -1.5235053258631275
    - type: nauc_recall_at_3_diff1
      value: 70.52940972112405
    - type: nauc_recall_at_3_max
      value: 70.3402053170779
    - type: nauc_recall_at_3_std
      value: -21.57977842424124
    - type: nauc_recall_at_5_diff1
      value: 68.78962580223575
    - type: nauc_recall_at_5_max
      value: 71.41410894398392
    - type: nauc_recall_at_5_std
      value: -20.415603405161793
    - type: ndcg_at_1
      value: 58.423
    - type: ndcg_at_10
      value: 70.645
    - type: ndcg_at_100
      value: 73.277
    - type: ndcg_at_1000
      value: 73.785
    - type: ndcg_at_20
      value: 71.918
    - type: ndcg_at_3
      value: 66.679
    - type: ndcg_at_5
      value: 68.72200000000001
    - type: precision_at_1
      value: 58.423
    - type: precision_at_10
      value: 8.338
    - type: precision_at_100
      value: 0.959
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.423
    - type: precision_at_3
      value: 24.113
    - type: precision_at_5
      value: 15.47
    - type: recall_at_1
      value: 58.423
    - type: recall_at_10
      value: 83.38
    - type: recall_at_100
      value: 95.887
    - type: recall_at_1000
      value: 99.831
    - type: recall_at_20
      value: 88.39399999999999
    - type: recall_at_3
      value: 72.33800000000001
    - type: recall_at_5
      value: 77.352
    task:
      type: Retrieval
  - dataset:
      config: deu-eng
      name: MTEB MLQARetrieval (deu-eng)
      revision: 397ed406c1a7902140303e7faf60fff35b58d285
      split: test
      type: facebook/mlqa
    metrics:
    - type: main_score
      value: 67.067
    - type: map_at_1
      value: 55.861000000000004
    - type: map_at_10
      value: 63.42100000000001
    - type: map_at_100
      value: 64.03
    - type: map_at_1000
      value: 64.05999999999999
    - type: map_at_20
      value: 63.819
    - type: map_at_3
      value: 61.773
    - type: map_at_5
      value: 62.736999999999995
    - type: mrr_at_1
      value: 55.88300465322402
    - type: mrr_at_10
      value: 63.43111082973707
    - type: mrr_at_100
      value: 64.03962373590272
    - type: mrr_at_1000
      value: 64.0698259866376
    - type: mrr_at_20
      value: 63.82871766489112
    - type: mrr_at_3
      value: 61.78447448112865
    - type: mrr_at_5
      value: 62.74835659945346
    - type: nauc_map_at_1000_diff1
      value: 74.58505763417352
    - type: nauc_map_at_1000_max
      value: 66.26060764852198
    - type: nauc_map_at_1000_std
      value: -16.896178230873897
    - type: nauc_map_at_100_diff1
      value: 74.57057487892857
    - type: nauc_map_at_100_max
      value: 66.26600433283826
    - type: nauc_map_at_100_std
      value: -16.87596113104189
    - type: nauc_map_at_10_diff1
      value: 74.53453636322749
    - type: nauc_map_at_10_max
      value: 66.27501737773804
    - type: nauc_map_at_10_std
      value: -17.178743257781775
    - type: nauc_map_at_1_diff1
      value: 77.63067209375254
    - type: nauc_map_at_1_max
      value: 64.17718675702672
    - type: nauc_map_at_1_std
      value: -17.639521106853717
    - type: nauc_map_at_20_diff1
      value: 74.52007402431164
    - type: nauc_map_at_20_max
      value: 66.28276291359268
    - type: nauc_map_at_20_std
      value: -16.939292897754758
    - type: nauc_map_at_3_diff1
      value: 74.79187974631951
    - type: nauc_map_at_3_max
      value: 66.23256568210611
    - type: nauc_map_at_3_std
      value: -17.894889918934112
    - type: nauc_map_at_5_diff1
      value: 74.63011328882517
    - type: nauc_map_at_5_max
      value: 66.35411054978499
    - type: nauc_map_at_5_std
      value: -17.50140342194211
    - type: nauc_mrr_at_1000_diff1
      value: 74.57520089771667
    - type: nauc_mrr_at_1000_max
      value: 66.27270912845914
    - type: nauc_mrr_at_1000_std
      value: -16.84012675362397
    - type: nauc_mrr_at_100_diff1
      value: 74.56070964572156
    - type: nauc_mrr_at_100_max
      value: 66.2780701126926
    - type: nauc_mrr_at_100_std
      value: -16.820035083069865
    - type: nauc_mrr_at_10_diff1
      value: 74.52455978435117
    - type: nauc_mrr_at_10_max
      value: 66.28697244023137
    - type: nauc_mrr_at_10_std
      value: -17.122477723330523
    - type: nauc_mrr_at_1_diff1
      value: 77.60643512422061
    - type: nauc_mrr_at_1_max
      value: 64.21736966061896
    - type: nauc_mrr_at_1_std
      value: -17.56627338275146
    - type: nauc_mrr_at_20_diff1
      value: 74.5099814266373
    - type: nauc_mrr_at_20_max
      value: 66.29485560556576
    - type: nauc_mrr_at_20_std
      value: -16.882350027335306
    - type: nauc_mrr_at_3_diff1
      value: 74.78132817375507
    - type: nauc_mrr_at_3_max
      value: 66.24761860047623
    - type: nauc_mrr_at_3_std
      value: -17.833128575678998
    - type: nauc_mrr_at_5_diff1
      value: 74.6193031207433
    - type: nauc_mrr_at_5_max
      value: 66.36951764432901
    - type: nauc_mrr_at_5_std
      value: -17.438203106324227
    - type: nauc_ndcg_at_1000_diff1
      value: 73.79386161629151
    - type: nauc_ndcg_at_1000_max
      value: 66.84013038018082
    - type: nauc_ndcg_at_1000_std
      value: -15.387358822700667
    - type: nauc_ndcg_at_100_diff1
      value: 73.36132885277745
    - type: nauc_ndcg_at_100_max
      value: 67.04416926901568
    - type: nauc_ndcg_at_100_std
      value: -14.503256942521972
    - type: nauc_ndcg_at_10_diff1
      value: 73.11847332785027
    - type: nauc_ndcg_at_10_max
      value: 67.02149621303091
    - type: nauc_ndcg_at_10_std
      value: -16.142234662067782
    - type: nauc_ndcg_at_1_diff1
      value: 77.60643512422061
    - type: nauc_ndcg_at_1_max
      value: 64.21736966061896
    - type: nauc_ndcg_at_1_std
      value: -17.56627338275146
    - type: nauc_ndcg_at_20_diff1
      value: 72.97961452569768
    - type: nauc_ndcg_at_20_max
      value: 67.12369127081152
    - type: nauc_ndcg_at_20_std
      value: -15.11921773223936
    - type: nauc_ndcg_at_3_diff1
      value: 73.77769312598772
    - type: nauc_ndcg_at_3_max
      value: 66.94438755852309
    - type: nauc_ndcg_at_3_std
      value: -17.75960443830741
    - type: nauc_ndcg_at_5_diff1
      value: 73.43991209562891
    - type: nauc_ndcg_at_5_max
      value: 67.21682951737418
    - type: nauc_ndcg_at_5_std
      value: -17.013510008231805
    - type: nauc_precision_at_1000_diff1
      value: 51.30633281948362
    - type: nauc_precision_at_1000_max
      value: 76.78675288883846
    - type: nauc_precision_at_1000_std
      value: 71.70041985304397
    - type: nauc_precision_at_100_diff1
      value: 59.86656455853326
    - type: nauc_precision_at_100_max
      value: 74.41958422732161
    - type: nauc_precision_at_100_std
      value: 22.098920296069124
    - type: nauc_precision_at_10_diff1
      value: 66.4696166928741
    - type: nauc_precision_at_10_max
      value: 69.88463108697104
    - type: nauc_precision_at_10_std
      value: -10.707950954702742
    - type: nauc_precision_at_1_diff1
      value: 77.60643512422061
    - type: nauc_precision_at_1_max
      value: 64.21736966061896
    - type: nauc_precision_at_1_std
      value: -17.56627338275146
    - type: nauc_precision_at_20_diff1
      value: 63.45094585276983
    - type: nauc_precision_at_20_max
      value: 71.57741245347195
    - type: nauc_precision_at_20_std
      value: -2.2211545419051744
    - type: nauc_precision_at_3_diff1
      value: 70.28060818081384
    - type: nauc_precision_at_3_max
      value: 69.22652927816439
    - type: nauc_precision_at_3_std
      value: -17.158576243559434
    - type: nauc_precision_at_5_diff1
      value: 68.90765418427162
    - type: nauc_precision_at_5_max
      value: 70.32585273389111
    - type: nauc_precision_at_5_std
      value: -14.950363729664524
    - type: nauc_recall_at_1000_diff1
      value: 65.11255117927331
    - type: nauc_recall_at_1000_max
      value: 88.35641213283338
    - type: nauc_recall_at_1000_std
      value: 69.89792573640547
    - type: nauc_recall_at_100_diff1
      value: 61.46376457272238
    - type: nauc_recall_at_100_max
      value: 75.48265142243015
    - type: nauc_recall_at_100_std
      value: 21.223182712042178
    - type: nauc_recall_at_10_diff1
      value: 66.89353375308997
    - type: nauc_recall_at_10_max
      value: 70.06655416883785
    - type: nauc_recall_at_10_std
      value: -11.100871879439435
    - type: nauc_recall_at_1_diff1
      value: 77.63067209375254
    - type: nauc_recall_at_1_max
      value: 64.17718675702672
    - type: nauc_recall_at_1_std
      value: -17.639521106853717
    - type: nauc_recall_at_20_diff1
      value: 63.98532276331878
    - type: nauc_recall_at_20_max
      value: 71.81562599791899
    - type: nauc_recall_at_20_std
      value: -2.696537977147695
    - type: nauc_recall_at_3_diff1
      value: 70.4507655865698
    - type: nauc_recall_at_3_max
      value: 69.25705030141037
    - type: nauc_recall_at_3_std
      value: -17.299948348202836
    - type: nauc_recall_at_5_diff1
      value: 69.09152857901888
    - type: nauc_recall_at_5_max
      value: 70.35609636026405
    - type: nauc_recall_at_5_std
      value: -15.105012139255896
    - type: ndcg_at_1
      value: 55.883
    - type: ndcg_at_10
      value: 67.067
    - type: ndcg_at_100
      value: 70.07
    - type: ndcg_at_1000
      value: 70.875
    - type: ndcg_at_20
      value: 68.498
    - type: ndcg_at_3
      value: 63.666
    - type: ndcg_at_5
      value: 65.40599999999999
    - type: precision_at_1
      value: 55.883
    - type: precision_at_10
      value: 7.8549999999999995
    - type: precision_at_100
      value: 0.928
    - type: precision_at_1000
      value: 0.099
    - type: precision_at_20
      value: 4.2090000000000005
    - type: precision_at_3
      value: 23.052
    - type: precision_at_5
      value: 14.677999999999999
    - type: recall_at_1
      value: 55.861000000000004
    - type: recall_at_10
      value: 78.495
    - type: recall_at_100
      value: 92.688
    - type: recall_at_1000
      value: 99.02499999999999
    - type: recall_at_20
      value: 84.124
    - type: recall_at_3
      value: 69.123
    - type: recall_at_5
      value: 73.355
    task:
      type: Retrieval
  - dataset:
      config: spa-deu
      name: MTEB MLQARetrieval (spa-deu)
      revision: 397ed406c1a7902140303e7faf60fff35b58d285
      split: test
      type: facebook/mlqa
    metrics:
    - type: main_score
      value: 73.90299999999999
    - type: map_at_1
      value: 61.236000000000004
    - type: map_at_10
      value: 69.88799999999999
    - type: map_at_100
      value: 70.319
    - type: map_at_1000
      value: 70.341
    - type: map_at_20
      value: 70.16799999999999
    - type: map_at_3
      value: 68.104
    - type: map_at_5
      value: 69.164
    - type: mrr_at_1
      value: 61.2739571589628
    - type: mrr_at_10
      value: 69.92589162684993
    - type: mrr_at_100
      value: 70.35245455509234
    - type: mrr_at_1000
      value: 70.37438351396742
    - type: mrr_at_20
      value: 70.20247469915404
    - type: mrr_at_3
      value: 68.14167606163099
    - type: mrr_at_5
      value: 69.20142803457354
    - type: nauc_map_at_1000_diff1
      value: 74.70416754842327
    - type: nauc_map_at_1000_max
      value: 65.86915994583384
    - type: nauc_map_at_1000_std
      value: -19.04437483534443
    - type: nauc_map_at_100_diff1
      value: 74.70011798058674
    - type: nauc_map_at_100_max
      value: 65.88507779167188
    - type: nauc_map_at_100_std
      value: -19.018670970643786
    - type: nauc_map_at_10_diff1
      value: 74.6362126804427
    - type: nauc_map_at_10_max
      value: 66.05733054427198
    - type: nauc_map_at_10_std
      value: -19.034317737897354
    - type: nauc_map_at_1_diff1
      value: 77.24970536833601
    - type: nauc_map_at_1_max
      value: 62.07820573048406
    - type: nauc_map_at_1_std
      value: -20.917086586335078
    - type: nauc_map_at_20_diff1
      value: 74.64113920401083
    - type: nauc_map_at_20_max
      value: 65.89991740166793
    - type: nauc_map_at_20_std
      value: -19.09987515041243
    - type: nauc_map_at_3_diff1
      value: 74.6518162332119
    - type: nauc_map_at_3_max
      value: 66.10312348194024
    - type: nauc_map_at_3_std
      value: -18.95881457716116
    - type: nauc_map_at_5_diff1
      value: 74.55141020670321
    - type: nauc_map_at_5_max
      value: 65.94345752979342
    - type: nauc_map_at_5_std
      value: -19.453976877992304
    - type: nauc_mrr_at_1000_diff1
      value: 74.64458488344088
    - type: nauc_mrr_at_1000_max
      value: 65.84575328456057
    - type: nauc_mrr_at_1000_std
      value: -18.901614615119904
    - type: nauc_mrr_at_100_diff1
      value: 74.64058497924627
    - type: nauc_mrr_at_100_max
      value: 65.86170461767928
    - type: nauc_mrr_at_100_std
      value: -18.87601697091505
    - type: nauc_mrr_at_10_diff1
      value: 74.57266634464752
    - type: nauc_mrr_at_10_max
      value: 66.03331587645152
    - type: nauc_mrr_at_10_std
      value: -18.87888060105393
    - type: nauc_mrr_at_1_diff1
      value: 77.19578272647183
    - type: nauc_mrr_at_1_max
      value: 62.05252035478773
    - type: nauc_mrr_at_1_std
      value: -20.790530940625267
    - type: nauc_mrr_at_20_diff1
      value: 74.5808171250021
    - type: nauc_mrr_at_20_max
      value: 65.87643606587798
    - type: nauc_mrr_at_20_std
      value: -18.95476583474199
    - type: nauc_mrr_at_3_diff1
      value: 74.5917053289191
    - type: nauc_mrr_at_3_max
      value: 66.08044079438714
    - type: nauc_mrr_at_3_std
      value: -18.81168463163586
    - type: nauc_mrr_at_5_diff1
      value: 74.48934579694608
    - type: nauc_mrr_at_5_max
      value: 65.91993162383771
    - type: nauc_mrr_at_5_std
      value: -19.302710791338797
    - type: nauc_ndcg_at_1000_diff1
      value: 74.20191283992186
    - type: nauc_ndcg_at_1000_max
      value: 66.60831175771229
    - type: nauc_ndcg_at_1000_std
      value: -18.175208725175484
    - type: nauc_ndcg_at_100_diff1
      value: 74.07713451642955
    - type: nauc_ndcg_at_100_max
      value: 67.02028626335476
    - type: nauc_ndcg_at_100_std
      value: -17.36560972181693
    - type: nauc_ndcg_at_10_diff1
      value: 73.63235521598476
    - type: nauc_ndcg_at_10_max
      value: 67.8118473312638
    - type: nauc_ndcg_at_10_std
      value: -17.647560577355915
    - type: nauc_ndcg_at_1_diff1
      value: 77.19578272647183
    - type: nauc_ndcg_at_1_max
      value: 62.05252035478773
    - type: nauc_ndcg_at_1_std
      value: -20.790530940625267
    - type: nauc_ndcg_at_20_diff1
      value: 73.65300308228291
    - type: nauc_ndcg_at_20_max
      value: 67.18353402731985
    - type: nauc_ndcg_at_20_std
      value: -17.9240756389792
    - type: nauc_ndcg_at_3_diff1
      value: 73.73764900202292
    - type: nauc_ndcg_at_3_max
      value: 67.60840957876889
    - type: nauc_ndcg_at_3_std
      value: -17.962667543518933
    - type: nauc_ndcg_at_5_diff1
      value: 73.49040500302092
    - type: nauc_ndcg_at_5_max
      value: 67.41251918514402
    - type: nauc_ndcg_at_5_std
      value: -18.851877225955523
    - type: nauc_precision_at_1000_diff1
      value: -18.652906102973922
    - type: nauc_precision_at_1000_max
      value: 2.1701672475574885
    - type: nauc_precision_at_1000_std
      value: 61.713411950188835
    - type: nauc_precision_at_100_diff1
      value: 62.37565302288498
    - type: nauc_precision_at_100_max
      value: 76.96921843049006
    - type: nauc_precision_at_100_std
      value: 19.152009040219678
    - type: nauc_precision_at_10_diff1
      value: 68.14047344105212
    - type: nauc_precision_at_10_max
      value: 77.7177273849099
    - type: nauc_precision_at_10_std
      value: -9.124325941493698
    - type: nauc_precision_at_1_diff1
      value: 77.19578272647183
    - type: nauc_precision_at_1_max
      value: 62.05252035478773
    - type: nauc_precision_at_1_std
      value: -20.790530940625267
    - type: nauc_precision_at_20_diff1
      value: 65.38487456362745
    - type: nauc_precision_at_20_max
      value: 74.61122933443669
    - type: nauc_precision_at_20_std
      value: -8.129775929648341
    - type: nauc_precision_at_3_diff1
      value: 70.45937744142297
    - type: nauc_precision_at_3_max
      value: 73.03004233073901
    - type: nauc_precision_at_3_std
      value: -14.246554579025158
    - type: nauc_precision_at_5_diff1
      value: 69.02821772428955
    - type: nauc_precision_at_5_max
      value: 73.52949774726446
    - type: nauc_precision_at_5_std
      value: -16.355747231517757
    - type: nauc_recall_at_1000_diff1
      value: 35.804192824985755
    - type: nauc_recall_at_1000_max
      value: 61.367785756485894
    - type: nauc_recall_at_1000_std
      value: 54.01380822466869
    - type: nauc_recall_at_100_diff1
      value: 67.96210883597479
    - type: nauc_recall_at_100_max
      value: 82.38124823732169
    - type: nauc_recall_at_100_std
      value: 16.814922595309966
    - type: nauc_recall_at_10_diff1
      value: 68.21964459634341
    - type: nauc_recall_at_10_max
      value: 77.68301934858845
    - type: nauc_recall_at_10_std
      value: -9.430792913885066
    - type: nauc_recall_at_1_diff1
      value: 77.24970536833601
    - type: nauc_recall_at_1_max
      value: 62.07820573048406
    - type: nauc_recall_at_1_std
      value: -20.917086586335078
    - type: nauc_recall_at_20_diff1
      value: 66.60569906579487
    - type: nauc_recall_at_20_max
      value: 75.66163186604354
    - type: nauc_recall_at_20_std
      value: -9.09826205489828
    - type: nauc_recall_at_3_diff1
      value: 70.52323701841641
    - type: nauc_recall_at_3_max
      value: 73.03478107411232
    - type: nauc_recall_at_3_std
      value: -14.432325989967962
    - type: nauc_recall_at_5_diff1
      value: 69.08521261524373
    - type: nauc_recall_at_5_max
      value: 73.51150270382094
    - type: nauc_recall_at_5_std
      value: -16.569387503524368
    - type: ndcg_at_1
      value: 61.273999999999994
    - type: ndcg_at_10
      value: 73.90299999999999
    - type: ndcg_at_100
      value: 75.983
    - type: ndcg_at_1000
      value: 76.488
    - type: ndcg_at_20
      value: 74.921
    - type: ndcg_at_3
      value: 70.277
    - type: ndcg_at_5
      value: 72.172
    - type: precision_at_1
      value: 61.273999999999994
    - type: precision_at_10
      value: 8.641
    - type: precision_at_100
      value: 0.962
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.524
    - type: precision_at_3
      value: 25.517
    - type: precision_at_5
      value: 16.223000000000003
    - type: recall_at_1
      value: 61.236000000000004
    - type: recall_at_10
      value: 86.37700000000001
    - type: recall_at_100
      value: 96.054
    - type: recall_at_1000
      value: 99.887
    - type: recall_at_20
      value: 90.398
    - type: recall_at_3
      value: 76.51299999999999
    - type: recall_at_5
      value: 81.07900000000001
    task:
      type: Retrieval
  - dataset:
      config: spa-spa
      name: MTEB MLQARetrieval (spa-spa)
      revision: 397ed406c1a7902140303e7faf60fff35b58d285
      split: test
      type: facebook/mlqa
    metrics:
    - type: main_score
      value: 68.632
    - type: map_at_1
      value: 57.046
    - type: map_at_10
      value: 64.869
    - type: map_at_100
      value: 65.384
    - type: map_at_1000
      value: 65.413
    - type: map_at_20
      value: 65.185
    - type: map_at_3
      value: 63.178
    - type: map_at_5
      value: 64.12
    - type: mrr_at_1
      value: 57.05579889544848
    - type: mrr_at_10
      value: 64.8806425382317
    - type: mrr_at_100
      value: 65.39469233244084
    - type: mrr_at_1000
      value: 65.42342199403159
    - type: mrr_at_20
      value: 65.19634815919534
    - type: mrr_at_3
      value: 63.18796419729591
    - type: mrr_at_5
      value: 64.13159398209874
    - type: nauc_map_at_1000_diff1
      value: 73.23803038674018
    - type: nauc_map_at_1000_max
      value: 67.44156201421714
    - type: nauc_map_at_1000_std
      value: -8.60143026450049
    - type: nauc_map_at_100_diff1
      value: 73.22575613034235
    - type: nauc_map_at_100_max
      value: 67.44735143420195
    - type: nauc_map_at_100_std
      value: -8.576905069492895
    - type: nauc_map_at_10_diff1
      value: 73.11950129610865
    - type: nauc_map_at_10_max
      value: 67.45107232305055
    - type: nauc_map_at_10_std
      value: -8.799837857015392
    - type: nauc_map_at_1_diff1
      value: 76.18354072047988
    - type: nauc_map_at_1_max
      value: 65.03342186728786
    - type: nauc_map_at_1_std
      value: -10.867650288695796
    - type: nauc_map_at_20_diff1
      value: 73.21570748770948
    - type: nauc_map_at_20_max
      value: 67.50340321088724
    - type: nauc_map_at_20_std
      value: -8.594057184944676
    - type: nauc_map_at_3_diff1
      value: 73.17239276163892
    - type: nauc_map_at_3_max
      value: 67.06319504819103
    - type: nauc_map_at_3_std
      value: -9.883216310270528
    - type: nauc_map_at_5_diff1
      value: 73.11913507367727
    - type: nauc_map_at_5_max
      value: 67.27497019567078
    - type: nauc_map_at_5_std
      value: -9.497714822103118
    - type: nauc_mrr_at_1000_diff1
      value: 73.22971233311306
    - type: nauc_mrr_at_1000_max
      value: 67.42977229057223
    - type: nauc_mrr_at_1000_std
      value: -8.550068702273297
    - type: nauc_mrr_at_100_diff1
      value: 73.21744467317815
    - type: nauc_mrr_at_100_max
      value: 67.43557491068093
    - type: nauc_mrr_at_100_std
      value: -8.52559275190607
    - type: nauc_mrr_at_10_diff1
      value: 73.11075619726137
    - type: nauc_mrr_at_10_max
      value: 67.43889760205286
    - type: nauc_mrr_at_10_std
      value: -8.74617232559183
    - type: nauc_mrr_at_1_diff1
      value: 76.17529975949547
    - type: nauc_mrr_at_1_max
      value: 65.02401127001608
    - type: nauc_mrr_at_1_std
      value: -10.817814457633952
    - type: nauc_mrr_at_20_diff1
      value: 73.20689275225138
    - type: nauc_mrr_at_20_max
      value: 67.49111752272192
    - type: nauc_mrr_at_20_std
      value: -8.539827528410353
    - type: nauc_mrr_at_3_diff1
      value: 73.16291729623958
    - type: nauc_mrr_at_3_max
      value: 67.05300993427998
    - type: nauc_mrr_at_3_std
      value: -9.827915885680811
    - type: nauc_mrr_at_5_diff1
      value: 73.11055686484109
    - type: nauc_mrr_at_5_max
      value: 67.26299851089122
    - type: nauc_mrr_at_5_std
      value: -9.445190276650903
    - type: nauc_ndcg_at_1000_diff1
      value: 72.58833638407177
    - type: nauc_ndcg_at_1000_max
      value: 68.10447506371374
    - type: nauc_ndcg_at_1000_std
      value: -6.910306241546282
    - type: nauc_ndcg_at_100_diff1
      value: 72.24524849631476
    - type: nauc_ndcg_at_100_max
      value: 68.30659210081238
    - type: nauc_ndcg_at_100_std
      value: -6.04305364268931
    - type: nauc_ndcg_at_10_diff1
      value: 71.87363502582961
    - type: nauc_ndcg_at_10_max
      value: 68.5010009653693
    - type: nauc_ndcg_at_10_std
      value: -7.021281296450588
    - type: nauc_ndcg_at_1_diff1
      value: 76.17529975949547
    - type: nauc_ndcg_at_1_max
      value: 65.02401127001608
    - type: nauc_ndcg_at_1_std
      value: -10.817814457633952
    - type: nauc_ndcg_at_20_diff1
      value: 72.21241010439327
    - type: nauc_ndcg_at_20_max
      value: 68.71743274030551
    - type: nauc_ndcg_at_20_std
      value: -6.186629577195946
    - type: nauc_ndcg_at_3_diff1
      value: 72.08204674794459
    - type: nauc_ndcg_at_3_max
      value: 67.5958365046156
    - type: nauc_ndcg_at_3_std
      value: -9.576418336610345
    - type: nauc_ndcg_at_5_diff1
      value: 71.93179095844508
    - type: nauc_ndcg_at_5_max
      value: 68.01914639754217
    - type: nauc_ndcg_at_5_std
      value: -8.833768332910777
    - type: nauc_precision_at_1000_diff1
      value: 63.0051360227489
    - type: nauc_precision_at_1000_max
      value: 79.93532442313229
    - type: nauc_precision_at_1000_std
      value: 52.869517607133254
    - type: nauc_precision_at_100_diff1
      value: 62.43301501857154
    - type: nauc_precision_at_100_max
      value: 75.57280416668183
    - type: nauc_precision_at_100_std
      value: 26.758300486132747
    - type: nauc_precision_at_10_diff1
      value: 66.29806375971134
    - type: nauc_precision_at_10_max
      value: 73.40301413754797
    - type: nauc_precision_at_10_std
      value: 1.9858547295235462
    - type: nauc_precision_at_1_diff1
      value: 76.17529975949547
    - type: nauc_precision_at_1_max
      value: 65.02401127001608
    - type: nauc_precision_at_1_std
      value: -10.817814457633952
    - type: nauc_precision_at_20_diff1
      value: 67.05111836051105
    - type: nauc_precision_at_20_max
      value: 76.09783190824155
    - type: nauc_precision_at_20_std
      value: 9.906010659515564
    - type: nauc_precision_at_3_diff1
      value: 68.44186679250453
    - type: nauc_precision_at_3_max
      value: 69.30301351119388
    - type: nauc_precision_at_3_std
      value: -8.566522518882348
    - type: nauc_precision_at_5_diff1
      value: 67.51737199297388
    - type: nauc_precision_at_5_max
      value: 70.75887601590472
    - type: nauc_precision_at_5_std
      value: -6.278983102710238
    - type: nauc_recall_at_1000_diff1
      value: 65.12360093170948
    - type: nauc_recall_at_1000_max
      value: 82.60209843191132
    - type: nauc_recall_at_1000_std
      value: 51.740179583368636
    - type: nauc_recall_at_100_diff1
      value: 62.82007697326819
    - type: nauc_recall_at_100_max
      value: 76.04844844677562
    - type: nauc_recall_at_100_std
      value: 26.4678415019248
    - type: nauc_recall_at_10_diff1
      value: 66.28557566848767
    - type: nauc_recall_at_10_max
      value: 73.40302709828738
    - type: nauc_recall_at_10_std
      value: 1.9224272854613582
    - type: nauc_recall_at_1_diff1
      value: 76.18354072047988
    - type: nauc_recall_at_1_max
      value: 65.03342186728786
    - type: nauc_recall_at_1_std
      value: 