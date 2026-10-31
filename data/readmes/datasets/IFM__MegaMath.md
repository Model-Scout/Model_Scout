---
license: odc-by
task_categories:
- text-generation
language:
- en
tags:
- math
- code
- pre-training
- synthesis
size_categories:
- 1B<n<10B
---

# MegaMath: Pushing the Limits of Open Math Copora

> Megamath is part of TxT360, curated by LLM360 Team.
<center><img src="teasor.png" alt="MegaMath Collection" /></center>

We introduce MegaMath, an open math pretraining dataset curated from diverse, math-focused sources, with over 300B tokens.
MegaMath is curated via the following three efforts:
- **Revisiting web data**:
  We re-extracted mathematical documents from Common Crawl with math-oriented HTML optimizations, fasttext-based filtering and deduplication, all for acquiring higher-quality data on the Internet.
- **Recalling Math-related code data**:
  We identified high quality math-related code from large code training corpus, Stack-V2, further enhancing data diversity.
- **Exploring Synthetic data**:
  We synthesized QA-style text, math-related code, and interleaved text-code blocks from web data or code data.

## MegaMath Compared to Existing Datasets
MegaMath is the largest open math pre-training dataset to date, surpassing DeepSeekMath (120B) tokens.
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/628f6e5ab90dde28ef57d293/lFa_r4gSXhjwep7XAwwQj.png" width="75%" />
</div>

## MegaMath Delivers with High Quality
During development, we use extensive experiments to find optimal practice for text extraction, deduplication, fasttext training, etc. Training MegaMath data shows better performance than existing open datasets.

<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/628f6e5ab90dde28ef57d293/-E1tZP-vbU1ZPzy56cl4s.png" width="30%" />
  <img src="https://cdn-uploads.huggingface.co/production/uploads/628f6e5ab90dde28ef57d293/XSBJ_wVexM-0rk9bcpU5Q.png" width="30%" />
</div>


## Training MegaMath on Latest LMs
We also release two proof-of-concept models which is based on [Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) and [LLama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B).
Training MegaMath on Llama-3.2-1B and LLama-3.2-3B brings about 15% ~ 20% performance boost on 10 downstream benchmarks, demonstrateing its high data quality.
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/628f6e5ab90dde28ef57d293/EIReQ8TIbyn1V3JfsEKiL.png" width="50%" />
</div>

## Detailed Statistics
| **Category**           | **# Sample(M)** | **# Toks(B)** | **Avg. (# Toks)** |
|------------------------|----------------:|--------------:|------------------:|
| **Web Domain**         | **121.5**       | **279.0**     | **2296.9**        |
| Web                    | 106.5           | 263.9         | 2478.7            |
| Web-Pro                | 15.0            | 15.1          | 1006.0            |
| **Code Domain**        | **13.4**        | **28.1**      | **2102.7**        |
| **Synthetic Data**     | **80.2**        | **64.5**      | **804.5**         |
| Translated Code        | 7.4             | 7.2           | 979.5             |
| Q&A                    | 22.6            | 7.0           | 308.3             |
| Text&Code Block        | 50.2            | 50.3          | 1002.1            |
| **Total**              | **215.1**       | **371.6**     | **1727.6**        |


## Citation
If you use our dataset or find our work useful, please cite
```bibtex
@article{zhou2025megamath,
  title     = {MegaMath: Pushing the Limits of Open Math Corpora},
  author    = {Zhou, Fan and Wang, Zengzhi and Ranjan, Nikhil and Cheng, Zhoujun and Tang, Liping and He, Guowei and Liu, Zhengzhong and Xing, Eric P.},
  journal   = {arXiv preprint arXiv:2504.02807},
  year      = {2025},
  note      = {Preprint}
}
```
