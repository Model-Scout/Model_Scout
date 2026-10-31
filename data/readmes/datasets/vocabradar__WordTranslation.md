---
configs:
- config_name: default
  data_files:
  - split: train
    path: "data/*.jsonl.gz"
language: [ar, bg, bn, ca, cs, da, de, el, en, es, fa, fi, fil, fr, he, hi, hu, id, is, it, ja, ko, lt, lv, mk, ms, nb, nl, pl, pt, ro, ru, sh, sk, sl, sv, ta, th, tr, uk, ur, vi, zh]
license: cc-by-sa-4.0
multilinguality: multilingual
pretty_name: WordTranslation — Offline Word Translation Packs (vocabradar/wordfreq vocabulary) / 离线单词翻译包（vocabradar/wordfreq 词表）
size_categories:
- 1M<n<10M
source_datasets:
- vocabradar/wordfreq
task_categories:
- translation
---

# WordTranslation — Offline Word Translation Packs (vocabradar/wordfreq vocabulary) / 离线单词翻译包（vocabradar/wordfreq 词表）

## What it is

Offline word-translation packs for **43 languages** around English and Chinese: every word
of a language's cleaned vocabulary, paired with its translations. **The vocabulary comes
straight from the [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
dataset** — that dataset is this one's direct source: the words translated here are its
`small_<code>` lists, in the order they are stored there. 166 gzipped JSONL files,
one per language pair (83.5 MiB in total, 0.09–1.07 MiB each);
`en ⇄ X` and `zh ⇄ X` share the same 41 partner languages (40 + Thai).

## What it is for

- **An offline lexicon.** Unzip one file and the whole pair is in memory — no network, no
  API key, no per-lookup cost.
- **Word hints in your own app** — the same packs are what the
  [VocabRadar browser extension](https://vocabradar.com) shows while you read.
- **Frequency-ordered work.** Lines follow the rank order of the vocabradar/wordfreq list
  (most frequent word first), so a pack also works as an MT / dev lexicon for a
  low-resource pair.
- **Gap checking.** The hit-rate tables below give, per language, how much of that
  vocabulary actually has a translation — enough to judge whether a pair suits your use.

## How it is built

**Words:** the `small_<code>` list of the source language, taken as-is from the
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) dataset, its
frequency order preserved.

**Translations:** professional bilingual dictionaries come first wherever a
license-compatible edition exists — **ECDICT** (en→zh, MIT), **CC-CEDICT** (zh→en,
CC BY-SA 4.0), **JMdict** (ja↔en, CC BY-SA 4.0), **HanDeDict** (zh↔de, CC BY-SA 2.0),
**CFDICT** (zh↔fr, CC BY-SA 3.0) and **Folkets lexikon** (sv↔en, CC BY-SA 2.5).
One-way dictionaries are inverted gloss→headword for their reverse direction, and only
target words that occur in the vocabulary are kept. The rest is base data — human-curated
dictionaries only: English / Chinese Wiktionary via
[wiktextract](https://github.com/tatuylonen/wiktextract) /
[kaikki.org](https://kaikki.org) (CC BY-SA 4.0) + PanLex (CC0) where available. Remaining
vocabulary gaps are filled by the local model **Hunyuan-MT2-1.8B Q4_K_M** (Apache-2.0,
official GGUF served by llama.cpp); languages it does not support are filled by a second
local model layer, **LMT-60-1.7B Q4_K_M** (Apache-2.0, NiuTrans) — also machine-generated.
Reverse directions obtained by gloss inversion are less reliable for closed-class words
(articles, copulas, particles): German `der` can surface a content-word gloss, and French
`est` can be read as “east”. HanDeDict/CFDICT entries for grammatical particles are usage
descriptions rather than single-word equivalents; both cases are kept as-is and marked here.

**Quality control.** Every pack passes a content-level QC sweep before release
(`tools/qc_check.py`): runaway model output (repeated-character runs, e.g. a French
`aïe` once glossed as 呜呜呜呜…), placeholder/model-leak strings, mojibake and
script violations are removed; stray leading combining marks are repaired; emptied
words are re-translated by the local model cascade and re-checked. Rules and the
2026-10 cleanup record live in `docs/`.

All directions live in one directory: one gzip JSONL file per language pair,
`data/<src>_<dst>.jsonl.gz` (the en ⇄ zh pair is stored once). Every line is one JSON
object with a fixed pair of fields — a source `word` and its `translations`.

> 中文版请见下方：[中文版说明](#zh)

## Files

```
├── README.md
├── meta.json                   # per-direction source, cap and language stats
├── files.json                  # per-file size (bytes) and SHA-256
└── data/                       # 166 files: <src>_<dst>.jsonl.gz
```

## Data format

```json
{"word": "house", "translations": ["casa", "hogar"]}
```

- Field names are constant on every line (`word`, `translations`), so the Hub's Dataset
  Viewer renders each file as a two-column table (`word: string`,
  `translations: list<string>`) instead of one column per source word.
- `data/<src>_<dst>.jsonl.gz` translates the `src` word list (the `small_<src>` list of
  [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)) into `dst`;
  lines are ordered by that list's rank — deterministic rebuilds.
- Translations are deduplicated case-insensitively and capped at 10 per word;
  gap-fill entries are capped at 3 and pass the same per-language Unicode script
  whitelist as every other layer.
- **The gap-fill layers are machine-generated and may contain errors.**

## Languages & hits

*hits* is the share of that language's list with at least one translation — **not** the
*cumulative coverage* column of vocabradar/wordfreq, which measures token coverage of a
corpus; a hit here only means "this vocabulary word has a translation in this file".
*native name* is the language's own name for itself — the same autonym the
vocabradar/wordfreq card lists.
*first line* is the first line of that row's own file, verbatim — the highest-frequency
source word (from the
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) list this
dataset is keyed to) together with the translations found for it, so one glance checks
both ends: the vocabulary (is that word really first?) and the target language (do the
translations look like it?). The **total** row adds up *words translated* and *entries*;
its *hits* is the weighted aggregate (Σ translated / Σ vocabulary), since each
reverse-direction language has its own denominator.

### en → X (EnToX)

English Wiktionary source; vocabulary = `small_en` of vocabradar/wordfreq — 41 languages

| code | language | native name | first line | words translated | hits | entries |
|------|----------|-------------|------------|------------------|----------|---------|
| ar | Arabic | العربية | `{"word":"the","translations":["الـ","ال"]}` | 28,223 | 100.0% | 111,486 |
| bg | Bulgarian | български | `{"word":"the","translations":["-та","-то","-те","по"]}` | 28,220 | 100.0% | 74,713 |
| bn | Bengali | বাংলা | `{"word":"the","translations":["-রা","-এরা","-গুলা","-গুলো","-টা","-টি","গাছা","গাছি","মহাবিশ্ব"]}` | 28,223 | 100.0% | 67,972 |
| ca | Catalan | català | `{"word":"the","translations":["el","la","l' els m pl les","es","sa","ets","sos","ses","els","les"]}` | 28,223 | 100.0% | 84,343 |
| cs | Czech | čeština | `{"word":"the","translations":["ta","ten","to","určitý člen","člen určitý"]}` | 28,223 | 100.0% | 106,829 |
| da | Danish | dansk | `{"word":"the","translations":["de","den","det","en","et","-et","-en","-ne"]}` | 28,223 | 100.0% | 63,132 |
| de | German | Deutsch | `{"word":"the","translations":["der","die","das","de","dr","den","dieser","umso","Platz","der die das die"]}` | 28,223 | 100.0% | 146,827 |
| el | Greek | Ελληνικά | `{"word":"the","translations":["ο","ὁ","στον","στη","στο","άρθρο","η","οι","παράμεσος","στα"]}` | 28,179 | 99.8% | 90,613 |
| es | Spanish | español | `{"word":"the","translations":["el","la","los","las","lo","el la los las","entonces","pero","pues"]}` | 28,223 | 100.0% | 126,135 |
| fa | Persian | فارسی | `{"word":"the","translations":["این","آن","ال","باسلیقون","ثلاثة غساله","دلیجه","ساز","سفیدرود","سنده","قبلة"]}` | 28,223 | 100.0% | 91,682 |
| fi | Finnish | suomi | `{"word":"the","translations":["se","-ni","-si","-nsa","-nsä","-mme","-nne","minun","sinun","hänen"]}` | 28,223 | 100.0% | 128,415 |
| fil | Filipino | Filipino | `{"word":"the","translations":["ang","nang","mga"]}` | 28,223 | 100.0% | 48,367 |
| fr | French | français | `{"word":"the","translations":["le","la","les","l'","comp.","colloquial or regional usage","acquitter","au","aux","ce"]}` | 28,223 | 100.0% | 132,443 |
| he | Hebrew | עברית | `{"word":"the","translations":["ה־","ה"]}` | 28,222 | 100.0% | 50,356 |
| hi | Hindi | हिन्दी | `{"word":"the","translations":["जिस काम के पूरे करने में सभी लगे हों","ईसामसीह","दि","यह","वह","वही"]}` | 28,223 | 100.0% | 106,614 |
| hu | Hungarian | magyar | `{"word":"the","translations":["a","az"]}` | 28,223 | 100.0% | 104,597 |
| id | Indonesian | Bahasa Indonesia | `{"word":"the","translations":["si","sang","itu","al","-nya","kian"]}` | 28,223 | 100.0% | 93,819 |
| is | Icelandic | íslenska | `{"word":"the","translations":["-inn","hinn","hið","-in","-nar","-ið","-nir"]}` | 28,223 | 100.0% | 57,806 |
| it | Italian | italiano | `{"word":"the","translations":["il","lo","la","l'","i","gli","le","li","lì","gl’"]}` | 28,223 | 100.0% | 120,328 |
| ja | Japanese | 日本語 | `{"word":"the","translations":["その","正に","正しく","ザ","這","あの","其の","定冠詞","当該","死因"]}` | 28,212 | 100.0% | 145,314 |
| ko | Korean | 한국어 | `{"word":"the","translations":["-을수록","그","그만큼$2$","저","하면 할수록","하면 할수록 그만큼 더"]}` | 28,217 | 100.0% | 104,823 |
| lt | Lithuanian | lietuvių | `{"word":"the","translations":["tai"]}` | 28,223 | 100.0% | 42,549 |
| lv | Latvian | latviešu | `{"word":"the","translations":["sirdi"]}` | 28,211 | 100.0% | 38,168 |
| mk | Macedonian | македонски | `{"word":"the","translations":["-ов","-те","-от","многуте","највеќе","најголем дел","најмногу","онака","постојано","-во"]}` | 28,184 | 99.9% | 47,766 |
| ms | Malay | Bahasa Melayu | `{"word":"the","translations":["sang","-nya","itu","ini","si","semakin..., semakin...","lagi..., lagi..."]}` | 28,223 | 100.0% | 85,179 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"the","translations":["det","den","-et","-en","-a","-i","de","desto","jo","-one"]}` | 28,223 | 100.0% | 68,517 |
| nl | Dutch | Nederlands | `{"word":"the","translations":["de","het","aan de","aan het","des te","die","hoe","naar de","naar het","’t"]}` | 28,223 | 100.0% | 107,151 |
| pl | Polish | polski | `{"word":"the","translations":["ten","czym","im","przedimek określony","ta","to","te"]}` | 28,223 | 100.0% | 95,604 |
| pt | Portuguese | português | `{"word":"the","translations":["o","a","os","as","o a os as"]}` | 28,223 | 100.0% | 107,945 |
| ro | Romanian | română | `{"word":"the","translations":["-ul","-a","cel","cea","-i","cele","-le"]}` | 28,223 | 100.0% | 61,507 |
| ru | Russian | русский | `{"word":"the","translations":["на ходу","определенный артикль","определённый артикль","подходящий","такой","тем","тот","чем","чем... тем"]}` | 28,219 | 100.0% | 148,990 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"the","translations":["Alpe","Antarktika","Atlantik","Balkan","Baltik","Drava","Drina","Dunav","Holandija","Jadran"]}` | 28,209 | 100.0% | 118,146 |
| sk | Slovak | slovenčina | `{"word":"the","translations":["ten","to","tá"]}` | 28,223 | 100.0% | 98,458 |
| sl | Slovenian | slovenščina | `{"word":"the","translations":["the"]}` | 28,223 | 100.0% | 76,078 |
| sv | Swedish | svenska | `{"word":"the","translations":["den","dess","desto","-en","de","det","ju","vederbörande","vintergatan","överklassen"]}` | 28,223 | 100.0% | 100,554 |
| ta | Tamil | தமிழ் | `{"word":"the","translations":["அது"]}` | 28,223 | 100.0% | 72,940 |
| th | Thai | ไทย | `{"word":"the","translations":["นั้น"]}` | 28,188 | 99.9% | 28,312 |
| tr | Turkish | Türkçe | `{"word":"the","translations":["bir","harfi tarif","ne kadar","üstlenmek"]}` | 28,223 | 100.0% | 99,531 |
| uk | Ukrainian | українська | `{"word":"the","translations":["те"]}` | 28,221 | 100.0% | 71,637 |
| ur | Urdu | اردو | `{"word":"the","translations":["ال"]}` | 28,223 | 100.0% | 60,976 |
| vi | Vietnamese | Tiếng Việt | `{"word":"the","translations":["con","càng","cái","duy nhất","này","ấy"]}` | 28,223 | 100.0% | 95,230 |
| **total** | 41 languages | — | — | 1,156,972 | 100.0% | 3,681,852 |

### X → en (XToEn)

English Wiktionary source, inverted; vocabulary = `small_<code>` of vocabradar/wordfreq — 41 languages

| code | language | native name | first line | words translated | hits | entries |
|------|----------|-------------|------------|------------------|----------|---------|
| ar | Arabic | العربية | `{"word":"في","translations":["a","in","on","at","by","into","through","during","times","within"]}` | 55,606 | 100.0% | 101,618 |
| bg | Bulgarian | български | `{"word":"на","translations":["of","in","on","at","onto","lo"]}` | 35,848 | 100.0% | 55,492 |
| bn | Bengali | বাংলা | `{"word":"না","translations":["not","no","don't","never","without","please","non","boat","un","na"]}` | 33,045 | 99.9% | 50,042 |
| ca | Catalan | català | `{"word":"de","translations":["of","in","with","from","about","more","off","again","coral","dee"]}` | 27,028 | 100.0% | 60,056 |
| cs | Czech | čeština | `{"word":"a","translations":["and","a","that","who","which","any","both","recent","double","plus"]}` | 51,744 | 100.0% | 92,063 |
| da | Danish | dansk | `{"word":"i","translations":["to","of","a","in","for","you","on","with","at","by"]}` | 29,321 | 100.0% | 50,479 |
| de | German | Deutsch | `{"word":"die","translations":["the","a","that","this","but","an","all","what","who","which"]}` | 38,989 | 100.0% | 114,757 |
| el | Greek | Ελληνικά | `{"word":"και","translations":["and","that","but","which","also","too","both"]}` | 43,188 | 100.0% | 61,778 |
| es | Spanish | español | `{"word":"de","translations":["of","in","for","on","with","be","as","at","by","from"]}` | 34,740 | 100.0% | 98,038 |
| fa | Persian | فارسی | `{"word":"و","translations":["and","both"]}` | 30,108 | 100.0% | 57,014 |
| fi | Finnish | suomi | `{"word":"ja","translations":["and","so","also","too","both","plus","likewise","wedge"]}` | 59,143 | 100.0% | 107,690 |
| fil | Filipino | Filipino | `{"word":"sa","translations":["to","of","a","in","for","on","with","at","by","from"]}` | 30,098 | 100.0% | 40,648 |
| fr | French | français | `{"word":"de","translations":["to","of","a","in","for","on","with","be","as","at"]}` | 31,203 | 100.0% | 100,218 |
| he | Hebrew | עברית | `{"word":"את","translations":["you","with","me","alongside","amongst","thou","shovel","spade"]}` | 57,376 | 99.9% | 68,773 |
| hi | Hindi | हिन्दी | `{"word":"के","translations":["of","in","for","with","as","have","by","from","his","about"]}` | 24,031 | 100.0% | 56,346 |
| hu | Hungarian | magyar | `{"word":"a","translations":["the","a","black","amps"]}` | 46,525 | 100.0% | 81,700 |
| id | Indonesian | Bahasa Indonesia | `{"word":"yang","translations":["that","who","which","second","third","whose","rel"]}` | 30,967 | 100.0% | 77,623 |
| is | Icelandic | íslenska | `{"word":"og","translations":["and","but","which","also","both","plus"]}` | 42,207 | 100.0% | 56,957 |
| it | Italian | italiano | `{"word":"di","translations":["to","of","in","for","that","on","with","be","at","by"]}` | 35,954 | 100.0% | 96,114 |
| ja | Japanese | 日本語 | `{"word":"の","translations":["indicates possessive","nominalizes verbs and adjectives","substitutes for \"ga\" in subordinate phrases","indicates a confident conclusion","indicates emotional emphasis","indicates question","field","plain","hidden interior part","wild"]}` | 27,856 | 100.0% | 138,071 |
| ko | Korean | 한국어 | `{"word":"이","translations":["and","that","you","this","be","he","but","she","only","two"]}` | 26,807 | 100.0% | 48,935 |
| lt | Lithuanian | lietuvių | `{"word":"ir","translations":["and","even","afterward"]}` | 63,973 | 100.0% | 71,616 |
| lv | Latvian | latviešu | `{"word":"un","translations":["and"]}` | 45,464 | 100.0% | 51,239 |
| mk | Macedonian | македонски | `{"word":"на","translations":["of","for","on","at","per"]}` | 32,925 | 100.0% | 42,850 |
| ms | Malay | Bahasa Melayu | `{"word":"yang","translations":["that","one","which","change","cash","coins","umbrella"]}` | 28,571 | 100.0% | 69,966 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"i","translations":["to","of","a","in","for","you","on","with","at","by"]}` | 25,994 | 100.0% | 48,694 |
| nl | Dutch | Nederlands | `{"word":"de","translations":["the","you","this","one","able","bus","exposure","repaid","earthy"]}` | 28,715 | 100.0% | 78,061 |
| pl | Polish | polski | `{"word":"w","translations":["to","of","a","in","for","on","with","at","by","an"]}` | 49,664 | 100.0% | 81,502 |
| pt | Portuguese | português | `{"word":"de","translations":["of","for","with","by","from","about","something","old","someone","hunger"]}` | 33,123 | 100.0% | 82,780 |
| ro | Romanian | română | `{"word":"de","translations":["of","for","on","by","from","since","against"]}` | 43,279 | 100.0% | 62,582 |
| ru | Russian | русский | `{"word":"в","translations":["to","of","a","in","for","on","with","as","at","by"]}` | 59,604 | 100.0% | 122,769 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"je","translations":["is","are","if","has","her","did","sued"]}` | 54,698 | 100.0% | 97,376 |
| sk | Slovak | slovenčina | `{"word":"a","translations":["and","amps"]}` | 59,414 | 100.0% | 101,829 |
| sl | Slovenian | slovenščina | `{"word":"je","translations":["is"]}` | 53,882 | 100.0% | 77,313 |
| sv | Swedish | svenska | `{"word":"är","translations":["is","are","am","result","arise"]}` | 30,515 | 100.0% | 66,415 |
| ta | Tamil | தமிழ் | `{"word":"ஒரு","translations":["a","an","hour","sole","sheep","mono"]}` | 64,751 | 100.0% | 83,531 |
| th | Thai | ไทย | `{"word":"ที่","translations":["place","that","which","who"]}` | 39,499 | 99.5% | 39,856 |
| tr | Turkish | Türkçe | `{"word":"ve","translations":["and","so","both","species","vee"]}` | 63,130 | 100.0% | 95,737 |
| uk | Ukrainian | українська | `{"word":"в","translations":["to","in","have","at","into","per"]}` | 46,285 | 100.0% | 62,505 |
| ur | Urdu | اردو | `{"word":"کے","translations":["of","at"]}` | 22,442 | 100.0% | 37,850 |
| vi | Vietnamese | Tiếng Việt | `{"word":"là","translations":["is","that","was","be","as","are","were","been","how","some"]}` | 10,519 | 100.0% | 26,597 |
| zh | Chinese | 中文 | `{"word":"的","translations":["of","s","used after an attribute when it modifies a noun","used at the end of a declarative sentence for emphasis","also pr. [di4] or [di5] in poetry and songs","a taxi","a cab","really and truly","bull's-eye","target"]}` | 35,723 | 100.0% | 145,872 |
| **total** | 42 languages | — | — | 1,683,954 | 100.0% | 3,161,352 |

### zh → X (ZhToX)

Chinese Wiktionary source; vocabulary = `small_zh` of vocabradar/wordfreq — 41 languages

| code | language | native name | first line | words translated | hits | entries |
|------|----------|-------------|------------|------------------|----------|---------|
| ar | Arabic | العربية | `{"word":"的","translations":["ال"]}` | 35,723 | 100.0% | 37,413 |
| bg | Bulgarian | български | `{"word":"的","translations":["ето"]}` | 35,702 | 99.9% | 36,852 |
| bn | Bengali | বাংলা | `{"word":"的","translations":["ের"]}` | 35,723 | 100.0% | 36,298 |
| ca | Catalan | català | `{"word":"的","translations":["de"]}` | 35,721 | 100.0% | 36,571 |
| cs | Czech | čeština | `{"word":"的","translations":["Jeho"]}` | 35,723 | 100.0% | 36,903 |
| da | Danish | dansk | `{"word":"的","translations":["Dan"]}` | 35,722 | 100.0% | 36,601 |
| de | German | Deutsch | `{"word":"的","translations":["wird nach einem Adjektiv oder einer Attributphrase verwendet","wird nach einem Verb verwendet, um das Subjekt, die Zeit","Ziel, das Schwarze","klar"]}` | 35,721 | 100.0% | 60,922 |
| el | Greek | Ελληνικά | `{"word":"的","translations":["του"]}` | 35,229 | 98.6% | 36,199 |
| es | Spanish | español | `{"word":"的","translations":["de"]}` | 35,723 | 100.0% | 38,381 |
| fa | Persian | فارسی | `{"word":"的","translations":["که"]}` | 35,721 | 100.0% | 37,234 |
| fi | Finnish | suomi | `{"word":"的","translations":["Finnish"]}` | 35,704 | 99.9% | 37,635 |
| fil | Filipino | Filipino | `{"word":"的","translations":["ay"]}` | 35,722 | 100.0% | 36,531 |
| fr | French | français | `{"word":"的","translations":["de","utilisé après un adjectif, un nom","centre de la cible","but","objectif","voir","vrai"]}` | 35,723 | 100.0% | 67,607 |
| he | Hebrew | עברית | `{"word":"的","translations":["של"]}` | 35,714 | 100.0% | 36,359 |
| hi | Hindi | हिन्दी | `{"word":"的","translations":["का"]}` | 35,722 | 100.0% | 37,985 |
| hu | Hungarian | magyar | `{"word":"的","translations":["És"]}` | 35,720 | 100.0% | 37,238 |
| id | Indonesian | Bahasa Indonesia | `{"word":"的","translations":["adalah"]}` | 35,723 | 100.0% | 36,491 |
| is | Icelandic | íslenska | `{"word":"的","translations":["Er"]}` | 35,723 | 100.0% | 36,535 |
| it | Italian | italiano | `{"word":"的","translations":["di"]}` | 35,723 | 100.0% | 37,266 |
| ja | Japanese | 日本語 | `{"word":"的","translations":["の"]}` | 35,706 | 100.0% | 38,413 |
| ko | Korean | 한국어 | `{"word":"的","translations":["-의"]}` | 35,706 | 100.0% | 36,859 |
| lt | Lithuanian | lietuvių | `{"word":"的","translations":["ž"]}` | 35,721 | 100.0% | 36,204 |
| lv | Latvian | latviešu | `{"word":"的","translations":["Latv"]}` | 35,663 | 99.8% | 36,253 |
| mk | Macedonian | македонски | `{"word":"的","translations":["Македонски"]}` | 35,587 | 99.6% | 36,528 |
| ms | Malay | Bahasa Melayu | `{"word":"的","translations":["nya"]}` | 35,723 | 100.0% | 36,659 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"的","translations":["Det"]}` | 35,721 | 100.0% | 36,475 |
| nl | Dutch | Nederlands | `{"word":"的","translations":["van"]}` | 35,723 | 100.0% | 37,389 |
| pl | Polish | polski | `{"word":"的","translations":["tak"]}` | 35,723 | 100.0% | 37,637 |
| pt | Portuguese | português | `{"word":"的","translations":["do"]}` | 35,719 | 100.0% | 37,492 |
| ro | Romanian | română | `{"word":"的","translations":["de”"]}` | 35,719 | 100.0% | 36,937 |
| ru | Russian | русский | `{"word":"的","translations":["дом"]}` | 35,694 | 99.9% | 63,021 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"的","translations":["Srbijanski"]}` | 35,494 | 99.4% | 37,198 |
| sk | Slovak | slovenčina | `{"word":"的","translations":["So"]}` | 35,723 | 100.0% | 36,532 |
| sl | Slovenian | slovenščina | `{"word":"的","translations":["Slovenski"]}` | 35,721 | 100.0% | 36,300 |
| sv | Swedish | svenska | `{"word":"的","translations":["av"]}` | 35,723 | 100.0% | 37,092 |
| ta | Tamil | தமிழ் | `{"word":"的","translations":["அதன்"]}` | 35,723 | 100.0% | 36,048 |
| th | Thai | ไทย | `{"word":"的","translations":["ของ"]}` | 34,357 | 96.2% | 34,368 |
| tr | Turkish | Türkçe | `{"word":"的","translations":["oldu"]}` | 35,723 | 100.0% | 37,256 |
| uk | Ukrainian | українська | `{"word":"的","translations":["Українською"]}` | 35,699 | 99.9% | 37,623 |
| ur | Urdu | اردو | `{"word":"的","translations":["کی"]}` | 35,723 | 100.0% | 36,683 |
| vi | Vietnamese | Tiếng Việt | `{"word":"的","translations":["của"]}` | 35,722 | 100.0% | 37,470 |
| **total** | 41 languages | — | — | 1,462,195 | 99.8% | 1,593,458 |

### X → zh (XToZh)

Chinese Wiktionary source, inverted; vocabulary = `small_<code>` of vocabradar/wordfreq — 41 languages

| code | language | native name | first line | words translated | hits | entries |
|------|----------|-------------|------------|------------------|----------|---------|
| ar | Arabic | العربية | `{"word":"في","translations":["在"]}` | 55,553 | 99.9% | 55,814 |
| bg | Bulgarian | български | `{"word":"на","translations":["在"]}` | 35,768 | 99.8% | 35,904 |
| bn | Bengali | বাংলা | `{"word":"না","translations":["从不"]}` | 32,791 | 99.2% | 32,874 |
| ca | Catalan | català | `{"word":"de","translations":["德"]}` | 27,006 | 99.9% | 27,148 |
| cs | Czech | čeština | `{"word":"a","translations":["a"]}` | 51,708 | 99.9% | 51,825 |
| da | Danish | dansk | `{"word":"i","translations":["i"]}` | 29,310 | 100.0% | 29,437 |
| de | German | Deutsch | `{"word":"die","translations":["是","这些"]}` | 38,975 | 100.0% | 61,494 |
| el | Greek | Ελληνικά | `{"word":"και","translations":["和"]}` | 42,952 | 99.4% | 43,061 |
| en | English | English | `{"word":"the","translations":["那"]}` | 28,219 | 100.0% | 84,155 |
| es | Spanish | español | `{"word":"de","translations":["德"]}` | 34,731 | 100.0% | 35,055 |
| fa | Persian | فارسی | `{"word":"و","translations":["和"]}` | 30,070 | 99.9% | 30,277 |
| fi | Finnish | suomi | `{"word":"ja","translations":["是"]}` | 59,030 | 99.8% | 59,234 |
| fil | Filipino | Filipino | `{"word":"sa","translations":["萨"]}` | 30,093 | 100.0% | 30,167 |
| fr | French | français | `{"word":"de","translations":["的","与","于","从","由","从中","乎","为了"]}` | 31,196 | 100.0% | 50,536 |
| he | Hebrew | עברית | `{"word":"את","translations":["你"]}` | 57,300 | 99.8% | 57,431 |
| hi | Hindi | हिन्दी | `{"word":"के","translations":["科"]}` | 23,800 | 99.0% | 24,036 |
| hu | Hungarian | magyar | `{"word":"a","translations":["a"]}` | 46,519 | 100.0% | 46,669 |
| id | Indonesian | Bahasa Indonesia | `{"word":"yang","translations":["杨"]}` | 30,957 | 100.0% | 31,060 |
| is | Icelandic | íslenska | `{"word":"og","translations":["og"]}` | 42,189 | 100.0% | 42,280 |
| it | Italian | italiano | `{"word":"di","translations":["迪"]}` | 35,947 | 100.0% | 36,154 |
| ja | Japanese | 日本語 | `{"word":"の","translations":["的"]}` | 27,822 | 99.9% | 28,038 |
| ko | Korean | 한국어 | `{"word":"이","translations":["牙齿","二"]}` | 26,758 | 99.8% | 26,847 |
| lt | Lithuanian | lietuvių | `{"word":"ir","translations":["ir"]}` | 63,905 | 99.9% | 63,978 |
| lv | Latvian | latviešu | `{"word":"un","translations":["不"]}` | 45,397 | 99.9% | 45,471 |
| mk | Macedonian | македонски | `{"word":"на","translations":["在"]}` | 32,840 | 99.7% | 32,954 |
| ms | Malay | Bahasa Melayu | `{"word":"yang","translations":["杨"]}` | 28,562 | 100.0% | 28,673 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"i","translations":["你"]}` | 25,985 | 100.0% | 26,067 |
| nl | Dutch | Nederlands | `{"word":"de","translations":["de"]}` | 28,708 | 100.0% | 28,879 |
| pl | Polish | polski | `{"word":"w","translations":["w"]}` | 49,651 | 100.0% | 49,832 |
| pt | Portuguese | português | `{"word":"de","translations":["de"]}` | 33,117 | 100.0% | 33,370 |
| ro | Romanian | română | `{"word":"de","translations":["德"]}` | 43,271 | 100.0% | 43,415 |
| ru | Russian | русский | `{"word":"в","translations":["就是","同时","如何","其中","影响","目前","参加","具有","实现","是不是"]}` | 59,388 | 99.6% | 72,489 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"je","translations":["你"]}` | 54,687 | 100.0% | 54,724 |
| sk | Slovak | slovenčina | `{"word":"a","translations":["a"]}` | 59,390 | 100.0% | 59,484 |
| sl | Slovenian | slovenščina | `{"word":"je","translations":["je"]}` | 53,870 | 100.0% | 53,934 |
| sv | Swedish | svenska | `{"word":"är","translations":["是"]}` | 30,507 | 100.0% | 30,680 |
| ta | Tamil | தமிழ் | `{"word":"ஒரு","translations":["一个"]}` | 64,563 | 99.7% | 64,609 |
| th | Thai | ไทย | `{"word":"ที่","translations":["地点","地點"]}` | 34,098 | 85.9% | 34,634 |
| tr | Turkish | Türkçe | `{"word":"ve","translations":["ve"]}` | 63,011 | 99.8% | 63,200 |
| uk | Ukrainian | українська | `{"word":"в","translations":["在"]}` | 46,084 | 99.6% | 46,236 |
| ur | Urdu | اردو | `{"word":"کے","translations":["的"]}` | 22,415 | 99.9% | 22,547 |
| vi | Vietnamese | Tiếng Việt | `{"word":"là","translations":["是"]}` | 10,510 | 99.9% | 10,589 |
| **total** | 42 languages | — | — | 1,668,653 | 99.5% | 1,785,261 |

## Regenerating

```bash
python tools/build_pro.py                       # rebuild professional-dictionary layer
python tools/wt.py probe --pair en              # vocabulary hit / gap report
python tools/wt.py fill  --pair en --pass p2    # local Hy-MT2 gap fill
python tools/wt.py pack  --pair en              # re-pack data/ + meta/files/README
```

## Toolchain

```
WordTranslation/
├── README.md / meta.json / files.json   # dataset card + sidecars (published)
├── data/                                # the only published artifact: <src>_<dst>.jsonl.gz
├── build/                               # build inputs (not published)
│   ├── raw/                             #   source dumps (wiktextract en/zh)
│   ├── pro/                             #   professional dictionary layer (<src>_<dst>.jsonl)
│   └── <pair>/{cache,llm,manual,...}    #   per-pair intermediates
├── tools/wt.py                          # probe | fill | pack, single file
├── docs/                                # plans and research
└── work/<pair>/{hymt,lmt}/<pass>/       # model gap-fill layers (pack input)
```

| subcommand | effect |
|------------|--------|
| `probe --pair en\|zh` | vocabulary hits and gaps, both directions |
| `fill --pair en --pass p1\|p2 [--engine hymt\|lmt] [--langs a,b] [--conc 8] [--limit N]` | fill the gaps word by word → `work/<pair>/<engine>/<pass>/<code>.jsonl` (append-only, resumable, Ctrl-C safe) |
| `pack --pair en [--pass both] [--base clean\|merged] [--no-pro]` | pro + base + hymt/lmt layers → re-pack `data/`, rebuild `meta.json` / `files.json` / `README.md` |

- `--base clean` (default) = professional dictionaries (pro_) + Wiktionary (pairs_) +
  PanLex (panlex_), human-curated only; the reverse direction is its inversion.
  `merged` = the old four-layer merge (deprecated, kept for comparison).
- The en ⇄ zh pair is produced twice with different content; the flat layout keeps one of
  each: `en_zh` from the zh p2 pipeline (XToZh) and `zh_en` from the en p2 pipeline (XToEn),
  matching the "definition-language family first" rule of the site consumer
  `VocabRadar/web/scripts/init_web.js`. Each of the two p1 passes skips that code
  (`wt.CROSS_SKIP`) so packing cannot overwrite the other.
- The model is served by `llama.cpp`'s `llama-server`; `wt.py` starts, reuses and shuts it
  down on its own.
- Environment variables: `WT_LLAMA_SERVER`, `WT_HYMT_GGUF`, `WT_LMT_GGUF`, `WT_PORT`
  (default 8791), `WT_WF_DATA` (the vocabradar/wordfreq vocabulary directory).

## License

- Professional dictionaries: ECDICT (MIT), CC-CEDICT (CC BY-SA 4.0), JMdict (CC BY-SA 4.0),
  HanDeDict (CC BY-SA 2.0), CFDICT (CC BY-SA 3.0), Folkets lexikon (CC BY-SA 2.5) — all
  compatible with this dataset's CC BY-SA 4.0 licence; attribution is given here and in
  `meta.json`.
- wiktextract/kaikki.org extraction: CC BY-SA 4.0 (Wiktionary, dual-licensed GFDL).
- PanLex supplement: CC0 (2024-03-01 dump).
- vocabulary, taken from the vocabradar/wordfreq dataset: MIT.
- Hunyuan-MT2-1.8B / LMT-60-1.7B gap-fill layers: machine-generated, disclosed here and
  in `meta.json`; both models Apache-2.0.

## About VocabRadar

This dataset is a **VocabRadar** project — the vocabulary radar. The
[VocabRadar browser extension](https://vocabradar.com) marks up the words you do not know
yet while you watch videos or browse the web: definitions in place, translation, bilingual
subtitles and annotated subtitles. Whatever you looked up can go on to
[vocabradar.com](https://vocabradar.com), which turns it into related exercises and games
so the words actually stick.

---

<a id="zh"></a>

# WordTranslation —— 离线单词翻译包（vocabradar/wordfreq 词表）

## 这是什么

**43 种语言**的离线单词翻译包，围绕英文与中文两翼：把某语言清洗后的词表里的每个词配上译文。
**词表直接来自 [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
数据集** —— 它就是本数据集的直接源头：这里翻译的就是它的 `small_<code>` 词表，按它在数据集里的
原顺序逐词来。共 166 个 gzip JSONL 文件，每对语言一个（合计 83.5 MiB，
单个 0.09–1.07 MiB）；`en ⇄ X` 与 `zh ⇄ X` 共用同一批 41 种伙伴语言（40 + 泰语）。

## 有什么用

- **离线词典**：解压一个文件，整对语言就是内存里的字典 —— 不联网、不要 API key、没有按次计费。
- **给自己的应用做生词提示** —— [VocabRadar 浏览器扩展](https://vocabradar.com) 阅读时显示的释义与字幕就是这份数据。
- **按频序取词与实验**：行序即 vocabradar/wordfreq 词表的排名（最高频的词在最前），也可当低资源语言对的翻译 / 词表实验数据。
- **查缺口**：下面的命中率表按语言给出「多少词真的有译文」，据此判断某一对够不够用。

## 怎么构建的

**词**：源语言的 `small_<code>` 列表，原样取自
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) 数据集，保留词频顺序。

**译文**：有许可兼容的专业双语词典时**优先用专业词典** —— **ECDICT**（en→zh，MIT）、
**CC-CEDICT**（zh→en，CC BY-SA 4.0）、**JMdict**（ja↔en，CC BY-SA 4.0）、
**HanDeDict**（zh↔de，CC BY-SA 2.0）、**CFDICT**（zh↔fr，CC BY-SA 3.0）、
**Folkets lexikon**（sv↔en，CC BY-SA 2.5）。单向词典的反向按「释义→词条」反转，
且只保留目标语词表里真实存在的词。其余基础数据只取人工编撰的词典：英文 / 中文
Wiktionary（经 [wiktextract](https://github.com/tatuylonen/wiktextract) /
[kaikki.org](https://kaikki.org) 抽取，CC BY-SA 4.0）+ 可得的 PanLex（CC0）。
剩余词表缺口由本地模型 **Hunyuan-MT2-1.8B Q4_K_M** 补译（Apache-2.0，llama.cpp
跑官方 GGUF）；它不支持的语言再由第二层本地模型 **LMT-60-1.7B Q4_K_M** 补
（Apache-2.0，NiuTrans）—— 同为机器生成。反查得到的译文对**封闭类词**
（冠词、系动词、助词）可靠性较低：德语 `der` 可能落到实词义，法语 `est` 可能被读成“东”。
HanDeDict/CFDICT 中语法助词的词条是用法说明而非单词对译；两类情况都按原样保留并在此注明。

**发布前质检**：每个包发布前过一遍内容级质检（`tools/qc_check.py`）——模型失控复读
（如法中 `aïe` 曾被译成 呜呜呜呜… 这类单字连跑）、占位语/模型泄漏、乱码与脚本违规
一律剔除；游离附加号开头的词典残留原位修复；被清空的词走本地模型级联补译并复检。
规则明细与 2026-10 清理记录见 `docs/`。

所有方向共用一个目录：每对语言一个 gzip JSONL 文件 `data/<src>_<dst>.jsonl.gz`
（en ⇄ zh 只存一份）。每行一个 JSON 对象，字段固定 —— 源词 `word` 及其 `translations`。

## 文件结构

```
├── README.md
├── meta.json                   # 各方向的来源、上限与语言统计
├── files.json                  # 每个文件的大小（字节）与 SHA-256
└── data/                       # 166 个文件：<src>_<dst>.jsonl.gz
```

## 数据格式

```json
{"word": "house", "translations": ["casa", "hogar"]}
```

- 每行字段名固定（`word`、`translations`），HF 的 Dataset Viewer 才能把每个文件渲染成
  两列表格（`word: string`、`translations: list<string>`），而不是每个源词一列。
- `data/<src>_<dst>.jsonl.gz` 把 `src` 词表（[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
  的 `small_<src>` 列表）译成 `dst`；行序按该列表的排名，重建结果确定。
- 译文按大小写不敏感去重，每词上限 10 条；补译条目上限 3 条，
  并与其他层一样过每语言的 Unicode script 白名单。
- **补译层是机器生成的，可能有错。**

## 语言与命中率

*命中率* 是该语言词表里有至少一条译文的词所占比例 —— **不是** vocabradar/wordfreq
那张表的 *cumulative coverage*（那是语料 token 覆盖率）；这里的「命中」只表示
「该词表词在本文件里有译文」。*自称* 是该语言自己的叫法（与 vocabradar/wordfreq 卡的
native name 同源）。*首行* 是该行自己那个文件的第一行，原样照抄 ——
最高频的源词（即本数据集所依据的
[vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) 词表里的第一个词）
加上给它找到的译文。一眼同时核对两头：词表（第一个词对不对）与译文语种（译文像不像该语言）。
末行 **合计** 的*已译词数*与*条目数*为直接相加；*命中率*为加权合计
（Σ 已译词数 / Σ 词表分母）—— 反向方向各语言分母不同，算术平均没有意义。

### en → X (EnToX)

英文维基词典来源；词表 = vocabradar/wordfreq 的 `small_en` — 40 种语言

| 代码 | 语言 | 自称 | 首行 | 已译词数 | 命中率 | 条目数 |
|------|------|------|------|----------|--------|--------|
| ar | Arabic | العربية | `{"word":"the","translations":["الـ","ال"]}` | 28,223 | 100.0% | 111,486 |
| bg | Bulgarian | български | `{"word":"the","translations":["-та","-то","-те","по"]}` | 28,220 | 100.0% | 74,713 |
| bn | Bengali | বাংলা | `{"word":"the","translations":["-রা","-এরা","-গুলা","-গুলো","-টা","-টি","গাছা","গাছি","মহাবিশ্ব"]}` | 28,223 | 100.0% | 67,972 |
| ca | Catalan | català | `{"word":"the","translations":["el","la","l' els m pl les","es","sa","ets","sos","ses","els","les"]}` | 28,223 | 100.0% | 84,343 |
| cs | Czech | čeština | `{"word":"the","translations":["ta","ten","to","určitý člen","člen určitý"]}` | 28,223 | 100.0% | 106,829 |
| da | Danish | dansk | `{"word":"the","translations":["de","den","det","en","et","-et","-en","-ne"]}` | 28,223 | 100.0% | 63,132 |
| de | German | Deutsch | `{"word":"the","translations":["der","die","das","de","dr","den","dieser","umso","Platz","der die das die"]}` | 28,223 | 100.0% | 146,827 |
| el | Greek | Ελληνικά | `{"word":"the","translations":["ο","ὁ","στον","στη","στο","άρθρο","η","οι","παράμεσος","στα"]}` | 28,179 | 99.8% | 90,613 |
| es | Spanish | español | `{"word":"the","translations":["el","la","los","las","lo","el la los las","entonces","pero","pues"]}` | 28,223 | 100.0% | 126,135 |
| fa | Persian | فارسی | `{"word":"the","translations":["این","آن","ال","باسلیقون","ثلاثة غساله","دلیجه","ساز","سفیدرود","سنده","قبلة"]}` | 28,223 | 100.0% | 91,682 |
| fi | Finnish | suomi | `{"word":"the","translations":["se","-ni","-si","-nsa","-nsä","-mme","-nne","minun","sinun","hänen"]}` | 28,223 | 100.0% | 128,415 |
| fil | Filipino | Filipino | `{"word":"the","translations":["ang","nang","mga"]}` | 28,223 | 100.0% | 48,367 |
| fr | French | français | `{"word":"the","translations":["le","la","les","l'","comp.","colloquial or regional usage","acquitter","au","aux","ce"]}` | 28,223 | 100.0% | 132,443 |
| he | Hebrew | עברית | `{"word":"the","translations":["ה־","ה"]}` | 28,222 | 100.0% | 50,356 |
| hi | Hindi | हिन्दी | `{"word":"the","translations":["जिस काम के पूरे करने में सभी लगे हों","ईसामसीह","दि","यह","वह","वही"]}` | 28,223 | 100.0% | 106,614 |
| hu | Hungarian | magyar | `{"word":"the","translations":["a","az"]}` | 28,223 | 100.0% | 104,597 |
| id | Indonesian | Bahasa Indonesia | `{"word":"the","translations":["si","sang","itu","al","-nya","kian"]}` | 28,223 | 100.0% | 93,819 |
| is | Icelandic | íslenska | `{"word":"the","translations":["-inn","hinn","hið","-in","-nar","-ið","-nir"]}` | 28,223 | 100.0% | 57,806 |
| it | Italian | italiano | `{"word":"the","translations":["il","lo","la","l'","i","gli","le","li","lì","gl’"]}` | 28,223 | 100.0% | 120,328 |
| ja | Japanese | 日本語 | `{"word":"the","translations":["その","正に","正しく","ザ","這","あの","其の","定冠詞","当該","死因"]}` | 28,212 | 100.0% | 145,314 |
| ko | Korean | 한국어 | `{"word":"the","translations":["-을수록","그","그만큼$2$","저","하면 할수록","하면 할수록 그만큼 더"]}` | 28,217 | 100.0% | 104,823 |
| lt | Lithuanian | lietuvių | `{"word":"the","translations":["tai"]}` | 28,223 | 100.0% | 42,549 |
| lv | Latvian | latviešu | `{"word":"the","translations":["sirdi"]}` | 28,211 | 100.0% | 38,168 |
| mk | Macedonian | македонски | `{"word":"the","translations":["-ов","-те","-от","многуте","највеќе","најголем дел","најмногу","онака","постојано","-во"]}` | 28,184 | 99.9% | 47,766 |
| ms | Malay | Bahasa Melayu | `{"word":"the","translations":["sang","-nya","itu","ini","si","semakin..., semakin...","lagi..., lagi..."]}` | 28,223 | 100.0% | 85,179 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"the","translations":["det","den","-et","-en","-a","-i","de","desto","jo","-one"]}` | 28,223 | 100.0% | 68,517 |
| nl | Dutch | Nederlands | `{"word":"the","translations":["de","het","aan de","aan het","des te","die","hoe","naar de","naar het","’t"]}` | 28,223 | 100.0% | 107,151 |
| pl | Polish | polski | `{"word":"the","translations":["ten","czym","im","przedimek określony","ta","to","te"]}` | 28,223 | 100.0% | 95,604 |
| pt | Portuguese | português | `{"word":"the","translations":["o","a","os","as","o a os as"]}` | 28,223 | 100.0% | 107,945 |
| ro | Romanian | română | `{"word":"the","translations":["-ul","-a","cel","cea","-i","cele","-le"]}` | 28,223 | 100.0% | 61,507 |
| ru | Russian | русский | `{"word":"the","translations":["на ходу","определенный артикль","определённый артикль","подходящий","такой","тем","тот","чем","чем... тем"]}` | 28,219 | 100.0% | 148,990 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"the","translations":["Alpe","Antarktika","Atlantik","Balkan","Baltik","Drava","Drina","Dunav","Holandija","Jadran"]}` | 28,209 | 100.0% | 118,146 |
| sk | Slovak | slovenčina | `{"word":"the","translations":["ten","to","tá"]}` | 28,223 | 100.0% | 98,458 |
| sl | Slovenian | slovenščina | `{"word":"the","translations":["the"]}` | 28,223 | 100.0% | 76,078 |
| sv | Swedish | svenska | `{"word":"the","translations":["den","dess","desto","-en","de","det","ju","vederbörande","vintergatan","överklassen"]}` | 28,223 | 100.0% | 100,554 |
| ta | Tamil | தமிழ் | `{"word":"the","translations":["அது"]}` | 28,223 | 100.0% | 72,940 |
| th | Thai | ไทย | `{"word":"the","translations":["นั้น"]}` | 28,188 | 99.9% | 28,312 |
| tr | Turkish | Türkçe | `{"word":"the","translations":["bir","harfi tarif","ne kadar","üstlenmek"]}` | 28,223 | 100.0% | 99,531 |
| uk | Ukrainian | українська | `{"word":"the","translations":["те"]}` | 28,221 | 100.0% | 71,637 |
| ur | Urdu | اردو | `{"word":"the","translations":["ال"]}` | 28,223 | 100.0% | 60,976 |
| vi | Vietnamese | Tiếng Việt | `{"word":"the","translations":["con","càng","cái","duy nhất","này","ấy"]}` | 28,223 | 100.0% | 95,230 |
| **合计** | 41 种语言 | — | — | 1,156,972 | 100.0% | 3,681,852 |

### X → en (XToEn)

英文维基词典来源反转；词表 = vocabradar/wordfreq 的 `small_<code>` — 41 种语言

| 代码 | 语言 | 自称 | 首行 | 已译词数 | 命中率 | 条目数 |
|------|------|------|------|----------|--------|--------|
| ar | Arabic | العربية | `{"word":"في","translations":["a","in","on","at","by","into","through","during","times","within"]}` | 55,606 | 100.0% | 101,618 |
| bg | Bulgarian | български | `{"word":"на","translations":["of","in","on","at","onto","lo"]}` | 35,848 | 100.0% | 55,492 |
| bn | Bengali | বাংলা | `{"word":"না","translations":["not","no","don't","never","without","please","non","boat","un","na"]}` | 33,045 | 99.9% | 50,042 |
| ca | Catalan | català | `{"word":"de","translations":["of","in","with","from","about","more","off","again","coral","dee"]}` | 27,028 | 100.0% | 60,056 |
| cs | Czech | čeština | `{"word":"a","translations":["and","a","that","who","which","any","both","recent","double","plus"]}` | 51,744 | 100.0% | 92,063 |
| da | Danish | dansk | `{"word":"i","translations":["to","of","a","in","for","you","on","with","at","by"]}` | 29,321 | 100.0% | 50,479 |
| de | German | Deutsch | `{"word":"die","translations":["the","a","that","this","but","an","all","what","who","which"]}` | 38,989 | 100.0% | 114,757 |
| el | Greek | Ελληνικά | `{"word":"και","translations":["and","that","but","which","also","too","both"]}` | 43,188 | 100.0% | 61,778 |
| es | Spanish | español | `{"word":"de","translations":["of","in","for","on","with","be","as","at","by","from"]}` | 34,740 | 100.0% | 98,038 |
| fa | Persian | فارسی | `{"word":"و","translations":["and","both"]}` | 30,108 | 100.0% | 57,014 |
| fi | Finnish | suomi | `{"word":"ja","translations":["and","so","also","too","both","plus","likewise","wedge"]}` | 59,143 | 100.0% | 107,690 |
| fil | Filipino | Filipino | `{"word":"sa","translations":["to","of","a","in","for","on","with","at","by","from"]}` | 30,098 | 100.0% | 40,648 |
| fr | French | français | `{"word":"de","translations":["to","of","a","in","for","on","with","be","as","at"]}` | 31,203 | 100.0% | 100,218 |
| he | Hebrew | עברית | `{"word":"את","translations":["you","with","me","alongside","amongst","thou","shovel","spade"]}` | 57,376 | 99.9% | 68,773 |
| hi | Hindi | हिन्दी | `{"word":"के","translations":["of","in","for","with","as","have","by","from","his","about"]}` | 24,031 | 100.0% | 56,346 |
| hu | Hungarian | magyar | `{"word":"a","translations":["the","a","black","amps"]}` | 46,525 | 100.0% | 81,700 |
| id | Indonesian | Bahasa Indonesia | `{"word":"yang","translations":["that","who","which","second","third","whose","rel"]}` | 30,967 | 100.0% | 77,623 |
| is | Icelandic | íslenska | `{"word":"og","translations":["and","but","which","also","both","plus"]}` | 42,207 | 100.0% | 56,957 |
| it | Italian | italiano | `{"word":"di","translations":["to","of","in","for","that","on","with","be","at","by"]}` | 35,954 | 100.0% | 96,114 |
| ja | Japanese | 日本語 | `{"word":"の","translations":["indicates possessive","nominalizes verbs and adjectives","substitutes for \"ga\" in subordinate phrases","indicates a confident conclusion","indicates emotional emphasis","indicates question","field","plain","hidden interior part","wild"]}` | 27,856 | 100.0% | 138,071 |
| ko | Korean | 한국어 | `{"word":"이","translations":["and","that","you","this","be","he","but","she","only","two"]}` | 26,807 | 100.0% | 48,935 |
| lt | Lithuanian | lietuvių | `{"word":"ir","translations":["and","even","afterward"]}` | 63,973 | 100.0% | 71,616 |
| lv | Latvian | latviešu | `{"word":"un","translations":["and"]}` | 45,464 | 100.0% | 51,239 |
| mk | Macedonian | македонски | `{"word":"на","translations":["of","for","on","at","per"]}` | 32,925 | 100.0% | 42,850 |
| ms | Malay | Bahasa Melayu | `{"word":"yang","translations":["that","one","which","change","cash","coins","umbrella"]}` | 28,571 | 100.0% | 69,966 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"i","translations":["to","of","a","in","for","you","on","with","at","by"]}` | 25,994 | 100.0% | 48,694 |
| nl | Dutch | Nederlands | `{"word":"de","translations":["the","you","this","one","able","bus","exposure","repaid","earthy"]}` | 28,715 | 100.0% | 78,061 |
| pl | Polish | polski | `{"word":"w","translations":["to","of","a","in","for","on","with","at","by","an"]}` | 49,664 | 100.0% | 81,502 |
| pt | Portuguese | português | `{"word":"de","translations":["of","for","with","by","from","about","something","old","someone","hunger"]}` | 33,123 | 100.0% | 82,780 |
| ro | Romanian | română | `{"word":"de","translations":["of","for","on","by","from","since","against"]}` | 43,279 | 100.0% | 62,582 |
| ru | Russian | русский | `{"word":"в","translations":["to","of","a","in","for","on","with","as","at","by"]}` | 59,604 | 100.0% | 122,769 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"je","translations":["is","are","if","has","her","did","sued"]}` | 54,698 | 100.0% | 97,376 |
| sk | Slovak | slovenčina | `{"word":"a","translations":["and","amps"]}` | 59,414 | 100.0% | 101,829 |
| sl | Slovenian | slovenščina | `{"word":"je","translations":["is"]}` | 53,882 | 100.0% | 77,313 |
| sv | Swedish | svenska | `{"word":"är","translations":["is","are","am","result","arise"]}` | 30,515 | 100.0% | 66,415 |
| ta | Tamil | தமிழ் | `{"word":"ஒரு","translations":["a","an","hour","sole","sheep","mono"]}` | 64,751 | 100.0% | 83,531 |
| th | Thai | ไทย | `{"word":"ที่","translations":["place","that","which","who"]}` | 39,499 | 99.5% | 39,856 |
| tr | Turkish | Türkçe | `{"word":"ve","translations":["and","so","both","species","vee"]}` | 63,130 | 100.0% | 95,737 |
| uk | Ukrainian | українська | `{"word":"в","translations":["to","in","have","at","into","per"]}` | 46,285 | 100.0% | 62,505 |
| ur | Urdu | اردو | `{"word":"کے","translations":["of","at"]}` | 22,442 | 100.0% | 37,850 |
| vi | Vietnamese | Tiếng Việt | `{"word":"là","translations":["is","that","was","be","as","are","were","been","how","some"]}` | 10,519 | 100.0% | 26,597 |
| zh | Chinese | 中文 | `{"word":"的","translations":["of","s","used after an attribute when it modifies a noun","used at the end of a declarative sentence for emphasis","also pr. [di4] or [di5] in poetry and songs","a taxi","a cab","really and truly","bull's-eye","target"]}` | 35,723 | 100.0% | 145,872 |
| **合计** | 42 种语言 | — | — | 1,683,954 | 100.0% | 3,161,352 |

### zh → X (ZhToX)

中文维基词典来源；词表 = vocabradar/wordfreq 的 `small_zh` — 40 种语言

| 代码 | 语言 | 自称 | 首行 | 已译词数 | 命中率 | 条目数 |
|------|------|------|------|----------|--------|--------|
| ar | Arabic | العربية | `{"word":"的","translations":["ال"]}` | 35,723 | 100.0% | 37,413 |
| bg | Bulgarian | български | `{"word":"的","translations":["ето"]}` | 35,702 | 99.9% | 36,852 |
| bn | Bengali | বাংলা | `{"word":"的","translations":["ের"]}` | 35,723 | 100.0% | 36,298 |
| ca | Catalan | català | `{"word":"的","translations":["de"]}` | 35,721 | 100.0% | 36,571 |
| cs | Czech | čeština | `{"word":"的","translations":["Jeho"]}` | 35,723 | 100.0% | 36,903 |
| da | Danish | dansk | `{"word":"的","translations":["Dan"]}` | 35,722 | 100.0% | 36,601 |
| de | German | Deutsch | `{"word":"的","translations":["wird nach einem Adjektiv oder einer Attributphrase verwendet","wird nach einem Verb verwendet, um das Subjekt, die Zeit","Ziel, das Schwarze","klar"]}` | 35,721 | 100.0% | 60,922 |
| el | Greek | Ελληνικά | `{"word":"的","translations":["του"]}` | 35,229 | 98.6% | 36,199 |
| es | Spanish | español | `{"word":"的","translations":["de"]}` | 35,723 | 100.0% | 38,381 |
| fa | Persian | فارسی | `{"word":"的","translations":["که"]}` | 35,721 | 100.0% | 37,234 |
| fi | Finnish | suomi | `{"word":"的","translations":["Finnish"]}` | 35,704 | 99.9% | 37,635 |
| fil | Filipino | Filipino | `{"word":"的","translations":["ay"]}` | 35,722 | 100.0% | 36,531 |
| fr | French | français | `{"word":"的","translations":["de","utilisé après un adjectif, un nom","centre de la cible","but","objectif","voir","vrai"]}` | 35,723 | 100.0% | 67,607 |
| he | Hebrew | עברית | `{"word":"的","translations":["של"]}` | 35,714 | 100.0% | 36,359 |
| hi | Hindi | हिन्दी | `{"word":"的","translations":["का"]}` | 35,722 | 100.0% | 37,985 |
| hu | Hungarian | magyar | `{"word":"的","translations":["És"]}` | 35,720 | 100.0% | 37,238 |
| id | Indonesian | Bahasa Indonesia | `{"word":"的","translations":["adalah"]}` | 35,723 | 100.0% | 36,491 |
| is | Icelandic | íslenska | `{"word":"的","translations":["Er"]}` | 35,723 | 100.0% | 36,535 |
| it | Italian | italiano | `{"word":"的","translations":["di"]}` | 35,723 | 100.0% | 37,266 |
| ja | Japanese | 日本語 | `{"word":"的","translations":["の"]}` | 35,706 | 100.0% | 38,413 |
| ko | Korean | 한국어 | `{"word":"的","translations":["-의"]}` | 35,706 | 100.0% | 36,859 |
| lt | Lithuanian | lietuvių | `{"word":"的","translations":["ž"]}` | 35,721 | 100.0% | 36,204 |
| lv | Latvian | latviešu | `{"word":"的","translations":["Latv"]}` | 35,663 | 99.8% | 36,253 |
| mk | Macedonian | македонски | `{"word":"的","translations":["Македонски"]}` | 35,587 | 99.6% | 36,528 |
| ms | Malay | Bahasa Melayu | `{"word":"的","translations":["nya"]}` | 35,723 | 100.0% | 36,659 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"的","translations":["Det"]}` | 35,721 | 100.0% | 36,475 |
| nl | Dutch | Nederlands | `{"word":"的","translations":["van"]}` | 35,723 | 100.0% | 37,389 |
| pl | Polish | polski | `{"word":"的","translations":["tak"]}` | 35,723 | 100.0% | 37,637 |
| pt | Portuguese | português | `{"word":"的","translations":["do"]}` | 35,719 | 100.0% | 37,492 |
| ro | Romanian | română | `{"word":"的","translations":["de”"]}` | 35,719 | 100.0% | 36,937 |
| ru | Russian | русский | `{"word":"的","translations":["дом"]}` | 35,694 | 99.9% | 63,021 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"的","translations":["Srbijanski"]}` | 35,494 | 99.4% | 37,198 |
| sk | Slovak | slovenčina | `{"word":"的","translations":["So"]}` | 35,723 | 100.0% | 36,532 |
| sl | Slovenian | slovenščina | `{"word":"的","translations":["Slovenski"]}` | 35,721 | 100.0% | 36,300 |
| sv | Swedish | svenska | `{"word":"的","translations":["av"]}` | 35,723 | 100.0% | 37,092 |
| ta | Tamil | தமிழ் | `{"word":"的","translations":["அதன்"]}` | 35,723 | 100.0% | 36,048 |
| th | Thai | ไทย | `{"word":"的","translations":["ของ"]}` | 34,357 | 96.2% | 34,368 |
| tr | Turkish | Türkçe | `{"word":"的","translations":["oldu"]}` | 35,723 | 100.0% | 37,256 |
| uk | Ukrainian | українська | `{"word":"的","translations":["Українською"]}` | 35,699 | 99.9% | 37,623 |
| ur | Urdu | اردو | `{"word":"的","translations":["کی"]}` | 35,723 | 100.0% | 36,683 |
| vi | Vietnamese | Tiếng Việt | `{"word":"的","translations":["của"]}` | 35,722 | 100.0% | 37,470 |
| **合计** | 41 种语言 | — | — | 1,462,195 | 99.8% | 1,593,458 |

### X → zh (XToZh)

中文维基词典来源反转；词表 = vocabradar/wordfreq 的 `small_<code>` — 41 种语言

| 代码 | 语言 | 自称 | 首行 | 已译词数 | 命中率 | 条目数 |
|------|------|------|------|----------|--------|--------|
| ar | Arabic | العربية | `{"word":"في","translations":["在"]}` | 55,553 | 99.9% | 55,814 |
| bg | Bulgarian | български | `{"word":"на","translations":["在"]}` | 35,768 | 99.8% | 35,904 |
| bn | Bengali | বাংলা | `{"word":"না","translations":["从不"]}` | 32,791 | 99.2% | 32,874 |
| ca | Catalan | català | `{"word":"de","translations":["德"]}` | 27,006 | 99.9% | 27,148 |
| cs | Czech | čeština | `{"word":"a","translations":["a"]}` | 51,708 | 99.9% | 51,825 |
| da | Danish | dansk | `{"word":"i","translations":["i"]}` | 29,310 | 100.0% | 29,437 |
| de | German | Deutsch | `{"word":"die","translations":["是","这些"]}` | 38,975 | 100.0% | 61,494 |
| el | Greek | Ελληνικά | `{"word":"και","translations":["和"]}` | 42,952 | 99.4% | 43,061 |
| en | English | English | `{"word":"the","translations":["那"]}` | 28,219 | 100.0% | 84,155 |
| es | Spanish | español | `{"word":"de","translations":["德"]}` | 34,731 | 100.0% | 35,055 |
| fa | Persian | فارسی | `{"word":"و","translations":["和"]}` | 30,070 | 99.9% | 30,277 |
| fi | Finnish | suomi | `{"word":"ja","translations":["是"]}` | 59,030 | 99.8% | 59,234 |
| fil | Filipino | Filipino | `{"word":"sa","translations":["萨"]}` | 30,093 | 100.0% | 30,167 |
| fr | French | français | `{"word":"de","translations":["的","与","于","从","由","从中","乎","为了"]}` | 31,196 | 100.0% | 50,536 |
| he | Hebrew | עברית | `{"word":"את","translations":["你"]}` | 57,300 | 99.8% | 57,431 |
| hi | Hindi | हिन्दी | `{"word":"के","translations":["科"]}` | 23,800 | 99.0% | 24,036 |
| hu | Hungarian | magyar | `{"word":"a","translations":["a"]}` | 46,519 | 100.0% | 46,669 |
| id | Indonesian | Bahasa Indonesia | `{"word":"yang","translations":["杨"]}` | 30,957 | 100.0% | 31,060 |
| is | Icelandic | íslenska | `{"word":"og","translations":["og"]}` | 42,189 | 100.0% | 42,280 |
| it | Italian | italiano | `{"word":"di","translations":["迪"]}` | 35,947 | 100.0% | 36,154 |
| ja | Japanese | 日本語 | `{"word":"の","translations":["的"]}` | 27,822 | 99.9% | 28,038 |
| ko | Korean | 한국어 | `{"word":"이","translations":["牙齿","二"]}` | 26,758 | 99.8% | 26,847 |
| lt | Lithuanian | lietuvių | `{"word":"ir","translations":["ir"]}` | 63,905 | 99.9% | 63,978 |
| lv | Latvian | latviešu | `{"word":"un","translations":["不"]}` | 45,397 | 99.9% | 45,471 |
| mk | Macedonian | македонски | `{"word":"на","translations":["在"]}` | 32,840 | 99.7% | 32,954 |
| ms | Malay | Bahasa Melayu | `{"word":"yang","translations":["杨"]}` | 28,562 | 100.0% | 28,673 |
| nb | Norwegian Bokmål | norsk bokmål | `{"word":"i","translations":["你"]}` | 25,985 | 100.0% | 26,067 |
| nl | Dutch | Nederlands | `{"word":"de","translations":["de"]}` | 28,708 | 100.0% | 28,879 |
| pl | Polish | polski | `{"word":"w","translations":["w"]}` | 49,651 | 100.0% | 49,832 |
| pt | Portuguese | português | `{"word":"de","translations":["de"]}` | 33,117 | 100.0% | 33,370 |
| ro | Romanian | română | `{"word":"de","translations":["德"]}` | 43,271 | 100.0% | 43,415 |
| ru | Russian | русский | `{"word":"в","translations":["就是","同时","如何","其中","影响","目前","参加","具有","实现","是不是"]}` | 59,388 | 99.6% | 72,489 |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | `{"word":"je","translations":["你"]}` | 54,687 | 100.0% | 54,724 |
| sk | Slovak | slovenčina | `{"word":"a","translations":["a"]}` | 59,390 | 100.0% | 59,484 |
| sl | Slovenian | slovenščina | `{"word":"je","translations":["je"]}` | 53,870 | 100.0% | 53,934 |
| sv | Swedish | svenska | `{"word":"är","translations":["是"]}` | 30,507 | 100.0% | 30,680 |
| ta | Tamil | தமிழ் | `{"word":"ஒரு","translations":["一个"]}` | 64,563 | 99.7% | 64,609 |
| th | Thai | ไทย | `{"word":"ที่","translations":["地点","地點"]}` | 34,098 | 85.9% | 34,634 |
| tr | Turkish | Türkçe | `{"word":"ve","translations":["ve"]}` | 63,011 | 99.8% | 63,200 |
| uk | Ukrainian | українська | `{"word":"в","translations":["在"]}` | 46,084 | 99.6% | 46,236 |
| ur | Urdu | اردو | `{"word":"کے","translations":["的"]}` | 22,415 | 99.9% | 22,547 |
| vi | Vietnamese | Tiếng Việt | `{"word":"là","translations":["是"]}` | 10,510 | 99.9% | 10,589 |
| **合计** | 42 种语言 | — | — | 1,668,653 | 99.5% | 1,785,261 |

## 重新生成

```bash
python tools/build_pro.py                       # 重建专业词典层 build/pro
python tools/wt.py probe --pair en              # 词表命中与缺口报告
python tools/wt.py fill  --pair en --pass p2    # 本地 Hy-MT2 补缺口
python tools/wt.py pack  --pair en              # 重打包 data/ + meta/files/README
```

## 工具链

```
WordTranslation/
├── README.md / meta.json / files.json   # 数据集卡 + 边车文件（发布）
├── data/                                # 唯一发布产物：<src>_<dst>.jsonl.gz
├── build/                               # 构建输入（不发布）
│   ├── raw/                             #   源 dump（wiktextract en/zh）
│   ├── pro/                             #   专业词典层（<src>_<dst>.jsonl）
│   └── <pair>/{cache,llm,manual,...}    #   各对的中间产物
├── tools/wt.py                          # probe | fill | pack 单文件工具链
├── docs/                                # 规划与调研
└── work/<pair>/{hymt,lmt}/<pass>/       # 模型补译层（pack 的输入）
```

| 子命令 | 作用 |
|--------|------|
| `probe --pair en\|zh` | 正/反双方向命中与缺口报告 |
| `fill --pair en --pass p1\|p2 [--engine hymt\|lmt] [--langs a,b] [--conc 8] [--limit N]` | 逐词补缺 → `work/<pair>/<engine>/<pass>/<code>.jsonl`（追加幂等，Ctrl-C 断点续跑） |
| `pack --pair en [--pass both] [--base clean\|merged] [--no-pro]` | pro + base + hymt/lmt 层 → 重打包 `data/`，重建 `meta.json` / `files.json` / `README.md` |

- `--base clean`（缺省）= 专业词典(pro_) + 维基(pairs_) + PanLex(panlex_) 纯人工来源，
  反向为其反转；`merged` = 旧管线四层合并包（已弃用，留作对照）。
- en ⇄ zh 这一对由**两套管线各产一份且内容不同**；扁平布局下只保留一份：
  `en_zh` 取 zh 对 p2（XToZh 管线），`zh_en` 取 en 对 p2（XToEn 管线），
  与网站消费端 `VocabRadar/web/scripts/init_web.js` 的「释义语族优先」口径一致。
  对应两对的 p1 自动跳过该 code（`wt.CROSS_SKIP`），避免 pack 时互相覆盖。
- 模型服务由 `llama.cpp` 的 `llama-server` 提供，`wt.py` 自动拉起/复用/关闭。
- 环境变量：`WT_LLAMA_SERVER`、`WT_HYMT_GGUF`、`WT_LMT_GGUF`、`WT_PORT`（缺省 8791）、
  `WT_WF_DATA`（vocabradar/wordfreq 词表目录）。

## 许可证

- 专业词典：ECDICT（MIT）、CC-CEDICT（CC BY-SA 4.0）、JMdict（CC BY-SA 4.0）、
  HanDeDict（CC BY-SA 2.0）、CFDICT（CC BY-SA 3.0）、Folkets lexikon（CC BY-SA 2.5）——
  均与本数据集的 CC BY-SA 4.0 兼容；署名见本节与 `meta.json`。
- wiktextract/kaikki.org 抽取：CC BY-SA 4.0（Wiktionary，另以 GFDL 双许可）。
- PanLex 补充：CC0（2024-03-01 dump）。
- 词表：取自 vocabradar/wordfreq 数据集，MIT。
- Hunyuan-MT2-1.8B / LMT-60-1.7B 补译层：机器生成，已在此与 `meta.json` 中披露；
  两个模型均为 Apache-2.0。

## 关于 VocabRadar

这项工作是 **VocabRadar**（词汇雷达）的工作：[VocabRadar 浏览器扩展](https://vocabradar.com)
让你在看视频、刷网页时把还不认识的生词就地标注出来 —— 释义、翻译、双语字幕、注释字幕；
查过的词还能送到 [vocabradar.com](https://vocabradar.com)，自动生成相关习题与游戏，把词真正记住。
