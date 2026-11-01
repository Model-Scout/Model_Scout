---
dataset_info:
- config_name: CoSyn_400k_chart
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 25619852113.664
    num_examples: 116814
  download_size: 25239736178
  dataset_size: 25619852113.664
- config_name: CoSyn_400k_chemical
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 284197936.992
    num_examples: 8942
  download_size: 273097193
  dataset_size: 284197936.992
- config_name: CoSyn_400k_circuit
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 395788840.72
    num_examples: 10470
  download_size: 381928378
  dataset_size: 395788840.72
- config_name: CoSyn_400k_diagram
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 7305286810.288
    num_examples: 34963
  download_size: 7234372451
  dataset_size: 7305286810.288
- config_name: CoSyn_400k_document
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 24180793229.832
    num_examples: 71282
  download_size: 24015209877
  dataset_size: 24180793229.832
- config_name: CoSyn_400k_graphic
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 335694057.168
    num_examples: 26968
  download_size: 313408282
  dataset_size: 335694057.168
- config_name: CoSyn_400k_math
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6107895469.064
    num_examples: 66714
  download_size: 6057279470
  dataset_size: 6107895469.064
- config_name: CoSyn_400k_music
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 405064954.03
    num_examples: 11969
  download_size: 377684174
  dataset_size: 405064954.03
- config_name: CoSyn_400k_nutrition
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1508994014.353
    num_examples: 6931
  download_size: 1485416825
  dataset_size: 1508994014.353
- config_name: CoSyn_400k_table
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 7684052957.968
    num_examples: 46518
  download_size: 7560488723
  dataset_size: 7684052957.968
- config_name: DoclingMatix
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 960982374796.28
    num_examples: 1270910
  download_size: 950807646187
  dataset_size: 960982374796.28
- config_name: LLaVA_Instruct_150K
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 76726976312.25
    num_examples: 157710
  download_size: 76639461610
  dataset_size: 76726976312.25
- config_name: SynthChartNet
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 17908210462
    num_examples: 500000
  download_size: 17714786653
  dataset_size: 17908210462
- config_name: SynthCodeNet
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 61998944812.125
    num_examples: 499983
  download_size: 61472605472
  dataset_size: 61998944812.125
- config_name: SynthFormulaNet
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2640399650.375
    num_examples: 499997
  download_size: 2534243196
  dataset_size: 2640399650.375
- config_name: Unichart
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 18177703609.375
    num_examples: 611925
  download_size: 16923868243
  dataset_size: 18177703609.375
- config_name: a_okvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 22759813096.74
    num_examples: 54602
  download_size: 22740515076
  dataset_size: 22759813096.74
- config_name: aguvis-stage-1
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 234712403450.264
    num_examples: 458957
  download_size: 227839724491
  dataset_size: 234712403450.264
- config_name: ai2d_merged
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 867183847.75
    num_examples: 4858
  download_size: 860582630
  dataset_size: 867183847.75
- config_name: alfworldgpt
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3890916009.875
    num_examples: 45073
  download_size: 2887255617
  dataset_size: 3890916009.875
- config_name: allava_laion
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 366924129181.264
    num_examples: 468664
  download_size: 366513300480
  dataset_size: 366924129181.264
- config_name: allava_vflan
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 92699946037.528
    num_examples: 177078
  download_size: 92524279162
  dataset_size: 92699946037.528
- config_name: aokvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 896746993.93
    num_examples: 16539
  download_size: 893471601
  dataset_size: 896746993.93
- config_name: art
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 5141087027.04
    num_examples: 5492
  download_size: 5140689948
  dataset_size: 5141087027.04
- config_name: arxivqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 81923895225
    num_examples: 100000
  download_size: 81811622698
  dataset_size: 81923895225
- config_name: bentham
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1450159090.168
    num_examples: 10843
  download_size: 1449119505
  dataset_size: 1450159090.168
- config_name: blockdiagramcomputerized
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 28792412
    num_examples: 502
  download_size: 28553870
  dataset_size: 28792412
- config_name: blockdiagramhandwritten
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 146651431.23
    num_examples: 1029
  download_size: 146191172
  dataset_size: 146651431.23
- config_name: cambrian(filtered)_processed
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 37993953612.448
    num_examples: 83123
  download_size: 37702528512
  dataset_size: 37993953612.448
- config_name: captcha
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1108385677.25
    num_examples: 113062
  download_size: 1093568723
  dataset_size: 1108385677.25
- config_name: chart2text
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1129182569.736
    num_examples: 26961
  download_size: 1108115443
  dataset_size: 1129182569.736
- config_name: chartqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 815177635.55
    num_examples: 18265
  download_size: 803910718
  dataset_size: 815177635.55
- config_name: chinesememe
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 14244173434.512
    num_examples: 54212
  download_size: 14222203753
  dataset_size: 14244173434.512
- config_name: chrome_writting
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 80739342.2
    num_examples: 8825
  download_size: 79343529
  dataset_size: 80739342.2
- config_name: clevr
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 10557164224
    num_examples: 70000
  download_size: 10465001066
  dataset_size: 10557164224
- config_name: clevr_math
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 9394753178
    num_examples: 70000
  download_size: 9344480504
  dataset_size: 9394753178
- config_name: clevr_math(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 708071620.6
    num_examples: 5280
  download_size: 697997425
  dataset_size: 708071620.6
- config_name: coco_colors
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 55374513710.125
    num_examples: 118287
  download_size: 55344845137
  dataset_size: 55374513710.125
- config_name: cocoqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2402176655.69
    num_examples: 46287
  download_size: 2394615512
  dataset_size: 2402176655.69
- config_name: cocotext
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 7930321103.875
    num_examples: 16169
  download_size: 7928989554
  dataset_size: 7930321103.875
- config_name: ctw
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 109319015738.75
    num_examples: 24290
  download_size: 109306604047
  dataset_size: 109319015738.75
- config_name: datik
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3646550812.875
    num_examples: 220537
  download_size: 3482030545
  dataset_size: 3646550812.875
- config_name: datikz
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 642401206.67
    num_examples: 47441
  download_size: 591381396
  dataset_size: 642401206.67
- config_name: densefusion_1m
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 146400262606.897
    num_examples: 1058751
  download_size: 144502318476
  dataset_size: 146400262606.897
- config_name: diagram_image_to_text
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 18704652
    num_examples: 300
  download_size: 18534456
  dataset_size: 18704652
- config_name: docvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 12018085125.664
    num_examples: 10189
  download_size: 12007345171
  dataset_size: 12018085125.664
- config_name: drivelm
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 37226102202.192
    num_examples: 4072
  download_size: 34029716036
  dataset_size: 37226102202.192
- config_name: dvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4581122677
    num_examples: 200000
  download_size: 4302544626
  dataset_size: 4581122677
- config_name: est_vqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 18902348521.25
    num_examples: 19358
  download_size: 18901853752
  dataset_size: 18902348521.25
- config_name: face_emotion
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 15127430
    num_examples: 797
  download_size: 14983116
  dataset_size: 15127430
- config_name: figureqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2346521984
    num_examples: 100000
  download_size: 2222862886
  dataset_size: 2346521984
- config_name: figureqa(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 419233306.69
    num_examples: 17587
  download_size: 414996519
  dataset_size: 419233306.69
- config_name: finqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 138086601.5
    num_examples: 5276
  download_size: 123625992
  dataset_size: 138086601.5
- config_name: funsd
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 35306471
    num_examples: 194
  download_size: 35104326
  dataset_size: 35306471
- config_name: geo170k(align)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 197478416.875
    num_examples: 35297
  download_size: 161890724
  dataset_size: 197478416.875
- config_name: geo170k(qa)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 87625237.87
    num_examples: 12101
  download_size: 52163819
  dataset_size: 87625237.87
- config_name: geo3k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 38756856.17
    num_examples: 2091
  download_size: 37400382
  dataset_size: 38756856.17
- config_name: geometry3k(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 197867040.88
    num_examples: 9724
  download_size: 184961625
  dataset_size: 197867040.88
- config_name: geomverse
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1183897660.128
    num_examples: 9303
  download_size: 1062185395
  dataset_size: 1183897660.128
- config_name: geoqa+(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 94213384.94
    num_examples: 17162
  download_size: 90953636
  dataset_size: 94213384.94
- config_name: geos(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3936551
    num_examples: 498
  download_size: 1613784
  dataset_size: 3936551
- config_name: google_landmarks
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 189460937100.184
    num_examples: 299993
  download_size: 189343235587
  dataset_size: 189460937100.184
- config_name: groundui
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6044682942.056
    num_examples: 13531
  download_size: 6027988163
  dataset_size: 6044682942.056
- config_name: handwriting_forms
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 168001610
    num_examples: 1400
  download_size: 164655119
  dataset_size: 168001610
- config_name: hateful_memes
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3059106937.5
    num_examples: 8500
  download_size: 3058138125
  dataset_size: 3059106937.5
- config_name: hitab
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 163934179
    num_examples: 2500
  download_size: 160422628
  dataset_size: 163934179
- config_name: hme100k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1547322234.04
    num_examples: 74492
  download_size: 1538339958
  dataset_size: 1547322234.04
- config_name: hw_squad
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 21637654637.632
    num_examples: 20457
  download_size: 21633468499
  dataset_size: 21637654637.632
- config_name: iam
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1138239910.217
    num_examples: 5663
  download_size: 1134974960
  dataset_size: 1138239910.217
- config_name: iconqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 330918682.09
    num_examples: 27307
  download_size: 326819099
  dataset_size: 330918682.09
- config_name: iconqa(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 209363820.43
    num_examples: 22589
  download_size: 204676537
  dataset_size: 209363820.43
- config_name: idk
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 5197458667.01
    num_examples: 11123
  download_size: 5194521196
  dataset_size: 5197458667.01
- config_name: iiit5k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 21788858.44
    num_examples: 1990
  download_size: 21513252
  dataset_size: 21788858.44
- config_name: image_textualization(filtered)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 39882386250.375
    num_examples: 99573
  download_size: 39829746385
  dataset_size: 39882386250.375
- config_name: imgur5k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 12591193342.434
    num_examples: 5934
  download_size: 12590763433
  dataset_size: 12591193342.434
- config_name: indoor_qa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 797864863.25
    num_examples: 3350
  download_size: 797431780
  dataset_size: 797864863.25
- config_name: infographic(gpt4v)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2014741558.032
    num_examples: 1982
  download_size: 2011159744
  dataset_size: 2014741558.032
- config_name: infographic_vqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4467479648.894
    num_examples: 4394
  download_size: 4465512444
  dataset_size: 4467479648.894
- config_name: infographic_vqa_llava_format
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1765450951.75
    num_examples: 2113
  download_size: 1764585485
  dataset_size: 1765450951.75
- config_name: intergps
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 25159455
    num_examples: 1280
  download_size: 24899065
  dataset_size: 25159455
- config_name: invoices_receipts
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1925658845.375
    num_examples: 3013
  download_size: 1923244863
  dataset_size: 1925658845.375
- config_name: k12_printing
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4587776492.32
    num_examples: 256636
  download_size: 4546453791
  dataset_size: 4587776492.32
- config_name: laion_gpt4v
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3021991360.375
    num_examples: 9301
  download_size: 3017230039
  dataset_size: 3021991360.375
- config_name: latex_handwritten
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 12665387206.408
    num_examples: 39583
  download_size: 12655091924
  dataset_size: 12665387206.408
- config_name: latexformulas
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 5604066568.5
    num_examples: 552340
  download_size: 5525103231
  dataset_size: 5604066568.5
- config_name: llavar_gpt4_20k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4235159184.04
    num_examples: 19790
  download_size: 4229077598
  dataset_size: 4235159184.04
- config_name: lnqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 266234680687.28
    num_examples: 302780
  download_size: 266088073857
  dataset_size: 266234680687.28
- config_name: localized_narratives
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 21346019807.448
    num_examples: 199998
  download_size: 21291848742
  dataset_size: 21346019807.448
- config_name: lrv_chart
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 86444276.008
    num_examples: 1776
  download_size: 85369432
  dataset_size: 86444276.008
- config_name: lrv_normal(filtered)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2985153010.43
    num_examples: 10489
  download_size: 2967270530
  dataset_size: 2985153010.43
- config_name: lvis_instruct4v
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 107372123408.125
    num_examples: 222711
  download_size: 107199700503
  dataset_size: 107372123408.125
- config_name: mapqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3371567797.875
    num_examples: 37417
  download_size: 3308958271
  dataset_size: 3371567797.875
- config_name: mapqa(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 351524458.75
    num_examples: 5225
  download_size: 345656246
  dataset_size: 351524458.75
- config_name: maptext
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1504185688
    num_examples: 200
  download_size: 1504165598
  dataset_size: 1504185688
- config_name: mathwriting-google
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 12299849132
    num_examples: 300000
  download_size: 12219456415
  dataset_size: 12299849132
- config_name: mavis_math_metagen
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3975734405.048
    num_examples: 87348
  download_size: 3266775104
  dataset_size: 3975734405.048
- config_name: mavis_math_rule_geo
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 20031463665.136
    num_examples: 99986
  download_size: 19769419782
  dataset_size: 20031463665.136
- config_name: memotion
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2530734349.206
    num_examples: 6991
  download_size: 2528737208
  dataset_size: 2530734349.206
- config_name: mimic_cgd
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 13184046225.25
    num_examples: 70939
  download_size: 13149862823
  dataset_size: 13184046225.25
- config_name: mmc_instruct
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 16504670029.128
    num_examples: 168178
  download_size: 16230725185
  dataset_size: 16504670029.128
- config_name: mmevol
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 25742246427.065
    num_examples: 160215
  download_size: 25480716864
  dataset_size: 25742246427.065
- config_name: mmra
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1289479228.248
    num_examples: 1024
  download_size: 1249496994
  dataset_size: 1289479228.248
- config_name: mmsoc_memotion
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2531497426.206
    num_examples: 6991
  download_size: 2529088456
  dataset_size: 2531497426.206
- config_name: multihiertt
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1378944031.237
    num_examples: 7619
  download_size: 1362595573
  dataset_size: 1378944031.237
- config_name: nlvr2
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 23552929006.152
    num_examples: 50426
  download_size: 23481437598
  dataset_size: 23552929006.152
- config_name: objects365_qa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 202609182505.89
    num_examples: 1665847
  download_size: 199554203410
  dataset_size: 202609182505.89
- config_name: ocrvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6148678275.896
    num_examples: 165746
  download_size: 6057032047
  dataset_size: 6148678275.896
- config_name: olmOCR-mix-0225-books
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6633513593.78
    num_examples: 15194
  download_size: 6618802397
  dataset_size: 6633513593.78
- config_name: olmOCR-mix-0225-documents
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 97945411922.46
    num_examples: 228858
  download_size: 97308921712
  dataset_size: 97945411922.46
- config_name: oodvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4694217369.688
    num_examples: 8488
  download_size: 4653237790
  dataset_size: 4694217369.688
- config_name: orand_car_a
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 23695905.13
    num_examples: 1999
  download_size: 23351148
  dataset_size: 23695905.13
- config_name: pathvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 18649772240
    num_examples: 32632
  download_size: 18155570098
  dataset_size: 18649772240
- config_name: pdfvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1663168578.91
    num_examples: 8593
  download_size: 1645451234
  dataset_size: 1663168578.91
- config_name: plotqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 8939469643.25
    num_examples: 157070
  download_size: 5345605223
  dataset_size: 8939469643.25
- config_name: pmc_vqa(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3445692373.648
    num_examples: 35948
  download_size: 3437305247
  dataset_size: 3445692373.648
- config_name: raven
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1734017137
    num_examples: 42000
  download_size: 1721095694
  dataset_size: 1734017137
- config_name: rendered_text
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 11087697572
    num_examples: 10000
  download_size: 11087197372
  dataset_size: 11087697572
- config_name: robut_sqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 691188383.864
    num_examples: 8514
  download_size: 684223334
  dataset_size: 691188383.864
- config_name: robut_wikisql
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6319659576.464
    num_examples: 74989
  download_size: 6292705239
  dataset_size: 6319659576.464
- config_name: robut_wtq
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4150727243.896
    num_examples: 38246
  download_size: 4125713020
  dataset_size: 4150727243.896
- config_name: scienceqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 287033977.12
    num_examples: 4976
  download_size: 283309644
  dataset_size: 287033977.12
- config_name: scienceqa(nona_context)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2014832143.96
    num_examples: 19208
  download_size: 1968554064
  dataset_size: 2014832143.96
- config_name: screen2words
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1693100006.1
    num_examples: 15730
  download_size: 1345772929
  dataset_size: 1693100006.1
- config_name: screenqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 44877746311.875
    num_examples: 80761
  download_size: 44817901938
  dataset_size: 44877746311.875
- config_name: sharegpt4o
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 39874535436.384
    num_examples: 57284
  download_size: 39791929512
  dataset_size: 39874535436.384
- config_name: sharegpt4v(coco)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 20028717347.875
    num_examples: 50017
  download_size: 20005211134
  dataset_size: 20028717347.875
- config_name: sharegpt4v(knowledge)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2405546343.928
    num_examples: 1988
  download_size: 2404816763
  dataset_size: 2405546343.928
- config_name: sharegpt4v(llava)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 5644424724.75
    num_examples: 29986
  download_size: 5627968195
  dataset_size: 5644424724.75
- config_name: sharegpt4v(sam)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 31591491436.24
    num_examples: 8990
  download_size: 31588799545
  dataset_size: 31591491436.24
- config_name: sketchyvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 462161568
    num_examples: 8000
  download_size: 454872096
  dataset_size: 462161568
- config_name: slidevqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4252726221.347
    num_examples: 1919
  download_size: 2508659044
  dataset_size: 4252726221.347
- config_name: spark
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1062710726.48
    num_examples: 3904
  download_size: 1061887418
  dataset_size: 1062710726.48
- config_name: spatialsense
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3539733377.8
    num_examples: 10440
  download_size: 3537019555
  dataset_size: 3539733377.8
- config_name: spot_the_diff
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1656404738.5
    num_examples: 8566
  download_size: 1590994273
  dataset_size: 1656404738.5
- config_name: sroie
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 382776987.92
    num_examples: 33616
  download_size: 377976339
  dataset_size: 382776987.92
- config_name: st_vqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 878506863.672
    num_examples: 17247
  download_size: 876025784
  dataset_size: 878506863.672
- config_name: sujet_finance
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4870775458.875
    num_examples: 9801
  download_size: 4859136094
  dataset_size: 4870775458.875
- config_name: super_clevr(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2494651975.75
    num_examples: 8642
  download_size: 2481704024
  dataset_size: 2494651975.75
- config_name: svrd
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4770520445.396
    num_examples: 4396
  download_size: 4294464627
  dataset_size: 4770520445.396
- config_name: synthdog
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 312184613844
    num_examples: 500000
  download_size: 312088721977
  dataset_size: 312184613844
- config_name: tabmwp
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 311512614.14
    num_examples: 22722
  download_size: 306381970
  dataset_size: 311512614.14
- config_name: tabmwp(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 308654364.24
    num_examples: 22452
  download_size: 304900175
  dataset_size: 308654364.24
- config_name: tal_ocr_eng
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4597914661.25
    num_examples: 256646
  download_size: 4570495461
  dataset_size: 4597914661.25
- config_name: tallyqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4683118092
    num_examples: 98680
  download_size: 4663708984
  dataset_size: 4683118092
- config_name: tat_dqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 56046237.351
    num_examples: 2207
  download_size: 51835448
  dataset_size: 56046237.351
- config_name: tat_qa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 74054155.13
    num_examples: 2199
  download_size: 70887428
  dataset_size: 74054155.13
- config_name: text_OpenMathInstruct-2
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1397157730
    num_examples: 1000000
  download_size: 716116310
  dataset_size: 1397157730
- config_name: text_code_feedback
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 395467554
    num_examples: 66383
  download_size: 177807405
  dataset_size: 395467554
- config_name: text_codefeedback_filtered_instruction
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 366717666
    num_examples: 156525
  download_size: 189995909
  dataset_size: 366717666
- config_name: text_infinitymath
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 36914765
    num_examples: 101380
  download_size: 19626819
  dataset_size: 36914765
- config_name: text_mathinstruct
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 199703065
    num_examples: 262039
  download_size: 111115007
  dataset_size: 199703065
- config_name: text_mathqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 309234514
    num_examples: 394996
  download_size: 161782592
  dataset_size: 309234514
- config_name: text_mathstepdpo10k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 5594152
    num_examples: 10795
  download_size: 3115607
  dataset_size: 5594152
- config_name: text_numinamath_cot
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1292196153
    num_examples: 859494
  download_size: 708138975
  dataset_size: 1292196153
- config_name: text_openhermes_2_5
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1573997409
    num_examples: 1001551
  download_size: 893716086
  dataset_size: 1573997409
- config_name: text_openorca
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 6918913888
    num_examples: 4233853
  download_size: 4333157269
  dataset_size: 6918913888
- config_name: text_orcamath
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 238325136
    num_examples: 200035
  download_size: 96194490
  dataset_size: 238325136
- config_name: text_pythoncode25k
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 26382364
    num_examples: 49626
  download_size: 14144270
  dataset_size: 26382364
- config_name: text_pythoncodealpaca
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 12659736
    num_examples: 18612
  download_size: 6520090
  dataset_size: 12659736
- config_name: text_ruozhiba
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 624832
    num_examples: 1496
  download_size: 425925
  dataset_size: 624832
- config_name: text_theoremqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 221207
    num_examples: 800
  download_size: 137531
  dataset_size: 221207
- config_name: text_wizardlm_evol
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 135800299
    num_examples: 69999
  download_size: 73655559
  dataset_size: 135800299
- config_name: textcaps
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 18032419585.056
    num_examples: 21906
  download_size: 18030277823
  dataset_size: 18032419585.056
- config_name: textocr(gpt4v)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 20681382782.56
    num_examples: 25060
  download_size: 20676591460
  dataset_size: 20681382782.56
- config_name: textvqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2145630068.41
    num_examples: 21943
  download_size: 2140127123
  dataset_size: 2145630068.41
- config_name: tqa
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 659074476.63
    num_examples: 2749
  download_size: 656833279
  dataset_size: 659074476.63
- config_name: unigeo(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 68744643.63
    num_examples: 11949
  download_size: 66357327
  dataset_size: 68744643.63
- config_name: ureader_cap
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 75068370896.84
    num_examples: 91215
  download_size: 75059667838
  dataset_size: 75068370896.84
- config_name: ureader_ie
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 9192939954.32
    num_examples: 17320
  download_size: 9130561778
  dataset_size: 9192939954.32
- config_name: ureader_kg_processed
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 19867189334.8
    num_examples: 37550
  download_size: 19845137580
  dataset_size: 19867189334.8
- config_name: ureader_qa_processed
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 150865741789.528
    num_examples: 252953
  download_size: 149919280977
  dataset_size: 150865741789.528
- config_name: vision_flan(filtered)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 82861363780.064
    num_examples: 175964
  download_size: 82808510061
  dataset_size: 82861363780.064
- config_name: vistext
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 551951787.944
    num_examples: 9969
  download_size: 544522262
  dataset_size: 551951787.944
- config_name: visual7w
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4452152281.25
    num_examples: 14366
  download_size: 4443416633
  dataset_size: 4452152281.25
- config_name: visualmrc
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 1765924752.032
    num_examples: 3027
  download_size: 1762499163
  dataset_size: 1765924752.032
- config_name: visualwebinstruct(filtered)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 36324448983.375
    num_examples: 263581
  download_size: 36238426746
  dataset_size: 36324448983.375
- config_name: vizwiz(mathv360k)
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 10145613386.2
    num_examples: 6604
  download_size: 9953393596
  dataset_size: 10145613386.2
- config_name: vqaonbd
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 7937425917.75
    num_examples: 39986
  download_size: 7749504823
  dataset_size: 7937425917.75
- config_name: vqarad
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 17413769
    num_examples: 313
  download_size: 16998366
  dataset_size: 17413769
- config_name: vqav2
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 4295913716.5
    num_examples: 82772
  download_size: 4262624701
  dataset_size: 4295913716.5
- config_name: vsr
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 108075930.59
    num_examples: 2157
  download_size: 107612332
  dataset_size: 108075930.59
- config_name: websight
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 8465472626
    num_examples: 10000
  download_size: 8422476950
  dataset_size: 8465472626
- config_name: wildvision
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 365457306
    num_examples: 333
  download_size: 253665007
  dataset_size: 365457306
- config_name: wordart
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 2837619342.804
    num_examples: 4804
  download_size: 2837305200
  dataset_size: 2837619342.804
- config_name: yesbut
  features:
  - name: images
    list: image
  - name: texts
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
  - name: source
    dtype: string
  - name: image_correspondence_ratings
    list: int64
  - name: image_correspondence_min
    dtype: int64
  - name: formatting_ratings
    list: int64
  - name: formatting_min
    dtype: int64
  - name: visual_dependency_ratings
    list: int64
  - name: visual_dependency_min
    dtype: int64
  - name: relevance_ratings
    list: int64
  - name: relevance_min
    dtype: int64
  splits:
  - name: train
    num_bytes: 3172970131.082
    num_examples: 4318
  download_size: 3171611057
  dataset_size: 3172970131.082
configs:
- config_name: CoSyn_400k_chart
  data_files:
  - split: train
    path: CoSyn_400k_chart/train-*
- config_name: CoSyn_400k_chemical
  data_files:
  - split: train
    path: CoSyn_400k_chemical/train-*
- config_name: CoSyn_400k_circuit
  data_files:
  - split: train
    path: CoSyn_400k_circuit/train-*
- config_name: CoSyn_400k_diagram
  data_files:
  - split: train
    path: CoSyn_400k_diagram/train-*
- config_name: CoSyn_400k_document
  data_files:
  - split: train
    path: CoSyn_400k_document/train-*
- config_name: CoSyn_400k_graphic
  data_files:
  - split: train
    path: CoSyn_400k_graphic/train-*
- config_name: CoSyn_400k_math
  data_files:
  - split: train
    path: CoSyn_400k_math/train-*
- config_name: CoSyn_400k_music
  data_files:
  - split: train
    path: CoSyn_400k_music/train-*
- config_name: CoSyn_400k_nutrition
  data_files:
  - split: train
    path: CoSyn_400k_nutrition/train-*
- config_name: CoSyn_400k_table
  data_files:
  - split: train
    path: CoSyn_400k_table/train-*
- config_name: DoclingMatix
  data_files:
  - split: train
    path: DoclingMatix/train-*
- config_name: LLaVA_Instruct_150K
  data_files:
  - split: train
    path: LLaVA_Instruct_150K/train-*
- config_name: SynthChartNet
  data_files:
  - split: train
    path: SynthChartNet/train-*
- config_name: SynthCodeNet
  data_files:
  - split: train
    path: SynthCodeNet/train-*
- config_name: SynthFormulaNet
  data_files:
  - split: train
    path: SynthFormulaNet/train-*
- config_name: Unichart
  data_files:
  - split: train
    path: Unichart/train-*
- config_name: a_okvqa
  data_files:
  - split: train
    path: a_okvqa/train-*
- config_name: aguvis-stage-1
  data_files:
  - split: train
    path: aguvis-stage-1/train-*
- config_name: ai2d_merged
  data_files:
  - split: train
    path: ai2d_merged/train-*
- config_name: alfworldgpt
  data_files:
  - split: train
    path: alfworldgpt/train-*
- config_name: allava_laion
  data_files:
  - split: train
    path: allava_laion/train-*
- config_name: allava_vflan
  data_files:
  - split: train
    path: allava_vflan/train-*
- config_name: aokvqa
  data_files:
  - split: train
    path: aokvqa/train-*
- config_name: art
  data_files:
  - split: train
    path: art/train-*
- config_name: arxivqa
  data_files:
  - split: train
    path: arxivqa/train-*
- config_name: bentham
  data_files:
  - split: train
    path: bentham/train-*
- config_name: blockdiagramcomputerized
  data_files:
  - split: train
    path: blockdiagramcomputerized/train-*
- config_name: blockdiagramhandwritten
  data_files:
  - split: train
    path: blockdiagramhandwritten/train-*
- config_name: cambrian(filtered)_processed
  data_files:
  - split: train
    path: cambrian(filtered)_processed/train-*
- config_name: captcha
  data_files:
  - split: train
    path: captcha/train-*
- config_name: chart2text
  data_files:
  - split: train
    path: chart2text/train-*
- config_name: chartqa
  data_files:
  - split: train
    path: chartqa/train-*
- config_name: chinesememe
  data_files:
  - split: train
    path: chinesememe/train-*
- config_name: chrome_writting
  data_files:
  - split: train
    path: chrome_writting/train-*
- config_name: clevr
  data_files:
  - split: train
    path: clevr/train-*
- config_name: clevr_math
  data_files:
  - split: train
    path: clevr_math/train-*
- config_name: clevr_math(mathv360k)
  data_files:
  - split: train
    path: clevr_math(mathv360k)/train-*
- config_name: coco_colors
  data_files:
  - split: train
    path: coco_colors/train-*
- config_name: cocoqa
  data_files:
  - split: train
    path: cocoqa/train-*
- config_name: cocotext
  data_files:
  - split: train
    path: cocotext/train-*
- config_name: ctw
  data_files:
  - split: train
    path: ctw/train-*
- config_name: datik
  data_files:
  - split: train
    path: datik/train-*
- config_name: datikz
  data_files:
  - split: train
    path: datikz/train-*
- config_name: densefusion_1m
  data_files:
  - split: train
    path: densefusion_1m/train-*
- config_name: diagram_image_to_text
  data_files:
  - split: train
    path: diagram_image_to_text/train-*
- config_name: docvqa
  data_files:
  - split: train
    path: docvqa/train-*
- config_name: drivelm
  data_files:
  - split: train
    path: drivelm/train-*
- config_name: dvqa
  data_files:
  - split: train
    path: dvqa/train-*
- config_name: est_vqa
  data_files:
  - split: train
    path: est_vqa/train-*
- config_name: face_emotion
  data_files:
  - split: train
    path: face_emotion/train-*
- config_name: figureqa
  data_files:
  - split: train
    path: figureqa/train-*
- config_name: figureqa(mathv360k)
  data_files:
  - split: train
    path: figureqa(mathv360k)/train-*
- config_name: finqa
  data_files:
  - split: train
    path: finqa/train-*
- config_name: funsd
  data_files:
  - split: train
    path: funsd/train-*
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
- config_name: geometry3k(mathv360k)
  data_files:
  - split: train
    path: geometry3k(mathv360k)/train-*
- config_name: geomverse
  data_files:
  - split: train
    path: geomverse/train-*
- config_name: geoqa+(mathv360k)
  data_files:
  - split: train
    path: geoqa+(mathv360k)/train-*
- config_name: geos(mathv360k)
  data_files:
  - split: train
    path: geos(mathv360k)/train-*
- config_name: google_landmarks
  data_files:
  - split: train
    path: google_landmarks/train-*
- config_name: groundui
  data_files:
  - split: train
    path: groundui/train-*
- config_name: handwriting_forms
  data_files:
  - split: train
    path: handwriting_forms/train-*
- config_name: hateful_memes
  data_files:
  - split: train
    path: hateful_memes/train-*
- config_name: hitab
  data_files:
  - split: train
    path: hitab/train-*
- config_name: hme100k
  data_files:
  - split: train
    path: hme100k/train-*
- config_name: hw_squad
  data_files:
  - split: train
    path: hw_squad/train-*
- config_name: iam
  data_files:
  - split: train
    path: iam/train-*
- config_name: iconqa
  data_files:
  - split: train
    path: iconqa/train-*
- config_name: iconqa(mathv360k)
  data_files:
  - split: train
    path: iconqa(mathv360k)/train-*
- config_name: idk
  data_files:
  - split: train
    path: idk/train-*
- config_name: iiit5k
  data_files:
  - split: train
    path: iiit5k/train-*
- config_name: image_textualization(filtered)
  data_files:
  - split: train
    path: image_textualization(filtered)/train-*
- config_name: imgur5k
  data_files:
  - split: train
    path: imgur5k/train-*
- config_name: indoor_qa
  data_files:
  - split: train
    path: indoor_qa/train-*
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
- config_name: intergps
  data_files:
  - split: train
    path: intergps/train-*
- config_name: invoices_receipts
  data_files:
  - split: train
    path: invoices_receipts/train-*
- config_name: k12_printing
  data_files:
  - split: train
    path: k12_printing/train-*
- config_name: laion_gpt4v
  data_files:
  - split: train
    path: laion_gpt4v/train-*
- config_name: latex_handwritten
  data_files:
  - split: train
    path: latex_handwritten/train-*
- config_name: latexformulas
  data_files:
  - split: train
    path: latexformulas/train-*
- config_name: llavar_gpt4_20k
  data_files:
  - split: train
    path: llavar_gpt4_20k/train-*
- config_name: lnqa
  data_files:
  - split: train
    path: lnqa/train-*
- config_name: localized_narratives
  data_files:
  - split: train
    path: localized_narratives/train-*
- config_name: lrv_chart
  data_files:
  - split: train
    path: lrv_chart/train-*
- config_name: lrv_normal(filtered)
  data_files:
  - split: train
    path: lrv_normal(filtered)/train-*
- config_name: lvis_instruct4v
  data_files:
  - split: train
    path: lvis_instruct4v/train-*
- config_name: mapqa
  data_files:
  - split: train
    path: mapqa/train-*
- config_name: mapqa(mathv360k)
  data_files:
  - split: train
    path: mapqa(mathv360k)/train-*
- config_name: maptext
  data_files:
  - split: train
    path: maptext/train-*
- config_name: mathwriting-google
  data_files:
  - split: train
    path: mathwriting-google/train-*
- config_name: mavis_math_metagen
  data_files:
  - split: train
    path: mavis_math_metagen/train-*
- config_name: mavis_math_rule_geo
  data_files:
  - split: train
    path: mavis_math_rule_geo/train-*
- config_name: memotion
  data_files:
  - split: train
    path: memotion/train-*
- config_name: mimic_cgd
  data_files:
  - split: train
    path: mimic_cgd/train-*
- config_name: mmc_instruct
  data_files:
  - split: train
    path: mmc_instruct/train-*
- config_name: mmevol
  data_files:
  - split: train
    path: mmevol/train-*
- config_name: mmra
  data_files:
  - split: train
    path: mmra/train-*
- config_name: mmsoc_memotion
  data_files:
  - split: train
    path: mmsoc_memotion/train-*
- config_name: multihiertt
  data_files:
  - split: train
    path: multihiertt/train-*
- config_name: nlvr2
  data_files:
  - split: train
    path: nlvr2/train-*
- config_name: objects365_qa
  data_files:
  - split: train
    path: objects365_qa/train-*
- config_name: ocrvqa
  data_files:
  - split: train
    path: ocrvqa/train-*
- config_name: olmOCR-mix-0225-books
  data_files:
  - split: train
    path: olmOCR-mix-0225-books/train-*
- config_name: olmOCR-mix-0225-documents
  data_files:
  - split: train
    path: olmOCR-mix-0225-documents/train-*
- config_name: oodvqa
  data_files:
  - split: train
    path: oodvqa/train-*
- config_name: orand_car_a
  data_files:
  - split: train
    path: orand_car_a/train-*
- config_name: pathvqa
  data_files:
  - split: train
    path: pathvqa/train-*
- config_name: pdfvqa
  data_files:
  - split: train
    path: pdfvqa/train-*
- config_name: plotqa
  data_files:
  - split: train
    path: plotqa/train-*
- config_name: pmc_vqa(mathv360k)
  data_files:
  - split: train
    path: pmc_vqa(mathv360k)/train-*
- config_name: raven
  data_files:
  - split: train
    path: raven/train-*
- config_name: rendered_text
  data_files:
  - split: train
    path: rendered_text/train-*
- config_name: robut_sqa
  data_files:
  - split: train
    path: robut_sqa/train-*
- config_name: robut_wikisql
  data_files:
  - split: train
    path: robut_wikisql/train-*
- config_name: robut_wtq
  data_files:
  - split: train
    path: robut_wtq/train-*
- config_name: scienceqa
  data_files:
  - split: train
    path: scienceqa/train-*
- config_name: scienceqa(nona_context)
  data_files:
  - split: train
    path: scienceqa(nona_context)/train-*
- config_name: screen2words
  data_files:
  - split: train
    path: screen2words/train-*
- config_name: screenqa
  data_files:
  - split: train
    path: screenqa/train-*
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
- config_name: sketchyvqa
  data_files:
  - split: train
    path: sketchyvqa/train-*
- config_name: slidevqa
  data_files:
  - split: train
    path: slidevqa/train-*
- config_name: spark
  data_files:
  - split: train
    path: spark/train-*
- config_name: spatialsense
  data_files:
  - split: train
    path: spatialsense/train-*
- config_name: spot_the_diff
  data_files:
  - split: train
    path: spot_the_diff/train-*
- config_name: sroie
  data_files:
  - split: train
    path: sroie/train-*
- config_name: st_vqa
  data_files:
  - split: train
    path: st_vqa/train-*
- config_name: sujet_finance
  data_files:
  - split: train
    path: sujet_finance/train-*
- config_name: super_clevr(mathv360k)
  data_files:
  - split: train
    path: super_clevr(mathv360k)/train-*
- config_name: svrd
  data_files:
  - split: train
    path: svrd/train-*
- config_name: synthdog
  data_files:
  - split: train
    path: synthdog/train-*
- config_name: tabmwp
  data_files:
  - split: train
    path: tabmwp/train-*
- config_name: tabmwp(mathv360k)
  data_files:
  - split: train
    path: tabmwp(mathv360k)/train-*
- config_name: tal_ocr_eng
  data_files:
  - split: train
    path: tal_ocr_eng/train-*
- config_name: tallyqa
  data_files:
  - split: train
    path: tallyqa/train-*
- config_name: tat_dqa
  data_files:
  - split: train
    path: tat_dqa/train-*
- config_name: tat_qa
  data_files:
  - split: train
    path: tat_qa/train-*
- config_name: text_OpenMathInstruct-2
  data_files:
  - split: train
    path: text_OpenMathInstruct-2/train-*
- config_name: text_code_feedback
  data_files:
  - split: train
    path: text_code_feedback/train-*
- config_name: text_codefeedback_filtered_instruction
  data_files:
  - split: train
    path: text_codefeedback_filtered_instruction/train-*
- config_name: text_infinitymath
  data_files:
  - split: train
    path: text_infinitymath/train-*
- config_name: text_mathinstruct
  data_files:
  - split: train
    path: text_mathinstruct/train-*
- config_name: text_mathqa
  data_files:
  - split: train
    path: text_mathqa/train-*
- config_name: text_mathstepdpo10k
  data_files:
  - split: train
    path: text_mathstepdpo10k/train-*
- config_name: text_numinamath_cot
  data_files:
  - split: train
    path: text_numinamath_cot/train-*
- config_name: text_openhermes_2_5
  data_files:
  - split: train
    path: text_openhermes_2_5/train-*
- config_name: text_openorca
  data_files:
  - split: train
    path: text_openorca/train-*
- config_name: text_orcamath
  data_files:
  - split: train
    path: text_orcamath/train-*
- config_name: text_pythoncode25k
  data_files:
  - split: train
    path: text_pythoncode25k/train-*
- config_name: text_pythoncodealpaca
  data_files:
  - split: train
    path: text_pythoncodealpaca/train-*
- config_name: text_ruozhiba
  data_files:
  - split: train
    path: text_ruozhiba/train-*
- config_name: text_theoremqa
  data_files:
  - split: train
    path: text_theoremqa/train-*
- config_name: text_wizardlm_evol
  data_files:
  - split: train
    path: text_wizardlm_evol/train-*
- config_name: textcaps
  data_files:
  - split: train
    path: textcaps/train-*
- config_name: textocr(gpt4v)
  data_files:
  - split: train
    path: textocr(gpt4v)/train-*
- config_name: textvqa
  data_files:
  - split: train
    path: textvqa/train-*
- config_name: tqa
  data_files:
  - split: train
    path: tqa/train-*
- config_name: unigeo(mathv360k)
  data_files:
  - split: train
    path: unigeo(mathv360k)/train-*
- config_name: ureader_cap
  data_files:
  - split: train
    path: ureader_cap/train-*
- config_name: ureader_ie
  data_files:
  - split: train
    path: ureader_ie/train-*
- config_name: ureader_kg_processed
  data_files:
  - split: train
    path: ureader_kg_processed/train-*
- config_name: ureader_qa_processed
  data_files:
  - split: train
    path: ureader_qa_processed/train-*
- config_name: vision_flan(filtered)
  data_files:
  - split: train
    path: vision_flan(filtered)/train-*
- config_name: vistext
  data_files:
  - split: train
    path: vistext/train-*
- config_name: visual7w
  data_files:
  - split: train
    path: visual7w/train-*
- config_name: visualmrc
  data_files:
  - split: train
    path: visualmrc/train-*
- config_name: visualwebinstruct(filtered)
  data_files:
  - split: train
    path: visualwebinstruct(filtered)/train-*
- config_name: vizwiz(mathv360k)
  data_files:
  - split: train
    path: vizwiz(mathv360k)/train-*
- config_name: vqaonbd
  data_files:
  - split: train
    path: vqaonbd/train-*
- config_name: vqarad
  data_files:
  - split: train
    path: vqarad/train-*
- config_name: vqav2
  data_files:
  - split: train
    path: vqav2/train-*
- config_name: vsr
  data_files:
  - split: train
    path: vsr/train-*
- config_name: websight
  data_files:
  - split: train
    path: websight/train-*
- config_name: wildvision
  data_files:
  - split: train
    path: wildvision/train-*
- config_name: wordart
  data_files:
  - split: train
    path: wordart/train-*
- config_name: yesbut
  data_files:
  - split: train
    path: yesbut/train-*
size_categories:
- 10M<n<100M
---

# Fine Vision

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6630afa2d40e9b46f95b4c15/8lfflTBHL2SAjcwPQjJSG.png)

FineVision is a massive collection of datasets with **17.3M images**, **24.3M samples**, **88.9M turns**, and **9.5B answer tokens**, designed for training state-of-the-art open Vision-Language-Models.

More detail can be found in the blog post: https://huggingface.co/spaces/HuggingFaceM4/FineVision


### Load the data
```python
  from datasets import load_dataset, get_dataset_config_names

  # Get all subset names and load the first one
  available_subsets = get_dataset_config_names('HuggingFaceM4/FineVision')
  ds = load_dataset('HuggingFaceM4/FineVision', name=available_subsets[0], split='train', streaming=True)
  
  # Inspect the first sample
  ds[0]
```

### Structure

```bash
{
  'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGB size=387x194 at 0x7F8F0B308200>],
  'texts': [{'user': 'Question: What is between the reticulum and the abomasum?\nChoices:\nA. Intestine\nB. Omasum\nC. Stomach\nD. Rumen\nAnswer with the letter.', 'assistant': 'Answer: B'},
            {'user': 'Here is a diagram figure extracted from some Grade 1 - 6 science books.\nPlease first describe the content of this figure in detail, including how the knowledge visually displayed in the diagram.\nThen start with a section title "related knowledge:", briefly and concisely highlight the related domain knowledge and theories that underly this diagram. Note that you do not need to provide much detail. Simply cover the most important concepts.', 'assistant': "The figure is a simple diagram of the four compartments of a ruminant animal's stomach, which are the rumen, reticulum, omasum, and abomasum. The diagram shows the relative size and position of each compartment within the stomach, with arrows indicating the direction of food flow from one compartment to the next. \n\nRelated Knowledge:\n- Ruminant Digestion: Ruminants such as cows, sheep, and goats have a unique digestive system that allows them to break down fibrous plant material, like grass, that other animals cannot digest.\n- Four Stomach Compartments: The rumen is the largest compartment and serves as a fermentation vat where microbes break down fibrous material. The reticulum traps foreign objects and also helps in fermentation. The omasum absorbs water and nutrients, and the abomasum is the true stomach where digestion occurs similarly to monogastric animals.\n- Microbial Fermentation: The microbes in the rumen produce volatile fatty acids which are the primary energy source for ruminants. They also produce gases like methane, which are eructated (belched) out.\n- Ruminant Nutrition: Ruminants rely on a high-fiber diet and have to consume large quantities of forage to meet their nutritional needs."}],
  'source': 'original',
  'image_correspondence_ratings': [4, 3],
  'image_correspondence_min': 3,
  'visual_dependency_ratings': [4, 5],
  'visual_dependency_min': 4,
  'formatting_ratings': [4, 4],
  'formatting_min': 4,
  'relevance_ratings': [5, 5],
  'relevance_min': 5
}
```

### Categories

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6630afa2d40e9b46f95b4c15/Ge_nQPmVrxDy_Te7kUpdB.png)

### Licensing Information

Each of the publicly available sub-datasets present in FineVision are governed by specific licensing conditions. Therefore, when making use of them you must take into consideration each of the licenses governing each dataset. To the extent we have any rights in the prompts, these are licensed under CC-BY-4.0.

### Citation

If you find this dataset useful, please cite:
```
@misc{wiedmann2025finevisionopendataneed,
      title={FineVision: Open Data Is All You Need}, 
      author={Luis Wiedmann and Orr Zohar and Amir Mahla and Xiaohan Wang and Rui Li and Thibaud Frere and Leandro von Werra and Aritra Roy Gosthipaty and Andrés Marafioti},
      year={2025},
      eprint={2510.17269},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.17269}, 
}
```