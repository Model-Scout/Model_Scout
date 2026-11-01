---
dataset_info:
  features:
  - name: example_tags
    list: string
  - name: ideal_completions_data
    struct:
    - name: ideal_completion
      dtype: string
    - name: ideal_completions_group
      dtype: string
    - name: ideal_completions_ref_completions
      list: string
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: prompt_id
    dtype: string
  - name: rubrics
    list:
    - name: criterion
      dtype: string
    - name: points
      dtype: int64
    - name: tags
      list: string
  - name: canary
    dtype: string
configs:
- config_name: Amharic
  data_files:
  - split: test
    path: data/Amharic-*

- config_name: Arabic
  data_files:
  - split: test
    path: data/Arabic-*

- config_name: Bengali
  data_files:
  - split: test
    path: data/Bengali-*

- config_name: Brazilian_Portuguese
  data_files:
  - split: test
    path: data/Brazilian_Portuguese-*

- config_name: Dutch
  data_files:
  - split: test
    path: data/Dutch-*

- config_name: English_original
  data_files:
  - split: test
    path: data/English_original-*

- config_name: Estonian
  data_files:
  - split: test
    path: data/Estonian-*

- config_name: Finnish
  data_files:
  - split: test
    path: data/Finnish-*

- config_name: French
  data_files:
  - split: test
    path: data/French-*

- config_name: German
  data_files:
  - split: test
    path: data/German-*

- config_name: Hausa
  data_files:
  - split: test
    path: data/Hausa-*

- config_name: Hindi
  data_files:
  - split: test
    path: data/Hindi-*

- config_name: Indonesian
  data_files:
  - split: test
    path: data/Indonesian-*

- config_name: Italian
  data_files:
  - split: test
    path: data/Italian-*

- config_name: Japanese
  data_files:
  - split: test
    path: data/Japanese-*

- config_name: Korean
  data_files:
  - split: test
    path: data/Korean-*

- config_name: Latvian
  data_files:
  - split: test
    path: data/Latvian-*

- config_name: Lithuanian
  data_files:
  - split: test
    path: data/Lithuanian-*

- config_name: Malay
  data_files:
  - split: test
    path: data/Malay-*

- config_name: Norwegian
  data_files:
  - split: test
    path: data/Norwegian-*

- config_name: Persian
  data_files:
  - split: test
    path: data/Persian-*
    
- config_name: Polish
  data_files:
  - split: test
    path: data/Polish-*

- config_name: Russian
  data_files:
  - split: test
    path: data/Russian-*

- config_name: Simplified_Chinese
  data_files:
  - split: test
    path: data/Simplified_Chinese-*

- config_name: Somali
  data_files:
  - split: test
    path: data/Somali-*

- config_name: Spanish
  data_files:
  - split: test
    path: data/Spanish-*

- config_name: Swahili
  data_files:
  - split: test
    path: data/Swahili-*

- config_name: Swedish
  data_files:
  - split: test
    path: data/Swedish-*

- config_name: Thai
  data_files:
  - split: test
    path: data/Thai-*

- config_name: Turkish
  data_files:
  - split: test
    path: data/Turkish-*

- config_name: Ukrainian
  data_files:
  - split: test
    path: data/Ukrainian-*

- config_name: Urdu
  data_files:
  - split: test
    path: data/Urdu-*

- config_name: Vietnamese
  data_files:
  - split: test
    path: data/Vietnamese-*
license: mit
language:
- am
- bn
- pt
- en
- fi
- fr
- de
- ha
- hi
- id
- ja
- ko
- 'no'
- zh
- es
- sw
- sv
- th
- tr
- ur
- vi
- it
- et
- lv
- lt
- ms
- fa
- nl
- pl
- ru
- so
- uk
- ar
tags:
- medical
- biology
size_categories:
- 100K<n<1M
task_categories:
- text-generation
pretty_name: HealthBench Multilingual
---

<p align="center">
  <img src="https://huggingface.co/datasets/projetogabi/healthbench-multilingual/resolve/main/splash.png" width="100%" style="border-radius: 16px;">
</p>



# HealthBench Multilingual

Part of the **AEGIS-1** collection: a large-scale effort to translate key medical AI datasets into underrepresented languages to advance global health data equity.

## Dataset Summary

This dataset is a multilingual translation of [HealthBench](https://openai.com/index/healthbench/), OpenAI's medical AI evaluation benchmark, covering **32 languages**. The original HealthBench consists of 5,000 realistic multi-turn clinical conversations and more than 48,000 physician-authored rubric criteria designed to evaluate how well AI systems respond to health questions from both patients and clinicians.

HealthBench Multilingual makes this benchmark accessible across a wide range of languages — including several that are severely underrepresented in medical NLP research, such as Amharic, Hausa, Swahili, and Urdu — to support the development and evaluation of AI systems that serve global populations.

## How to Use
```python
from datasets import load_dataset

language = "French"
dataset_handle = "projetogabi/healthbench-multilingual"

dataset = load_dataset(dataset_handle, language, split = "test")
```


## Why This Dataset Exists

The vast majority of medical AI benchmarks are English-only. This creates a compounding problem: models trained and evaluated primarily on English data perform worse for speakers of other languages, and those performance gaps are hardest to detect because the evaluation tooling itself is English-centric.

AEGIS-1 is a direct response to this gap. By translating high-quality, physician-validated benchmarks into languages spoken across Africa, Asia, the Middle East, Latin America, and Europe, AEGIS-1 enables:

- **Evaluation** of multilingual and language-specific medical AI models
- **Fine-tuning** data for models targeting non-English health contexts
- **Research** into cross-lingual transfer in the medical domain
- **Benchmarking** health equity across language communities

## Source Dataset

| Field | Details |
|---|---|
| **Original dataset** | [HealthBench](https://openai.com/index/healthbench/) by OpenAI |
| **Original size** | 5,000 multi-turn clinical conversations |
| **Rubric criteria** | 48,562+ physician-authored evaluation criteria |
| **Physician contributors** | 262 physicians across 60 countries |
| **Original languages** | English |
| **Format** | Multi-turn conversations (user + assistant turns) with graded rubric criteria |

HealthBench was designed to be **meaningful** (reflecting real-world use cases), **reliable** (grounded in physician judgment), and **unsaturated** (hard enough that even state-of-the-art models have room to improve).

## Languages

This dataset covers 33 languages (1 original + 32 translated):

| Language   | Code | Region                          |
| ---------- | ---- | ------------------------------- |
| Amharic    | `am` | East Africa                     |
| Arabic     | `ar` | Middle East / North Africa      |
| Bengali    | `bn` | South Asia                      |
| Chinese    | `zh` | East Asia                       |
| Dutch      | `nl` | Western Europe                  |
| English    | `en` | Global                          |
| Estonian   | `et` | Northern Europe                 |
| Finnish    | `fi` | Northern Europe                 |
| French     | `fr` | Europe / West & Central Africa  |
| German     | `de` | Central Europe                  |
| Hausa      | `ha` | West Africa                     |
| Hindi      | `hi` | South Asia                      |
| Indonesian | `id` | Southeast Asia                  |
| Italian    | `it` | Southern Europe                 |
| Japanese   | `ja` | East Asia                       |
| Korean     | `ko` | East Asia                       |
| Latvian    | `lv` | Northern Europe                 |
| Lithuanian | `lt` | Northern Europe                 |
| Malay      | `ms` | Southeast Asia                  |
| Norwegian  | `no` | Northern Europe                 |
| Persian    | `fa` | Middle East / Central Asia      |
| Polish     | `pl` | Central Europe                  |
| Portuguese | `pt` | Europe / Latin America / Africa |
| Russian    | `ru` | Eastern Europe / Northern Asia  |
| Somali     | `so` | East Africa                     |
| Spanish    | `es` | Europe / Latin America          |
| Swahili    | `sw` | East / Central Africa           |
| Swedish    | `sv` | Northern Europe                 |
| Thai       | `th` | Southeast Asia                  |
| Turkish    | `tr` | Western Asia / Eastern Europe   |
| Ukrainian  | `uk` | Eastern Europe                  |
| Urdu       | `ur` | South Asia                      |
| Vietnamese | `vi` | Southeast Asia                  |



## Intended Uses

### Suitable Uses
- Evaluating multilingual medical LLMs against physician-validated criteria
- Fine-tuning language models on medical conversation data in non-English languages
- Cross-lingual transfer learning research in the clinical domain
- Studying health information disparities across language communities

### Out-of-Scope Uses
- **Not for clinical decision-making.** This is a research benchmark. Nothing in this dataset should be used as medical advice.
- **Not a replacement for native clinical data.** Translated benchmarks complement but do not substitute for datasets collected natively in each target language.

## Limitations

- **Translation artifacts.** Machine translation of medical text is imperfect. Nuanced clinical language, idioms, and culturally specific health concepts may not translate perfectly.
- **Cultural context.** Clinical norms, terminology, and patient-provider communication styles vary across cultures. Translated conversations may not fully reflect these differences.
- **Rubric transferability.** Physician rubric criteria were authored in an English-language medical context. Their applicability may vary for clinicians operating in different healthcare systems.
- **Underrepresented languages.** While AEGIS-1 prioritizes low-resource languages, the quality of translation for certain languages may be lower than for high-resource languages due to limited model support.

## Ethics & Responsible Use

HealthBench was constructed using synthetic and adversarially-generated conversations — no real patient data was used.

Users of this dataset should be aware that:
- AI systems evaluated on this benchmark may still produce harmful or incorrect health information
- Benchmark performance does not guarantee clinical safety or efficacy
- Medical AI systems should always be validated with domain experts before deployment

## Citation

If you use this dataset, please cite both AEGIS-1 and the original HealthBench:

```bibtex
@article{daddario2026aegis1,
  title   = {AEGIS-1: A Context-Aware Translated Medical Dataset for Global Health Data Equity},
  author  = {D'addario, Andrew},
  year    = {2026},
  month   = feb,
  journal = {arXiv preprint arXiv:XXXX.XXXXX},
  url     = {https://arxiv.org/abs/XXXX.XXXXX}
}

@techreport{arora2025healthbench,
  title       = {HealthBench: Evaluating Large Language Models Towards Improved Human Health},
  author      = {Arora, Rahul K. and Wei, Jason and {Soskin Hicks}, Rebecca and Bowman, Preston
                 and {Qui{\~n}onero-Candela}, Joaquin and Tsimpourlas, Foivos and Sharman, Michael
                 and Shah, Meghan and Vallone, Andrea and Beutel, Alex and Heidecke, Johannes
                 and Singhal, Karan},
  institution = {OpenAI},
  year        = {2025},
  url         = {https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf}
}
```

## Part of AEGIS-1

This dataset is one component of the broader **AEGIS-1** collection, which translates multiple medical AI datasets into underrepresented languages. See the [AEGIS-1 collection](#) for the full list of datasets and source benchmarks.