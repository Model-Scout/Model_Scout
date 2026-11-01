---
language:
- ko
license: cc-by-4.0
size_categories:
- 1M<n<10M
dataset_info:
  features:
  - name: Task
    dtype: string
  - name: Question
    dtype: string
  - name: CoT_Rationale
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 1789334780
    num_examples: 1586688
  download_size: 1053794527
  dataset_size: 1789334780
tags:
- haerae
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# Dataset Card for "HAE-RAE-COT-1.5M"
HAE-RAE-COT-1.5M is a dataset encompassing 1,586,688 samples of questions paired with CoT (Chain of Thought) rationales. 
The majority of this dataset is a translation of samples from the [CoT-Collection](https://huggingface.co/datasets/kaist-ai/CoT-Collection), with a portion of samples derived from Korean datasets through the utilization of the gpt-3.5-turbo API. The translation of the CoT-Collection was carried out using the NLLB 600M model.

To the best of our knowledge, HAE-RAE-COT-1.5M represents the largest available CoT or instruction data in the Korean language.

# Summary of included datasets.

| Dataset                                                                      | Count   | %      | License |
|------------------------------------------------------------------------------|---------|--------|--------|
| CoT Collection                                                               | 1,545,112 | 97.38% | non-commercial use |
| [LEAP_NLI](https://github.com/onspark/LEAP_NLI_v2.0)                          | 11,547  | 0.0072%| unknown |
| [squad_kor_v1](https://huggingface.co/datasets/squad_kor_v1)                  | 9,606   | 0.0061%| cc-by-nd-4.0|
| [mwp_kor_v2](https://github.com/jkc-ai/mwp_kr_data)                           | 9,327   | 0.0059%| Apache License 2.0|
| [KorWikiTQ](https://github.com/LG-NLP/KorWikiTableQuestions)                  | 8,276   | 0.0052%| CC BY-SA 4.0 |
| [mwp_kor_v3](https://github.com/tunib-ai/KMWP)                                | 2,820   | 0.0018%| CC-BY-NC-SA 4.0|
| **Total**                                                                    | 1,586,688 | 100.00%|

# License
HAE-RAE-COT-1.5M is only for non-commercial use and is subject to OpenAI's Terms of Use for the generated data. 

# Point of Contact
For any questions contact us via the following email:)
```
spthsrbwls123@yonsei.ac.kr
```

# Contributors
[Baek Sang Won](http://www.linkedin.com/in/sangwon-baek-74a3241b7), [Guijin Son](https://github.com/guijinSON)