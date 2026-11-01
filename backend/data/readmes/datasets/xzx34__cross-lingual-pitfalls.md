---
license: mit
task_categories:
- question-answering
- multiple-choice
language:
- en
- zh
- ja
- ko
- fr
- es
- it
- uk
- de
- bn
- hi
- ar
- he
- am
- yo
- sw
- zu
tags:
- multilingual
- cross-lingual
- llm-evaluation
- benchmark
- multilingual-llm
- cross-lingual-consistency
- cross-lingual-weakness
- multilingual-evaluation
- automatic-probing
- failure-discovery
- search-based-evaluation
- adversarial-evaluation
- multilingual-post-training
- arxiv:2505.18673
pretty_name: 'Cross-Lingual Pitfalls: Multilingual LLM Failure Probes'
size_categories:
- 1K<n<10K
configs:
- config_name: Chinese
  data_files: data/Chinese.json
- config_name: Japanese
  data_files: data/Japanese.json
- config_name: Korean
  data_files: data/Korean.json
- config_name: French
  data_files: data/French.json
- config_name: Spanish
  data_files: data/Spanish.json
- config_name: Italian
  data_files: data/Italian.json
- config_name: Ukrainian
  data_files: data/Ukrainian.json
- config_name: German
  data_files: data/German.json
- config_name: Bengali
  data_files: data/Bengali.json
- config_name: Hindi
  data_files: data/Hindi.json
- config_name: Arabic
  data_files: data/Arabic.json
- config_name: Hebrew
  data_files: data/Hebrew.json
- config_name: Amharic
  data_files: data/Amharic.json
- config_name: Yoruba
  data_files: data/Yoruba.json
- config_name: Swahili
  data_files: data/Swahili.json
- config_name: Zulu
  data_files: data/Zulu.json
---

# Cross-Lingual Pitfalls

**Cross-Lingual Pitfalls** is a fixed, failure-focused dataset from the ACL 2025 paper *"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models."* It contains **6,713 bilingual English-to-target-language question pairs across 16 target languages**. The paper's search-based multilingual LLM evaluation method uses beam search and LLM-based simulation to discover cases where a model answers correctly in English but fails on a semantically checked target-language version.

Unlike a fixed benchmark used only to estimate average multilingual accuracy, the generation method actively searches for cross-lingual consistency failures. **This published dataset is a fixed snapshot, not a continuously updated benchmark.** Results on these selected questions are diagnostic and should not be read as population-wide performance estimates for a language.

- 🌐 Project page: https://xzx34.github.io/cross-lingual-pitfalls/
- 📄 Paper (ACL Anthology): https://aclanthology.org/2025.acl-long.404/
- 💻 Code & Data: https://github.com/xzx34/Cross-Lingual-Pitfalls
- 📄 arXiv: https://arxiv.org/abs/2505.18673

## Dataset summary

The pairs are produced by automatic probing (beam search + LLM-based simulation) to expose English-correct, target-language-wrong cases. On these **selected failure-focused pairs**, English accuracy is near-perfect while most evaluated models show target-language accuracy drops of **over 50%** in the paper's setting. Particularly large gaps occur in the tested low-resource languages. These results do not estimate average model accuracy on all questions from those languages.

The dataset probes multilingual question answering and cross-lingual consistency. It is not a benchmark for cultural knowledge, code-switching, translation quality, safety, or agent tool use. The generation method can be rerun for different model settings; the files released here do not change automatically.

### Languages and pair counts (16 languages, 6,713 pairs)

| Language | Pairs | Language | Pairs |
|---|---|---|---|
| Chinese | 342 | Hindi | 327 |
| Japanese | 314 | Arabic | 424 |
| Korean | 456 | Hebrew | 319 |
| French | 312 | Amharic | 665 |
| Spanish | 242 | Yoruba | 813 |
| Italian | 295 | Swahili | 417 |
| Ukrainian | 323 | Zulu | 711 |
| German | 322 | Bengali | 431 |
| | | **Total** | **6,713** |

In the paper's evaluation on selected pairs, Amharic, Yoruba, Swahili, and Zulu show particularly large cross-lingual gaps.

### Source benchmarks

Each pair originates from one of five English QA benchmarks (recorded in the `source` field):

| Source | Pairs |
|---|---|
| MMLU | 1,684 |
| SciQ | 1,616 |
| CommonsenseQA | 1,604 |
| ARC | 962 |
| TruthfulQA | 847 |

## Data fields

Each record contains the English source question and answer, the target-language `question`, `choices`, and `answer`, the originating benchmark (`source`), the subject `category`, and the intermediate perturbation / translation / scoring fields used by the generation pipeline (e.g. `oriquestion`, `transquestion`, `rate_ori`, `rate_trans`).

## Usage

```python
from datasets import load_dataset

# load a single language
ds = load_dataset("xzx34/cross-lingual-pitfalls", "Chinese")
```

## License & source data

The released questions and accompanying code are distributed under the **MIT license**, matching the [code repository](https://github.com/xzx34/Cross-Lingual-Pitfalls). Items are derived from MMLU, ARC, CommonsenseQA, TruthfulQA, and SciQ; downstream use is additionally subject to the terms of those upstream datasets.

## Citation

```bibtex
@inproceedings{xu-etal-2025-cross,
    title = "Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models",
    author = "Xu, Zixiang  and Wang, Yanbo  and Huang, Yue  and Chen, Xiuying  and Zhao, Jieyu  and Jiang, Meng  and Zhang, Xiangliang",
    editor = "Che, Wanxiang  and Nabende, Joyce  and Shutova, Ekaterina  and Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.404/",
    doi = "10.18653/v1/2025.acl-long.404",
    pages = "8254--8284",
    ISBN = "979-8-89176-251-0"
}
```
