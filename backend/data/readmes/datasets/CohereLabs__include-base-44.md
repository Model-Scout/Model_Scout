---
language:
- sq
- ar
- hy
- az
- be
- bn
- eu
- bg
- tr
- hr
- nl
- fa
- es
- et
- fi
- fr
- de
- el
- ka
- he
- hi
- hu
- id
- it
- ja
- kk
- ko
- lt
- ml
- ms
- ne
- pl
- pt
- ru
- ta
- tl
- te
- uk
- ur
- uz
- vi
- zh
- sr
- mk
license: apache-2.0
size_categories:
- 100K<n<1M
task_categories:
- text2text-generation
- multiple-choice
dataset_info:
- config_name: Albanian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 191129
    num_examples: 551
  - name: validation
    num_bytes: 7474
    num_examples: 25
  download_size: 109606
  dataset_size: 198603
- config_name: Arabic
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 291074
    num_examples: 552
  - name: validation
    num_bytes: 17468
    num_examples: 30
  download_size: 135995
  dataset_size: 308542
- config_name: Armenian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 319592
    num_examples: 550
  - name: validation
    num_bytes: 11861
    num_examples: 20
  download_size: 145425
  dataset_size: 331453
- config_name: Azerbaijani
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 223995
    num_examples: 548
  - name: validation
    num_bytes: 11162
    num_examples: 30
  download_size: 115991
  dataset_size: 235157
- config_name: Basque
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 258042
    num_examples: 500
  - name: validation
    num_bytes: 2593
    num_examples: 5
  download_size: 137381
  dataset_size: 260635
- config_name: Belarusian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 273210
    num_examples: 550
  - name: validation
    num_bytes: 6042
    num_examples: 15
  download_size: 131589
  dataset_size: 279252
- config_name: Bengali
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 193337
    num_examples: 548
  - name: validation
    num_bytes: 6933
    num_examples: 20
  download_size: 82272
  dataset_size: 200270
- config_name: Bulgarian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 235519
    num_examples: 550
  - name: validation
    num_bytes: 7317
    num_examples: 15
  download_size: 117309
  dataset_size: 242836
- config_name: Chinese
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 165891
    num_examples: 545
  - name: validation
    num_bytes: 12058
    num_examples: 40
  download_size: 108768
  dataset_size: 177949
- config_name: Croatian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 166462
    num_examples: 550
  - name: validation
    num_bytes: 4038
    num_examples: 15
  download_size: 98909
  dataset_size: 170500
- config_name: Dutch
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 234942
    num_examples: 551
  - name: validation
    num_bytes: 13901
    num_examples: 25
  download_size: 140370
  dataset_size: 248843
- config_name: Dutch - Flemish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 238005
    num_examples: 551
  download_size: 108695
  dataset_size: 238005
- config_name: Dutch-Flemish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 238005
    num_examples: 551
  - name: validation
    num_bytes: 14001
    num_examples: 25
  download_size: 121051
  dataset_size: 252006
- config_name: Estonian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 56037
    num_examples: 224
  - name: validation
    num_bytes: 5806
    num_examples: 25
  download_size: 36464
  dataset_size: 61843
- config_name: Finnish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 314636
    num_examples: 551
  - name: validation
    num_bytes: 11707
    num_examples: 25
  download_size: 182200
  dataset_size: 326343
- config_name: French
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 116611
    num_examples: 419
  - name: validation
    num_bytes: 6129
    num_examples: 25
  download_size: 73077
  dataset_size: 122740
- config_name: Georgian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 390977
    num_examples: 500
  - name: validation
    num_bytes: 5570
    num_examples: 5
  download_size: 149525
  dataset_size: 396547
- config_name: German
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 49451
    num_examples: 139
  - name: validation
    num_bytes: 6385
    num_examples: 15
  download_size: 45375
  dataset_size: 55836
- config_name: Greek
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 409707
    num_examples: 552
  - name: validation
    num_bytes: 22394
    num_examples: 35
  download_size: 188739
  dataset_size: 432101
- config_name: Hebrew
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 295725
    num_examples: 550
  - name: validation
    num_bytes: 7007
    num_examples: 10
  download_size: 149052
  dataset_size: 302732
- config_name: Hindi
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 320205
    num_examples: 547
  - name: validation
    num_bytes: 24722
    num_examples: 40
  download_size: 142242
  dataset_size: 344927
- config_name: Hungarian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 162624
    num_examples: 550
  - name: validation
    num_bytes: 4758
    num_examples: 15
  download_size: 93036
  dataset_size: 167382
- config_name: Indonesian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 213932
    num_examples: 550
  - name: validation
    num_bytes: 12665
    num_examples: 25
  download_size: 127258
  dataset_size: 226597
- config_name: Italian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 372615
    num_examples: 548
  - name: validation
    num_bytes: 15619
    num_examples: 30
  download_size: 182845
  dataset_size: 388234
- config_name: Japanese
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 337780
    num_examples: 501
  - name: validation
    num_bytes: 7102
    num_examples: 15
  download_size: 181822
  dataset_size: 344882
- config_name: Kazakh
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 168787
    num_examples: 500
  - name: validation
    num_bytes: 1606
    num_examples: 5
  download_size: 86848
  dataset_size: 170393
- config_name: Korean
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 259130
    num_examples: 500
  - name: validation
    num_bytes: 5128
    num_examples: 10
  download_size: 132843
  dataset_size: 264258
- config_name: Lithuanian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 187471
    num_examples: 534
  - name: validation
    num_bytes: 8601
    num_examples: 25
  download_size: 109699
  dataset_size: 196072
- config_name: Malay
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 165073
    num_examples: 501
  - name: validation
    num_bytes: 4937
    num_examples: 15
  download_size: 84234
  dataset_size: 170010
- config_name: Malayalam
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 217851
    num_examples: 479
  - name: validation
    num_bytes: 14660
    num_examples: 30
  download_size: 96693
  dataset_size: 232511
- config_name: Nepali
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 238848
    num_examples: 500
  - name: validation
    num_bytes: 4517
    num_examples: 10
  download_size: 93174
  dataset_size: 243365
- config_name: North Macedonian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 286850
    num_examples: 551
  - name: validation
    num_bytes: 9058
    num_examples: 20
  download_size: 133808
  dataset_size: 295908
- config_name: Persian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 351012
    num_examples: 548
  - name: validation
    num_bytes: 16249
    num_examples: 25
  download_size: 184546
  dataset_size: 367261
- config_name: Polish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 189467
    num_examples: 548
  - name: validation
    num_bytes: 8063
    num_examples: 15
  download_size: 113665
  dataset_size: 197530
- config_name: Portuguese
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 573388
    num_examples: 551
  - name: validation
    num_bytes: 32890
    num_examples: 30
  download_size: 347568
  dataset_size: 606278
- config_name: Russian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 281323
    num_examples: 552
  - name: validation
    num_bytes: 23864
    num_examples: 40
  download_size: 138233
  dataset_size: 305187
- config_name: Serbian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 262712
    num_examples: 550
  - name: validation
    num_bytes: 6752
    num_examples: 15
  download_size: 141108
  dataset_size: 269464
- config_name: Spanish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 180237
    num_examples: 550
  - name: validation
    num_bytes: 5553
    num_examples: 20
  download_size: 106489
  dataset_size: 185790
- config_name: Tagalog
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 165883
    num_examples: 500
  - name: validation
    num_bytes: 3118
    num_examples: 10
  download_size: 88113
  dataset_size: 169001
- config_name: Tamil
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 258989
    num_examples: 550
  - name: validation
    num_bytes: 5873
    num_examples: 10
  download_size: 106785
  dataset_size: 264862
- config_name: Telugu
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 327527
    num_examples: 548
  - name: validation
    num_bytes: 11828
    num_examples: 20
  download_size: 145949
  dataset_size: 339355
- config_name: Turkish
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 244565
    num_examples: 548
  - name: validation
    num_bytes: 11100
    num_examples: 20
  download_size: 149858
  dataset_size: 255665
- config_name: Ukrainian
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 362922
    num_examples: 550
  - name: validation
    num_bytes: 7392
    num_examples: 15
  download_size: 160662
  dataset_size: 370314
- config_name: Urdu
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 85348
    num_examples: 352
  - name: validation
    num_bytes: 4276
    num_examples: 15
  download_size: 46763
  dataset_size: 89624
- config_name: Uzbek
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 163712
    num_examples: 551
  - name: validation
    num_bytes: 5594
    num_examples: 20
  download_size: 93035
  dataset_size: 169306
- config_name: Vietnamese
  features:
  - name: language
    dtype: string
  - name: country
    dtype: string
  - name: domain
    dtype: string
  - name: subject
    dtype: string
  - name: regional_feature
    dtype: string
  - name: level
    dtype: string
  - name: question
    dtype: string
  - name: option_a
    dtype: string
  - name: option_b
    dtype: string
  - name: option_c
    dtype: string
  - name: option_d
    dtype: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 240273
    num_examples: 550
  - name: validation
    num_bytes: 7449
    num_examples: 15
  download_size: 117027
  dataset_size: 247722
configs:
- config_name: Albanian
  data_files:
  - split: test
    path: Albanian/test-*
  - split: validation
    path: Albanian/validation-*
- config_name: Arabic
  data_files:
  - split: test
    path: Arabic/test-*
  - split: validation
    path: Arabic/validation-*
- config_name: Armenian
  data_files:
  - split: test
    path: Armenian/test-*
  - split: validation
    path: Armenian/validation-*
- config_name: Azerbaijani
  data_files:
  - split: test
    path: Azerbaijani/test-*
  - split: validation
    path: Azerbaijani/validation-*
- config_name: Basque
  data_files:
  - split: test
    path: Basque/test-*
  - split: validation
    path: Basque/validation-*
- config_name: Belarusian
  data_files:
  - split: test
    path: Belarusian/test-*
  - split: validation
    path: Belarusian/validation-*
- config_name: Bengali
  data_files:
  - split: test
    path: Bengali/test-*
  - split: validation
    path: Bengali/validation-*
- config_name: Bulgarian
  data_files:
  - split: test
    path: Bulgarian/test-*
  - split: validation
    path: Bulgarian/validation-*
- config_name: Chinese
  data_files:
  - split: test
    path: Chinese/test-*
  - split: validation
    path: Chinese/validation-*
- config_name: Croatian
  data_files:
  - split: test
    path: Croatian/test-*
  - split: validation
    path: Croatian/validation-*
- config_name: Dutch
  data_files:
  - split: test
    path: Dutch/test-*
  - split: validation
    path: Dutch/validation-*
- config_name: Dutch - Flemish
  data_files:
  - split: test
    path: Dutch - Flemish/test-*
- config_name: Dutch-Flemish
  data_files:
  - split: test
    path: Dutch-Flemish/test-*
  - split: validation
    path: Dutch-Flemish/validation-*
- config_name: Estonian
  data_files:
  - split: test
    path: Estonian/test-*
  - split: validation
    path: Estonian/validation-*
- config_name: Finnish
  data_files:
  - split: test
    path: Finnish/test-*
  - split: validation
    path: Finnish/validation-*
- config_name: French
  data_files:
  - split: test
    path: French/test-*
  - split: validation
    path: French/validation-*
- config_name: Georgian
  data_files:
  - split: test
    path: Georgian/test-*
  - split: validation
    path: Georgian/validation-*
- config_name: German
  data_files:
  - split: test
    path: German/test-*
  - split: validation
    path: German/validation-*
- config_name: Greek
  data_files:
  - split: test
    path: Greek/test-*
  - split: validation
    path: Greek/validation-*
- config_name: Hebrew
  data_files:
  - split: test
    path: Hebrew/test-*
  - split: validation
    path: Hebrew/validation-*
- config_name: Hindi
  data_files:
  - split: test
    path: Hindi/test-*
  - split: validation
    path: Hindi/validation-*
- config_name: Hungarian
  data_files:
  - split: test
    path: Hungarian/test-*
  - split: validation
    path: Hungarian/validation-*
- config_name: Indonesian
  data_files:
  - split: test
    path: Indonesian/test-*
  - split: validation
    path: Indonesian/validation-*
- config_name: Italian
  data_files:
  - split: test
    path: Italian/test-*
  - split: validation
    path: Italian/validation-*
- config_name: Japanese
  data_files:
  - split: test
    path: Japanese/test-*
  - split: validation
    path: Japanese/validation-*
- config_name: Kazakh
  data_files:
  - split: test
    path: Kazakh/test-*
  - split: validation
    path: Kazakh/validation-*
- config_name: Korean
  data_files:
  - split: test
    path: Korean/test-*
  - split: validation
    path: Korean/validation-*
- config_name: Lithuanian
  data_files:
  - split: test
    path: Lithuanian/test-*
  - split: validation
    path: Lithuanian/validation-*
- config_name: Malay
  data_files:
  - split: test
    path: Malay/test-*
  - split: validation
    path: Malay/validation-*
- config_name: Malayalam
  data_files:
  - split: test
    path: Malayalam/test-*
  - split: validation
    path: Malayalam/validation-*
- config_name: Nepali
  data_files:
  - split: test
    path: Nepali/test-*
  - split: validation
    path: Nepali/validation-*
- config_name: North Macedonian
  data_files:
  - split: test
    path: North Macedonian/test-*
  - split: validation
    path: North Macedonian/validation-*
- config_name: Persian
  data_files:
  - split: test
    path: Persian/test-*
  - split: validation
    path: Persian/validation-*
- config_name: Polish
  data_files:
  - split: test
    path: Polish/test-*
  - split: validation
    path: Polish/validation-*
- config_name: Portuguese
  data_files:
  - split: test
    path: Portuguese/test-*
  - split: validation
    path: Portuguese/validation-*
- config_name: Russian
  data_files:
  - split: test
    path: Russian/test-*
  - split: validation
    path: Russian/validation-*
- config_name: Serbian
  data_files:
  - split: test
    path: Serbian/test-*
  - split: validation
    path: Serbian/validation-*
- config_name: Spanish
  data_files:
  - split: test
    path: Spanish/test-*
  - split: validation
    path: Spanish/validation-*
- config_name: Tagalog
  data_files:
  - split: test
    path: Tagalog/test-*
  - split: validation
    path: Tagalog/validation-*
- config_name: Tamil
  data_files:
  - split: test
    path: Tamil/test-*
  - split: validation
    path: Tamil/validation-*
- config_name: Telugu
  data_files:
  - split: test
    path: Telugu/test-*
  - split: validation
    path: Telugu/validation-*
- config_name: Turkish
  data_files:
  - split: test
    path: Turkish/test-*
  - split: validation
    path: Turkish/validation-*
- config_name: Ukrainian
  data_files:
  - split: test
    path: Ukrainian/test-*
  - split: validation
    path: Ukrainian/validation-*
- config_name: Urdu
  data_files:
  - split: test
    path: Urdu/test-*
  - split: validation
    path: Urdu/validation-*
- config_name: Uzbek
  data_files:
  - split: test
    path: Uzbek/test-*
  - split: validation
    path: Uzbek/validation-*
- config_name: Vietnamese
  data_files:
  - split: test
    path: Vietnamese/test-*
  - split: validation
    path: Vietnamese/validation-*
tags:
- chemistry
- biology
- legal
- music
- finance
- medical
- climate
- art
- code
---
# INCLUDE-base (44 languages)


## Dataset Description

<!-- - **Repository**: https://github.com/agromanou/ -->
- **Paper**: http://arxiv.org/abs/2411.19799


### Dataset Summary

INCLUDE is a comprehensive knowledge- and reasoning-centric benchmark across **44 languages** that evaluates multilingual LLMs for performance in the actual language environments where they would be deployed. 
It contains 22,637 4-option multiple-choice-questions (MCQ) extracted from academic and professional exams, covering 57 topics, including regional knowledge.

For a quicker evaluation, you can use [include-lite-44](https://huggingface.co/datasets/CohereLabs/include-lite-44), which is a subset of `include-base-44`, covering the same 44 languages.

### Languages

Albanian, Arabic, Armenian, Azerbaijani, Basque, Belarusian, Bengali, Bulgarian, Chinese, Croatian, Dutch, Estonian, Finnish, French, Georgian, German, Greek, Hebrew, Hindi, Hungarian, Indonesia, Italian, Japanese, Kazakh, Korean, Lithuanian, Malay, Malayalam, Nepali, North Macedonian, Persian, Polish, Portuguese, russian, Serbian, Spanish, Tagalog, Tamil, Telugu, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese

### Topics

- **Academic**:
Accounting, Agriculture, Anthropology, Architecture and Design, Arts & Humanities, Biology, Business administration, Business ethics, Business, Chemistry, Computer Science, Culturology, Earth science, Economics, Education, Engineering, Environmental studies and forestry, Family and consumer science, Finance, Geography, Health, History, Human physical performance and recreation, Industrial and labor relations, International trade, Journalism, media studies, and communication, Language, Law, Library and museum studies, Literature, Logic, Management, Marketing, Math, Medicine, Military Sciences, Multiple exams, Performing arts, Philosophy, Physics, Political sciences, Psychology, Public Administration, Public Policy, Qualimetry, Religious studies, Risk management and insurance, Social Work, Social work, Sociology, STEM, Transportation, Visual Arts

- **Licenses**:
Driving License, Marine License, Medical License, Professional Certifications


### Data schema

An example from a French Law question looks as follows:
```
{
	"language": "French",
	"country": "France",
	"level": "Academic",
	"domain": "Arts & Humanities",
	"subject": "Law",
	"regional_feature": "region explicit",
	"question": "Que permet l'article 49-3 de la Constitution ?",
	"choices": ["de recourir au référendum", "au Parlement de contrôler l'action du Gouvernement", "l'adoption sans vote d'une loi", "de prononcer la dissolution de l'Assemblée nationale"],
	"answer": 2
}
```

### Model Performance

Models performance on **INCLUDE** using the Harness-eval framework.


| **Model**                          | **Original Language instructions** | **English instructions** |
|------------------------------------|:--------------------------:|:--------------------:|
| Llama3.1-70B-Instruct              |            70.6            |         70.9         |
| Qwen2.5-14B                        |            62.3            |         62.6         |
| Aya-expanse-32b                    |            59.1            |         59.5         |
| Qwen2.5-7B                         |            55.0            |         55.5         |
| Qwen2.5-7B-Instruct                |            54.8            |         54.8         |
| Llama-3.1-8B-Instruct              |            53.5            |         54.4         |
| Gemma-7B                           |            53.5            |         53.2         |
| Llama-3.1-8B                       |            51.2            |         51.9         |
| Aya-expanse-8b                     |            47.2            |         47.8         |
| Mistral-7B                         |            44.1            |         44.6         |
| Mistral-7B-Instruct                |            44.2            |         44.3         |
| Gemma-7B-Instruct                  |            38.6            |         39.3         |


## Citation

```
@article{romanou2024include,
  title={INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge},
  author={Romanou, Angelika and Foroutan, Negar and Sotnikova, Anna and Chen, Zeming and Nelaturu, Sree Harsha and Singh, Shivalika and Maheshwary, Rishabh and Altomare, Micol and Haggag, Mohamed A and Amayuelas, Alfonso and others},
  journal={arXiv preprint arXiv:2411.19799},
  year={2024}
}
```