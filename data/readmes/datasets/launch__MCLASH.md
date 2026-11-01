---
language:
- en
- es
- hi
- ko
- ms
- zh
license: mit
size_categories:
- 1K<n<10K
task_categories:
- text-classification
- text-generation
configs:
- config_name: English
  default: true
  data_files:
  - split: test
    path: dataset_final_en.csv
- config_name: Spanish
  data_files:
  - split: test
    path: dataset_final_es.csv
- config_name: Hindi
  data_files:
  - split: test
    path: dataset_final_hi.csv
- config_name: Malay
  data_files:
  - split: test
    path: dataset_final_ms.csv
- config_name: Korean
  data_files:
  - split: test
    path: dataset_final_ko.csv
- config_name: Chinese
  data_files:
  - split: test
    path: dataset_final_zh-CN.csv
- config_name: Values
  data_files:
  - split: test
    path: wvs_values.txt
---

# MCLASH: Multilingual CLASH

[Paper](https://huggingface.co/papers/2607.11736) | [Code](https://github.com/aylee2008/met)

MCLASH is the multilingual extension of [CLASH](https://huggingface.co/datasets/launch/CLASH) (**C**haracter perspective-based **L**LM **A**ssessments in **S**ituations with **H**igh-stakes), a benchmark of long-form, human-written high-stakes dilemmas evaluated from multiple character perspectives. MCLASH carries the same dilemmas and character-perspective methodology into 5 additional languages — Spanish, Hindi, Korean, Malay, and Chinese.

See [CLASH dataset card](https://huggingface.co/datasets/launch/CLASH) for detailed explanation of the dataset structure and ground-truth answer format.

Note: MCLASH covers only the **static** character-perspective categories (*Straightforward, Simple Contrast, Swayed Contrast*) from CLASH. The **dynamic** (temporal value-shift) categories (*Shift, Half-Shift, False-Shift*) were not adapted and remain English-only.

### Cultural Adaptation, Not Direct Translation

Existing multilingual moral-dilemma benchmarks are built by directly translating English scenarios, which leaves U.S.-centric named entities untouched, importing improper cultural context into the target language. For example, a scenario mentioning "Amazon," the American big-tech company, would remain "Amazon" under direct translation even when adapted for a Korean audience, where a comparable dilemma would more plausibly involve a local company like Naver or Kakao. To avoid this, **each CLASH scenario was adapted rather than translated**: we use Qwen3-32B for initial adaptation and then carefully inspect the results with human inspectors.

### Citation

If you use this, please cite:

```bibtex
@article{lee2026met,
  title={MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning},
  author={Lee, Ayoung and Kwon, Ryan and Zhang, Yunxiang and Liu, Yuxuan and Railton, Peter and Wang, Lu},
  journal={arXiv preprint arXiv:2607.11736},
  year={2026}
}
```