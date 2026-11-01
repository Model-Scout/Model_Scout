---
language:
- ar
- zh
- cs
- nl
- fr
- de
- el
- he
- hi
- id
- it
- ja
- ko
- fa
- pl
- pt
- ro
- ru
- es
- tr
- uk
- vi
size_categories:
- 10K<n<100K
pretty_name: Multilingual RewardBench (M-RewardBench)
configs:
- config_name: arb_Arab
  data_files:
  - split: test
    path: arb_Arab/test-*
- config_name: ces_Latn
  data_files:
  - split: test
    path: ces_Latn/test-*
- config_name: deu_Latn
  data_files:
  - split: test
    path: deu_Latn/test-*
- config_name: ell_Grek
  data_files:
  - split: test
    path: ell_Grek/test-*
- config_name: fra_Latn
  data_files:
  - split: test
    path: fra_Latn/test-*
- config_name: heb_Hebr
  data_files:
  - split: test
    path: heb_Hebr/test-*
- config_name: hin_Deva
  data_files:
  - split: test
    path: hin_Deva/test-*
- config_name: ind_Latn
  data_files:
  - split: test
    path: ind_Latn/test-*
- config_name: ita_Latn
  data_files:
  - split: test
    path: ita_Latn/test-*
- config_name: jpn_Jpan
  data_files:
  - split: test
    path: jpn_Jpan/test-*
- config_name: kor_Hang
  data_files:
  - split: test
    path: kor_Hang/test-*
- config_name: nld_Latn
  data_files:
  - split: test
    path: nld_Latn/test-*
- config_name: pes_Arab
  data_files:
  - split: test
    path: pes_Arab/test-*
- config_name: pol_Latn
  data_files:
  - split: test
    path: pol_Latn/test-*
- config_name: por_Latn
  data_files:
  - split: test
    path: por_Latn/test-*
- config_name: ron_Latn
  data_files:
  - split: test
    path: ron_Latn/test-*
- config_name: rus_Cyrl
  data_files:
  - split: test
    path: rus_Cyrl/test-*
- config_name: spa_Latn
  data_files:
  - split: test
    path: spa_Latn/test-*
- config_name: translation
  data_files:
  - split: test
    path: translation/test-*
- config_name: tur_Latn
  data_files:
  - split: test
    path: tur_Latn/test-*
- config_name: ukr_Cyrl
  data_files:
  - split: test
    path: ukr_Cyrl/test-*
- config_name: vie_Latn
  data_files:
  - split: test
    path: vie_Latn/test-*
- config_name: zho_Hans
  data_files:
  - split: test
    path: zho_Hans/test-*
- config_name: zho_Hant
  data_files:
  - split: test
    path: zho_Hant/test-*
tags:
- rewardbench
- cohere
- aya-23
- command-r
dataset_info:
- config_name: arb_Arab
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 6422621
    num_examples: 2869
  download_size: 2761138
  dataset_size: 6422621
- config_name: ces_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 4933560
    num_examples: 2869
  download_size: 2549880
  dataset_size: 4933560
- config_name: deu_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5363398
    num_examples: 2869
  download_size: 2570122
  dataset_size: 5363398
- config_name: ell_Grek
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 8589852
    num_examples: 2869
  download_size: 3527277
  dataset_size: 8589852
- config_name: fra_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5430186
    num_examples: 2869
  download_size: 2565005
  dataset_size: 5430186
- config_name: heb_Hebr
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5939866
    num_examples: 2869
  download_size: 2660058
  dataset_size: 5939866
- config_name: hin_Deva
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 10042205
    num_examples: 2869
  download_size: 3691680
  dataset_size: 10042205
- config_name: ind_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5057921
    num_examples: 2869
  download_size: 2522910
  dataset_size: 5057921
- config_name: ita_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5059482
    num_examples: 2869
  download_size: 2459951
  dataset_size: 5059482
- config_name: jpn_Jpan
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5628914
    num_examples: 2869
  download_size: 2530341
  dataset_size: 5628914
- config_name: kor_Hang
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5245895
    num_examples: 2869
  download_size: 2418778
  dataset_size: 5245895
- config_name: nld_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5089854
    num_examples: 2869
  download_size: 2443945
  dataset_size: 5089854
- config_name: pes_Arab
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 6930424
    num_examples: 2869
  download_size: 2910234
  dataset_size: 6930424
- config_name: pol_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5090190
    num_examples: 2869
  download_size: 2566907
  dataset_size: 5090190
- config_name: por_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5011139
    num_examples: 2869
  download_size: 2416184
  dataset_size: 5011139
- config_name: ron_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5254994
    num_examples: 2869
  download_size: 2557299
  dataset_size: 5254994
- config_name: rus_Cyrl
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 7905166
    num_examples: 2869
  download_size: 3323479
  dataset_size: 7905166
- config_name: spa_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5145292
    num_examples: 2869
  download_size: 2464045
  dataset_size: 5145292
- config_name: translation
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: source
    dtype: string
  - name: chosen_score
    dtype: float64
  - name: rejected_score
    dtype: float64
  - name: chosen_id
    dtype: int64
  - name: rejected_id
    dtype: int64
  - name: chosen_system
    dtype: string
  - name: rejected_system
    dtype: string
  - name: pref_diff
    dtype: float64
  - name: subset
    dtype: string
  splits:
  - name: test
    num_bytes: 742300
    num_examples: 800
  download_size: 351059
  dataset_size: 742300
- config_name: tur_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 5058561
    num_examples: 2869
  download_size: 2429786
  dataset_size: 5058561
- config_name: ukr_Cyrl
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 7577324
    num_examples: 2869
  download_size: 3275068
  dataset_size: 7577324
- config_name: vie_Latn
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 6008277
    num_examples: 2869
  download_size: 2549860
  dataset_size: 6008277
- config_name: zho_Hans
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 4210319
    num_examples: 2869
  download_size: 2161299
  dataset_size: 4210319
- config_name: zho_Hant
  features:
  - name: prompt
    dtype: string
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: language
    dtype: string
  - name: chosen_model
    dtype: string
  - name: rejected_model
    dtype: string
  - name: source
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 4092805
    num_examples: 2869
  download_size: 2416283
  dataset_size: 4092805
license: odc-by
---