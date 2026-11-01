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
base_model: ibm-granite/granite-embedding-278m-multilingual
model-index:
- name: ibm-granite/granite-embedding-278m-multilingual
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
      value: 0.45557
    - type: ndcg_at_10
      value: 0.49372
    - type: ndcg_at_100
      value: 0.5728
    - type: ndcg_at_1000
      value: 0.59187
    - type: ndcg_at_20
      value: 0.52863
    - type: ndcg_at_3
      value: 0.43969
    - type: ndcg_at_5
      value: 0.45551
    - type: recall_at_1
      value: 0.21785
    - type: recall_at_10
      value: 0.59513
    - type: recall_at_100
      value: 0.85785
    - type: recall_at_1000
      value: 0.96041
    - type: recall_at_20
      value: 0.69357
    - type: recall_at_3
      value: 0.40403
    - type: recall_at_5
      value: 0.48499
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ar)
      type: miracl/mmteb-miracl
      config: ar
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.57459
    - type: ndcg_at_10
      value: 0.64238
    - type: ndcg_at_100
      value: 0.6867
    - type: ndcg_at_1000
      value: 0.6951
    - type: ndcg_at_20
      value: 0.66455
    - type: ndcg_at_3
      value: 0.58162
    - type: ndcg_at_5
      value: 0.60831
    - type: recall_at_1
      value: 0.38064
    - type: recall_at_10
      value: 0.75098
    - type: recall_at_100
      value: 0.91203
    - type: recall_at_1000
      value: 0.96706
    - type: recall_at_20
      value: 0.81978
    - type: recall_at_3
      value: 0.58618
    - type: recall_at_5
      value: 0.66353
  - task:
      type: Retrieval
    dataset:
      name: Miracl (bn)
      type: miracl/mmteb-miracl
      config: bn
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.60341
    - type: ndcg_at_10
      value: 0.68055
    - type: ndcg_at_100
      value: 0.72008
    - type: ndcg_at_1000
      value: 0.72716
    - type: ndcg_at_20
      value: 0.69914
    - type: ndcg_at_3
      value: 0.60805
    - type: ndcg_at_5
      value: 0.64486
    - type: recall_at_1
      value: 0.37948
    - type: recall_at_10
      value: 0.80609
    - type: recall_at_100
      value: 0.94305
    - type: recall_at_1000
      value: 0.98625
    - type: recall_at_20
      value: 0.86141
    - type: recall_at_3
      value: 0.61095
    - type: recall_at_5
      value: 0.71316
  - task:
      type: Retrieval
    dataset:
      name: Miracl (de)
      type: miracl/mmteb-miracl
      config: de
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.45574
    - type: ndcg_at_10
      value: 0.48123
    - type: ndcg_at_100
      value: 0.56049
    - type: ndcg_at_1000
      value: 0.57979
    - type: ndcg_at_20
      value: 0.51785
    - type: ndcg_at_3
      value: 0.41243
    - type: ndcg_at_5
      value: 0.4386
    - type: recall_at_1
      value: 0.20401
    - type: recall_at_10
      value: 0.58779
    - type: recall_at_100
      value: 0.8584
    - type: recall_at_1000
      value: 0.97364
    - type: recall_at_20
      value: 0.69061
    - type: recall_at_3
      value: 0.36573
    - type: recall_at_5
      value: 0.47495
  - task:
      type: Retrieval
    dataset:
      name: Miracl (es)
      type: miracl/mmteb-miracl
      config: es
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.5571
    - type: ndcg_at_10
      value: 0.49688
    - type: ndcg_at_100
      value: 0.60493
    - type: ndcg_at_1000
      value: 0.62922
    - type: ndcg_at_20
      value: 0.54438
    - type: ndcg_at_3
      value: 0.47981
    - type: ndcg_at_5
      value: 0.46584
    - type: recall_at_1
      value: 0.1638
    - type: recall_at_10
      value: 0.54155
    - type: recall_at_100
      value: 0.85136
    - type: recall_at_1000
      value: 0.96951
    - type: recall_at_20
      value: 0.65329
    - type: recall_at_3
      value: 0.31503
    - type: recall_at_5
      value: 0.40356
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fa)
      type: miracl/mmteb-miracl
      config: fa
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.39873
    - type: ndcg_at_10
      value: 0.50226
    - type: ndcg_at_100
      value: 0.56517
    - type: ndcg_at_1000
      value: 0.57967
    - type: ndcg_at_20
      value: 0.5292
    - type: ndcg_at_3
      value: 0.42738
    - type: ndcg_at_5
      value: 0.45843
    - type: recall_at_1
      value: 0.25369
    - type: recall_at_10
      value: 0.63776
    - type: recall_at_100
      value: 0.87686
    - type: recall_at_1000
      value: 0.9671
    - type: recall_at_20
      value: 0.72099
    - type: recall_at_3
      value: 0.43808
    - type: recall_at_5
      value: 0.52378
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fi)
      type: miracl/mmteb-miracl
      config: fi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.60818
    - type: ndcg_at_10
      value: 0.6746
    - type: ndcg_at_100
      value: 0.71516
    - type: ndcg_at_1000
      value: 0.7218
    - type: ndcg_at_20
      value: 0.69692
    - type: ndcg_at_3
      value: 0.6006
    - type: ndcg_at_5
      value: 0.63842
    - type: recall_at_1
      value: 0.39264
    - type: recall_at_10
      value: 0.78577
    - type: recall_at_100
      value: 0.93291
    - type: recall_at_1000
      value: 0.97493
    - type: recall_at_20
      value: 0.85435
    - type: recall_at_3
      value: 0.61055
    - type: recall_at_5
      value: 0.69774
  - task:
      type: Retrieval
    dataset:
      name: Miracl (fr)
      type: miracl/mmteb-miracl
      config: fr
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.3965
    - type: ndcg_at_10
      value: 0.49891
    - type: ndcg_at_100
      value: 0.56492
    - type: ndcg_at_1000
      value: 0.57837
    - type: ndcg_at_20
      value: 0.53163
    - type: ndcg_at_3
      value: 0.39843
    - type: ndcg_at_5
      value: 0.44416
    - type: recall_at_1
      value: 0.22644
    - type: recall_at_10
      value: 0.65169
    - type: recall_at_100
      value: 0.89786
    - type: recall_at_1000
      value: 0.98081
    - type: recall_at_20
      value: 0.75338
    - type: recall_at_3
      value: 0.39798
    - type: recall_at_5
      value: 0.51001
  - task:
      type: Retrieval
    dataset:
      name: Miracl (hi)
      type: miracl/mmteb-miracl
      config: hi
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.36857
    - type: ndcg_at_10
      value: 0.46141
    - type: ndcg_at_100
      value: 0.52565
    - type: ndcg_at_1000
      value: 0.54319
    - type: ndcg_at_20
      value: 0.49384
    - type: ndcg_at_3
      value: 0.39469
    - type: ndcg_at_5
      value: 0.4184
    - type: recall_at_1
      value: 0.20185
    - type: recall_at_10
      value: 0.59474
    - type: recall_at_100
      value: 0.83385
    - type: recall_at_1000
      value: 0.94813
    - type: recall_at_20
      value: 0.69437
    - type: recall_at_3
      value: 0.38993
    - type: recall_at_5
      value: 0.47881
  - task:
      type: Retrieval
    dataset:
      name: Miracl (id)
      type: miracl/mmteb-miracl
      config: id
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.46354
    - type: ndcg_at_10
      value: 0.47229
    - type: ndcg_at_100
      value: 0.5525
    - type: ndcg_at_1000
      value: 0.57648
    - type: ndcg_at_20
      value: 0.50606
    - type: ndcg_at_3
      value: 0.42538
    - type: ndcg_at_5
      value: 0.43717
    - type: recall_at_1
      value: 0.20787
    - type: recall_at_10
      value: 0.54771
    - type: recall_at_100
      value: 0.80689
    - type: recall_at_1000
      value: 0.94032
    - type: recall_at_20
      value: 0.63842
    - type: recall_at_3
      value: 0.36229
    - type: recall_at_5
      value: 0.44437
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ja)
      type: miracl/mmteb-miracl
      config: ja
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.56279
    - type: ndcg_at_10
      value: 0.6281
    - type: ndcg_at_100
      value: 0.67757
    - type: ndcg_at_1000
      value: 0.68667
    - type: ndcg_at_20
      value: 0.6521
    - type: ndcg_at_3
      value: 0.56226
    - type: ndcg_at_5
      value: 0.5866
    - type: recall_at_1
      value: 0.36648
    - type: recall_at_10
      value: 0.7496
    - type: recall_at_100
      value: 0.92461
    - type: recall_at_1000
      value: 0.97827
    - type: recall_at_20
      value: 0.82326
    - type: recall_at_3
      value: 0.55845
    - type: recall_at_5
      value: 0.63854
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ko)
      type: miracl/mmteb-miracl
      config: ko
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.52582
    - type: ndcg_at_10
      value: 0.59216
    - type: ndcg_at_100
      value: 0.65093
    - type: ndcg_at_1000
      value: 0.66204
    - type: ndcg_at_20
      value: 0.62427
    - type: ndcg_at_3
      value: 0.5373
    - type: ndcg_at_5
      value: 0.55886
    - type: recall_at_1
      value: 0.30521
    - type: recall_at_10
      value: 0.71159
    - type: recall_at_100
      value: 0.90203
    - type: recall_at_1000
      value: 0.96714
    - type: recall_at_20
      value: 0.80209
    - type: recall_at_3
      value: 0.515
    - type: recall_at_5
      value: 0.6071
  - task:
      type: Retrieval
    dataset:
      name: Miracl (ru)
      type: miracl/mmteb-miracl
      config: ru
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.47524
    - type: ndcg_at_10
      value: 0.52349
    - type: ndcg_at_100
      value: 0.59725
    - type: ndcg_at_1000
      value: 0.61313
    - type: ndcg_at_20
      value: 0.55669
    - type: ndcg_at_3
      value: 0.46812
    - type: ndcg_at_5
      value: 0.48442
    - type: recall_at_1
      value: 0.24337
    - type: recall_at_10
      value: 0.62437
    - type: recall_at_100
      value: 0.86489
    - type: recall_at_1000
      value: 0.95266
    - type: recall_at_20
      value: 0.71411
    - type: recall_at_3
      value: 0.42927
    - type: recall_at_5
      value: 0.51258
  - task:
      type: Retrieval
    dataset:
      name: Miracl (sw)
      type: miracl/mmteb-miracl
      config: sw
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.5166
    - type: ndcg_at_10
      value: 0.61271
    - type: ndcg_at_100
      value: 0.66099
    - type: ndcg_at_1000
      value: 0.66867
    - type: ndcg_at_20
      value: 0.63643
    - type: ndcg_at_3
      value: 0.54828
    - type: ndcg_at_5
      value: 0.57382
    - type: recall_at_1
      value: 0.35277
    - type: recall_at_10
      value: 0.74368
    - type: recall_at_100
      value: 0.92261
    - type: recall_at_1000
      value: 0.97109
    - type: recall_at_20
      value: 0.81888
    - type: recall_at_3
      value: 0.56739
    - type: recall_at_5
      value: 0.6421
  - task:
      type: Retrieval
    dataset:
      name: Miracl (te)
      type: miracl/mmteb-miracl
      config: te
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.63768
    - type: ndcg_at_10
      value: 0.79193
    - type: ndcg_at_100
      value: 0.80243
    - type: ndcg_at_1000
      value: 0.80438
    - type: ndcg_at_20
      value: 0.79549
    - type: ndcg_at_3
      value: 0.76031
    - type: ndcg_at_5
      value: 0.77915
    - type: recall_at_1
      value: 0.63084
    - type: recall_at_10
      value: 0.92411
    - type: recall_at_100
      value: 0.97363
    - type: recall_at_1000
      value: 0.98833
    - type: recall_at_20
      value: 0.9374
    - type: recall_at_3
      value: 0.84159
    - type: recall_at_5
      value: 0.88627
  - task:
      type: Retrieval
    dataset:
      name: Miracl (th)
      type: miracl/mmteb-miracl
      config: th
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.66712
    - type: ndcg_at_10
      value: 0.73324
    - type: ndcg_at_100
      value: 0.76633
    - type: ndcg_at_1000
      value: 0.77119
    - type: ndcg_at_20
      value: 0.75243
    - type: ndcg_at_3
      value: 0.67393
    - type: ndcg_at_5
      value: 0.70201
    - type: recall_at_1
      value: 0.47106
    - type: recall_at_10
      value: 0.84294
    - type: recall_at_100
      value: 0.95949
    - type: recall_at_1000
      value: 0.98874
    - type: recall_at_20
      value: 0.90085
    - type: recall_at_3
      value: 0.68456
    - type: recall_at_5
      value: 0.75915
  - task:
      type: Retrieval
    dataset:
      name: Miracl (yo)
      type: miracl/mmteb-miracl
      config: yo
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.4958
    - type: ndcg_at_10
      value: 0.68705
    - type: ndcg_at_100
      value: 0.70664
    - type: ndcg_at_1000
      value: 0.71197
    - type: ndcg_at_20
      value: 0.698
    - type: ndcg_at_3
      value: 0.64793
    - type: ndcg_at_5
      value: 0.66709
    - type: recall_at_1
      value: 0.46289
    - type: recall_at_10
      value: 0.85154
    - type: recall_at_100
      value: 0.93557
    - type: recall_at_1000
      value: 0.97479
    - type: recall_at_20
      value: 0.89076
    - type: recall_at_3
      value: 0.7507
    - type: recall_at_5
      value: 0.79202
  - task:
      type: Retrieval
    dataset:
      name: Miracl (zh)
      type: miracl/mmteb-miracl
      config: zh
      split: dev
    metrics:
    - type: ndcg_at_1
      value: 0.47583
    - type: ndcg_at_10
      value: 0.52553
    - type: ndcg_at_100
      value: 0.6
    - type: ndcg_at_1000
      value: 0.61415
    - type: ndcg_at_20
      value: 0.55668
    - type: ndcg_at_3
      value: 0.45839
    - type: ndcg_at_5
      value: 0.48127
    - type: recall_at_1
      value: 0.24488
    - type: recall_at_10
      value: 0.63659
    - type: recall_at_100
      value: 0.89702
    - type: recall_at_1000
      value: 0.97996
    - type: recall_at_20
      value: 0.72652
    - type: recall_at_3
      value: 0.42827
    - type: recall_at_5
      value: 0.52081
---
## 💫 Community Model> granite embedding 278m multilingual by Ibm-Granite

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [ibm-granite](https://huggingface.co/ibm-granite)<br>
**Original model**: [granite-embedding-278m-multilingual](https://huggingface.co/ibm-granite/granite-embedding-278m-multilingual)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b4381](https://github.com/ggerganov/llama.cpp/releases/tag/b4381)<br>

## Technical Details

Embedding model with vector size 768

Max length of 512 tokens

278 million parameters for high quality fast embedding

Supported Languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
