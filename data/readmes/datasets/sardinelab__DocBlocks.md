---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: sources
    dtype: string
  - name: references
    dtype: string
  - name: language_pair
    dtype: string
  - name: dataset
    dtype: string
  splits:
  - name: train
    num_bytes: 14008918721
    num_examples: 241828
  download_size: 7996471024
  dataset_size: 14008918721
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
task_categories:
- translation
language:
- en
- de
- es
- fr
- it
- ko
- nl
- pt
- ru
- zh
size_categories:
- 100K<n<1M
---
# Dataset Card for DocBlocks

DocBlocks is a high-quality, multilingual document-level machine translation (MT) dataset designed to fine-tune large language models (LLMs) on long-context translation tasks. Unlike traditional sentence-level datasets, it contains full documents with natural discourse structures and contextual alignment, helping models maintain coherence, consistency, and high translation quality across longer texts.

- **Curated by:** Instituto Superior Técnico, Instituto de Telecomunicações, Carnegie Mellon University and Unbabel;
- **Language(s) (NLP):** English, German, Spanish, French, Italian, Dutch, Portuguese, Russian, Korean, Chinese;
- **License:** DocBlocks includes data from the following sources: **IWSLT**, **Europarl**, **News Commentary**, **GuoFeng**, and **BWB**. For licensing information, please refer to the official documentation or websites of each source.

### Dataset Details

* `conversations` - The user and assistant dialogue turns, following an instruction-based format suitable for LLM fine-tuning;
* `sources` - The original source text in the source language;
* `references` - The human-translated target/reference text in the target language;
* `language_pair` - The language direction of the translation pair;
* `dataset` - The name of the original dataset from which the document was sourced.

## Bias, Risks, and Limitations

DocBlocks may reflect linguistic, cultural, and domain biases from its source corpora, and its performance is influenced by language coverage and document structure variability.


## Citation
```bibtex
@misc{multilingual_contextualization_llm_2025,
      title={Multilingual Contextualization of Large Language Models for Document-Level Machine Translation}, 
      author={Miguel Moura Ramos and Patrick Fernandes and Sweta Agrawal and André F. T. Martins},
      year={2025},
      eprint={2504.12140},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.12140}, 
}
```