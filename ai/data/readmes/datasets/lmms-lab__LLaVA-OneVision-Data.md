---
language:
- en
- zh
license: apache-2.0
pretty_name: llava-onevision-data
dataset_info:
- config_name: CLEVR-Math(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 791346970
    num_examples: 5280
  download_size: 441208499
  dataset_size: 791346970
- config_name: Evol-Instruct-GPT4-Turbo
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 340249088
    num_examples: 142985
  download_size: 161543154
  dataset_size: 340249088
- config_name: FigureQA(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 463326576.625
    num_examples: 17587
  download_size: 258197193
  dataset_size: 463326576.625
- config_name: GEOS(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1503641
    num_examples: 498
  download_size: 684471
  dataset_size: 1503641
- config_name: GeoQA+(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 53579705.75
    num_examples: 17162
  download_size: 33480538
  dataset_size: 53579705.75
- config_name: Geometry3K(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 218085473.5
    num_examples: 9724
  download_size: 125914780
  dataset_size: 218085473.5
- config_name: IconQA(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 208430568.375
    num_examples: 22589
  download_size: 117222488
  dataset_size: 208430568.375
- config_name: MapQA(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 384120915.875
    num_examples: 5225
  download_size: 215768443
  dataset_size: 384120915.875
- config_name: MathV360K_TQA
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2735376770.0
    num_examples: 10176
  download_size: 1532213164
  dataset_size: 2735376770.0
- config_name: MathV360K_VQA-AS
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 904123650.25
    num_examples: 5902
  download_size: 506909370
  dataset_size: 904123650.25
- config_name: MathV360K_VQA-RAD
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 114333011.375
    num_examples: 2125
  download_size: 63460571
  dataset_size: 114333011.375
- config_name: PMC-VQA(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 571444866.5
    num_examples: 35948
  download_size: 326541003
  dataset_size: 571444866.5
- config_name: Super-CLEVR(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2795082410.75
    num_examples: 8642
  download_size: 1580301917
  dataset_size: 2795082410.75
- config_name: TabMWP(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 307726997.5
    num_examples: 22452
  download_size: 173938487
  dataset_size: 307726997.5
- config_name: UniGeo(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 38296693.375
    num_examples: 11949
  download_size: 24170743
  dataset_size: 38296693.375
- config_name: VisualWebInstruct(filtered)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 36317112275.0
    num_examples: 263584
  download_size: 36239916454
  dataset_size: 36317112275.0
- config_name: VizWiz(MathV360K)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1170333936.5
    num_examples: 6604
  download_size: 660752297
  dataset_size: 1170333936.5
- config_name: ai2d(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 438572782.375
    num_examples: 2429
  download_size: 437348514
  dataset_size: 438572782.375
- config_name: ai2d(gpt4v)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 866076731
    num_examples: 4864
  download_size: 860306578
  dataset_size: 866076731
- config_name: ai2d(internvl)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1832787249.625
    num_examples: 12403
  download_size: 527493895
  dataset_size: 1832787249.625
- config_name: allava_instruct_laion4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 5981767621.25
    num_examples: 49990
  download_size: 5873046236
  dataset_size: 5981767621.25
- config_name: allava_instruct_vflan4v
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2680974558.25
    num_examples: 19990
  download_size: 2670088751
  dataset_size: 2680974558.25
- config_name: aokvqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 6896420844.25
    num_examples: 16534
  download_size: 6894236970
  dataset_size: 6896420844.25
- config_name: chart2text(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1145458729.5
    num_examples: 26956
  download_size: 1123681047
  dataset_size: 1145458729.5
- config_name: chartqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 815335215.5
    num_examples: 18260
  download_size: 803084541
  dataset_size: 815335215.5
- config_name: chrome_writting
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 44422597.875
    num_examples: 8825
  download_size: 39611257
  dataset_size: 44422597.875
- config_name: clevr(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 10528974543.625
    num_examples: 69995
  download_size: 10460536445
  dataset_size: 10528974543.625
- config_name: diagram_image_to_text(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 18858266
    num_examples: 295
  download_size: 18659115
  dataset_size: 18858266
- config_name: dvqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4487270615.625
    num_examples: 199995
  download_size: 4277056467
  dataset_size: 4487270615.625
- config_name: figureqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2351194509.625
    num_examples: 99995
  download_size: 2222640639
  dataset_size: 2351194509.625
- config_name: geo170k(align)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 204236256.75
    num_examples: 60242
  download_size: 58185410
  dataset_size: 204236256.75
- config_name: geo170k(qa)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 266040519.125
    num_examples: 67823
  download_size: 160022430
  dataset_size: 266040519.125
- config_name: geo3k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 42634333.625
    num_examples: 2091
  download_size: 41097851
  dataset_size: 42634333.625
- config_name: geomverse(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2263893609.75
    num_examples: 9298
  download_size: 2211726352
  dataset_size: 2263893609.75
- config_name: hateful_memes(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3057252325.125
    num_examples: 8495
  download_size: 3055839880
  dataset_size: 3057252325.125
- config_name: hitab(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 161706881.125
    num_examples: 2495
  download_size: 157871287
  dataset_size: 161706881.125
- config_name: hme100k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 273229915.5
    num_examples: 74492
  download_size: 241005430
  dataset_size: 273229915.5
- config_name: iam(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1131633206.75
    num_examples: 5658
  download_size: 1128371221
  dataset_size: 1131633206.75
- config_name: iconqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 331284932.25
    num_examples: 27302
  download_size: 327005220
  dataset_size: 331284932.25
- config_name: iiit5k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 21821437.25
    num_examples: 1990
  download_size: 21623116
  dataset_size: 21821437.25
- config_name: image_textualization(filtered)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 5218283253.375
    num_examples: 99573
  download_size: 5164176816
  dataset_size: 5218283253.375
- config_name: infographic(gpt4v)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 713657496.25
    num_examples: 1982
  download_size: 656276080
  dataset_size: 713657496.25
- config_name: infographic_vqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1528953078.75
    num_examples: 4394
  download_size: 1419340319
  dataset_size: 1528953078.75
- config_name: infographic_vqa_llava_format
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1765315696.875
    num_examples: 2113
  download_size: 1764548536
  dataset_size: 1765315696.875
- config_name: intergps(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 24973395.625
    num_examples: 1275
  download_size: 24736545
  dataset_size: 24973395.625
- config_name: k12_printing
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1205153118.5
    num_examples: 256636
  download_size: 1108572712
  dataset_size: 1205153118.5
- config_name: llava_wild_4v_12k_filtered
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 502505489.5
    num_examples: 15124
  download_size: 492970980
  dataset_size: 502505489.5
- config_name: llava_wild_4v_39k_filtered
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1239693377.75
    num_examples: 39362
  download_size: 1220949808
  dataset_size: 1239693377.75
- config_name: llavar_gpt4_20k
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 633833350.25
    num_examples: 19790
  download_size: 625365542
  dataset_size: 633833350.25
- config_name: lrv_chart
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 99338686
    num_examples: 1776
  download_size: 97979446
  dataset_size: 99338686
- config_name: lrv_normal(filtered)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 422589381.75
    num_examples: 10490
  download_size: 406958773
  dataset_size: 422589381.75
- config_name: magpie_pro(l3_80b_mt)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1657129141
    num_examples: 299988
  download_size: 885893066
  dataset_size: 1657129141
- config_name: magpie_pro(l3_80b_st)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1033666690
    num_examples: 299990
  download_size: 562771564
  dataset_size: 1033666690
- config_name: magpie_pro(qwen2_72b_st)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 703489344
    num_examples: 299982
  download_size: 361433408
  dataset_size: 703489344
- config_name: mapqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 3355751195.5
    num_examples: 37412
  download_size: 3305639218
  dataset_size: 3355751195.5
- config_name: mathqa
  features:
  - name: id
    dtype: string
  - name: image
    dtype: 'null'
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 18318538
    num_examples: 29827
  download_size: 7857130
  dataset_size: 18318538
- config_name: mavis_math_metagen
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2304025372.5
    num_examples: 87348
  download_size: 322776224
  dataset_size: 2304025372.5
- config_name: mavis_math_rule_geo
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14313211512.25
    num_examples: 99990
  download_size: 5841283073
  dataset_size: 14313211512.25
- config_name: multihiertt(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 300319803.25
    num_examples: 7614
  download_size: 295638314
  dataset_size: 300319803.25
- config_name: orand_car_a
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 23602442.125
    num_examples: 1999
  download_size: 23333412
  dataset_size: 23602442.125
- config_name: raven(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 1706160514.625
    num_examples: 41995
  download_size: 1693150088
  dataset_size: 1706160514.625
- config_name: rendered_text(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 11082594894.625
    num_examples: 9995
  download_size: 11081962044
  dataset_size: 11082594894.625
- config_name: robut_sqa(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 685580779.375
    num_examples: 8509
  download_size: 678666263
  dataset_size: 685580779.375
- config_name: robut_wikisql(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 6200499653
    num_examples: 74984
  download_size: 6168399217
  dataset_size: 6200499653
- config_name: robut_wtq(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4091776188.875
    num_examples: 38241
  download_size: 4062777449
  dataset_size: 4091776188.875
- config_name: scienceqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 286843125.625
    num_examples: 4971
  download_size: 282896809
  dataset_size: 286843125.625
- config_name: scienceqa(nona_context)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2111029055
    num_examples: 19208
  download_size: 2053942726
  dataset_size: 2111029055
- config_name: screen2words(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 7977502095.375
    num_examples: 15725
  download_size: 7962327904
  dataset_size: 7977502095.375
- config_name: sharegpt4o
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 6968025789.5
    num_examples: 57284
  download_size: 6772195470
  dataset_size: 6968025789.5
- config_name: sharegpt4v(coco)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2620153362.875
    num_examples: 50017
  download_size: 2595583499
  dataset_size: 2620153362.875
- config_name: sharegpt4v(knowledge)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 372100773.5
    num_examples: 1988
  download_size: 369799318
  dataset_size: 372100773.5
- config_name: sharegpt4v(llava)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 781795487.25
    num_examples: 29990
  download_size: 400344187
  dataset_size: 781795487.25
- config_name: sharegpt4v(sam)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4437405218.25
    num_examples: 8990
  download_size: 4428597081
  dataset_size: 4437405218.25
- config_name: sroie
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 117810195
    num_examples: 33616
  download_size: 103647636
  dataset_size: 117810195
- config_name: st_vqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 5771194098.75
    num_examples: 17242
  download_size: 5768888141
  dataset_size: 5771194098.75
- config_name: tabmwp(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 311192518.375
    num_examples: 22717
  download_size: 306092255
  dataset_size: 311192518.375
- config_name: tallyqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 35998988065.625
    num_examples: 98675
  download_size: 35982430394
  dataset_size: 35998988065.625
- config_name: textcaps
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2222268476.25
    num_examples: 21942
  download_size: 2217838132
  dataset_size: 2222268476.25
- config_name: textocr(gpt4v)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2581655353
    num_examples: 25104
  download_size: 2574418106
  dataset_size: 2581655353
- config_name: tqa(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 331203026.25
    num_examples: 27302
  download_size: 326999466
  dataset_size: 331203026.25
- config_name: ureader_cap
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 9269857109.75
    num_examples: 91434
  download_size: 2292099971
  dataset_size: 9269857109.75
- config_name: ureader_ie
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 11871457209.75
    num_examples: 17322
  download_size: 1999083115
  dataset_size: 11871457209.75
- config_name: vision_flan(filtered)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 24847242604.5
    num_examples: 186060
  download_size: 24750561877
  dataset_size: 24847242604.5
- config_name: vistext(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 550187184.5
    num_examples: 9964
  download_size: 452795103
  dataset_size: 550187184.5
- config_name: visual7w(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 4451436523.875
    num_examples: 14361
  download_size: 4441971985
  dataset_size: 4451436523.875
- config_name: visualmrc(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 2938154124.25
    num_examples: 3022
  download_size: 2909296079
  dataset_size: 2938154124.25
- config_name: vqarad(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 95533417
    num_examples: 308
  download_size: 95410398
  dataset_size: 95533417
- config_name: vsr(cauldron,llava_format)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 891981646
    num_examples: 2152
  download_size: 891572866
  dataset_size: 891981646
- config_name: websight(cauldron)
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 11209715828.625
    num_examples: 9995
  download_size: 11144460985
  dataset_size: 11209715828.625
configs:
- config_name: CLEVR-Math(MathV360K)
  data_files:
  - split: train
    path: CLEVR-Math(MathV360K)/train-*
- config_name: Evol-Instruct-GPT4-Turbo
  data_files:
  - split: train
    path: Evol-Instruct-GPT4-Turbo/train-*
- config_name: FigureQA(MathV360K)
  data_files:
  - split: train
    path: FigureQA(MathV360K)/train-*
- config_name: GEOS(MathV360K)
  data_files:
  - split: train
    path: GEOS(MathV360K)/train-*
- config_name: GeoQA+(MathV360K)
  data_files:
  - split: train
    path: GeoQA+(MathV360K)/train-*
- config_name: Geometry3K(MathV360K)
  data_files:
  - split: train
    path: Geometry3K(MathV360K)/train-*
- config_name: IconQA(MathV360K)
  data_files:
  - split: train
    path: IconQA(MathV360K)/train-*
- config_name: MapQA(MathV360K)
  data_files:
  - split: train
    path: MapQA(MathV360K)/train-*
- config_name: MathV360K_TQA
  data_files:
  - split: train
    path: MathV360K_TQA/train-*
- config_name: MathV360K_VQA-AS
  data_files:
  - split: train
    path: MathV360K_VQA-AS/train-*
- config_name: MathV360K_VQA-RAD
  data_files:
  - split: train
    path: MathV360K_VQA-RAD/train-*
- config_name: PMC-VQA(MathV360K)
  data_files:
  - split: train
    path: PMC-VQA(MathV360K)/train-*
- config_name: Super-CLEVR(MathV360K)
  data_files:
  - split: train
    path: Super-CLEVR(MathV360K)/train-*
- config_name: TabMWP(MathV360K)
  data_files:
  - split: train
    path: TabMWP(MathV360K)/train-*
- config_name: UniGeo(MathV360K)
  data_files:
  - split: train
    path: UniGeo(MathV360K)/train-*
- config_name: VisualWebInstruct(filtered)
  data_files:
  - split: train
    path: VisualWebInstruct(filtered)/train-*
- config_name: VizWiz(MathV360K)
  data_files:
  - split: train
    path: VizWiz(MathV360K)/train-*
- config_name: ai2d(cauldron,llava_format)
  data_files:
  - split: train
    path: ai2d(cauldron,llava_format)/train-*
- config_name: ai2d(gpt4v)
  data_files:
  - split: train
    path: ai2d(gpt4v)/train-*
- config_name: ai2d(internvl)
  data_files:
  - split: train
    path: ai2d(internvl)/train-*
- config_name: allava_instruct_laion4v
  data_files:
  - split: train
    path: allava_instruct_laion4v/train-*
- config_name: allava_instruct_vflan4v
  data_files:
  - split: train
    path: allava_instruct_vflan4v/train-*
- config_name: aokvqa(cauldron,llava_format)
  data_files:
  - split: train
    path: aokvqa(cauldron,llava_format)/train-*
- config_name: chart2text(cauldron)
  data_files:
  - split: train
    path: chart2text(cauldron)/train-*
- config_name: chartqa(cauldron,llava_format)
  data_files:
  - split: train
    path: chartqa(cauldron,llava_format)/train-*
- config_name: chrome_writting
  data_files:
  - split: train
    path: chrome_writting/train-*
- config_name: clevr(cauldron,llava_format)
  data_files:
  - split: train
    path: clevr(cauldron,llava_format)/train-*
- config_name: diagram_image_to_text(cauldron)
  data_files:
  - split: train
    path: diagram_image_to_text(cauldron)/train-*
- config_name: dvqa(cauldron,llava_format)
  data_files:
  - split: train
    path: dvqa(cauldron,llava_format)/train-*
- config_name: figureqa(cauldron,llava_format)
  data_files:
  - split: train
    path: figureqa(cauldron,llava_format)/train-*
- config_name: geo170k(align)
  data_files:
  - split: train
    path: geo170k(align)/train-*
- config_name: geo170k(qa)
  data_files:
  - split: train
    path: geo170k(qa)/train-*
- config_name: geo3k
  data_files:
  - split: train
    path: geo3k/train-*
- config_name: geomverse(cauldron)
  data_files:
  - split: train
    path: geomverse(cauldron)/train-*
- config_name: hateful_memes(cauldron,llava_format)
  data_files:
  - split: train
    path: hateful_memes(cauldron,llava_format)/train-*
- config_name: hitab(cauldron,llava_format)
  data_files:
  - split: train
    path: hitab(cauldron,llava_format)/train-*
- config_name: hme100k
  data_files:
  - split: train
    path: hme100k/train-*
- config_name: iam(cauldron)
  data_files:
  - split: train
    path: iam(cauldron)/train-*
- config_name: iconqa(cauldron,llava_format)
  data_files:
  - split: train
    path: iconqa(cauldron,llava_format)/train-*
- config_name: iiit5k
  data_files:
  - split: train
    path: iiit5k/train-*
- config_name: image_textualization(filtered)
  data_files:
  - split: train
    path: image_textualization(filtered)/train-*
- config_name: infographic(gpt4v)
  data_files:
  - split: train
    path: infographic(gpt4v)/train-*
- config_name: infographic_vqa
  data_files:
  - split: train
    path: infographic_vqa/train-*
- config_name: infographic_vqa_llava_format
  data_files:
  - split: train
    path: infographic_vqa_llava_format/train-*
- config_name: intergps(cauldron,llava_format)
  data_files:
  - split: train
    path: intergps(cauldron,llava_format)/train-*
- config_name: k12_printing
  data_files:
  - split: train
    path: k12_printing/train-*
- config_name: llava_wild_4v_12k_filtered
  data_files:
  - split: train
    path: llava_wild_4v_12k_filtered/train-*
- config_name: llava_wild_4v_39k_filtered
  data_files:
  - split: train
    path: llava_wild_4v_39k_filtered/train-*
- config_name: llavar_gpt4_20k
  data_files:
  - split: train
    path: llavar_gpt4_20k/train-*
- config_name: lrv_chart
  data_files:
  - split: train
    path: lrv_chart/train-*
- config_name: lrv_normal(filtered)
  data_files:
  - split: train
    path: lrv_normal(filtered)/train-*
- config_name: magpie_pro(l3_80b_mt)
  data_files:
  - split: train
    path: magpie_pro(l3_80b_mt)/train-*
- config_name: magpie_pro(l3_80b_st)
  data_files:
  - split: train
    path: magpie_pro(l3_80b_st)/train-*
- config_name: magpie_pro(qwen2_72b_st)
  data_files:
  - split: train
    path: magpie_pro(qwen2_72b_st)/train-*
- config_name: mapqa(cauldron,llava_format)
  data_files:
  - split: train
    path: mapqa(cauldron,llava_format)/train-*
- config_name: mathqa
  data_files:
  - split: train
    path: mathqa/train-*
- config_name: mavis_math_metagen
  data_files:
  - split: train
    path: mavis_math_metagen/train-*
- config_name: mavis_math_rule_geo
  data_files:
  - split: train
    path: mavis_math_rule_geo/train-*
- config_name: multihiertt(cauldron)
  data_files:
  - split: train
    path: multihiertt(cauldron)/train-*
- config_name: orand_car_a
  data_files:
  - split: train
    path: orand_car_a/train-*
- config_name: raven(cauldron)
  data_files:
  - split: train
    path: raven(cauldron)/train-*
- config_name: rendered_text(cauldron)
  data_files:
  - split: train
    path: rendered_text(cauldron)/train-*
- config_name: robut_sqa(cauldron)
  data_files:
  - split: train
    path: robut_sqa(cauldron)/train-*
- config_name: robut_wikisql(cauldron)
  data_files:
  - split: train
    path: robut_wikisql(cauldron)/train-*
- config_name: robut_wtq(cauldron,llava_format)
  data_files:
  - split: train
    path: robut_wtq(cauldron,llava_format)/train-*
- config_name: scienceqa(cauldron,llava_format)
  data_files:
  - split: train
    path: scienceqa(cauldron,llava_format)/train-*
- config_name: scienceqa(nona_context)
  data_files:
  - split: train
    path: scienceqa(nona_context)/train-*
- config_name: screen2words(cauldron)
  data_files:
  - split: train
    path: screen2words(cauldron)/train-*
- config_name: sharegpt4o
  data_files:
  - split: train
    path: sharegpt4o/train-*
- config_name: sharegpt4v(coco)
  data_files:
  - split: train
    path: sharegpt4v(coco)/train-*
- config_name: sharegpt4v(knowledge)
  data_files:
  - split: train
    path: sharegpt4v(knowledge)/train-*
- config_name: sharegpt4v(llava)
  data_files:
  - split: train
    path: sharegpt4v(llava)/train-*
- config_name: sharegpt4v(sam)
  data_files:
  - split: train
    path: sharegpt4v(sam)/train-*
- config_name: sroie
  data_files:
  - split: train
    path: sroie/train-*
- config_name: st_vqa(cauldron,llava_format)
  data_files:
  - split: train
    path: st_vqa(cauldron,llava_format)/train-*
- config_name: tabmwp(cauldron)
  data_files:
  - split: train
    path: tabmwp(cauldron)/train-*
- config_name: tallyqa(cauldron,llava_format)
  data_files:
  - split: train
    path: tallyqa(cauldron,llava_format)/train-*
- config_name: textcaps
  data_files:
  - split: train
    path: textcaps/train-*
- config_name: textocr(gpt4v)
  data_files:
  - split: train
    path: textocr(gpt4v)/train-*
- config_name: tqa(cauldron,llava_format)
  data_files:
  - split: train
    path: tqa(cauldron,llava_format)/train-*
- config_name: ureader_cap
  data_files:
  - split: train
    path: ureader_cap/train-*
- config_name: ureader_ie
  data_files:
  - split: train
    path: ureader_ie/train-*
- config_name: vision_flan(filtered)
  data_files:
  - split: train
    path: vision_flan(filtered)/train-*
- config_name: vistext(cauldron)
  data_files:
  - split: train
    path: vistext(cauldron)/train-*
- config_name: visual7w(cauldron,llava_format)
  data_files:
  - split: train
    path: visual7w(cauldron,llava_format)/train-*
- config_name: visualmrc(cauldron)
  data_files:
  - split: train
    path: visualmrc(cauldron)/train-*
- config_name: vqarad(cauldron,llava_format)
  data_files:
  - split: train
    path: vqarad(cauldron,llava_format)/train-*
- config_name: vsr(cauldron,llava_format)
  data_files:
  - split: train
    path: vsr(cauldron,llava_format)/train-*
- config_name: websight(cauldron)
  data_files:
  - split: train
    path: websight(cauldron)/train-*
---

# Dataset Card for LLaVA-OneVision

**[2024-09-01]: Uploaded VisualWebInstruct(filtered), it's used in OneVision Stage**
> almost all subsets are uploaded with HF's required format and you can use the recommended interface to download them and follow our code below to convert them. 

> the subset of `ureader_kg` and `ureader_qa` are uploaded with the processed jsons and tar.gz of image folders.
> You may directly download them from the following url.
> https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data/tree/main/ureader_kg

In this dataset, we include the data splits used in the both final image stage and one-vision stage. For more details, please check our [paper](arxiv.org/abs/2408.03326) and our [training doc](https://github.com/LLaVA-VL/LLaVA-NeXT/tree/main/scripts/train#about-the-llava-onevision-data).

## Dataset Description

- **Curated by:** Bo Li, Kaichen Zhang, Hao Zhang, Yuanhan Zhang, Renrui Zhang, Feng Li, Dong Guo
- **Language(s) (NLP):** English, Chinese
- **License:** Apache License 2.0

## Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Dataset Collection:** We include a few subsets from existing dataset collection [Cambrian](https://huggingface.co/datasets/nyu-visionx/Cambrian-10M), [Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron), [UReader](https://arxiv.org/abs/2310.05126). Since we only used a few subsets from these datasets, and applied the cleaning and re-annotation process, we uploaded our processed version of these datasets into our own repository and thank the authors for providing the original datasets.
- **Other Datasets:** For rest single source dataset, such as AI2D, OKVQA, we cite and link the original sources in our paper.

## Uses

This dataset is used for the training of the LLaVA-OneVision model. We only allow the use of this dataset for academic research and education purpose. For OpenAI GPT-4 generated data, we recommend the users to check the [OpenAI Usage Policy](https://openai.com/policies/usage-policies/).

## Dataset Structure

We expalin the data composition for mid-stage and final-stage at our repo in [**training doc**](https://github.com/LLaVA-VL/LLaVA-NeXT/tree/main/scripts/train#about-the-llava-onevision-data).

### Statistics

We provide the statistics of the dataset in the following figures, and refer the audience to check our paper.

![](https://i.postimg.cc/2y989XZJ/WX20240802-145215-2x.png)

![](https://i.postimg.cc/MZ9TGXFD/WX20240802-145226-2x.png)

### Code Guidance

To help audience to better understand our dataest, we upload them into Hugging Face Dataset compatible format. During LLaVA-OneVision training, we use the `json` and `image/video` folder to store the data.

> the subset of `ureader_kg` and `ureader_qa` are uploaded with the processed jsons and tar.gz of image folders. You may directly download them from the following url.
> https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data/tree/main/ureader_kg

Here we provide the code guidance to convert the dataset into the format of LLaVA-OneVision, and conduct the training of the LLaVA-OneVision model with converted dataset.

```python
import os
from datasets import load_dataset
from tqdm import tqdm
import json

data = load_dataset("lmms-lab/LLaVA-OneVision-Data", split="train")

image_folder = "<your_image_folder>"

converted_data = []

for da in tqdm(data):
    json_data = {}
    json_data["id"] = da["id"]
    if da["image"] is not None:
        json_data["image"] = f"{da['id']}.jpg"
        da["image"].save(os.path.join(image_folder, json_data["image"]))
    json_data["conversations"] = da["conversations"]
    converted_data.append(json_data)


with open("<your_json_file>.json", "w") as f:
    json.dump(converted_data, f, indent=4, ensure_ascii=False)


```

## Citation

**BibTeX:**

[More Information Needed]

## Glossary

The dataset collection process is conducted by all of the authors, we thank the Feng Li and Renrui Zhang for providing [LLaVA-M4-Instruct Data](https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data) and Yuanhan for providing the [Video datasets](https://huggingface.co/datasets/lmms-lab/LLaVA-Video-178K).

After the dataset collection, the cleaning and re-annotation process, including final mixture of the dataset, is conducted by Bo Li and with the great help of Kaichen Zhang.

## Dataset Card Authors

The dataset is curated by the following authors:

Bo Li, Kaichen Zhang, Hao Zhang, Yuanhan Zhang, Renrui Zhang, Feng Li

## Dataset Card Contact

[Bo Li](https://brianboli.com/): drluodian@gmail.com

[Kaichen Zhang](https://www.linkedin.com/in/kaichen-zhang-014b17219/?originalSubdomain=sg)