---
pipeline_tag: sentence-similarity
tags:
  - sentence-similarity
  - sentence-transformers
license: mit
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
---

A quantized version of [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small). Quantization was performed per-layer under the same conditions as our ELSERv2 model, as described [here](https://www.elastic.co/search-labs/blog/articles/introducing-elser-v2-part-1#quantization).

[Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://arxiv.org/pdf/2212.03533.pdf).
Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, Furu Wei, arXiv 2022

## Benchmarks

We performed a number of small benchmarks to assess both the changes in quality as well as inference latency against the baseline original model.

### Quality

Measuring NDCG@10 using the dev split of the MIRACL datasets for select languages, we see mostly a marginal change in quality of the quantized model.

| | de | yo| ru | ar | es | th |
| --- | --- | ---| --- | --- | --- | --- |
| multilingual-e5-small | 0.75862 | 0.56193 | 0.80309 | 0.82778 | 0.81672 | 0.85072 |
| multilingual-e5-small-optimized | 0.75992 | 0.48934 | 0.79668 | 0.82017 | 0.8135 | 0.84316 |

To test the English out-of-domain performance, we used the test split of various datasets in the BEIR evaluation. Measuring NDCG@10, we see a larger change in SCIFACT, but marginal in the other datasets evaluated.

| | FIQA | SCIFACT | nfcorpus |
| --- | --- | --- | --- |
| multilingual-e5-small | 0.33126 | 0.677 | 0.31004 |
| multilingual-e5-small-optimized | 0.31734 | 0.65484 | 0.30126 |

### Performance

Using a PyTorch model traced for Linux and Intel CPUs, we performed performance benchmarking with various lengths of input. Overall, we see on average a 50-20% performance improvement with the optimized model.

| input length (characters) | multilingual-e5-small | multilingual-e5-small-optimized | speedup |
| --- | --- | --- | --- |
| 0 - 50 | 0.0181 | 0.00826 | 54.36% |
| 50 - 100 | 0.0275 | 0.0164 | 40.36% |
| 100 - 150 | 0.0366 | 0.0237 | 35.25% |
| 150 - 200 | 0.0435 | 0.0301 | 30.80% |
| 200 - 250 | 0.0514 | 0.0379 | 26.26% |
| 250 - 300 | 0.0569 | 0.043 | 24.43% |
| 300 - 350 | 0.0663 | 0.0513 | 22.62% |
| 350 - 400 | 0.0737 | 0.0576 | 21.85% |

### Disclaimer

This e5 model, as defined, hosted, integrated and used in conjunction with our other Elastic Software is covered by our standard warranty.
