---
license: cc-by-nc-4.0
language:
  - ko
  - lzh
  - ja
pretty_name: Open Korean Historical Corpus
size_categories:
  - 10M<n<100M
---

# Open Korean Historical Corpus

## Dataset Description

The **Open Korean Historical Corpus** is a large-scale, openly licensed dataset created to address the lack of accessible data for Korean NLP and historical linguistics.

It contains **17.7 million documents** (5.1 billion tokens) compiled from 19 distinct archives, spanning 1,300 years from the 7th century to 2025. The corpus is linguistically diverse, covering Korean (Middle, Early Modern, Modern, North), Classical Chinese, and Japanese. It provides the first large-scale, open resource for under-represented writing systems like **Korean-style Sinitic (Idu)** and **Hanja-Hangul mixed script**.

## Data Sample

```json
{
  "id": "news_archive:CNTS-00093108108",
  "text": "昨日內部에셔 郡守奏本을 奉呈얏더라",
  "content": {
    "body": "昨日內部에셔 郡守奏本을 奉呈얏더라",
    "title": "郡奏三度"
  },
  "year": 1905,
  "language": "Modern Korean",
  "script": "Hanja, Old Hangeul",
  "source": "National Library of Korea",
  "corpus": "Korean Newspaper Archive",
  "copyright": "Public Domain",
  "url": "https://www.nl.go.kr/newspaper/detail.do?content_id=CNTS-00093108108",
  "format": "{body}",
  "metadata": {
    "host_ko": "대한매일신보",
    "year_str": "西曆一千九百五"
  },
  "analytics": {
    "text_length": 19,
    "content_body_length": 19,
    "content_title_length": 4
  }
}
```

## Intended Use

This corpus is intended for:

- Quantitative diachronic analysis of the Korean language.
- Pre-training or fine-tuning Large Language Models (LLMs) on historical and diverse Korean scripts.
- Research in historical NLP, digital humanities, and Korean linguistics.
