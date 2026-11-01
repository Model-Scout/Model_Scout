---
quantized_by: bartowski
pipeline_tag: text-generation
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
tags:
- language
- granite
- embeddings
- multilingual
license: apache-2.0
base_model: ibm-granite/granite-embedding-107m-multilingual
model-index:
- name: ibm-granite/granite-embedding-107m-multilingual
  results:
  - task:
      type: Retrieval
    dataset:
      name: Miracl (en)
      type: miracl/mmteb-miracl
      config: en
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41176
    - type: ndcg_at_10
      value: 0.46682
    - type: ndcg_at_100
      value: 0.54326
    - type: ndcg_at_1000
      value: 0.56567
    - type: ndcg_at_20
      value: 0.50157
    - type: ndcg_at_3
      value: 0.41197
    - type: ndcg_at_5
      value: 0.42086
    - type: recall_at_1
      value: 0.19322
    - type: recall_at_10
      value: 0.57721
    - type: recall_at_100
      value: 0.83256
    - type: recall_at_1000
      value: 0.95511
    - type: recall_at_20
      value: 0.6757
    - type: recall_at_3
      value: 0.37171
    - type: recall_at_5
      value: 0.44695
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ar)
      type: miracl/mmteb-miracl
      config: ar
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.55559
    - type: ndcg_at_10
      value: 0.62541
    - type: ndcg_at_100
      value: 0.67101
    - type: ndcg_at_1000
      value: 0.6805
    - type: ndcg_at_20
      value: 0.64739
    - type: ndcg_at_3
      value: 0.56439
    - type: ndcg_at_5
      value: 0.59347
    - type: recall_at_1
      value: 0.37009
    - type: recall_at_10
      value: 0.73317
    - type: recall_at_100
      value: 0.90066
    - type: recall_at_1000
      value: 0.96272
    - type: recall_at_20
      value: 0.80205
    - type: recall_at_3
      value: 0.56903
    - type: recall_at_5
      value: 0.6518
  - task:
      type: Retrieval
    dataset:
      name: Miracl (bn)
      type: miracl/mmteb-miracl
      config: bn
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.56691
    - type: ndcg_at_10
      value: 0.65484
    - type: ndcg_at_100
      value: 0.70142
    - type: ndcg_at_1000
      value: 0.70994
    - type: ndcg_at_20
      value: 0.67838
    - type: ndcg_at_3
      value: 0.5988
    - type: ndcg_at_5
      value: 0.62718
    - type: recall_at_1
      value: 0.3605
    - type: recall_at_10
      value: 0.76854
    - type: recall_at_100
      value: 0.9285
    - type: recall_at_1000
      value: 0.97928
    - type: recall_at_20
      value: 0.83667
    - type: recall_at_3
      value: 0.61596
    - type: recall_at_5
      value: 0.69766
  - task:
      type: Retrieval
    dataset:
      name: Miracl (de)
      type: miracl/mmteb-miracl
      config: de
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41967
    - type: ndcg_at_10
      value: 0.45141
    - type: ndcg_at_100
      value: 0.53461
    - type: ndcg_at_1000
      value: 0.55463
    - type: ndcg_at_20
      value: 0.49012
    - type: ndcg_at_3
      value: 0.39486
    - type: ndcg_at_5
      value: 0.41496
    - type: recall_at_1
      value: 0.19494
    - type: recall_at_10
      value: 0.53774
    - type: recall_at_100
      value: 0.83314
    - type: recall_at_1000
      value: 0.95045
    - type: recall_at_20
      value: 0.65659
    - type: recall_at_3
      value: 0.3556
    - type: recall_at_5
      value: 0.44448
  - task:
      type: Retrieval
    dataset:
      name: Miracl (es)
      type: miracl/mmteb-miracl
      config: es
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.54475
    - type: ndcg_at_10
      value: 0.46593
    - type: ndcg_at_100
      value: 0.58079
    - type: ndcg_at_1000
      value: 0.60656
    - type: ndcg_at_20
      value: 0.51858
    - type: ndcg_at_3
      value: 0.4578
    - type: ndcg_at_5
      value: 0.44321
    - type: recall_at_1
      value: 0.15966
    - type: recall_at_10
      value: 0.49343
    - type: recall_at_100
      value: 0.82684
    - type: recall_at_1000
      value: 0.95299
    - type: recall_at_20
      value: 0.62367
    - type: recall_at_3
      value: 0.2949
    - type: recall_at_5
      value: 0.37983
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fa)
      type: miracl/mmteb-miracl
      config: fa
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.36709
    - type: ndcg_at_10
      value: 0.46961
    - type: ndcg_at_100
      value: 0.53262
    - type: ndcg_at_1000
      value: 0.55024
    - type: ndcg_at_20
      value: 0.49892
    - type: ndcg_at_3
      value: 0.40235
    - type: ndcg_at_5
      value: 0.42866
    - type: recall_at_1
      value: 0.22735
    - type: recall_at_10
      value: 0.59949
    - type: recall_at_100
      value: 0.83867
    - type: recall_at_1000
      value: 0.95007
    - type: recall_at_20
      value: 0.68947
    - type: recall_at_3
      value: 0.41781
    - type: recall_at_5
      value: 0.49374
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fi)
      type: miracl/mmteb-miracl
      config: fi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.59245
    - type: ndcg_at_10
      value: 0.65551
    - type: ndcg_at_100
      value: 0.6967
    - type: ndcg_at_1000
      value: 0.70521
    - type: ndcg_at_20
      value: 0.67552
    - type: ndcg_at_3
      value: 0.58876
    - type: ndcg_at_5
      value: 0.61779
    - type: recall_at_1
      value: 0.37669
    - type: recall_at_10
      value: 0.76529
    - type: recall_at_100
      value: 0.9156
    - type: recall_at_1000
      value: 0.96977
    - type: recall_at_20
      value: 0.82685
    - type: recall_at_3
      value: 0.60234
    - type: recall_at_5
      value: 0.67135
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fr)
      type: miracl/mmteb-miracl
      config: fr
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.38776
    - type: ndcg_at_10
      value: 0.47589
    - type: ndcg_at_100
      value: 0.54641
    - type: ndcg_at_1000
      value: 0.5629
    - type: ndcg_at_20
      value: 0.51203
    - type: ndcg_at_3
      value: 0.38924
    - type: ndcg_at_5
      value: 0.42572
    - type: recall_at_1
      value: 0.22082
    - type: recall_at_10
      value: 0.61619
    - type: recall_at_100
      value: 0.87237
    - type: recall_at_1000
      value: 0.97449
    - type: recall_at_20
      value: 0.72689
    - type: recall_at_3
      value: 0.39527
    - type: recall_at_5
      value: 0.48983
  - task:
      type: Retrieval
    dataset:
      name: Miracl (hi)
      type: miracl/mmteb-miracl
      config: hi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.33143
    - type: ndcg_at_10
      value: 0.42084
    - type: ndcg_at_100
      value: 0.48647
    - type: ndcg_at_1000
      value: 0.50712
    - type: ndcg_at_20
      value: 0.45399
    - type: ndcg_at_3
      value: 0.34988
    - type: ndcg_at_5
      value: 0.37938
    - type: recall_at_1
      value: 0.17852
    - type: recall_at_10
      value: 0.55217
    - type: recall_at_100
      value: 0.79929
    - type: recall_at_1000
      value: 0.93434
    - type: recall_at_20
      value: 0.65231
    - type: recall_at_3
      value: 0.33765
    - type: recall_at_5
      value: 0.43828
  - task:
      type: Retrieval
    dataset:
      name: Miracl (id)
      type: miracl/mmteb-miracl
      config: id
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.43854
    - type: ndcg_at_10
      value: 0.45459
    - type: ndcg_at_100
      value: 0.53643
    - type: ndcg_at_1000
      value: 0.56052
    - type: ndcg_at_20
      value: 0.48795
    - type: ndcg_at_3
      value: 0.41041
    - type: ndcg_at_5
      value: 0.42235
    - type: recall_at_1
      value: 0.19193
    - type: recall_at_10
      value: 0.5289
    - type: recall_at_100
      value: 0.79649
    - type: recall_at_1000
      value: 0.92937
    - type: recall_at_20
      value: 0.61813
    - type: recall_at_3
      value: 0.35431
    - type: recall_at_5
      value: 0.43348
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ja)
      type: miracl/mmteb-miracl
      config: ja
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.53256
    - type: ndcg_at_10
      value: 0.59922
    - type: ndcg_at_100
      value: 0.65407
    - type: ndcg_at_1000
      value: 0.66484
    - type: ndcg_at_20
      value: 0.62596
    - type: ndcg_at_3
      value: 0.53717
    - type: ndcg_at_5
      value: 0.56523
    - type: recall_at_1
      value: 0.34555
    - type: recall_at_10
      value: 0.71476
    - type: recall_at_100
      value: 0.91152
    - type: recall_at_1000
      value: 0.97728
    - type: recall_at_20
      value: 0.79811
    - type: recall_at_3
      value: 0.53482
    - type: recall_at_5
      value: 0.62327
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ko)
      type: miracl/mmteb-miracl
      config: ko
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.5493
    - type: ndcg_at_10
      value: 0.58413
    - type: ndcg_at_100
      value: 0.64374
    - type: ndcg_at_1000
      value: 0.65655
    - type: ndcg_at_20
      value: 0.61732
    - type: ndcg_at_3
      value: 0.53068
    - type: ndcg_at_5
      value: 0.55202
    - type: recall_at_1
      value: 0.32602
    - type: recall_at_10
      value: 0.68647
    - type: recall_at_100
      value: 0.87746
    - type: recall_at_1000
      value: 0.95524
    - type: recall_at_20
      value: 0.78089
    - type: recall_at_3
      value: 0.49173
    - type: recall_at_5
      value: 0.5827
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ru)
      type: miracl/mmteb-miracl
      config: ru
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.43131
    - type: ndcg_at_10
      value: 0.48262
    - type: ndcg_at_100
      value: 0.56158
    - type: ndcg_at_1000
      value: 0.57929
    - type: ndcg_at_20
      value: 0.52023
    - type: ndcg_at_3
      value: 0.42808
    - type: ndcg_at_5
      value: 0.44373
    - type: recall_at_1
      value: 0.22018
    - type: recall_at_10
      value: 0.58034
    - type: recall_at_100
      value: 0.84074
    - type: recall_at_1000
      value: 0.93938
    - type: recall_at_20
      value: 0.68603
    - type: recall_at_3
      value: 0.39307
    - type: recall_at_5
      value: 0.47077
  - task:
      type: Retrieval
    dataset:
      name: Miracl (sw)
      type: miracl/mmteb-miracl
      config: sw
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.50415
    - type: ndcg_at_10
      value: 0.59111
    - type: ndcg_at_100
      value: 0.64312
    - type: ndcg_at_1000
      value: 0.65089
    - type: ndcg_at_20
      value: 0.61651
    - type: ndcg_at_3
      value: 0.5304
    - type: ndcg_at_5
      value: 0.56139
    - type: recall_at_1
      value: 0.33267
    - type: recall_at_10
      value: 0.72082
    - type: recall_at_100
      value: 0.91377
    - type: recall_at_1000
      value: 0.96152
    - type: recall_at_20
      value: 0.79943
    - type: recall_at_3
      value: 0.5548
    - type: recall_at_5
      value: 0.64302
  - task:
      type: Retrieval
    dataset:
      name: Miracl (te)
      type: miracl/mmteb-miracl
      config: te
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.64372
    - type: ndcg_at_10
      value: 0.78175
    - type: ndcg_at_100
      value: 0.79523
    - type: ndcg_at_1000
      value: 0.79774
    - type: ndcg_at_20
      value: 0.78826
    - type: ndcg_at_3
      value: 0.74856
    - type: ndcg_at_5
      value: 0.77128
    - type: recall_at_1
      value: 0.63688
    - type: recall_at_10
      value: 0.90358
    - type: recall_at_100
      value: 0.96558
    - type: recall_at_1000
      value: 0.9847
    - type: recall_at_20
      value: 0.92834
    - type: recall_at_3
      value: 0.81804
    - type: recall_at_5
      value: 0.87198
  - task:
      type: Retrieval
    dataset:
      name: Miracl (th)
      type: miracl/mmteb-miracl
      config: th
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.65484
    - type: ndcg_at_10
      value: 0.71774
    - type: ndcg_at_100
      value: 0.75362
    - type: ndcg_at_1000
      value: 0.75898
    - type: ndcg_at_20
      value: 0.73709
    - type: ndcg_at_3
      value: 0.66199
    - type: ndcg_at_5
      value: 0.68451
    - type: recall_at_1
      value: 0.45911
    - type: recall_at_10
      value: 0.82619
    - type: recall_at_100
      value: 0.95515
    - type: recall_at_1000
      value: 0.98854
    - type: recall_at_20
      value: 0.88447
    - type: recall_at_3
      value: 0.67437
    - type: recall_at_5
      value: 0.73786
  - task:
      type: Retrieval
    dataset:
      name: Miracl (yo)
      type: miracl/mmteb-miracl
      config: yo
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.46218
    - type: ndcg_at_10
      value: 0.64685
    - type: ndcg_at_100
      value: 0.66941
    - type: ndcg_at_1000
      value: 0.67361
    - type: ndcg_at_20
      value: 0.65548
    - type: ndcg_at_3
      value: 0.57609
    - type: ndcg_at_5
      value: 0.62021
    - type: recall_at_1
      value: 0.42787
    - type: recall_at_10
      value: 0.82913
    - type: recall_at_100
      value: 0.93277
    - type: recall_at_1000
      value: 0.96499
    - type: recall_at_20
      value: 0.85994
    - type: recall_at_3
      value: 0.65406
    - type: recall_at_5
      value: 0.7542
  - task:
      type: Retrieval
    dataset:
      name: Miracl (zh)
      type: miracl/mmteb-miracl
      config: zh
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.41985
    - type: ndcg_at_10
      value: 0.4837
    - type: ndcg_at_100
      value: 0.55961
    - type: ndcg_at_1000
      value: 0.5762
    - type: ndcg_at_20
      value: 0.51595
    - type: ndcg_at_3
      value: 0.42094
    - type: ndcg_at_5
      value: 0.44273
    - type: recall_at_1
      value: 0.21446
    - type: recall_at_10
      value: 0.59695
    - type: recall_at_100
      value: 0.87388
    - type: recall_at_1000
      value: 0.96833
    - type: recall_at_20
      value: 0.69252
    - type: recall_at_3
      value: 0.40377
    - type: recall_at_5
      value: 0.4903
---
## 💫 Community Model> granite embedding 107m multilingual by Ibm-Granite

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [ibm-granite](https://huggingface.co/ibm-granite)<br>
**Original model**: [granite-embedding-107m-multilingual](https://huggingface.co/ibm-granite/granite-embedding-107m-multilingual)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b4381](https://github.com/ggerganov/llama.cpp/releases/tag/b4381)<br>

## Technical Details

Embedding model with vector size 384

Max length of 512 tokens

107 million parameters for high quality fast embedding

Supported Languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
