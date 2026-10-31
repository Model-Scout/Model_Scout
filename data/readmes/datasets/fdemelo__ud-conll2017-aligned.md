---
language:
  - ar
  - bg
  - bxr
  - ca
  - cs
  - cu
  - da
  - de
  - el
  - en
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - ga
  - gl
  - got
  - grc
  - he
  - hi
  - hr
  - hsb
  - hu
  - id
  - it
  - ja
  - kk
  - kmr
  - ko
  - la
  - lv
  - nb
  - nl
  - nn
  - pl
  - pt
  - pt
  - ro
  - ru
  - sk
  - sl
  - sme
  - sv
  - tr
  - ug
  - uk
  - ur
  - vi
  - zh
license: cc-by-nc-sa-4.0
---

# UD CoNLL-U 2017 aligned

This dataset is a processed version of the dataset made available for the [UD CoNLL Shared Task 2017](http://universaldependencies.org/conll17/), entitled "Multilingual Parsing from Raw Text to Universal Dependencies." This task is based on the [Universal Dependencies 2.0 dataset](https://lindat.mff.cuni.cz/repository/items/1333f6f2-1627-4fa2-9b6d-e4c24456fe3d).

The processing aligns words and tokens along with their morphological annotations using the [universal part-of-speech set](https://universaldependencies.org/u/pos/) for sequence-to-sequence task training. 

The dataset fields are described in the table below:

|  Field |  Description                          |
| ------ | ------------------------------------- |
| `id`   |  Universal Dependencies submission ID |
| `lang` |  IETF language code (cf. [langcodes](https://github.com/georgkrause/langcodes)) |
| `text` |  Text sentence                        |
| `tags` |  Sequence of universal POS tags       |


## Sequence of Part-of-Speech tags

The sequence of POS tags is separated by spaces, but contiguity of words with punctuation
and contractions from combinations of words are marked by a `+` character. Example:

```
Text: You   won't     see   this section.
Tags: PRON  AUX+PART  VERB  DET  NOUN+PUNCT
```

Note that `won't`, as equivalent to `will+not`, is tagged as `AUX+PART` accordingly.
Also, the contiguity between `section` and the period renders the tagging as `NOUN+PUNCT`.

## Languages

The following languages are available in the dataset.

| Tag  |  Language                  |
| ---- | -------------------------- |
|  ar  |  Arabic                    |
|  bg  |  Bulgarian                 |
|  ca  |  Catalan                   |
|  cs  |  Czech                     |
|  cu  |  Old Church Slavic         |
|  da  |  Danish                    |
|  de  |  German                    |
|  el  |  Greek                     |
|  en  |  English                   |
|  es  |  Spanish                   |
|  et  |  Estonian                  |
|  eu  |  Basque                    |
|  fa  |  Persian                   |
|  fi  |  Finnish                   |
|  fr  |  French                    |
|  ga  |  Irish                     |
|  gl  |  Galician<sup>\*</sup>     |
|  got |  Gothic                    |
|  grc |  Ancient Greek             |
|  he  |  Hebrew                    |
|  hi  |  Hindi                     |
|  hr  |  Croatian                  |
|  hu  |  Hungarian                 |
|  id  |  Indonesian                |
|  it  |  Italian                   |
|  ja  |  Japanese                  |
|  kk  |  Kazakh<sup>\*</sup>       |
|  ko  |  Korean                    |
|  la  |  Latin                     |
|  lv  |  Latvian                   |
|  nb  |  Norwegian Bokmål          |
|  nl  |  Dutch                     |
|  nn  |  Norwegian Nynorsk         |
|  pl  |  Polish                    |
|  pt  |  Portuguese                |
| pt-BR|  Portuguese (Brazil)       |
|  ro  |  Romanian                  |
|  ru  |  Russian                   |
|  sk  |  Slovak                    |
|  sl  |  Slovenian                 |
|  sv  |  Swedish                   |
|  tr  |  Turkish                   |
|  ug  |  Uyghur<sup>\*</sup>       |
|  uk  |  Ukrainian<sup>\*</sup>    |
|  ur  |  Urdu                      |
|  vi  |  Vietnamese                |
|  zh  |  Chinese                   |

\* Not available in the `development` subset.

Only in the `test` subset, the following "surprise" languages are added:

| Tag  |  Language                  |
| ---- | -------------------------- |
|  bxr |  Buriat                    |
|  hsb |  Upper Sorbian             |
|  kmr |  Northern Kurdish          |
|  sme |  Northern Sami             |


## License

The distribution license is inherited from the original dataset and so available to free copy and use under the CC BY-SA or CC BY-NC-SA licenses, depending on the language. See [UD licenses](https://lindat.mff.cuni.cz/repository/static/licence-UD-2.0.html) for more details.
