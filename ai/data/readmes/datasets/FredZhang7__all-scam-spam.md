---
license: apache-2.0
language:
- no
- es
- so
- ca
- af
- it
- nl
- hi
- cy
- ar
- sv
- cs
- pl
- de
- lt
- sq
- uk
- tl
- sl
- hr
- en
- fi
- vi
- id
- da
- ko
- bg
- mr
- ja
- bn
- ro
- pt
- fr
- hu
- tr
- zh
- mk
- ur
- sk
- ne
- et
- sw
- ru
- multilingual
task_categories:
- text-classification
- zero-shot-classification
tags:
- nlp
- moderation
size_categories:
- 10K<n<100K
---

This is a large corpus of 42,619 preprocessed text messages and emails sent by humans in 43 languages. `is_spam=1` means spam and `is_spam=0` means ham.

1040 rows of balanced data, consisting of casual conversations and scam emails in ≈10 languages, were manually collected and annotated by me, with some help from ChatGPT.

<br>

### Some preprcoessing algorithms
- [spam_assassin.js](./spam_assassin.js), followed by [spam_assassin.py](./spam_assassin.py)
- [enron_spam.py](./enron_spam.py)

<br>

### Data composition
![Spam vs Non-spam (Ham)](https://i.imgur.com/p5ytV4q.png)

<br>

### Description
To make the text format between sms messages and emails consistent, email subjects and content are separated by two newlines:

```python
text = email.subject + "\n\n" + email.content
```

<br>

### Suggestions
- If you plan to train a model based on this dataset alone, I recommend adding **some** rows with `is_toxic=0` from `FredZhang7/toxi-text-3M`. Make sure the rows aren't spam.

<br>

### Other Sources
- https://huggingface.co/datasets/sms_spam
- https://github.com/MWiechmann/enron_spam_data
- https://github.com/stdlib-js/datasets-spam-assassin
- https://repository.ortolang.fr/api/content/comere/v3.3/cmr-simuligne.html