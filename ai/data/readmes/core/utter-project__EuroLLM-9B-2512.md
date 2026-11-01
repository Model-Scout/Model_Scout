---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
library_name: transformers
---

# Model Card for EuroLLM-9B-2512

This is the model card for EuroLLM-9B-2512, an improved version of [utter-project/EuroLLM-9B](https://huggingface.co/utter-project/EuroLLM-9B).
In comparison with the previous version, this version includes the long-context extension phase from [utter-project/EuroLLM-22B](https://huggingface.co/utter-project/EuroLLM-22B-2512).

- **Developed by:** Instituto Superior Técnico - University of Lisbon, Instituto de Telecomunicações, University of Edinburgh, Aveni, Unbabel, University of Paris-Saclay, Artefact Research Center, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 9B parameter multilingual transfomer LLM.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

## Bias, Risks, and Limitations

This model has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).

## Citation
If you use our work, please cite:
```
@misc{ramos2026eurollm22btechnicalreport,
      title={EuroLLM-22B: Technical Report}, 
      author={Miguel Moura Ramos and Duarte M. Alves and Hippolyte Gisserot-Boukhlef and João Alves and Pedro Henrique Martins and Patrick Fernandes and José Pombal and Nuno M. Guerreiro and Ricardo Rei and Nicolas Boizard and Amin Farajian and Mateusz Klimaszewski and José G. C. de Souza and Barry Haddow and François Yvon and Pierre Colombo and Alexandra Birch and André F. T. Martins},
      year={2026},
      eprint={2602.05879},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.05879}, 
}
```