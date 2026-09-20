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

## Llamacpp Static Quantizations of granite-embedding-278m-multilingual

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b4381">b4381</a> for quantization.

Original model: https://huggingface.co/ibm-granite/granite-embedding-278m-multilingual

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

No prompt format found, check original model page

## What's new:

Fix tokenizer

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [granite-embedding-278m-multilingual-f16.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-f16.gguf) | f16 | 0.56GB | false | Full F16 weights. |
| [granite-embedding-278m-multilingual-Q8_0.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q8_0.gguf) | Q8_0 | 0.30GB | false | Extremely high quality, generally unneeded but max available quant. |
| [granite-embedding-278m-multilingual-Q6_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q6_K_L.gguf) | Q6_K_L | 0.28GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [granite-embedding-278m-multilingual-Q5_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q5_K_L.gguf) | Q5_K_L | 0.27GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [granite-embedding-278m-multilingual-Q4_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q4_K_L.gguf) | Q4_K_L | 0.27GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [granite-embedding-278m-multilingual-Q3_K_XL.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q3_K_XL.gguf) | Q3_K_XL | 0.26GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [granite-embedding-278m-multilingual-Q6_K.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q6_K.gguf) | Q6_K | 0.24GB | false | Very high quality, near perfect, *recommended*. |
| [granite-embedding-278m-multilingual-Q5_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q5_K_M.gguf) | Q5_K_M | 0.23GB | false | High quality, *recommended*. |
| [granite-embedding-278m-multilingual-Q5_K_S.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q5_K_S.gguf) | Q5_K_S | 0.22GB | false | High quality, *recommended*. |
| [granite-embedding-278m-multilingual-Q4_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q4_K_M.gguf) | Q4_K_M | 0.22GB | false | Good quality, default size for most use cases, *recommended*. |
| [granite-embedding-278m-multilingual-Q4_K_S.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q4_K_S.gguf) | Q4_K_S | 0.21GB | false | Slightly lower quality with more space savings, *recommended*. |
| [granite-embedding-278m-multilingual-Q4_0.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q4_0.gguf) | Q4_0 | 0.21GB | false | Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [granite-embedding-278m-multilingual-IQ4_NL.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-IQ4_NL.gguf) | IQ4_NL | 0.21GB | false | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [granite-embedding-278m-multilingual-IQ4_XS.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-IQ4_XS.gguf) | IQ4_XS | 0.21GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [granite-embedding-278m-multilingual-Q3_K_L.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q3_K_L.gguf) | Q3_K_L | 0.21GB | false | Lower quality but usable, good for low RAM availability. |
| [granite-embedding-278m-multilingual-Q3_K_M.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-Q3_K_M.gguf) | Q3_K_M | 0.21GB | false | Low quality. |
| [granite-embedding-278m-multilingual-IQ3_M.gguf](https://huggingface.co/bartowski/granite-embedding-278m-multilingual-GGUF/blob/main/granite-embedding-278m-multilingual-IQ3_M.gguf) | IQ3_M | 0.21GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

## Downloading using huggingface-cli

<details>
  <summary>Click to view download instructions</summary>

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/granite-embedding-278m-multilingual-GGUF --include "granite-embedding-278m-multilingual-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/granite-embedding-278m-multilingual-GGUF --include "granite-embedding-278m-multilingual-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (granite-embedding-278m-multilingual-Q8_0) or download them all in place (./)

</details>

## ARM/AVX information

Previously, you would download Q4_0_4_4/4_8/8_8, and these would have their weights interleaved in memory in order to improve performance on ARM and AVX machines by loading up more data in one pass.

Now, however, there is something called "online repacking" for weights. details in [this PR](https://github.com/ggerganov/llama.cpp/pull/9921). If you use Q4_0 and your hardware would benefit from repacking weights, it will do it automatically on the fly.

As of llama.cpp build [b4282](https://github.com/ggerganov/llama.cpp/releases/tag/b4282) you will not be able to run the Q4_0_X_X files and will instead need to use Q4_0.

Additionally, if you want to get slightly better quality for , you can use IQ4_NL thanks to [this PR](https://github.com/ggerganov/llama.cpp/pull/10541) which will also repack the weights for ARM, though only the 4_4 for now. The loading time may be slower but it will result in an overall speed incrase.

<details>
  <summary>Click to view Q4_0_X_X information (deprecated</summary>

I'm keeping this section to show the potential theoretical uplift in performance from using the Q4_0 with online repacking.

<details>
  <summary>Click to view benchmarks on an AVX2 system (EPYC7702)</summary>

| model                          |       size |     params | backend    | threads |          test |                  t/s |  % (vs Q4_0)  |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |-------------: |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         pp512 |        204.03 ± 1.03 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp1024 |        282.92 ± 0.19 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp2048 |        259.49 ± 0.44 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg128 |         39.12 ± 0.27 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg256 |         39.31 ± 0.69 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg512 |         40.52 ± 0.03 |          100% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         pp512 |        301.02 ± 1.74 |          147% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp1024 |        287.23 ± 0.20 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp2048 |        262.77 ± 1.81 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg128 |         18.80 ± 0.99 |           48% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg256 |         24.46 ± 3.04 |           83% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg512 |         36.32 ± 3.59 |           90% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         pp512 |        271.71 ± 3.53 |          133% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp1024 |       279.86 ± 45.63 |          100% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp2048 |        320.77 ± 5.00 |          124% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg128 |         43.51 ± 0.05 |          111% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg256 |         43.35 ± 0.09 |          110% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg512 |         42.60 ± 0.31 |          105% |

Q4_0_8_8 offers a nice bump to prompt processing and a small bump to text generation

</details>

</details>

## Which file should I choose?

<details>
  <summary>Click here for details</summary>

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

</details>

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.

Thank you ZeroWw for the inspiration to experiment with embed/output.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
