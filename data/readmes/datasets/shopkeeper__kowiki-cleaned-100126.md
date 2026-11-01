---
language:
- ko
license: cc-by-sa-4.0
task_categories:
- text-generation
pretty_name: Korean Wikipedia (cleaned) 2026-10-01
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_examples: 606438
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Korean Wikipedia, cleaned (2026-10-01 dump)

Plain-text articles from the Korean Wikipedia dump
[`kowiki-20261001-pages-articles.xml.bz2`](https://dumps.wikimedia.org/kowiki/20261001/).

| | |
|---|---|
| Articles | 606,438 |
| Characters | 820,734,450 |
| Source pages scanned | 2,251,724 |

## Fields

- `id`: Wikipedia page id
- `url`: article URL on ko.wikipedia.org
- `title`: article title
- `text`: cleaned plain text. Section headings appear on their own line;
  paragraphs are separated by a blank line.

## Cleaning

- Main namespace (ns 0) articles only; redirects and disambiguation pages removed.
- Wiki markup converted to plain text. Templates are removed, except inline ones whose
  text is part of the sentence (e.g. `{{lang}}`, `{{llang}}`, `{{임시링크}}`,
  `{{국기나라}}`, `{{convert}}`), which keep their visible text.
- Removed: references/footnotes, tables, infoboxes, navboxes, images and their captions,
  galleries, categories, interlanguage links, HTML comments and tags.
- Removed sections: 각주, 참고 문헌, 외부 링크, 같이 보기 and similar, plus headings left
  with no content.
- Leftovers from removed templates are repaired (e.g. empty `( , )` parentheses).
- Unicode NFC normalisation; zero-width/control characters removed; whitespace normalised.
- Articles shorter than 100 characters after cleaning and exact-duplicate texts dropped.

Drop counts for this dump:

```
disambiguation: 79,283
duplicate_text: 77
kept: 606,438
not_article_namespace: 578,172
redirect: 906,953
too_short: 80,878
```

## License

Text is from Wikipedia and is available under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (and GFDL).
