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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: source
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
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

# Multilingual Reward Bench (v1.0)

Reward models (RMs) have driven the development of state-of-the-art LLMs today, with unprecedented impact across the globe. However, their performance in multilingual settings still remains understudied. 
In order to probe reward model behavior on multilingual data, we present M-RewardBench, a benchmark for 23 typologically diverse languages. 
M-RewardBench contains prompt-chosen-rejected preference triples obtained by curating and translating chat, safety, and reasoning instances from [RewardBench](https://huggingface.co/datasets/allenai/reward-bench) (Lambert et al., 2024)
This project was part of C4AI's [Expedition Aya challenge](https://sites.google.com/cohere.com/expedition-aya/home), a 6-week open build program, where it won **Silver Prize**.


- **Paper:** https://arxiv.org/abs/2410.15522
- **Presentation**: https://www.youtube.com/watch?v=XIVTXO5myHY
- **Code Repository:** https://github.com/for-ai/m-rewardbench
- **Slides**: https://docs.google.com/presentation/d/19dMkHRjPmBsuHI7jpbmxEptuHKYEyg8hGgCZ0AdSems/edit?usp=sharing


### Dataset Description

Current version of the dataset (v1.0) covers ~2.87k text samples from RewardBench, translated to 23 other languages.

- **Curated by:** Aya RM Multilingual Team
- **Funded by:** The dataset creation part until v1.0 is made possible through Cohere's Research Compute Grant [July 2024].
- **Language(s):** Currently 23 languages: [ Arabic , Chinese , Czech , Dutch , English , French , German , Greek , Hebrew , Hindi , Indonesian , Italian , Japanese , Korean , Persian , Polish , Portuguese , Romanian , Russian , Spanish , Turkish , Ukrainian , Vietnamese ]


## Dataset Structure

M-RewardBench v1 evaluates two capabilities: General-purpose capabilities (Chat, Chat-Hard, Safety, and Reasoning) and Multilingual knowledge (Translation).
The general-purpose tasks follow similar schema as RewardBench, with 23 subsets for each language (~2.87k instances), as shown below:

- id             : unique ID for that particular instance
- prompt         : user request or prompt
- chosen         : human-validated chosen response in the original RewardBench dataset
- rejected       : human-validated rejected response in the original RewardBench dataset
- language       : text's ISO language code
- chosen_model   : model used to generate the chosen response
- rejected_model : model used to generate the rejected response
- source         : the dataset the particular instance was sourced from.
- category       : the RewardBench category an instance belongs to (Chat, Chat-Hard, Safety, Reasoning)

The translation task (800 instances) is another subset, with the following schema:

- id             : unique ID for that particular instance.
- source         : the source text that was translated by the prompt.
- prompt         : the prompt used for requesting the right translation.
- chosen         : human-validated chosen response.
- rejected       : human-validated rejected response.
- subset         : the subset where a particular instance belongs (translation direction + whether it's the easy / hard subset).   
- {chosen, rejected}_score   : the score of the chosen and rejected responses.
- {chosen, rejected}_id      : the ID of the chosen and rejected responses in the original MAPLE dataset.
- {chosen_rejected}_system   : the system used to obtain the chosen / rejected response.


## Citation


```
@inproceedings{gureja-etal-2025-rewardbench,
    title = "{M}-{R}eward{B}ench: Evaluating Reward Models in Multilingual Settings",
    author = "Gureja, Srishti  and
      Miranda, Lester James Validad  and
      Islam, Shayekh Bin  and
      Maheshwary, Rishabh  and
      Sharma, Drishti  and
      Winata, Gusti Triandi  and
      Lambert, Nathan  and
      Ruder, Sebastian  and
      Hooker, Sara  and
      Fadaee, Marzieh",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.3/",
    pages = "43--58",
    ISBN = "979-8-89176-251-0",
    abstract = "Reward models (RMs) have driven the state-of-the-art performance of LLMs today by enabling the integration of human feedback into the language modeling process. However, RMs are primarily trained and evaluated in English, and their capabilities in multilingual settings remain largely understudied. In this work, we conduct a systematic evaluation of several reward models in multilingual settings. We first construct the first-of-its-kind multilingual RM evaluation benchmark, M-RewardBench, consisting of 2.87k preference instances for 23 typologically diverse languages, that tests the chat, safety, reasoning, and translation capabilities of RMs. We then rigorously evaluate a wide range of reward models on M-RewardBench, offering fresh insights into their performance across diverse languages. We identify a significant gap in RMs' performances between English and non-English languages and show that RM preferences can change substantially from one language to another. We also present several findings on how different multilingual aspects impact RM performance. Specifically, we show that the performance of RMs is improved with improved translation quality. Similarly, we demonstrate that the models exhibit better performance for high-resource languages. We release M-RewardBench dataset and the codebase in this study to facilitate a better understanding of RM evaluation in multilingual settings."
}
```

## Dataset Card Authors

- Srishti Gureja ([@srishti-git1110](https://github.com/srishti-git1110))
- Lj Miranda ([@ljvmiranda921](https://github.com/ljvmiranda921))
- Shayekh Bin Islam, ([@ShayekhBinIslam](https://github.com/ShayekhBinIslam))
- Rishabh Maheshwary ([@RishabhMaheshwary](https://github.com/RishabhMaheshwary))
- Drishti Sushma ([@DrishtiShrrrma](https://github.com/DrishtiShrrrma))
- Gusti Winata ([@sanggusti](https://github.com/sanggusti))