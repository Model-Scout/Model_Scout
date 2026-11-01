---
language:
- ar
- hr
- sr
- bg
- ca
- zh
- cs
- da
- nl
- en
- et
- fi
- fr
- de
- he
- hi
- el
- hu
- id
- it
- ja
- ko
- lv
- lt
- 'no'
- pl
- pt
- ro
- ru
- sl
- sk
- es
- sw
- sv
- th
- tr
- uk
- vi
- cy
license: mit
task_categories:
- text-classification
pretty_name: RTP-LX
size_categories:
- 1K<n<10K
---

**WARNING: This repository contains and discusses content that is offensive or upsetting. All materials are intended to support research that improves toxicity detection methods. Included examples of toxicity do not represent how the authors or sponsors feel about any identity groups. This corpus was made by a multi-national, multi-cultural team of various faiths, beliefs, and origins. Please note that toxicity is dynamic, evolves with societal perceptions, and these labels may change.**

**Please note: we would very much rather have you _not_ train your models on this dataset. It's very toxic, and will contaminate the benchmarks. So pretty please, don't.**

**Another note: the file is password-protected. Check below for instructions on how to open it.**

# RTP-LX

RTP-LX (RealToxicityPrompts-Language eXpanded) is a human-translated, human-curated dataset multilingual set of 1k+ (per locale) toxic prompts and passages designed for toxicity evaluation. It is manually translated from a subset of the original RTP dataset, and annotated by native speakers. It also includes:

- Coverage in 38 languages (but more files because graphically-distinct dialects like ZH-Hans vs. ZH-Hant and DE-de vs. DE-ch are treated separately)
- Manually designed prompts that are considered "hard" to translate to English, and could be considered offensive in the language's geolocale.
- Translations may include dialect-specific indications (e.g., Levantine Arabic, Brazilian Portuguese)

## Languages covered
RTP-LX currently covers 38 languages:

- Arabic (Egyptian, Levantine, Saudi)
- BCMS
- Bulgarian*
- Catalan*
- Chinese (standard, simplified and standard, traditional)
- Czech
- Danish
- Dutch
- English
- Estonian*
- Finnish
- French (France)
- German (standard, Germany and standard, Switzerland*)
- Greek
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Korean
- Latvian*
- Lithuanian*
- Norwegian (Bokmål)
- Polish
- Portuguese (Brazilian, Portuguese)
- Romanian*
- Russian (Russia, Ukraine)
- Slovak*
- Slovenian*
- Spanish (Spain)
- Swahili
- Swedish
- Thai
- Turkish
- Ukrainian
- Vietnamese*
- Welsh*

The languages marked with an asterisk (*) do not contain Completions or the culturally-specific prompts (budgetary reasons)


## Harm Categories
RTP-LX is annotated in the following categories:

- Bias
- Insult
- Identity Attack
- Microagression
- Violence
- Self-harm
- Sexual content
- Overall toxicity


## Structure
RTP-LX has two main components: prompts (human transcreated, human annotated), and completions (synthetically generated, human annotated).

1. Prompts are meant to measure the effectiveness of your guardrails in multilingual scenarios, as well as automated annotation capabilities.
2. Completions, on the other hand, are much, much more toxic and are designed for ablation analysis of harm categories.
3. BenignCompletions are human-written completions -- perfect for DPO!
4. PromptAnnotations and CompletionsAnnotations contain the aggregated (majority vote) scores for the users.

## Uncompressing

To avoid crawlers, we have zipped and password-protected the entries. Please use the name of the dataset all in lowercase plus "-entries" and -4/8/24 as the password. So if the repo is "ASDF-BLAH", you want asdf-blah-entries-4/8/24.

## Misc

- For the full description (and the usually more up-to-date data, rubrics, code, etc), see [here](https://github.com/microsoft/RTP-LX)
- For the paper, see [here](https://arxiv.org/abs/2404.14397)

And here is the citation:

```
@article{rtplx,
    author = {Adrian de Wynter and Ishaan Watts and Tua Wongsangaroonsri and Minghui Zhang and Noura Farra and Nektar Ege Alt{\i}ntoprak and Lena Baur and Samantha Claudet and Pavel Gajdusek and Can G\"oren and Qilong Gu and Anna Kaminska and Tomasz Kaminski and Ruby Kuo and Akiko Kyuba and Jongho Lee and Kartik Mathur and Petter Merok and Ivana Milovanovi\'c and Nani Paananen and Vesa-Matti Paananen and Anna Pavlenko and Bruno Pereira Vidal and Luciano Strika and Yueh Tsao and Davide Turcato and Oleksandr Vakhno and Judit Velcsov and Anna Vickers and St\'ephanie Visser and Herdyan Widarmanto and Andrey Zaikin and Si-Qing Chen},
    title = {{RTP-LX}: Can {LLMs} Evaluate Toxicity in Multilingual Scenarios?},
    volume = {AAAI AISI},
    url = {https://openreview.net/forum?id=ZC0Hs5QyCw},
    volume={AAAI},
    year = 2025
}
```

Please note that there's a few other datasets we've based ourselves off. The citations are in the repo.