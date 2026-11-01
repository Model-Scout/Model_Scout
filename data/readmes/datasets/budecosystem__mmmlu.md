---
task_categories:
- question-answering
configs:
- config_name: default
  data_files:
  - split: test
    path: test/*.csv
- config_name: AR_XY
  data_files:
  - split: test
    path: test/mmlu_AR-XY.csv
- config_name: BN_BD
  data_files:
  - split: test
    path: test/mmlu_BN-BD.csv
- config_name: DE_DE
  data_files:
  - split: test
    path: test/mmlu_DE-DE.csv
- config_name: ES_LA
  data_files:
  - split: test
    path: test/mmlu_ES-LA.csv
- config_name: FR_FR
  data_files:
  - split: test
    path: test/mmlu_FR-FR.csv
- config_name: HI_IN
  data_files:
  - split: test
    path: test/mmlu_HI-IN.csv
- config_name: ID_ID
  data_files:
  - split: test
    path: test/mmlu_ID-ID.csv
- config_name: IT_IT
  data_files:
  - split: test
    path: test/mmlu_IT-IT.csv
- config_name: JA_JP
  data_files:
  - split: test
    path: test/mmlu_JA-JP.csv
- config_name: KO_KR
  data_files:
  - split: test
    path: test/mmlu_KO-KR.csv
- config_name: PT_BR
  data_files:
  - split: test
    path: test/mmlu_PT-BR.csv
- config_name: SW_KE
  data_files:
  - split: test
    path: test/mmlu_SW-KE.csv
- config_name: YO_NG
  data_files:
  - split: test
    path: test/mmlu_YO-NG.csv
- config_name: ZH_CN
  data_files:
  - split: test
    path: test/mmlu_ZH-CN.csv
language:
- ar
- bn
- de
- es
- fr
- hi
- id
- it
- ja
- ko
- pt
- sw
- yo
- zh
license: mit
---

> **Bud Ecosystem mirror** of [`openai/MMMLU`](https://huggingface.co/datasets/openai/MMMLU) — a verbatim copy for offline, reproducible model evaluation. License **unchanged (MIT)**; all rights remain with the original authors.

# Multilingual Massive Multitask Language Understanding (MMMLU)

The MMLU is a widely recognized benchmark of general knowledge attained by AI models. It covers a broad range of topics from 57 different categories, covering elementary-level knowledge up to advanced professional subjects like law, physics, history, and computer science.

We translated the MMLU’s test set into 14 languages using professional human translators. Relying on human translators for this evaluation increases confidence in the accuracy of the translations, especially for low-resource languages like Yoruba. We are publishing the professional human translations and the code we use to run the evaluations.

This effort reflects our commitment to improving the multilingual capabilities of AI models, ensuring they perform accurately across languages, particularly for underrepresented communities. By prioritizing high-quality translations, we aim to make AI technology more inclusive and effective for users worldwide.

## Locales

MMMLU contains the MMLU test set translated into the following locales:
* AR_XY (Arabic)
* BN_BD (Bengali)
* DE_DE (German)
* ES_LA (Spanish)
* FR_FR (French)
* HI_IN (Hindi)
* ID_ID (Indonesian)
* IT_IT (Italian)
* JA_JP (Japanese)
* KO_KR (Korean)
* PT_BR (Brazilian Portuguese)
* SW_KE (Swahili)
* YO_NG (Yoruba)
* ZH_CN (Simplified Chinese)

## Sources

Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., & Steinhardt, J. (2021). [*Measuring Massive Multitask Language Understanding*](https://arxiv.org/abs/2009.03300).

[OpenAI Simple Evals GitHub Repository](https://github.com/openai/simple-evals)