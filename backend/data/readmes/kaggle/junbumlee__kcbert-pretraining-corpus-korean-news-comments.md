# KcBERT Pre-Training Corpus (Korean News Comments)

Korean Naver News Comments Corpus (cleaned)

# KcBERT Pre-Training Corpus (Korean News Comments)

## KcBERT?

Github KcBERT Repo: [https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)
KcBERT is Korean Comments BERT pretrained on this Corpus set.
(You can use it via Huggingface's Transformers library!)

## What's this?

This Kaggle Dataset contains **CLEANED** dataset preprocessed with the code below.

```python
import re
import emoji
from soynlp.normalizer import repeat_normalize

emojis = ''.join(emoji.UNICODE_EMOJI.keys())
pattern = re.compile(f'[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-힣{emojis}]+')
url_pattern = re.compile(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

def clean(x):
    x = pattern.sub(' ', x)
    x = url_pattern.sub('', x)
    x = x.strip()
    x = repeat_normalize(x, num_repeats=2)
    return x
```

## How to use?

You can use this dataset the way you want to :)
Feel free to use!

출처: Kaggle (junbumlee/kcbert-pretraining-corpus-korean-news-comments)
태그: education, computer science, nlp, text, news
라이선스: CC BY-SA 4.0
수정일: 2020-08-22T02:59:23.697Z
