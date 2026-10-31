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
    path: test/mmlu_AR-XY*.csv
- config_name: BN_BD
  data_files:
  - split: test
    path: test/mmlu_BN-BD*.csv
- config_name: DE_DE
  data_files:
  - split: test
    path: test/mmlu_DE-DE*.csv
- config_name: ES_LA
  data_files:
  - split: test
    path: test/mmlu_ES-LA*.csv
- config_name: FR_FR
  data_files:
  - split: test
    path: test/mmlu_FR-FR*.csv
- config_name: HI_IN
  data_files:
  - split: test
    path: test/mmlu_HI-IN*.csv
- config_name: ID_ID
  data_files:
  - split: test
    path: test/mmlu_ID-ID*.csv
- config_name: IT_IT
  data_files:
  - split: test
    path: test/mmlu_IT-IT*.csv
- config_name: JA_JP
  data_files:
  - split: test
    path: test/mmlu_JA-JP*.csv
- config_name: KO_KR
  data_files:
  - split: test
    path: test/mmlu_KO-KR*.csv
- config_name: PT_BR
  data_files:
  - split: test
    path: test/mmlu_PT-BR*.csv
- config_name: SW_KE
  data_files:
  - split: test
    path: test/mmlu_SW-KE*.csv
- config_name: YO_NG
  data_files:
  - split: test
    path: test/mmlu_YO-NG*.csv
- config_name: ZH_CN
  data_files:
  - split: test
    path: test/mmlu_ZH-CN*.csv
- config_name: STEM
  data_files:
  - split: test
    path: test/*STEM.csv
- config_name: humanities
  data_files:
  - split: test
    path: test/*humanities.csv
- config_name: social_sciences
  data_files:
  - split: test
    path: test/*social_sciences.csv
- config_name: other
  data_files:
  - split: test
    path: test/*other.csv
- config_name: AR_XY_STEM
  data_files:
  - split: test
    path: test/mmlu_AR-XY_STEM.csv
- config_name: AR_XY_humanities
  data_files:
  - split: test
    path: test/mmlu_AR-XY_humanities.csv
- config_name: AR_XY_social_sciences
  data_files:
  - split: test
    path: test/mmlu_AR-XY_social_sciences.csv
- config_name: AR_XY_other
  data_files:
  - split: test
    path: test/mmlu_AR-XY_other.csv
- config_name: SW_KE_STEM
  data_files:
  - split: test
    path: test/mmlu_SW-KE_STEM.csv
- config_name: SW_KE_humanities
  data_files:
  - split: test
    path: test/mmlu_SW-KE_humanities.csv
- config_name: SW_KE_social_sciences
  data_files:
  - split: test
    path: test/mmlu_SW-KE_social_sciences.csv
- config_name: SW_KE_other
  data_files:
  - split: test
    path: test/mmlu_SW-KE_other.csv
- config_name: ES_LA_STEM
  data_files:
  - split: test
    path: test/mmlu_ES-LA_STEM.csv
- config_name: ES_LA_humanities
  data_files:
  - split: test
    path: test/mmlu_ES-LA_humanities.csv
- config_name: ES_LA_social_sciences
  data_files:
  - split: test
    path: test/mmlu_ES-LA_social_sciences.csv
- config_name: ES_LA_other
  data_files:
  - split: test
    path: test/mmlu_ES-LA_other.csv
- config_name: IT_IT_STEM
  data_files:
  - split: test
    path: test/mmlu_IT-IT_STEM.csv
- config_name: IT_IT_humanities
  data_files:
  - split: test
    path: test/mmlu_IT-IT_humanities.csv
- config_name: IT_IT_social_sciences
  data_files:
  - split: test
    path: test/mmlu_IT-IT_social_sciences.csv
- config_name: IT_IT_other
  data_files:
  - split: test
    path: test/mmlu_IT-IT_other.csv
- config_name: DE_DE_STEM
  data_files:
  - split: test
    path: test/mmlu_DE-DE_STEM.csv
- config_name: DE_DE_humanities
  data_files:
  - split: test
    path: test/mmlu_DE-DE_humanities.csv
- config_name: DE_DE_social_sciences
  data_files:
  - split: test
    path: test/mmlu_DE-DE_social_sciences.csv
- config_name: DE_DE_other
  data_files:
  - split: test
    path: test/mmlu_DE-DE_other.csv
- config_name: ZH_CN_STEM
  data_files:
  - split: test
    path: test/mmlu_ZH-CN_STEM.csv
- config_name: ZH_CN_humanities
  data_files:
  - split: test
    path: test/mmlu_ZH-CN_humanities.csv
- config_name: ZH_CN_social_sciences
  data_files:
  - split: test
    path: test/mmlu_ZH-CN_social_sciences.csv
- config_name: ZH_CN_other
  data_files:
  - split: test
    path: test/mmlu_ZH-CN_other.csv
- config_name: BN_BD_STEM
  data_files:
  - split: test
    path: test/mmlu_BN-BD_STEM.csv
- config_name: BN_BD_humanities
  data_files:
  - split: test
    path: test/mmlu_BN-BD_humanities.csv
- config_name: BN_BD_social_sciences
  data_files:
  - split: test
    path: test/mmlu_BN-BD_social_sciences.csv
- config_name: BN_BD_other
  data_files:
  - split: test
    path: test/mmlu_BN-BD_other.csv
- config_name: HI_IN_STEM
  data_files:
  - split: test
    path: test/mmlu_HI-IN_STEM.csv
- config_name: HI_IN_humanities
  data_files:
  - split: test
    path: test/mmlu_HI-IN_humanities.csv
- config_name: HI_IN_social_sciences
  data_files:
  - split: test
    path: test/mmlu_HI-IN_social_sciences.csv
- config_name: HI_IN_other
  data_files:
  - split: test
    path: test/mmlu_HI-IN_other.csv
- config_name: FR_FR_STEM
  data_files:
  - split: test
    path: test/mmlu_FR-FR_STEM.csv
- config_name: FR_FR_humanities
  data_files:
  - split: test
    path: test/mmlu_FR-FR_humanities.csv
- config_name: FR_FR_social_sciences
  data_files:
  - split: test
    path: test/mmlu_FR-FR_social_sciences.csv
- config_name: FR_FR_other
  data_files:
  - split: test
    path: test/mmlu_FR-FR_other.csv
- config_name: ID_ID_STEM
  data_files:
  - split: test
    path: test/mmlu_ID-ID_STEM.csv
- config_name: ID_ID_humanities
  data_files:
  - split: test
    path: test/mmlu_ID-ID_humanities.csv
- config_name: ID_ID_social_sciences
  data_files:
  - split: test
    path: test/mmlu_ID-ID_social_sciences.csv
- config_name: ID_ID_other
  data_files:
  - split: test
    path: test/mmlu_ID-ID_other.csv
- config_name: KO_KR_STEM
  data_files:
  - split: test
    path: test/mmlu_KO-KR_STEM.csv
- config_name: KO_KR_humanities
  data_files:
  - split: test
    path: test/mmlu_KO-KR_humanities.csv
- config_name: KO_KR_social_sciences
  data_files:
  - split: test
    path: test/mmlu_KO-KR_social_sciences.csv
- config_name: KO_KR_other
  data_files:
  - split: test
    path: test/mmlu_KO-KR_other.csv
- config_name: YO_NG_STEM
  data_files:
  - split: test
    path: test/mmlu_YO-NG_STEM.csv
- config_name: YO_NG_humanities
  data_files:
  - split: test
    path: test/mmlu_YO-NG_humanities.csv
- config_name: YO_NG_social_sciences
  data_files:
  - split: test
    path: test/mmlu_YO-NG_social_sciences.csv
- config_name: YO_NG_other
  data_files:
  - split: test
    path: test/mmlu_YO-NG_other.csv
- config_name: JA_JP_STEM
  data_files:
  - split: test
    path: test/mmlu_JA-JP_STEM.csv
- config_name: JA_JP_humanities
  data_files:
  - split: test
    path: test/mmlu_JA-JP_humanities.csv
- config_name: JA_JP_social_sciences
  data_files:
  - split: test
    path: test/mmlu_JA-JP_social_sciences.csv
- config_name: JA_JP_other
  data_files:
  - split: test
    path: test/mmlu_JA-JP_other.csv
- config_name: PT_BR_STEM
  data_files:
  - split: test
    path: test/mmlu_PT-BR_STEM.csv
- config_name: PT_BR_humanities
  data_files:
  - split: test
    path: test/mmlu_PT-BR_humanities.csv
- config_name: PT_BR_social_sciences
  data_files:
  - split: test
    path: test/mmlu_PT-BR_social_sciences.csv
- config_name: PT_BR_other
  data_files:
  - split: test
    path: test/mmlu_PT-BR_other.csv

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

# About MMMLU subset
  This is a subset of MMMLU, specifically, we sampled 10% of the original data to improve evaluation efficiency.
  In addition, we categorize the questions into four categories by subject, i.e., STEM, HUMANITIES, SOCIAL SCIENCES, and OTHER, aligned with [MMLU](https://huggingface.co/datasets/cais/mmlu).

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