---
language:
- ko

license: mit
task_categories:
- question-answering
dataset_info:
  features:
  - name: 'Unnamed: 0'
    dtype: int64
  - name: Question
    dtype: string
  - name: A
    dtype: string
  - name: B
    dtype: string
  - name: C
    dtype: string
  - name: D
    dtype: string
  - name: Answer
    dtype: string
  - name: Subject
    dtype: string
---

# MMMLU_KOREAN

this dataset is korean subset of [openai/MMMLU](https://huggingface.co/datasets/openai/MMMLU) dataset.









---

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
* ZH_CH (Simplied Chinese)

## Sources

Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., & Steinhardt, J. (2021). [*Measuring Massive Multitask Language Understanding*](https://arxiv.org/abs/2009.03300).

[OpenAI Simple Evals GitHub Repository](https://github.com/openai/simple-evals)