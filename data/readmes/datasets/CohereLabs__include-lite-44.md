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
- 1K<n<10K
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 91738
    num_examples: 251
  download_size: 46696
  dataset_size: 91738
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 132872
    num_examples: 250
  download_size: 51481
  dataset_size: 132872
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 147071
    num_examples: 251
  download_size: 57254
  dataset_size: 147071
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 101309
    num_examples: 250
  download_size: 45393
  dataset_size: 101309
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 131676
    num_examples: 250
  download_size: 59081
  dataset_size: 131676
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 135477
    num_examples: 250
  download_size: 62264
  dataset_size: 135477
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 91032
    num_examples: 249
  download_size: 34326
  dataset_size: 91032
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 106771
    num_examples: 250
  download_size: 47035
  dataset_size: 106771
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 76709
    num_examples: 245
  download_size: 43485
  dataset_size: 76709
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 76437
    num_examples: 250
  download_size: 38307
  dataset_size: 76437
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 111189
    num_examples: 251
  download_size: 54365
  dataset_size: 111189
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
    num_bytes: 111763
    num_examples: 251
  download_size: 54179
  dataset_size: 111763
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 45059
    num_examples: 183
  download_size: 20098
  dataset_size: 45059
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 144646
    num_examples: 251
  download_size: 74146
  dataset_size: 144646
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 68283
    num_examples: 250
  download_size: 33679
  dataset_size: 68283
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 199506
    num_examples: 250
  download_size: 63702
  dataset_size: 199506
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 29946
    num_examples: 89
  download_size: 18834
  dataset_size: 29946
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 180912
    num_examples: 253
  download_size: 71681
  dataset_size: 180912
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 127152
    num_examples: 250
  download_size: 54731
  dataset_size: 127152
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 149815
    num_examples: 245
  download_size: 55111
  dataset_size: 149815
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 75141
    num_examples: 250
  download_size: 37423
  dataset_size: 75141
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 102154
    num_examples: 248
  download_size: 50504
  dataset_size: 102154
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 171408
    num_examples: 251
  download_size: 83567
  dataset_size: 171408
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 149605
    num_examples: 249
  download_size: 73173
  dataset_size: 149605
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 85483
    num_examples: 250
  download_size: 40370
  dataset_size: 85483
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 131721
    num_examples: 250
  download_size: 59342
  dataset_size: 131721
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 94088
    num_examples: 250
  download_size: 46970
  dataset_size: 94088
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 83375
    num_examples: 249
  download_size: 38086
  dataset_size: 83375
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 111903
    num_examples: 252
  download_size: 40696
  dataset_size: 111903
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 119606
    num_examples: 250
  download_size: 41847
  dataset_size: 119606
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 135718
    num_examples: 251
  download_size: 57077
  dataset_size: 135718
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 159685
    num_examples: 248
  download_size: 70919
  dataset_size: 159685
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 91001
    num_examples: 250
  download_size: 47730
  dataset_size: 91001
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 280924
    num_examples: 253
  download_size: 152158
  dataset_size: 280924
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 127893
    num_examples: 252
  download_size: 52680
  dataset_size: 127893
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 116271
    num_examples: 250
  download_size: 51407
  dataset_size: 116271
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 85132
    num_examples: 250
  download_size: 44015
  dataset_size: 85132
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 84686
    num_examples: 250
  download_size: 39822
  dataset_size: 84686
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 114008
    num_examples: 250
  download_size: 41047
  dataset_size: 114008
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 153062
    num_examples: 249
  download_size: 62104
  dataset_size: 153062
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 116830
    num_examples: 249
  download_size: 64902
  dataset_size: 116830
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 175129
    num_examples: 250
  download_size: 67190
  dataset_size: 175129
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 57366
    num_examples: 250
  download_size: 22493
  dataset_size: 57366
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 73036
    num_examples: 251
  download_size: 36549
  dataset_size: 73036
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
  - name: choices
    sequence: string
  - name: answer
    dtype: int64
  splits:
  - name: test
    num_bytes: 111844
    num_examples: 250
  download_size: 46950
  dataset_size: 111844
configs:
- config_name: Albanian
  data_files:
  - split: test
    path: Albanian/test-*
- config_name: Arabic
  data_files:
  - split: test
    path: Arabic/test-*
- config_name: Armenian
  data_files:
  - split: test
    path: Armenian/test-*
- config_name: Azerbaijani
  data_files:
  - split: test
    path: Azerbaijani/test-*
- config_name: Basque
  data_files:
  - split: test
    path: Basque/test-*
- config_name: Belarusian
  data_files:
  - split: test
    path: Belarusian/test-*
- config_name: Bengali
  data_files:
  - split: test
    path: Bengali/test-*
- config_name: Bulgarian
  data_files:
  - split: test
    path: Bulgarian/test-*
- config_name: Chinese
  data_files:
  - split: test
    path: Chinese/test-*
- config_name: Croatian
  data_files:
  - split: test
    path: Croatian/test-*
- config_name: Dutch
  data_files:
  - split: test
    path: Dutch/test-*
- config_name: Dutch-Flemish
  data_files:
  - split: test
    path: Dutch-Flemish/test-*
- config_name: Estonian
  data_files:
  - split: test
    path: Estonian/test-*
- config_name: Finnish
  data_files:
  - split: test
    path: Finnish/test-*
- config_name: French
  data_files:
  - split: test
    path: French/test-*
- config_name: Georgian
  data_files:
  - split: test
    path: Georgian/test-*
- config_name: German
  data_files:
  - split: test
    path: German/test-*
- config_name: Greek
  data_files:
  - split: test
    path: Greek/test-*
- config_name: Hebrew
  data_files:
  - split: test
    path: Hebrew/test-*
- config_name: Hindi
  data_files:
  - split: test
    path: Hindi/test-*
- config_name: Hungarian
  data_files:
  - split: test
    path: Hungarian/test-*
- config_name: Indonesian
  data_files:
  - split: test
    path: Indonesian/test-*
- config_name: Italian
  data_files:
  - split: test
    path: Italian/test-*
- config_name: Japanese
  data_files:
  - split: test
    path: Japanese/test-*
- config_name: Kazakh
  data_files:
  - split: test
    path: Kazakh/test-*
- config_name: Korean
  data_files:
  - split: test
    path: Korean/test-*
- config_name: Lithuanian
  data_files:
  - split: test
    path: Lithuanian/test-*
- config_name: Malay
  data_files:
  - split: test
    path: Malay/test-*
- config_name: Malayalam
  data_files:
  - split: test
    path: Malayalam/test-*
- config_name: Nepali
  data_files:
  - split: test
    path: Nepali/test-*
- config_name: North Macedonian
  data_files:
  - split: test
    path: North Macedonian/test-*
- config_name: Persian
  data_files:
  - split: test
    path: Persian/test-*
- config_name: Polish
  data_files:
  - split: test
    path: Polish/test-*
- config_name: Portuguese
  data_files:
  - split: test
    path: Portuguese/test-*
- config_name: Russian
  data_files:
  - split: test
    path: Russian/test-*
- config_name: Serbian
  data_files:
  - split: test
    path: Serbian/test-*
- config_name: Spanish
  data_files:
  - split: test
    path: Spanish/test-*
- config_name: Tagalog
  data_files:
  - split: test
    path: Tagalog/test-*
- config_name: Tamil
  data_files:
  - split: test
    path: Tamil/test-*
- config_name: Telugu
  data_files:
  - split: test
    path: Telugu/test-*
- config_name: Turkish
  data_files:
  - split: test
    path: Turkish/test-*
- config_name: Ukrainian
  data_files:
  - split: test
    path: Ukrainian/test-*
- config_name: Urdu
  data_files:
  - split: test
    path: Urdu/test-*
- config_name: Uzbek
  data_files:
  - split: test
    path: Uzbek/test-*
- config_name: Vietnamese
  data_files:
  - split: test
    path: Vietnamese/test-*
tags:
- chemistry
- biology
- finance
- legal
- art
- code
- medical
- music
- climate
---
# INCLUDE-lite (44 languages)


## Dataset Description

<!-- - **Repository**: https://github.com/agromanou/ -->
- **Paper**: http://arxiv.org/abs/2411.19799


### Dataset Summary

INCLUDE is a comprehensive knowledge- and reasoning-centric benchmark across **44 languages** that evaluates multilingual LLMs for performance in the actual language environments where they would be deployed. 
It contains 11,095 4-option multiple-choice-questions (MCQ) extracted from academic and professional exams, covering 57 topics, including regional knowledge.

For evaluation in a larger set, you can use [include-base-44](https://huggingface.co/datasets/CohereLabs/include-base-44), which is a superset of `include-lite-44`, covering the same 44 languages.



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


| **Model**                          | **Original Lang instructions** | **English instructions** |
|------------------------------------|:------------------------------:|:------------------------:|
| Llama3.1-70B-Instruct              |              70.3              |           70.6           |
| Qwen2.5-14B                        |              61.8              |           61.9           |
| Aya-expanse-32b                    |              58.9              |           59.5           |
| Qwen2.5-7B                         |              54.4              |           54.9           |
| Qwen2.5-7B-Instruct                |              54.5              |           54.6           |
| Llama-3.1-8B-Instruct              |              53.5              |           54.4           |
| Gemma-7B                           |              53.6              |           53.1           |
| Llama-3.1-8B                       |              51.2              |           52.1           |
| Aya-expanse-8b                     |              47.3              |           48.0           |
| Mistral-7B                         |              44.5              |           44.7           |
| Mistral-7B-Instruct                |              43.8              |           43.9           |
| Gemma-7B-Instruct                  |              39.1              |           39.7           |


## Citation

```
  @article{romanou2024include,
  title={INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge},
  author={Romanou, Angelika and Foroutan, Negar and Sotnikova, Anna and Chen, Zeming and Nelaturu, Sree Harsha and Singh, Shivalika and Maheshwary, Rishabh and Altomare, Micol and Haggag, Mohamed A and Amayuelas, Alfonso and others},
  journal={arXiv preprint arXiv:2411.19799},
  year={2024}
}
```