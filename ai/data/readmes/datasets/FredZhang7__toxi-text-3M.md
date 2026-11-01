---
license: apache-2.0
task_categories:
- text-classification
- zero-shot-classification
size_categories:
- 1M<n<10M
language:
- ar
- es
- pa
- th
- et
- fr
- fi
- hu
- lt
- ur
- so
- pl
- el
- mr
- sk
- gu
- he
- af
- te
- ro
- lv
- sv
- ne
- kn
- it
- mk
- cs
- en
- de
- da
- ta
- bn
- pt
- sq
- tl
- uk
- bg
- ca
- sw
- hi
- zh
- ja
- hr
- ru
- vi
- id
- sl
- cy
- ko
- nl
- ml
- tr
- fa
- 'no'
- multilingual
tags:
- nlp
- moderation
---

This is a large multilingual toxicity dataset with 3M rows of text data from 55 natural languages, all of which are written/sent by humans, not machine translation models.

The preprocessed training data alone consists of 2,880,667 rows of comments, tweets, and messages. Among these rows, 416,529 are classified as toxic, while the remaining 2,463,773 are considered neutral. Below is a table to illustrate the data composition:
|       |   Toxic  |  Neutral |   Total  |
|-------|----------|----------|----------|
| [multilingual-train-deduplicated.csv](./train/multilingual-train-deduplicated.csv) |   416,529   |   2,464,138   |   2,880,667   |
| [multilingual-validation(new).csv](./validation/multilingual-validation(new).csv) |   10,613  |  19,028   |   29,641   |
| [multilingual-test.csv](./test/multilingual-test.csv) |   14,410   |   49,402   |   63,812   |
Each CSV file has three columns: `text`, `is_toxic`, and `lang`.

Supported types of toxicity:
- Identity Hate/Homophobia
- Misogyny
- Violent Extremism
- Hate Speech
- Offensive Insults
- Sexting
- Obscene
- Threats
- Harassment
- Racism
- Trolling
- Doxing
- Others

Supported languages:
- Afrikaans
- Albanian
- Arabic
- Bengali
- Bulgarian
- Catalan
- Chinese (Simplified)
- Chinese (Traditional)
- Croatian
- Czech
- Danish
- Dutch
- English
- Estonian
- Finnish
- French
- German
- Greek
- Gujarati
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Kannada
- Korean
- Latvian
- Lithuanian
- Macedonian
- Malayalam
- Marathi
- Nepali
- Norwegian
- Persian
- Polish
- Portuguese
- Punjabi
- Romanian
- Russian
- Slovak
- Slovenian
- Somali
- Spanish
- Swahili
- Swedish
- Tagalog
- Tamil
- Telugu
- Thai
- Turkish
- Ukrainian
- Urdu
- Vietnamese
- Welsh


<br>


### Original Source?
Around 11 months ago, I downloaded and preprocessed 2.7M rows of text data, but completely forgot the original source of these datasets...
All I remember is that I downloaded datasets from everywhere I could: HuggingFace, research papers, GitHub, Kaggle, SurgeAI, and Google search. I even fetched 20K+ tweets using the Twitter API.
Recently, I came across 6 datasets, so I remembered to credit them below.

Known datasets:
- tomekkorbak/pile-toxicity-balanced2 (HuggingFace)
- datasets/thai_toxicity_tweet (HuggingFace)
- datasets/ethos (HuggingFace)
- inspection-ai/japanese-toxic-dataset (GitHub)
- mathigatti/sexting-dataset (GitHub)
- omar-sharif03/BAD-Bangla-Aggressive-Text-Dataset (GitHub)

I manually collected and wrote 100 rows of data.

<br>

### Loading the Dataset

To prevent errors like [row count mismatch](https://huggingface.co/datasets/FredZhang7/toxi-text-3M/discussions/5), please add `verification_mode="no_checks"` when loading the dataset.

```py
from datasets import load_dataset

ds = load_dataset("FredZhang7/toxi-text-3M", verification_mode="no_checks")
```


<br>

### Limitations
Limitations include:
- All labels were rounded to the nearest integer. If a text was classified as 46%-54% toxic, the text itself might not be noticeably toxic or neutral.
- There were disagreements among moderators on some labels, due to ambiguity and lack of context.
- When there're only URL(s), emojis, or anything that's unrecognizable as natural language in the "text" column, the corresponding "lang" is "unknown".

Have fun modelling!