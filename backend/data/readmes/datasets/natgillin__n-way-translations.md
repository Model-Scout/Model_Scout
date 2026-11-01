---
pretty_name: N-way Translations
license: other
license_name: per-upstream-corpus
task_categories:
  - translation
language:
  - en
  - de
  - es
  - ko
  - nl
  - pt
  - ja
  - it
  - pl
  - fr
  - ar
  - uk
  - ru
  - he
  - hu
  - el
  - bg
  - sv
  - hr
  - tr
  - vi
  - bn
  - sr
  - sk
  - fi
  - cs
  - be
  - hi
  - ro
  - da
  - "no"
  - uz
  - is
  - id
  - ca
  - az
  - ms
  - th
  - ur
  - pa
  - et
  - mr
  - ta
  - gu
  - sl
  - ml
  - te
  - kn
  - or
  - zh
tags:
  - parallel-corpus
  - multilingual
  - n-way
  - machine-translation
  - tatoeba
size_categories:
  - 100K<n<1M
configs:
  - config_name: tatoeba-flatten
    data_files:
      - split: train
        path: data/tatoeba-flatten/*.parquet
---

# natgillin/n-way-translations

Multilingual **N-way** parallel corpus: every row is one logical sentence
expressed in as many languages as the upstream source has it.

## Schema

| column        | type                                       | description |
| ------------- | ------------------------------------------ | ----------- |
| `sentence_id` | string                                     | `<origin>-<NNNNNNNN>` — stable within an origin |
| `origin`      | string                                     | upstream identifier (e.g. `tatoeba-flatten`) |
| `eng`         | string                                     | English text (also kept inside `translations`); null if the row has no English |
| `translations`| list&lt;struct&lt;lang: string, text: string&gt;&gt; | one entry per non-null language: `[{lang: "eng", text: "..."}, {lang: "deu", text: "..."}, ...]` |

`eng` is duplicated as a top-level column for easy filtering / sorting /
joining; the same value is also kept inside `translations` under
`lang == "eng"` so each row stays self-contained.

`translations` uses `list<struct<lang,text>>` (not `map<string,string>`)
because the HF dataset viewer does not yet render map columns. Convert
back to a Python dict in one line: `dict((e['lang'], e['text']) for e in row['translations'])`.

## Configs / layout

One config per upstream origin.

```
data/
  tatoeba-flatten/
    train-00000-of-NNNNN.parquet
    ...
```

## Origins

| origin            | rows    | source                       | languages |
| ----------------- | ------- | ---------------------------- | --------- |
| `tatoeba-flatten` | 215,912 | `alvations/tatoeba-flatten`  | up to 50 (ISO 639-3): eng, deu, spa, kor, nld, por, jpn, ita, pol, fra, ara, ukr, rus, heb, hun, ell, bul, swe, hrv, tur, vie, ben, srp, slk, fin, ces, bel, hin, ron, dan, nob, uzb, isl, ind, cat, aze, msa, tha, urd, pan, est, mar, tam, guj, slv, mal, tel, kan, ori, zho |

## Loading

```python
from datasets import load_dataset

ds = load_dataset("natgillin/n-way-translations", "tatoeba-flatten", split="train")

ex = ds[0]
print(ex["eng"])                                                # English text
print({e["lang"]: e["text"] for e in ex["translations"]})       # full dict view
```

## License

Inherits per-corpus terms from the upstream sources. Tatoeba:
<https://tatoeba.org>.
