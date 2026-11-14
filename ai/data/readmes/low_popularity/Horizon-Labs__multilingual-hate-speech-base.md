---
license: apache-2.0
language:
- multilingual
- en
- es
- fr
- de
- it
- pt
- nl
- pl
- cs
- ro
- hu
- el
- bg
- sr
- hr
- uk
- ru
- sv
- da
- 'no'
- fi
- tr
- ar
- he
- fa
- ur
- hi
- bn
- ta
- te
- mr
- zh
- ja
- ko
- vi
- th
- id
- ms
- tl
- sw
- am
- ha
- yo
- af
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
tags:
- hate-speech
- hate-speech-detection
- content-moderation
- trust-and-safety
- multi-label-classification
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "Immigrants are vermin and should be thrown out of the country."
  example_title: "Hateful"
- text: "Saying that immigrants are vermin is disgusting and wrong."
  example_title: "Counter-speech"
- text: "You are a complete idiot."
  example_title: "Insult, not hate"
- text: "Die sind alle Ungeziefer, schmeißt sie raus."
  example_title: "German"
---

# Multilingual Hate Speech Detector (base, 308M)

Detects **hate speech**, meaning attacks on people because of a protected characteristic, in English and about 50 other languages.
It also says **which group is targeted**. Outputs (independent sigmoid probabilities):

- **`hate`**: the text attacks, demeans, dehumanises, stereotypes or calls for harm or exclusion of people because of their race or
  ethnicity, nationality or migration status, religion, gender, sexual orientation, gender identity, disability or age;
- **`target_race`, `target_religion`, `target_origin`, `target_gender`, `target_sexuality`, `target_age`, `target_disability`**:
  which group is attacked (meaningful when `hate` is high).

Ordinary insults, profanity, attacks on politicians, companies or sports fans, criticism of ideas, and counter-speech are *not*
hate speech here, so it complements a general toxicity model such as our
[multilingual-toxicity](https://huggingface.co/Horizon-Labs/multilingual-toxicity-small).
Built on [mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base), Apache-2.0, ONNX for CPU and the browser (transformers.js) included.


- Flag with `hate >= 0.5`, or tune the threshold on your own data. `onnx/model_quantized.onnx` (int8 embeddings, 641 MB): probabilities differ from fp32 by 0.0012 on average over 448 test texts.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/multilingual-hate-speech-base", top_k=None)
print(clf("Die sind alle Ungeziefer, schmeißt sie raus."))
# [[{'label': 'hate', 'score': ...}, {'label': 'target_origin', 'score': ...}, ...]]
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/multilingual-hate-speech-base", { dtype: "q8" });
console.log(await clf("Immigrants are vermin.", { top_k: null }));
```

## Evaluation

Every model is scored the same way (`code/hate/eval_hate.py`): ROC AUC of its hate probability, and F1 at 0.5. No test item was
used for training.

- **Multilingual HateCheck** ([mteb/multi-hatecheck](https://huggingface.co/datasets/mteb/multi-hatecheck), CC-BY-4.0): 40,310 functional
  test cases in 11 languages, including hard non-hateful cases (counter-speech, negation, abuse of individuals or objects, neutral
  mentions of groups).
- **Held-out real comments** (no text from these sets was used in training): Stormfront forum sentences
  ([hate_speech18](https://huggingface.co/datasets/odegiber/hate_speech18), CC-BY-SA-3.0), [ETHOS](https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset)
  binary (YouTube and Reddit), [OLID-BR](https://huggingface.co/datasets/dougtrajano/olid-br) test (Brazilian Portuguese; racism,
  LGBTQphobia, religious intolerance, sexism or xenophobia count as hate) and [K-MHaS](https://github.com/adlnlp/K-MHaS) (Korean news
  comments, 5,000; attacks on protected groups vs not hate speech).
- ¹ **In-domain**: [Measuring Hate Speech](https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech) (6,000 comments,
  hateful = the authors' score > 0.5) and the [HateXplain](https://github.com/hate-alert/HateXplain) test split (offensive-but-not-hate
  counts as negative). Other texts from these two datasets (not the test items, and not their labels) are in our training data.

| model | licence | HateCheck, 11 languages: AUC | HateCheck: F1 @ 0.5 | held-out real comments, 4 sets: mean AUC | Measuring Hate Speech (EN)¹: AUC | HateXplain (EN)¹: AUC | note |
|---|---|---|---|---|---|---|---|
| **this model** (308M) | Apache-2.0 | 0.866 | 0.805 | 0.841 | 0.757 | 0.847 | multilingual |
| [facebook/roberta-hate-speech-dynabench-r4-target](https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target) (125M) | none given | 0.607 | 0.435 | 0.781 | 0.752 | 0.761 | English (Dynabench; the HateCheck authors' lab) |
| [cardiffnlp/twitter-roberta-base-hate-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-hate-latest) (125M) | CC-BY-4.0 | 0.541 | 0.167 | 0.713 | 0.863 | 0.731 | English tweets; trained on 13 hate sets, likely incl. Measuring Hate Speech |
| [Hate-speech-CNERG/dehatebert-mono-english](https://huggingface.co/Hate-speech-CNERG/dehatebert-mono-english) (110M) | Apache-2.0 | 0.569 | 0.309 | 0.687 | 0.737 | 0.722 | English |
| [pysentimiento/robertuito-hate-speech](https://huggingface.co/pysentimiento/robertuito-hate-speech) (109M) | none given | 0.574 | 0.174 | 0.683 | 0.680 | 0.569 | Spanish tweets |
| [IMSyPP/hate_speech_multilingual](https://huggingface.co/IMSyPP/hate_speech_multilingual) (178M) | MIT | 0.691 | 0.762 | 0.741 | 0.803 | 0.609 | multilingual; score = 1 - P(acceptable) |
| [christinacdl/XLM_RoBERTa-Multilingual-Hate-Speech-Detection-New](https://huggingface.co/christinacdl/XLM_RoBERTa-Multilingual-Hate-Speech-Detection-New) (560M) | MIT | 0.973 | 0.961 | 0.767 | 0.797 | 0.781 | multilingual; AUC 1.00 on 8 HateCheck languages, so almost surely trained on HateCheck |
| [Horizon-Labs/multilingual-toxicity-small](https://huggingface.co/Horizon-Labs/multilingual-toxicity-small) (141M) | Apache-2.0 | 0.665 | 0.554 | 0.778 | 0.532 | 0.621 | our toxicity model, identity_attack label |
| Qwen/Qwen3.8-27B (teacher, prompted) (27B) | Apache-2.0 | 0.941 | 0.906 | 0.865 | 0.767 | 0.850 | our teacher, for reference |

- The table shows the released checkpoint. Means over 2 training seeds (HateCheck .866 / .867, held-out real comments .841 / .841, Measuring Hate Speech + HateXplain + K-MHaS .804 / .805).
- The English baselines do well on English but are near chance on the other HateCheck languages. Among models not trained on
  HateCheck, this model leads in 10 of 11 HateCheck languages (Arabic, Mandarin, German, French, Hindi, Italian, Dutch, Polish, Portuguese, Spanish). On the held-out real-comment mean, models ahead of it: none (teacher excluded).
  The XLM-R-large model's near-perfect HateCheck score comes with no training-data documentation; its real-comment scores are the
  comparable evidence.
- Caveat: our synthetic training data deliberately includes counter-speech, quoted hate, offensive-but-not-hateful text and implicit
  hate, which HateCheck also tests (no HateCheck items or templates were used). The held-out real comments are the more independent test.

Held-out real comments by set (AUC):

| model | Stormfront forum (EN) | ETHOS: YouTube, Reddit (EN) | OLID-BR (Brazilian Portuguese) | K-MHaS (Korean) |
|---|---|---|---|---|
| **this model** | 0.904 | 0.932 | 0.721 | 0.808 |
| [facebook/roberta-hate-speech-dynabench-r4-target](https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target) | 0.940 | 0.855 | 0.590 | 0.738 |
| [cardiffnlp/twitter-roberta-base-hate-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-hate-latest) | 0.870 | 0.862 | 0.581 | 0.541 |
| [Hate-speech-CNERG/dehatebert-mono-english](https://huggingface.co/Hate-speech-CNERG/dehatebert-mono-english) | 0.900 | 0.760 | 0.611 | 0.478 |
| [pysentimiento/robertuito-hate-speech](https://huggingface.co/pysentimiento/robertuito-hate-speech) | 0.805 | 0.792 | 0.677 | 0.456 |
| [IMSyPP/hate_speech_multilingual](https://huggingface.co/IMSyPP/hate_speech_multilingual) | 0.867 | 0.803 | 0.516 | 0.778 |
| [christinacdl/XLM_RoBERTa-Multilingual-Hate-Speech-Detection-New](https://huggingface.co/christinacdl/XLM_RoBERTa-Multilingual-Hate-Speech-Detection-New) | 0.802 | 0.832 | 0.639 | 0.796 |
| [Horizon-Labs/multilingual-toxicity-small](https://huggingface.co/Horizon-Labs/multilingual-toxicity-small) | 0.845 | 0.858 | 0.674 | 0.737 |
| Qwen/Qwen3.8-27B (teacher, prompted) | 0.911 | 0.947 | 0.738 | 0.865 |

Per HateCheck language:

| language | this model: AUC | F1 @ 0.5 | IMSyPP multilingual: AUC | facebook r4 (English): AUC | teacher: AUC |
|---|---|---|---|---|---|
| Arabic | 0.776 | 0.699 | 0.597 | 0.509 | 0.847 |
| Mandarin | 0.922 | 0.869 | 0.765 | 0.475 | 0.974 |
| German | 0.910 | 0.878 | 0.711 | 0.595 | 0.971 |
| English | 0.923 | 0.864 | 0.696 | 0.979 | 0.990 |
| French | 0.889 | 0.852 | 0.721 | 0.626 | 0.960 |
| Hindi | 0.677 | 0.491 | 0.566 | 0.541 | 0.828 |
| Italian | 0.901 | 0.850 | 0.665 | 0.600 | 0.959 |
| Dutch | 0.871 | 0.836 | 0.720 | 0.576 | 0.951 |
| Polish | 0.860 | 0.817 | 0.708 | 0.513 | 0.939 |
| Portuguese | 0.900 | 0.849 | 0.737 | 0.628 | 0.969 |
| Spanish | 0.893 | 0.851 | 0.713 | 0.638 | 0.964 |

HateCheck by test type (mean over languages): hateful cases detected 0.67; non-hateful cases correctly left alone:

| non-hateful test type | this model: accuracy @ 0.5 | teacher |
|---|---|---|
| counter-speech quoting hate | 0.82 | 0.79 |
| counter-speech referencing hate | 0.86 | 0.66 |
| neutral mention of a group | 0.95 | 0.99 |
| positive statement about a group | 0.79 | 0.93 |
| negated hate | 0.76 | 0.91 |
| profanity, not hateful | 1.00 | 1.00 |
| slur homonyms | 0.77 | 1.00 |
| reclaimed slurs | 0.86 | 1.00 |
| abuse aimed at non-protected groups | 0.88 | 0.89 |
| abuse aimed at individuals | 1.00 | 0.98 |
| abuse aimed at objects | 1.00 | 1.00 |

Target groups (Measuring Hate Speech, hateful comments, AUC of each `target_*` output vs the annotated target): race 0.89, religion 0.96, origin 0.92, gender 0.90, sexuality 0.92, age 0.83, disability 0.94.

## Training

- **Texts**: 119,983 comments from [Civil Comments](https://huggingface.co/datasets/google/civil_comments) (CC0) and
  their machine translations from [Horizon-Labs/civil-comments-multilingual](https://huggingface.co/datasets/Horizon-Labs/civil-comments-multilingual)
  (half selected for identity-related attacks), plus 85,732 texts written natively in 52 languages by Qwen3.8-27B
  (Apache-2.0) for this purpose: hateful texts against groups of 7 protected categories (explicit and implicit or coded), non-hateful
  texts mentioning those groups (neutral, news-style, counter-speech, quoted hate), and offensive texts that are not hate speech.
  Plus 50,793 real social-media posts: Measuring Hate Speech comments outside our 6,000-comment
  test sample, and the HateXplain train and validation splits (CC-BY-4.0), counted twice. Only their text was used; the labels came
  from the teacher.
- **Labels**: Qwen3.8-27B (prompted with the definition above) answered one yes/no question per output for every text; the model learns
  these probabilities (soft labels, binary cross-entropy). The checkpoint was chosen on 12,881 held-out teacher-labelled texts.
- mmBERT-base, max length 256 tokens. Code: `code/` in this repository.

## Limitations

- What counts as hate speech depends on law, platform policy and culture. This model follows one definition (above). Check it
  against your own policy and data before relying on it.
- Labels come from an LLM teacher, not human annotators, and its errors carry over. The teacher's own scores are in the table.
- Weaker on implicit hate, on Arabic and Hindi (see the per-language table), and on languages and dialects that are rare in the data.
- Do not use it as the only basis for decisions about people. Keep a human in the loop for enforcement.
