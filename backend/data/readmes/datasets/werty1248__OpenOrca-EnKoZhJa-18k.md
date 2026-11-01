---
license: mit
language:
- en
- ko
- zh
- ja
size_categories:
- 10K<n<100K
---

This dataset is a collection of Korean, Chinese, and Japanese OpenOrca translation datasets.

The dataset was matched using **id** based on **kyujinpy/OpenOrca-KO**, which had the smallest number of rows.

When more than one translation existed for a language, I chose the more similar one based on similarity of embedding([BAAI/BGE-m3](https://huggingface.co/BAAI/bge-m3)).

### Data Sources
- English(Original)
  - [Open-Orca/OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca)
- Korean(Translated with DeepL Pro API)
  - [kyujinpy/OpenOrca-KO](https://huggingface.co/datasets/kyujinpy/OpenOrca-KO)
- Chinese(Translated with Google Translate)
  - [yys/OpenOrca-Chinese](https://huggingface.co/datasets/yys/OpenOrca-Chinese)
- Japanese(Translated)
  - [shi3z/OpenOrcaJapanese](https://huggingface.co/datasets/shi3z/OpenOrcaJapanese)
  - [shumpei2525/OpenOrca-train-ja](https://huggingface.co/datasets/shumpei2525/OpenOrca-train-ja)