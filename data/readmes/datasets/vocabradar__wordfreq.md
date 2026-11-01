---
language: [ar, bg, bn, ca, cs, da, de, el, en, es, fa, fi, fil, fr, he, hi, hu, id, is, it, ja, ko, lt, lv, mk, ms, nb, nl, pl, pt, ro, ru, sh, sk, sl, sv, ta, th, tr, uk, ur, vi, zh]
license: mit
multilinguality: multilingual
pretty_name: Cleaned Word Frequency Lists (43 languages) / 清洗版词频表（43 语）
size_categories:
- 1M<n<10M
---

# Cleaned Word Frequency Lists (43 languages)

Small word-frequency lists for 43 languages, derived from [wordfreq](https://github.com/rspeer/wordfreq) 3.0.2 and cleaned for use as offline frequency dictionaries: one gzip-compressed MessagePack file per language, roughly 8 MB in total. These lists are also the direct vocabulary source of [vocabradar/WordTranslation](https://huggingface.co/datasets/vocabradar/WordTranslation), which translates them word by word.

Each list is the upstream wordfreq "small" list for that language — every word that occurs at least once per million tokens (frequency ≥ 10⁻⁶) — with noise removed up front: words written in a foreign script, pure numbers and template-digit tokens, possessive forms, and lone character tokens that are not words.

**Current revision: v4 (2026-10-12).** Cumulative across all revisions: 3,995 entries removed (1,870 numeric tokens from v3 + 2,125 non-word tokens from the v4 rules). See [Version history](#version-history).

> 中文版请见下方：[中文版说明](#zh)

## Files

```
├── README.md
├── clean.js                       # preprocessing script that regenerates data/ from raw wordfreq
├── gen_language_table.js          # regenerates the generated sections in this README
├── meta.json                      # dataset metadata (fields below)
├── files.json                     # per-file size (bytes) and SHA-256
└── data/
    └── small_<code>.msgpack.gz    # one file per language,
                                   # e.g. small_en.msgpack.gz, small_zh.msgpack.gz
```

`meta.json` records, per language: `total` (cumulative raw entries ever processed), `kept` (words in the current list), and `removed` (entries dropped, grouped by cleaning rule); the top level carries `version` and `generatedAt`. The identity `total = kept + Σremoved` holds for every language. Counts are cumulative across in-place revisions.

## Cleaning rules

- `numeric`: numeric words — pure digits and CJK numerals (`五百`, `二零一`), digit-led codes (`00k`, `1990s`, `3rd`), and numeric phrases (`百分之百`, `八成`, `第十`, `五点`)
- `digit_mix`: letters mixed with a multi-digit run or a decimal point — news-template noise (`a00`, `0.00pm`, `00x00`, `ال00`); single-digit product codes like `mp3`, `f1`, `b2b` are kept
- `possessive`: lowercase-led `'s` genitives (`women's`, `cnn's`) — contractions like `it's`/`who's` and capitalized genitives like `McDonald's` are kept
- `mark_only`: tokens made only of Unicode modifier letters (`ゝ`, `ヽ`, `ー`)
- `diacritic_single`: a lone non-ASCII Latin letter in a language where it isn't a word (`â`, `ó` in en/de/…) — languages where such singles ARE words (`fr es it pt ca da nb is sv vi`), ASCII singles (`a`, `i`), and Hungarian `ő` are kept (see `KEEP_DIACRITIC_SINGLE` in `clean.js`)
- `stroke_single`: lone CJK strokes (`丶`, `丨`, `丿`)
- `jamo_single`: lone Hangul jamo components (never standalone syllables)
- `foreign`, `pure_num`, `no_letter`: fallback rules — letters outside the language's Unicode-script whitelist, digits without letters, and tokens with neither letters nor digits (symbols, emoji)

**In-place revisions**: counts in `meta.json` are cumulative. When re-running on an already-cleaned list (input words ≤ previous `total`), the previous `removed` breakdown is merged in; when the input is fresh upstream data (input words > previous `total`), the counters restart from the new baseline instead of double-counting. Rule changes per revision are documented in [Version history](#version-history) and in `clean.js`.

## Regenerating

```bash
# raw input: wordfreq v3.0.2 small lists
# https://github.com/rspeer/wordfreq/tree/v3.0.2/wordfreq/data
npm install msgpack-lite
node clean.js --input <raw-wordfreq-data-dir> --output data
node gen_language_table.js
```

`clean.js` reads raw `small_<code>.msgpack.gz` files from the input directory, applies the cleaning rules, and writes cleaned `small_<code>.msgpack.gz` files plus `meta.json` (`--output` defaults to `data`). Pointing `--input` at an already-cleaned directory performs an in-place revision (previous counts are carried over).

## Vocabulary lists

Sorted by coverage (fraction of the language's word tokens found in this list). Coverage is computed on the raw (uncleaned) upstream corpus, so the stop-token exclusion — which removes the most frequent function words — accounts for most of the gap from 100%.

<!-- BEGIN GENERATED LANGUAGE TABLE -- run `node gen_language_table.js` -->
| code | language | native name | first word | cb | float | words | cumulative coverage |
|------|----------|-------------|------------|----|-------|-------|---------------------|
| ar | Arabic | العربية | في | 146 | 3.47e-2 | 55611 | 90.2% |
| bg | Bulgarian | български | на | 127 | 5.37e-2 | 35848 | 91.0% |
| bn | Bengali | বাংলা | না | 199 | 1.02e-2 | 33062 | 93.3% |
| ca | Catalan | català | de | 122 | 6.03e-2 | 27028 | 95.1% |
| cs | Czech | čeština | a | 149 | 3.24e-2 | 51744 | 89.9% |
| da | Danish | dansk | i | 151 | 3.09e-2 | 29321 | 93.2% |
| de | German | Deutsch | die | 152 | 3.02e-2 | 38989 | 90.4% |
| el | Greek | Ελληνικά | και | 149 | 3.24e-2 | 43191 | 89.7% |
| en | English | English | the | 127 | 5.37e-2 | 28223 | 93.5% |
| es | Spanish | español | de | 119 | 6.46e-2 | 34740 | 93.6% |
| fa | Persian | فارسی | و | 140 | 3.98e-2 | 30108 | 94.2% |
| fi | Finnish | suomi | ja | 144 | 3.63e-2 | 59143 | 88.7% |
| fil | Filipino | Filipino | sa | 113 | 7.41e-2 | 30098 | 95.2% |
| fr | French | français | de | 132 | 4.79e-2 | 31203 | 93.9% |
| he | Hebrew | עברית | את | 169 | 2.04e-2 | 57405 | 90.5% |
| hi | Hindi | हिन्दी | के | 142 | 3.80e-2 | 24031 | 93.2% |
| hu | Hungarian | magyar | a | 103 | 9.33e-2 | 46525 | 87.7% |
| id | Indonesian | Bahasa Indonesia | yang | 153 | 2.95e-2 | 30967 | 93.8% |
| is | Icelandic | íslenska | og | 132 | 4.79e-2 | 42207 | 91.6% |
| it | Italian | italiano | di | 141 | 3.89e-2 | 35954 | 93.6% |
| ja | Japanese | 日本語 | の | 128 | 5.25e-2 | 27856 | 91.4% |
| ko | Korean | 한국어 | 이 | 150 | 3.16e-2 | 26807 | 90.2% |
| lt | Lithuanian | lietuvių | ir | 148 | 3.31e-2 | 63973 | 87.4% |
| lv | Latvian | latviešu | un | 148 | 3.31e-2 | 45464 | 92.1% |
| mk | Macedonian | македонски | на | 123 | 5.89e-2 | 32925 | 93.9% |
| ms | Malay | Bahasa Melayu | yang | 150 | 3.16e-2 | 28571 | 95.9% |
| nb | Norwegian Bokmål | norsk bokmål | i | 152 | 3.02e-2 | 25994 | 94.0% |
| nl | Dutch | Nederlands | de | 127 | 5.37e-2 | 28715 | 93.5% |
| pl | Polish | polski | w | 145 | 3.55e-2 | 49664 | 91.6% |
| pt | Portuguese | português | de | 132 | 4.79e-2 | 33123 | 94.3% |
| ro | Romanian | română | de | 128 | 5.25e-2 | 43279 | 91.8% |
| ru | Russian | русский | в | 137 | 4.27e-2 | 59604 | 86.9% |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | je | 136 | 4.37e-2 | 54698 | 88.7% |
| sk | Slovak | slovenčina | a | 147 | 3.39e-2 | 59414 | 88.9% |
| sl | Slovenian | slovenščina | je | 133 | 4.68e-2 | 53882 | 90.6% |
| sv | Swedish | svenska | är | 148 | 3.31e-2 | 30515 | 94.0% |
| ta | Tamil | தமிழ் | ஒரு | 199 | 1.02e-2 | 64756 | 86.2% |
| th | Thai | ไทย | ที่ | 170 | 2.00e-2 | 39680 | 71.0% |
| tr | Turkish | Türkçe | ve | 163 | 2.34e-2 | 63130 | 86.9% |
| uk | Ukrainian | українська | в | 160 | 2.51e-2 | 46286 | 90.0% |
| ur | Urdu | اردو | کے | 137 | 4.27e-2 | 22442 | 96.0% |
| vi | Vietnamese | Tiếng Việt | là | 174 | 1.82e-2 | 10519 | 95.4% |
| zh | Chinese | 中文 | 的 | 121 | 6.17e-2 | 35723 | 90.7% |
| **total** | 43 languages | — | — | — | — | 1,712,418 | — |
<!-- END GENERATED LANGUAGE TABLE -->

*first word* is the most frequent word in the list — a quick sanity check that the file is in the right language. *cb* is the centibel band of that word (upstream stores each word's frequency rounded to the nearest centibel, so band *b* ≈ 10<sup>−b/100</sup> of tokens; *float* is that value for the top word). *words* is the list size after cleaning. *cumulative coverage* estimates the share of running words the list covers, summing 10<sup>−b/100</sup> over each band's word count — the shortfall from 100% is mostly the 10⁻⁶ entry cutoff. The **total** row sums the *words* column across all lists; the other columns are per-language facts and are not additive.

Language codes present in this dataset:

<!-- BEGIN GENERATED LANGUAGE LIST -- run `node gen_language_table.js` -->
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- fa
- fi
- fil
- fr
- he
- hi
- hu
- id
- is
- it
- ja
- ko
- lt
- lv
- mk
- ms
- nb
- nl
- pl
- pt
- ro
- ru
- sh
- sk
- sl
- sv
- ta
- th
- tr
- uk
- ur
- vi
- zh
<!-- END GENERATED LANGUAGE LIST -->

## Data format

Each file is a gzipped MessagePack array of `[word, rank, frequency]` triples, where rank is the 1-based position in the frequency-sorted list:

```python
import gzip, msgpack

with gzip.open('data/small_en.msgpack.gz', 'rb') as f:
    header, *bands = msgpack.unpackb(f.read())

# header == {'format': 'cB', 'version': 1}
# band b holds words whose frequency was rounded to centibel b (~10**(-b/100));
# bands concatenated in order yield words sorted by frequency rank.
words = [(w, 10 ** (-b / 100)) for b, band in enumerate(bands) for w in band]
# words[0] ≈ (b'the', 5.37e-2) — rank 1, ~5.4% of tokens
```

This is the upstream wordfreq "cBpack" encoding: 600 frequency bands per language, with each word's frequency rounded to the nearest centibel. For most applications you only need the rank (band order); the band-midpoint frequency is a tie-breaker and thresholding aid. Each file's size and SHA-256 are listed in `files.json`.

## Version history

- **v4** (2026-10-12): added cleaning rules `digit_mix`, `possessive`, `mark_only`, `diacritic_single`, `stroke_single`, `jamo_single`; `meta.json` counters became cumulative across in-place revisions (`total = kept + Σremoved`).
- **v3** (2026-10-10): added the `numeric` rule (digit-led codes, CJK numerals and numeric phrases are not headwords); `meta.json` reorganized as `languages[lang] = {total, removed, kept}`.
- **v1–v2**: initial releases of the wordfreq 3.0.2 small lists with Unicode-script whitelist cleaning (`foreign`, `pure_num`, `no_letter`).

## License

MIT

## About VocabRadar

This dataset is a **VocabRadar** project — the vocabulary radar. The
[VocabRadar browser extension](https://vocabradar.com) marks up the words you do not know
yet while you watch videos or browse the web: definitions in place, translation, bilingual
subtitles and annotated subtitles. Whatever you watched can go on to
[vocabradar.com](https://vocabradar.com), which turns it into related exercises and games
so the words actually stick.

---

<a id="zh"></a>

# 清洗版词频表（43 语）

43 种语言的小型词频表，源自 [wordfreq](https://github.com/rspeer/wordfreq) 3.0.2 并做了清洗，可直接当离线词频字典使用：每种语言一个 gzip 压缩的 MessagePack 文件，合计约 8 MB。这些词表也是 [vocabradar/WordTranslation](https://huggingface.co/datasets/vocabradar/WordTranslation) 的直接词表来源，后者逐词为它们配上译文。

每个文件都是该语种的 wordfreq "small" 列表 —— 即所有每百万词至少出现一次的词（词频 ≥ 10⁻⁶）—— 并在源头剔除了噪声：外文文字的词、纯数字与数字模板 token、属格形式、以及不成词的单字符 token。

**当前修订版：v4（2026-10-12）。** 跨全部修订累计剔除 3,995 条（v3 的 numeric 数字词 1,870 条 + v4 六类非词条 token 2,125 条）。见[版本历史](#版本历史)。

## 文件结构

```
├── README.md
├── clean.js                       # 预处理脚本：从原始 wordfreq 重新生成 data/
├── gen_language_table.js          # 重新生成本 README 中的生成段落
├── meta.json                      # 数据集元信息（字段见下）
├── files.json                     # 每个文件的大小（字节）与 SHA-256
└── data/
    └── small_<code>.msgpack.gz    # 每语种一个文件，
                                   # 如 small_en.msgpack.gz、small_zh.msgpack.gz
```

`meta.json` 按语种记录：`total`（累计处理的原始词条数）、`kept`（当前列表词数）、`removed`（按清洗规则分组的剔除数）；顶层含 `version` 与 `generatedAt`。所有语种满足恒等式 `total = kept + Σremoved`。计数为跨就地修订的累计值。

## 清洗规则

- `numeric`：数字词 —— 纯数字与中文数字（五百、二零一）、数字起头短代码（00k、1990s、3rd）、数字短语（百分之百、八成、第十、五点）
- `digit_mix`：字母与多位数字串或小数点混合的新闻模板噪声（a00、0.00pm、00x00、ال00）；`mp3`、`f1`、`b2b` 等单数字产品码保留
- `possessive`：小写起始的 's 属格（women's、cnn's）—— `it's`/`who's` 等缩合与 `McDonald's` 等大写属格保留
- `mark_only`：全部由 Unicode modifier letter（Lm）构成的 token（ゝ、ヽ、ー）
- `diacritic_single`：非豁免语种中单个注音拉丁字母（en/de 等语种的 â、ó）—— 单字成词语种（fr es it pt ca da nb is sv vi）、ASCII 单字母（a、i）与匈牙利语 ő 豁免（见 `clean.js` 的 `KEEP_DIACRITIC_SINGLE`）
- `stroke_single`：单个 CJK 笔画（丶、丨、丿）
- `jamo_single`：韩文单个字母部件（不成音节）
- `foreign`、`pure_num`、`no_letter`：兜底规则 —— 含语种文字白名单外字母、有数字无字母、以及既无字母也无数字（符号、emoji）的 token

**就地修订**：`meta.json` 的计数是累计值。对已清洗列表重跑（输入词数 ≤ 上版 `total`）时，上版 `removed` 明细会合并累计；输入为新上游原始数据（输入词数 > 上版 `total`）时，计数从新基线重新起算，避免重复计数。每版规则变化见下方[版本历史](#版本历史)与 `clean.js`。

## 重新生成

```bash
# raw input: wordfreq v3.0.2 small lists
# https://github.com/rspeer/wordfreq/tree/v3.0.2/wordfreq/data
npm install msgpack-lite
node clean.js --input <raw-wordfreq-data-dir> --output data
node gen_language_table.js
```

`clean.js` 读取输入目录中的原始 `small_<code>.msgpack.gz`，应用清洗规则，输出清洗后的 `small_<code>.msgpack.gz` 与 `meta.json`（`--output` 默认为 `data`）。把 `--input` 指向已清洗目录即为就地修订（自动携带上版统计）。

## 词表一览

按覆盖率排序（该语种词 token 中出现在本列表内的比例）。覆盖率在原始（未清洗）上游语料上计算，因此停用虚词排除 —— 它移除的正是最高频的功能词 —— 是距 100% 差距的主要来源。

<!-- BEGIN GENERATED LANGUAGE TABLE -- run `node gen_language_table.js` -->
| code | language | native name | first word | cb | float | words | cumulative coverage |
|------|----------|-------------|------------|----|-------|-------|---------------------|
| ar | Arabic | العربية | في | 146 | 3.47e-2 | 55611 | 90.2% |
| bg | Bulgarian | български | на | 127 | 5.37e-2 | 35848 | 91.0% |
| bn | Bengali | বাংলা | না | 199 | 1.02e-2 | 33062 | 93.3% |
| ca | Catalan | català | de | 122 | 6.03e-2 | 27028 | 95.1% |
| cs | Czech | čeština | a | 149 | 3.24e-2 | 51744 | 89.9% |
| da | Danish | dansk | i | 151 | 3.09e-2 | 29321 | 93.2% |
| de | German | Deutsch | die | 152 | 3.02e-2 | 38989 | 90.4% |
| el | Greek | Ελληνικά | και | 149 | 3.24e-2 | 43191 | 89.7% |
| en | English | English | the | 127 | 5.37e-2 | 28223 | 93.5% |
| es | Spanish | español | de | 119 | 6.46e-2 | 34740 | 93.6% |
| fa | Persian | فارسی | و | 140 | 3.98e-2 | 30108 | 94.2% |
| fi | Finnish | suomi | ja | 144 | 3.63e-2 | 59143 | 88.7% |
| fil | Filipino | Filipino | sa | 113 | 7.41e-2 | 30098 | 95.2% |
| fr | French | français | de | 132 | 4.79e-2 | 31203 | 93.9% |
| he | Hebrew | עברית | את | 169 | 2.04e-2 | 57405 | 90.5% |
| hi | Hindi | हिन्दी | के | 142 | 3.80e-2 | 24031 | 93.2% |
| hu | Hungarian | magyar | a | 103 | 9.33e-2 | 46525 | 87.7% |
| id | Indonesian | Bahasa Indonesia | yang | 153 | 2.95e-2 | 30967 | 93.8% |
| is | Icelandic | íslenska | og | 132 | 4.79e-2 | 42207 | 91.6% |
| it | Italian | italiano | di | 141 | 3.89e-2 | 35954 | 93.6% |
| ja | Japanese | 日本語 | の | 128 | 5.25e-2 | 27856 | 91.4% |
| ko | Korean | 한국어 | 이 | 150 | 3.16e-2 | 26807 | 90.2% |
| lt | Lithuanian | lietuvių | ir | 148 | 3.31e-2 | 63973 | 87.4% |
| lv | Latvian | latviešu | un | 148 | 3.31e-2 | 45464 | 92.1% |
| mk | Macedonian | македонски | на | 123 | 5.89e-2 | 32925 | 93.9% |
| ms | Malay | Bahasa Melayu | yang | 150 | 3.16e-2 | 28571 | 95.9% |
| nb | Norwegian Bokmål | norsk bokmål | i | 152 | 3.02e-2 | 25994 | 94.0% |
| nl | Dutch | Nederlands | de | 127 | 5.37e-2 | 28715 | 93.5% |
| pl | Polish | polski | w | 145 | 3.55e-2 | 49664 | 91.6% |
| pt | Portuguese | português | de | 132 | 4.79e-2 | 33123 | 94.3% |
| ro | Romanian | română | de | 128 | 5.25e-2 | 43279 | 91.8% |
| ru | Russian | русский | в | 137 | 4.27e-2 | 59604 | 86.9% |
| sh | Serbo-Croatian | srpskohrvatski / српскохрватски | je | 136 | 4.37e-2 | 54698 | 88.7% |
| sk | Slovak | slovenčina | a | 147 | 3.39e-2 | 59414 | 88.9% |
| sl | Slovenian | slovenščina | je | 133 | 4.68e-2 | 53882 | 90.6% |
| sv | Swedish | svenska | är | 148 | 3.31e-2 | 30515 | 94.0% |
| ta | Tamil | தமிழ் | ஒரு | 199 | 1.02e-2 | 64756 | 86.2% |
| th | Thai | ไทย | ที่ | 170 | 2.00e-2 | 39680 | 71.0% |
| tr | Turkish | Türkçe | ve | 163 | 2.34e-2 | 63130 | 86.9% |
| uk | Ukrainian | українська | в | 160 | 2.51e-2 | 46286 | 90.0% |
| ur | Urdu | اردو | کے | 137 | 4.27e-2 | 22442 | 96.0% |
| vi | Vietnamese | Tiếng Việt | là | 174 | 1.82e-2 | 10519 | 95.4% |
| zh | Chinese | 中文 | 的 | 121 | 6.17e-2 | 35723 | 90.7% |
| **合计** | 43 种语言 | — | — | — | — | 1,712,418 | — |
<!-- END GENERATED LANGUAGE TABLE -->

*first word* 是列表中最高频的词 —— 快速确认文件语言正确。*cb* 是该词所在的 centibel 频段（上游将词频四舍五入到整数 centibel，频段 *b* ≈ 10<sup>−b/100</sup> token 概率；*float* 即榜首词的该概率值）。*words* 是清洗后列表大小。*cumulative coverage* 按各频段词数 × 10<sup>−b/100</sup> 求和估算覆盖比例 —— 距 100% 的差主要是 10⁻⁶ 收录门槛。末行 **合计** 为各语种 *words* 之和；其余列是各语种的独立事实，不可相加。

本数据集包含的语种代码：

<!-- BEGIN GENERATED LANGUAGE LIST -- run `node gen_language_table.js` -->
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- fa
- fi
- fil
- fr
- he
- hi
- hu
- id
- is
- it
- ja
- ko
- lt
- lv
- mk
- ms
- nb
- nl
- pl
- pt
- ro
- ru
- sh
- sk
- sl
- sv
- ta
- th
- tr
- uk
- ur
- vi
- zh
<!-- END GENERATED LANGUAGE LIST -->

## 数据格式

每个文件是 gzip 压缩的 MessagePack 数组，沿用上游 wordfreq 的 cBpack 编码（与 `wordfreq` 库读取的文件相同，仅做了原地清洗）：结构为 `[header, band_0..band_599]`，频段 *b* 装有词频四舍五入到 *b* centibel 的词。

```python
import gzip, msgpack

with gzip.open('data/small_en.msgpack.gz', 'rb') as f:
    header, *bands = msgpack.unpackb(f.read())

# header == {'format': 'cB', 'version': 1}
# 频段 b 装有词频四舍五入到 b centibel 的词（约 10**(-b/100)）；
# 按顺序连接频段即得到按词频排序的词表。
words = [(w, 10 ** (-b / 100)) for b, band in enumerate(bands) for w in band]
# words[0] ≈ (b'the', 5.37e-2) —— 第 1 位，约占 token 的 5.4%
```

这是上游 wordfreq 的 "cBpack" 编码：每语种 600 个频段，词频四舍五入到最近的 centibel。多数场景只需排名（频段顺序）即可；频段中点概率（`10**(-b/100)`）供并列打破与阈值过滤使用。各文件的大小与 SHA-256 见 `files.json`。

## 版本历史

- **v4**（2026-10-12）：新增清洗规则 `digit_mix`、`possessive`、`mark_only`、`diacritic_single`、`stroke_single`、`jamo_single`；`meta.json` 计数改为跨就地修订累计（`total = kept + Σremoved`）。
- **v3**（2026-10-10）：新增 `numeric` 规则（数字起头代码、中文数字与数字短语不是词条）；`meta.json` 重组为 `languages[lang] = {total, removed, kept}`。
- **v1–v2**：初始发布 —— wordfreq 3.0.2 small 列表 + Unicode 文字白名单清洗（`foreign`、`pure_num`、`no_letter`）。

## 许可证

MIT

## 关于 VocabRadar

这项工作是 **VocabRadar**（词汇雷达）的工作：[VocabRadar 浏览器扩展](https://vocabradar.com)
让你在看视频、刷网页时把还不认识的生词就地标注出来 —— 释义、翻译、双语字幕、注释字幕；
看过的内容还能送到 [vocabradar.com](https://vocabradar.com)，自动生成相关习题与游戏，把词真正记住。
