
---
license: apache-2.0
language:
- kor
datasets:
- oscar-corpus/OSCAR-2109
library_name: transformers
pipeline_tag: text-generation
tags:
- goldfish
- arxiv:2408.10441
---

# kor_hang_1000mb

Goldfish is a suite of monolingual language models trained for 350 languages.
This model is the <b>Korean</b> (Hangul script) model trained on 1000MB of data, after accounting for an estimated byte premium of 1.29; content-matched text in Korean takes on average 1.29x as many UTF-8 bytes to encode as English.
The Goldfish models are trained primarily for comparability across languages and for low-resource languages; Goldfish performance for high-resource languages is not designed to be comparable with modern large language models (LLMs).

Note: kor_hang is an [individual language](https://iso639-3.sil.org/code_tables/639/data) code. It is not contained in any macrolanguage codes contained in Goldfish (for script hang).

All training and hyperparameter details are in our paper, [Goldfish: Monolingual Language Models for 350 Languages (Chang et al., 2024)](https://www.arxiv.org/abs/2408.10441).

Training code and sample usage: https://github.com/tylerachang/goldfish

Sample usage also in this Google Colab: [link](https://colab.research.google.com/drive/1rHFpnQsyXJ32ONwCosWZ7frjOYjbGCXG?usp=sharing)

## Model details:

To access all Goldfish model details programmatically, see https://github.com/tylerachang/goldfish/blob/main/model_details.json.
All models are trained with a [CLS] (same as [BOS]) token prepended, and a [SEP] (same as [EOS]) token separating sequences.
For best results, make sure that [CLS] is prepended to your input sequence (see sample usage linked above)!
Details for this model specifically:

* Architecture: gpt2
* Parameters: 124770816
* Maximum sequence length: 512 tokens
* Training text data (raw): 1293.31MB
* Training text data (byte premium scaled): 1000.005MB
* Training tokens: 227021824 (x10 epochs)
* Vocabulary size: 50000
* Compute cost: 1.158590818418688e+18 FLOPs or ~109.5 NVIDIA A6000 GPU hours

Training datasets (percentages prior to deduplication):
* 100.00000%: [OSCAR 2021/09](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109)


## Citation

If you use this model, please cite:

```
@article{chang-etal-2024-goldfish,
  title={Goldfish: Monolingual Language Models for 350 Languages},
  author={Chang, Tyler A. and Arnett, Catherine and Tu, Zhuowen and Bergen, Benjamin K.},
  journal={Preprint},
  year={2024},
  url={https://www.arxiv.org/abs/2408.10441},
}
```
