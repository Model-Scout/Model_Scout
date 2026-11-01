---
dataset_info:
  features:
  - name: sent1
    dtype: string
  - name: sent2
    dtype: string
  - name: labels
    dtype: int64
  splits:
  - name: test
    num_bytes: 637234
    num_examples: 554
  download_size: 322760
  dataset_size: 637234
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
license: cc-by-nc-sa-4.0
language:
- en
- ko
task_categories:
- text-classification
tags:
- chemistry
- chemteb
- wikipedia
- pubchem
pretty_name: PubChem & Wikipedia English-Korean Paragraph Pair Classification
size_categories:
- n<1K
---
# PubChem & Wikipedia English-Korean Paragraph Pair Classification
This dataset is a multilingual extension of the [PubChem & Wikipedia Paragraphs Pair Classification](https://huggingface.co/datasets/BASF-AI/PubChemWikiParagraphsPC) dataset. It includes pairs of paragraphs in English and Korean (sent1 and sent2) with a binary labels column indicating whether the paragraphs describe the same entity (1) or different entities (0).