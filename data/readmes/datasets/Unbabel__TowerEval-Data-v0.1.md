---
language:
- en
- de
- fr
- zh
- pt
- nl
- ru
- ko
- it
- es
size_categories:
- 10K<n<100K
task_categories:
- translation
- text-generation
---

# Dataset Card for TowerEval-Data

TowerEval-Data is the suite of datasets used to evaluate [Tower](https://huggingface.co/collections/Unbabel/tower-7b-v01-659eaedfe36e6dd29eb1805c), language models specialized for translation tasks such as machine translation (e.g. general, document, terminology-aware or context-aware translation), automatic post edition, named-entity recognition, gramatical error correction, and paraphrase generation.

For generation and evaluation code, see our repo [`tower-eval`](https://github.com/deep-spin/tower-eval).

- **Curated by:** Unbabel, Instituto Superior Técnico, CentraleSupélec, University of Paris-Saclay;
- **Language(s) (NLP):** English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese, Russian;
- **License:** TowerEval contains data from many sources. We refer to the respective data sources below for information regarding licensing of the data.


## Dataset Details

TowerEval contains 0- and few-shot instructions created and corresponding raw data from the following sources:

| Data Source | Task(s) | 
| -------------- | ----------- | 
| [Flores](https://github.com/facebookresearch/flores) | General Translation |
| [WMT23](https://www2.statmt.org/wmt23/translation-task.html#_data) | General Translation |
| [TICO-19](https://tico-19.github.io/) | Domain-specific Translation |
| [WMT23](https://www2.statmt.org/wmt23/translation-task.html#_data) | Automatic Post Edition (NLLB 3B translations on WMT23 test data) |
| [MultiCoNER II](https://multiconer.github.io/) | Named Entity Recognition (1000 randomly selected test instances) |
| [CoNLL-2014](https://www.comp.nus.edu.sg/~nlp/conll14st.html) | Grammatical Error Correction |
| [COWS-L2H](https://github.com/abhisaary/spanish_gec) | Grammatical Error Correction |
| [mlconvgec2018](https://github.com/adrianeboyd/boyd-wnut2018/) | Grammatical Error Correction |

## Intended uses and limitations

TowerEval-Data is intended to be used to evaluate large language models on translation and related tasks.
Check out our [repo](https://github.com/deep-spin/tower-eval) for details on how to use the data.

## Citation 

```bibtex
@misc{tower_llm_2024,
      title={Tower: An Open Multilingual Large Language Model for Translation-Related Tasks}, 
      author={Duarte M. Alves and José Pombal and Nuno M. Guerreiro and Pedro H. Martins and João Alves and Amin Farajian and Ben Peters and Ricardo Rei and Patrick Fernandes and Sweta Agrawal and Pierre Colombo and José G. C. de Souza and André F. T. Martins},
      year={2024},
      eprint={2402.17733},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```